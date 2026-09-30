# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:46 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.13** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹2,070 (+0.69%) | ₹0 | 0 | 5 | ₹2,99,889 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | +₹1,560 (+6.99%) | +₹1,953 (+5.22%) | 2 | 1 | ₹22,311 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | −₹5,509 (-1.53%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,60,849 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | −₹311 (-0.33%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹22,445** | **−₹2,190** | **−₹22,445** | **22** | **15** | **₹7,78,261** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:39:39] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:40:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:41:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:43:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:43:54] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:44:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:44:24] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:44:42] API       rate limited by Dhan - now one call every 15.1 s
[13:45:03] API       rate limited by Dhan - now one call every 15.1 s
[13:46:04] API       rate limited by Dhan - now one call every 15.1 s
[13:46:24] API       rate limited by Dhan - now one call every 15.1 s
[13:46:25] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:44:41] API       rate limited by Dhan - now one call every 15.1 s
[13:45:11] API       rate limited by Dhan - now one call every 15.1 s
[13:45:41] API       rate limited by Dhan - now one call every 15.1 s
[13:45:57] API       rate limited by Dhan - now one call every 15.1 s
[13:46:12] API       rate limited by Dhan - now one call every 15.1 s
[13:46:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:35:02] SKIP      short 2026-10-27 22000 PE ignored - premium 71.15 is outside 144 - 1600
[13:02:43] API       rate limited by Dhan - now one call every 5.1 s
[13:12:11] API       rate limited by Dhan - now one call every 5.1 s
[13:21:41] API       rate limited by Dhan - now one call every 5.1 s
[13:29:54] VIX       India VIX prev close 13.41 - entries allowed
[13:33:52] API       rate limited by Dhan - now one call every 5.1 s
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
[13:45:25] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:45:38] WARM      bar history loaded for all 1568 contracts
[13:45:50] WARM      bar history loaded for all 1568 contracts
[13:45:57] WARM      bar history loaded for all 1568 contracts
[13:46:02] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:46:31] WARM      bar history loaded for all 1570 contracts
```
</details>

