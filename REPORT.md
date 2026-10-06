# NIFTY Cloud report

**Running until 15:15 IST** · updated 06 Oct 2026 14:50 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **13.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹19,867 (+3.47%) | −₹39,933 (-5.84%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,84,198 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,415 (-22.41%) | +₹5,698 (+5.34%) | −₹41,790 (-5.37%) | 3 | 5 | ₹1,06,691 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,411 (-12.00%) | ₹0 | 0 | 8 | ₹1,53,387 |
| **Total** | | **+₹5,452** | **−₹52,646** | **+₹54,159** | **7** | **19** | **₹9,44,276** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 14:40:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:40:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:41:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:42:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:47:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:47:25] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:42:06] API       rate limited by Dhan - now one call every 15.1 s
[14:43:07] API       rate limited by Dhan - now one call every 15.1 s
[14:43:48] API       rate limited by Dhan - now one call every 15.1 s
[14:44:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:49:31] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:50:14] API       rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:48:36] GAP       2026-10-13 21500 PE: no prices for 4 min - bar history restarts
[14:48:36] GAP       2026-10-13 23700 CE: no prices for 4 min - bar history restarts
[14:48:36] GAP       2026-10-13 23700 PE: no prices for 4 min - bar history restarts
[14:49:15] API       rate limited by Dhan - now one call every 15.1 s
[14:49:30] API       rate limited by Dhan - now one call every 15.1 s
[14:50:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:42:56] API       rate limited by Dhan - now one call every 15.1 s
[14:45:37] API       rate limited by Dhan - now one call every 15.1 s
[14:45:52] API       rate limited by Dhan - now one call every 15.1 s
[14:48:41] API       rate limited by Dhan - now one call every 14.1 s
[14:49:09] API       rate limited by Dhan - now one call every 15.1 s
[14:49:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 14:40:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:42:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:44:08] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:45:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:47:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:49:16] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:48:36] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:48:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:50:15] SIGNAL    ADANIPORTS 1800 CE 27 Oct crossed EMA 144 at 31.70 - not taken: momentum -3.1%
[14:50:15] SIGNAL    BEL 390 PE 27 Oct crossed EMA 144 at 9.95 - not taken: under EMA 55, momentum -1.0%
[14:50:15] SIGNAL    NTPC 320 PE 27 Oct crossed EMA 144 at 4.75 - not taken: under EMA 55, premium under Rs 5
[14:50:22] ENTRY     BUY ETERNAL 325 CE 27 Oct x2425 @ 12.55 (signal close 12.55, EMA 144 12.42, momentum 4.6%)  quick 14.43 till 15:20, target 21.34, stop below EMA 55
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:48:10] API       rate limited by Dhan - now one call every 15.1 s
[14:48:54] API       rate limited by Dhan - now one call every 15.1 s
[14:49:39] API       rate limited by Dhan - now one call every 15.1 s
[14:49:54] API       rate limited by Dhan - now one call every 15.1 s
[14:50:09] SIGNAL    2026-10-27 26000 CE VIX Fix crossed above 10.00 (10.00 -> 11.11, bar close 1.30)
[14:50:09] ENTRY     BUY 2026-10-27 26000 CE @ 1.40 x 65  (Rs 91) - buy 2 of 10, average 1.48, target 2.22
```
</details>

