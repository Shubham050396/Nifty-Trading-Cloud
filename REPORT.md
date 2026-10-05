# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:14 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹6,412 (+0.83%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,390 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹1,056 (+0.88%) | −₹11,956 (-2.08%) | 12 | 7 | ₹1,19,616 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,940 (-4.57%) | ₹0 | 0 | 7 | ₹1,08,105 |
| **Total** | | **+₹22,543** | **+₹2,528** | **+₹81,007** | **25** | **24** | **₹10,02,111** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:06:49] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:09:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:09:49] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:12:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:12:50] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:13:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:07:10] API       rate limited by Dhan - now one call every 15.1 s
[13:08:11] API       rate limited by Dhan - now one call every 15.1 s
[13:08:32] API       rate limited by Dhan - now one call every 15.1 s
[13:08:39] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:08:52] API       rate limited by Dhan - now one call every 15.1 s
[13:12:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:08:34] API       rate limited by Dhan - now one call every 15.1 s
[13:10:56] API       rate limited by Dhan - now one call every 15.1 s
[13:11:55] API       rate limited by Dhan - now one call every 15.1 s
[13:12:10] API       rate limited by Dhan - now one call every 15.1 s
[13:13:08] API       rate limited by Dhan - now one call every 15.1 s
[13:14:20] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:06:30] API       rate limited by Dhan - now one call every 5.1 s
[13:08:23] API       rate limited by Dhan - now one call every 5.1 s
[13:09:36] API       rate limited by Dhan - now one call every 5.1 s
[13:11:43] API       rate limited by Dhan - now one call every 5.1 s
[13:12:55] API       rate limited by Dhan - now one call every 5.1 s
[13:13:54] API       rate limited by Dhan - now one call every 5.1 s
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
[13:10:03] SIGNAL    TMPV 285 PE 27 Oct crossed EMA 144 at 7.00 - not taken: under EMA 55, momentum -2.8%
[13:10:03] SIGNAL    TCS 2120 PE 27 Oct crossed EMA 144 at 82.65 - not taken: under EMA 55, momentum 3.4%
[13:10:03] SIGNAL    INDHOTEL 720 PE 27 Oct crossed EMA 144 at 14.95 - not taken: momentum 0.3%
[13:10:09] WARM      bar history loaded for all 774 contracts
[13:10:50] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:11:50] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:10:11] API       rate limited by Dhan - now one call every 15.1 s
[13:10:55] API       rate limited by Dhan - now one call every 15.1 s
[13:12:44] API       rate limited by Dhan - now one call every 15.1 s
[13:13:15] API       rate limited by Dhan - now one call every 15.1 s
[13:13:30] API       rate limited by Dhan - now one call every 15.1 s
[13:14:15] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

