# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:48 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.82 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹634 (-1.37%) | +₹3,055 (+8.35%) | +₹19,786 (+7.37%) | 2 | 2 | ₹36,592 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹31,350 (+5.55%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,500 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹4,948 (-5.26%) | −₹2,212 (-0.49%) | 6 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹2,613 (-4.33%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹2,758** | **+₹26,844** | **+₹55,706** | **8** | **16** | **₹7,55,457** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:32:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:32:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:34:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:34:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:37:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:37:11] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:42:13] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:42:46] API       rate limited by Dhan - now one call every 15.1 s
[10:44:28] API       rate limited by Dhan - now one call every 15.1 s
[10:45:49] API       rate limited by Dhan - now one call every 15.1 s
[10:46:30] API       rate limited by Dhan - now one call every 15.1 s
[10:47:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:44:49] API       rate limited by Dhan - now one call every 15.1 s
[10:45:05] SIGNAL    2026-10-13 22700 PE held above 264.35 for 5 min - fall-back exit is armed
[10:45:48] API       rate limited by Dhan - now one call every 15.1 s
[10:46:32] API       rate limited by Dhan - now one call every 15.1 s
[10:46:48] API       rate limited by Dhan - now one call every 15.1 s
[10:47:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:45:57] API       rate limited by Dhan - now one call every 15.1 s
[10:46:12] API       rate limited by Dhan - now one call every 15.1 s
[10:46:27] API       rate limited by Dhan - now one call every 15.1 s
[10:46:43] API       rate limited by Dhan - now one call every 15.1 s
[10:47:55] API       rate limited by Dhan - now one call every 15.1 s
[10:48:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:36:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:38:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:40:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:41:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:45:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:46:58] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:45:25] SIGNAL    TMPV 280 PE 27 Oct crossed EMA 144 at 5.95 - not taken: under EMA 55, momentum -20.1%
[10:45:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:46:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:47:00] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:47:12] WARM      bar history loaded for all 738 contracts
[10:47:36] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:45:45] API       rate limited by Dhan - now one call every 15.1 s
[10:46:57] API       rate limited by Dhan - now one call every 15.1 s
[10:47:12] API       rate limited by Dhan - now one call every 15.1 s
[10:47:27] API       rate limited by Dhan - now one call every 15.1 s
[10:47:43] API       rate limited by Dhan - now one call every 15.1 s
[10:48:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

