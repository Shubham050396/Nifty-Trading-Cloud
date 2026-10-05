# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:44 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,897 (+1.57%) | +₹8,973 (+1.03%) | +₹60,336 (+1.65%) | 16 | 10 | ₹8,71,941 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,045 (-5.41%) | +₹3,860 (+2.13%) | −₹13,134 (-2.22%) | 13 | 9 | ₹1,81,141 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹9,324 (-6.49%) | ₹0 | 0 | 7 | ₹1,43,744 |
| **Total** | | **+₹12,383** | **+₹3,509** | **+₹70,845** | **36** | **26** | **₹11,96,826** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:33:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:34:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:35:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:36:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:40:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:40:57] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:39:49] API       rate limited by Dhan - now one call every 15.1 s
[13:41:11] API       rate limited by Dhan - now one call every 15.1 s
[13:42:32] API       rate limited by Dhan - now one call every 15.1 s
[13:42:45] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:44:34] API       rate limited by Dhan - now one call every 15.1 s
[13:44:46] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:41:04] API       rate limited by Dhan - now one call every 15.1 s
[13:41:49] API       rate limited by Dhan - now one call every 15.1 s
[13:42:04] API       rate limited by Dhan - now one call every 15.1 s
[13:43:02] API       rate limited by Dhan - now one call every 15.1 s
[13:44:01] API       rate limited by Dhan - now one call every 15.1 s
[13:44:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:40:13] SKIP      short 2026-12-29 24000 PE ignored - open-position cap
[13:42:38] API       rate limited by Dhan - now one call every 5.1 s
[13:43:34] API       rate limited by Dhan - now one call every 5.1 s
[13:43:39] API       rate limited by Dhan - now one call every 7.1 s
[13:44:20] API       rate limited by Dhan - now one call every 5.1 s
[13:44:46] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:50:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:52:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:40:36] ENTRY     BUY 195 22550 CALL @ 105.10  target 156.38  stop 99.97  (IV slope +0.265, z +0.72)
[2026-10-05 13:41:19] EXIT      SIGNAL_DECAY 22550 195 CALL @ 107.55  gross +478  net +403  (0.7)
[2026-10-05 13:42:32] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:44:05] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:42:51] API       market quote: rate limited by Dhan - now one call every 2.5 s
[13:43:08] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:43:46] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:43:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:43:58] API       market quote: rate limited by Dhan - now one call every 2.5 s
[13:44:47] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:39:58] API       rate limited by Dhan - now one call every 15.1 s
[13:42:09] API       rate limited by Dhan - now one call every 15.1 s
[13:42:40] API       rate limited by Dhan - now one call every 15.1 s
[13:42:55] API       rate limited by Dhan - now one call every 15.1 s
[13:43:25] API       rate limited by Dhan - now one call every 15.1 s
[13:44:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

