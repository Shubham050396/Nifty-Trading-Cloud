"""
NIFTY Option Scalper — IVX-G  (Implied-Vol Expansion, Gamma-Feasible)
=====================================================================

A SECOND, SEPARATE app from trading_web_app.py.  Different port, different data
folder, its own state.  Nothing is shared.

    python scalper_app.py        ->  http://127.0.0.1:5001

Strategy in one line: buy a single ATM NIFTY option only when implied volatility
is EXPANDING, direction agrees across three independent reads, and gamma makes
the target physically reachable before theta eats the stop.

READ THIS BEFORE YOU TRADE IT
-----------------------------
The Rs 3,000 target / Rs 1,000 stop pair is NOT a 3:1 edge.  On lot 65 that is
+46.15 / -15.38 premium points.  For a driftless option the probability of
touching the target before the stop is 15.38 / (46.15 + 15.38) = 25.0%, which is
exactly the breakeven win rate for 3:1.  Gamma convexity lifts it to roughly 30%;
theta pushes it back down; costs (spread, brokerage, STT, 4-second sampling
overshoot) take roughly another 4 points of win rate.

    0 DTE   ~18% expected hit rate   ->  decisively negative
    1 DTE   ~24%                     ->  below breakeven
    4-7 DTE ~25%                     ->  a coin flip, minus costs

The ONLY term that can pay for the trade is IV expansion, through vega.  At 4 DTE
one vol point is worth about Rs 679 on a lot, so a +2 vol move hands you Rs 1,357
of the Rs 3,000 target with no index move at all.  That is why the entry is
primarily an IV filter, why 0-DTE is OFF by default, and why the app refuses to
trade when IV is falling.

This is paper trading.  Run it for a few weeks and read your own hit rate off the
Trade tape before you consider anything else.

Requires: pip install flask requests
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
import statistics
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

try:
    from zoneinfo import ZoneInfo
    IST = ZoneInfo("Asia/Kolkata")
except Exception:
    IST = timezone(timedelta(hours=5, minutes=30), "IST")


def now_ist():
    return datetime.now(IST)


def ts_now():
    return now_ist().strftime("%Y-%m-%d %H:%M:%S")


APP_DIR = os.path.dirname(os.path.abspath(__file__))


def _env(name, default=None):
    v = os.environ.get(name)
    if v is None:
        return default
    v = v.strip()
    return v if v else default


DATA_DIR = _env("SCALP_DATA_DIR") or os.path.join(APP_DIR, "data_scalp")
os.makedirs(DATA_DIR, exist_ok=True)

STATE_FILE = os.path.join(DATA_DIR, "scalp_state.json")
RUNTIME_FILE = os.path.join(DATA_DIR, "runtime.json")
SECRET_FILE = os.path.join(DATA_DIR, "secret_key")
AUTH_FILE = os.path.join(DATA_DIR, "auth.json")
LOCK_FILE = os.path.join(DATA_DIR, "scalper.lock")
SCRIP_CACHE = os.path.join(DATA_DIR, "scrip_nifty.json")
TRADES_REMOVED_FILE = os.path.join(DATA_DIR, "trades_removed.jsonl")

UNDERLYING_SYM = "NIFTY"
UNDERLYING_SCRIP = 13
UNDERLYING_SEG = "IDX_I"
EXCHANGE_SEGMENT = "NSE_FNO"
# INTRADAY, not MARGIN: a scalp is squared off the same session and intraday
# product gets the lower margin. The credit-spread app uses MARGIN because those
# are carry-forward positions.
PRODUCT_TYPE = "INTRADAY"
ORDER_TYPE = "LIMIT"
VALIDITY = "DAY"
SCHEMA_VERSION = 1

TRADING_MINUTES_PER_DAY = 375.0     # NOT 1440 — decay is realised in-session

DEFAULTS = {
    # ---- exits (his spec; points are derived from rupees / lot at runtime) ----
    "target_rupees": 3000.0,
    "stop_rupees": 1000.0,
    "lots": 1,
    # ---- cadence ----
    "poll_interval": 4.0,
    "fast_window": 15,              # 60 s
    "slow_window": 75,              # 300 s
    "buffer_cap": 450,              # 30 min
    # ---- gate A: IV expansion ----
    "iv_slope_min": 0.08,           # vol points per minute
    "iv_z_min": 0.50,
    # ---- gate B: direction ----
    "rr_delta_min": 0.10,           # vol points vs its own 5-min mean
    "basis_slope_min": 0.30,        # index points per minute
    # ---- gate C: feasibility ----
    "x_target_max": 95.0,           # index points
    "gamma_min": 0.0008,
    "need_sigma_max": 2.2,
    "sigma_min_floor": 4.0,         # index pts/min
    "sigma_min_ceil": 25.0,
    # ---- gate D: liquidity ----
    "spread_abs_max": 0.80,
    "spread_pct_max": 0.012,
    "depth_lots_min": 5,
    "cost_frac_of_risk": 0.08,
    "min_premium_mult": 1.6,        # mid >= 1.6 x target points
    # ---- gate E: theta ----
    "theta_frac_of_stop": 0.30,
    # ---- exit tuning ----
    "time_stop_min": 5,
    "time_stop_max": 40,
    "trail_arm_frac": 0.50,
    "trail_giveback": 12.0,
    "trail_floor": 2.0,
    "signal_decay_slope": -0.10,
    "signal_decay_profit_pts": 15.0,
    # ---- expiry selection ----
    "allow_zero_dte": False,
    "dte_min": 1,
    "dte_max": 7,
    # ---- risk engine ----
    "daily_loss_cap": 3000.0,
    "daily_profit_stop": 6000.0,
    "max_trades": 6,
    "cooldown_stop_1": 300,
    "cooldown_stop_2": 900,
    "cooldown_win": 60,
    "max_consecutive_stops": 3,
    "max_concurrent": 1,
    "lunch_block": False,
    # ---- costs, so paper P&L is not a fantasy ----
    "cost_per_trade": 75.0,         # brokerage + STT + exch + GST + stamp, round trip
    "slippage_extra_pts": 0.0,      # added on top of the real bid at exit
}

# no-entry clock windows (IST)
OPEN_NOISE_END = dtime(9, 25)
LUNCH_START, LUNCH_END = dtime(12, 30), dtime(13, 15)
NO_NEW_ENTRY_AFTER = dtime(15, 0)
HARD_FLAT = dtime(15, 20)
HALT_ALL = dtime(15, 25)
MKT_OPEN, MKT_CLOSE = dtime(9, 15), dtime(15, 30)

STALE_SEC = 12.0
DATA_LOSS_SEC = 120.0
BUFFER_GAP_SEC = 15.0


# ─────────────────────────────────────────────────────────────────────────────
#  EVENTS / PERSISTENCE
# ─────────────────────────────────────────────────────────────────────────────
_events = deque(maxlen=800)
_events_lock = threading.Lock()
_event_seq = itertools.count(1)
_JWT_RE = re.compile(r"eyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]+")


def _scrub(t):
    return _JWT_RE.sub("<token-redacted>", str(t))


def log_event(kind, msg):
    ev = {"id": next(_event_seq), "ts": ts_now(), "epoch": time.time(),
          "kind": kind, "msg": _scrub(msg)[:400]}
    with _events_lock:
        _events.append(ev)
    print("[%s] %-9s %s" % (ev["ts"], kind.upper(), ev["msg"]), flush=True)


def recent_events(since=0, limit=250):
    with _events_lock:
        return [e for e in _events if e["id"] > since][-limit:]


def write_json_atomic(path, obj, backups=3, private=False):
    folder = os.path.dirname(os.path.abspath(path)) or "."
    os.makedirs(folder, exist_ok=True)
    payload = json.dumps(obj, indent=2, default=str).encode("utf-8")
    if backups and os.path.exists(path):
        try:
            for i in range(backups, 1, -1):
                nx = "%s.bak.%d" % (path, i - 1)
                if os.path.exists(nx):
                    os.replace(nx, "%s.bak.%d" % (path, i))
            shutil.copy2(path, path + ".bak.1")
        except OSError:
            pass
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
            with open(cand, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            continue
    return default


# ─────────────────────────────────────────────────────────────────────────────
#  CREDENTIALS  (same precedence as the other app, separate runtime file)
# ─────────────────────────────────────────────────────────────────────────────
try:
    import config as _config
except Exception:
    _config = None


def _cfg(n):
    return getattr(_config, n, None) if _config is not None else None


_rt_lock = threading.RLock()
_rt_cache = None


def runtime_read():
    global _rt_cache
    with _rt_lock:
        if _rt_cache is None:
            _rt_cache = read_json_safe(RUNTIME_FILE, default={}) or {}
        return dict(_rt_cache)


def runtime_write(**kw):
    global _rt_cache
    with _rt_lock:
        d = runtime_read()
        d.update(kw)
        write_json_atomic(RUNTIME_FILE, d, private=True)
        _rt_cache = d
        return dict(d)


class Creds:
    __slots__ = ("client_id", "token", "source", "env_pinned")

    def __init__(self, c, t, s, p):
        self.client_id, self.token, self.source, self.env_pinned = c, t, s, p


def resolve_credentials():
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


def decode_jwt_unverified(token):
    if not token:
        return None, "no token"
    p = token.split(".")
    if len(p) != 3:
        return None, "not a JWT"
    try:
        raw = p[1].encode("ascii")
        raw += b"=" * (-len(raw) % 4)
        return json.loads(base64.urlsafe_b64decode(raw).decode("utf-8", "replace")), None
    except Exception as e:
        return None, e.__class__.__name__


def mask_token(t):
    return "" if not t else ("*" * len(t) if len(t) <= 16
                             else "%s...%s (%d chars)" % (t[:8], t[-6:], len(t)))


def _human_delta(s):
    s = int(s)
    if s <= 0:
        return "expired"
    h, r = divmod(s, 3600)
    return "%dd %dh" % (h // 24, h % 24) if h >= 24 else "%dh %dm" % (h, r // 60)


def token_status():
    c = resolve_credentials()
    out = {"configured": bool(c.token), "source": c.source, "env_pinned": c.env_pinned,
           "masked": mask_token(c.token), "client_id": c.client_id,
           "human": "not configured", "expired": True, "warn": True, "exp_ist": None}
    if not c.token:
        return out
    payload, err = decode_jwt_unverified(c.token)
    if err:
        out["human"] = "unreadable (%s)" % err
        return out
    exp = payload.get("exp")
    if not isinstance(exp, (int, float)):
        out.update(human="no exp claim", expired=False)
        return out
    left = exp - time.time()
    out["exp_ist"] = datetime.fromtimestamp(exp, IST).strftime("%Y-%m-%d %H:%M IST")
    out["expired"] = left <= 0
    out["warn"] = left < 2 * 3600
    out["human"] = ("EXPIRED %s ago" % _human_delta(-left)) if left <= 0 \
        else "expires in %s" % _human_delta(left)
    return out


# ─────────────────────────────────────────────────────────────────────────────
#  DHAN
# ─────────────────────────────────────────────────────────────────────────────
DHAN_BASE = "https://api.dhan.co/v2"
_HTTP = requests.Session()
_HTTP.headers.update({"Accept": "application/json"})
_api_gate = threading.Lock()
_api_last = [0.0]
MIN_API_INTERVAL = 3.1


def call_dhan(endpoint, payload=None, method="POST", timeout=15):
    c = resolve_credentials()
    if not c.token:
        return {"status": "error", "_http": 0, "message": "No access token."}
    headers = {"access-token": c.token, "client-id": c.client_id,
               "Content-Type": "application/json", "Accept": "application/json"}
    url = "%s/%s" % (DHAN_BASE, str(endpoint).lstrip("/"))
    try:
        if method.upper() == "GET":
            r = _HTTP.get(url, headers=headers, timeout=timeout)
        else:
            r = _HTTP.post(url, headers=headers, json=(payload or {}), timeout=timeout)
    except requests.RequestException as e:
        return {"status": "error", "_http": 0, "message": str(e)}
    if r.status_code in (401, 403):
        log_event("token", "%s -> HTTP %d, broker rejected the token" % (endpoint, r.status_code))
        return {"status": "error", "_http": r.status_code, "message": "Auth failed."}
    if r.status_code == 429:
        return {"status": "error", "_http": 429, "message": "rate limited"}
    try:
        d = r.json()
    except ValueError:
        return {"status": "error", "_http": r.status_code, "message": "non-JSON"}
    if not isinstance(d, dict):
        return {"status": "error", "_http": r.status_code, "message": "bad payload"}
    if r.status_code >= 400:
        d.setdefault("status", "error")
        d["message"] = d.get("errorMessage") or d.get("message") or "HTTP %d" % r.status_code
    d["_http"] = r.status_code
    return d


def throttled_chain(expiry):
    with _api_gate:
        wait = MIN_API_INTERVAL - (time.time() - _api_last[0])
        if wait > 0:
            time.sleep(wait)
        res = call_dhan("optionchain", {"UnderlyingScrip": UNDERLYING_SCRIP,
                                        "UnderlyingSeg": UNDERLYING_SEG,
                                        "Expiry": expiry})
        _api_last[0] = time.time()
    return res


def fetch_expiry_list():
    r = call_dhan("optionchain/expirylist",
                  {"UnderlyingScrip": UNDERLYING_SCRIP, "UnderlyingSeg": UNDERLYING_SEG})
    return [str(x)[:10] for x in (r.get("data") or [])] if r.get("status") == "success" else []


# ─────────────────────────────────────────────────────────────────────────────
#  MATH
# ─────────────────────────────────────────────────────────────────────────────
def _f(x, d=0.0):
    try:
        v = float(x)
        return d if (math.isnan(v) or math.isinf(v)) else v
    except (TypeError, ValueError):
        return d


def expiry_dt(e):
    y, m, d = (int(x) for x in str(e)[:10].split("-"))
    return datetime(y, m, d, 15, 30, tzinfo=IST)


def dte_of(e, now=None):
    return int(math.floor((expiry_dt(e) - (now or now_ist())).total_seconds() / 86400.0))


def ols_slope(ys, dt_min):
    """Slope per minute of an evenly spaced series."""
    n = len(ys)
    if n < 8 or dt_min <= 0:
        return None
    xs = [i * dt_min for i in range(n)]
    mx, my = sum(xs) / n, sum(ys) / n
    den = sum((x - mx) ** 2 for x in xs)
    if den <= 0:
        return None
    return sum((xs[i] - mx) * (ys[i] - my) for i in range(n)) / den


def zscore(v, series):
    if len(series) < 8:
        return None
    m = statistics.fmean(series)
    try:
        s = statistics.stdev(series)
    except statistics.StatisticsError:
        return None
    return None if s <= 1e-9 else (v - m) / s


def interp_atm_iv(chain, spot):
    """Linear interpolation of (CE_IV + PE_IV)/2 at exactly spot, between the two
    bracketing strikes.  Using the nearest strike instead makes the series jump
    0.3-0.8 vol every time spot crosses a 50-point boundary, which fires the
    slope gate on nothing at all."""
    ks = sorted(chain)
    if not ks:
        return None
    lo = [k for k in ks if k <= spot]
    hi = [k for k in ks if k >= spot]
    if not lo or not hi:
        return None
    k0, k1 = lo[-1], hi[0]

    def mid_iv(k):
        row = chain.get(k) or {}
        ce = _f((row.get("ce") or {}).get("implied_volatility"))
        pe = _f((row.get("pe") or {}).get("implied_volatility"))
        vals = [v for v in (ce, pe) if v > 0]
        return sum(vals) / len(vals) if vals else None

    v0, v1 = mid_iv(k0), mid_iv(k1)
    if v0 is None or v1 is None:
        return v0 if v1 is None else v1
    if k1 == k0:
        return v0
    w = (spot - k0) / (k1 - k0)
    return v0 + w * (v1 - v0)


def risk_reversal(chain):
    """IV(25-delta call) - IV(25-delta put).  The ATM CE-vs-PE IV difference is
    NOT a directional tell — put-call parity forces them nearly equal and the
    residual is a forward-basis artefact."""
    best_c = best_p = None
    for k, row in chain.items():
        ce, pe = row.get("ce") or {}, row.get("pe") or {}
        cd = abs(_f((ce.get("greeks") or {}).get("delta")))
        pd = abs(_f((pe.get("greeks") or {}).get("delta")))
        civ, piv = _f(ce.get("implied_volatility")), _f(pe.get("implied_volatility"))
        if civ > 0 and cd > 0:
            e = abs(cd - 0.25)
            if best_c is None or e < best_c[0]:
                best_c = (e, civ)
        if piv > 0 and pd > 0:
            e = abs(pd - 0.25)
            if best_p is None or e < best_p[0]:
                best_p = (e, piv)
    if not best_c or not best_p:
        return None
    return best_c[1] - best_p[1]


def synthetic_basis(chain, spot):
    """K_atm + mid(CE) - mid(PE) - spot.  A cleaner directional read than spot
    alone because it is where the option market is pricing the forward."""
    if not chain:
        return None
    katm = min(chain, key=lambda k: abs(k - spot))
    row = chain.get(katm) or {}
    ce, pe = row.get("ce") or {}, row.get("pe") or {}

    def mid(q):
        b, a = _f(q.get("top_bid_price")), _f(q.get("top_ask_price"))
        if b > 0 and a >= b:
            return (a + b) / 2.0
        return _f(q.get("last_price"))

    c, p = mid(ce), mid(pe)
    if c <= 0 or p <= 0:
        return None
    return katm + c - p - spot


def x_for_premium(delta, gamma, dprem):
    """Index move needed for a given premium move, solving dP = d*x + 0.5*g*x^2."""
    d, g = abs(_f(delta)), abs(_f(gamma))
    if g <= 1e-12:
        return abs(dprem) / d if d > 1e-9 else None
    disc = d * d + 2 * g * dprem
    if disc < 0:
        return None
    return (-d + math.sqrt(disc)) / g


def x_for_stop(delta, gamma, dprem):
    d, g = abs(_f(delta)), abs(_f(gamma))
    if g <= 1e-12:
        return abs(dprem) / d if d > 1e-9 else None
    disc = d * d - 2 * g * dprem
    if disc < 0:
        return abs(dprem) / d if d > 1e-9 else None
    return (d - math.sqrt(disc)) / g


# ─────────────────────────────────────────────────────────────────────────────
#  SCRIP MASTER  (lot size and security ids — never hard-code 65)
# ─────────────────────────────────────────────────────────────────────────────
SCRIP_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"


def load_scrip_lookup():
    today = now_ist().strftime("%Y-%m-%d")
    cached = read_json_safe(SCRIP_CACHE, default=None)
    if isinstance(cached, dict) and cached.get("date") == today and cached.get("map"):
        return cached["map"]
    try:
        r = requests.get(SCRIP_URL, timeout=120)
        r.raise_for_status()
        lookup = {}
        for row in csv.DictReader(io.StringIO(r.text)):
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
            opt = "CALL" if row.get("SEM_OPTION_TYPE") == "CE" else "PUT"
            lookup["%s_%.1f_%s" % ((row.get("SEM_EXPIRY_DATE") or "")[:10], strike, opt)] = {
                "sec_id": str(row.get("SEM_SMST_SECURITY_ID", "")).strip(),
                "lot": lot, "tsym": tsym}
        if not lookup:
            raise ValueError("no NIFTY rows")
        write_json_atomic(SCRIP_CACHE, {"date": today, "map": lookup}, backups=1)
        log_event("boot", "scrip master: %d NIFTY contracts" % len(lookup))
        return lookup
    except Exception as e:
        log_event("error", "scrip master failed: %s" % e)
        if isinstance(cached, dict) and cached.get("map"):
            return cached["map"]
        return {}


def get_mapping(expiry, strike, opt_type):
    t = "CALL" if str(opt_type).upper() in ("CE", "CALL") else "PUT"
    return STATE.scrip_lookup.get("%s_%.1f_%s" % (str(expiry)[:10], float(strike), t))


def nifty_lot():
    """Read the real lot from the scrip master; fall back only for display."""
    for v in STATE.scrip_lookup.values():
        return int(v.get("lot") or 65)
    return 65


# ─────────────────────────────────────────────────────────────────────────────
#  SNAPSHOT BUFFER
# ─────────────────────────────────────────────────────────────────────────────
class Buffer:
    """Rolling window of chain snapshots.  Slopes are never regressed across a
    hole: any gap over BUFFER_GAP_SEC clears it and forces a re-warm."""

    def __init__(self):
        self.lock = threading.RLock()
        self.buf = deque(maxlen=DEFAULTS["buffer_cap"])
        self.discontinuities = 0

    def add(self, snap):
        with self.lock:
            if self.buf and snap["ts"] - self.buf[-1]["ts"] > BUFFER_GAP_SEC:
                self.buf.clear()
                self.discontinuities += 1
                log_event("data", "buffer gap > %ds - cleared, re-warming" % BUFFER_GAP_SEC)
            self.buf.append(snap)

    def clear(self, why=""):
        with self.lock:
            self.buf.clear()
        if why:
            log_event("data", "buffer cleared: %s" % why)

    def tail(self, n):
        with self.lock:
            return list(self.buf)[-n:]

    def warm(self):
        with self.lock:
            if len(self.buf) < DEFAULTS["slow_window"]:
                return False
            return (self.buf[-1]["ts"] - self.buf[0]["ts"]) >= 270.0

    def age(self):
        with self.lock:
            return (time.time() - self.buf[-1]["ts"]) if self.buf else 1e9

    def size(self):
        with self.lock:
            return len(self.buf)


BUF = Buffer()


def build_snapshot(expiry, res):
    """One chain response -> everything the signal and the marker both need."""
    if res.get("status") != "success":
        return None
    data = res.get("data") or {}
    spot = _f(data.get("last_price"))
    raw = data.get("oc") or {}
    if spot <= 0 or not raw:
        return None
    chain = {}
    for k, v in raw.items():
        try:
            chain[round(float(k), 2)] = v or {}
        except (TypeError, ValueError):
            continue
    if not chain:
        return None
    return {"ts": time.time(), "expiry": expiry, "spot": spot, "chain": chain,
            "iv_atm": interp_atm_iv(chain, spot), "rr": risk_reversal(chain),
            "basis": synthetic_basis(chain, spot)}


def quote_at(snap, strike, side):
    """side 'ce'|'pe'.  IV stays in VOL POINTS here (12.5, not 0.125) — the
    opposite of the credit-spread app. Do not copy that convention across."""
    row = (snap.get("chain") or {}).get(round(_f(strike), 2))
    if not row:
        return None
    q = row.get(side)
    if not isinstance(q, dict):
        return None
    g = q.get("greeks") or {}
    bid, ask = _f(q.get("top_bid_price")), _f(q.get("top_ask_price"))
    mid = (bid + ask) / 2.0 if (bid > 0 and ask >= bid) else _f(q.get("last_price"))
    return {"strike": round(_f(strike), 2), "side": side,
            "ltp": _f(q.get("last_price")), "bid": bid, "ask": ask, "mid": mid,
            "spread": (ask - bid) if (bid > 0 and ask >= bid) else None,
            "iv": _f(q.get("implied_volatility")),
            "delta": abs(_f(g.get("delta"))), "gamma": abs(_f(g.get("gamma"))),
            "theta": -abs(_f(g.get("theta"))), "vega": abs(_f(g.get("vega"))),
            "oi": _f(q.get("oi")), "volume": _f(q.get("volume")),
            "bid_qty": _f(q.get("top_bid_quantity")), "ask_qty": _f(q.get("top_ask_quantity"))}


def atm_strike(snap):
    return min(snap["chain"], key=lambda k: abs(k - snap["spot"])) if snap["chain"] else None


# ─────────────────────────────────────────────────────────────────────────────
#  SIGNAL  —  IVX-G
# ─────────────────────────────────────────────────────────────────────────────
def compute_metrics(cfg):
    """Everything the gates need, from the buffer. None means 'not yet knowable'."""
    fast = BUF.tail(cfg["fast_window"])
    slow = BUF.tail(cfg["slow_window"])
    if len(slow) < 8:
        return None
    dt_min = cfg["poll_interval"] / 60.0

    iv_f = [s["iv_atm"] for s in fast if s.get("iv_atm")]
    iv_s = [s["iv_atm"] for s in slow if s.get("iv_atm")]
    spot_f = [s["spot"] for s in fast]
    basis_f = [s["basis"] for s in fast if s.get("basis") is not None]
    rr_s = [s["rr"] for s in slow if s.get("rr") is not None]

    last = slow[-1]
    iv_now = last.get("iv_atm")

    # per-minute realised sigma of spot, from successive diffs
    diffs = [spot_f[i] - spot_f[i - 1] for i in range(1, len(spot_f))]
    sigma_min = None
    if len(diffs) >= 8:
        try:
            sigma_tick = statistics.stdev(diffs)
            sigma_min = sigma_tick * math.sqrt(60.0 / cfg["poll_interval"])
        except statistics.StatisticsError:
            sigma_min = None

    return {
        "iv_atm": iv_now,
        "iv_slope": ols_slope(iv_f, dt_min) if len(iv_f) >= 8 else None,
        "iv_z": zscore(iv_now, iv_s) if (iv_now and len(iv_s) >= 8) else None,
        "spot": last["spot"],
        "spot_slope": ols_slope(spot_f, dt_min) if len(spot_f) >= 8 else None,
        "basis": last.get("basis"),
        "basis_slope": ols_slope(basis_f, dt_min) if len(basis_f) >= 8 else None,
        "rr": last.get("rr"),
        "d_rr": ((last["rr"] - statistics.fmean(rr_s))
                 if (last.get("rr") is not None and len(rr_s) >= 8) else None),
        "sigma_min": sigma_min,
        "snapshots": len(slow),
    }


def clock_block(cfg, now=None):
    now = now or now_ist()
    if now.weekday() >= 5:
        return "weekend"
    t = now.time()
    if t < MKT_OPEN:
        return "pre-open"
    if t > MKT_CLOSE:
        return "after close"
    if t < OPEN_NOISE_END:
        return "opening auction 09:15-09:25"
    if cfg.get("lunch_block") and LUNCH_START <= t < LUNCH_END:
        return "lunch 12:30-13:15"
    if t >= NO_NEW_ENTRY_AFTER:
        return "no new entries after 15:00"
    return None


def evaluate_signal(snap, m, cfg):
    """Returns {side, strike, quote, gates, blocks, reasons}.  side is None when
    no trade. Every gate and every suppressor is reported by name so the screen
    can show exactly which rail is holding."""
    out = {"side": None, "strike": None, "quote": None,
           "gates": {}, "blocks": [], "detail": {}}
    if not snap or not m:
        out["blocks"].append("WARMING")
        return out

    # ---- suppressors that do not depend on a candidate strike ----
    cb = clock_block(cfg)
    if cb:
        out["blocks"].append("N5 clock: %s" % cb)
    if BUF.age() > STALE_SEC:
        out["blocks"].append("N7 stale data (%.0fs)" % BUF.age())
    if not BUF.warm():
        out["blocks"].append("WARMING (%d/%d snapshots)" % (BUF.size(), cfg["slow_window"]))

    iv = m.get("iv_atm")
    if iv is None or iv < 5.0 or iv > 60.0:
        out["blocks"].append("N9 IV solve looks broken (%s)" % ("n/a" if iv is None else round(iv, 1)))

    sg = m.get("sigma_min")
    if sg is not None and sg < cfg["sigma_min_floor"]:
        out["blocks"].append("N6 tape too quiet (sigma %.1f < %.1f)" % (sg, cfg["sigma_min_floor"]))
    if sg is not None and sg > cfg["sigma_min_ceil"]:
        out["blocks"].append("N6 tape gapping (sigma %.1f > %.1f)" % (sg, cfg["sigma_min_ceil"]))

    dte = dte_of(snap["expiry"])
    if dte <= 0 and not cfg.get("allow_zero_dte"):
        out["blocks"].append("N4 0-DTE disabled (negative expectancy)")

    # ---- GATE A: IV expansion (the thesis) ----
    ivs, ivz = m.get("iv_slope"), m.get("iv_z")
    gate_a = (ivs is not None and ivz is not None
              and ivs >= cfg["iv_slope_min"] and ivz >= cfg["iv_z_min"])
    out["gates"]["A_iv_expansion"] = gate_a
    out["detail"]["iv_slope"] = ivs
    out["detail"]["iv_z"] = ivz
    if ivs is not None and (ivs <= -0.05 or (ivz is not None and ivz <= -0.50)):
        out["blocks"].append("N1 IV collapsing - buying premium into a vol crush")

    # ---- GATE B: direction ----
    drr, bs, ss = m.get("d_rr"), m.get("basis_slope"), m.get("spot_slope")
    out["detail"].update(d_rr=drr, basis_slope=bs, spot_slope=ss)
    side = None
    if None not in (drr, bs, ss):
        if drr >= cfg["rr_delta_min"] and bs >= cfg["basis_slope_min"] and ss > 0:
            side = "ce"
        elif drr <= -cfg["rr_delta_min"] and bs <= -cfg["basis_slope_min"] and ss < 0:
            side = "pe"
    out["gates"]["B_direction"] = side is not None
    if side is None and None not in (drr, bs, ss):
        out["detail"]["direction_note"] = "three reads disagree - no trade"

    # ---- candidate strike: max gamma == delta nearest 0.50 ----
    k = atm_strike(snap)
    q = quote_at(snap, k, side) if (side and k) else None
    out["strike"] = k
    if q:
        out["quote"] = q

    target_pts = cfg["target_rupees"] / max(1, nifty_lot() * cfg["lots"])
    stop_pts = cfg["stop_rupees"] / max(1, nifty_lot() * cfg["lots"])
    out["detail"]["target_pts"] = round(target_pts, 2)
    out["detail"]["stop_pts"] = round(stop_pts, 2)

    # ---- GATE C: feasibility (gamma's real job) ----
    gate_c = False
    if q:
        xt = x_for_premium(q["delta"], q["gamma"], target_pts)
        xs = x_for_stop(q["delta"], q["gamma"], stop_pts)
        theta_min = abs(q["theta"]) / TRADING_MINUTES_PER_DAY
        t_stop = 30.0
        if theta_min > 1e-9:
            t_stop = max(cfg["time_stop_min"],
                         min(cfg["time_stop_max"], 0.25 * stop_pts / theta_min))
        need = None
        if xt and sg and sg > 0:
            need = xt / (sg * math.sqrt(max(t_stop, 1.0)))
        out["detail"].update(x_target=xt, x_stop=xs, t_stop_min=round(t_stop, 1),
                             need_sigma=need, theta_per_min=theta_min,
                             theta_rupees_per_min=theta_min * nifty_lot() * cfg["lots"])
        gate_c = bool(xt and xt <= cfg["x_target_max"]
                      and q["gamma"] >= cfg["gamma_min"]
                      and need is not None and need <= cfg["need_sigma_max"]
                      and sg is not None
                      and cfg["sigma_min_floor"] <= sg <= cfg["sigma_min_ceil"])
        if xt and xt > cfg["x_target_max"]:
            out["blocks"].append("N3 target needs %.0f index pts (max %.0f)"
                                 % (xt, cfg["x_target_max"]))
        if need is not None and need > cfg["need_sigma_max"]:
            out["blocks"].append("N3 target is %.1f sigma away - unreachable in %.0f min"
                                 % (need, t_stop))
    out["gates"]["C_feasible"] = gate_c

    # ---- GATE D: liquidity and cost ----
    gate_d = False
    if q:
        qty = nifty_lot() * cfg["lots"]
        spr = q["spread"]
        lim = max(cfg["spread_abs_max"], cfg["spread_pct_max"] * max(q["mid"], 1.0))
        cost_ok = spr is not None and (2 * spr * qty) <= cfg["cost_frac_of_risk"] * cfg["stop_rupees"]
        depth_ok = (q["bid_qty"] >= cfg["depth_lots_min"] * nifty_lot()
                    and q["ask_qty"] >= cfg["depth_lots_min"] * nifty_lot())
        prem_ok = q["mid"] >= cfg["min_premium_mult"] * target_pts
        fresh_ok = q["volume"] > 0 and q["mid"] > 0 and abs(q["ltp"] - q["mid"]) <= 0.03 * q["mid"]
        gate_d = bool(spr is not None and spr <= lim and cost_ok and depth_ok
                      and prem_ok and fresh_ok)
        out["detail"].update(spread=spr, spread_limit=round(lim, 2),
                             spread_cost_rupees=(2 * spr * qty) if spr else None,
                             premium_ok=prem_ok, depth_ok=depth_ok)
        if spr is not None and spr > lim:
            out["blocks"].append("N2 spread %.2f > %.2f" % (spr, lim))
        if not prem_ok:
            out["blocks"].append("N2 premium %.1f too small for a %.1f pt target"
                                 % (q["mid"], target_pts))
    out["gates"]["D_liquidity"] = gate_d

    # ---- GATE E: theta budget ----
    tpm = out["detail"].get("theta_per_min")
    tsm = out["detail"].get("t_stop_min")
    gate_e = bool(tpm is not None and tsm and (tpm * tsm) <= cfg["theta_frac_of_stop"] * stop_pts)
    out["gates"]["E_theta"] = gate_e
    if tpm is not None and tsm and not gate_e:
        out["blocks"].append("N-theta decay %.1f pts over %.0f min eats the stop"
                             % (tpm * tsm, tsm))

    if side and all(out["gates"].values()) and not out["blocks"]:
        out["side"] = side
    return out


# ─────────────────────────────────────────────────────────────────────────────
#  STATE
# ─────────────────────────────────────────────────────────────────────────────
class AppState:
    def __init__(self):
        self.lock = threading.RLock()
        self.cfg = dict(DEFAULTS)
        self.open_trades = []
        self.trades = []                 # today's closed tape
        self.history = []                # all closed, all days
        self.day = now_ist().strftime("%Y-%m-%d")
        self.running = False             # the scalper loop is armed
        # Launch = trading: set once at launch by the process that owns the
        # lock; the loop turns it into running=True as soon as it may.  Never
        # saved - a restart decides afresh, and Stop / Kill clear it.
        self.autostart = False
        self.kill = False
        self.halted = False
        self.halt_reason = ""
        self.cooldown_until = 0.0
        self.consecutive_stops = 0
        self.scrip_lookup = {}
        self.expiry_list = []
        self.expiry = None               # the one expiry we poll
        self.last_signal = {}
        self.last_metrics = {}
        self.status = "Starting up"
        self.data_ok = False
        self.last_poll_ok = 0.0
        self.poll_fails = 0
        self.owner = False
        self.load()

    # ---- money ----
    def realised_net(self):
        return round(sum(_f(t.get("net_pnl")) for t in self.trades), 2)

    def open_residual_risk(self):
        """How much MORE the open book can lose before its own stops fire.
        Budgeting against current MTM would be wrong: a trade sitting at -100
        can still lose another 900."""
        tot = 0.0
        for t in self.open_trades:
            mark = _f(t.get("mark"), _f(t.get("entry_fill")))
            stop = _f(t.get("stop_price"))
            qty = _f(t.get("quantity"), 1)
            tot += max(0.0, (mark - stop)) * qty
        return round(tot, 2)

    def open_mtm(self):
        return round(sum(_f(t.get("mtm")) for t in self.open_trades), 2)

    def roll_day(self):
        d = now_ist().strftime("%Y-%m-%d")
        if d != self.day:
            log_event("day", "new session %s - counters reset (kill switch is NOT cleared)" % d)
            self.day = d
            self.trades = []
            self.consecutive_stops = 0
            self.cooldown_until = 0.0
            if not self.kill:
                self.halted = False
                self.halt_reason = ""
            BUF.clear("day roll")

    def save(self):
        write_json_atomic(STATE_FILE, {
            "schema": SCHEMA_VERSION, "saved_at": ts_now(), "day": self.day,
            "cfg": self.cfg, "open_trades": self.open_trades,
            "trades": self.trades, "history": self.history[-2000:],
            "running": self.running, "kill": self.kill,
            "halted": self.halted, "halt_reason": self.halt_reason,
            "consecutive_stops": self.consecutive_stops,
            "expiry": self.expiry,
        })

    def load(self):
        d = read_json_safe(STATE_FILE, default=None)
        if not isinstance(d, dict):
            return
        self.cfg.update({k: v for k, v in (d.get("cfg") or {}).items() if k in DEFAULTS})
        self.open_trades = d.get("open_trades") or []
        self.history = d.get("history") or []
        self.day = d.get("day") or self.day
        self.trades = (d.get("trades") or []) if self.day == now_ist().strftime("%Y-%m-%d") else []
        self.kill = bool(d.get("kill"))
        self.halted = bool(d.get("halted"))
        self.halt_reason = d.get("halt_reason") or ""
        self.consecutive_stops = int(_f(d.get("consecutive_stops")))
        self.expiry = d.get("expiry")
        # Never auto-resume trading after a restart.
        self.running = False
        log_event("boot", "loaded %d open, %d today, %d historical"
                  % (len(self.open_trades), len(self.trades), len(self.history)))


STATE = AppState()


# ─────────────────────────────────────────────────────────────────────────────
#  RISK ENGINE  —  one gate, and the reason is shown verbatim on screen
# ─────────────────────────────────────────────────────────────────────────────
def halt(reason):
    if not STATE.halted:
        STATE.halted = True
        STATE.halt_reason = reason
        log_event("halt", "HALTED: %s" % reason)


def machine_state():
    if STATE.kill:
        return "KILLED"
    if STATE.halted:
        return "HALTED"
    if STATE.open_trades:
        return "IN_TRADE"
    if time.time() < STATE.cooldown_until:
        return "COOLDOWN"
    if not STATE.running:
        return "IDLE"
    ok, _ = can_enter()
    return "ARMED" if ok else "IDLE"


def can_enter():
    """The only gate. Nothing else may open a position."""
    c = STATE.cfg
    if STATE.kill:
        return False, "kill switch is on"
    if STATE.halted:
        return False, "halted: %s" % STATE.halt_reason
    if not STATE.running:
        return False, "scalper is stopped"
    if not STATE.data_ok:
        return False, "chain data stale - not entering blind"
    cb = clock_block(c)
    if cb:
        return False, cb
    if len(STATE.open_trades) >= c["max_concurrent"]:
        return False, "already holding %d (max %d)" % (len(STATE.open_trades), c["max_concurrent"])
    if len(STATE.trades) >= c["max_trades"]:
        return False, "max %d trades today" % c["max_trades"]
    left = time.time() - STATE.cooldown_until
    if left < 0:
        return False, "cooldown %ds left" % int(-left)
    if c["daily_profit_stop"] and STATE.realised_net() >= c["daily_profit_stop"]:
        return False, "daily profit stop reached"
    budget_left = c["daily_loss_cap"] + min(0.0, STATE.realised_net())
    worst_new = c["stop_rupees"] + c["cost_per_trade"]
    if STATE.open_residual_risk() + worst_new > budget_left:
        return False, ("would risk Rs %.0f against Rs %.0f of loss budget left"
                       % (STATE.open_residual_risk() + worst_new, budget_left))
    return True, "ready"


def post_exit_risk(trade):
    """Runs after every close. Sets cooldown and trips the day's rails."""
    c = STATE.cfg
    reason = trade.get("exit_reason") or ""
    is_stop = reason.startswith("STOP") or reason.startswith("DATA_LOSS")
    if is_stop:
        STATE.consecutive_stops += 1
        if STATE.consecutive_stops >= c["max_consecutive_stops"]:
            halt("%d consecutive stops - the regime is not the one this signal was built for"
                 % STATE.consecutive_stops)
        else:
            cd = c["cooldown_stop_1"] if STATE.consecutive_stops == 1 else c["cooldown_stop_2"]
            STATE.cooldown_until = time.time() + cd
            log_event("risk", "cooldown %ds after stop #%d" % (cd, STATE.consecutive_stops))
    else:
        STATE.consecutive_stops = 0
        STATE.cooldown_until = time.time() + c["cooldown_win"]

    net = STATE.realised_net()
    if net <= -c["daily_loss_cap"]:
        halt("daily loss cap Rs %.0f hit (net Rs %.0f)" % (c["daily_loss_cap"], net))
    if c["daily_profit_stop"] and net >= c["daily_profit_stop"]:
        halt("daily profit stop Rs %.0f reached (net Rs %.0f)" % (c["daily_profit_stop"], net))
    if len(STATE.trades) >= c["max_trades"]:
        halt("max %d trades today" % c["max_trades"])


# ─────────────────────────────────────────────────────────────────────────────
#  TRADE LIFECYCLE
# ─────────────────────────────────────────────────────────────────────────────
def open_trade(snap, sig, cfg):
    if kill_blocks():
        return None                   # a VIX rule says no new trades
    q = sig["quote"]
    side = sig["side"]
    opt_type = "CALL" if side == "ce" else "PUT"
    mapping = get_mapping(snap["expiry"], q["strike"], side)
    if not mapping:
        log_event("error", "no scrip mapping for %s %s %s - refusing entry"
                  % (snap["expiry"], q["strike"], opt_type))
        return None
    lot = int(mapping["lot"])
    qty = lot * int(cfg["lots"])
    target_pts = cfg["target_rupees"] / qty
    stop_pts = cfg["stop_rupees"] / qty
    # A long option is BOUGHT at the ask. Entering at mid or LTP is the second
    # most common way a paper scalper lies to itself.
    fill = q["ask"] if q["ask"] > 0 else q["mid"]
    t_stop = _f(sig["detail"].get("t_stop_min"), 30.0)
    tr = {
        "schema": SCHEMA_VERSION, "id": uuid.uuid4().hex[:16],
        "strategy": "IVX-G", "mode": "PAPER", "status": "OPEN",
        "underlying": UNDERLYING_SYM, "expiry": snap["expiry"], "dte": dte_of(snap["expiry"]),
        "option_type": opt_type, "strike": q["strike"],
        # --- order-ready for Dhan ---
        "security_id": str(mapping["sec_id"]), "exchange_segment": EXCHANGE_SEGMENT,
        "transaction_type": "BUY", "exit_transaction_type": "SELL",
        "product_type": PRODUCT_TYPE, "order_type": ORDER_TYPE, "validity": VALIDITY,
        "trading_symbol": mapping.get("tsym"), "lot_size": lot,
        "lots": int(cfg["lots"]), "quantity": qty,
        # --- levels, frozen at entry ---
        "entry_time": ts_now(), "entry_epoch": time.time(),
        "entry_quote": q["ask"], "entry_fill": round(fill, 2),
        "entry_bid": q["bid"], "entry_mid": round(q["mid"], 2), "entry_spread": q["spread"],
        "target_pts": round(target_pts, 2), "stop_pts": round(stop_pts, 2),
        "target_price": round(fill + target_pts, 2),
        "stop_price": round(fill - stop_pts, 2),
        "time_stop_min": round(t_stop, 1),
        "trail_arm_price": round(fill + cfg["trail_arm_frac"] * target_pts, 2),
        "trail_price": None, "high_water_bid": q["bid"],
        # --- what the signal looked like, so a bad run can be diagnosed ---
        "entry_spot": snap["spot"], "entry_iv": q["iv"],
        "entry_delta": q["delta"], "entry_gamma": q["gamma"],
        "entry_theta": q["theta"], "entry_vega": q["vega"],
        "signal": {k: (round(v, 4) if isinstance(v, float) else v)
                   for k, v in (sig.get("detail") or {}).items()},
        # --- live ---
        "mark": q["bid"], "mark_source": "bid", "mtm": 0.0, "stale": False,
        "exit_time": None, "exit_fill": None, "exit_reason": None,
        "gross_pnl": None, "net_pnl": None, "slippage_pts": None,
        "cost": cfg["cost_per_trade"],
    }
    with STATE.lock:
        STATE.open_trades.append(tr)
        STATE.save()
    log_event("entry", "BUY %d %s %s @ %.2f  target %.2f  stop %.2f  (IV slope %+.3f, z %+.2f)"
              % (qty, int(q["strike"]), opt_type, fill, tr["target_price"], tr["stop_price"],
                 _f(sig["detail"].get("iv_slope")), _f(sig["detail"].get("iv_z"))))
    return tr


def mark_trade(tr, snap, cfg):
    """Mark a long option at the BID - that is where it can actually be sold."""
    side = "ce" if tr["option_type"] == "CALL" else "pe"
    q = quote_at(snap, tr["strike"], side) if snap else None
    if not q or q["bid"] <= 0:
        tr["stale"] = True
        return None
    tr["stale"] = False
    tr["mark"] = q["bid"]
    tr["mark_source"] = "bid"
    tr["mid"] = round(q["mid"], 2)
    tr["iv_now"] = q["iv"]
    tr["mtm"] = round((q["bid"] - tr["entry_fill"]) * tr["quantity"], 2)
    if q["bid"] > _f(tr.get("high_water_bid")):
        tr["high_water_bid"] = q["bid"]
    return q


def close_trade(tr, price, reason, cfg, slip_from=None):
    qty = tr["quantity"]
    exit_fill = round(price - _f(cfg.get("slippage_extra_pts")), 2)
    gross = (exit_fill - tr["entry_fill"]) * qty
    net = gross - _f(tr.get("cost"), cfg["cost_per_trade"])
    tr.update(status="CLOSED", exit_time=ts_now(), exit_epoch=time.time(),
              exit_fill=exit_fill, exit_reason=reason,
              gross_pnl=round(gross, 2), net_pnl=round(net, 2),
              held_min=round((time.time() - _f(tr.get("entry_epoch"), time.time())) / 60.0, 1))
    if slip_from is not None:
        tr["slippage_pts"] = round(exit_fill - slip_from, 2)
    with STATE.lock:
        STATE.open_trades = [x for x in STATE.open_trades if x.get("id") != tr.get("id")]
        STATE.trades.append(tr)
        STATE.history.append(tr)
        post_exit_risk(tr)
        STATE.save()
    log_event("exit", "%s %s %d %s @ %.2f  gross %+.0f  net %+.0f  (%s)"
              % (reason, int(tr["strike"]), tr["quantity"], tr["option_type"],
                 exit_fill, gross, net, tr.get("held_min")))
    return tr


def evaluate_exits(snap, metrics, cfg):
    """Order is fixed and matters: STALE -> EOD -> STOP -> TRAIL -> TARGET ->
    TIME -> SIGNAL_DECAY.  Stop before target, so a snapshot that breaches both
    books the loss rather than being rescued by the same tick."""
    now = now_ist()
    for tr in list(STATE.open_trades):
        q = mark_trade(tr, snap, cfg)

        # STALE
        if q is None:
            age = BUF.age()
            if age > DATA_LOSS_SEC:
                last = _f(tr.get("mark"), tr["entry_fill"])
                close_trade(tr, last, "DATA_LOSS", cfg)
                log_event("data", "closed %s on data loss - a quality event, not a strategy result"
                          % tr["id"][:8])
            continue

        bid = q["bid"]

        # EOD
        if now.time() >= HARD_FLAT:
            close_trade(tr, bid, "EOD", cfg)
            continue

        # STOP  (fill at the real bid, and record the overshoot honestly)
        if bid <= tr["stop_price"]:
            close_trade(tr, bid, "STOP", cfg, slip_from=tr["stop_price"])
            continue

        # TRAIL
        if tr.get("trail_price") is None and bid >= tr["trail_arm_price"]:
            tr["trail_price"] = round(max(tr["entry_fill"] + cfg["trail_floor"],
                                          tr["high_water_bid"] - cfg["trail_giveback"]), 2)
            log_event("trail", "%s trail armed at %.2f" % (tr["id"][:8], tr["trail_price"]))
        if tr.get("trail_price") is not None:
            newt = round(max(tr["entry_fill"] + cfg["trail_floor"],
                             tr["high_water_bid"] - cfg["trail_giveback"]), 2)
            if newt > tr["trail_price"]:          # ratchet only, never loosened
                tr["trail_price"] = newt
            if bid <= tr["trail_price"]:
                close_trade(tr, bid, "TRAIL", cfg)
                continue

        # TARGET
        if bid >= tr["target_price"]:
            close_trade(tr, bid, "TARGET", cfg)
            continue

        # TIME
        held = (time.time() - _f(tr.get("entry_epoch"), time.time())) / 60.0
        if held >= _f(tr.get("time_stop_min"), 30.0):
            close_trade(tr, bid, "TIME", cfg)
            continue

        # SIGNAL DECAY - the reason we paid the spread has evaporated
        ivs = (metrics or {}).get("iv_slope")
        if (ivs is not None and ivs <= cfg["signal_decay_slope"]
                and (bid - tr["entry_fill"]) < cfg["signal_decay_profit_pts"]):
            close_trade(tr, bid, "SIGNAL_DECAY", cfg)
            continue

    # hard MTM trip, independent of any single trade
    c = cfg
    if STATE.open_trades and (STATE.realised_net() + STATE.open_mtm()) <= -1.2 * c["daily_loss_cap"]:
        log_event("risk", "MTM breach of 1.2x the daily cap - flattening")
        flatten_now(snap, "MTM_BREACH")


def flatten_now(snap, reason="MANUAL_FLATTEN"):
    cfg = STATE.cfg
    for tr in list(STATE.open_trades):
        q = mark_trade(tr, snap, cfg) if snap else None
        price = q["bid"] if q else _f(tr.get("mark"), tr["entry_fill"])
        close_trade(tr, price, reason, cfg)
    halt(reason if reason != "MANUAL_FLATTEN" else "flattened by hand")


# ─────────────────────────────────────────────────────────────────────────────
#  POLL LOOP  —  ONE chain call serves both the signal and the marking
# ─────────────────────────────────────────────────────────────────────────────
_SHUTDOWN = threading.Event()


def pick_expiry(cfg):
    """Nearest expiry inside [dte_min, dte_max].  0-DTE is excluded unless
    explicitly enabled, because its expectancy is decisively negative."""
    best = None
    for e in STATE.expiry_list:
        try:
            d = dte_of(e)
        except Exception:
            continue
        lo = 0 if cfg.get("allow_zero_dte") else max(1, cfg["dte_min"])
        if lo <= d <= cfg["dte_max"]:
            if best is None or d < best[0]:
                best = (d, e)
    return best[1] if best else None


_autostart_wait_logged = [False]


def autostart_step():
    """Launch = trading.  Turns the launch-time autostart flag into running as
    soon as this copy may trade: it owns the lock, the kill switch is off and
    the broker token is valid - the same checks as pressing Start.  It never
    overrides the kill switch (an engaged one cancels the automatic start for
    this launch), and a missing or expired token is a wait, not an error.
    Returns a status line while it is waiting, else None."""
    if not STATE.autostart or STATE.running:
        return None
    if not STATE.owner:
        STATE.autostart = False
        return None
    if STATE.kill:
        with STATE.lock:
            STATE.autostart = False
        log_event("run", "not starting automatically: the kill switch is on - "
                         "press Re-arm after halt, then Start")
        return None
    ts = token_status()
    if not ts["configured"] or ts["expired"]:
        if not _autostart_wait_logged[0]:
            _autostart_wait_logged[0] = True
            log_event("run", "will start automatically once the broker token works (token %s)"
                      % ts["human"])
        return "Starting automatically once the broker token works - token %s" % ts["human"]
    with STATE.lock:
        # Re-checked under the lock: Stop or Kill may have landed meanwhile.
        if not STATE.autostart or STATE.running or STATE.kill:
            return None
        STATE.autostart = False
        STATE.running = True
        STATE.save()
    log_event("run", "scalper armed - started automatically on launch")
    return None


def scalper_loop():
    log_event("boot", "scalper thread started")
    while not _SHUTDOWN.is_set():
        cfg = dict(STATE.cfg)
        _SHUTDOWN.wait(max(1.0, cfg["poll_interval"]))
        if _SHUTDOWN.is_set():
            break
        try:
            STATE.roll_day()

            if now_ist().time() >= HALT_ALL and not STATE.halted:
                halt("session over (15:25)")

            waiting = autostart_step()

            if not (STATE.running or STATE.open_trades):
                STATE.status = waiting or ("Stopped" if not STATE.running else STATE.status)
                continue

            if not STATE.expiry or dte_of(STATE.expiry) < (0 if cfg["allow_zero_dte"] else 1):
                STATE.expiry = pick_expiry(cfg)
            if not STATE.expiry:
                STATE.status = "No expiry in the %d-%d DTE window" % (cfg["dte_min"], cfg["dte_max"])
                continue

            res = throttled_chain(STATE.expiry)
            snap = build_snapshot(STATE.expiry, res)
            if not snap:
                STATE.poll_fails += 1
                STATE.data_ok = False
                if STATE.poll_fails >= 2:
                    STATE.status = "Chain unavailable (%d failed polls) - %s" % (
                        STATE.poll_fails, res.get("message", ""))
                evaluate_exits(None, None, cfg)     # may trip DATA_LOSS
                continue

            STATE.poll_fails = 0
            STATE.last_poll_ok = time.time()
            BUF.add(snap)
            STATE.data_ok = BUF.age() <= STALE_SEC

            kill_step(True, lambda: _kill_close_all(snap))
            metrics = compute_metrics(cfg)
            STATE.last_metrics = metrics or {}

            # exits first: an open position outranks a new signal
            evaluate_exits(snap, metrics, cfg)

            sig = evaluate_signal(snap, metrics, cfg)
            STATE.last_signal = {k: v for k, v in sig.items() if k != "quote"}
            STATE.last_signal["quote"] = sig.get("quote")

            ok, why = can_enter()
            STATE.last_signal["risk_gate"] = why
            if sig.get("side") and ok:
                open_trade(snap, sig, cfg)
                STATE.status = "In trade"
            else:
                st = machine_state()
                STATE.status = ("%s - %s" % (st, why)) if not ok else \
                    ("%s - waiting for a signal" % st)
        except Exception as e:
            log_event("error", "loop: %s: %s" % (e.__class__.__name__, e))
            STATE.status = "Loop error: %s" % e


def boot_loop():
    while not _SHUTDOWN.is_set():
        try:
            STATE.scrip_lookup = load_scrip_lookup()
            STATE.expiry_list = fetch_expiry_list()
            if STATE.expiry_list:
                STATE.expiry = pick_expiry(STATE.cfg)
                STATE.status = "Ready - lot %d, %d expiries, trading %s" % (
                    nifty_lot(), len(STATE.expiry_list), STATE.expiry or "none in window")
                log_event("boot", STATE.status)
                return
            STATE.status = "Could not load expiries - token %s" % token_status()["human"]
            log_event("boot", STATE.status)
        except Exception as e:
            STATE.status = "Boot error: %s" % e
            log_event("error", "boot: %s" % e)
        _SHUTDOWN.wait(120)


# ─────────────────────────────────────────────────────────────────────────────
#  EXPECTANCY  —  shown in the app, so the maths is never out of sight
# ─────────────────────────────────────────────────────────────────────────────
def expectancy(cfg, win_rate=None, sample=None):
    """Break-even win rate and expected P&L per trade, net of costs.

    Barrier probability for a driftless option is stop/(target+stop). Everything
    the strategy does has to beat that number, not the naive 3:1 headline."""
    qty = max(1, nifty_lot() * int(cfg["lots"]))
    tp = cfg["target_rupees"] / qty
    sp = cfg["stop_rupees"] / qty
    cost = cfg["cost_per_trade"]
    win_rs = cfg["target_rupees"] - cost
    loss_rs = cfg["stop_rupees"] + cost
    be = loss_rs / (win_rs + loss_rs) * 100.0
    naive_be = sp / (tp + sp) * 100.0
    out = {"target_pts": round(tp, 2), "stop_pts": round(sp, 2),
           "reward_risk": round(cfg["target_rupees"] / cfg["stop_rupees"], 2),
           "naive_breakeven_pct": round(naive_be, 1),
           "breakeven_pct": round(be, 1),
           "cost_per_trade": cost, "lot": nifty_lot(), "qty": qty}
    if sample:
        wins = [t for t in sample if _f(t.get("net_pnl")) > 0]
        n = len(sample)
        out["actual"] = {
            "trades": n,
            "win_rate": round(len(wins) / n * 100.0, 1) if n else None,
            "net": round(sum(_f(t.get("net_pnl")) for t in sample), 2),
            "per_trade": round(sum(_f(t.get("net_pnl")) for t in sample) / n, 2) if n else None,
            "edge_pct": (round(len(wins) / n * 100.0 - be, 1) if n else None),
        }
    if win_rate is not None:
        w = win_rate / 100.0
        out["projected_per_trade"] = round(w * win_rs - (1 - w) * loss_rs, 2)
    return out


# ─────────────────────────────────────────────────────────────────────────────
#  FLASK + AUTH
# ─────────────────────────────────────────────────────────────────────────────
app = Flask(__name__)
LISTEN_PUBLIC = (_env("APP_ENV") == "hosted") or (_env("HOST") == "0.0.0.0")


def _write_private(path, data):
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


def _secret():
    k = _env("SECRET_KEY")
    if k:
        return k.encode()
    if os.path.exists(SECRET_FILE):
        try:
            with open(SECRET_FILE, "rb") as f:
                k = f.read().strip()
            if len(k) >= 32:
                return k
        except OSError:
            pass
    k = secrets.token_hex(32).encode()
    _write_private(SECRET_FILE, k)
    return k


app.secret_key = _secret()
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax",
                  SESSION_COOKIE_SECURE=(_env("COOKIE_SECURE", "0") == "1"),
                  PERMANENT_SESSION_LIFETIME=timedelta(days=30),
                  MAX_CONTENT_LENGTH=256 * 1024)

_SCRYPT = dict(n=2 ** 14, r=8, p=1, maxmem=64 * 1024 * 1024, dklen=32)


def hash_password(pw, salt=None):
    salt = salt or secrets.token_bytes(16)
    return {"algo": "scrypt", "n": _SCRYPT["n"], "r": _SCRYPT["r"], "p": _SCRYPT["p"],
            "salt": salt.hex(),
            "hash": hashlib.scrypt(pw.encode(), salt=salt, **_SCRYPT).hex()}


def verify_password(pw, rec):
    if not rec or rec.get("algo") != "scrypt":
        return False
    try:
        dk = hashlib.scrypt(pw.encode(), salt=bytes.fromhex(rec["salt"]),
                            n=rec["n"], r=rec["r"], p=rec["p"],
                            maxmem=_SCRYPT["maxmem"], dklen=32)
    except Exception:
        return False
    return hmac.compare_digest(dk.hex(), rec.get("hash", ""))


def _bootstrap_auth():
    stored = read_json_safe(AUTH_FILE, default=None)
    pw = _env("APP_PASSWORD")
    if pw:
        fp = hashlib.sha256(("v1" + pw).encode()).hexdigest()[:16]
        if not stored or stored.get("env_fp") != fp:
            rec = hash_password(pw)
            rec["env_fp"] = fp
            write_json_atomic(AUTH_FILE, rec, private=True)
            return rec
        return stored
    if stored:
        return stored
    if not LISTEN_PUBLIC:
        return None
    gen = secrets.token_urlsafe(12)
    rec = hash_password(gen)
    write_json_atomic(AUTH_FILE, rec, private=True)
    print("\n" + "=" * 60 + "\n  SCALPER LOGIN PASSWORD: %s\n" % gen + "=" * 60 + "\n", flush=True)
    return rec


AUTH_RECORD = _bootstrap_auth()
AUTH_ON = AUTH_RECORD is not None
_fails, _fail_lock = {}, threading.Lock()
PUBLIC_PATHS = {"/login", "/health", "/favicon.ico"}


def _ip():
    if _env("TRUST_PROXY", "0") == "1":
        x = request.headers.get("X-Forwarded-For", "")
        if x:
            return x.split(",")[0].strip()
    return request.remote_addr or "?"


@app.before_request
def _gate():
    if request.path in PUBLIC_PATHS:
        return None
    if AUTH_ON and session.get("auth") is not True:
        if request.path.startswith("/api/"):
            return jsonify({"error": "not authenticated", "login_required": True}), 401
        return redirect(url_for("login"))
    if AUTH_ON and request.method not in ("GET", "HEAD", "OPTIONS"):
        if not hmac.compare_digest(request.headers.get("X-CSRF-Token", ""),
                                   session.get("csrf", "") or "\x00"):
            return jsonify({"error": "bad CSRF token"}), 403
    return None


@app.after_request
def _csrf(resp):
    if AUTH_ON and session.get("auth") and session.get("csrf"):
        resp.set_cookie("csrf", session["csrf"], samesite="Lax", httponly=False,
                        secure=app.config["SESSION_COOKIE_SECURE"], max_age=30 * 24 * 3600)
    return resp


@app.route("/login", methods=["GET", "POST"])
def login():
    if not AUTH_ON:
        return redirect("/")
    ip, err = _ip(), None
    with _fail_lock:
        rec = _fails.get(ip, {"n": 0, "until": 0})
    locked = max(0, int(rec["until"] - time.time()))
    if request.method == "POST":
        if locked:
            err = "Too many attempts. %ds left." % locked
        elif verify_password(request.form.get("password") or "", AUTH_RECORD):
            with _fail_lock:
                _fails.pop(ip, None)
            session.clear()
            session.permanent = True
            session["auth"] = True
            session["csrf"] = secrets.token_urlsafe(24)
            return redirect("/")
        else:
            with _fail_lock:
                r = _fails.setdefault(ip, {"n": 0, "until": 0})
                r["n"] += 1
                if r["n"] >= 6:
                    r["until"] = time.time() + 900
            err = "Wrong password."
    return render_template_string(LOGIN_HTML, error=err, locked=locked)


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
def health():
    ts = token_status()
    ok = bool(STATE.expiry_list) and ts["configured"] and not ts["expired"]
    return jsonify({"ok": ok, "state": machine_state(), "running": STATE.running,
                    "open": len(STATE.open_trades), "today": len(STATE.trades),
                    "token": ts["human"], "data_ok": STATE.data_ok}), (200 if ok else 503)


def market_note(now=None):
    """The header pill: the NSE session by the clock (holidays are not known)."""
    now = now or now_ist()
    if now.weekday() >= 5:
        return "CLOSED - weekend"
    t = now.time()
    if t < MKT_OPEN:
        return "PRE - pre-open, starts 09:15 IST"
    if t > MKT_CLOSE:
        return "CLOSED - after close"
    return "OPEN - session live"


@app.route("/api/state")
def api_state():
    cfg = STATE.cfg
    ok, why = can_enter()
    net = STATE.realised_net()
    with STATE.lock:
        open_t = [dict(t) for t in STATE.open_trades]
        today = [dict(t) for t in STATE.trades]
    wins = len([t for t in today if _f(t.get("net_pnl")) > 0])
    return jsonify({
        "machine_state": machine_state(),
        "running": STATE.running, "kill": STATE.kill,
        "halted": STATE.halted, "halt_reason": STATE.halt_reason,
        "status": STATE.status, "day": STATE.day,
        "expiry": STATE.expiry, "dte": dte_of(STATE.expiry) if STATE.expiry else None,
        "expiry_list": STATE.expiry_list, "lot": nifty_lot(),
        "data_ok": STATE.data_ok, "buffer": BUF.size(), "buffer_warm": BUF.warm(),
        "buffer_age": round(BUF.age(), 1) if BUF.size() else None,
        "signal": STATE.last_signal, "metrics": STATE.last_metrics,
        "risk_gate": why, "can_enter": ok,
        "open_trades": open_t, "today_trades": today,
        "cooldown_left": max(0, int(STATE.cooldown_until - time.time())),
        "consecutive_stops": STATE.consecutive_stops,
        "realised_net": net, "open_mtm": STATE.open_mtm(),
        "residual_risk": STATE.open_residual_risk(),
        "loss_budget_left": round(cfg["daily_loss_cap"] + min(0.0, net), 2),
        "trades_left": max(0, cfg["max_trades"] - len(today)),
        "wins": wins, "losses": len(today) - wins,
        "cfg": cfg, "token": token_status(), "auth_on": AUTH_ON,
        "expectancy": expectancy(cfg, sample=STATE.history[-200:] or None),
        "owner": STATE.owner,
        "autostart": STATE.autostart, "market": market_note(),
        "updated": now_ist().strftime("%H:%M:%S"),
    })


@app.route("/api/start", methods=["POST"])
def api_start():
    if not STATE.owner:
        return jsonify({"error": "another instance owns the scalper"}), 409
    if STATE.kill:
        return jsonify({"error": "kill switch is on - clear it first"}), 400
    ts = token_status()
    if not ts["configured"] or ts["expired"]:
        return jsonify({"error": "token %s" % ts["human"]}), 400
    with STATE.lock:
        STATE.running = True
        STATE.autostart = False          # started by hand; nothing left pending
        STATE.save()
    log_event("run", "scalper armed")
    return jsonify({"ok": True})


@app.route("/api/stop", methods=["POST"])
def api_stop():
    with STATE.lock:
        STATE.running = False
        STATE.autostart = False          # Stop also cancels a pending automatic start
        STATE.save()
    log_event("run", "scalper stopped (open positions keep being managed)")
    return jsonify({"ok": True})


@app.route("/api/kill", methods=["POST"])
def api_kill():
    with STATE.lock:
        STATE.kill = True
        STATE.running = False
        STATE.autostart = False          # the kill switch always wins over the automatic start
        halt("kill switch")
        STATE.save()
    log_event("halt", "KILL SWITCH - re-arm by hand")
    return jsonify({"ok": True})


@app.route("/api/rearm", methods=["POST"])
def api_rearm():
    STATE.kill = False
    STATE.halted = False
    STATE.halt_reason = ""
    STATE.consecutive_stops = 0
    STATE.cooldown_until = 0.0
    with STATE.lock:
        STATE.save()
    log_event("run", "re-armed by hand")
    return jsonify({"ok": True})


@app.route("/api/flatten", methods=["POST"])
def api_flatten():
    snap = BUF.tail(1)
    flatten_now(snap[0] if snap else None, "MANUAL_FLATTEN")
    return jsonify({"ok": True, "open": len(STATE.open_trades)})


@app.route("/api/config", methods=["POST"])
def api_config():
    body = request.get_json(force=True, silent=True) or {}
    cfg = dict(STATE.cfg)
    for k, v in body.items():
        if k not in DEFAULTS:
            continue
        cur = DEFAULTS[k]
        if isinstance(cur, bool):
            cfg[k] = bool(v)
        elif isinstance(cur, int):
            cfg[k] = int(_f(v, cur))
        else:
            cfg[k] = _f(v, cur)
    if cfg["target_rupees"] <= 0 or cfg["stop_rupees"] <= 0:
        return jsonify({"error": "target and stop must both be positive"}), 400
    with STATE.lock:
        STATE.cfg = cfg
        STATE.save()
    log_event("cfg", "settings updated")
    return jsonify({"ok": True, "cfg": cfg, "expectancy": expectancy(cfg)})


@app.route("/api/expectancy")
def api_expectancy():
    wr = request.args.get("win_rate")
    return jsonify(expectancy(STATE.cfg, win_rate=_f(wr) if wr else None,
                              sample=STATE.history[-500:] or None))


@app.route("/api/history")
def api_history():
    with STATE.lock:
        rows = [dict(t) for t in STATE.history[-500:]]
    rows.reverse()
    return jsonify({"rows": rows, "count": len(STATE.history)})


@app.route("/api/history.csv")
def api_history_csv():
    hdr = ["Date", "Entry Time", "Exit Time", "Held (min)", "Expiry", "DTE", "Type", "Strike",
           "Qty", "Entry Fill", "Exit Fill", "Target", "Stop", "Exit Reason",
           "Gross PnL", "Cost", "Net PnL", "Slippage pts",
           "Entry Spot", "Entry IV", "Entry Delta", "Entry Gamma", "Entry Theta", "Entry Vega",
           "IV Slope", "IV Z", "d RR", "Basis Slope", "Spot Slope", "Sigma/min",
           "x_target", "need_sigma", "Security ID"]
    rows = []
    with STATE.lock:
        hist = [dict(t) for t in STATE.history]
    for t in hist:
        s = t.get("signal") or {}
        rows.append([
            str(t.get("entry_time"))[:10], t.get("entry_time"), t.get("exit_time"),
            t.get("held_min"), t.get("expiry"), t.get("dte"), t.get("option_type"),
            t.get("strike"), t.get("quantity"), t.get("entry_fill"), t.get("exit_fill"),
            t.get("target_price"), t.get("stop_price"), t.get("exit_reason"),
            t.get("gross_pnl"), t.get("cost"), t.get("net_pnl"), t.get("slippage_pts"),
            t.get("entry_spot"), t.get("entry_iv"), t.get("entry_delta"),
            t.get("entry_gamma"), t.get("entry_theta"), t.get("entry_vega"),
            s.get("iv_slope"), s.get("iv_z"), s.get("d_rr"), s.get("basis_slope"),
            s.get("spot_slope"), s.get("sigma_min"), s.get("x_target"), s.get("need_sigma"),
            t.get("security_id"),
        ])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(hdr)
    w.writerows(rows)
    return Response("﻿" + buf.getvalue(), content_type="text/csv; charset=utf-8",
                    headers={"Content-Disposition":
                             'attachment; filename="scalp_trades_%s.csv"'
                             % now_ist().strftime("%Y%m%d_%H%M")})


def _remove_trades(pred, why):
    """Clear / Wipe on the Trade Report never destroy anything: the removed
    trades are appended to trades_removed.jsonl FIRST, and only then is the
    report book rewritten without them.

    This touches STATE.history (the report) alone.  STATE.trades - today's
    list, which feeds realised_net(), the max-trades cap and the loss budget
    in can_enter() - is deliberately left exactly as it is, so pruning the
    report can never loosen a risk gate.  Both lists hold the same trade
    dicts, so dropping a row from one does not disturb the other."""
    with STATE.lock:
        snap = list(STATE.history)
        gone = [r for r in snap if pred(r)]
        if not gone:
            return 0
        keep = [r for r in snap if not pred(r)]
        stamp = ts_now()
        blob = "".join(json.dumps(dict(r, removed=stamp, removed_why=why), default=str) + "\n"
                       for r in gone)
        # If this write fails we keep the book untouched rather than lose trades.
        with open(TRADES_REMOVED_FILE, "a", encoding="utf-8") as f:
            f.write(blob)
            f.flush()
            os.fsync(f.fileno())
        STATE.history = keep
        STATE.save()
    log_event("report", "%s: %d trade%s moved to trades_removed.jsonl"
              % (why, len(gone), "" if len(gone) == 1 else "s"))
    return len(gone)


@app.route("/api/history/clear", methods=["POST"])
def api_history_clear():
    ids = set((request.get_json(silent=True) or {}).get("ids") or [])
    try:
        n = _remove_trades(lambda r: r.get("id") in ids, "clear selected")
    except OSError as e:
        return jsonify({"error": "could not write trades_removed.jsonl - "
                                 "nothing was removed (%s)" % e}), 500
    return jsonify({"ok": True, "removed": n})


@app.route("/api/history/wipe", methods=["POST"])
def api_history_wipe():
    try:
        n = _remove_trades(lambda r: True, "wipe all")
    except OSError as e:
        return jsonify({"error": "could not write trades_removed.jsonl - "
                                 "nothing was removed (%s)" % e}), 500
    return jsonify({"ok": True, "removed": n})


@app.route("/api/events")
def api_events():
    return jsonify({"events": recent_events(int(_f(request.args.get("since"), 0)))})


@app.route("/api/token", methods=["GET"])
def api_token_get():
    return jsonify(token_status())


@app.route("/api/token", methods=["POST"])
def api_token_set():
    c = resolve_credentials()
    if c.env_pinned:
        return jsonify({"error": "DHAN_ACCESS_TOKEN is set in the environment "
                                 "and overrides this form."}), 409
    body = request.get_json(force=True, silent=True) or {}
    tok = (body.get("token") or "").strip().strip('"').replace("\n", "").replace(" ", "")
    if tok.lower().startswith("bearer "):
        tok = tok[7:].strip()
    if len(tok) < 40 or tok.count(".") != 2:
        return jsonify({"error": "that does not look like a Dhan access token"}), 400
    payload, err = decode_jwt_unverified(tok)
    if err:
        return jsonify({"error": "could not read that token: %s" % err}), 400
    fields = {"access_token": tok, "token_saved_at": ts_now()}
    cid = (body.get("client_id") or "").strip()
    if cid:
        fields["client_id"] = cid
    elif payload.get("dhanClientId"):
        fields["client_id"] = str(payload["dhanClientId"])
    runtime_write(**fields)
    log_event("token", "new access token saved")
    if not STATE.expiry_list:
        threading.Thread(target=boot_loop, daemon=True).start()
    return jsonify({"ok": True, "token": token_status()})


@app.route("/api/token/test", methods=["POST"])
def api_token_test():
    t0 = time.time()
    lst = fetch_expiry_list()
    ms = int((time.time() - t0) * 1000)
    if lst:
        return jsonify({"ok": True, "ms": ms, "detail": "%d expiries" % len(lst)})
    return jsonify({"ok": False, "ms": ms, "detail": "no response - check the token"})


INDEX_HTML = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NIFTY Scalper</title>
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
/* ---- scalper additions, same tokens ---- */
[hidden]{display:none!important}
a.btn.ghost{background:transparent;color:var(--tx);border:1px solid var(--bd2)}
textarea{width:100%;background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:8px 11px;color:var(--br);font:12px ui-monospace,Consolas,monospace;resize:vertical}
.note.bad{background:rgba(239,68,68,.1);border-left-color:var(--rd)}
.hero{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center;border-left:4px solid var(--m2);margin-bottom:16px}
.hero.t-ready{border-left-color:var(--ac)}.hero.t-trade{border-left-color:var(--gn)}
.hero.t-stop{border-left-color:var(--rd)}.hero.t-cool{border-left-color:var(--or)}
.headline{font-size:22px;font-weight:700;color:var(--br);margin:4px 0 2px}
.why{font-size:13px}
.ctl{display:flex;flex-direction:column;gap:8px;min-width:270px}
.ctl .row{display:flex;gap:8px}.ctl .row button{flex:1}
.meter{height:6px;border-radius:3px;background:var(--p2);margin-top:10px;overflow:hidden}
.meter i{display:block;height:100%;border-radius:3px;background:var(--gn);transition:width .4s}
.three{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:14px;margin-bottom:16px}
.step{display:grid;grid-template-columns:28px 1fr;gap:10px;padding:9px 0;border-bottom:1px solid var(--bd)}
.step:last-child{border-bottom:0}
.badge{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;background:var(--p2);color:var(--mu);border:1px solid var(--bd2)}
.step.ok .badge{background:rgba(34,197,94,.14);color:#86efac;border-color:rgba(34,197,94,.5)}
.step.no .badge{background:rgba(239,68,68,.12);color:#fca5a5;border-color:rgba(239,68,68,.4)}
.step .t{font-weight:600;color:var(--br);font-size:13px}
.step .d{font-size:12px;color:var(--mu)}
.step .d b{color:var(--tx);font-family:ui-monospace,Consolas,monospace;font-weight:600}
.blk{background:rgba(245,158,11,.1);border-left:3px solid var(--or);color:#fcd34d;padding:6px 10px;border-radius:6px;font-size:12px;margin-top:6px}
.blk.ok{background:rgba(34,197,94,.1);border-left-color:var(--gn);color:#86efac}
.nopos{padding:34px 10px;text-align:center;color:var(--mu);font-size:13px}
.nopos b{color:var(--tx)}
.pos-head{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8px}
.pos-head .sym{font-size:18px}
.pos-head .pnl{font-size:24px;font-weight:700;font-family:ui-monospace,Consolas,monospace}
.ladder{position:relative;height:44px;margin:26px 0 30px}
.ladder .track{position:absolute;top:18px;left:0;right:0;height:8px;border-radius:4px;
 background:linear-gradient(90deg,var(--rd) 0%,#3b2530 25%,#1e2a3a 25%,#1e3a2c 75%,var(--gn) 100%)}
.ladder .tick{position:absolute;top:10px;width:2px;height:24px;background:var(--bd2)}
.ladder .tl{position:absolute;font-size:11px;white-space:nowrap;transform:translateX(-50%)}
.ladder .tl.up{top:-14px}.ladder .tl.dn{top:38px}
.ladder .now{position:absolute;top:8px;width:14px;height:28px;margin-left:-7px;border-radius:4px;
 background:var(--br);box-shadow:0 0 0 3px rgba(255,255,255,.15);transition:left .4s}
.facts{display:grid;grid-template-columns:repeat(2,1fr);gap:6px 14px;font-size:12px}
.facts div{display:flex;justify-content:space-between;border-bottom:1px dashed var(--bd);padding:3px 0}
.facts span:first-child{color:var(--mu)}
.facts span:last-child{font-family:ui-monospace,Consolas,monospace;color:var(--br)}
.tbar{height:6px;background:var(--p2);border-radius:3px;overflow:hidden;margin-top:4px}
.tbar i{display:block;height:100%;background:var(--or)}
.mrow{display:grid;grid-template-columns:1fr auto;gap:2px 10px;padding:7px 0;border-bottom:1px solid var(--bd)}
.mrow:last-child{border-bottom:0}
.mrow .nm{font-size:13px}
.mrow .vl{font-family:ui-monospace,Consolas,monospace;font-weight:700;color:var(--br);text-align:right}
.mrow .vl.g{color:#4ade80}.mrow .vl.r{color:#f87171}
.mrow .ex{grid-column:1/-1;font-size:11px;color:var(--mu)}
.x-TARGET,.x-TRAIL{background:rgba(34,197,94,.14);color:#86efac}
.x-STOP,.x-DATA_LOSS,.x-MTM_BREACH{background:rgba(239,68,68,.14);color:#fca5a5}
.x-TIME,.x-SIGNAL_DECAY,.x-EOD,.x-MANUAL_FLATTEN{background:var(--p2);color:var(--mu)}
.kd{background:var(--p2)}
.kd-entry{color:#86efac}.kd-exit{color:#f9a8d4}.kd-halt,.kd-error{color:#fca5a5}.kd-risk,.kd-token{color:#fcd34d}
.how{max-width:1040px}
.how h4{color:var(--br);font-size:15px;margin:22px 0 6px}.how h4:first-child{margin-top:0}
.how p,.how li{font-size:13px}
.flow{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:10px 0}
.flow span{background:var(--p2);border:1px solid var(--bd2);border-radius:8px;padding:6px 10px;font-size:12px}
.flow em{color:var(--mu);font-style:normal}
.logbox{background:var(--bg);border:1px solid var(--bd);border-radius:8px;padding:10px 12px;
 font-family:ui-monospace,Consolas,monospace;font-size:12px;white-space:pre-wrap;color:#a5f3fc;overflow-x:auto}
@media(max-width:760px){.hero{grid-template-columns:1fr}.ctl{min-width:0}}
@media(max-width:520px){.two{grid-template-columns:1fr}.facts{grid-template-columns:1fr}}
</style></head><body>

<div class="top">
  <div><h1>NIFTY Option Scalper (IVX-G)</h1>
    <p class="sub">Buys one at-the-money NIFTY option when volatility is rising and direction agrees - one position at a time, with a daily loss budget - paper trading</p></div>
  <div class="sp"></div>
  <span class="pill" id="p_mkt">-</span>
  <span class="pill" id="p_tok">-</span>
  <span class="pill" id="p_run">-</span>
  <button class="go" id="b_start">Start</button>
  <button class="stop" id="b_stop">Stop</button>
  <a href="/logout" class="btn sm ghost" id="logout" hidden>Log out</a>
</div>
<nav class="tabs" id="tabs">
  <button data-tab="dash" class="on">Dashboard</button>
  <button data-tab="report">Trade Report</button>
  <button data-tab="activity">Activity</button>
  <button data-tab="guide">Guide</button>
  <button data-tab="settings">Settings</button>
</nav>
<div class="statusline" id="statusline">-</div>

<main>
<!-- DASHBOARD -->
<section class="panel on" id="p-dash">
  <div class="note">Paper trading only - nothing is sent to the broker. It starts by itself when launched from NIFTY Trader. Stop blocks new entries; an open position keeps its stop, target, trail and time exits until it is out. The kill switch overrides everything, including the automatic start.</div>
  <div id="d_notes"></div>
  <div class="card hero t-wait" id="hero">
    <div>
      <div class="k">WHAT THE BOT IS DOING NOW &middot; <span id="state">-</span></div>
      <div class="headline" id="headline">Loading...</div>
      <div class="why" id="why"></div>
    </div>
    <div class="ctl">
      <div class="k">SAFETY CONTROLS</div>
      <div class="row">
        <button class="danger" id="btn_flat" title="Sell the open position at the bid - this also halts the bot for the day">Close position</button>
        <button class="stop" id="btn_kill" title="Stop everything for the day">Kill switch</button>
      </div>
      <button class="ghost" id="btn_rearm" hidden>Re-arm after halt</button>
    </div>
  </div>
  <div class="grid">
    <div class="card"><div class="k">TODAY'S NET P&amp;L</div><div class="v" id="net">-</div><div class="hint" id="wl">-</div></div>
    <div class="card"><div class="k">OPEN POSITION P&amp;L</div><div class="v" id="mtm">-</div><div class="hint" id="residual">-</div></div>
    <div class="card"><div class="k">LOSS BUDGET LEFT</div><div class="v" id="budget">-</div><div class="meter"><i id="budgetbar" style="width:100%"></i></div></div>
    <div class="card"><div class="k">TRADES LEFT TODAY</div><div class="v" id="left">-</div><div class="hint" id="cooldown">-</div></div>
    <div class="card"><div class="k">EXPIRY TRADED</div><div class="v" id="expiry">-</div><div class="hint" id="dte">-</div></div>
  </div>
  <div class="three">
    <div class="card"><h3>ENTRY CHECKLIST</h3>
      <p class="hint" style="margin-top:0">A trade opens only when all 5 checks are green at the same moment <i>and</i> nothing below is blocking.</p>
      <div id="gates"></div><div id="blocks"></div></div>
    <div class="card"><h3>OPEN POSITION</h3>
      <p class="hint" style="margin-top:0">Marked at the bid - the price you could actually sell at.</p>
      <div id="open_box"></div></div>
    <div class="card"><h3>MARKET READ</h3>
      <p class="hint" style="margin-top:0">Live numbers from the option chain, refreshed every ~4s.</p>
      <div id="metrics"></div></div>
  </div>
  <div class="card"><h3>RECENT ACTIVITY</h3><div class="tw" id="d_ev"></div></div>
</section>

<!-- TRADE REPORT -->
<section class="panel" id="p-report">
  <div class="bar">
    <span class="big" id="r_total">Realized P&amp;L: -</span><div class="sp"></div>
    <a href="/api/history.csv" class="btn sm" download>Download for Excel</a>
    <button class="sm danger" id="b_clear">Clear Selected</button>
    <button class="sm danger" id="b_wipe">Wipe All</button>
  </div>
  <div class="grid" id="r_stats"></div>
  <div class="card" style="margin-bottom:16px"><h3>CUMULATIVE REALIZED P&amp;L (NET OF COSTS)</h3><div id="r_chart"></div></div>
  <div class="card" style="margin-bottom:16px"><h3>TODAY</h3>
    <div class="hint">Cumulative net P&amp;L today, then every trade closed today.</div>
    <div id="r_today_chart"></div><div class="tw" id="r_today"></div></div>
  <div class="card" style="margin-bottom:16px"><h3>IS IT PROFITABLE?</h3><div id="exp_box"><div class="empty">Loading...</div></div></div>
  <div class="grid" id="r_break"></div>
  <div class="card"><h3>ALL TRADES</h3><div class="scroll" id="r_table"></div></div>
  <p class="hint">Net P&amp;L is after the cost per trade set in Settings. Download for Excel has every trade with the signal readings at entry.
    Clear and Wipe never destroy anything: removed trades are moved to trades_removed.jsonl in this strategy's data folder, and today's
    risk counters (loss budget, trades left) are left alone.</p>
</section>

<!-- ACTIVITY -->
<section class="panel" id="p-activity">
  <div class="bar">
    <select id="a_kind"><option value="">Every kind</option></select>
    <button class="sm ghost" id="a_refresh">Refresh</button>
    <span class="hint">The last 250 entries since this launch - the log is kept in memory and starts fresh on every restart.</span>
  </div>
  <div class="card scroll"><div id="a_table"></div></div>
  <div style="margin-top:10px"><span class="hint" id="a_note"></span></div>
</section>

<!-- GUIDE -->
<section class="panel" id="p-guide">
  <div class="card how">
    <h4>The idea in one line</h4>
    <p>Buy <b>one at-the-money NIFTY option</b> (CE or PE) only when option <b>volatility is rising</b>,
      three direction signals <b>agree</b>, and the target is realistically <b>reachable</b> before time decay eats the stop.
      Exit at +&#8377;3,000 target or &minus;&#8377;1,000 stop (or earlier via trail / time stop).</p>
    <div class="flow">
      <span>Every 4s: fetch option chain</span><em>&rarr;</em>
      <span>A. IV rising?</span><em>&rarr;</em><span>B. Direction agrees?</span><em>&rarr;</em>
      <span>C. Target reachable?</span><em>&rarr;</em><span>D. Spread OK?</span><em>&rarr;</em>
      <span>E. Theta OK?</span><em>&rarr;</em><span>Risk rules OK?</span><em>&rarr;</em>
      <span style="border-color:var(--gn);color:#86efac">BUY at ask</span>
    </div>

    <h4>Worked example (lot 65, target &#8377;3,000, stop &#8377;1,000)</h4>
    <p>It is 10:42 on a Thursday. NIFTY is 24,480. The next expiry is 4 days away.
       Once the buffer has 5 minutes of data, the bot reads:</p>
    <div class="two">
      <div class="tw"><table><thead><tr><th>Check</th><th>Reading</th><th>Needs</th><th>Result</th></tr></thead><tbody>
        <tr><td>A. IV slope</td><td>+0.12 vol/min</td><td>&ge; 0.08</td><td class="g">pass</td></tr>
        <tr><td>A. IV z-score</td><td>+0.90</td><td>&ge; 0.50</td><td class="g">pass</td></tr>
        <tr><td>B. Risk-reversal change</td><td>+0.15</td><td>&ge; +0.10</td><td class="g">bullish</td></tr>
        <tr><td>B. Basis slope</td><td>+0.45 pts/min</td><td>&ge; +0.30</td><td class="g">bullish</td></tr>
        <tr><td>B. Spot slope</td><td>+1.2 pts/min</td><td>&gt; 0</td><td class="g">bullish &rarr; CE</td></tr>
        <tr><td>C. Index move for target</td><td>87 pts</td><td>&le; 95</td><td class="g">pass</td></tr>
        <tr><td>C. Move in sigmas</td><td>1.54 &sigma;</td><td>&le; 2.2</td><td class="g">pass</td></tr>
        <tr><td>D. Spread</td><td>0.50</td><td>&le; 1.71</td><td class="g">pass</td></tr>
        <tr><td>E. Theta over 40 min</td><td>1.3 pts</td><td>&le; 4.6</td><td class="g">pass</td></tr>
      </tbody></table></div>
      <div>
        <p style="margin-top:0"><b>Entry:</b> buys 24500 CE &times; 65 at the <b>ask, 142.30</b>.</p>
        <p>Target = 3000 &divide; 65 = <b>46.15 pts</b> &rarr; sell at <b>188.45</b><br>
           Stop = 1000 &divide; 65 = <b>15.38 pts</b> &rarr; sell at <b>126.92</b><br>
           Trail arms at half the target &rarr; <b>165.38</b><br>
           Time stop: <b>40 min</b></p>
        <div class="logbox">[10:42:08] ENTRY  BUY 65 24500 CALL @ 142.30  target 188.45  stop 126.92  (IV slope +0.120, z +0.90)</div>
      </div>
    </div>

    <h4>The four ways it can end</h4>
    <div class="tw"><table><thead><tr><th>Scenario</th><th>Exit price</th><th>Gross</th><th>Costs</th><th>Net</th></tr></thead><tbody>
      <tr><td class="wrap"><span class="tag x-TARGET">TARGET</span> NIFTY rallies ~90 pts, bid reaches 188.45</td><td>188.45</td><td class="g">+&#8377;3,000</td><td>&#8377;75</td><td class="g"><b>+&#8377;2,925</b></td></tr>
      <tr><td class="wrap"><span class="tag x-TRAIL">TRAIL</span> bid peaks at 172, falls back 12 pts</td><td>160.00</td><td class="g">+&#8377;1,151</td><td>&#8377;75</td><td class="g"><b>+&#8377;1,076</b></td></tr>
      <tr><td class="wrap"><span class="tag x-TIME">TIME</span> goes nowhere for 40 min</td><td>145.00</td><td class="g">+&#8377;176</td><td>&#8377;75</td><td class="g"><b>+&#8377;101</b></td></tr>
      <tr><td class="wrap"><span class="tag x-STOP">STOP</span> NIFTY drops ~35 pts, bid gaps to 126.50</td><td>126.50</td><td class="r">&minus;&#8377;1,027</td><td>&#8377;75</td><td class="r"><b>&minus;&#8377;1,102</b></td></tr>
    </tbody></table></div>
    <div class="logbox" style="margin-top:10px">[11:03:44] EXIT   TARGET 24500 65 CALL @ 188.45  gross +3000  net +2925  (21.6)
[11:03:44] RISK   cooldown 60s after win</div>

    <h4>What happens after</h4>
    <ul>
      <li>After a <b>win</b>: 1-minute cooldown. After a <b>stop</b>: 5 min (1st), 15 min (2nd); <b>3 stops in a row halts the day</b>.</li>
      <li>Day halts at &minus;&#8377;3,000 net, +&#8377;6,000 net, or 6 trades. All positions are closed at 15:20.</li>
      <li>No new entries before 09:25 or after 15:00. 0-DTE is off by default.</li>
    </ul>

    <h4>Start, Stop and the kill switch</h4>
    <ul>
      <li><b>Launching</b> the strategy from NIFTY Trader starts it by itself, as soon as the broker token works. Until then the status line says what it is waiting for.</li>
      <li><b>Stop</b> blocks new entries. An open position keeps its stop, target, trail and time exits until it is out. <b>Start</b> resumes.</li>
      <li><b>Kill switch</b> stops the bot and halts the day. It stays on across restarts and also blocks the automatic start. Press <b>Re-arm after halt</b>, then <b>Start</b>, to trade again.</li>
      <li><b>Close position</b> sells the open position at the bid and halts the bot for the day.</li>
    </ul>

    <h4>The honest bit</h4>
    <p>3:1 reward:risk sounds great, but the stop is 3&times; closer than the target, so a random option hits the stop first ~75% of the time.
      Breakeven after costs is about <b>27%</b> wins. Most of the day you will see <b>"No trade"</b> - that is by design.
      Check <b>Is it profitable?</b> on the Trade Report tab after a few weeks of paper trading.</p>
  </div>
</section>

<!-- SETTINGS -->
<section class="panel" id="p-settings">
  <div id="s_form">
    <div class="card grp"><h3>EXITS</h3>
      <div class="f">
        <div class="fl"><label for="c_target">Target (&#8377;)</label><input type="number" id="c_target" step="100"><span class="hint">Profit to take per trade</span></div>
        <div class="fl"><label for="c_stop">Stop (&#8377;)</label><input type="number" id="c_stop" step="100"><span class="hint">Max loss per trade</span></div>
        <div class="fl"><label for="c_lots">Lots</label><input type="number" id="c_lots" min="1" max="20"><span class="hint">Contracts per trade</span></div>
        <div class="fl"><label for="c_cost">Cost per trade (&#8377;)</label><input type="number" id="c_cost" step="5"><span class="hint">Brokerage + taxes, round trip</span></div>
      </div></div>
    <div class="card grp"><h3>DAILY GUARDRAILS</h3>
      <div class="f">
        <div class="fl"><label for="c_loss">Daily loss cap (&#8377;)</label><input type="number" id="c_loss" step="500"><span class="hint">Halt when net loss reaches this</span></div>
        <div class="fl"><label for="c_profit">Daily profit stop (&#8377;)</label><input type="number" id="c_profit" step="500"><span class="hint">Halt when net profit reaches this</span></div>
        <div class="fl"><label for="c_maxtr">Max trades / day</label><input type="number" id="c_maxtr" min="1" max="50"></div>
        <div class="fl"><label for="c_conc">Max open at once</label><input type="number" id="c_conc" min="1" max="3"></div>
      </div></div>
    <div class="card grp"><h3>SIGNAL THRESHOLDS (ADVANCED)</h3>
      <div class="f">
        <div class="fl"><label for="c_ivs">Min IV slope</label><input type="number" id="c_ivs" step="0.01"><span class="hint">vol points / min</span></div>
        <div class="fl"><label for="c_ivz">Min IV z-score</label><input type="number" id="c_ivz" step="0.1"><span class="hint">IV vs its 5-min average</span></div>
        <div class="fl"><label for="c_rr">Min risk-reversal change</label><input type="number" id="c_rr" step="0.01"><span class="hint">vol points</span></div>
        <div class="fl"><label for="c_bs">Min basis slope</label><input type="number" id="c_bs" step="0.05"><span class="hint">index pts / min</span></div>
        <div class="fl"><label for="c_xt">Max index move for target</label><input type="number" id="c_xt" step="5"><span class="hint">index points</span></div>
        <div class="fl"><label for="c_ns">Max sigmas to target</label><input type="number" id="c_ns" step="0.1"><span class="hint">lower = stricter</span></div>
      </div></div>
    <div class="card grp"><h3>EXPIRY AND SESSION</h3>
      <div class="f">
        <div class="fl"><label for="c_dmin">Min days to expiry</label><input type="number" id="c_dmin" min="0" max="30"></div>
        <div class="fl"><label for="c_dmax">Max days to expiry</label><input type="number" id="c_dmax" min="0" max="60"></div>
      </div>
      <div class="chips" style="margin-top:12px">
        <label class="chip"><input type="checkbox" id="c_zero"> Allow expiry-day (0-DTE) trades <small>not recommended, ~18% expected hit rate</small></label>
        <label class="chip"><input type="checkbox" id="c_lunch"> Skip the 12:30-13:15 lunch lull</label>
      </div>
      <p class="hint" id="s_expinfo" style="margin-bottom:0"></p>
    </div>
    <div class="bar" style="margin:4px 0 0">
      <button class="go" id="b_save">Save settings</button>
      <button class="ghost" id="b_revert">Discard changes</button>
      <span class="hint" id="s_msg"></span>
    </div>
  </div>
  <div class="card" style="margin-top:14px"><h3>BROKER</h3>
    <div class="hint" id="s_tok">-</div>
    <div class="note info" id="s_tokhub" style="margin:10px 0 0" hidden>Set in NIFTY Trader's Broker token screen. This strategy restarts with a new token automatically, so there is nothing to paste here.</div>
    <div id="s_tokform" style="margin-top:10px;max-width:640px" hidden>
      <div class="fl"><label for="tok_in">Paste a fresh Dhan access token</label>
        <textarea id="tok_in" rows="3" placeholder="eyJ0eXAiOiJKV1Qi..."></textarea></div>
      <div class="bar" style="margin:8px 0 0"><button class="sm go" id="btn_tok">Save token</button></div>
    </div>
    <div class="bar" style="margin:10px 0 0">
      <button class="sm ghost" id="btn_test">Test connection</button>
      <span class="hint" id="tok_msg"></span>
    </div>
  </div>
</section>
</main>

<script>
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const num=(n,d)=>n==null||isNaN(n)?'-':Number(n).toFixed(d==null?2:d);
const inr=(n,d)=>n==null||isNaN(n)?'-':(n<0?'-':'')+'₹'+Math.abs(Number(n)).toLocaleString('en-IN',{minimumFractionDigits:d==null?2:d,maximumFractionDigits:d==null?2:d});
const inrShort=v=>{const a=Math.abs(v),s=v<0?'-':'';return a>=1e5?s+'₹'+(a/1e5).toFixed(a>=1e6?0:1)+'L':a>=1e3?s+'₹'+(a/1e3).toFixed(a>=1e4?0:1)+'k':s+'₹'+a.toFixed(0);};
const cls=n=>n>0?'g':(n<0?'r':'');
const rs=v=>v==null||isNaN(v)?'-':(v<0?'-':(v>0?'+':''))+'₹'+Math.abs(Math.round(v)).toLocaleString('en-IN');
const rsp=v=>v==null||isNaN(v)?'-':'₹'+Math.round(v).toLocaleString('en-IN');
const sgn=(v,d)=>v==null||isNaN(v)?'-':(v>0?'+':'')+Number(v).toFixed(d==null?2:d);
const hm=t=>String(t||'').slice(11,16);
const tag=t=>'<span class="tag '+(t==='PE'?'pe':'ce')+'">'+esc(t)+'</span>';
const sideOf=t=>t.option_type==='CALL'?'CE':'PE';
const optName=t=>'<b>'+esc(Math.round(t.strike))+'</b> '+tag(sideOf(t));
const reason=r=>'<span class="tag x-'+esc(r)+'">'+esc(String(r||'-').replace(/_/g,' '))+'</span>';
const table=(head,rows,empty)=>rows.length?'<table><thead><tr>'+head.map(h=>'<th>'+h+'</th>').join('')+'</tr></thead><tbody>'+rows.join('')+'</tbody></table>':'<div class="empty">'+empty+'</div>';
function setHTML(el,html){if(el&&el.__h!==html){el.innerHTML=html;el.__h=html;}}
// Every request carries the CSRF header from the csrf cookie (hosted mode);
// a 401 means the session ended, so go to the sign-in page.
const csrf=()=>(document.cookie.match(/(?:^|;\s*)csrf=([^;]+)/)||[,''])[1];
async function api(u,o){o=o||{};
  o.headers=Object.assign({'X-CSRF-Token':decodeURIComponent(csrf())},o.headers||{});
  if(o.body)o.headers['Content-Type']='application/json';
  const r=await fetch(u,o);
  if(r.status===401){location.href='/login';throw new Error('not signed in');}
  const d=await r.json().catch(()=>({}));
  if(!r.ok)throw new Error(d.error||('failed ('+r.status+')'));
  return d;}
const post=(u,b)=>api(u,{method:'POST',body:JSON.stringify(b||{})});
const get=u=>api(u);
const store={get(k){try{return localStorage.getItem(k);}catch(e){return null;}},set(k,v){try{localStorage.setItem(k,v);}catch(e){}}};

/* ---------- tabs ---------- */
let TAB='dash';
function showTab(t){if(!$('#p-'+t))t='dash';TAB=t;store.set('scalp_tab',t);
  $$('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.tab===t));
  $$('.panel').forEach(p=>p.classList.toggle('on',p.id==='p-'+t));
  if(t==='report')loadReport(); if(t==='activity')loadEvents();}
$('#tabs').onclick=e=>{const b=e.target.closest('button[data-tab]');if(b)showTab(b.dataset.tab);};

/* ---------- what the bot is doing ---------- */
function tokenWhere(tk){
  if(tk.source==='environment')return "Update it in NIFTY Trader's Broker token screen - this strategy restarts with it automatically.";
  if(tk.source==='not configured')return "Set it in NIFTY Trader's Broker token screen (or on the Settings tab when this runs on its own).";
  return 'Paste a fresh one on the Settings tab.';}
function heroFor(s){
  const sig=s.signal||{},st=s.machine_state,ot=s.open_trades||[];
  if(st==='KILLED')return ['t-stop','Kill switch is ON','Nothing will trade, and it will not start by itself. Press "Re-arm after halt", then Start.'];
  if(st==='HALTED')return ['t-stop','Halted for the day',(s.halt_reason||'')+' - "Re-arm after halt" resumes it; otherwise it clears at the next session.'];
  if(ot.length){const t=ot[0];
    return ['t-trade','In a trade: '+Math.round(t.strike)+' '+sideOf(t)+'  '+rs(t.mtm),'Bought at '+num(t.entry_fill)+'. Exits at target '+num(t.target_price)+
      ', stop '+num(t.stop_price)+', or after '+num(t.time_stop_min,0)+' min.'+(s.running?'':' Stopped: no new entries after this one.')];}
  if(st==='COOLDOWN')return ['t-cool','Cooling down ('+s.cooldown_left+'s)','Short pause after the last exit before looking for a new entry.'];
  if(!s.running)return s.autostart?['t-wait','Starting automatically',s.status||'Waiting for the broker token.']:
    ['t-wait','Stopped','Press Start (top right) to let the bot look for trades. It will not open a trade until you do.'];
  if(sig.side)return ['t-ready','Signal: BUY '+sig.strike+' '+sig.side.toUpperCase(),s.can_enter?'Entering on this tick.':'Risk rules holding: '+s.risk_gate];
  const passed=Object.values(sig.gates||{}).filter(Boolean).length;
  const first=(sig.blocks||[])[0]||(s.can_enter?'':s.risk_gate);
  return ['t-ready','Watching - no trade yet ('+passed+'/5 checks pass)',
    first?'Main reason: '+plain(first):'All clear on blockers; waiting for all 5 checks to line up.'];}
function plain(b){b=String(b);
  if(b.startsWith('WARMING'))return 'collecting 5 minutes of data first '+(b.match(/\(.*\)/)||[''])[0];
  if(b.startsWith('N5'))return 'market clock - '+b.replace(/^N5 clock:\s*/,'');
  if(b.startsWith('N7'))return 'data is stale '+(b.match(/\(.*\)/)||[''])[0];
  if(b.startsWith('N1'))return 'volatility is falling - buying now would lose to vol crush';
  if(b.startsWith('N4'))return 'expiry-day trading is disabled';
  if(b.includes('too quiet'))return 'market is too quiet to reach the target';
  if(b.includes('gapping'))return 'market is too jumpy';
  return b.replace(/^N[-\w]*\s*/,'');}
function gatesHtml(s){
  const sig=s.signal||{},g=sig.gates||{},d=sig.detail||{},c=s.cfg;
  const dir=d.d_rr==null?'-':(sig.side?(sig.side==='ce'?'bullish → CE':'bearish → PE'):(d.direction_note||'no clear direction'));
  const items=[
    ['A_iv_expansion','Volatility is rising','IV slope <b>'+sgn(d.iv_slope,3)+'</b> (need ≥ '+esc(c.iv_slope_min)+') · z <b>'+sgn(d.iv_z,2)+'</b> (need ≥ '+esc(c.iv_z_min)+')'],
    ['B_direction','Direction agrees ('+esc(dir)+')','RR Δ <b>'+sgn(d.d_rr,2)+'</b> · basis <b>'+sgn(d.basis_slope,2)+'</b>/min · spot <b>'+sgn(d.spot_slope,2)+'</b>/min'],
    ['C_feasible','Target is reachable','needs <b>'+num(d.x_target,0)+'</b> index pts (max '+esc(c.x_target_max)+') = <b>'+num(d.need_sigma,2)+'σ</b> (max '+esc(c.need_sigma_max)+')'],
    ['D_liquidity','Spread &amp; depth OK','spread <b>'+num(d.spread,2)+'</b> (max '+num(d.spread_limit,2)+')'],
    ['E_theta','Time decay is affordable','theta <b>'+rsp(d.theta_rupees_per_min)+'</b>/min over '+num(d.t_stop_min,0)+' min']];
  const noData=!Object.keys(g).length;
  return items.map((it,i)=>{const st=noData?'':(g[it[0]]?'ok':'no');
    return '<div class="step '+st+'"><div class="badge">'+(st==='ok'?'✓':'ABCDE'[i])+'</div><div><div class="t">'+it[1]+'</div><div class="d">'+it[2]+'</div></div></div>';}).join('');}
function positionHtml(t){
  const lo=t.stop_price,hi=t.target_price,span=(hi-lo)||1;
  const p=v=>Math.max(0,Math.min(100,(v-lo)/span*100));
  const heldMin=(Date.now()/1000-t.entry_epoch)/60;
  const tpct=Math.max(0,Math.min(100,heldMin/t.time_stop_min*100));
  const marks=[[lo,'Stop '+num(lo),'r','dn'],[t.entry_fill,'Entry '+num(t.entry_fill),'','dn'],[hi,'Target '+num(hi),'g','dn'],[t.trail_arm_price,'Trail arms','hint','up']];
  if(t.trail_price)marks.push([t.trail_price,'Trail '+num(t.trail_price),'g','up']);
  return '<div class="pos-head"><div><span class="sym">'+optName(t)+'</span> <span class="hint">×'+esc(t.quantity)+' · '+esc(t.expiry)+'</span></div><div class="pnl '+cls(t.mtm)+'">'+rs(t.mtm)+'</div></div>'+
    (t.stale?'<div class="blk">Price feed stale - holding last mark</div>':'')+
    '<div class="ladder"><div class="track"></div>'+
    marks.map(m=>'<div class="tick" style="left:'+p(m[0])+'%"></div><div class="tl '+m[3]+' '+m[2]+'" style="left:'+Math.max(8,Math.min(92,p(m[0])))+'%">'+m[1]+'</div>').join('')+
    '<div class="now" style="left:'+p(t.mark)+'%" title="Now '+num(t.mark)+'"></div></div>'+
    '<div class="facts">'+
    '<div><span>Bid now</span><span>'+num(t.mark)+'</span></div>'+
    '<div><span>Entry</span><span>'+num(t.entry_fill)+' @ '+esc(hm(t.entry_time))+'</span></div>'+
    '<div><span>To target</span><span class="g">'+num(hi-t.mark)+' pts</span></div>'+
    '<div><span>To stop</span><span class="r">'+num(t.mark-lo)+' pts</span></div>'+
    '<div><span>IV entry → now</span><span>'+num(t.entry_iv,1)+' → '+num(t.iv_now,1)+'</span></div>'+
    '<div><span>Best bid</span><span>'+num(t.high_water_bid)+'</span></div></div>'+
    '<div class="hint" style="margin-top:10px">Time stop: '+num(heldMin,1)+' of '+num(t.time_stop_min,0)+' min</div>'+
    '<div class="tbar"><i style="width:'+tpct+'%"></i></div>';}

/* ---------- live state ---------- */
let S=null,todayKey=null;
async function poll(){
  let s;
  try{s=await get('/api/state');}catch(e){$('#statusline').textContent='cannot reach the strategy: '+e.message;return;}
  S=s;const c=s.cfg,tk=s.token,ot=s.open_trades||[],m=s.metrics||{},sig=s.signal||{};
  $('#p_mkt').textContent=s.market||'-';
  $('#p_tok').textContent='token '+tk.human; $('#p_tok').className='pill '+(tk.configured&&!tk.expired?'on':'off');
  // The pill has to agree with the hero and with can_enter(): halt() only sets
  // halted (roll_day clears it at the next session), so running stays True after
  // the 15:25 halt or a risk stop - 'RUNNING' alone would claim the bot is still
  // trading for the rest of the day while it cannot open a thing.
  const rp=s.kill?['KILLED','off']:(s.halted?['HALTED','off']:(s.running?['RUNNING','on']:(s.autostart?['STARTING','']:['STOPPED','off'])));
  $('#p_run').textContent=rp[0]; $('#p_run').className='pill '+rp[1];
  $('#b_start').disabled=s.running||s.kill||!s.owner;
  $('#b_start').title=s.kill?'The kill switch is on - press Re-arm after halt first':(!s.owner?'Another copy owns the scalper - this window is view-only':'');
  $('#b_stop').disabled=!(s.running||s.autostart);
  $('#logout').hidden=!s.auth_on;
  const feed=s.data_ok?'data live':(s.buffer?'data stale':'no data');
  $('#statusline').textContent=s.status+(m.spot?'   |   NIFTY '+num(m.spot,2):'')+'   |   '+feed+' - '+s.buffer+' snapshots'+
    (s.buffer_warm?'':' (warming up)')+(s.buffer_age!=null?', last '+s.buffer_age+'s ago':'')+'   |   '+s.updated+' IST';

  /* dashboard */
  const n=[];
  if(!tk.configured||tk.expired)n.push('<div class="note bad"><b>Broker token '+esc(tk.human)+'.</b> '+esc(tokenWhere(tk))+(s.autostart?' Trading starts by itself as soon as a working token is in.':'')+'</div>');
  else if(tk.warn)n.push('<div class="note">Broker token '+esc(tk.human)+'. '+esc(tokenWhere(tk))+'</div>');
  if(!s.owner)n.push('<div class="note">Another copy of the app is running the bot. This window is view-only - it never starts trading.</div>');
  setHTML($('#d_notes'),n.join(''));
  const h=heroFor(s);
  $('#hero').className='card hero '+h[0];
  $('#state').textContent=String(s.machine_state).replace('_',' ');
  $('#headline').textContent=h[1]; $('#why').textContent=h[2];
  $('#btn_flat').disabled=!ot.length;
  $('#btn_rearm').disabled=!(s.kill||s.halted); $('#btn_rearm').hidden=!(s.kill||s.halted);

  $('#net').textContent=rs(s.realised_net); $('#net').className='v '+cls(s.realised_net);
  $('#wl').textContent=s.wins+' wins · '+s.losses+' losses';
  $('#mtm').textContent=ot.length?rs(s.open_mtm):'-'; $('#mtm').className='v '+(ot.length?cls(s.open_mtm):'');
  $('#residual').textContent=ot.length?'can still lose '+rsp(s.residual_risk):'no open position';
  $('#budget').textContent=rsp(s.loss_budget_left);
  const bp=c.daily_loss_cap>0?Math.max(0,Math.min(100,s.loss_budget_left/c.daily_loss_cap*100)):0;
  $('#budgetbar').style.width=bp+'%';
  $('#budgetbar').style.background=bp>50?'var(--gn)':bp>25?'var(--or)':'var(--rd)';
  $('#left').textContent=s.trades_left+' / '+c.max_trades;
  $('#cooldown').textContent=s.cooldown_left?'cooldown '+s.cooldown_left+'s':(s.consecutive_stops?s.consecutive_stops+' stop(s) in a row':'no cooldown');
  $('#expiry').textContent=s.expiry||'-';
  $('#dte').textContent=(s.dte==null?'':s.dte+' days to expiry · ')+'lot '+s.lot;

  setHTML($('#gates'),gatesHtml(s));
  const blocks=(sig.blocks||[]).slice();
  if(!s.can_enter&&s.running)blocks.push('Risk: '+(s.risk_gate||'blocked'));
  setHTML($('#blocks'),blocks.length?'<div class="hint" style="font-weight:600;margin-top:8px">Blocking right now:</div>'+
    blocks.map(x=>'<div class="blk" title="'+esc(x)+'">'+esc(plain(x))+'</div>').join(''):
    (s.running?'<div class="blk ok">Nothing blocking. Waiting for all 5 checks to line up.</div>':''));

  const d=sig.detail||{};
  const mr=(nm,vl,ex,k)=>'<div class="mrow"><span class="nm">'+nm+'</span><span class="vl '+(k||'')+'">'+vl+'</span><span class="ex">'+ex+'</span></div>';
  setHTML($('#metrics'),
    mr('NIFTY spot',num(m.spot,2),'Trend '+sgn(m.spot_slope,2)+' pts/min · realised move '+num(m.sigma_min,1)+' pts/min','')+
    mr('ATM implied volatility',num(m.iv_atm,2)+'%',m.iv_slope==null?'Needs a few minutes of data':
      (m.iv_slope>0?'Rising ':'Falling ')+sgn(m.iv_slope,3)+' vol/min - '+(m.iv_slope>=c.iv_slope_min?'good for buyers':m.iv_slope<=-0.05?'bad for buyers':'flat'),
      m.iv_slope==null?'':cls(m.iv_slope))+
    mr('Risk reversal (25Δ)',num(m.rr,2),'Call IV − put IV. Rising = market paying up for upside',cls(d.d_rr))+
    mr('Synthetic basis',num(m.basis,2),'Where options price the forward vs spot',cls(d.basis_slope))+
    mr('Target / stop',num(d.target_pts,1)+' / '+num(d.stop_pts,1)+' pts',rsp(c.target_rupees)+' / '+rsp(c.stop_rupees)+' on '+(s.lot*c.lots)+' qty')+
    mr('Premium',sig.quote?num(sig.quote.bid)+' / '+num(sig.quote.ask):'-',
      sig.quote?'bid / ask of candidate '+esc(sig.strike)+' '+esc((sig.side||'').toUpperCase()):'Shown once a direction is picked')+
    mr('Data feed',feed,s.buffer+' snapshots'+(s.buffer_warm?' (warm)':' (warming up)')+(s.buffer_age!=null?' · last '+s.buffer_age+'s ago':''),s.data_ok?'g':'r'));

  setHTML($('#open_box'),ot.length?ot.map(positionHtml).join('<hr style="border:0;border-top:1px solid var(--bd);margin:14px 0">'):
    '<div class="nopos"><b>No open position</b><br>When the checklist turns fully green, a trade appears here with its stop, target and live P&amp;L.</div>');

  /* trade report: today */
  const today=s.today_trades||[];
  setHTML($('#r_today'),table(['Time','Option','Bought','Sold','Held','Exit reason','Gross','Net','Slip'],today.slice().reverse().map(t=>
    '<tr><td class="mono">'+esc(hm(t.entry_time))+'–'+esc(hm(t.exit_time))+'</td><td>'+optName(t)+'</td>'+
    '<td>'+num(t.entry_fill)+'</td><td>'+num(t.exit_fill)+'</td><td>'+num(t.held_min,1)+'m</td><td>'+reason(t.exit_reason)+'</td>'+
    '<td class="'+cls(t.gross_pnl)+'">'+rs(t.gross_pnl)+'</td><td class="'+cls(t.net_pnl)+'"><b>'+rs(t.net_pnl)+'</b></td>'+
    '<td class="hint">'+num(t.slippage_pts)+'</td></tr>'),
    'No trades today yet. Most sessions have only a few - the filters are strict on purpose.'));
  const key=today.map(t=>t.id).join(',');
  if(key!==todayKey){const changed=todayKey!==null;todayKey=key;
    if(TAB==='report'){if(changed)loadReport();else equityChart($('#r_today_chart'),seriesOf(today));}}

  paintSettings(s);
}

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
  const dots=n<=200?series.map((p,i)=>'<circle class="dot" stroke="'+(p.pnl>=0?'#22c55e':'#ef4444')+'" cx="'+X(i+1).toFixed(1)+'" cy="'+Y(p.cum).toFixed(1)+'" r="3.2"><title>#'+(i+1)+'  '+esc(p.contract)+'  '+esc(p.closed)+'\ntrade '+inr(p.pnl)+'   cumulative '+inr(p.cum)+'</title></circle>').join(''):'';
  el.innerHTML='<svg width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'">'+g+
    '<line class="zero" x1="'+L+'" x2="'+(W-R)+'" y1="'+Y(0).toFixed(1)+'" y2="'+Y(0).toFixed(1)+'"/>'+
    '<path d="'+area+'" fill="'+col+'" fill-opacity=".13"/><path d="'+line+'" fill="none" stroke="'+col+'" stroke-width="2"/>'+dots+xl+'</svg>';
  el.__h=null;
}
function seriesOf(rows){let cum=0;return rows.map(t=>{const p=Number(t.net_pnl)||0;cum+=p;
  return {cum:Math.round(cum*100)/100,pnl:p,contract:Math.round(t.strike)+' '+sideOf(t)+' '+(t.expiry||''),closed:(t.exit_time||'')+' '+(t.exit_reason||'')};});}
function tradeStats(rows){
  const p=rows.map(t=>Number(t.net_pnl)||0),n=p.length,w=p.filter(x=>x>0),l=p.filter(x=>x<0);
  const ws=w.reduce((a,b)=>a+b,0),ls=l.reduce((a,b)=>a+b,0);
  let cum=0,peak=0,dd=0;p.forEach(x=>{cum+=x;peak=Math.max(peak,cum);dd=Math.min(dd,cum-peak);});
  return {trades:n,wins:w.length,losses:l.length,win_rate:n?Math.round(w.length/n*1000)/10:0,
    avg_win:w.length?ws/w.length:0,avg_loss:l.length?ls/l.length:0,
    profit_factor:ls?Math.round(ws/Math.abs(ls)*100)/100:(w.length?'inf':null),
    total:ws+ls,best:n?Math.max(...p):0,worst:n?Math.min(...p):0,max_drawdown:dd};}
function groupBy(rows,f){const g={};rows.forEach(t=>{const k=String(f(t)),p=Number(t.net_pnl)||0,e=g[k]||(g[k]={n:0,pnl:0,wins:0});e.n++;e.pnl+=p;if(p>0)e.wins++;});return g;}
function statCard(k,v,c,h){return '<div class="card"><div class="k">'+k+'</div><div class="v '+(c||'')+'">'+v+'</div>'+(h?'<div class="hint">'+h+'</div>':'')+'</div>';}
function breakCard(title,g,label){const ks=Object.keys(g||{}).sort((a,b)=>(parseFloat(a)-parseFloat(b))||a.localeCompare(b));
  return '<div class="card"><h3>'+title+'</h3>'+table(['','Trades','Win rate','P&amp;L'],ks.map(k=>'<tr><td>'+(label?label(k):esc(k))+'</td><td>'+g[k].n+'</td><td>'+
    (g[k].n?Math.round(g[k].wins/g[k].n*100):0)+'%</td><td class="'+cls(g[k].pnl)+'">'+inr(g[k].pnl,0)+'</td></tr>'),'-')+'</div>';}
function paintExpectancy(e){
  const a=e.actual||{},beat=a.win_rate!=null&&a.win_rate>=e.breakeven_pct;
  let h='<div class="note '+(a.trades?(beat?'info':'bad'):'')+'">'+(a.trades
    ?(beat?'So far your win rate ('+esc(a.win_rate)+'%) is <b>above</b> breakeven ('+esc(e.breakeven_pct)+'%) over '+esc(a.trades)+' trades.'
          :'So far your win rate ('+esc(a.win_rate)+'%) is <b>below</b> breakeven ('+esc(e.breakeven_pct)+'%) over '+esc(a.trades)+' trades.')+
      (a.trades<50?' Fewer than 50 trades is too few to trust.':'')
    :'No trades yet. You need to win at least <b>'+esc(e.breakeven_pct)+'%</b> of trades to break even.')+'</div>';
  h+='<div class="grid">'+statCard('REWARD : RISK',esc(e.reward_risk)+' : 1','',esc(e.target_pts)+' vs '+esc(e.stop_pts)+' pts')+
    statCard('BREAKEVEN WIN RATE','<span style="color:var(--or)">'+esc(e.breakeven_pct)+'%</span>','','after ₹'+esc(e.cost_per_trade)+' costs')+
    statCard('YOUR WIN RATE',a.win_rate==null?'-':esc(a.win_rate)+'%',a.win_rate==null?'':(beat?'g':'r'),esc(a.trades||0)+' trades')+
    statCard('AVG NET / TRADE',a.per_trade==null?'-':rs(a.per_trade),cls(a.per_trade),'total '+(a.net==null?'-':rs(a.net)))+'</div>';
  const win=e.target_pts*e.qty-e.cost_per_trade,loss=e.stop_pts*e.qty+e.cost_per_trade;
  const rows=[15,20,25,30,35,40,50].map(w=>{const per=(w/100)*win-(1-w/100)*loss;
    const mark=a.win_rate!=null&&Math.abs(a.win_rate-w)<2.5?'← you':(Math.abs(e.breakeven_pct-w)<2.5?'≈ breakeven':'');
    return '<tr><td>'+w+'%</td><td class="'+cls(per)+'">'+rs(per)+'</td><td class="'+cls(per)+'">'+rs(per*6)+'</td><td class="'+cls(per)+'"><b>'+rs(per*120)+'</b></td><td class="hint">'+mark+'</td></tr>';});
  h+='<div class="hint" style="margin-bottom:6px">What you would make at different win rates (all trades hit target or stop):</div>'+
    '<div class="tw">'+table(['Win rate','Per trade','Per day (6 trades)','Per month (20 days)',''],rows,'-')+'</div>';
  setHTML($('#exp_box'),h);}
let REPORT=null,repBusy=false;
async function loadReport(){
  if(repBusy)return; repBusy=true;
  try{
    let d,e;
    try{[d,e]=await Promise.all([get('/api/history'),get('/api/expectancy')]);}catch(err){$('#r_total').textContent=err.message;return;}
    REPORT=d;
    const rows=(d.rows||[]).slice().reverse(),st=tradeStats(rows);   // oldest first
    $('#r_total').textContent='Realized P&L: '+inr(st.total)+(d.count>rows.length?'  (last '+rows.length+' of '+d.count+' trades)':'');
    $('#r_total').className='big '+cls(st.total);
    setHTML($('#r_stats'),statCard('TRADES',st.trades,'',st.wins+' won / '+st.losses+' lost')+
      statCard('WIN RATE',st.win_rate+'%',st.trades?(st.win_rate>=50?'g':'r'):'')+
      statCard('AVG WIN',inr(st.avg_win,0),'g','best '+inr(st.best,0))+
      statCard('AVG LOSS',inr(st.avg_loss,0),st.losses?'r':'','worst '+inr(st.worst,0))+
      statCard('PROFIT FACTOR',st.profit_factor==null?'-':(st.profit_factor==='inf'?'∞':st.profit_factor),
        st.profit_factor==null?'':((st.profit_factor==='inf'||st.profit_factor>=1)?'g':'r'),st.profit_factor==='inf'?'no losing trade yet':'gross wins / gross losses')+
      statCard('MAX DRAWDOWN',inr(st.max_drawdown,0),st.max_drawdown<0?'r':'','deepest fall from a peak'));
    REPORT.series=seriesOf(rows);
    equityChart($('#r_chart'),REPORT.series);
    if(S)equityChart($('#r_today_chart'),seriesOf(S.today_trades||[]));
    setHTML($('#r_break'),breakCard('BY SIDE',groupBy(rows,sideOf),tag)+breakCard('BY EXIT REASON',groupBy(rows,t=>t.exit_reason||'?'),reason)+
      breakCard('BY DAYS TO EXPIRY',groupBy(rows,t=>t.dte==null?'?':t.dte+' days')));
    // The report reloads itself every 20s and whenever a trade closes; a tick
    // the user has already made must survive that, or Clear Selected would
    // quietly act on fewer trades than were ticked.
    const ticked=new Set($$('.r_chk').filter(c=>c.checked).map(c=>c.value));
    setHTML($('#r_table'),table(['<input type="checkbox" id="r_all">','Date','Time','Option','Expiry','DTE','Qty','Bought','Sold','Held','Exit reason','Gross','Net','Slip','IV slope','IV z'],(d.rows||[]).map(t=>{const g=t.signal||{};
      return '<tr><td><input type="checkbox" class="r_chk" value="'+esc(t.id)+'"></td>'+
        '<td class="mono">'+esc(String(t.entry_time||'').slice(0,10))+'</td><td class="mono">'+esc(hm(t.entry_time))+'–'+esc(hm(t.exit_time))+'</td><td>'+optName(t)+'</td>'+
        '<td>'+esc(t.expiry)+'</td><td>'+esc(t.dte)+'</td><td>'+esc(t.quantity)+'</td><td>'+num(t.entry_fill)+'</td><td>'+num(t.exit_fill)+'</td><td>'+num(t.held_min,1)+'m</td>'+
        '<td>'+reason(t.exit_reason)+'</td><td class="'+cls(t.gross_pnl)+'">'+rs(t.gross_pnl)+'</td><td class="'+cls(t.net_pnl)+'"><b>'+rs(t.net_pnl)+'</b></td>'+
        '<td class="hint">'+num(t.slippage_pts)+'</td><td class="hint">'+num(g.iv_slope,3)+'</td><td class="hint">'+num(g.iv_z,2)+'</td></tr>';}),'No trades yet.'));
    if(ticked.size){const c=$$('.r_chk');c.forEach(x=>{x.checked=ticked.has(x.value);});
      if($('#r_all'))$('#r_all').checked=c.length>0&&c.every(x=>x.checked);}
    paintExpectancy(e);
  }finally{repBusy=false;}
}
// The header checkbox is delegated because setHTML replaces the table on every
// reload, which would drop a handler bound to the element itself.
document.addEventListener('change',e=>{if(e.target.id==='r_all')$$('.r_chk').forEach(c=>c.checked=e.target.checked);});
$('#b_clear').onclick=async()=>{const ids=$$('.r_chk').filter(c=>c.checked).map(c=>c.value);
  if(!ids.length){alert('Tick the trades to clear first.');return;}
  if(!confirm('Remove '+ids.length+' trade(s) from the report?\n\nThey are moved to trades_removed.jsonl, not destroyed. Today\'s loss budget and trade count do not change.'))return;
  try{await post('/api/history/clear',{ids});}catch(err){alert(err.message);} loadReport();};
$('#b_wipe').onclick=async()=>{if(!confirm('Remove EVERY trade from the report?\n\nThey are moved to trades_removed.jsonl, not destroyed. Today\'s loss budget and trade count do not change.'))return;
  try{await post('/api/history/wipe');}catch(err){alert(err.message);} loadReport();};
window.addEventListener('resize',()=>{if(TAB!=='report')return;
  if(REPORT&&REPORT.series)equityChart($('#r_chart'),REPORT.series);
  if(S)equityChart($('#r_today_chart'),seriesOf(S.today_trades||[]));});

/* ---------- activity ---------- */
const KINDS=['entry','exit','trail','risk','halt','run','cfg','report','data','token','day','boot','error'];
KINDS.forEach(k=>{const o=document.createElement('option');o.value=k;o.textContent=k;$('#a_kind').appendChild(o);});
let EV=[],evBusy=false;
function eventRows(evs){return table(['Time','Kind','What happened'],evs.map(e=>
  '<tr><td class="mono">'+esc(e.ts)+'</td><td><span class="tag kd kd-'+esc(e.kind)+'">'+esc(e.kind)+'</span></td><td class="wrap">'+esc(e.msg)+'</td></tr>'),'Nothing logged yet.');}
function paintEvents(){const k=$('#a_kind').value,rows=k?EV.filter(e=>e.kind===k):EV;
  setHTML($('#a_table'),eventRows(rows)); $('#a_note').textContent=rows.length+' shown';
  setHTML($('#d_ev'),eventRows(EV.slice(0,10)));}
async function loadEvents(){if(evBusy)return; evBusy=true;
  try{const d=await get('/api/events');EV=(d.events||[]).slice().reverse();}catch(e){}
  evBusy=false; paintEvents();}
$('#a_kind').onchange=paintEvents; $('#a_refresh').onclick=loadEvents;

/* ---------- settings ---------- */
const FIELDS=[['c_target','target_rupees'],['c_stop','stop_rupees'],['c_lots','lots'],['c_cost','cost_per_trade'],
  ['c_loss','daily_loss_cap'],['c_profit','daily_profit_stop'],['c_maxtr','max_trades'],['c_conc','max_concurrent'],
  ['c_ivs','iv_slope_min'],['c_ivz','iv_z_min'],['c_rr','rr_delta_min'],['c_bs','basis_slope_min'],
  ['c_xt','x_target_max'],['c_ns','need_sigma_max'],['c_dmin','dte_min'],['c_dmax','dte_max']];
const CHECKS=[['c_zero','allow_zero_dte'],['c_lunch','lunch_block']];
let touched=false;
function chips(){CHECKS.forEach(x=>{const el=$('#'+x[0]);el.closest('.chip').classList.toggle('on',el.checked);});}
$('#s_form').addEventListener('input',()=>{touched=true;chips();});
$('#s_form').addEventListener('change',()=>{touched=true;chips();});
function fillCfg(c){FIELDS.forEach(x=>{if(c[x[1]]!=null)$('#'+x[0]).value=c[x[1]];});CHECKS.forEach(x=>{$('#'+x[0]).checked=!!c[x[1]];});chips();}
const dteOf=e=>Math.floor((Date.parse(e+'T15:30:00+05:30')-Date.now())/864e5);
function paintSettings(s){
  const tk=s.token,hub=tk.source==='environment';
  setHTML($('#s_tok'),'Token <b>'+esc(tk.human)+'</b> - from '+esc(tk.source)+(tk.client_id?' - client '+esc(tk.client_id):'')+
    (tk.masked?' - '+esc(tk.masked):'')+(tk.exp_ist?' - valid until '+esc(tk.exp_ist):''));
  $('#s_tokhub').hidden=!hub; $('#s_tokform').hidden=hub;
  const list=(s.expiry_list||[]).slice(0,8).map(e=>esc(e)+' ('+dteOf(e)+'d)');
  setHTML($('#s_expinfo'),'Trading now: <b>'+esc(s.expiry||'none')+'</b>'+(s.dte!=null?' ('+s.dte+' days)':'')+'. Listed by the broker: '+
    (list.length?list.join(', ')+((s.expiry_list||[]).length>8?', ...':''):'loads once the broker token works')+
    '. The bot trades the nearest listed expiry inside this window (0-DTE only when allowed). It is picked when the app launches and kept until it expires, so a change here takes effect from the next launch.');
  if(!touched)fillCfg(s.cfg);
}
$('#b_save').onclick=async()=>{
  const b={};
  for(const x of FIELDS){const el=$('#'+x[0]),lab=el.closest('.fl').querySelector('label').textContent.trim();
    if(el.value.trim()===''){alert(lab+' is empty.');el.focus();return;}
    const v=Number(el.value);
    if(!isFinite(v)){alert(lab+' must be a number.');el.focus();return;}
    if(el.min!==''&&v<Number(el.min)){alert(lab+' must be at least '+el.min+'.');el.focus();return;}
    b[x[1]]=v;}
  if(b.dte_min>b.dte_max){alert('Min days to expiry is above Max days to expiry - no expiry could ever be picked.');$('#c_dmin').focus();return;}
  CHECKS.forEach(x=>{b[x[1]]=$('#'+x[0]).checked;});
  try{const r=await post('/api/config',b);touched=false;
    $('#s_msg').textContent='Saved. You now need to win '+r.expectancy.breakeven_pct+'% of trades to break even.';poll();}
  catch(e){alert(e.message);}
};
$('#b_revert').onclick=()=>{touched=false;$('#s_msg').textContent='';poll();};
$('#btn_tok').onclick=async()=>{const t=$('#tok_in').value.trim();if(!t){alert('Paste a token first.');return;}
  try{await post('/api/token',{token:t});$('#tok_in').value='';$('#tok_msg').textContent='Token saved.';poll();}
  catch(e){$('#tok_msg').textContent=e.message;alert(e.message);}};
$('#btn_test').onclick=async()=>{$('#tok_msg').textContent='Testing...';
  try{const d=await post('/api/token/test');$('#tok_msg').textContent=(d.ok?'Connected - ':'Failed - ')+d.detail+' ('+d.ms+' ms)';}
  catch(e){$('#tok_msg').textContent=e.message;}};

/* ---------- controls ---------- */
$('#b_start').onclick=async()=>{try{await post('/api/start');}catch(e){alert(e.message);}poll();};
$('#b_stop').onclick=async()=>{try{await post('/api/stop');}catch(e){alert(e.message);}poll();};
$('#btn_kill').onclick=async()=>{
  if(!confirm('Kill switch: stop the bot and halt for the rest of the day?\n\nIt stays on after a restart and blocks the automatic start. You will have to press "Re-arm after halt", then Start, to trade again.'))return;
  try{await post('/api/kill');}catch(e){alert(e.message);}poll();};
$('#btn_rearm').onclick=async()=>{try{await post('/api/rearm');}catch(e){alert(e.message);}poll();};
$('#btn_flat').onclick=async()=>{
  if(!confirm('Close the open position now at the current bid?\n(This also halts the bot for the day.)'))return;
  try{await post('/api/flatten');}catch(e){alert(e.message);}poll();};

showTab(store.get('scalp_tab')||'dash');
poll();setInterval(poll,2000);
loadEvents();setInterval(loadEvents,5000);
setInterval(()=>{if(TAB==='report')loadReport();},20000);
</script></body></html>
"""


LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sign in - NIFTY Scalper</title>
<style>
:root{--bg:#0d0f14;--panel:#131720;--border:#1e2330;--border2:#2a3145;
      --text:#c8ccd4;--muted:#64748b;--accent:#38bdf8;--red:#ef4444}
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:var(--bg);color:var(--text);
  font-family:'Consolas','Courier New',monospace;font-size:13px}
.wrap{min-height:100%;display:flex;align-items:center;justify-content:center;padding:24px}
.box{width:100%;max-width:340px;background:var(--panel);border:1px solid var(--border);
  border-radius:8px;padding:26px 22px}
h1{margin:0 0 4px;font-size:15px;color:#e2e8f0;letter-spacing:.05em}
.sub{color:var(--muted);font-size:11px;margin-bottom:18px}
label{display:block;font-size:10px;color:var(--muted);letter-spacing:.08em;margin-bottom:6px}
input{width:100%;background:#0d0f14;border:1px solid var(--border2);color:var(--text);
  padding:11px 10px;border-radius:4px;font-family:inherit;font-size:14px}
input:focus{outline:none;border-color:var(--accent)}
button{width:100%;margin-top:14px;background:#0e3d6b;border:1px solid var(--accent);
  color:#7dd3fc;padding:11px;border-radius:4px;font-family:inherit;font-size:13px;cursor:pointer}
.err{margin-top:12px;color:var(--red);font-size:11px;text-align:center}
</style></head><body>
<div class="wrap"><form class="box" method="POST" autocomplete="off">
  <h1>NIFTY SCALPER</h1>
  <div class="sub">IVX-G &mdash; sign in to continue</div>
  <label>PASSWORD</label>
  <input type="password" name="password" autofocus {% if locked %}disabled{% endif %}>
  <button type="submit" {% if locked %}disabled{% endif %}>SIGN IN</button>
  {% if error %}<div class="err">{{ error }}</div>{% endif %}
</form></div></body></html>"""


# ─────────────────────────────────────────────────────────────────────────────
#  PROCESS MODEL
# ─────────────────────────────────────────────────────────────────────────────
_bg_lock = threading.Lock()
_bg_started = False
_lock_handle = None


def _acquire_lock():
    """Only one process may run the scalper loop. A second copy serves the UI
    read-only rather than opening a parallel set of trades."""
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
    if not _acquire_lock():
        STATE.owner = False
        STATE.status = "Read-only: another copy owns the scalper."
        log_event("boot", "scalper lock held elsewhere; pid %d serves the UI only" % os.getpid())
        return False
    STATE.owner = True
    # Launched = trading.  A launch-time decision only: the saved "running"
    # flag is still never restored.  The loop starts it once the token works
    # and the kill switch is off (autostart_step); Stop or Kill cancel it.
    STATE.autostart = True
    threading.Thread(target=boot_loop, name="boot", daemon=True).start()
    threading.Thread(target=scalper_loop, name="scalper", daemon=True).start()
    log_event("boot", "scalper up (pid %d, DATA_DIR=%s, auth=%s)"
              % (os.getpid(), DATA_DIR, "on" if AUTH_ON else "off"))
    return True


def _graceful(*_a):
    if _SHUTDOWN.is_set():
        return
    _SHUTDOWN.set()
    try:
        with STATE.lock:
            STATE.running = False
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
        open_ = list(STATE.open_trades)
        lots = int(_f(STATE.cfg.get("lots"), 1)) or 1
    used = sum(_f(t.get("entry_fill")) * _f(t.get("quantity")) for t in open_)
    nxt = []
    try:
        snap = (BUF.tail(1) or [None])[0]
        if snap:
            atm = min(snap["chain"], key=lambda k: abs(k - snap["spot"]))
            for side in ("ce", "pe"):
                q = quote_at(snap, atm, side)
                if q and (q["ask"] or q["ltp"]) > 0:
                    nxt.append((q["ask"] or q["ltp"]) * nifty_lot() * lots)
    except Exception:
        pass
    return {"margin_used": round(used), "open": len(open_),
            "margin_next": round(min(nxt)) if nxt else None,
            "margin_next_max": round(max(nxt)) if nxt else None,
            "basis": "option buying: ATM premium x quantity, paid in full"}


def _pnl_summary(margin_used):
    with STATE.lock:
        hist = list(STATE.history)
        today_rows = list(STATE.trades)
        open_pnl = sum((_f(t.get("mark")) - _f(t.get("entry_fill"))) * _f(t.get("quantity"))
                       for t in STATE.open_trades if _f(t.get("mark")) > 0)
    cap = lambda r: _f(r.get("entry_fill")) * _f(r.get("quantity"))
    return _pnl_pack(today_rows, hist, lambda r: _f(r.get("net_pnl")), cap, open_pnl, margin_used)


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


# ─────────────────────────────────────────────────────────────────────────────
#  VIX RULES  (optional for this strategy - tick it in NIFTY Trader's
#  "VIX rules" dialog).  Two opposite rules, and a strategy can be in at most
#  one of them:
#    KILL ABOVE        while India VIX is ABOVE the level: no new trades, and
#                      every open position is closed (market hours).  Trading
#                      resumes by itself once VIX is back at or below it.
#    TRADE ONLY ABOVE  while India VIX is BELOW the level: no new trades.
#                      Open positions are left alone - this rule only decides
#                      whether a new trade may be taken.
#  Both levels and both tick lists live in hub/risk.json, re-read every check.
#  If VIX cannot be read, nothing changes.
# ─────────────────────────────────────────────────────────────────────────────
_KILL_DEFAULT_ON = ("credit_spreads", "ema_hedge")
_KILL_RISK_FILE = _env("NIFTY_RISK_FILE") if "_env" in globals() else os.environ.get("NIFTY_RISK_FILE")
_KILL_RISK_FILE = _KILL_RISK_FILE or os.path.join(os.path.dirname(os.path.dirname(APP_DIR)), "hub", "risk.json")
KILL = {"value": None, "kill": False, "hold": False, "checked": 0.0, "note": "not checked yet"}


def _risk_level(d, key):
    try:
        v = float(d.get(key, 13.5))
    except (TypeError, ValueError):
        return 13.5
    return v if v == v and v >= 0 else 13.5


def vix_kill_settings():
    """(kill-above level, trade-only-above level) for THIS strategy.  Either
    is 0 when that rule is not ticked here, so the caller needs no flags."""
    sid = os.path.basename(APP_DIR)
    try:
        with open(_KILL_RISK_FILE, encoding="utf-8") as f:
            d = json.load(f)
        apply, apply_min = d.get("apply") or {}, d.get("apply_min") or {}
        # NIFTY Trader never saves both rules for one strategy, but an older
        # file or one edited by hand can hold both, so settle it the way the
        # hub does (vix_rules_for): a tick someone actually wrote beats the
        # default, and if both were written the kill switch wins - it is the
        # rule that protects open positions, not the one that only waits.
        stated = apply.get(sid) if sid in apply else None
        floor_on = bool(apply_min.get(sid))
        kill_on = (bool(stated) if stated is not None
                   else (sid in _KILL_DEFAULT_ON and not floor_on))
        return (_risk_level(d, "vix_limit") if kill_on else 0.0,
                _risk_level(d, "vix_min") if (floor_on and not kill_on) else 0.0)
    except (OSError, ValueError, TypeError, AttributeError):
        return (13.5 if sid in _KILL_DEFAULT_ON else 0.0), 0.0


def kill_blocks():
    """True while either VIX rule says this strategy may not open anything."""
    return bool(KILL["kill"] or KILL["hold"])


def _kill_note(v, lim, floor):
    bits = []
    if lim > 0:
        bits.append("kill above %.2f" % lim)
    if floor > 0:
        bits.append("trade only above %.2f" % floor)
    return "India VIX %.2f, %s" % (v, " and ".join(bits))


def kill_step(market_open, close_all):
    lim, floor = vix_kill_settings()
    if lim <= 0 and floor <= 0:
        KILL.update(kill=False, hold=False, note="No VIX rule applies to this strategy")
        return
    if time.time() - KILL["checked"] < (60 if market_open else 900):
        return
    KILL["checked"] = time.time()
    res = call_dhan("marketfeed/ltp", {"IDX_I": [21]}, timeout=10)
    node = (((res.get("data") or {}).get("IDX_I") or {}).get("21") or {}) if res.get("status") == "success" else {}
    v = _f(node.get("last_price") if isinstance(node, dict) else None)
    if v <= 0:
        KILL["note"] = "India VIX unavailable - VIX rules unchanged"
        return
    kill = lim > 0 and v > lim
    hold = floor > 0 and v < floor
    if kill != KILL["kill"]:
        log_event("vix", ("India VIX %.2f crossed ABOVE the %.2f limit - KILL SWITCH ON: no new trades, "
                          "closing every open position" if kill else
                          "India VIX %.2f is back at or below the %.2f limit - new trades allowed again") % (v, lim))
    if hold != KILL["hold"]:
        log_event("vix", ("India VIX %.2f is BELOW %.2f - no new trades until it is above it; open "
                          "positions are left alone" if hold else
                          "India VIX %.2f is back above %.2f - new trades allowed again") % (v, floor))
    KILL.update(value=v, kill=kill, hold=hold, note=_kill_note(v, lim, floor))
    if kill and market_open:
        close_all()


def _kill_close_all(snap=None):
    cfg = STATE.cfg
    for tr in list(STATE.open_trades):
        q = mark_trade(tr, snap, cfg) if snap else None
        close_trade(tr, q["bid"] if q else _f(tr.get("mark"), tr["entry_fill"]), "VIX_KILL", cfg)


if __name__ == "__main__":
    port = int(_f(_env("SCALP_PORT", "5001"), 5001))
    host = _env("HOST") or ("0.0.0.0" if _env("APP_ENV") == "hosted" else "127.0.0.1")
    print("\n  NIFTY scalper (IVX-G)  ->  http://%s:%d" % (host, port))
    print("  PAPER TRADING. Breakeven win rate for 3000/1000 after costs is ~29%.")
    print("  Read the Expectancy tab before you trust a good day.\n", flush=True)
    app.run(host=host, port=port, debug=False, threaded=True, use_reloader=False)
