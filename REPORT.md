# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:54 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.99 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | −₹364 (-1.18%) | +₹21,548 (+7.07%) | 4 | 2 | ₹30,946 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹8,222 (+1.06%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,369 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹8,020 (-5.89%) | −₹911 (-0.74%) | −₹8,109 (-1.66%) | 8 | 6 | ₹1,22,424 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹3,724 (-6.14%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹26,391** | **+₹3,223** | **+₹84,854** | **19** | **22** | **₹9,88,358** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:43:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:44:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:47:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:47:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:53:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:53:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:50:44] API       rate limited by Dhan - now one call every 15.1 s
[11:51:04] API       rate limited by Dhan - now one call every 15.1 s
[11:52:05] API       rate limited by Dhan - now one call every 15.1 s
[11:52:26] API       rate limited by Dhan - now one call every 15.1 s
[11:53:29] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:53:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:50:18] API       rate limited by Dhan - now one call every 15.1 s
[11:50:49] ENTRY     L2 BUY 2026-10-19 22500 PE @ 242.35  target 292.35  trail 206.00 (15%)
[11:51:17] API       rate limited by Dhan - now one call every 15.1 s
[11:51:47] API       rate limited by Dhan - now one call every 15.1 s
[11:52:17] API       rate limited by Dhan - now one call every 15.1 s
[11:53:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:50:43] SIGNAL    2026-10-27 21000 PE MACD crossed UP (bar close 30.85, hist -0.02 -> +0.03)
[11:50:43] SKIP      buy 2026-10-27 21000 PE ignored - premium 30.85 is outside 144 - 1600
[11:51:12] API       rate limited by Dhan - now one call every 15.1 s
[11:52:37] API       rate limited by Dhan - now one call every 15.1 s
[11:53:07] API       rate limited by Dhan - now one call every 15.1 s
[11:53:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:41:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:44:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:47:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:50:32] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:51:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:54:00] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:50:29] ENTRY     BUY ADANIGREEN 1300 PE 27 Oct x600 @ 55.95 (signal close 55.95, EMA 144 54.17, momentum 11.8%)  quick 64.34 till 12:20, target 95.12, stop below EMA 55
[11:50:43] WARM      bar history loaded for all 760 contracts
[11:51:29] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:52:15] WARM      bar history loaded for all 762 contracts
[11:52:29] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:52:40] WARM      bar history loaded for all 762 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:49:10] API       rate limited by Dhan - now one call every 15.1 s
[11:51:22] API       rate limited by Dhan - now one call every 15.1 s
[11:51:37] API       rate limited by Dhan - now one call every 15.1 s
[11:51:52] API       rate limited by Dhan - now one call every 15.1 s
[11:53:04] API       rate limited by Dhan - now one call every 15.1 s
[11:53:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

