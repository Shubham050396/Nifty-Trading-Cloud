# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 13:18 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.78 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,253 (+10.10%) | ₹0 | +₹17,170 (+8.34%) | 5 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹26,783 (+6.53%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,10,180 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | −₹153 (-1.77%) | ₹0 | 0 | 1 | ₹8,638 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹13,424 (+8.01%) | −₹2,935 (-2.86%) | +₹21 (+0.01%) | 8 | 5 | ₹1,02,645 |
| **Total** | | **+₹55,736** | **+₹23,695** | **+₹33,366** | **21** | **10** | **₹5,21,463** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 13:13:28] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 13:14:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:15:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:16:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:18:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:18:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:12:51] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:14:30] API       rate limited by Dhan - now one call every 15.1 s
[13:14:50] API       rate limited by Dhan - now one call every 15.1 s
[13:16:11] API       rate limited by Dhan - now one call every 15.1 s
[13:17:12] API       rate limited by Dhan - now one call every 15.1 s
[13:17:33] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:17:05] API       rate limited by Dhan - now one call every 15.1 s
[13:17:21] API       rate limited by Dhan - now one call every 15.1 s
[13:17:36] API       rate limited by Dhan - now one call every 15.1 s
[13:18:06] API       rate limited by Dhan - now one call every 15.1 s
[13:18:21] API       rate limited by Dhan - now one call every 15.1 s
[13:18:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:06:48] API       rate limited by Dhan - now one call every 15.1 s
[13:07:04] API       rate limited by Dhan - now one call every 15.1 s
[13:08:02] API       rate limited by Dhan - now one call every 15.1 s
[13:13:09] API       rate limited by Dhan - now one call every 5.1 s
[13:15:51] API       rate limited by Dhan - now one call every 5.1 s
[13:18:34] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 13:01:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:03:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:06:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:06:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:07:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:18:09] ENTRY     BUY 65 22350 PUT @ 132.90  target 179.05  stop 117.52  (IV slope +0.175, z +2.00)
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:11:28] API       market quote: rate limited by Dhan - now one call every 4.0 s
[13:12:28] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:15:04] SIGNAL    AXISBANK 1200 PE 27 Oct crossed EMA 144 at 20.60 - not taken: under EMA 55
[13:17:29] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:17:36] WARM      bar history loaded for all 1574 contracts
[13:17:45] WARM      bar history loaded for all 1574 contracts
```
</details>

