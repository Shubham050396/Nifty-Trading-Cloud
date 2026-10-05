# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:59 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.99 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | −₹608 (-1.96%) | +₹21,548 (+7.07%) | 4 | 2 | ₹30,946 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹7,381 (+0.95%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,73,935 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹8,020 (-5.89%) | −₹1,376 (-1.12%) | −₹8,109 (-1.66%) | 8 | 6 | ₹1,22,424 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,683 (-7.73%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹26,391** | **+₹714** | **+₹84,854** | **19** | **22** | **₹9,87,924** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:43:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:44:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:47:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:47:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:53:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:53:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:52:26] API       rate limited by Dhan - now one call every 15.1 s
[11:53:29] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:53:47] API       rate limited by Dhan - now one call every 15.1 s
[11:54:48] API       rate limited by Dhan - now one call every 15.1 s
[11:55:09] API       rate limited by Dhan - now one call every 15.1 s
[11:57:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:55:14] GAP       2026-10-06 23500 PE: no prices for 7 min - bar history restarts
[11:55:29] API       rate limited by Dhan - now one call every 15.1 s
[11:55:59] API       rate limited by Dhan - now one call every 15.1 s
[11:56:15] API       rate limited by Dhan - now one call every 15.1 s
[11:57:13] API       rate limited by Dhan - now one call every 15.1 s
[11:57:58] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:54:51] API       rate limited by Dhan - now one call every 15.1 s
[11:55:07] API       rate limited by Dhan - now one call every 15.1 s
[11:55:22] API       rate limited by Dhan - now one call every 15.1 s
[11:56:07] API       rate limited by Dhan - now one call every 15.1 s
[11:57:05] API       rate limited by Dhan - now one call every 15.1 s
[11:58:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:47:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:50:32] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:51:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:54:00] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:56:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:59:02] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:54:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:55:25] SKIP      COALINDIA 430 PE 27 Oct signal at 11.60 skipped - already 1 open on COALINDIA
[11:55:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:56:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:58:27] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:58:56] WARM      bar history loaded for all 762 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:56:56] API       rate limited by Dhan - now one call every 15.1 s
[11:57:41] API       rate limited by Dhan - now one call every 15.1 s
[11:57:56] API       rate limited by Dhan - now one call every 15.1 s
[11:58:12] API       rate limited by Dhan - now one call every 15.1 s
[11:58:27] API       rate limited by Dhan - now one call every 15.1 s
[11:58:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

