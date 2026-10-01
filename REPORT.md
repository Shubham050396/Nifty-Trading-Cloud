# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 13:08 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.78 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,253 (+10.10%) | ₹0 | +₹17,170 (+8.34%) | 5 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹18,522 (+4.51%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,10,652 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹18,126 (+12.93%) | −₹1,830 (-1.69%) | +₹4,724 (+1.65%) | 7 | 5 | ₹1,08,300 |
| **Total** | | **+₹60,438** | **+₹16,692** | **+₹38,069** | **20** | **9** | **₹5,18,952** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:48:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:49:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:50:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:51:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:08:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:08:27] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:57:12] API       rate limited by Dhan - now one call every 15.1 s
[12:59:34] API       rate limited by Dhan - now one call every 15.1 s
[13:01:44] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:02:37] API       rate limited by Dhan - now one call every 15.1 s
[13:06:42] API       rate limited by Dhan - now one call every 15.1 s
[13:08:03] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:06:58] API       rate limited by Dhan - now one call every 15.1 s
[13:07:13] API       rate limited by Dhan - now one call every 15.1 s
[13:07:43] API       rate limited by Dhan - now one call every 15.1 s
[13:07:58] API       rate limited by Dhan - now one call every 15.1 s
[13:08:14] API       rate limited by Dhan - now one call every 15.1 s
[13:08:29] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:04:51] API       rate limited by Dhan - now one call every 15.1 s
[13:05:06] API       rate limited by Dhan - now one call every 15.1 s
[13:06:18] API       rate limited by Dhan - now one call every 15.1 s
[13:06:48] API       rate limited by Dhan - now one call every 15.1 s
[13:07:04] API       rate limited by Dhan - now one call every 15.1 s
[13:08:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:58:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:01:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:03:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:06:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:06:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:07:41] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:05:15] WARM      bar history loaded for all 1574 contracts
[13:05:22] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:05:22] SIGNAL    DMART 3800 CE 27 Oct crossed EMA 144 at 141.40 - not taken: under EMA 55, momentum -8.8%
[13:05:31] ENTRY     BUY HDFCLIFE 530 CE 27 Oct x1100 @ 18.05 (signal close 17.90, EMA 144 17.39, momentum 14.0%)  quick 20.76 till 13:35, target 30.68, stop below EMA 55
[13:07:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:08:18] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

