# NIFTY Trader - Cloud

The NIFTY Trader strategies, running on GitHub by themselves every weekday. No laptop and no other website.
Paper trading only, as in the desktop app.

**📊 Live report: [REPORT.md on the cloud-data branch](https://github.com/Shubham050396/Nifty-Trading-Cloud/blob/cloud-data/REPORT.md)** (refreshed every 5 minutes while it runs)

This is a separate copy. The desktop app and its repository (`Nifty-Trading-Software`) are not touched and keep
their own trade book. Both use the same Dhan token.

## Your daily routine

1. **Evening:** put a fresh Dhan token in, either way round:
   - **From the desktop app** (NIFTY Trader 1.7.0 and later): ⚙ → **Broker token** → paste → Save. It goes to this
     PC *and* up to the secret below, so this is the only place you paste it. Set it up once under
     ☁ **Cloud → Set up sending**.
   - **On GitHub:** this repository → **Settings → Secrets and variables → Actions** → `DHAN_ACCESS_TOKEN` →
     ✏️ **Update** → paste → **Update secret**. The phone browser works too.

   Either way nobody can read the secret back, not even in the logs.
2. **Next day:** nothing. It starts by itself at about 09:10 IST and stops at 15:15 IST.
3. **Any time:** see the results in the desktop app's ☁ **Cloud** screen, or open the
   [report](https://github.com/Shubham050396/Nifty-Trading-Cloud/blob/cloud-data/REPORT.md) in any browser
   or the GitHub app.

A Dhan token lasts 24 hours from when it is made, so a token made in the evening covers the whole next trading day.

## When it runs

| | |
|---|---|
| Starts | 09:10 IST, Monday to Friday. GitHub sometimes starts scheduled runs 5-15 minutes late. |
| Stops | 15:15 IST, or earlier if GitHub's 6-hour limit per run comes first (then about 15:05). |
| Holidays | It still starts; the strategies see the market is closed and do nothing. |
| Saves | Trades, state and the report go to the `cloud-data` branch every 5 minutes and at the end. The next day continues from there, so open positions carry over. |

Because the run ends before 15:30, the end-of-day rules are moved a little earlier in the cloud only:

- **Scalper:** no new trades 15 minutes before the stop; everything closed 4 minutes before it (desktop: 15:00 / 15:20).
- **Stock Options EMA Cross:** expiry-day exit 5 minutes before the stop (desktop: 15:20).
- **EMA Breakout Hedge:** expiry-day exit 5 minutes before the stop, if that is earlier than its own setting (15:15).

The strategy files themselves are identical to the desktop app's; `cloud/child.py` makes these changes as they start.

## Start or test it by hand

**Actions → Cloud trading → Run workflow → Run workflow.**

- During market hours it trades until 15:15 IST, e.g. after you updated an expired token.
- Outside market hours it runs a **5-minute check**: it confirms the token works, starts every strategy and writes the report.
- Type a number in *minutes* to stop it after that many minutes.

Each run's page (Actions tab) shows the same report at the end, and its **logs** can be downloaded there for 14 days.

## If something is wrong

| You see | Do this |
|---|---|
| Report says *❌ Not trading* and *the Dhan token expired* (the run is red in the Actions tab) | Update the `DHAN_ACCESS_TOKEN` secret, then **Run workflow**. |
| Report not updated today | Actions tab → is *Cloud trading* switched on? GitHub switches off schedules in public repositories after 60 days without activity. Each run asks GitHub to keep it on, but if you ever get an email saying it was disabled, press **Enable workflow** there. |
| A strategy shows 🔴 stopped | Open its *last log lines* in the report. It is restarted up to 3 times per day by itself. |

## Settings

Two ways to change them, both ending up in [`cloud/config.json`](cloud/config.json), which the next run uses.

**From the desktop app** (easier, and it checks as you type): set the strategy up on its own dashboard as usual,
then ☁ **Cloud → Send my settings** on that strategy's card. The card also says whether the cloud's settings
already match this PC's. Needs ☁ **Cloud → Set up sending** once.

**On GitHub:** edit `cloud/config.json` directly (✏️).

| Key | Meaning |
|---|---|
| `strategies` | Which strategies run in the cloud. Remove one to switch it off. |
| `stop_at` | End of the trading day in IST (default `15:15`). |
| `save_every_minutes` | How often trades and the report are saved (default 5). |
| `vix_limit` | **Kill above** this India VIX: no new trades, and every open trade is closed (default 13.5; 0 = off). |
| `vix_limit_applies_to` | e.g. `{"scalper": true}`. Empty = the option-selling strategies only (credit spreads, EMA hedge), as in the desktop app. |
| `vix_min` | **Trade only above** this India VIX: below it, no new trades, and open trades are left alone (default 13.5; 0 = off). |
| `vix_min_applies_to` | e.g. `{"level_cross": true}`. Empty = no strategy waits for VIX. A strategy listed here is taken out of `vix_limit_applies_to`: the two rules are opposites, so one strategy never gets both. |
| `settings` | Strategy settings, e.g. `{"scalper": {"max_trades": 4}}`. Sent to the strategy the way its own Save button sends them. Empty = each strategy's defaults. This is what **Send my settings** in the app writes. |

Until you send settings, the strategies run with their **default settings**, not the ones on your laptop.

## Where things are

```
.github/workflows/cloud.yml   the schedule
cloud/run.py                  starts the strategies, saves every 5 minutes, stops them
cloud/child.py                runs one strategy (like the desktop app does) with the cloud's end-of-day times
cloud/config.json             your cloud settings
hub/hub.py                    from the desktop app, used to run each strategy
strategies/                   copied from Nifty-Trading-Software (commit ab471db)

cloud-data branch
  REPORT.md                   the report
  status.json                 the same figures, read by the app's ☁ Cloud screen
  state/<strategy>/           each strategy's trade book and state
```

Not saved: the token, the strategies' token and login files, and their download caches. Every file is checked
for the token before it is saved, and the token and client id are blanked out of the logs.

## Updating a strategy

Strategy code is **not** synced automatically from the desktop repository. Copy the changed files from
`Nifty-Trading-Software/strategies/<name>/` into `strategies/<name>/` here (never the `data/` folder).

## Try it on a PC

```
pip install flask requests tzdata
set DHAN_ACCESS_TOKEN=...            (Windows)   export DHAN_ACCESS_TOKEN=...   (Mac/Linux)
python cloud/run.py --local --minutes 3
```

`--local` keeps everything in `.cloud-data/` and does not touch GitHub.
