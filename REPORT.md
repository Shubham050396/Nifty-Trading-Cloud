# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 13:13 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.78 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,253 (+10.10%) | ₹0 | +₹17,170 (+8.34%) | 5 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹19,841 (+4.83%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,10,558 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹13,424 (+8.01%) | −₹1,332 (-1.30%) | +₹21 (+0.01%) | 8 | 5 | ₹1,02,645 |
| **Total** | | **+₹55,736** | **+₹18,509** | **+₹33,366** | **21** | **9** | **₹5,13,203** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:50:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:51:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:08:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:08:27] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 13:13:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:13:28] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:08:44] API       rate limited by Dhan - now one call every 15.1 s
[13:09:25] API       rate limited by Dhan - now one call every 15.1 s
[13:10:26] API       rate limited by Dhan - now one call every 15.1 s
[13:10:46] API       rate limited by Dhan - now one call every 15.1 s
[13:11:47] API       rate limited by Dhan - now one call every 15.1 s
[13:12:51] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:11:31] API       rate limited by Dhan - now one call every 15.1 s
[13:12:02] API       rate limited by Dhan - now one call every 15.1 s
[13:12:17] API       rate limited by Dhan - now one call every 15.1 s
[13:12:32] API       rate limited by Dhan - now one call every 15.1 s
[13:12:47] API       rate limited by Dhan - now one call every 15.1 s
[13:13:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:05:06] API       rate limited by Dhan - now one call every 15.1 s
[13:06:18] API       rate limited by Dhan - now one call every 15.1 s
[13:06:48] API       rate limited by Dhan - now one call every 15.1 s
[13:07:04] API       rate limited by Dhan - now one call every 15.1 s
[13:08:02] API       rate limited by Dhan - now one call every 15.1 s
[13:13:09] API       rate limited by Dhan - now one call every 5.1 s
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
[13:10:20] ENTRY     BUY INDIGO 5000 CE 27 Oct x150 @ 145.60 (signal close 149.15, EMA 144 138.30, momentum 10.6%)  quick 167.44 till 13:40, target 247.52, stop below EMA 55
[13:10:20] SKIP      INDIGO 4900 CE 27 Oct signal at 205.20 skipped - 5 positions already open
[13:10:20] SKIP      INDIGO 5100 CE 27 Oct signal at 105.00 skipped - 5 positions already open
[13:10:20] SKIP      INDIGO 4800 CE 27 Oct signal at 271.10 skipped - 5 positions already open
[13:11:28] API       market quote: rate limited by Dhan - now one call every 4.0 s
[13:12:28] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

