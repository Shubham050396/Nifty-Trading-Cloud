# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:53 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.94 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹25,665 (+2.60%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,735 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹15,218 (+8.89%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,855 (-10.06%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹59,353** | **+₹17,028** | **−₹1,570** | **40** | **27** | **₹13,97,185** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:46:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:48:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:49:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:50:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:52:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:52:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:50:53] API       rate limited by Dhan - now one call every 15.1 s
[13:51:34] API       rate limited by Dhan - now one call every 15.1 s
[13:52:15] API       rate limited by Dhan - now one call every 15.1 s
[13:52:55] API       rate limited by Dhan - now one call every 15.1 s
[13:53:18] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:53:36] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:52:33] GAP       2026-10-27 21500 PE: no prices for 5 min - bar history restarts
[13:52:33] GAP       2026-10-27 23700 CE: no prices for 5 min - bar history restarts
[13:52:33] GAP       2026-10-27 23700 PE: no prices for 5 min - bar history restarts
[13:53:01] API       rate limited by Dhan - now one call every 15.1 s
[13:53:17] API       rate limited by Dhan - now one call every 15.1 s
[13:53:32] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:43:55] API       rate limited by Dhan - now one call every 15.1 s
[13:46:35] API       rate limited by Dhan - now one call every 15.1 s
[13:49:33] API       rate limited by Dhan - now one call every 13.1 s
[13:52:06] API       rate limited by Dhan - now one call every 8.1 s
[13:53:07] API       rate limited by Dhan - now one call every 5.1 s
[13:53:28] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 13:43:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:45:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:47:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:49:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:51:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:53:47] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:48:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:50:15] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:50:25] SKIP      DLF 670 PE 27 Oct signal at 23.95 skipped - 20 trades already today
[13:51:56] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:52:05] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:53:34] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:47:22] API       rate limited by Dhan - now one call every 15.1 s
[13:47:38] API       rate limited by Dhan - now one call every 15.1 s
[13:49:02] API       rate limited by Dhan - now one call every 15.1 s
[13:49:32] API       rate limited by Dhan - now one call every 15.1 s
[13:52:38] API       rate limited by Dhan - now one call every 12.1 s
[13:53:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

