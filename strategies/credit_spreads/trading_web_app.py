"""
NIFTY Options — Hedged Credit-Spread Paper Trading Dashboard
============================================================

Single-file Flask app.  Sells a strike and BUYS a wing `wing_width` points
further out-of-the-money (CE: K+W, PE: K-W), so every position is a defined-risk
credit spread instead of a naked short.

    python trading_web_app.py          ->  http://127.0.0.1:5000

Dependencies:  pip install flask requests
    (pandas / numpy / scipy are deliberately NOT used — the scrip master is
     parsed with the stdlib csv module and the normal CDF comes from math.erfc.
     That drops ~200 MB of wheels, cuts boot from ~15 s to ~2 s, and lets the
     app run inside a 512 MB hosted container.)

Credentials are never stored in this file.  Resolution order, highest first:
    DHAN_ACCESS_TOKEN env var  ->  DATA_DIR/runtime.json (the Settings tab)
    ->  config.py  ->  nothing.

Environment variables (all optional):
    DATA_DIR        where state lives          (default: ./data beside this file)
    DHAN_CLIENT_ID  Dhan client id
    APP_PASSWORD    login password             (required when bound publicly)
    SECRET_KEY      Flask session key          (default: generated + persisted)
    PORT / HOST     bind address               (default: 5000 / 127.0.0.1)
    APP_ENV=hosted  bind 0.0.0.0, require auth
    COOKIE_SECURE=1 set when served over HTTPS
    TRUST_PROXY=1   honour X-Forwarded-For (behind nginx/Caddy/Render)
"""

import atexit
import base64
import csv
import hashlib
import hmac
import io
import itertools
import json
import math
import os
import re
import secrets
import shutil
import signal
import sys
import tempfile
import threading
import time
import uuid
from collections import deque
from datetime import datetime, timedelta, timezone, time as dtime

import requests
from flask import (Flask, jsonify, request, Response, session, redirect,
                   url_for, render_template_string)

# ─────────────────────────────────────────────────────────────────────────────
#  CLOCK — India only.  A hosted box runs UTC; naive datetime.now() would put
#  every DTE and every trade timestamp up to 13.5 hours out.
# ─────────────────────────────────────────────────────────────────────────────
try:
    from zoneinfo import ZoneInfo
    IST = ZoneInfo("Asia/Kolkata")
except Exception:
    # No tzdata (bare Windows / pendrive).  India observes no DST, so a fixed
    # offset is exactly correct, not an approximation.
    IST = timezone(timedelta(hours=5, minutes=30), "IST")

YEAR_SECONDS = 365.0 * 24 * 3600


def now_ist():
    return datetime.now(IST)


def ts_now():
    return now_ist().strftime("%Y-%m-%d %H:%M:%S")


def expiry_dt(expiry):
    """'2026-11-23' -> 2026-11-23 15:30 IST, the NSE expiry cutoff."""
    y, m, d = (int(x) for x in str(expiry)[:10].split("-"))
    return datetime(y, m, d, 15, 30, tzinfo=IST)


def dte_of(expiry, now=None):
    delta = expiry_dt(expiry) - (now or now_ist())
    return int(math.floor(delta.total_seconds() / 86400.0))


def time_to_expiry(expiry, now=None):
    secs = (expiry_dt(expiry) - (now or now_ist())).total_seconds()
    return max(secs, 60.0) / YEAR_SECONDS


# ─────────────────────────────────────────────────────────────────────────────
#  PATHS
# ─────────────────────────────────────────────────────────────────────────────
APP_DIR = os.path.dirname(os.path.abspath(__file__))


def _env(name, default=None):
    v = os.environ.get(name)
    if v is None:
        return default
    v = v.strip()
    return v if v else default


DATA_DIR = _env("DATA_DIR") or os.path.join(APP_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

TRADES_FILE = os.path.join(DATA_DIR, "paper_trades.json")
RUNTIME_FILE = os.path.join(DATA_DIR, "runtime.json")
SECRET_FILE = os.path.join(DATA_DIR, "secret_key")
AUTH_FILE = os.path.join(DATA_DIR, "auth.json")
LOCK_FILE = os.path.join(DATA_DIR, "scanner.lock")
SCRIP_CACHE = os.path.join(DATA_DIR, "scrip_nifty.json")
HOLIDAY_FILE = os.path.join(DATA_DIR, "nse_holidays.json")
# The VIX kill-switch limit is shared by every strategy: set once in the hub.
VIX_SECURITY_ID, VIX_SEG = 21, "IDX_I"          # NSE "INDIA VIX", from the scrip master
DEFAULT_VIX_LIMIT = 13.5
RISK_FILE = _env("NIFTY_RISK_FILE") or os.path.join(
    os.path.dirname(os.path.dirname(APP_DIR)), "hub", "risk.json")
LEGACY_TRADES = os.path.join(os.path.expanduser("~"), "Trading", "Dhan_Algo",
                             "500_SP", "paper_trades.json")

SCHEMA_VERSION = 2
UNDERLYING_SYM = "NIFTY"
UNDERLYING_SCRIP = 13
UNDERLYING_SEG = "IDX_I"
EXCHANGE_SEGMENT = "NSE_FNO"
PRODUCT_TYPE = "MARGIN"
ORDER_TYPE = "LIMIT"
VALIDITY = "DAY"
STRIKE_GRID = 500
MAX_DEFERRALS = 20
SIDE_TO_TYPE = {"ce": "CALL", "pe": "PUT"}
TYPE_TO_SIDE = {"CALL": "ce", "PUT": "pe"}
GOOD_EXIT_SOURCES = ("ltp", "mid", "settled_intrinsic")

DEFAULT_FILTERS = {
    "min_eff": 50,
    "min_pop": 72,
    "dte_range": [45, 90],
    "ltp_range": [127, 1000],
    "exit_dte": 21,
    "wing_width": 500,
    "lots": 1,
    "min_credit": 0,
    "min_ror": 0,
    "min_spread_pop": 0,
}

# ─────────────────────────────────────────────────────────────────────────────
#  EVENT LOG — a ring buffer surfaced in the UI, so that after two days away he
#  can open the URL and see what the bot actually did.
# ─────────────────────────────────────────────────────────────────────────────
_events = deque(maxlen=800)
_events_lock = threading.Lock()
_event_seq = itertools.count(1)
_JWT_RE = re.compile(r"eyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]+")


def _scrub(text):
    return _JWT_RE.sub("<token-redacted>", str(text))


def log_event(kind, message):
    ev = {"id": next(_event_seq), "ts": ts_now(), "epoch": time.time(),
          "kind": kind, "msg": _scrub(message)[:400]}
    with _events_lock:
        _events.append(ev)
    print("[%s] %-9s %s" % (ev["ts"], kind.upper(), ev["msg"]), flush=True)


def recent_events(since_id=0, limit=250):
    with _events_lock:
        return [e for e in _events if e["id"] > since_id][-limit:]


# ─────────────────────────────────────────────────────────────────────────────
#  DURABLE JSON — the old code opened the live file in "w" mode, truncating the
#  entire trade book before writing a byte.  A power cut mid-write lost
#  everything, and load() swallowed the corruption and started empty.
# ─────────────────────────────────────────────────────────────────────────────
def write_json_atomic(path, obj, backups=3, private=False):
    folder = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(folder, exist_ok=True)
    payload = json.dumps(obj, indent=2, default=str).encode("utf-8")

    if backups and os.path.exists(path):
        try:
            for i in range(backups, 1, -1):
                newer = "%s.bak.%d" % (path, i - 1)
                if os.path.exists(newer):
                    os.replace(newer, "%s.bak.%d" % (path, i))
            shutil.copy2(path, path + ".bak.1")
        except OSError as e:
            log_event("error", "backup rotation failed for %s: %s"
                      % (os.path.basename(path), e))

    fd, tmp = tempfile.mkstemp(dir=folder, prefix=".tmp_", suffix=".json")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(payload)
            f.flush()
            os.fsync(f.fileno())
        if private and os.name != "nt":
            os.chmod(tmp, 0o600)
        os.replace(tmp, path)
        tmp = None
    finally:
        if tmp and os.path.exists(tmp):
            try:
                os.unlink(tmp)
            except OSError:
                pass


def read_json_safe(path, default=None):
    for cand in [path] + ["%s.bak.%d" % (path, i) for i in (1, 2, 3)]:
        if not os.path.exists(cand):
            continue
        try:
            with open(cand, "r", encoding="utf-8") as f:
                data = json.load(f)
            if cand != path:
                log_event("recover", "%s unreadable; recovered from %s"
                          % (os.path.basename(path), os.path.basename(cand)))
            return data
        except Exception as e:
            log_event("error", "unreadable %s: %s" % (os.path.basename(cand), e))
    return default


# ─────────────────────────────────────────────────────────────────────────────
#  CONFIG PRECEDENCE
# ─────────────────────────────────────────────────────────────────────────────
try:
    import config as _config
except Exception:
    _config = None


def _cfg(name):
    return getattr(_config, name, None) if _config is not None else None


_runtime_lock = threading.RLock()
_runtime_cache = None


def runtime_read():
    global _runtime_cache
    with _runtime_lock:
        if _runtime_cache is None:
            _runtime_cache = read_json_safe(RUNTIME_FILE, default={}) or {}
        return dict(_runtime_cache)


def runtime_write(**kw):
    global _runtime_cache
    with _runtime_lock:
        d = runtime_read()
        d.update(kw)
        write_json_atomic(RUNTIME_FILE, d, private=True)
        _runtime_cache = d
        return dict(d)


class Creds:
    __slots__ = ("client_id", "token", "source", "env_pinned")

    def __init__(self, client_id, token, source, env_pinned):
        self.client_id = client_id
        self.token = token
        self.source = source
        self.env_pinned = env_pinned


def resolve_credentials():
    """Re-read on every single API call.  Nothing about the token may be
    captured at import time — that is what makes 'paste a new token from your
    phone' work without a restart."""
    rt = runtime_read()
    token, source, pinned = _env("DHAN_ACCESS_TOKEN"), "environment", True
    if not token:
        pinned = False
        token, source = (rt.get("access_token") or "").strip(), "settings tab"
    if not token:
        token, source = (_cfg("ACCESS_TOKEN") or "").strip(), "config.py"
    if not token:
        source = "not configured"
    cid = (_env("DHAN_CLIENT_ID") or (rt.get("client_id") or "").strip()
           or str(_cfg("CLIENT_ID") or "").strip() or "")
    return Creds(str(cid), token or "", source, pinned)


# ─────────────────────────────────────────────────────────────────────────────
#  MATH
# ─────────────────────────────────────────────────────────────────────────────
def _f(x, d=0.0):
    """NaN/inf/None -> d.  Flask's jsonify happily emits a bare NaN token, which
    the browser's JSON.parse rejects — one bad quote used to kill a whole tab."""
    try:
        v = float(x)
        return d if (math.isnan(v) or math.isinf(v)) else v
    except (TypeError, ValueError):
        return d


def _ncdf(x):
    return 0.5 * math.erfc(-x / math.sqrt(2.0))


def calculate_pop_exact(fwd, strike, premium, T, sigma, opt_type):
    """Probability a short position with breakeven K±premium expires profitable,
    under the lognormal forward measure implied by the option prices.

    `premium` is the leg LTP for a naked short and the NET CREDIT for a spread —
    that single substitution is the whole difference between the two.

    Returns None when uncomputable.  The old code returned a fake 50.0, and for
    a put with breakeven <= 0 it returned NaN, which passed `pop < min_pop`
    (every comparison with NaN is False) and then broke the JSON response.
    """
    fwd, strike = _f(fwd), _f(strike)
    premium, T, sigma = _f(premium), _f(T), _f(sigma)
    if fwd <= 0 or strike <= 0 or T <= 0 or sigma <= 0 or premium <= 0:
        return None
    is_call = str(opt_type).lower() in ("ce", "call")
    be = strike + premium if is_call else strike - premium
    if be <= 0:
        return 100.0
    d2 = (math.log(fwd / be) - 0.5 * sigma * sigma * T) / (sigma * math.sqrt(T))
    pop = _ncdf(-d2) if is_call else _ncdf(d2)
    return max(0.0, min(100.0, pop * 100.0))


# ─────────────────────────────────────────────────────────────────────────────
#  TOKEN
# ─────────────────────────────────────────────────────────────────────────────
def decode_jwt_unverified(token):
    """Read the `exp` claim only.  Dhan authenticates the token; we just want to
    tell him when it dies.  Signature is deliberately not verified."""
    if not token:
        return None, "no token"
    parts = token.split(".")
    if len(parts) != 3:
        return None, "not a JWT"
    try:
        raw = parts[1].encode("ascii")
        raw += b"=" * (-len(raw) % 4)
        payload = json.loads(base64.urlsafe_b64decode(raw).decode("utf-8", "replace"))
    except Exception as e:
        return None, "undecodable payload (%s)" % e.__class__.__name__
    return (payload, None) if isinstance(payload, dict) else (None, "payload not an object")


def mask_token(token):
    if not token:
        return ""
    if len(token) <= 16:
        return "*" * len(token)
    return "%s...%s  (%d chars)" % (token[:8], token[-6:], len(token))


def _human_delta(seconds):
    seconds = int(seconds)
    if seconds <= 0:
        return "expired"
    h, rem = divmod(seconds, 3600)
    m = rem // 60
    if h >= 24:
        return "%dd %dh" % (h // 24, h % 24)
    return "%dh %dm" % (h, m)


class _TokenState:
    def __init__(self):
        self.lock = threading.Lock()
        self.reject_ts = 0.0
        self.reject_msg = ""

    def mark_rejected(self, msg):
        with self.lock:
            self.reject_ts, self.reject_msg = time.time(), str(msg)[:200]

    def mark_ok(self):
        with self.lock:
            self.reject_ts, self.reject_msg = 0.0, ""

    def snapshot(self):
        with self.lock:
            return self.reject_ts, self.reject_msg


TOKEN_STATE = _TokenState()


def token_status():
    """Safe to hand to the browser — never contains the raw token."""
    c = resolve_credentials()
    rej_ts, rej_msg = TOKEN_STATE.snapshot()
    out = {"configured": bool(c.token), "source": c.source,
           "env_pinned": c.env_pinned, "masked": mask_token(c.token),
           "client_id": c.client_id, "exp_ist": None, "expires_in": None,
           "human": "not configured", "expired": True, "warn": True,
           "rejected": bool(rej_ts), "rejected_msg": rej_msg,
           "saved_at": runtime_read().get("token_saved_at")}
    if not c.token:
        return out
    payload, err = decode_jwt_unverified(c.token)
    if err:
        out["human"] = "unreadable (%s)" % err
        return out
    exp = payload.get("exp")
    if not isinstance(exp, (int, float)):
        out.update(human="no exp claim", expired=False, warn=True)
        return out
    left = exp - time.time()
    out["exp_ist"] = datetime.fromtimestamp(exp, IST).strftime("%Y-%m-%d %H:%M IST")
    out["expires_in"] = int(left)
    out["expired"] = left <= 0
    out["warn"] = left < 2 * 3600
    out["human"] = ("EXPIRED %s ago" % _human_delta(-left)) if left <= 0 \
        else "expires in %s" % _human_delta(left)
    return out


# ─────────────────────────────────────────────────────────────────────────────
#  DHAN API
# ─────────────────────────────────────────────────────────────────────────────
DHAN_BASE = "https://api.dhan.co/v2"
_HTTP = requests.Session()
_HTTP.headers.update({"Accept": "application/json"})


def call_dhan(endpoint, payload=None, method="POST", timeout=20):
    """The old version returned r.json() without looking at the status code, so
    a 401 became a dict with no "status" key and every caller treated it as
    "no data".  He would watch a green RUNNING light for hours against a dead
    token and never be told."""
    c = resolve_credentials()
    if not c.token:
        return {"status": "error", "_http": 0,
                "message": "No Dhan access token. Open Settings and paste one."}
    headers = {"access-token": c.token, "client-id": c.client_id,
               "Content-Type": "application/json", "Accept": "application/json"}
    url = "%s/%s" % (DHAN_BASE, str(endpoint).lstrip("/"))
    try:
        if method.upper() == "GET":
            r = _HTTP.get(url, headers=headers, timeout=timeout)
        else:
            r = _HTTP.post(url, headers=headers, json=(payload or {}), timeout=timeout)
    except requests.RequestException as e:
        log_event("api_error", "%s: %s" % (endpoint, e.__class__.__name__))
        return {"status": "error", "_http": 0, "message": "network error: %s" % e}

    if r.status_code in (401, 403):
        TOKEN_STATE.mark_rejected("HTTP %d on %s" % (r.status_code, endpoint))
        log_event("token", "%s -> HTTP %d: broker rejected the token (source: %s)"
                  % (endpoint, r.status_code, c.source))
        return {"status": "error", "_http": r.status_code,
                "message": "Auth failed (HTTP %d). Token expired or revoked."
                           % r.status_code}
    if r.status_code == 429:
        log_event("api_error", "%s: HTTP 429 rate limited" % endpoint)
        return {"status": "error", "_http": 429, "message": "rate limited by Dhan"}
    try:
        data = r.json()
    except ValueError:
        log_event("api_error", "%s: HTTP %d non-JSON body" % (endpoint, r.status_code))
        return {"status": "error", "_http": r.status_code,
                "message": "HTTP %d, non-JSON response" % r.status_code}
    if not isinstance(data, dict):
        return {"status": "error", "_http": r.status_code, "message": "unexpected payload"}
    if r.status_code >= 400:
        # Dhan uses errorMessage, not message.  Reading the wrong key is why the
        # UI always showed a generic failure.
        msg = data.get("errorMessage") or data.get("message") or str(data)[:160]
        log_event("api_error", "%s: HTTP %d: %s" % (endpoint, r.status_code, msg))
        data.setdefault("status", "error")
        data["message"] = msg
    else:
        TOKEN_STATE.mark_ok()
    data["_http"] = r.status_code
    return data


def test_dhan_connection():
    t0 = time.time()
    res = call_dhan("optionchain/expirylist",
                    {"UnderlyingScrip": UNDERLYING_SCRIP, "UnderlyingSeg": UNDERLYING_SEG},
                    timeout=15)
    ms = int((time.time() - t0) * 1000)
    if res.get("status") == "success":
        n = len(res.get("data") or [])
        log_event("token", "connection test OK (%d ms, %d expiries)" % (ms, n))
        return {"ok": True, "ms": ms, "detail": "Dhan responded — %d expiries" % n,
                "token": token_status()}
    return {"ok": False, "ms": ms,
            "detail": _scrub(res.get("message") or "unknown failure"),
            "token": token_status()}


# ─────────────────────────────────────────────────────────────────────────────
#  OPTION CHAIN SNAPSHOT CACHE
#  Dhan throttles POST /v2/optionchain to roughly one request every 3 seconds.
#  The old code fired one call per expiry on every Positions refresh and one
#  call PER POSITION inside the exit loop, so a 3-expiry book rate-limited
#  itself; the rejections came back as empty price maps and every position
#  silently marked at its entry price, showing P&L of exactly Rs 0.00.
# ─────────────────────────────────────────────────────────────────────────────
def chain_index(oc):
    """Dhan keys the chain map as '25000.000000'.  str(float(25000)) is
    '25000.0', which never matched — the old ATM lookup always missed, so the
    synthetic forward silently collapsed to the ATM strike and every screener
    POP was computed off the wrong forward."""
    out = {}
    for k, v in (oc or {}).items():
        try:
            out[round(float(k), 2)] = v or {}
        except (TypeError, ValueError):
            continue
    return out


def quote_of(node):
    if not isinstance(node, dict):
        return None
    g = node.get("greeks") or {}
    oi, prev_oi = node.get("oi"), node.get("previous_oi")
    return {
        "ltp": _f(node.get("last_price")),
        "bid": _f(node.get("top_bid_price")),
        "ask": _f(node.get("top_ask_price")),
        "iv": _f(node.get("implied_volatility")) / 100.0,
        "delta": abs(_f(g.get("delta"))),
        "gamma": abs(_f(g.get("gamma"))),
        # A long vanilla's theta is <= 0.  Taking abs() per leg is harmless in a
        # one-leg ratio and fatal when netting two legs, so normalise here and
        # take the position sign from transaction_type instead.
        "theta": -abs(_f(g.get("theta"))),
        "vega": abs(_f(g.get("vega"))),
        "oi": _f(oi),
        "doi": (_f(oi) - _f(prev_oi)) if prev_oi is not None else None,
        "volume": _f(node.get("volume")),
    }


def node_at(snap, strike, side):
    row = snap["chain"].get(round(_f(strike), 2)) if snap else None
    return row.get(side) if row else None


class ChainCache:
    TTL = 20.0
    MIN_INTERVAL = 3.1

    def __init__(self):
        self._d = {}
        self._lock = threading.Lock()
        self._gate = threading.Lock()
        self._last = 0.0

    def _fetch(self, expiry):
        with self._gate:
            wait = self.MIN_INTERVAL - (time.time() - self._last)
            if wait > 0:
                time.sleep(wait)
            res = call_dhan("optionchain", {"UnderlyingScrip": UNDERLYING_SCRIP,
                                            "UnderlyingSeg": UNDERLYING_SEG,
                                            "Expiry": expiry})
            self._last = time.time()
        if res.get("status") != "success":
            return None
        d = res.get("data") or {}
        chain = chain_index(d.get("oc"))
        spot = _f(d.get("last_price"))
        if not chain or spot <= 0:
            return None
        atm = min(chain, key=lambda k: abs(k - spot))
        ce = quote_of(chain[atm].get("ce")) or {}
        pe = quote_of(chain[atm].get("pe")) or {}
        synth = atm + _f(ce.get("ltp")) - _f(pe.get("ltp"))
        return {"expiry": expiry, "spot": spot, "atm": atm,
                "synth": synth if synth > 0 else spot, "chain": chain,
                "T": time_to_expiry(expiry), "ts": time.time(), "stale": False}

    def get(self, expiry, ttl=None, force=False):
        ttl = self.TTL if ttl is None else ttl
        with self._lock:
            hit = self._d.get(expiry)
        if hit and not force and (time.time() - hit["ts"]) < ttl:
            return hit
        snap = self._fetch(expiry)
        if snap:
            with self._lock:
                self._d[expiry] = snap
            return snap
        # A stale snapshot is honest; a fabricated price is not.
        return dict(hit, stale=True) if hit else None


CHAINS = ChainCache()


def fetch_expiry_list():
    res = call_dhan("optionchain/expirylist",
                    {"UnderlyingScrip": UNDERLYING_SCRIP, "UnderlyingSeg": UNDERLYING_SEG})
    if res.get("status") == "success":
        return [str(x)[:10] for x in (res.get("data") or [])]
    return []


# ─────────────────────────────────────────────────────────────────────────────
#  SCRIP MASTER
#  Verified against the live 25.6 MB file: SM_SYMBOL_NAME is EMPTY for every NSE
#  row, so filtering on it yields zero NIFTY contracts.  The underlying has to
#  come from SEM_TRADING_SYMBOL ('NIFTY-Nov2026-18950-CE'), split on '-' and
#  compared exactly — a prefix test would also match NIFTYNXT50 and NIFTYFPI.
#  NIFTY's lot is 65 (all 4,000 rows); the old hardcoded fallback of 50 made
#  every rupee figure 30% wrong, so a missing mapping now rejects the trade.
# ─────────────────────────────────────────────────────────────────────────────
SCRIP_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"


def _parse_scrip_csv(text):
    lookup = {}
    reader = csv.DictReader(io.StringIO(text))
    for row in reader:
        if row.get("SEM_INSTRUMENT_NAME") != "OPTIDX":
            continue
        if row.get("SEM_EXM_EXCH_ID") != "NSE":
            continue
        tsym = (row.get("SEM_TRADING_SYMBOL") or "").strip()
        if tsym.split("-")[0] != UNDERLYING_SYM:
            continue
        try:
            strike = float(row["SEM_STRIKE_PRICE"])
            lot = int(float(row["SEM_LOT_UNITS"]))
        except (TypeError, ValueError, KeyError):
            continue
        if lot <= 0:
            continue
        expiry = (row.get("SEM_EXPIRY_DATE") or "")[:10]
        opt = "CALL" if row.get("SEM_OPTION_TYPE") == "CE" else "PUT"
        lookup["%s_%.1f_%s" % (expiry, strike, opt)] = {
            "sec_id": str(row.get("SEM_SMST_SECURITY_ID", "")).strip(),
            "lot": lot,
            "tsym": tsym,
        }
    return lookup


def load_scrip_lookup():
    """Cached to disk for the day.  The old code re-downloaded and pandas-parsed
    25.6 MB on every process start, then swallowed any failure into {} — after
    which every mapping missed and every position booked at the wrong lot."""
    today = now_ist().strftime("%Y-%m-%d")
    cached = read_json_safe(SCRIP_CACHE, default=None)
    if isinstance(cached, dict) and cached.get("date") == today and cached.get("map"):
        log_event("boot", "scrip master from cache: %d NIFTY contracts"
                  % len(cached["map"]))
        return cached["map"]
    try:
        t0 = time.time()
        r = requests.get(SCRIP_URL, timeout=120)
        r.raise_for_status()
        lookup = _parse_scrip_csv(r.text)
        if not lookup:
            raise ValueError("no NIFTY OPTIDX rows found in the scrip master")
        write_json_atomic(SCRIP_CACHE, {"date": today, "map": lookup}, backups=1)
        log_event("boot", "scrip master downloaded: %d NIFTY contracts in %.1fs"
                  % (len(lookup), time.time() - t0))
        return lookup
    except Exception as e:
        log_event("error", "scrip master download failed: %s" % e)
        if isinstance(cached, dict) and cached.get("map"):
            log_event("boot", "falling back to yesterday's scrip cache (%d contracts)"
                      % len(cached["map"]))
            return cached["map"]
        return {}


def get_mapping(expiry, strike, opt_type):
    t = "CALL" if str(opt_type).upper() in ("CE", "CALL") else "PUT"
    return STATE.scrip_lookup.get("%s_%.1f_%s" % (str(expiry)[:10], float(strike), t))


# ─────────────────────────────────────────────────────────────────────────────
#  SPREAD SCHEMA
#
#  A short vertical IS a short position in the synthetic instrument
#      V = P_short - P_wing,   opened at   V = net credit.
#  Everything falls out of that one identity:
#      MTM P&L   = (net_credit - V_now) * qty
#      breakeven = K +/- net_credit
#      max profit= net_credit * qty          max loss = (width - credit) * qty
#      spread POP= the same d2 function, fed the credit instead of the leg LTP
#  A legacy naked short is the degenerate case where the wing price is zero.
# ─────────────────────────────────────────────────────────────────────────────
def leg_sign(leg):
    return -1.0 if str(leg.get("transaction_type", "SELL")).upper() == "SELL" else 1.0


def short_leg(pos):
    return next((l for l in pos.get("legs", []) if l.get("role") == "SHORT"), None)


def wing_leg(pos):
    return next((l for l in pos.get("legs", []) if l.get("role") == "WING"), None)


def legs_exit_order(pos):
    return sorted(pos.get("legs", []), key=lambda l: l.get("sequence_exit", 9))


def make_leg(role, expiry, strike, opt_type, mapping, lots, q, ts):
    """Every field above entry_quote is verbatim what Dhan's POST /v2/orders
    wants.  Going live later means replacing the PAPER fill lines with a real
    order call — not a schema migration."""
    txn = "SELL" if role == "SHORT" else "BUY"
    lot = int(mapping["lot"])
    qty = lot * int(lots)
    return {
        "role": role,
        "transaction_type": txn,
        "exit_transaction_type": "BUY" if txn == "SELL" else "SELL",
        "security_id": str(mapping["sec_id"]),
        "exchange_segment": EXCHANGE_SEGMENT,
        "product_type": PRODUCT_TYPE,
        "order_type": ORDER_TYPE,
        "validity": VALIDITY,
        "drv_expiry_date": expiry,
        "drv_option_type": opt_type,
        "drv_strike_price": float(strike),
        "trading_symbol": mapping.get("tsym") or "%s %s %d %s" % (
            UNDERLYING_SYM, expiry, int(strike), opt_type),
        "lot_size": lot, "lots": int(lots), "quantity": qty,
        # Buy the wing FIRST on the way in, buy the short back FIRST on the way
        # out.  Either order leaves us never momentarily naked.
        "sequence_entry": 1 if role == "WING" else 2,
        "sequence_exit": 1 if role == "SHORT" else 2,
        "entry_quote": round(q["ltp"], 2),
        "entry_bid": round(q["bid"], 2),
        "entry_ask": round(q["ask"], 2),
        "entry_fill_price": round(q["ltp"], 2),
        "entry_filled_qty": qty,
        "entry_order_id": None,
        "entry_order_status": "PAPER_FILLED",
        "entry_time": ts,
        "entry_iv": round(q["iv"] * 100.0, 2),
        "entry_greeks": {"delta": round(q["delta"], 4), "gamma": round(q["gamma"], 7),
                         "theta": round(q["theta"], 3), "vega": round(q["vega"], 2)},
        "exit_quote": None, "exit_fill_price": None, "exit_price_source": None,
        "exit_filled_qty": 0, "exit_order_id": None, "exit_order_status": None,
        "exit_time": None,
        "last_mark": round(q["ltp"], 2), "last_mark_source": "ltp",
    }


def mirror_legacy_keys(pos):
    """Entry_Price mirrors the NET CREDIT (not the short leg's premium), so the
    untouched old formula (Entry_Price - Exit_price) * Qty yields the correct
    spread P&L.  Any call site missed during the rewrite stays benign."""
    sl = short_leg(pos)
    pos["Strike"] = pos.get("Short_Strike")
    pos["Entry_Price"] = pos.get("Net_Credit")
    pos["SecurityID"] = sl["security_id"] if sl else "N/A"
    pos["Time"] = pos.get("Entry_Time")
    pos["DTE"] = pos.get("Entry_DTE")
    if pos.get("Net_Exit_Debit") is not None:
        pos["Exit_price"] = pos["Net_Exit_Debit"]
        pos["Exit_time"] = pos.get("Exit_Time")
    return pos


def make_spread_position(m, lots=1):
    ts = ts_now()
    lot = int(m["Lot_Size"])
    lots = max(1, int(lots or 1))
    qty = lot * lots
    pos = {
        "schema": SCHEMA_VERSION, "id": uuid.uuid4().hex[:16],
        "Structure": "CREDIT_SPREAD",
        "Strategy": "BEAR_CALL_SPREAD" if m["Type"] == "CALL" else "BULL_PUT_SPREAD",
        "Order_Mode": "PAPER", "Status": "OPEN",
        "Underlying": UNDERLYING_SYM,
        "Expiry": m["Expiry"], "Type": m["Type"],
        "Short_Strike": m["Short_Strike"], "Long_Strike": m["Long_Strike"],
        "Wing_Width": m["Wing_Width"],
        "Lot_Size": lot, "Lots": lots, "Qty": qty,
        "Entry_Time": ts, "Entry_DTE": m["DTE"],
        "Entry_Spot": m["Spot"], "Entry_Synth": m["Synth"],
        "Net_Credit": m["Net_Credit"],
        "Credit_Received": round(m["Net_Credit"] * qty, 2),
        "Max_Profit": round(m["Net_Credit"] * qty, 2),
        "Max_Loss": round((m["Wing_Width"] - m["Net_Credit"]) * qty, 2),
        "Return_On_Risk": m["ROR"], "Breakeven": m["Breakeven"],
        "POP": m["Spread_POP"], "Short_POP": m["Short_POP"],
        "Efficiency": m["Efficiency"], "Spread_Efficiency": m["Spread_Efficiency"],
        "Net_Delta": m["Net_Delta"], "Net_Theta": m["Net_Theta"],
        "Net_Gamma": m["Net_Gamma"], "Net_Vega": m["Net_Vega"],
        "Label": m["Label"],
        "legs": [
            make_leg("WING", m["Expiry"], m["Long_Strike"], m["Type"],
                     m["Long_Map"], lots, m["Long_Q"], ts),
            make_leg("SHORT", m["Expiry"], m["Short_Strike"], m["Type"],
                     m["Short_Map"], lots, m["Short_Q"], ts),
        ],
        "Defer_Count": 0, "Exit_Time": None, "Exit_Reason": None,
        "Net_Exit_Debit": None, "Realized_PnL": None,
    }
    return mirror_legacy_keys(pos)


def legacy_id(p):
    raw = "%s|%s|%s|%s|%s" % (p.get("Time"), p.get("Expiry"), p.get("Strike"),
                              p.get("Type"), p.get("Exit_time"))
    return "lg" + hashlib.md5(raw.encode()).hexdigest()[:14]


def upgrade_record(p):
    """His existing paper_trades.json is full of single-leg records.  Migrate in
    memory so both shapes render; never rewrite his history in place."""
    if not isinstance(p, dict):
        return None
    if p.get("legs"):
        p.setdefault("schema", SCHEMA_VERSION)
        p.setdefault("id", uuid.uuid4().hex[:16])
        return p
    K = _f(p.get("Strike"))
    typ = "CALL" if str(p.get("Type") or "CALL").upper() in ("CALL", "CE") else "PUT"
    qty = int(_f(p.get("Qty"), 65) or 65)
    entry = _f(p.get("Entry_Price"))
    ts = p.get("Time") or ""
    leg = {
        "role": "SHORT", "transaction_type": "SELL", "exit_transaction_type": "BUY",
        "security_id": str(p.get("SecurityID", "N/A")),
        "exchange_segment": EXCHANGE_SEGMENT, "product_type": PRODUCT_TYPE,
        "order_type": ORDER_TYPE, "validity": VALIDITY,
        "drv_expiry_date": p.get("Expiry"), "drv_option_type": typ,
        "drv_strike_price": K,
        "trading_symbol": "%s %s %d %s" % (UNDERLYING_SYM, p.get("Expiry"), int(K), typ),
        "lot_size": qty, "lots": 1, "quantity": qty,
        "sequence_entry": 1, "sequence_exit": 1,
        "entry_quote": entry, "entry_bid": 0.0, "entry_ask": 0.0,
        "entry_fill_price": entry, "entry_filled_qty": qty,
        "entry_order_id": None, "entry_order_status": "LEGACY", "entry_time": ts,
        "entry_iv": None, "entry_greeks": {},
        "exit_quote": p.get("Exit_price"), "exit_fill_price": p.get("Exit_price"),
        "exit_price_source": "legacy" if p.get("Exit_price") is not None else None,
        "exit_filled_qty": qty if p.get("Exit_price") is not None else 0,
        "exit_order_id": None, "exit_order_status": None,
        "exit_time": p.get("Exit_time"),
        "last_mark": entry, "last_mark_source": "legacy",
    }
    out = dict(p)
    out.update({
        "schema": SCHEMA_VERSION, "id": p.get("id") or legacy_id(p),
        "Structure": "SINGLE", "Strategy": "NAKED_SHORT", "Order_Mode": "PAPER",
        "Underlying": UNDERLYING_SYM, "Type": typ,
        "Short_Strike": K, "Long_Strike": None, "Wing_Width": 0.0,
        "Lot_Size": qty, "Lots": 1, "Qty": qty,
        "Entry_Time": ts, "Entry_DTE": p.get("DTE"),
        "Status": p.get("Status", "OPEN"),
        "Net_Credit": entry, "Credit_Received": round(entry * qty, 2),
        "Max_Profit": round(entry * qty, 2),
        # A naked short call has unbounded risk; the UI shows it as such rather
        # than quietly understating the book's total.
        "Max_Loss": None if typ == "CALL" else round(max(0.0, K - entry) * qty, 2),
        "Return_On_Risk": None,
        "Breakeven": round(K + entry if typ == "CALL" else K - entry, 2),
        "POP": _f(str(p.get("POP", "")).rstrip("%")) or None,
        "Short_POP": _f(str(p.get("POP", "")).rstrip("%")) or None,
        "Spread_Efficiency": None, "Defer_Count": 0,
        "Net_Delta": 0.0, "Net_Theta": 0.0, "Net_Gamma": 0.0, "Net_Vega": 0.0,
        "Label": "%d %s (naked)" % (int(K), typ),
        "legs": [leg],
        "Exit_Time": p.get("Exit_time"), "Net_Exit_Debit": p.get("Exit_price"),
        "Realized_PnL": (round((entry - _f(p.get("Exit_price"))) * qty, 2)
                         if p.get("Exit_price") is not None else None),
    })
    return out


# ─────────────────────────────────────────────────────────────────────────────
#  MARGIN  —  what this spread actually blocks in the Dhan account
#
#  Two tiers, and the UI must always say which one it is showing:
#    tier 1  estimate  local arithmetic, zero network, every screener row
#    tier 2  live      ONE POST to margincalculator/multi with BOTH legs,
#                      fired only for the row he clicks / deploys / refreshes
#
#  NEVER call margincalculator once per leg and add the two totals.  SPAN nets
#  the legs; summing them prices a naked short and overstates a 500-wide NIFTY
#  spread by roughly 4x.
#
#  Exchange parameters (NSE Clearing / SEBI, checked Sep-2026).  If SEBI ships
#  the proposed 44-scenario SPAN with ELM = PSR/10, only these three change.
# ─────────────────────────────────────────────────────────────────────────────
#  CALIBRATION.  These were first derived from published exchange percentages and
#  were BOTH wrong.  They are now fitted to a real Dhan basket quote:
#      NIFTY 29-Sep-2026,  SELL 23500 CE / BUY 24000 CE,  65 x 1,  spot ~23,260
#          Dhan overall (un-netted)  Rs 1,48,009.55   -> naked short leg Rs 1,46,518
#          Dhan final   (netted)     Rs    62,847.72
#          Dhan hedge benefit        Rs    84,640.40
#  giving exposure ~2.47% of notional and a naked short ~9.69% of notional.
#  This is ONE observation, so the estimate is still only +/-15% - the live quote
#  from margincalculator/multi is the number to trust.
ELM_INDEX_PCT        = 0.0247  # exposure margin, % of SHORT leg notional. NOT netted by the hedge.
ELM_EXPIRY_EXTRA_PCT = 0.02    # extra ELM on short index options ON expiry day (SEBI, 21-Nov-2024)
NAKED_SHORT_PCT      = 0.0969  # SPAN+exposure for a near-ATM naked index short, % of notional
MARGIN_TTL_SEC       = 120.0   # Dhan: "indicative and valid only for the current trading session"
MARGIN_API_COOLDOWN  = 900.0   # stop hammering a margin endpoint this build cannot speak to

_MARGIN_CACHE = {}
_MARGIN_LOCK  = threading.Lock()
_MARGIN_API_DEAD = [0.0]       # epoch until which we stop retrying a broken endpoint


def _margin_inputs(obj):
    """Accept EITHER a screener candidate (Short_Strike/Long_Strike/Short_LTP/...)
    OR an open paper position (legs[] with role SHORT/WING).  Returns the numbers
    both tiers need, or None if the row is not a two-leg vertical."""
    if not isinstance(obj, dict):
        return None
    typ = "CALL" if str(obj.get("Type") or "CALL").upper() in ("CALL", "CE") else "PUT"
    expiry = str(obj.get("Expiry") or "")[:10]
    legs = obj.get("legs") or []
    if legs:
        sl, wl = short_leg(obj), wing_leg(obj)
        if not sl or not wl:
            return None                      # legacy single-leg record: no spread margin
        k   = _f(sl.get("drv_strike_price"))
        wk  = _f(wl.get("drv_strike_price"))
        sp  = _f(sl.get("last_mark"), _f(sl.get("entry_fill_price")))
        lp  = _f(wl.get("last_mark"), _f(wl.get("entry_fill_price")))
        qty = int(_f(sl.get("quantity"), 0))
        s_id, l_id = str(sl.get("security_id") or ""), str(wl.get("security_id") or "")
        prod = sl.get("product_type") or PRODUCT_TYPE
        spot = _f(obj.get("Entry_Spot"))
    else:
        k   = _f(obj.get("Short_Strike"))
        wk  = _f(obj.get("Long_Strike"))
        sp  = _f(obj.get("Short_LTP"))
        lp  = _f(obj.get("Long_LTP"))
        qty = int(_f(obj.get("Qty"), 0))
        # Short_Map/Long_Map are stripped by public_match() before the row reaches
        # the browser, so re-resolve from the scrip master when they are absent.
        sm = obj.get("Short_Map") or get_mapping(expiry, k, typ) or {}
        lm = obj.get("Long_Map")  or get_mapping(expiry, wk, typ) or {}
        s_id, l_id = str(sm.get("sec_id") or ""), str(lm.get("sec_id") or "")
        prod = PRODUCT_TYPE
        spot = _f(obj.get("Spot"))
    if qty <= 0 or k <= 0 or wk <= 0:
        return None
    if spot <= 0:
        spot = k                             # ~0.1% error on the ELM term; never fatal
    return {"typ": typ, "expiry": expiry, "k": k, "wk": wk, "short_px": sp,
            "long_px": lp, "qty": qty, "spot": spot, "prod": prod,
            "short_id": s_id, "long_id": l_id}


def _is_expiry_day(expiry):
    try:
        return str(expiry)[:10] == now_ist().strftime("%Y-%m-%d")
    except Exception:
        return False


def estimate_spread_margin(d):
    """No network.  margin = SPAN + exposure, where the wing caps SPAN at the
    spread's own max loss and the exposure term is charged on the SHORT leg's
    notional and is NOT netted by the hedge.

    Max loss alone is not a proxy: on the calibrating basket it was Rs 25,506
    against a real Rs 62,848, because the un-netted exposure term is the larger
    of the two.  An earlier version modelled SPAN as a fraction of max loss and
    came out 11% low; the fitted form below reproduces the observed quote to
    within 1%."""
    width    = abs(d["wk"] - d["k"])
    credit   = d["short_px"] - d["long_px"]
    max_loss = max(width - credit, 0.0) * d["qty"]
    span     = max_loss
    notional = d["spot"] * d["qty"]
    elm      = ELM_INDEX_PCT * notional
    expiry_day = _is_expiry_day(d["expiry"])
    if expiry_day:
        elm += ELM_EXPIRY_EXTRA_PCT * notional       # levied even on a hedged position
    naked  = NAKED_SHORT_PCT * notional
    margin = min(max(span + elm, max_loss), naked)   # never below own max loss, never above naked
    note = "Estimate (approx +/-15%) — not a broker quote. Click for Dhan's figure."
    if expiry_day:
        note += " Expiry day: extra 2% exposure included."
    return {
        "margin": round(margin, 2),
        "source": "estimate",
        "note": note,
        "low": round(margin * 0.85, 2), "high": round(margin * 1.15, 2),
        "span": round(span, 2), "elm": round(elm, 2),
        "max_loss": round(max_loss, 2),
        "credit_received": round(credit * d["qty"], 2),
        "naked_equivalent": round(naked, 2),
        "hedge_benefit": round(naked - margin, 2),
        "roi_on_margin": (round(100.0 * credit * d["qty"] / margin, 2)
                          if margin > 0 else 0.0),
        "expiry_day": expiry_day,
        "as_of": ts_now(),
    }


def _leg_scrip(d, which):
    return {
        "exchangeSegment": EXCHANGE_SEGMENT,
        "transactionType": "SELL" if which == "short" else "BUY",
        "quantity": int(d["qty"]),                 # ABSOLUTE qty (65), never lots
        "productType": d["prod"],                  # MARGIN = Dhan's carry-forward F&O; NRML is not a v2 value
        "securityId": d["short_id"] if which == "short" else d["long_id"],
        "price": float(d["short_px"] if which == "short" else d["long_px"]),
        "triggerPrice": 0,
    }


def _mf(v, default=None):
    """margincalculator/multi returns STRINGS ("150000.00"), the single-order
    endpoint returns floats, and hedge_benefit can be "".  Never raise, and
    never turn an unknown into a zero."""
    if v is None or v == "":
        return default
    try:
        f = float(v)
        return default if (math.isnan(f) or math.isinf(f)) else f
    except (TypeError, ValueError):
        return default


def live_spread_margin(d, include_position=False):
    """ONE basket call for the whole spread, so the exchange's hedge offset is
    applied.  Dhan's docs print this body two ways — the cURL block uses
    scripList/includeOrder, the prose block uses scripts/includeOrders — so try
    each spelling once and keep whichever the server accepts.  Returns None on
    any failure; the caller falls back to the estimate."""
    if not d["short_id"] or not d["long_id"]:
        return None
    c = resolve_credentials()
    if not c.token:
        return None
    if time.time() < _MARGIN_API_DEAD[0]:
        return None                            # endpoint rejected us recently
    scrips = [_leg_scrip(d, "short"), _leg_scrip(d, "long")]
    bodies = [
        {"dhanClientId": str(c.client_id), "includePosition": bool(include_position),
         "includeOrder": False, "scripList": scrips},
        {"dhanClientId": str(c.client_id), "includePosition": bool(include_position),
         "includeOrders": False, "scripts": scrips},
    ]
    for body in bodies:
        r = call_dhan("margincalculator/multi", body) or {}
        http = r.get("_http", 0)
        if http in (0, 401, 403, 429):
            log_event("margin", "live margin unavailable (HTTP %s) — showing estimate" % http)
            return None                        # network/auth/rate-limit: retrying is pointless
        total = _mf(r.get("total_margin", r.get("totalMargin")))
        if http < 400 and total is not None:
            return {
                "margin": round(total, 2),
                "source": "dhan",
                "note": "Dhan quote — indicative, valid for this trading session only.",
                "span": _mf(r.get("span_margin", r.get("spanMargin"))),
                "elm": _mf(r.get("exposure_margin", r.get("exposureMargin"))),
                "fo_margin": _mf(r.get("fo_margin")),
                # blank in Dhan's own example = UNKNOWN, not "no benefit". Do not render 0.
                "hedge_benefit": _mf(r.get("hedge_benefit")),
                "as_of": ts_now(),
            }
    _MARGIN_API_DEAD[0] = time.time() + MARGIN_API_COOLDOWN
    log_event("margin", "margincalculator/multi rejected both field spellings - "
                        "falling back to estimates for %d min"
                        % int(MARGIN_API_COOLDOWN / 60))
    return None


def spread_margin(obj, live=False, include_position=False):
    """The one entry point.  Screener rows call it with live=False (zero network,
    every row).  A clicked row / deploy preview / positions refresh calls it with
    live=True (one cached basket call).  Always returns a dict carrying margin,
    source and note — never None, never a blank cell."""
    d = _margin_inputs(obj)
    if not d:
        return {"margin": None, "source": "unavailable", "as_of": ts_now(),
                "note": "Not a two-leg vertical — no spread margin."}

    est = estimate_spread_margin(d)
    if not live:
        return est

    key = (d["short_id"], d["long_id"], d["qty"], d["prod"], bool(include_position))
    now = time.time()
    with _MARGIN_LOCK:
        hit = _MARGIN_CACHE.get(key)
        if hit and hit[0] > now:
            return hit[1]

    try:
        out = live_spread_margin(d, include_position)
    except Exception as e:                     # a margin cell must never break the page
        log_event("margin", "live margin failed: %s" % e.__class__.__name__)
        out = None

    if out is None:                            # degrade, do not cache the failure
        out = dict(est)
        out["note"] = est["note"] + " Live quote unavailable."
        return out

    for f in ("max_loss", "credit_received", "naked_equivalent", "expiry_day"):
        out.setdefault(f, est.get(f))
    out["estimate"] = est["margin"]
    if out["margin"] > 0:
        out["roi_on_margin"] = round(100.0 * est["credit_received"] / out["margin"], 2)
    if est["expiry_day"]:
        out["note"] += " Expiry day: extra 2% ELM applies."
    with _MARGIN_LOCK:
        _MARGIN_CACHE[key] = (now + MARGIN_TTL_SEC, out)
    return out


# ─────────────────────────────────────────────────────────────────────────────
#  STATE
# ─────────────────────────────────────────────────────────────────────────────
class AppState:
    def __init__(self):
        self.lock = threading.RLock()
        self.paper_positions = []
        self.trade_history = []
        self.pnl_series = []
        self.scanning_active = False
        # Launched = scanning.  Set at boot by the scanner owner; the scanner
        # loop turns scanning on as soon as it can (token configured and not
        # expired) and clears it.  Stop clears it too.  Never persisted.
        self.autostart = False
        self.force_scan = False
        self.scanner_owner = False
        self.scrip_lookup = {}
        self.expiry_list = []
        self.expiry_fetched = 0.0
        self.last_scan_time = "Never"
        self.status_message = "Starting up..."
        self.market_note = ""
        self.last_scan = {}
        self.last_rejects = {}
        self.filters = dict(DEFAULT_FILTERS)
        # VIX kill switch (see vix_guard).  Live values, never persisted.
        self.vix = None
        self.vix_at = ""
        self.vix_limit = DEFAULT_VIX_LIMIT
        self.vix_kill_on = False
        self.vix_note = "not checked yet"
        self.load()

    def save(self):
        write_json_atomic(TRADES_FILE, {
            "schema_version": SCHEMA_VERSION,
            "saved_at": ts_now(),
            "paper_positions": self.paper_positions,
            "trade_history": self.trade_history,
            "pnl_series": self.pnl_series[-3000:],
            "filters": self.filters,
            "scanning_active": self.scanning_active,
            "force_scan": self.force_scan,
        })

    def load(self):
        if not os.path.exists(TRADES_FILE) and os.path.exists(LEGACY_TRADES):
            try:
                shutil.copy2(LEGACY_TRADES, TRADES_FILE)
                log_event("boot", "migrated legacy state from %s" % LEGACY_TRADES)
            except OSError as e:
                log_event("error", "legacy migration failed: %s" % e)
        d = read_json_safe(TRADES_FILE, default=None)
        if not isinstance(d, dict):
            return
        if int(_f(d.get("schema_version"), 1)) < SCHEMA_VERSION and os.path.exists(TRADES_FILE):
            try:
                shutil.copy2(TRADES_FILE, TRADES_FILE +
                             now_ist().strftime(".bak-%Y%m%d-%H%M%S"))
                log_event("boot", "backed up v1 state before migrating to v2")
            except OSError:
                pass
        self.paper_positions = [r for r in (upgrade_record(x)
                                            for x in (d.get("paper_positions") or [])) if r]
        self.trade_history = [r for r in (upgrade_record(x)
                                          for x in (d.get("trade_history") or [])) if r]
        self.pnl_series = d.get("pnl_series") or []
        if isinstance(d.get("filters"), dict):
            self.filters.update({k: v for k, v in d["filters"].items()
                                 if k in DEFAULT_FILTERS})
        self.scanning_active = bool(d.get("scanning_active", False))
        self.force_scan = bool(d.get("force_scan", False))
        log_event("boot", "loaded %d open, %d closed"
                  % (len(self.paper_positions), len(self.trade_history)))


STATE = AppState()


# ─────────────────────────────────────────────────────────────────────────────
#  SCREENER — the four original gates still decide the SHORT leg, untouched.
#  The wing is an additive layer applied only after a candidate has passed.
# ─────────────────────────────────────────────────────────────────────────────
def resolve_wing(snap, side, k, width):
    """Exact width or no trade.  Substituting a wider wing would raise max loss
    far above the risk he approved while still being labelled the same."""
    wk = k + width if side == "ce" else k - width
    if wk <= 0:
        return None, None, "wing_off_grid"
    node = node_at(snap, wk, side)
    if node is None:
        return None, None, "wing_strike_absent"
    q = quote_of(node)
    if not q or q["ltp"] <= 0:
        return None, None, "wing_unpriced"
    return wk, q, None


def build_spread_candidate(f, exp, dte, snap, k, side, s_q, short_pop, eff):
    opt_type = SIDE_TO_TYPE[side]
    width = _f(f.get("wing_width"), float(STRIKE_GRID))
    wk, l_q, why = resolve_wing(snap, side, k, width)
    if wk is None:
        return None, why

    s_map = get_mapping(exp, k, side)
    l_map = get_mapping(exp, wk, side)
    if not s_map or not l_map:
        return None, "not_in_scrip_master"
    if int(s_map["lot"]) != int(l_map["lot"]):
        return None, "lot_mismatch"

    credit = round(s_q["ltp"] - l_q["ltp"], 2)
    if credit <= 0:
        return None, "credit_not_positive"
    if credit >= width:
        return None, "credit_exceeds_width"
    if credit < _f(f.get("min_credit")):
        return None, "below_min_credit"

    lot = int(s_map["lot"])
    lots = max(1, int(f.get("lots", 1) or 1))
    qty = lot * lots
    max_profit = credit * qty
    max_loss = (width - credit) * qty
    ror = round(max_profit / max_loss * 100.0, 2) if max_loss > 0 else 0.0
    if ror < _f(f.get("min_ror")):
        return None, "below_min_ror"

    be = k + credit if side == "ce" else k - credit
    spread_pop = calculate_pop_exact(snap["synth"], k, credit, snap["T"], s_q["iv"], side)
    if spread_pop is None:
        return None, "spread_pop_uncomputable"
    if spread_pop < _f(f.get("min_spread_pop")):
        return None, "below_min_spread_pop"

    nd = (-s_q["delta"] + l_q["delta"]) if side == "ce" else (s_q["delta"] - l_q["delta"])
    ng = -s_q["gamma"] + l_q["gamma"]
    nt = -s_q["theta"] + l_q["theta"]
    nv = -s_q["vega"] + l_q["vega"]

    return {
        "key": "%s|%s|%d|%d" % (exp, opt_type, k, wk),
        "Expiry": exp, "DTE": dte, "Type": opt_type, "side": side,
        "Short_Strike": k, "Long_Strike": wk, "Wing_Width": width,
        "Short_LTP": round(s_q["ltp"], 2), "Long_LTP": round(l_q["ltp"], 2),
        "Net_Credit": credit, "Credit_Received": round(max_profit, 2),
        "Max_Profit": round(max_profit, 2), "Max_Loss": round(max_loss, 2),
        "ROR": ror, "Breakeven": round(be, 2),
        "Short_POP": round(short_pop, 1), "Spread_POP": round(spread_pop, 1),
        "Efficiency": eff,
        "Spread_Efficiency": (round(nt / (abs(ng) * 100.0), 1)
                              if abs(ng) > 1e-9 else None),
        "Net_Delta": round(nd, 4), "Net_Gamma": round(ng, 7),
        "Net_Theta": round(nt, 3), "Net_Vega": round(nv, 2),
        "Lot_Size": lot, "Lots": lots, "Qty": qty,
        "Spot": round(snap["spot"], 2), "Synth": round(snap["synth"], 2),
        "Label": "%d / %d %s" % (k, wk, "CE" if side == "ce" else "PE"),
        "Short_Map": s_map, "Long_Map": l_map, "Short_Q": s_q, "Long_Q": l_q,
    }, None


def attach_margin(cand):
    """Local arithmetic only — a live quote per screener row would be dozens of
    API calls against a rate-limited endpoint."""
    m = spread_margin(cand)
    cand["Margin"] = m.get("margin")
    cand["Margin_Source"] = m.get("source")
    cand["Margin_Naked"] = m.get("naked_equivalent")
    cand["ROI_On_Margin"] = m.get("roi_on_margin")
    return cand


_PRIVATE = ("Short_Map", "Long_Map", "Short_Q", "Long_Q")


def public_match(m):
    return {k: v for k, v in m.items() if k not in _PRIVATE}


def position_index():
    """Open spreads, plus every strike already held in ANY leg — selling a strike
    we hold long as another spread's wing nets to flat at the broker and
    destroys that hedge."""
    keys, strikes = set(), set()
    for p in STATE.paper_positions:
        keys.add("%s|%s|%d" % (p.get("Expiry"), p.get("Type"), _f(p.get("Short_Strike"))))
        for lg in p.get("legs", []):
            strikes.add((p.get("Expiry"), p.get("Type"),
                         round(_f(lg.get("drv_strike_price")))))
    return keys, strikes


def run_screener_scan(f):
    matches, rejects = [], {}
    now = now_ist()
    with STATE.lock:
        open_keys, held = position_index()

    for exp in list(STATE.expiry_list):
        try:
            dte = dte_of(exp, now)
        except Exception:
            continue
        if not (f["dte_range"][0] <= dte <= f["dte_range"][1]):
            continue
        snap = CHAINS.get(exp)
        if not snap or snap.get("stale"):
            rejects["chain_unavailable"] = rejects.get("chain_unavailable", 0) + 1
            continue

        for k in sorted(snap["chain"]):
            if round(k) % STRIKE_GRID != 0:
                continue
            for side in ("ce", "pe"):
                opt_type = SIDE_TO_TYPE[side]
                if "%s|%s|%d" % (exp, opt_type, k) in open_keys:
                    continue
                if (exp, opt_type, round(k)) in held:
                    continue
                try:
                    s_q = quote_of(node_at(snap, k, side))
                    if not s_q:
                        continue

                    # ---- the original four gates, on the short leg, verbatim ----
                    if not (f["ltp_range"][0] <= s_q["ltp"] <= f["ltp_range"][1]):
                        continue
                    short_pop = calculate_pop_exact(snap["synth"], k, s_q["ltp"],
                                                    snap["T"], s_q["iv"], side)
                    if short_pop is None or short_pop < f["min_pop"]:
                        continue
                    eff = (round(abs(s_q["theta"]) / (s_q["gamma"] * 100.0), 2)
                           if s_q["gamma"] > 1e-12 else 0.0)
                    if eff < f["min_eff"]:
                        continue
                    # -------------------------------------------------------------

                    cand, why = build_spread_candidate(f, exp, dte, snap, k, side,
                                                       s_q, short_pop, eff)
                    # Buying a wing at a strike we are already short elsewhere
                    # nets to flat at the broker and destroys both hedges, so
                    # deploy refuses it — do not offer it in the first place.
                    if cand and (exp, opt_type, round(cand["Long_Strike"])) in held:
                        cand, why = None, "wing_already_held"
                    if cand:
                        matches.append(attach_margin(cand))
                    elif why:
                        rejects[why] = rejects.get(why, 0) + 1
                except Exception as e:
                    # One malformed strike must not abort the whole expiry.
                    rejects["error"] = rejects.get("error", 0) + 1
                    log_event("error", "candidate %s %s %s: %s" % (exp, k, side, e))

    matches.sort(key=lambda m: (-_f(m["ROR"]), -_f(m["Spread_POP"])))
    with STATE.lock:
        STATE.last_scan = {m["key"]: m for m in matches}
        STATE.last_rejects = rejects
    return matches


# ─────────────────────────────────────────────────────────────────────────────
#  MARK TO MARKET / EXIT
# ─────────────────────────────────────────────────────────────────────────────
def intrinsic(leg, spot):
    k = _f(leg.get("drv_strike_price"))
    if not spot or spot <= 0 or k <= 0:
        return None
    return (max(0.0, spot - k) if leg.get("drv_option_type") == "CALL"
            else max(0.0, k - spot))


def resolve_leg_price(snap, leg):
    """Returns (price, source) or (None, 'unavailable').

    Never silently substitutes the entry price.  A node that EXISTS and quotes
    0.00 is a real price — a far-OTM wing is genuinely worthless — but a node
    that is ABSENT is not a price at all.  The old code conflated the two, so a
    failed fetch booked a permanent, traceless realized P&L of exactly Rs 0.00.
    """
    if snap is None:
        return None, "unavailable"
    side = TYPE_TO_SIDE.get(leg.get("drv_option_type"), "ce")
    node = node_at(snap, leg.get("drv_strike_price"), side)
    if node is None:
        # Past expiry the chain simply disappears.  Index options are cash
        # settled, so settle at intrinsic rather than deferring forever.
        try:
            if dte_of(leg["drv_expiry_date"]) < 0:
                iv = intrinsic(leg, snap.get("spot"))
                return (iv, "settled_intrinsic") if iv is not None else (None, "unavailable")
        except Exception:
            pass
        return None, "unavailable"
    q = quote_of(node) or {}
    if _f(q.get("ltp")) > 0:
        return _f(q["ltp"]), "ltp"
    bid, ask = _f(q.get("bid")), _f(q.get("ask"))
    if bid > 0 and ask >= bid:
        return round((bid + ask) / 2.0, 2), "mid"
    if ask > 0:
        return ask, "ask"
    iv = intrinsic(leg, snap.get("spot"))
    return (iv, "intrinsic") if iv is not None else (0.0, "zero")


def mark_position(pos, snap):
    """Must be called under STATE.lock — it writes last_mark into the legs.  By
    that point the network call has already happened, so it is pure CPU."""
    value, ok, detail = 0.0, True, []
    for leg in pos.get("legs", []):
        px, src = resolve_leg_price(snap, leg)
        if px is None:
            ok = False
            px = _f(leg.get("last_mark"), _f(leg.get("entry_fill_price")))
            src = "last_mark"
        else:
            leg["last_mark"], leg["last_mark_source"] = round(px, 2), src
        value += -leg_sign(leg) * px
        detail.append({"role": leg.get("role"), "strike": leg.get("drv_strike_price"),
                       "price": round(px, 2), "source": src})
    clamped = False
    w = _f(pos.get("Wing_Width"))
    if w > 0 and not (0.0 <= value <= w):
        # A vertical's value is bounded by [0, width]; anything outside is a
        # crossed or stale quote.  Clamp so the screen can never show a loss
        # bigger than max loss.
        value, clamped = min(max(value, 0.0), w), True
    qty = int(_f(pos.get("Qty"), 65))
    return {"value": round(value, 2),
            "pnl": round((_f(pos.get("Net_Credit")) - value) * qty, 2),
            "ok": ok, "clamped": clamped, "legs": detail}


def close_position(pos, snap, reason, allow_degraded=False):
    """Returns the closed record, or None to defer.  Display tolerates any mark;
    CLOSING writes permanently to history, so it demands a real price on every
    leg.  A half-closed spread is a naked short — the exact thing this whole
    change exists to eliminate — so it is all legs or none."""
    mtm = mark_position(pos, snap)
    sources = [d["source"] for d in mtm["legs"]]
    good = all(s in GOOD_EXIT_SOURCES for s in sources)
    if not good and not allow_degraded:
        return None
    ts = ts_now()
    closed = json.loads(json.dumps(pos))
    by_role = {d["role"]: d for d in mtm["legs"]}
    realized = 0.0
    for leg in legs_exit_order(closed):
        d = by_role.get(leg.get("role")) or {"price": _f(leg.get("last_mark")),
                                             "source": "last_mark"}
        leg["exit_quote"] = leg["exit_fill_price"] = d["price"]
        leg["exit_price_source"] = d["source"]
        leg["exit_filled_qty"] = int(leg.get("quantity", 0))
        leg["exit_order_status"], leg["exit_time"] = "PAPER_FILLED", ts
        realized += leg_sign(leg) * (d["price"] - _f(leg.get("entry_fill_price"))) \
            * int(leg.get("quantity", 0))
    if not good:
        reason += "|MARK_DEGRADED"
    closed.update({"Status": "CLOSED", "Exit_Time": ts, "Exit_Reason": reason,
                   "Net_Exit_Debit": mtm["value"], "Realized_PnL": round(realized, 2)})
    return mirror_legacy_keys(closed)


def do_auto_exit(exit_dte, force_ids=None, reason="DTE_RULE"):
    """Three phases: pick under the lock, fetch WITHOUT it, apply under it.
    The old version held STATE.lock across a 10-second HTTP call per position,
    freezing the entire UI."""
    now = now_ist()
    force_ids = set(force_ids or [])
    with STATE.lock:
        due = []
        for p in STATE.paper_positions:
            if p.get("id") in force_ids:
                due.append(p["id"])
                continue
            if force_ids:
                continue
            try:
                live_dte = dte_of(p["Expiry"], now)
            except Exception:
                live_dte = int(_f(p.get("Entry_DTE"), 99))
            if live_dte <= exit_dte:
                due.append(p["id"])
        due = set(due)
        exps = {p["Expiry"] for p in STATE.paper_positions if p.get("id") in due}
    if not due:
        return 0, []

    snaps = {e: CHAINS.get(e, force=True) for e in exps}

    exited, deferred, keep = 0, [], []
    with STATE.lock:
        for p in STATE.paper_positions:
            if p.get("id") not in due:
                keep.append(p)
                continue
            degraded = int(_f(p.get("Defer_Count"))) >= MAX_DEFERRALS
            rec = close_position(p, snaps.get(p.get("Expiry")), reason, degraded)
            if rec is None:
                p["Defer_Count"] = int(_f(p.get("Defer_Count"))) + 1
                p["Defer_Note"] = "no usable mark at %s" % now.strftime("%H:%M:%S")
                deferred.append(p.get("id"))
                keep.append(p)
                continue
            STATE.trade_history.append(rec)
            exited += 1
        if exited or deferred:
            STATE.paper_positions = keep
            STATE.save()
    if exited:
        log_event("exit", "closed %d position(s) [%s]" % (exited, reason))
    if deferred:
        log_event("exit", "deferred %d position(s): no usable price" % len(deferred))
    return exited, deferred


def do_auto_deploy(f):
    matches = run_screener_scan(f)
    new = 0
    with STATE.lock:
        open_keys, held = position_index()
        for m in matches:
            key = "%s|%s|%d" % (m["Expiry"], m["Type"], m["Short_Strike"])
            if key in open_keys:
                continue
            if any((m["Expiry"], m["Type"], round(s)) in held
                   for s in (m["Short_Strike"], m["Long_Strike"])):
                continue
            STATE.paper_positions.append(make_spread_position(m, f.get("lots", 1)))
            open_keys.add(key)
            held.add((m["Expiry"], m["Type"], round(m["Short_Strike"])))
            held.add((m["Expiry"], m["Type"], round(m["Long_Strike"])))
            new += 1
        if new:
            STATE.save()
    if new:
        log_event("deploy", "auto-deployed %d spread(s)" % new)
    return new


# ─────────────────────────────────────────────────────────────────────────────
#  MARKET HOURS + SCANNER
# ─────────────────────────────────────────────────────────────────────────────
MKT_OPEN, MKT_CLOSE = dtime(9, 15), dtime(15, 30)
SCAN_INTERVAL = 60
HEARTBEAT_CLOSED = 900
TICK = 5
EXPIRY_REFRESH = 6 * 3600
_SHUTDOWN = threading.Event()


def load_holidays():
    data = read_json_safe(HOLIDAY_FILE, default=[]) or []
    return {str(d)[:10] for d in data} if isinstance(data, list) else set()


def market_state(now=None):
    now = now or now_ist()
    if STATE.force_scan:
        return "OPEN", "manual override"
    if now.weekday() >= 5:
        return "CLOSED", "weekend"
    if now.date().isoformat() in load_holidays():
        return "CLOSED", "NSE holiday"
    t = now.time()
    if t < MKT_OPEN:
        return "PRE", "pre-open, session starts 09:15 IST"
    if t > MKT_CLOSE:
        return "CLOSED", "after close"
    return "OPEN", "regular session"


def record_pnl_point():
    with STATE.lock:
        if not STATE.paper_positions:
            return
        expiries = {p.get("Expiry") for p in STATE.paper_positions if p.get("Expiry")}
    snaps = {e: CHAINS.get(e) for e in expiries}
    with STATE.lock:
        total = sum(mark_position(p, snaps.get(p.get("Expiry")))["pnl"]
                    for p in STATE.paper_positions)
        STATE.pnl_series.append([int(time.time()), round(total, 2)])
        if len(STATE.pnl_series) > 3000:
            STATE.pnl_series = STATE.pnl_series[-3000:]


# ─────────────────────────────────────────────────────────────────────────────
#  VIX KILL SWITCH
#  While India VIX is ABOVE the limit this hedged-selling strategy takes no new
#  trades and closes every open spread.  Trading resumes by itself once VIX is
#  back at or below the limit.
#
#  The limit is set in ONE place: NIFTY Trader's "VIX limit" (hub/risk.json).
#  It is re-read every cycle, so a change applies within a minute, no restart.
#  0 turns the switch off.  If VIX cannot be read, no new trades are opened
#  (open spreads are kept - closing them on a missing price would be a guess).
# ─────────────────────────────────────────────────────────────────────────────


def vix_limit():
    try:
        with open(RISK_FILE, encoding="utf-8") as f:
            d = json.load(f)
        v = float(d.get("vix_limit", DEFAULT_VIX_LIMIT))
        # Unticked for this strategy in the hub's VIX limit dialog = switch off.
        if not (d.get("apply") or {}).get(os.path.basename(APP_DIR), True):
            return 0.0
        return v if math.isfinite(v) and v >= 0 else DEFAULT_VIX_LIMIT
    except (OSError, ValueError, TypeError, AttributeError):
        return DEFAULT_VIX_LIMIT


def fetch_india_vix():
    """(live India VIX, "") or (None, why)."""
    res = call_dhan("marketfeed/ltp", {VIX_SEG: [VIX_SECURITY_ID]}, timeout=10)
    if res.get("status") != "success":
        return None, _scrub(res.get("message") or "no answer")
    seg = (res.get("data") or {}).get(VIX_SEG) or {}
    node = seg.get(str(VIX_SECURITY_ID)) or seg.get(VIX_SECURITY_ID) or {}
    v = _f(node.get("last_price") if isinstance(node, dict) else None)
    return (v, "") if v > 0 else (None, "no VIX price in Dhan's answer")


def vix_guard(close=True):
    """Returns (new trades allowed, spreads closed by the kill switch).
    close=False only reads VIX for the dashboard (outside market hours)."""
    limit = vix_limit()
    STATE.vix_limit = limit
    if limit <= 0:
        STATE.vix_kill_on = False
        STATE.vix_note = "VIX kill switch is off (limit 0)"
        return True, 0
    v, err = fetch_india_vix()
    if v is None:
        note = "India VIX unavailable (%s) - no new trades until it can be read" % err
        if note != STATE.vix_note:
            log_event("vix", note)
        STATE.vix_note = note
        return False, 0
    STATE.vix, STATE.vix_at = v, now_ist().strftime("%H:%M:%S")
    kill = v > limit
    if kill != STATE.vix_kill_on:
        log_event("vix", ("India VIX %.2f crossed ABOVE the %.2f limit - KILL SWITCH ON: "
                          "no new trades, closing every open spread" if kill else
                          "India VIX %.2f is back at or below the %.2f limit - "
                          "new trades allowed again") % (v, limit))
    STATE.vix_kill_on = kill
    STATE.vix_note = "India VIX %.2f at %s, limit %.2f" % (v, STATE.vix_at, limit)
    if not kill or not close:
        return not kill, 0
    with STATE.lock:
        ids = [p.get("id") for p in STATE.paper_positions]
    closed = 0
    if ids:
        # Deferred ones (no usable price yet) are retried on the next cycle.
        closed, _ = do_auto_exit(0, force_ids=ids, reason="VIX_KILL")
    return False, closed


def do_scan_cycle():
    f = dict(STATE.filters)
    allowed, nk = vix_guard()
    nx, _ = do_auto_exit(f["exit_dte"])
    nx += nk
    nd = do_auto_deploy(f) if allowed else 0
    record_pnl_point()
    STATE.last_scan_time = now_ist().strftime("%H:%M:%S")
    if not allowed:
        STATE.status_message = ("No new trades - %s%s at %s"
                                % (STATE.vix_note, (", closed %d" % nx) if nx else "",
                                   STATE.last_scan_time))
        if nx:
            with STATE.lock:
                STATE.save()
    elif nd or nx:
        STATE.status_message = ("Deployed %d, exited %d at %s"
                                % (nd, nx, STATE.last_scan_time))
        with STATE.lock:
            STATE.save()
    else:
        STATE.status_message = "Scanned, no action, %s" % STATE.last_scan_time


def boot_loop():
    while not _SHUTDOWN.is_set():
        try:
            STATE.scrip_lookup = load_scrip_lookup()
            STATE.expiry_list = fetch_expiry_list()
            STATE.expiry_fetched = time.time()
            if STATE.expiry_list:
                STATE.status_message = ("Ready - %d expiries, %d NIFTY contracts"
                                        % (len(STATE.expiry_list), len(STATE.scrip_lookup)))
                log_event("boot", STATE.status_message)
                return
            ts = token_status()
            STATE.status_message = ("Could not load expiries - token %s. Open Settings."
                                    % ts["human"])
            log_event("boot", STATE.status_message)
        except Exception as e:
            STATE.status_message = "Boot error: %s" % e
            log_event("error", "boot: %s" % e)
        # A transient failure at startup used to degrade the app permanently.
        _SHUTDOWN.wait(120)


_AUTOSTART_WAIT_LOGGED = [False]


def maybe_autostart():
    """Launch = scanning.  Same gate as the Start button (/api/scanner/start):
    only the scanner owner, and only with a configured, unexpired token.  A
    missing or expired token just waits - no error loop - and Stop cancels."""
    if not STATE.autostart or STATE.scanning_active or not STATE.scanner_owner:
        return
    ts = token_status()
    if not ts["configured"] or ts["expired"]:
        if not _AUTOSTART_WAIT_LOGGED[0]:
            _AUTOSTART_WAIT_LOGGED[0] = True
            log_event("scan", "auto-start waiting: token %s - the scanner starts by itself "
                              "once a valid token is set" % ts["human"])
        return
    with STATE.lock:
        if not STATE.autostart or STATE.scanning_active:
            return
        STATE.autostart = False
        STATE.scanning_active = True
        STATE.save()
    log_event("scan", "scanner started automatically on launch")


def scanner_loop():
    last_scan = last_beat = last_guard = 0.0
    log_event("boot", "scanner thread started")
    try:
        maybe_autostart()
    except Exception as e:
        log_event("error", "auto-start: %s: %s" % (e.__class__.__name__, e))
    while not _SHUTDOWN.is_set():
        _SHUTDOWN.wait(TICK)
        if _SHUTDOWN.is_set():
            break
        try:
            now = time.time()
            state, why = market_state()
            STATE.market_note = "%s - %s" % (state, why)
            maybe_autostart()

            if (STATE.expiry_list and
                    now - STATE.expiry_fetched > EXPIRY_REFRESH and state == "OPEN"):
                lst = fetch_expiry_list()
                if lst:
                    STATE.expiry_list = lst
                STATE.expiry_fetched = now

            if state == "OPEN" and STATE.scanning_active:
                if now - last_scan >= SCAN_INTERVAL:
                    last_scan = now
                    ts = token_status()
                    if not ts["configured"] or ts["expired"]:
                        STATE.status_message = "Scan skipped - token %s. Open Settings." % ts["human"]
                        if now - last_beat >= HEARTBEAT_CLOSED:
                            last_beat = now
                            log_event("token", "scan skipped: %s" % ts["human"])
                        continue
                    do_scan_cycle()
            elif (state == "OPEN" and STATE.scanner_owner and STATE.paper_positions
                  and now - last_guard >= SCAN_INTERVAL):
                # Scanner stopped but spreads are open: the kill switch still
                # protects them.
                last_guard = now
                vix_guard()
            elif (state != "OPEN" and STATE.scanner_owner
                  and now - last_guard >= (60 if STATE.vix is None else HEARTBEAT_CLOSED)):
                # Market closed: read VIX now and then so the dashboard shows it
                # and the limit.  Never closes anything outside market hours.
                last_guard = now
                vix_guard(close=False)
            elif now - last_beat >= HEARTBEAT_CLOSED:
                last_beat = now
                ts = token_status()
                STATE.status_message = "Idle (%s) - token %s" % (why, ts["human"])
                log_event("market", "heartbeat: %s; token %s" % (why, ts["human"]))
                if ts["configured"] and not ts["expired"] and ts["warn"]:
                    log_event("token", "token expires in under 2 hours - paste a fresh one")
        except Exception as e:
            log_event("error", "scanner: %s: %s" % (e.__class__.__name__, e))
            STATE.status_message = "Scanner error: %s" % e


# ─────────────────────────────────────────────────────────────────────────────
#  FLASK + AUTH
# ─────────────────────────────────────────────────────────────────────────────
app = Flask(__name__)

LISTEN_PUBLIC = (_env("APP_ENV") == "hosted") or (_env("HOST") == "0.0.0.0") \
    or bool(_env("PORT") and _env("APP_ENV"))


def _write_private_bytes(path, data):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".tmp_")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        if os.name != "nt":
            os.chmod(tmp, 0o600)
        os.replace(tmp, path)
        tmp = None
    finally:
        if tmp and os.path.exists(tmp):
            os.unlink(tmp)


def _load_secret_key():
    k = _env("SECRET_KEY")
    if k:
        return k.encode("utf-8")
    if os.path.exists(SECRET_FILE):
        try:
            with open(SECRET_FILE, "rb") as f:
                k = f.read().strip()
            if len(k) >= 32:
                return k
        except OSError:
            pass
    k = secrets.token_hex(32).encode("ascii")
    _write_private_bytes(SECRET_FILE, k)
    return k


app.secret_key = _load_secret_key()
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=(_env("COOKIE_SECURE", "0") == "1"),
    PERMANENT_SESSION_LIFETIME=timedelta(days=30),
    MAX_CONTENT_LENGTH=256 * 1024,
)

_SCRYPT = dict(n=2 ** 14, r=8, p=1, maxmem=64 * 1024 * 1024, dklen=32)


def hash_password(pw, salt=None):
    salt = salt or secrets.token_bytes(16)
    dk = hashlib.scrypt(pw.encode("utf-8"), salt=salt, **_SCRYPT)
    return {"algo": "scrypt", "n": _SCRYPT["n"], "r": _SCRYPT["r"], "p": _SCRYPT["p"],
            "salt": salt.hex(), "hash": dk.hex()}


def verify_password(pw, rec):
    if not rec or rec.get("algo") != "scrypt":
        return False
    try:
        dk = hashlib.scrypt(pw.encode("utf-8"), salt=bytes.fromhex(rec["salt"]),
                            n=rec["n"], r=rec["r"], p=rec["p"],
                            maxmem=_SCRYPT["maxmem"], dklen=32)
    except Exception:
        return False
    return hmac.compare_digest(dk.hex(), rec.get("hash", ""))


def _bootstrap_auth():
    """Password required whenever the app is reachable from outside this
    machine.  Purely local runs (the pendrive case) skip the gate."""
    stored = read_json_safe(AUTH_FILE, default=None)
    env_pw = _env("APP_PASSWORD")
    if env_pw:
        fp = hashlib.sha256(("v1" + env_pw).encode()).hexdigest()[:16]
        if not stored or stored.get("env_fp") != fp:
            rec = hash_password(env_pw)
            rec["env_fp"] = fp
            write_json_atomic(AUTH_FILE, rec, private=True)
            log_event("boot", "login password set from APP_PASSWORD")
            return rec
        return stored
    if stored:
        return stored
    if not LISTEN_PUBLIC:
        return None
    gen = secrets.token_urlsafe(12)
    rec = hash_password(gen)
    write_json_atomic(AUTH_FILE, rec, private=True)
    print("\n" + "=" * 64)
    print("  NO APP_PASSWORD SET. Generated a login password:")
    print("      %s" % gen)
    print("  Set APP_PASSWORD and restart to choose your own.")
    print("=" * 64 + "\n", flush=True)
    log_event("boot", "generated a random login password (see console)")
    return rec


AUTH_RECORD = _bootstrap_auth()
AUTH_ON = AUTH_RECORD is not None

_LOCKOUT_MAX, _LOCKOUT_WINDOW, _LOCKOUT_SECONDS = 6, 600, 900
_fail_lock = threading.Lock()
_fails = {}


def _client_ip():
    if _env("TRUST_PROXY", "0") == "1":
        xff = request.headers.get("X-Forwarded-For", "")
        if xff:
            return xff.split(",")[0].strip()
    return request.remote_addr or "?"


def lockout_remaining(ip):
    now = time.time()
    with _fail_lock:
        rec = _fails.get(ip)
        if not rec:
            return 0
        if rec["until"] > now:
            return int(rec["until"] - now)
        if now - rec["first"] > _LOCKOUT_WINDOW:
            _fails.pop(ip, None)
        return 0


def note_failure(ip):
    now = time.time()
    with _fail_lock:
        rec = _fails.setdefault(ip, {"n": 0, "first": now, "until": 0.0})
        if now - rec["first"] > _LOCKOUT_WINDOW:
            rec.update(n=0, first=now, until=0.0)
        rec["n"] += 1
        if rec["n"] >= _LOCKOUT_MAX:
            rec["until"] = now + _LOCKOUT_SECONDS
            log_event("auth", "locked out %s for %d min" % (ip, _LOCKOUT_SECONDS // 60))
        if len(_fails) > 2000:
            _fails.clear()


PUBLIC_PATHS = {"/login", "/health", "/healthz", "/favicon.ico"}


def _logged_in():
    return (not AUTH_ON) or session.get("auth") is True


@app.before_request
def _gate():
    if request.path in PUBLIC_PATHS:
        return None
    if not _logged_in():
        if request.path.startswith("/api/"):
            return jsonify({"error": "not authenticated", "login_required": True}), 401
        return redirect(url_for("login"))
    if AUTH_ON and request.method not in ("GET", "HEAD", "OPTIONS"):
        sent = request.headers.get("X-CSRF-Token", "")
        want = session.get("csrf", "")
        if not want or not hmac.compare_digest(sent, want):
            return jsonify({"error": "bad or missing CSRF token"}), 403
    return None


@app.after_request
def _csrf_cookie(resp):
    if AUTH_ON and session.get("auth") and session.get("csrf"):
        resp.set_cookie("csrf", session["csrf"], samesite="Lax", httponly=False,
                        secure=app.config["SESSION_COOKIE_SECURE"], max_age=30 * 24 * 3600)
    return resp


@app.route("/login", methods=["GET", "POST"])
def login():
    if not AUTH_ON:
        return redirect("/")
    ip = _client_ip()
    left = lockout_remaining(ip)
    error = None
    if request.method == "POST":
        if left:
            error = "Too many attempts. Try again in %dm %ds." % (left // 60, left % 60)
        elif verify_password(request.form.get("password") or "", AUTH_RECORD):
            with _fail_lock:
                _fails.pop(ip, None)
            session.clear()
            session.permanent = True
            session["auth"] = True
            session["csrf"] = secrets.token_urlsafe(24)
            log_event("auth", "login OK from %s" % ip)
            return redirect("/")
        else:
            note_failure(ip)
            log_event("auth", "login FAILED from %s" % ip)
            error = "Wrong password."
            left = lockout_remaining(ip)
    return render_template_string(LOGIN_HTML, error=error, locked=left)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login") if AUTH_ON else "/")


# ─────────────────────────────────────────────────────────────────────────────
#  ROUTES
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return Response(INDEX_HTML, mimetype="text/html")


@app.route("/health")
@app.route("/healthz")
def health():
    ts = token_status()
    ok = bool(STATE.expiry_list) and ts["configured"] and not ts["expired"]
    return jsonify({
        "ok": ok, "token": ts["human"], "expiries": len(STATE.expiry_list),
        "open_positions": len(STATE.paper_positions),
        "scanning": STATE.scanning_active, "market": STATE.market_note,
        "last_scan": STATE.last_scan_time, "scanner_owner": STATE.scanner_owner,
    }), (200 if ok else 503)


@app.route("/api/status")
def api_status():
    return jsonify({
        "scanning_active": STATE.scanning_active,
        "autostart": STATE.autostart,
        "force_scan": STATE.force_scan,
        "last_scan_time": STATE.last_scan_time,
        "status_message": STATE.status_message,
        "market": STATE.market_note,
        "expiry_list": STATE.expiry_list,
        "scrip_count": len(STATE.scrip_lookup),
        "open_count": len(STATE.paper_positions),
        "filters": STATE.filters,
        "token": token_status(),
        "auth_on": AUTH_ON,
        "scanner_owner": STATE.scanner_owner,
        "vix": {"value": STATE.vix, "at": STATE.vix_at, "limit": vix_limit(),
                "kill": STATE.vix_kill_on, "note": STATE.vix_note},
    })


@app.route("/api/filters", methods=["POST"])
def api_set_filters():
    if STATE.scanning_active:
        return jsonify({"error": "Stop the scanner before changing filters."}), 400
    body = request.get_json(force=True, silent=True) or {}
    f = dict(STATE.filters)
    for key in ("min_eff", "min_pop", "min_credit", "min_ror", "min_spread_pop"):
        if key in body:
            f[key] = _f(body[key])
    for key in ("exit_dte", "lots"):
        if key in body:
            f[key] = max(1, int(_f(body[key], f[key])))
    if "wing_width" in body:
        f["wing_width"] = max(50, int(_f(body["wing_width"], f["wing_width"])))
    for key in ("dte_range", "ltp_range"):
        v = body.get(key)
        if isinstance(v, (list, tuple)) and len(v) == 2:
            lo, hi = _f(v[0]), _f(v[1])
            # Inverted sliders used to return zero matches forever with no hint.
            f[key] = [min(lo, hi), max(lo, hi)]
    with STATE.lock:
        STATE.filters = f
        STATE.save()
    return jsonify({"ok": True, "filters": f})


@app.route("/api/scanner/start", methods=["POST"])
def api_scanner_start():
    if not STATE.scanner_owner:
        return jsonify({"error": "This process does not own the scanner."}), 409
    ts = token_status()
    if not ts["configured"] or ts["expired"]:
        return jsonify({"error": "Access token %s. Open Settings and paste a fresh one."
                        % ts["human"]}), 400
    with STATE.lock:
        STATE.autostart = False
        STATE.scanning_active = True
        STATE.save()
    log_event("scan", "scanner started")
    return jsonify({"ok": True})


@app.route("/api/scanner/stop", methods=["POST"])
def api_scanner_stop():
    # Stop also cancels a pending auto-start, so "Stop" always means "not
    # scanning" until Start is pressed or the strategy is launched again.
    with STATE.lock:
        STATE.autostart = False
        STATE.scanning_active = False
        STATE.save()
    log_event("scan", "scanner stopped")
    return jsonify({"ok": True})


@app.route("/api/scanner/force", methods=["POST"])
def api_scanner_force():
    body = request.get_json(force=True, silent=True) or {}
    STATE.force_scan = bool(body.get("on"))
    with STATE.lock:
        STATE.save()
    return jsonify({"ok": True, "force_scan": STATE.force_scan})


@app.route("/api/chain")
def api_chain():
    expiry = request.args.get("expiry", "")
    if not expiry:
        return jsonify({"error": "expiry required"}), 400
    snap = CHAINS.get(expiry)
    if not snap:
        return jsonify({"error": "Could not load the chain. %s"
                        % token_status()["human"]}), 502
    rows = []
    for k in sorted(snap["chain"]):
        ce = quote_of(snap["chain"][k].get("ce")) or {}
        pe = quote_of(snap["chain"][k].get("pe")) or {}
        # The old code dropped every strike under 10 rupees, which is exactly
        # the far-OTM wing a spread seller buys and where the skew lives.
        rows.append({
            "strike": k,
            "ce_ltp": round(_f(ce.get("ltp")), 2), "pe_ltp": round(_f(pe.get("ltp")), 2),
            "ce_oi": _f(ce.get("oi")), "pe_oi": _f(pe.get("oi")),
            "ce_doi": ce.get("doi"), "pe_doi": pe.get("doi"),
            "ce_iv": round(_f(ce.get("iv")) * 100, 2), "pe_iv": round(_f(pe.get("iv")) * 100, 2),
            "ce_delta": round(_f(ce.get("delta")), 4), "pe_delta": round(_f(pe.get("delta")), 4),
            "ce_gamma": round(_f(ce.get("gamma")), 6), "pe_gamma": round(_f(pe.get("gamma")), 6),
            "ce_theta": round(_f(ce.get("theta")), 3), "pe_theta": round(_f(pe.get("theta")), 3),
            "ce_pop": calculate_pop_exact(snap["synth"], k, _f(ce.get("ltp")),
                                          snap["T"], _f(ce.get("iv")), "ce"),
            "pe_pop": calculate_pop_exact(snap["synth"], k, _f(pe.get("ltp")),
                                          snap["T"], _f(pe.get("iv")), "pe"),
        })
    return jsonify({"spot": round(snap["spot"], 2), "synth": round(snap["synth"], 2),
                    "atm": snap["atm"], "dte": dte_of(expiry), "expiry": expiry,
                    "stale": snap.get("stale", False),
                    "key": "%s|%d" % (expiry, int(snap["ts"])), "rows": rows})


@app.route("/api/screener/run", methods=["POST"])
def api_screener_run():
    if not STATE.expiry_list:
        return jsonify({"matches": [], "rejects": {},
                        "note": "No expiries loaded. %s" % token_status()["human"]})
    if not STATE.scrip_lookup:
        return jsonify({"matches": [], "rejects": {},
                        "note": "Scrip master unavailable - cannot resolve lot sizes."})
    matches = run_screener_scan(dict(STATE.filters))
    return jsonify({"matches": [public_match(m) for m in matches],
                    "rejects": STATE.last_rejects,
                    "wing_width": STATE.filters["wing_width"]})


@app.route("/api/screener/deploy", methods=["POST"])
def api_screener_deploy():
    """Re-validated server-side against the last scan.  The old endpoint trusted
    whatever LTP, SecurityID and Qty the browser posted and had no duplicate
    check at all, so a double-click opened the same position twice."""
    keys = (request.get_json(force=True, silent=True) or {}).get("keys") or []
    if STATE.vix_kill_on:
        return jsonify({"error": "VIX kill switch is on (%s). No new trades until India VIX "
                                 "is back at or below the limit." % STATE.vix_note}), 400
    deployed, dupes, stale = 0, 0, 0
    with STATE.lock:
        open_keys, held = position_index()
        for key in keys:
            m = STATE.last_scan.get(key)
            if not m:
                stale += 1
                continue
            k = "%s|%s|%d" % (m["Expiry"], m["Type"], m["Short_Strike"])
            if k in open_keys or any((m["Expiry"], m["Type"], round(s)) in held
                                     for s in (m["Short_Strike"], m["Long_Strike"])):
                dupes += 1
                continue
            STATE.paper_positions.append(make_spread_position(m, STATE.filters.get("lots", 1)))
            open_keys.add(k)
            held.add((m["Expiry"], m["Type"], round(m["Short_Strike"])))
            held.add((m["Expiry"], m["Type"], round(m["Long_Strike"])))
            deployed += 1
        if deployed:
            STATE.save()
    if deployed:
        log_event("deploy", "manually deployed %d spread(s)" % deployed)
    return jsonify({"ok": True, "deployed": deployed, "duplicates": dupes, "stale": stale})


@app.route("/api/margin", methods=["POST"])
def api_margin():
    """One live basket quote, for the row he actually clicked.  Never called per
    screener row — margincalculator is rate-limited and the screener can return
    thirty candidates."""
    body = request.get_json(force=True, silent=True) or {}
    key, pid = body.get("key"), body.get("id")
    if pid:
        with STATE.lock:
            obj = next((p for p in STATE.paper_positions if p.get("id") == pid), None)
        if not obj:
            return jsonify({"error": "position not found"}), 404
        return jsonify(spread_margin(obj, live=True, include_position=True))
    if key:
        obj = STATE.last_scan.get(key)
        if not obj:
            return jsonify({"error": "stale row - rerun the screener"}), 404
        return jsonify(spread_margin(obj, live=True))
    return jsonify({"error": "key or id required"}), 400


@app.route("/api/positions")
def api_positions():
    exit_dte = STATE.filters["exit_dte"]
    with STATE.lock:
        expiries = {p.get("Expiry") for p in STATE.paper_positions if p.get("Expiry")}
    snaps = {e: CHAINS.get(e) for e in expiries}
    # Real Dhan quotes, computed BEFORE the lock is taken — spread_margin(live=True)
    # does network I/O and must never run while holding STATE.lock.  Cached for
    # MARGIN_TTL_SEC, and an open book is only a handful of rows.
    with STATE.lock:
        open_now = list(STATE.paper_positions)
    margins = {}
    for p in open_now:
        try:
            margins[p.get("id")] = spread_margin(p, live=True, include_position=False)
        except Exception:
            margins[p.get("id")] = spread_margin(p)

    now = now_ist()
    rows = []
    tot_pnl = tot_credit = tot_risk = tot_delta = tot_theta = tot_margin = 0.0
    unbounded = False
    margin_live = False
    with STATE.lock:
        for p in STATE.paper_positions:
            snap = snaps.get(p.get("Expiry"))
            mtm = mark_position(p, snap)
            tot_pnl += mtm["pnl"]
            tot_credit += _f(p.get("Credit_Received"))
            if p.get("Max_Loss") is None:
                unbounded = True
            tot_risk += _f(p.get("Max_Loss"))
            qty = _f(p.get("Qty"), 65)
            tot_delta += _f(p.get("Net_Delta")) * qty
            tot_theta += _f(p.get("Net_Theta")) * qty
            try:
                dte_now = dte_of(p["Expiry"], now)
            except Exception:
                dte_now = int(_f(p.get("Entry_DTE")))
            mp = _f(p.get("Max_Profit"))
            is_call = p.get("Type") == "CALL"
            mg = margins.get(p.get("id")) or spread_margin(p)
            tot_margin += _f(mg.get("margin"))
            if mg.get("source") == "dhan":
                margin_live = True
            legs = [{"side": "S" if leg_sign(l) < 0 else "B",
                     "type": "CE" if l.get("drv_option_type") == "CALL" else "PE",
                     "strike": _f(l.get("drv_strike_price")),
                     "premium": _f(l.get("entry_fill_price")),
                     "qty": int(_f(l.get("quantity"), 65)),
                     "role": l.get("role"), "sec_id": l.get("security_id"),
                     "mark": _f(l.get("last_mark")), "src": l.get("last_mark_source"),
                     "pnl": round(leg_sign(l) * (_f(l.get("last_mark")) -
                                  _f(l.get("entry_fill_price"))) * _f(l.get("quantity")), 2)}
                    for l in legs_exit_order(p)]
            rows.append({
                "id": p.get("id"), "structure": p.get("Structure", "SINGLE"),
                "label": p.get("Label") or "%d %s" % (_f(p.get("Short_Strike")),
                                                      "CE" if is_call else "PE"),
                "time": p.get("Entry_Time", ""), "expiry": p.get("Expiry", ""),
                "type": p.get("Type", ""),
                "short_strike": p.get("Short_Strike"), "long_strike": p.get("Long_Strike"),
                "width": p.get("Wing_Width"),
                "credit": _f(p.get("Net_Credit")), "now": mtm["value"], "pnl": mtm["pnl"],
                "pnl_pct_max": round(mtm["pnl"] / mp * 100.0, 1) if mp > 0 else None,
                "max_profit": p.get("Max_Profit"), "max_loss": p.get("Max_Loss"),
                "ror": p.get("Return_On_Risk"), "breakeven": p.get("Breakeven"),
                "pop": p.get("POP"), "short_pop": p.get("Short_POP"),
                "net_delta": p.get("Net_Delta"), "net_theta": p.get("Net_Theta"),
                "lots": p.get("Lots", 1), "qty": p.get("Qty"),
                "dte_now": dte_now, "exit_due": dte_now <= exit_dte,
                "margin": mg.get("margin"), "margin_source": mg.get("source"),
                "margin_naked": mg.get("naked_equivalent"),
                "roi_on_margin": mg.get("roi_on_margin"),
                "legs": legs,
                "flags": [x for x in (
                    "STALE" if (snap or {}).get("stale") or not mtm["ok"] else None,
                    "CLAMPED" if mtm["clamped"] else None,
                    "NAKED" if p.get("Structure") == "SINGLE" else None,
                    "DEFERRED" if p.get("Defer_Note") else None) if x],
            })
    return jsonify({
        "rows": rows, "total_pnl": round(tot_pnl, 2),
        "total_credit": round(tot_credit, 2), "total_risk": round(tot_risk, 2),
        "risk_unbounded": unbounded,
        "portfolio_delta": round(tot_delta, 1), "portfolio_theta": round(tot_theta, 1),
        "total_margin": round(tot_margin, 2), "margin_live": margin_live,
        "spot_by_expiry": {e: round(_f((snaps.get(e) or {}).get("spot")), 2)
                           for e in expiries},
        "exit_dte": exit_dte,
        "updated": now.strftime("%H:%M:%S"),
    })


@app.route("/api/positions/exit", methods=["POST"])
def api_positions_exit():
    """Addressed by stable id.  Index addressing raced the background scanner:
    a concurrent auto-exit shifted the list and closed the wrong spread."""
    ids = (request.get_json(force=True, silent=True) or {}).get("ids") or []
    if not ids:
        return jsonify({"error": "no positions selected"}), 400
    n, deferred = do_auto_exit(STATE.filters["exit_dte"], force_ids=ids, reason="MANUAL")
    return jsonify({"ok": True, "exited": n, "deferred": deferred})


@app.route("/api/history")
def api_history():
    rows, total = [], 0.0
    wins = losses = 0
    win_sum = loss_sum = 0.0
    with STATE.lock:
        hist = list(STATE.trade_history)
    for t in hist:
        pnl = t.get("Realized_PnL")
        if pnl is None:
            pnl = (_f(t.get("Entry_Price")) - _f(t.get("Exit_price"))) * _f(t.get("Qty"), 65)
        pnl = round(_f(pnl), 2)
        total += pnl
        if pnl >= 0:
            wins += 1
            win_sum += pnl
        else:
            losses += 1
            loss_sum += pnl
        rows.append({
            "id": t.get("id"), "expiry": t.get("Expiry", ""),
            "label": t.get("Label") or "%s %s" % (t.get("Strike"), t.get("Type")),
            "strike": t.get("Short_Strike") or t.get("Strike"),
            "type": t.get("Type", ""), "structure": t.get("Structure", "SINGLE"),
            "entry_time": t.get("Entry_Time") or t.get("Time", ""),
            "exit_time": t.get("Exit_Time") or t.get("Exit_time", ""),
            "credit": _f(t.get("Net_Credit")), "debit": _f(t.get("Net_Exit_Debit")),
            "qty": t.get("Qty"), "pnl": pnl,
            "reason": t.get("Exit_Reason") or "", "width": t.get("Wing_Width"),
        })
    rows.sort(key=lambda r: str(r["exit_time"]))
    n = len(rows)
    stats = {
        "trades": n,
        "win_rate": round(wins / n * 100.0, 1) if n else 0.0,
        "avg_win": round(win_sum / wins, 2) if wins else 0.0,
        "avg_loss": round(loss_sum / losses, 2) if losses else 0.0,
        "profit_factor": round(win_sum / abs(loss_sum), 2) if loss_sum else None,
    }
    return jsonify({"rows": rows, "total_pnl": round(total, 2), "stats": stats})


def _csv_response(filename, header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(header)
    w.writerows(rows)
    # The BOM is what makes Excel open this as UTF-8 and render the rupee sign
    # and the spread arrows correctly instead of mojibake.
    return Response("﻿" + buf.getvalue(),
                    content_type="text/csv; charset=utf-8",
                    headers={"Content-Disposition": 'attachment; filename="%s"' % filename,
                             "Cache-Control": "no-store"})


def _margin_cols(pos):
    m = spread_margin(pos)
    return [m.get("margin"), m.get("naked_equivalent"), m.get("roi_on_margin")]


def _leg_cols(pos):
    s, w = short_leg(pos) or {}, wing_leg(pos) or {}
    return [s.get("drv_strike_price"), s.get("security_id"),
            s.get("entry_fill_price"), s.get("exit_fill_price"), s.get("exit_price_source"),
            w.get("drv_strike_price") if w else "", w.get("security_id") if w else "",
            w.get("entry_fill_price") if w else "", w.get("exit_fill_price") if w else "",
            w.get("exit_price_source") if w else ""]


TRADE_CSV_HEADER = [
    "Expiry", "Structure", "Strategy", "Type", "Short Strike", "Long Strike", "Wing Width",
    "Lots", "Lot Size", "Qty", "Entered", "Exited", "Exit Reason",
    "Net Credit", "Net Exit Debit", "Credit Received", "Realized PnL",
    "Max Profit", "Max Loss", "Return on Risk %", "Breakeven",
    "Spread POP %", "Short POP %", "Efficiency", "Entry DTE",
    "Margin Blocked (est)", "Margin if Naked (est)", "Return on Margin %",
    "Short Leg Strike", "Short Security ID", "Short Entry", "Short Exit", "Short Exit Source",
    "Wing Leg Strike", "Wing Security ID", "Wing Entry", "Wing Exit", "Wing Exit Source",
]


@app.route("/api/history.csv")
def api_history_csv():
    with STATE.lock:
        hist = list(STATE.trade_history)
    rows = []
    for t in hist:
        pnl = t.get("Realized_PnL")
        if pnl is None:
            pnl = (_f(t.get("Entry_Price")) - _f(t.get("Exit_price"))) * _f(t.get("Qty"), 65)
        rows.append([
            t.get("Expiry"), t.get("Structure"), t.get("Strategy"), t.get("Type"),
            t.get("Short_Strike"), t.get("Long_Strike"), t.get("Wing_Width"),
            t.get("Lots"), t.get("Lot_Size"), t.get("Qty"),
            t.get("Entry_Time") or t.get("Time"), t.get("Exit_Time") or t.get("Exit_time"),
            t.get("Exit_Reason"),
            t.get("Net_Credit"), t.get("Net_Exit_Debit"), t.get("Credit_Received"),
            round(_f(pnl), 2), t.get("Max_Profit"), t.get("Max_Loss"),
            t.get("Return_On_Risk"), t.get("Breakeven"),
            t.get("POP"), t.get("Short_POP"), t.get("Efficiency"), t.get("Entry_DTE"),
        ] + _margin_cols(t) + _leg_cols(t))
    rows.sort(key=lambda r: str(r[11]))
    return _csv_response("nifty_trade_report_%s.csv" % now_ist().strftime("%Y%m%d_%H%M"),
                         TRADE_CSV_HEADER, rows)


@app.route("/api/positions.csv")
def api_positions_csv():
    with STATE.lock:
        expiries = {p.get("Expiry") for p in STATE.paper_positions if p.get("Expiry")}
    snaps = {e: CHAINS.get(e) for e in expiries}
    now = now_ist()
    rows = []
    with STATE.lock:
        for p in STATE.paper_positions:
            mtm = mark_position(p, snaps.get(p.get("Expiry")))
            try:
                dte_now = dte_of(p["Expiry"], now)
            except Exception:
                dte_now = p.get("Entry_DTE")
            rows.append([
                p.get("Expiry"), p.get("Structure"), p.get("Strategy"), p.get("Type"),
                p.get("Short_Strike"), p.get("Long_Strike"), p.get("Wing_Width"),
                p.get("Lots"), p.get("Lot_Size"), p.get("Qty"),
                p.get("Entry_Time"), "", "OPEN",
                p.get("Net_Credit"), mtm["value"], p.get("Credit_Received"),
                mtm["pnl"], p.get("Max_Profit"), p.get("Max_Loss"),
                p.get("Return_On_Risk"), p.get("Breakeven"),
                p.get("POP"), p.get("Short_POP"), p.get("Efficiency"), dte_now,
            ] + _margin_cols(p) + _leg_cols(p))
    return _csv_response("nifty_open_positions_%s.csv" % now_ist().strftime("%Y%m%d_%H%M"),
                         TRADE_CSV_HEADER, rows)


@app.route("/api/history/clear", methods=["POST"])
def api_history_clear():
    ids = set((request.get_json(force=True, silent=True) or {}).get("ids") or [])
    with STATE.lock:
        STATE.trade_history = [t for t in STATE.trade_history if t.get("id") not in ids]
        STATE.save()
    return jsonify({"ok": True})


@app.route("/api/history/wipe", methods=["POST"])
def api_history_wipe():
    with STATE.lock:
        STATE.trade_history = []
        STATE.save()
    log_event("exit", "trade history wiped")
    return jsonify({"ok": True})


@app.route("/api/pnl-series")
def api_pnl_series():
    return jsonify({"series": STATE.pnl_series[-1500:]})


@app.route("/api/events")
def api_events():
    since = int(_f(request.args.get("since"), 0))
    return jsonify({"events": recent_events(since)})


@app.route("/api/token", methods=["GET"])
def api_token_get():
    return jsonify(token_status())


@app.route("/api/token", methods=["POST"])
def api_token_set():
    c = resolve_credentials()
    if c.env_pinned:
        return jsonify({"error": "DHAN_ACCESS_TOKEN is set in the environment and "
                                 "overrides this form. Unset it and restart."}), 409
    body = request.get_json(force=True, silent=True) or {}
    token = (body.get("token") or "").strip().strip('"').replace("\n", "").replace(" ", "")
    if token.lower().startswith("bearer "):
        token = token[7:].strip()
    if len(token) < 40 or token.count(".") != 2:
        return jsonify({"error": "That does not look like a Dhan access token (JWT)."}), 400
    payload, err = decode_jwt_unverified(token)
    if err:
        return jsonify({"error": "Could not read that token: %s" % err}), 400
    fields = {"access_token": token, "token_saved_at": ts_now()}
    cid = (body.get("client_id") or "").strip()
    if cid:
        fields["client_id"] = cid
    elif payload.get("dhanClientId"):
        fields["client_id"] = str(payload["dhanClientId"])
    runtime_write(**fields)
    TOKEN_STATE.mark_ok()
    log_event("token", "new access token saved (%s)" % token_status()["human"])
    if not STATE.expiry_list:
        threading.Thread(target=boot_loop, daemon=True).start()
    return jsonify({"ok": True, "token": token_status()})


@app.route("/api/token/test", methods=["POST"])
def api_token_test():
    return jsonify(test_dhan_connection())


@app.route("/api/exit-check")
def api_exit_check():
    """Alerts on positions actually held, not on the exchange's whole expiry
    calendar — the old tab warned about expiries he had no position in."""
    exit_dte = STATE.filters["exit_dte"]
    now = now_ist()
    alerts = []
    with STATE.lock:
        for p in STATE.paper_positions:
            try:
                dte = dte_of(p["Expiry"], now)
            except Exception:
                continue
            days_until = dte - exit_dte
            if days_until <= 10:
                alerts.append({"id": p.get("id"), "label": p.get("Label"),
                               "expiry": p.get("Expiry"), "dte": dte,
                               "days_until": days_until, "critical": days_until <= 0})
    alerts.sort(key=lambda a: a["days_until"])
    return jsonify({"alerts": alerts, "exit_dte": exit_dte,
                    "open_count": len(STATE.paper_positions)})


INDEX_HTML = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NIFTY Credit Spreads</title>
<style>
:root{--bg:#0b0e14;--panel:#121722;--p2:#171d2b;--bd:#222a3b;--bd2:#2e3850;
 --tx:#cbd5e1;--br:#f1f5f9;--mu:#7c8aa3;--m2:#56627a;--ac:#38bdf8;--gn:#22c55e;--rd:#ef4444;--or:#f59e0b}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);font:14px/1.5 'Segoe UI',system-ui,sans-serif}
.top{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:14px 20px 10px}
.top h1{font-size:18px;margin:0;color:var(--br)}
.top .sub{color:var(--mu);font-size:12px;margin:0}
.sp{flex:1}
.pill{padding:4px 12px;border-radius:999px;font-size:12px;background:var(--p2);color:var(--mu);white-space:nowrap}
.pill.on{background:rgba(34,197,94,.14);color:#86efac}.pill.off{background:rgba(239,68,68,.14);color:#fca5a5}
nav.tabs{display:flex;gap:0;border-bottom:1px solid var(--bd);padding:0 20px;overflow-x:auto}
nav.tabs button{background:none;border:0;border-bottom:2px solid transparent;color:var(--mu);padding:12px 18px;
 font:14px ui-monospace,Consolas,monospace;cursor:pointer;white-space:nowrap;border-radius:0}
nav.tabs button:hover{color:var(--tx)}
nav.tabs button.on{color:var(--br);border-bottom-color:var(--ac);background:var(--panel)}
.statusline{padding:8px 20px;font-size:12px;color:var(--mu);border-bottom:1px solid var(--bd);font-family:ui-monospace,Consolas,monospace}
main{padding:18px 20px 40px;max-width:1500px}
.panel{display:none}.panel.on{display:block}
button{font:inherit;border:0;border-radius:8px;padding:9px 16px;cursor:pointer;background:var(--p2);color:var(--tx)}
button:hover{filter:brightness(1.15)} button:disabled{opacity:.45;cursor:default}
button.sm,a.sm{padding:6px 12px;font-size:12px}
.go{background:var(--gn);color:#04210f;font-weight:600}
.stop{background:var(--rd);color:#fff}
.ghost{background:transparent;border:1px solid var(--bd2)}
a.btn{display:inline-block;text-decoration:none;border-radius:8px;background:rgba(34,197,94,.14);color:#86efac;border:1px solid rgba(34,197,94,.35)}
.danger{background:rgba(239,68,68,.12);color:#fca5a5;border:1px solid rgba(239,68,68,.35)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px;margin-bottom:16px}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(460px,1fr));gap:14px;margin-bottom:16px}
.card{background:var(--panel);border:1px solid var(--bd);border-radius:12px;padding:16px}
.card h3{margin:0 0 10px;font-size:11px;letter-spacing:.12em;color:var(--mu);font-weight:700}
.k{font-size:10px;letter-spacing:.12em;color:var(--mu);font-weight:700}
.v{font-size:22px;color:var(--br);margin-top:4px;font-variant-numeric:tabular-nums}
.g{color:#4ade80}.r{color:#f87171}
.hint{font-size:12px;color:var(--mu)}
.empty{padding:22px;text-align:center;color:var(--mu);font-size:13px}
.tw{overflow-x:auto}
.scroll{max-height:62vh;overflow:auto}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;color:var(--mu);font-size:11px;letter-spacing:.06em;padding:8px;border-bottom:1px solid var(--bd);white-space:nowrap;position:sticky;top:0;background:var(--panel)}
td{padding:7px 8px;border-bottom:1px solid var(--bd);font-variant-numeric:tabular-nums;white-space:nowrap}
td.wrap{white-space:normal}
tr:last-child td{border-bottom:0}
.tag{display:inline-block;padding:1px 8px;border-radius:6px;font-size:11px;font-weight:700}
.ce{background:rgba(34,197,94,.14);color:#86efac}.pe{background:rgba(239,68,68,.14);color:#fca5a5}
.bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.big{font-size:20px;font-weight:700;font-family:ui-monospace,Consolas,monospace}
.f{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.fl{display:flex;flex-direction:column;gap:5px}
label{font-size:12px;color:var(--mu)}
input,select{background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:8px 11px;color:var(--br);font:inherit}
input:disabled{opacity:.45}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{display:flex;align-items:center;gap:7px;background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:8px 12px;cursor:pointer;font-size:13px;color:var(--tx);user-select:none}
.chip input{margin:0}.chip.on{border-color:var(--ac);background:rgba(56,189,248,.1);color:var(--br)}
.chip.dis{opacity:.4;cursor:not-allowed}.chip small{color:var(--mu)}
.grp{margin-bottom:16px}.grp>label{display:block;margin-bottom:6px}
.mode{display:flex;flex-direction:column;gap:10px}
.mode .row{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:13px}
.note{background:rgba(245,158,11,.1);border-left:3px solid var(--or);padding:10px 14px;border-radius:8px;font-size:13px;margin-bottom:14px}
.info{background:rgba(56,189,248,.08);border-left-color:var(--ac)}
svg text.ax{fill:var(--m2);font:11px ui-monospace,Consolas,monospace}
svg line.grid{stroke:var(--bd);stroke-width:1}
svg line.zero{stroke:var(--bd2);stroke-dasharray:4 4}
svg circle.dot{fill:var(--panel);stroke-width:2}
.mono{font-family:ui-monospace,Consolas,monospace;font-size:12px}
/* ---- credit-spreads additions, same tokens ---- */
[hidden]{display:none!important}
.pill.wait{background:rgba(245,158,11,.14);color:#fcd34d}
.o{color:#fbbf24}
.note.crit{background:rgba(239,68,68,.1);border-left-color:var(--rd)}
.note.ok{background:rgba(34,197,94,.08);border-left-color:var(--gn)}
.note.plain{background:var(--p2);border-left-color:var(--bd2)}
.hrow{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0 0 10px}
.hrow h3{margin:0}
.ghost.on{border-color:var(--ac);background:rgba(56,189,248,.1);color:var(--br)}
button.okb{background:rgba(34,197,94,.14);color:#86efac;border:1px solid rgba(34,197,94,.35)}
a.btn.danger{background:rgba(239,68,68,.12);color:#fca5a5;border-color:rgba(239,68,68,.35)}
select.sm{padding:5px 8px;font-size:12px}
textarea{background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:8px 11px;color:var(--br);font:12px ui-monospace,Consolas,monospace;width:100%;resize:vertical}
.split{display:grid;grid-template-columns:minmax(0,2fr) minmax(320px,1fr);gap:14px;margin-bottom:16px}
.mini{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-top:12px}
.mini .card{padding:10px 12px;border-radius:10px}.mini .v{font-size:16px}
.chart-host{position:relative;min-width:0}
.viz-tip{position:absolute;z-index:20;pointer-events:none;background:rgba(11,14,20,.96);border:1px solid var(--bd2);border-radius:8px;
 padding:7px 10px;font:12px/1.55 ui-monospace,Consolas,monospace;color:var(--tx);white-space:nowrap;box-shadow:0 6px 18px rgba(0,0,0,.5)}
.viz-tip b{display:block;color:var(--br);margin-bottom:3px;font-weight:600}
.viz-tip i{display:inline-block;width:7px;height:7px;border-radius:2px;margin-right:6px;font-style:normal}
.viz-tip u{float:right;margin-left:18px;text-decoration:none;color:var(--br)}
tr.clickable{cursor:pointer}
tr.clickable:hover td{background:var(--p2)}
tr.sel td{background:rgba(56,189,248,.08)}
tr.legrow td{background:var(--bg);color:var(--mu);font:12px/1.7 ui-monospace,Consolas,monospace;white-space:normal;padding:8px 14px}
.badge{display:inline-block;font-size:10px;padding:0 6px;border-radius:6px;margin-left:5px;border:1px solid var(--bd2);color:var(--mu);font-weight:700}
.badge.warn{color:#fcd34d;border-color:rgba(245,158,11,.5)}.badge.bad{color:#fca5a5;border-color:rgba(239,68,68,.5)}
.rbar{display:inline-block;vertical-align:middle;width:50px;height:8px;background:var(--bd);border-radius:4px;overflow:hidden;margin-right:6px}
.rbar i{display:block;height:100%;background:var(--ac)}
.pop-hi{color:#4ade80}.pop-mid{color:#fbbf24}.pop-lo{color:#f87171}
details.chain>summary{cursor:pointer;font-size:11px;letter-spacing:.12em;color:var(--mu);font-weight:700;list-style:none}
details.chain>summary::-webkit-details-marker{display:none}
details.chain>summary:hover{color:var(--tx)}
.spin{display:inline-block;width:15px;height:15px;border:2px solid var(--bd2);border-top-color:var(--ac);border-radius:50%;animation:spin .7s linear infinite;vertical-align:middle}
@keyframes spin{to{transform:rotate(360deg)}}
.tag.kind{background:var(--p2);color:var(--tx)}
.tag.k-error,.tag.k-api_error{background:rgba(239,68,68,.14);color:#fca5a5}
.tag.k-token,.tag.k-margin{background:rgba(245,158,11,.14);color:#fcd34d}
.tag.k-deploy,.tag.k-scan{background:rgba(34,197,94,.14);color:#86efac}
.tag.k-exit{background:rgba(244,114,182,.14);color:#f9a8d4}
@media(max-width:760px){.split{grid-template-columns:1fr}}
</style></head><body>

<div class="top">
  <div><h1>NIFTY Credit Spreads</h1>
    <p class="sub">Sells defined-risk credit spreads on the NIFTY option chain - screener, margin check and a hard DTE exit - paper trading</p></div>
  <div class="sp"></div>
  <span class="pill" id="p_mkt">-</span>
  <span class="pill" id="p_tok">-</span>
  <span class="pill" id="p_run">-</span>
  <button class="go" id="b_start">Start</button>
  <button class="stop" id="b_stop">Stop</button>
</div>
<nav class="tabs" id="tabs">
  <button data-tab="dashboard" class="on">Dashboard</button>
  <button data-tab="screener">Screener</button>
  <button data-tab="positions">Positions</button>
  <button data-tab="report">Trade Report</button>
  <button data-tab="exitcheck">Exit Check</button>
  <button data-tab="activity">Activity</button>
  <button data-tab="settings">Settings</button>
</nav>
<div class="statusline" id="statusline">Loading...</div>

<main>
<!-- DASHBOARD -->
<section class="panel on" id="p-dashboard">
  <div class="note">Paper trading only - nothing is sent to the broker. It starts scanning by itself when launched from NIFTY Trader and scans every 60 s from 09:15 to 15:30 IST. Stop pauses the scanner: no new spreads and no automatic DTE exits until you press Start. Exits from the Positions tab always work.</div>
  <div id="tokenbanner"></div>
  <div id="vixbanner"></div>
  <div class="grid">
    <div class="card"><div class="k">SCANNER</div><div class="v" id="d_run">-</div><div class="hint" id="d_run2">-</div></div>
    <div class="card"><div class="k">OPEN SPREADS</div><div class="v" id="d_open">-</div><div class="hint" id="d_open2">-</div></div>
    <div class="card"><div class="k">LAST SCAN</div><div class="v" id="d_scan">-</div><div class="hint" id="d_scan2">-</div></div>
    <div class="card"><div class="k">EXPIRIES LOADED</div><div class="v" id="d_exp">-</div><div class="hint" id="d_exp2">-</div></div>
  </div>
  <div class="card" style="margin-bottom:16px">
    <h3>OPTION CHAIN</h3>
    <div class="bar" style="margin-bottom:0">
      <label for="expiry_combo">Expiry</label>
      <select id="expiry_combo"><option value="">No expiries yet</option></select>
      <button class="go sm" id="btn_load">Load chain</button>
      <span class="spin" id="dash_spinner" hidden></span>
      <div class="sp"></div>
      <span class="hint" id="chain_note">Pick an expiry and press Load chain.</span>
    </div>
  </div>
  <div class="grid">
    <div class="card"><div class="k">NIFTY SPOT</div><div class="v" id="m_spot">-</div></div>
    <div class="card"><div class="k">SYNTHETIC FUTURE</div><div class="v" id="m_synth">-</div></div>
    <div class="card"><div class="k">ATM STRIKE</div><div class="v" id="m_atm">-</div></div>
    <div class="card"><div class="k">DAYS TO EXPIRY</div><div class="v" id="m_dte">-</div></div>
  </div>
  <div class="two">
    <div class="card">
      <div class="hrow"><h3>OPEN INTEREST BY STRIKE</h3><div class="sp"></div>
        <button class="sm ghost on" id="oi_mode_oi">OI</button>
        <button class="sm ghost" id="oi_mode_doi">Change</button>
        <select class="sm" id="zoom" title="Strikes shown in both charts">
          <option value="0.05">&plusmn;5%</option>
          <option value="0.1" selected>&plusmn;10%</option>
          <option value="0.2">&plusmn;20%</option>
          <option value="9">All strikes</option>
        </select></div>
      <div class="chart-host" id="c_oi"></div>
    </div>
    <div class="card"><h3>IMPLIED VOLATILITY SKEW</h3><div class="chart-host" id="c_smile"></div></div>
  </div>
  <details class="card chain" style="margin-bottom:16px">
    <summary>FULL OPTION CHAIN TABLE (CLICK TO EXPAND)</summary>
    <div class="tw scroll" style="margin-top:10px">
      <table>
        <thead><tr>
          <th>CE POP</th><th>CE Theta</th><th>CE Gamma</th><th>CE Delta</th><th>CE IV</th>
          <th>CE OI</th><th>CE dOI</th><th>CE LTP</th>
          <th>STRIKE</th>
          <th>PE LTP</th><th>PE dOI</th><th>PE OI</th><th>PE IV</th>
          <th>PE Delta</th><th>PE Gamma</th><th>PE Theta</th><th>PE POP</th>
        </tr></thead>
        <tbody id="chain_body"><tr><td colspan="17" class="empty">Load a chain to fill this table.</td></tr></tbody>
      </table>
    </div>
  </details>
  <div class="card"><h3>RECENT ACTIVITY</h3><div class="tw" id="d_ev"></div></div>
</section>

<!-- SCREENER -->
<section class="panel" id="p-screener">
  <div class="bar">
    <button class="go sm" id="btn_screener_refresh">Find spreads</button>
    <button class="sm okb" id="btn_screener_deploy">Deploy selected</button>
    <span class="spin" id="screener_spinner" hidden></span>
    <div class="sp"></div>
    <span class="hint" id="match_lbl">Press Find spreads to scan with the saved filters.</span>
  </div>
  <div class="hint" id="reject_note" style="margin-bottom:10px"></div>
  <div class="split">
    <div class="card scroll"><div id="screener_wrap"><div class="empty">No scan yet.</div></div></div>
    <div class="card">
      <div class="hrow"><h3>EXPIRY PAYOFF</h3><div class="sp"></div><span class="hint" id="payoff_lbl">click a row</span></div>
      <div class="chart-host" id="c_screen_payoff"></div>
      <div class="mini" id="screen_stats"></div>
    </div>
  </div>
  <p class="hint">The screener uses the filters saved on the Settings tab. Margin in the table is a local SPAN + ELM estimate; clicking a row asks Dhan for a live quote for that one spread.</p>
</section>

<!-- POSITIONS -->
<section class="panel" id="p-positions">
  <div class="grid" id="pos_strip"></div>
  <div class="bar">
    <button class="ghost sm" id="btn_pos_refresh">Refresh prices</button>
    <button class="danger sm" id="btn_pos_exit">Exit selected</button>
    <label class="chip" style="padding:6px 10px"><input type="checkbox" id="pos_check_all"> Select all</label>
    <span class="spin" id="pos_spinner" hidden></span>
    <div class="sp"></div>
    <span class="hint mono" id="pos_updated">-</span>
    <a href="/api/positions.csv" class="btn sm" download>Download for Excel</a>
  </div>
  <div class="chips" id="exp_chips" style="margin-bottom:14px"></div>
  <div class="two">
    <div class="card"><div class="hrow"><h3>BOOK PAYOFF AT EXPIRY</h3><div class="sp"></div><span class="hint" id="payoff_exp_lbl"></span></div>
      <div class="chart-host" id="c_book"></div></div>
    <div class="card"><h3>P&amp;L BY POSITION</h3><div class="chart-host" id="c_posbars"></div></div>
  </div>
  <div class="card tw" id="pos_table"><div class="empty">Loading...</div></div>
  <p class="hint">Click a row to see its legs. Exit selected closes both legs together at live prices; a position with no usable price is left open rather than booked at a made-up price. Prices refresh every 3 minutes while this tab is open.</p>
</section>

<!-- TRADE REPORT -->
<section class="panel" id="p-report">
  <div class="bar">
    <span class="big" id="report_pnl">Realized P&amp;L: -</span><div class="sp"></div>
    <a href="/api/history.csv" class="btn sm" download>Download for Excel</a>
    <button class="sm danger" id="btn_report_clear">Clear Selected</button>
    <button class="sm danger" id="btn_report_wipe">Wipe All</button>
  </div>
  <div class="grid" id="report_stats"></div>
  <div class="card" style="margin-bottom:16px"><h3>CUMULATIVE REALIZED P&amp;L</h3><div id="c_equity"></div></div>
  <div class="card scroll"><div id="report_table"></div></div>
  <p class="hint">Clear Selected and Wipe All permanently remove trades from this strategy's trade book - they cannot be brought back from this screen. Use Download for Excel first if you want a copy.</p>
</section>

<!-- EXIT CHECK -->
<section class="panel" id="p-exitcheck">
  <div class="bar">
    <span class="hint">Open spreads approaching the hard exit rule (Settings - Hard exit DTE). While the scanner is running it closes them automatically when they reach the rule.</span>
    <div class="sp"></div>
    <button class="ghost sm" id="btn_exitcheck_refresh">Refresh</button>
  </div>
  <div class="card" style="margin-bottom:16px"><h3>DAYS TO EXPIRY BY POSITION</h3><div class="chart-host" id="c_ladder"></div></div>
  <div id="exitcheck_list"></div>
</section>

<!-- ACTIVITY -->
<section class="panel" id="p-activity">
  <div class="bar">
    <select id="a_kind"><option value="">Every kind</option></select>
    <button class="sm ghost" id="btn_events_refresh">Refresh</button>
    <span class="hint">The latest 250 events since this strategy process started - they are not kept across restarts.</span>
  </div>
  <div class="card" style="margin-bottom:16px"><h3>UNREALIZED P&amp;L OVER TIME</h3><div class="chart-host" id="c_pnlseries"></div></div>
  <div class="card scroll"><div id="events_wrap"></div></div>
</section>

<!-- SETTINGS -->
<section class="panel" id="p-settings">
  <div id="s_form">
    <div class="card">
      <h3>STRATEGY FILTERS</h3>
      <div class="note info" id="s_lock" hidden>The scanner is running. Filters can only change while it is stopped, so Save settings stops it, saves the filters and starts it again.</div>
      <div class="f">
        <div class="fl"><label for="f_min_eff">Min efficiency (short leg theta / gamma)</label><input id="f_min_eff" type="number" min="0" max="200" step="1"></div>
        <div class="fl"><label for="f_min_pop">Min POP % (short leg)</label><input id="f_min_pop" type="number" min="0" max="100" step="1"></div>
        <div class="fl"><label for="f_dte_lo">Entry DTE from (days)</label><input id="f_dte_lo" type="number" min="0" max="400" step="1"></div>
        <div class="fl"><label for="f_dte_hi">Entry DTE to (days)</label><input id="f_dte_hi" type="number" min="0" max="400" step="1"></div>
        <div class="fl"><label for="f_ltp_lo">Short leg LTP from (Rs)</label><input id="f_ltp_lo" type="number" min="0" max="2000" step="1"></div>
        <div class="fl"><label for="f_ltp_hi">Short leg LTP to (Rs)</label><input id="f_ltp_hi" type="number" min="0" max="2000" step="1"></div>
        <div class="fl"><label for="f_wing_width">Hedge wing width (points)</label><input id="f_wing_width" type="number" min="50" max="2000" step="50"></div>
        <div class="fl"><label for="f_lots">Lots per spread</label><input id="f_lots" type="number" min="1" max="50" step="1"></div>
        <div class="fl"><label for="f_exit_dte">Hard exit DTE (days)</label><input id="f_exit_dte" type="number" min="1" max="200" step="1"></div>
      </div>
      <h3 style="margin-top:18px">EXTRA SPREAD FILTERS (0 = OFF)</h3>
      <div class="f">
        <div class="fl"><label for="f_min_credit">Min net credit (Rs per share)</label><input id="f_min_credit" type="number" min="0" step="0.5"></div>
        <div class="fl"><label for="f_min_ror">Min return on risk (%)</label><input id="f_min_ror" type="number" min="0" step="0.5"></div>
        <div class="fl"><label for="f_min_spread_pop">Min spread POP (%)</label><input id="f_min_spread_pop" type="number" min="0" max="100" step="1"></div>
      </div>
      <p class="hint" style="margin-bottom:0">Each spread sells strike K and buys the wing at K + width (CE) or K - width (PE). The screener looks at strikes on the 500-point grid, in expiries inside the entry DTE range, whose short leg passes the LTP, POP and efficiency limits. Open spreads are closed once their days to expiry reach the hard exit DTE.</p>
    </div>
    <div class="card" style="margin-top:14px">
      <h3>SCANNER</h3>
      <label class="chip" id="chip_force" style="display:inline-flex"><input type="checkbox" id="force_scan"> Ignore market hours (scan around the clock)</label>
      <p class="hint">Normally the scanner only runs 09:15-15:30 IST on weekdays. Off-hours it makes no broker calls at all, which keeps your token and rate limit intact.</p>
      <p class="hint" id="market_note" style="margin-bottom:0"></p>
    </div>
    <div class="bar" style="margin:16px 0 0">
      <button class="go" id="b_save">Save settings</button>
      <button class="ghost" id="b_revert">Discard changes</button>
      <span class="hint" id="s_saved"></span>
    </div>
  </div>

  <div class="card" style="margin-top:14px">
    <h3>BROKER</h3>
    <div id="tok_banner"></div>
    <div class="grid" style="margin-bottom:8px">
      <div><div class="k">STATUS</div><div class="v" id="tok_human" style="font-size:16px">-</div></div>
      <div><div class="k">SOURCE</div><div class="v" id="tok_source" style="font-size:16px">-</div></div>
      <div><div class="k">CLIENT ID</div><div class="v" id="tok_client" style="font-size:16px">-</div></div>
    </div>
    <div class="hint mono" id="tok_masked"></div>
    <p class="hint" id="tok_hub" hidden>Set in NIFTY Trader's Broker token screen. It reaches this strategy as the DHAN_ACCESS_TOKEN environment variable, which overrides any token saved here, and this strategy restarts with a new token automatically.</p>
    <div id="tok_form" hidden>
      <div class="f" style="margin-top:12px">
        <div class="fl" style="grid-column:1/-1"><label for="tok_input">Paste a fresh access token</label>
          <textarea id="tok_input" rows="4" placeholder="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9..."></textarea></div>
        <div class="fl"><label for="tok_client_input">Client ID (optional - read from the token if blank)</label>
          <input type="text" id="tok_client_input" placeholder="1100150851"></div>
      </div>
      <p class="hint">The token is stored on the machine running this strategy, so the bot keeps running after you close this page. Dhan tokens generated from the web portal last 24 hours; tokens generated from an API key + secret can last up to 30 days.</p>
    </div>
    <div class="bar" style="margin:10px 0 0">
      <button class="go sm" id="btn_tok_save" hidden>Save token</button>
      <button class="ghost sm" id="btn_tok_test">Test connection</button>
      <span class="spin" id="tok_spinner" hidden></span>
      <span class="hint" id="tok_result"></span>
    </div>
  </div>

  <div class="card" style="margin-top:14px">
    <h3>SESSION</h3>
    <div class="bar" style="margin:0">
      <a href="/logout" class="btn sm danger">Log out</a>
      <span class="hint" id="auth_note"></span>
    </div>
  </div>
</section>
</main>

<script>
/* ==========================================================================
   Viz — dependency-free inline-SVG charting for the Nifty spread dashboard.
   No CDN, no fonts, no images.
   ========================================================================== */
const Viz = (function () {
  const NS = 'http://www.w3.org/2000/svg';
  const FONT = "ui-monospace,Consolas,monospace";
  /* the shared NIFTY Trader tokens: --bd, --bd2, --tx, --mu, --ac, --gn, --rd, --or, --panel */
  const P = {
    grid: '#222a3b', axis: '#2e3850', text: '#cbd5e1', muted: '#7c8aa3',
    accent: '#38bdf8', green: '#22c55e', red: '#ef4444', orange: '#f59e0b',
    pink: '#f472b6', purple: '#a78bfa', panel: '#121722'
  };
  let UID = 0;

  /* ---------- micro DOM ---------- */
  function el(tag, attrs, parent) {
    const n = document.createElementNS(NS, tag);
    if (attrs) for (const k in attrs) {
      const v = attrs[k];
      if (v !== null && v !== undefined && v !== false) n.setAttribute(k, v);
    }
    if (parent) parent.appendChild(n);
    return n;
  }
  const R = v => Math.round(v * 10) / 10;

  /* ---------- formatting (Indian units) ---------- */
  const fmt = {
    compact(v) {
      const a = Math.abs(v);
      if (a >= 1e7) return (v / 1e7).toFixed(a >= 1e8 ? 0 : 1) + 'Cr';
      if (a >= 1e5) return (v / 1e5).toFixed(a >= 1e6 ? 0 : 1) + 'L';
      if (a >= 1e3) return (v / 1e3).toFixed(a >= 1e4 ? 0 : 1) + 'k';
      return String(Math.round(v * 100) / 100);
    },
    money: v => (v < 0 ? '-₹' : '₹') + fmt.compact(Math.abs(v)),
    rupee: v => (v < 0 ? '-₹' : '₹') + Math.abs(Math.round(v)).toLocaleString('en-IN'),
    int: v => Math.round(v || 0).toLocaleString('en-IN'),
    strike: v => String(Math.round(v)),
    pct: v => (Math.round(v * 10) / 10) + '%'
  };

  /* ---------- scales ---------- */
  function linear(d0, d1, r0, r1) {
    if (!isFinite(d0) || !isFinite(d1)) { d0 = 0; d1 = 1; }
    if (d0 === d1) { d0 -= 0.5; d1 += 0.5; }
    const k = (r1 - r0) / (d1 - d0);
    const f = v => r0 + (v - d0) * k;
    f.invert = px => d0 + (px - r0) / k;
    f.domain = [d0, d1]; f.range = [r0, r1]; f.kind = 'linear';
    return f;
  }
  function band(n, w, padFrac) {
    const step = w / Math.max(1, n);
    const inner = Math.max(1, step * (1 - (padFrac == null ? 0.28 : padFrac)));
    const f = i => step * i + step / 2;
    f.invert = px => Math.max(0, Math.min(n - 1, Math.floor(px / step)));
    f.width = inner; f.step = step; f.n = n; f.kind = 'band';
    f.domain = [0, n - 1]; f.range = [0, w];
    return f;
  }
  function ticks(min, max, count) {
    if (!isFinite(min) || !isFinite(max) || min === max) return [min || 0];
    count = Math.max(2, count || 4);
    const raw = (max - min) / count;
    const mag = Math.pow(10, Math.floor(Math.log10(Math.abs(raw) || 1)));
    const n = raw / mag;
    const step = (n >= 7.07 ? 10 : n >= 3.53 ? 5 : n >= 2.24 ? 2.5 : n >= 1.41 ? 2 : 1) * mag;
    const out = [];
    for (let v = Math.ceil(min / step) * step; v <= max + step * 1e-9; v += step) {
      out.push(Math.abs(v) < step * 1e-9 ? 0 : +v.toPrecision(12));
    }
    return out;
  }

  /* ---------- payoff math (works for any leg set) ---------- */
  function payoffAt(legs, S) {
    let v = 0;
    for (let i = 0; i < legs.length; i++) {
      const L = legs[i];
      const isPut = L.type === 'PE' || L.type === 'PUT';
      const intr = isPut ? Math.max(0, L.strike - S) : Math.max(0, S - L.strike);
      const sgn = (L.side === 'S' || L.side === 'SELL' || L.side === 'SHORT') ? -1 : 1;
      v += sgn * (intr - (L.premium || 0)) * (L.qty || 1);
    }
    return v;
  }
  function payoffCurve(legs, x0, x1) {
    const xs = [x0, x1];
    legs.forEach(L => { if (L.strike > x0 && L.strike < x1) xs.push(L.strike); });
    xs.sort((a, b) => a - b);
    const knots = []; let prev = null;
    for (const s of xs) {
      if (prev !== null && Math.abs(s - prev) < 1e-9) continue;
      prev = s; knots.push([s, payoffAt(legs, s)]);
    }
    const pts = [], be = [];
    for (let i = 0; i < knots.length; i++) {
      if (i) {
        const a = knots[i - 1], b = knots[i];
        if ((a[1] < 0 && b[1] > 0) || (a[1] > 0 && b[1] < 0)) {
          const t = -a[1] / (b[1] - a[1]);
          const bx = a[0] + t * (b[0] - a[0]);
          be.push(bx); pts.push([bx, 0]);
        }
      }
      pts.push(knots[i]);
      if (Math.abs(knots[i][1]) < 1e-9) be.push(knots[i][0]);
    }
    let mx = -Infinity, mn = Infinity;
    pts.forEach(p => { if (p[1] > mx) mx = p[1]; if (p[1] < mn) mn = p[1]; });
    return { pts, be, max: mx, min: mn };
  }

  /* ---------- persistent plot bound to a host div ---------- */
  function plot(host, cfg) {
    if (host.__viz) { if (cfg) Object.assign(host.__viz.cfg, cfg); return host.__viz; }
    cfg = Object.assign({ height: 240, margin: { t: 16, r: 14, b: 26, l: 48 } }, cfg || {});
    if (getComputedStyle(host).position === 'static') host.style.position = 'relative';

    const svg = el('svg', { width: '100%', height: cfg.height, 'font-family': FONT });
    svg.style.display = 'block';
    svg.style.touchAction = 'pan-y';
    host.appendChild(svg);

    const tip = document.createElement('div');
    tip.className = 'viz-tip'; tip.hidden = true;
    host.appendChild(tip);

    const api = {
      host, svg, tip, cfg, _key: undefined, _w: 0, _draw: null,
      /* render(key, draw) — no-ops when key and width are unchanged */
      render(key, draw) {
        if (draw === undefined) { draw = key; key = undefined; }
        const w = host.clientWidth || 0;
        if (key !== undefined && key === api._key && Math.abs(w - api._w) < 2 && api._draw) return false;
        api._key = key; api._draw = draw; api.paint(); return true;
      },
      invalidate() { api._key = undefined; },
      paint() {
        /* host is inside a display:none tab-panel → clientWidth 0. Don't paint at a
           bogus width; forget the key so the next render() after the tab is shown
           repaints at the real size. */
        if (!host.clientWidth) { api._key = undefined; api._w = 0; return; }
        const m = api.cfg.margin;
        const W = Math.max(200, host.clientWidth), H = api.cfg.height;
        api._w = W;
        svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
        svg.setAttribute('height', H);
        const g = el('g', { transform: 'translate(' + m.l + ',' + m.t + ')' }); // detached
        const f = makeFrame(api, g, W - m.l - m.r, H - m.t - m.b);
        try { if (api._draw) api._draw(f); }
        catch (e) { f.empty('chart error'); if (window.console) console.error(e); }
        f._finish();
        while (svg.firstChild) svg.removeChild(svg.firstChild);
        svg.appendChild(g);                                   // one reflow, not N
        tip.hidden = true;
      }
    };
    host.__viz = api;

    if (window.ResizeObserver) {
      let raf = 0;
      new ResizeObserver(() => {
        const w = host.clientWidth || 0;
        if (!api._draw || Math.abs(w - api._w) < 8 || raf) return;
        raf = requestAnimationFrame(() => { raf = 0; api.paint(); });
      }).observe(host);
    }
    return api;
  }

  /* ---------- per-paint drawing frame ---------- */
  function makeFrame(api, g, w, h) {
    const f = { g, w, h, svg: api.svg, x: null, y: null, narrow: w < 420, _hover: null };
    f.add = (tag, attrs, parent) => el(tag, attrs, parent || g);

    /* scales */
    f.xLinear = (a, b, pad) => { const p = (b - a) * (pad || 0); f.x = linear(a - p, b + p, 0, w); return f.x; };
    f.yLinear = (a, b, pad) => { const p = (b - a) * (pad || 0); f.y = linear(a - p, b + p, h, 0); return f.y; };
    f.xBand = (n, pad) => { f.x = band(n, w, pad); return f.x; };
    f.yFrom = (vals, o) => {
      o = o || {};
      let lo = Infinity, hi = -Infinity;
      for (let i = 0; i < vals.length; i++) {
        const v = vals[i];
        if (v == null || !isFinite(v)) continue;
        if (v < lo) lo = v; if (v > hi) hi = v;
      }
      if (lo === Infinity) { lo = 0; hi = 1; }
      if (o.zero !== false) { lo = Math.min(lo, 0); hi = Math.max(hi, 0); }
      if (lo === hi) hi = lo + 1;
      const pad = (hi - lo) * (o.pad == null ? 0.12 : o.pad);
      return f.yLinear(lo - pad, hi + pad);
    };

    /* grid + axes */
    f.grid = o => {
      o = o || {};
      if (f.y) for (const t of ticks(f.y.domain[0], f.y.domain[1], o.yCount || (h < 170 ? 3 : 4))) {
        const py = R(f.y(t)); if (py < -0.5 || py > h + 0.5) continue;
        el('line', { x1: 0, x2: w, y1: py, y2: py, stroke: P.grid, 'stroke-width': 1, 'shape-rendering': 'crispEdges' }, g);
      }
      if (o.x && f.x && f.x.kind === 'linear') {
        for (const t of ticks(f.x.domain[0], f.x.domain[1], o.xCount || (f.narrow ? 3 : 5))) {
          const px = R(f.x(t)); if (px < -0.5 || px > w + 0.5) continue;
          el('line', { x1: px, x2: px, y1: 0, y2: h, stroke: P.grid, 'stroke-width': 1, 'shape-rendering': 'crispEdges' }, g);
        }
      }
      el('line', { x1: 0, x2: w, y1: h, y2: h, stroke: P.axis, 'stroke-width': 1, 'shape-rendering': 'crispEdges' }, g);
      return f;
    };
    f.axisY = (format, count) => {
      for (const t of ticks(f.y.domain[0], f.y.domain[1], count || (h < 170 ? 3 : 4))) {
        const py = f.y(t); if (py < -0.5 || py > h + 0.5) continue;
        el('text', { x: -8, y: R(py) + 3.5, fill: P.muted, 'font-size': 10, 'text-anchor': 'end' }, g)
          .textContent = (format || fmt.compact)(t);
      }
      return f;
    };
    f.axisX = (format, count) => {
      for (const t of ticks(f.x.domain[0], f.x.domain[1], count || (f.narrow ? 3 : 5))) {
        const px = f.x(t); if (px < -0.5 || px > w + 0.5) continue;
        el('text', { x: R(px), y: h + 15, fill: P.muted, 'font-size': 10, 'text-anchor': 'middle' }, g)
          .textContent = (format || fmt.compact)(t);
      }
      return f;
    };
    f.axisCats = (labels, format) => {
      const every = Math.max(1, Math.ceil(labels.length / (f.narrow ? 4 : 9)));
      for (let i = 0; i < labels.length; i++) {
        if (i % every) continue;
        el('text', { x: R(f.x(i)), y: h + 15, fill: P.muted, 'font-size': 10, 'text-anchor': 'middle' }, g)
          .textContent = format ? format(labels[i], i) : String(labels[i]);
      }
      return f;
    };

    /* marks */
    function dOf(pts, step) {
      let d = '';
      for (let i = 0; i < pts.length; i++) {
        const x = R(pts[i][0]), y = R(pts[i][1]);
        if (!i) d = 'M' + x + ' ' + y;
        else if (step) d += 'H' + x + 'V' + y;
        else d += 'L' + x + ' ' + y;
      }
      return d;
    }
    f.px = pts => pts.map(p => [f.x(p[0]), f.y(p[1])]);
    f.line = (pts, o) => {
      o = o || {};
      return el('path', {
        d: dOf(o.raw ? pts : f.px(pts), o.step), fill: 'none', stroke: o.color || P.accent,
        'stroke-width': o.width || 1.6, 'stroke-linejoin': 'round', 'stroke-linecap': 'round',
        opacity: o.opacity, 'stroke-dasharray': o.dash
      }, g);
    };
    f.area = (pts, o) => {
      o = o || {};
      const p = o.raw ? pts : f.px(pts);
      if (p.length < 2) return null;
      const y0 = R(f.y(o.base == null ? 0 : o.base));
      const d = dOf(p, o.step) + 'L' + R(p[p.length - 1][0]) + ' ' + y0 + 'L' + R(p[0][0]) + ' ' + y0 + 'Z';
      return el('path', { d, fill: o.color || P.accent, opacity: o.opacity == null ? 0.14 : o.opacity, stroke: 'none' }, g);
    };
    /* bars: ONE <path> per colour — 200 bars = 2 DOM nodes */
    f.bars = (values, o) => {
      o = o || {};
      const bw = o.width || (f.x.width || 6);
      const y0 = R(f.y(o.base == null ? 0 : o.base));
      const at = o.at || (i => f.x(i));
      const groups = Object.create(null);
      for (let i = 0; i < values.length; i++) {
        const v = values[i];
        if (v == null || !isFinite(v)) continue;
        const c = typeof o.color === 'function' ? o.color(v, i) : (o.color || P.accent);
        const py = R(f.y(v));
        const x = R(at(i) + (o.dx || 0) - bw / 2);
        const top = Math.min(py, y0), hh = Math.max(1, Math.abs(py - y0));
        groups[c] = (groups[c] || '') + 'M' + x + ' ' + R(top) + 'h' + R(bw) + 'v' + R(hh) + 'h' + R(-bw) + 'Z';
      }
      const out = [];
      for (const c in groups) out.push(el('path', { d: groups[c], fill: c, opacity: o.opacity, 'shape-rendering': 'crispEdges' }, g));
      return out;
    };
    f.vline = (xv, o) => {
      o = o || {};
      const px = R(f.x(xv));
      if (px < -0.5 || px > w + 0.5) return null;
      el('line', {
        x1: px, x2: px, y1: 0, y2: h, stroke: o.color || P.orange, 'stroke-width': o.width || 1,
        'stroke-dasharray': o.dash === '' ? null : (o.dash || '3 3'), opacity: o.opacity == null ? 0.85 : o.opacity
      }, g);
      if (o.label) {
        const flip = px > w - 52;
        el('text', {
          x: px + (flip ? -4 : 4), y: o.labelY || 10, fill: o.color || P.orange, 'font-size': 10,
          'text-anchor': flip ? 'end' : 'start'
        }, g).textContent = o.label;
      }
      return px;
    };
    f.hline = (yv, o) => {
      o = o || {};
      const py = R(f.y(yv));
      el('line', {
        x1: 0, x2: w, y1: py, y2: py, stroke: o.color || P.axis, 'stroke-width': o.width || 1,
        'stroke-dasharray': o.dash, 'shape-rendering': 'crispEdges'
      }, g);
      return py;
    };
    f.legend = items => {
      let x = 0;
      items.forEach(it => {
        el('rect', { x, y: -10, width: 8, height: 8, fill: it.color, rx: 1 }, g);
        el('text', { x: x + 11, y: -3, fill: P.muted, 'font-size': 10 }, g).textContent = it.label;
        x += 11 + it.label.length * 6.1 + 12;
      });
      return f;
    };
    f.note = (s, o) => {
      o = o || {};
      el('text', {
        x: o.right ? w : 0, y: o.y == null ? -3 : o.y, fill: o.color || P.muted, 'font-size': 10,
        'text-anchor': o.right ? 'end' : 'start'
      }, g).textContent = s;
      return f;
    };
    f.empty = msg => {
      el('text', { x: w / 2, y: h / 2, fill: P.muted, 'font-size': 11, 'text-anchor': 'middle' }, g)
        .textContent = msg || 'no data';
      el('line', { x1: 0, x2: w, y1: h, y2: h, stroke: P.axis, 'stroke-width': 1, 'shape-rendering': 'crispEdges' }, g);
      return f;
    };

    /* payoff diagram: zero line, shaded profit/loss, strikes, breakevens, spot */
    f.payoff = (legs, o) => {
      o = o || {};
      if (!legs || !legs.length) { f.empty(o.empty || 'no legs'); return null; }
      let lo = Infinity, hi = -Infinity;
      legs.forEach(L => { lo = Math.min(lo, L.strike); hi = Math.max(hi, L.strike); });
      if (o.spot) { lo = Math.min(lo, o.spot); hi = Math.max(hi, o.spot); }
      const wide = Math.max(hi - lo, 500);
      const range = o.range || [lo - wide * 0.9, hi + wide * 0.9];
      const cur = payoffCurve(legs, range[0], range[1]);

      f.xLinear(range[0], range[1]);
      const span = (cur.max - cur.min) || Math.abs(cur.max) || 1;
      f.yLinear(cur.min - span * 0.18, cur.max + span * 0.24);
      f.grid({ x: true });

      const yz = R(f.y(0)), pxPts = f.px(cur.pts), id = 'pf' + (++UID);
      const defs = el('defs', null, g);
      el('rect', { x: 0, y: -4, width: w, height: Math.max(0, yz + 4) },
        el('clipPath', { id: id + 'a' }, defs));
      el('rect', { x: 0, y: yz, width: w, height: Math.max(0, h - yz + 4) },
        el('clipPath', { id: id + 'b' }, defs));
      const poly = dOf(pxPts) + 'L' + R(pxPts[pxPts.length - 1][0]) + ' ' + yz + 'L' + R(pxPts[0][0]) + ' ' + yz + 'Z';
      el('path', { d: poly, fill: P.green, opacity: 0.17, 'clip-path': 'url(#' + id + 'a)' }, g);
      el('path', { d: poly, fill: P.red, opacity: 0.17, 'clip-path': 'url(#' + id + 'b)' }, g);
      el('line', { x1: 0, x2: w, y1: yz, y2: yz, stroke: P.axis, 'stroke-width': 1, 'shape-rendering': 'crispEdges' }, g);

      legs.forEach(L => {
        const sx = R(f.x(L.strike));
        if (sx < 0 || sx > w) return;
        const short = L.side === 'S' || L.side === 'SELL' || L.side === 'SHORT';
        el('line', {
          x1: sx, x2: sx, y1: 0, y2: h, stroke: short ? P.pink : P.purple,
          'stroke-width': 1, 'stroke-dasharray': '2 3', opacity: 0.5
        }, g);
      });
      f.line(cur.pts, { color: P.accent, width: 2 });
      if (o.breakevens !== false) cur.be.forEach(b => f.vline(b, { color: P.orange, dash: '4 3', label: 'BE ' + Math.round(b), labelY: h - 4 }));
      if (o.spot) f.vline(o.spot, { color: P.text, dash: '', opacity: 0.5, label: 'spot ' + Math.round(o.spot) });
      f.axisY(fmt.money); f.axisX(fmt.strike);

      f.hover(px => {
        const S = f.x.invert(px);
        if (S < f.x.domain[0] || S > f.x.domain[1]) return null;
        const v = payoffAt(legs, S);
        return {
          x: px, y: f.y(v), title: 'Nifty ' + Math.round(S),
          rows: [['P&L at expiry', fmt.rupee(v), v >= 0 ? P.green : P.red]]
        };
      });
      return cur;
    };

    /* hover: locate(pxX, pxY, dataX) -> {x, y, title, rows:[[label,val,color]]} | null */
    f.hover = locate => { f._hover = locate; return f; };

    f._finish = () => {
      if (!f._hover) return;
      const cross = el('g', { 'pointer-events': 'none', visibility: 'hidden' }, g);
      const vl = el('line', { x1: 0, x2: 0, y1: 0, y2: h, stroke: P.accent, 'stroke-width': 1, opacity: 0.55 }, cross);
      const dot = el('circle', { r: 3.2, fill: P.accent, visibility: 'hidden' }, cross);
      const cap = el('rect', { x: 0, y: 0, width: w, height: h, fill: 'transparent' }, g);
      const tip = api.tip, m = api.cfg.margin;
      let box = null;
      const hide = () => { cross.setAttribute('visibility', 'hidden'); tip.hidden = true; };
      const move = e => {
        if (!box) box = api.svg.getBoundingClientRect();
        const px = e.clientX - box.left - m.l, py = e.clientY - box.top - m.t;
        let hit = null;
        try { hit = f._hover(px, py, f.x && f.x.invert ? f.x.invert(px) : px); } catch (err) { hit = null; }
        if (!hit) { hide(); return; }
        const hx = R(hit.x == null ? px : hit.x);
        vl.setAttribute('x1', hx); vl.setAttribute('x2', hx);
        if (hit.y == null) dot.setAttribute('visibility', 'hidden');
        else { dot.setAttribute('visibility', 'visible'); dot.setAttribute('cx', hx); dot.setAttribute('cy', R(hit.y)); }
        cross.setAttribute('visibility', 'visible');
        let html = hit.title ? '<b>' + hit.title + '</b>' : '';
        (hit.rows || []).forEach(r => {
          html += '<i style="background:' + (r[2] || P.muted) + '"></i>' + r[0] + '<u>' + r[1] + '</u>';
        });
        tip.innerHTML = html; tip.hidden = false;
        let left = m.l + hx + 14;
        if (left + tip.offsetWidth > box.width - 4) left = m.l + hx - tip.offsetWidth - 14;
        let top = m.t + (hit.y == null ? py : hit.y) - tip.offsetHeight - 12;
        if (top < 2) top = 2;
        tip.style.left = Math.max(2, left) + 'px';
        tip.style.top = top + 'px';
      };
      cap.addEventListener('pointerenter', () => { box = api.svg.getBoundingClientRect(); });
      cap.addEventListener('pointermove', move);
      cap.addEventListener('pointerdown', e => { box = api.svg.getBoundingClientRect(); move(e); });
      cap.addEventListener('pointerleave', hide);
      cap.addEventListener('pointercancel', hide);
    };
    return f;
  }

  /* ======================================================================
     Ready-made charts. Each takes a host div + data and is idempotent:
     calling it again with the same data does no DOM work at all.
     ====================================================================== */

  /* 1. OI / ΔOI by strike, CE vs PE, spot marked. mode: 'oi' | 'doi' */
  function oiChart(host, ch, opts) {
    opts = opts || {};
    const p = plot(host, { height: opts.height || 230, margin: { t: 18, r: 12, b: 26, l: 46 } });
    const mode = opts.mode || 'oi';
    p.render(ch ? ch.key + '|' + mode : 'empty', f => {
      if (!ch || !ch.rows || !ch.rows.length) { f.empty('Load a chain to see open interest'); return; }
      const rows = ch.rows, n = rows.length;
      const ce = rows.map(r => mode === 'oi' ? r.ce_oi : r.ce_doi);
      const pe = rows.map(r => mode === 'oi' ? r.pe_oi : r.pe_doi);
      f.xBand(n, n > 40 ? 0.15 : 0.3);
      f.yFrom(ce.concat(pe));
      f.grid();
      const bw = Math.max(1.5, f.x.width / 2 - 0.5);
      f.bars(ce, { width: bw, dx: -bw / 2 - 0.4, color: P.accent });
      f.bars(pe, { width: bw, dx: bw / 2 + 0.4, color: P.pink });
      f.hline(0);
      let si = 0, best = Infinity;
      rows.forEach((r, i) => { const d = Math.abs(r.strike - ch.spot); if (d < best) { best = d; si = i; } });
      const sx = R(f.x(si));
      el('line', { x1: sx, x2: sx, y1: 0, y2: f.h, stroke: P.orange, 'stroke-width': 1, 'stroke-dasharray': '3 3' }, f.g);
      f.axisY(fmt.compact);
      f.axisCats(rows.map(r => r.strike), v => String(Math.round(v)));
      f.legend([{ label: 'CE ' + (mode === 'oi' ? 'OI' : 'ΔOI'), color: P.accent },
                { label: 'PE ' + (mode === 'oi' ? 'OI' : 'ΔOI'), color: P.pink }]);
      f.hover(px => {
        const i = f.x.invert(px), r = rows[i];
        if (!r) return null;
        return {
          x: f.x(i), title: 'Strike ' + r.strike,
          rows: [['CE', fmt.int(ce[i]), P.accent], ['PE', fmt.int(pe[i]), P.pink],
                 ['PE/CE', ce[i] ? (pe[i] / ce[i]).toFixed(2) : '—', P.muted]]
        };
      });
    });
    return p;
  }

  /* 2. IV smile / skew across strikes */
  function smileChart(host, ch, opts) {
    opts = opts || {};
    const p = plot(host, { height: opts.height || 200, margin: { t: 18, r: 12, b: 26, l: 40 } });
    p.render(ch ? ch.key : 'empty', f => {
      if (!ch || !ch.rows || !ch.rows.length) { f.empty('Load a chain to see the IV skew'); return; }
      const rows = ch.rows;
      const ceP = rows.filter(r => r.ce_iv > 0).map(r => [r.strike, r.ce_iv]);
      const peP = rows.filter(r => r.pe_iv > 0).map(r => [r.strike, r.pe_iv]);
      if (!ceP.length && !peP.length) { f.empty('no IV in this chain'); return; }
      f.xLinear(rows[0].strike, rows[rows.length - 1].strike);
      f.yFrom(ceP.concat(peP).map(d => d[1]), { zero: false, pad: 0.18 });
      f.grid({ x: true });
      f.line(peP, { color: P.pink });
      f.line(ceP, { color: P.accent });
      f.vline(ch.spot, { color: P.orange, label: 'spot' });
      f.axisY(v => v.toFixed(0) + '%');
      f.axisX(fmt.strike);
      f.legend([{ label: 'CE IV', color: P.accent }, { label: 'PE IV', color: P.pink }]);
      f.hover(px => {
        const s = f.x.invert(px);
        let r = null, best = Infinity;
        rows.forEach(q => { const d = Math.abs(q.strike - s); if (d < best) { best = d; r = q; } });
        if (!r) return null;
        return {
          x: f.x(r.strike), title: 'Strike ' + r.strike,
          rows: [['CE IV', (r.ce_iv || 0).toFixed(1) + '%', P.accent],
                 ['PE IV', (r.pe_iv || 0).toFixed(1) + '%', P.pink]]
        };
      });
    });
    return p;
  }

  /* 3. expiry payoff for one spread or the whole book */
  function payoffChart(host, legs, spot, opts) {
    opts = opts || {};
    const p = plot(host, { height: opts.height || 250, margin: { t: 16, r: 14, b: 26, l: 58 } });
    const key = legs && legs.length
      ? legs.map(L => L.side + L.type + L.strike + ':' + L.premium + 'x' + L.qty).join(',') + '|' + Math.round(spot || 0)
      : 'empty';
    p.render(key, f => {
      const cur = f.payoff(legs, { spot, empty: opts.empty || 'Deploy a spread to see its expiry payoff' });
      if (!cur) return;
      f.note('max ' + fmt.rupee(cur.max), { color: P.green });
      f.note('worst ' + fmt.rupee(cur.min), { right: true, color: P.red });
    });
    return p;
  }

  /* 4. cumulative realised P&L (equity curve) + drawdown in the tooltip */
  function equityChart(host, rows, opts) {
    opts = opts || {};
    const p = plot(host, { height: opts.height || 230, margin: { t: 16, r: 14, b: 26, l: 56 } });
    const key = rows && rows.length ? rows.length + ':' + rows[rows.length - 1].exit_time : 'empty';
    p.render(key, f => {
      if (!rows || !rows.length) { f.empty('Closed trades will plot your equity curve here'); return; }
      const s = rows.slice().sort((a, b) => String(a.exit_time).localeCompare(String(b.exit_time)));
      const pts = [[0, 0]], dd = [0];
      let cum = 0, peak = 0;
      s.forEach((t, i) => {
        cum += Number(t.pnl) || 0;
        if (cum > peak) peak = cum;
        pts.push([i + 1, cum]); dd.push(cum - peak);
      });
      const up = cum >= 0;
      f.xLinear(0, pts.length - 1);
      f.yFrom(pts.map(q => q[1]));
      f.grid();
      f.area(pts, { color: up ? P.green : P.red, opacity: 0.12 });
      f.line(pts, { color: up ? P.green : P.red, width: 2 });
      f.hline(0);
      f.axisY(fmt.money);
      f.axisX(v => '#' + Math.round(v));
      f.hover(px => {
        const i = Math.round(f.x.invert(px));
        if (i < 1 || i >= pts.length) return null;
        const t = s[i - 1];
        return {
          x: f.x(i), y: f.y(pts[i][1]),
          title: '#' + i + '  ' + String(t.exit_time || '').slice(0, 10),
          rows: [[t.strike + ' ' + t.type, fmt.rupee(t.pnl), t.pnl >= 0 ? P.green : P.red],
                 ['Cumulative', fmt.rupee(pts[i][1]), P.text],
                 ['Drawdown', fmt.rupee(dd[i]), P.muted]]
        };
      });
    });
    return p;
  }

  /* 5. per-position P&L contribution bars */
  function pnlBars(host, rows, opts) {
    opts = opts || {};
    const label = opts.label || (r => r.strike + (String(r.type).charAt(0) === 'C' ? 'C' : 'P'));
    const p = plot(host, { height: opts.height || 170, margin: { t: 14, r: 12, b: 30, l: 56 } });
    const key = rows && rows.length ? rows.map(r => r.pnl).join(',') : 'empty';
    p.render(key, f => {
      if (!rows || !rows.length) { f.empty('No open positions'); return; }
      const v = rows.map(r => Number(r.pnl) || 0);
      f.xBand(rows.length, rows.length > 20 ? 0.2 : 0.45);
      f.yFrom(v);
      f.grid();
      f.bars(v, { color: x => x >= 0 ? P.green : P.red });
      f.hline(0);
      f.axisY(fmt.money);
      f.axisCats(rows.map(label));
      f.hover(px => {
        const i = f.x.invert(px), r = rows[i];
        if (!r) return null;
        return {
          x: f.x(i), y: f.y(v[i]), title: label(r, i) + '  ' + (r.expiry || ''),
          rows: [['P&L', fmt.rupee(v[i]), v[i] >= 0 ? P.green : P.red],
                 ['DTE left', String(r.dte_now == null ? '—' : r.dte_now), P.muted]]
        };
      });
    });
    return p;
  }

  /* 6. DTE ladder — one horizontal bar per position, exit threshold marked */
  function dteLadder(host, rows, exitDte, opts) {
    opts = opts || {};
    const rowH = 16;
    const p = plot(host, {
      height: Math.max(90, 30 + rowH * ((rows && rows.length) || 3)),
      margin: { t: 14, r: 14, b: 24, l: 92 }
    });
    const key = rows && rows.length ? rows.map(r => r.dte_now).join(',') + '|' + exitDte : 'empty';
    p.render(key, f => {
      if (!rows || !rows.length) { f.empty('No open positions to age'); return; }
      const maxD = Math.max(90, ...rows.map(r => Number(r.dte_now) || 0));
      f.xLinear(0, maxD);
      f.grid({ x: true, yCount: 0 });
      const bh = Math.min(11, (f.h - 4) / rows.length - 3);
      rows.forEach((r, i) => {
        const y = 2 + i * (f.h - 4) / rows.length;
        const d = Number(r.dte_now) || 0;
        const danger = d <= exitDte;
        el('rect', {
          x: 0, y: R(y), width: Math.max(2, R(f.x(d))), height: R(bh),
          fill: danger ? P.red : P.accent, opacity: danger ? 0.85 : 0.6, rx: 2
        }, f.g);
        el('text', { x: -8, y: R(y + bh - 1), fill: P.text, 'font-size': 10, 'text-anchor': 'end' }, f.g)
          .textContent = (opts.label ? opts.label(r) : r.strike + ' ' + String(r.type).charAt(0)) ;
      });
      f.vline(exitDte, { color: P.orange, label: 'exit ' + exitDte + 'd', labelY: f.h - 2 });
      f.axisX(v => Math.round(v) + 'd');
    });
    return p;
  }

  return {
    plot, colors: P, fmt, ticks, linear, band, payoffAt, payoffCurve,
    oiChart, smileChart, payoffChart, equityChart, pnlBars, dteLadder
  };
})();

/* ==========================================================================
   App
   ========================================================================== */
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const num=(n,d)=>n==null||isNaN(n)?'-':Number(n).toFixed(d==null?2:d);
const inr=(n,d)=>n==null||isNaN(n)?'-':(n<0?'-':'')+'₹'+Math.abs(Number(n)).toLocaleString('en-IN',{minimumFractionDigits:d==null?2:d,maximumFractionDigits:d==null?2:d});
const inrShort=v=>{const a=Math.abs(v),s=v<0?'-':'';return a>=1e5?s+'₹'+(a/1e5).toFixed(a>=1e6?0:1)+'L':a>=1e3?s+'₹'+(a/1e3).toFixed(a>=1e4?0:1)+'k':s+'₹'+a.toFixed(0);};
const rs0=v=>v==null||isNaN(v)?'-':inr(Math.round(Number(v))||0,0);   // whole rupees, never "-0"
const cls=n=>n>0?'g':(n<0?'r':'');
const tag=t=>'<span class="tag '+(t==='PE'?'pe':'ce')+'">'+esc(t)+'</span>';
const table=(head,rows,empty)=>rows.length?'<table><thead><tr>'+head.map(h=>'<th>'+h+'</th>').join('')+'</tr></thead><tbody>'+rows.join('')+'</tbody></table>':'<div class="empty">'+empty+'</div>';
function setHTML(el,html){if(el&&el.__h!==html){el.innerHTML=html;el.__h=html;}}
const store={get(k){try{return localStorage.getItem(k);}catch(e){return null;}},set(k,v){try{localStorage.setItem(k,v);}catch(e){}}};

/* Hosted mode: the session cookie plus the CSRF header on every POST, and a
   401 sends the browser to the login page.  Every call goes through here. */
function csrf(){
  const m=document.cookie.match(/(?:^|;\s*)csrf=([^;]+)/);
  return m?decodeURIComponent(m[1]):'';
}
async function api(path,opts){
  opts=opts||{};
  opts.headers=Object.assign({'X-CSRF-Token':csrf()},opts.headers||{});
  if(opts.body)opts.headers['Content-Type']='application/json';
  const res=await fetch(path,opts);
  if(res.status===401){location.href='/login';throw new Error('not authenticated');}
  const body=await res.json().catch(()=>({}));
  if(!res.ok)throw new Error(body.error||(res.status+' '+res.statusText));
  return body;
}
const post=(p,b)=>api(p,{method:'POST',body:JSON.stringify(b||{})});
const get=p=>api(p);

/* Charts get a compact label; the full "24000 / 24500 CE" form overlaps once
   there are more than about four bars. */
const shortLabel=r=>(r.short_strike!=null?r.short_strike:r.strike)+(String(r.type).charAt(0)==='C'?'CE':'PE');
const popCls=p=>p==null?'':(p>=75?'pop-hi':p>=65?'pop-mid':'pop-lo');
function spreadCell(type,shortK,longK){
  const t=type==='CALL'?'CE':'PE';
  if(longK==null)return '<td><b>'+esc(shortK)+'</b> '+tag(t)+'<span class="badge bad">NAKED</span></td>';
  return '<td><b>'+esc(shortK)+'</b> <span class="hint">/ '+esc(longK)+'</span> '+tag(t)+'</td>';
}
function eventRows(evs){return table(['Time','Kind','What happened'],(evs||[]).map(e=>
  '<tr><td class="mono">'+esc(e.ts)+'</td><td><span class="tag kind k-'+esc(e.kind)+'">'+esc(e.kind)+'</span></td><td class="wrap">'+esc(e.msg)+'</td></tr>'),'Nothing logged yet.');}
function tokenBanner(t){
  const fix=t.env_pinned?'Set a fresh one in NIFTY Trader\'s Broker token screen.':
    'Set one in NIFTY Trader\'s Broker token screen, or paste one under Settings - Broker when this strategy runs on its own.';
  if(!t.configured)return '<div class="note crit">No Dhan access token. '+fix+'</div>';
  if(t.expired)return '<div class="note crit">Access token '+esc(t.human)+'. '+fix+'</div>';
  if(t.rejected)return '<div class="note crit">Dhan rejected the token: '+esc(t.rejected_msg)+'</div>';
  if(t.warn)return '<div class="note">Access token '+esc(t.human)+'.</div>';
  return '';
}

/* ---------- tabs ---------- */
const renderers={};
let TAB='dashboard',userPickedTab=false;
function showTab(t,auto){
  if(!$('#p-'+t))t='dashboard';
  TAB=t;if(!auto)store.set('cs_tab',t);
  $$('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.tab===t));
  $$('.panel').forEach(p=>p.classList.toggle('on',p.id==='p-'+t));
  const fn=renderers[t];if(fn)fn();
}
$('#tabs').onclick=e=>{const b=e.target.closest('button[data-tab]');if(b){userPickedTab=true;showTab(b.dataset.tab);}};

/* ---------- live state ---------- */
let S=null,sentToSettings=false,lastExpiries='';
function runState(s){
  if(!s.scanner_owner)return 'ro';
  if(s.scanning_active)return 'run';
  if(s.autostart)return (s.token.configured&&!s.token.expired)?'starting':'wait';
  return 'stop';
}
/* [pill text, pill class, dashboard colour].  STARTING / WAITING are the
   launch-time automatic start that has not happened yet (WAITING = no usable
   broker token yet); Stop cancels it. */
const RUNS={run:['RUNNING','on','g'],stop:['STOPPED','off','r'],starting:['STARTING','wait','o'],
  wait:['WAITING','wait','o'],ro:['READ-ONLY','off','r']};
async function poll(){
  let s;
  try{s=await get('/api/status');}catch(e){$('#statusline').textContent='cannot reach the strategy: '+e.message;return;}
  S=s;
  const tokOk=s.token.configured&&!s.token.expired, st=runState(s), R=RUNS[st];
  $('#p_mkt').textContent=s.market||'-';
  $('#p_tok').textContent='token '+s.token.human;$('#p_tok').className='pill '+(tokOk?'on':'off');
  $('#p_run').textContent=R[0];$('#p_run').className='pill '+R[1];
  $('#b_start').disabled=st==='run'||st==='ro';
  $('#b_stop').disabled=st==='stop'||st==='ro';
  let line=s.status_message||'';
  if(st==='wait')line='Waiting for a valid broker token (token '+s.token.human+') - the scanner starts by itself once it works   |   '+line;
  if(st==='starting')line='Starting the scanner...   |   '+line;
  $('#statusline').textContent=line+'   |   last scan '+s.last_scan_time+(s.force_scan?'   |   market hours ignored':'');

  /* dashboard */
  $('#d_run').textContent=st==='wait'?'WAITING FOR TOKEN':R[0];$('#d_run').className='v '+R[2];
  $('#d_run2').textContent={run:'scans every 60 s'+(s.force_scan?', around the clock':', 09:15-15:30 IST'),
    stop:'press Start to scan again',starting:'starts within a few seconds',
    wait:'starts by itself once the broker token works',ro:'another copy owns the scanner'}[st];
  $('#d_open').textContent=s.open_count;
  $('#d_open2').textContent='hard exit at '+s.filters.exit_dte+' days to expiry while scanning';
  const vx=s.vix||{};let vh='';
  const lim=vx.limit>0?vx.limit:null;
  if(!lim)vh='<div class="note"><b>VIX kill switch: OFF</b> (limit set to 0 in NIFTY Trader &rarr; VIX limit).</div>';
  else if(vx.kill)vh='<div class="note crit"><b>VIX KILL SWITCH ON</b> - India VIX '+esc(vx.value)+' is above the '+esc(lim)+' limit. No new trades, and every open spread is closed during market hours. Trading resumes by itself when VIX is back at or below '+esc(lim)+'.</div>';
  else vh='<div class="note ok"><b>VIX kill switch: ACTIVE</b> - limit India VIX '+esc(lim)+'. Above it: no new trades and all open spreads are closed. '+
    (vx.value!=null?'Now: India VIX '+esc(vx.value)+' at '+esc(vx.at)+' - trades allowed.':'Current VIX: '+esc(vx.note==='not checked yet'?'checking...':vx.note)+'.')+
    ' Change the limit in NIFTY Trader &rarr; VIX limit.</div>';
  if($('#vixbanner').dataset.h!==vh){$('#vixbanner').innerHTML=vh;$('#vixbanner').dataset.h=vh;}
  $('#d_scan').textContent=s.last_scan_time;
  $('#d_scan2').textContent=s.market||'';
  $('#d_exp').textContent=s.expiry_list.length;
  $('#d_exp2').textContent=s.scrip_count+' NIFTY contracts in the scrip master';
  let banner=tokenBanner(s.token);
  if(!s.scanner_owner)banner+='<div class="note">Another copy of this app is already running and owns the scanner. This window is read-only - close one of them.</div>';
  setHTML($('#tokenbanner'),banner);

  // Nothing works without a token, so take him to Settings once rather than
  // leaving him on a Dashboard that cannot load anything.
  if(!sentToSettings&&!userPickedTab&&!tokOk){sentToSettings=true;showTab('settings',true);}

  const sig=JSON.stringify(s.expiry_list);
  if(sig!==lastExpiries){
    lastExpiries=sig;const c=$('#expiry_combo'),prev=c.value;
    c.innerHTML=s.expiry_list.length?s.expiry_list.map(e=>'<option value="'+esc(e)+'">'+esc(e)+'</option>').join(''):
      '<option value="">No expiries yet - they load once the broker token works</option>';
    if(s.expiry_list.includes(prev))c.value=prev;
  }
  if(!chainBusy)$('#btn_load').disabled=!s.expiry_list.length;

  paintSettings(s);
  $('#market_note').textContent='Market now: '+(s.market||'-');
  $('#auth_note').textContent=s.auth_on?'Password protection is ON.':
    'Running locally without a password. Set APP_PASSWORD before hosting this.';
  if(TAB==='dashboard')loadDashEvents();
  if(TAB==='settings')paintToken(s.token);
  if(TAB==='activity')refreshEvents();
}

/* ---------- dashboard ---------- */
let dashEvBusy=false;
async function loadDashEvents(){
  if(dashEvBusy)return;dashEvBusy=true;
  try{const d=await get('/api/events');setHTML($('#d_ev'),eventRows(d.events.slice(-8).reverse()));}catch(e){}
  dashEvBusy=false;
}
let chainData=null,oiMode='oi',chainBusy=false;
function zoomRows(ch){
  const z=parseFloat($('#zoom').value);
  if(!ch||z>=9)return ch;
  const lo=ch.spot*(1-z),hi=ch.spot*(1+z);
  return Object.assign({},ch,{rows:ch.rows.filter(r=>r.strike>=lo&&r.strike<=hi)});
}
function drawChain(){
  const v=zoomRows(chainData);
  Viz.oiChart($('#c_oi'),v,{mode:oiMode});
  Viz.smileChart($('#c_smile'),v);
}
$('#zoom').addEventListener('change',drawChain);
$('#oi_mode_oi').onclick=()=>{oiMode='oi';$('#oi_mode_oi').classList.add('on');$('#oi_mode_doi').classList.remove('on');drawChain();};
$('#oi_mode_doi').onclick=()=>{oiMode='doi';$('#oi_mode_doi').classList.add('on');$('#oi_mode_oi').classList.remove('on');drawChain();};
const dash=v=>v==null?'-':esc(v);
async function loadChain(){
  const exp=$('#expiry_combo').value;
  if(!exp){$('#chain_note').textContent='No expiry to load yet - expiries appear once the broker token works.';return;}
  chainBusy=true;$('#dash_spinner').hidden=false;$('#btn_load').disabled=true;
  try{
    const d=await get('/api/chain?expiry='+encodeURIComponent(exp));
    chainData=d;
    $('#m_spot').textContent=inr(d.spot);
    $('#m_synth').textContent=inr(d.synth);
    $('#m_atm').textContent=Math.round(d.atm);
    $('#m_dte').textContent=d.dte+'d';
    $('#chain_note').textContent=d.expiry+' - '+d.rows.length+' strikes'+(d.stale?' (stale snapshot)':'');
    drawChain();
    setHTML($('#chain_body'),d.rows.map(r=>
      '<tr><td class="'+popCls(r.ce_pop)+'">'+(r.ce_pop==null?'-':num(r.ce_pop,1))+'</td>'+
      '<td>'+dash(r.ce_theta)+'</td><td>'+dash(r.ce_gamma)+'</td><td>'+dash(r.ce_delta)+'</td>'+
      '<td>'+dash(r.ce_iv)+'</td><td>'+dash(r.ce_oi)+'</td><td>'+dash(r.ce_doi)+'</td>'+
      '<td>'+dash(r.ce_ltp)+'</td><td><b>'+dash(r.strike)+'</b></td><td>'+dash(r.pe_ltp)+'</td>'+
      '<td>'+dash(r.pe_doi)+'</td><td>'+dash(r.pe_oi)+'</td><td>'+dash(r.pe_iv)+'</td>'+
      '<td>'+dash(r.pe_delta)+'</td><td>'+dash(r.pe_gamma)+'</td><td>'+dash(r.pe_theta)+'</td>'+
      '<td class="'+popCls(r.pe_pop)+'">'+(r.pe_pop==null?'-':num(r.pe_pop,1))+'</td></tr>').join('')||
      '<tr><td colspan="17" class="empty">This chain has no strikes.</td></tr>');
  }catch(e){$('#chain_note').textContent=e.message;}
  finally{chainBusy=false;$('#dash_spinner').hidden=true;$('#btn_load').disabled=!(S&&S.expiry_list.length);}
}
$('#btn_load').onclick=loadChain;
renderers.dashboard=()=>{if(chainData)drawChain();loadDashEvents();};

/* ---------- screener ---------- */
let matches=[],selMatch=null;
const REJECT_TEXT={
  wing_strike_absent:'wing strike not listed',
  wing_already_held:'wing strike already sold in another spread',
  wing_unpriced:'wing has no price',
  wing_off_grid:'wing below zero',
  not_in_scrip_master:'contract not in scrip master',
  lot_mismatch:'legs have different lot sizes',
  credit_not_positive:'wing costs more than the short',
  credit_exceeds_width:'bad quote (credit above width)',
  below_min_credit:'credit below your minimum',
  below_min_ror:'return on risk too low',
  below_min_spread_pop:'spread POP too low',
  spread_pop_uncomputable:'POP not computable',
  chain_unavailable:'chain unavailable',
  error:'errors'
};
async function runScreener(){
  $('#screener_spinner').hidden=false;$('#btn_screener_refresh').disabled=true;
  try{
    const d=await post('/api/screener/run');
    matches=d.matches||[];
    $('#match_lbl').textContent=matches.length+' spread'+(matches.length===1?'':'s')+' ('+(d.wing_width||500)+' pt wing)';
    const rj=Object.entries(d.rejects||{}).sort((a,b)=>b[1]-a[1]);
    setHTML($('#reject_note'),d.note?'<div class="note">'+esc(d.note)+'</div>':
      (rj.length?'Skipped: '+rj.map(([k,v])=>esc(REJECT_TEXT[k]||k)+' &times;'+esc(v)).join(' &middot; '):''));
    setHTML($('#screener_wrap'),table(['<input type="checkbox" id="screener_check_all">','Expiry','DTE','Spread','Credit','Credit ₹',
      'Max loss','Margin','RoR','Short POP','Spread POP','Eff','Qty'],matches.map((m,i)=>
      '<tr class="clickable" data-i="'+i+'"><td><input type="checkbox" class="sc-chk" value="'+esc(m.key)+'"></td>'+
      '<td>'+esc(m.Expiry)+'</td><td>'+esc(m.DTE)+'</td>'+spreadCell(m.Type,m.Short_Strike,m.Long_Strike)+
      '<td>'+num(m.Net_Credit)+'</td><td>'+rs0(m.Credit_Received)+'</td><td class="r">'+rs0(m.Max_Loss)+'</td>'+
      '<td title="Estimated SPAN + ELM. Click the row for a live Dhan quote.">'+rs0(m.Margin)+'<span class="badge">est</span></td>'+
      '<td><span class="rbar" title="'+esc(m.ROR)+'%"><i style="width:'+Math.max(0,Math.min(100,Number(m.ROR)||0))+'%"></i></span><span class="hint">'+esc(m.ROR)+'%</span></td>'+
      '<td class="'+popCls(m.Short_POP)+'">'+esc(m.Short_POP)+'%</td><td class="'+popCls(m.Spread_POP)+'">'+esc(m.Spread_POP)+'%</td>'+
      '<td>'+esc(m.Efficiency)+'</td><td>'+esc(m.Qty)+'</td></tr>'),
      d.note?'No scan possible yet.':'No spread passes the saved filters right now.'));
    if(matches.length)selectMatch(0);else showPayoff(null);
  }catch(e){setHTML($('#reject_note'),'<div class="note crit">'+esc(e.message)+'</div>');}
  finally{$('#screener_spinner').hidden=true;$('#btn_screener_refresh').disabled=false;}
}
function selectMatch(i){
  $$('#screener_wrap tr[data-i]').forEach(tr=>tr.classList.toggle('sel',tr.dataset.i===String(i)));
  showPayoff(matches[i]||null);
}
$('#screener_wrap').addEventListener('click',e=>{
  if(e.target.type==='checkbox')return;
  const tr=e.target.closest('tr[data-i]');if(tr)selectMatch(+tr.dataset.i);
});
$('#screener_wrap').addEventListener('change',e=>{
  if(e.target.id==='screener_check_all')$$('.sc-chk').forEach(c=>c.checked=e.target.checked);
});
const miniCard=(k,v,c)=>'<div class="card"><div class="k">'+k+'</div><div class="v '+(c||'')+'">'+v+'</div></div>';
function marginCard(v,source,naked,roi){
  return '<div class="card" style="grid-column:1/-1"><div class="k">MARGIN BLOCKED '+(source==='dhan'?'(DHAN)':'(EST)')+
    '</div><div class="v o">'+rs0(v)+'</div><div class="hint">'+
    (naked?'naked would block '+rs0(naked)+(roi?' - ':''):'')+(roi?'credit is '+esc(roi)+'% of margin':'')+'</div></div>';
}
function showPayoff(m){
  selMatch=m;
  if(!m){
    Viz.payoffChart($('#c_screen_payoff'),[],0,{height:210});
    setHTML($('#screen_stats'),'');$('#payoff_lbl').textContent='click a row';
    return;
  }
  const t=m.Type==='CALL'?'CE':'PE';
  const legs=[
    {side:'S',type:t,strike:m.Short_Strike,premium:m.Short_LTP,qty:m.Qty},
    {side:'B',type:t,strike:m.Long_Strike,premium:m.Long_LTP,qty:m.Qty}
  ];
  $('#payoff_lbl').textContent=m.Label+'  '+m.Expiry;
  Viz.payoffChart($('#c_screen_payoff'),legs,m.Spot,{height:210});
  const away=(m.Breakeven-m.Spot)/m.Spot*100;
  setHTML($('#screen_stats'),
    miniCard('CREDIT',rs0(m.Credit_Received),'g')+
    miniCard('MAX LOSS',rs0(m.Max_Loss),'r')+
    miniCard('BREAKEVEN',num(m.Breakeven,0))+
    miniCard('BE DISTANCE',(away>=0?'+':'')+num(away,1)+'%')+
    marginCard(m.Margin,'estimate',m.Margin_Naked,m.ROI_On_Margin));
  liveMargin({key:m.key},m);
}
/* One live basket quote for the row he actually clicked. Doing this per row
   would be dozens of calls against a rate-limited endpoint. */
async function liveMargin(ref,m){
  try{
    const d=await post('/api/margin',ref);
    if(!d||d.margin==null)return;
    if(m&&selMatch!==m)return;                 // he clicked elsewhere meanwhile
    const cards=$('#screen_stats').querySelectorAll('.card');
    if(cards.length)cards[cards.length-1].outerHTML=marginCard(d.margin,d.source,d.naked_equivalent,d.roi_on_margin);
    $('#screen_stats').__h=null;
  }catch(e){/* estimate already shown */}
}
$('#btn_screener_refresh').onclick=runScreener;
$('#btn_screener_deploy').onclick=async()=>{
  const keys=$$('.sc-chk').filter(c=>c.checked).map(c=>c.value);
  if(!keys.length){alert('Tick at least one spread to deploy.');return;}
  try{
    const d=await post('/api/screener/deploy',{keys});
    let msg='Deployed '+d.deployed+' spread(s).';
    if(d.duplicates)msg+=' '+d.duplicates+' skipped (already held).';
    if(d.stale)msg+=' '+d.stale+' skipped (stale - rerun the screener).';
    alert(msg);
  }catch(e){alert(e.message);}
  runScreener();poll();
};
renderers.screener=()=>{if(selMatch)showPayoff(selMatch);};

/* ---------- positions ---------- */
let posData=null,selExpiry=null,posBusy=false;
async function refreshPositions(){
  if(posBusy)return;posBusy=true;
  $('#pos_spinner').hidden=false;$('#btn_pos_refresh').disabled=true;
  try{
    const d=await get('/api/positions');
    posData=d;
    $('#pos_updated').textContent='updated '+d.updated;
    setHTML($('#pos_strip'),
      miniCard('UNREALIZED P&amp;L',rs0(d.total_pnl),cls(d.total_pnl))+
      miniCard('CREDIT COLLECTED',rs0(d.total_credit))+
      miniCard('MAX RISK',rs0(d.total_risk)+(d.risk_unbounded?' + UNBOUNDED':''),d.risk_unbounded?'r':'o')+
      miniCard('MARGIN BLOCKED',rs0(d.total_margin)+(d.margin_live?'':' est'),'o')+
      miniCard('NET DELTA',esc(d.portfolio_delta))+
      miniCard('THETA / DAY',rs0(d.portfolio_theta),'g')+
      miniCard('OPEN',d.rows.length));
    const exps=Array.from(new Set(d.rows.map(r=>r.expiry))).sort();
    if(!exps.includes(selExpiry))selExpiry=exps[0]||null;
    setHTML($('#exp_chips'),exps.map(e=>'<span class="chip'+(e===selExpiry?' on':'')+'" data-e="'+esc(e)+'">'+
      esc(e)+' <small>'+d.rows.filter(r=>r.expiry===e).length+' open</small></span>').join(''));
    setHTML($('#pos_table'),table(['','Entered','Expiry','Spread','Credit','Now','P&amp;L','% of max','Max loss','Margin','DTE left','Qty'],
      d.rows.map(r=>
      '<tr class="clickable" data-id="'+esc(r.id)+'"><td><input type="checkbox" class="pos-chk" value="'+esc(r.id)+'"></td>'+
      '<td class="mono">'+esc(String(r.time).slice(0,16))+'</td><td>'+esc(r.expiry)+'</td>'+
      spreadCell(r.type,r.short_strike,r.long_strike)+
      '<td>'+num(r.credit)+'</td><td>'+num(r.now)+'</td>'+
      '<td class="'+cls(r.pnl)+'"><b>'+rs0(r.pnl)+'</b></td>'+
      '<td class="hint">'+(r.pnl_pct_max==null?'-':esc(r.pnl_pct_max)+'%')+'</td>'+
      '<td class="r">'+(r.max_loss==null?'UNBOUNDED':rs0(r.max_loss))+'</td>'+
      '<td class="o" title="'+(r.margin_source==='dhan'?'Live quote from Dhan':'Local estimate, approx +/-15%')+'">'+rs0(r.margin)+
        (r.margin_source==='dhan'?'':'<span class="badge">est</span>')+'</td>'+
      '<td class="'+(r.exit_due?'r':'')+'">'+(r.exit_due?'<b>EXIT NOW</b>':esc(r.dte_now)+'d')+'</td>'+
      '<td>'+esc(r.qty)+(r.flags||[]).map(f=>'<span class="badge '+(f==='NAKED'||f==='STALE'?'warn':'')+'">'+esc(f)+'</span>').join('')+'</td></tr>'+
      '<tr class="legrow" data-for="'+esc(r.id)+'" hidden><td colspan="12">'+
      (r.legs||[]).map(l=>(l.side==='S'?'SELL':'BUY ')+' '+esc(l.strike)+' '+esc(l.type)+'  x'+esc(l.qty)+
        '   entry '+num(l.premium)+'   mark '+num(l.mark)+' ('+esc(l.src)+')   leg P&amp;L '+rs0(l.pnl)+'   id '+esc(l.sec_id)).join('<br>')+
      '<br>breakeven '+(r.breakeven==null?'-':esc(r.breakeven))+
      '   entry POP '+(r.pop==null?'-':esc(r.pop)+'%')+
      '   RoR '+(r.ror==null?'-':esc(r.ror)+'%')+
      '<br>margin '+rs0(r.margin)+(r.margin_source==='dhan'?' (Dhan quote)':' estimated')+
      (r.margin_naked?'  (naked would block '+rs0(r.margin_naked)+')':'')+
      '   - margin only stays low while BOTH legs are open</td></tr>'),'No open positions.'));
    drawBook();
  }catch(e){$('#pos_updated').textContent=e.message;}
  finally{$('#pos_spinner').hidden=true;$('#btn_pos_refresh').disabled=false;posBusy=false;}
}
function drawBook(){
  const d=posData;if(!d)return;
  const rows=selExpiry?d.rows.filter(r=>r.expiry===selExpiry):d.rows;
  const legs=[];rows.forEach(r=>(r.legs||[]).forEach(l=>legs.push(l)));
  $('#payoff_exp_lbl').textContent=selExpiry?'at '+selExpiry:'';
  Viz.payoffChart($('#c_book'),legs,(d.spot_by_expiry||{})[selExpiry]||0,{height:240,empty:'Deploy a spread to see the book payoff'});
  Viz.pnlBars($('#c_posbars'),d.rows,{height:240,label:shortLabel});
}
$('#exp_chips').addEventListener('click',e=>{
  const c=e.target.closest('.chip[data-e]');if(!c)return;
  selExpiry=c.dataset.e;$$('#exp_chips .chip').forEach(x=>x.classList.toggle('on',x===c));drawBook();
});
$('#pos_table').addEventListener('click',e=>{
  if(e.target.type==='checkbox')return;
  const tr=e.target.closest('tr.clickable[data-id]');if(!tr)return;
  const lr=[...$('#pos_table').querySelectorAll('tr.legrow')].find(x=>x.dataset.for===tr.dataset.id);
  if(lr)lr.hidden=!lr.hidden;
});
$('#pos_check_all').addEventListener('change',e=>$$('.pos-chk').forEach(c=>c.checked=e.target.checked));
$('#btn_pos_refresh').onclick=refreshPositions;
$('#btn_pos_exit').onclick=async()=>{
  const ids=$$('.pos-chk').filter(c=>c.checked).map(c=>c.value);
  if(!ids.length){alert('Tick at least one position to exit.');return;}
  if(!confirm('Close '+ids.length+' position(s)? Both legs are closed together.'))return;
  try{
    const d=await post('/api/positions/exit',{ids});
    let msg='Closed '+d.exited+' position(s).';
    if(d.deferred&&d.deferred.length)
      msg+='\n'+d.deferred.length+' could not be priced and were left open (nothing was booked at a made-up price).';
    alert(msg);
  }catch(e){alert(e.message);}
  $('#pos_check_all').checked=false;
  refreshPositions();poll();
};
renderers.positions=refreshPositions;

/* ---------- trade report ---------- */
function niceStep(range){const raw=range/4||1,p=Math.pow(10,Math.floor(Math.log10(raw))),m=raw/p;return (m<=1?1:m<=2?2:m<=5?5:10)*p;}
function equityChart(el,series){
  if(!series.length){setHTML(el,'<div class="empty">No closed trades yet - the curve starts at the first exit.</div>');return;}
  const W=Math.max(320,el.clientWidth||900),H=260,L=72,R=18,T=14,B=30,n=series.length;
  let lo=Math.min(0,...series.map(p=>p.cum)),hi=Math.max(0,...series.map(p=>p.cum));
  if(lo===hi){lo-=100;hi+=100;}
  const st=niceStep(hi-lo);lo=Math.floor(lo/st)*st;hi=Math.ceil(hi/st)*st;
  const X=i=>L+(W-L-R)*(i/n),Y=v=>T+(H-T-B)*(1-(v-lo)/(hi-lo));
  const col=series[n-1].cum>=0?'#22c55e':'#ef4444';
  let g='';for(let v=lo;v<=hi+st/2;v+=st)g+='<line class="grid" x1="'+L+'" x2="'+(W-R)+'" y1="'+Y(v).toFixed(1)+'" y2="'+Y(v).toFixed(1)+'"/><text class="ax" x="'+(L-8)+'" y="'+(Y(v)+4).toFixed(1)+'" text-anchor="end">'+inrShort(v)+'</text>';
  const pts=[[X(0),Y(0)]].concat(series.map((p,i)=>[X(i+1),Y(p.cum)]));
  const line=pts.map((p,i)=>(i?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1)).join(' ');
  const area=line+' L'+X(n).toFixed(1)+' '+Y(0).toFixed(1)+' L'+X(0).toFixed(1)+' '+Y(0).toFixed(1)+' Z';
  const k=Math.min(n,6);let xl='';const seen={};
  for(let j=0;j<=k;j++){const i=Math.round(j*n/k);if(seen[i])continue;seen[i]=1;xl+='<text class="ax" x="'+X(i).toFixed(1)+'" y="'+(H-8)+'" text-anchor="middle">#'+i+'</text>';}
  const dots=n<=200?series.map((p,i)=>'<circle class="dot" stroke="'+(p.pnl>=0?'#22c55e':'#ef4444')+'" cx="'+X(i+1).toFixed(1)+'" cy="'+Y(p.cum).toFixed(1)+'" r="3.2"><title>#'+(i+1)+'  '+esc(p.contract)+'  '+esc(p.closed)+'\ntrade '+inr(p.pnl)+'   cumulative '+inr(p.cum)+'   drawdown '+inr(p.dd)+'</title></circle>').join(''):'';
  el.innerHTML='<svg width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'">'+g+
    '<line class="zero" x1="'+L+'" x2="'+(W-R)+'" y1="'+Y(0).toFixed(1)+'" y2="'+Y(0).toFixed(1)+'"/>'+
    '<path d="'+area+'" fill="'+col+'" fill-opacity=".13"/><path d="'+line+'" fill="none" stroke="'+col+'" stroke-width="2"/>'+dots+xl+'</svg>';
  el.__h=null;
}
function statCard(k,v,c,h){return '<div class="card"><div class="k">'+k+'</div><div class="v '+(c||'')+'">'+v+'</div>'+(h?'<div class="hint">'+h+'</div>':'')+'</div>';}
function reportLong(t){return t.structure==='SINGLE'?null:(t.width?(t.type==='CALL'?t.strike+t.width:t.strike-t.width):null);}
let REPORT=null,SERIES=[];
async function refreshReport(){
  try{REPORT=await get('/api/history');}catch(e){$('#report_pnl').textContent=e.message;return;}
  const d=REPORT,st=d.stats,rows=d.rows;          // rows come oldest exit first
  $('#report_pnl').textContent='Realized P&L: '+inr(d.total_pnl);$('#report_pnl').className='big '+cls(d.total_pnl);
  let cum=0,peak=0,mdd=0,wins=0,losses=0,best=null,worst=null;SERIES=[];
  rows.forEach(t=>{const p=Number(t.pnl)||0;cum+=p;if(cum>peak)peak=cum;if(cum-peak<mdd)mdd=cum-peak;
    if(p>=0){wins++;best=best==null?p:Math.max(best,p);}else{losses++;worst=worst==null?p:Math.min(worst,p);}
    SERIES.push({cum,pnl:p,dd:cum-peak,contract:t.label+' '+t.expiry,closed:String(t.exit_time||'').slice(0,16)});});
  setHTML($('#report_stats'),
    statCard('TRADES',esc(st.trades),'',wins+' won / '+losses+' lost')+
    statCard('WIN RATE',esc(st.win_rate)+'%',st.trades?(st.win_rate>=50?'g':'r'):'')+
    statCard('AVG WIN',inr(st.avg_win,0),'g',best==null?'':'best '+inr(best,0))+
    statCard('AVG LOSS',inr(st.avg_loss,0),losses?'r':'',worst==null?'':'worst '+inr(worst,0))+
    statCard('PROFIT FACTOR',st.profit_factor==null?'-':esc(st.profit_factor),
      st.profit_factor==null?'':(st.profit_factor>=1?'g':'r'),
      st.profit_factor==null?(st.trades?'no losing trade yet':''):'gross wins / gross losses')+
    statCard('MAX DRAWDOWN',inr(mdd,0),mdd<0?'r':'','deepest fall from a peak'));
  equityChart($('#c_equity'),SERIES);
  setHTML($('#report_table'),table(['<input type="checkbox" id="rp_all">','Closed','Expiry','Spread','Entered','Credit in','Debit out','Qty','P&amp;L','Why'],
    rows.slice().reverse().map(t=>
    '<tr><td><input type="checkbox" class="rp-chk" value="'+esc(t.id)+'"></td>'+
    '<td class="mono">'+esc(String(t.exit_time||'').slice(0,16))+'</td><td>'+esc(t.expiry)+'</td>'+
    spreadCell(t.type,t.strike,reportLong(t))+
    '<td class="mono">'+esc(String(t.entry_time||'').slice(0,16))+'</td>'+
    '<td>'+num(t.credit)+'</td><td>'+num(t.debit)+'</td><td>'+esc(t.qty)+'</td>'+
    '<td class="'+cls(t.pnl)+'"><b>'+rs0(t.pnl)+'</b></td><td class="hint">'+esc(t.reason)+'</td></tr>'),'No closed trades yet.'));
}
$('#report_table').addEventListener('change',e=>{if(e.target.id==='rp_all')$$('.rp-chk').forEach(c=>c.checked=e.target.checked);});
$('#btn_report_clear').onclick=async()=>{
  const ids=$$('.rp-chk').filter(c=>c.checked).map(c=>c.value);
  if(!ids.length){alert('Tick the trades to clear first.');return;}
  if(!confirm('Remove '+ids.length+' trade(s) from the trade report?\n\nThis cannot be undone.'))return;
  try{await post('/api/history/clear',{ids});}catch(e){alert(e.message);}
  refreshReport();
};
$('#btn_report_wipe').onclick=async()=>{
  if(!confirm('Delete the entire trade history? This cannot be undone.'))return;
  try{await post('/api/history/wipe');}catch(e){alert(e.message);}
  refreshReport();
};
renderers.report=refreshReport;

/* ---------- exit check ---------- */
async function refreshExitCheck(){
  try{
    const d=await get('/api/exit-check');
    let h;
    if(!d.open_count)h='<div class="note ok">No open positions.</div>';
    else if(!d.alerts.length)h='<div class="note ok">All '+esc(d.open_count)+' open position(s) are comfortably above the '+esc(d.exit_dte)+'-day exit rule.</div>';
    else h=d.alerts.map(a=>a.critical
      ?'<div class="note crit"><b>EXIT NOW</b> - '+esc(a.label)+' ('+esc(a.expiry)+') is at DTE '+esc(a.dte)+', past the '+esc(d.exit_dte)+'-day rule.</div>'
      :'<div class="note">'+esc(a.label)+' ('+esc(a.expiry)+') hits the '+esc(d.exit_dte)+'-day rule in '+esc(a.days_until)+' day(s). DTE now '+esc(a.dte)+'.</div>').join('');
    setHTML($('#exitcheck_list'),h);
    Viz.dteLadder($('#c_ladder'),(posData&&posData.rows)||[],d.exit_dte,{label:shortLabel});
  }catch(e){setHTML($('#exitcheck_list'),'<div class="note crit">'+esc(e.message)+'</div>');}
}
renderers.exitcheck=async()=>{if(!posData)await refreshPositions();refreshExitCheck();};
$('#btn_exitcheck_refresh').onclick=async()=>{await refreshPositions();refreshExitCheck();};

/* ---------- activity ---------- */
let EV=[],KINDS=new Set(),evBusy=false;
async function refreshEvents(){
  if(evBusy)return;evBusy=true;
  try{
    const d=await get('/api/events');
    EV=d.events.slice().reverse();
    let added=false;EV.forEach(e=>{if(!KINDS.has(e.kind)){KINDS.add(e.kind);added=true;}});
    if(added){const sel=$('#a_kind'),cur=sel.value;
      sel.innerHTML='<option value="">Every kind</option>'+[...KINDS].sort().map(k=>'<option value="'+esc(k)+'">'+esc(k)+'</option>').join('');
      sel.value=cur;}
    const k=$('#a_kind').value;
    setHTML($('#events_wrap'),eventRows(k?EV.filter(e=>e.kind===k):EV));
    const s=await get('/api/pnl-series');
    const pts=(s.series||[]).map((p,i)=>[i,p[1]]);
    Viz.plot($('#c_pnlseries'),{height:190}).render('pnl'+pts.length+':'+(pts.length?pts[pts.length-1][1]:''),f=>{
      if(pts.length<2){f.empty('The scanner records a point every minute while it runs');return;}
      const last=pts[pts.length-1][1];
      f.xLinear(0,pts.length-1);
      f.yFrom(pts.map(p=>p[1]));
      f.grid();
      f.area(pts,{color:last>=0?Viz.colors.green:Viz.colors.red,opacity:0.12});
      f.line(pts,{color:last>=0?Viz.colors.green:Viz.colors.red,width:2});
      f.hline(0);
      f.axisY(Viz.fmt.money);
      f.axisX(()=>'');
    });
  }catch(e){/* transient */}
  evBusy=false;
}
$('#a_kind').onchange=()=>{const k=$('#a_kind').value;setHTML($('#events_wrap'),eventRows(k?EV.filter(e=>e.kind===k):EV));};
$('#btn_events_refresh').onclick=refreshEvents;
renderers.activity=refreshEvents;

/* ---------- settings ---------- */
const FKEYS=['min_eff','min_pop','dte_lo','dte_hi','ltp_lo','ltp_hi','wing_width','lots','exit_dte','min_credit','min_ror','min_spread_pop'];
const INTS=['wing_width','lots','exit_dte'];
let touched=false,saving=false;
$('#s_form').addEventListener('input',()=>{touched=true;});
$('#s_form').addEventListener('change',e=>{touched=true;
  if(e.target.id==='force_scan')$('#chip_force').classList.toggle('on',e.target.checked);});
function normFilters(f){
  return {min_eff:+f.min_eff,min_pop:+f.min_pop,dte_range:[+f.dte_range[0],+f.dte_range[1]],
    ltp_range:[+f.ltp_range[0],+f.ltp_range[1]],wing_width:+f.wing_width,lots:+f.lots,exit_dte:+f.exit_dte,
    min_credit:+(f.min_credit||0),min_ror:+(f.min_ror||0),min_spread_pop:+(f.min_spread_pop||0)};
}
function paintSettings(s){
  $('#s_lock').hidden=!(s.scanning_active&&s.scanner_owner);
  if(touched)return;                   // never overwrite what he is typing
  const f=s.filters,v={min_eff:f.min_eff,min_pop:f.min_pop,dte_lo:f.dte_range[0],dte_hi:f.dte_range[1],
    ltp_lo:f.ltp_range[0],ltp_hi:f.ltp_range[1],wing_width:f.wing_width,lots:f.lots,exit_dte:f.exit_dte,
    min_credit:f.min_credit,min_ror:f.min_ror,min_spread_pop:f.min_spread_pop};
  FKEYS.forEach(k=>{const el=$('#f_'+k);if(el&&v[k]!=null)el.value=v[k];});
  $('#force_scan').checked=!!s.force_scan;$('#chip_force').classList.toggle('on',!!s.force_scan);
}
function readForm(){
  const v={};
  for(const k of FKEYS){
    const el=$('#f_'+k),t=el.value.trim(),lab=el.closest('.fl').querySelector('label').textContent.trim();
    if(t===''||isNaN(Number(t))){alert(lab+' is empty or not a number.');el.focus();return null;}
    const n=Number(t);
    if(el.min!==''&&n<Number(el.min)){alert(lab+' must be at least '+el.min+'.');el.focus();return null;}
    if(el.max!==''&&n>Number(el.max)){alert(lab+' must be at most '+el.max+'.');el.focus();return null;}
    if(INTS.includes(k)&&!Number.isInteger(n)){alert(lab+' must be a whole number.');el.focus();return null;}
    v[k]=n;
  }
  if(v.wing_width%50){alert('Hedge wing width must be a multiple of 50 points.');$('#f_wing_width').focus();return null;}
  if(v.dte_lo>v.dte_hi){alert('Entry DTE "from" is above "to".');$('#f_dte_lo').focus();return null;}
  if(v.ltp_lo>v.ltp_hi){alert('Short leg LTP "from" is above "to".');$('#f_ltp_lo').focus();return null;}
  // Same payload the old sidebar posted, plus the three extra spread filters
  // the endpoint has always accepted.
  return {min_eff:v.min_eff,min_pop:v.min_pop,dte_range:[v.dte_lo,v.dte_hi],ltp_range:[v.ltp_lo,v.ltp_hi],
    wing_width:v.wing_width,lots:v.lots,exit_dte:v.exit_dte,
    min_credit:v.min_credit,min_ror:v.min_ror,min_spread_pop:v.min_spread_pop};
}
$('#b_save').onclick=async()=>{
  if(saving)return;
  // A "Saved at ..." from an earlier press must not survive this one - it is only
  // true again once this save succeeds.
  $('#s_saved').textContent='';
  const body=readForm();if(!body)return;
  if(!S){alert('Still loading - try again in a moment.');return;}
  const fChanged=JSON.stringify(normFilters(body))!==JSON.stringify(normFilters(S.filters));
  const force=$('#force_scan').checked,forceChanged=force!==!!S.force_scan;
  saving=true;$('#b_save').disabled=true;
  try{
    if(fChanged){
      // The server only accepts new filters while the scanner is stopped, so
      // a running scanner is stopped, the filters saved, and it is started again.
      // Ask the server first: the launch-time auto-start may have switched the
      // scanner on since the last poll.
      try{S=await get('/api/status');}catch(e){}
      const restart=S.scanning_active&&S.scanner_owner;
      if(restart&&!confirm('The scanner is running, and filters can only change while it is stopped.\n\nStop it, save the new filters and start it again?'))return;
      if(restart)await post('/api/scanner/stop');
      try{await post('/api/filters',body);}
      catch(e){if(restart){try{await post('/api/scanner/start');}catch(_){}}throw e;}
      if(restart){
        try{await post('/api/scanner/start');}
        catch(e){alert('Filters saved, but the scanner could not start again: '+e.message+'\n\nPress Start once that is fixed.');}
      }
    }
    if(forceChanged)await post('/api/scanner/force',{on:force});
    touched=false;
    $('#s_saved').textContent=(fChanged||forceChanged)?'Saved at '+new Date().toLocaleTimeString():'Nothing changed.';
  }catch(e){$('#s_saved').textContent='Not saved.';alert(e.message);}
  finally{saving=false;$('#b_save').disabled=false;poll();}
};
$('#b_revert').onclick=()=>{touched=false;$('#s_saved').textContent='';if(S)paintSettings(S);poll();};

function paintToken(t){
  $('#tok_human').textContent=t.human;$('#tok_human').className='v '+(t.expired?'r':(t.warn?'o':'g'));
  $('#tok_source').textContent=t.source;
  $('#tok_client').textContent=t.client_id||'-';
  $('#tok_masked').textContent=t.masked?'Current: '+t.masked+(t.exp_ist?'   expires '+t.exp_ist:''):'';
  const hub=!!t.env_pinned;
  $('#tok_hub').hidden=!hub;$('#tok_form').hidden=hub;$('#btn_tok_save').hidden=hub;
  setHTML($('#tok_banner'),tokenBanner(t));
}
async function refreshToken(){try{paintToken(await get('/api/token'));}catch(e){}}
renderers.settings=refreshToken;
$('#btn_tok_save').onclick=async()=>{
  const token=$('#tok_input').value.trim();
  if(!token){alert('Paste a token first.');return;}
  $('#tok_spinner').hidden=false;
  try{
    await post('/api/token',{token,client_id:$('#tok_client_input').value.trim()});
    $('#tok_input').value='';
    $('#tok_result').textContent='Saved.';$('#tok_result').className='hint g';
    await refreshToken();await poll();
  }catch(e){$('#tok_result').textContent=e.message;$('#tok_result').className='hint r';}
  finally{$('#tok_spinner').hidden=true;}
};
$('#btn_tok_test').onclick=async()=>{
  $('#tok_spinner').hidden=false;$('#tok_result').textContent='Testing...';$('#tok_result').className='hint';
  try{
    const d=await post('/api/token/test');
    $('#tok_result').textContent=(d.ok?'OK - ':'FAILED - ')+d.detail+' ('+d.ms+' ms)';
    $('#tok_result').className='hint '+(d.ok?'g':'r');
    await refreshToken();
  }catch(e){$('#tok_result').textContent=e.message;$('#tok_result').className='hint r';}
  finally{$('#tok_spinner').hidden=true;}
};

/* ---------- controls ---------- */
$('#b_start').onclick=async()=>{$('#b_start').disabled=true;try{await post('/api/scanner/start');}catch(e){alert(e.message);}poll();};
$('#b_stop').onclick=async()=>{$('#b_stop').disabled=true;try{await post('/api/scanner/stop');}catch(e){alert(e.message);}poll();};

/* ---------- boot ---------- */
showTab(store.get('cs_tab')||'dashboard',true);
poll();setInterval(poll,5000);
setInterval(()=>{if(TAB==='positions')refreshPositions();},180000);
setInterval(()=>{if(TAB==='report')refreshReport();},20000);
window.addEventListener('resize',()=>{
  if(TAB==='report'&&REPORT)equityChart($('#c_equity'),SERIES);
  if(TAB==='dashboard'&&chainData)drawChain();
});
</script></body></html>

"""


LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sign in - NIFTY Paper Trading</title>
<style>
:root{--bg:#0b0e14;--panel:#121722;--p2:#171d2b;--bd:#222a3b;--bd2:#2e3850;
 --tx:#cbd5e1;--br:#f1f5f9;--mu:#7c8aa3;--m2:#56627a;--ac:#38bdf8;--gn:#22c55e;--rd:#ef4444;--or:#f59e0b}
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:var(--bg);color:var(--tx);font:14px/1.5 'Segoe UI',system-ui,sans-serif}
.wrap{min-height:100%;display:flex;align-items:center;justify-content:center;padding:24px 16px}
.box{width:100%;max-width:360px;background:var(--panel);border:1px solid var(--bd);border-radius:12px;padding:26px 22px}
h1{margin:0 0 4px;font-size:18px;color:var(--br)}
.sub{color:var(--mu);font-size:12px;margin-bottom:18px}
label{display:block;font-size:12px;color:var(--mu);margin-bottom:6px}
input{width:100%;background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:9px 11px;color:var(--br);font:inherit}
input:focus{outline:none;border-color:var(--ac)}
button{width:100%;margin-top:14px;border:0;border-radius:8px;padding:10px 16px;cursor:pointer;
  background:var(--gn);color:#04210f;font:inherit;font-weight:600}
button:hover{filter:brightness(1.15)} button:disabled{opacity:.45;cursor:default}
.err{margin-top:12px;color:#fca5a5;font-size:12px;text-align:center}
.foot{margin-top:16px;color:var(--m2);font-size:12px;text-align:center}
</style></head><body>
<div class="wrap"><form class="box" method="POST" autocomplete="off">
  <h1>NIFTY Credit Spreads</h1>
  <div class="sub">Private dashboard - sign in to continue</div>
  <label>PASSWORD</label>
  <input type="password" name="password" autofocus autocomplete="current-password"
         {% if locked %}disabled{% endif %}>
  <button type="submit" {% if locked %}disabled{% endif %}>SIGN IN</button>
  {% if error %}<div class="err">{{ error }}</div>{% endif %}
  <div class="foot">Sessions last 30 days on this device.</div>
</form></div></body></html>"""


# ─────────────────────────────────────────────────────────────────────────────
#  PROCESS MODEL
#  The old code called Thread(...).start() at module scope.  Under any
#  multi-process server that is N independent scanners deploying the same trades
#  into the same JSON file, with no cross-process lock — three of four workers
#  lose their positions on every save.  Start once, and hold an OS-level lock so
#  a second process serves the UI read-only instead of double-trading.
# ─────────────────────────────────────────────────────────────────────────────
_bg_lock = threading.Lock()
_bg_started = False
_lock_handle = None


def _acquire_scanner_lock():
    global _lock_handle
    try:
        f = open(LOCK_FILE, "a+b")
        f.seek(0)
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        f.write(str(os.getpid()).encode())
        f.flush()
        _lock_handle = f
        return True
    except Exception:
        return False


def start_background_once():
    global _bg_started
    with _bg_lock:
        if _bg_started:
            return False
        _bg_started = True
    if not _acquire_scanner_lock():
        STATE.scanner_owner = False
        STATE.status_message = "Read-only: another instance owns the scanner."
        log_event("boot", "scanner lock held elsewhere; pid %d serves the UI only" % os.getpid())
        return False
    STATE.scanner_owner = True
    # Launched = scanning.  Whatever scanning_active was saved last time does
    # not decide it any more: the scanner loop turns it on as soon as the token
    # allows (maybe_autostart), and Stop turns it off until Start is pressed.
    with STATE.lock:
        STATE.scanning_active = False
        STATE.autostart = True
    threading.Thread(target=boot_loop, name="boot", daemon=True).start()
    threading.Thread(target=scanner_loop, name="scanner", daemon=True).start()
    log_event("boot", "started (pid %d, DATA_DIR=%s, auth=%s)"
              % (os.getpid(), DATA_DIR, "on" if AUTH_ON else "off"))
    return True


def _graceful(*_a):
    if _SHUTDOWN.is_set():
        return
    _SHUTDOWN.set()
    try:
        with STATE.lock:
            STATE.save()
    except Exception:
        pass


atexit.register(_graceful)
for _sig in ("SIGTERM", "SIGINT"):
    if hasattr(signal, _sig):
        try:
            signal.signal(getattr(signal, _sig), lambda *a: (_graceful(), sys.exit(0)))
        except (ValueError, OSError):
            pass

start_background_once()


# ─────────────────────────────────────────────────────────────────────────────
#  MARGIN FOR NIFTY TRADER'S HOME SCREEN
#  hub_summary() is read by the hub (through its /__hub__/status call) to show
#  each strategy's margin on one screen.  Local arithmetic only - no API calls.
#    margin_used      Rs blocked by the open positions now
#    margin_next      Rs one new trade needs (lowest candidate), margin_next_max the highest
# ─────────────────────────────────────────────────────────────────────────────
def hub_summary():
    with STATE.lock:
        pos = list(STATE.paper_positions)
        scan = list(STATE.last_scan.values())
    used = 0.0
    for p in pos:
        try:
            used += _f(spread_margin(p).get("margin"))
        except Exception:
            pass
    nxt = [_f(m.get("Margin")) for m in scan if _f(m.get("Margin")) > 0]
    return {"margin_used": round(used), "open": len(pos),
            "margin_next": round(min(nxt)) if nxt else None,
            "margin_next_max": round(max(nxt)) if nxt else None,
            "basis": "hedged credit spread: SPAN + exposure estimate (+/-15%)"}


def _pnl_summary(margin_used):
    today = now_ist().strftime("%Y-%m-%d")
    with STATE.lock:
        hist = list(STATE.trade_history)
        open_pnl = STATE.pnl_series[-1][1] if (STATE.paper_positions and STATE.pnl_series) else 0.0
    rows_today = [r for r in hist if str(r.get("Exit_Time") or "").startswith(today)]
    return _pnl_pack(rows_today, hist, lambda r: _f(r.get("Realized_PnL")),
                     lambda r: _f(spread_margin(r).get("margin")), _f(open_pnl), margin_used)


# P&L for the hub's home screen: today, open, all-time, and % profit (P&L as a
# % of the margin/capital the trades used; open P&L as a % of margin blocked).
def _pnl_pack(today_rows, all_rows, pnl_of, cap_of, open_pnl, margin_used):
    def pct(p, c):
        return round(100.0 * p / c, 2) if c > 0 else None
    t = sum(pnl_of(r) for r in today_rows)
    a = sum(pnl_of(r) for r in all_rows)
    return {"pnl_today": round(t), "pnl_all": round(a), "pnl_open": round(open_pnl),
            "pct_today": pct(t, sum(cap_of(r) for r in today_rows)),
            "pct_all": pct(a, sum(cap_of(r) for r in all_rows)),
            "pct_open": pct(open_pnl, margin_used),
            "trades_today": len(today_rows), "trades_all": len(all_rows)}


_margin_summary = hub_summary


def hub_summary():
    out = _margin_summary()
    try:
        out.update(_pnl_summary(out.get("margin_used") or 0))
    except Exception as e:                 # P&L must never break the margin figures
        out["pnl_error"] = "%s: %s" % (e.__class__.__name__, e)
    return out


if __name__ == "__main__":
    port = int(_f(_env("PORT", "5000"), 5000))
    host = _env("HOST") or ("0.0.0.0" if _env("APP_ENV") == "hosted" else "127.0.0.1")
    print("\n  NIFTY credit-spread dashboard  ->  http://%s:%d\n" % (host, port), flush=True)
    app.run(host=host, port=port, debug=False, threaded=True, use_reloader=False)


# ─────────────────────────────────────────────────────────────────────────────
#  HOSTING IT SO IT RUNS WITHOUT YOUR LAPTOP
#
#  The single worker is the design, not a compromise: one process owns the state
#  file and the scanner.  Threads give the browser concurrency.  Never raise -w
#  above 1, and never add --preload (threads do not survive fork).
#
#      pip install flask requests gunicorn
#      gunicorn -w 1 -k gthread --threads 8 -t 180 -b 0.0.0.0:$PORT trading_web_app:app
#
#  Required env vars on the host:
#      DATA_DIR=/var/data        a mounted disk, or the state is wiped on deploy
#      DHAN_CLIENT_ID=...
#      APP_PASSWORD=...          anything reachable from the internet needs this
#      APP_ENV=hosted  COOKIE_SECURE=1  TRUST_PROXY=1
#  Deliberately do NOT set DHAN_ACCESS_TOKEN — the environment outranks the
#  Settings tab, which would make pasting a token there a silent no-op.
# ─────────────────────────────────────────────────────────────────────────────
