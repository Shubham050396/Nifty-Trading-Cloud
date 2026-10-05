# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:19 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.22 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | +₹1,999 (+6.46%) | +₹21,548 (+7.07%) | 4 | 2 | ₹30,946 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹17,033 (+2.20%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,73,552 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹8,590 (-5.56%) | +₹404 (+0.28%) | −₹8,679 (-1.71%) | 9 | 7 | ₹1,41,819 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹5,908 (-9.75%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹25,821** | **+₹13,528** | **+₹84,284** | **20** | **23** | **₹10,06,936** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:03:33] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:04:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:06:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:06:34] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:15:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:15:36] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:12:28] API       rate limited by Dhan - now one call every 15.1 s
[12:14:10] API       rate limited by Dhan - now one call every 15.1 s
[12:15:32] API       rate limited by Dhan - now one call every 15.1 s
[12:15:52] API       rate limited by Dhan - now one call every 15.1 s
[12:17:32] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:18:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:17:30] GAP       2026-10-06 23600 CE: no prices for 9 min - bar history restarts
[12:17:30] GAP       2026-10-06 23500 CE: no prices for 9 min - bar history restarts
[12:17:30] GAP       2026-10-06 23600 PE: no prices for 9 min - bar history restarts
[12:17:30] GAP       2026-10-06 23500 PE: no prices for 9 min - bar history restarts
[12:18:08] API       rate limited by Dhan - now one call every 15.1 s
[12:19:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:09:28] API       rate limited by Dhan - now one call every 15.1 s
[12:10:27] API       rate limited by Dhan - now one call every 15.1 s
[12:11:52] API       rate limited by Dhan - now one call every 15.1 s
[12:13:52] API       rate limited by Dhan - now one call every 15.1 s
[12:16:24] API       rate limited by Dhan - now one call every 15.1 s
[12:17:22] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:05:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:08:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:09:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:12:52] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:15:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:17:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:13:03] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:14:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:15:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:15:32] SKIP      COALINDIA 415 PE 27 Oct signal at 5.15 skipped - already 1 open on COALINDIA
[12:16:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:18:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:16:20] API       rate limited by Dhan - now one call every 15.1 s
[12:16:36] API       rate limited by Dhan - now one call every 15.1 s
[12:17:20] API       rate limited by Dhan - now one call every 15.1 s
[12:17:36] API       rate limited by Dhan - now one call every 15.1 s
[12:17:51] API       rate limited by Dhan - now one call every 15.1 s
[12:18:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

