# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:45 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.91 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | +₹26 (+0.00%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,892 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,624 (-7.36%) | −₹5,521 (-3.49%) | −₹23,712 (-3.52%) | 17 | 8 | ₹1,58,174 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹7,270 (-5.05%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,268** | **−₹12,765** | **+₹59,731** | **41** | **26** | **₹13,02,910** |

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
[14:41:00] API       rate limited by Dhan - now one call every 15.1 s
[14:41:55] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:42:22] API       rate limited by Dhan - now one call every 15.1 s
[14:44:03] API       rate limited by Dhan - now one call every 15.1 s
[14:44:55] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:45:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:39:47] API       rate limited by Dhan - now one call every 15.1 s
[14:41:26] VIX       India VIX prev close 14.46 -> target 1000 ticks (Rs 50.00)
[14:42:18] API       rate limited by Dhan - now one call every 15.1 s
[14:43:17] API       rate limited by Dhan - now one call every 15.1 s
[14:44:15] API       rate limited by Dhan - now one call every 15.1 s
[14:45:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:40:32] VIX       India VIX prev close 14.46 - entries allowed
[14:41:36] API       rate limited by Dhan - now one call every 15.1 s
[14:41:52] API       rate limited by Dhan - now one call every 15.1 s
[14:43:52] API       rate limited by Dhan - now one call every 15.1 s
[14:44:07] API       rate limited by Dhan - now one call every 15.1 s
[14:44:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:29:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:30:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:33:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:40:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:42:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:44:15] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:40:32] SIGNAL    ETERNAL 315 PE 27 Oct crossed EMA 144 at 7.55 - not taken: under EMA 55, momentum 2.0%
[14:41:55] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:42:13] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:43:13] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:43:40] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:45:02] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:42:34] API       rate limited by Dhan - now one call every 15.1 s
[14:43:04] API       rate limited by Dhan - now one call every 15.1 s
[14:43:19] API       rate limited by Dhan - now one call every 15.1 s
[14:44:04] API       rate limited by Dhan - now one call every 15.1 s
[14:45:02] API       rate limited by Dhan - now one call every 15.1 s
[14:45:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

