# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:02 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.12 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹10,602 (-1.56%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,540 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹6,704 (+7.48%) | +₹4,046 (+3.01%) | −₹31,461 (-3.53%) | 6 | 9 | ₹1,34,212 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹19,212 (-8.96%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹6,704** | **−₹25,768** | **+₹64,488** | **6** | **23** | **₹10,30,130** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:52:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:55:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:55:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 09:56:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:57:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:58:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:59:31] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:59:44] API       rate limited by Dhan - now one call every 15.1 s
[10:00:45] API       rate limited by Dhan - now one call every 15.1 s
[10:01:05] API       rate limited by Dhan - now one call every 15.1 s
[10:01:32] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:01:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:58:58] API       rate limited by Dhan - now one call every 15.1 s
[09:59:56] API       rate limited by Dhan - now one call every 15.1 s
[10:00:27] API       rate limited by Dhan - now one call every 15.1 s
[10:00:57] API       rate limited by Dhan - now one call every 15.1 s
[10:01:27] API       rate limited by Dhan - now one call every 15.1 s
[10:01:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:57:37] API       rate limited by Dhan - now one call every 15.1 s
[09:57:52] API       rate limited by Dhan - now one call every 15.1 s
[09:59:29] API       rate limited by Dhan - now one call every 15.1 s
[09:59:44] API       rate limited by Dhan - now one call every 15.1 s
[10:00:29] API       rate limited by Dhan - now one call every 15.1 s
[10:01:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 09:51:29] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:53:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:55:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:57:10] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:59:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:01:07] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:00:10] API       market quote: rate limited by Dhan - now one call every 3.0 s
[10:00:19] API       market quote: rate limited by Dhan - now one call every 4.0 s
[10:00:28] API       market quote: rate limited by Dhan - now one call every 6.5 s
[10:02:01] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:02:10] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:02:12] API       market quote: rate limited by Dhan - now one call every 3.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:55:47] API       rate limited by Dhan - now one call every 15.1 s
[09:57:12] API       rate limited by Dhan - now one call every 15.1 s
[09:57:42] API       rate limited by Dhan - now one call every 15.1 s
[09:59:30] API       rate limited by Dhan - now one call every 15.1 s
[10:00:55] API       rate limited by Dhan - now one call every 15.1 s
[10:01:56] VIX       India VIX prev close 13.61
```
</details>

