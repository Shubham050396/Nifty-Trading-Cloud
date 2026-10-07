# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:32 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.72 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹3,204 (-5.28%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹13,098 (-1.69%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,75,686 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,068 (-5.53%) | +₹3,996 (+2.06%) | −₹50,232 (-4.92%) | 14 | 10 | ₹1,93,932 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,065 (-8.20%) | ₹0 | 0 | 8 | ₹2,20,397 |
| **Total** | | **−₹46,570** | **−₹30,371** | **+₹11,215** | **21** | **31** | **₹12,50,725** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:23:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:23:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:29:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:29:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:32:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:32:31] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:27:11] API       rate limited by Dhan - now one call every 15.1 s
[11:29:33] API       rate limited by Dhan - now one call every 15.1 s
[11:29:53] API       rate limited by Dhan - now one call every 15.1 s
[11:31:56] API       rate limited by Dhan - now one call every 15.1 s
[11:32:16] API       rate limited by Dhan - now one call every 15.1 s
[11:32:36] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:28:34] API       rate limited by Dhan - now one call every 15.1 s
[11:29:19] API       rate limited by Dhan - now one call every 15.1 s
[11:30:03] API       rate limited by Dhan - now one call every 15.1 s
[11:31:01] API       rate limited by Dhan - now one call every 15.1 s
[11:32:00] API       rate limited by Dhan - now one call every 15.1 s
[11:32:30] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:25:35] API       rate limited by Dhan - now one call every 15.1 s
[11:25:50] SIGNAL    2026-11-23 24000 CE MACD crossed UP (bar close 66.80, hist -0.03 -> +0.00)
[11:25:50] SKIP      buy 2026-11-23 24000 CE ignored - premium 66.80 is outside 144 - 1600
[11:28:15] API       rate limited by Dhan - now one call every 15.1 s
[11:29:52] API       rate limited by Dhan - now one call every 15.1 s
[11:31:29] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:19:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:24:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:26:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:28:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:30:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:31:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:30:25] SIGNAL    SOLARINDS 20000 CE 27 Oct crossed EMA 144 at 642.25 - not taken: momentum -1.2%
[11:30:25] SIGNAL    SBILIFE 1760 PE 27 Oct crossed EMA 144 at 56.00 - not taken: under EMA 55, momentum -7.4%
[11:30:33] ENTRY     BUY DLF 650 PE 27 Oct x950 @ 13.65 (signal close 13.60, EMA 144 13.36, momentum 11.0%)  quick 15.70 till 12:00, target 23.20, stop below EMA 55
[11:31:47] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:31:57] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:32:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:27:41] API       rate limited by Dhan - now one call every 15.1 s
[11:27:56] API       rate limited by Dhan - now one call every 15.1 s
[11:28:55] API       rate limited by Dhan - now one call every 15.1 s
[11:29:53] API       rate limited by Dhan - now one call every 15.1 s
[11:30:52] API       rate limited by Dhan - now one call every 15.1 s
[11:32:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

