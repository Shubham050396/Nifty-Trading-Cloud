# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:03 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.41 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 (+0.00%) | +₹20,420 (+9.20%) | 0 | 1 | ₹22,536 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹49,150 (+8.69%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,65,788 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,650 (-34.21%) | +₹4,760 (+3.96%) | −₹12,739 (-3.28%) | 2 | 6 | ₹1,20,099 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹13 (-4.09%) | ₹0 | 0 | 1 | ₹318 |
| **Total** | | **−₹12,650** | **+₹53,897** | **+₹45,813** | **2** | **13** | **₹7,08,741** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 09:58:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:59:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:00:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:02:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:02:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:03:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:55:07] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:56:33] API       rate limited by Dhan - now one call every 15.1 s
[09:58:07] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:58:15] API       rate limited by Dhan - now one call every 15.1 s
[09:59:37] API       rate limited by Dhan - now one call every 15.1 s
[10:00:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:02:20] GAP       2026-10-19 23400 PE: no prices for 4 min - bar history restarts
[10:02:20] GAP       2026-10-19 22000 PE: no prices for 4 min - bar history restarts
[10:02:20] GAP       2026-10-19 22900 PE: no prices for 4 min - bar history restarts
[10:02:35] API       rate limited by Dhan - now one call every 15.1 s
[10:02:50] API       rate limited by Dhan - now one call every 15.1 s
[10:03:05] ENTRY     L3 BUY 2026-10-13 22900 PE @ 346.70  target 416.70  trail 312.03 (10%)
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:55:19] API       rate limited by Dhan - now one call every 15.1 s
[09:56:18] API       rate limited by Dhan - now one call every 15.1 s
[09:57:16] API       rate limited by Dhan - now one call every 15.1 s
[09:58:01] API       rate limited by Dhan - now one call every 15.1 s
[10:00:12] API       rate limited by Dhan - now one call every 15.1 s
[10:02:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 09:50:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:52:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:54:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:56:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:58:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:01:27] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:02:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:02:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:02:34] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:02:44] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:02:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:03:02] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:58:38] API       rate limited by Dhan - now one call every 15.1 s
[10:00:03] API       rate limited by Dhan - now one call every 15.1 s
[10:00:18] SIGNAL    2026-10-27 25000 CE VIX Fix crossed above 10.00 (9.82 -> 10.12, bar close 4.95)
[10:00:18] ENTRY     BUY 2026-10-27 25000 CE @ 4.90 x 65  (Rs 318) - buy 1 of 10, average 4.90, target 7.35
[10:01:52] API       rate limited by Dhan - now one call every 15.1 s
[10:02:36] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

