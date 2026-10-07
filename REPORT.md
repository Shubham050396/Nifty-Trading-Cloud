# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:34 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹50,193 (-3.09%) | +₹1,076 (+0.13%) | +₹22,113 (+0.35%) | 17 | 10 | ₹8,58,231 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,420 (-4.18%) | +₹15,154 (+10.01%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹22,864 (-9.41%) | ₹0 | 0 | 8 | ₹2,42,932 |
| **Total** | | **−₹61,731** | **−₹6,634** | **−₹3,948** | **42** | **26** | **₹12,52,571** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 14:27:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:27:09] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:28:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:33:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:33:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:34:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:31:32] API       rate limited by Dhan - now one call every 15.1 s
[14:31:53] API       rate limited by Dhan - now one call every 15.1 s
[14:32:13] API       rate limited by Dhan - now one call every 15.1 s
[14:32:33] API       rate limited by Dhan - now one call every 15.1 s
[14:33:14] API       rate limited by Dhan - now one call every 15.1 s
[14:33:34] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:32:37] GAP       2026-10-27 21500 CE: no prices for 5 min - bar history restarts
[14:32:37] GAP       2026-10-27 21500 PE: no prices for 5 min - bar history restarts
[14:32:37] GAP       2026-10-27 23700 CE: no prices for 5 min - bar history restarts
[14:32:37] GAP       2026-10-27 23700 PE: no prices for 5 min - bar history restarts
[14:33:05] API       rate limited by Dhan - now one call every 15.1 s
[14:34:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:28:27] API       rate limited by Dhan - now one call every 15.1 s
[14:30:38] SIGNAL    2026-12-29 24000 CE MACD crossed UP (bar close 157.65, hist -0.22 -> +0.09)
[14:30:38] EXIT      SHORT 2026-12-29 24000 CE MACD_UP @ 157.55  P&L Rs -328.25
[14:30:38] ENTRY     BUY 2026-12-29 24000 CE @ 157.55  (bar close 157.65, MACD hist +0.09, VIX 13.61)
[14:31:32] API       rate limited by Dhan - now one call every 12.1 s
[14:32:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:23:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:25:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:27:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:29:08] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:30:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:33:21] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:30:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:31:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:31:21] WARM      bar history loaded for all 791 contracts
[14:31:40] WARM      bar history loaded for all 791 contracts
[14:32:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:33:38] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:30:05] ENTRY     BUY 2026-10-27 22000 PE @ 73.45 x 65  (Rs 4,774) - buy 4 of 10, average 92.64, target 138.96
[14:31:01] API       rate limited by Dhan - now one call every 15.1 s
[14:31:16] API       rate limited by Dhan - now one call every 15.1 s
[14:31:32] API       rate limited by Dhan - now one call every 15.1 s
[14:32:56] API       rate limited by Dhan - now one call every 15.1 s
[14:34:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

