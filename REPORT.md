# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:43 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.90 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | ₹0 | +₹21,548 (+7.07%) | 4 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹172 (+0.03%) | +₹69,722 (+2.42%) | 7 | 8 | ₹6,15,077 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹6,044 (-4.93%) | −₹3,110 (-3.04%) | −₹6,132 (-1.29%) | 7 | 6 | ₹1,02,369 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹2,580 (-4.26%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹28,367** | **−₹5,518** | **+₹86,831** | **18** | **18** | **₹7,78,065** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:37:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:40:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:40:27] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:41:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:42:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:43:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:37:29] API       rate limited by Dhan - now one call every 15.1 s
[11:38:10] API       rate limited by Dhan - now one call every 15.1 s
[11:38:30] API       rate limited by Dhan - now one call every 15.1 s
[11:38:50] API       rate limited by Dhan - now one call every 15.1 s
[11:40:12] API       rate limited by Dhan - now one call every 15.1 s
[11:43:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:43:34] GAP       2026-10-06 21400 CE: no prices for 16 min - bar history restarts
[11:43:34] GAP       2026-10-06 21400 PE: no prices for 16 min - bar history restarts
[11:43:34] GAP       2026-10-06 23600 CE: no prices for 16 min - bar history restarts
[11:43:34] GAP       2026-10-06 23500 CE: no prices for 16 min - bar history restarts
[11:43:34] GAP       2026-10-06 23600 PE: no prices for 16 min - bar history restarts
[11:43:34] GAP       2026-10-06 23500 PE: no prices for 16 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:41:00] API       rate limited by Dhan - now one call every 15.1 s
[11:41:15] API       rate limited by Dhan - now one call every 15.1 s
[11:42:14] SIGNAL    2027-03-30 21000 CE MACD crossed DOWN (bar close 2316.00, hist +0.12 -> -0.20)
[11:42:14] SKIP      short 2027-03-30 21000 CE ignored - premium 2316.00 is outside 144 - 1600
[11:42:14] SIGNAL    2027-03-30 21000 PE MACD crossed UP (bar close 207.00, hist -0.12 -> +0.07)
[11:42:14] ENTRY     BUY 2027-03-30 21000 PE @ 205.80  (bar close 207.00, MACD hist +0.07, VIX 14.46)
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:31:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:34:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:35:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:37:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:40:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:41:40] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:41:03] WARM      bar history loaded for all 758 contracts
[11:41:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:42:20] WARM      bar history loaded for all 758 contracts
[11:42:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:43:02] WARM      bar history loaded for all 758 contracts
[11:43:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:38:19] API       rate limited by Dhan - now one call every 15.1 s
[11:39:43] API       rate limited by Dhan - now one call every 15.1 s
[11:41:21] API       rate limited by Dhan - now one call every 15.1 s
[11:42:19] API       rate limited by Dhan - now one call every 15.1 s
[11:42:34] API       rate limited by Dhan - now one call every 15.1 s
[11:43:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

