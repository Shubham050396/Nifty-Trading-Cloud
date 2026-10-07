# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:43 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.92 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹20,176 (+2.04%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,89,399 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹13,783 (+8.05%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,420 (-9.87%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹59,353** | **+₹10,539** | **−₹1,570** | **40** | **27** | **₹13,97,849** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:32:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:32:56] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:34:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:34:57] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:37:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:37:58] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:38:41] API       rate limited by Dhan - now one call every 15.1 s
[13:39:22] API       rate limited by Dhan - now one call every 15.1 s
[13:40:44] API       rate limited by Dhan - now one call every 15.1 s
[13:41:24] API       rate limited by Dhan - now one call every 15.1 s
[13:42:05] API       rate limited by Dhan - now one call every 15.1 s
[13:43:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:39:32] GAP       2026-10-13 23700 PE: no prices for 5 min - bar history restarts
[13:40:00] API       rate limited by Dhan - now one call every 15.1 s
[13:40:30] API       rate limited by Dhan - now one call every 15.1 s
[13:41:29] API       rate limited by Dhan - now one call every 15.1 s
[13:42:53] API       rate limited by Dhan - now one call every 15.1 s
[13:43:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:38:50] API       rate limited by Dhan - now one call every 7.1 s
[13:39:26] API       rate limited by Dhan - now one call every 6.1 s
[13:39:33] API       rate limited by Dhan - now one call every 9.1 s
[13:39:59] API       rate limited by Dhan - now one call every 13.1 s
[13:42:06] API       rate limited by Dhan - now one call every 12.1 s
[13:42:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 13:34:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:36:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:37:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:39:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:41:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:43:27] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:40:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:40:59] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:41:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:41:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:41:27] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:41:38] WARM      bar history loaded for all 790 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:40:12] ENTRY     BUY 2026-10-27 22000 PE @ 88.00 x 65  (Rs 5,720) - buy 3 of 10, average 99.03, target 148.55
[13:40:52] API       rate limited by Dhan - now one call every 15.1 s
[13:41:36] API       rate limited by Dhan - now one call every 15.1 s
[13:42:06] API       rate limited by Dhan - now one call every 15.1 s
[13:42:37] API       rate limited by Dhan - now one call every 15.1 s
[13:43:48] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

