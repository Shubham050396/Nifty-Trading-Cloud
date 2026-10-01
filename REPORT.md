# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:18 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **13.76 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹7,917 (+6.92%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | ₹0 | +₹14,544 (+0.84%) | 4 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹4,558 (-17.18%) | +₹15,710 (+16.77%) | −₹17,960 (-10.44%) | 2 | 4 | ₹93,672 |
| **Total** | | **+₹28,501** | **+₹15,710** | **+₹6,132** | **10** | **4** | **₹93,672** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:07:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:08:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:09:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:11:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:11:15] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:12:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:16:15] API       rate limited by Dhan - now one call every 15.1 s
[12:16:35] API       rate limited by Dhan - now one call every 15.1 s
[12:16:55] API       rate limited by Dhan - now one call every 15.1 s
[12:17:16] API       rate limited by Dhan - now one call every 15.1 s
[12:17:36] API       rate limited by Dhan - now one call every 15.1 s
[12:17:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:16:23] API       rate limited by Dhan - now one call every 15.1 s
[12:16:39] API       rate limited by Dhan - now one call every 15.1 s
[12:17:09] API       rate limited by Dhan - now one call every 15.1 s
[12:17:24] API       rate limited by Dhan - now one call every 15.1 s
[12:17:40] API       rate limited by Dhan - now one call every 15.1 s
[12:18:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:12:11] API       rate limited by Dhan - now one call every 15.1 s
[12:12:55] API       rate limited by Dhan - now one call every 15.1 s
[12:15:37] API       rate limited by Dhan - now one call every 15.1 s
[12:15:52] API       rate limited by Dhan - now one call every 15.1 s
[12:17:41] API       rate limited by Dhan - now one call every 15.1 s
[12:17:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:05:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:08:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:11:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:13:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:15:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:17:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:15:16] SIGNAL    LODHA 1100 PE 27 Oct crossed EMA 144 at 34.55 - not taken: momentum -1.6%
[12:15:25] ENTRY     BUY ADANIPORTS 1800 PE 27 Oct x475 @ 59.10 (signal close 59.20, EMA 144 58.32, momentum 7.6%)  quick 67.97 till 12:45, target 100.47, stop below EMA 55
[12:15:52] SIGNAL    HDFCLIFE 540 PE 27 Oct crossed EMA 144 at 19.25 - not taken: under EMA 55
[12:16:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:17:15] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:17:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

