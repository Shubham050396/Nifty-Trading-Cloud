# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 14:21 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹2,051 (+0.68%) | ₹0 | 0 | 5 | ₹2,99,869 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | +₹2,740 (+12.28%) | +₹1,953 (+5.22%) | 2 | 1 | ₹22,311 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹5,304 (+1.37%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,86,689 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹1,152 (+1.21%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹27,011** | **+₹11,247** | **−₹27,011** | **26** | **15** | **₹8,04,081** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 14:14:44] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:15:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:17:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:17:55] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 14:21:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:21:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:17:34] API       rate limited by Dhan - now one call every 15.1 s
[14:17:51] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:18:35] API       rate limited by Dhan - now one call every 15.1 s
[14:18:55] API       rate limited by Dhan - now one call every 15.1 s
[14:19:56] API       rate limited by Dhan - now one call every 15.1 s
[14:21:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:20:02] API       rate limited by Dhan - now one call every 15.1 s
[14:20:18] API       rate limited by Dhan - now one call every 15.1 s
[14:20:33] API       rate limited by Dhan - now one call every 15.1 s
[14:20:48] API       rate limited by Dhan - now one call every 15.1 s
[14:21:18] API       rate limited by Dhan - now one call every 15.1 s
[14:21:49] API       rate limited by Dhan - now one call every 15.1 s
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
[14:16:48] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:16:51] API       market quote: rate limited by Dhan - now one call every 3.0 s
[14:17:48] GAP       1 contract had no prices for 259+ session minutes (HEROMOTOCO 5150 PE 27 Oct) - reloading their bar history
[14:17:49] WARM      bar history loaded for all 1572 contracts
[14:18:59] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:20:03] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

