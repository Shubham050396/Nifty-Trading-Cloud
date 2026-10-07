# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:19 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.08 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹24,846 (+2.51%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,768 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,420 (-4.18%) | +₹17,868 (+11.80%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,907 (-10.08%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹61,403** | **+₹18,807** | **−₹3,620** | **41** | **26** | **₹13,77,368** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 14:05:04] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:11:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:11:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:12:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:14:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:14:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:14:37] API       rate limited by Dhan - now one call every 15.1 s
[14:15:17] API       rate limited by Dhan - now one call every 15.1 s
[14:15:58] API       rate limited by Dhan - now one call every 15.1 s
[14:16:18] API       rate limited by Dhan - now one call every 15.1 s
[14:17:19] API       rate limited by Dhan - now one call every 15.1 s
[14:18:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:14:58] GAP       2026-10-27 23700 CE: no prices for 5 min - bar history restarts
[14:14:58] GAP       2026-10-27 23700 PE: no prices for 5 min - bar history restarts
[14:15:26] API       rate limited by Dhan - now one call every 15.1 s
[14:17:05] VIX       India VIX prev close 13.61 -> target 1000 ticks (Rs 50.00)
[14:17:15] API       rate limited by Dhan - now one call every 15.1 s
[14:18:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:14:41] API       rate limited by Dhan - now one call every 15.1 s
[14:14:57] API       rate limited by Dhan - now one call every 15.1 s
[14:16:21] API       rate limited by Dhan - now one call every 15.1 s
[14:16:36] API       rate limited by Dhan - now one call every 15.1 s
[14:16:52] API       rate limited by Dhan - now one call every 15.1 s
[14:18:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:07:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:09:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:11:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:14:10] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:16:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:18:40] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:15:16] SKIP      ZYDUSLIFE 1150 PE 27 Oct signal at 27.55 skipped - 20 trades already today
[14:15:33] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:16:03] WARM      bar history loaded for all 790 contracts
[14:16:09] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:17:09] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:19:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:13:49] API       rate limited by Dhan - now one call every 15.1 s
[14:15:01] API       rate limited by Dhan - now one call every 15.1 s
[14:16:38] API       rate limited by Dhan - now one call every 15.1 s
[14:16:53] API       rate limited by Dhan - now one call every 15.1 s
[14:17:38] API       rate limited by Dhan - now one call every 15.1 s
[14:19:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

