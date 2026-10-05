# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:09 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹6,107 (+0.79%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,367 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹914 (+0.76%) | −₹11,956 (-2.08%) | 12 | 7 | ₹1,19,616 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,495 (-4.16%) | ₹0 | 0 | 7 | ₹1,08,105 |
| **Total** | | **+₹22,543** | **+₹2,526** | **+₹81,007** | **25** | **24** | **₹10,02,088** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:01:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:02:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:04:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:04:48] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:06:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:06:49] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:06:50] API       rate limited by Dhan - now one call every 15.1 s
[13:07:10] API       rate limited by Dhan - now one call every 15.1 s
[13:08:11] API       rate limited by Dhan - now one call every 15.1 s
[13:08:32] API       rate limited by Dhan - now one call every 15.1 s
[13:08:39] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:08:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:04:29] API       rate limited by Dhan - now one call every 15.1 s
[13:04:45] API       rate limited by Dhan - now one call every 15.1 s
[13:05:43] API       rate limited by Dhan - now one call every 15.1 s
[13:07:20] API       rate limited by Dhan - now one call every 15.1 s
[13:07:36] API       rate limited by Dhan - now one call every 15.1 s
[13:08:34] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:03:37] API       rate limited by Dhan - now one call every 5.1 s
[13:03:56] API       rate limited by Dhan - now one call every 5.1 s
[13:05:08] SIGNAL    2026-10-27 23000 CE MACD crossed UP (bar close 141.80, hist -0.11 -> +0.05)
[13:05:08] SKIP      buy 2026-10-27 23000 CE ignored - premium 141.80 is outside 144 - 1600
[13:06:30] API       rate limited by Dhan - now one call every 5.1 s
[13:08:23] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:42:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:44:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:47:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:48:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:50:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:52:43] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:03:48] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:05:01] SIGNAL    TCS 2140 PE 27 Oct crossed EMA 144 at 93.80 - not taken: under EMA 55, momentum 0.1%
[13:05:48] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:07:39] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:07:49] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:08:49] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:03:26] API       rate limited by Dhan - now one call every 15.1 s
[13:05:37] API       rate limited by Dhan - now one call every 15.1 s
[13:06:49] API       rate limited by Dhan - now one call every 15.1 s
[13:07:04] API       rate limited by Dhan - now one call every 15.1 s
[13:08:42] API       rate limited by Dhan - now one call every 15.1 s
[13:08:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

