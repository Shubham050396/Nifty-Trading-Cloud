# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:53 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.92 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹4,833 (+12.99%) | +₹3,253 (+8.42%) | +₹12,750 (+8.41%) | 2 | 2 | ₹38,623 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹29,234 (+7.12%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,10,325 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹3,205 (+3.32%) | +₹16,874 (+14.87%) | −₹10,198 (-4.21%) | 5 | 5 | ₹1,13,511 |
| **Total** | | **+₹41,097** | **+₹49,361** | **+₹18,727** | **15** | **11** | **₹5,62,459** |

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
[12:51:47] API       rate limited by Dhan - now one call every 15.1 s
[12:52:07] API       rate limited by Dhan - now one call every 15.1 s
[12:52:28] API       rate limited by Dhan - now one call every 15.1 s
[12:52:48] API       rate limited by Dhan - now one call every 15.1 s
[12:53:08] API       rate limited by Dhan - now one call every 15.1 s
[12:53:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:51:04] ENTRY     L3 BUY 2026-10-06 22700 PE @ 352.25  target 402.25  trail 317.03 (10%)
[12:51:19] API       rate limited by Dhan - now one call every 15.1 s
[12:51:49] API       rate limited by Dhan - now one call every 15.1 s
[12:52:04] API       rate limited by Dhan - now one call every 15.1 s
[12:52:19] API       rate limited by Dhan - now one call every 15.1 s
[12:53:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:47:29] API       rate limited by Dhan - now one call every 14.1 s
[12:47:44] API       rate limited by Dhan - now one call every 15.1 s
[12:48:42] API       rate limited by Dhan - now one call every 15.1 s
[12:50:07] API       rate limited by Dhan - now one call every 15.1 s
[12:50:37] API       rate limited by Dhan - now one call every 15.1 s
[12:51:35] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:43:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:46:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:48:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:49:32] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:50:10] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:52:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:51:06] SKIP      HDFCBANK 690 PE 27 Oct signal at 7.65 skipped - 5 positions already open
[12:51:06] SKIP      CGPOWER 900 PE 27 Oct signal at 43.65 skipped - 5 positions already open
[12:51:13] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:51:52] WARM      bar history loaded for all 1554 contracts
[12:52:13] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:53:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

