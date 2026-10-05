# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:19 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹3,828 (+0.49%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,779 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹1,710 (+1.43%) | −₹11,956 (-2.08%) | 12 | 7 | ₹1,19,616 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,982 (-4.61%) | ₹0 | 0 | 7 | ₹1,08,105 |
| **Total** | | **+₹22,543** | **+₹556** | **+₹81,007** | **25** | **24** | **₹10,02,500** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:13:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:14:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:15:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:16:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:18:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:18:52] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:08:52] API       rate limited by Dhan - now one call every 15.1 s
[13:12:16] API       rate limited by Dhan - now one call every 15.1 s
[13:14:39] API       rate limited by Dhan - now one call every 15.1 s
[13:15:40] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:17:43] API       rate limited by Dhan - now one call every 15.1 s
[13:19:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:14:20] API       rate limited by Dhan - now one call every 15.1 s
[13:15:05] API       rate limited by Dhan - now one call every 15.1 s
[13:16:03] API       rate limited by Dhan - now one call every 15.1 s
[13:17:42] API       rate limited by Dhan - now one call every 15.1 s
[13:17:57] API       rate limited by Dhan - now one call every 15.1 s
[13:18:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:13:54] API       rate limited by Dhan - now one call every 5.1 s
[13:14:53] API       rate limited by Dhan - now one call every 5.1 s
[13:15:08] SIGNAL    2027-03-30 21000 CE MACD crossed UP (bar close 2319.05, hist -0.13 -> +0.22)
[13:15:08] SKIP      buy 2027-03-30 21000 CE ignored - premium 2319.05 is outside 144 - 1600
[13:15:52] API       rate limited by Dhan - now one call every 5.1 s
[13:16:51] API       rate limited by Dhan - now one call every 5.1 s
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
[13:10:09] WARM      bar history loaded for all 774 contracts
[13:10:50] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:11:50] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:14:40] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:15:04] SIGNAL    HDFCLIFE 520 PE 27 Oct crossed EMA 144 at 10.50 - not taken: under EMA 55, momentum -3.7%
[13:17:51] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:14:15] API       rate limited by Dhan - now one call every 15.1 s
[13:15:00] API       rate limited by Dhan - now one call every 15.1 s
[13:16:12] API       rate limited by Dhan - now one call every 15.1 s
[13:17:11] API       rate limited by Dhan - now one call every 15.1 s
[13:17:26] API       rate limited by Dhan - now one call every 15.1 s
[13:19:03] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

