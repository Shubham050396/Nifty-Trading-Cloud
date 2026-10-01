# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:58 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **15.33 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹8,083 (+15.27%) | +₹2,428 (+6.28%) | +₹16,000 (+9.56%) | 3 | 2 | ₹38,672 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹38,483 (+9.39%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,09,814 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹3,205 (+3.32%) | +₹22,146 (+19.51%) | −₹10,198 (-4.21%) | 5 | 5 | ₹1,13,511 |
| **Total** | | **+₹44,347** | **+₹63,057** | **+₹21,977** | **16** | **11** | **₹5,61,997** |

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
[12:53:28] API       rate limited by Dhan - now one call every 15.1 s
[12:53:49] API       rate limited by Dhan - now one call every 15.1 s
[12:54:29] API       rate limited by Dhan - now one call every 15.1 s
[12:55:51] API       rate limited by Dhan - now one call every 15.1 s
[12:56:40] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:57:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:56:21] API       rate limited by Dhan - now one call every 15.1 s
[12:56:37] API       rate limited by Dhan - now one call every 15.1 s
[12:57:07] ENTRY     L2 BUY 2026-10-06 22500 PE @ 242.70  target 292.70  trail 206.29 (15%)
[12:57:21] API       rate limited by Dhan - now one call every 15.1 s
[12:57:51] API       rate limited by Dhan - now one call every 15.1 s
[12:58:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:50:37] API       rate limited by Dhan - now one call every 15.1 s
[12:51:35] API       rate limited by Dhan - now one call every 15.1 s
[12:54:06] API       rate limited by Dhan - now one call every 15.1 s
[12:55:18] API       rate limited by Dhan - now one call every 15.1 s
[12:55:33] API       rate limited by Dhan - now one call every 15.1 s
[12:56:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:48:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:49:32] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:50:10] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:52:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:54:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:56:55] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:56:05] WARM      bar history loaded for all 1566 contracts
[12:56:52] WARM      bar history loaded for all 1568 contracts
[12:57:13] WARM      bar history loaded for all 1570 contracts
[12:57:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:58:03] WARM      bar history loaded for all 1570 contracts
[12:58:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

