# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:40 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.90 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹1,024 (-0.10%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,424 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,624 (-7.36%) | −₹7,856 (-4.97%) | −₹23,712 (-3.52%) | 17 | 8 | ₹1,58,174 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6,961 (-4.84%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,268** | **−₹15,841** | **+₹59,731** | **41** | **26** | **₹13,02,442** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:27:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:27:09] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:32:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:32:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:39:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:39:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:32:50] API       rate limited by Dhan - now one call every 15.1 s
[14:33:31] API       rate limited by Dhan - now one call every 15.1 s
[14:34:12] API       rate limited by Dhan - now one call every 15.1 s
[14:37:15] API       rate limited by Dhan - now one call every 15.1 s
[14:37:56] API       rate limited by Dhan - now one call every 15.1 s
[14:39:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:37:54] GAP       2026-10-06 23500 CE: no prices for 5 min - bar history restarts
[14:37:54] GAP       2026-10-06 23600 PE: no prices for 5 min - bar history restarts
[14:37:54] GAP       2026-10-06 23500 PE: no prices for 5 min - bar history restarts
[14:38:33] API       rate limited by Dhan - now one call every 15.1 s
[14:38:48] API       rate limited by Dhan - now one call every 15.1 s
[14:39:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:34:44] API       rate limited by Dhan - now one call every 15.1 s
[14:35:15] API       rate limited by Dhan - now one call every 15.1 s
[14:35:30] API       rate limited by Dhan - now one call every 15.1 s
[14:36:55] API       rate limited by Dhan - now one call every 15.1 s
[14:39:45] API       rate limited by Dhan - now one call every 14.1 s
[14:39:59] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:26:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:27:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:28:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:29:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:30:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:33:33] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:35:14] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:36:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:37:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:38:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:39:29] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:40:13] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:36:45] API       rate limited by Dhan - now one call every 15.1 s
[14:37:30] API       rate limited by Dhan - now one call every 15.1 s
[14:37:45] API       rate limited by Dhan - now one call every 15.1 s
[14:38:32] VIX       India VIX prev close 14.46
[14:39:34] API       rate limited by Dhan - now one call every 15.1 s
[14:40:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

