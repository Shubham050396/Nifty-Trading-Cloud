# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:33 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.67 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹367 (+0.55%) | +₹842 (+5.30%) | +₹20,787 (+7.19%) | 3 | 1 | ₹15,883 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹30,082 (+4.04%) | +₹36,439 (+1.71%) | 0 | 7 | ₹7,45,013 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹6,274 (-5.75%) | −₹2,212 (-0.49%) | 6 | 6 | ₹1,09,151 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹601 (-0.99%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **−₹1,757** | **+₹24,049** | **+₹56,707** | **9** | **18** | **₹9,30,666** |

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
[11:29:19] API       rate limited by Dhan - now one call every 15.1 s
[11:30:41] API       rate limited by Dhan - now one call every 15.1 s
[11:31:02] API       rate limited by Dhan - now one call every 15.1 s
[11:32:03] API       rate limited by Dhan - now one call every 15.1 s
[11:33:24] API       rate limited by Dhan - now one call every 15.1 s
[11:33:26] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:29:45] API       rate limited by Dhan - now one call every 15.1 s
[11:30:44] API       rate limited by Dhan - now one call every 15.1 s
[11:31:14] API       rate limited by Dhan - now one call every 15.1 s
[11:31:44] API       rate limited by Dhan - now one call every 15.1 s
[11:32:42] API       rate limited by Dhan - now one call every 15.1 s
[11:33:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:30:07] SIGNAL    2026-11-23 23000 PE MACD crossed UP (bar close 598.00, hist -0.50 -> +0.08)
[11:30:07] ENTRY     BUY 2026-11-23 23000 PE @ 585.95  (bar close 598.00, MACD hist +0.08, VIX 14.46)
[11:30:50] API       rate limited by Dhan - now one call every 15.1 s
[11:31:49] API       rate limited by Dhan - now one call every 15.1 s
[11:32:47] API       rate limited by Dhan - now one call every 15.1 s
[11:33:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:18:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:21:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:23:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:25:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:26:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:31:57] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:30:10] SIGNAL    DLF 680 CE 27 Oct crossed EMA 144 at 15.90 - not taken: momentum 2.9%
[11:30:10] SIGNAL    KOTAKBANK 410 CE 27 Oct crossed EMA 144 at 14.45 - not taken: momentum -4.9%
[11:30:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:31:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:32:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:33:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:27:51] API       rate limited by Dhan - now one call every 15.1 s
[11:30:02] API       rate limited by Dhan - now one call every 15.1 s
[11:30:32] API       rate limited by Dhan - now one call every 15.1 s
[11:31:18] API       rate limited by Dhan - now one call every 15.1 s
[11:32:29] API       rate limited by Dhan - now one call every 15.1 s
[11:33:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

