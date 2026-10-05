# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:33 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.64 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,313 (+5.83%) | −₹3,438 (-5.69%) | +₹21,733 (+8.89%) | 1 | 3 | ₹60,463 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹44,327 (+7.84%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,65,239 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹1,468 (-1.60%) | −₹4,211 (-3.96%) | −₹1,556 (-0.35%) | 5 | 6 | ₹1,06,445 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹218 (-1.92%) | ₹0 | 0 | 3 | ₹11,313 |
| **Total** | | **−₹155** | **+₹36,460** | **+₹58,309** | **6** | **17** | **₹7,43,460** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:24:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:24:08] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:30:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:30:09] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:32:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:32:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:28:09] API       rate limited by Dhan - now one call every 15.1 s
[10:28:50] API       rate limited by Dhan - now one call every 15.1 s
[10:30:53] API       rate limited by Dhan - now one call every 15.1 s
[10:32:14] API       rate limited by Dhan - now one call every 15.1 s
[10:32:34] API       rate limited by Dhan - now one call every 15.1 s
[10:33:15] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:29:32] SIGNAL    2026-10-13 22900 PE held above 366.70 for 5 min - fall-back exit is armed
[10:30:16] API       rate limited by Dhan - now one call every 15.1 s
[10:31:14] API       rate limited by Dhan - now one call every 15.1 s
[10:31:44] API       rate limited by Dhan - now one call every 15.1 s
[10:32:29] EXIT      L3 2026-10-13 22900 PE TRAIL_STOP @ 366.90  P&L Rs 1313.00
[10:33:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:29:55] API       rate limited by Dhan - now one call every 15.1 s
[10:30:53] API       rate limited by Dhan - now one call every 15.1 s
[10:31:08] API       rate limited by Dhan - now one call every 15.1 s
[10:32:33] API       rate limited by Dhan - now one call every 15.1 s
[10:32:48] API       rate limited by Dhan - now one call every 15.1 s
[10:33:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:19:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:21:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:22:26] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:25:29] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:29:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:33:04] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:29:10] WARM      bar history loaded for all 736 contracts
[10:29:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:30:26] ENTRY     BUY SBILIFE 1700 PE 27 Oct x375 @ 33.05 (signal close 35.00, EMA 144 33.48, momentum 22.0%)  quick 38.01 till 11:00, target 56.18, stop below EMA 55
[10:32:13] API       market quote: rate limited by Dhan - now one call every 6.0 s
[10:32:34] WARM      bar history loaded for all 736 contracts
[10:33:12] API       market quote: rate limited by Dhan - now one call every 5.5 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:29:21] API       rate limited by Dhan - now one call every 15.1 s
[10:29:37] API       rate limited by Dhan - now one call every 15.1 s
[10:30:07] API       rate limited by Dhan - now one call every 15.1 s
[10:31:05] API       rate limited by Dhan - now one call every 15.1 s
[10:32:04] API       rate limited by Dhan - now one call every 15.1 s
[10:33:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

