# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:30 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.99 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | +₹3,744 (+0.37%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,964 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,624 (-7.36%) | −₹5,255 (-3.32%) | −₹23,712 (-3.52%) | 17 | 8 | ₹1,58,174 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹7,153 (-4.97%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,268** | **−₹8,664** | **+₹59,731** | **41** | **26** | **₹13,02,982** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:22:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:22:07] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:24:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:24:08] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:27:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:27:09] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:25:52] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:26:03] API       rate limited by Dhan - now one call every 15.1 s
[14:26:43] API       rate limited by Dhan - now one call every 15.1 s
[14:27:24] API       rate limited by Dhan - now one call every 15.1 s
[14:28:25] API       rate limited by Dhan - now one call every 15.1 s
[14:28:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:26:25] API       rate limited by Dhan - now one call every 15.1 s
[14:27:10] API       rate limited by Dhan - now one call every 15.1 s
[14:27:40] API       rate limited by Dhan - now one call every 15.1 s
[14:28:10] API       rate limited by Dhan - now one call every 15.1 s
[14:29:47] API       rate limited by Dhan - now one call every 15.1 s
[14:30:03] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:22:03] API       rate limited by Dhan - now one call every 15.1 s
[14:22:18] API       rate limited by Dhan - now one call every 15.1 s
[14:23:55] API       rate limited by Dhan - now one call every 15.1 s
[14:25:44] API       rate limited by Dhan - now one call every 15.1 s
[14:28:16] API       rate limited by Dhan - now one call every 15.1 s
[14:29:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:25:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:26:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:26:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:27:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:28:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:29:30] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:25:46] WARM      bar history loaded for all 791 contracts
[14:26:40] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:26:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:26:59] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:27:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:29:46] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:25:16] API       rate limited by Dhan - now one call every 15.1 s
[14:26:01] API       rate limited by Dhan - now one call every 15.1 s
[14:27:00] API       rate limited by Dhan - now one call every 15.1 s
[14:27:44] API       rate limited by Dhan - now one call every 15.1 s
[14:28:56] API       rate limited by Dhan - now one call every 15.1 s
[14:29:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

