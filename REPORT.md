# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:34 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,984 (+3.17%) | +₹4,050 (+0.70%) | +₹69,423 (+2.19%) | 9 | 10 | ₹5,80,233 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹1,540 (+1.08%) | −₹11,956 (-2.08%) | 12 | 8 | ₹1,42,816 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹5,677 (-3.95%) | ₹0 | 0 | 7 | ₹1,43,744 |
| **Total** | | **+₹22,244** | **−₹87** | **+₹80,708** | **27** | **25** | **₹8,66,793** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:29:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:29:54] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:30:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:32:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:32:55] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:33:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:30:17] API       rate limited by Dhan - now one call every 15.1 s
[13:31:39] API       rate limited by Dhan - now one call every 15.1 s
[13:32:40] API       rate limited by Dhan - now one call every 15.1 s
[13:33:00] API       rate limited by Dhan - now one call every 15.1 s
[13:34:01] API       rate limited by Dhan - now one call every 15.1 s
[13:34:22] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:30:23] GAP       2026-10-27 21500 PE: no prices for 5 min - bar history restarts
[13:30:23] GAP       2026-10-27 21400 CE: no prices for 5 min - bar history restarts
[13:30:23] GAP       2026-10-27 21400 PE: no prices for 5 min - bar history restarts
[13:30:37] API       rate limited by Dhan - now one call every 15.1 s
[13:32:26] API       rate limited by Dhan - now one call every 15.1 s
[13:33:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:27:16] API       rate limited by Dhan - now one call every 5.1 s
[13:30:07] SIGNAL    2026-11-23 22000 CE MACD crossed UP (bar close 901.00, hist -0.04 -> +0.29)
[13:30:07] EXIT      SHORT 2026-11-23 22000 CE MACD_UP @ 892.20  P&L Rs 16.25
[13:30:07] ENTRY     BUY 2026-11-23 22000 CE @ 892.20  (bar close 901.00, MACD hist +0.29, VIX 14.46)
[13:31:11] API       rate limited by Dhan - now one call every 5.1 s
[13:34:26] API       rate limited by Dhan - now one call every 5.1 s
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
[13:25:53] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:26:42] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:27:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:28:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:30:02] SIGNAL    TMPV 290 PE 27 Oct crossed EMA 144 at 10.30 - not taken: under EMA 55
[13:31:55] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:27:36] API       rate limited by Dhan - now one call every 15.1 s
[13:29:25] API       rate limited by Dhan - now one call every 15.1 s
[13:30:24] API       rate limited by Dhan - now one call every 15.1 s
[13:31:22] API       rate limited by Dhan - now one call every 15.1 s
[13:33:11] API       rate limited by Dhan - now one call every 15.1 s
[13:34:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

