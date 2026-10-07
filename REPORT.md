# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:07 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.12 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹11,440 (-1.68%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,847 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹6,272 (+6.25%) | +₹1,700 (+1.05%) | −₹31,892 (-3.53%) | 7 | 10 | ₹1,61,201 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,435 (-8.60%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹6,272** | **−₹28,175** | **+₹64,057** | **7** | **24** | **₹10,57,426** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:55:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 09:56:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:57:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:58:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:03:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:03:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:03:48] API       rate limited by Dhan - now one call every 15.1 s
[10:04:28] API       rate limited by Dhan - now one call every 15.1 s
[10:04:34] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:05:09] API       rate limited by Dhan - now one call every 15.1 s
[10:06:30] API       rate limited by Dhan - now one call every 15.1 s
[10:07:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:05:56] GAP       2026-10-13 22900 PE: no prices for 7 min - bar history restarts
[10:05:56] GAP       2026-10-13 21500 CE: no prices for 7 min - bar history restarts
[10:05:56] GAP       2026-10-13 21500 PE: no prices for 7 min - bar history restarts
[10:05:56] GAP       2026-10-13 23700 CE: no prices for 7 min - bar history restarts
[10:05:56] GAP       2026-10-13 23700 PE: no prices for 7 min - bar history restarts
[10:06:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:01:27] API       rate limited by Dhan - now one call every 15.1 s
[10:02:14] VIX       India VIX prev close 13.61 - entries allowed
[10:04:33] API       rate limited by Dhan - now one call every 12.1 s
[10:04:57] API       rate limited by Dhan - now one call every 15.1 s
[10:05:27] API       rate limited by Dhan - now one call every 15.1 s
[10:06:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 09:59:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:01:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:02:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:03:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:04:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:06:03] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:05:14] EXIT      SELL ITC 267.5 PE 27 Oct EMA_STOP @ 6.00  -4.0%  P&L Rs -431.25
[10:05:14] SIGNAL    PFC 320 PE 27 Oct crossed EMA 144 at 4.95 - not taken: under EMA 55, momentum -18.9%, premium under Rs 5
[10:05:14] SIGNAL    DABUR 380 CE 27 Oct crossed EMA 144 at 12.00 - not taken: momentum -9.1%
[10:05:22] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:05:22] ENTRY     BUY ADANIPORTS 1760 PE 27 Oct x475 @ 34.00 (signal close 34.00, EMA 144 32.06, momentum 26.2%)  quick 39.10 till 10:35, target 57.80, stop below EMA 55
[10:05:22] ENTRY     BUY ADANIPOWER 200 PE 27 Oct x3550 @ 6.09 (signal close 6.09, EMA 144 5.68, momentum 20.6%)  quick 7.00 till 10:35, target 10.35, stop below EMA 55
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:01:56] VIX       India VIX prev close 13.61
[10:02:32] API       rate limited by Dhan - now one call every 15.1 s
[10:03:17] API       rate limited by Dhan - now one call every 15.1 s
[10:04:01] API       rate limited by Dhan - now one call every 15.1 s
[10:05:50] API       rate limited by Dhan - now one call every 15.1 s
[10:07:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

