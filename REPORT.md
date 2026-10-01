# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:28 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.04 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹1,488 (+9.73%) | +₹7,917 (+6.92%) | 0 | 1 | ₹15,304 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹2,116 (+0.51%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,11,868 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹4,558 (-17.18%) | +₹14,840 (+12.93%) | −₹17,960 (-10.44%) | 2 | 5 | ₹1,14,732 |
| **Total** | | **+₹28,501** | **+₹18,444** | **+₹6,132** | **10** | **10** | **₹5,41,904** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:09:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:11:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:11:15] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:12:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:23:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:23:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:26:24] API       rate limited by Dhan - now one call every 15.1 s
[12:26:44] API       rate limited by Dhan - now one call every 15.1 s
[12:27:04] API       rate limited by Dhan - now one call every 15.1 s
[12:27:25] API       rate limited by Dhan - now one call every 15.1 s
[12:27:45] API       rate limited by Dhan - now one call every 15.1 s
[12:28:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:26:15] API       rate limited by Dhan - now one call every 15.1 s
[12:26:30] API       rate limited by Dhan - now one call every 15.1 s
[12:27:01] API       rate limited by Dhan - now one call every 15.1 s
[12:27:16] API       rate limited by Dhan - now one call every 15.1 s
[12:27:46] API       rate limited by Dhan - now one call every 15.1 s
[12:28:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:25:12] SIGNAL    2026-10-27 21000 PE MACD crossed UP (bar close 27.90, hist -0.05 -> +0.03)
[12:25:12] SKIP      buy 2026-10-27 21000 PE ignored - premium 27.90 is outside 144 - 1600
[12:25:12] SIGNAL    2026-10-27 25000 PE MACD crossed UP (bar close 2410.00, hist -0.65 -> +0.80)
[12:25:12] SKIP      buy 2026-10-27 25000 PE ignored - premium 2410.00 is outside 144 - 1600
[12:26:19] API       rate limited by Dhan - now one call every 15.1 s
[12:27:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:15:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:17:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:19:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:21:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:23:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:26:34] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:26:29] SKIP      HDFCBANK 710 PE 27 Oct signal at 13.35 skipped - 5 positions already open
[12:26:29] SKIP      HDFCBANK 700 PE 27 Oct signal at 9.80 skipped - 5 positions already open
[12:26:29] SKIP      HCLTECH 1210 PE 27 Oct signal at 34.50 skipped - 5 positions already open
[12:26:37] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:27:07] WARM      bar history loaded for all 1478 contracts
[12:27:44] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

