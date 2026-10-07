# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:14 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.08 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹32,565 (+3.30%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,231 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹15,466 (+9.03%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹22,909 (-9.66%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹59,353** | **+₹25,122** | **−₹1,570** | **40** | **27** | **₹13,96,681** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:58:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:05:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:05:04] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:11:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:11:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:12:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:09:52] API       rate limited by Dhan - now one call every 15.1 s
[14:10:33] API       rate limited by Dhan - now one call every 15.1 s
[14:11:54] API       rate limited by Dhan - now one call every 15.1 s
[14:12:55] API       rate limited by Dhan - now one call every 15.1 s
[14:13:15] API       rate limited by Dhan - now one call every 15.1 s
[14:13:32] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:13:30] GAP       2026-10-13 22900 PE: no prices for 9 min - bar history restarts
[14:13:30] GAP       2026-10-13 21500 CE: no prices for 9 min - bar history restarts
[14:13:30] GAP       2026-10-13 21500 PE: no prices for 9 min - bar history restarts
[14:13:30] GAP       2026-10-13 23700 CE: no prices for 9 min - bar history restarts
[14:13:30] GAP       2026-10-13 23700 PE: no prices for 9 min - bar history restarts
[14:13:58] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:07:41] API       rate limited by Dhan - now one call every 15.1 s
[14:09:29] API       rate limited by Dhan - now one call every 15.1 s
[14:09:59] API       rate limited by Dhan - now one call every 15.1 s
[14:11:48] API       rate limited by Dhan - now one call every 15.1 s
[14:12:46] API       rate limited by Dhan - now one call every 15.1 s
[14:13:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:01:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:03:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:05:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:07:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:09:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:11:59] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:09:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:10:15] SIGNAL    HDFCLIFE 550 CE 27 Oct crossed EMA 144 at 11.55 - not taken: momentum 3.1%
[14:10:29] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:11:57] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:12:43] WARM      bar history loaded for all 790 contracts
[14:13:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:09:03] API       rate limited by Dhan - now one call every 15.1 s
[14:10:01] API       rate limited by Dhan - now one call every 15.1 s
[14:10:45] API       rate limited by Dhan - now one call every 15.1 s
[14:11:16] API       rate limited by Dhan - now one call every 15.1 s
[14:12:00] API       rate limited by Dhan - now one call every 15.1 s
[14:13:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

