# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 09:43 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.41 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹20,420 (+9.20%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹56,059 (+9.90%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,66,256 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,650 (-34.21%) | +₹12,068 (+21.24%) | −₹12,739 (-3.28%) | 2 | 3 | ₹56,825 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **−₹12,650** | **+₹68,127** | **+₹45,813** | **2** | **8** | **₹6,23,081** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/status HTTP/1.1" 200 -
[2026-10-05 09:38:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:39:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:40:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:41:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:42:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:40:16] API       rate limited by Dhan - now one call every 15.1 s
[09:40:36] API       rate limited by Dhan - now one call every 15.1 s
[09:41:37] API       rate limited by Dhan - now one call every 15.1 s
[09:41:57] API       rate limited by Dhan - now one call every 15.1 s
[09:42:58] API       rate limited by Dhan - now one call every 15.1 s
[09:43:02] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:39:29] API       rate limited by Dhan - now one call every 15.1 s
[09:40:14] API       rate limited by Dhan - now one call every 15.1 s
[09:40:29] API       rate limited by Dhan - now one call every 15.1 s
[09:41:14] API       rate limited by Dhan - now one call every 15.1 s
[09:41:29] API       rate limited by Dhan - now one call every 15.1 s
[09:42:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:40:59] API       rate limited by Dhan - now one call every 5.1 s
[09:41:04] API       rate limited by Dhan - now one call every 7.1 s
[09:41:11] API       rate limited by Dhan - now one call every 11.1 s
[09:41:34] API       rate limited by Dhan - now one call every 15.1 s
[09:42:45] API       rate limited by Dhan - now one call every 15.1 s
[09:43:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 09:37:55] DATA      buffer cleared: day roll
[2026-10-05 09:37:55] RUN       scalper armed - started automatically on launch
[2026-10-05 09:37:57] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-05 09:37:57] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/state HTTP/1.1" 200 -
[2026-10-05 09:41:28] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:42:10] EXIT      SELL DLF 670 PE 27 Oct EMA_STOP @ 19.00  -30.1%  P&L Rs -7790.00
[09:42:19] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:42:28] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:42:37] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:42:47] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:42:56] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:39:30] API       rate limited by Dhan - now one call every 15.1 s
[09:39:45] API       rate limited by Dhan - now one call every 15.1 s
[09:40:00] API       rate limited by Dhan - now one call every 15.1 s
[09:40:16] API       rate limited by Dhan - now one call every 15.1 s
[09:40:31] API       rate limited by Dhan - now one call every 15.1 s
[09:42:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

