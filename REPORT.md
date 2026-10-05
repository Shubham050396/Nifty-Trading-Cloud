# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:24 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,968 (+3.66%) | +₹3,806 (+0.57%) | +₹69,407 (+2.29%) | 8 | 10 | ₹6,63,803 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹1,678 (+1.17%) | −₹11,956 (-2.08%) | 12 | 8 | ₹1,42,816 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹5,310 (-4.91%) | ₹0 | 0 | 7 | ₹1,08,105 |
| **Total** | | **+₹22,228** | **+₹174** | **+₹80,692** | **26** | **25** | **₹9,14,724** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:18:52] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:19:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:20:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:21:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:22:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:23:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:19:24] API       rate limited by Dhan - now one call every 15.1 s
[13:20:46] API       rate limited by Dhan - now one call every 15.1 s
[13:21:47] API       rate limited by Dhan - now one call every 15.1 s
[13:22:08] API       rate limited by Dhan - now one call every 15.1 s
[13:22:41] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:23:29] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:21:33] API       rate limited by Dhan - now one call every 15.1 s
[13:21:48] API       rate limited by Dhan - now one call every 15.1 s
[13:22:47] API       rate limited by Dhan - now one call every 15.1 s
[13:23:31] API       rate limited by Dhan - now one call every 15.1 s
[13:23:46] API       rate limited by Dhan - now one call every 15.1 s
[13:24:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:20:06] EXIT      SHORT 2026-12-29 23000 CE MACD_UP @ 473.40  P&L Rs -315.25
[13:20:06] ENTRY     BUY 2026-12-29 23000 CE @ 473.40  (bar close 473.15, MACD hist +0.06, VIX 14.46)
[13:20:27] API       rate limited by Dhan - now one call every 5.1 s
[13:22:33] API       rate limited by Dhan - now one call every 5.1 s
[13:22:51] API       rate limited by Dhan - now one call every 5.1 s
[13:23:10] API       rate limited by Dhan - now one call every 5.1 s
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
[13:17:51] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:20:03] SIGNAL    TMPV 285 PE 27 Oct crossed EMA 144 at 7.10 - not taken: under EMA 55
[13:20:04] ENTRY     BUY KOTAKBANK 415 CE 27 Oct x2000 @ 11.60 (signal close 11.50, EMA 144 11.33, momentum 5.5%)  quick 13.34 till 13:50, target 19.72, stop below EMA 55
[13:20:04] SKIP      KOTAKBANK 420 CE 27 Oct signal at 8.90 skipped - already 1 open on KOTAKBANK
[13:20:04] SKIP      KOTAKBANK 410 CE 27 Oct signal at 14.30 skipped - already 1 open on KOTAKBANK
[13:21:41] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:17:26] API       rate limited by Dhan - now one call every 15.1 s
[13:19:03] API       rate limited by Dhan - now one call every 15.1 s
[13:20:02] API       rate limited by Dhan - now one call every 15.1 s
[13:20:46] API       rate limited by Dhan - now one call every 15.1 s
[13:22:35] API       rate limited by Dhan - now one call every 15.1 s
[13:24:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

