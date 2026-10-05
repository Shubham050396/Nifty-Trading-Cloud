# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:59 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | +₹3,760 (+0.38%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,499 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,125 (-5.58%) | −₹7,365 (-3.54%) | −₹14,214 (-2.35%) | 14 | 10 | ₹2,07,996 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹8,622 (-6.00%) | ₹0 | 0 | 7 | ₹1,43,744 |
| **Total** | | **+₹10,767** | **−₹12,227** | **+₹69,229** | **38** | **27** | **₹13,52,239** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:49:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:49:59] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:55:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:55:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:56:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:57:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:54:26] API       rate limited by Dhan - now one call every 15.1 s
[13:54:46] API       rate limited by Dhan - now one call every 15.1 s
[13:56:08] API       rate limited by Dhan - now one call every 15.1 s
[13:57:29] API       rate limited by Dhan - now one call every 15.1 s
[13:58:31] API       rate limited by Dhan - now one call every 15.1 s
[13:59:48] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:56:41] API       rate limited by Dhan - now one call every 15.1 s
[13:57:39] API       rate limited by Dhan - now one call every 15.1 s
[13:58:09] API       rate limited by Dhan - now one call every 15.1 s
[13:58:40] API       rate limited by Dhan - now one call every 15.1 s
[13:59:38] API       rate limited by Dhan - now one call every 15.1 s
[13:59:54] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:50:01] SKIP      buy 2026-11-23 21000 CE ignored - premium 1815.20 is outside 144 - 1600
[13:52:18] API       rate limited by Dhan - now one call every 15.1 s
[13:54:07] API       rate limited by Dhan - now one call every 15.1 s
[13:55:56] API       rate limited by Dhan - now one call every 15.1 s
[13:58:28] API       rate limited by Dhan - now one call every 15.1 s
[13:59:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 13:47:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:49:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:50:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:50:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:52:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:54:45] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:56:48] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:57:48] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:58:48] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:58:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:59:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:59:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:55:21] SIGNAL    2026-10-27 24000 PE VIX Fix crossed above 10.00 (9.76 -> 10.85, bar close 1330.00)
[13:55:21] SKIP      buy 2026-10-27 24000 PE ignored - premium 1330.00 is outside 0 - 1000
[13:55:51] API       rate limited by Dhan - now one call every 15.1 s
[13:56:49] API       rate limited by Dhan - now one call every 15.1 s
[13:57:04] API       rate limited by Dhan - now one call every 15.1 s
[13:59:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

