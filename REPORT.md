# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:33 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.04 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹1,372 (+3.69%) | +₹7,917 (+6.92%) | 0 | 2 | ₹37,193 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹2,064 (+0.50%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,11,842 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹4,558 (-17.18%) | +₹14,442 (+12.59%) | −₹17,960 (-10.44%) | 2 | 5 | ₹1,14,732 |
| **Total** | | **+₹28,501** | **+₹17,878** | **+₹6,132** | **10** | **11** | **₹5,63,767** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:11:15] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:12:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:23:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:23:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:30:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:30:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:31:08] API       rate limited by Dhan - now one call every 15.1 s
[12:31:29] API       rate limited by Dhan - now one call every 15.1 s
[12:31:49] API       rate limited by Dhan - now one call every 15.1 s
[12:32:09] API       rate limited by Dhan - now one call every 15.1 s
[12:32:50] API       rate limited by Dhan - now one call every 15.1 s
[12:33:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:32:04] API       rate limited by Dhan - now one call every 15.1 s
[12:32:19] API       rate limited by Dhan - now one call every 15.1 s
[12:32:35] ENTRY     L3 BUY 2026-10-06 22800 PE @ 336.75  target 386.75  trail 303.07 (10%)
[12:32:49] API       rate limited by Dhan - now one call every 15.1 s
[12:33:05] API       rate limited by Dhan - now one call every 15.1 s
[12:33:20] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:29:15] API       rate limited by Dhan - now one call every 15.1 s
[12:29:45] API       rate limited by Dhan - now one call every 15.1 s
[12:30:00] SIGNAL    2026-10-27 26000 PE MACD crossed UP (bar close 3418.70, hist -0.81 -> +0.83)
[12:30:00] SKIP      buy 2026-10-27 26000 PE ignored - premium 3418.70 is outside 144 - 1600
[12:30:43] API       rate limited by Dhan - now one call every 15.1 s
[12:31:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:19:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:21:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:23:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:26:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:29:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:31:37] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:30:26] SKIP      INDHOTEL 700 PE 27 Oct signal at 7.20 skipped - 5 positions already open
[12:30:26] SKIP      HDFCBANK 690 PE 27 Oct signal at 7.50 skipped - 5 positions already open
[12:30:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:31:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:32:12] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:33:12] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

