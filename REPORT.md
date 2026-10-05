# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:18 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.86 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹367 (+0.55%) | +₹2,925 (+18.42%) | +₹20,787 (+7.19%) | 3 | 1 | ₹15,883 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹29,910 (+4.24%) | +₹36,439 (+1.71%) | 0 | 6 | ₹7,06,013 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹6,519 (-5.97%) | −₹2,212 (-0.49%) | 6 | 6 | ₹1,09,151 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹2,710 (-4.49%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹1,757** | **+₹23,606** | **+₹56,707** | **9** | **17** | **₹8,91,361** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:12:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:14:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:14:21] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:15:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:18:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:18:22] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:14:01] API       rate limited by Dhan - now one call every 15.1 s
[11:14:21] API       rate limited by Dhan - now one call every 15.1 s
[11:15:22] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:15:43] API       rate limited by Dhan - now one call every 15.1 s
[11:17:04] API       rate limited by Dhan - now one call every 15.1 s
[11:18:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:16:06] GAP       2026-10-06 23500 PE: no prices for 5 min - bar history restarts
[11:16:45] API       rate limited by Dhan - now one call every 15.1 s
[11:17:00] API       rate limited by Dhan - now one call every 15.1 s
[11:17:45] API       rate limited by Dhan - now one call every 15.1 s
[11:18:00] API       rate limited by Dhan - now one call every 15.1 s
[11:18:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:15:27] API       rate limited by Dhan - now one call every 15.1 s
[11:15:58] API       rate limited by Dhan - now one call every 15.1 s
[11:16:28] SIGNAL    2026-12-29 24000 CE MACD crossed DOWN (bar close 160.00, hist +0.03 -> -0.00)
[11:16:28] ENTRY     SELL SHORT 2026-12-29 24000 CE @ 158.25  (bar close 160.00, MACD hist -0.00, VIX 14.46)
[11:17:22] API       rate limited by Dhan - now one call every 15.1 s
[11:17:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:08:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:10:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:12:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:14:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:15:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:18:35] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:15:20] SIGNAL    TMPV 290 PE 27 Oct crossed EMA 144 at 10.35 - not taken: under EMA 55, momentum -11.2%
[11:15:29] ENTRY     BUY INDHOTEL 720 PE 27 Oct x1000 @ 15.10 (signal close 14.90, EMA 144 14.43, momentum 7.6%)  quick 17.36 till 11:45, target 25.67, stop below EMA 55
[11:15:46] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:15:55] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:17:26] WARM      bar history loaded for all 754 contracts
[11:17:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:10:27] API       rate limited by Dhan - now one call every 15.1 s
[11:12:04] API       rate limited by Dhan - now one call every 15.1 s
[11:12:48] API       rate limited by Dhan - now one call every 15.1 s
[11:14:13] API       rate limited by Dhan - now one call every 15.1 s
[11:15:12] API       rate limited by Dhan - now one call every 15.1 s
[11:18:01] API       rate limited by Dhan - now one call every 14.1 s
```
</details>

