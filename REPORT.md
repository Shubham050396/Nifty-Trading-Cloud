# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:26 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.96** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹887 (+0.30%) | ₹0 | 0 | 5 | ₹2,98,706 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | ₹0 | +₹1,953 (+5.22%) | 2 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | +₹5,827 (+1.61%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,625 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | −₹61 (-0.06%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹22,445** | **+₹6,653** | **−₹22,445** | **22** | **14** | **₹7,55,543** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:20:31] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:21:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:22:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:23:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:24:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:25:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:23:02] API       rate limited by Dhan - now one call every 15.1 s
[13:23:22] API       rate limited by Dhan - now one call every 15.1 s
[13:24:23] API       rate limited by Dhan - now one call every 15.1 s
[13:24:43] API       rate limited by Dhan - now one call every 15.1 s
[13:25:45] API       rate limited by Dhan - now one call every 15.1 s
[13:26:10] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:24:28] API       rate limited by Dhan - now one call every 15.1 s
[13:24:43] API       rate limited by Dhan - now one call every 15.1 s
[13:24:58] API       rate limited by Dhan - now one call every 15.1 s
[13:25:29] API       rate limited by Dhan - now one call every 15.1 s
[13:25:59] API       rate limited by Dhan - now one call every 15.1 s
[13:26:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:30:01] SKIP      short 2026-10-27 26000 PE ignored - premium 3105.50 is outside 144 - 1600
[12:35:02] SIGNAL    2026-10-27 22000 PE MACD crossed DOWN (bar close 71.15, hist +0.16 -> -0.03)
[12:35:02] SKIP      short 2026-10-27 22000 PE ignored - premium 71.15 is outside 144 - 1600
[13:02:43] API       rate limited by Dhan - now one call every 5.1 s
[13:12:11] API       rate limited by Dhan - now one call every 5.1 s
[13:21:41] API       rate limited by Dhan - now one call every 5.1 s
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
[13:21:13] GAP       1 contract had no prices for 214+ session minutes (HAVELLS 1030 PE 27 Oct) - reloading their bar history
[13:21:14] WARM      bar history loaded for all 1566 contracts
[13:23:00] WARM      bar history loaded for all 1566 contracts
[13:24:10] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:25:05] SKIP      INDHOTEL 750 CE 27 Oct signal at 12.00 skipped - 5 positions already open
[13:25:10] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

