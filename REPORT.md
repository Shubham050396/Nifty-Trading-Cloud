# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 13:23 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.78 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,253 (+10.10%) | ₹0 | +₹17,170 (+8.34%) | 5 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹29,627 (+7.23%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,09,993 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | +₹925 (+1.01%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹52,288** | **+₹30,552** | **+₹29,918** | **23** | **9** | **₹5,01,935** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 13:18:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 13:19:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:21:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:21:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 13:22:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:23:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:17:33] API       rate limited by Dhan - now one call every 15.1 s
[13:18:54] API       rate limited by Dhan - now one call every 15.1 s
[13:19:55] API       rate limited by Dhan - now one call every 15.1 s
[13:21:36] API       rate limited by Dhan - now one call every 15.1 s
[13:22:37] API       rate limited by Dhan - now one call every 15.1 s
[13:22:58] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:21:08] API       rate limited by Dhan - now one call every 15.1 s
[13:21:38] API       rate limited by Dhan - now one call every 15.1 s
[13:21:53] API       rate limited by Dhan - now one call every 15.1 s
[13:22:23] API       rate limited by Dhan - now one call every 15.1 s
[13:22:53] API       rate limited by Dhan - now one call every 15.1 s
[13:23:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:07:04] API       rate limited by Dhan - now one call every 15.1 s
[13:08:02] API       rate limited by Dhan - now one call every 15.1 s
[13:13:09] API       rate limited by Dhan - now one call every 5.1 s
[13:15:51] API       rate limited by Dhan - now one call every 5.1 s
[13:18:34] API       rate limited by Dhan - now one call every 5.1 s
[13:21:16] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 13:03:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:06:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:06:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:07:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:18:09] ENTRY     BUY 65 22350 PUT @ 132.90  target 179.05  stop 117.52  (IV slope +0.175, z +2.00)
[2026-10-01 13:19:59] EXIT      SIGNAL_DECAY 22350 65 PUT @ 135.00  gross +136  net +61  (1.8)
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:20:06] SKIP      INDIGO 5000 PE 27 Oct signal at 180.00 skipped - 5 positions already open
[13:20:30] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:21:58] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:22:10] WARM      bar history loaded for all 1576 contracts
[13:22:22] WARM      bar history loaded for all 1576 contracts
[13:22:59] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

