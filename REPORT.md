# NIFTY Cloud report

**Running until 15:15 IST** · updated 06 Oct 2026 15:00 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **13.72 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹19,867 (+3.47%) | −₹38,434 (-5.62%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,83,924 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,415 (-22.41%) | +₹8,955 (+6.42%) | −₹41,790 (-5.37%) | 3 | 7 | ₹1,39,441 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,716 (-12.03%) | ₹0 | 0 | 8 | ₹1,55,606 |
| **Total** | | **+₹5,452** | **−₹48,195** | **+₹54,159** | **7** | **21** | **₹9,78,971** |

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
[14:57:41] API       rate limited by Dhan - now one call every 15.1 s
[14:58:38] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:58:42] API       rate limited by Dhan - now one call every 15.1 s
[14:59:23] API       rate limited by Dhan - now one call every 15.1 s
[14:59:43] API       rate limited by Dhan - now one call every 15.1 s
[15:00:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:59:21] GAP       2026-10-13 21500 CE: no prices for 7 min - bar history restarts
[14:59:21] GAP       2026-10-13 21500 PE: no prices for 7 min - bar history restarts
[14:59:21] GAP       2026-10-13 23700 CE: no prices for 7 min - bar history restarts
[14:59:21] GAP       2026-10-13 23700 PE: no prices for 7 min - bar history restarts
[15:00:11] API       rate limited by Dhan - now one call every 15.1 s
[15:00:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:55:27] API       rate limited by Dhan - now one call every 15.1 s
[14:56:38] API       rate limited by Dhan - now one call every 15.1 s
[14:57:50] API       rate limited by Dhan - now one call every 15.1 s
[14:58:20] API       rate limited by Dhan - now one call every 15.1 s
[14:59:57] API       rate limited by Dhan - now one call every 15.1 s
[15:00:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 14:51:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:53:20] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:54:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:56:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:58:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:00:06] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:59:46] API       market quote: rate limited by Dhan - now one call every 8.6 s
[15:00:14] WARM      bar history loaded for all 642 contracts
[15:00:20] SIGNAL    NTPC 320 PE 27 Oct crossed EMA 144 at 4.75 - not taken: under EMA 55, premium under Rs 5
[15:00:28] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:00:28] ENTRY     BUY INDHOTEL 730 CE 27 Oct x1000 @ 19.85 (signal close 19.85, EMA 144 19.72, momentum 4.7%)  quick 22.83 till 15:30, target 33.75, stop below EMA 55
[15:00:28] ENTRY     BUY GODREJCP 860 CE 27 Oct x500 @ 25.80 (signal close 25.80, EMA 144 25.70, momentum 4.9%)  quick 29.67 till 15:30, target 43.86, stop below EMA 55
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:57:19] API       rate limited by Dhan - now one call every 15.1 s
[14:58:04] API       rate limited by Dhan - now one call every 15.1 s
[15:00:04] SIGNAL    2026-10-27 24000 CE VIX Fix crossed above 10.00 (9.42 -> 10.58, bar close 14.00)
[15:00:04] ENTRY     BUY 2026-10-27 24000 CE @ 13.90 x 65  (Rs 904) - buy 2 of 10, average 15.07, target 22.61
[15:00:04] SIGNAL    2026-10-27 25000 CE VIX Fix crossed above 10.00 (9.41 -> 10.59, bar close 3.75)
[15:00:04] ENTRY     BUY 2026-10-27 25000 CE @ 3.75 x 65  (Rs 244) - buy 3 of 10, average 4.45, target 6.68
```
</details>

