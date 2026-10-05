# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:14 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.28 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | +₹3,920 (+12.67%) | +₹21,548 (+7.07%) | 4 | 2 | ₹30,946 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹25,191 (+3.26%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,73,106 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹8,590 (-5.56%) | +₹2,171 (+1.53%) | −₹8,679 (-1.71%) | 9 | 7 | ₹1,41,819 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹7,410 (-12.22%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹25,821** | **+₹23,872** | **+₹84,284** | **20** | **23** | **₹10,06,490** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:53:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:03:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:03:33] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:04:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:06:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:06:34] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:04:39] API       rate limited by Dhan - now one call every 15.1 s
[12:06:01] API       rate limited by Dhan - now one call every 15.1 s
[12:11:27] API       rate limited by Dhan - now one call every 12.1 s
[12:11:31] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:12:08] API       rate limited by Dhan - now one call every 15.1 s
[12:12:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:10:39] API       rate limited by Dhan - now one call every 15.1 s
[12:11:37] API       rate limited by Dhan - now one call every 15.1 s
[12:12:36] API       rate limited by Dhan - now one call every 15.1 s
[12:12:51] API       rate limited by Dhan - now one call every 15.1 s
[12:13:36] API       rate limited by Dhan - now one call every 15.1 s
[12:13:51] SIGNAL    2026-10-13 22600 PE held above 253.75 for 5 min - fall-back exit is armed
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:08:58] API       rate limited by Dhan - now one call every 15.1 s
[12:09:13] API       rate limited by Dhan - now one call every 15.1 s
[12:09:28] API       rate limited by Dhan - now one call every 15.1 s
[12:10:27] API       rate limited by Dhan - now one call every 15.1 s
[12:11:52] API       rate limited by Dhan - now one call every 15.1 s
[12:13:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:02:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:04:00] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:05:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:08:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:09:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:12:52] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:10:15] ENTRY     BUY INDIGO 4900 PE 27 Oct x150 @ 129.30 (signal close 129.50, EMA 144 122.03, momentum 6.5%)  quick 148.69 till 12:40, target 219.81, stop below EMA 55
[12:10:27] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:10:45] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:11:03] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:12:03] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:13:03] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:09:48] API       rate limited by Dhan - now one call every 15.1 s
[12:10:33] API       rate limited by Dhan - now one call every 15.1 s
[12:11:17] API       rate limited by Dhan - now one call every 15.1 s
[12:12:02] API       rate limited by Dhan - now one call every 15.1 s
[12:13:51] API       rate limited by Dhan - now one call every 15.1 s
[12:14:06] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

