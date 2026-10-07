# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:22 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.82 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | −₹162 (-0.71%) | +₹21,548 (+6.41%) | 0 | 1 | ₹22,987 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹28,034 (-4.10%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,83,517 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹3,288 (-2.00%) | +₹5,310 (+3.39%) | −₹41,452 (-4.29%) | 11 | 8 | ₹1,56,730 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,001 (-7.26%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹3,288** | **−₹38,887** | **+₹54,497** | **11** | **23** | **₹10,83,566** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:03:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:03:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:16:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:16:15] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:22:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:22:16] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:15:42] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:16:40] API       rate limited by Dhan - now one call every 15.1 s
[10:20:24] API       rate limited by Dhan - now one call every 15.1 s
[10:20:44] API       rate limited by Dhan - now one call every 15.1 s
[10:20:45] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:21:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:20:48] GAP       2026-10-27 22900 PE: no prices for 4 min - bar history restarts
[10:20:48] GAP       2026-10-27 21500 CE: no prices for 4 min - bar history restarts
[10:20:48] GAP       2026-10-27 21500 PE: no prices for 4 min - bar history restarts
[10:20:48] GAP       2026-10-27 23700 CE: no prices for 4 min - bar history restarts
[10:20:48] GAP       2026-10-27 23700 PE: no prices for 4 min - bar history restarts
[10:21:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:15:39] API       rate limited by Dhan - now one call every 15.1 s
[10:18:10] API       rate limited by Dhan - now one call every 15.1 s
[10:18:41] API       rate limited by Dhan - now one call every 15.1 s
[10:19:11] API       rate limited by Dhan - now one call every 15.1 s
[10:19:26] API       rate limited by Dhan - now one call every 15.1 s
[10:21:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:14:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:14:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:15:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:17:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:18:46] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:21:01] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:20:29] ENTRY     BUY ICICIBANK 1330 CE 27 Oct x700 @ 36.25 (signal close 36.00, EMA 144 35.76, momentum 18.6%)  quick 41.69 till 10:50, target 61.62, stop below EMA 55
[10:20:57] WARM      bar history loaded for all 780 contracts
[10:21:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:21:31] WARM      bar history loaded for all 780 contracts
[10:21:47] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:21:59] WARM      bar history loaded for all 780 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:20:23] ENTRY     BUY 2026-10-27 21000 PE @ 15.70 x 65  (Rs 1,020) - buy 3 of 10, average 21.20, target 31.80
[10:20:23] SIGNAL    2026-10-27 22000 PE VIX Fix crossed above 10.00 (7.77 -> 12.23, bar close 76.25)
[10:20:23] ENTRY     BUY 2026-10-27 22000 PE @ 75.90 x 65  (Rs 4,934) - buy 2 of 10, average 104.55, target 156.82
[10:21:06] API       rate limited by Dhan - now one call every 15.1 s
[10:21:36] API       rate limited by Dhan - now one call every 15.1 s
[10:22:06] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

