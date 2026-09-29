"""
NIFTY Option 2-Level Cross + Momentum  -  ported from the TradingView strategy
=============================================================================

The Pine script ran on ONE option's chart, so `close` was that option's premium
and the levels (233 / 344) were premium levels.  This app runs that same logic
on many charts at once: every chosen expiry x side (CE, PE) x strike is its own
contract, with its own bars, momentum and position.  Strikes are multiples of
100 - a window of ATM +/- N strikes that follows NIFTY, or a list you type.  A
contract's strike never changes.  Only the daily trade cap and the open-position
cap are shared between contracts.  One option-chain call per expiry covers every
strike, so watching more strikes costs no extra broker calls.

Every closed trade is kept in data/trades.jsonl and every event in
data/events.jsonl - never trimmed - for the Trade Report and Activity tabs.

WHAT IT DOES

    entry   premium crosses UP through Level 2 (or Level 3), and momentum
            (close - close N bars ago) is above the threshold, and we are flat.
    exit    whichever comes first:
              * target      entry + target_ticks x tick, target picked from
                            yesterday's India VIX close
              * trail       highest premium since entry, minus trail %
              * push/fail   premium held above (entry + move) for N minutes,
                            then fell back through it

PAPER TRADING ONLY.  It places nothing with the broker.  It reads the option
chain and fills at the bid/ask you could actually have traded at.

THREE THINGS IN THE PINE SCRIPT WERE CONTRADICTORY.  They are settings here
rather than a silent choice, and the defaults follow what the code DID, not
what the comments said:

  1. "300 ticks = Rs 20" - a tick on NSE options is Rs 0.05, so 300 ticks is
     Rs 15.  The code used entryPrice + 20, i.e. 400 ticks.  Default: 20.0.
  2. Level 3's trailing stop was set to 15% on entry and 10% in the exit block,
     so 10% is what actually ran.  Both are exposed; L3 defaults to 10%.
  3. `profit = targetTicks` in Pine is in TICKS, so 800 was Rs 40 a unit, not
     800 points.  Shown in rupees everywhere in this app.

The secret key is gone: the Pine version fired webhook JSON at a relay, and
this app talks to Dhan directly with the access token the hub injects.
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
STATE_FILE = os.path.join(DATA_DIR, "level_cross_state.json")
RUNTIME_FILE = os.path.join(DATA_DIR, "runtime.json")
SCRIP_CACHE = os.path.join(DATA_DIR, "scrip_nifty.json")
# Append-only, never trimmed: every closed trade and every event, forever.
TRADES_FILE = os.path.join(DATA_DIR, "trades.jsonl")
TRADES_REMOVED_FILE = os.path.join(DATA_DIR, "trades_removed.jsonl")   # what Clear/Wipe took out
EVENTS_FILE = os.path.join(DATA_DIR, "events.jsonl")
EVENTS_MAX_BYTES = 20 * 1024 * 1024        # then rolled to events.<n>.jsonl - every archive kept

IST = timezone(timedelta(hours=5, minutes=30))
MKT_OPEN, MKT_CLOSE = dtime(9, 15), dtime(15, 30)
UNDERLYING_SCRIP, UNDERLYING_SEG = 13, "IDX_I"
VIX_SECURITY_ID, VIX_SEG = "21", "IDX_I"        # NSE "INDIA VIX", from the scrip master
TICK = 0.05                                      # NSE option tick, Rs


def now_ist():
    return datetime.now(IST)


def _f(x, d=0.0):
    try:
        v = float(x)
        return d if v != v or v in (float("inf"), float("-inf")) else v
    except (TypeError, ValueError):
        return d


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

    Every chosen expiry is one call per pass, and Dhan's limit is per CLIENT -
    the other strategies in NIFTY Trader draw on the same allowance.  So a 429
    widens the gap instead of retrying hard, and the gap shrinks back as calls
    succeed again."""
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
    return [str(x)[:10] for x in (r.get("data") or [])] if r.get("status") == "success" else []


def fetch_vix_prev_close():
    """Yesterday's India VIX close.  The Pine script used close[1] on a daily
    series, so today's own candle must be skipped even when it exists."""
    today = now_ist().date()
    r = call_dhan("charts/historical", {
        "securityId": VIX_SECURITY_ID, "exchangeSegment": VIX_SEG, "instrument": "INDEX",
        "fromDate": (today - timedelta(days=20)).isoformat(), "toDate": today.isoformat()})
    closes, stamps = r.get("close") or [], r.get("timestamp") or []
    if not closes:
        return None, (r.get("message") or "no data")
    for i in range(len(closes) - 1, -1, -1):
        try:
            d = datetime.fromtimestamp(int(stamps[i]), IST).date()
        except (TypeError, ValueError, IndexError, OSError):
            d = None
        if d is None or d < today:
            return _f(closes[i]), None
    return _f(closes[-1]), None


# ─────────────────────────────────────────────────────────────────────────────
#  SCRIP MASTER  -  for the lot size and the contract list
# ─────────────────────────────────────────────────────────────────────────────
SCRIP_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"


def load_scrip_lookup():
    today = now_ist().strftime("%Y-%m-%d")
    cached = read_json_safe(SCRIP_CACHE, default=None)
    if isinstance(cached, dict) and cached.get("date") == today and cached.get("map"):
        return cached["map"]
    try:
        import csv
        import io
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
                "lot": int(_f(row.get("SEM_LOT_UNITS"), 65)),
                "tick": _f(row.get("SEM_TICK_SIZE"), 5.0) / 100.0}
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


# ─────────────────────────────────────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────────────────────────────────────
STRIKE_STEP = 100          # contracts are traded at strikes in multiples of 100 only
MAX_EXPIRIES = 4           # each expiry costs one ~3 s option-chain call per pass
MAX_EACH_SIDE = 30         # ATM +/- 30 strikes = a 6,000-point window
MAX_LIST = 60              # strikes in "my own list" mode
KEEP_EXTRA = 2             # a strike drifting out of the window is kept 2 steps longer
GAP_FILL_BARS = 2          # up to 2 missed bars are filled flat; a longer gap restarts the series
BAR_MEMORY = 400           # closed bars kept in memory per contract

DEFAULTS = {
    "expiries": [], "opt_types": ["CE", "PE"],
    "strike_mode": "atm",              # "atm": ATM +/- N strikes, following NIFTY. "list": your strikes
    "strikes_each_side": 10,
    "strike_list": [],
    "level2": 233.0, "level3": 344.0,
    "mom_length": 14, "mom_threshold": 20.0,
    "trail_l2_pct": 15.0, "trail_l3_pct": 10.0,
    "move_rupees": 20.0,               # the Pine "300 tick" level, which was +20
    "confirm_minutes": 5.0,
    "bar_seconds": 60,                 # Pine bars; 1 minute matches a 1m chart
    "lots": 1,
    "vix_targets": [[12, 800], [15, 1000], [20, 1200], [None, 1400]],   # ticks
    "max_trades_per_day": 6,           # across every contract together
    "max_open": 2,                     # positions open at once, across every contract
}
_EXPIRY_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

# Checked on Save: the value must be a real number inside this range.
RANGES = {
    "level2": (0.05, 100000), "level3": (0.05, 100000),
    "mom_length": (1, 200), "mom_threshold": (0, 100000),
    "trail_l2_pct": (0.1, 99), "trail_l3_pct": (0.1, 99),
    "move_rupees": (0, 100000), "confirm_minutes": (0, 375),
    "bar_seconds": (5, 900), "lots": (1, 50),
    "max_trades_per_day": (1, 500), "max_open": (1, 100),
    "strikes_each_side": (0, MAX_EACH_SIDE),
}
LABELS = {
    "level2": "Level 2", "level3": "Level 3", "mom_length": "Momentum length",
    "mom_threshold": "Momentum threshold", "trail_l2_pct": "Trailing stop L2",
    "trail_l3_pct": "Trailing stop L3", "move_rupees": "Push level",
    "confirm_minutes": "Hold-above minutes", "bar_seconds": "Bar length",
    "lots": "Lots", "max_trades_per_day": "Max trades per day",
    "max_open": "Max open at once", "strikes_each_side": "Strikes each side of ATM",
}


def round_strike(x):
    """Nearest multiple of 100, halves rounding UP.  Python's round() is
    banker's rounding and would send 25050 down but 25150 up."""
    v = _f(x)
    if v <= 0:
        return 0.0
    return float(int(math.floor(v / STRIKE_STEP + 0.5)) * STRIKE_STEP)


def is_strike_step(x):
    v = _f(x)
    return v > 0 and abs(v / STRIKE_STEP - round(v / STRIKE_STEP)) < 1e-9


def _valid_vix_targets(v):
    try:
        rows = [[None if b is None else float(b), int(t)] for b, t in v]
        return rows if rows and rows[-1][0] is None else None
    except (TypeError, ValueError):
        return None


def parse_strikes(v):
    """A list, or text like '25000, 25100 25200'."""
    if isinstance(v, str):
        v = re.split(r"[\s,;]+", v.strip())
    if not isinstance(v, (list, tuple)):
        return []
    return [x for x in v if str(x).strip() != ""]


def clean_cfg(d):
    d = dict(d or {})
    # schema 1 had one expiry and one contract
    if "expiries" not in d and d.get("expiry"):
        d["expiries"] = [d["expiry"]]
    # schemas 1-2: auto_atm + a single strike became a mode + a list
    if "strike_mode" not in d:
        d["strike_mode"] = "atm" if d.get("auto_atm", True) else "list"
        if _f(d.get("strike")) > 0 and not d.get("strike_list"):
            d["strike_list"] = [d["strike"]]
    c = dict(DEFAULTS)
    c.update({k: v for k, v in d.items() if k in DEFAULTS})

    raw = c["expiries"] if isinstance(c["expiries"], (list, tuple)) else [c["expiries"]]
    exps = []
    for e in raw:
        e = str(e or "")[:10]
        if _EXPIRY_RE.fullmatch(e) and e not in exps:
            exps.append(e)
    c["expiries"] = sorted(exps)[:MAX_EXPIRIES]

    raw = c["opt_types"] if isinstance(c["opt_types"], (list, tuple)) else [c["opt_types"]]
    want = {str(t).upper() for t in raw}
    c["opt_types"] = [t for t in ("CE", "PE") if t in want]

    c["strike_mode"] = "list" if c["strike_mode"] == "list" else "atm"
    c["strike_list"] = sorted({round_strike(x) for x in parse_strikes(c["strike_list"])
                               if round_strike(x) > 0})[:MAX_LIST]
    c["strikes_each_side"] = max(0, min(MAX_EACH_SIDE, int(_f(c["strikes_each_side"], 10))))
    c["mom_length"] = max(1, min(200, int(_f(c["mom_length"], 14))))
    c["bar_seconds"] = max(5, min(900, int(_f(c["bar_seconds"], 60))))
    c["lots"] = max(1, min(50, int(_f(c["lots"], 1))))
    c["max_trades_per_day"] = max(1, min(500, int(_f(c["max_trades_per_day"], 6))))
    c["max_open"] = max(1, min(100, int(_f(c["max_open"], 2))))
    for k in ("level2", "level3", "mom_threshold", "trail_l2_pct", "trail_l3_pct",
              "move_rupees", "confirm_minutes"):
        c[k] = _f(c[k], DEFAULTS[k])
    c["vix_targets"] = (_valid_vix_targets(c["vix_targets"])
                        or [list(r) for r in DEFAULTS["vix_targets"]])
    return c


# ─────────────────────────────────────────────────────────────────────────────
#  STATE
# ─────────────────────────────────────────────────────────────────────────────
def lane_key(expiry, opt_type, strike):
    return "%s|%s|%d" % (expiry, opt_type, int(round(_f(strike))))


def contract_label(expiry, strike, opt_type):
    return "%s %d %s" % (expiry, int(round(_f(strike))), opt_type)


class Lane:
    """One contract: an expiry, a side and a FIXED strike.

    TradingView ran the script on ONE option's chart.  Watching many strikes,
    both sides and several expiries is running it on many charts at once, so
    each contract keeps what a chart would: its own bars, momentum and
    position.  The strike never changes - a bar series is only meaningful for
    one contract, and rolling strikes mid-series would fake price moves."""

    def __init__(self, expiry, opt_type, strike):
        self.expiry, self.opt_type, self.strike = expiry, opt_type, float(strike)
        self.bars, self.cur = [], None
        self.series_bar = None         # bar length the bars were built with
        self.position = None
        self.last_quote = None
        self.last_quote_ts = 0.0
        self.status = "waiting for the first quote"

    @property
    def key(self):
        return lane_key(self.expiry, self.opt_type, self.strike)

    @property
    def label(self):
        return contract_label(self.expiry, self.strike, self.opt_type)

    def to_json(self, keep):
        return {"expiry": self.expiry, "opt_type": self.opt_type, "strike": self.strike,
                "bars": self.bars[-keep:], "cur": self.cur, "series_bar": self.series_bar,
                "position": self.position}

    @classmethod
    def from_json(cls, d):
        lane = cls(str(d.get("expiry") or ""), "PE" if str(d.get("opt_type")).upper() == "PE" else "CE",
                   _f(d.get("strike")))
        lane.bars = [b for b in (d.get("bars") or []) if isinstance(b, dict)]
        lane.cur = d.get("cur") if isinstance(d.get("cur"), dict) else None
        lane.series_bar = d.get("series_bar")
        lane.position = d.get("position")
        return lane


class Book:
    def __init__(self):
        self.lock = threading.RLock()
        self.cfg = clean_cfg({})
        self.running = False
        self.scrip_lookup = {}
        self.expiry_list = []
        self.expiry_fetched = 0.0
        self.lanes = {}                # lane key -> Lane.  ONLY the engine thread adds or drops.
        self.centers = {}              # expiry -> ATM strike the window is built around
        self.history = []              # every closed trade, oldest first (mirrors trades.jsonl)
        self.vix = None
        self.vix_note = ""
        self.target_ticks = 1400
        self.spot = None
        self.status = "idle"
        self.market_note = ""
        self.trades_today = 0
        self.day = now_ist().strftime("%Y-%m-%d")
        self.last_save = 0.0
        # Launching the strategy from NIFTY Trader starts it.  If the settings
        # are not usable yet (no expiry list before the token works), the
        # engine keeps trying and starts as soon as they are.  Stop cancels it.
        self.autostart = False
        # Closed trades not yet safely in trades.jsonl.  Saved in the state
        # file too, so a failed write (disk full, file locked) never loses one.
        self.unflushed = []

    def open_count(self):
        with self.lock:
            return sum(1 for l in self.lanes.values() if l.position)

    # ---- persistence ----
    def snapshot(self):
        keep = self.cfg["mom_length"] + 20
        return {"schema": 3, "saved_at": ts(), "cfg": self.cfg,
                "lanes": {k: l.to_json(keep) for k, l in self.lanes.items()},
                "unflushed_trades": self.unflushed,
                "trades_today": self.trades_today, "day": self.day}

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
        old_history = []
        if isinstance(d, dict):
            self.cfg = clean_cfg(d.get("cfg"))
            self.day = d.get("day") or self.day
            self.trades_today = int(d.get("trades_today") or 0)
            old_history = d.get("history") or []
            self.unflushed = [r for r in (d.get("unflushed_trades") or []) if isinstance(r, dict)]
            schema = int(d.get("schema") or 1)
            if schema >= 3:
                for ld in (d.get("lanes") or {}).values():
                    try:
                        lane = Lane.from_json(ld)
                    except Exception:
                        continue
                    if lane.expiry and lane.strike > 0:
                        self.lanes[lane.key] = lane
            else:
                # Schemas 1-2 keyed a contract without its strike.  Only an
                # OPEN POSITION matters enough to carry over; bars restart.
                old = d.get("cfg") or {}
                candidates = []
                if schema == 2:
                    candidates = [(ld, ld.get("position")) for ld in (d.get("lanes") or {}).values()]
                elif d.get("position"):
                    candidates = [({"expiry": old.get("expiry"), "opt_type": old.get("opt_type")},
                                   d.get("position"))]
                for ld, pos in candidates:
                    if not pos:
                        continue
                    exp = str(pos.get("expiry") or ld.get("expiry") or "")[:10]
                    typ = "PE" if str(pos.get("opt_type") or ld.get("opt_type")).upper() == "PE" else "CE"
                    strike = _f(pos.get("strike"))
                    if not exp or strike <= 0:
                        continue
                    lane = Lane(exp, typ, strike)
                    pos.update(lane=lane.key, expiry=exp, opt_type=typ)
                    lane.position = pos
                    self.lanes[lane.key] = lane
        # Every closed trade lives in trades.jsonl.  Older versions kept the
        # last 400 inside the state file; move those over once.
        if old_history and not os.path.exists(TRADES_FILE):
            write_trades(old_history)
        on_disk = load_trades()
        if self.unflushed:
            # A pending trade may already be in trades.jsonl: the flush can
            # succeed after the state file was last saved.  Match on the trade
            # id so a restart never books the same trade twice.
            have = {trade_key(r) for r in on_disk}
            self.unflushed = [r for r in self.unflushed if trade_key(r) not in have]
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


def ts():
    return now_ist().strftime("%Y-%m-%d %H:%M:%S")


# ---- the trade book on disk ----
def trade_key(r):
    """What makes a closed trade unique: its id, or for very old rows that
    have none, when it closed and what it was."""
    return r.get("id") or (r.get("closed"), r.get("contract"), r.get("entry"), r.get("exit"))


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
    """Rewrite a whole .jsonl atomically (Clear / Wipe / migration)."""
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


def append_trade(rec, path=None):
    append_trades([rec], path)


# Serialises every write to the trade book files.  Lock order is ALWAYS
# _book_lock first, then STATE.lock - never the other way round.
_book_lock = threading.Lock()
_flush_warned = [False]


def flush_unflushed():
    """Move pending closed trades into trades.jsonl.  Never called while
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
                log_event("error", "could not write %d closed trade(s) to trades.jsonl (%s) - "
                                   "kept safely in the state file and retried every pass" % (len(pending), e))
            return False
        _flush_warned[0] = False
        with STATE.lock:
            STATE.unflushed = [r for r in STATE.unflushed if not any(r is x for x in pending)]
        return True


STATE = Book()
_SHUTDOWN = threading.Event()


# ─────────────────────────────────────────────────────────────────────────────
#  MARKET HOURS
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


# ─────────────────────────────────────────────────────────────────────────────
#  PRICE FEED  ->  BARS
# ─────────────────────────────────────────────────────────────────────────────
def quote_for(snap, strike, opt_type):
    side = "ce" if str(opt_type).upper() == "CE" else "pe"
    row = (snap.get("chain") or {}).get(round(_f(strike), 2))
    if not row:
        return None
    q = row.get(side)
    if not isinstance(q, dict):
        return None
    bid, ask = _f(q.get("top_bid_price")), _f(q.get("top_ask_price"))
    ltp = _f(q.get("last_price"))
    return {"ltp": ltp, "bid": bid, "ask": ask,
            "mid": (bid + ask) / 2.0 if (bid > 0 and ask >= bid) else ltp,
            "iv": _f(q.get("implied_volatility")), "oi": _f(q.get("oi")),
            "volume": _f(q.get("volume"))}


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


def _ist(t):
    return datetime.fromtimestamp(t, IST)


def slot_of(at, span):
    """Bars are anchored to the 09:15 IST session open, as TradingView's are -
    not to the UTC epoch, which puts 2- and 10-minute bars a minute off."""
    d = _ist(at)
    anchor = datetime(d.year, d.month, d.day, MKT_OPEN.hour, MKT_OPEN.minute, tzinfo=IST).timestamp()
    return anchor + math.floor((at - anchor) / span) * span


def _session_ts(t, hhmm):
    d = _ist(t)
    return datetime(d.year, d.month, d.day, hhmm.hour, hhmm.minute, tzinfo=IST).timestamp()


def _is_closing_bar(bar, span):
    """The session's last bar - judged by where the bar ENDS, so 15-minute
    bars (15:15-15:30) count too - allowing the usual 1-2 missed bars."""
    return bar["t"] + span >= _session_ts(bar["t"], MKT_CLOSE) - GAP_FILL_BARS * span


def _is_opening_slot(slot, span):
    return slot - _session_ts(slot, MKT_OPEN) <= GAP_FILL_BARS * span


def _next_trading_day(prev_t, slot):
    """True when slot is on the trading day straight after prev_t - only a
    weekend in between.  A skipped weekday (the app was off, or a holiday)
    returns False, which merely restarts the series."""
    a, b = _ist(prev_t).date(), _ist(slot).date()
    if b <= a:
        return False
    d = a + timedelta(days=1)
    while d < b:
        if d.weekday() < 5:
            return False
        d += timedelta(days=1)
    return True


def push_tick(lane, price, at=None):
    """Fold one LTP into the lane's current bar.  Returns the bars that CLOSED
    FRESH on this tick - the only ones a signal may be taken on.

    Gaps are where a naive bar builder goes wrong.  If polling stopped (Stop,
    an outage, a restart) the old unfinished bar must not be closed with a
    price from hours later: that fakes a cross and trades a stale signal.
      * next slot                 -> the bar closes normally
      * 1-2 bars missed           -> filled flat, the bar closes normally
      * a longer gap, same day    -> the series restarts (not enough data)
      * overnight: kept ONLY when all three hold - the old bar was that
        session's closing bar, its day is the previous trading day, and the
        new bar is today's opening bar.  Then yesterday's close is the
        previous bar, as on TradingView.  It is returned marked "stale": a
        held position may still exit on it, but it is never an entry signal.
        Anything else (a late Start, a missed day) restarts the series.
    """
    at = time.time() if at is None else at
    span = STATE.cfg["bar_seconds"]
    slot = slot_of(at, span)
    fresh = []
    with STATE.lock:
        if lane.series_bar != span:            # bars of another length are not one series
            lane.bars, lane.cur, lane.series_bar = [], None, span
        cur = lane.cur
        if cur is not None and slot != cur["t"]:
            same_day = _ist(cur["t"]).date() == _ist(slot).date()
            missing = int(round((slot - cur["t"]) / span)) - 1
            if slot < cur["t"]:
                lane.bars = []                  # clock went backwards: never corrupt the series
            elif same_day and missing <= GAP_FILL_BARS:
                lane.bars.append(cur)
                fresh.append(cur)
                for k in range(1, missing + 1):
                    c = cur["c"]
                    lane.bars.append({"t": cur["t"] + k * span, "o": c, "h": c, "l": c, "c": c,
                                      "fill": True})
            elif (not same_day and _is_closing_bar(cur, span)
                  and _next_trading_day(cur["t"], slot) and _is_opening_slot(slot, span)):
                cur["stale"] = True
                lane.bars.append(cur)
                fresh.append(cur)
            else:
                if lane.bars:
                    log_event("gap", "%s: no prices for %d min - bar history restarts"
                              % (lane.label, int((slot - cur["t"]) // 60)))
                lane.bars = []
            if len(lane.bars) > BAR_MEMORY:
                del lane.bars[:-BAR_MEMORY]
            cur = None
        if cur is None:
            cur = {"t": slot, "o": price, "h": price, "l": price, "c": price}
        else:
            cur["h"] = max(cur["h"], price)
            cur["l"] = min(cur["l"], price)
            cur["c"] = price
        lane.cur = cur
    return fresh


def bar_index(lane, bar):
    for i in range(len(lane.bars) - 1, max(-1, len(lane.bars) - 2 - GAP_FILL_BARS - 2), -1):
        if lane.bars[i] is bar:
            return i
    return -1


def momentum_at(lane, idx):
    """Pine ta.mom(close, n) = close - close[n], on closed bars."""
    n = STATE.cfg["mom_length"]
    if idx < n or idx >= len(lane.bars):
        return None
    return lane.bars[idx]["c"] - lane.bars[idx - n]["c"]


def momentum(lane):
    return momentum_at(lane, len(lane.bars) - 1)


# ─────────────────────────────────────────────────────────────────────────────
#  TARGET FROM VIX
# ─────────────────────────────────────────────────────────────────────────────
def target_ticks_for(vix):
    """<12 -> 800, <15 -> 1000, <20 -> 1200, else 1400, exactly as the script."""
    if vix is None:
        return DEFAULTS["vix_targets"][-1][1]
    for bound, ticks in STATE.cfg["vix_targets"]:
        if bound is None or vix < _f(bound):
            return int(ticks)
    return DEFAULTS["vix_targets"][-1][1]


def refresh_vix():
    v, err = fetch_vix_prev_close()
    with STATE.lock:
        if v:
            STATE.vix = v
            STATE.vix_note = "prev close %.2f" % v
        else:
            STATE.vix_note = "unavailable (%s) - using the widest target" % (err or "?")
        STATE.target_ticks = target_ticks_for(STATE.vix)
    log_event("vix", "India VIX %s -> target %d ticks (Rs %.2f)"
              % (STATE.vix_note, STATE.target_ticks, STATE.target_ticks * TICK))


# ─────────────────────────────────────────────────────────────────────────────
#  TRADING
# ─────────────────────────────────────────────────────────────────────────────
def lot_for(expiry, strike, opt_type):
    """The lot of THIS contract.  NSE changes lot sizes between series, so one
    expiry's lot is not another's."""
    meta = contract_meta(expiry, strike, opt_type)
    if meta and meta.get("lot"):
        return int(meta["lot"])
    return lot_size()


def open_position(lane, which, bar, quote):
    if kill_blocks():
        return None                   # VIX kill switch: no new trades
    cfg = STATE.cfg
    lot = lot_for(lane.expiry, lane.strike, lane.opt_type)
    qty = lot * cfg["lots"]
    # Filled at the ask: buying an option, that is the price actually payable.
    fill = quote["ask"] if quote and quote["ask"] > 0 else bar["c"]
    trail_pct = cfg["trail_l2_pct"] if which == "L2" else cfg["trail_l3_pct"]
    now = time.time()
    pos = {
        "id": "%s-%s-%d-%s-%d" % (lane.expiry, lane.opt_type, int(lane.strike), which, int(now * 1000)),
        "lane": lane.key, "contract": lane.label, "leg": which,
        "opened": ts(), "opened_ts": now,
        "expiry": lane.expiry, "opt_type": lane.opt_type, "strike": lane.strike,
        "entry": round(fill, 2), "qty": qty, "lot": lot, "lots": cfg["lots"],
        "entry_level": cfg["level2"] if which == "L2" else cfg["level3"],
        "highest": round(fill, 2),
        "trail_pct": trail_pct,
        "trail_level": round(fill * (1 - trail_pct / 100.0), 2),
        "target": round(fill + STATE.target_ticks * TICK, 2),
        "target_ticks": STATE.target_ticks,
        "move_level": round(fill + cfg["move_rupees"], 2),
        "above_since": None, "move_confirmed": False,
        "mark": round(fill, 2), "pnl": 0.0, "status": "OPEN",
    }
    lane.position = pos
    STATE.trades_today += 1
    STATE.save()
    log_event("entry", "%s BUY %s @ %.2f  target %.2f  trail %.2f (%.0f%%)"
              % (which, lane.label, fill, pos["target"], pos["trail_level"], trail_pct))
    return pos


def close_position(lane, reason, price):
    """price=None closes at the position's last mark, read under the lock -
    so a caller never has to touch lane.position itself (it may be gone)."""
    with STATE.lock:
        pos = lane.position
        if not pos:
            return None
        exit_px = round(_f(price, _f(pos.get("mark"))), 2)
        if exit_px <= 0:
            exit_px = round(_f(pos.get("mark")), 2)
        pnl = round((exit_px - pos["entry"]) * pos["qty"], 2)
        rec = dict(pos)
        rec.update(status="CLOSED", closed=ts(), closed_ts=time.time(), exit=exit_px,
                   reason=reason, pnl=pnl, points=round(exit_px - pos["entry"], 2),
                   contract=contract_label(pos["expiry"], pos["strike"], pos["opt_type"]))
        STATE.unflushed.append(rec)            # durable in the state file from here on
        STATE.history.append(rec)
        lane.position = None
        STATE.save()
    flush_unflushed()                          # outside STATE.lock: lock order
    log_event("exit", "%s %s %s @ %.2f  P&L Rs %.2f"
              % (rec["leg"], rec["contract"], reason, exit_px, pnl))
    return rec


def mark_position(lane, quote):
    """Mark at the BID: that is what the position could be sold for."""
    with STATE.lock:
        pos = lane.position
        if not pos or not quote:
            return
        mark = quote["bid"] if quote["bid"] > 0 else quote["ltp"]
        if mark <= 0:
            return
        pos["mark"] = round(mark, 2)
        pos["pnl"] = round((mark - pos["entry"]) * pos["qty"], 2)


def check_tick_exits(lane, quote):
    """Target and trailing stop are RESTING orders in Pine (strategy.exit), so
    they act on every price, not just a bar close.  The trail rides the highest
    price since entry.  Both trigger on the traded price, as the chart does."""
    with STATE.lock:
        pos = lane.position
        if not pos or not quote:
            return
        ltp = quote["ltp"]
        if ltp > pos["highest"]:
            pos["highest"] = round(ltp, 2)
            pos["trail_level"] = round(pos["highest"] * (1 - pos["trail_pct"] / 100.0), 2)
        target, trail = pos["target"], pos["trail_level"]
    sell = quote["bid"] if quote["bid"] > 0 else ltp
    if ltp <= trail:
        close_position(lane, "TRAIL_STOP", sell)            # a stop sells at the market
    elif ltp >= target:
        close_position(lane, "TARGET", target)              # a resting limit fills at its price


def evaluate_bar_exits(lane, bar, quote, now):
    """The push-then-fail rule reads the bar CLOSE, as the Pine script did."""
    with STATE.lock:
        pos = lane.position
        if not pos:
            return
        cfg = STATE.cfg
        close = bar["c"]
        if bar["h"] > pos["highest"]:
            pos["highest"] = round(bar["h"], 2)
            pos["trail_level"] = round(pos["highest"] * (1 - pos["trail_pct"] / 100.0), 2)
        if close > pos["move_level"]:
            if pos["above_since"] is None:
                pos["above_since"] = now
            elif (not pos["move_confirmed"]
                  and now - pos["above_since"] >= cfg["confirm_minutes"] * 60):
                pos["move_confirmed"] = True
                log_event("signal", "%s held above %.2f for %g min - fall-back exit is armed"
                          % (lane.label, pos["move_level"], cfg["confirm_minutes"]))
        elif not pos["move_confirmed"]:
            pos["above_since"] = None
        confirmed, move_level = pos["move_confirmed"], pos["move_level"]
    if confirmed and close < move_level:
        sell = quote["bid"] if (quote and quote["bid"] > 0) else close
        close_position(lane, "PUSH_FAILED", sell)


def lane_wanted(lane, keep=True):
    cfg = STATE.cfg
    return (lane.expiry in active_expiries() and lane.opt_type in cfg["opt_types"]
            and lane.strike in strike_window(lane.expiry, keep=keep))


def evaluate_entries(lane, bar, quote):
    """Pine: close[1] <= level and close > level, plus momentum, plus flat."""
    if bar.get("stale"):
        return                                 # yesterday's close is never an entry signal
    idx = bar_index(lane, bar)
    if idx < 1:
        return
    cfg = STATE.cfg
    prev, cur = lane.bars[idx - 1]["c"], bar["c"]
    mom = momentum_at(lane, idx)
    if mom is None:
        lane.status = "collecting bars (%d/%d)" % (len(lane.bars), cfg["mom_length"] + 1)
        return
    if mom <= cfg["mom_threshold"]:
        lane.status = "momentum %.1f, needs > %g" % (mom, cfg["mom_threshold"])
        return
    for which, level in (("L2", cfg["level2"]), ("L3", cfg["level3"])):
        if prev <= level < cur:
            # Everything below is decided under the lock, so two contracts can
            # never both take the last slot, and a contract that was just
            # unticked or dropped can never open a trade nobody can see.
            with STATE.lock:
                if not STATE.running:
                    lane.status = "stopped"    # Stop landed between the check and here
                    return
                if STATE.lanes.get(lane.key) is not lane or lane.position:
                    return
                if not lane_wanted(lane, keep=True):
                    lane.status = "signal ignored - no longer chosen in Settings"
                    return
                if STATE.trades_today >= cfg["max_trades_per_day"]:
                    lane.status = "signal skipped: %d trades already today" % cfg["max_trades_per_day"]
                    log_event("skip", "%s %s cross ignored - daily cap" % (which, lane.label))
                    return
                if STATE.open_count() >= cfg["max_open"]:
                    lane.status = "signal skipped: %d positions already open" % cfg["max_open"]
                    log_event("skip", "%s %s cross ignored - open-position cap" % (which, lane.label))
                    return
                open_position(lane, which, bar, quote)
                lane.status = "in a position"
            return
    lane.status = "waiting for a cross (last %.2f)" % cur


def atm_of(snap):
    """ATM in steps of 100: spot rounded to 100, or the nearest listed 100-step."""
    listed = [k for k in snap["chain"] if is_strike_step(k)]
    if not listed:
        return None
    atm = round_strike(snap["spot"])
    if atm in snap["chain"]:
        return atm
    return min(listed, key=lambda k: (abs(k - snap["spot"]), -k))


# ─────────────────────────────────────────────────────────────────────────────
#  CONTRACTS  (only the engine thread adds or drops them)
# ─────────────────────────────────────────────────────────────────────────────
def active_expiries():
    """Chosen expiries that still exist.  Before the list has loaded, trust the
    config; after, drop anything that has expired or was never listed."""
    exps = STATE.cfg["expiries"]
    if STATE.expiry_list:
        exps = [e for e in exps if e in STATE.expiry_list]
    return exps


def strike_window(expiry, keep=False):
    cfg = STATE.cfg
    if cfg["strike_mode"] == "list":
        return set(cfg["strike_list"])
    c = STATE.centers.get(expiry)
    if c is None:
        return set()
    n = cfg["strikes_each_side"] + (KEEP_EXTRA if keep else 0)
    return {float(c + k * STRIKE_STEP) for k in range(-n, n + 1)}


def sync_expiry(expiry, snap):
    """Re-centre the window on today's ATM, add the contracts in it, and drop
    FLAT contracts that have drifted well outside.  A contract in a position
    is never dropped: it must be managed until it exits."""
    with STATE.lock:
        cfg = STATE.cfg
        if cfg["strike_mode"] == "atm":
            atm = atm_of(snap)
            if atm is not None and atm != STATE.centers.get(expiry):
                if STATE.centers.get(expiry) is None:
                    log_event("contract", "%s: watching ATM %d +/- %d strikes (%s)" % (
                        expiry, int(atm), cfg["strikes_each_side"], "/".join(cfg["opt_types"])))
                STATE.centers[expiry] = atm
        listed = {k for k in snap["chain"] if is_strike_step(k)}
        want = strike_window(expiry) & listed
        keep = strike_window(expiry, keep=True)
        for side in cfg["opt_types"]:
            for strike in want:
                k = lane_key(expiry, side, strike)
                if k not in STATE.lanes:
                    STATE.lanes[k] = Lane(expiry, side, strike)
        for k, lane in list(STATE.lanes.items()):
            if lane.expiry != expiry or lane.position:
                continue
            if lane.opt_type not in cfg["opt_types"] or lane.strike not in keep:
                del STATE.lanes[k]


def prune_lanes():
    """Drop flat contracts whose expiry or side is no longer chosen."""
    with STATE.lock:
        exps, sides = set(active_expiries()), set(STATE.cfg["opt_types"])
        for k, lane in list(STATE.lanes.items()):
            if not lane.position and (lane.expiry not in exps or lane.opt_type not in sides):
                del STATE.lanes[k]
        for e in list(STATE.centers):
            if e not in exps:
                del STATE.centers[e]


def settle_expired():
    """A position whose expiry date has passed can no longer be quoted, and
    left alone it would hold an open-position slot forever.  Close it at its
    last mark."""
    today = now_ist().strftime("%Y-%m-%d")
    with STATE.lock:
        stale = [l for l in STATE.lanes.values() if l.position and l.expiry < today]
    for lane in stale:
        close_position(lane, "EXPIRED", None)    # None: last mark, read under the lock


def refresh_expiries(force=False):
    """The expiry list is re-read every 30 minutes, and at once when a new day
    starts.  Expiries before today are dropped by date (not only when Dhan stops
    listing them), and each one dropped is replaced by the next listed expiry."""
    today = now_ist().strftime("%Y-%m-%d")
    if not force and time.time() - STATE.expiry_fetched < 1800 and _expiry_day[0] == today:
        return
    STATE.expiry_fetched = time.time()
    _expiry_day[0] = today
    lst = [e for e in fetch_expiry_list() if e >= today]
    if not lst:
        return
    with STATE.lock:
        STATE.expiry_list = lst
        _roll_expiries(lst)
        STATE.save()


_expiry_day = [""]


def _roll_expiries(pool, what="expiry"):
    """Drop chosen expiries that are no longer in pool and, for each one
    dropped, tick the next listed expiry - so the number chosen stays the same
    without having to re-tick anything by hand.  Call under STATE.lock."""
    cur = list(STATE.cfg["expiries"])
    keep = [e for e in cur if e in pool]
    gone = [e for e in cur if e not in pool]
    want = min(max(len(cur), 1), MAX_EXPIRIES)
    fill = [e for e in pool if e not in keep][:max(0, want - len(keep))]
    if gone or fill:
        STATE.cfg["expiries"] = sorted(keep + fill)
    if gone:
        log_event("config", "removed expired %s %s%s" % (what, ", ".join(gone),
                  (" - now using %s instead" % ", ".join(fill)) if fill else ""))
    elif fill:
        log_event("config", "no %s chosen - using %s" % (what, ", ".join(fill)))


# ─────────────────────────────────────────────────────────────────────────────
#  ENGINE
# ─────────────────────────────────────────────────────────────────────────────
_last_vix = [0.0]


def step_lane(lane, snap, at=None):
    """One price for one contract.  Returns True when a bar closed."""
    q = quote_for(snap, lane.strike, lane.opt_type)
    if not q or q["ltp"] <= 0:
        lane.status = "no quote"
        return False
    now = time.time() if at is None else at
    lane.last_quote, lane.last_quote_ts = q, time.time()
    was_in = bool(lane.position)
    mark_position(lane, q)
    if lane.position:
        check_tick_exits(lane, q)
    fresh = push_tick(lane, q["ltp"], at=at)
    for bar in fresh:
        if lane.position:
            evaluate_bar_exits(lane, bar, q, now)
        elif STATE.running and not was_in:
            # was_in: a position open at this bar's close means Pine would not
            # look for an entry on it - even if this very price just exited it.
            evaluate_entries(lane, bar, q)
    if lane.position:
        lane.status = "in a position"
    elif not fresh and lane.status.startswith("waiting for the first"):
        lane.status = "collecting bars (%d/%d)" % (len(lane.bars), STATE.cfg["mom_length"] + 1)
    return bool(fresh)


def engine_step(at=None):
    """One pass of the engine.  Split out of the loop so tests can drive it
    with a fake chain and a fake clock."""
    state, why = market_state()
    STATE.market_note = "%s - %s" % (state, why)
    kill_step(state == "OPEN", _kill_close_all)

    if STATE.autostart and not STATE.running:
        err = validate_contracts(STATE.cfg)
        if err is None:
            with STATE.lock:
                STATE.autostart, STATE.running, STATE.centers = False, True, {}
            log_event("control", "started automatically on launch")

    day = now_ist().strftime("%Y-%m-%d")
    if day != STATE.day:
        with STATE.lock:
            STATE.day, STATE.trades_today = day, 0
            STATE.centers = {}                  # re-centre every window on today's ATM
        STATE.expiry_fetched = 0.0
        log_event("day", "new session %s - counters reset" % day)

    if state in ("OPEN", "PRE"):
        refresh_expiries()
    settle_expired()
    prune_lanes()
    with STATE.lock:
        holding = [l for l in STATE.lanes.values() if l.position]

    # Stopping blocks NEW entries only.  An open position keeps its target,
    # trail and push exits until it is out - a stop must never strand a trade.
    if not STATE.running and not holding:
        STATE.status = "stopped"
        return
    if state != "OPEN":
        STATE.status = "market %s" % why
        return
    ts_info = token_status()
    if not ts_info["configured"] or ts_info["expired"]:
        STATE.status = "token %s" % ts_info["human"]
        return
    if time.time() < _auth_block[0]:
        STATE.status = ("the broker rejected the token - paste a fresh one in Broker token "
                        "(retrying in %ds)" % int(_auth_block[0] - time.time()))
        return

    expiries = set(active_expiries()) if STATE.running else set()
    expiries |= {l.expiry for l in holding}
    if not expiries:
        STATE.status = "choose at least one expiry and CE or PE in Settings"
        return

    if time.time() - _last_vix[0] > 3600:
        _last_vix[0] = time.time()
        refresh_vix()

    active = set(active_expiries())
    bar_closed = False
    for expiry in sorted(expiries):
        if _SHUTDOWN.is_set() or time.time() < _auth_block[0]:
            break
        res = throttled_chain(expiry)
        snap = build_chain_snapshot(expiry, res)
        if not snap:
            msg = "option chain unavailable: %s" % (res.get("message") or "?")
            with STATE.lock:
                for lane in STATE.lanes.values():
                    if lane.expiry == expiry:
                        lane.status = msg
            continue
        STATE.spot = snap["spot"]
        watching = STATE.running and expiry in active
        if watching:
            sync_expiry(expiry, snap)
        with STATE.lock:
            # An unticked expiry is polled only for its open positions.
            group = [l for l in STATE.lanes.values()
                     if l.expiry == expiry and (watching or l.position)]
        for lane in group:
            if step_lane(lane, snap, at):
                bar_closed = True

    if bar_closed and time.time() - STATE.last_save > 60:
        STATE.save()                            # bars: at most once a minute
    if STATE.unflushed:
        flush_unflushed()                       # retry a trade write that failed
    n_open = STATE.open_count()
    if STATE.running:
        STATE.status = "watching %d contracts across %d expir%s - %d open" % (
            len(STATE.lanes), len(expiries), "y" if len(expiries) == 1 else "ies", n_open)
    else:
        STATE.status = "stopped - still managing %d open position%s until they exit" % (
            n_open, "" if n_open == 1 else "s")


def engine_loop():
    log_event("boot", "engine thread started")
    while not _SHUTDOWN.is_set():
        _SHUTDOWN.wait(2.0)
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
                log_event("boot", "ready - %d expiries, %d contracts in the scrip master"
                          % (len(STATE.expiry_list), len(STATE.scrip_lookup)))
                refresh_vix()
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


def seconds_per_check(n_expiries):
    """How often ONE contract gets a price: one chain call per expiry, each at
    least MIN_API_INTERVAL apart, plus any 429 backoff."""
    return max(1, n_expiries) * (MIN_API_INTERVAL + _api_backoff[0])


def dte_of(expiry):
    try:
        return (datetime.strptime(expiry, "%Y-%m-%d").date() - now_ist().date()).days
    except ValueError:
        return None


def next_level(ltp):
    cfg = STATE.cfg
    if ltp is None:
        return None, None
    if ltp <= cfg["level2"]:
        return "L2", round(cfg["level2"] - ltp, 2)
    if ltp <= cfg["level3"]:
        return "L3", round(cfg["level3"] - ltp, 2)
    return None, None


def lane_view(lane):
    q = lane.last_quote or {}
    lvl, dist = next_level(q.get("ltp"))
    return {"key": lane.key, "contract": lane.label, "expiry": lane.expiry,
            "dte": dte_of(lane.expiry), "opt_type": lane.opt_type, "strike": lane.strike,
            "ltp": q.get("ltp"), "bid": q.get("bid"), "ask": q.get("ask"),
            "quote_age": round(time.time() - lane.last_quote_ts) if lane.last_quote_ts else None,
            "momentum": momentum(lane), "bars": len(lane.bars),
            "need": STATE.cfg["mom_length"] + 1, "next_level": lvl, "distance": dist,
            "status": lane.status, "in_position": bool(lane.position)}


def position_view(lane):
    p = dict(lane.position)
    p["quote_age"] = round(time.time() - lane.last_quote_ts) if lane.last_quote_ts else None
    p["contract"] = lane.label
    return p


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
                       "contract": r.get("contract") or "", "closed": r.get("closed") or ""})

    def group(key):
        g = {}
        for r in rows:
            k = str(r.get(key) or "?")
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
        "by_side": group("opt_type"), "by_leg": group("leg"), "by_reason": group("reason"),
        "series": series,
    }


def check_body(body):
    """Numbers must be numbers, inside a sane range - never silently 0."""
    for k, (lo, hi) in RANGES.items():
        if k not in body:
            continue
        v = body[k]
        try:
            fv = float(v)
        except (TypeError, ValueError):
            return "%s must be a number." % LABELS.get(k, k)
        if fv != fv or not (lo <= fv <= hi):
            return "%s must be between %g and %g." % (LABELS.get(k, k), lo, hi)
    return None


def validate_contracts(cfg, raw_strikes=None):
    """Errors a user can fix, in words.  None when all is well."""
    if not cfg["expiries"]:
        return "Choose at least one expiry."
    if STATE.expiry_list:
        gone = [e for e in cfg["expiries"] if e not in STATE.expiry_list]
        if gone:
            return "No longer listed (expired?): %s. Untick it." % ", ".join(gone)
    if not cfg["opt_types"]:
        return "Choose CE, PE or both."
    need = 2 * len(cfg["expiries"]) * MIN_API_INTERVAL
    if cfg["bar_seconds"] < need:
        return ("Bar length must be at least %ds with %d expir%s: each contract only gets a price "
                "about every %.0fs, so shorter bars would be mostly empty."
                % (math.ceil(need), len(cfg["expiries"]), "y" if len(cfg["expiries"]) == 1 else "ies",
                   need / 2))
    if cfg["strike_mode"] == "list":
        raw = parse_strikes(raw_strikes) if raw_strikes is not None else cfg["strike_list"]
        if not raw:
            return "Type at least one strike, e.g. 25000, 25100 - or choose 'Around ATM'."
        bad = [str(x) for x in raw if not is_strike_step(x)]
        if bad:
            return "Strikes must be multiples of %d - not %s." % (STRIKE_STEP, ", ".join(bad[:5]))
        if len(raw) > MAX_LIST:
            return "At most %d strikes in your list." % MAX_LIST
    return None


@app.route("/api/state")
def api_state():
    today = now_ist().strftime("%Y-%m-%d")
    with STATE.lock:
        lanes = list(STATE.lanes.values())
        positions = [position_view(l) for l in sorted(lanes, key=lambda l: l.key) if l.position]
        near = []
        for l in lanes:
            if l.position or not l.last_quote:
                continue
            v = lane_view(l)
            if v["distance"] is not None:
                near.append(v)
        near.sort(key=lambda v: v["distance"])
        hist = list(STATE.history)
        exps = sorted({l.expiry for l in lanes})
    today_rows = [h for h in hist if str(h.get("closed") or "").startswith(today)]
    return jsonify({
        "running": STATE.running, "status": STATE.status, "market": STATE.market_note,
        "cfg": STATE.cfg, "expiry_list": STATE.expiry_list, "centers": STATE.centers,
        "token": token_status(), "spot": STATE.spot,
        "vix": STATE.vix, "vix_note": STATE.vix_note,
        "target_ticks": STATE.target_ticks, "target_rupees": round(STATE.target_ticks * TICK, 2),
        "trades_today": STATE.trades_today,
        "today_pnl": round(sum(_f(h.get("pnl")) for h in today_rows), 2),
        "today_trades": len(today_rows),
        "realised": round(sum(_f(h.get("pnl")) for h in hist), 2), "all_trades": len(hist),
        "open_count": len(positions), "lanes_count": len(lanes),
        "positions": positions, "near": near[:12],
        "events": recent_events(15), "tick": TICK, "lot": lot_size(),
        "strike_step": STRIKE_STEP, "max_expiries": MAX_EXPIRIES, "max_each_side": MAX_EACH_SIDE,
        "seconds_per_check": round(seconds_per_check(len(exps) or len(STATE.cfg["expiries"])), 1),
    })


@app.route("/api/lanes")
def api_lanes():
    exp, side = request.args.get("expiry") or "", request.args.get("side") or ""
    with STATE.lock:
        rows = [lane_view(l) for l in STATE.lanes.values()
                if (not exp or l.expiry == exp) and (not side or l.opt_type == side)]
    rows.sort(key=lambda r: (r["expiry"], r["opt_type"], r["strike"]))
    return jsonify({"rows": rows})


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


TRADE_COLS = [("Closed", "closed"), ("Contract", "contract"), ("Expiry", "expiry"),
              ("Side", "opt_type"), ("Strike", "strike"), ("Leg", "leg"),
              ("Level", "entry_level"), ("Opened", "opened"), ("Entry", "entry"),
              ("Exit", "exit"), ("Points", "points"), ("Lots", "lots"), ("Lot size", "lot"),
              ("Qty", "qty"), ("P&L", "pnl"), ("Exit reason", "reason"),
              ("Highest", "highest"), ("Target", "target"), ("Target ticks", "target_ticks"),
              ("Trail %", "trail_pct"), ("Push level", "move_level"), ("Id", "id")]


@app.route("/api/history.csv")
def api_history_csv():
    with STATE.lock:
        rows = list(STATE.history)
    return _csv("level_cross_trades_%s.csv" % now_ist().strftime("%Y%m%d"),
                [c for c, _ in TRADE_COLS], [[r.get(k, "") for _, k in TRADE_COLS] for r in rows])


@app.route("/api/positions.csv")
def api_positions_csv():
    cols = [("Contract", "contract"), ("Leg", "leg"), ("Opened", "opened"), ("Entry", "entry"),
            ("Mark", "mark"), ("Qty", "qty"), ("Open P&L", "pnl"), ("Target", "target"),
            ("Trail", "trail_level"), ("Highest", "highest"), ("Push level", "move_level")]
    with STATE.lock:
        rows = [position_view(l) for l in STATE.lanes.values() if l.position]
    return _csv("level_cross_positions_%s.csv" % now_ist().strftime("%Y%m%d"),
                [c for c, _ in cols], [[r.get(k, "") for _, k in cols] for r in rows])


def _remove_trades(pred, why):
    """Clear/Wipe never destroy data: removed trades are appended to
    trades_removed.jsonl first, then the book is rewritten without them.

    The files are written holding only _book_lock, so the engine keeps
    pricing and exiting positions meanwhile; a trade that closes during the
    rewrite is kept."""
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
    err = validate_contracts(STATE.cfg)
    if err:
        return jsonify({"error": err}), 400
    with STATE.lock:
        STATE.centers = {}                      # re-centre on the ATM of right now
        STATE.running = True
    log_event("control", "started")
    STATE.save()
    return jsonify({"ok": True})


@app.route("/api/stop", methods=["POST"])
def api_stop():
    with STATE.lock:
        STATE.running = False
        STATE.autostart = False
        n = STATE.open_count()
    log_event("control", "stopped - no new entries%s" % (
        "; %d open position%s keep their exits" % (n, "" if n == 1 else "s") if n else ""))
    STATE.save()
    return jsonify({"ok": True})


@app.route("/api/flatten", methods=["POST"])
def api_flatten():
    body = request.get_json(silent=True) or {}
    key = body.get("key")
    with STATE.lock:
        lanes = [l for l in STATE.lanes.values() if l.position and (not key or l.key == key)]
    closed = []
    for lane in lanes:
        q = lane.last_quote or {}
        fresh = lane.last_quote_ts and time.time() - lane.last_quote_ts < 30
        if fresh and (q.get("bid") or q.get("ltp")):
            px, why = q.get("bid") or q.get("ltp"), "MANUAL"
        else:
            # No live price (market closed, chain down): say so rather than
            # pretend the old mark is 'the current bid'.  None = last mark,
            # read under the lock - the engine may have closed it meanwhile.
            px, why = None, "MANUAL_LAST_MARK"
        rec = close_position(lane, why, px)
        if rec:
            closed.append({"contract": rec["contract"], "exit": rec["exit"], "reason": why})
    return jsonify({"ok": True, "closed": closed})


@app.route("/api/config", methods=["POST"])
def api_config():
    body = request.get_json(silent=True) or {}
    err = check_body(body)
    if err:
        return jsonify({"error": err}), 400
    raw_exps = body.get("expiries")
    if isinstance(raw_exps, list) and len({str(e)[:10] for e in raw_exps}) > MAX_EXPIRIES:
        return jsonify({"error": "Choose at most %d expiries - each one adds about 3 s "
                                 "between price checks." % MAX_EXPIRIES}), 400
    with STATE.lock:
        new = clean_cfg({**STATE.cfg, **body})
        err = validate_contracts(new, raw_strikes=body.get("strike_list")
                                 if new["strike_mode"] == "list" else None)
        if err:
            return jsonify({"error": err}), 400
        # Only the config changes here.  Contracts are added and dropped by the
        # engine thread at the start of its next pass, so a Save can never
        # pull a contract out from under a pass that is still using it.
        STATE.cfg = new
        STATE.save()
    log_event("config", "settings saved - %d expir%s x %s, %s" % (
        len(new["expiries"]), "y" if len(new["expiries"]) == 1 else "ies",
        "/".join(new["opt_types"]),
        ("ATM +/- %d strikes" % new["strikes_each_side"] if new["strikes_each_side"] else "ATM only")
        if new["strike_mode"] == "atm"
        else "%d chosen strikes" % len(new["strike_list"])))
    return jsonify({"ok": True, "cfg": STATE.cfg})


@app.route("/api/reset-bars", methods=["POST"])
def api_reset_bars():
    with STATE.lock:
        for lane in STATE.lanes.values():
            lane.bars, lane.cur = [], None
    log_event("control", "bar history cleared on every contract")
    return jsonify({"ok": True})


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
    runtime_write(access_token=tok, client_id=str(claims.get("dhanClientId") or ""),
                  saved_at=ts())
    log_event("token", "token saved locally")
    return jsonify({"ok": True, "token": token_status()})


@app.route("/")
def index():
    return Response(PAGE, mimetype="text/html")


PAGE = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>2-Level Cross</title>
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
</style></head><body>

<div class="top">
  <div><h1>2-Level Cross + Momentum</h1>
    <p class="sub">Buys an option when its premium crosses up through a level - many strikes, CE and PE, several expiries - paper trading</p></div>
  <div class="sp"></div>
  <span class="pill" id="p_mkt">-</span>
  <span class="pill" id="p_tok">-</span>
  <span class="pill" id="p_run">-</span>
  <button class="go" id="b_start">Start</button>
  <button class="stop" id="b_stop">Stop</button>
</div>
<nav class="tabs" id="tabs">
  <button data-tab="dash" class="on">Dashboard</button>
  <button data-tab="contracts">Contracts</button>
  <button data-tab="positions">Positions</button>
  <button data-tab="report">Trade Report</button>
  <button data-tab="activity">Activity</button>
  <button data-tab="settings">Settings</button>
</nav>
<div class="statusline" id="statusline">-</div>

<main>
<!-- DASHBOARD -->
<section class="panel on" id="p-dash">
  <div class="note">Paper trading only - nothing is sent to the broker. It starts by itself when launched from NIFTY Trader. Stop blocks new entries; open positions keep their exits until they are out.</div>
  <div class="grid">
    <div class="card"><div class="k">CONTRACTS WATCHED</div><div class="v" id="d_lanes">-</div><div class="hint" id="d_lanes2">-</div></div>
    <div class="card"><div class="k">OPEN POSITIONS</div><div class="v" id="d_open">-</div><div class="hint" id="d_open2">-</div></div>
    <div class="card"><div class="k">TARGET (FROM VIX)</div><div class="v" id="d_tgt">-</div><div class="hint" id="d_tgt2">-</div></div>
    <div class="card"><div class="k">TODAY'S P&amp;L</div><div class="v" id="d_pnl">-</div><div class="hint" id="d_pnl2">-</div></div>
  </div>
  <div class="two">
    <div class="card"><h3>OPEN POSITIONS</h3><div class="tw" id="d_pos"></div></div>
    <div class="card"><h3>CLOSEST TO A LEVEL</h3><div class="tw" id="d_near"></div></div>
  </div>
  <div class="card"><h3>RECENT ACTIVITY</h3><div class="tw" id="d_ev"></div></div>
</section>

<!-- CONTRACTS -->
<section class="panel" id="p-contracts">
  <div class="bar">
    <select id="f_exp"><option value="">All expiries</option></select>
    <select id="f_side"><option value="">CE and PE</option><option value="CE">CE only</option><option value="PE">PE only</option></select>
    <label class="chip" style="padding:6px 10px" title="Premium is still under Level 2 or Level 3, so it can still cross UP and trigger a buy. Contracts already above both levels cannot signal until they fall back below."><input type="checkbox" id="f_near"> Only those that can still cross up</label>
    <span class="hint" id="c_count"></span>
  </div>
  <div class="card scroll"><div id="c_table"></div></div>
</section>

<!-- POSITIONS -->
<section class="panel" id="p-positions">
  <div class="bar">
    <span class="big" id="pos_total">-</span><div class="sp"></div>
    <a href="/api/positions.csv" class="btn sm" download>Download for Excel</a>
    <button class="sm danger" id="b_flat">Close all</button>
  </div>
  <div class="card tw" id="pos_table"></div>
  <p class="hint">Target and trailing stop act on every price check, like resting orders. The push rule acts on bar closes. Close sells at the live bid; with no live price it uses the last mark and says so.</p>
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
    <div class="grp"><label>Expiries - tick up to <span id="maxexp">4</span></label><div class="chips" id="s_exps"></div>
      <div class="hint" id="s_expnote"></div></div>
    <div class="grp"><label>Sides</label><div class="chips">
      <label class="chip" id="chip_CE"><input type="checkbox" id="t_CE"> <span class="tag ce">CE</span> Calls</label>
      <label class="chip" id="chip_PE"><input type="checkbox" id="t_PE"> <span class="tag pe">PE</span> Puts</label>
    </div></div>
    <div class="grp"><label>Strikes (always multiples of 100)</label>
      <div class="mode">
        <div class="row"><label class="chip" style="margin:0"><input type="radio" name="smode" value="atmonly" id="m_atmonly"> ATM only</label>
          just the at-the-money strike (rounded to 100), following NIFTY as it moves</div>
        <div class="row"><label class="chip" style="margin:0"><input type="radio" name="smode" value="atm" id="m_atm"> Around ATM</label>
          ATM +/- <input id="c_strikes_each_side" type="number" min="1" max="30" style="width:80px"> strikes, following NIFTY as it moves</div>
        <div class="row"><label class="chip" style="margin:0"><input type="radio" name="smode" value="list" id="m_list"> My strikes</label>
          <input id="c_strike_list" placeholder="e.g. 24800, 25000, 25200" style="min-width:320px"></div>
        <div class="hint" id="s_count"></div>
      </div></div>
    <div class="f">
      <div class="fl"><label>Level 2</label><input id="c_level2" type="number" step="0.05"></div>
      <div class="fl"><label>Level 3</label><input id="c_level3" type="number" step="0.05"></div>
      <div class="fl"><label>Momentum length (bars)</label><input id="c_mom_length" type="number"></div>
      <div class="fl"><label>Momentum threshold</label><input id="c_mom_threshold" type="number" step="0.5"></div>
      <div class="fl"><label>Trailing stop L2 (%)</label><input id="c_trail_l2_pct" type="number" step="0.5"></div>
      <div class="fl"><label>Trailing stop L3 (%)</label><input id="c_trail_l3_pct" type="number" step="0.5"></div>
      <div class="fl"><label>Push level (Rs above entry)</label><input id="c_move_rupees" type="number" step="0.05"></div>
      <div class="fl"><label>Hold above for (minutes)</label><input id="c_confirm_minutes" type="number" step="0.5"></div>
      <div class="fl"><label>Bar length (seconds)</label><input id="c_bar_seconds" type="number"></div>
      <div class="fl"><label>Lots per trade</label><input id="c_lots" type="number"></div>
      <div class="fl"><label>Max trades per day (all contracts)</label><input id="c_max_trades_per_day" type="number"></div>
      <div class="fl"><label>Max open at once (all contracts)</label><input id="c_max_open" type="number"></div>
    </div>
    <div class="bar" style="margin:16px 0 0">
      <button class="go" id="b_save">Save settings</button>
      <button class="ghost" id="b_revert">Discard changes</button>
      <button class="ghost" id="b_reset">Clear bar history</button>
    </div>
    <p class="hint" id="s_foot"></p>
  </div>
  <div class="card" style="margin-top:14px"><h3>BROKER</h3><div id="s_tok" class="hint"></div></div>
</section>
</main>

<script>
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const esc=v=>String(v==null?'':v).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const num=(n,d)=>n==null||isNaN(n)?'-':Number(n).toFixed(d==null?2:d);
const inr=(n,d)=>n==null||isNaN(n)?'-':(n<0?'-':'')+'₹'+Math.abs(Number(n)).toLocaleString('en-IN',{minimumFractionDigits:d==null?2:d,maximumFractionDigits:d==null?2:d});
const inrShort=v=>{const a=Math.abs(v),s=v<0?'-':'';return a>=1e5?s+'₹'+(a/1e5).toFixed(a>=1e6?0:1)+'L':a>=1e3?s+'₹'+(a/1e3).toFixed(a>=1e4?0:1)+'k':s+'₹'+a.toFixed(0);};
const cls=n=>n>0?'g':(n<0?'r':'');
const tag=t=>'<span class="tag '+(t==='PE'?'pe':'ce')+'">'+esc(t)+'</span>';
const table=(head,rows,empty)=>rows.length?'<table><thead><tr>'+head.map(h=>'<th>'+h+'</th>').join('')+'</tr></thead><tbody>'+rows.join('')+'</tbody></table>':'<div class="empty">'+empty+'</div>';
function setHTML(el,html){if(el&&el.__h!==html){el.innerHTML=html;el.__h=html;}}
async function post(u,b){const r=await fetch(u,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b||{})});
 const d=await r.json().catch(()=>({}));if(!r.ok)throw new Error(d.error||('failed ('+r.status+')'));return d;}
async function get(u){const r=await fetch(u);if(!r.ok)throw new Error('failed ('+r.status+')');return r.json();}
const store={get(k){try{return localStorage.getItem(k);}catch(e){return null;}},set(k,v){try{localStorage.setItem(k,v);}catch(e){}}};

/* ---------- tabs ---------- */
let TAB='dash';
function showTab(t){TAB=t;store.set('lc_tab',t);
  $$('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.tab===t));
  $$('.panel').forEach(p=>p.classList.toggle('on',p.id==='p-'+t));
  if(t==='report')loadReport(); if(t==='activity')loadEvents(true); if(t==='contracts')loadLanes();}
$('#tabs').onclick=e=>{const b=e.target.closest('button[data-tab]');if(b)showTab(b.dataset.tab);};

/* ---------- live state ---------- */
let S=null;
async function poll(){
  try{S=await get('/api/state');}catch(e){$('#statusline').textContent='cannot reach the strategy: '+e.message;return;}
  const s=S;
  $('#p_mkt').textContent=s.market;
  $('#p_tok').textContent='token '+s.token.human; $('#p_tok').className='pill '+(s.token.configured&&!s.token.expired?'on':'off');
  $('#p_run').textContent=s.running?'RUNNING':'STOPPED'; $('#p_run').className='pill '+(s.running?'on':'off');
  $('#b_start').disabled=s.running; $('#b_stop').disabled=!s.running;
  $('#statusline').textContent=s.status+(s.spot?'   |   NIFTY '+num(s.spot,2):'');

  /* dashboard */
  const nexp=s.cfg.expiries.length, nside=s.cfg.opt_types.length;
  $('#d_lanes').textContent=s.lanes_count;
  $('#d_lanes2').textContent=nexp+' expir'+(nexp===1?'y':'ies')+' x '+(s.cfg.opt_types.join('+')||'-')+
    (s.cfg.strike_mode==='atm'?(s.cfg.strikes_each_side?' x ATM +/- '+s.cfg.strikes_each_side:' x ATM only'):' x '+s.cfg.strike_list.length+' strikes')+' - checked every ~'+s.seconds_per_check+'s';
  $('#d_open').textContent=s.open_count+' / '+s.cfg.max_open;
  $('#d_open2').textContent=s.trades_today+' of '+s.cfg.max_trades_per_day+' trades used today';
  $('#d_tgt').textContent=inr(s.target_rupees);
  $('#d_tgt2').textContent=s.target_ticks+' ticks - India VIX '+(s.vix_note||'-');
  $('#d_pnl').textContent=inr(s.today_pnl); $('#d_pnl').className='v '+cls(s.today_pnl);
  $('#d_pnl2').textContent=s.today_trades+' closed today - all time '+inr(s.realised)+' over '+s.all_trades+' trades';
  setHTML($('#d_pos'),table(['Contract','Leg','Entry','Mark','P&amp;L'],s.positions.map(p=>
    '<tr><td>'+contractCell(p)+'</td><td>'+esc(p.leg)+'</td><td>'+num(p.entry)+'</td><td>'+num(p.mark)+'</td><td class="'+cls(p.pnl)+'">'+inr(p.pnl)+'</td></tr>'),'No open positions.'));
  setHTML($('#d_near'),table(['Contract','Premium','Next','Needs','Momentum'],s.near.map(l=>
    '<tr><td>'+contractCell(l)+'</td><td>'+num(l.ltp)+'</td><td>'+esc(l.next_level)+'</td><td>+'+num(l.distance)+'</td><td>'+momCell(l)+'</td></tr>'),
    s.running?'Waiting for prices.':'Press Start to watch contracts.'));
  setHTML($('#d_ev'),eventRows(s.events));

  /* positions */
  const tot=s.positions.reduce((a,p)=>a+(p.pnl||0),0);
  $('#pos_total').textContent='Open P&L: '+inr(tot); $('#pos_total').className='big '+cls(tot);
  setHTML($('#pos_table'),table(['Contract','Leg','Opened','Entry','Mark','Open P&amp;L','Target','Trail','Push level','Price age',''],s.positions.map(p=>
    '<tr><td>'+contractCell(p)+'</td><td>'+esc(p.leg)+' <span class="hint">@'+num(p.entry_level)+'</span></td><td>'+esc(String(p.opened||'').slice(5,16))+'</td>'+
    '<td>'+num(p.entry)+'</td><td>'+num(p.mark)+'</td><td class="'+cls(p.pnl)+'"><b>'+inr(p.pnl)+'</b></td>'+
    '<td>'+num(p.target)+'</td><td>'+num(p.trail_level)+' <span class="hint">high '+num(p.highest)+'</span></td>'+
    '<td>'+num(p.move_level)+' <span class="hint">'+(p.move_confirmed?'confirmed':(p.above_since?'timing':'not reached'))+'</span></td>'+
    '<td class="hint">'+(p.quote_age==null?'-':p.quote_age+'s')+'</td>'+
    '<td><button class="sm danger" data-close="'+esc(p.lane)+'" data-name="'+esc(p.contract)+'">Close</button></td></tr>'),'No open positions.'));

  paintSettings(s);
  if(TAB==='contracts')loadLanes();
}
function contractCell(x){return esc(x.expiry)+' <b>'+esc(Math.round(x.strike))+'</b> '+tag(x.opt_type);}
function momCell(l){return l.momentum==null?'<span class="hint">'+l.bars+'/'+l.need+' bars</span>':'<span class="'+(S&&l.momentum>S.cfg.mom_threshold?'g':'')+'">'+num(l.momentum)+'</span>';}
function eventRows(evs){return table(['Time','Kind','What happened'],(evs||[]).map(e=>
  '<tr><td class="mono">'+esc(e.ts||e.at)+'</td><td><span class="tag" style="background:var(--p2)">'+esc(e.kind)+'</span></td><td class="wrap">'+esc(e.msg)+'</td></tr>'),'Nothing yet.');}

/* ---------- contracts ---------- */
let lanesBusy=false;
async function loadLanes(){
  if(lanesBusy)return; lanesBusy=true;
  try{
    const q='?expiry='+encodeURIComponent($('#f_exp').value)+'&side='+encodeURIComponent($('#f_side').value);
    let rows=(await get('/api/lanes'+q)).rows;
    if($('#f_near').checked)rows=rows.filter(r=>r.distance!=null).sort((a,b)=>a.distance-b.distance);
    $('#c_count').textContent=rows.length+' contract'+(rows.length===1?'':'s');
    setHTML($('#c_table'),table(['Expiry','Side','Strike','Premium','Bid / Ask','Momentum','Bars','Next level','Needs','Status'],rows.map(r=>
      '<tr><td>'+esc(r.expiry)+' <span class="hint">'+(r.dte==null?'':r.dte+'d')+'</span></td><td>'+tag(r.opt_type)+'</td><td><b>'+esc(Math.round(r.strike))+'</b></td>'+
      '<td>'+num(r.ltp)+'</td><td>'+num(r.bid)+' / '+num(r.ask)+'</td><td>'+momCell(r)+'</td><td>'+r.bars+'/'+r.need+'</td>'+
      '<td>'+(r.next_level||'<span class="hint">above both</span>')+'</td><td>'+(r.distance==null?'-':'+'+num(r.distance))+'</td>'+
      '<td class="wrap">'+(r.in_position?'<b class="g">in a position</b>':esc(r.status))+'</td></tr>'),
      !S?'Loading...':(!S.running?'Stopped - press Start. Contracts appear once prices arrive.':
      (String(S.market).indexOf('OPEN')===0?'Waiting for the first option-chain call.':
       'Market closed - contracts are built from the first prices after 09:15.'))));
  }catch(e){}
  lanesBusy=false;
}
['#f_exp','#f_side','#f_near'].forEach(id=>$(id).addEventListener('change',loadLanes));

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
function statCard(k,v,c,h){return '<div class="card"><div class="k">'+k+'</div><div class="v '+(c||'')+'">'+v+'</div>'+(h?'<div class="hint">'+h+'</div>':'')+'</div>';}
function breakCard(title,g){const ks=Object.keys(g||{}).sort();return '<div class="card"><h3>'+title+'</h3>'+
  table(['','Trades','Win rate','P&amp;L'],ks.map(k=>'<tr><td>'+(k==='CE'||k==='PE'?tag(k):esc(k))+'</td><td>'+g[k].n+'</td><td>'+(g[k].n?Math.round(g[k].wins/g[k].n*100):0)+'%</td><td class="'+cls(g[k].pnl)+'">'+inr(g[k].pnl,0)+'</td></tr>'),'-')+'</div>';}
let REPORT=null;
async function loadReport(){
  try{REPORT=await get('/api/history');}catch(e){$('#r_total').textContent=e.message;return;}
  const st=REPORT.stats;
  $('#r_total').textContent='Realized P&L: '+inr(st.total); $('#r_total').className='big '+cls(st.total);
  setHTML($('#r_stats'),statCard('TRADES',st.trades,'',st.wins+' won / '+st.losses+' lost')+
    statCard('WIN RATE',st.win_rate+'%',st.win_rate>=50?'g':'r')+
    statCard('AVG WIN',inr(st.avg_win,0),'g','best '+inr(st.best,0))+
    statCard('AVG LOSS',inr(st.avg_loss,0),st.losses?'r':'','worst '+inr(st.worst,0))+
    statCard('PROFIT FACTOR',st.profit_factor==null?'-':(st.profit_factor==='inf'?'\u221e':st.profit_factor),
      st.profit_factor==null?'':((st.profit_factor==='inf'||st.profit_factor>=1)?'g':'r'),st.profit_factor==='inf'?'no losing trade yet':'gross wins / gross losses')+
    statCard('MAX DRAWDOWN',inr(st.max_drawdown,0),st.max_drawdown<0?'r':'','deepest fall from a peak'));
  equityChart($('#r_chart'),st.series);
  setHTML($('#r_break'),breakCard('BY SIDE',st.by_side)+breakCard('BY LEVEL',st.by_leg)+breakCard('BY EXIT REASON',st.by_reason));
  const rows=REPORT.rows.slice().reverse();
  setHTML($('#r_table'),table(['<input type="checkbox" id="r_all">','Closed','Contract','Leg','Opened','Entry','Exit','Qty','P&amp;L','Why'],rows.map(t=>
    '<tr><td><input type="checkbox" class="r_chk" value="'+esc(t.id)+'"></td><td class="mono">'+esc(String(t.closed||'').slice(0,16))+'</td><td>'+contractCell(t)+'</td>'+
    '<td>'+esc(t.leg)+'</td><td class="mono">'+esc(String(t.opened||'').slice(5,16))+'</td><td>'+num(t.entry)+'</td><td>'+num(t.exit)+'</td><td>'+esc(t.qty)+'</td>'+
    '<td class="'+cls(t.pnl)+'"><b>'+inr(t.pnl,0)+'</b></td><td class="hint">'+esc(t.reason)+'</td></tr>'),'No closed trades yet.'));
}
document.addEventListener('change',e=>{if(e.target.id==='r_all')$$('.r_chk').forEach(c=>c.checked=e.target.checked);});
$('#b_clear').onclick=async()=>{const ids=$$('.r_chk').filter(c=>c.checked).map(c=>c.value);
  if(!ids.length){alert('Tick the trades to clear first.');return;}
  if(!confirm('Remove '+ids.length+' trade(s) from the report? They are moved to trades_removed.jsonl, not destroyed.'))return;
  try{await post('/api/history/clear',{ids});}catch(e){alert(e.message);} loadReport();};
$('#b_wipe').onclick=async()=>{if(!confirm('Remove EVERY trade from the report?\n\nThey are moved to trades_removed.jsonl, not destroyed.'))return;
  try{await post('/api/history/wipe');}catch(e){alert(e.message);} loadReport();};
window.addEventListener('resize',()=>{if(TAB==='report'&&REPORT)equityChart($('#r_chart'),REPORT.stats.series);});

/* ---------- activity ---------- */
const KINDS=['entry','exit','signal','skip','contract','gap','config','control','report','token','api','vix','day','boot','error'];
KINDS.forEach(k=>{const o=document.createElement('option');o.value=k;o.textContent=k;$('#a_kind').appendChild(o);});
let EV=[],evDone=false,evSeq=0;
async function loadEvents(reset){
  // Only the newest request may write: a double click or a quick filter
  // change must not duplicate rows or mix kinds.
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
const NUMS=['level2','level3','mom_length','mom_threshold','trail_l2_pct','trail_l3_pct','move_rupees','confirm_minutes','bar_seconds','lots','max_trades_per_day','max_open','strikes_each_side'];
let touched=false,expTouched=false,MAXEXP=4,lastList='';
$('#p-settings').addEventListener('input',()=>{touched=true;countNote();});
$('#p-settings').addEventListener('change',e=>{touched=true;
  if(e.target.closest('#s_exps')){expTouched=true;enforceMax();}
  if(e.target.id==='t_CE'||e.target.id==='t_PE')sideChips();
  if(e.target.name==='smode')modeUI();
  countNote();});
function dteLabel(e){const d=Math.round((new Date(e+'T00:00:00')-new Date(new Date().toDateString()))/864e5);return d<=0?'today':(d===1?'1 day':d+' days');}
function chosenExps(){return $$('#s_exps input:checked').map(b=>b.value);}
function paintExps(list,chosen){
  $('#s_exps').innerHTML=(list||[]).map(e=>'<label class="chip'+(chosen.includes(e)?' on':'')+'"><input type="checkbox" value="'+esc(e)+'"'+(chosen.includes(e)?' checked':'')+'> '+esc(e)+' <small>'+dteLabel(e)+'</small></label>').join('')
    ||'<span class="hint">Expiries load once the broker token works.</span>';
  enforceMax();}
function enforceMax(){const bs=$$('#s_exps input'),n=bs.filter(b=>b.checked).length;
  bs.forEach(b=>{const full=!b.checked&&n>=MAXEXP;b.disabled=full;b.parentElement.classList.toggle('dis',full);b.parentElement.classList.toggle('on',b.checked);});
  $('#s_expnote').textContent=n+' of '+MAXEXP+' chosen.';}
function sideChips(){['CE','PE'].forEach(t=>$('#chip_'+t).classList.toggle('on',$('#t_'+t).checked));}
function modeUI(){const atm=$('#m_atm').checked;$('#c_strikes_each_side').disabled=!atm;$('#c_strike_list').disabled=!$('#m_list').checked;}
function countNote(){const e=$$('#s_exps input').length?chosenExps().length:(S?S.cfg.expiries.length:0),sd=['CE','PE'].filter(t=>$('#t_'+t).checked).length;
  const per=$('#m_atmonly').checked?1:($('#m_atm').checked?(2*Math.max(0,Number($('#c_strikes_each_side').value)||0)+1):$('#c_strike_list').value.split(/[\s,;]+/).filter(Boolean).length);
  $('#s_count').textContent='= '+(e*sd*per)+' contracts ('+e+' expir'+(e===1?'y':'ies')+' x '+sd+' side'+(sd===1?'':'s')+' x '+per+' strike'+(per===1?'':'s')+'). One option-chain call per expiry covers every strike.';}
function paintSettings(s){
  MAXEXP=s.max_expiries;$('#maxexp').textContent=MAXEXP;
  const key=(s.expiry_list||[]).join(',');
  // The chips are repainted whenever the list itself changes - keeping what
  // is ticked on screen if the form is mid-edit - so they always appear.
  // Ticks come from the screen only if the user actually changed an expiry
  // chip; otherwise from the saved settings (chips may not have existed yet).
  if(key!==lastList||!$('#s_exps').children.length){const keep=expTouched?chosenExps():s.cfg.expiries;lastList=key;paintExps(s.expiry_list,keep);}
  const fx=$('#f_exp'),want=s.cfg.expiries.join(',');
  if(fx.dataset.k!==want){const cur=fx.value;fx.dataset.k=want;
    fx.innerHTML='<option value="">All expiries</option>'+s.cfg.expiries.map(e=>'<option value="'+esc(e)+'">'+esc(e)+'</option>').join('');
    fx.value=s.cfg.expiries.includes(cur)?cur:'';}
  $('#s_tok').textContent='Token '+s.token.human+' - from '+s.token.source+(s.token.client_id?' - client '+s.token.client_id:'')+
    '. Change it in NIFTY Trader\'s Broker token screen; this strategy restarts with it automatically.';
  $('#s_foot').textContent='Lot size '+s.lot+' (each contract uses its own lot from the scrip master). One tick = Rs '+s.tick+
    '. Strikes are multiples of '+s.strike_step+'. Bars close every '+s.cfg.bar_seconds+'s, anchored to 09:15; signals are only taken on a closed bar.';
  if(touched)return;
  $$('#s_exps input').forEach(b=>b.checked=s.cfg.expiries.includes(b.value));enforceMax();
  ['CE','PE'].forEach(t=>$('#t_'+t).checked=s.cfg.opt_types.includes(t));sideChips();
  const only=s.cfg.strike_mode!=='list'&&!s.cfg.strikes_each_side;
  $('#m_atmonly').checked=only;$('#m_atm').checked=s.cfg.strike_mode!=='list'&&!only;$('#m_list').checked=s.cfg.strike_mode==='list';
  $('#c_strike_list').value=(s.cfg.strike_list||[]).map(x=>Math.round(x)).join(', ');
  NUMS.forEach(k=>{const el=$('#c_'+k);if(el&&s.cfg[k]!=null)el.value=s.cfg[k];});
  if(only)$('#c_strikes_each_side').value=5;       // a sensible width if they switch to 'Around ATM'
  modeUI();countNote();
}
$('#b_save').onclick=async()=>{
  const b={};
  for(const k of NUMS){const el=$('#c_'+k);if(el.disabled)continue;
    if(el.value.trim()===''){alert(el.closest('.fl,.row').querySelector('label').textContent.trim()+' is empty.');el.focus();return;}
    b[k]=Number(el.value);}
  if($$('#s_exps input').length)b.expiries=chosenExps();   // no chips yet: keep the saved list
  b.opt_types=['CE','PE'].filter(t=>$('#t_'+t).checked);
  b.strike_mode=$('#m_list').checked?'list':'atm';
  if($('#m_atmonly').checked)b.strikes_each_side=0;
  if(b.strike_mode==='list'){b.strike_list=$('#c_strike_list').value;
    const bad=b.strike_list.split(/[\s,;]+/).filter(Boolean).filter(x=>!(Number(x)>0&&Number(x)%100===0));
    if(bad.length){alert('Strikes must be multiples of 100 - not '+bad.join(', '));return;}}
  try{await post('/api/config',b);touched=false;expTouched=false;poll();}catch(e){alert(e.message);}
};
$('#b_revert').onclick=()=>{touched=false;expTouched=false;lastList='';poll();};
$('#b_reset').onclick=async()=>{if(confirm('Clear collected bars on every contract? Momentum restarts from nothing.')){await post('/api/reset-bars');poll();}};

/* ---------- controls ---------- */
$('#b_start').onclick=async()=>{try{await post('/api/start');poll();}catch(e){alert(e.message);}};
$('#b_stop').onclick=async()=>{await post('/api/stop');poll();};
$('#b_flat').onclick=async()=>{if(!S||!S.open_count){alert('No open positions.');return;}
  if(!confirm('Close ALL '+S.open_count+' open positions at the live bid?'))return;
  try{const d=await post('/api/flatten',{});poll();report(d);}catch(e){alert(e.message);}};
document.addEventListener('click',async e=>{const b=e.target.closest('[data-close]');if(!b)return;
  if(!confirm('Close '+b.dataset.name+' at the live bid?'))return;
  try{const d=await post('/api/flatten',{key:b.dataset.close});poll();report(d);}catch(err){alert(err.message);}});
function report(d){const m=(d.closed||[]).filter(c=>c.reason==='MANUAL_LAST_MARK');
  if(m.length)alert('No live price for '+m.map(c=>c.contract).join(', ')+' - closed at the last mark instead.');}

showTab(store.get('lc_tab')||'dash');
poll();setInterval(poll,3000);
setInterval(()=>{if(TAB==='report')loadReport();},20000);
</script></body></html>"""


# ─────────────────────────────────────────────────────────────────────────────
#  BOOT
# ─────────────────────────────────────────────────────────────────────────────
STATE.load()
STATE.autostart = True                  # launched = trading; the engine starts it once settings are usable
threading.Thread(target=boot_loop, name="boot", daemon=True).start()
threading.Thread(target=engine_loop, name="engine", daemon=True).start()
log_event("boot", "level-cross app up (pid %d, DATA_DIR=%s)" % (os.getpid(), DATA_DIR))

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
_MARGIN_BASIS = "option buying: premium x quantity, paid in full"
_MARGIN_OPEN = lambda p: _f(p.get("entry")) * _f(p.get("qty"))
_MARGIN_NEXT = lambda lane, lots: (_f((lane.last_quote or {}).get("ask")) or _f((lane.last_quote or {}).get("ltp"))) \
    * lot_for(lane.expiry, lane.strike, lane.opt_type) * lots


def hub_summary():
    lots = int(_f(STATE.cfg.get("lots"), 1)) or 1
    used, n, nxt = 0.0, 0, []
    with STATE.lock:
        for lane in list(STATE.lanes.values()):
            p = lane.position
            if p:
                n += 1
                used += _MARGIN_OPEN(p)
                continue
            try:
                c = _MARGIN_NEXT(lane, lots)
            except Exception:
                c = 0.0
            if c > 0:
                nxt.append(c)
    return {"margin_used": round(used), "open": n,
            "margin_next": round(min(nxt)) if nxt else None,
            "margin_next_max": round(max(nxt)) if nxt else None,
            "basis": _MARGIN_BASIS}


_CAP_OF = lambda r: _f(r.get("entry")) * _f(r.get("qty"))

def _pnl_summary(margin_used):
    today = now_ist().strftime("%Y-%m-%d")
    with STATE.lock:
        hist = list(STATE.history)
        open_pnl = sum(_f(l.position.get("pnl")) for l in STATE.lanes.values() if l.position)
    rows_today = [h for h in hist if str(h.get("closed") or "").startswith(today)]
    return _pnl_pack(rows_today, hist, lambda r: _f(r.get("pnl")), _CAP_OF, open_pnl, margin_used)


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
#  VIX KILL SWITCH  (optional for this strategy - tick it in NIFTY Trader's
#  "VIX limit" dialog).  When ticked and India VIX is ABOVE the limit: no new
#  trades, and every open position is closed (market hours).  Trading resumes
#  by itself once VIX is back at or below the limit.  Limit and tick live in
#  hub/risk.json, re-read every check.  If VIX cannot be read, nothing changes.
# ─────────────────────────────────────────────────────────────────────────────
_KILL_DEFAULT_ON = ("credit_spreads", "ema_hedge")
_KILL_RISK_FILE = _env("NIFTY_RISK_FILE") if "_env" in globals() else os.environ.get("NIFTY_RISK_FILE")
_KILL_RISK_FILE = _KILL_RISK_FILE or os.path.join(os.path.dirname(os.path.dirname(APP_DIR)), "hub", "risk.json")
KILL = {"value": None, "kill": False, "checked": 0.0, "note": "not checked yet"}


def vix_kill_settings():
    """(limit, applies to this strategy)."""
    sid = os.path.basename(APP_DIR)
    try:
        with open(_KILL_RISK_FILE, encoding="utf-8") as f:
            d = json.load(f)
        lim = float(d.get("vix_limit", 13.5))
        apply = d.get("apply") or {}
        on = bool(apply[sid]) if sid in apply else sid in _KILL_DEFAULT_ON
        return (lim if lim == lim and lim >= 0 else 13.5), on
    except (OSError, ValueError, TypeError, AttributeError):
        return 13.5, sid in _KILL_DEFAULT_ON


def kill_blocks():
    lim, on = vix_kill_settings()
    return on and lim > 0 and KILL["kill"]


def kill_step(market_open, close_all):
    lim, on = vix_kill_settings()
    if not on or lim <= 0:
        KILL.update(kill=False, note="VIX kill switch not applied to this strategy")
        return
    if time.time() - KILL["checked"] < (60 if market_open else 900):
        return
    KILL["checked"] = time.time()
    res = call_dhan("marketfeed/ltp", {"IDX_I": [21]}, timeout=10)
    node = (((res.get("data") or {}).get("IDX_I") or {}).get("21") or {}) if res.get("status") == "success" else {}
    v = _f(node.get("last_price") if isinstance(node, dict) else None)
    if v <= 0:
        KILL["note"] = "India VIX unavailable - kill switch unchanged"
        return
    kill = v > lim
    if kill != KILL["kill"]:
        log_event("vix", ("India VIX %.2f crossed ABOVE the %.2f limit - KILL SWITCH ON: no new trades, "
                          "closing every open position" if kill else
                          "India VIX %.2f is back at or below the %.2f limit - new trades allowed again") % (v, lim))
    KILL.update(value=v, kill=kill, note="India VIX %.2f, limit %.2f" % (v, lim))
    if kill and market_open:
        close_all()


def _kill_close_all():
    with STATE.lock:
        lanes = [l for l in STATE.lanes.values() if l.position]
    for lane in lanes:
        q = lane.last_quote or {}
        fresh = lane.last_quote_ts and time.time() - lane.last_quote_ts < 30
        close_position(lane, "VIX_KILL", (q.get("bid") or q.get("ltp")) if fresh else None)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(_env("PORT", "5002")), threaded=True, use_reloader=False)
