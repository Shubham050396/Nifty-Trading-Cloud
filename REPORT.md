# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:58 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.84 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹634 (-1.37%) | +₹2,870 (+7.84%) | +₹19,786 (+7.37%) | 2 | 2 | ₹36,592 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹35,545 (+6.29%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,683 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹4,039 (-4.29%) | −₹2,212 (-0.49%) | 6 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹1,940 (-3.22%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹2,758** | **+₹32,436** | **+₹55,706** | **8** | **16** | **₹7,55,640** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:51:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:52:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:53:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:54:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:55:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:56:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:53:58] API       rate limited by Dhan - now one call every 15.1 s
[10:56:21] API       rate limited by Dhan - now one call every 15.1 s
[10:56:42] API       rate limited by Dhan - now one call every 15.1 s
[10:57:02] API       rate limited by Dhan - now one call every 15.1 s
[10:58:03] API       rate limited by Dhan - now one call every 15.1 s
[10:58:23] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:55:39] API       rate limited by Dhan - now one call every 15.1 s
[10:56:37] API       rate limited by Dhan - now one call every 15.1 s
[10:56:53] SIGNAL    2026-10-13 22800 PE held above 338.60 for 5 min - fall-back exit is armed
[10:57:22] API       rate limited by Dhan - now one call every 15.1 s
[10:57:37] API       rate limited by Dhan - now one call every 15.1 s
[10:58:22] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:50:55] SKIP      short 2026-11-23 24000 CE ignored - premium 68.85 is outside 144 - 1600
[10:52:02] API       rate limited by Dhan - now one call every 15.1 s
[10:53:26] API       rate limited by Dhan - now one call every 15.1 s
[10:54:25] API       rate limited by Dhan - now one call every 15.1 s
[10:55:24] API       rate limited by Dhan - now one call every 15.1 s
[10:56:22] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:46:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:48:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:51:00] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:53:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:55:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:57:23] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:55:10] SIGNAL    BAJFINANCE 1000 PE 27 Oct crossed EMA 144 at 34.80 - not taken: under EMA 55
[10:55:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:56:03] WARM      bar history loaded for all 744 contracts
[10:56:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:57:21] WARM      bar history loaded for all 744 contracts
[10:57:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:52:38] API       rate limited by Dhan - now one call every 15.1 s
[10:52:53] API       rate limited by Dhan - now one call every 15.1 s
[10:53:38] API       rate limited by Dhan - now one call every 15.1 s
[10:54:37] API       rate limited by Dhan - now one call every 15.1 s
[10:55:35] API       rate limited by Dhan - now one call every 15.1 s
[10:57:36] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

