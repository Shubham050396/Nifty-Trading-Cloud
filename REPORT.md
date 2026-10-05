# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:13 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.85 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹367 (+0.55%) | +₹1,670 (+10.52%) | +₹20,787 (+7.19%) | 3 | 1 | ₹15,883 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹35,659 (+6.32%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,629 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹5,385 (-5.73%) | −₹2,212 (-0.49%) | 6 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹1,160 (-1.92%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹1,757** | **+₹30,784** | **+₹56,707** | **9** | **15** | **₹7,34,877** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:07:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:08:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:09:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:10:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:11:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:12:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:10:17] API       rate limited by Dhan - now one call every 15.1 s
[11:10:37] API       rate limited by Dhan - now one call every 15.1 s
[11:11:38] API       rate limited by Dhan - now one call every 15.1 s
[11:13:00] API       rate limited by Dhan - now one call every 15.1 s
[11:13:21] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:13:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:10:04] GAP       2026-10-27 21500 PE: no prices for 6 min - bar history restarts
[11:10:17] API       rate limited by Dhan - now one call every 15.1 s
[11:11:54] API       rate limited by Dhan - now one call every 15.1 s
[11:12:10] API       rate limited by Dhan - now one call every 15.1 s
[11:13:08] API       rate limited by Dhan - now one call every 15.1 s
[11:13:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:05:00] API       rate limited by Dhan - now one call every 11.1 s
[11:05:34] API       rate limited by Dhan - now one call every 15.1 s
[11:07:45] API       rate limited by Dhan - now one call every 15.1 s
[11:09:56] API       rate limited by Dhan - now one call every 15.1 s
[11:13:17] API       rate limited by Dhan - now one call every 10.1 s
[11:13:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:01:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:03:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:05:15] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:08:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:10:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:12:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:09:56] WARM      bar history loaded for all 752 contracts
[11:10:45] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:11:45] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:12:14] WARM      bar history loaded for all 752 contracts
[11:12:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:13:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:05:53] API       rate limited by Dhan - now one call every 15.1 s
[11:08:05] API       rate limited by Dhan - now one call every 15.1 s
[11:09:42] API       rate limited by Dhan - now one call every 15.1 s
[11:10:27] API       rate limited by Dhan - now one call every 15.1 s
[11:12:04] API       rate limited by Dhan - now one call every 15.1 s
[11:12:48] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

