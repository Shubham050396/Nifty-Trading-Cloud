# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 14:49 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.84 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹12,503 (+11.62%) | ₹0 | +₹20,420 (+9.20%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹54,698 (+6.98%) | −₹1,658 (-0.39%) | +₹36,439 (+1.71%) | 8 | 4 | ₹4,21,237 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | −₹3,190 (-3.47%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹77,434** | **−₹4,848** | **+₹55,063** | **28** | **9** | **₹5,13,179** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 14:42:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:43:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:44:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:45:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:47:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:47:48] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:42:56] API       rate limited by Dhan - now one call every 15.1 s
[14:43:36] API       rate limited by Dhan - now one call every 15.1 s
[14:44:17] API       rate limited by Dhan - now one call every 15.1 s
[14:47:00] API       rate limited by Dhan - now one call every 15.1 s
[14:47:03] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:49:04] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:47:17] API       rate limited by Dhan - now one call every 15.1 s
[14:47:32] API       rate limited by Dhan - now one call every 15.1 s
[14:48:02] API       rate limited by Dhan - now one call every 15.1 s
[14:48:17] API       rate limited by Dhan - now one call every 15.1 s
[14:48:33] API       rate limited by Dhan - now one call every 15.1 s
[14:49:03] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:45:00] EXIT      LONG 2026-10-27 23000 PE MACD_DOWN @ 651.30  P&L Rs 6630.00
[14:45:00] ENTRY     SELL SHORT 2026-10-27 23000 PE @ 651.30  (bar close 651.60, MACD hist -1.41, VIX 13.49)
[14:46:06] API       rate limited by Dhan - now one call every 15.1 s
[14:46:36] API       rate limited by Dhan - now one call every 15.1 s
[14:47:35] API       rate limited by Dhan - now one call every 15.1 s
[14:48:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 14:34:10] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:34:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:41:08] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:42:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:45:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:48:14] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:45:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:47:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:47:37] WARM      bar history loaded for all 1582 contracts
[14:48:02] WARM      bar history loaded for all 1582 contracts
[14:48:26] WARM      bar history loaded for all 1582 contracts
[14:49:15] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

