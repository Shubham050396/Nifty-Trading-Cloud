# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:42 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.77 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹793 (-3.45%) | +₹20,280 (+5.68%) | 1 | 1 | ₹22,987 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹23,195 (-3.40%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,82,953 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | +₹4,867 (+2.89%) | −₹45,941 (-4.70%) | 12 | 8 | ₹1,68,286 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,474 (-8.38%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹9,044** | **−₹37,595** | **+₹48,740** | **13** | **23** | **₹10,94,558** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:32:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:32:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:35:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:35:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:39:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:39:20] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:37:01] API       rate limited by Dhan - now one call every 15.1 s
[10:39:03] API       rate limited by Dhan - now one call every 15.1 s
[10:40:25] API       rate limited by Dhan - now one call every 15.1 s
[10:41:05] API       rate limited by Dhan - now one call every 15.1 s
[10:41:46] API       rate limited by Dhan - now one call every 15.1 s
[10:41:59] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:40:46] GAP       2026-10-13 21500 PE: no prices for 8 min - bar history restarts
[10:40:46] GAP       2026-10-13 23700 CE: no prices for 8 min - bar history restarts
[10:40:46] GAP       2026-10-13 23700 PE: no prices for 8 min - bar history restarts
[10:41:13] API       rate limited by Dhan - now one call every 15.1 s
[10:41:28] API       rate limited by Dhan - now one call every 15.1 s
[10:42:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:38:47] API       rate limited by Dhan - now one call every 7.1 s
[10:39:42] API       rate limited by Dhan - now one call every 5.1 s
[10:40:43] API       rate limited by Dhan - now one call every 5.1 s
[10:41:25] API       rate limited by Dhan - now one call every 5.1 s
[10:42:07] API       rate limited by Dhan - now one call every 5.1 s
[10:42:29] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:31:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:33:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:35:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:37:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:39:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:42:07] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:40:09] SIGNAL    WIPRO 157.5 PE 27 Oct crossed EMA 144 at 3.48 - not taken: under EMA 55, premium under Rs 5
[10:40:09] SIGNAL    RECLTD 310 PE 27 Oct crossed EMA 144 at 14.35 - not taken: under EMA 55
[10:40:17] ENTRY     BUY ADANIPOWER 200 PE 27 Oct x3550 @ 6.25 (signal close 6.18, EMA 144 5.68, momentum 18.8%)  quick 7.19 till 11:10, target 10.62, stop below EMA 55
[10:41:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:42:12] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:42:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:37:24] API       rate limited by Dhan - now one call every 15.1 s
[10:37:39] API       rate limited by Dhan - now one call every 15.1 s
[10:38:24] API       rate limited by Dhan - now one call every 15.1 s
[10:39:08] API       rate limited by Dhan - now one call every 15.1 s
[10:40:21] API       rate limited by Dhan - now one call every 15.1 s
[10:41:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

