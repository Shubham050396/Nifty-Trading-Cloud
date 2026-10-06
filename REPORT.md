# NIFTY Cloud report

**Running until 15:15 IST** · updated 06 Oct 2026 15:10 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **13.67 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹19,867 (+3.47%) | −₹40,514 (-5.92%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,84,296 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹10,790 (-12.22%) | +₹5,210 (+4.24%) | −₹38,165 (-4.76%) | 4 | 7 | ₹1,22,921 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,944 (-12.17%) | ₹0 | 0 | 8 | ₹1,55,606 |
| **Total** | | **+₹9,077** | **−₹54,248** | **+₹57,784** | **8** | **21** | **₹9,62,823** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 14:47:25] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:54:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:54:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:55:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 15:01:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 15:01:28] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:04:07] API       rate limited by Dhan - now one call every 15.1 s
[15:05:29] API       rate limited by Dhan - now one call every 15.1 s
[15:06:30] API       rate limited by Dhan - now one call every 15.1 s
[15:06:50] API       rate limited by Dhan - now one call every 15.1 s
[15:08:11] API       rate limited by Dhan - now one call every 15.1 s
[15:09:32] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:05:53] API       rate limited by Dhan - now one call every 15.1 s
[15:07:30] API       rate limited by Dhan - now one call every 15.1 s
[15:07:46] API       rate limited by Dhan - now one call every 15.1 s
[15:08:44] API       rate limited by Dhan - now one call every 15.1 s
[15:09:55] API       rate limited by Dhan - now one call every 15.1 s
[15:10:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[15:06:56] API       rate limited by Dhan - now one call every 5.1 s
[15:07:14] API       rate limited by Dhan - now one call every 5.1 s
[15:07:19] API       rate limited by Dhan - now one call every 7.1 s
[15:08:14] API       rate limited by Dhan - now one call every 5.1 s
[15:08:42] API       rate limited by Dhan - now one call every 5.1 s
[15:09:57] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 15:00:06] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:01:26] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:03:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:05:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:07:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:09:01] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:08:33] API       market quote: rate limited by Dhan - now one call every 8.6 s
[15:08:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:09:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:10:24] SIGNAL    JIOFIN 215 PE 27 Oct crossed EMA 144 at 4.55 - not taken: under EMA 55, momentum 0.4%, premium under Rs 5
[15:10:24] SIGNAL    TATAPOWER 350 PE 27 Oct crossed EMA 144 at 4.50 - not taken: under EMA 55, premium under Rs 5
[15:10:33] ENTRY     BUY VEDL 270 CE 27 Oct x1150 @ 6.50 (signal close 6.25, EMA 144 6.06, momentum 14.7%)  quick 7.47 till 15:40, target 11.05, stop below EMA 55
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[15:06:57] API       rate limited by Dhan - now one call every 15.1 s
[15:07:42] API       rate limited by Dhan - now one call every 15.1 s
[15:07:57] API       rate limited by Dhan - now one call every 15.1 s
[15:09:46] API       rate limited by Dhan - now one call every 15.1 s
[15:10:16] API       rate limited by Dhan - now one call every 15.1 s
[15:10:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

