# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:47 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹13,442 (-1.97%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,805 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹10,216 (+17.54%) | +₹4,719 (+3.05%) | −₹27,949 (-3.25%) | 4 | 10 | ₹1,54,806 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,584 (-8.20%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹10,216** | **−₹26,307** | **+₹68,000** | **4** | **24** | **₹10,50,989** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:41:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:42:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:43:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:44:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:45:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:46:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:39:18] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:39:24] API       rate limited by Dhan - now one call every 15.1 s
[09:40:45] API       rate limited by Dhan - now one call every 15.1 s
[09:43:28] API       rate limited by Dhan - now one call every 15.1 s
[09:44:08] API       rate limited by Dhan - now one call every 15.1 s
[09:46:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:44:46] GAP       2026-10-13 21500 CE: no prices for 7 min - bar history restarts
[09:44:46] GAP       2026-10-13 21500 PE: no prices for 7 min - bar history restarts
[09:44:46] GAP       2026-10-13 23700 CE: no prices for 7 min - bar history restarts
[09:44:46] GAP       2026-10-13 23700 PE: no prices for 7 min - bar history restarts
[09:45:42] API       rate limited by Dhan - now one call every 15.1 s
[09:46:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:42:48] API       rate limited by Dhan - now one call every 5.1 s
[09:43:02] API       rate limited by Dhan - now one call every 5.1 s
[09:43:08] API       rate limited by Dhan - now one call every 7.1 s
[09:43:52] API       rate limited by Dhan - now one call every 5.1 s
[09:45:21] API       rate limited by Dhan - now one call every 5.1 s
[09:46:16] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 09:33:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:35:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:37:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:41:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:43:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:45:51] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:46:30] SKIP      DRREDDY 1230 CE 27 Oct signal at 24.90 skipped - 10 positions already open
[09:46:30] SKIP      HDFCLIFE 550 CE 27 Oct signal at 12.10 skipped - 10 positions already open
[09:46:39] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:46:51] WARM      bar history loaded for all 776 contracts
[09:46:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:47:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:44:24] API       rate limited by Dhan - now one call every 15.1 s
[09:44:39] API       rate limited by Dhan - now one call every 15.1 s
[09:45:38] API       rate limited by Dhan - now one call every 15.1 s
[09:46:22] API       rate limited by Dhan - now one call every 15.1 s
[09:46:37] API       rate limited by Dhan - now one call every 15.1 s
[09:46:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

