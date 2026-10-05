# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:28 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.86 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹367 (+0.55%) | +₹2,824 (+17.78%) | +₹20,787 (+7.19%) | 3 | 1 | ₹15,883 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹31,434 (+4.45%) | +₹36,439 (+1.71%) | 0 | 6 | ₹7,05,986 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹6,306 (-5.78%) | −₹2,212 (-0.49%) | 6 | 6 | ₹1,09,151 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹2,886 (-4.76%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **−₹1,757** | **+₹25,066** | **+₹56,707** | **9** | **17** | **₹8,91,639** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:15:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:18:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:18:22] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:19:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:27:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:27:24] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:21:09] API       rate limited by Dhan - now one call every 15.1 s
[11:22:31] API       rate limited by Dhan - now one call every 15.1 s
[11:23:53] API       rate limited by Dhan - now one call every 15.1 s
[11:25:15] API       rate limited by Dhan - now one call every 15.1 s
[11:25:36] API       rate limited by Dhan - now one call every 15.1 s
[11:26:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:24:38] API       rate limited by Dhan - now one call every 15.1 s
[11:25:50] API       rate limited by Dhan - now one call every 15.1 s
[11:26:49] API       rate limited by Dhan - now one call every 15.1 s
[11:27:19] API       rate limited by Dhan - now one call every 15.1 s
[11:28:31] API       rate limited by Dhan - now one call every 15.1 s
[11:28:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:20:40] API       rate limited by Dhan - now one call every 15.1 s
[11:21:39] API       rate limited by Dhan - now one call every 15.1 s
[11:23:28] API       rate limited by Dhan - now one call every 15.1 s
[11:25:28] SIGNAL    2026-11-23 21000 CE MACD crossed DOWN (bar close 1720.00, hist +1.57 -> -0.29)
[11:25:28] SKIP      short 2026-11-23 21000 CE ignored - premium 1720.00 is outside 144 - 1600
[11:25:59] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:15:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:18:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:21:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:23:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:25:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:26:21] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:25:10] SIGNAL    INFY 1060 PE 27 Oct crossed EMA 144 at 61.15 - not taken: under EMA 55
[11:25:10] SIGNAL    HDFCLIFE 520 PE 27 Oct crossed EMA 144 at 11.00 - not taken: under EMA 55
[11:25:27] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:25:45] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:27:14] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:28:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:25:12] ENTRY     BUY 2026-10-27 25000 CE @ 4.70 x 65  (Rs 306) - buy 2 of 10, average 4.80, target 7.20
[11:25:27] API       rate limited by Dhan - now one call every 15.1 s
[11:27:05] API       rate limited by Dhan - now one call every 15.1 s
[11:27:20] API       rate limited by Dhan - now one call every 15.1 s
[11:27:35] API       rate limited by Dhan - now one call every 15.1 s
[11:27:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

