# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:08 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.41 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | −₹16 (-0.04%) | +₹20,420 (+9.20%) | 0 | 2 | ₹38,418 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹47,850 (+8.46%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,65,616 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,650 (-34.21%) | +₹6,780 (+5.65%) | −₹12,739 (-3.28%) | 2 | 6 | ₹1,20,099 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6 (-2.04%) | ₹0 | 0 | 1 | ₹318 |
| **Total** | | **−₹12,650** | **+₹54,608** | **+₹45,813** | **2** | **14** | **₹7,24,451** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:03:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:04:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:05:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:06:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:08:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:08:04] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:04:43] API       rate limited by Dhan - now one call every 15.1 s
[10:06:09] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:06:25] API       rate limited by Dhan - now one call every 15.1 s
[10:07:06] API       rate limited by Dhan - now one call every 15.1 s
[10:07:26] API       rate limited by Dhan - now one call every 15.1 s
[10:07:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:03:51] API       rate limited by Dhan - now one call every 15.1 s
[10:04:49] API       rate limited by Dhan - now one call every 15.1 s
[10:05:48] API       rate limited by Dhan - now one call every 15.1 s
[10:06:03] ENTRY     L2 BUY 2026-10-13 22700 PE @ 244.35  target 314.35  trail 207.70 (15%)
[10:06:46] API       rate limited by Dhan - now one call every 15.1 s
[10:07:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:58:01] API       rate limited by Dhan - now one call every 15.1 s
[10:00:12] API       rate limited by Dhan - now one call every 15.1 s
[10:02:01] API       rate limited by Dhan - now one call every 15.1 s
[10:05:00] API       rate limited by Dhan - now one call every 13.1 s
[10:06:13] API       rate limited by Dhan - now one call every 15.1 s
[10:07:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 09:54:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:56:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:58:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:01:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:03:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:04:43] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:07:23] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:07:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:07:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:07:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:08:00] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:08:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:00:18] SIGNAL    2026-10-27 25000 CE VIX Fix crossed above 10.00 (9.82 -> 10.12, bar close 4.95)
[10:00:18] ENTRY     BUY 2026-10-27 25000 CE @ 4.90 x 65  (Rs 318) - buy 1 of 10, average 4.90, target 7.35
[10:01:52] API       rate limited by Dhan - now one call every 15.1 s
[10:02:36] API       rate limited by Dhan - now one call every 15.1 s
[10:04:26] API       rate limited by Dhan - now one call every 15.1 s
[10:05:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

