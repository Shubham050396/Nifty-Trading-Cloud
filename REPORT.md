# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:08 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.84 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹367 (+0.55%) | +₹2,012 (+12.67%) | +₹20,787 (+7.19%) | 3 | 1 | ₹15,883 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹35,984 (+6.37%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,617 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹6,236 (-6.63%) | −₹2,212 (-0.49%) | 6 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹1,830 (-3.03%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹1,757** | **+₹29,930** | **+₹56,707** | **9** | **15** | **₹7,34,865** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:03:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:04:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:05:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:07:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:07:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:08:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:06:32] API       rate limited by Dhan - now one call every 15.1 s
[11:06:53] API       rate limited by Dhan - now one call every 15.1 s
[11:07:34] API       rate limited by Dhan - now one call every 15.1 s
[11:07:54] API       rate limited by Dhan - now one call every 15.1 s
[11:08:14] API       rate limited by Dhan - now one call every 15.1 s
[11:08:35] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:06:06] API       rate limited by Dhan - now one call every 15.1 s
[11:06:21] API       rate limited by Dhan - now one call every 15.1 s
[11:06:51] API       rate limited by Dhan - now one call every 15.1 s
[11:07:07] API       rate limited by Dhan - now one call every 15.1 s
[11:08:05] API       rate limited by Dhan - now one call every 15.1 s
[11:08:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:03:38] API       rate limited by Dhan - now one call every 5.1 s
[11:03:43] API       rate limited by Dhan - now one call every 7.1 s
[11:03:58] API       rate limited by Dhan - now one call every 10.1 s
[11:05:00] API       rate limited by Dhan - now one call every 11.1 s
[11:05:34] API       rate limited by Dhan - now one call every 15.1 s
[11:07:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:57:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:59:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:01:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:03:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:05:15] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:08:40] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:05:14] SIGNAL    BAJFINANCE 1000 PE 27 Oct crossed EMA 144 at 34.60 - not taken: under EMA 55
[11:05:14] SIGNAL    COALINDIA 435 CE 27 Oct crossed EMA 144 at 6.00 - not taken: momentum -9.8%
[11:05:46] WARM      bar history loaded for all 752 contracts
[11:05:53] API       market quote: rate limited by Dhan - now one call every 8.1 s
[11:06:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:07:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:04:08] API       rate limited by Dhan - now one call every 6.1 s
[11:04:20] API       rate limited by Dhan - now one call every 8.1 s
[11:04:28] API       rate limited by Dhan - now one call every 13.1 s
[11:05:08] API       rate limited by Dhan - now one call every 15.1 s
[11:05:53] API       rate limited by Dhan - now one call every 15.1 s
[11:08:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

