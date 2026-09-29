"""
NIFTY Cloud runner
==================

Runs the strategies on GitHub's computers: no window, no laptop.  Started by
.github/workflows/cloud.yml every weekday morning.

  1. checks the Dhan token (the DHAN_ACCESS_TOKEN secret),
  2. restores the trades and state saved by the last run (cloud-data branch),
  3. starts every strategy listed in cloud/config.json, each in its own process,
  4. every few minutes saves their state and REPORT.md to the cloud-data branch,
  5. stops them cleanly at 15:15 IST, or earlier if GitHub's 6-hour limit comes first.

    python cloud/run.py                    what the workflow runs
    python cloud/run.py --local            try it on a PC: no git, state kept in .cloud-data/
    python cloud/run.py --local --minutes 3

Nothing secret is ever saved: the token lives only in the GitHub secret and in
the environment of this run.  Every file is checked for it before it is saved.
"""

import json
import os
import re
import secrets
import shutil
import signal
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

CLOUD_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CLOUD_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "hub"))
import hub  # noqa: E402

STRATEGIES_DIR = os.path.join(BASE_DIR, "strategies")
CONFIG_FILE = os.path.join(CLOUD_DIR, "config.json")
CHILD = os.path.join(CLOUD_DIR, "child.py")
WORK = os.path.join(BASE_DIR, ".cloud-data")          # the cloud-data branch, checked out here
RISK_FILE = os.path.join(BASE_DIR, "hub", "risk.json")
DATA_BRANCH = "cloud-data"

IST = timezone(timedelta(hours=5, minutes=30))
JOB_BUDGET_MIN = 354          # GitHub stops a job at 360 minutes; keep a few for the final save
CHECK_RUN_MIN = 5             # a run started outside market hours only checks that everything starts
MAX_RESTARTS = 3
SETTINGS_PATH = {"credit_spreads": "/api/filters"}     # every other strategy saves settings at /api/config
STATUS_PATH = {"credit_spreads": "/api/status"}        # every other strategy reports at /api/state
SETTINGS_KEY = {"credit_spreads": "filters"}           # the key its settings live under
PAUSE_TO_SAVE = {"credit_spreads": ("/api/scanner/stop", "/api/scanner/start")}

# Never saved: login and session secrets, the token form's file, caches, locks.
SKIP_FILE = re.compile(r"^(secret_key|auth\.json|runtime\.json.*|scrip_.*\.json|.*\.lock|.*\.pid|.*\.tmp)$")
MAX_FILE_BYTES = 40 * 1024 * 1024
JWT_RE = re.compile(r"eyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]+")

LOCAL = "--local" in sys.argv
STOP = threading.Event()


def ist_now():
    return datetime.now(IST)


def log(msg):
    print("%s  %s" % (ist_now().strftime("%H:%M:%S"), msg), flush=True)


def _arg(name, default=None):
    return hub._arg(name, default)


def load_config():
    with open(CONFIG_FILE, encoding="utf-8") as f:
        cfg = json.load(f)
    cfg.setdefault("strategies", [])
    cfg.setdefault("stop_at", "15:15")
    cfg.setdefault("save_every_minutes", 5)
    cfg.setdefault("vix_limit", hub.DEFAULT_VIX_LIMIT)
    cfg.setdefault("vix_limit_applies_to", {})
    cfg.setdefault("settings", {})
    return cfg


# ═════════════════════════════════════════════════════════════════════════════
#  SECRETS  -  masked in GitHub's log, and never written into a saved file
# ═════════════════════════════════════════════════════════════════════════════
SECRETS = []


def add_secret(value):
    if value and value not in SECRETS:
        SECRETS.append(value)
        if os.environ.get("GITHUB_ACTIONS") == "true":
            print("::add-mask::%s" % value, flush=True)


def redact(text):
    for s in SECRETS:
        text = text.replace(s, "***")
    return JWT_RE.sub("***", text)


def holds_secret(data):
    return any(s.encode() in data for s in SECRETS) or JWT_RE.search(data.decode("latin-1")) is not None


# ═════════════════════════════════════════════════════════════════════════════
#  DHAN TOKEN AND INDIA VIX
# ═════════════════════════════════════════════════════════════════════════════
def read_token():
    tok = (os.environ.get("DHAN_ACCESS_TOKEN") or "").strip()
    cid = (os.environ.get("DHAN_CLIENT_ID") or "").strip() or (hub._jwt_client_id(tok) if tok else "")
    add_secret(tok)
    add_secret(cid)
    exp = hub._jwt_expiry(tok) if tok else None
    return tok, cid, exp


def fetch_vix(tok, cid):
    """(value, problem, http code).  The same call the desktop app makes."""
    req = urllib.request.Request(
        "https://api.dhan.co/v2/marketfeed/ltp", data=json.dumps({"IDX_I": [21]}).encode(),
        headers={"access-token": tok, "client-id": cid, "Content-Type": "application/json",
                 "Accept": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode("utf-8"))
        node = ((d.get("data") or {}).get("IDX_I") or {}).get("21") or {}
        v = float(node.get("last_price") or 0)
        return (round(v, 2), "", 200) if v > 0 else (None, "no VIX in Dhan's answer", 200)
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode("utf-8", "replace")[:300]
        except Exception:
            body = ""
        return None, redact("Dhan answered HTTP %d %s" % (e.code, body)).strip(), e.code
    except Exception as e:
        return None, "could not reach Dhan (%s)" % e.__class__.__name__, 0


# ═════════════════════════════════════════════════════════════════════════════
#  THE cloud-data BRANCH  -  trades, state and REPORT.md
# ═════════════════════════════════════════════════════════════════════════════
class GitError(RuntimeError):
    pass


def git(*args, cwd=BASE_DIR, check=True):
    r = subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True, text=True)
    if check and r.returncode:
        raise GitError(redact("git %s: %s" % (args[0], (r.stderr or r.stdout).strip()[-400:])))
    return r


def _retry(fn, what, tries=4):
    for i in range(tries):
        try:
            return fn()
        except GitError as e:
            if i == tries - 1:
                raise
            log("%s failed (%s) - retrying" % (what, e))
            time.sleep(2 ** (i + 1))


def open_data_branch():
    """Check the cloud-data branch out into .cloud-data/.  If GitHub cannot be
    asked whether it exists, stop: starting from an empty book and saving it
    over the real one would lose every trade."""
    if LOCAL:
        os.makedirs(WORK, exist_ok=True)
        return "local folder"
    if os.path.isdir(WORK):
        git("worktree", "remove", "--force", WORK, check=False)
        shutil.rmtree(WORK, ignore_errors=True)
    git("config", "user.name", "NIFTY Cloud")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    heads = _retry(lambda: git("ls-remote", "--heads", "origin", DATA_BRANCH), "reading the saved state")
    if heads.stdout.strip():
        _retry(lambda: git("fetch", "-q", "--depth=1", "origin",
                           "+refs/heads/%s:refs/remotes/origin/%s" % (DATA_BRANCH, DATA_BRANCH)),
               "downloading the saved state")
        git("worktree", "add", "-q", "-B", DATA_BRANCH, WORK, "origin/" + DATA_BRANCH)
        return "restored from the %s branch" % DATA_BRANCH
    git("worktree", "add", "-q", "--detach", WORK)
    git("checkout", "-q", "--orphan", DATA_BRANCH, cwd=WORK)
    git("rm", "-rfq", "--ignore-unmatch", ".", cwd=WORK)
    return "first run: starting with empty trade books"


def publish(message):
    if LOCAL:
        return True
    try:
        git("add", "-A", cwd=WORK)
        if git("diff", "--cached", "--quiet", cwd=WORK, check=False).returncode == 0:
            return True
        git("commit", "-q", "-m", message, cwd=WORK)
        _retry(lambda: git("push", "-q", "origin", "HEAD:refs/heads/" + DATA_BRANCH, cwd=WORK),
               "saving to GitHub")
        return True
    except GitError as e:
        log("WARNING: could not save to GitHub: %s" % e)
        return False


def _files(root):
    for d, _dirs, names in os.walk(root):
        for n in names:
            yield os.path.relpath(os.path.join(d, n), root), n


def restore_state(sids):
    for sid in sids:
        src = os.path.join(WORK, "state", sid)
        dst = os.path.join(STRATEGIES_DIR, sid, "data")
        os.makedirs(dst, exist_ok=True)
        if not os.path.isdir(src):
            continue
        n = 0
        for rel, name in _files(src):
            if SKIP_FILE.match(name):
                continue
            os.makedirs(os.path.dirname(os.path.join(dst, rel)), exist_ok=True)
            shutil.copy2(os.path.join(src, rel), os.path.join(dst, rel))
            n += 1
        log("%s: restored %d saved file%s" % (sid, n, "" if n == 1 else "s"))


def save_state(sids, warnings):
    """Mirror each strategy's data/ folder into cloud-data/state/<id>/, minus
    the files in SKIP_FILE and anything that contains the token."""
    for sid in sids:
        src = os.path.join(STRATEGIES_DIR, sid, "data")
        dst = os.path.join(WORK, "state", sid)
        if not os.path.isdir(src):
            continue
        keep = set()
        for rel, name in _files(src):
            if SKIP_FILE.match(name):
                continue
            path = os.path.join(src, rel)
            try:
                if os.path.getsize(path) > MAX_FILE_BYTES:
                    warnings.add("%s/%s is over 40 MB and was not saved" % (sid, rel))
                    continue
                with open(path, "rb") as f:
                    data = f.read()
            except OSError:
                continue
            if holds_secret(data):
                warnings.add("%s/%s was not saved because it contains a token" % (sid, rel))
                continue
            keep.add(rel)
            out = os.path.join(dst, rel)
            try:
                with open(out, "rb") as f:
                    if f.read() == data:
                        continue
            except OSError:
                pass
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, "wb") as f:
                f.write(data)
        if os.path.isdir(dst):
            for rel, _name in list(_files(dst)):
                if rel not in keep:
                    os.remove(os.path.join(dst, rel))


# ═════════════════════════════════════════════════════════════════════════════
#  ONE STRATEGY PROCESS
# ═════════════════════════════════════════════════════════════════════════════
class Strategy:
    def __init__(self, sid):
        self.id = sid
        self.dir = os.path.join(STRATEGIES_DIR, sid)
        self.man = hub._read_manifest(self.dir)
        self.name = self.man["name"]
        self.proc = self.port = self.token = None
        self.state, self.error = "stopped", ""
        self.summary = None
        self.started = self.crashed_at = 0.0
        self.restarts = 0
        self.settings_done = False
        self.ever_ran = False
        self.settings = None          # what this strategy is actually using now
        self.settings_error = ""      # cloud/config.json refused; the strategy itself is fine

    def start(self, env_base, stop_hhmm):
        self.port = hub._free_port()
        self.token = secrets.token_urlsafe(24)
        env = dict(env_base)
        if self.man.get("data_env"):
            env[self.man["data_env"]] = os.path.join(self.dir, "data")
        env[hub.TOKEN_ENV] = self.token
        cmd = [sys.executable, CHILD, "--run-strategy", self.dir, "--port", str(self.port),
               "--parent-pid", str(os.getpid()), "--stop-at", stop_hhmm]
        self.proc = subprocess.Popen(cmd, cwd=self.dir, env=env, stdin=subprocess.DEVNULL,
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.state, self.error, self.started = "starting", "", time.time()

    def call(self, path, method="GET", body=None, timeout=5.0):
        data = json.dumps(body).encode() if body is not None else (b"" if method == "POST" else None)
        req = urllib.request.Request("http://127.0.0.1:%d%s" % (self.port, path), data=data, method=method,
                                     headers={"X-Hub-Token": self.token, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())

    def log_tail(self, n=6):
        lines = [ln for ln in hub._tail(os.path.join(self.dir, "logs", "output.log"), 400)
                 if ln.strip() and "/__hub__/" not in ln]
        return [redact(ln)[:300] for ln in lines[-n:]]

    def poll(self):
        if not self.proc:
            return
        code = self.proc.poll()
        if code is not None:
            last = next((ln for ln in reversed(self.log_tail(40)) if "Error" in ln or "Exception" in ln), "")
            self.state, self.proc, self.crashed_at = "crashed", None, time.time()
            self.error = ("exited with code %s. %s" % (code, last.strip())).strip()
            log("%s: STOPPED - %s" % (self.id, self.error))
            return
        try:
            st = self.call("/__hub__/status", timeout=3)
            if self.state == "starting":
                log("%s: running" % self.id)
            self.state, self.summary, self.ever_ran = "running", st.get("summary"), True
        except Exception:
            if self.state == "starting" and time.time() - self.started > 180:
                self.error = "has not answered for 3 minutes - see its log"

    def read_settings(self):
        """The settings this strategy is running with, straight from the
        strategy itself.  Saved into status.json so the desktop app can show
        them and say whether they match the PC's."""
        try:
            st = self.call(STATUS_PATH.get(self.id, "/api/state"), timeout=10)
            got = st.get(SETTINGS_KEY.get(self.id, "cfg"))
            if isinstance(got, dict):
                self.settings = got
        except Exception:
            pass
        return self.settings

    def apply_settings(self, settings):
        """Settings from cloud/config.json, sent the way the strategy's own
        Save button sends them, so the strategy checks them itself."""
        if self.settings_done or self.state != "running":
            return
        self.settings_done = True
        body = settings.get(self.id)
        current = self.read_settings()
        if not body:
            return
        if isinstance(current, dict) and all(current.get(k) == v for k, v in body.items()):
            log("%s: settings already as cloud/config.json asks" % self.id)
            return
        # Credit spreads refuses a filter change while its scanner is running,
        # so pause it around the change; it is started again right after.
        pause = PAUSE_TO_SAVE.get(self.id)
        try:
            if pause:
                self.call(pause[0], "POST", {}, timeout=10)
            self.call(SETTINGS_PATH.get(self.id, "/api/config"), "POST", body, timeout=20)
            log("%s: settings from cloud/config.json applied" % self.id)
        except urllib.error.HTTPError as e:
            msg = redact(e.read().decode("utf-8", "replace"))[:300]
            self.settings_error = "cloud/config.json was refused: %s" % msg
            log("%s: %s" % (self.id, self.settings_error))
        except Exception as e:
            log("%s: could not apply settings (%s)" % (self.id, e.__class__.__name__))
        finally:
            if pause:
                try:
                    self.call(pause[1], "POST", {}, timeout=10)
                except Exception as e:
                    log("%s: could not restart the scanner after saving settings (%s)"
                        % (self.id, e.__class__.__name__))
            self.read_settings()

    def stop(self):
        proc = self.proc
        if not proc:
            return
        try:
            self.call("/__hub__/shutdown", "POST", timeout=5)
        except Exception:
            pass
        try:
            proc.wait(timeout=20)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=5)
        self.proc, self.state = None, "stopped"


# ═════════════════════════════════════════════════════════════════════════════
#  REPORT.md and status.json
# ═════════════════════════════════════════════════════════════════════════════
def _indian(n):
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    return re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", head) + "," + tail


def inr(v, signed=False):
    if v is None:
        return "-"
    v = round(float(v))
    sign = ("+" if v > 0 else "−" if v < 0 else "") if signed else ("−" if v < 0 else "")
    return "%s₹%s" % (sign, _indian(abs(v)))


def pct(v):
    return "" if v is None else " (%+.2f%%)" % v


STATE_LABEL = {"running": "🟢 running", "starting": "⏳ starting", "crashed": "🔴 stopped",
               "stopped": "⏹ stopped", "saved": "✅ saved"}


def render(ctx):
    now = ist_now()
    L = ["# NIFTY Cloud report", ""]
    L.append("**%s** · updated %s IST · %s" % (
        ctx["headline"], now.strftime("%d %b %Y %H:%M"),
        "[this run](%s)" % ctx["run_url"] if ctx["run_url"] else "local run"))
    L.append("")
    vix = ctx.get("vix")
    limit = ctx.get("vix_limit") or 0
    vix_txt = "-" if vix is None else ("%.2f" % vix)
    if vix is not None and limit and vix > limit:
        vix_txt += " 🔴 above the limit"
    L.append("India VIX **%s** (limit %s) · Dhan token: %s · trading window: %s" % (
        vix_txt, ("%.2f" % limit) if limit else "off", ctx["token_text"], ctx["window"]))
    L.append("")
    for w in ctx["notices"]:
        L.append("> ⚠️ %s" % w)
        L.append("")

    rows, tot = [], {"pnl_today": 0.0, "pnl_open": 0.0, "pnl_all": 0.0, "trades_today": 0, "open": 0,
                     "margin_used": 0.0}
    for s in ctx["strategies"]:
        m = s.summary if isinstance(s.summary, dict) else {}
        for k in tot:
            try:
                tot[k] += float(m.get(k) or 0)
            except (TypeError, ValueError):
                pass
        state = STATE_LABEL.get(s.state, s.state)
        if s.error:
            state += " - " + s.error.replace("|", "/")[:160]
        if s.settings_error:
            state += " ⚠️ " + s.settings_error.replace("|", "/")[:160]
        rows.append("| %s %s | %s | %s%s | %s%s | %s%s | %s | %s | %s |" % (
            s.man.get("icon", ""), s.name, state,
            inr(m.get("pnl_today"), True), pct(m.get("pct_today")),
            inr(m.get("pnl_open"), True), pct(m.get("pct_open")),
            inr(m.get("pnl_all"), True), pct(m.get("pct_all")),
            m.get("trades_today", "-"), m.get("open", "-"), inr(m.get("margin_used"))))
    L.append("| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |")
    L.append("|---|---|--:|--:|--:|--:|--:|--:|")
    L.extend(rows)
    L.append("| **Total** | | **%s** | **%s** | **%s** | **%d** | **%d** | **%s** |" % (
        inr(tot["pnl_today"], True), inr(tot["pnl_open"], True), inr(tot["pnl_all"], True),
        tot["trades_today"], tot["open"], inr(tot["margin_used"])))
    L.append("")
    L.append("Paper trading only. Margin figures are estimates, as in the desktop app. "
             "Trades and state for each strategy are in the [state](state) folder.")
    L.append("")
    for s in ctx["strategies"]:
        tail = s.log_tail()
        if tail:
            L.append("<details><summary>%s - last log lines</summary>\n\n```text\n%s\n```\n</details>\n"
                     % (s.name, "\n".join(ln.replace("```", "'''") for ln in tail)))
    return "\n".join(L) + "\n"


def status_json(ctx):
    return {
        "updated": ist_now().isoformat(timespec="seconds"), "headline": ctx["headline"],
        "phase": ctx["phase"], "window": ctx["window"], "vix": ctx.get("vix"),
        "vix_limit": ctx.get("vix_limit"), "run_url": ctx["run_url"], "notices": ctx["notices"],
        "token_text": ctx["token_text"], "token_expires": ctx.get("token_expires"),
        "stop_at": ctx.get("stop_at"),
        "strategies": {s.id: {"name": s.name, "icon": s.man.get("icon", ""),
                              "color": s.man.get("color", ""), "description": s.man.get("description", ""),
                              "state": s.state, "error": s.error, "summary": s.summary,
                              "settings": s.settings, "settings_error": s.settings_error}
                       for s in ctx["strategies"]},
    }


def write_report(ctx):
    os.makedirs(WORK, exist_ok=True)
    with open(os.path.join(WORK, "REPORT.md"), "w", encoding="utf-8") as f:
        f.write(render(ctx))
    with open(os.path.join(WORK, "status.json"), "w", encoding="utf-8") as f:
        json.dump(status_json(ctx), f, indent=2)


def step_summary(ctx):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as f:
            f.write(render(ctx))


def redact_logs(sids):
    """The logs are uploaded with the run; make sure no token is in them."""
    for sid in sids:
        d = os.path.join(STRATEGIES_DIR, sid, "logs")
        if not os.path.isdir(d):
            continue
        for rel, _n in _files(d):
            p = os.path.join(d, rel)
            try:
                with open(p, encoding="utf-8", errors="replace") as f:
                    text = f.read()
                clean = redact(text)
                if clean != text:
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(clean)
            except OSError:
                pass


# ═════════════════════════════════════════════════════════════════════════════
#  WHEN TO STOP
# ═════════════════════════════════════════════════════════════════════════════
def plan_stop(cfg):
    """(stop time, what kind of run).  A normal day ends at stop_at (15:15 IST)
    or before GitHub's 6-hour limit, whichever is first.  Started at a weekend
    or after stop_at, the run only checks that everything starts."""
    now = ist_now()
    started = float(os.environ.get("CLOUD_JOB_STARTED") or time.time())
    hard = datetime.fromtimestamp(started + JOB_BUDGET_MIN * 60, IST)
    h, m = (int(x) for x in str(cfg["stop_at"]).split(":"))
    day_stop = now.replace(hour=h, minute=m, second=0, microsecond=0)
    minutes = _arg("--minutes") or os.environ.get("CLOUD_MINUTES") or ""
    try:
        minutes = int(float(minutes))
    except ValueError:
        minutes = 0
    if minutes > 0:
        return min(now + timedelta(minutes=minutes), hard), "manual run (%d min)" % minutes
    if now.weekday() >= 5 or now >= day_stop - timedelta(minutes=CHECK_RUN_MIN):
        return min(now + timedelta(minutes=CHECK_RUN_MIN), hard), "check run (outside trading hours)"
    return min(day_stop, hard), "trading day"


def token_text(exp, stop):
    if not exp:
        return "expiry unknown"
    left = exp - time.time()
    if left <= 0:
        return "**EXPIRED**"
    when = datetime.fromtimestamp(exp, IST)
    txt = "valid until %s IST" % when.strftime("%d %b %H:%M")
    return txt + (" ⚠️ before this run ends" if when < stop else "")


# ═════════════════════════════════════════════════════════════════════════════
def main():
    cfg = load_config()
    run_url = ""
    if os.environ.get("GITHUB_RUN_ID"):
        run_url = "%s/%s/actions/runs/%s" % (os.environ.get("GITHUB_SERVER_URL", "https://github.com"),
                                             os.environ.get("GITHUB_REPOSITORY", ""), os.environ["GITHUB_RUN_ID"])
    stop, kind = plan_stop(cfg)
    stop_ts = stop.timestamp()
    window = "%s → %s IST (%s)" % (ist_now().strftime("%H:%M"), stop.strftime("%H:%M"), kind)
    log("NIFTY Cloud - %s" % window)

    sids = []
    for sid in cfg["strategies"]:
        if os.path.isfile(os.path.join(STRATEGIES_DIR, sid, "strategy.json")):
            sids.append(sid)
        else:
            log("WARNING: cloud/config.json lists '%s' but strategies/%s/strategy.json does not exist" % (sid, sid))
    strategies = [Strategy(sid) for sid in sids]
    ctx = {"headline": "Starting", "phase": "starting", "run_url": run_url, "window": window,
           "notices": [], "strategies": strategies, "vix": None, "vix_limit": cfg["vix_limit"],
           "token_text": "-", "token_expires": None, "stop_at": stop.isoformat(timespec="seconds")}
    warnings = set()

    def finish_failed(msg):
        ctx.update(headline="❌ Not trading", phase="failed")
        ctx["notices"].append(msg[0].upper() + msg[1:])
        log("FAILED: " + msg)
        write_report(ctx)
        publish("Cloud run failed %s IST" % ist_now().strftime("%d %b %H:%M"))
        step_summary(ctx)
        return 1

    how = open_data_branch()
    log("saved state: %s" % how)

    # ── the token ────────────────────────────────────────────────────────────
    tok, cid, exp = read_token()
    ctx["token_text"], ctx["token_expires"] = token_text(exp, stop), exp
    if not tok:
        return finish_failed("no Dhan token. On GitHub open Settings → Secrets and variables → Actions and "
                             "add DHAN_ACCESS_TOKEN.")
    if exp and exp <= time.time():
        return finish_failed("the Dhan token expired at %s IST. Paste a fresh one into the DHAN_ACCESS_TOKEN "
                             "secret, then start this workflow again from the Actions tab."
                             % datetime.fromtimestamp(exp, IST).strftime("%d %b %H:%M"))
    if "--no-token-check" not in sys.argv or not LOCAL:
        vix, problem, code = fetch_vix(tok, cid)
        if code in (401, 403):
            return finish_failed("Dhan refused the token (%s). Paste a fresh one into the DHAN_ACCESS_TOKEN "
                                 "secret, then start this workflow again from the Actions tab." % problem)
        ctx["vix"] = vix
        if problem:
            log("India VIX: %s" % problem)
    if exp and exp < stop_ts:
        ctx["notices"].append("The Dhan token expires at %s IST, before this run ends. The strategies stop "
                              "trading then." % datetime.fromtimestamp(exp, IST).strftime("%H:%M"))

    if not strategies:
        return finish_failed("cloud/config.json lists no strategy that exists.")

    # ── start ────────────────────────────────────────────────────────────────
    restore_state(sids)
    hub._write_json_atomic(RISK_FILE, {"vix_limit": cfg["vix_limit"], "apply": cfg["vix_limit_applies_to"]})
    env = {k: v for k, v in os.environ.items() if k not in ("HOST", "APP_ENV", "PORT", "APP_PASSWORD")}
    env.update(NIFTY_RISK_FILE=RISK_FILE, PYTHONIOENCODING="utf-8", DHAN_ACCESS_TOKEN=tok)
    if cid:
        env["DHAN_CLIENT_ID"] = cid
    stop_hhmm = stop.strftime("%H:%M")
    for s in strategies:
        s.start(env, stop_hhmm)
        log("%s: starting" % s.id)

    for sig in ("SIGTERM", "SIGINT"):
        signal.signal(getattr(signal, sig), lambda *_a: STOP.set())

    ctx.update(headline="Running until %s IST" % stop_hhmm, phase="running")
    save_every = max(1.0, float(cfg["save_every_minutes"])) * 60
    last_save = last_vix = time.time()
    first_save_done = False
    while not STOP.is_set() and time.time() < stop_ts:
        STOP.wait(10)
        now = time.time()
        for s in strategies:
            s.poll()
            s.apply_settings(cfg["settings"])
            if s.state == "crashed" and s.restarts < MAX_RESTARTS and now - s.crashed_at > 30 and now < stop_ts - 120:
                s.restarts += 1
                log("%s: restarting (%d of %d)" % (s.id, s.restarts, MAX_RESTARTS))
                s.start(env, stop_hhmm)
        # First save once everything answered (or after 3 minutes), then every few minutes.
        booted = all(s.state != "starting" for s in strategies) or now - last_save > 180
        if (not first_save_done and booted) or now - last_save >= save_every:
            if now - last_vix >= 240 or ctx["vix"] is None:
                v, _p, _c = fetch_vix(tok, cid)
                ctx["vix"], last_vix = (v if v is not None else ctx["vix"]), now
            save_state(sids, warnings)
            ctx["notices"] = [n for n in ctx["notices"] if n not in warnings] + sorted(warnings)
            write_report(ctx)
            publish("Cloud state %s IST" % ist_now().strftime("%d %b %H:%M"))
            last_save, first_save_done = now, True

    # ── stop ─────────────────────────────────────────────────────────────────
    log("stopping every strategy and saving")
    for s in strategies:
        s.poll()
    threads = [threading.Thread(target=s.stop) for s in strategies]
    for t in threads:
        t.start()
    for t in threads:
        t.join(40)
    for s in strategies:
        if s.state == "stopped" and not s.error:
            s.state = "saved"
    save_state(sids, warnings)
    redact_logs(sids)
    ran = any(s.ever_ran for s in strategies)
    ctx.update(headline="Finished for the day at %s IST" % ist_now().strftime("%H:%M") if ran
               else "Finished - no strategy answered", phase="finished")
    ctx["notices"] = [n for n in ctx["notices"] if n not in warnings] + sorted(warnings)
    write_report(ctx)
    ok = publish("Cloud close %s IST" % ist_now().strftime("%d %b %H:%M"))
    step_summary(ctx)
    log("done%s" % ("" if ok else " - WARNING: the last save did not reach GitHub"))
    return 0 if ran else 1


if __name__ == "__main__":
    sys.exit(main())
