# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:47 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹1,492 (-2.46%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹7,728 (-1.00%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,212 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,361 (-5.78%) | +₹6,895 (+3.38%) | −₹51,526 (-4.98%) | 15 | 10 | ₹2,03,879 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,051 (-7.71%) | ₹0 | 0 | 8 | ₹2,21,096 |
| **Total** | | **−₹47,863** | **−₹19,376** | **+₹9,921** | **22** | **31** | **₹12,61,897** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:42:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:44:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:44:33] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:46:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:46:34] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:47:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:43:47] API       rate limited by Dhan - now one call every 15.1 s
[11:44:07] API       rate limited by Dhan - now one call every 15.1 s
[11:45:29] API       rate limited by Dhan - now one call every 15.1 s
[11:46:10] API       rate limited by Dhan - now one call every 15.1 s
[11:46:50] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:46:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:45:10] API       rate limited by Dhan - now one call every 15.1 s
[11:45:26] API       rate limited by Dhan - now one call every 15.1 s
[11:45:41] API       rate limited by Dhan - now one call every 15.1 s
[11:45:56] API       rate limited by Dhan - now one call every 15.1 s
[11:47:21] API       rate limited by Dhan - now one call every 15.1 s
[11:47:36] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:39:22] API       rate limited by Dhan - now one call every 15.1 s
[11:39:52] API       rate limited by Dhan - now one call every 15.1 s
[11:41:17] API       rate limited by Dhan - now one call every 15.1 s
[11:44:22] API       rate limited by Dhan - now one call every 12.1 s
[11:45:47] API       rate limited by Dhan - now one call every 14.1 s
[11:47:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:39:09] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:41:08] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:42:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:44:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:46:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:47:53] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:45:08] SIGNAL    PFC 320 PE 27 Oct crossed EMA 144 at 5.00 - not taken: under EMA 55, premium under Rs 5
[11:45:08] EXIT      SELL ITC 262.5 CE 27 Oct EMA_STOP @ 6.60  -10.2%  P&L Rs -1293.75
[11:45:18] ENTRY     BUY LODHA 1120 PE 27 Oct x625 @ 36.20 (signal close 36.10, EMA 144 35.13, momentum 13.9%)  quick 41.63 till 12:15, target 61.54, stop below EMA 55
[11:45:18] SKIP      DLF 670 PE 27 Oct signal at 24.70 skipped - 10 positions already open
[11:46:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:47:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:43:36] API       rate limited by Dhan - now one call every 15.1 s
[11:44:48] API       rate limited by Dhan - now one call every 15.1 s
[11:46:12] API       rate limited by Dhan - now one call every 15.1 s
[11:46:43] API       rate limited by Dhan - now one call every 15.1 s
[11:46:58] API       rate limited by Dhan - now one call every 15.1 s
[11:47:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

