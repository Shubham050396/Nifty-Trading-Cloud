# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 14:26 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹2,327 (+0.78%) | ₹0 | 0 | 5 | ₹3,00,145 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹5,203 (+8.71%) | +₹682 (+4.18%) | +₹5,203 (+8.71%) | 3 | 1 | ₹16,312 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹12,698 (+3.29%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,86,262 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹956 (+1.00%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹23,761** | **+₹16,663** | **−₹23,761** | **27** | **15** | **₹7,97,931** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 14:21:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:21:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 14:23:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:23:14] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 14:24:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:25:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:22:59] API       rate limited by Dhan - now one call every 15.1 s
[14:24:00] API       rate limited by Dhan - now one call every 15.1 s
[14:24:20] API       rate limited by Dhan - now one call every 15.1 s
[14:25:21] API       rate limited by Dhan - now one call every 15.1 s
[14:25:41] API       rate limited by Dhan - now one call every 15.1 s
[14:26:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:25:05] API       rate limited by Dhan - now one call every 15.1 s
[14:25:21] API       rate limited by Dhan - now one call every 15.1 s
[14:25:36] API       rate limited by Dhan - now one call every 15.1 s
[14:26:06] API       rate limited by Dhan - now one call every 15.1 s
[14:26:36] API       rate limited by Dhan - now one call every 15.1 s
[14:26:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:55:00] EXIT      SHORT 2026-10-27 23000 PE MACD_UP @ 379.00  P&L Rs -903.50
[13:55:00] ENTRY     BUY 2026-10-27 23000 PE @ 379.00  (bar close 376.00, MACD hist +0.31, VIX 13.41)
[13:55:33] API       rate limited by Dhan - now one call every 5.1 s
[13:56:54] API       rate limited by Dhan - now one call every 5.1 s
[14:09:06] API       rate limited by Dhan - now one call every 5.1 s
[14:10:27] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
serving NIFTY Scalper - IVX-G on http://127.0.0.1:46175
[2026-09-30 09:29:47] RUN       scalper armed - started automatically on launch
[2026-09-30 09:29:48] BOOT      scrip master: 4036 NIFTY contracts
[2026-09-30 09:29:48] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
[2026-09-30 11:38:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:25:07] SKIP      JINDALSTEL 1100 PE 27 Oct signal at 14.90 skipped - 5 positions already open
[14:25:07] SKIP      HEROMOTOCO 5200 PE 27 Oct signal at 94.30 skipped - 5 positions already open
[14:25:39] WARM      bar history loaded for all 1576 contracts
[14:25:53] WARM      bar history loaded for all 1576 contracts
[14:25:57] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:26:26] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

