# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 09:58 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.41 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹20,420 (+9.20%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹59,121 (+10.43%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,66,622 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,650 (-34.21%) | +₹6,966 (+5.80%) | −₹12,739 (-3.28%) | 2 | 6 | ₹1,20,099 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **−₹12,650** | **+₹66,087** | **+₹45,813** | **2** | **11** | **₹6,86,721** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 09:54:00] VIX       India VIX 14.44 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-05 09:55:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:55:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 09:56:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:57:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:58:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:52:29] API       rate limited by Dhan - now one call every 15.1 s
[09:52:49] API       rate limited by Dhan - now one call every 15.1 s
[09:53:50] API       rate limited by Dhan - now one call every 15.1 s
[09:55:07] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:56:33] API       rate limited by Dhan - now one call every 15.1 s
[09:58:07] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:53:03] API       rate limited by Dhan - now one call every 15.1 s
[09:54:01] API       rate limited by Dhan - now one call every 15.1 s
[09:55:50] API       rate limited by Dhan - now one call every 15.1 s
[09:56:35] API       rate limited by Dhan - now one call every 15.1 s
[09:57:33] API       rate limited by Dhan - now one call every 15.1 s
[09:57:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:52:18] API       rate limited by Dhan - now one call every 15.1 s
[09:53:42] API       rate limited by Dhan - now one call every 15.1 s
[09:55:19] API       rate limited by Dhan - now one call every 15.1 s
[09:56:18] API       rate limited by Dhan - now one call every 15.1 s
[09:57:16] API       rate limited by Dhan - now one call every 15.1 s
[09:58:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 09:46:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:48:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:50:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:52:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:54:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 09:56:42] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:57:18] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:57:27] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:57:37] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:57:46] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:57:55] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:58:05] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:52:51] API       rate limited by Dhan - now one call every 15.1 s
[09:53:50] API       rate limited by Dhan - now one call every 15.1 s
[09:54:48] API       rate limited by Dhan - now one call every 15.1 s
[09:55:47] API       rate limited by Dhan - now one call every 15.1 s
[09:56:02] API       rate limited by Dhan - now one call every 15.1 s
[09:57:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

