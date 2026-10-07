# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:22 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.72 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹318 (-0.52%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹4,066 (-0.52%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,205 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹10,911 (-5.44%) | +₹1,167 (+0.59%) | −₹49,076 (-4.89%) | 13 | 10 | ₹1,98,840 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,134 (-7.32%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹45,413** | **−₹19,351** | **+₹12,371** | **20** | **31** | **₹12,56,087** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:03:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:04:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:05:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:06:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:10:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:10:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:19:03] API       rate limited by Dhan - now one call every 15.1 s
[11:19:23] API       rate limited by Dhan - now one call every 15.1 s
[11:19:44] API       rate limited by Dhan - now one call every 15.1 s
[11:21:05] API       rate limited by Dhan - now one call every 15.1 s
[11:22:26] API       rate limited by Dhan - now one call every 15.1 s
[11:22:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:16:46] API       rate limited by Dhan - now one call every 15.1 s
[11:17:45] API       rate limited by Dhan - now one call every 15.1 s
[11:19:33] API       rate limited by Dhan - now one call every 15.1 s
[11:20:32] API       rate limited by Dhan - now one call every 15.1 s
[11:21:30] API       rate limited by Dhan - now one call every 15.1 s
[11:22:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:15:57] API       rate limited by Dhan - now one call every 15.1 s
[11:16:12] API       rate limited by Dhan - now one call every 15.1 s
[11:17:10] API       rate limited by Dhan - now one call every 15.1 s
[11:18:48] API       rate limited by Dhan - now one call every 15.1 s
[11:20:59] API       rate limited by Dhan - now one call every 15.1 s
[11:22:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:10:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:12:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:14:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:17:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:18:46] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:19:41] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:20:22] SIGNAL    HDFCBANK 700 PE 27 Oct crossed EMA 144 at 10.80 - not taken: under EMA 55
[11:20:22] SIGNAL    TMPV 280 PE 27 Oct crossed EMA 144 at 5.65 - not taken: under EMA 55, momentum -2.6%
[11:20:22] SIGNAL    TMPV 275 PE 27 Oct crossed EMA 144 at 3.80 - not taken: under EMA 55, momentum -6.2%, premium under Rs 5
[11:20:30] ENTRY     BUY ITC 262.5 CE 27 Oct x1725 @ 7.35 (signal close 7.70, EMA 144 7.15, momentum 10.8%)  quick 8.45 till 11:50, target 12.49, stop below EMA 55
[11:21:29] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:22:28] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:17:17] API       rate limited by Dhan - now one call every 15.1 s
[11:18:01] API       rate limited by Dhan - now one call every 15.1 s
[11:18:17] API       rate limited by Dhan - now one call every 15.1 s
[11:19:15] API       rate limited by Dhan - now one call every 15.1 s
[11:20:13] API       rate limited by Dhan - now one call every 15.1 s
[11:22:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

