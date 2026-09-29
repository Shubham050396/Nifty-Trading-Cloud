"""
NIFTY 100 EMA Breakout - hedged option spreads  (ported from the TradingView strategy)
======================================================================================

The Pine script traded one future (GOLDM1!) on its own chart.  This app runs the
SAME signal on the NIFTY 50 index and trades it with NIFTY options instead.
Every position is hedged: one option is sold and one is bought, so the most a
position can lose is known the moment it opens.

SIGNAL  -  NIFTY index candles, the Pine rules unchanged

    long    the last 25 closes were ALL below the 100 EMA, and this bar
            closes back above it (a crossover)
    short   the last 25 closes were ALL above the 100 EMA, and this bar
            closes back below it
    exit    whichever comes first, on a bar close:
              * the close crosses the 40 EMA against you  (below it for a long)
              * the close is 10% against the entry close  (stop)
              * the close is 100% in your favour          (target)
    One position at a time, and a new signal only when flat - as in Pine.
    Candles come from Dhan's intraday chart API, so the EMAs are warmed up on
    days of history and match the TradingView chart from the first minute.

TRADE  -  NIFTY options at the ATM strike, in the current 4 expiries

    For every expiry you tick (the 1st to 4th listed - they roll forward on
    their own as expiries pass) the signal opens one two-leg spread:

        credit (default)   long  -> SELL the ATM PE, BUY a PE N strikes lower
                           short -> SELL the ATM CE, BUY a CE N strikes higher
        debit              long  -> BUY the ATM CE, SELL a CE N strikes higher
                           short -> BUY the ATM PE, SELL a PE N strikes lower

    Every spread closes when the index signal exits.  On an expiry's last day
    its spread is closed at a set time instead of being left to settle, and
    (Roll, on by default) re-opened in the next expiry while the signal holds.
    Two optional rules act on a spread by itself: take profit at X% of its
    maximum profit, stop at Y% of its maximum loss (both off by default).

PAPER TRADING ONLY.  Nothing is sent to the broker.  Prices come from the Dhan
option chain: a leg you sell fills at the bid, a leg you buy at the ask, and an
open spread is valued at what closing it would cost right now.

The Pine script's secret key and webhook JSON are gone: this app talks to Dhan
directly with the access token NIFTY Trader injects.
"""

import base64
import csv
import io
import json
import math
import os
import re
import tempfile
import threading
import time
from collections import deque
from datetime import datetime, timedelta, time as dtime, timezone

import requests
from flask import Flask, Response, jsonify, request

APP_DIR = os.path.dirname(os.path.abspath(__file__))


def _env(name, default=None):
    v = os.environ.get(name)
    return v.strip() if isinstance(v, str) and v.strip() else default


DATA_DIR = _env("DATA_DIR") or os.path.join(APP_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
STATE_FILE = os.path.join(DATA_DIR, "ema_hedge_state.json")
RUNTIME_FILE = os.path.join(DATA_DIR, "runtime.json")
SCRIP_CACHE = os.path.join(DATA_DIR, "scrip_nifty.json")
# Append-only, never trimmed: every closed spread and every event, forever.
TRADES_FILE = os.path.join(DATA_DIR, "trades.jsonl")
TRADES_REMOVED_FILE = os.path.join(DATA_DIR, "trades_removed.jsonl")   # what Clear/Wipe took out
EVENTS_FILE = os.path.join(DATA_DIR, "events.jsonl")
EVENTS_MAX_BYTES = 20 * 1024 * 1024        # then rolled to events.<n>.jsonl - every archive kept

IST = timezone(timedelta(hours=5, minutes=30))
MKT_OPEN, MKT_CLOSE = dtime(9, 15), dtime(15, 30)
UNDERLYING_SCRIP, UNDERLYING_SEG = 13, "IDX_I"


def now_ist():
    return datetime.now(IST)


def _ist(t):
    return datetime.fromtimestamp(t, IST)


def ts():
    return now_ist().strftime("%Y-%m-%d %H:%M:%S")


def _f(x, d=0.0):
    try:
        v = float(x)
        return d if v != v or v in (float("inf"), float("-inf")) else v
    except (TypeError, ValueError):
        return d


def _r2(x):
    return None if x is None else round(x, 2)


# ─────────────────────────────────────────────────────────────────────────────
#  EVENT LOG
# ─────────────────────────────────────────────────────────────────────────────
_events = deque(maxlen=2000)             # recent events, for the live views
_events_lock = threading.Lock()
_JWT_RE = re.compile(r"eyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]+")


def _reverse_lines(path):
    """Lines of a file, last first, without reading it all into memory."""
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            pos, tail = f.tell(), b""
            while pos > 0:
                step = min(65536, pos)
                pos -= step
                f.seek(pos)
                chunk = f.read(step) + tail
                lines = chunk.split(b"\n")
                tail = lines.pop(0)
                for line in reversed(lines):
                    if line.strip():
                        yield line
            if tail.strip():
                yield tail
    except OSError:
        return


def _event_archives():
    """events.1.jsonl, events.2.jsonl, ... newest (highest number) first."""
    found = []
    try:
        for name in os.listdir(DATA_DIR):
            m = re.fullmatch(r"events\.(\d+)\.jsonl", name)
            if m:
                found.append((int(m.group(1)), os.path.join(DATA_DIR, name)))
    except OSError:
        pass
    return [path for _, path in sorted(found, reverse=True)]


def _event_files():
    return [EVENTS_FILE] + _event_archives()


def _last_event_id():
    """Event ids keep counting across restarts, so paging back through history
    never mixes two runs up."""
    for path in _event_files():
        for raw in _reverse_lines(path):
            try:
                return int(json.loads(raw.decode("utf-8", "replace"))["id"])
            except (ValueError, KeyError, TypeError):
                continue
    return 0


_seq = [_last_event_id()]


def log_event(kind, msg):
    """Kept in memory for the live views AND appended to events.jsonl, so the
    Activity tab can show everything that ever happened, across restarts.
    A token never reaches either: it is scrubbed first."""
    txt = _JWT_RE.sub("<token-redacted>", str(msg))
    now = now_ist()
    with _events_lock:
        _seq[0] += 1
        ev = {"id": _seq[0], "ts": now.strftime("%Y-%m-%d %H:%M:%S"),
              "at": now.strftime("%H:%M:%S"), "kind": kind, "msg": txt}
        _events.appendleft(ev)
        # The roll and the append are separate on purpose: on Windows the
        # rename fails while any reader has the file open, and that must only
        # postpone the roll - never lose the event.
        try:
            if os.path.exists(EVENTS_FILE) and os.path.getsize(EVENTS_FILE) > EVENTS_MAX_BYTES:
                nums = [int(re.search(r"(\d+)\.jsonl$", a).group(1)) for a in _event_archives()]
                os.replace(EVENTS_FILE, os.path.join(DATA_DIR, "events.%d.jsonl" % (max(nums, default=0) + 1)))
        except OSError:
            pass                       # retried on a later event
        try:
            with open(EVENTS_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")
        except OSError:
            pass                       # the live view still has it; never crash on logging
    print("[%s] %-9s %s" % (ev["at"], kind.upper(), txt), flush=True)


def recent_events(limit=200):
    with _events_lock:
        return list(_events)[:limit]


def read_events(before=None, limit=200, kind=None):
    """Events newest first, from disk.  before=<id> pages back through history."""
    out = []
    for path in _event_files():
        for raw in _reverse_lines(path):
            try:
                ev = json.loads(raw.decode("utf-8", "replace"))
            except ValueError:
                continue
            if before is not None and int(ev.get("id") or 0) >= before:
                continue
            if kind and ev.get("kind") != kind:
                continue
            out.append(ev)
            if len(out) >= limit:
                return out
    return out


# ─────────────────────────────────────────────────────────────────────────────
#  DURABLE JSON
# ─────────────────────────────────────────────────────────────────────────────
def write_json_atomic(path, obj, backups=3):
    payload = json.dumps(obj, indent=2, default=str).encode("utf-8")
    if backups and os.path.exists(path):
        try:
            for i in range(backups, 1, -1):
                older = "%s.bak.%d" % (path, i - 1)
                if os.path.exists(older):
                    os.replace(older, "%s.bak.%d" % (path, i))
            with open(path, "rb") as src, open(path + ".bak.1", "wb") as dst:
                dst.write(src.read())
        except OSError:
            pass
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path) or ".", prefix=".tmp_", suffix=".json")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(payload)
            f.flush()
            os.fsync(f.fileno())
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
        except (OSError, ValueError):
            continue
    return default


def runtime_read():
    return read_json_safe(RUNTIME_FILE, default={}) or {}


def runtime_write(**kw):
    d = runtime_read()
    d.update(kw)
    write_json_atomic(RUNTIME_FILE, d, backups=1)
    return d


# ─────────────────────────────────────────────────────────────────────────────
#  CREDENTIALS  -  the hub injects these; the form below is the fallback
# ─────────────────────────────────────────────────────────────────────────────
class Creds:
    def __init__(self, client_id, token, source, pinned):
        self.client_id, self.token, self.source, self.pinned = client_id, token, source, pinned


def resolve_credentials():
    rt = runtime_read()
    token, source, pinned = _env("DHAN_ACCESS_TOKEN"), "environment", True
    if not token:
        pinned = False
        token, source = (rt.get("access_token") or "").strip(), "settings tab"
    if not token:
        source = "not configured"
    cid = _env("DHAN_CLIENT_ID") or (rt.get("client_id") or "").strip() or ""
    if not cid and token:
        cid = str((decode_jwt(token) or {}).get("dhanClientId") or "")
    return Creds(str(cid), token or "", source, pinned)


def decode_jwt(token):
    try:
        p = token.split(".")[1]
        p += "=" * (-len(p) % 4)
        return json.loads(base64.urlsafe_b64decode(p).decode("utf-8", "replace"))
    except Exception:
        return None


def token_status():
    c = resolve_credentials()
    if not c.token:
        return {"configured": False, "expired": False, "human": "not configured",
                "source": c.source, "client_id": c.client_id, "pinned": c.pinned}
    claims = decode_jwt(c.token) or {}
    exp = claims.get("exp")
    left = (int(exp) - time.time()) if exp else None
    expired = bool(left is not None and left <= 0)
    if left is None:
        human = "unreadable (not a JWT)"
    elif expired:
        human = "EXPIRED"
    else:
        human = "expires in %dh %dm" % (left // 3600, (left % 3600) // 60)
    return {"configured": True, "expired": expired, "human": human, "source": c.source,
            "client_id": c.client_id, "pinned": c.pinned,
            "masked": (c.token[:8] + "..." + c.token[-6:]) if len(c.token) > 16 else "*" * len(c.token)}


# ─────────────────────────────────────────────────────────────────────────────
#  DHAN API
# ─────────────────────────────────────────────────────────────────────────────
DHAN_BASE = "https://api.dhan.co/v2"
_HTTP = requests.Session()
_HTTP.headers.update({"Accept": "application/json"})
_api_gate = threading.Lock()
_api_last = [0.0]
_api_backoff = [0.0]            # extra seconds added after a 429, decays on success
MIN_API_INTERVAL = 3.1          # Dhan throttles the option chain to 1 call / 3s
AUTH_PAUSE = 60                 # after a 401/403, stop calling for this long
_auth_block = [0.0]


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
        first = time.time() >= _auth_block[0]
        _auth_block[0] = time.time() + AUTH_PAUSE
        if first:
            log_event("token", "%s -> HTTP %d: the broker rejected the token. Pausing %ds - "
                               "paste a fresh token in NIFTY Trader's Broker token screen."
                      % (endpoint, r.status_code, AUTH_PAUSE))
        return {"status": "error", "_http": r.status_code, "message": "Auth failed."}
    try:
        d = r.json()
    except ValueError:
        return {"status": "error", "_http": r.status_code, "message": "non-JSON reply"}
    if not isinstance(d, dict):
        return {"status": "error", "_http": r.status_code, "message": "bad payload"}
    if r.status_code >= 400:
        d.setdefault("status", "error")
        d["message"] = d.get("errorMessage") or d.get("message") or "HTTP %d" % r.status_code
    d["_http"] = r.status_code
    return d


def throttled_chain(expiry):
    """One option-chain call at a time, at most one per MIN_API_INTERVAL.

    Dhan's limit is per CLIENT - the other strategies in NIFTY Trader draw on
    the same allowance.  So a 429 widens the gap instead of retrying hard, and
    the gap shrinks back as calls succeed again."""
    with _api_gate:
        wait = MIN_API_INTERVAL + _api_backoff[0] - (time.time() - _api_last[0])
        if wait > 0:
            time.sleep(wait)
        res = call_dhan("optionchain", {"UnderlyingScrip": UNDERLYING_SCRIP,
                                        "UnderlyingSeg": UNDERLYING_SEG, "Expiry": expiry})
        _api_last[0] = time.time()
        if res.get("_http") == 429:
            _api_backoff[0] = min(12.0, max(2.0, _api_backoff[0] * 2))
            log_event("api", "rate limited by Dhan - now one call every %.1f s"
                      % (MIN_API_INTERVAL + _api_backoff[0]))
        elif res.get("status") == "success" and _api_backoff[0]:
            _api_backoff[0] = max(0.0, _api_backoff[0] - 0.5)
    return res


def fetch_expiry_list():
    r = call_dhan("optionchain/expirylist",
                  {"UnderlyingScrip": UNDERLYING_SCRIP, "UnderlyingSeg": UNDERLYING_SEG})
    return sorted({str(x)[:10] for x in (r.get("data") or [])}) if r.get("status") == "success" else []


# ─────────────────────────────────────────────────────────────────────────────
#  SCRIP MASTER  -  for the lot size
# ─────────────────────────────────────────────────────────────────────────────
SCRIP_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"


def load_scrip_lookup():
    today = now_ist().strftime("%Y-%m-%d")
    cached = read_json_safe(SCRIP_CACHE, default=None)
    if isinstance(cached, dict) and cached.get("date") == today and cached.get("map"):
        return cached["map"]
    try:
        r = requests.get(SCRIP_URL, timeout=180)
        r.raise_for_status()
        out = {}
        for row in csv.DictReader(io.StringIO(r.content.decode("utf-8", "replace"))):
            if row.get("SEM_EXM_EXCH_ID") != "NSE" or row.get("SEM_OPTION_TYPE") not in ("CE", "PE"):
                continue
            if not (row.get("SEM_CUSTOM_SYMBOL") or "").upper().startswith("NIFTY "):
                continue
            try:
                strike = float(row["SEM_STRIKE_PRICE"])
                expiry = str(row["SEM_EXPIRY_DATE"])[:10]
            except (KeyError, TypeError, ValueError):
                continue
            side = "CALL" if row["SEM_OPTION_TYPE"] == "CE" else "PUT"
            out["%s_%.1f_%s" % (expiry, strike, side)] = {
                "sid": row.get("SEM_SMST_SECURITY_ID"),
                "lot": int(_f(row.get("SEM_LOT_UNITS"), 65))}
        if out:
            write_json_atomic(SCRIP_CACHE, {"date": today, "map": out}, backups=1)
        return out
    except Exception as e:
        log_event("error", "scrip master: %s" % e)
        return (cached or {}).get("map", {}) if isinstance(cached, dict) else {}


def contract_meta(expiry, strike, opt_type):
    key = "%s_%.1f_%s" % (str(expiry)[:10], float(strike),
                          "CALL" if str(opt_type).upper() in ("CE", "CALL") else "PUT")
    return STATE.scrip_lookup.get(key)


def lot_size():
    for v in STATE.scrip_lookup.values():
        return int(v.get("lot") or 65)
    return 65


def lot_for(expiry, strike, opt_type):
    """The lot of THIS contract.  NSE changes lot sizes between series, so one
    expiry's lot is not another's."""
    meta = contract_meta(expiry, strike, opt_type)
    if meta and meta.get("lot"):
        return int(meta["lot"])
    return lot_size()


# ─────────────────────────────────────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────────────────────────────────────
MAX_SLOTS = 4                   # "the current 4 expiries"
INTERVALS = (1, 5, 15, 25, 60)  # candle lengths (minutes) Dhan's intraday chart API serves
SIGNAL_KEYS = ("interval", "ema_entry", "ema_stop", "lookback")   # change these = a new signal series

DEFAULTS = {
    # ---- the Pine inputs ----
    "interval": 5,                     # the chart timeframe the script runs on
    "ema_entry": 100, "ema_stop": 40, "lookback": 25,
    "stop_pct": 10.0, "target_pct": 100.0,
    # ---- the option trade ----
    "slots": [1, 2, 3, 4],             # which of the current 4 expiries (1 = nearest)
    "spread": "credit",                # credit: SELL ATM + BUY hedge.  debit: BUY ATM + SELL further out
    "strike_step": 50,                 # NIFTY lists strikes every 50
    "hedge_strikes": 4,                # the second leg sits this many strikes away from ATM
    "lots": 1,
    "expiry_exit": "15:15",            # a spread's last day: closed at this time, never left to settle
    "roll": True,                      # ...and re-opened in the next expiry while the signal holds
    "spread_tp_pct": 0.0,              # close a spread at this % of its max profit (0 = off)
    "spread_sl_pct": 0.0,              # close a spread at this % of its max loss (0 = off)
}

# Checked on Save: the value must be a real number inside this range.
RANGES = {
    "ema_entry": (2, 500), "ema_stop": (2, 500), "lookback": (1, 200),
    "stop_pct": (0.1, 100), "target_pct": (0.1, 1000),
    "hedge_strikes": (1, 20), "lots": (1, 50),
    "spread_tp_pct": (0, 100), "spread_sl_pct": (0, 100),
}
LABELS = {
    "interval": "Candle length", "ema_entry": "Entry EMA", "ema_stop": "Stop-loss EMA",
    "lookback": "Lookback", "stop_pct": "Stop loss %", "target_pct": "Take profit %",
    "hedge_strikes": "Hedge distance", "lots": "Lots per spread",
    "spread_tp_pct": "Spread take profit", "spread_sl_pct": "Spread stop",
    "expiry_exit": "Expiry-day exit time",
}


def _hhmm(v):
    """'HH:MM' inside market hours, or None."""
    m = re.fullmatch(r"(\d{1,2}):(\d{2})", str(v or "").strip())
    if not m:
        return None
    h, mi = int(m.group(1)), int(m.group(2))
    if h > 23 or mi > 59 or not (MKT_OPEN <= dtime(h, mi) <= MKT_CLOSE):
        return None
    return "%02d:%02d" % (h, mi)


def clean_cfg(d):
    c = dict(DEFAULTS)
    c.update({k: v for k, v in (d or {}).items() if k in DEFAULTS})
    iv = int(_f(c["interval"], 5))
    c["interval"] = iv if iv in INTERVALS else DEFAULTS["interval"]
    for k in ("ema_entry", "ema_stop", "lookback", "hedge_strikes", "lots"):
        lo, hi = RANGES[k]
        c[k] = int(max(lo, min(hi, int(_f(c[k], DEFAULTS[k])))))
    for k in ("stop_pct", "target_pct", "spread_tp_pct", "spread_sl_pct"):
        lo, hi = RANGES[k]
        c[k] = max(lo, min(hi, _f(c[k], DEFAULTS[k])))
    raw = c["slots"] if isinstance(c["slots"], (list, tuple)) else [c["slots"]]
    c["slots"] = sorted({int(_f(s)) for s in raw if 1 <= int(_f(s)) <= MAX_SLOTS})
    c["spread"] = "debit" if c["spread"] == "debit" else "credit"
    c["strike_step"] = 100 if int(_f(c["strike_step"], 50)) == 100 else 50
    c["expiry_exit"] = _hhmm(c["expiry_exit"]) or DEFAULTS["expiry_exit"]
    c["roll"] = c["roll"] is True
    return c


def check_body(body):
    """Numbers must be numbers, inside a sane range - never silently 0."""
    for k, (lo, hi) in RANGES.items():
        if k not in body:
            continue
        try:
            fv = float(body[k])
        except (TypeError, ValueError):
            return "%s must be a number." % LABELS.get(k, k)
        if fv != fv or not (lo <= fv <= hi):
            return "%s must be between %g and %g." % (LABELS.get(k, k), lo, hi)
    if "interval" in body and int(_f(body["interval"], -1)) not in INTERVALS:
        return "Candle length must be one of %s minutes." % ", ".join(str(i) for i in INTERVALS)
    if "expiry_exit" in body and not _hhmm(body["expiry_exit"]):
        return "Expiry-day exit time must be HH:MM between 09:15 and 15:30."
    if "strike_step" in body and int(_f(body["strike_step"], -1)) not in (50, 100):
        return "Strike step must be 50 or 100."
    return None


def validate_cfg(cfg):
    """Errors a user can fix, in words.  None when all is well."""
    if not cfg["slots"]:
        return "Tick at least one of the current 4 expiries."
    return None


# ─────────────────────────────────────────────────────────────────────────────
#  STATE
# ─────────────────────────────────────────────────────────────────────────────
SIGNALS_KEEP = 200              # recent signals, for the chart markers and the Signals table
BARS_KEEP = 3000                # closed candles kept in memory (1-minute candles run long)


def flat_sig():
    return {"side": None}


class Book:
    def __init__(self):
        self.lock = threading.RLock()
        self.cfg = clean_cfg({})
        self.running = False
        # Launching the strategy from NIFTY Trader starts it; Stop cancels this.
        self.autostart = False
        self.scrip_lookup = {}
        self.expiry_list = []
        self.expiry_fetched = 0.0
        # ---- the index signal, exactly Pine's position state ----
        self.sig = flat_sig()
        self.last_bar_t = 0            # the newest candle already run through the rules
        self.bars, self.ema_e, self.ema_s = [], [], []
        self.ind = {}
        self.signals = []              # recent entries and exits, oldest first
        self.candles_loaded = False
        self.candle_try_at = 0.0       # no candle call before this time
        self.candle_backoff = 0.0
        self.candle_note = "not loaded yet"
        # ---- the options ----
        self.positions = []            # open spreads, one per expiry
        self.pending = None            # spreads a fresh signal (or a roll) still has to open
        self.snaps = {}                # expiry -> the last option-chain snapshot
        self.chain_note = {}           # expiry -> why its chain is unavailable
        self.chain_tried = {}          # expiry -> when its chain was last asked for (worked or not)
        self.preview_at = 0.0
        self.spot = None
        self.history = []              # every closed spread, oldest first (mirrors trades.jsonl)
        # Closed spreads not yet safely in trades.jsonl.  Saved in the state
        # file too, so a failed write (disk full, file locked) never loses one.
        self.unflushed = []
        self.status = "idle"
        self.market_note = ""
        self.day = now_ist().strftime("%Y-%m-%d")
        self.last_save = 0.0

    # ---- persistence ----
    def snapshot(self):
        return {"schema": 1, "saved_at": ts(), "cfg": self.cfg,
                "sig": self.sig, "last_bar_t": self.last_bar_t,
                "signals": self.signals[-SIGNALS_KEEP:],
                "positions": self.positions, "pending": self.pending,
                "unflushed_trades": self.unflushed, "day": self.day}

    def save(self):
        # Under the lock: the engine thread and a web request can both save,
        # and the snapshot must not be taken while the other is mid-change.
        with self.lock:
            try:
                write_json_atomic(STATE_FILE, self.snapshot())
                self.last_save = time.time()
            except (OSError, TypeError, ValueError) as e:
                log_event("error", "save failed: %s" % e)

    def load(self):
        d = read_json_safe(STATE_FILE, default=None)
        if isinstance(d, dict):
            self.cfg = clean_cfg(d.get("cfg"))
            self.day = d.get("day") or self.day
            sig = d.get("sig")
            self.sig = sig if isinstance(sig, dict) and sig.get("side") in ("LONG", "SHORT") else flat_sig()
            self.last_bar_t = int(_f(d.get("last_bar_t")))
            self.signals = [s for s in (d.get("signals") or []) if isinstance(s, dict)][-SIGNALS_KEEP:]
            self.positions = [p for p in (d.get("positions") or [])
                              if isinstance(p, dict) and p.get("legs") and p.get("expiry")]
            self.pending = d.get("pending") if isinstance(d.get("pending"), dict) else None
            self.unflushed = [r for r in (d.get("unflushed_trades") or []) if isinstance(r, dict)]
        on_disk = load_trades()
        if self.unflushed:
            # A pending trade may already be in trades.jsonl: the flush can
            # succeed after the state file was last saved.  Match on the trade
            # id so a restart never books the same trade twice.
            have = {r.get("id") for r in on_disk}
            self.unflushed = [r for r in self.unflushed if r.get("id") not in have]
            try:
                append_trades(self.unflushed)
                on_disk += self.unflushed
                self.unflushed = []
            except OSError:
                pass                   # still pending; retried every engine pass
        self.history = on_disk + list(self.unflushed)
        # `running` is not restored from the file: whether it starts is decided
        # at launch (see STATE.autostart), not by what it was doing last time.
        self.running = False


# ---- the trade book on disk ----
def load_trades():
    out = []
    try:
        with open(TRADES_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        out.append(json.loads(line))
                    except ValueError:
                        continue
    except OSError:
        pass
    return out


def write_trades(rows, path=None):
    """Rewrite a whole .jsonl atomically (Clear / Wipe)."""
    path = path or TRADES_FILE
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path) or ".", prefix=".tmp_", suffix=".jsonl")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False, default=str) + "\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
        tmp = None
    finally:
        if tmp and os.path.exists(tmp):
            try:
                os.unlink(tmp)
            except OSError:
                pass


def append_trades(recs, path=None):
    """Append many rows with ONE open and ONE fsync."""
    if not recs:
        return
    with open(path or TRADES_FILE, "a", encoding="utf-8") as f:
        for rec in recs:
            f.write(json.dumps(rec, ensure_ascii=False, default=str) + "\n")
        f.flush()
        os.fsync(f.fileno())


# Serialises every write to the trade book files.  Lock order is ALWAYS
# _book_lock first, then STATE.lock - never the other way round.
_book_lock = threading.Lock()
_flush_warned = [False]


def flush_unflushed():
    """Move pending closed spreads into trades.jsonl.  Never called while
    holding STATE.lock (see the lock order above)."""
    with _book_lock:
        with STATE.lock:
            pending = list(STATE.unflushed)
        if not pending:
            return True
        try:
            append_trades(pending)
        except OSError as e:
            if not _flush_warned[0]:
                _flush_warned[0] = True
                log_event("error", "could not write %d closed spread(s) to trades.jsonl (%s) - "
                                   "kept safely in the state file and retried every pass" % (len(pending), e))
            return False
        _flush_warned[0] = False
        with STATE.lock:
            STATE.unflushed = [r for r in STATE.unflushed if not any(r is x for x in pending)]
        return True


STATE = Book()
_SHUTDOWN = threading.Event()


# ─────────────────────────────────────────────────────────────────────────────
#  MARKET HOURS AND CANDLE SLOTS
# ─────────────────────────────────────────────────────────────────────────────
def market_state(now=None):
    now = now or now_ist()
    if now.weekday() >= 5:
        return "CLOSED", "weekend"
    t = now.time()
    if t < MKT_OPEN:
        return "PRE", "pre-open, starts 09:15 IST"
    if t > MKT_CLOSE:
        return "CLOSED", "after close"
    return "OPEN", "session live"


def _session_ts(t, hhmm):
    d = _ist(t)
    return int(datetime(d.year, d.month, d.day, hhmm.hour, hhmm.minute, tzinfo=IST).timestamp())


def in_session(t):
    return _session_ts(t, MKT_OPEN) <= t < _session_ts(t, MKT_CLOSE)


def bar_end(t, span_min):
    """When a candle closes.  The session's last candle is cut short at 15:30:
    on a 60-minute chart the 15:15 candle closes at 15:30, not 16:15."""
    return min(t + span_min * 60, _session_ts(t, MKT_CLOSE))


def last_closed_slot(now_ts, span_min):
    """Start time of TODAY's newest candle that has closed by now_ts, or None
    (a weekend, or before the first candle of the day has closed).  Candles
    are anchored to 09:15, as on TradingView and in Dhan's data."""
    if _ist(now_ts).weekday() >= 5:
        return None
    op, cl, span = _session_ts(now_ts, MKT_OPEN), _session_ts(now_ts, MKT_CLOSE), span_min * 60
    if now_ts >= cl:
        return op + ((cl - op - 1) // span) * span
    k = int((now_ts - op) // span)
    return op + (k - 1) * span if k >= 1 else None


# ─────────────────────────────────────────────────────────────────────────────
#  CANDLES  ->  EMAs  ->  THE PINE SIGNAL
# ─────────────────────────────────────────────────────────────────────────────
CANDLE_DELAY = 2.0              # ask for a candle this long after it closes
CANDLE_BACKOFF_MAX = 300.0      # a candle that is late (or a holiday) is retried at most this far apart
IST_SHIFT = 19800               # 5h30m in seconds


def history_days(cfg):
    """Calendar days of candles to load: enough for the slow EMA to settle
    (4x its length) plus the lookback, within Dhan's 90-day window."""
    per_day = math.ceil(375 / cfg["interval"])
    need = 4 * max(cfg["ema_entry"], cfg["ema_stop"]) + cfg["lookback"] + 10
    trading_days = math.ceil(need / per_day) + 1
    return max(5, min(89, math.ceil(trading_days * 7 / 5) + 6))


def parse_candles(d, span_min, now_ts):
    """Closed, in-session candles from a Dhan chart reply, oldest first.
    The candle still forming is dropped: a signal is only ever taken on a
    closed bar, as `alert.freq_once_per_bar_close` did."""
    stamps = d.get("timestamp") or []
    o_, h_, l_, c_ = (d.get(k) or [] for k in ("open", "high", "low", "close"))
    raw = []
    for i in range(min(len(stamps), len(c_))):
        t, c = int(_f(stamps[i])), _f(c_[i])
        if t <= 0 or c <= 0:
            continue
        o = _f(o_[i] if i < len(o_) else c, c) or c
        raw.append({"t": t, "o": o, "h": _f(h_[i] if i < len(h_) else c, c) or c,
                    "l": _f(l_[i] if i < len(l_) else c, c) or c, "c": c})
    # Some builds of the API stamp candles with IST wall-clock seconds rather
    # than a true epoch.  Then each day's first candle reads 14:45, not 09:15.
    firsts = {}
    for b in raw:
        day = _ist(b["t"]).date()
        firsts[day] = min(firsts.get(day, b["t"]), b["t"])
    at_open = sum(1 for t in firsts.values() if _ist(t).strftime("%H:%M") == "09:15")
    at_shift = sum(1 for t in firsts.values() if _ist(t).strftime("%H:%M") == "14:45")
    if at_shift > at_open:
        for b in raw:
            b["t"] -= IST_SHIFT
    out, seen = [], set()
    for b in sorted(raw, key=lambda b: b["t"]):
        if b["t"] in seen or not in_session(b["t"]) or bar_end(b["t"], span_min) > now_ts:
            continue
        seen.add(b["t"])
        out.append(b)
    return out


def fetch_candles(cfg, now_ts):
    now = _ist(now_ts)
    frm = now.date() - timedelta(days=history_days(cfg))
    body = {"securityId": str(UNDERLYING_SCRIP), "exchangeSegment": UNDERLYING_SEG,
            "instrument": "INDEX", "interval": str(cfg["interval"]), "oi": False,
            "fromDate": frm.strftime("%Y-%m-%d") + " 09:15:00",
            "toDate": now.strftime("%Y-%m-%d") + " 15:30:00"}
    r = call_dhan("charts/intraday", body, timeout=30)
    d = r.get("data") if isinstance(r.get("data"), dict) else r
    if not (d.get("close") and d.get("timestamp")):
        if r.get("_http") == 200 and not r.get("message"):
            return None, "the broker sent no NIFTY candles"
        return None, (r.get("message") or r.get("errorMessage") or "no candles (HTTP %s)" % r.get("_http"))
    bars = parse_candles(d, cfg["interval"], now_ts)
    return (bars, None) if bars else (None, "no closed NIFTY candles in the reply")


def ema_series(values, n):
    """Pine ta.ema: alpha = 2/(n+1), started from the average of the first n
    values; None until then.  Days of history are loaded, so by the bars that
    matter the starting value has decayed to nothing."""
    out = [None] * len(values)
    if n < 1 or len(values) < n:
        return out
    a = 2.0 / (n + 1)
    e = sum(values[:n]) / float(n)
    out[n - 1] = e
    for i in range(n, len(values)):
        e = a * values[i] + (1 - a) * e
        out[i] = e
    return out


def entry_signal(bars, ee, i, lookback):
    """Pine:  longSetup  = every one of close[1..lookback] < ema[1..lookback]
              longCondition = longSetup and ta.crossover(close, ema)
    and the mirror image for a short."""
    if i < lookback or ee[i] is None or ee[i - lookback] is None:
        return None
    c = [b["c"] for b in bars[i - lookback:i + 1]]
    e = ee[i - lookback:i + 1]
    past = range(lookback)                  # close[lookback] .. close[1]
    if all(c[k] < e[k] for k in past) and c[-1] > e[-1] and c[-2] <= e[-2]:
        return "LONG"
    if all(c[k] > e[k] for k in past) and c[-1] < e[-1] and c[-2] >= e[-2]:
        return "SHORT"
    return None


def exit_reason(sig, close, ema_stop):
    """Pine's three exits, in its order: target, % stop, then the stop EMA."""
    if sig.get("side") == "LONG":
        if close >= sig["target"]:
            return "TARGET"
        if close <= sig["stop"]:
            return "STOP"
        if ema_stop is not None and close < ema_stop:
            return "EMA_STOP"
    elif sig.get("side") == "SHORT":
        if close <= sig["target"]:
            return "TARGET"
        if close >= sig["stop"]:
            return "STOP"
        if ema_stop is not None and close > ema_stop:
            return "EMA_STOP"
    return None


def step_signal(sig, bars, ee, es, i, cfg):
    """One closed bar through the Pine script.  Returns (new sig, event|None).

    Pine fills orders at the NEXT bar's open, so on the bar a signal fires its
    position is still 0: the exits are not checked on the entry bar, and no
    entry is possible on the bar an exit fires.  The if/else keeps both."""
    b = bars[i]
    close = b["c"]
    if sig.get("side") is None:
        side = entry_signal(bars, ee, i, cfg["lookback"])
        if not side:
            return sig, None
        sl, tp = cfg["stop_pct"] / 100.0, cfg["target_pct"] / 100.0
        new = {"side": side, "id": "%s-%d" % (side[0], b["t"]), "t": b["t"],
               "at": _ist(b["t"]).strftime("%Y-%m-%d %H:%M"), "entry": close,
               "stop": round(close * (1 - sl) if side == "LONG" else close * (1 + sl), 2),
               "target": round(close * (1 + tp) if side == "LONG" else close * (1 - tp), 2),
               "stop_pct": cfg["stop_pct"], "target_pct": cfg["target_pct"]}
        return new, {"kind": side, "t": b["t"], "close": close}
    why = exit_reason(sig, close, es[i])
    if not why:
        return sig, None
    return flat_sig(), {"kind": "EXIT", "t": b["t"], "close": close, "reason": why,
                        "side": sig["side"], "sig_id": sig.get("id"), "entry": sig.get("entry")}


def indicators(bars, ee, es, lookback):
    """What the dashboard shows about the newest closed bar."""
    if not bars:
        return {}
    i = len(bars) - 1
    below = above = 0
    for k in range(i, -1, -1):
        if ee[k] is None:
            break
        if bars[k]["c"] < ee[k] and not above:
            below += 1
        elif bars[k]["c"] > ee[k] and not below:
            above += 1
        else:
            break
    armed = "LONG" if below >= lookback else ("SHORT" if above >= lookback else None)
    return {"t": bars[i]["t"], "at": _ist(bars[i]["t"]).strftime("%Y-%m-%d %H:%M"),
            "close": bars[i]["c"], "ema_e": _r2(ee[i]), "ema_s": _r2(es[i]),
            "run_below": below, "run_above": above, "armed": armed}


def fresh_window(span_min):
    """How late a signal may still be traded: the bar must have closed at most
    this long ago.  Anything older is a signal the app missed, not a trade."""
    return max(90, span_min * 60)


def process_bars(bars, now_ts):
    """Run every candle newer than the last one seen through the rules, in
    order.  Returns the events to act on, each marked fresh or not.

    A restart, an outage or a Stop leaves a gap; the bars in it are caught up
    here, so the signal state is always what TradingView shows.  Exits found
    in the gap still close spreads (holding past Pine's exit is wrong), but an
    entry is only traded when it is the newest bar and just closed."""
    cfg = STATE.cfg
    closes = [b["c"] for b in bars]
    ee, es = ema_series(closes, cfg["ema_entry"]), ema_series(closes, cfg["ema_stop"])
    events = []
    with STATE.lock:
        first_load = STATE.last_bar_t == 0
        for i, b in enumerate(bars):
            if b["t"] <= STATE.last_bar_t:
                continue
            STATE.sig, ev = step_signal(STATE.sig, bars, ee, es, i, cfg)
            STATE.last_bar_t = b["t"]
            if ev:
                ev["fresh"] = (i == len(bars) - 1
                               and now_ts - bar_end(b["t"], cfg["interval"]) <= fresh_window(cfg["interval"]))
                ev["history"] = first_load and not ev["fresh"]
                ev["at"] = _ist(b["t"]).strftime("%Y-%m-%d %H:%M")
                events.append(ev)
        STATE.bars, STATE.ema_e, STATE.ema_s = bars[-BARS_KEEP:], ee[-BARS_KEEP:], es[-BARS_KEEP:]
        STATE.ind = indicators(bars, ee, es, cfg["lookback"])
    return events, first_load


def note_signal(ev, note):
    with STATE.lock:
        row = {k: ev.get(k) for k in ("kind", "t", "at", "close", "reason", "side")}
        row["note"] = note
        STATE.signals.append(row)
        del STATE.signals[:-SIGNALS_KEEP]


def act_on_events(events, first_load, now_ts):
    for ev in events:
        if ev["kind"] == "EXIT":
            with STATE.lock:
                STATE.pending = None
                n = len(STATE.positions)
            note_signal(ev, ("closing %d spread%s" % (n, "" if n == 1 else "s")) if n
                        else ("before this app was watching" if ev["history"] else "no spreads open"))
            if not ev["history"]:
                log_event("signal", "EXIT %s at %s: NIFTY closed %.2f - %s%s"
                          % (ev["side"], ev["at"], ev["close"], REASON_WORDS.get(ev["reason"], ev["reason"]),
                             "" if ev["fresh"] else " (caught up - the app had no candles then)"))
            if n:
                close_all(ev["reason"], index_px=ev["close"])
            continue
        # an entry
        if ev["history"]:
            note_signal(ev, "before this app was watching - not traded")
            continue
        if not ev["fresh"]:
            note_signal(ev, "missed - the app had no candles then; not traded late")
            log_event("skip", "%s signal at %s was missed (the app had no candles then) - "
                              "not traded late" % (ev["kind"], ev["at"]))
            continue
        with STATE.lock:
            running = STATE.running
            if running:
                STATE.pending = new_pending("entry")
        if not running:
            note_signal(ev, "stopped - not traded")
            log_event("signal", "%s signal at %s (NIFTY %.2f) - the strategy is stopped, so no spreads"
                      % (ev["kind"], ev["at"], ev["close"]))
            continue
        note_signal(ev, "traded")
        log_event("signal", "%s signal at %s: NIFTY closed %.2f %s the %d EMA after %d+ bars %s it - "
                            "opening %s spreads" % (
                                ev["kind"], ev["at"], ev["close"],
                                "above" if ev["kind"] == "LONG" else "below", STATE.cfg["ema_entry"],
                                STATE.cfg["lookback"], "under" if ev["kind"] == "LONG" else "over",
                                "bullish" if ev["kind"] == "LONG" else "bearish"))
    if first_load:
        s = STATE.sig
        log_event("candles", "loaded %d NIFTY %d-minute candles. The script's position right now: %s" % (
            len(STATE.bars), STATE.cfg["interval"],
            "FLAT" if not s.get("side") else "%s since %s @ %.2f - opened before this app was watching, "
                                             "so not traded; waiting for the next fresh signal"
                                             % (s["side"], s["at"], s["entry"])))


def candle_step(now_ts):
    """Fetch candles when a new one has closed (or on first load), then run
    the rules.  A candle the broker has not published yet is retried with a
    growing gap - and on a holiday, when none will come, that gap caps out."""
    cfg = STATE.cfg
    exp = last_closed_slot(now_ts, cfg["interval"])
    if STATE.candles_loaded:
        if exp is None or exp <= STATE.last_bar_t:
            return
        if now_ts < bar_end(exp, cfg["interval"]) + CANDLE_DELAY:
            return
    if now_ts < STATE.candle_try_at:
        return
    bars, err = fetch_candles(cfg, now_ts)
    if bars is None:
        STATE.candle_backoff = min(CANDLE_BACKOFF_MAX, max(5.0, STATE.candle_backoff * 2))
        STATE.candle_try_at = now_ts + STATE.candle_backoff
        if STATE.candle_note != err:
            log_event("candles", "NIFTY candles unavailable: %s - retrying" % err)
        STATE.candle_note = err
        return
    if any(STATE.cfg[k] != cfg[k] for k in SIGNAL_KEYS):
        return                         # the chart settings changed during the call: this series is stale
    STATE.candles_loaded = True
    events, first_load = process_bars(bars, now_ts)
    if exp is not None and STATE.last_bar_t < exp:
        STATE.candle_backoff = min(CANDLE_BACKOFF_MAX, max(5.0, STATE.candle_backoff * 2))
        STATE.candle_try_at = now_ts + STATE.candle_backoff
        STATE.candle_note = "waiting for the %s candle" % _ist(exp).strftime("%H:%M")
    else:
        STATE.candle_backoff, STATE.candle_try_at = 0.0, 0.0
        STATE.candle_note = "up to date"
    act_on_events(events, first_load, now_ts)
    STATE.save()


# ─────────────────────────────────────────────────────────────────────────────
#  OPTION CHAIN
# ─────────────────────────────────────────────────────────────────────────────
def quote_for(snap, strike, opt_type):
    side = "ce" if str(opt_type).upper() == "CE" else "pe"
    row = (snap.get("chain") or {}).get(round(_f(strike), 2))
    if not row:
        return None
    q = row.get(side)
    if not isinstance(q, dict):
        return None
    return {"ltp": _f(q.get("last_price")), "bid": _f(q.get("top_bid_price")),
            "ask": _f(q.get("top_ask_price")), "iv": _f(q.get("implied_volatility")),
            "oi": _f(q.get("oi"))}


def build_chain_snapshot(expiry, res):
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
    return {"expiry": expiry, "spot": spot, "chain": chain} if chain else None


def get_snap(expiry, max_age=0.0):
    """The expiry's option chain, from the cache if younger than max_age."""
    with STATE.lock:
        c = STATE.snaps.get(expiry)
    if c and time.time() - c["_at"] <= max_age:
        return c
    STATE.chain_tried[expiry] = time.time()
    res = throttled_chain(expiry)
    snap = build_chain_snapshot(expiry, res)
    with STATE.lock:
        if snap:
            snap["_at"] = time.time()
            STATE.snaps[expiry] = snap
            STATE.spot = snap["spot"]
            STATE.chain_note.pop(expiry, None)
        else:
            STATE.chain_note[expiry] = res.get("message") or "option chain unavailable"
    return snap


def on_step(k, step):
    return k > 0 and abs(k / step - round(k / step)) < 1e-9


def atm_strike(spot, listed, step):
    """Spot rounded to the strike step (halves UP - Python's round() is
    banker's rounding), or the nearest listed strike when that is missing."""
    k = float(int(math.floor(spot / step + 0.5)) * step)
    if k in listed:
        return k
    return min(listed, key=lambda x: (abs(x - spot), -x))


def fill_px(role, q):
    """What a paper order fills at: a sale at the bid, a purchase at the ask.
    A side with no quote falls back to the last traded price."""
    if not q:
        return None
    px = (q["bid"] if role == "SELL" else q["ask"]) or q["ltp"]
    return px if px > 0 else None


def close_px(leg, q):
    """Closing a leg is the opposite order: a sold leg is bought back."""
    return fill_px("BUY" if leg["sign"] < 0 else "SELL", q)


def spread_plan(view, expiry, snap, cfg=None):
    """The two legs a LONG or SHORT signal trades in one expiry, priced off
    its option chain right now.  Returns (plan, None) or (None, why)."""
    cfg = cfg or STATE.cfg
    credit = cfg["spread"] == "credit"
    opt = "PE" if (view == "LONG") == credit else "CE"
    step = cfg["strike_step"]
    listed = sorted(k for k in snap["chain"] if on_step(k, step))
    if not listed:
        return None, "no strikes in the option chain"
    atm = atm_strike(snap["spot"], listed, step)
    dist = cfg["hedge_strikes"] * step
    if opt == "PE":
        far = max((k for k in listed if k <= atm - dist + 1e-6), default=None)
    else:
        far = min((k for k in listed if k >= atm + dist - 1e-6), default=None)
    if far is None:
        return None, "no %s strike %d points %s the ATM %d is listed" % (
            opt, dist, "below" if opt == "PE" else "above", atm)
    roles = ("SELL", "BUY") if credit else ("BUY", "SELL")
    legs = []
    for role, k in zip(roles, (atm, far)):
        q = quote_for(snap, k, opt)
        px = fill_px(role, q)
        if not px:
            return None, "no price for %d %s" % (k, opt)
        mark = close_px({"sign": 1 if role == "BUY" else -1}, q) or px
        legs.append({"role": role, "sign": 1 if role == "BUY" else -1, "strike": k, "opt_type": opt,
                     "entry": round(px, 2), "mark": round(mark, 2)})
    net = round(sum(-l["sign"] * l["entry"] for l in legs), 2)       # + credit received, - debit paid
    width = abs(atm - far)
    if credit and not 0 < net < width:
        return None, "the quotes give no usable credit (%.2f on a %d-point spread)" % (net, width)
    if not credit and not 0 < -net < width:
        return None, "the quotes give no usable debit (%.2f on a %d-point spread)" % (-net, width)
    lot = lot_for(expiry, atm, opt)
    qty = lot * cfg["lots"]
    net_now = round(sum(-l["sign"] * l["mark"] for l in legs), 2)
    return {"view": view, "spread": cfg["spread"], "opt_type": opt, "expiry": expiry,
            "atm": atm, "far": far, "width": width, "legs": legs, "net": net,
            "lot": lot, "lots": cfg["lots"], "qty": qty,
            "max_profit": round((net if credit else width + net) * qty, 2),
            "max_loss": round((width - net if credit else -net) * qty, 2),
            "net_now": net_now, "pnl": round((net - net_now) * qty, 2),
            "spot": snap["spot"]}, None


def legs_text(p, price_key="entry"):
    return " + ".join("%s %d %s @ %.2f" % (l["role"], int(l["strike"]), l["opt_type"], _f(l.get(price_key)))
                      for l in p["legs"])


# ─────────────────────────────────────────────────────────────────────────────
#  SPREADS
# ─────────────────────────────────────────────────────────────────────────────
REASON_WORDS = {
    "EMA_STOP": "closed through the stop EMA", "STOP": "index stop-loss %", "TARGET": "index take-profit %",
    "EXPIRY_DAY": "expiry-day exit", "EXPIRED": "expired while the app was off",
    "SPREAD_TARGET": "spread take-profit", "SPREAD_STOP": "spread stop",
    "MANUAL": "closed by hand", "MANUAL_LAST_MARK": "closed by hand at the last mark",
    "SIGNAL_FLAT": "the index signal is flat",
    "VIX_KILL": "VIX kill switch - India VIX above the limit",
}


# ─────────────────────────────────────────────────────────────────────────────
#  VIX KILL SWITCH
#  While India VIX is ABOVE the limit this hedged-selling strategy opens no
#  spreads and closes every open one.  New spreads are allowed again once VIX
#  is back at or below the limit (on the next signal or roll).
#  The limit is set in ONE place: NIFTY Trader's "VIX limit" (hub/risk.json),
#  re-read every check, so a change applies within a minute.  0 turns it off.
#  If VIX cannot be read, no new spreads are opened; open ones are kept.
# ─────────────────────────────────────────────────────────────────────────────
VIX_SECURITY_ID, VIX_SEG = 21, "IDX_I"          # NSE "INDIA VIX"
DEFAULT_VIX_LIMIT = 13.5
RISK_FILE = _env("NIFTY_RISK_FILE") or os.path.join(
    os.path.dirname(os.path.dirname(APP_DIR)), "hub", "risk.json")
VIX_EVERY_OPEN, VIX_EVERY_CLOSED = 60, 900
VIX = {"value": None, "at": "", "kill": False, "blocked": True, "note": "not checked yet", "checked": 0.0}


def vix_limit():
    try:
        with open(RISK_FILE, encoding="utf-8") as f:
            d = json.load(f)
        v = float(d.get("vix_limit", DEFAULT_VIX_LIMIT))
        # Unticked for this strategy in the hub's VIX limit dialog = switch off.
        if not (d.get("apply") or {}).get(os.path.basename(APP_DIR), True):
            return 0.0
        return v if v == v and v >= 0 else DEFAULT_VIX_LIMIT
    except (OSError, ValueError, TypeError, AttributeError):
        return DEFAULT_VIX_LIMIT


def fetch_india_vix():
    res = call_dhan("marketfeed/ltp", {VIX_SEG: [VIX_SECURITY_ID]}, timeout=10)
    if res.get("status") != "success":
        return None, res.get("message") or "no answer"
    seg = (res.get("data") or {}).get(VIX_SEG) or {}
    node = seg.get(str(VIX_SECURITY_ID)) or seg.get(VIX_SECURITY_ID) or {}
    v = _f(node.get("last_price") if isinstance(node, dict) else None)
    return (v, "") if v > 0 else (None, "no VIX price in Dhan's answer")


def vix_step(now_ts, market_open):
    """Throttled VIX check.  Closes everything only while the market is open."""
    limit = vix_limit()
    if limit <= 0:
        VIX.update(kill=False, blocked=False, note="VIX kill switch is off (limit 0)")
        return
    if now_ts - VIX["checked"] < (VIX_EVERY_OPEN if market_open else VIX_EVERY_CLOSED) \
            and VIX["value"] is not None:
        return
    VIX["checked"] = now_ts
    v, err = fetch_india_vix()
    if v is None:
        note = "India VIX unavailable (%s) - no new spreads until it can be read" % err
        if note != VIX["note"]:
            log_event("vix", note)
        VIX.update(blocked=True, note=note)
        return
    kill = v > limit
    if kill != VIX["kill"]:
        log_event("vix", ("India VIX %.2f crossed ABOVE the %.2f limit - KILL SWITCH ON: no new "
                          "spreads, closing every open one" if kill else
                          "India VIX %.2f is back at or below the %.2f limit - new spreads allowed "
                          "again") % (v, limit))
    VIX.update(value=v, at=now_ist().strftime("%H:%M:%S"), kill=kill, blocked=kill,
               note="India VIX %.2f at %s, limit %.2f" % (v, now_ist().strftime("%H:%M:%S"), limit))
    if kill and market_open:
        with STATE.lock:
            STATE.pending = None
            has = bool(STATE.positions)
        if has:
            close_all("VIX_KILL")


def expiry_due(expiry, now):
    """Why a spread in this expiry must close now, or None.  An expiry's last
    day ends at the exit time: a short ATM option is not left to settle."""
    today = now.strftime("%Y-%m-%d")
    if expiry < today:
        return "EXPIRED"
    if expiry == today and now.strftime("%H:%M") >= STATE.cfg["expiry_exit"]:
        return "EXPIRY_DAY"
    return None


def live_expiries(now):
    return [e for e in STATE.expiry_list if not expiry_due(e, now)]


def wanted_expiries(now):
    """[(slot, expiry)] for the ticked slots - slot 1 is the nearest expiry
    still tradeable, so the slots roll forward on their own."""
    live = live_expiries(now)
    return [(s, live[s - 1]) for s in STATE.cfg["slots"] if s <= len(live)]


def new_pending(kind):
    """Spreads still to open for the current signal.  Expiries that already
    hold a spread are marked done, so a roll only fills the gap."""
    return {"kind": kind, "sig_id": STATE.sig.get("id"), "side": STATE.sig.get("side"),
            "created": time.time(), "deadline": None,
            "done": sorted({p["expiry"] for p in STATE.positions}), "why": {}}


PENDING_WINDOW = 600            # a spread that cannot open within 10 market minutes is skipped


def open_spread(sig, slot, expiry, snap, kind):
    if VIX["blocked"] and vix_limit() > 0:
        return None, "VIX kill switch: %s" % VIX["note"]
    plan, err = spread_plan(sig["side"], expiry, snap)
    if not plan:
        return None, err
    now = time.time()
    pos = dict(plan)
    pos.update(id="%s-%s-%s-%d" % (sig["id"], expiry, plan["opt_type"], int(now * 1000)),
               sig_id=sig["id"], slot=slot, kind=kind, opened=ts(), opened_ts=now,
               index_signal=sig["entry"], signal_at=sig["at"], spot_entry=snap["spot"],
               mark_at=now, status="OPEN")
    for leg in pos["legs"]:
        meta = contract_meta(expiry, leg["strike"], leg["opt_type"])
        leg["sid"] = (meta or {}).get("sid")
    with STATE.lock:
        STATE.positions.append(pos)
        STATE.save()
    log_event("entry", "%s%s %s (slot %d): %s = %s %.2f x %d - max profit Rs %.0f, max loss Rs %.0f" % (
        "ROLL " if kind == "roll" else "", "BULL" if sig["side"] == "LONG" else "BEAR", expiry, slot,
        legs_text(pos), "credit" if pos["net"] > 0 else "debit", abs(pos["net"]), pos["qty"],
        pos["max_profit"], pos["max_loss"]))
    return pos, None


def mark_spread(pos, snap):
    """Value the spread at what closing it costs right now: the sold leg at
    the ask, the bought leg at the bid.  Called under STATE.lock."""
    marks = []
    for leg in pos["legs"]:
        px = close_px(leg, quote_for(snap, leg["strike"], leg["opt_type"]))
        if not px:
            return False
        marks.append(px)
    for leg, px in zip(pos["legs"], marks):
        leg["mark"] = round(px, 2)
    pos["net_now"] = round(sum(-l["sign"] * l["mark"] for l in pos["legs"]), 2)
    pos["pnl"] = round((pos["net"] - pos["net_now"]) * pos["qty"], 2)
    pos["mark_at"] = time.time()
    pos["spot_now"] = snap["spot"]
    return True


def close_position(pid, reason, snap=None, index_px=None):
    """Close one spread at the snapshot's prices, or at its last marks when a
    leg has no quote there (said so in the record, never hidden)."""
    with STATE.lock:
        pos = next((p for p in STATE.positions if p["id"] == pid), None)
        if not pos:
            return None
        live = bool(snap)
        exits = []
        for leg in pos["legs"]:
            px = close_px(leg, quote_for(snap, leg["strike"], leg["opt_type"])) if snap else None
            if not px:
                px, live = _f(leg.get("mark"), leg["entry"]), False
            exits.append(round(px, 2))
        rec = json.loads(json.dumps(pos))
        for leg, px in zip(rec["legs"], exits):
            leg["exit"] = px
        net_exit = round(sum(-l["sign"] * l["exit"] for l in rec["legs"]), 2)
        pnl = round((rec["net"] - net_exit) * rec["qty"], 2)
        sell = next((l for l in rec["legs"] if l["role"] == "SELL"), {})
        buy = next((l for l in rec["legs"] if l["role"] == "BUY"), {})
        rec.update(status="CLOSED", closed=ts(), closed_ts=time.time(), reason=reason,
                   exit_src="live quote" if live else "last mark", net_exit=net_exit, pnl=pnl,
                   spot_exit=(snap or {}).get("spot") or STATE.spot, index_exit=index_px,
                   sell_strike=sell.get("strike"), sell_entry=sell.get("entry"), sell_exit=sell.get("exit"),
                   buy_strike=buy.get("strike"), buy_entry=buy.get("entry"), buy_exit=buy.get("exit"))
        rec.pop("mark_at", None)
        STATE.positions = [p for p in STATE.positions if p["id"] != pid]
        STATE.unflushed.append(rec)            # durable in the state file from here on
        STATE.history.append(rec)
        STATE.save()
    flush_unflushed()                          # outside STATE.lock: lock order
    log_event("exit", "%s %s: %s - %s. P&L Rs %.2f%s" % (
        "BULL" if rec["view"] == "LONG" else "BEAR", rec["expiry"], legs_text(rec, "exit"),
        REASON_WORDS.get(reason, reason), pnl, "" if live else " (no live quote - last mark)"))
    return rec


def close_all(reason, index_px=None):
    """The index signal exited: every spread goes, each at a fresh quote."""
    with STATE.lock:
        by_exp = {}
        for p in STATE.positions:
            by_exp.setdefault(p["expiry"], []).append(p["id"])
    for expiry, ids in sorted(by_exp.items()):
        snap = get_snap(expiry, max_age=5)
        for pid in ids:
            close_position(pid, reason, snap, index_px)


def check_spread_exits(expiry):
    """The optional per-spread take-profit and stop, on every fresh mark."""
    cfg = STATE.cfg
    hits = []
    with STATE.lock:
        for p in STATE.positions:
            if p["expiry"] != expiry:
                continue
            if cfg["spread_tp_pct"] > 0 and p["pnl"] >= p["max_profit"] * cfg["spread_tp_pct"] / 100.0:
                hits.append((p["id"], "SPREAD_TARGET"))
            elif cfg["spread_sl_pct"] > 0 and p["pnl"] <= -p["max_loss"] * cfg["spread_sl_pct"] / 100.0:
                hits.append((p["id"], "SPREAD_STOP"))
        snap = STATE.snaps.get(expiry)
    for pid, why in hits:
        close_position(pid, why, snap)


# ─────────────────────────────────────────────────────────────────────────────
#  ENGINE
# ─────────────────────────────────────────────────────────────────────────────
PREVIEW_EVERY = 20              # while flat, one expiry's chain every 20 s for the "if a signal fired now" table


def refresh_expiries(force=False):
    """Re-read every 30 minutes, so a new expiry appears and slot 1 rolls on."""
    if not force and time.time() - STATE.expiry_fetched < 1800:
        return
    STATE.expiry_fetched = time.time()
    lst = fetch_expiry_list()
    if lst:
        with STATE.lock:
            STATE.expiry_list = lst


def expiry_step(now_ts):
    """Close spreads whose expiry has reached its exit time (or passed while
    the app was off), then queue the roll into the next expiry."""
    now = _ist(now_ts)
    with STATE.lock:
        due = {}
        for p in STATE.positions:
            why = expiry_due(p["expiry"], now)
            if why:
                due.setdefault((p["expiry"], why), []).append(p["id"])
    if not due:
        return
    closed = 0
    for (expiry, why), ids in sorted(due.items()):
        snap = get_snap(expiry, max_age=5) if why == "EXPIRY_DAY" else None   # an expired contract has no quote
        for pid in ids:
            if close_position(pid, why, snap):
                closed += 1
    with STATE.lock:
        roll = (closed and STATE.cfg["roll"] and STATE.running and STATE.sig.get("side")
                and not STATE.pending)
        if roll:
            STATE.pending = new_pending("roll")
            STATE.save()
    if roll:
        log_event("roll", "%d spread%s closed for expiry - the %s signal still holds, so rolling into "
                          "the next expiry" % (closed, "" if closed == 1 else "s", STATE.sig["side"]))


def orphan_step():
    """A spread whose direction no longer matches the index signal (a crash
    between the exit and the close, say) is closed - never left unmanaged."""
    with STATE.lock:
        side = STATE.sig.get("side")
        stray = [p["id"] for p in STATE.positions if p.get("view") != side]
    for pid in stray:
        with STATE.lock:
            p = next((x for x in STATE.positions if x["id"] == pid), None)
            snap = STATE.snaps.get(p["expiry"]) if p else None
        if p:
            fresh = snap and time.time() - snap["_at"] < 30
            close_position(pid, "SIGNAL_FLAT", snap if fresh else None)


def pending_step(now_ts):
    """Open the spreads a fresh signal (or a roll) asked for, one expiry at a
    time.  A chain that is down is retried until PENDING_WINDOW runs out."""
    with STATE.lock:
        p = STATE.pending
        if not p:
            return
        sig = dict(STATE.sig)
        if not STATE.running or sig.get("id") != p["sig_id"] or sig.get("side") != p["side"]:
            STATE.pending = None
            return
        if p.get("deadline") is None:
            p["deadline"] = now_ts + PENDING_WINDOW
        if now_ts > p["deadline"]:
            left = {e: w for e, w in p["why"].items() if e not in p["done"]}
            STATE.pending = None
            STATE.save()
            if left:
                log_event("skip", "gave up opening %s: %s" % (
                    ", ".join(sorted(left)), "; ".join("%s - %s" % (e, w) for e, w in sorted(left.items()))))
            return
        held = {x["expiry"] for x in STATE.positions}
        todo = [(s, e) for s, e in wanted_expiries(_ist(now_ts)) if e not in held and e not in p["done"]]
        if not todo:
            STATE.pending = None
            STATE.save()
            return
    for slot, expiry in todo:
        if _SHUTDOWN.is_set():
            return
        snap = get_snap(expiry, max_age=5)
        pos, err = (None, "option chain unavailable: %s" % STATE.chain_note.get(expiry, "?")) if not snap \
            else open_spread(sig, slot, expiry, snap, p["kind"])
        with STATE.lock:
            if STATE.pending is not p:
                return                 # stopped, or the signal exited, meanwhile
            if pos:
                p["done"].append(expiry)
                p["why"].pop(expiry, None)
            else:
                if p["why"].get(expiry) != err:
                    log_event("skip", "%s: cannot open the spread yet - %s" % (expiry, err))
                p["why"][expiry] = err


def mark_step():
    """Re-price the held expiry asked for longest ago - one chain call a pass.
    By last ATTEMPT, not last success, so one expiry whose chain is down
    cannot starve the others of prices."""
    with STATE.lock:
        held = sorted({p["expiry"] for p in STATE.positions})
        if not held:
            return
        expiry = min(held, key=lambda e: STATE.chain_tried.get(e, 0))
    snap = get_snap(expiry)
    if not snap:
        return
    with STATE.lock:
        for p in STATE.positions:
            if p["expiry"] == expiry:
                mark_spread(p, snap)
    check_spread_exits(expiry)


def preview_step():
    """While nothing is held, refresh one ticked expiry every PREVIEW_EVERY
    seconds so the dashboard can show what a signal would trade right now."""
    if time.time() - STATE.preview_at < PREVIEW_EVERY:
        return
    with STATE.lock:
        if STATE.positions:
            return
        want = [e for _, e in wanted_expiries(now_ist())]
        if not want:
            return
        expiry = min(want, key=lambda e: STATE.chain_tried.get(e, 0))
    STATE.preview_at = time.time()
    get_snap(expiry)


def engine_step(at=None):
    """One pass of the engine.  Split out of the loop so tests can drive it
    with fake candles, a fake chain and a fake clock."""
    now_ts = time.time() if at is None else at
    now = _ist(now_ts)
    mstate, why = market_state(now)
    STATE.market_note = "%s - %s" % (mstate, why)

    if STATE.autostart and not STATE.running and validate_cfg(STATE.cfg) is None:
        with STATE.lock:
            STATE.autostart, STATE.running = False, True
        log_event("control", "started automatically on launch")

    day = now.strftime("%Y-%m-%d")
    if day != STATE.day:
        STATE.day = day
        STATE.expiry_fetched = 0.0
        log_event("day", "new session %s" % day)

    ts_info = token_status()
    if not ts_info["configured"] or ts_info["expired"]:
        STATE.status = "token %s" % ts_info["human"]
        return
    if time.time() < _auth_block[0]:
        STATE.status = ("the broker rejected the token - paste a fresh one in Broker token "
                        "(retrying in %ds)" % int(_auth_block[0] - time.time()))
        return
    if mstate in ("OPEN", "PRE") or not STATE.expiry_list:
        refresh_expiries()

    vix_step(now_ts, mstate == "OPEN")
    candle_step(now_ts)
    expiry_step(now_ts)
    orphan_step()
    if mstate == "OPEN":
        pending_step(now_ts)
        mark_step()
        if STATE.running:
            preview_step()
    if STATE.unflushed:
        flush_unflushed()                       # retry a trade write that failed

    with STATE.lock:
        n, side = len(STATE.positions), STATE.sig.get("side")
    sig_txt = "signal %s" % (side or "FLAT")
    if not STATE.running:
        STATE.status = "stopped - %s%s" % (sig_txt, "; still managing %d open spread%s until the signal exits"
                                                    % (n, "" if n == 1 else "s") if n else "")
    elif mstate != "OPEN":
        STATE.status = "market %s - %s, %d open spread%s" % (why, sig_txt, n, "" if n == 1 else "s")
    else:
        STATE.status = "%s - %d open spread%s - candles %s" % (sig_txt, n, "" if n == 1 else "s",
                                                               STATE.candle_note)


def engine_loop():
    log_event("boot", "engine thread started")
    while not _SHUTDOWN.is_set():
        _SHUTDOWN.wait(1.0)
        if _SHUTDOWN.is_set():
            break
        try:
            engine_step()
        except Exception as e:
            log_event("error", "engine: %s: %s" % (e.__class__.__name__, e))
            STATE.status = "error: %s" % e


def boot_loop():
    while not _SHUTDOWN.is_set():
        try:
            STATE.scrip_lookup = load_scrip_lookup()
            refresh_expiries(force=True)
            if STATE.expiry_list:
                log_event("boot", "ready - %d expiries listed, NIFTY lot %d"
                          % (len(STATE.expiry_list), lot_size()))
                return
            STATE.status = "could not load expiries - check the token"
        except Exception as e:
            log_event("error", "boot: %s" % e)
        _SHUTDOWN.wait(120)


def _graceful(*_a):
    if _SHUTDOWN.is_set():
        return
    _SHUTDOWN.set()
    try:
        STATE.save()
    except Exception:
        pass


# ─────────────────────────────────────────────────────────────────────────────
#  WEB
# ─────────────────────────────────────────────────────────────────────────────
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 256 * 1024


@app.before_request
def _same_origin_only():
    """No password on the desktop, so refuse anything that is not this page:
    a foreign Host (DNS rebinding) or a cross-site POST (any web page in your
    browser could otherwise start the bot or wipe the trade book)."""
    host = (request.host or "").rsplit(":", 1)[0].strip("[]")
    if host not in ("127.0.0.1", "localhost"):
        return jsonify({"error": "forbidden host"}), 403
    if request.method not in ("GET", "HEAD", "OPTIONS"):
        if request.headers.get("Sec-Fetch-Site") == "cross-site":
            return jsonify({"error": "cross-site request refused"}), 403
        origin = request.headers.get("Origin")
        if origin and origin.rstrip("/") != request.host_url.rstrip("/"):
            return jsonify({"error": "cross-site request refused"}), 403
    return None


@app.after_request
def _no_foreign_frames(resp):
    # Only NIFTY Trader (another port on this machine) may show this page in a
    # frame.  Any other site framing it could steer clicks onto Start or Wipe.
    resp.headers["Content-Security-Policy"] = ("frame-ancestors 'self' http://127.0.0.1:* "
                                               "http://localhost:*")
    return resp


def dte_of(expiry, today=None):
    try:
        return (datetime.strptime(expiry, "%Y-%m-%d").date() - (today or now_ist().date())).days
    except ValueError:
        return None


def position_view(p):
    v = dict(p)
    v["quote_age"] = round(time.time() - p["mark_at"]) if p.get("mark_at") else None
    v["dte"] = dte_of(p["expiry"])
    return v


def trade_stats(rows):
    n = len(rows)
    wins = [r for r in rows if _f(r.get("pnl")) > 0]
    losses = [r for r in rows if _f(r.get("pnl")) < 0]
    win_sum = sum(_f(r.get("pnl")) for r in wins)
    loss_sum = sum(_f(r.get("pnl")) for r in losses)
    cum = peak = 0.0
    dd = 0.0
    series = []
    for i, r in enumerate(rows, 1):
        cum += _f(r.get("pnl"))
        peak = max(peak, cum)
        dd = min(dd, cum - peak)
        series.append({"i": i, "cum": round(cum, 2), "pnl": round(_f(r.get("pnl")), 2),
                       "contract": "%s %s" % (r.get("expiry") or "", "bull" if r.get("view") == "LONG" else "bear"),
                       "closed": r.get("closed") or ""})

    def group(fn):
        g = {}
        for r in rows:
            k = str(fn(r))
            e = g.setdefault(k, {"n": 0, "pnl": 0.0, "wins": 0})
            e["n"] += 1
            e["pnl"] = round(e["pnl"] + _f(r.get("pnl")), 2)
            e["wins"] += 1 if _f(r.get("pnl")) > 0 else 0
        return g

    if loss_sum:
        pf = round(win_sum / abs(loss_sum), 2)
    else:
        pf = "inf" if wins else None           # all winners: infinite, not "no data"
    return {
        "trades": n, "wins": len(wins), "losses": len(losses),
        "win_rate": round(len(wins) / n * 100.0, 1) if n else 0.0,
        "avg_win": round(win_sum / len(wins), 2) if wins else 0.0,
        "avg_loss": round(loss_sum / len(losses), 2) if losses else 0.0,
        "profit_factor": pf,
        "total": round(win_sum + loss_sum, 2),
        "best": round(max((_f(r.get("pnl")) for r in rows), default=0.0), 2),
        "worst": round(min((_f(r.get("pnl")) for r in rows), default=0.0), 2),
        "max_drawdown": round(dd, 2),
        "by_view": group(lambda r: "Bull" if r.get("view") == "LONG" else "Bear"),
        "by_slot": group(lambda r: "Expiry %s" % (r.get("slot") or "?")),
        "by_reason": group(lambda r: REASON_WORDS.get(r.get("reason"), r.get("reason") or "?")),
        "series": series,
    }


def preview_rows(now):
    """What a signal would trade right now, from the cached option chains."""
    rows = []
    with STATE.lock:
        wanted = wanted_expiries(now)
        snaps = dict(STATE.snaps)
    for slot, e in wanted:
        snap = snaps.get(e)
        row = {"slot": slot, "expiry": e, "dte": dte_of(e, now.date()),
               "age": round(time.time() - snap["_at"]) if snap else None,
               "note": STATE.chain_note.get(e)}
        if snap:
            for view in ("LONG", "SHORT"):
                plan, err = spread_plan(view, e, snap)
                row[view] = plan or {"error": err}
        rows.append(row)
    return rows


@app.route("/api/state")
def api_state():
    today = now_ist().strftime("%Y-%m-%d")
    now = now_ist()
    with STATE.lock:
        positions = [position_view(p) for p in sorted(STATE.positions, key=lambda p: p["expiry"])]
        hist = list(STATE.history)
        pend = STATE.pending
        pending = None if not pend else {"kind": pend["kind"], "done": list(pend["done"]),
                                         "why": dict(pend["why"])}
        live = live_expiries(now)
        slots = [{"slot": i + 1, "expiry": e, "dte": dte_of(e, now.date())} for i, e in enumerate(live[:MAX_SLOTS])]
        sig = dict(STATE.sig)
        ind = dict(STATE.ind)
        signals = list(reversed(STATE.signals[-15:]))
    today_rows = [h for h in hist if str(h.get("closed") or "").startswith(today)]
    return jsonify({
        "running": STATE.running, "status": STATE.status, "market": STATE.market_note,
        "cfg": STATE.cfg, "token": token_status(), "spot": STATE.spot,
        "sig": sig, "ind": ind, "candle_note": STATE.candle_note, "last_bar_t": STATE.last_bar_t,
        "slots": slots, "signals": signals, "pending": pending,
        "today_pnl": round(sum(_f(h.get("pnl")) for h in today_rows), 2),
        "today_trades": len(today_rows),
        "realised": round(sum(_f(h.get("pnl")) for h in hist), 2), "all_trades": len(hist),
        "open_pnl": round(sum(_f(p.get("pnl")) for p in positions), 2),
        "open_risk": round(sum(_f(p.get("max_loss")) for p in positions), 2),
        "positions": positions, "preview": preview_rows(now) if not positions else [],
        "events": recent_events(15), "lot": lot_size(),
        "intervals": list(INTERVALS), "max_slots": MAX_SLOTS,
        "fresh_window": fresh_window(STATE.cfg["interval"]),
        "vix": {"value": VIX["value"], "at": VIX["at"], "kill": VIX["kill"], "note": VIX["note"],
                "limit": vix_limit()},
    })


@app.route("/api/chart")
def api_chart():
    n = max(20, min(400, int(_f(request.args.get("n"), 150))))
    with STATE.lock:
        bars, ee, es = STATE.bars[-n:], STATE.ema_e[-n:], STATE.ema_s[-n:]
        t0 = bars[0]["t"] if bars else 0
        marks = [s for s in STATE.signals if _f(s.get("t")) >= t0]
    rows = []
    for b, e1, e2 in zip(bars, ee, es):
        d = _ist(b["t"])
        rows.append({"t": b["t"], "c": b["c"], "ee": _r2(e1), "es": _r2(e2),
                     "hm": d.strftime("%H:%M"), "day": d.strftime("%d %b")})
    return jsonify({"interval": STATE.cfg["interval"], "ema_entry": STATE.cfg["ema_entry"],
                    "ema_stop": STATE.cfg["ema_stop"], "bars": rows, "markers": marks,
                    "note": STATE.candle_note})


@app.route("/api/history")
def api_history():
    with STATE.lock:
        rows = list(STATE.history)
    return jsonify({"rows": rows, "stats": trade_stats(rows)})


def _csv(filename, header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(header)
    w.writerows(rows)
    # The BOM makes Excel open this as UTF-8.
    return Response("﻿" + buf.getvalue(), content_type="text/csv; charset=utf-8",
                    headers={"Content-Disposition": 'attachment; filename="%s"' % filename,
                             "Cache-Control": "no-store"})


TRADE_COLS = [("Closed", "closed"), ("Expiry", "expiry"), ("Expiry slot", "slot"), ("Signal", "view"),
              ("Spread", "spread"), ("Type", "opt_type"),
              ("Sell strike", "sell_strike"), ("Sell entry", "sell_entry"), ("Sell exit", "sell_exit"),
              ("Buy strike", "buy_strike"), ("Buy entry", "buy_entry"), ("Buy exit", "buy_exit"),
              ("Net entry (+credit)", "net"), ("Net exit", "net_exit"),
              ("Lots", "lots"), ("Lot size", "lot"), ("Qty", "qty"), ("P&L", "pnl"),
              ("Max profit", "max_profit"), ("Max loss", "max_loss"), ("Exit reason", "reason"),
              ("Exit priced from", "exit_src"), ("Opened", "opened"), ("Opened by", "kind"),
              ("Signal bar", "signal_at"), ("NIFTY signal close", "index_signal"),
              ("NIFTY exit close", "index_exit"), ("Spot at entry", "spot_entry"),
              ("Spot at exit", "spot_exit"), ("Id", "id")]


@app.route("/api/history.csv")
def api_history_csv():
    with STATE.lock:
        rows = list(STATE.history)
    return _csv("ema_hedge_trades_%s.csv" % now_ist().strftime("%Y%m%d"),
                [c for c, _ in TRADE_COLS], [[r.get(k, "") for _, k in TRADE_COLS] for r in rows])


@app.route("/api/positions.csv")
def api_positions_csv():
    cols = [("Expiry", "expiry"), ("Slot", "slot"), ("Signal", "view"), ("Legs", "legs_text"),
            ("Opened", "opened"), ("Net entry (+credit)", "net"), ("Net now", "net_now"), ("Qty", "qty"),
            ("Open P&L", "pnl"), ("Max profit", "max_profit"), ("Max loss", "max_loss")]
    with STATE.lock:
        rows = [dict(position_view(p), legs_text=legs_text(p)) for p in STATE.positions]
    return _csv("ema_hedge_positions_%s.csv" % now_ist().strftime("%Y%m%d"),
                [c for c, _ in cols], [[r.get(k, "") for _, k in cols] for r in rows])


def _remove_trades(pred, why):
    """Clear/Wipe never destroy data: removed trades are appended to
    trades_removed.jsonl first, then the book is rewritten without them."""
    flush_unflushed()
    with _book_lock:
        with STATE.lock:
            snap = list(STATE.history)
        gone = [r for r in snap if pred(r)]
        if not gone:
            return 0
        keep = [r for r in snap if not pred(r)]
        stamp = ts()
        append_trades([dict(r, removed=stamp, removed_why=why) for r in gone], TRADES_REMOVED_FILE)
        write_trades(keep)
        with STATE.lock:
            later = STATE.history[len(snap):]  # closed while we wrote; appended after us
            STATE.history = keep + later
    log_event("report", "%s: %d trade%s moved to trades_removed.jsonl"
              % (why, len(gone), "" if len(gone) == 1 else "s"))
    return len(gone)


@app.route("/api/history/clear", methods=["POST"])
def api_history_clear():
    ids = set((request.get_json(silent=True) or {}).get("ids") or [])
    n = _remove_trades(lambda r: r.get("id") in ids, "clear selected")
    return jsonify({"ok": True, "removed": n})


@app.route("/api/history/wipe", methods=["POST"])
def api_history_wipe():
    n = _remove_trades(lambda r: True, "wipe all")
    return jsonify({"ok": True, "removed": n})


@app.route("/api/events")
def api_events():
    before = request.args.get("before")
    try:
        before = int(before) if before else None
    except ValueError:
        before = None
    limit = max(1, min(1000, int(_f(request.args.get("limit"), 200))))
    kind = request.args.get("kind") or None
    return jsonify({"rows": read_events(before=before, limit=limit, kind=kind)})


@app.route("/api/start", methods=["POST"])
def api_start():
    err = validate_cfg(STATE.cfg)
    if err:
        return jsonify({"error": err}), 400
    with STATE.lock:
        STATE.running = True
    log_event("control", "started - the next fresh signal opens spreads")
    STATE.save()
    return jsonify({"ok": True})


@app.route("/api/stop", methods=["POST"])
def api_stop():
    with STATE.lock:
        STATE.running = False
        STATE.autostart = False
        STATE.pending = None
        n = len(STATE.positions)
    log_event("control", "stopped - no new spreads%s" % (
        "; %d open spread%s still close on the signal's exit" % (n, "" if n == 1 else "s") if n else ""))
    STATE.save()
    return jsonify({"ok": True})


@app.route("/api/flatten", methods=["POST"])
def api_flatten():
    """Close by hand at the last quote if it is fresh; otherwise at the last
    mark, and say so rather than pretend it is the current price."""
    pid = (request.get_json(silent=True) or {}).get("id")
    with STATE.lock:
        todo = [(p["id"], p["expiry"]) for p in STATE.positions if not pid or p["id"] == pid]
        snaps = dict(STATE.snaps)
    closed = []
    for i, expiry in todo:
        snap = snaps.get(expiry)
        fresh = snap and time.time() - snap["_at"] < 30
        why = "MANUAL" if fresh else "MANUAL_LAST_MARK"
        rec = close_position(i, why, snap if fresh else None)
        if rec:
            with STATE.lock:
                if STATE.pending and expiry not in STATE.pending["done"]:
                    STATE.pending["done"].append(expiry)       # a pending roll must not re-open it
            closed.append({"expiry": expiry, "reason": why, "pnl": rec["pnl"]})
    return jsonify({"ok": True, "closed": closed})


@app.route("/api/config", methods=["POST"])
def api_config():
    body = request.get_json(silent=True) or {}
    err = check_body(body)
    if err:
        return jsonify({"error": err}), 400
    with STATE.lock:
        new = clean_cfg({**STATE.cfg, **body})
        err = validate_cfg(new)
        if err:
            return jsonify({"error": err}), 400
        changed = [k for k in SIGNAL_KEYS if new[k] != STATE.cfg[k]]
        if changed and STATE.positions:
            return jsonify({"error": "Close the open spreads first: changing %s starts the index signal "
                                     "over from scratch, and the spreads would lose the signal that "
                                     "closes them." % ", ".join(LABELS[k] for k in changed)}), 400
        STATE.cfg = new
        if changed:
            # A new candle length or EMA is a different chart: rebuild the
            # signal from history (never traded) on the next pass.
            STATE.sig, STATE.last_bar_t, STATE.pending = flat_sig(), 0, None
            STATE.bars, STATE.ema_e, STATE.ema_s, STATE.ind, STATE.signals = [], [], [], {}, []
            STATE.candles_loaded, STATE.candle_try_at, STATE.candle_backoff = False, 0.0, 0.0
            STATE.candle_note = "reloading for the new settings"
        STATE.save()
    log_event("config", "settings saved - %d-min candles, EMA %d/%d, lookback %d; %s spreads, hedge %d strikes "
                        "(%d pts), expiries %s%s" % (
                            new["interval"], new["ema_entry"], new["ema_stop"], new["lookback"], new["spread"],
                            new["hedge_strikes"], new["hedge_strikes"] * new["strike_step"],
                            ",".join(str(s) for s in new["slots"]),
                            " - signal restarts from history" if changed else ""))
    return jsonify({"ok": True, "cfg": STATE.cfg})


@app.route("/api/token", methods=["POST"])
def api_token():
    if _env("DHAN_ACCESS_TOKEN"):
        return jsonify({"error": "The token comes from NIFTY Trader's Broker token "
                                 "screen. Change it there."}), 400
    body = request.get_json(silent=True) or {}
    tok = (body.get("access_token") or "").strip()
    if not tok:
        return jsonify({"error": "empty token"}), 400
    claims = decode_jwt(tok) or {}
    runtime_write(access_token=tok, client_id=str(claims.get("dhanClientId") or ""), saved_at=ts())
    log_event("token", "token saved locally")
    return jsonify({"ok": True, "token": token_status()})


@app.route("/")
def index():
    return Response(PAGE, mimetype="text/html")


PAGE = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>EMA Breakout Hedge</title>
<style>
:root{--bg:#0b0e14;--panel:#121722;--p2:#171d2b;--bd:#222a3b;--bd2:#2e3850;
 --tx:#cbd5e1;--br:#f1f5f9;--mu:#7c8aa3;--m2:#56627a;--ac:#38bdf8;--gn:#22c55e;--rd:#ef4444;--or:#f59e0b;
 --s1:#3987e5;--s2:#d95926;--s3:#199e70}
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
.bull{background:rgba(34,197,94,.14);color:#86efac}.bear{background:rgba(239,68,68,.14);color:#fca5a5}.flat{background:var(--p2);color:var(--mu)}
.bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.big{font-size:20px;font-weight:700;font-family:ui-monospace,Consolas,monospace}
.f{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.fl{display:flex;flex-direction:column;gap:5px}
label{font-size:12px;color:var(--mu)}
input,select{background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:8px 11px;color:var(--br);font:inherit}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{display:flex;align-items:center;gap:7px;background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:8px 12px;cursor:pointer;font-size:13px;color:var(--tx);user-select:none}
.chip input{margin:0}.chip.on{border-color:var(--ac);background:rgba(56,189,248,.1);color:var(--br)}
.chip small{color:var(--mu)}
.grp{margin-bottom:16px}.grp>label{display:block;margin-bottom:6px}
.mode{display:flex;flex-direction:column;gap:10px}
.mode .row{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:13px}
.note{background:rgba(245,158,11,.1);border-left:3px solid var(--or);padding:10px 14px;border-radius:8px;font-size:13px;margin-bottom:14px}
.mt{margin-top:14px}
svg text.ax{fill:var(--m2);font:11px ui-monospace,Consolas,monospace}
svg text.dl{fill:var(--tx);font:11px ui-monospace,Consolas,monospace}
svg line.grid{stroke:var(--bd);stroke-width:1}
svg line.zero{stroke:var(--bd2);stroke-dasharray:4 4}
svg line.xh{stroke:var(--mu);stroke-width:1}
svg circle.dot{fill:var(--panel);stroke-width:2}
svg:focus{outline:1px solid var(--bd2);outline-offset:2px}
.chart{position:relative}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--mu);margin:0 0 8px}
.legend i,.tip i{display:inline-block;width:14px;border-top:2px solid;vertical-align:middle;margin-right:6px}
.tip{position:absolute;top:10px;pointer-events:none;background:var(--p2);border:1px solid var(--bd2);border-radius:8px;padding:8px 10px;font-size:12px;display:none;min-width:170px;box-shadow:0 6px 20px rgba(0,0,0,.45)}
.tip .t{color:var(--mu);margin-bottom:4px}
.tip .row{display:flex;align-items:center;gap:6px;white-space:nowrap}
.tip b{color:var(--br);font-variant-numeric:tabular-nums;min-width:72px;display:inline-block}
.tip .sig{margin-top:6px;color:var(--br);white-space:normal}
details summary{cursor:pointer;margin-top:8px}
.mono{font-family:ui-monospace,Consolas,monospace;font-size:12px}
</style></head><body>

<div class="top">
  <div><h1>NIFTY EMA Breakout - Hedged Spreads</h1>
    <p class="sub">100 EMA breakout on the NIFTY index, traded as ATM option spreads (one leg sold, one bought) in the current 4 expiries - paper trading</p></div>
  <div class="sp"></div>
  <span class="pill" id="p_mkt">-</span>
  <span class="pill" id="p_tok">-</span>
  <span class="pill" id="p_run">-</span>
  <button class="go" id="b_start">Start</button>
  <button class="stop" id="b_stop">Stop</button>
</div>
<nav class="tabs" id="tabs">
  <button data-tab="dash" class="on">Dashboard</button>
  <button data-tab="positions">Positions</button>
  <button data-tab="report">Trade Report</button>
  <button data-tab="activity">Activity</button>
  <button data-tab="settings">Settings</button>
</nav>
<div class="statusline" id="statusline">-</div>

<main>
<!-- DASHBOARD -->
<section class="panel on" id="p-dash">
  <div class="note">Paper trading only - nothing is sent to the broker. It starts by itself when launched from NIFTY Trader. Stop blocks new spreads; open ones still close when the index signal exits.</div>
  <div id="vixbanner"></div>
  <div class="grid">
    <div class="card"><div class="k">INDEX SIGNAL</div><div class="v" id="d_sig">-</div><div class="hint" id="d_sig2">-</div></div>
    <div class="card"><div class="k">NIFTY (LAST CLOSED CANDLE)</div><div class="v" id="d_ema">-</div><div class="hint" id="d_ema2">-</div></div>
    <div class="card"><div class="k">OPEN SPREADS</div><div class="v" id="d_open">-</div><div class="hint" id="d_open2">-</div></div>
    <div class="card"><div class="k">TODAY'S P&amp;L</div><div class="v" id="d_pnl">-</div><div class="hint" id="d_pnl2">-</div></div>
  </div>
  <div class="card" style="margin-bottom:16px">
    <h3 id="ch_title">NIFTY 50</h3>
    <div class="legend" id="ch_legend"></div>
    <div class="chart" id="ch"></div>
    <details><summary class="hint">Show the last 20 candles as a table</summary><div class="tw" id="ch_table"></div></details>
  </div>
  <div class="two">
    <div class="card"><h3>OPEN SPREADS</h3><div class="tw" id="d_pos"></div></div>
    <div class="card"><h3>IF A SIGNAL FIRED NOW</h3><div class="tw" id="d_prev"></div></div>
  </div>
  <div class="two">
    <div class="card"><h3>SIGNALS</h3><div class="tw" id="d_sigs"></div></div>
    <div class="card"><h3>RECENT ACTIVITY</h3><div class="tw" id="d_ev"></div></div>
  </div>
</section>

<!-- POSITIONS -->
<section class="panel" id="p-positions">
  <div class="bar">
    <span class="big" id="pos_total">-</span><div class="sp"></div>
    <a href="/api/positions.csv" class="btn sm" download>Download for Excel</a>
    <button class="sm danger" id="b_flat">Close all</button>
  </div>
  <div class="card tw" id="pos_table"></div>
  <p class="hint">A spread is valued at what closing it costs now: the sold leg bought back at the ask, the bought leg sold at the bid. Close uses the live quote when it is under 30 s old; otherwise the last mark, and says so.</p>
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
  <div class="card" style="margin-bottom:16px"><h3>CUMULATIVE REALIZED P&amp;L</h3><div id="r_chart"></div></div>
  <div class="grid" id="r_break"></div>
  <div class="card scroll"><div id="r_table"></div></div>
  <p class="hint">Clear and Wipe never destroy anything: removed trades are moved to trades_removed.jsonl in this strategy's data folder.</p>
</section>

<!-- ACTIVITY -->
<section class="panel" id="p-activity">
  <div class="bar">
    <select id="a_kind"><option value="">Every kind</option></select>
    <button class="sm ghost" id="a_refresh">Refresh</button>
    <span class="hint">Everything since this strategy was first started - kept on disk across restarts.</span>
  </div>
  <div class="card scroll"><div id="a_table"></div></div>
  <div style="margin-top:10px"><button class="sm ghost" id="a_more">Load older</button> <span class="hint" id="a_note"></span></div>
</section>

<!-- SETTINGS -->
<section class="panel" id="p-settings">
  <div class="card">
    <h3>INDEX SIGNAL - THE PINE SCRIPT INPUTS</h3>
    <div class="f">
      <div class="fl"><label>Candle length (the chart timeframe)</label><select id="c_interval"></select></div>
      <div class="fl"><label>Entry EMA length</label><input id="c_ema_entry" type="number"></div>
      <div class="fl"><label>Stop-loss EMA length</label><input id="c_ema_stop" type="number"></div>
      <div class="fl"><label>Lookback (bars on one side first)</label><input id="c_lookback" type="number"></div>
      <div class="fl"><label>Stop loss % (on the index close)</label><input id="c_stop_pct" type="number" step="0.1"></div>
      <div class="fl"><label>Take profit % (on the index close)</label><input id="c_target_pct" type="number" step="0.1"></div>
    </div>
    <p class="hint">Changing the candle length, an EMA or the lookback rebuilds the signal from history (history is never traded), so it is refused while spreads are open.</p>
  </div>
  <div class="card mt">
    <h3>OPTION TRADE</h3>
    <div class="grp"><label>Expiries - the current 4, rolling forward as each one ends</label><div class="chips" id="s_slots"></div></div>
    <div class="grp"><label>Spread</label><div class="mode">
      <div class="row"><label class="chip" style="margin:0"><input type="radio" name="spread" value="credit" id="sp_credit"> Credit - SELL ATM, BUY the hedge</label>
        <span>long signal: sell ATM PE + buy a lower PE &middot; short signal: sell ATM CE + buy a higher CE</span></div>
      <div class="row"><label class="chip" style="margin:0"><input type="radio" name="spread" value="debit" id="sp_debit"> Debit - BUY ATM, SELL further out</label>
        <span>long signal: buy ATM CE + sell a higher CE &middot; short signal: buy ATM PE + sell a lower PE</span></div>
    </div></div>
    <div class="f">
      <div class="fl"><label>Strike step</label><select id="c_strike_step"><option value="50">50 (every NIFTY strike)</option><option value="100">100</option></select></div>
      <div class="fl"><label>Hedge distance (strikes from ATM)</label><input id="c_hedge_strikes" type="number"></div>
      <div class="fl"><label>Lots per spread</label><input id="c_lots" type="number"></div>
      <div class="fl"><label>Expiry-day exit time (HH:MM)</label><input id="c_expiry_exit" placeholder="15:15"></div>
      <div class="fl"><label>Spread take profit, % of its max profit (0 = off)</label><input id="c_spread_tp_pct" type="number" step="1"></div>
      <div class="fl"><label>Spread stop, % of its max loss (0 = off)</label><input id="c_spread_sl_pct" type="number" step="1"></div>
    </div>
    <div class="grp mt"><label class="chip" id="chip_roll" style="display:inline-flex"><input type="checkbox" id="c_roll"> Roll: when a spread's expiry ends and the signal still holds, open one in the next expiry</label></div>
    <p class="hint" id="s_note"></p>
    <div class="bar" style="margin:16px 0 0">
      <button class="go" id="b_save">Save settings</button>
      <button class="ghost" id="b_revert">Discard changes</button>
    </div>
  </div>
  <div class="card mt"><h3>BROKER</h3><div id="s_tok" class="hint"></div></div>
</section>
</main>

<script>
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const num=(n,d)=>n==null||isNaN(n)?'-':Number(n).toFixed(d==null?2:d);
const inr=(n,d)=>n==null||isNaN(n)?'-':(n<0?'-':'')+'₹'+Math.abs(Number(n)).toLocaleString('en-IN',{minimumFractionDigits:d==null?2:d,maximumFractionDigits:d==null?2:d});
const inrShort=v=>{const a=Math.abs(v),s=v<0?'-':'';return a>=1e5?s+'₹'+(a/1e5).toFixed(a>=1e6?0:1)+'L':a>=1e3?s+'₹'+(a/1e3).toFixed(a>=1e4?0:1)+'k':s+'₹'+a.toFixed(0);};
const pts=v=>v==null||isNaN(v)?'-':Number(v).toLocaleString('en-IN',{minimumFractionDigits:2,maximumFractionDigits:2});
const cls=n=>n>0?'g':(n<0?'r':'');
const view=v=>v==='LONG'?'<span class="tag bull">BULL</span>':(v==='SHORT'?'<span class="tag bear">BEAR</span>':'<span class="tag flat">FLAT</span>');
const table=(head,rows,empty)=>rows.length?'<table><thead><tr>'+head.map(h=>'<th>'+h+'</th>').join('')+'</tr></thead><tbody>'+rows.join('')+'</tbody></table>':'<div class="empty">'+empty+'</div>';
function setHTML(el,html){if(el&&el.__h!==html){el.innerHTML=html;el.__h=html;}}
async function post(u,b){const r=await fetch(u,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b||{})});
 const d=await r.json().catch(()=>({}));if(!r.ok)throw new Error(d.error||('failed ('+r.status+')'));return d;}
async function get(u){const r=await fetch(u);if(!r.ok)throw new Error('failed ('+r.status+')');return r.json();}
const store={get(k){try{return localStorage.getItem(k);}catch(e){return null;}},set(k,v){try{localStorage.setItem(k,v);}catch(e){}}};
const REASON={EMA_STOP:'closed through the stop EMA',STOP:'index stop-loss %',TARGET:'index take-profit %',
  EXPIRY_DAY:'expiry-day exit',EXPIRED:'expired while the app was off',SPREAD_TARGET:'spread take-profit',
  SPREAD_STOP:'spread stop',MANUAL:'closed by hand',MANUAL_LAST_MARK:'closed by hand at the last mark',SIGNAL_FLAT:'the index signal is flat'};
const ord=k=>['1st','2nd','3rd','4th'][k-1]||k+'th';
const dteTxt=d=>d==null?'':(d<=0?'today':(d===1?'1 day':d+' days'));

/* ---------- tabs ---------- */
let TAB='dash';
function showTab(t){TAB=t;store.set('eh_tab',t);
  $$('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.tab===t));
  $$('.panel').forEach(p=>p.classList.toggle('on',p.id==='p-'+t));
  if(t==='report')loadReport(); if(t==='activity')loadEvents(true); if(t==='dash')drawChart();}
$('#tabs').onclick=e=>{const b=e.target.closest('button[data-tab]');if(b)showTab(b.dataset.tab);};

/* ---------- legs ---------- */
function legsCell(p,key){return p.legs.map(l=>'<span class="'+(l.role==='SELL'?'r':'g')+'">'+l.role+'</span> <b>'+esc(Math.round(l.strike))+'</b> '+esc(l.opt_type)+
  ' <span class="hint">@</span> '+num(l.entry)+(key&&l[key]!=null?' <span class="hint">&rarr;</span> '+num(l[key]):'')).join('<br>');}
function netCell(n){return n==null?'-':(n>=0?'credit ':'debit ')+num(Math.abs(n));}

/* ---------- live state ---------- */
let S=null,chT=null;
async function poll(){
  try{S=await get('/api/state');}catch(e){$('#statusline').textContent='cannot reach the strategy: '+e.message;return;}
  {const vx=S.vix||{},lim=vx.limit>0?vx.limit:null;let vh;
   const box=(c,t)=>'<div class="note" style="border-left-color:'+c+';background:'+c+'1a">'+t+'</div>';
   if(!lim)vh=box('#94a3b8','<b>VIX kill switch: OFF</b> (limit 0 in NIFTY Trader &rarr; VIX limit).');
   else if(vx.kill)vh=box('#ef4444','<b>VIX KILL SWITCH ON</b> - India VIX '+esc(vx.value)+' is above the '+esc(lim)+' limit. No new spreads, and every open spread is closed during market hours. New spreads are allowed again once VIX is at or below '+esc(lim)+'.');
   else vh=box('#22c55e','<b>VIX kill switch: ACTIVE</b> - limit India VIX '+esc(lim)+'. Above it: no new spreads and all open spreads are closed. '+(vx.value!=null?'Now: India VIX '+esc(vx.value)+' at '+esc(vx.at)+'.':'Current VIX: '+esc(vx.note==='not checked yet'?'checking...':vx.note)+'.')+' Change the limit in NIFTY Trader &rarr; VIX limit.');
   const vb=$('#vixbanner');if(vb&&vb.dataset.h!==vh){vb.innerHTML=vh;vb.dataset.h=vh;}}
  const s=S,c=s.cfg,g=s.sig||{},ind=s.ind||{};
  $('#p_mkt').textContent=s.market;
  $('#p_tok').textContent='token '+s.token.human; $('#p_tok').className='pill '+(s.token.configured&&!s.token.expired?'on':'off');
  $('#p_run').textContent=s.running?'RUNNING':'STOPPED'; $('#p_run').className='pill '+(s.running?'on':'off');
  $('#b_start').disabled=s.running; $('#b_stop').disabled=!s.running;
  $('#statusline').textContent=s.status+(s.spot?'   |   NIFTY spot '+pts(s.spot):'');

  /* cards */
  $('#d_sig').innerHTML=g.side?view(g.side)+' <span style="font-size:15px">since '+esc(String(g.at||'').slice(5))+'</span>':'FLAT';
  if(g.side){
    const ex=g.side==='LONG'?'a close below':'a close above';
    $('#d_sig2').textContent='entry close '+pts(g.entry)+' - exits on '+ex+' the '+c.ema_stop+' EMA'+(ind.ema_s!=null?' ('+pts(ind.ema_s)+')':'')+
      ', stop '+pts(g.stop)+', target '+pts(g.target);
  }else if(ind.armed){
    $('#d_sig2').textContent=(ind.armed==='LONG'?ind.run_below+' closes below':ind.run_above+' closes above')+' the '+c.ema_entry+' EMA - armed: the next close '+
      (ind.armed==='LONG'?'above it goes LONG':'below it goes SHORT');
  }else{
    const run=Math.max(ind.run_below||0,ind.run_above||0);
    $('#d_sig2').textContent=ind.t?'needs '+c.lookback+' closes on one side of the '+c.ema_entry+' EMA, then a cross - '+run+' so far '+
      ((ind.run_below||0)>=(ind.run_above||0)?'below':'above'):'candles: '+s.candle_note;
  }
  $('#d_ema').textContent=ind.close!=null?pts(ind.close):'-';
  $('#d_ema2').textContent=ind.t?(c.interval+'-min candle '+String(ind.at).slice(11)+' - EMA '+c.ema_entry+' '+pts(ind.ema_e)+', EMA '+c.ema_stop+' '+pts(ind.ema_s)):'candles: '+s.candle_note;
  $('#d_open').textContent=s.positions.length;
  $('#d_open2').textContent=s.positions.length?('open P&L '+inr(s.open_pnl)+' - most they can lose '+inr(s.open_risk,0)):
    (s.pending?'opening spreads now...':'expiries '+c.slots.map(ord).join(', ')+' - '+c.spread+' spreads, hedge '+c.hedge_strikes*c.strike_step+' pts');
  $('#d_pnl').textContent=inr(s.today_pnl); $('#d_pnl').className='v '+cls(s.today_pnl);
  $('#d_pnl2').textContent=s.today_trades+' closed today - all time '+inr(s.realised)+' over '+s.all_trades+' spreads';

  setHTML($('#d_pos'),table(['Expiry','Signal','Legs','Net','P&amp;L'],s.positions.map(p=>
    '<tr><td>'+esc(p.expiry)+' <span class="hint">'+dteTxt(p.dte)+'</span></td><td>'+view(p.view)+'</td><td>'+legsCell(p,'mark')+'</td><td>'+netCell(p.net)+'</td><td class="'+cls(p.pnl)+'"><b>'+inr(p.pnl)+'</b></td></tr>'),
    s.pending?'Opening spreads for the new signal...':'No open spreads.'));
  setHTML($('#d_prev'),s.positions.length?'<div class="empty">Spreads are open - this preview returns once they close.</div>':
    table(['Expiry','If','Legs (fill price)','Net','Max profit','Max loss'],[].concat(...s.preview.map(r=>['LONG','SHORT'].map((v,j)=>{
      const pl=r[v],ex='<td rowspan="2">'+ord(r.slot)+' &middot; '+esc(r.expiry)+'<br><span class="hint">'+dteTxt(r.dte)+'</span></td>';
      const head=(j===0?ex:'')+'<td>'+view(v)+'</td>';
      if(!pl)return '<tr>'+head+'<td colspan="4" class="hint wrap">'+esc(r.note?'option chain unavailable: '+r.note:'waiting for the option chain')+'</td></tr>';
      if(pl.error)return '<tr>'+head+'<td colspan="4" class="hint wrap">'+esc(pl.error)+'</td></tr>';
      return '<tr>'+head+'<td>'+legsCell(pl)+'</td><td>'+netCell(pl.net)+'</td><td class="g">'+inr(pl.max_profit,0)+'</td><td class="r">'+inr(pl.max_loss,0)+'</td></tr>';}))),
      s.running?'Waiting for option chains (refreshed one expiry every 20 s while the market is open).':'Press Start to preview.'));
  setHTML($('#d_sigs'),table(['Candle','Signal','NIFTY','What happened'],(s.signals||[]).map(x=>
    '<tr><td class="mono">'+esc(x.at)+'</td><td>'+(x.kind==='EXIT'?'<span class="tag flat">EXIT '+esc(x.side==='LONG'?'BULL':'BEAR')+'</span>':view(x.kind))+'</td><td>'+pts(x.close)+'</td>'+
    '<td class="wrap">'+(x.reason?esc(REASON[x.reason]||x.reason)+' - ':'')+esc(x.note)+'</td></tr>'),'No signals yet - they appear here and on the chart.'));
  setHTML($('#d_ev'),eventRows(s.events));

  /* positions tab */
  $('#pos_total').textContent='Open P&L: '+inr(s.open_pnl); $('#pos_total').className='big '+cls(s.open_pnl);
  setHTML($('#pos_table'),table(['Expiry','Signal','Legs (entry → now)','Opened','Net at entry','Net now','Qty','Open P&amp;L','Max profit','Max loss','Price age',''],s.positions.map(p=>
    '<tr><td>'+ord(p.slot)+' &middot; '+esc(p.expiry)+'<br><span class="hint">'+dteTxt(p.dte)+(p.kind==='roll'?' &middot; rolled in':'')+'</span></td><td>'+view(p.view)+'</td>'+
    '<td>'+legsCell(p,'mark')+'</td><td class="mono">'+esc(String(p.opened||'').slice(5,16))+'</td><td>'+netCell(p.net)+'</td><td>'+netCell(p.net_now)+'</td><td>'+esc(p.qty)+'</td>'+
    '<td class="'+cls(p.pnl)+'"><b>'+inr(p.pnl)+'</b></td><td class="g">'+inr(p.max_profit,0)+'</td><td class="r">'+inr(p.max_loss,0)+'</td>'+
    '<td class="hint">'+(p.quote_age==null?'-':p.quote_age+'s')+'</td>'+
    '<td><button class="sm danger" data-close="'+esc(p.id)+'" data-name="'+esc(p.expiry)+'">Close</button></td></tr>'),'No open spreads.'));

  paintSettings(s);
  const key=s.last_bar_t+'|'+c.interval+'|'+c.ema_entry+'|'+c.ema_stop+'|'+(s.signals||[]).length;
  if(key!==chT){chT=key;loadChart();}
}
function eventRows(evs){return table(['Time','Kind','What happened'],(evs||[]).map(e=>
  '<tr><td class="mono">'+esc(e.ts||e.at)+'</td><td><span class="tag" style="background:var(--p2)">'+esc(e.kind)+'</span></td><td class="wrap">'+esc(e.msg)+'</td></tr>'),'Nothing yet.');}

/* ---------- NIFTY + EMA chart ---------- */
let CH=null;
async function loadChart(){try{CH=await get('/api/chart?n=150');}catch(e){return;}drawChart();}
const fmtAx=v=>Number(v).toLocaleString('en-IN',{maximumFractionDigits:0});
function niceStep(range){const raw=range/4||1,p=Math.pow(10,Math.floor(Math.log10(raw))),m=raw/p;return (m<=1?1:m<=2?2:m<=5?5:10)*p;}
function drawChart(){
  const el=$('#ch'),d=CH;
  if(!d||TAB!=='dash')return;
  const SER=[{k:'c',name:'NIFTY',col:'var(--s1)'},{k:'ee',name:'EMA '+d.ema_entry,col:'var(--s2)',role:'entry'},{k:'es',name:'EMA '+d.ema_stop,col:'var(--s3)',role:'stop'}];
  $('#ch_title').textContent='NIFTY 50 - '+d.interval+'-MINUTE CANDLES'+(d.bars.length?' - LAST '+d.bars.length:'');
  setHTML($('#ch_legend'),SER.map(s=>'<span><i style="border-color:'+s.col+'"></i>'+esc(s.name)+(s.role?' ('+s.role+')':'')+'</span>').join('')+
    '<span>&#9650; long &middot; &#9660; short &middot; &#9670; exit &middot; hollow = not traded</span>');
  const bars=d.bars,n=bars.length;
  if(!n){setHTML(el,'<div class="empty">'+esc('Candles: '+(d.note||'not loaded yet'))+'</div>');
    setHTML($('#ch_table'),'<div class="empty">No candles yet.</div>');return;}
  const W=Math.max(320,el.clientWidth||900),H=300,L=64,R=118,T=14,B=28;
  const vals=[];bars.forEach(b=>SER.forEach(s=>{if(b[s.k]!=null)vals.push(b[s.k]);}));
  let lo=Math.min(...vals),hi=Math.max(...vals);if(hi-lo<10){lo-=5;hi+=5;}
  const st=niceStep(hi-lo);lo=Math.floor(lo/st)*st;hi=Math.ceil(hi/st)*st;
  const X=i=>L+(W-L-R)*(n<2?0.5:i/(n-1)),Y=v=>T+(H-T-B)*(1-(v-lo)/(hi-lo));
  let g='';
  for(let v=lo;v<=hi+st/2;v+=st)g+='<line class="grid" x1="'+L+'" x2="'+(W-R)+'" y1="'+Y(v).toFixed(1)+'" y2="'+Y(v).toFixed(1)+'"/><text class="ax" x="'+(L-8)+'" y="'+(Y(v)+4).toFixed(1)+'" text-anchor="end">'+fmtAx(v)+'</text>';
  for(let i=1;i<n;i++)if(bars[i].day!==bars[i-1].day){const x=((X(i-1)+X(i))/2).toFixed(1);g+='<line class="zero" x1="'+x+'" x2="'+x+'" y1="'+T+'" y2="'+(H-B)+'"/>';}
  const k=Math.min(6,n);let xl='',prevDay=null;
  for(let j=0;j<k;j++){const i=k<2?0:Math.round(j*(n-1)/(k-1)),b=bars[i],a=j===0?'start':(j===k-1?'end':'middle');
    xl+='<text class="ax" x="'+X(i).toFixed(1)+'" y="'+(H-8)+'" text-anchor="'+a+'">'+esc((b.day!==prevDay?b.day+' ':'')+b.hm)+'</text>';prevDay=b.day;}
  const path=key=>{let s='',on=false;bars.forEach((b,i)=>{const v=b[key];if(v==null){on=false;return;}s+=(on?'L':'M')+X(i).toFixed(1)+' '+Y(v).toFixed(1)+' ';on=true;});return s;};
  const lines=[SER[1],SER[2],SER[0]].map(s=>'<path d="'+path(s.k)+'" fill="none" stroke="'+s.col+'" stroke-width="2" stroke-linejoin="round"/>').join('');
  const idx={};bars.forEach((b,i)=>idx[b.t]=i);
  const MK={};let marks='';
  (d.markers||[]).forEach(m=>{const i=idx[m.t];if(i==null)return;(MK[i]=MK[i]||[]).push(m);
    const x=X(i),y=Y(bars[i].c),done=m.note==='traded'||/^closing/.test(m.note||'');
    const fill=done?'var(--br)':'var(--panel)',sh=m.kind==='LONG'?[[x,y+7],[x-6,y+17],[x+6,y+17]]:m.kind==='SHORT'?[[x,y-7],[x-6,y-17],[x+6,y-17]]:[[x,y-6],[x+6,y],[x,y+6],[x-6,y]];
    marks+='<polygon points="'+sh.map(p=>p[0].toFixed(1)+','+p[1].toFixed(1)).join(' ')+'" fill="'+fill+'" stroke="var(--br)" stroke-width="1.5" paint-order="stroke"/>';});
  let lab=SER.map(s=>{let i=n-1;while(i>=0&&bars[i][s.k]==null)i--;return i<0?null:{s,v:bars[i][s.k],y:Y(bars[i][s.k])};}).filter(Boolean).sort((a,b)=>a.y-b.y);
  for(let i=1;i<lab.length;i++)if(lab[i].y-lab[i-1].y<14)lab[i].y=lab[i-1].y+14;
  const over=lab.length?lab[lab.length-1].y-(H-B):0;if(over>0)lab.forEach(l=>l.y-=over);
  const dl=lab.map(l=>'<line x1="'+(W-R+6)+'" x2="'+(W-R+18)+'" y1="'+l.y.toFixed(1)+'" y2="'+l.y.toFixed(1)+'" stroke="'+l.s.col+'" stroke-width="2"/>'+
    '<text class="dl" x="'+(W-R+22)+'" y="'+(l.y+4).toFixed(1)+'">'+esc(l.s.k==='c'?pts(l.v):l.s.name)+'</text>').join('');
  el.innerHTML='<svg id="ch_svg" tabindex="0" width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'" role="img" aria-label="NIFTY close with its two EMAs; arrow keys move through the candles">'+
    g+lines+marks+dl+xl+'<line class="xh" id="ch_x" x1="-9" x2="-9" y1="'+T+'" y2="'+(H-B)+'"/>'+
    '<rect x="'+L+'" y="0" width="'+(W-L-R)+'" height="'+H+'" fill="transparent"/></svg><div class="tip" id="ch_tip"></div>';
  el.__h=null;
  const svg=$('#ch_svg'),tip=$('#ch_tip'),xh=$('#ch_x');let cur=n-1;
  function show(i){cur=Math.max(0,Math.min(n-1,i));const b=bars[cur],x=X(cur);
    xh.setAttribute('x1',x);xh.setAttribute('x2',x);
    tip.innerHTML='<div class="t">'+esc(b.day+' '+b.hm)+'</div>'+SER.map(s=>'<div class="row"><i style="border-color:'+s.col+'"></i><b>'+(b[s.k]==null?'-':pts(b[s.k]))+'</b><span class="hint">'+esc(s.name)+'</span></div>').join('')+
      (MK[cur]||[]).map(m=>'<div class="sig">'+esc((m.kind==='EXIT'?'EXIT '+(m.side==='LONG'?'bull':'bear')+' - '+(REASON[m.reason]||m.reason||''):m.kind+' signal')+' - '+(m.note||''))+'</div>').join('');
    tip.style.display='block';const w=tip.offsetWidth;tip.style.left=(x+14+w>W?x-14-w:x+14)+'px';}
  function hide(){tip.style.display='none';xh.setAttribute('x1',-9);xh.setAttribute('x2',-9);}
  svg.addEventListener('pointermove',e=>{const r=svg.getBoundingClientRect();show(Math.round((e.clientX-r.left-L)/(W-L-R)*(n-1)));});
  svg.addEventListener('pointerleave',()=>{if(document.activeElement!==svg)hide();});
  svg.addEventListener('focus',()=>show(cur));svg.addEventListener('blur',hide);
  svg.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'){show(cur-1);e.preventDefault();}else if(e.key==='ArrowRight'){show(cur+1);e.preventDefault();}});
  setHTML($('#ch_table'),table(['Candle','NIFTY close','EMA '+d.ema_entry,'EMA '+d.ema_stop],bars.slice(-20).reverse().map(b=>
    '<tr><td class="mono">'+esc(b.day+' '+b.hm)+'</td><td>'+pts(b.c)+'</td><td>'+pts(b.ee)+'</td><td>'+pts(b.es)+'</td></tr>'),'No candles yet.'));
}
window.addEventListener('resize',()=>{if(TAB==='dash')drawChart();if(TAB==='report'&&REPORT)equityChart($('#r_chart'),REPORT.stats.series);});

/* ---------- trade report ---------- */
function equityChart(el,series){
  if(!series.length){setHTML(el,'<div class="empty">No closed spreads yet - the curve starts at the first exit.</div>');return;}
  const W=Math.max(320,el.clientWidth||900),H=260,L=72,R=18,T=14,B=30,n=series.length;
  let lo=Math.min(0,...series.map(p=>p.cum)),hi=Math.max(0,...series.map(p=>p.cum));
  if(lo===hi){lo-=100;hi+=100;}
  const st=niceStep(hi-lo);lo=Math.floor(lo/st)*st;hi=Math.ceil(hi/st)*st;
  const X=i=>L+(W-L-R)*(i/n),Y=v=>T+(H-T-B)*(1-(v-lo)/(hi-lo));
  const col=series[n-1].cum>=0?'#22c55e':'#ef4444';
  let g='';for(let v=lo;v<=hi+st/2;v+=st)g+='<line class="grid" x1="'+L+'" x2="'+(W-R)+'" y1="'+Y(v).toFixed(1)+'" y2="'+Y(v).toFixed(1)+'"/><text class="ax" x="'+(L-8)+'" y="'+(Y(v)+4).toFixed(1)+'" text-anchor="end">'+inrShort(v)+'</text>';
  const pp=[[X(0),Y(0)]].concat(series.map((p,i)=>[X(i+1),Y(p.cum)]));
  const line=pp.map((p,i)=>(i?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1)).join(' ');
  const area=line+' L'+X(n).toFixed(1)+' '+Y(0).toFixed(1)+' L'+X(0).toFixed(1)+' '+Y(0).toFixed(1)+' Z';
  const k=Math.min(n,6);let xl='';const seen={};
  for(let j=0;j<=k;j++){const i=Math.round(j*n/k);if(seen[i])continue;seen[i]=1;xl+='<text class="ax" x="'+X(i).toFixed(1)+'" y="'+(H-8)+'" text-anchor="middle">#'+i+'</text>';}
  const dots=n<=200?series.map((p,i)=>'<circle class="dot" stroke="'+(p.pnl>=0?'#22c55e':'#ef4444')+'" cx="'+X(i+1).toFixed(1)+'" cy="'+Y(p.cum).toFixed(1)+'" r="4"><title>#'+(i+1)+'  '+esc(p.contract)+'  '+esc(p.closed)+'\nspread '+inr(p.pnl)+'   cumulative '+inr(p.cum)+'</title></circle>').join(''):'';
  el.innerHTML='<svg width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'">'+g+
    '<line class="zero" x1="'+L+'" x2="'+(W-R)+'" y1="'+Y(0).toFixed(1)+'" y2="'+Y(0).toFixed(1)+'"/>'+
    '<path d="'+area+'" fill="'+col+'" fill-opacity=".13"/><path d="'+line+'" fill="none" stroke="'+col+'" stroke-width="2"/>'+dots+xl+'</svg>';
  el.__h=null;
}
function statCard(k,v,c,h){return '<div class="card"><div class="k">'+k+'</div><div class="v '+(c||'')+'">'+v+'</div>'+(h?'<div class="hint">'+h+'</div>':'')+'</div>';}
function breakCard(title,g){const ks=Object.keys(g||{}).sort();return '<div class="card"><h3>'+title+'</h3>'+
  table(['','Spreads','Win rate','P&amp;L'],ks.map(k=>'<tr><td>'+esc(k)+'</td><td>'+g[k].n+'</td><td>'+(g[k].n?Math.round(g[k].wins/g[k].n*100):0)+'%</td><td class="'+cls(g[k].pnl)+'">'+inr(g[k].pnl,0)+'</td></tr>'),'-')+'</div>';}
let REPORT=null;
async function loadReport(){
  try{REPORT=await get('/api/history');}catch(e){$('#r_total').textContent=e.message;return;}
  const st=REPORT.stats;
  $('#r_total').textContent='Realized P&L: '+inr(st.total); $('#r_total').className='big '+cls(st.total);
  setHTML($('#r_stats'),statCard('SPREADS',st.trades,'',st.wins+' won / '+st.losses+' lost')+
    statCard('WIN RATE',st.win_rate+'%',st.win_rate>=50?'g':'r')+
    statCard('AVG WIN',inr(st.avg_win,0),'g','best '+inr(st.best,0))+
    statCard('AVG LOSS',inr(st.avg_loss,0),st.losses?'r':'','worst '+inr(st.worst,0))+
    statCard('PROFIT FACTOR',st.profit_factor==null?'-':(st.profit_factor==='inf'?'∞':st.profit_factor),
      st.profit_factor==null?'':((st.profit_factor==='inf'||st.profit_factor>=1)?'g':'r'),st.profit_factor==='inf'?'no losing spread yet':'gross wins / gross losses')+
    statCard('MAX DRAWDOWN',inr(st.max_drawdown,0),st.max_drawdown<0?'r':'','deepest fall from a peak'));
  equityChart($('#r_chart'),st.series);
  setHTML($('#r_break'),breakCard('BY SIGNAL',st.by_view)+breakCard('BY EXPIRY SLOT',st.by_slot)+breakCard('BY EXIT REASON',st.by_reason));
  const rows=REPORT.rows.slice().reverse();
  setHTML($('#r_table'),table(['<input type="checkbox" id="r_all">','Closed','Expiry','Signal','Legs (entry → exit)','Net in','Net out','Qty','P&amp;L','Why'],rows.map(t=>
    '<tr><td><input type="checkbox" class="r_chk" value="'+esc(t.id)+'"></td><td class="mono">'+esc(String(t.closed||'').slice(0,16))+'</td><td>'+esc(t.expiry)+'</td>'+
    '<td>'+view(t.view)+'</td><td>'+legsCell(t,'exit')+'</td><td>'+netCell(t.net)+'</td><td>'+netCell(t.net_exit)+'</td><td>'+esc(t.qty)+'</td>'+
    '<td class="'+cls(t.pnl)+'"><b>'+inr(t.pnl,0)+'</b></td><td class="hint wrap">'+esc(REASON[t.reason]||t.reason)+(t.exit_src==='last mark'?' (last mark)':'')+'</td></tr>'),'No closed spreads yet.'));
}
document.addEventListener('change',e=>{if(e.target.id==='r_all')$$('.r_chk').forEach(c=>c.checked=e.target.checked);});
$('#b_clear').onclick=async()=>{const ids=$$('.r_chk').filter(c=>c.checked).map(c=>c.value);
  if(!ids.length){alert('Tick the trades to clear first.');return;}
  if(!confirm('Remove '+ids.length+' trade(s) from the report? They are moved to trades_removed.jsonl, not destroyed.'))return;
  try{await post('/api/history/clear',{ids});}catch(e){alert(e.message);} loadReport();};
$('#b_wipe').onclick=async()=>{if(!confirm('Remove EVERY trade from the report?\n\nThey are moved to trades_removed.jsonl, not destroyed.'))return;
  try{await post('/api/history/wipe');}catch(e){alert(e.message);} loadReport();};

/* ---------- activity ---------- */
const KINDS=['entry','exit','signal','skip','roll','candles','config','control','report','token','api','day','boot','error'];
KINDS.forEach(k=>{const o=document.createElement('option');o.value=k;o.textContent=k;$('#a_kind').appendChild(o);});
let EV=[],evDone=false,evSeq=0;
async function loadEvents(reset){
  const my=++evSeq;
  if(reset){EV=[];evDone=false;}
  const before=EV.length?EV[EV.length-1].id:'';
  $('#a_more').disabled=true;
  try{const d=await get('/api/events?limit=200&kind='+encodeURIComponent($('#a_kind').value)+(before?'&before='+before:''));
    if(my!==evSeq)return;
    const seen=new Set(EV.map(e=>e.id));
    EV=EV.concat(d.rows.filter(e=>!seen.has(e.id)));evDone=d.rows.length<200;}catch(e){if(my!==evSeq)return;}
  setHTML($('#a_table'),eventRows(EV));
  $('#a_more').disabled=evDone; $('#a_note').textContent=EV.length+' shown'+(evDone?' - that is everything':'');
}
$('#a_kind').onchange=()=>loadEvents(true); $('#a_refresh').onclick=()=>loadEvents(true); $('#a_more').onclick=()=>loadEvents(false);

/* ---------- settings ---------- */
const NUMS=['ema_entry','ema_stop','lookback','stop_pct','target_pct','hedge_strikes','lots','spread_tp_pct','spread_sl_pct'];
let touched=false,slotKey='';
$('#p-settings').addEventListener('input',()=>{touched=true;chipsUI();});
$('#p-settings').addEventListener('change',()=>{touched=true;chipsUI();});
function chipsUI(){$$('#s_slots .chip,#chip_roll').forEach(ch=>{const i=ch.querySelector('input');ch.classList.toggle('on',i.checked);});
  $$('input[name=spread]').forEach(r=>r.parentElement.classList.toggle('on',r.checked));
  const step=Number($('#c_strike_step').value)||50,h=Number($('#c_hedge_strikes').value)||0,lot=S?S.lot:0,lots=Number($('#c_lots').value)||1;
  const cr=$('#sp_credit').checked;
  $('#s_note').textContent='Hedge = '+h+' strikes x '+step+' = '+(h*step)+' points. '+(cr?'Most a spread can lose = ('+(h*step)+' - credit) x ':'Most a spread can lose = the debit x ')+
    (lot?lot+' (lot) x '+lots+' lot'+(lots===1?'':'s')+'.':'the quantity.')+' The ATM strike is NIFTY spot rounded to the strike step when the spread opens.';}
function paintSettings(s){
  const iv=$('#c_interval');if(!iv.options.length)iv.innerHTML=s.intervals.map(m=>'<option value="'+m+'">'+m+' minute'+(m===1?'':'s')+'</option>').join('');
  const key=JSON.stringify(s.slots);
  if(key!==slotKey){const keep=touched?$$('#s_slots input').filter(b=>b.checked).map(b=>Number(b.value)):s.cfg.slots;slotKey=key;
    $('#s_slots').innerHTML=[1,2,3,4].map(k=>{const x=s.slots[k-1];return '<label class="chip"><input type="checkbox" value="'+k+'"'+(keep.includes(k)?' checked':'')+'> '+ord(k)+
      (x?' &middot; '+esc(x.expiry)+' <small>'+dteTxt(x.dte)+'</small>':' <small>(expiries load once the token works)</small>')+'</label>';}).join('');}
  $('#s_tok').textContent='Token '+s.token.human+' - from '+s.token.source+(s.token.client_id?' - client '+s.token.client_id:'')+
    '. Change it in NIFTY Trader\'s Broker token screen; this strategy restarts with it automatically.';
  if(touched){chipsUI();return;}
  const c=s.cfg;
  $$('#s_slots input').forEach(b=>b.checked=c.slots.includes(Number(b.value)));
  iv.value=c.interval;$('#c_strike_step').value=c.strike_step;$('#c_expiry_exit').value=c.expiry_exit;
  $('#sp_credit').checked=c.spread==='credit';$('#sp_debit').checked=c.spread==='debit';$('#c_roll').checked=!!c.roll;
  NUMS.forEach(k=>{const el=$('#c_'+k);if(el&&c[k]!=null)el.value=c[k];});
  chipsUI();
}
$('#b_save').onclick=async()=>{
  const b={};
  for(const k of NUMS){const el=$('#c_'+k);
    if(el.value.trim()===''){alert(el.closest('.fl').querySelector('label').textContent.trim()+' is empty.');el.focus();return;}
    b[k]=Number(el.value);}
  b.interval=Number($('#c_interval').value);b.strike_step=Number($('#c_strike_step').value);
  b.expiry_exit=$('#c_expiry_exit').value.trim();b.spread=$('#sp_debit').checked?'debit':'credit';b.roll=$('#c_roll').checked;
  b.slots=$$('#s_slots input').filter(x=>x.checked).map(x=>Number(x.value));
  try{await post('/api/config',b);touched=false;poll();}catch(e){alert(e.message);}
};
$('#b_revert').onclick=()=>{touched=false;slotKey='';poll();};

/* ---------- controls ---------- */
$('#b_start').onclick=async()=>{try{await post('/api/start');poll();}catch(e){alert(e.message);}};
$('#b_stop').onclick=async()=>{await post('/api/stop');poll();};
$('#b_flat').onclick=async()=>{if(!S||!S.positions.length){alert('No open spreads.');return;}
  if(!confirm('Close ALL '+S.positions.length+' open spreads now?\n\nThe index signal stays as it is; these are not re-opened.'))return;
  try{const d=await post('/api/flatten',{});poll();report(d);}catch(e){alert(e.message);}};
document.addEventListener('click',async e=>{const b=e.target.closest('[data-close]');if(!b)return;
  if(!confirm('Close the '+b.dataset.name+' spread now?'))return;
  try{const d=await post('/api/flatten',{id:b.dataset.close});poll();report(d);}catch(err){alert(err.message);}});
function report(d){const m=(d.closed||[]).filter(c=>c.reason==='MANUAL_LAST_MARK');
  if(m.length)alert('No fresh price for '+m.map(c=>c.expiry).join(', ')+' - closed at the last mark instead.');}

showTab(store.get('eh_tab')||'dash');
poll();setInterval(poll,3000);
setInterval(()=>{if(TAB==='report')loadReport();},20000);
</script></body></html>"""


# ─────────────────────────────────────────────────────────────────────────────
#  BOOT
# ─────────────────────────────────────────────────────────────────────────────
STATE.load()
STATE.autostart = True                  # launched = trading; Stop cancels it
threading.Thread(target=boot_loop, name="boot", daemon=True).start()
threading.Thread(target=engine_loop, name="engine", daemon=True).start()
log_event("boot", "ema-hedge app up (pid %d, DATA_DIR=%s)" % (os.getpid(), DATA_DIR))

import atexit                                                        # noqa: E402
import signal                                                        # noqa: E402

atexit.register(_graceful)
for _s in ("SIGTERM", "SIGINT"):
    if hasattr(signal, _s):
        try:
            signal.signal(getattr(signal, _s), lambda *a: (_graceful(), os._exit(0)))
        except (ValueError, OSError):
            pass


# ─────────────────────────────────────────────────────────────────────────────
#  MARGIN FOR NIFTY TRADER'S HOME SCREEN
#  hub_summary() is read by the hub (through its /__hub__/status call) to show
#  each strategy's margin on one screen.  Local arithmetic only - no API calls.
#    margin_used      Rs blocked by the open positions now
#    margin_next      Rs one new trade needs (lowest candidate), margin_next_max the highest
# ─────────────────────────────────────────────────────────────────────────────
ELM_INDEX_PCT, NAKED_SHORT_PCT = 0.0247, 0.0969     # fitted to a real Dhan quote (see credit spreads)


def _spread_margin(plan, spot):
    """Credit spread: SPAN (capped at max loss) + exposure on the short leg's
    notional, never above a naked short.  Debit spread: the premium paid."""
    qty, max_loss = _f(plan.get("qty")), _f(plan.get("max_loss"))
    if _f(plan.get("net")) <= 0:
        return max_loss
    notional = _f(spot) * qty
    return min(max(max_loss + ELM_INDEX_PCT * notional, max_loss), NAKED_SHORT_PCT * notional or max_loss)


def hub_summary():
    with STATE.lock:
        pos = list(STATE.positions)
        spot = STATE.spot
    used = sum(_spread_margin(p, spot or p.get("spot_entry")) for p in pos)
    # One signal opens a spread in each of the current expiries: add them up.
    per_view = {}
    try:
        for row in preview_rows(now_ist()):
            for view in ("LONG", "SHORT"):
                plan = row.get(view) or {}
                if plan.get("qty"):
                    per_view[view] = per_view.get(view, 0.0) + _spread_margin(plan, spot)
    except Exception:
        pass
    vals = sorted(v for v in per_view.values() if v > 0)
    return {"margin_used": round(used), "open": len(pos),
            "margin_next": round(vals[0]) if vals else None,
            "margin_next_max": round(vals[-1]) if vals else None,
            "basis": "hedged spreads in every current expiry: SPAN + exposure estimate"}


def _pnl_summary(margin_used):
    today = now_ist().strftime("%Y-%m-%d")
    with STATE.lock:
        hist = list(STATE.history)
        open_pnl = sum(_f(p.get("pnl")) for p in STATE.positions)
    rows_today = [h for h in hist if str(h.get("closed") or "").startswith(today)]
    return _pnl_pack(rows_today, hist, lambda r: _f(r.get("pnl")),
                     lambda r: _spread_margin(r, r.get("spot_entry") or STATE.spot), open_pnl, margin_used)


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
    app.run(host="127.0.0.1", port=int(_env("PORT", "5006")), threaded=True, use_reloader=False)
