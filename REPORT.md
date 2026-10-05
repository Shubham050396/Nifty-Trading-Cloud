# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:48 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.90 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | ₹0 | +₹21,548 (+7.07%) | 4 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹4,709 (+0.61%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,299 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹6,044 (-4.93%) | −₹3,256 (-3.18%) | −₹6,132 (-1.29%) | 7 | 6 | ₹1,02,369 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹3,663 (-6.04%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹28,367** | **−₹2,210** | **+₹86,831** | **18** | **20** | **₹9,37,287** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:41:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:42:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:43:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:44:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:47:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:47:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:43:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:44:16] API       rate limited by Dhan - now one call every 15.1 s
[11:45:18] API       rate limited by Dhan - now one call every 15.1 s
[11:47:00] API       rate limited by Dhan - now one call every 15.1 s
[11:48:01] API       rate limited by Dhan - now one call every 15.1 s
[11:48:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:46:18] GAP       2026-10-27 22000 PE: no prices for 5 min - bar history restarts
[11:46:18] GAP       2026-10-27 22900 PE: no prices for 5 min - bar history restarts
[11:46:18] GAP       2026-10-27 21500 CE: no prices for 5 min - bar history restarts
[11:46:18] GAP       2026-10-27 21500 PE: no prices for 5 min - bar history restarts
[11:47:25] API       rate limited by Dhan - now one call every 15.1 s
[11:48:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:46:08] SKIP      short 2026-11-23 23000 CE ignored - open-position cap
[11:46:08] SIGNAL    2026-11-23 24000 PE MACD crossed UP (bar close 1343.00, hist -0.22 -> +0.31)
[11:46:08] SKIP      buy 2026-11-23 24000 PE ignored - open-position cap
[11:46:51] API       rate limited by Dhan - now one call every 15.1 s
[11:47:07] API       rate limited by Dhan - now one call every 15.1 s
[11:48:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:35:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:37:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:40:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:41:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:44:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:47:21] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:45:20] WARM      bar history loaded for all 758 contracts
[11:45:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:46:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:48:39] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:48:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:48:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:44:16] API       rate limited by Dhan - now one call every 15.1 s
[11:45:28] API       rate limited by Dhan - now one call every 15.1 s
[11:45:59] API       rate limited by Dhan - now one call every 15.1 s
[11:46:29] API       rate limited by Dhan - now one call every 15.1 s
[11:47:13] API       rate limited by Dhan - now one call every 15.1 s
[11:48:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

