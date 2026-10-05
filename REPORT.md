# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 09:48 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.41 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹20,420 (+9.20%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹62,644 (+11.05%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,66,764 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,650 (-34.21%) | +₹11,290 (+19.87%) | −₹12,739 (-3.28%) | 2 | 3 | ₹56,825 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **−₹12,650** | **+₹73,934** | **+₹45,813** | **2** | **8** | **₹6,23,589** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 09:42:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:43:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:44:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:45:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:46:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:47:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:42:58] API       rate limited by Dhan - now one call every 15.1 s
[09:43:02] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:43:19] API       rate limited by Dhan - now one call every 15.1 s
[09:43:59] API       rate limited by Dhan - now one call every 15.1 s
[09:46:01] API       rate limited by Dhan - now one call every 15.1 s
[09:47:23] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:48:03] GAP       2026-10-27 23000 PE: no prices for 4 min - bar history restarts
[09:48:03] GAP       2026-10-27 21600 PE: no prices for 4 min - bar history restarts
[09:48:03] GAP       2026-10-27 22500 PE: no prices for 4 min - bar history restarts
[09:48:03] GAP       2026-10-27 23400 PE: no prices for 4 min - bar history restarts
[09:48:03] GAP       2026-10-27 22000 PE: no prices for 4 min - bar history restarts
[09:48:03] GAP       2026-10-27 22900 PE: no prices for 4 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:43:01] API       rate limited by Dhan - now one call every 15.1 s
[09:43:59] API       rate limited by Dhan - now one call every 15.1 s
[09:44:15] API       rate limited by Dhan - now one call every 15.1 s
[09:44:45] API       rate limited by Dhan - now one call every 15.1 s
[09:45:44] API       rate limited by Dhan - now one call every 15.1 s
[09:46:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 09:37:57] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/state HTTP/1.1" 200 -
[2026-10-05 09:41:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:43:06] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:44:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:46:39] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:47:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:47:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:47:35] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:47:44] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:47:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:48:03] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:40:31] API       rate limited by Dhan - now one call every 15.1 s
[09:42:09] API       rate limited by Dhan - now one call every 15.1 s
[09:43:46] API       rate limited by Dhan - now one call every 15.1 s
[09:44:44] API       rate limited by Dhan - now one call every 15.1 s
[09:45:43] API       rate limited by Dhan - now one call every 15.1 s
[09:47:43] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

