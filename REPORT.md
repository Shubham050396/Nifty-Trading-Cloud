# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:34 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹2,190 (+2.23%) | −₹13 (-0.08%) | +₹22,610 (+7.06%) | 5 | 1 | ₹15,753 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹9,942 (+1.28%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,73,952 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹958 (+1.11%) | −₹11,956 (-2.08%) | 12 | 5 | ₹86,249 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,134 (-5.80%) | ₹0 | 0 | 6 | ₹71,318 |
| **Total** | | **+₹23,605** | **+₹6,753** | **+₹82,069** | **24** | **22** | **₹9,47,272** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:15:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:15:36] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:20:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:20:37] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:22:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:22:38] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:29:07] API       rate limited by Dhan - now one call every 15.1 s
[12:30:28] API       rate limited by Dhan - now one call every 15.1 s
[12:31:50] API       rate limited by Dhan - now one call every 15.1 s
[12:32:51] API       rate limited by Dhan - now one call every 15.1 s
[12:33:11] API       rate limited by Dhan - now one call every 15.1 s
[12:34:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:30:49] API       rate limited by Dhan - now one call every 15.1 s
[12:31:34] API       rate limited by Dhan - now one call every 15.1 s
[12:32:58] API       rate limited by Dhan - now one call every 15.1 s
[12:33:14] API       rate limited by Dhan - now one call every 15.1 s
[12:33:29] API       rate limited by Dhan - now one call every 15.1 s
[12:33:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:31:53] API       rate limited by Dhan - now one call every 5.1 s
[12:31:58] API       rate limited by Dhan - now one call every 7.1 s
[12:32:35] API       rate limited by Dhan - now one call every 6.1 s
[12:33:06] API       rate limited by Dhan - now one call every 5.1 s
[12:33:16] API       rate limited by Dhan - now one call every 6.1 s
[12:34:00] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:20:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:24:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:27:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:29:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:31:52] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:33:47] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:31:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:31:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:31:34] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:32:34] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:33:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:33:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:30:40] API       rate limited by Dhan - now one call every 15.1 s
[12:30:56] API       rate limited by Dhan - now one call every 15.1 s
[12:32:33] API       rate limited by Dhan - now one call every 15.1 s
[12:33:17] API       rate limited by Dhan - now one call every 15.1 s
[12:33:33] API       rate limited by Dhan - now one call every 15.1 s
[12:33:48] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

