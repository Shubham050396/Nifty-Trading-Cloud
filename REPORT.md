# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:37 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹13,978 (-2.05%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,789 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹12,459 (+24.54%) | +₹484 (+0.32%) | −₹25,706 (-3.01%) | 3 | 10 | ₹1,49,361 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,185 (-8.48%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹12,459** | **−₹31,679** | **+₹70,243** | **3** | **24** | **₹10,45,528** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:31:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:32:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:33:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:34:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:35:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:36:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:30:35] API       rate limited by Dhan - now one call every 15.1 s
[09:31:57] API       rate limited by Dhan - now one call every 15.1 s
[09:33:18] API       rate limited by Dhan - now one call every 15.1 s
[09:33:38] API       rate limited by Dhan - now one call every 15.1 s
[09:33:59] API       rate limited by Dhan - now one call every 15.1 s
[09:35:14] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:33:52] API       rate limited by Dhan - now one call every 15.1 s
[09:34:22] API       rate limited by Dhan - now one call every 15.1 s
[09:34:52] API       rate limited by Dhan - now one call every 15.1 s
[09:35:23] API       rate limited by Dhan - now one call every 15.1 s
[09:36:21] API       rate limited by Dhan - now one call every 15.1 s
[09:36:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:33:59] API       rate limited by Dhan - now one call every 5.1 s
[09:34:09] API       rate limited by Dhan - now one call every 6.1 s
[09:34:40] API       rate limited by Dhan - now one call every 5.1 s
[09:35:05] API       rate limited by Dhan - now one call every 5.1 s
[09:36:03] API       rate limited by Dhan - now one call every 5.1 s
[09:36:28] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 09:01:44] RUN       scalper armed - started automatically on launch
[2026-10-07 09:01:45] BOOT      scrip master: 4056 NIFTY contracts
[2026-10-07 09:01:45] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
[2026-10-07 09:33:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:35:56] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:36:12] SIGNAL    ZYDUSLIFE 1150 PE 27 Oct crossed EMA 144 at 25.70 - not taken: under EMA 55
[09:36:21] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:36:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:36:39] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:36:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:36:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:34:06] API       rate limited by Dhan - now one call every 10.1 s
[09:34:35] API       rate limited by Dhan - now one call every 15.1 s
[09:34:50] API       rate limited by Dhan - now one call every 15.1 s
[09:35:35] API       rate limited by Dhan - now one call every 15.1 s
[09:36:33] API       rate limited by Dhan - now one call every 15.1 s
[09:36:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

