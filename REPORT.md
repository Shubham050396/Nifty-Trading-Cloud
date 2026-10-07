# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:49 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.73 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹43,192 (-1.74%) | −₹6,896 (-0.77%) | +₹29,114 (+0.41%) | 26 | 10 | ₹8,95,526 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,420 (-4.18%) | +₹18,461 (+12.19%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹24,909 (-10.25%) | ₹0 | 0 | 8 | ₹2,42,932 |
| **Total** | | **−₹54,730** | **−₹13,344** | **+₹3,053** | **51** | **26** | **₹12,89,866** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 14:44:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:45:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:46:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:47:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:48:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:49:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:43:04] API       rate limited by Dhan - now one call every 15.1 s
[14:43:52] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:44:25] API       rate limited by Dhan - now one call every 15.1 s
[14:47:08] API       rate limited by Dhan - now one call every 15.1 s
[14:48:29] API       rate limited by Dhan - now one call every 15.1 s
[14:48:56] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:44:53] API       rate limited by Dhan - now one call every 15.1 s
[14:46:18] API       rate limited by Dhan - now one call every 15.1 s
[14:46:48] API       rate limited by Dhan - now one call every 15.1 s
[14:47:46] API       rate limited by Dhan - now one call every 15.1 s
[14:48:16] API       rate limited by Dhan - now one call every 15.1 s
[14:49:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:45:52] SIGNAL    2027-03-30 24000 PE MACD crossed DOWN (bar close 1112.75, hist +0.30 -> -0.39)
[14:45:52] EXIT      LONG 2027-03-30 24000 PE MACD_DOWN @ 1102.65  P&L Rs 692.25
[14:45:52] ENTRY     SELL SHORT 2027-03-30 24000 PE @ 1102.65  (bar close 1112.75, MACD hist -0.39, VIX 13.61)
[14:46:20] API       rate limited by Dhan - now one call every 15.1 s
[14:48:08] API       rate limited by Dhan - now one call every 15.1 s
[14:48:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:37:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:39:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:42:08] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:43:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:45:26] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:47:29] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:42:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:44:33] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:45:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:46:13] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:47:34] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:48:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:43:41] API       rate limited by Dhan - now one call every 15.1 s
[14:43:56] API       rate limited by Dhan - now one call every 15.1 s
[14:44:11] API       rate limited by Dhan - now one call every 15.1 s
[14:46:22] API       rate limited by Dhan - now one call every 15.1 s
[14:47:07] API       rate limited by Dhan - now one call every 15.1 s
[14:47:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

