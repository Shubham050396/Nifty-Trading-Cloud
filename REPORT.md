# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:03 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.81 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹367 (+0.55%) | +₹1,814 (+11.42%) | +₹20,787 (+7.19%) | 3 | 1 | ₹15,883 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹35,877 (+6.35%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,690 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹5,169 (-5.50%) | −₹2,212 (-0.49%) | 6 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹1,878 (-3.11%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹1,757** | **+₹30,644** | **+₹56,707** | **9** | **15** | **₹7,34,938** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:59:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:59:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:00:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:01:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:03:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:03:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:01:47] API       rate limited by Dhan - now one call every 15.1 s
[11:02:07] API       rate limited by Dhan - now one call every 15.1 s
[11:02:18] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:02:28] API       rate limited by Dhan - now one call every 15.1 s
[11:02:48] API       rate limited by Dhan - now one call every 15.1 s
[11:03:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:58:52] EXIT      L3 2026-10-13 22800 PE PUSH_FAILED @ 334.00  P&L Rs 1001.00
[10:59:34] API       rate limited by Dhan - now one call every 15.1 s
[11:01:11] API       rate limited by Dhan - now one call every 15.1 s
[11:01:26] API       rate limited by Dhan - now one call every 15.1 s
[11:02:25] API       rate limited by Dhan - now one call every 15.1 s
[11:03:23] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:01:49] API       rate limited by Dhan - now one call every 5.1 s
[11:02:21] API       rate limited by Dhan - now one call every 5.1 s
[11:02:39] API       rate limited by Dhan - now one call every 5.1 s
[11:02:58] API       rate limited by Dhan - now one call every 5.1 s
[11:03:16] API       rate limited by Dhan - now one call every 5.1 s
[11:03:38] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:53:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:55:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:57:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:59:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:01:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:03:37] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:01:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:01:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:02:06] WARM      bar history loaded for all 750 contracts
[11:02:11] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:02:47] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:03:17] WARM      bar history loaded for all 750 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:54:37] API       rate limited by Dhan - now one call every 15.1 s
[10:55:35] API       rate limited by Dhan - now one call every 15.1 s
[10:57:36] API       rate limited by Dhan - now one call every 15.1 s
[10:59:25] API       rate limited by Dhan - now one call every 15.1 s
[10:59:55] API       rate limited by Dhan - now one call every 15.1 s
[11:00:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

