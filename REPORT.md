# NIFTY Cloud report

**Running until 15:15 IST** · updated 06 Oct 2026 14:55 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **13.67 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹19,867 (+3.47%) | −₹38,012 (-5.56%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,84,205 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,415 (-22.41%) | +₹7,976 (+7.48%) | −₹41,790 (-5.37%) | 3 | 5 | ₹1,06,691 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹19,038 (-12.33%) | ₹0 | 0 | 8 | ₹1,54,460 |
| **Total** | | **+₹5,452** | **−₹49,074** | **+₹54,159** | **7** | **19** | **₹9,45,356** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 14:42:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:47:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:47:25] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:54:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:54:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:55:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:44:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:49:31] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:50:14] API       rate limited by Dhan - now one call every 9.1 s
[14:51:32] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:52:36] API       rate limited by Dhan - now one call every 9.1 s
[14:53:58] API       rate limited by Dhan - now one call every 12.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:53:12] GAP       2026-10-06 23700 PE: no prices for 5 min - bar history restarts
[14:53:27] API       rate limited by Dhan - now one call every 15.1 s
[14:53:57] API       rate limited by Dhan - now one call every 15.1 s
[14:54:27] API       rate limited by Dhan - now one call every 15.1 s
[14:54:58] API       rate limited by Dhan - now one call every 15.1 s
[14:55:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:51:36] API       rate limited by Dhan - now one call every 15.1 s
[14:51:51] API       rate limited by Dhan - now one call every 15.1 s
[14:53:03] API       rate limited by Dhan - now one call every 15.1 s
[14:53:47] API       rate limited by Dhan - now one call every 15.1 s
[14:54:02] API       rate limited by Dhan - now one call every 15.1 s
[14:55:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 14:45:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:47:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:49:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:51:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:53:20] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:54:53] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:53:21] WARM      bar history loaded for all 634 contracts
[14:53:27] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:55:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:55:19] WARM      bar history loaded for all 636 contracts
[14:55:26] SIGNAL    ABB 7200 CE 27 Oct crossed EMA 144 at 183.35 - not taken: momentum 3.3%
[14:55:26] SIGNAL    TATAPOWER 355 PE 27 Oct crossed EMA 144 at 6.10 - not taken: under EMA 55
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:53:21] API       rate limited by Dhan - now one call every 15.1 s
[14:54:19] API       rate limited by Dhan - now one call every 15.1 s
[14:54:35] API       rate limited by Dhan - now one call every 15.1 s
[14:55:05] SIGNAL    2026-10-27 21000 PE VIX Fix crossed above 10.00 (9.97 -> 10.87, bar close 16.60)
[14:55:05] ENTRY     BUY 2026-10-27 21000 PE @ 16.50 x 65  (Rs 1,072) - buy 2 of 10, average 23.95, target 35.92
[14:55:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

