"""
Runs ONE strategy for the cloud runner (cloud/run.py).

The same as `hub.py --run-strategy`, which the desktop app uses, with one
addition: the cloud run stops before 15:30 (GitHub ends a job after 6 hours),
so anything a strategy does "at the end of the day" is moved to just before
the run stops.  The strategy files themselves are not changed.

    python cloud/child.py --run-strategy DIR --port N --parent-pid P --stop-at HH:MM
"""

import importlib.util
import logging
import os
import re
import sys
import threading
import traceback
from datetime import datetime, time as dtime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "hub"))
import hub  # noqa: E402

# Strategy id -> {module constant: minutes before the cloud run stops}.
# A constant is only ever moved earlier, never later.
EOD_CONSTANTS = {
    "scalper": {"NO_NEW_ENTRY_AFTER": 15, "HARD_FLAT": 4, "HALT_ALL": 2},
    "stock_ema_cross": {"EXPIRY_DAY_EXIT": 5},
}
# ema_hedge keeps its expiry-day exit time in its settings; it is closed this
# many minutes before the stop instead, if that is earlier.
EMA_HEDGE_EXPIRY_MINUTES = 5


def _minus(hhmm, minutes):
    t = datetime.combine(datetime(2000, 1, 1), dtime(*map(int, hhmm.split(":"))))
    return (t - timedelta(minutes=minutes)).time()


def apply_cloud_times(sid, mod, stop_at):
    for name, before in EOD_CONSTANTS.get(sid, {}).items():
        cur = getattr(mod, name, None)
        if isinstance(cur, dtime):
            new = min(cur, _minus(stop_at, before))
            if new != cur:
                setattr(mod, name, new)
                print("cloud: %s %s -> %s" % (name, cur.strftime("%H:%M"), new.strftime("%H:%M")), flush=True)

    orig = getattr(mod, "expiry_due", None)
    if sid == "ema_hedge" and callable(orig):
        cut = _minus(stop_at, EMA_HEDGE_EXPIRY_MINUTES).strftime("%H:%M")

        def expiry_due(expiry, now):
            why = orig(expiry, now)
            if why is None and expiry == now.strftime("%Y-%m-%d") and now.strftime("%H:%M") >= cut:
                return "EXPIRY_DAY"
            return why
        mod.expiry_due = expiry_due
        try:
            if cut < str(mod.STATE.cfg.get("expiry_exit") or ""):
                print("cloud: expiry-day exit %s -> %s" % (mod.STATE.cfg["expiry_exit"], cut), flush=True)
        except Exception:
            pass


def main():
    sdir = os.path.abspath(hub._arg("--run-strategy"))
    port = int(hub._arg("--port"))
    ppid = int(hub._arg("--parent-pid", "0") or 0)
    stop_at = hub._arg("--stop-at", "15:15")
    token = os.environ.pop(hub.TOKEN_ENV, "")
    sid = os.path.basename(sdir)

    logs = os.path.join(sdir, "logs")
    os.makedirs(logs, exist_ok=True)
    log_path = os.path.join(logs, "output.log")
    out = open(log_path, "a", encoding="utf-8", buffering=1, errors="replace")
    sys.stdout = sys.stderr = out
    print("\n==== %s IST  cloud start (pid %d, port %d, stop %s IST) ====" % (
        hub._ist_now().strftime("%Y-%m-%d %H:%M:%S"), os.getpid(), port, stop_at), flush=True)
    # The runner asks every few seconds whether the strategy is alive; keep
    # those requests out of the log.
    logging.getLogger("werkzeug").addFilter(lambda r: "/__hub__/" not in r.getMessage())

    try:
        man = hub._read_manifest(sdir)
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
        try:
            app.config["SESSION_COOKIE_NAME"] = "session_" + re.sub(r"\W", "_", sid)
        except Exception:
            pass
        apply_cloud_times(sid, mod, stop_at)
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
        print("cloud: shutdown requested - saving state", flush=True)
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

    srv = make_server("127.0.0.1", port, hub._HubMiddleware(app, token, mod, shutdown), threaded=True)
    holder["srv"] = srv
    if ppid:
        threading.Thread(target=hub._watch_parent, args=(ppid, shutdown), daemon=True).start()
    print("serving %s on http://127.0.0.1:%d" % (man["name"], port), flush=True)
    srv.serve_forever()
    t = threading.Timer(6.0, os._exit, (0,))
    t.daemon = True
    t.start()
    sys.exit(0)


if __name__ == "__main__":
    main()
