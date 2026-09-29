"""
NIFTY Trader - desktop hub
==========================

One window that lists every strategy in ../strategies, starts and stops them,
shows each one's dashboard inside the window, and lets you add new ones.

    python hub/hub.py               desktop window
    python hub/hub.py --no-window   serve the hub only and print its URL (debugging)

Built into "NIFTY Trader.exe" by hub/build_exe.bat.

HOW STRATEGIES RUN
------------------
Each strategy is a folder with a strategy.json and a Python file that defines a
Flask object called `app`.  The hub runs every strategy in its OWN process
(this same exe/script with --run-strategy), on a free localhost port.  So:

  * a crash in one strategy cannot take down the hub or the others,
  * two strategies can both have a global called STATE without clashing,
  * each strategy writes its state to <folder>/data and output to <folder>/logs.

Stopping asks the strategy to save (its _graceful()) before it exits. If the hub
itself dies, every strategy notices within a second and shuts itself down.
"""

import ast
import hashlib
import importlib.util
import json
import os
import re
import secrets
import shutil
import socket
import subprocess
import sys
import threading
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

FROZEN = getattr(sys, "frozen", False)
HUB_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
RES_DIR = getattr(sys, "_MEIPASS", HUB_SRC_DIR)      # bundled files when frozen
APP_NAME = "NIFTY Trader"
# Bump this, then push a matching tag (v1.2.3) to publish a GitHub release.
APP_VERSION = "1.6.0"
DEFAULT_UPDATE_REPO = "Shubham050396/Nifty-Trading-Software"
TOKEN_ENV = "NIFTY_HUB_TOKEN"
LOG_MAX_BYTES = 5 * 1024 * 1024


def _find_base():
    """The project folder: the first of exe-dir / parent / grandparent that has
    a strategies/ folder.  Lets the exe sit at the top level or one level down."""
    start = os.path.dirname(sys.executable) if FROZEN else os.path.dirname(HUB_SRC_DIR)
    d = start
    for _ in range(3):
        if os.path.isdir(os.path.join(d, "strategies")):
            return d
        d = os.path.dirname(d)
    return start


BASE_DIR = _find_base()
STRATEGIES_DIR = os.path.join(BASE_DIR, "strategies")
ARCHIVE_DIR = os.path.join(BASE_DIR, "_archive", "removed_strategies")
HUB_DIR = os.path.join(BASE_DIR, "hub")
BROKER_FILE = os.path.join(HUB_DIR, "broker.json")
GITHUB_FILE = os.path.join(HUB_DIR, "github.json")
RISK_FILE = os.path.join(HUB_DIR, "risk.json")
DEFAULT_VIX_LIMIT = 13.5
UPDATE_BACKUP_DIR = os.path.join(BASE_DIR, "_archive", "strategy_updates")


# ═════════════════════════════════════════════════════════════════════════════
#  BROKER CREDENTIALS  -  entered ONCE, for every strategy
#
#  Both strategies already read DHAN_ACCESS_TOKEN / DHAN_CLIENT_ID from their
#  environment, and treat the environment as outranking their own Settings tab.
#  So the hub stores the token here and injects it into every strategy process
#  it launches.  Their per-strategy Settings tabs then show it as "set from the
#  environment" and stop asking, which is what makes this the single place.
#
#  The token expires daily, so it is stored in plain JSON beside the app, the
#  same way each strategy already stored it in its own data folder.  Anyone who
#  can read this file could already read those.
# ═════════════════════════════════════════════════════════════════════════════
def read_broker():
    try:
        with open(BROKER_FILE, encoding="utf-8") as f:
            d = json.load(f)
        return {"access_token": (d.get("access_token") or "").strip(),
                "client_id": (d.get("client_id") or "").strip(),
                "saved_at": d.get("saved_at") or ""}
    except (OSError, ValueError):
        return {"access_token": "", "client_id": "", "saved_at": ""}


def write_broker(access_token, client_id):
    os.makedirs(HUB_DIR, exist_ok=True)
    rec = {"access_token": (access_token or "").strip(),
           "client_id": (client_id or "").strip(),
           "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    _write_json_atomic(BROKER_FILE, rec)
    try:
        if os.name != "nt":
            os.chmod(BROKER_FILE, 0o600)
    except OSError:
        pass
    return rec


# ═════════════════════════════════════════════════════════════════════════════
#  VIX LIMIT  -  the one place it is set
#
#  Option-SELLING strategies (credit spreads) stop trading and close every open
#  position while India VIX is above this.  Each such strategy re-reads this
#  file every cycle, so a change applies within a minute without a restart.
#  0 turns the kill switch off.
# ═════════════════════════════════════════════════════════════════════════════
KILL_DEFAULT_ON = ("credit_spreads", "ema_hedge")     # the option-selling ones


def read_risk():
    """{"vix_limit", "apply": {strategy id: ticked}}.  A strategy not saved
    yet is ticked only if it is one of the option-selling ones."""
    try:
        with open(RISK_FILE, encoding="utf-8") as f:
            d = json.load(f)
        v = float(d.get("vix_limit", DEFAULT_VIX_LIMIT))
        apply = {str(k): bool(x) for k, x in (d.get("apply") or {}).items()}
        return {"vix_limit": v if v >= 0 else DEFAULT_VIX_LIMIT, "apply": apply}
    except (OSError, ValueError, TypeError, AttributeError):
        return {"vix_limit": DEFAULT_VIX_LIMIT, "apply": {}}


def kill_applies(sid, risk=None):
    a = (risk or read_risk())["apply"]
    return a[sid] if sid in a else sid in KILL_DEFAULT_ON


def write_risk(body):
    try:
        v = round(float(body.get("vix_limit")), 2)
    except (TypeError, ValueError):
        raise ValueError("Enter the VIX limit as a number, e.g. 13.5 (0 turns it off).")
    if not (0 <= v <= 100):
        raise ValueError("The VIX limit must be between 0 and 100.")
    apply = read_risk()["apply"]
    if isinstance(body.get("apply"), dict):
        for sid, on in body["apply"].items():
            if isinstance(sid, str) and re.match(r"^[A-Za-z0-9_][A-Za-z0-9_.-]*$", sid):
                apply[sid] = bool(on)
    os.makedirs(HUB_DIR, exist_ok=True)
    _write_json_atomic(RISK_FILE, {"vix_limit": v, "apply": apply,
                                   "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    return read_risk()


# ═════════════════════════════════════════════════════════════════════════════
#  INDIA VIX  -  read by the hub with the broker token, shown in one place
#  (the sidebar).  Every minute in market hours, every 15 minutes otherwise.
# ═════════════════════════════════════════════════════════════════════════════
HUB_VIX = {"value": None, "at": "", "error": "not read yet", "checked": 0.0, "token": ""}
_IST = None


def _ist_now():
    global _IST
    if _IST is None:
        from datetime import timezone, timedelta
        _IST = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(_IST)


def _market_open(now):
    return now.weekday() < 5 and (9, 15) <= (now.hour, now.minute) <= (15, 30)


def fetch_vix_now():
    cred = read_broker()
    tok = cred["access_token"]
    if not tok:
        HUB_VIX.update(error="add your Dhan token in ⚙ → Broker token to see it", checked=time.time(), token="")
        return
    cid = cred["client_id"] or _jwt_client_id(tok)
    req = urllib.request.Request(
        "https://api.dhan.co/v2/marketfeed/ltp", data=json.dumps({"IDX_I": [21]}).encode(),
        headers={"access-token": tok, "client-id": cid, "Content-Type": "application/json",
                 "Accept": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            d = json.loads(r.read().decode("utf-8"))
        node = ((d.get("data") or {}).get("IDX_I") or {}).get("21") or {}
        v = float(node.get("last_price") or 0)
        if v <= 0:
            raise ValueError("no VIX in the answer")
        HUB_VIX.update(value=round(v, 2), at=_ist_now().strftime("%H:%M"), error="")
    except urllib.error.HTTPError as e:
        HUB_VIX.update(error="Dhan token expired - paste a fresh one in ⚙ → Broker token" if e.code in (401, 403)
                       else "Dhan answered HTTP %d" % e.code)
    except Exception as e:
        HUB_VIX.update(error="could not reach Dhan (%s)" % e.__class__.__name__)
    HUB_VIX.update(checked=time.time(), token=tok[-12:])


def _vix_loop():
    while True:
        try:
            gap = 60 if _market_open(_ist_now()) else 900
            fresh_token = read_broker()["access_token"][-12:] != HUB_VIX["token"]
            if fresh_token or time.time() - HUB_VIX["checked"] >= gap:
                fetch_vix_now()
        except Exception:
            traceback.print_exc()
        time.sleep(5)


def _jwt_claims(tok):
    """Decode a JWT's payload without verifying it. We are only reading claims
    the broker put there for our own display, never trusting them for access."""
    try:
        import base64
        part = tok.split(".")[1]
        part += "=" * (-len(part) % 4)
        return json.loads(base64.urlsafe_b64decode(part))
    except Exception:
        return {}


def _jwt_client_id(tok):
    """Dhan puts the client id inside the token. The strategies only derive it
    when a token is saved through their OWN settings form, so with the hub as
    the single entry point we must derive it here or a fresh strategy folder
    would run with no client id at all."""
    v = _jwt_claims(tok).get("dhanClientId")
    return str(v).strip() if v else ""


def _jwt_expiry(tok):
    """Dhan tokens are JWTs. Read the exp claim so the UI can warn before it
    dies mid-session, without calling the broker."""
    try:
        import base64
        part = tok.split(".")[1]
        part += "=" * (-len(part) % 4)
        exp = json.loads(base64.urlsafe_b64decode(part)).get("exp")
        return int(exp) if exp else None
    except Exception:
        return None


def _bundle_hint():  # pragma: no cover - never called
    """PyInstaller only packs modules it can see imported.  Strategies are loaded
    from disk at runtime, so anything they import must be named here or it will
    be missing from the exe.  Add to this list and rebuild if a strategy needs more."""
    import atexit, base64, bisect, calendar, collections, concurrent.futures, contextlib, copy, csv  # noqa
    import dataclasses, decimal, enum, fractions, functools, glob, gzip, hashlib, heapq, hmac, html  # noqa
    import http.cookies, io, itertools, logging, logging.handlers, math, operator, pathlib, pickle  # noqa
    import platform, pprint, queue, random, sqlite3, ssl, statistics, string, struct, tempfile  # noqa
    import textwrap, typing, urllib.parse, uuid, warnings, weakref, zipfile, zoneinfo, tzdata  # noqa
    import signal, msvcrt, xml.etree.ElementTree, email.utils, wsgiref.simple_server  # noqa
    import flask, requests, werkzeug, jinja2, markupsafe, itsdangerous, click, urllib3, certifi  # noqa
    import idna, charset_normalizer  # noqa


def _write_json_atomic(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def _read_manifest(sdir):
    with open(os.path.join(sdir, "strategy.json"), encoding="utf-8") as f:
        m = json.load(f)
    if not isinstance(m, dict):
        raise ValueError("strategy.json is not an object")
    return _manifest_defaults(m, os.path.basename(sdir))


def _manifest_defaults(m, sid):
    m.setdefault("name", sid)
    m.setdefault("description", "")
    m.setdefault("entry", "strategy.py")
    m.setdefault("app_object", "app")
    m.setdefault("data_env", "DATA_DIR")
    m.setdefault("icon", "📈")
    m.setdefault("color", "#38bdf8")
    m.setdefault("autostart", False)
    m.setdefault("runtime", "bundled")
    return m


# ═════════════════════════════════════════════════════════════════════════════
#  CHILD MODE  -  runs ONE strategy.  Invoked as:  <exe|hub.py> --run-strategy DIR --port N --parent-pid P
# ═════════════════════════════════════════════════════════════════════════════
def _arg(name, default=None):
    if name in sys.argv:
        i = sys.argv.index(name)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return default


def _watch_parent(ppid, on_gone):
    """Block until the hub process exits, then call on_gone.  Without this a
    killed hub would leave strategies trading with no window to see them."""
    try:
        if os.name == "nt":
            import ctypes
            k32 = ctypes.windll.kernel32
            k32.OpenProcess.restype = ctypes.c_void_p
            k32.OpenProcess.argtypes = [ctypes.c_uint32, ctypes.c_int, ctypes.c_uint32]
            k32.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
            h = k32.OpenProcess(0x00100000, 0, int(ppid))          # SYNCHRONIZE
            if h:
                k32.WaitForSingleObject(h, 0xFFFFFFFF)
        else:
            while True:
                time.sleep(1.0)
                os.kill(int(ppid), 0)
    except Exception:
        pass
    on_gone()


# Theme and text size for every strategy dashboard, set once in the hub.  The
# hub adds this to each strategy page as it is served (all six share the same
# colour variables) and then tells it what to use with postMessage, so no
# strategy has to know about it and a newly added one gets it for free.
_UI_SNIPPET = b"""<style id="nifty-hub-theme">
html[data-theme=light]{--bg:#f3f5f9;--panel:#ffffff;--p2:#eef1f6;--bd:#dde3ec;--bd2:#c5cfdc;
 --tx:#334155;--br:#0f172a;--mu:#5b6b82;--m2:#8a99ad;--ac:#0369a1;--border:#dde3ec;--border2:#c5cfdc}
html[data-theme=blue]{--bg:#0a1628;--panel:#0f2038;--p2:#142a48;--bd:#1e3a5f;--bd2:#2b4d78;
 --tx:#cfe0f5;--br:#f1f7ff;--mu:#86a3c7;--m2:#5d7ba1;--ac:#60a5fa;--border:#1e3a5f;--border2:#2b4d78}
html[data-theme=grey]{--bg:#1c1f24;--panel:#24282e;--p2:#2c3138;--bd:#3a4048;--bd2:#4a515b;
 --tx:#d4d8de;--br:#f5f6f8;--mu:#9aa2ad;--m2:#737b86;--ac:#5eb8e0;--border:#3a4048;--border2:#4a515b}
html[data-theme=light] body{background:var(--bg);color:var(--tx)}
</style><script>(function(){var T=["dark","light","blue","grey"];
function apply(d){if(!d||typeof d!=="object")return;var h=document.documentElement;
if(T.indexOf(d.theme)>=0)h.setAttribute("data-theme",d.theme);var z=+d.zoom;
if(z>=0.7&&z<=1.4)h.style.zoom=z;}
window.addEventListener("message",function(e){if(e.source===window.parent&&e.data&&e.data.nifty_ui)apply(e.data.nifty_ui);});
try{if(window.parent!==window)window.parent.postMessage({nifty_ui_ready:1},"*");}catch(e){}})();</script>
<style>#nifty-strip{display:flex;gap:18px;flex-wrap:wrap;align-items:baseline;padding:8px 16px;font:12px/1.4 'Segoe UI',system-ui,sans-serif;
 background:var(--panel,#121722);border-bottom:1px solid var(--bd,#222a3b);color:var(--mu,#7c8aa3)}
#nifty-strip b{color:var(--br,#f1f5f9);font-size:13px}#nifty-strip .u{color:#22c55e}#nifty-strip .d{color:#ef4444}
#nifty-strip .k{font-size:10px;font-weight:700;letter-spacing:.1em;margin-right:4px}</style>
<script>(function(){function rs(v){return v==null?"-":"\u20b9"+Math.round(Math.abs(v)).toLocaleString("en-IN");}
function sg(v){return v==null?"-":(v>0?"+":v<0?"\u2212":"")+rs(v);}function c(v){return v>0?"u":v<0?"d":"";}
function pc(v){return v==null?"":" ("+(v>0?"+":"")+v.toFixed(2)+"%)";}
function it(k,v){return '<span><span class="k">'+k+"</span>"+v+"</span>";}
function paint(m){var el=document.getElementById("nifty-strip");if(!el){el=document.createElement("div");el.id="nifty-strip";
document.body.insertBefore(el,document.body.firstChild);}if(!m||m.error){el.textContent="Margin: "+(m&&m.error||"unavailable");return;}
var h=it("MARGIN BLOCKED","<b>"+rs(m.margin_used)+"</b> ("+m.open+" open)")+
it("NEXT TRADE","<b>"+(m.margin_next==null?"-":rs(m.margin_next))+"</b>");
if(m.pnl_today!=null)h+=it("P&amp;L TODAY",'<b class="'+c(m.pnl_today)+'">'+sg(m.pnl_today)+"</b>"+pc(m.pct_today))+
it("OPEN",'<b class="'+c(m.pnl_open)+'">'+sg(m.pnl_open)+"</b>"+pc(m.pct_open))+
it("ALL-TIME",'<b class="'+c(m.pnl_all)+'">'+sg(m.pnl_all)+"</b>"+pc(m.pct_all));
el.title="Estimates: "+(m.basis||"");if(el.innerHTML!==h)el.innerHTML=h;}
function tick(){fetch("/__hub__/summary",{cache:"no-store"}).then(function(r){return r.json();}).then(paint).catch(function(){});}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",tick);else tick();setInterval(tick,5000);})();</script>"""


class _HubMiddleware:
    """Adds /__hub__/status and /__hub__/shutdown in front of the strategy's own
    Flask app, guarded by a per-launch token only the hub knows."""

    def __init__(self, app, token, mod, shutdown):
        self.app, self.token, self.mod, self.shutdown = app, token, mod, shutdown

    def _json(self, start_response, code, obj):
        body = json.dumps(obj).encode()
        start_response(code, [("Content-Type", "application/json"),
                              ("Content-Length", str(len(body)))])
        return [body]

    def _with_ui(self, environ, start_response):
        """Serve the strategy's page with _UI_SNIPPET added before </head>."""
        held = {}

        def capture(status, headers, exc_info=None):
            held["status"], held["headers"] = status, headers
            return lambda data: held.setdefault("early", []).append(data)
        body_iter = self.app(environ, capture)
        ctype = next((v for k, v in held.get("headers", []) if k.lower() == "content-type"), "")
        if not ctype.startswith("text/html"):
            start_response(held["status"], held["headers"])
            return body_iter
        try:
            body = b"".join(held.get("early", [])) + b"".join(body_iter)
        finally:
            if hasattr(body_iter, "close"):
                body_iter.close()
        if b"</head>" in body and b"nifty-hub-theme" not in body:
            body = body.replace(b"</head>", _UI_SNIPPET + b"</head>", 1)
        headers = [(k, v) for k, v in held["headers"] if k.lower() != "content-length"]
        headers.append(("Content-Length", str(len(body))))
        start_response(held["status"], headers)
        return [body]

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "")
        if not path.startswith("/__hub__/"):
            if environ.get("REQUEST_METHOD") == "GET" and not path.startswith("/api/"):
                return self._with_ui(environ, start_response)
            return self.app(environ, start_response)
        if path == "/__hub__/summary" and environ.get("REQUEST_METHOD") == "GET":
            # Read-only margin/P&L for the strip at the top of this strategy's
            # own page; no token, like the page itself.
            fn = getattr(self.mod, "hub_summary", None)
            try:
                return self._json(start_response, "200 OK", fn() if callable(fn) else {"error": "not reported"})
            except Exception as e:
                return self._json(start_response, "200 OK", {"error": "%s: %s" % (e.__class__.__name__, e)})
        if not secrets.compare_digest(environ.get("HTTP_X_HUB_TOKEN", ""), self.token):
            return self._json(start_response, "403 Forbidden", {"error": "bad token"})
        if path == "/__hub__/status":
            st = getattr(self.mod, "STATE", None)
            owner = getattr(st, "owner", getattr(st, "scanner_owner", None))
            summary = None
            fn = getattr(self.mod, "hub_summary", None)
            if callable(fn):
                try:
                    summary = fn()
                except Exception as e:             # a margin figure must never break status
                    summary = {"error": "%s: %s" % (e.__class__.__name__, e)}
            return self._json(start_response, "200 OK",
                              {"ok": True, "pid": os.getpid(), "owner": owner, "summary": summary})
        if path == "/__hub__/shutdown" and environ.get("REQUEST_METHOD") == "POST":
            threading.Thread(target=self.shutdown, daemon=True).start()
            return self._json(start_response, "200 OK", {"ok": True})
        return self._json(start_response, "404 Not Found", {"error": "unknown"})


def run_strategy_child():
    sdir = os.path.abspath(_arg("--run-strategy"))
    port = int(_arg("--port"))
    ppid = int(_arg("--parent-pid", "0") or 0)
    token = os.environ.pop(TOKEN_ENV, "")

    logs = os.path.join(sdir, "logs")
    os.makedirs(logs, exist_ok=True)
    log_path = os.path.join(logs, "output.log")
    try:
        if os.path.getsize(log_path) > LOG_MAX_BYTES:
            os.replace(log_path, log_path + ".1")
    except OSError:
        pass
    # Always to a file: a windowed exe has no console (print would raise), and
    # the hub's "Log" button reads this file.
    out = open(log_path, "a", encoding="utf-8", buffering=1, errors="replace")
    sys.stdout = sys.stderr = out
    print("\n==== %s  start (pid %d, port %d) ====" % (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"), os.getpid(), port), flush=True)

    try:
        man = _read_manifest(sdir)
        os.chdir(sdir)
        sys.path.insert(0, sdir)
        entry = os.path.join(sdir, man["entry"])
        modname = os.path.splitext(os.path.basename(entry))[0]
        spec = importlib.util.spec_from_file_location(modname, entry)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[modname] = mod
        spec.loader.exec_module(mod)
        app = getattr(mod, man["app_object"], None)
        if app is None or not callable(app):
            raise RuntimeError("%s has no Flask object called '%s'" % (man["entry"], man["app_object"]))
        # Every strategy is served from 127.0.0.1, and browsers scope cookies by
        # host, not port - so without a unique name two strategies' Flask
        # session cookies would overwrite each other.
        try:
            app.config["SESSION_COOKIE_NAME"] = "session_" + re.sub(r"\W", "_", os.path.basename(sdir))
        except Exception:
            pass
    except Exception:
        traceback.print_exc()
        out.flush()
        os._exit(3)

    from werkzeug.serving import make_server
    stopping = threading.Event()
    holder = {}

    def shutdown():
        if stopping.is_set():
            return
        stopping.set()
        print("hub: shutdown requested - saving state", flush=True)
        g = getattr(mod, "_graceful", None)
        if callable(g):
            try:
                g()
            except Exception:
                traceback.print_exc()
        srv = holder.get("srv")
        if srv:
            srv.shutdown()
        else:
            os._exit(0)

    srv = make_server("127.0.0.1", port, _HubMiddleware(app, token, mod, shutdown), threaded=True)
    holder["srv"] = srv
    if ppid:
        threading.Thread(target=_watch_parent, args=(ppid, shutdown), daemon=True).start()
    print("serving %s on http://127.0.0.1:%d" % (man["name"], port), flush=True)
    srv.serve_forever()
    # A strategy's own non-daemon thread must not keep a zombie alive.
    t = threading.Timer(6.0, os._exit, (0,))
    t.daemon = True
    t.start()
    sys.exit(0)


# ═════════════════════════════════════════════════════════════════════════════
#  HUB MODE  -  process manager
# ═════════════════════════════════════════════════════════════════════════════
def _free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _system_python():
    if not FROZEN:
        return sys.executable
    for name in ("python", "py"):
        p = shutil.which(name)
        if p and "WindowsApps" not in p:          # skip the Store stub
            return p
    return None


def _tail(path, n=400):
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - 200_000))
            return f.read().decode("utf-8", "replace").splitlines()[-n:]
    except OSError:
        return []


class Runner:
    def __init__(self, sid):
        self.id = sid
        self.dir = os.path.join(STRATEGIES_DIR, sid)
        self.proc = None
        self.port = None
        self.token = None
        self.pid = None
        self.state = "stopped"        # stopped | starting | running | stopping | crashed
        self.error = ""
        self.owner = None
        self.started_at = None
        self.summary, self.summary_at = None, 0.0
        self.lock = threading.RLock()

    def manifest(self):
        return _read_manifest(self.dir)

    def url(self):
        return "http://127.0.0.1:%d/" % self.port if self.port else None

    def _hub_call(self, path, method="GET", timeout=2.0):
        req = urllib.request.Request(self.url().rstrip("/") + path, method=method,
                                     headers={"X-Hub-Token": self.token}, data=b"" if method == "POST" else None)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())

    def start(self):
        with self.lock:
            if self.state in ("starting", "running", "stopping"):
                return
            m = self.manifest()
            entry = os.path.join(self.dir, m["entry"])
            if not os.path.isfile(entry):
                self.state, self.error = "crashed", "Entry file %s not found" % m["entry"]
                return
            if m["runtime"] == "system" or not FROZEN:
                py = _system_python()
                if not py:
                    self.state, self.error = "crashed", "runtime is 'system' but no Python is installed"
                    return
                hub_py = os.path.join(BASE_DIR, "hub", "hub.py") if FROZEN else os.path.abspath(__file__)
                cmd = [py, hub_py]
            else:
                cmd = [sys.executable]
            self.port = _free_port()
            self.token = secrets.token_urlsafe(24)
            cmd += ["--run-strategy", self.dir, "--port", str(self.port), "--parent-pid", str(os.getpid())]
            env = dict(os.environ)
            for k in ("HOST", "APP_ENV", "PORT"):       # never let a desktop strategy think it is hosted
                env.pop(k, None)
            if m.get("data_env"):
                env[m["data_env"]] = os.path.join(self.dir, "data")
            env[TOKEN_ENV] = self.token
            env["NIFTY_RISK_FILE"] = RISK_FILE
            env["PYTHONIOENCODING"] = "utf-8"
            # The one place the token is entered. Injected here so every
            # strategy sees the same credentials without its own Settings tab.
            cred = read_broker()
            if cred["access_token"]:
                env["DHAN_ACCESS_TOKEN"] = cred["access_token"]
            else:
                env.pop("DHAN_ACCESS_TOKEN", None)
            cid = cred["client_id"] or _jwt_client_id(cred["access_token"])
            if cid:
                env["DHAN_CLIENT_ID"] = cid
            flags = 0x08000000 if os.name == "nt" else 0          # CREATE_NO_WINDOW
            self.state, self.error, self.owner, self.pid = "starting", "", None, None
            self.started_at = time.time()
            self.proc = subprocess.Popen(cmd, cwd=self.dir, env=env, creationflags=flags,
                                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                         stderr=subprocess.DEVNULL)
            threading.Thread(target=self._supervise, args=(self.proc,), daemon=True).start()

    def _supervise(self, proc):
        deadline = time.time() + 120
        while proc.poll() is None and self.state == "starting" and time.time() < deadline:
            try:
                st = self._hub_call("/__hub__/status", timeout=1.5)
                with self.lock:
                    if self.proc is proc and self.state == "starting":
                        self.state, self.pid, self.owner = "running", st.get("pid"), st.get("owner")
                break
            except Exception:
                time.sleep(0.4)
        if proc.poll() is None and self.state == "starting":
            self.error = "did not answer within 120s - see Log"
        code = proc.wait()
        with self.lock:
            if self.proc is not proc:
                return
            if self.state == "stopping":
                self.state = "stopped"
            else:
                self.state = "crashed"
                tail = [ln for ln in _tail(os.path.join(self.dir, "logs", "output.log"), 60) if ln.strip()]
                last = next((ln for ln in reversed(tail) if "Error" in ln or "Exception" in ln), tail[-1] if tail else "")
                self.error = "exited with code %s. %s" % (code, last.strip()[:300])
            self.proc, self.port, self.pid = None, None, None

    def refresh_summary(self, max_age=5.0):
        """Margin figures from the running strategy, at most every few seconds."""
        if self.state != "running" or time.time() - self.summary_at < max_age:
            return
        self.summary_at = time.time()
        try:
            st = self._hub_call("/__hub__/status", timeout=1.5)
            self.summary, self.owner = st.get("summary"), st.get("owner", self.owner)
        except Exception:
            pass

    def refresh_owner(self):
        if self.state == "running":
            try:
                self.owner = self._hub_call("/__hub__/status", timeout=1.0).get("owner")
            except Exception:
                pass

    def stop(self, wait=10.0):
        with self.lock:
            proc = self.proc
            if not proc or self.state in ("stopped", "crashed"):
                return
            self.state = "stopping"
        try:
            self._hub_call("/__hub__/shutdown", method="POST", timeout=3)
        except Exception:
            pass
        try:
            proc.wait(timeout=wait)
        except subprocess.TimeoutExpired:
            # /T: under a onefile exe the real Python process is a CHILD of the
            # bootloader we launched; killing only the bootloader orphans it.
            if os.name == "nt":
                subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)],
                               creationflags=0x08000000, capture_output=True)
            else:
                proc.kill()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
        # Mark it stopped HERE, not only in _supervise.  A restart is stop()
        # then start(), and start() refuses to run while the state is still
        # "stopping" - so leaving this to the supervisor thread makes restart
        # silently leave the strategy down whenever the supervisor is a moment
        # behind.  Guarded on `is proc` so a newer process is never clobbered.
        with self.lock:
            if self.proc is proc:
                self.state, self.proc, self.port, self.pid = "stopped", None, None, None

    def info(self):
        try:
            m = self.manifest()
            bad = ""
        except Exception as e:
            m, bad = {"name": self.id, "description": "", "icon": "⚠️", "color": "#ef4444",
                      "entry": "?", "autostart": False, "runtime": "bundled", "data_env": ""}, str(e)
        return {
            "id": self.id, "name": m["name"], "description": m["description"],
            "icon": m["icon"], "color": m["color"], "entry": m["entry"],
            "autostart": bool(m["autostart"]), "runtime": m["runtime"],
            "state": self.state, "error": bad or self.error, "owner": self.owner,
            "port": self.port, "url": self.url() if self.state == "running" else None,
            "pid": self.pid, "folder": self.dir,
            "uptime": int(time.time() - self.started_at) if self.started_at and self.state == "running" else None,
            "summary": self.summary if self.state == "running" else None,
        }


class Manager:
    def __init__(self):
        self.lock = threading.RLock()
        self.runners = {}
        os.makedirs(STRATEGIES_DIR, exist_ok=True)
        self.scan()

    def scan(self):
        with self.lock:
            found = sorted(d for d in os.listdir(STRATEGIES_DIR)
                           if os.path.isfile(os.path.join(STRATEGIES_DIR, d, "strategy.json")))
            for sid in found:
                self.runners.setdefault(sid, Runner(sid))
            for sid in list(self.runners):
                if sid not in found and self.runners[sid].state in ("stopped", "crashed"):
                    del self.runners[sid]
            return [self.runners[s] for s in found if s in self.runners]

    def get(self, sid):
        with self.lock:
            r = self.runners.get(sid)
        if not r:
            raise KeyError(sid)
        return r

    def stop_all(self):
        ts = [threading.Thread(target=r.stop, daemon=True) for r in list(self.runners.values())]
        for t in ts:
            t.start()
        for t in ts:
            t.join(15)


# ═════════════════════════════════════════════════════════════════════════════
#  NEW STRATEGIES
# ═════════════════════════════════════════════════════════════════════════════
def _slug(name):
    s = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")[:40] or "strategy"
    base, i = s, 2
    while os.path.exists(os.path.join(STRATEGIES_DIR, s)):
        s = "%s_%d" % (base, i)
        i += 1
    return s


_STDLIB = set(getattr(sys, "stdlib_module_names", ()))


def inspect_code(code, app_object="app"):
    """Check an imported .py before it is installed. Returns (errors, warnings, data_env)."""
    errors, warnings = [], []
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return ["Python syntax error on line %s: %s" % (e.lineno, e.msg)], [], None

    has_app = False
    for node in tree.body:
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets = [node.target]
        for t in targets:
            if isinstance(t, ast.Name) and t.id == app_object:
                has_app = True
    if not has_app:
        errors.append("No top-level `%s = Flask(__name__)` found. The hub shows a strategy by "
                      "serving its Flask app, so the file must define one." % app_object)

    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            roots.add(node.module.split(".")[0])
    missing = sorted(r for r in roots if r not in _STDLIB and r != "config"
                     and importlib.util.find_spec(r) is None)
    if missing:
        warnings.append("Uses packages that are not available here: %s. Install them "
                        "(pip install %s) and set Runtime to 'System Python'."
                        % (", ".join(missing), " ".join(missing)))

    m = re.search(r"""(?:_env|environ\.get|getenv)\(\s*["']([A-Z0-9_]*DATA[A-Z0-9_]*DIR)["']""", code)
    return errors, warnings, (m.group(1) if m else None)


def create_strategy(body):
    name = (body.get("name") or "").strip()[:60]
    if not name:
        raise ValueError("Give the strategy a name.")
    mode = body.get("mode")
    manifest = {"name": name, "description": (body.get("description") or "").strip()[:300],
                "icon": (body.get("icon") or "📈")[:4], "color": body.get("color") or "#38bdf8",
                "app_object": "app", "autostart": False, "runtime": "bundled"}
    warnings = []
    if mode == "template":
        with open(os.path.join(RES_DIR, "strategy_template.py"), encoding="utf-8") as f:
            code = f.read().replace("__STRATEGY_NAME__", name.replace('"', "'"))
        manifest.update(entry="strategy.py", data_env="DATA_DIR")
    elif mode == "import":
        code = body.get("code") or ""
        if len(code) > 5 * 1024 * 1024:
            raise ValueError("That file is over 5 MB.")
        errors, warnings, data_env = inspect_code(code)
        if errors:
            raise ValueError(" ".join(errors))
        fname = re.sub(r"[^A-Za-z0-9_.-]", "_", os.path.basename(body.get("filename") or "strategy.py"))
        if not fname.endswith(".py"):
            fname += ".py"
        manifest.update(entry=fname, data_env=data_env or "")
        if warnings:
            manifest["runtime"] = "system"
    else:
        raise ValueError("unknown mode")

    sid = _slug(name)
    sdir = os.path.join(STRATEGIES_DIR, sid)
    os.makedirs(os.path.join(sdir, "data"))
    with open(os.path.join(sdir, manifest["entry"]), "w", encoding="utf-8", newline="\n") as f:
        f.write(code)
    _write_json_atomic(os.path.join(sdir, "strategy.json"), manifest)
    return sid, warnings


def update_manifest(sid, body):
    path = os.path.join(STRATEGIES_DIR, sid, "strategy.json")
    m = _read_manifest(os.path.dirname(path))
    for k in ("name", "description", "icon", "color"):
        if k in body and isinstance(body[k], str):
            m[k] = body[k].strip()[:300] or m[k]
    if "autostart" in body:
        m["autostart"] = bool(body["autostart"])
    if body.get("runtime") in ("bundled", "system"):
        m["runtime"] = body["runtime"]
    _write_json_atomic(path, m)
    return m


def archive_strategy(sid):
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    dest = os.path.join(ARCHIVE_DIR, "%s_%s" % (sid, datetime.now().strftime("%Y%m%d_%H%M%S")))
    shutil.move(os.path.join(STRATEGIES_DIR, sid), dest)
    return dest


def _restart_later(runner):
    """Stop then start a strategy on a background thread, so it loads new
    credentials or new code without the caller waiting for it to save."""
    def _re():
        try:
            runner.stop()
            runner.start()
        except Exception:
            traceback.print_exc()
    threading.Thread(target=_re, daemon=True).start()


# ═════════════════════════════════════════════════════════════════════════════
#  UPDATES FROM GITHUB
#
#  strategies/ in the GitHub repository is the master copy of every strategy's
#  code.  A check compares each file there with the local copy by its git blob
#  hash, so nothing is downloaded until something actually differs.  Installing:
#
#    * only touches code: data/ and logs/ are never read from GitHub or written,
#      so trade books, state and tokens stay exactly as they were;
#    * copies every file it replaces to _archive/strategy_updates/ first;
#    * keeps this PC's own choices in strategy.json (autostart, runtime);
#    * never deletes a local file, and leaves strategies that only exist on
#      this PC alone;
#    * restarts a running strategy so it loads the new code.
#
#  A running exe cannot replace itself, so for the app the hub only checks the
#  latest GitHub release and offers its download page.
# ═════════════════════════════════════════════════════════════════════════════
_REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
_SID_RE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_.-]*$")
_NEVER_SYNC_DIRS = {"data", "logs", "__pycache__"}
_NEVER_SYNC_FILES = {"secret_key", "runtime.json", "broker.json", "github.json", "config.py"}
_KEEP_LOCAL = ("autostart", "runtime")
_MAX_SYNC_FILE = 20 * 1024 * 1024
_update_lock = threading.Lock()
_last_check = {}


class UpdateError(Exception):
    def __init__(self, msg, code=None):
        super().__init__(msg)
        self.code = code


def read_github():
    try:
        with open(GITHUB_FILE, encoding="utf-8") as f:
            d = json.load(f)
    except (OSError, ValueError):
        d = {}
    return {"repo": (d.get("repo") or DEFAULT_UPDATE_REPO).strip(),
            "branch": (d.get("branch") or "").strip(),
            "token": (d.get("token") or "").strip()}


def write_github(body):
    repo = (body.get("repo") or DEFAULT_UPDATE_REPO).strip()
    repo = re.sub(r"^(https?://)?(www\.)?github\.com/", "", repo).strip("/")
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not _REPO_RE.match(repo):
        raise ValueError("Repository should look like owner/name, e.g. %s" % DEFAULT_UPDATE_REPO)
    branch = (body.get("branch") or "").strip()
    if branch and (".." in branch or not re.match(r"^[A-Za-z0-9._/-]+$", branch)):
        raise ValueError("That is not a valid branch name.")
    # A blank token field means "keep the saved one", so the token never has
    # to be sent back to the page just to save the other fields.
    token = read_github()["token"]
    if body.get("clear_token"):
        token = ""
    elif (body.get("token") or "").strip():
        token = body["token"].strip()
    os.makedirs(HUB_DIR, exist_ok=True)
    _write_json_atomic(GITHUB_FILE, {"repo": repo, "branch": branch, "token": token})
    try:
        if os.name != "nt":
            os.chmod(GITHUB_FILE, 0o600)
    except OSError:
        pass
    return read_github()


def _gh(cfg, path, raw=False, accept=None, timeout=30):
    """GET https://api.github.com/repos/<repo><path>.  raw=True returns bytes."""
    req = urllib.request.Request(
        "https://api.github.com/repos/%s%s" % (cfg["repo"], path),
        headers={"Accept": accept or ("application/vnd.github.raw" if raw else "application/vnd.github+json"),
                 "X-GitHub-Api-Version": "2022-11-28",
                 "User-Agent": "NIFTY-Trader/" + APP_VERSION})
    if cfg["token"]:
        # Unredirected: if GitHub ever redirects to another host, the token stays behind.
        req.add_unredirected_header("Authorization", "Bearer " + cfg["token"])
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise UpdateError(
                "GitHub could not find %s (or its branch). " % cfg["repo"] +
                ("Check the names in Update settings, and that the token can read this repository."
                 if cfg["token"] else
                 "If the repository is private, add a GitHub token in Update settings."), 404)
        if e.code == 401:
            raise UpdateError("GitHub rejected the token. Paste a new one in Update settings.", 401)
        if e.code in (403, 429) and e.headers.get("X-RateLimit-Remaining") == "0":
            raise UpdateError("GitHub's hourly request limit was reached. Try again later%s."
                              % ("" if cfg["token"] else ", or add a token to raise the limit"), e.code)
        raise UpdateError("GitHub answered HTTP %d." % e.code, e.code)
    except (urllib.error.URLError, OSError) as e:
        raise UpdateError("Could not reach GitHub: %s" % getattr(e, "reason", e))
    return data if raw else json.loads(data.decode("utf-8"))


def _blob_sha(data):
    """The id git gives a file's content, so a local file can be compared with
    one on GitHub without downloading it."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _local_sha(path):
    try:
        with open(path, "rb") as f:
            return _blob_sha(f.read())
    except OSError:
        return None


def _syncable(rel):
    """Whether strategies/<sid>/<rel> on GitHub is code this PC should take.
    Also refuses anything that could climb out of the strategy's folder."""
    parts = rel.split("/")
    if any(p in ("", ".", "..") for p in parts) or "\\" in rel or ":" in rel:
        return False
    if any(p in _NEVER_SYNC_DIRS for p in parts[:-1]) or parts[-1] in _NEVER_SYNC_FILES:
        return False
    name = parts[-1]
    return not (name.endswith((".pyc", ".bak", ".tmp", ".lock", ".log", ".pid")) or ".bak." in name)


def _remote_strategies(cfg):
    """({repo, branch, commit, ...}, {sid: {relpath: blob sha}}) for each
    strategies/<sid>/ on GitHub that has a strategy.json."""
    branch = cfg["branch"] or _gh(cfg, "")["default_branch"]
    commit = _gh(cfg, "/branches/" + urllib.parse.quote(branch, safe="/"))["commit"]
    tree = _gh(cfg, "/git/trees/%s?recursive=1" % commit["commit"]["tree"]["sha"])
    found = {}
    for e in tree.get("tree", []):
        parts = e.get("path", "").split("/", 2)
        if e.get("type") != "blob" or len(parts) < 3 or parts[0] != "strategies":
            continue
        sid, rel = parts[1], parts[2]
        if _SID_RE.match(sid) and _syncable(rel) and (e.get("size") or 0) <= _MAX_SYNC_FILE:
            found.setdefault(sid, {})[rel] = e["sha"]
    found = {sid: files for sid, files in found.items() if "strategy.json" in files}
    info = {"repo": cfg["repo"], "branch": branch, "commit": commit["sha"][:7],
            "date": commit["commit"]["committer"]["date"],
            "message": (commit["commit"]["message"].splitlines() or [""])[0][:120],
            "truncated": bool(tree.get("truncated"))}
    return info, found


def _manifest_from(raw, sdir):
    """GitHub's strategy.json with this PC's own choices kept, normalised the
    same way as _read_manifest so the two compare equal when nothing changed."""
    m = json.loads(raw.decode("utf-8"))
    if not isinstance(m, dict):
        raise ValueError("strategy.json is not an object")
    local = _local_manifest(sdir)
    if local:
        for k in _KEEP_LOCAL:
            m[k] = local[k]
    return _manifest_defaults(m, os.path.basename(sdir))


def _local_manifest(sdir):
    try:
        return _read_manifest(sdir)
    except (OSError, ValueError):
        return None


def _changes(cfg, sid, files):
    """What installing <sid> from GitHub would change here.
    Returns ({relpath: blob sha} to download, merged manifest or None)."""
    sdir = os.path.join(STRATEGIES_DIR, sid)
    todo = {rel: sha for rel, sha in files.items()
            if _local_sha(os.path.join(sdir, *rel.split("/"))) != sha}
    man = None
    if "strategy.json" in todo:
        # Byte-different is not enough: this PC keeps its own autostart and
        # runtime, so compare what would actually be written.
        try:
            man = _manifest_from(_gh(cfg, "/git/blobs/" + files["strategy.json"], raw=True), sdir)
        except ValueError:
            raise UpdateError("strategy.json for %s on GitHub is not valid JSON." % sid)
        if man == _local_manifest(sdir):
            del todo["strategy.json"]
    return todo, man


def _version_tuple(v):
    return tuple(int(x) for x in re.findall(r"\d+", v or "")[:3])


def _latest_release(cfg):
    try:
        r = _gh(cfg, "/releases/latest")
    except UpdateError as e:
        return {"error": None if e.code == 404 else str(e)}      # 404: nothing released yet
    tag = r.get("tag_name") or ""
    url = r.get("html_url") or ""
    zips = [a for a in (r.get("assets") or [])
            if str(a.get("name", "")).lower().endswith("windows.zip") and a.get("id")]
    return {"tag": tag, "name": r.get("name") or tag, "published_at": r.get("published_at"),
            "url": url if url.startswith("https://github.com/") else "",
            "newer": _version_tuple(tag) > _version_tuple(APP_VERSION),
            "asset_id": zips[0]["id"] if zips else None,
            "asset_size": zips[0].get("size") if zips else None}


def can_self_update():
    return FROZEN and os.name == "nt"


# Runs after the hub has exited: waits for this process (and the onefile
# bootloader that holds the exe open) to go, swaps the exe, and reopens it.
_SWAP_BAT = r"""@echo off
set /a n=0
:wait
set /a n+=1
if %n% gtr 90 goto swap
tasklist /FI "PID eq __PID__" 2>nul | find " __PID__ " >nul && (ping -n 2 127.0.0.1 >nul & goto wait)
if %n% gtr 30 goto swap
tasklist /FI "PID eq __PPID__" 2>nul | find " __PPID__ " >nul && (ping -n 2 127.0.0.1 >nul & goto wait)
:swap
for /L %%i in (1,1,40) do (
  move /Y "__NEW__" "__EXE__" >nul 2>&1 && goto open
  ping -n 2 127.0.0.1 >nul
)
:open
start "" "__EXE__"
(goto) 2>nul & del "%~f0"
"""


def install_app_update(mgr):
    """Download the latest release's exe, then close and let _SWAP_BAT replace
    this exe and reopen it.  Strategies and their data are not touched."""
    if not can_self_update():
        raise UpdateError("Only the installed NIFTY Trader.exe on Windows can update itself.")
    if not _update_lock.acquire(blocking=False):
        raise UpdateError("An update is already being installed.")
    try:
        cfg = read_github()
        rel = _latest_release(cfg)
        if rel.get("error"):
            raise UpdateError(rel["error"])
        if not rel.get("newer"):
            raise UpdateError("This is already the latest version.")
        if not rel.get("asset_id"):
            raise UpdateError("The %s release has no Windows zip to install." % rel.get("tag"))
        data = _gh(cfg, "/releases/assets/%d" % int(rel["asset_id"]), raw=True,
                   accept="application/octet-stream", timeout=300)
        import io
        import zipfile
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                names = [n for n in z.namelist() if n.replace("\\", "/").split("/")[-1] == "NIFTY Trader.exe"]
                if not names:
                    raise UpdateError("NIFTY Trader.exe is missing from the downloaded zip.")
                exe_bytes = z.read(names[0])
        except zipfile.BadZipFile:
            raise UpdateError("The download is not a valid zip. Try again.")
        if len(exe_bytes) < 1_000_000 or exe_bytes[:2] != b"MZ":
            raise UpdateError("The downloaded NIFTY Trader.exe does not look right. Nothing was changed.")

        exe = os.path.abspath(sys.executable)
        new = exe[:-4] + ".new.exe"
        with open(new, "wb") as f:
            f.write(exe_bytes)
            f.flush()
            os.fsync(f.fileno())
        try:
            shutil.copy2(exe, exe[:-4] + ".old.exe")        # to roll back by hand
        except OSError:
            pass
        bat = os.path.join(os.environ.get("TEMP") or BASE_DIR, "nifty_trader_update.bat")
        script = (_SWAP_BAT.replace("__PID__", str(os.getpid())).replace("__PPID__", str(os.getppid()))
                  .replace("__NEW__", new.replace("%", "%%")).replace("__EXE__", exe.replace("%", "%%")))
        with open(bat, "w", encoding="mbcs" if os.name == "nt" else "utf-8", newline="\r\n") as f:
            f.write(script)
        subprocess.Popen(["cmd", "/c", bat], creationflags=0x08000000 | 0x00000200,
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL, close_fds=True)
    finally:
        _update_lock.release()

    def _quit():
        time.sleep(1.5)                   # let the page show "restarting"
        mgr.stop_all()
        os._exit(0)
    threading.Thread(target=_quit, daemon=True).start()
    return rel["tag"]


def check_updates():
    cfg = read_github()
    res = {"version": APP_VERSION, "checked_at": time.time(), "strategies": [], "available": 0}
    try:
        info, remote = _remote_strategies(cfg)
        res["source"] = info
        for sid in sorted(remote):
            todo, man = _changes(cfg, sid, remote[sid])
            local = _local_manifest(os.path.join(STRATEGIES_DIR, sid))
            m = local or man or {}
            status = "new" if not local else ("update" if todo else "current")
            res["strategies"].append({"id": sid, "name": m.get("name") or sid, "icon": m.get("icon") or "📈",
                                      "status": status, "files": sorted(todo)})
        on_github = set(remote)
        for sid in sorted(os.listdir(STRATEGIES_DIR)):
            local = _local_manifest(os.path.join(STRATEGIES_DIR, sid))
            if local and sid not in on_github:
                res["strategies"].append({"id": sid, "name": local["name"], "icon": local["icon"],
                                          "status": "local", "files": []})
        res["available"] = sum(1 for s in res["strategies"] if s["status"] in ("new", "update"))
    except UpdateError as e:
        res["error"] = str(e)
    except (KeyError, TypeError, ValueError) as e:
        res["error"] = "Unexpected answer from GitHub (%s)." % e
    res["release"] = _latest_release(cfg)
    _last_check.clear()
    _last_check.update(res)
    return res


def install_updates(mgr, sids):
    """Install the GitHub version of each strategy in sids.  Returns
    [{id, files, backup}] and the ids that were restarted."""
    if not _update_lock.acquire(blocking=False):
        raise UpdateError("An update is already being installed.")
    try:
        cfg = read_github()
        _, remote = _remote_strategies(cfg)
        # Download everything before writing anything: a dropped connection
        # must never leave a strategy half old code, half new.
        plan = []
        for sid in sids:
            if not _SID_RE.match(sid or "") or sid not in remote:
                raise UpdateError("%s is not on GitHub (any more). Check again." % sid)
            todo, man = _changes(cfg, sid, remote[sid])
            blobs = {}
            for rel, sha in todo.items():
                if rel == "strategy.json":
                    continue
                data = _gh(cfg, "/git/blobs/" + sha, raw=True)
                if _blob_sha(data) != sha:
                    raise UpdateError("The download of %s/%s was damaged. Nothing was changed." % (sid, rel))
                blobs[rel] = data
            if blobs or "strategy.json" in todo:
                plan.append((sid, blobs, man if "strategy.json" in todo else None))

        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        done = []
        for sid, blobs, man in plan:
            sdir = os.path.join(STRATEGIES_DIR, sid)
            backup = os.path.join(UPDATE_BACKUP_DIR, "%s_%s" % (sid, stamp))
            rels = sorted(blobs) + (["strategy.json"] if man else [])
            for rel in rels:
                src = os.path.join(sdir, *rel.split("/"))
                if os.path.isfile(src):
                    dst = os.path.join(backup, *rel.split("/"))
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy2(src, dst)
            os.makedirs(os.path.join(sdir, "data"), exist_ok=True)
            for rel, data in blobs.items():
                path = os.path.join(sdir, *rel.split("/"))
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path + ".tmp", "wb") as f:
                    f.write(data)
                    f.flush()
                    os.fsync(f.fileno())
                os.replace(path + ".tmp", path)
            # Last, so a strategy only appears in the list once its code is in place.
            if man:
                _write_json_atomic(os.path.join(sdir, "strategy.json"), man)
            done.append({"id": sid, "files": rels, "backup": backup if os.path.isdir(backup) else None})
    finally:
        _update_lock.release()

    mgr.scan()
    restarted = []
    for d in done:
        try:
            r = mgr.get(d["id"])
        except KeyError:
            continue
        if r.state in ("running", "starting"):
            _restart_later(r)
            restarted.append(r.id)
    return done, restarted


def _auto_check():
    """Check once shortly after launch, then every few hours, so the sidebar
    can say an update is waiting without anyone having to look."""
    time.sleep(5)
    while True:
        try:
            check_updates()
        except Exception:
            traceback.print_exc()
        time.sleep(6 * 3600)


# ═════════════════════════════════════════════════════════════════════════════
#  HUB WEB API
# ═════════════════════════════════════════════════════════════════════════════
def build_hub_app(mgr, port_holder):
    from flask import Flask, jsonify, request, Response
    hub = Flask("nifty_hub")
    token = secrets.token_urlsafe(24)

    @hub.before_request
    def _guard():
        # Only this window may drive the hub.  The Host check blocks DNS
        # rebinding; the token (only ever written into our own page) blocks any
        # other web page on this machine from POSTing "create strategy" here.
        port = port_holder["port"]
        if request.host not in ("127.0.0.1:%d" % port, "localhost:%d" % port):
            return Response("forbidden", 403)
        if request.path.startswith("/api/") and not secrets.compare_digest(
                request.headers.get("X-Hub-Token", ""), token):
            return jsonify({"error": "forbidden"}), 403
        return None

    def ok(**kw):
        kw.setdefault("ok", True)
        return jsonify(kw)

    def fail(msg, code=400):
        return jsonify({"error": str(msg)}), code

    @hub.route("/")
    def index():
        with open(os.path.join(RES_DIR, "hub_ui.html"), encoding="utf-8") as f:
            html = f.read()
        return Response(html.replace("__HUB_TOKEN__", token), mimetype="text/html",
                        headers={"Cache-Control": "no-store"})

    @hub.route("/api/strategies")
    def list_strategies():
        runners = mgr.scan()
        for r in runners:
            r.refresh_summary()
        lim = read_risk()["vix_limit"]
        return ok(strategies=[r.info() for r in runners], base=BASE_DIR,
                  frozen=FROZEN, system_python=bool(_system_python()),
                  vix={"value": HUB_VIX["value"], "at": HUB_VIX["at"], "error": HUB_VIX["error"],
                       "limit": lim, "above": bool(lim > 0 and HUB_VIX["value"] and HUB_VIX["value"] > lim)})

    @hub.route("/api/broker", methods=["GET"])
    def broker_get():
        c = read_broker()
        tok = c["access_token"]
        exp = _jwt_expiry(tok) if tok else None
        derived = _jwt_client_id(tok) if tok else ""
        return ok(configured=bool(tok), client_id=c["client_id"], derived_client_id=derived,
                  saved_at=c["saved_at"],
                  tail=tok[-6:] if len(tok) > 6 else "", expires_at=exp,
                  expired=bool(exp and exp <= time.time()))

    @hub.route("/api/broker", methods=["POST"])
    def broker_set():
        body = request.get_json(silent=True) or {}
        write_broker(body.get("access_token"), body.get("client_id"))
        # A running strategy read the old token at launch, so it must be
        # restarted to pick this up. Doing it here is the whole point of having
        # one place: the user should not have to remember to do it per strategy.
        restarted = []
        for r in mgr.scan():
            if r.state in ("running", "starting"):
                _restart_later(r)
                restarted.append(r.id)
        return ok(restarted=restarted)

    def _github_settings():
        c = read_github()
        return {"repo": c["repo"], "branch": c["branch"], "has_token": bool(c["token"]),
                "token_tail": c["token"][-4:] if len(c["token"]) > 8 else ""}

    @hub.route("/api/updates", methods=["GET"])
    def updates_get():
        return ok(version=APP_VERSION, last=dict(_last_check) or None, settings=_github_settings(),
                  can_self_update=can_self_update())

    @hub.route("/api/updates/check", methods=["POST"])
    def updates_check():
        return ok(version=APP_VERSION, last=check_updates(), settings=_github_settings(),
                  can_self_update=can_self_update())

    @hub.route("/api/updates/install", methods=["POST"])
    def updates_install():
        body = request.get_json(force=True, silent=True) or {}
        ids = [s for s in (body.get("ids") or []) if isinstance(s, str)]
        if not ids:
            return fail("Pick at least one strategy to update.")
        try:
            done, restarted = install_updates(mgr, ids)
        except (UpdateError, OSError) as e:
            return fail(e)
        return ok(installed=done, restarted=restarted, last=check_updates())

    @hub.route("/api/updates/settings", methods=["POST"])
    def updates_settings():
        try:
            write_github(request.get_json(force=True, silent=True) or {})
        except ValueError as e:
            return fail(e)
        return ok(settings=_github_settings())

    @hub.route("/api/updates/install-app", methods=["POST"])
    def updates_install_app():
        try:
            tag = install_app_update(mgr)
        except (UpdateError, OSError) as e:
            return fail(e)
        return ok(tag=tag)

    @hub.route("/api/updates/open-release", methods=["POST"])
    def updates_open_release():
        url = ((_last_check.get("release") or {}).get("url") or "")
        if not url.startswith("https://github.com/"):
            return fail("No release to open. Check for updates first.")
        import webbrowser
        webbrowser.open(url)
        return ok()

    def _risk_view():
        r = read_risk()
        strategies = []
        for x in mgr.scan():
            try:
                m = x.manifest()
            except Exception:
                continue
            kind = ("sells options - recommended" if x.id in KILL_DEFAULT_ON else
                    "buys, and sells short on a down-cross" if x.id == "macd_monthly" else "buys options")
            strategies.append({"id": x.id, "name": m["name"], "icon": m["icon"],
                               "on": kill_applies(x.id, r), "kind": kind})
        return {"vix_limit": r["vix_limit"], "strategies": strategies}

    @hub.route("/api/risk", methods=["GET"])
    def risk_get():
        return ok(**_risk_view(), default=DEFAULT_VIX_LIMIT)

    @hub.route("/api/risk", methods=["POST"])
    def risk_set():
        try:
            write_risk(request.get_json(force=True, silent=True) or {})
        except ValueError as e:
            return fail(e)
        return ok(**_risk_view())

    @hub.route("/api/strategies/all/<action>", methods=["POST"])
    def act_all(action):
        # Start every stopped strategy (or stop every running one) in one click.
        done = []
        for r in mgr.scan():
            if action == "start" and r.state in ("stopped", "crashed"):
                r.start()
                done.append(r.id)
            elif action == "stop" and r.state in ("running", "starting"):
                threading.Thread(target=r.stop, daemon=True).start()
                done.append(r.id)
        if action not in ("start", "stop"):
            return fail("unknown action", 404)
        return ok(ids=done)

    @hub.route("/api/strategies/<sid>/<action>", methods=["POST"])
    def act(sid, action):
        try:
            r = mgr.get(sid)
        except KeyError:
            return fail("no such strategy", 404)
        if action == "start":
            r.start()
        elif action == "stop":
            threading.Thread(target=r.stop, daemon=True).start()
        elif action == "restart":
            def _re():
                r.stop()
                r.start()
            threading.Thread(target=_re, daemon=True).start()
        elif action == "open-folder":
            os.startfile(r.dir) if os.name == "nt" else subprocess.Popen(["xdg-open", r.dir])
        elif action == "open-browser":
            if not r.url():
                return fail("start it first")
            import webbrowser
            webbrowser.open(r.url())
        elif action == "update":
            try:
                update_manifest(sid, request.get_json(force=True, silent=True) or {})
            except Exception as e:
                return fail(e)
        elif action == "remove":
            if r.state not in ("stopped", "crashed"):
                return fail("Stop it before removing it.")
            try:
                dest = archive_strategy(sid)
            except Exception as e:
                return fail("Could not move the folder (is a file in it open?): %s" % e)
            mgr.scan()
            return ok(archived_to=dest)
        else:
            return fail("unknown action", 404)
        return ok(strategy=r.info())

    @hub.route("/api/strategies/<sid>/log")
    def log(sid):
        try:
            r = mgr.get(sid)
        except KeyError:
            return fail("no such strategy", 404)
        return ok(lines=_tail(os.path.join(r.dir, "logs", "output.log")))

    @hub.route("/api/strategies/check", methods=["POST"])
    def check():
        body = request.get_json(force=True, silent=True) or {}
        errors, warnings, data_env = inspect_code(body.get("code") or "")
        return ok(errors=errors, warnings=warnings, data_env=data_env)

    @hub.route("/api/strategies/new", methods=["POST"])
    def new():
        try:
            sid, warnings = create_strategy(request.get_json(force=True, silent=True) or {})
        except Exception as e:
            return fail(e)
        mgr.scan()
        return ok(id=sid, warnings=warnings)

    return hub


# ═════════════════════════════════════════════════════════════════════════════
#  HUB MAIN
# ═════════════════════════════════════════════════════════════════════════════
_instance_lock = None


def _single_instance():
    global _instance_lock
    folder = os.path.join(os.environ.get("LOCALAPPDATA") or os.path.expanduser("~"), "NIFTYTrader")
    os.makedirs(folder, exist_ok=True)
    try:
        f = open(os.path.join(folder, "hub.lock"), "a+b")
        f.seek(0)
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        _instance_lock = f
        return True
    except OSError:
        return False


def _message(text):
    if os.name == "nt":
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, text, APP_NAME, 0x40)
    else:
        print(text)


def hub_main():
    if FROZEN or sys.stdout is None:
        os.makedirs(os.path.join(BASE_DIR, "hub", "logs"), exist_ok=True)
        f = open(os.path.join(BASE_DIR, "hub", "logs", "hub.log"), "a", encoding="utf-8", buffering=1)
        sys.stdout = sys.stderr = f
    print("\n==== hub start %s  base=%s ====" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), BASE_DIR))

    if not _single_instance():
        _message("%s is already open.\n\nLook for its window in the taskbar." % APP_NAME)
        return

    no_window = "--no-window" in sys.argv
    mgr = Manager()
    port_holder = {"port": int(_arg("--hub-port", "0") or 0) or _free_port()}
    hub = build_hub_app(mgr, port_holder)

    from werkzeug.serving import make_server
    srv = make_server("127.0.0.1", port_holder["port"], hub, threaded=True)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    url = "http://127.0.0.1:%d/" % port_holder["port"]
    print("hub at", url, flush=True)

    for r in mgr.scan():
        try:
            if r.manifest().get("autostart"):
                r.start()
        except Exception:
            traceback.print_exc()
    threading.Thread(target=_auto_check, daemon=True).start()
    threading.Thread(target=_vix_loop, daemon=True).start()

    if no_window:
        try:
            while True:
                time.sleep(3600)
        except KeyboardInterrupt:
            pass
        mgr.stop_all()
        return

    import webview
    webview.settings["ALLOW_DOWNLOADS"] = True
    icon = os.path.join(RES_DIR, "icon.ico")
    win = webview.create_window(APP_NAME, url, width=1480, height=940, min_size=(1000, 640),
                                background_color="#0b0e14", confirm_close=True)

    def on_closed():
        mgr.stop_all()
        os._exit(0)

    win.events.closed += on_closed
    webview.start(private_mode=False, icon=icon if os.path.exists(icon) else None,
                  localization={"global.quitConfirmation":
                                "Close NIFTY Trader?\n\nAll running strategies will be stopped "
                                "and open positions will no longer be managed."})
    mgr.stop_all()
    os._exit(0)


if __name__ == "__main__":
    if "--run-strategy" in sys.argv:
        run_strategy_child()
    else:
        hub_main()
