# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:13 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.54 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | −₹84 (-0.22%) | +₹20,420 (+9.20%) | 0 | 2 | ₹38,418 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹48,610 (+8.59%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,65,720 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,650 (-34.21%) | +₹7,865 (+6.55%) | −₹12,739 (-3.28%) | 2 | 6 | ₹1,20,099 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹10 (-3.07%) | ₹0 | 0 | 1 | ₹318 |
| **Total** | | **−₹12,650** | **+₹56,381** | **+₹45,813** | **2** | **14** | **₹7,24,555** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:08:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:08:04] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:09:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:10:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:12:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:12:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:09:08] API       rate limited by Dhan - now one call every 15.1 s
[10:09:09] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:10:30] API       rate limited by Dhan - now one call every 15.1 s
[10:11:51] API       rate limited by Dhan - now one call every 15.1 s
[10:12:09] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:13:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:10:42] API       rate limited by Dhan - now one call every 15.1 s
[10:11:12] API       rate limited by Dhan - now one call every 15.1 s
[10:11:27] API       rate limited by Dhan - now one call every 15.1 s
[10:11:43] API       rate limited by Dhan - now one call every 15.1 s
[10:12:27] API       rate limited by Dhan - now one call every 15.1 s
[10:12:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:05:00] API       rate limited by Dhan - now one call every 13.1 s
[10:06:13] API       rate limited by Dhan - now one call every 15.1 s
[10:07:11] API       rate limited by Dhan - now one call every 15.1 s
[10:08:23] API       rate limited by Dhan - now one call every 15.1 s
[10:11:43] API       rate limited by Dhan - now one call every 10.1 s
[10:12:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:01:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:03:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:04:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:08:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:10:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:12:22] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:12:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:12:22] WARM      bar history loaded for all 700 contracts
[10:12:28] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:12:40] API       chart history: rate limited by Dhan - now one call every 1.2 s
[10:13:11] WARM      bar history loaded for all 702 contracts
[10:13:15] WARM      bar history loaded for all 704 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:08:30] API       rate limited by Dhan - now one call every 12.1 s
[10:08:43] API       rate limited by Dhan - now one call every 15.1 s
[10:09:41] API       rate limited by Dhan - now one call every 15.1 s
[10:10:11] API       rate limited by Dhan - now one call every 15.1 s
[10:10:42] API       rate limited by Dhan - now one call every 15.1 s
[10:12:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

