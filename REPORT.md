# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:18 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.52 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹260 (+0.68%) | +₹20,420 (+9.20%) | 0 | 2 | ₹38,418 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹46,442 (+8.21%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,65,745 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,650 (-34.21%) | +₹6,515 (+4.92%) | −₹12,739 (-3.28%) | 2 | 7 | ₹1,32,416 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | +₹214 (+1.90%) | ₹0 | 0 | 3 | ₹11,313 |
| **Total** | | **−₹12,650** | **+₹53,431** | **+₹45,813** | **2** | **17** | **₹7,47,892** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:12:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:12:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:15:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:15:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:16:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:17:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:12:09] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:13:13] API       rate limited by Dhan - now one call every 15.1 s
[10:14:34] API       rate limited by Dhan - now one call every 15.1 s
[10:15:36] API       rate limited by Dhan - now one call every 15.1 s
[10:15:56] API       rate limited by Dhan - now one call every 15.1 s
[10:17:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:14:55] API       rate limited by Dhan - now one call every 15.1 s
[10:15:39] API       rate limited by Dhan - now one call every 15.1 s
[10:16:24] API       rate limited by Dhan - now one call every 15.1 s
[10:16:39] API       rate limited by Dhan - now one call every 15.1 s
[10:17:38] API       rate limited by Dhan - now one call every 15.1 s
[10:17:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:14:44] API       rate limited by Dhan - now one call every 15.1 s
[10:15:43] API       rate limited by Dhan - now one call every 15.1 s
[10:15:58] API       rate limited by Dhan - now one call every 15.1 s
[10:16:13] API       rate limited by Dhan - now one call every 15.1 s
[10:16:58] API       rate limited by Dhan - now one call every 15.1 s
[10:17:43] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:10:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:12:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:14:00] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:16:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:17:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:17:54] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:15:20] ENTRY     BUY HDFCBANK 720 PE 27 Oct x650 @ 18.95 (signal close 18.70, EMA 144 17.22, momentum 39.6%)  quick 21.79 till 10:45, target 32.21, stop below EMA 55
[10:15:20] SKIP      HDFCBANK 710 PE 27 Oct signal at 14.00 skipped - already 1 open on HDFCBANK
[10:15:20] SKIP      HDFCBANK 730 PE 27 Oct signal at 24.35 skipped - already 1 open on HDFCBANK
[10:15:30] WARM      bar history loaded for all 710 contracts
[10:15:47] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:17:46] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:15:19] SIGNAL    2026-10-27 24000 CE VIX Fix crossed above 10.00 (9.12 -> 10.39, bar close 16.30)
[10:15:19] ENTRY     BUY 2026-10-27 24000 CE @ 16.25 x 65  (Rs 1,056) - buy 1 of 10, average 16.25, target 24.38
[10:15:19] SIGNAL    2026-10-27 23000 CE VIX Fix crossed above 10.00 (9.57 -> 10.94, bar close 153.90)
[10:15:19] ENTRY     BUY 2026-10-27 23000 CE @ 152.90 x 65  (Rs 9,938) - buy 1 of 10, average 152.90, target 229.35
[10:15:48] API       rate limited by Dhan - now one call every 15.1 s
[10:16:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

