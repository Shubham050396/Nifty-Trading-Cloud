# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 13:03 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.86 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,253 (+10.10%) | ₹0 | +₹17,170 (+8.34%) | 5 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹22,061 (+5.37%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,10,497 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹18,126 (+12.93%) | +₹5,328 (+6.02%) | +₹4,724 (+1.65%) | 7 | 4 | ₹88,445 |
| **Total** | | **+₹60,438** | **+₹27,389** | **+₹38,069** | **20** | **8** | **₹4,98,942** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:43:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:48:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:48:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:49:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:50:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:51:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:55:51] API       rate limited by Dhan - now one call every 15.1 s
[12:56:40] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:57:12] API       rate limited by Dhan - now one call every 15.1 s
[12:59:34] API       rate limited by Dhan - now one call every 15.1 s
[13:01:44] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:02:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:02:10] EXIT      L2 2026-10-06 22500 PE TRAIL_STOP @ 210.70  P&L Rs -2080.00
[13:02:24] API       rate limited by Dhan - now one call every 15.1 s
[13:02:40] API       rate limited by Dhan - now one call every 15.1 s
[13:03:10] API       rate limited by Dhan - now one call every 15.1 s
[13:03:12] VIX       India VIX prev close 13.49 -> target 1000 ticks (Rs 50.00)
[13:03:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:58:49] API       rate limited by Dhan - now one call every 15.1 s
[12:59:04] API       rate limited by Dhan - now one call every 15.1 s
[13:00:53] API       rate limited by Dhan - now one call every 15.1 s
[13:02:04] API       rate limited by Dhan - now one call every 15.1 s
[13:02:20] API       rate limited by Dhan - now one call every 15.1 s
[13:03:07] VIX       India VIX prev close 13.49 - entries allowed
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:50:10] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:52:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:54:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:56:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:58:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:01:21] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:00:23] SKIP      DMART 3700 PE 27 Oct signal at 83.00 skipped - already 1 open on DMART
[13:00:41] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:00:59] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:02:14] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:02:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:02:53] WARM      bar history loaded for all 1574 contracts
```
</details>

