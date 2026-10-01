# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 13:33 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.78 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,253 (+10.10%) | ₹0 | +₹17,170 (+8.34%) | 5 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹24,105 (+5.88%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,10,226 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | +₹855 (+0.93%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹52,288** | **+₹24,960** | **+₹29,918** | **23** | **9** | **₹5,02,168** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 13:27:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:28:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:29:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:30:32] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:31:32] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:32:32] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:28:02] API       rate limited by Dhan - now one call every 15.1 s
[13:29:24] API       rate limited by Dhan - now one call every 15.1 s
[13:31:06] API       rate limited by Dhan - now one call every 15.1 s
[13:32:06] API       rate limited by Dhan - now one call every 15.1 s
[13:32:27] API       rate limited by Dhan - now one call every 15.1 s
[13:33:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:31:14] API       rate limited by Dhan - now one call every 15.1 s
[13:31:44] API       rate limited by Dhan - now one call every 15.1 s
[13:32:14] API       rate limited by Dhan - now one call every 15.1 s
[13:32:44] API       rate limited by Dhan - now one call every 15.1 s
[13:33:00] API       rate limited by Dhan - now one call every 15.1 s
[13:33:30] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:08:02] API       rate limited by Dhan - now one call every 15.1 s
[13:13:09] API       rate limited by Dhan - now one call every 5.1 s
[13:15:51] API       rate limited by Dhan - now one call every 5.1 s
[13:18:34] API       rate limited by Dhan - now one call every 5.1 s
[13:21:16] API       rate limited by Dhan - now one call every 5.1 s
[13:30:46] API       rate limited by Dhan - now one call every 5.1 s
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
[13:25:03] SIGNAL    BPCL 290 PE 27 Oct crossed EMA 144 at 3.30 - not taken: premium under Rs 5
[13:25:03] SIGNAL    CGPOWER 840 PE 27 Oct crossed EMA 144 at 13.50 - not taken: under EMA 55
[13:25:04] SKIP      INDIGO 4800 PE 27 Oct signal at 95.85 skipped - 5 positions already open
[13:25:16] WARM      bar history loaded for all 1576 contracts
[13:30:01] SIGNAL    ADANIGREEN 1300 PE 27 Oct crossed EMA 144 at 54.15 - not taken: under EMA 55
[13:33:32] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

