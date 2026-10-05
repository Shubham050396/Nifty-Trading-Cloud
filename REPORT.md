# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:04 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.01 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹7,163 (-0.72%) | +₹59,800 (+1.63%) | 17 | 10 | ₹9,98,876 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹15,138 (-5.68%) | −₹13,040 (-6.70%) | −₹15,226 (-2.46%) | 15 | 9 | ₹1,94,496 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹5,885 (-4.09%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹9,754** | **−₹26,088** | **+₹68,217** | **39** | **27** | **₹13,37,216** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:55:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:56:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:57:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:00:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:00:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:01:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:58:31] API       rate limited by Dhan - now one call every 15.1 s
[13:59:48] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:01:34] API       rate limited by Dhan - now one call every 15.1 s
[14:01:55] API       rate limited by Dhan - now one call every 15.1 s
[14:02:56] API       rate limited by Dhan - now one call every 15.1 s
[14:04:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:00:55] API       rate limited by Dhan - now one call every 15.1 s
[14:01:10] API       rate limited by Dhan - now one call every 15.1 s
[14:02:22] API       rate limited by Dhan - now one call every 15.1 s
[14:03:20] API       rate limited by Dhan - now one call every 15.1 s
[14:03:36] API       rate limited by Dhan - now one call every 15.1 s
[14:04:34] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:58:28] API       rate limited by Dhan - now one call every 15.1 s
[13:59:26] API       rate limited by Dhan - now one call every 15.1 s
[14:00:25] API       rate limited by Dhan - now one call every 15.1 s
[14:01:23] API       rate limited by Dhan - now one call every 15.1 s
[14:02:21] API       rate limited by Dhan - now one call every 15.1 s
[14:04:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 13:49:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:50:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:50:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:52:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:54:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:01:43] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:00:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:02:31] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:02:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:03:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:04:35] WARM      bar history loaded for all 784 contracts
[14:04:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:00:25] API       rate limited by Dhan - now one call every 15.1 s
[14:01:24] API       rate limited by Dhan - now one call every 15.1 s
[14:02:09] API       rate limited by Dhan - now one call every 15.1 s
[14:03:21] API       rate limited by Dhan - now one call every 15.1 s
[14:03:36] API       rate limited by Dhan - now one call every 15.1 s
[14:04:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

