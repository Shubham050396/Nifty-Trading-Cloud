# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:42 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹11,346 (-1.66%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,566 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹12,459 (+24.54%) | −₹1,028 (-0.69%) | −₹25,706 (-3.01%) | 3 | 10 | ₹1,49,361 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,318 (-8.54%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹12,459** | **−₹30,692** | **+₹70,243** | **3** | **24** | **₹10,45,305** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:36:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:37:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:39:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:39:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 09:40:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:41:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:33:59] API       rate limited by Dhan - now one call every 15.1 s
[09:35:14] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:38:43] API       rate limited by Dhan - now one call every 14.1 s
[09:39:18] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:39:24] API       rate limited by Dhan - now one call every 15.1 s
[09:40:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:39:16] API       rate limited by Dhan - now one call every 15.1 s
[09:39:46] API       rate limited by Dhan - now one call every 15.1 s
[09:40:16] API       rate limited by Dhan - now one call every 15.1 s
[09:40:46] API       rate limited by Dhan - now one call every 15.1 s
[09:41:45] API       rate limited by Dhan - now one call every 15.1 s
[09:42:00] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:39:46] API       rate limited by Dhan - now one call every 5.1 s
[09:40:05] API       rate limited by Dhan - now one call every 5.1 s
[09:40:23] API       rate limited by Dhan - now one call every 5.1 s
[09:40:51] API       rate limited by Dhan - now one call every 5.1 s
[09:41:26] API       rate limited by Dhan - now one call every 5.1 s
[09:41:45] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 09:01:45] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
[2026-10-07 09:33:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:35:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:37:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:41:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:41:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:41:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:41:34] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:41:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:41:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:42:02] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:39:15] API       rate limited by Dhan - now one call every 15.1 s
[09:39:31] API       rate limited by Dhan - now one call every 15.1 s
[09:40:42] API       rate limited by Dhan - now one call every 15.1 s
[09:40:58] API       rate limited by Dhan - now one call every 15.1 s
[09:41:13] API       rate limited by Dhan - now one call every 15.1 s
[09:41:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

