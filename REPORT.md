# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:10 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.02 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹8,122 (-0.81%) | +₹59,800 (+1.63%) | 17 | 10 | ₹9,99,570 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,624 (-7.36%) | −₹5,582 (-3.99%) | −₹23,712 (-3.52%) | 17 | 7 | ₹1,39,799 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6,285 (-4.37%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,268** | **−₹19,989** | **+₹59,731** | **41** | **25** | **₹12,83,213** |

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
[14:02:56] API       rate limited by Dhan - now one call every 15.1 s
[14:04:17] API       rate limited by Dhan - now one call every 15.1 s
[14:05:39] API       rate limited by Dhan - now one call every 15.1 s
[14:06:49] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:08:22] API       rate limited by Dhan - now one call every 15.1 s
[14:09:50] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:07:29] API       rate limited by Dhan - now one call every 15.1 s
[14:07:44] SKIP      L3 2026-10-13 22800 PE cross ignored - daily cap
[14:08:27] API       rate limited by Dhan - now one call every 15.1 s
[14:08:43] API       rate limited by Dhan - now one call every 15.1 s
[14:09:27] API       rate limited by Dhan - now one call every 15.1 s
[14:09:43] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:02:21] API       rate limited by Dhan - now one call every 15.1 s
[14:04:53] API       rate limited by Dhan - now one call every 15.1 s
[14:05:51] API       rate limited by Dhan - now one call every 15.1 s
[14:06:50] API       rate limited by Dhan - now one call every 15.1 s
[14:07:48] API       rate limited by Dhan - now one call every 15.1 s
[14:08:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 13:52:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:54:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:01:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:05:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:09:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:09:52] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:06:18] WARM      bar history loaded for all 784 contracts
[14:07:04] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:07:56] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:08:56] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:09:05] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:09:51] WARM      bar history loaded for all 784 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:06:05] API       rate limited by Dhan - now one call every 15.1 s
[14:07:17] API       rate limited by Dhan - now one call every 15.1 s
[14:08:02] API       rate limited by Dhan - now one call every 15.1 s
[14:09:01] API       rate limited by Dhan - now one call every 15.1 s
[14:09:16] API       rate limited by Dhan - now one call every 15.1 s
[14:09:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

