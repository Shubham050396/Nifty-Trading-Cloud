# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:20 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.92 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹3,747 (-0.37%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,879 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,624 (-7.36%) | −₹5,152 (-3.26%) | −₹23,712 (-3.52%) | 17 | 8 | ₹1,58,174 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6,701 (-4.66%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,268** | **−₹15,600** | **+₹59,731** | **41** | **26** | **₹13,02,897** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:57:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:00:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:00:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:01:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:12:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:12:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:15:51] API       rate limited by Dhan - now one call every 15.1 s
[14:16:31] API       rate limited by Dhan - now one call every 15.1 s
[14:17:53] API       rate limited by Dhan - now one call every 15.1 s
[14:19:14] API       rate limited by Dhan - now one call every 15.1 s
[14:19:35] API       rate limited by Dhan - now one call every 15.1 s
[14:19:51] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:16:18] API       rate limited by Dhan - now one call every 15.1 s
[14:16:48] API       rate limited by Dhan - now one call every 15.1 s
[14:17:18] API       rate limited by Dhan - now one call every 15.1 s
[14:18:03] API       rate limited by Dhan - now one call every 15.1 s
[14:18:18] API       rate limited by Dhan - now one call every 15.1 s
[14:19:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:12:00] API       rate limited by Dhan - now one call every 11.1 s
[14:13:31] API       rate limited by Dhan - now one call every 10.1 s
[14:13:52] API       rate limited by Dhan - now one call every 15.1 s
[14:16:13] API       rate limited by Dhan - now one call every 15.1 s
[14:19:19] API       rate limited by Dhan - now one call every 12.1 s
[14:20:06] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:05:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:09:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:09:52] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:12:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:14:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:17:19] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:15:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:16:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:17:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:18:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:19:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:19:30] WARM      bar history loaded for all 791 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:15:38] API       rate limited by Dhan - now one call every 15.1 s
[14:16:22] API       rate limited by Dhan - now one call every 15.1 s
[14:17:34] API       rate limited by Dhan - now one call every 15.1 s
[14:18:05] API       rate limited by Dhan - now one call every 15.1 s
[14:19:03] API       rate limited by Dhan - now one call every 15.1 s
[14:20:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

