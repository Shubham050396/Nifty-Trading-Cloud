# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:57 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹12,178 (-1.79%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,795 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹6,704 (+7.48%) | +₹7,884 (+6.39%) | −₹31,461 (-3.53%) | 6 | 8 | ₹1,23,431 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,650 (-8.70%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹6,704** | **−₹22,944** | **+₹64,488** | **6** | **22** | **₹10,19,604** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:51:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:52:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:55:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:55:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 09:56:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:57:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:52:57] API       rate limited by Dhan - now one call every 15.1 s
[09:54:18] API       rate limited by Dhan - now one call every 15.1 s
[09:54:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:54:39] API       rate limited by Dhan - now one call every 15.1 s
[09:55:40] API       rate limited by Dhan - now one call every 15.1 s
[09:57:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:57:04] GAP       2026-10-13 22000 PE: no prices for 4 min - bar history restarts
[09:57:04] GAP       2026-10-13 22900 PE: no prices for 4 min - bar history restarts
[09:57:04] GAP       2026-10-13 21500 CE: no prices for 4 min - bar history restarts
[09:57:04] GAP       2026-10-13 21500 PE: no prices for 4 min - bar history restarts
[09:57:04] GAP       2026-10-13 23700 CE: no prices for 4 min - bar history restarts
[09:57:04] GAP       2026-10-13 23700 PE: no prices for 4 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:49:12] API       rate limited by Dhan - now one call every 13.1 s
[09:49:25] API       rate limited by Dhan - now one call every 15.1 s
[09:51:46] API       rate limited by Dhan - now one call every 15.1 s
[09:54:52] API       rate limited by Dhan - now one call every 12.1 s
[09:56:40] API       rate limited by Dhan - now one call every 11.1 s
[09:56:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 09:47:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:49:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:51:29] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:53:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:55:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:57:10] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:55:15] SIGNAL    BRITANNIA 4800 PE 27 Oct crossed EMA 144 at 73.75 - not taken: under EMA 55
[09:55:24] WARM      bar history loaded for all 776 contracts
[09:55:44] WARM      bar history loaded for all 776 contracts
[09:56:27] API       market quote: rate limited by Dhan - now one call every 2.0 s
[09:56:36] API       market quote: rate limited by Dhan - now one call every 2.0 s
[09:56:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:53:24] API       rate limited by Dhan - now one call every 15.1 s
[09:53:39] API       rate limited by Dhan - now one call every 15.1 s
[09:53:55] API       rate limited by Dhan - now one call every 15.1 s
[09:54:10] API       rate limited by Dhan - now one call every 15.1 s
[09:55:47] API       rate limited by Dhan - now one call every 15.1 s
[09:57:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

