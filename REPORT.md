# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:12 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.02 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹14,180 (-2.08%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,996 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹6,272 (+6.25%) | −₹1,207 (-0.75%) | −₹31,892 (-3.53%) | 7 | 10 | ₹1,61,201 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,994 (-8.86%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹6,272** | **−₹34,381** | **+₹64,057** | **7** | **24** | **₹10,57,575** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:55:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 09:56:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:57:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:58:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:03:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:03:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:07:11] API       rate limited by Dhan - now one call every 15.1 s
[10:07:36] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:07:51] API       rate limited by Dhan - now one call every 15.1 s
[10:09:13] API       rate limited by Dhan - now one call every 15.1 s
[10:10:34] API       rate limited by Dhan - now one call every 15.1 s
[10:11:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:05:56] GAP       2026-10-13 23700 PE: no prices for 7 min - bar history restarts
[10:06:51] API       rate limited by Dhan - now one call every 15.1 s
[10:08:15] API       rate limited by Dhan - now one call every 15.1 s
[10:08:45] API       rate limited by Dhan - now one call every 15.1 s
[10:10:34] API       rate limited by Dhan - now one call every 15.1 s
[10:11:32] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:04:33] API       rate limited by Dhan - now one call every 12.1 s
[10:04:57] API       rate limited by Dhan - now one call every 15.1 s
[10:05:27] API       rate limited by Dhan - now one call every 15.1 s
[10:06:25] API       rate limited by Dhan - now one call every 15.1 s
[10:07:23] API       rate limited by Dhan - now one call every 15.1 s
[10:09:54] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:02:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:03:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:04:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:06:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:07:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:09:55] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:10:17] SKIP      ICICIBANK 1330 CE 27 Oct signal at 38.05 skipped - 10 positions already open
[10:10:45] WARM      bar history loaded for all 780 contracts
[10:11:01] WARM      bar history loaded for all 780 contracts
[10:11:14] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:11:24] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:11:53] WARM      bar history loaded for all 780 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:05:50] API       rate limited by Dhan - now one call every 15.1 s
[10:07:02] API       rate limited by Dhan - now one call every 15.1 s
[10:09:12] API       rate limited by Dhan - now one call every 15.1 s
[10:10:11] API       rate limited by Dhan - now one call every 15.1 s
[10:10:41] API       rate limited by Dhan - now one call every 15.1 s
[10:12:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

