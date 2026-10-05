# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:04 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.07 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | +₹978 (+3.16%) | +₹21,548 (+7.07%) | 4 | 2 | ₹30,946 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹12,236 (+1.58%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,73,823 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹8,020 (-5.89%) | +₹426 (+0.30%) | −₹8,109 (-1.66%) | 8 | 7 | ₹1,40,821 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹5,106 (-8.42%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹26,391** | **+₹8,534** | **+₹84,854** | **19** | **23** | **₹10,06,209** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:47:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:47:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:53:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:53:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:03:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:03:33] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:54:48] API       rate limited by Dhan - now one call every 15.1 s
[11:55:09] API       rate limited by Dhan - now one call every 15.1 s
[11:57:31] API       rate limited by Dhan - now one call every 15.1 s
[12:01:36] API       rate limited by Dhan - now one call every 15.1 s
[12:01:56] API       rate limited by Dhan - now one call every 15.1 s
[12:03:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:03:56] GAP       2026-10-06 21400 CE: no prices for 4 min - bar history restarts
[12:03:56] GAP       2026-10-06 21400 PE: no prices for 4 min - bar history restarts
[12:03:56] GAP       2026-10-06 23600 CE: no prices for 4 min - bar history restarts
[12:03:56] GAP       2026-10-06 23500 CE: no prices for 4 min - bar history restarts
[12:03:56] GAP       2026-10-06 23600 PE: no prices for 4 min - bar history restarts
[12:03:56] GAP       2026-10-06 23500 PE: no prices for 4 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:59:15] API       rate limited by Dhan - now one call every 15.1 s
[12:00:27] API       rate limited by Dhan - now one call every 15.1 s
[12:02:05] API       rate limited by Dhan - now one call every 15.1 s
[12:02:20] API       rate limited by Dhan - now one call every 15.1 s
[12:03:04] API       rate limited by Dhan - now one call every 15.1 s
[12:03:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:51:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:54:00] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:56:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:59:02] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:02:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:04:00] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:00:33] ENTRY     BUY INDIGO 4900 PE 27 Oct x150 @ 122.65 (signal close 123.65, EMA 144 121.95, momentum 3.9%)  quick 141.05 till 12:30, target 208.50, stop below EMA 55
[12:00:47] WARM      bar history loaded for all 768 contracts
[12:01:33] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:02:33] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:03:35] WARM      bar history loaded for all 770 contracts
[12:04:04] WARM      bar history loaded for all 772 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:59:56] API       rate limited by Dhan - now one call every 15.1 s
[12:01:20] API       rate limited by Dhan - now one call every 15.1 s
[12:02:57] API       rate limited by Dhan - now one call every 15.1 s
[12:03:28] API       rate limited by Dhan - now one call every 15.1 s
[12:03:43] API       rate limited by Dhan - now one call every 15.1 s
[12:03:58] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

