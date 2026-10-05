# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:38 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.64 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹634 (-1.37%) | +₹1,820 (+4.97%) | +₹19,786 (+7.37%) | 2 | 2 | ₹36,592 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹41,662 (+7.38%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,856 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹3,906 (-4.15%) | −₹2,212 (-0.49%) | 6 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹1,514 (-2.51%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹2,758** | **+₹38,062** | **+₹55,706** | **8** | **16** | **₹7,55,813** |

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
[10:33:35] API       rate limited by Dhan - now one call every 15.1 s
[10:34:57] API       rate limited by Dhan - now one call every 15.1 s
[10:35:38] API       rate limited by Dhan - now one call every 15.1 s
[10:35:58] API       rate limited by Dhan - now one call every 15.1 s
[10:36:19] API       rate limited by Dhan - now one call every 15.1 s
[10:37:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:33:40] EXIT      L3 2026-10-19 22800 PE TRAIL_STOP @ 337.30  P&L Rs -1946.75
[10:34:08] API       rate limited by Dhan - now one call every 15.1 s
[10:35:06] API       rate limited by Dhan - now one call every 15.1 s
[10:36:05] API       rate limited by Dhan - now one call every 15.1 s
[10:37:03] API       rate limited by Dhan - now one call every 15.1 s
[10:38:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:34:46] API       rate limited by Dhan - now one call every 15.1 s
[10:35:58] API       rate limited by Dhan - now one call every 15.1 s
[10:36:28] API       rate limited by Dhan - now one call every 15.1 s
[10:37:26] API       rate limited by Dhan - now one call every 15.1 s
[10:37:56] API       rate limited by Dhan - now one call every 15.1 s
[10:38:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:21:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:22:26] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:25:29] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:29:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:33:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:36:37] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:35:13] SIGNAL    WIPRO 165 CE 27 Oct crossed EMA 144 at 4.66 - not taken: momentum -7.5%, premium under Rs 5
[10:35:13] EXIT      SELL SBILIFE 1700 PE 27 Oct EMA_STOP @ 31.30  -5.3%  P&L Rs -656.25
[10:35:40] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:36:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:37:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:38:01] WARM      bar history loaded for all 736 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:35:17] API       rate limited by Dhan - now one call every 15.1 s
[10:35:32] SIGNAL    2026-10-27 22000 CE VIX Fix crossed above 10.00 (9.61 -> 10.12, bar close 762.15)
[10:35:32] ENTRY     BUY 2026-10-27 22000 CE @ 753.85 x 65  (Rs 49,000) - buy 1 of 10, average 753.85, target 1130.78
[10:37:18] API       rate limited by Dhan - now one call every 15.1 s
[10:37:48] API       rate limited by Dhan - now one call every 15.1 s
[10:38:06] VIX       India VIX prev close 14.46
```
</details>

