"""
Stock Options 2-EMA Cross + Momentum  -  ported from the TradingView strategy
============================================================================

The Pine script "Options 2 EMA Crossover - Buy - D (Momentum Filter)" ran on ONE
NIFTY option's chart, so `close` was that option's premium.  This app runs the
same rules on STOCK options instead: the Nifty 100 companies that have options
on NSE (the list is editable).  For every stock it watches the at-the-money
strike and N strikes either side of it (3 by default), calls and puts, on the
stock's monthly expiry.  Each contract is its own chart - its own bars, EMAs,
momentum and position - exactly as if the script were loaded on each one.

    entry   on a closed chart bar (5 minutes by default), all of:
              * premium closes above the 55 EMA        (30-minute, "EMA SL")
              * premium crosses UP through the 144 EMA (30-minute, "EMA Entry")
              * momentum  close - close 10 bars ago  above the threshold
              * premium above the minimum
            and the contract is flat and is one of the ATM +/- N strikes now.
    exit    whichever comes first.  Once a contract is entered it is priced and
            checked until it is out, even after the stock has moved and the
            strike is no longer near the money:
              * quick target   +15% within 30 minutes of the signal bar
              * EMA stop       premium closes a bar below the 55 EMA
              * target         +70%
              * profit target  open profit >= Rs 12,000
              * pre-holiday    on a Friday or the day before a holiday,
                               15:00-15:30, at least +15%

HOW THE PRICES ARE READ.  Dhan's market-quote API prices up to 1,000 contracts
in one call (1 call a second), so every contract gets a price every 2-3 s.  The
30-minute EMAs need about 12 trading days of bars before they mean anything, so
each contract's history is loaded from Dhan's intraday-chart API when it is
first watched - ATM strikes and open positions first.  Between polls the EMAs
move with the price, as TradingView's request.security() does on a live bar.

PAPER TRADING ONLY.  It places nothing with the broker.  Buys fill at the ask,
sells at the bid.  The Pine version fired webhook JSON (the secret key); this
app talks to Dhan directly with the access token NIFTY Trader injects.

WHERE THIS DIFFERS FROM THE SCRIPT, on purpose (all are settings):
  1. `close > 144` and `momentum > 5` are rupee values sized for NIFTY
     premiums.  Most ATM stock options trade at Rs 5-60, so they would almost
     never trade.  Defaults here: minimum premium Rs 5 and momentum above 3.5%
     of the premium (Rs 5 on a Rs 144 premium).  Set the unit to Rs and the
     values to 5 and 144 to run the script exactly.
  2. The script's comments say "50% Target" and "Pre-Holiday Exit 20%"; the
     code used 15% for both.  The code is what runs here.
  3. Targets use the actual fill (the ask), not the signal bar's close.
  4. Safety rules the chart never needed: at most one open position per
     stock, caps on open positions and trades per day, no entry when the
     bid/ask spread is wider than 5%, and positions still open on their
     expiry day are closed at 15:20.
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
from datetime import date, datetime, timedelta, time as dtime, timezone

import requests
from flask import Flask, Response, jsonify, request

APP_DIR = os.path.dirname(os.path.abspath(__file__))


def _env(name, default=None):
    v = os.environ.get(name)
    return v.strip() if isinstance(v, str) and v.strip() else default


DATA_DIR = _env("DATA_DIR") or os.path.join(APP_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
STATE_FILE = os.path.join(DATA_DIR, "stock_ema_state.json")
RUNTIME_FILE = os.path.join(DATA_DIR, "runtime.json")
SCRIP_CACHE = os.path.join(DATA_DIR, "scrip_stock_options.json")
# Append-only, never trimmed: every closed trade and every event, forever.
TRADES_FILE = os.path.join(DATA_DIR, "trades.jsonl")
TRADES_REMOVED_FILE = os.path.join(DATA_DIR, "trades_removed.jsonl")   # what Clear/Wipe took out
EVENTS_FILE = os.path.join(DATA_DIR, "events.jsonl")
EVENTS_MAX_BYTES = 20 * 1024 * 1024        # then rolled to events.<n>.jsonl - every archive kept

IST = timezone(timedelta(hours=5, minutes=30))
IST_OFFSET = 19800
MKT_OPEN, MKT_CLOSE = dtime(9, 15), dtime(15, 30)
PRE_FROM = dtime(8, 30)                    # spots and bar history are loaded from here
EXPIRY_DAY_EXIT = dtime(15, 20)
FNO, EQ = "NSE_FNO", "NSE_EQ"


def clock():
    """Seconds since the epoch.  Everything that decides reads the time here,
    so a test can drive the engine with a fake clock."""
    return time.time()


def now_ist(at=None):
    return datetime.fromtimestamp(clock() if at is None else at, IST)


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
AUTH_PAUSE = 60                 # after a 401/403, stop calling for this long
_auth_block = [0.0]
MAX_PER_QUOTE = 1000            # instruments in one market-quote call


def call_dhan(endpoint, payload=None, method="POST", timeout=20):
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


class Gate:
    """One call at a time on one of Dhan's rate limits, at most one per
    `interval` seconds.  Dhan's limits are per CLIENT - the other strategies in
    NIFTY Trader draw on the same allowance - so a 429 widens the gap instead of
    retrying hard, and the gap shrinks back as calls succeed again."""

    def __init__(self, name, interval, max_backoff=8.0):
        self.name, self.interval, self.max_backoff = name, interval, max_backoff
        self.lock = threading.Lock()
        self.last = 0.0
        self.backoff = 0.0

    def call(self, endpoint, payload):
        with self.lock:
            wait = self.interval + self.backoff - (time.time() - self.last)
            if wait > 0:
                time.sleep(wait)
            res = call_dhan(endpoint, payload)
            self.last = time.time()
            if res.get("_http") == 429:
                self.backoff = min(self.max_backoff, max(1.0, self.backoff * 2))
                log_event("api", "%s: rate limited by Dhan - now one call every %.1f s"
                          % (self.name, self.interval + self.backoff))
            elif res.get("_http") == 200 and self.backoff:
                self.backoff = max(0.0, self.backoff - 0.25)
        return res


QUOTE_GATE = Gate("market quote", 1.05)     # Dhan: 1 market-quote call a second
DATA_GATE = Gate("chart history", 0.25)     # Dhan: 5 data calls a second


def _chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def _quote_body(pairs):
    body = {}
    for seg, sid in pairs:
        try:
            body.setdefault(seg, []).append(int(sid))
        except (TypeError, ValueError):
            continue
    return body


def fetch_ltp(pairs):
    """Last traded price of many instruments.  pairs: [(segment, security id)].
    Returns ({(segment, sid): price}, error) - the dict is None when every call
    failed, so a dead feed is never mistaken for 'no trades'."""
    out, err, ok = {}, None, False
    for chunk in _chunks(list(dict.fromkeys(pairs)), MAX_PER_QUOTE):
        if _SHUTDOWN.is_set() or time.time() < _auth_block[0]:
            break
        res = QUOTE_GATE.call("marketfeed/ltp", _quote_body(chunk))
        if res.get("status") != "success":
            err = res.get("message") or "HTTP %s" % res.get("_http")
            continue
        ok = True
        for seg, rows in (res.get("data") or {}).items():
            if not isinstance(rows, dict):
                continue
            for sid, row in rows.items():
                px = _f(row.get("last_price")) if isinstance(row, dict) else 0.0
                if px > 0:
                    out[(seg, str(sid))] = px
    return (out if ok else None), err


def fetch_depth(sids):
    """Best bid and ask of option contracts: {sid: {"bid", "ask", "ltp"}}."""
    out = {}
    for chunk in _chunks(list(dict.fromkeys(str(s) for s in sids)), MAX_PER_QUOTE):
        if _SHUTDOWN.is_set() or time.time() < _auth_block[0]:
            break
        res = QUOTE_GATE.call("marketfeed/quote", _quote_body([(FNO, s) for s in chunk]))
        if res.get("status") != "success":
            continue
        for sid, row in ((res.get("data") or {}).get(FNO) or {}).items():
            if not isinstance(row, dict):
                continue
            depth = row.get("depth") or {}
            buy, sell = depth.get("buy") or [], depth.get("sell") or []
            bid = _f(buy[0].get("price")) if buy and isinstance(buy[0], dict) else 0.0
            ask = _f(sell[0].get("price")) if sell and isinstance(sell[0], dict) else 0.0
            out[str(sid)] = {"bid": bid, "ask": ask, "ltp": _f(row.get("last_price"))}
    return out


_DATE_STYLE = ["datetime"]      # the fromDate/toDate format Dhan last accepted


def _history_payload(sid, interval, frm, to, style):
    if style == "datetime":
        f, t = frm.strftime("%Y-%m-%d") + " 09:15:00", to.strftime("%Y-%m-%d %H:%M:%S")
    else:                                   # date only: toDate is exclusive
        f, t = frm.strftime("%Y-%m-%d"), (to + timedelta(days=1)).strftime("%Y-%m-%d")
    return {"securityId": str(sid), "exchangeSegment": FNO, "instrument": "OPTSTK",
            "interval": str(int(interval)), "oi": False, "fromDate": f, "toDate": t}


def _in_session(t):
    d = datetime.fromtimestamp(t, IST).time()
    return MKT_OPEN <= d < MKT_CLOSE


def clean_candles(stamps, closes, now_ts):
    """(start time, close) pairs inside the session, oldest first.  Candle
    times should be plain epoch seconds; if they come back shifted by IST's
    5:30 (session candles at 03:45-10:00), they are shifted back."""
    rows = []
    for t, c in zip(stamps or [], closes or []):
        t, c = _f(t, -1), _f(c)
        if t > 0 and c > 0:
            rows.append((int(t), c))
    if not rows:
        return []
    inside = sum(1 for t, _ in rows if _in_session(t))
    if sum(1 for t, _ in rows if _in_session(t + IST_OFFSET)) > inside:
        rows = [(t + IST_OFFSET, c) for t, c in rows]
    elif sum(1 for t, _ in rows if _in_session(t - IST_OFFSET)) > inside:
        rows = [(t - IST_OFFSET, c) for t, c in rows]
    out = {}
    for t, c in rows:
        if _in_session(t) and t <= now_ts + 60:
            out[t] = c
    return sorted(out.items())


def fetch_candles(sid, interval, days):
    """Intraday candles of one option contract: ([(start, close)], error).
    Only candles with trades exist, as on TradingView."""
    to = now_ist()
    frm = to - timedelta(days=days)
    styles = [_DATE_STYLE[0]] + [s for s in ("datetime", "date") if s != _DATE_STYLE[0]]
    err = None
    for style in styles:
        res = DATA_GATE.call("charts/intraday", _history_payload(sid, interval, frm, to, style))
        stamps, closes = res.get("timestamp"), res.get("close")
        if isinstance(stamps, list) and isinstance(closes, list):
            _DATE_STYLE[0] = style
            return clean_candles(stamps, closes, to.timestamp()), None
        http = res.get("_http") or 0
        err = str(res.get("message") or res.get("errorMessage") or "HTTP %s" % http)
        if http == 200 and not res.get("errorCode"):
            return [], None                 # an empty answer: no trades in the period
        if http in (0, 401, 403, 429) or http >= 500:
            break                           # not a date-format problem
    return None, err


# ─────────────────────────────────────────────────────────────────────────────
#  SCRIP MASTER  -  every NSE stock option, its lot, and each stock's share id
#  SM_SYMBOL_NAME is empty on NSE rows, so the underlying comes from
#  SEM_TRADING_SYMBOL ('RELIANCE-Oct2026-1400-CE').  It is split from the RIGHT:
#  'BAJAJ-AUTO-Oct2026-8000-CE' has a dash in the stock's own name.
# ─────────────────────────────────────────────────────────────────────────────
SCRIP_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"


def skey(strike):
    return "%.2f" % float(strike)


def parse_scrip(text):
    """{"eq": {symbol: share security id},
        "opt": {symbol: {expiry: {"lot": n, "k": {"1400.00": [ce_sid, pe_sid]}}}}}"""
    eq, eq_series, opt = {}, {}, {}
    for row in csv.DictReader(io.StringIO(text)):
        if row.get("SEM_EXM_EXCH_ID") != "NSE":
            continue
        inst = (row.get("SEM_INSTRUMENT_NAME") or "").strip()
        tsym = (row.get("SEM_TRADING_SYMBOL") or "").strip().upper()
        sid = str(row.get("SEM_SMST_SECURITY_ID") or "").strip()
        if not tsym or not sid:
            continue
        if inst == "EQUITY":
            series = (row.get("SEM_SERIES") or "").strip().upper()
            # the EQ series is the one that trades normally; anything else only
            # if nothing better turns up
            if series == "EQ" or (tsym not in eq and series in ("", "BE")):
                if series == "EQ" or eq_series.get(tsym) != "EQ":
                    eq[tsym], eq_series[tsym] = sid, series
            continue
        if inst != "OPTSTK":
            continue
        parts = tsym.rsplit("-", 3)
        typ = (row.get("SEM_OPTION_TYPE") or "").strip().upper()
        if len(parts) != 4 or typ not in ("CE", "PE"):
            continue
        try:
            strike = float(row["SEM_STRIKE_PRICE"])
            lot = int(float(row["SEM_LOT_UNITS"]))
        except (KeyError, TypeError, ValueError):
            continue
        expiry = str(row.get("SEM_EXPIRY_DATE") or "")[:10]
        if strike <= 0 or lot <= 0 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", expiry):
            continue
        e = opt.setdefault(parts[0], {}).setdefault(expiry, {"lot": lot, "k": {}})
        pair = e["k"].setdefault(skey(strike), [None, None])
        pair[0 if typ == "CE" else 1] = sid
    return {"eq": {s: v for s, v in eq.items() if s in opt}, "opt": opt}


def load_scrip():
    """Today's copy from the cache, else a fresh download (~25 MB), else the
    last cached copy - an older list is still usable for a day."""
    today = now_ist().strftime("%Y-%m-%d")
    cached = read_json_safe(SCRIP_CACHE, default=None)
    ok = isinstance(cached, dict) and cached.get("opt")
    if ok and cached.get("date") == today:
        return cached
    try:
        t0 = time.time()
        r = requests.get(SCRIP_URL, timeout=180)
        r.raise_for_status()
        sc = parse_scrip(r.content.decode("utf-8", "replace"))
        if not sc["opt"]:
            raise ValueError("no NSE stock options (OPTSTK) found in the scrip master")
        sc["date"] = today
        write_json_atomic(SCRIP_CACHE, sc, backups=1)
        log_event("boot", "scrip master downloaded in %.0fs: %d stocks with options"
                  % (time.time() - t0, len(sc["opt"])))
        return sc
    except Exception as e:
        log_event("error", "scrip master: %s" % e)
        if ok:
            log_event("boot", "using the scrip master saved on %s" % cached.get("date"))
            return cached
        return None


# ─────────────────────────────────────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────────────────────────────────────
# The Nifty 50 and Nifty Next 50 as of 2026.  Anything here without stock
# options on NSE is skipped and listed in Settings; edit the list freely.
NIFTY100 = [
    "ADANIENT", "ADANIPORTS", "APOLLOHOSP", "ASIANPAINT", "AXISBANK", "BAJAJ-AUTO",
    "BAJFINANCE", "BAJAJFINSV", "BEL", "BHARTIARTL", "CIPLA", "COALINDIA", "DRREDDY",
    "EICHERMOT", "ETERNAL", "GRASIM", "HCLTECH", "HDFCBANK", "HDFCLIFE", "HINDALCO",
    "HINDUNILVR", "ICICIBANK", "INDIGO", "INFY", "ITC", "JIOFIN", "JSWSTEEL", "KOTAKBANK",
    "LT", "M&M", "MARUTI", "MAXHEALTH", "NESTLEIND", "NTPC", "ONGC", "POWERGRID",
    "RELIANCE", "SBILIFE", "SBIN", "SHRIRAMFIN", "SUNPHARMA", "TATACONSUM", "TMPV",
    "TATASTEEL", "TCS", "TECHM", "TITAN", "TRENT", "ULTRACEMCO", "WIPRO",
    "ABB", "ADANIENSOL", "ADANIGREEN", "ADANIPOWER", "AMBUJACEM", "BAJAJHLDNG",
    "BANKBARODA", "BOSCHLTD", "BPCL", "BRITANNIA", "CANBK", "CGPOWER", "CHOLAFIN",
    "DABUR", "DIVISLAB", "DLF", "DMART", "GAIL", "GODREJCP", "HAL", "HAVELLS",
    "HEROMOTOCO", "HINDZINC", "HYUNDAI", "ICICIGI", "INDHOTEL", "INDUSINDBK", "IOC",
    "IRFC", "JINDALSTEL", "JSWENERGY", "LICI", "LODHA", "LTIM", "MOTHERSON", "NAUKRI",
    "PFC", "PIDILITIND", "PNB", "RECLTD", "SHREECEM", "SIEMENS", "SOLARINDS",
    "TORNTPHARM", "TVSMOTOR", "UNITDSPR", "VBL", "VEDL", "ZYDUSLIFE", "TATAPOWER",
]

# From the Pine script's holiday input.  Used for the pre-holiday exit and to
# know the market is shut.
HOLIDAYS = ["2026-04-03", "2026-05-28", "2026-06-26", "2026-08-15", "2026-09-14",
            "2026-10-02", "2026-10-20", "2026-11-10", "2026-11-24", "2026-12-25",
            "2027-01-26", "2027-03-06", "2027-03-10", "2027-03-22", "2027-03-26"]

BAR_CHOICES = (1, 3, 5, 10, 15)            # chart bar, minutes
EMA_TF_CHOICES = (15, 30, 60)              # EMA time frame, minutes (the script: 30)
MAX_SYMBOLS = 200
MAX_EACH_SIDE = 5
KEEP_EXTRA = 1              # a strike drifting out of the window is kept 1 step longer
EMA_HISTORY_DAYS = 45       # calendar days of 15-minute candles behind the EMAs
BAR_HISTORY_DAYS = 5        # calendar days of chart-bar candles behind momentum
BAR_MEMORY = 300            # closed chart bars kept per contract
PENDING_MAX = 4000          # prices kept while a contract's history loads

DEFAULTS = {
    "symbols": list(NIFTY100),
    "opt_types": ["CE", "PE"],
    "strikes_each_side": 3,            # ATM +/- 3 strikes
    "roll_days": 3,                    # move to next month when fewer days are left
    "bar_minutes": 5,
    "ema_minutes": 30,                 # timeFrame
    "ema_sl_len": 55,                  # emaLength1 "EMA SL"
    "ema_entry_len": 144,              # emaLength2 "EMA Entry"
    "mom_length": 10,
    "mom_unit": "pct",                 # "pct" of the premium N bars ago, or "rs"
    "mom_threshold": 3.5,
    "min_premium": 5.0,                # the script's close > 144
    "quick_target_pct": 15.0,          # close >= entry * 1.15 ...
    "quick_minutes": 30,               # ... within 30 minutes
    "target_pct": 70.0,                # longTargetPct
    "profit_target_rs": 12000.0,       # targetProfitRs
    "preholiday_pct": 15.0,
    "holidays": list(HOLIDAYS),
    "ema_stop_on_tick": False,         # False: the EMA stop needs a bar CLOSE below, as the script
    "max_spread_pct": 5.0,             # 0 = buy whatever the spread
    "lots": 1,
    "max_open": 5,
    "max_per_stock": 1,
    "max_trades_per_day": 20,
}

# Checked on Save: the value must be a real number inside this range.
RANGES = {
    "strikes_each_side": (0, MAX_EACH_SIDE), "roll_days": (0, 20),
    "bar_minutes": (1, 15), "ema_minutes": (15, 60),
    "ema_sl_len": (2, 300), "ema_entry_len": (2, 300),
    "mom_length": (1, 100), "mom_threshold": (0, 100000), "min_premium": (0, 100000),
    "quick_target_pct": (0.1, 1000), "quick_minutes": (0, 375), "target_pct": (0.1, 10000),
    "profit_target_rs": (1, 100000000), "preholiday_pct": (0, 1000),
    "max_spread_pct": (0, 100), "lots": (1, 50), "max_open": (1, 200),
    "max_per_stock": (1, 20), "max_trades_per_day": (1, 1000),
}
LABELS = {
    "strikes_each_side": "Strikes each side of ATM", "roll_days": "Roll to next expiry",
    "bar_minutes": "Chart bar", "ema_minutes": "EMA time frame",
    "ema_sl_len": "EMA SL length", "ema_entry_len": "EMA Entry length",
    "mom_length": "Momentum length", "mom_threshold": "Momentum threshold",
    "min_premium": "Minimum premium", "quick_target_pct": "Quick target",
    "quick_minutes": "Quick target window", "target_pct": "Target",
    "profit_target_rs": "Profit target", "preholiday_pct": "Pre-holiday exit",
    "max_spread_pct": "Widest spread", "lots": "Lots", "max_open": "Max open at once",
    "max_per_stock": "Max open per stock", "max_trades_per_day": "Max trades per day",
}
_INT_KEYS = ("strikes_each_side", "roll_days", "bar_minutes", "ema_minutes", "ema_sl_len",
             "ema_entry_len", "mom_length", "quick_minutes", "lots", "max_open",
             "max_per_stock", "max_trades_per_day")
_SYM_RE = re.compile(r"^[A-Z0-9&_\-]{1,30}$")


def parse_symbols(v):
    """A list, or text like 'RELIANCE, TCS  INFY'.  Upper-cased, de-duplicated."""
    if isinstance(v, str):
        v = re.split(r"[\s,;]+", v.strip())
    if not isinstance(v, (list, tuple)):
        return []
    out = []
    for x in v:
        s = str(x or "").strip().upper()
        if s and _SYM_RE.match(s) and s not in out:
            out.append(s)
    return out


def parse_dates(v):
    if isinstance(v, (list, tuple)):
        v = " ".join(str(x) for x in v)
    return sorted(set(re.findall(r"\d{4}-\d{2}-\d{2}", str(v or ""))))


def clean_cfg(d):
    c = dict(DEFAULTS)
    c.update({k: v for k, v in dict(d or {}).items() if k in DEFAULTS})
    c["symbols"] = parse_symbols(c["symbols"])[:MAX_SYMBOLS]
    raw = c["opt_types"] if isinstance(c["opt_types"], (list, tuple)) else [c["opt_types"]]
    want = {str(t).upper() for t in raw}
    c["opt_types"] = [t for t in ("CE", "PE") if t in want]
    c["holidays"] = parse_dates(c["holidays"])
    c["mom_unit"] = "rs" if str(c["mom_unit"]).lower() == "rs" else "pct"
    c["ema_stop_on_tick"] = bool(c["ema_stop_on_tick"]) and str(c["ema_stop_on_tick"]).lower() not in ("0", "false", "no")
    for k in _INT_KEYS:
        lo, hi = RANGES[k]
        c[k] = max(int(lo), min(int(hi), int(round(_f(c[k], DEFAULTS[k])))))
    for k in ("mom_threshold", "min_premium", "quick_target_pct", "target_pct",
              "profit_target_rs", "preholiday_pct", "max_spread_pct"):
        lo, hi = RANGES[k]
        c[k] = max(lo, min(hi, _f(c[k], DEFAULTS[k])))
    if c["bar_minutes"] not in BAR_CHOICES:
        c["bar_minutes"] = DEFAULTS["bar_minutes"]
    if c["ema_minutes"] not in EMA_TF_CHOICES:
        c["ema_minutes"] = DEFAULTS["ema_minutes"]
    return c


def validate_cfg(c):
    """Errors a user can fix, in words.  None when all is well."""
    if not c["symbols"]:
        return "List at least one stock, e.g. RELIANCE, TCS, INFY."
    if not c["opt_types"]:
        return "Choose CE, PE or both."
    if c["bar_minutes"] not in BAR_CHOICES:
        return "Chart bar must be one of %s minutes." % ", ".join(map(str, BAR_CHOICES))
    if c["ema_minutes"] not in EMA_TF_CHOICES:
        return "EMA time frame must be one of %s minutes." % ", ".join(map(str, EMA_TF_CHOICES))
    if c["ema_minutes"] % c["bar_minutes"]:
        return ("The EMA time frame (%d min) must be a whole number of chart bars (%d min)."
                % (c["ema_minutes"], c["bar_minutes"]))
    return None


def series_sig(cfg):
    """What a contract's bar history was built with.  Change any of these and
    every contract's history is loaded again."""
    return (cfg["bar_minutes"], cfg["ema_minutes"], cfg["ema_sl_len"], cfg["ema_entry_len"])


# ─────────────────────────────────────────────────────────────────────────────
#  BARS AND EMAS
# ─────────────────────────────────────────────────────────────────────────────
def _ist(t):
    return datetime.fromtimestamp(t, IST)


def slot_of(at, span):
    """Bars are anchored to the 09:15 IST session open, as TradingView's are."""
    d = _ist(at)
    anchor = datetime(d.year, d.month, d.day, MKT_OPEN.hour, MKT_OPEN.minute, tzinfo=IST).timestamp()
    return anchor + math.floor((at - anchor) / span) * span


class Series:
    """One contract's chart: closed chart bars, and two EMAs of its premium on
    the higher time frame.

    Pine: ema = request.security(ticker, "30", ta.ema(close, n)).  On a live
    chart that is the EMA of the finished 30-minute bars, moved by the price of
    the 30-minute bar still forming.  So each chart bar, when it closes, stores
    the EMA values as they stood at that moment (e1, e2) - that is what
    ema[1] reads on TradingView."""

    def __init__(self, cfg):
        self.span = cfg["bar_minutes"] * 60
        self.hspan = cfg["ema_minutes"] * 60
        self.lens = (cfg["ema_sl_len"], cfg["ema_entry_len"])
        self.bars = []            # closed chart bars {t, o, h, l, c, e1, e2}
        self.cur = None           # the chart bar still forming
        self.h_t = None           # the EMA-time-frame bar still forming: start ...
        self.h_c = None           # ... and its latest price
        self.n = 0                # finished EMA-time-frame bars
        self.seed = [0.0, 0.0]    # each EMA starts from the SMA of its first n bars
        self.e = [None, None]     # EMAs through the finished bars
        self.last_at = 0.0        # the data is complete up to here

    def _finish_htf(self, close):
        self.n += 1
        for i, n in enumerate(self.lens):
            if self.e[i] is None:
                self.seed[i] += close
                if self.n == n:
                    self.e[i] = self.seed[i] / n
            else:
                a = 2.0 / (n + 1)
                self.e[i] = a * close + (1 - a) * self.e[i]

    def push_htf(self, px, at):
        h = slot_of(at, self.hspan)
        if self.h_t is not None and h != self.h_t:
            if h < self.h_t:
                return
            self._finish_htf(self.h_c)
            self.h_t = None
        if self.h_t is None:
            self.h_t = h
        self.h_c = px

    def ema(self, i):
        """EMA i (0 = SL, 1 = entry) right now, the forming bar included."""
        if self.e[i] is None:
            return None
        if self.h_t is None:
            return self.e[i]
        a = 2.0 / (self.lens[i] + 1)
        return a * self.h_c + (1 - a) * self.e[i]

    def push(self, px, at):
        """Fold one price in.  Returns the chart bars it closed."""
        slot = slot_of(at, self.span)
        closed = []
        if self.cur is not None and slot != self.cur["t"]:
            if slot < self.cur["t"]:
                return []                       # never let the clock run backwards
            bar = self.cur
            # The EMA state still ends at this bar's last price: exactly the
            # values the chart showed when the bar closed.
            bar["e1"], bar["e2"] = self.ema(0), self.ema(1)
            self.bars.append(bar)
            if len(self.bars) > BAR_MEMORY:
                del self.bars[:-BAR_MEMORY]
            closed.append(bar)
            self.cur = None
        self.push_htf(px, at)
        if self.cur is None:
            self.cur = {"t": slot, "o": px, "h": px, "l": px, "c": px}
        else:
            self.cur["h"] = max(self.cur["h"], px)
            self.cur["l"] = min(self.cur["l"], px)
            self.cur["c"] = px
        self.last_at = max(self.last_at, at)
        return closed

    def momentum(self, m, idx=None):
        """Pine close - close[m] on closed bars: (rupees, the old close)."""
        idx = len(self.bars) - 1 if idx is None else idx
        if idx < m or idx >= len(self.bars):
            return None, None
        return self.bars[idx]["c"] - self.bars[idx - m]["c"], self.bars[idx - m]["c"]


def build_series(cfg, htf_candles, bar_candles, complete_to):
    """A contract's chart from its history.  The EMAs come from 15-minute
    candles going back EMA_HISTORY_DAYS; the chart bars from the finer candles
    of the last few days, which take over where they start."""
    s = Series(cfg)
    b0 = bar_candles[0][0] if bar_candles else None
    for t, c in htf_candles or []:
        if b0 is not None and t >= b0:
            break
        s.push_htf(c, t)
    for t, c in bar_candles or []:
        s.push(c, t)
    # No candle means no trade: the history is complete up to when it was read.
    s.last_at = max(s.last_at, complete_to)
    return s


def base_interval(bar_minutes):
    """The Dhan candle size the chart bars are built from."""
    return 15 if bar_minutes == 15 else (5 if bar_minutes % 5 == 0 else 1)


# ─────────────────────────────────────────────────────────────────────────────
#  STATE
# ─────────────────────────────────────────────────────────────────────────────
def fmt_strike(k):
    v = float(k)
    return "%d" % v if v == int(v) else ("%.2f" % v).rstrip("0").rstrip(".")


def fmt_expiry(e):
    try:
        return datetime.strptime(e, "%Y-%m-%d").strftime("%d %b")
    except ValueError:
        return str(e)


def lane_key(sym, expiry, strike, typ):
    return "%s|%s|%s|%s" % (sym, expiry, skey(strike), typ)


def contract_label(sym, expiry, strike, typ):
    return "%s %s %s %s" % (sym, fmt_strike(strike), typ, fmt_expiry(expiry))


class Lane:
    """One contract: a stock, an expiry, a side and a FIXED strike - one chart."""

    def __init__(self, sym, expiry, strike, typ, sid, lot):
        self.sym, self.expiry, self.strike, self.opt_type = sym, expiry, float(strike), typ
        self.sid, self.lot = str(sid), int(lot or 1)
        self.series = None
        self.series_sig = None
        self.ready = False            # history loaded and live prices flowing into it
        self.warm = "queued"          # queued / loading / ready
        self.warm_fails = 0
        self.warm_after = 0.0
        self.warm_note = ""
        self.warm_sig = None
        self.pending = []             # (at, price) that arrived while the history loaded
        self.fetch_started = 0.0
        self.position = None
        self.ltp, self.ltp_ts = None, 0.0
        self.bid = self.ask = None
        self.quote_ts = 0.0
        self.status = "waiting for its bar history"

    @property
    def key(self):
        return lane_key(self.sym, self.expiry, self.strike, self.opt_type)

    @property
    def label(self):
        return contract_label(self.sym, self.expiry, self.strike, self.opt_type)


class Book:
    def __init__(self):
        self.lock = threading.RLock()
        self.cfg = clean_cfg({})
        self.running = False
        # Launching the strategy from NIFTY Trader starts it once the stock
        # list has loaded.  Stop cancels that.
        self.autostart = False
        self.scrip = None
        self.scrip_day = None
        self.strike_cache = {}
        self.universe = []            # listed stocks that have options
        self.skipped = {}             # listed stocks that don't: symbol -> why
        self.spots = {}               # symbol -> share price
        self.sym_info = {}            # symbol -> expiry, strikes, ATM
        self.lanes = {}               # lane key -> Lane.  ONLY the engine thread adds or drops.
        self.history = []             # every closed trade, oldest first (mirrors trades.jsonl)
        self.unflushed = []           # closed trades not yet safely in trades.jsonl
        self.trades_today = 0
        self.day = now_ist().strftime("%Y-%m-%d")
        self.status = "starting"
        self.market_note = ""
        self.last_save = 0.0
        self.last_spot_poll = 0.0
        self.last_pass = 0.0
        self.pass_seconds = None
        self.warm_all_logged = False

    def open_count(self):
        with self.lock:
            return sum(1 for l in self.lanes.values() if l.position)

    # ---- persistence ----
    def snapshot(self):
        return {"schema": 1, "saved_at": ts(), "cfg": self.cfg,
                "positions": [dict(l.position) for l in self.lanes.values() if l.position],
                "unflushed_trades": self.unflushed,
                "trades_today": self.trades_today, "day": self.day}

    def save(self):
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
            self.trades_today = int(_f(d.get("trades_today")))
            self.unflushed = [r for r in (d.get("unflushed_trades") or []) if isinstance(r, dict)]
            for pos in d.get("positions") or []:
                try:
                    lane = Lane(pos["sym"], pos["expiry"], pos["strike"], pos["opt_type"],
                                pos["sid"], pos.get("lot") or 1)
                except (KeyError, TypeError, ValueError):
                    continue
                pos["lane"] = lane.key
                lane.position = pos
                self.lanes[lane.key] = lane
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
        self.running = False


def ts():
    return now_ist().strftime("%Y-%m-%d %H:%M:%S")


# ---- the trade book on disk ----
def trade_key(r):
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
def is_trading_day(d):
    return d.weekday() < 5 and d.isoformat() not in STATE.cfg["holidays"]


def market_state(at=None):
    now = now_ist(at)
    if now.weekday() >= 5:
        return "CLOSED", "weekend"
    if not is_trading_day(now.date()):
        return "CLOSED", "exchange holiday"
    t = now.time()
    if t < PRE_FROM:
        return "CLOSED", "opens 09:15 IST"
    if t < MKT_OPEN:
        return "PRE", "pre-open, starts 09:15 IST"
    if t > MKT_CLOSE:
        return "CLOSED", "after close"
    return "OPEN", "session live"


def session_seconds(a, b):
    """Seconds of trading session between two instants - what a gap in the
    prices really cost.  A night or a weekend costs nothing."""
    if b <= a:
        return 0.0
    total, d, end = 0.0, _ist(a).date(), _ist(b).date()
    if (end - d).days > 40:
        return float("inf")
    while d <= end:
        if is_trading_day(d):
            o = datetime(d.year, d.month, d.day, MKT_OPEN.hour, MKT_OPEN.minute, tzinfo=IST).timestamp()
            c = datetime(d.year, d.month, d.day, MKT_CLOSE.hour, MKT_CLOSE.minute, tzinfo=IST).timestamp()
            total += max(0.0, min(b, c) - max(a, o))
        d += timedelta(days=1)
    return total


def rewarm_after(span):
    """A hole in the live prices longer than this reloads the contract's history."""
    return max(3 * span, 180)


def dte_of(expiry, at=None):
    try:
        return (datetime.strptime(expiry, "%Y-%m-%d").date() - now_ist(at).date()).days
    except ValueError:
        return None


# ─────────────────────────────────────────────────────────────────────────────
#  CONTRACTS  (only the engine thread adds or drops them)
# ─────────────────────────────────────────────────────────────────────────────
def refresh_universe():
    sc = STATE.scrip
    if not sc:
        return
    uni, skipped = [], {}
    for sym in STATE.cfg["symbols"]:
        if sym not in sc["opt"]:
            skipped[sym] = "no stock options on NSE"
        elif sym not in sc["eq"]:
            skipped[sym] = "share price id not found"
        else:
            uni.append(sym)
    with STATE.lock:
        STATE.universe, STATE.skipped = uni, skipped


def pick_expiry(sym, at=None):
    """The nearest expiry with at least roll_days to go."""
    today = now_ist(at).strftime("%Y-%m-%d")
    exps = sorted(e for e in (STATE.scrip or {}).get("opt", {}).get(sym, {}) if e >= today)
    for e in exps:
        if dte_of(e, at) >= STATE.cfg["roll_days"]:
            return e
    return exps[-1] if exps else None


def strikes_for(sym, expiry):
    k = (sym, expiry)
    got = STATE.strike_cache.get(k)
    if got is None:
        got = sorted(float(x) for x in STATE.scrip["opt"][sym][expiry]["k"])
        STATE.strike_cache[k] = got
    return got


def update_spots(syms, ltp, at):
    with STATE.lock:
        for sym in syms:
            sid = (STATE.scrip or {}).get("eq", {}).get(sym)
            px = ltp.get((EQ, str(sid))) if sid else None
            if px:
                STATE.spots[sym] = px
        STATE.last_spot_poll = at


def sync_lanes(at):
    """Centre each stock's window on its ATM strike, add the contracts in it and
    drop FLAT ones that have drifted outside.  A contract in a position is never
    dropped: its exits are checked until it is out."""
    cfg = STATE.cfg
    n = cfg["strikes_each_side"]
    added = 0
    with STATE.lock:
        keep = set()
        for sym in STATE.universe:
            spot = STATE.spots.get(sym)
            exp = pick_expiry(sym, at)
            if not spot or not exp:
                continue
            strikes = strikes_for(sym, exp)
            if not strikes:
                continue
            atm = min(strikes, key=lambda k: (abs(k - spot), -k))
            i0 = strikes.index(atm)
            info = STATE.scrip["opt"][sym][exp]
            STATE.sym_info[sym] = {"spot": spot, "expiry": exp, "strikes": strikes,
                                   "atm": atm, "atm_idx": i0, "lot": info["lot"]}
            for i in range(max(0, i0 - n - KEEP_EXTRA), min(len(strikes), i0 + n + KEEP_EXTRA + 1)):
                pair = info["k"].get(skey(strikes[i])) or [None, None]
                for side in cfg["opt_types"]:
                    sid = pair[0 if side == "CE" else 1]
                    if not sid:
                        continue
                    k = lane_key(sym, exp, strikes[i], side)
                    keep.add(k)
                    if abs(i - i0) <= n and k not in STATE.lanes:
                        STATE.lanes[k] = Lane(sym, exp, strikes[i], side, sid, info["lot"])
                        added += 1
        for sym in list(STATE.sym_info):
            if sym not in STATE.universe:
                del STATE.sym_info[sym]
        dropped = [k for k, l in STATE.lanes.items() if not l.position and k not in keep]
        for k in dropped:
            del STATE.lanes[k]
        total = len(STATE.lanes)
    if added >= 10 or len(dropped) >= 10:
        log_event("contract", "watching %d contracts on %d stocks (ATM +/- %d, %s): %d added, %d dropped"
                  % (total, len(STATE.sym_info), n, "/".join(cfg["opt_types"]), added, len(dropped)))
    return added, len(dropped)


def lane_offset(lane):
    """Strikes away from ATM right now; None when not on today's strike list."""
    info = STATE.sym_info.get(lane.sym)
    if not info or info["expiry"] != lane.expiry:
        return None
    try:
        return info["strikes"].index(lane.strike) - info["atm_idx"]
    except ValueError:
        return None


def lane_wanted(lane):
    off = lane_offset(lane)
    return (lane.sym in STATE.universe and lane.opt_type in STATE.cfg["opt_types"]
            and off is not None and abs(off) <= STATE.cfg["strikes_each_side"])


def reset_stale_series():
    """Settings that change what a bar or an EMA is make every history void."""
    sig = series_sig(STATE.cfg)
    n = 0
    with STATE.lock:
        for lane in STATE.lanes.values():
            if lane.series is not None and lane.series_sig != sig:
                requeue(lane, None)
                n += 1
    if n:
        log_event("warm", "chart settings changed - reloading the bar history of %d contracts" % n)


def requeue(lane, first_price):
    """Under STATE.lock.  The contract's chart is rebuilt from history; prices
    arriving meanwhile are kept and replayed on top."""
    lane.ready, lane.warm, lane.series = False, "queued", None
    lane.warm_fails, lane.warm_after = 0, 0.0
    lane.pending = [first_price] if first_price else []


# ─────────────────────────────────────────────────────────────────────────────
#  BAR HISTORY  (its own thread, so the engine never waits for it)
# ─────────────────────────────────────────────────────────────────────────────
def next_warm_lane(at):
    """Open positions first (their EMA stop needs the EMA), then ATM, then
    outward.  Stopped: only open positions."""
    with STATE.lock:
        best, best_k = None, None
        for lane in STATE.lanes.values():
            if lane.warm != "queued" or lane.warm_after > at:
                continue
            if not lane.position and not STATE.running:
                continue
            off = lane_offset(lane)
            k = (0 if lane.position else 1, abs(off) if off is not None else 99, lane.sym, lane.key)
            if best_k is None or k < best_k:
                best, best_k = lane, k
        if best is not None:
            best.warm = "loading"
            best.fetch_started = clock()
            best.warm_sig = series_sig(STATE.cfg)
        return best


_no_history = [0]


def warm_lane(lane):
    cfg = dict(STATE.cfg)
    sig = lane.warm_sig
    started = lane.fetch_started
    htf, err = fetch_candles(lane.sid, 15, EMA_HISTORY_DAYS)
    base = base_interval(cfg["bar_minutes"])
    if htf is None:
        bars, err2 = None, None
    elif base == 15:
        bars, err2 = htf, None
    else:
        bars, err2 = fetch_candles(lane.sid, base, BAR_HISTORY_DAYS)
    err = err or err2
    with STATE.lock:
        if STATE.lanes.get(lane.key) is not lane:
            return                                    # dropped meanwhile
        if sig != series_sig(STATE.cfg):
            requeue(lane, None)                       # settings changed meanwhile
            return
        if htf is None or bars is None:
            lane.warm_fails += 1
            if lane.warm_fails < 3:
                lane.warm, lane.warm_after = "queued", clock() + 30 * lane.warm_fails
                lane.warm_note = "history failed (%s) - retrying" % err
                return
            # The broker will not give it: build the chart from live prices.
            htf, bars = [], []
            lane.warm_note = "no history from the broker (%s) - bars build from live prices" % err
            _no_history[0] += 1
            if _no_history[0] <= 5 or _no_history[0] % 100 == 0:
                log_event("warm", "%s: %s (%d contract%s so far)" % (
                    lane.label, lane.warm_note, _no_history[0], "" if _no_history[0] == 1 else "s"))
        else:
            lane.warm_note = "%d history candles" % (len(htf) + (0 if base == 15 else len(bars)))
        s = build_series(cfg, htf, bars, started)
        for at, px in lane.pending:
            if at >= started:
                s.push(px, at)
                s.last_at = max(s.last_at, at)
        lane.series, lane.series_sig = s, sig
        lane.pending = []
        lane.ready, lane.warm = True, "ready"
        lane.status = "history loaded"


def warm_once():
    """Load one contract's history.  False when there was nothing to do."""
    if time.time() < _auth_block[0]:
        return False
    tok = token_status()
    if not tok["configured"] or tok["expired"]:
        return False
    lane = next_warm_lane(clock())
    if lane is None:
        with STATE.lock:
            total = len(STATE.lanes)
            loaded = sum(1 for l in STATE.lanes.values() if l.warm == "ready")
        if total and loaded == total and not STATE.warm_all_logged:
            STATE.warm_all_logged = True
            log_event("warm", "bar history loaded for all %d contracts" % total)
        return False
    STATE.warm_all_logged = False
    try:
        warm_lane(lane)
    except Exception as e:
        with STATE.lock:
            if lane.warm == "loading":
                lane.warm, lane.warm_after = "queued", clock() + 60
        log_event("error", "history %s: %s: %s" % (lane.label, e.__class__.__name__, e))
    return True


# ─────────────────────────────────────────────────────────────────────────────
#  TRADING
# ─────────────────────────────────────────────────────────────────────────────
def pct_of(mom, base):
    return mom / base * 100.0 if base and base > 0 else None


def entry_signal(lane, bar, now):
    """Pine:  close > ema55  and  close > ema144  and  ta.crossover(close, ema144)
              and  momentum > threshold  and  close > minimum
    judged on the bar that just closed.  Returns the signal, or None and says
    why in lane.status."""
    s, cfg = lane.series, STATE.cfg
    if now - (bar["t"] + s.span) > max(s.span, 120):
        return None                       # closed long ago (overnight): never an entry
    idx = len(s.bars) - 1
    if idx < 1 or s.bars[idx] is not bar:
        return None
    prev = s.bars[idx - 1]
    m = cfg["mom_length"]
    mom, old = s.momentum(m, idx)
    c = bar["c"]
    if bar.get("e1") is None or bar.get("e2") is None or prev.get("e2") is None:
        lane.status = "EMAs need %d finished %d-min bars (have %d)" % (
            max(s.lens), cfg["ema_minutes"], s.n)
        return None
    if mom is None:
        lane.status = "collecting bars for momentum (%d/%d)" % (len(s.bars), m + 1)
        return None
    mom_pct = pct_of(mom, old)
    crossed = prev["c"] <= prev["e2"] and c > bar["e2"]
    if cfg["mom_unit"] == "rs":
        mom_ok = mom > cfg["mom_threshold"]
    else:
        mom_ok = mom_pct is not None and mom_pct > cfg["mom_threshold"]
    if not crossed:
        gap = (bar["e2"] - c) / c * 100.0
        if c > bar["e2"]:
            lane.status = "above EMA %d - waits for a fresh cross" % cfg["ema_entry_len"]
        elif gap < 0.05:
            lane.status = "at EMA %d - needs a close above it" % cfg["ema_entry_len"]
        else:
            lane.status = "%.1f%% below EMA %d" % (gap, cfg["ema_entry_len"])
        return None
    why = []
    if not c > bar["e1"]:
        why.append("under EMA %d" % cfg["ema_sl_len"])
    if not mom_ok:
        why.append("momentum %s" % ("Rs %.2f" % mom if cfg["mom_unit"] == "rs" else "%.1f%%" % (mom_pct or 0)))
    if not c > cfg["min_premium"]:
        why.append("premium under Rs %g" % cfg["min_premium"])
    if why:
        lane.status = "crossed EMA %d but %s" % (cfg["ema_entry_len"], ", ".join(why))
        log_event("signal", "%s crossed EMA %d at %.2f - not taken: %s"
                  % (lane.label, cfg["ema_entry_len"], c, ", ".join(why)))
        return None
    off = lane_offset(lane)
    return {"lane": lane, "bar": bar, "mom": mom, "mom_pct": mom_pct,
            "offset": off if off is not None else 99}


def take_entries(cands):
    """Every contract that signalled on this pass, the nearest to ATM first and
    then the strongest momentum, until the caps are full."""
    cfg = STATE.cfg
    cands.sort(key=lambda c: (abs(c["offset"]), -(c["mom_pct"] or 0)))
    cands = cands[:50]
    depth = fetch_depth([c["lane"].sid for c in cands])
    with STATE.lock:
        for c in cands:
            lane, bar = c["lane"], c["bar"]
            q = depth.get(lane.sid) or {}
            if q:
                lane.bid, lane.ask, lane.quote_ts = q["bid"], q["ask"], clock()
            if not STATE.running:
                lane.status = "stopped"
                continue
            if STATE.lanes.get(lane.key) is not lane or lane.position:
                continue
            if not lane_wanted(lane):
                lane.status = "signal ignored - no longer ATM +/- %d" % cfg["strikes_each_side"]
                continue
            held = [l for l in STATE.lanes.values() if l.position]
            why = None
            if STATE.trades_today >= cfg["max_trades_per_day"]:
                why = "%d trades already today" % cfg["max_trades_per_day"]
            elif len(held) >= cfg["max_open"]:
                why = "%d positions already open" % cfg["max_open"]
            elif sum(1 for l in held if l.sym == lane.sym) >= cfg["max_per_stock"]:
                why = "already %d open on %s" % (cfg["max_per_stock"], lane.sym)
            else:
                bid, ask = q.get("bid") or 0, q.get("ask") or 0
                if cfg["max_spread_pct"] > 0 and bid > 0 and ask > 0:
                    spread = (ask - bid) / ((ask + bid) / 2.0) * 100.0
                    if spread > cfg["max_spread_pct"]:
                        why = "spread %.1f%% (bid %.2f / ask %.2f) wider than %g%%" % (
                            spread, bid, ask, cfg["max_spread_pct"])
            if why:
                lane.status = "signal skipped: " + why
                log_event("skip", "%s signal at %.2f skipped - %s" % (lane.label, bar["c"], why))
                continue
            open_position(lane, c, q)


def open_position(lane, sig, quote):
    if kill_blocks():
        return None                   # a VIX rule says no new trades
    """Under STATE.lock."""
    cfg, bar = STATE.cfg, sig["bar"]
    qty = lane.lot * cfg["lots"]
    ask = (quote or {}).get("ask") or 0
    fill = round(ask if ask > 0 else (lane.ltp or bar["c"]), 2)
    now = clock()
    pos = {
        "id": "%s-%d" % (re.sub(r"\W", "_", lane.key), int(now * 1000)),
        "lane": lane.key, "contract": lane.label, "sym": lane.sym, "sid": lane.sid,
        "expiry": lane.expiry, "strike": lane.strike, "opt_type": lane.opt_type,
        "opened": ts(), "opened_ts": now,
        "signal_t": bar["t"], "signal_close": round(bar["c"], 2),
        "entry": fill, "qty": qty, "lot": lane.lot, "lots": cfg["lots"],
        "quick_target": round(fill * (1 + cfg["quick_target_pct"] / 100.0), 2),
        "quick_until": bar["t"] + cfg["quick_minutes"] * 60,
        "target": round(fill * (1 + cfg["target_pct"] / 100.0), 2),
        "profit_target_rs": cfg["profit_target_rs"],
        "ema_sl": round(bar["e1"], 2), "ema_sl_entry": round(bar["e1"], 2),
        "ema_entry": round(bar["e2"], 2),
        "momentum": round(sig["mom"], 2),
        "momentum_pct": round(sig["mom_pct"], 2) if sig["mom_pct"] is not None else None,
        "offset": sig["offset"], "highest": fill,
        "mark": fill, "pnl": 0.0, "status": "OPEN",
    }
    lane.position = pos
    lane.status = "in a position"
    STATE.trades_today += 1
    STATE.save()
    log_event("entry", "BUY %s x%d @ %.2f (signal close %.2f, EMA %d %.2f, momentum %s)  "
                       "quick %.2f till %s, target %.2f, stop below EMA %d"
              % (lane.label, qty, fill, bar["c"], cfg["ema_entry_len"], bar["e2"],
                 ("Rs %.2f" % sig["mom"]) if cfg["mom_unit"] == "rs" else "%.1f%%" % (sig["mom_pct"] or 0),
                 pos["quick_target"], _ist(pos["quick_until"] + lane.series.span).strftime("%H:%M")
                 if lane.series else "-", pos["target"], cfg["ema_sl_len"]))
    return pos


def close_position(lane, reason, price):
    """price=None closes at the position's last mark, read under the lock."""
    with STATE.lock:
        pos = lane.position
        if not pos:
            return None
        exit_px = round(_f(price, _f(pos.get("mark"))), 2)
        if exit_px <= 0:
            exit_px = round(_f(pos.get("mark")), 2)
        pnl = round((exit_px - pos["entry"]) * pos["qty"], 2)
        rec = dict(pos)
        rec.update(status="CLOSED", closed=ts(), closed_ts=clock(), exit=exit_px,
                   reason=reason, pnl=pnl, points=round(exit_px - pos["entry"], 2),
                   pct=round((exit_px - pos["entry"]) / pos["entry"] * 100.0, 2) if pos["entry"] else None)
        STATE.unflushed.append(rec)            # durable in the state file from here on
        STATE.history.append(rec)
        lane.position = None
        lane.status = "exited: %s" % reason
        STATE.save()
    flush_unflushed()                          # outside STATE.lock: lock order
    log_event("exit", "SELL %s %s @ %.2f  %+.1f%%  P&L Rs %.2f"
              % (rec["contract"], reason, exit_px, rec["pct"] or 0, pnl))
    return rec


def sell_price(lane, now):
    """What a market sell gets: the live bid, else the last price."""
    if lane.bid and lane.bid > 0 and now - lane.quote_ts < 15:
        return lane.bid
    return lane.ltp


def mark_position(lane, now):
    with STATE.lock:
        pos = lane.position
        if not pos:
            return
        mark = sell_price(lane, now)
        if not mark or mark <= 0:
            return
        pos["mark"] = round(mark, 2)
        pos["pnl"] = round((mark - pos["entry"]) * pos["qty"], 2)
        if lane.ltp and lane.ltp > pos["highest"]:
            pos["highest"] = round(lane.ltp, 2)
        if lane.series:
            e1 = lane.series.ema(0)
            if e1 is not None:
                pos["ema_sl"] = round(e1, 2)


def exit_reason(pos, price, bar_t, ema_sl, timed=True):
    """The script's exit block, in its order.  bar_t is the open time of the
    bar being judged (Pine's `time`); price is its close, or the live price."""
    cfg, entry = STATE.cfg, pos["entry"]
    if entry <= 0:
        return None
    if timed:
        d = _ist(bar_t)
        tomorrow = (d.date() + timedelta(days=1)).isoformat()
        if (d.hour == 15 and (price - entry) / entry >= cfg["preholiday_pct"] / 100.0
                and (d.weekday() == 4 or tomorrow in cfg["holidays"])):
            return "PRE_HOLIDAY"
        if bar_t <= pos["quick_until"] and price >= pos["quick_target"]:
            return "QUICK_TARGET"
    if ema_sl is not None and price < ema_sl:
        return "EMA_STOP"
    if price >= pos["target"]:
        return "TARGET"
    if (price - entry) * pos["qty"] >= pos["profit_target_rs"]:
        return "PROFIT_TARGET"
    return None


def check_tick_exits(lane, now):
    """The targets act the moment the price gets there (the script's exit
    alerts fire once per bar, not at its close).  The EMA stop waits for a bar
    close unless 'EMA stop on every price' is on."""
    with STATE.lock:
        pos, s = lane.position, lane.series
        if not pos or not lane.ltp:
            return
        span = s.span if s else STATE.cfg["bar_minutes"] * 60
        ema = s.ema(0) if (s and lane.ready and STATE.cfg["ema_stop_on_tick"]) else None
        why = exit_reason(pos, lane.ltp, slot_of(now, span), ema)
    if why:
        close_position(lane, why, sell_price(lane, now))


def check_bar_exits(lane, bar, now):
    """The whole exit block on the close of a bar, as the script ran it.  A bar
    that closed long ago (the last one of yesterday) still counts for the EMA
    stop and the targets, but not for the clock-based rules."""
    with STATE.lock:
        pos = lane.position
        if not pos:
            return
        live = now - (bar["t"] + lane.series.span) <= max(lane.series.span, 120)
        why = exit_reason(pos, bar["c"], bar["t"], bar.get("e1"), timed=live)
    if why:
        close_position(lane, why, sell_price(lane, now))


def settle_expiry(at):
    """A position must not ride into expiry: it is sold at 15:20 on its expiry
    day, and one whose expiry has passed (the app was off) is closed at its
    last mark."""
    d = now_ist(at)
    today = d.strftime("%Y-%m-%d")
    with STATE.lock:
        held = [l for l in STATE.lanes.values() if l.position]
    for lane in held:
        if lane.expiry < today:
            close_position(lane, "EXPIRED", None)
        elif (lane.expiry == today and d.time() >= EXPIRY_DAY_EXIT and market_state(at)[0] == "OPEN"
              and lane.ltp_ts and at - lane.ltp_ts < 60):
            close_position(lane, "EXPIRY_DAY", sell_price(lane, at))


_gaps = []          # contracts whose live prices had a hole, this pass


def feed_live(lane, px, now):
    """A live price into the lane's chart.  Returns the bars it closed.  While
    the history loads, prices wait; a hole in the prices longer than a few bars
    reloads the history rather than join two distant prices into one bar."""
    with STATE.lock:
        lane.ltp, lane.ltp_ts = px, now
        if not lane.ready:
            lane.pending.append((now, px))
            if len(lane.pending) > PENDING_MAX:
                del lane.pending[:-PENDING_MAX]
            return []
        s = lane.series
        hole = session_seconds(s.last_at, now)
        if hole > rewarm_after(s.span):
            _gaps.append((lane.label, hole))
            requeue(lane, (now, px))
            return []
        return s.push(px, now)


def step_lane(lane, px, now, cands):
    was_in = bool(lane.position)
    closed = feed_live(lane, px, now)
    if lane.position:
        mark_position(lane, now)
        check_tick_exits(lane, now)
    for bar in closed:
        if lane.position:
            check_bar_exits(lane, bar, now)
        elif STATE.running and not was_in and bar is closed[-1]:
            # was_in: a position open when this bar closed means the script
            # would not look for an entry on it - even if it just exited.
            sig = entry_signal(lane, bar, now)
            if sig:
                cands.append(sig)
    if lane.position:
        lane.status = "in a position"
    elif not lane.ready:
        lane.status = {"queued": "waiting for its bar history", "loading": "loading bar history"}.get(
            lane.warm, lane.status)


def apply_depth(lanes, depth, at):
    with STATE.lock:
        for lane in lanes:
            q = depth.get(lane.sid)
            if q:
                lane.bid, lane.ask, lane.quote_ts = q["bid"], q["ask"], at


# ─────────────────────────────────────────────────────────────────────────────
#  ENGINE
# ─────────────────────────────────────────────────────────────────────────────
def poll_quiet(at, state, why):
    """Market shut: read the share prices now and then, so the strike windows
    are set and their history loads before 09:15."""
    every = 30 if state == "PRE" else 600
    if STATE.running and at - STATE.last_spot_poll >= every:
        syms = list(STATE.universe)
        ltp, err = fetch_ltp([(EQ, STATE.scrip["eq"][s]) for s in syms])
        if ltp is not None:
            update_spots(syms, ltp, clock())
            sync_lanes(clock())
        else:
            STATE.last_spot_poll = at
            log_event("api", "share prices unavailable: %s" % err)
    with STATE.lock:
        total = len(STATE.lanes)
        ready = sum(1 for l in STATE.lanes.values() if l.warm == "ready")
        n_open = sum(1 for l in STATE.lanes.values() if l.position)
    STATE.status = "market %s - %d contracts, history loaded for %d%s" % (
        why, total, ready, (", %d open" % n_open) if n_open else "")


def poll_open(at, holding):
    running = STATE.running
    with STATE.lock:
        syms = list(STATE.universe) if running else sorted({l.sym for l in holding})
        lanes = list(STATE.lanes.values()) if running else list(holding)
    eq = STATE.scrip["eq"]
    pairs = [(EQ, eq[s]) for s in syms if s in eq] + [(FNO, l.sid) for l in lanes]
    t0 = clock()
    ltp, err = fetch_ltp(pairs)
    if ltp is None:
        STATE.status = "market quote unavailable: %s" % (err or "?")
        return
    now = clock()
    update_spots(syms, ltp, now)
    if running:
        sync_lanes(now)
    held = [l for l in lanes if l.position]
    if held:
        apply_depth(held, fetch_depth([l.sid for l in held]), clock())
    cands = []
    del _gaps[:]
    for lane in lanes:
        px = ltp.get((FNO, lane.sid))
        if not px:
            lane.status = "no price from the broker"
            continue
        step_lane(lane, px, now, cands)
    if _gaps:
        log_event("gap", "%d contract%s had no prices for %d+ session minutes (%s%s) - reloading "
                         "their bar history" % (
                             len(_gaps), "" if len(_gaps) == 1 else "s", min(h for _, h in _gaps) // 60,
                             ", ".join(l for l, _ in _gaps[:3]), ", ..." if len(_gaps) > 3 else ""))
    if cands and STATE.running:
        take_entries(cands)
    STATE.pass_seconds = round(clock() - t0, 1)


def engine_step():
    """One pass.  Split out of the loop so tests can drive it with a fake feed
    and a fake clock."""
    at = clock()
    state, why = market_state(at)
    STATE.market_note = "%s - %s" % (state, why)
    kill_step(state == "OPEN", _kill_close_all)

    day = now_ist(at).strftime("%Y-%m-%d")
    if day != STATE.day:
        with STATE.lock:
            STATE.day, STATE.trades_today = day, 0
        log_event("day", "new day %s - counters reset" % day)
        STATE.save()

    if not STATE.scrip:
        STATE.status = "loading the list of stock options (scrip master)"
        return
    if STATE.autostart and not STATE.running:
        if validate_cfg(STATE.cfg) is None and STATE.universe:
            with STATE.lock:
                STATE.autostart, STATE.running = False, True
            log_event("control", "started automatically on launch - %d stocks" % len(STATE.universe))
    tok = token_status()
    if not tok["configured"] or tok["expired"]:
        STATE.status = "token %s" % tok["human"]
        return
    if time.time() < _auth_block[0]:
        STATE.status = ("the broker rejected the token - paste a fresh one in Broker token "
                        "(retrying in %ds)" % int(_auth_block[0] - time.time()))
        return

    reset_stale_series()
    settle_expiry(at)
    with STATE.lock:
        holding = [l for l in STATE.lanes.values() if l.position]
    # Stopping blocks NEW entries only.  An open position keeps its exits
    # until it is out - a stop must never strand a trade.
    if not STATE.running and not holding:
        STATE.status = "stopped"
        return
    if state == "OPEN":
        poll_open(at, holding)
    else:
        poll_quiet(at, state, why)
        return

    if STATE.unflushed:
        flush_unflushed()                       # retry a trade write that failed
    with STATE.lock:
        total = len(STATE.lanes)
        ready = sum(1 for l in STATE.lanes.values() if l.ready)
        n_open = sum(1 for l in STATE.lanes.values() if l.position)
    if STATE.status.startswith("market quote unavailable"):
        return
    if STATE.running:
        STATE.status = "watching %d contracts on %d stocks - %d ready, %d open - a price every %.0fs" % (
            total, len(STATE.sym_info), ready, n_open, max(1, STATE.pass_seconds or 0))
    else:
        STATE.status = "stopped - still managing %d open position%s until they exit" % (
            n_open, "" if n_open == 1 else "s")


def engine_loop():
    log_event("boot", "engine thread started")
    while not _SHUTDOWN.is_set():
        _SHUTDOWN.wait(0.5)
        if _SHUTDOWN.is_set():
            break
        try:
            engine_step()
        except Exception as e:
            log_event("error", "engine: %s: %s" % (e.__class__.__name__, e))
            STATE.status = "error: %s" % e
            _SHUTDOWN.wait(5)


def warm_loop():
    while not _SHUTDOWN.is_set():
        try:
            busy = warm_once()
        except Exception as e:
            log_event("error", "history: %s: %s" % (e.__class__.__name__, e))
            busy = False
        if not busy:
            _SHUTDOWN.wait(1.0)


def scrip_loop():
    """The scrip master at boot, then again each morning for the day's new
    strikes and expiries."""
    while not _SHUTDOWN.is_set():
        now = now_ist()
        today = now.strftime("%Y-%m-%d")
        if STATE.scrip_day != today and (STATE.scrip is None or now.time() >= dtime(8, 0)):
            try:
                sc = load_scrip()
            except Exception as e:
                log_event("error", "scrip master: %s" % e)
                sc = None
            if sc:
                with STATE.lock:
                    STATE.scrip, STATE.scrip_day, STATE.strike_cache = sc, sc.get("date"), {}
                refresh_universe()
                log_event("boot", "%d of %d listed stocks have options%s" % (
                    len(STATE.universe), len(STATE.cfg["symbols"]),
                    (" - skipped: " + ", ".join(sorted(STATE.skipped))) if STATE.skipped else ""))
        _SHUTDOWN.wait(300 if STATE.scrip else 60)


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


def _r(v, d=2):
    return None if v is None else round(v, d)


def lane_view(lane, now):
    s = lane.series if lane.ready else None
    cfg = STATE.cfg
    e1 = s.ema(0) if s else None
    e2 = s.ema(1) if s else None
    mom, old = s.momentum(cfg["mom_length"]) if s else (None, None)
    ltp = lane.ltp
    return {"key": lane.key, "contract": lane.label, "sym": lane.sym, "expiry": lane.expiry,
            "dte": dte_of(lane.expiry), "strike": lane.strike, "opt_type": lane.opt_type,
            "offset": lane_offset(lane), "ltp": ltp,
            "price_age": round(now - lane.ltp_ts) if lane.ltp_ts else None,
            "ema_sl": _r(e1), "ema_entry": _r(e2),
            "gap_pct": _r((e2 - ltp) / ltp * 100.0) if (e2 and ltp) else None,
            "momentum": _r(mom), "momentum_pct": _r(pct_of(mom, old)) if mom is not None else None,
            "bars": len(s.bars) if s else 0, "ema_bars": s.n if s else 0,
            "warm": lane.warm, "warm_note": lane.warm_note, "status": lane.status,
            "in_position": bool(lane.position)}


def position_view(lane, now):
    p = dict(lane.position)
    p["price_age"] = round(now - lane.ltp_ts) if lane.ltp_ts else None
    p["ltp"] = lane.ltp
    p["pct"] = round((p["mark"] - p["entry"]) / p["entry"] * 100.0, 2) if p.get("entry") else None
    p["in_window"] = lane_wanted(lane)
    p["ready"] = lane.ready
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
    by_sym = group("sym")
    top = dict(sorted(by_sym.items(), key=lambda kv: -abs(kv[1]["pnl"]))[:12])
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
        "by_side": group("opt_type"), "by_reason": group("reason"), "by_stock": top,
        "series": series,
    }


def load_estimate(cfg):
    """Contracts, market-quote calls per pass and the first history load."""
    n_sym = len(STATE.universe) if STATE.scrip else len(cfg["symbols"])
    contracts = n_sym * (2 * cfg["strikes_each_side"] + 1) * len(cfg["opt_types"])
    calls = max(1, int(math.ceil((contracts + n_sym) / float(MAX_PER_QUOTE))))
    per = 1 if base_interval(cfg["bar_minutes"]) == 15 else 2
    return {"stocks": n_sym, "contracts": contracts, "quote_calls": calls,
            "seconds_per_price": round(calls * QUOTE_GATE.interval + 0.5, 1),
            "history_minutes": round(contracts * per * DATA_GATE.interval / 60.0, 1)}


@app.route("/api/state")
def api_state():
    today = now_ist().strftime("%Y-%m-%d")
    now = clock()
    with STATE.lock:
        lanes = list(STATE.lanes.values())
        positions = [position_view(l, now) for l in sorted(lanes, key=lambda l: l.key) if l.position]
        near = []
        for l in lanes:
            if l.position or not l.ready or not l.ltp:
                continue
            v = lane_view(l, now)
            if v["gap_pct"] is not None and v["gap_pct"] > 0 and (v["offset"] is not None
                                                                   and abs(v["offset"]) <= STATE.cfg["strikes_each_side"]):
                near.append(v)
        near.sort(key=lambda v: v["gap_pct"])
        hist = list(STATE.history)
        warm = {"ready": sum(1 for l in lanes if l.warm == "ready"),
                "loading": sum(1 for l in lanes if l.warm == "loading"),
                "queued": sum(1 for l in lanes if l.warm == "queued")}
        skipped = dict(STATE.skipped)
        n_uni = len(STATE.universe)
        n_spot = len(STATE.sym_info)
    today_rows = [h for h in hist if str(h.get("closed") or "").startswith(today)]
    return jsonify({
        "running": STATE.running, "status": STATE.status, "market": STATE.market_note,
        "cfg": STATE.cfg, "token": token_status(),
        "universe": n_uni, "skipped": skipped, "stocks_priced": n_spot,
        "scrip_day": STATE.scrip_day, "lanes_count": len(lanes), "warm": warm,
        "trades_today": STATE.trades_today,
        "today_pnl": round(sum(_f(h.get("pnl")) for h in today_rows), 2),
        "today_trades": len(today_rows),
        "realised": round(sum(_f(h.get("pnl")) for h in hist), 2), "all_trades": len(hist),
        "open_count": len(positions), "positions": positions, "near": near[:12],
        "events": recent_events(15), "estimate": load_estimate(STATE.cfg),
        "defaults": {"symbols": NIFTY100, "holidays": HOLIDAYS},
        "choices": {"bar": BAR_CHOICES, "ema_tf": EMA_TF_CHOICES, "max_each_side": MAX_EACH_SIDE,
                    "max_symbols": MAX_SYMBOLS},
    })


@app.route("/api/stocks")
def api_stocks():
    now = clock()
    with STATE.lock:
        by_sym = {}
        for l in STATE.lanes.values():
            e = by_sym.setdefault(l.sym, {"lanes": 0, "ready": 0, "open": 0})
            e["lanes"] += 1
            e["ready"] += 1 if l.ready else 0
            e["open"] += 1 if l.position else 0
        rows = []
        for sym in STATE.cfg["symbols"]:
            info = STATE.sym_info.get(sym) or {}
            e = by_sym.get(sym, {"lanes": 0, "ready": 0, "open": 0})
            win = []
            if info:
                i0, n = info["atm_idx"], STATE.cfg["strikes_each_side"]
                win = info["strikes"][max(0, i0 - n): i0 + n + 1]
            rows.append({"sym": sym, "skipped": STATE.skipped.get(sym),
                         "spot": info.get("spot") or STATE.spots.get(sym),
                         "expiry": info.get("expiry"), "dte": dte_of(info["expiry"]) if info else None,
                         "atm": info.get("atm"), "lot": info.get("lot"),
                         "low": win[0] if win else None, "high": win[-1] if win else None,
                         "lanes": e["lanes"], "ready": e["ready"], "open": e["open"]})
    return jsonify({"rows": rows, "at": now})


@app.route("/api/lanes")
def api_lanes():
    sym, side = (request.args.get("sym") or "").upper(), request.args.get("side") or ""
    now = clock()
    with STATE.lock:
        rows = [lane_view(l, now) for l in STATE.lanes.values()
                if (not sym or l.sym == sym) and (not side or l.opt_type == side)]
    rows.sort(key=lambda r: (r["sym"], r["opt_type"], r["strike"]))
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


TRADE_COLS = [("Closed", "closed"), ("Contract", "contract"), ("Stock", "sym"), ("Expiry", "expiry"),
              ("Side", "opt_type"), ("Strike", "strike"), ("Strikes from ATM", "offset"),
              ("Opened", "opened"), ("Entry", "entry"), ("Signal close", "signal_close"),
              ("Exit", "exit"), ("Points", "points"), ("%", "pct"), ("Lots", "lots"),
              ("Lot size", "lot"), ("Qty", "qty"), ("P&L", "pnl"), ("Exit reason", "reason"),
              ("Highest", "highest"), ("Quick target", "quick_target"), ("Target", "target"),
              ("EMA SL at entry", "ema_sl_entry"), ("EMA Entry at entry", "ema_entry"),
              ("Momentum", "momentum"), ("Momentum %", "momentum_pct"), ("Id", "id")]


@app.route("/api/history.csv")
def api_history_csv():
    with STATE.lock:
        rows = list(STATE.history)
    return _csv("stock_ema_trades_%s.csv" % now_ist().strftime("%Y%m%d"),
                [c for c, _ in TRADE_COLS], [[r.get(k, "") for _, k in TRADE_COLS] for r in rows])


@app.route("/api/positions.csv")
def api_positions_csv():
    cols = [("Contract", "contract"), ("Opened", "opened"), ("Entry", "entry"), ("Mark", "mark"),
            ("Qty", "qty"), ("Open P&L", "pnl"), ("%", "pct"), ("Quick target", "quick_target"),
            ("Target", "target"), ("EMA stop", "ema_sl"), ("Highest", "highest")]
    now = clock()
    with STATE.lock:
        rows = [position_view(l, now) for l in STATE.lanes.values() if l.position]
    return _csv("stock_ema_positions_%s.csv" % now_ist().strftime("%Y%m%d"),
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
    if STATE.scrip and not STATE.universe:
        return jsonify({"error": "None of the listed stocks has options on NSE - check the list in Settings."}), 400
    with STATE.lock:
        STATE.running = True
        STATE.last_spot_poll = 0.0
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
    now = clock()
    with STATE.lock:
        lanes = [l for l in STATE.lanes.values() if l.position and (not key or l.key == key)]
    closed = []
    for lane in lanes:
        if lane.ltp_ts and now - lane.ltp_ts < 30 and sell_price(lane, now):
            px, why = sell_price(lane, now), "MANUAL"
        else:
            # No live price (market closed, feed down): say so rather than
            # pretend the old mark is the current bid.
            px, why = None, "MANUAL_LAST_MARK"
        rec = close_position(lane, why, px)
        if rec:
            closed.append({"contract": rec["contract"], "exit": rec["exit"], "reason": why})
    return jsonify({"ok": True, "closed": closed})


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
    return None


@app.route("/api/config", methods=["POST"])
def api_config():
    body = request.get_json(silent=True) or {}
    err = check_body(body)
    if err:
        return jsonify({"error": err}), 400
    if "symbols" in body:
        syms = parse_symbols(body["symbols"])
        if len(syms) > MAX_SYMBOLS:
            return jsonify({"error": "At most %d stocks." % MAX_SYMBOLS}), 400
        raw = body["symbols"] if isinstance(body["symbols"], list) else re.split(r"[\s,;]+", str(body["symbols"]))
        bad = [str(x) for x in raw if str(x).strip() and not _SYM_RE.match(str(x).strip().upper())]
        if bad:
            return jsonify({"error": "Not a stock symbol: %s" % ", ".join(bad[:5])}), 400
    with STATE.lock:
        new = clean_cfg({**STATE.cfg, **body})
        err = validate_cfg(new)
        if err:
            return jsonify({"error": err}), 400
        # Only the config changes here.  Contracts are added and dropped by the
        # engine thread on its next pass.
        STATE.cfg = new
        STATE.last_spot_poll = 0.0
        STATE.save()
    refresh_universe()
    log_event("config", "settings saved - %d stocks (%d with options), ATM +/- %d, %s, %d-min bars, "
                        "EMA %d/%d on %d min" % (
                            len(new["symbols"]), len(STATE.universe), new["strikes_each_side"],
                            "/".join(new["opt_types"]), new["bar_minutes"], new["ema_sl_len"],
                            new["ema_entry_len"], new["ema_minutes"]))
    return jsonify({"ok": True, "cfg": STATE.cfg})


@app.route("/api/rewarm", methods=["POST"])
def api_rewarm():
    with STATE.lock:
        for lane in STATE.lanes.values():
            requeue(lane, None)
    log_event("control", "bar history cleared - reloading it for every contract")
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
    runtime_write(access_token=tok, client_id=str(claims.get("dhanClientId") or ""), saved_at=ts())
    log_event("token", "token saved locally")
    return jsonify({"ok": True, "token": token_status()})


@app.route("/")
def index():
    return Response(PAGE, mimetype="text/html")


PAGE = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Stock Options EMA Cross</title>
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
.g{color:#4ade80}.r{color:#f87171}.o{color:#fbbf24}
.hint{font-size:12px;color:var(--mu)}
.empty{padding:22px;text-align:center;color:var(--mu);font-size:13px}
.tw{overflow-x:auto}
.scroll{max-height:64vh;overflow:auto}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;color:var(--mu);font-size:11px;letter-spacing:.06em;padding:8px;border-bottom:1px solid var(--bd);white-space:nowrap;position:sticky;top:0;background:var(--panel)}
td{padding:7px 8px;border-bottom:1px solid var(--bd);font-variant-numeric:tabular-nums;white-space:nowrap}
td.wrap{white-space:normal}
tr:last-child td{border-bottom:0}
.tag{display:inline-block;padding:1px 8px;border-radius:6px;font-size:11px;font-weight:700}
.ce{background:rgba(34,197,94,.14);color:#86efac}.pe{background:rgba(239,68,68,.14);color:#fca5a5}
.bar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:14px}
.big{font-size:20px;font-weight:700;font-family:ui-monospace,Consolas,monospace}
.f{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}
.fl{display:flex;flex-direction:column;gap:5px}
.fl .row2{display:flex;gap:8px}.fl .row2>*{flex:1;min-width:0}
label{font-size:12px;color:var(--mu)}
input,select,textarea{background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:8px 11px;color:var(--br);font:inherit}
textarea{width:100%;min-height:92px;resize:vertical;font:13px/1.5 ui-monospace,Consolas,monospace}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{display:flex;align-items:center;gap:7px;background:var(--bg);border:1px solid var(--bd2);border-radius:8px;padding:8px 12px;cursor:pointer;font-size:13px;color:var(--tx);user-select:none}
.chip input{margin:0}.chip.on{border-color:var(--ac);background:rgba(56,189,248,.1);color:var(--br)}
.grp{margin-bottom:16px}.grp>label{display:block;margin-bottom:6px}
.sec{font-size:11px;letter-spacing:.12em;color:var(--mu);font-weight:700;margin:18px 0 10px}
.note{background:rgba(245,158,11,.1);border-left:3px solid var(--or);padding:10px 14px;border-radius:8px;font-size:13px;margin-bottom:14px}
.info{background:rgba(56,189,248,.08);border-left-color:var(--ac)}
svg text.ax{fill:var(--m2);font:11px ui-monospace,Consolas,monospace}
svg line.grid{stroke:var(--bd);stroke-width:1}
svg line.zero{stroke:var(--bd2);stroke-dasharray:4 4}
svg circle.dot{fill:var(--panel);stroke-width:2}
.mono{font-family:ui-monospace,Consolas,monospace;font-size:12px}
</style></head><body>

<div class="top">
  <div><h1>Stock Options 2-EMA Cross + Momentum</h1>
    <p class="sub">Buys an ATM-area stock option when its premium crosses up through its 30-minute EMA 144 with momentum - Nifty 100 stocks, CE and PE - paper trading</p></div>
  <div class="sp"></div>
  <span class="pill" id="p_mkt">-</span>
  <span class="pill" id="p_tok">-</span>
  <span class="pill" id="p_run">-</span>
  <button class="go" id="b_start">Start</button>
  <button class="stop" id="b_stop">Stop</button>
</div>
<nav class="tabs" id="tabs">
  <button data-tab="dash" class="on">Dashboard</button>
  <button data-tab="stocks">Stocks</button>
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
  <div class="note">Paper trading only - nothing is sent to the broker. New entries only on the ATM +/- N strikes; once a contract is bought, its exits are checked on every price until it is sold, even if the stock moves away. Stop blocks new entries; open positions keep their exits.</div>
  <div class="grid">
    <div class="card"><div class="k">STOCKS</div><div class="v" id="d_stk">-</div><div class="hint" id="d_stk2">-</div></div>
    <div class="card"><div class="k">CONTRACTS WATCHED</div><div class="v" id="d_lanes">-</div><div class="hint" id="d_lanes2">-</div></div>
    <div class="card"><div class="k">OPEN POSITIONS</div><div class="v" id="d_open">-</div><div class="hint" id="d_open2">-</div></div>
    <div class="card"><div class="k">TODAY'S P&amp;L</div><div class="v" id="d_pnl">-</div><div class="hint" id="d_pnl2">-</div></div>
  </div>
  <div class="two">
    <div class="card"><h3>OPEN POSITIONS</h3><div class="tw" id="d_pos"></div></div>
    <div class="card"><h3>CLOSEST TO A CROSS OF EMA <span id="d_len">144</span></h3><div class="tw" id="d_near"></div></div>
  </div>
  <div class="card"><h3>RECENT ACTIVITY</h3><div class="tw" id="d_ev"></div></div>
</section>

<!-- STOCKS -->
<section class="panel" id="p-stocks">
  <div class="bar">
    <input id="st_q" placeholder="Filter, e.g. BANK" style="width:220px">
    <span class="hint" id="st_count"></span>
  </div>
  <div class="card scroll"><div id="st_table"></div></div>
  <p class="hint">Each stock trades its nearest monthly expiry until fewer than the "roll" days are left, then the next one. ATM is the listed strike nearest the share price; the window moves with the price.</p>
</section>

<!-- CONTRACTS -->
<section class="panel" id="p-contracts">
  <div class="bar">
    <select id="f_sym"><option value="">All stocks</option></select>
    <select id="f_side"><option value="">CE and PE</option><option value="CE">CE only</option><option value="PE">PE only</option></select>
    <label class="chip" style="padding:6px 10px" title="Premium is under the entry EMA, so it can still cross up and signal."><input type="checkbox" id="f_below"> Only those under the entry EMA</label>
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
  <p class="hint">The quick target, target, profit target and pre-holiday exit act on every price check. The EMA stop acts when a bar closes below the EMA (or on every price, if chosen in Settings). Sells fill at the live bid; with no live price, Close uses the last mark and says so.</p>
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
    <div class="grp"><label>Stocks - NSE symbols, separated by commas or spaces (<span id="s_symcount">0</span>)</label>
      <textarea id="c_symbols" spellcheck="false"></textarea>
      <div class="bar" style="margin:8px 0 0"><button class="sm ghost" id="b_n100">Use the Nifty 100 list</button><span class="hint" id="s_skipped"></span></div></div>
    <div class="grp"><label>Sides</label><div class="chips">
      <label class="chip" id="chip_CE"><input type="checkbox" id="t_CE"> <span class="tag ce">CE</span> Calls</label>
      <label class="chip" id="chip_PE"><input type="checkbox" id="t_PE"> <span class="tag pe">PE</span> Puts</label>
    </div></div>

    <div class="sec">CONTRACTS</div>
    <div class="f">
      <div class="fl"><label>Strikes each side of ATM (0 = ATM only)</label><input id="c_strikes_each_side" type="number" min="0" max="5"></div>
      <div class="fl"><label>Roll to next expiry when fewer than (days) left</label><input id="c_roll_days" type="number" min="0" max="20"></div>
    </div>

    <div class="sec">ENTRY - THE SCRIPT'S buyCondition</div>
    <div class="f">
      <div class="fl"><label>Chart bar</label><select id="c_bar_minutes"></select></div>
      <div class="fl"><label>EMA time frame (timeFrame)</label><select id="c_ema_minutes"></select></div>
      <div class="fl"><label>EMA SL length (close must be above)</label><input id="c_ema_sl_len" type="number"></div>
      <div class="fl"><label>EMA Entry length (close crosses up)</label><input id="c_ema_entry_len" type="number"></div>
      <div class="fl"><label>Momentum length (bars)</label><input id="c_mom_length" type="number"></div>
      <div class="fl"><label>Momentum above</label><div class="row2"><input id="c_mom_threshold" type="number" step="0.1">
        <select id="c_mom_unit"><option value="pct">% of premium</option><option value="rs">Rs</option></select></div></div>
      <div class="fl"><label>Minimum premium (Rs) - the script's close &gt; 144</label><input id="c_min_premium" type="number" step="0.5"></div>
    </div>

    <div class="sec">EXITS - THE SCRIPT'S EXIT BLOCK</div>
    <div class="f">
      <div class="fl"><label>Quick target (% above entry)</label><input id="c_quick_target_pct" type="number" step="0.5"></div>
      <div class="fl"><label>... within (minutes of the signal bar)</label><input id="c_quick_minutes" type="number"></div>
      <div class="fl"><label>EMA SL stop acts on a</label><select id="c_ema_stop_on_tick"><option value="0">bar close below it</option><option value="1">any price below it</option></select></div>
      <div class="fl"><label>Target (% above entry) - longTargetPct</label><input id="c_target_pct" type="number" step="1"></div>
      <div class="fl"><label>Profit target (Rs, open P&amp;L)</label><input id="c_profit_target_rs" type="number" step="100"></div>
      <div class="fl"><label>Pre-holiday exit at 15:00 if up (%)</label><input id="c_preholiday_pct" type="number" step="0.5"></div>
    </div>
    <div class="grp" style="margin-top:12px"><label>Holidays (YYYY-MM-DD) - the pre-holiday exit runs the trading day before each, and on Fridays</label>
      <textarea id="c_holidays" spellcheck="false" style="min-height:60px"></textarea></div>

    <div class="sec">SIZE AND LIMITS</div>
    <div class="f">
      <div class="fl"><label>Lots per trade</label><input id="c_lots" type="number"></div>
      <div class="fl"><label>Max open at once (all stocks)</label><input id="c_max_open" type="number"></div>
      <div class="fl"><label>Max open per stock</label><input id="c_max_per_stock" type="number"></div>
      <div class="fl"><label>Max trades per day</label><input id="c_max_trades_per_day" type="number"></div>
      <div class="fl"><label>Skip if bid/ask spread wider than (%, 0 = never)</label><input id="c_max_spread_pct" type="number" step="0.5"></div>
    </div>
    <div class="note info" style="margin:16px 0 0" id="s_est">-</div>
    <div class="bar" style="margin:16px 0 0">
      <button class="go" id="b_save">Save settings</button>
      <button class="ghost" id="b_revert">Discard changes</button>
      <button class="ghost" id="b_rewarm">Reload bar history</button>
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
const pct=n=>n==null||isNaN(n)?'-':(n>0?'+':'')+Number(n).toFixed(1)+'%';
const cls=n=>n>0?'g':(n<0?'r':'');
const tag=t=>'<span class="tag '+(t==='PE'?'pe':'ce')+'">'+esc(t)+'</span>';
const strike=k=>{const v=Number(k);return v===Math.round(v)?String(v):String(+v.toFixed(2));};
const table=(head,rows,empty)=>rows.length?'<table><thead><tr>'+head.map(h=>'<th>'+h+'</th>').join('')+'</tr></thead><tbody>'+rows.join('')+'</tbody></table>':'<div class="empty">'+empty+'</div>';
function setHTML(el,html){if(el&&el.__h!==html){el.innerHTML=html;el.__h=html;}}
async function post(u,b){const r=await fetch(u,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b||{})});
 const d=await r.json().catch(()=>({}));if(!r.ok)throw new Error(d.error||('failed ('+r.status+')'));return d;}
async function get(u){const r=await fetch(u);if(!r.ok)throw new Error('failed ('+r.status+')');return r.json();}
const store={get(k){try{return localStorage.getItem(k);}catch(e){return null;}},set(k,v){try{localStorage.setItem(k,v);}catch(e){}}};
function fmtExp(e){if(!e)return '-';const d=new Date(e+'T00:00:00');return isNaN(d)?e:d.toLocaleDateString('en-GB',{day:'2-digit',month:'short'});}
function offCell(o){return o==null?'<span class="hint">off list</span>':(o===0?'<b>ATM</b>':(o>0?'+':'')+o);}

/* ---------- tabs ---------- */
let TAB='dash';
function showTab(t){if(!$('#p-'+t))t='dash';TAB=t;store.set('se_tab',t);
  $$('#tabs button').forEach(b=>b.classList.toggle('on',b.dataset.tab===t));
  $$('.panel').forEach(p=>p.classList.toggle('on',p.id==='p-'+t));
  if(t==='report')loadReport(); if(t==='activity')loadEvents(true); if(t==='contracts')loadLanes(); if(t==='stocks')loadStocks();}
$('#tabs').onclick=e=>{const b=e.target.closest('button[data-tab]');if(b)showTab(b.dataset.tab);};

/* ---------- live state ---------- */
let S=null;
async function poll(){
  try{S=await get('/api/state');}catch(e){$('#statusline').textContent='cannot reach the strategy: '+e.message;return;}
  const s=S,c=s.cfg;
  $('#p_mkt').textContent=s.market;
  $('#p_tok').textContent='token '+s.token.human; $('#p_tok').className='pill '+(s.token.configured&&!s.token.expired?'on':'off');
  $('#p_run').textContent=s.running?'RUNNING':'STOPPED'; $('#p_run').className='pill '+(s.running?'on':'off');
  $('#b_start').disabled=s.running; $('#b_stop').disabled=!s.running;
  $('#statusline').textContent=s.status;

  /* dashboard */
  const nsk=Object.keys(s.skipped||{}).length;
  $('#d_stk').textContent=s.scrip_day?s.universe:'-';
  $('#d_stk2').textContent=s.scrip_day?(c.symbols.length+' listed'+(nsk?', '+nsk+' without options':'')+' - '+s.stocks_priced+' priced'):'loading the scrip master...';
  $('#d_lanes').textContent=s.lanes_count;
  $('#d_lanes2').textContent='ATM +/- '+c.strikes_each_side+' x '+(c.opt_types.join('+')||'-')+' - history '+s.warm.ready+' loaded'+
    (s.warm.queued+s.warm.loading?', '+(s.warm.queued+s.warm.loading)+' to go':'');
  $('#d_open').textContent=s.open_count+' / '+c.max_open;
  $('#d_open2').textContent=s.trades_today+' of '+c.max_trades_per_day+' trades used today';
  $('#d_pnl').textContent=inr(s.today_pnl); $('#d_pnl').className='v '+cls(s.today_pnl);
  $('#d_pnl2').textContent=s.today_trades+' closed today - all time '+inr(s.realised)+' over '+s.all_trades+' trades';
  $('#d_len').textContent=c.ema_entry_len;
  setHTML($('#d_pos'),table(['Contract','Entry','Mark','%','P&amp;L'],s.positions.map(p=>
    '<tr><td>'+contractCell(p)+'</td><td>'+num(p.entry)+'</td><td>'+num(p.mark)+'</td><td class="'+cls(p.pct)+'">'+pct(p.pct)+'</td><td class="'+cls(p.pnl)+'">'+inr(p.pnl)+'</td></tr>'),'No open positions.'));
  setHTML($('#d_near'),table(['Contract','From ATM','Premium','EMA '+c.ema_entry_len,'Needs','Momentum'],s.near.map(l=>
    '<tr><td>'+contractCell(l)+'</td><td>'+offCell(l.offset)+'</td><td>'+num(l.ltp)+'</td><td>'+num(l.ema_entry)+'</td><td>+'+num(l.gap_pct,1)+'%</td><td>'+momCell(l)+'</td></tr>'),
    s.running?'Waiting for prices and bar history.':'Press Start to watch contracts.'));
  setHTML($('#d_ev'),eventRows(s.events));

  /* positions */
  const tot=s.positions.reduce((a,p)=>a+(p.pnl||0),0);
  $('#pos_total').textContent='Open P&L: '+inr(tot); $('#pos_total').className='big '+cls(tot);
  setHTML($('#pos_table'),table(['Contract','From ATM','Opened','Entry','Mark','%','Open P&amp;L','Quick target','Target','EMA stop','Price age',''],s.positions.map(p=>
    '<tr><td>'+contractCell(p)+'</td><td>'+(p.in_window?'<span class="hint">in window</span>':'<span class="o" title="No longer near ATM - its exits are still checked">out of window</span>')+'</td>'+
    '<td>'+esc(String(p.opened||'').slice(5,16))+'</td><td>'+num(p.entry)+'</td><td>'+num(p.mark)+'</td><td class="'+cls(p.pct)+'">'+pct(p.pct)+'</td>'+
    '<td class="'+cls(p.pnl)+'"><b>'+inr(p.pnl)+'</b></td>'+
    '<td>'+num(p.quick_target)+' <span class="hint">till '+esc(hhmm((p.quick_until||0)+c.bar_minutes*60))+'</span></td>'+
    '<td>'+num(p.target)+'</td><td>'+(p.ready?num(p.ema_sl):'<span class="hint">loading</span>')+'</td>'+
    '<td class="hint">'+(p.price_age==null?'-':p.price_age+'s')+'</td>'+
    '<td><button class="sm danger" data-close="'+esc(p.lane)+'" data-name="'+esc(p.contract)+'">Close</button></td></tr>'),'No open positions.'));

  paintSettings(s);
  if(TAB==='contracts')loadLanes();
  if(TAB==='stocks')loadStocks();
}
function hhmm(t){const d=new Date(t*1000);return isNaN(d)?'-':d.toLocaleTimeString('en-GB',{hour:'2-digit',minute:'2-digit',timeZone:'Asia/Kolkata'});}
function contractCell(x){return '<b>'+esc(x.sym)+'</b> '+esc(strike(x.strike))+' '+tag(x.opt_type)+' <span class="hint">'+esc(fmtExp(x.expiry))+'</span>';}
function momCell(l){if(l.momentum==null)return '<span class="hint">'+(l.bars||0)+' bars</span>';
  const v=S&&S.cfg.mom_unit==='rs'?l.momentum:l.momentum_pct, ok=S&&v!=null&&v>S.cfg.mom_threshold;
  return '<span class="'+(ok?'g':'')+'">'+(S&&S.cfg.mom_unit==='rs'?'₹'+num(l.momentum):pct(l.momentum_pct))+'</span>';}
function eventRows(evs){return table(['Time','Kind','What happened'],(evs||[]).map(e=>
  '<tr><td class="mono">'+esc(e.ts||e.at)+'</td><td><span class="tag" style="background:var(--p2)">'+esc(e.kind)+'</span></td><td class="wrap">'+esc(e.msg)+'</td></tr>'),'Nothing yet.');}

/* ---------- stocks ---------- */
let stBusy=false;
async function loadStocks(){
  if(stBusy)return; stBusy=true;
  try{
    const q=$('#st_q').value.trim().toUpperCase();
    let rows=(await get('/api/stocks')).rows;
    if(q)rows=rows.filter(r=>r.sym.indexOf(q)>=0);
    $('#st_count').textContent=rows.length+' stock'+(rows.length===1?'':'s');
    setHTML($('#st_table'),table(['Stock','Share price','Expiry','ATM','Strikes watched','Lot','Contracts','History','Open'],rows.map(r=>
      r.skipped?'<tr><td><b>'+esc(r.sym)+'</b></td><td colspan="8" class="hint">skipped - '+esc(r.skipped)+'</td></tr>':
      '<tr><td><b>'+esc(r.sym)+'</b></td><td>'+num(r.spot)+'</td><td>'+esc(fmtExp(r.expiry))+' <span class="hint">'+(r.dte==null?'':r.dte+'d')+'</span></td>'+
      '<td>'+(r.atm==null?'-':esc(strike(r.atm)))+'</td><td>'+(r.low==null?'-':esc(strike(r.low))+' - '+esc(strike(r.high)))+'</td><td>'+(r.lot||'-')+'</td>'+
      '<td>'+r.lanes+'</td><td>'+r.ready+'/'+r.lanes+'</td><td>'+(r.open?'<b class="g">'+r.open+'</b>':'-')+'</td></tr>'),
      !S||!S.scrip_day?'Loading the list of stock options...':'No stocks.'));
  }catch(e){}
  stBusy=false;
}
$('#st_q').addEventListener('input',loadStocks);

/* ---------- contracts ---------- */
let lanesBusy=false;
async function loadLanes(){
  if(lanesBusy)return; lanesBusy=true;
  try{
    const q='?sym='+encodeURIComponent($('#f_sym').value)+'&side='+encodeURIComponent($('#f_side').value);
    let rows=(await get('/api/lanes'+q)).rows;
    if($('#f_below').checked)rows=rows.filter(r=>r.gap_pct!=null&&r.gap_pct>0).sort((a,b)=>a.gap_pct-b.gap_pct);
    $('#c_count').textContent=rows.length+' contract'+(rows.length===1?'':'s');
    const c=S?S.cfg:{ema_sl_len:55,ema_entry_len:144};
    setHTML($('#c_table'),table(['Contract','From ATM','Premium','EMA '+c.ema_sl_len,'EMA '+c.ema_entry_len,'To cross','Momentum','Bars','History','Status'],rows.map(r=>
      '<tr><td>'+contractCell(r)+'</td><td>'+offCell(r.offset)+'</td><td>'+num(r.ltp)+'</td><td>'+num(r.ema_sl)+'</td><td>'+num(r.ema_entry)+'</td>'+
      '<td>'+(r.gap_pct==null?'-':(r.gap_pct>0?'+'+num(r.gap_pct,1)+'%':'<span class="hint">'+(r.gap_pct<0?'above':'at')+'</span>'))+'</td><td>'+momCell(r)+'</td>'+
      '<td class="hint">'+r.bars+' / '+r.ema_bars+'</td><td class="hint" title="'+esc(r.warm_note)+'">'+esc(r.warm)+'</td>'+
      '<td class="wrap">'+(r.in_position?'<b class="g">in a position</b>':esc(r.status))+'</td></tr>'),
      !S?'Loading...':(!S.running?'Stopped - press Start. Contracts appear once share prices arrive.':'Waiting for share prices to set each stock\'s ATM.')));
  }catch(e){}
  lanesBusy=false;
}
['#f_sym','#f_side','#f_below'].forEach(id=>$(id).addEventListener('change',loadLanes));

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
function breakCard(title,g,sorted){const ks=Object.keys(g||{});if(!sorted)ks.sort();return '<div class="card"><h3>'+title+'</h3>'+
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
    statCard('PROFIT FACTOR',st.profit_factor==null?'-':(st.profit_factor==='inf'?'∞':st.profit_factor),
      st.profit_factor==null?'':((st.profit_factor==='inf'||st.profit_factor>=1)?'g':'r'),st.profit_factor==='inf'?'no losing trade yet':'gross wins / gross losses')+
    statCard('MAX DRAWDOWN',inr(st.max_drawdown,0),st.max_drawdown<0?'r':'','deepest fall from a peak'));
  equityChart($('#r_chart'),st.series);
  setHTML($('#r_break'),breakCard('BY SIDE',st.by_side)+breakCard('BY EXIT REASON',st.by_reason)+breakCard('BY STOCK (BIGGEST P&amp;L)',st.by_stock,true));
  const rows=REPORT.rows.slice().reverse();
  setHTML($('#r_table'),table(['<input type="checkbox" id="r_all">','Closed','Contract','Opened','Entry','Exit','%','Qty','P&amp;L','Why'],rows.map(t=>
    '<tr><td><input type="checkbox" class="r_chk" value="'+esc(t.id)+'"></td><td class="mono">'+esc(String(t.closed||'').slice(0,16))+'</td><td>'+contractCell(t)+'</td>'+
    '<td class="mono">'+esc(String(t.opened||'').slice(5,16))+'</td><td>'+num(t.entry)+'</td><td>'+num(t.exit)+'</td><td class="'+cls(t.pct)+'">'+pct(t.pct)+'</td><td>'+esc(t.qty)+'</td>'+
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
const KINDS=['entry','exit','signal','skip','contract','warm','gap','config','control','report','token','api','day','boot','error'];
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
const NUMS=['strikes_each_side','roll_days','ema_sl_len','ema_entry_len','mom_length','mom_threshold','min_premium',
  'quick_target_pct','quick_minutes','target_pct','profit_target_rs','preholiday_pct','lots','max_open','max_per_stock',
  'max_trades_per_day','max_spread_pct'];
const SELS=['bar_minutes','ema_minutes','mom_unit','ema_stop_on_tick'];
let touched=false,symKey='';
$('#p-settings').addEventListener('input',()=>{touched=true;symCount();});
$('#p-settings').addEventListener('change',e=>{touched=true;if(e.target.id==='t_CE'||e.target.id==='t_PE')sideChips();symCount();});
function sideChips(){['CE','PE'].forEach(t=>$('#chip_'+t).classList.toggle('on',$('#t_'+t).checked));}
function symList(){return $('#c_symbols').value.split(/[\s,;]+/).map(x=>x.trim().toUpperCase()).filter(Boolean);}
function symCount(){const n=new Set(symList()).size;$('#s_symcount').textContent=n+' stock'+(n===1?'':'s');}
function fillSelect(el,vals,fmt){const k=vals.join(',');if(el.dataset.k===k)return;el.dataset.k=k;
  el.innerHTML=vals.map(v=>'<option value="'+v+'">'+fmt(v)+'</option>').join('');}
function paintSettings(s){
  const c=s.cfg;
  fillSelect($('#c_bar_minutes'),s.choices.bar,v=>v+' minute'+(v===1?'':'s'));
  fillSelect($('#c_ema_minutes'),s.choices.ema_tf,v=>v+' minutes');
  const fs=$('#f_sym'),uni=c.symbols.filter(x=>!(x in (s.skipped||{}))),k=uni.join(',');
  if(fs.dataset.k!==k){const cur=fs.value;fs.dataset.k=k;
    fs.innerHTML='<option value="">All stocks</option>'+uni.map(x=>'<option value="'+esc(x)+'">'+esc(x)+'</option>').join('');
    fs.value=uni.includes(cur)?cur:'';}
  const sk=Object.keys(s.skipped||{});
  $('#s_skipped').textContent=!s.scrip_day?'Checking which of these have options once the scrip master loads.':
    (sk.length?'Skipped - no stock options on NSE: '+sk.join(', '):'Every listed stock has options.');
  const e=s.estimate;
  $('#s_est').textContent='≈ '+e.contracts.toLocaleString('en-IN')+' contracts on '+e.stocks+' stocks: '+e.quote_calls+' market-quote call'+(e.quote_calls===1?'':'s')+
    ' per pass, so each contract gets a price about every '+e.seconds_per_price+'s. Loading their bar history takes about '+e.history_minutes+
    ' minutes (ATM strikes and open positions first); a contract cannot signal until its history is in.';
  $('#s_tok').textContent='Token '+s.token.human+' - from '+s.token.source+(s.token.client_id?' - client '+s.token.client_id:'')+
    '. Change it in NIFTY Trader\'s Broker token screen; this strategy restarts with it automatically.';
  $('#s_foot').textContent='Bars are anchored to 09:15 like TradingView; signals are only taken on a closed bar. The script exactly: momentum unit Rs, momentum 5, minimum premium 144.';
  if(touched)return;
  const sk2=c.symbols.join(',');
  if(symKey!==sk2||!$('#c_symbols').value){symKey=sk2;$('#c_symbols').value=c.symbols.join(', ');}
  $('#c_holidays').value=(c.holidays||[]).join(', ');
  ['CE','PE'].forEach(t=>$('#t_'+t).checked=c.opt_types.includes(t));sideChips();
  NUMS.forEach(k=>{const el=$('#c_'+k);if(el&&c[k]!=null)el.value=c[k];});
  $('#c_bar_minutes').value=c.bar_minutes;$('#c_ema_minutes').value=c.ema_minutes;
  $('#c_mom_unit').value=c.mom_unit;$('#c_ema_stop_on_tick').value=c.ema_stop_on_tick?'1':'0';
  symCount();
}
$('#b_n100').onclick=()=>{if(!S)return;$('#c_symbols').value=S.defaults.symbols.join(', ');touched=true;symCount();};
$('#b_save').onclick=async()=>{
  const b={};
  for(const k of NUMS){const el=$('#c_'+k);
    if(el.value.trim()===''){alert(el.closest('.fl').querySelector('label').textContent.trim()+' is empty.');el.focus();return;}
    b[k]=Number(el.value);}
  b.bar_minutes=Number($('#c_bar_minutes').value);b.ema_minutes=Number($('#c_ema_minutes').value);
  b.mom_unit=$('#c_mom_unit').value;b.ema_stop_on_tick=$('#c_ema_stop_on_tick').value==='1';
  b.opt_types=['CE','PE'].filter(t=>$('#t_'+t).checked);
  b.symbols=$('#c_symbols').value;b.holidays=$('#c_holidays').value;
  try{await post('/api/config',b);touched=false;symKey='';poll();}catch(e){alert(e.message);}
};
$('#b_revert').onclick=()=>{touched=false;symKey='';poll();};
$('#b_rewarm').onclick=async()=>{if(confirm('Reload the bar history of every contract from the broker? Signals pause on each contract until its history is back.')){await post('/api/rewarm');poll();}};

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

showTab(store.get('se_tab')||'dash');
poll();setInterval(poll,3000);
setInterval(()=>{if(TAB==='report')loadReport();},20000);
</script></body></html>"""


# ─────────────────────────────────────────────────────────────────────────────
#  BOOT
# ─────────────────────────────────────────────────────────────────────────────
STATE.load()
if not _env("ENGINE_OFF"):              # ENGINE_OFF=1: import without trading (tests)
    STATE.autostart = True              # launched = trading, once the stock list has loaded
    threading.Thread(target=scrip_loop, name="scrip", daemon=True).start()
    threading.Thread(target=engine_loop, name="engine", daemon=True).start()
    threading.Thread(target=warm_loop, name="history", daemon=True).start()
    log_event("boot", "stock-options EMA app up (pid %d, DATA_DIR=%s)" % (os.getpid(), DATA_DIR))

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
_MARGIN_NEXT = lambda lane, lots: _f(getattr(lane, "ask", 0)) * int(getattr(lane, "lot", 1) or 1) * lots


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


def _kill_close_all():
    now = clock()
    with STATE.lock:
        lanes = [l for l in STATE.lanes.values() if l.position]
    for lane in lanes:
        px = sell_price(lane, now) if lane.ltp_ts and now - lane.ltp_ts < 30 else None
        close_position(lane, "VIX_KILL", px or None)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(_env("PORT", "5003")), threaded=True, use_reloader=False)
