# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:49 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.00 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹1,176 (+0.15%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,520 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹675 (+0.78%) | −₹11,956 (-2.08%) | 12 | 5 | ₹86,249 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹3,130 (-4.39%) | ₹0 | 0 | 6 | ₹71,318 |
| **Total** | | **+₹22,543** | **−₹1,279** | **+₹81,007** | **25** | **21** | **₹9,32,087** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:34:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:34:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:37:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:37:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:43:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:43:43] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:44:04] API       rate limited by Dhan - now one call every 15.1 s
[12:45:26] API       rate limited by Dhan - now one call every 15.1 s
[12:46:27] API       rate limited by Dhan - now one call every 15.1 s
[12:47:36] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:48:29] API       rate limited by Dhan - now one call every 15.1 s
[12:49:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:44:27] API       rate limited by Dhan - now one call every 15.1 s
[12:45:26] API       rate limited by Dhan - now one call every 15.1 s
[12:46:24] API       rate limited by Dhan - now one call every 15.1 s
[12:48:13] API       rate limited by Dhan - now one call every 15.1 s
[12:48:43] EXIT      L2 2026-10-19 22500 PE TRAIL_STOP @ 226.00  P&L Rs -1062.75
[12:49:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:45:11] SIGNAL    2026-11-23 24000 CE MACD crossed UP (bar close 71.50, hist -0.01 -> +0.09)
[12:45:11] SKIP      buy 2026-11-23 24000 CE ignored - premium 71.50 is outside 144 - 1600
[12:46:54] API       rate limited by Dhan - now one call every 10.1 s
[12:48:03] API       rate limited by Dhan - now one call every 10.1 s
[12:48:24] API       rate limited by Dhan - now one call every 15.1 s
[12:48:54] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:38:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:40:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:42:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:44:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:47:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:48:53] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:42:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:44:11] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:45:47] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:47:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:47:44] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:48:11] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:39:49] API       rate limited by Dhan - now one call every 15.1 s
[12:42:20] API       rate limited by Dhan - now one call every 15.1 s
[12:43:19] API       rate limited by Dhan - now one call every 15.1 s
[12:45:08] API       rate limited by Dhan - now one call every 15.1 s
[12:46:57] API       rate limited by Dhan - now one call every 15.1 s
[12:47:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

