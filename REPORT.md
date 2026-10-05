# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:29 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,968 (+3.66%) | +₹6,529 (+0.98%) | +₹69,407 (+2.29%) | 8 | 10 | ₹6,63,596 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹1,265 (+0.89%) | −₹11,956 (-2.08%) | 12 | 8 | ₹1,42,816 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,865 (-3.38%) | ₹0 | 0 | 7 | ₹1,43,744 |
| **Total** | | **+₹22,228** | **+₹2,929** | **+₹80,692** | **26** | **25** | **₹9,50,156** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:21:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:22:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:23:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:24:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:26:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:26:54] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:26:13] API       rate limited by Dhan - now one call every 15.1 s
[13:27:34] API       rate limited by Dhan - now one call every 15.1 s
[13:27:42] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:27:55] API       rate limited by Dhan - now one call every 15.1 s
[13:28:35] API       rate limited by Dhan - now one call every 15.1 s
[13:28:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:27:24] API       rate limited by Dhan - now one call every 15.1 s
[13:27:39] API       rate limited by Dhan - now one call every 15.1 s
[13:28:23] API       rate limited by Dhan - now one call every 15.1 s
[13:28:39] API       rate limited by Dhan - now one call every 15.1 s
[13:29:23] API       rate limited by Dhan - now one call every 15.1 s
[13:29:39] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:22:33] API       rate limited by Dhan - now one call every 5.1 s
[13:22:51] API       rate limited by Dhan - now one call every 5.1 s
[13:23:10] API       rate limited by Dhan - now one call every 5.1 s
[13:25:31] API       rate limited by Dhan - now one call every 5.1 s
[13:25:50] API       rate limited by Dhan - now one call every 5.1 s
[13:27:16] API       rate limited by Dhan - now one call every 5.1 s
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
[13:20:04] SKIP      KOTAKBANK 410 CE 27 Oct signal at 14.30 skipped - already 1 open on KOTAKBANK
[13:21:41] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:25:53] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:26:42] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:27:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:28:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:25:09] SIGNAL    2026-10-27 23000 PE VIX Fix crossed above 10.00 (9.80 -> 10.27, bar close 545.55)
[13:25:09] ENTRY     BUY 2026-10-27 23000 PE @ 548.30 x 65  (Rs 35,640) - buy 2 of 10, average 557.12, target 835.68
[13:26:36] API       rate limited by Dhan - now one call every 15.1 s
[13:26:51] API       rate limited by Dhan - now one call every 15.1 s
[13:27:36] API       rate limited by Dhan - now one call every 15.1 s
[13:29:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

