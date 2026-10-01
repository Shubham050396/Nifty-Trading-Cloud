# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 14:59 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.62 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹12,503 (+11.62%) | ₹0 | +₹20,420 (+9.20%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹54,698 (+6.98%) | +₹8,070 (+1.43%) | +₹36,439 (+1.71%) | 8 | 5 | ₹5,62,895 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | −₹632 (-0.69%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹77,434** | **+₹7,438** | **+₹55,063** | **28** | **10** | **₹6,54,837** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 14:47:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:47:48] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 14:51:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:51:49] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 14:53:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:53:49] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:55:08] API       rate limited by Dhan - now one call every 15.1 s
[14:56:09] API       rate limited by Dhan - now one call every 15.1 s
[14:56:30] API       rate limited by Dhan - now one call every 15.1 s
[14:57:31] API       rate limited by Dhan - now one call every 15.1 s
[14:57:51] API       rate limited by Dhan - now one call every 15.1 s
[14:59:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:57:09] API       rate limited by Dhan - now one call every 15.1 s
[14:57:39] API       rate limited by Dhan - now one call every 15.1 s
[14:57:54] API       rate limited by Dhan - now one call every 15.1 s
[14:58:24] API       rate limited by Dhan - now one call every 15.1 s
[14:58:39] API       rate limited by Dhan - now one call every 15.1 s
[14:59:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:52:48] API       rate limited by Dhan - now one call every 15.1 s
[14:54:48] API       rate limited by Dhan - now one call every 15.1 s
[14:55:04] SIGNAL    2026-10-27 21000 PE MACD crossed DOWN (bar close 36.65, hist +0.08 -> -0.23)
[14:55:04] SKIP      short 2026-10-27 21000 PE ignored - premium 36.65 is outside 144 - 1600
[14:56:59] API       rate limited by Dhan - now one call every 15.1 s
[14:57:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 14:42:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:45:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:48:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:49:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:53:15] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:56:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:55:39] SKIP      INFY 1040 CE 27 Oct signal at 36.00 skipped - 5 positions already open
[14:56:25] WARM      bar history loaded for all 1582 contracts
[14:56:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:57:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:58:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:59:14] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

