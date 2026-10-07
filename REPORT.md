# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:39 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹48,588 (-2.42%) | +₹3,396 (+0.49%) | +₹23,718 (+0.35%) | 20 | 10 | ₹6,94,242 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,420 (-4.18%) | +₹16,720 (+11.04%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,895 (-9.84%) | ₹0 | 0 | 8 | ₹2,42,932 |
| **Total** | | **−₹60,126** | **−₹3,779** | **−₹2,343** | **45** | **26** | **₹10,88,582** |

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
[14:33:14] API       rate limited by Dhan - now one call every 15.1 s
[14:33:34] API       rate limited by Dhan - now one call every 15.1 s
[14:34:35] API       rate limited by Dhan - now one call every 15.1 s
[14:34:45] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:35:16] API       rate limited by Dhan - now one call every 15.1 s
[14:36:47] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:34:04] API       rate limited by Dhan - now one call every 15.1 s
[14:35:02] API       rate limited by Dhan - now one call every 15.1 s
[14:36:00] API       rate limited by Dhan - now one call every 15.1 s
[14:37:49] API       rate limited by Dhan - now one call every 15.1 s
[14:38:19] API       rate limited by Dhan - now one call every 15.1 s
[14:38:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:36:18] SIGNAL    2026-10-27 24000 PE MACD crossed DOWN (bar close 1292.00, hist +1.31 -> -0.43)
[14:36:18] EXIT      LONG 2026-10-27 24000 PE MACD_DOWN @ 1303.05  P&L Rs 1147.25
[14:36:18] ENTRY     SELL SHORT 2026-10-27 24000 PE @ 1303.05  (bar close 1292.00, MACD hist -0.43, VIX 13.61)
[14:37:49] API       rate limited by Dhan - now one call every 15.1 s
[14:38:04] API       rate limited by Dhan - now one call every 15.1 s
[14:39:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:27:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:29:08] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:30:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:33:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:36:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:37:42] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:36:18] WARM      bar history loaded for all 791 contracts
[14:36:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:38:05] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:38:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:38:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:39:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:37:04] API       rate limited by Dhan - now one call every 15.1 s
[14:37:34] API       rate limited by Dhan - now one call every 15.1 s
[14:38:04] API       rate limited by Dhan - now one call every 15.1 s
[14:38:19] API       rate limited by Dhan - now one call every 15.1 s
[14:38:35] API       rate limited by Dhan - now one call every 15.1 s
[14:39:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

