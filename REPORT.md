# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:09 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.33 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | +₹4,180 (+13.51%) | +₹21,548 (+7.07%) | 4 | 2 | ₹30,946 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹27,592 (+3.57%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,72,843 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹8,590 (-5.56%) | +₹3,125 (+2.55%) | −₹8,679 (-1.71%) | 9 | 6 | ₹1,22,424 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹7,680 (-12.67%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹25,821** | **+₹27,217** | **+₹84,284** | **20** | **22** | **₹9,86,832** |

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
[11:57:31] API       rate limited by Dhan - now one call every 15.1 s
[12:01:36] API       rate limited by Dhan - now one call every 15.1 s
[12:01:56] API       rate limited by Dhan - now one call every 15.1 s
[12:03:18] API       rate limited by Dhan - now one call every 15.1 s
[12:04:39] API       rate limited by Dhan - now one call every 15.1 s
[12:06:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:03:56] GAP       2026-10-06 23500 PE: no prices for 4 min - bar history restarts
[12:04:40] SKIP      L3 2026-10-27 22600 PE cross ignored - daily cap
[12:04:53] API       rate limited by Dhan - now one call every 15.1 s
[12:06:42] API       rate limited by Dhan - now one call every 15.1 s
[12:07:40] API       rate limited by Dhan - now one call every 15.1 s
[12:08:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:06:14] API       rate limited by Dhan - now one call every 15.1 s
[12:06:30] API       rate limited by Dhan - now one call every 15.1 s
[12:07:28] API       rate limited by Dhan - now one call every 15.1 s
[12:07:43] API       rate limited by Dhan - now one call every 15.1 s
[12:07:59] API       rate limited by Dhan - now one call every 15.1 s
[12:08:58] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:56:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:59:02] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:02:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:04:00] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:05:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:08:03] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:07:03] API       market quote: rate limited by Dhan - now one call every 3.0 s
[12:07:14] API       market quote: rate limited by Dhan - now one call every 3.5 s
[12:07:31] API       market quote: rate limited by Dhan - now one call every 4.0 s
[12:07:50] API       market quote: rate limited by Dhan - now one call every 5.0 s
[12:08:35] API       market quote: rate limited by Dhan - now one call every 4.0 s
[12:08:54] API       market quote: rate limited by Dhan - now one call every 5.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:03:58] API       rate limited by Dhan - now one call every 15.1 s
[12:04:14] API       rate limited by Dhan - now one call every 15.1 s
[12:05:26] API       rate limited by Dhan - now one call every 15.1 s
[12:05:41] API       rate limited by Dhan - now one call every 15.1 s
[12:08:03] API       rate limited by Dhan - now one call every 15.1 s
[12:08:33] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

