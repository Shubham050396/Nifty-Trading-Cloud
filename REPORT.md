# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:48 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.94 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹22,805 (+2.30%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,89,505 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹15,535 (+9.07%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,458 (-9.89%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹59,353** | **+₹14,882** | **−₹1,570** | **40** | **27** | **₹13,97,955** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:37:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:37:58] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:45:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:45:59] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:46:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:48:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:44:11] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:44:47] API       rate limited by Dhan - now one call every 15.1 s
[13:46:09] API       rate limited by Dhan - now one call every 15.1 s
[13:47:30] API       rate limited by Dhan - now one call every 15.1 s
[13:48:11] API       rate limited by Dhan - now one call every 15.1 s
[13:48:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:48:05] GAP       2026-10-13 21500 CE: no prices for 4 min - bar history restarts
[13:48:05] GAP       2026-10-13 21500 PE: no prices for 4 min - bar history restarts
[13:48:05] GAP       2026-10-13 23700 CE: no prices for 4 min - bar history restarts
[13:48:05] GAP       2026-10-13 23700 PE: no prices for 4 min - bar history restarts
[13:48:32] API       rate limited by Dhan - now one call every 15.1 s
[13:48:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:39:33] API       rate limited by Dhan - now one call every 9.1 s
[13:39:59] API       rate limited by Dhan - now one call every 13.1 s
[13:42:06] API       rate limited by Dhan - now one call every 12.1 s
[13:42:18] API       rate limited by Dhan - now one call every 15.1 s
[13:43:55] API       rate limited by Dhan - now one call every 15.1 s
[13:46:35] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 13:37:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:39:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:41:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:43:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:45:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:47:11] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:45:18] SIGNAL    SOLARINDS 20250 CE 27 Oct crossed EMA 144 at 535.00 - not taken: momentum -8.8%
[13:45:18] SIGNAL    ITC 260 PE 27 Oct crossed EMA 144 at 3.10 - not taken: premium under Rs 5
[13:45:51] API       market quote: rate limited by Dhan - now one call every 8.6 s
[13:46:09] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:46:18] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:47:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:43:48] API       rate limited by Dhan - now one call every 15.1 s
[13:44:18] API       rate limited by Dhan - now one call every 15.1 s
[13:45:30] API       rate limited by Dhan - now one call every 15.1 s
[13:45:45] API       rate limited by Dhan - now one call every 15.1 s
[13:47:22] API       rate limited by Dhan - now one call every 15.1 s
[13:47:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

