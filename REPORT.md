# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:04 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.04 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹31,050 (+3.14%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,538 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹16,382 (+9.57%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹22,932 (-9.67%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹59,353** | **+₹24,500** | **−₹1,570** | **40** | **27** | **₹13,96,988** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:49:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:50:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:52:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:52:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:58:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:58:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:56:19] API       rate limited by Dhan - now one call every 15.1 s
[13:56:39] API       rate limited by Dhan - now one call every 15.1 s
[13:56:59] API       rate limited by Dhan - now one call every 15.1 s
[13:58:21] API       rate limited by Dhan - now one call every 15.1 s
[13:59:42] API       rate limited by Dhan - now one call every 15.1 s
[14:00:03] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:02:41] GAP       2026-10-13 23700 CE: no prices for 4 min - bar history restarts
[14:02:41] GAP       2026-10-13 23700 PE: no prices for 4 min - bar history restarts
[14:03:07] API       rate limited by Dhan - now one call every 15.1 s
[14:03:23] API       rate limited by Dhan - now one call every 15.1 s
[14:03:38] API       rate limited by Dhan - now one call every 15.1 s
[14:03:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:59:14] API       rate limited by Dhan - now one call every 6.1 s
[13:59:51] API       rate limited by Dhan - now one call every 5.1 s
[14:00:01] API       rate limited by Dhan - now one call every 6.1 s
[14:00:13] API       rate limited by Dhan - now one call every 8.1 s
[14:00:22] API       rate limited by Dhan - now one call every 13.1 s
[14:01:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 13:53:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:55:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:57:06] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:59:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:01:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:03:50] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:00:18] SKIP      ICICIBANK 1350 CE 27 Oct signal at 26.85 skipped - 20 trades already today
[14:01:24] API       market quote: rate limited by Dhan - now one call every 5.5 s
[14:01:40] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:02:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:03:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:03:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:00:18] API       rate limited by Dhan - now one call every 15.1 s
[14:01:03] API       rate limited by Dhan - now one call every 15.1 s
[14:01:47] API       rate limited by Dhan - now one call every 15.1 s
[14:02:19] VIX       India VIX prev close 13.61
[14:02:45] API       rate limited by Dhan - now one call every 15.1 s
[14:03:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

