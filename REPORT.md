# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:11 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.96** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹582 (+0.19%) | ₹0 | 0 | 5 | ₹2,98,400 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | ₹0 | +₹1,953 (+5.22%) | 2 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | +₹8,040 (+2.22%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,691 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹2,292 (+3.49%) | −₹9,071 (-7.30%) | 6 | 3 | ₹65,600 |
| **Total** | | **−₹22,445** | **+₹10,914** | **−₹22,445** | **22** | **12** | **₹7,25,691** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:05:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:06:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:07:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:08:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:09:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:10:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:08:08] API       rate limited by Dhan - now one call every 15.1 s
[13:08:28] API       rate limited by Dhan - now one call every 15.1 s
[13:09:29] API       rate limited by Dhan - now one call every 15.1 s
[13:09:49] API       rate limited by Dhan - now one call every 15.1 s
[13:09:59] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:10:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:09:50] API       rate limited by Dhan - now one call every 15.1 s
[13:10:05] API       rate limited by Dhan - now one call every 15.1 s
[13:10:35] API       rate limited by Dhan - now one call every 15.1 s
[13:10:50] API       rate limited by Dhan - now one call every 15.1 s
[13:11:06] API       rate limited by Dhan - now one call every 15.1 s
[13:11:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:29:53] VIX       India VIX prev close 13.41 - entries allowed
[12:30:01] SIGNAL    2026-10-27 26000 PE MACD crossed DOWN (bar close 3105.50, hist +0.24 -> -0.50)
[12:30:01] SKIP      short 2026-10-27 26000 PE ignored - premium 3105.50 is outside 144 - 1600
[12:35:02] SIGNAL    2026-10-27 22000 PE MACD crossed DOWN (bar close 71.15, hist +0.16 -> -0.03)
[12:35:02] SKIP      short 2026-10-27 22000 PE ignored - premium 71.15 is outside 144 - 1600
[13:02:43] API       rate limited by Dhan - now one call every 5.1 s
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
[13:10:03] SIGNAL    IRFC 82 CE 27 Oct crossed EMA 144 at 1.61 - not taken: premium under Rs 5
[13:10:03] SIGNAL    DIVISLAB 9000 PE 27 Oct crossed EMA 144 at 105.00 - not taken: momentum -5.6%
[13:11:01] WARM      bar history loaded for all 1566 contracts
[13:11:12] GAP       1 contract had no prices for 191+ session minutes (CGPOWER 830 PE 27 Oct) - reloading their bar history
[13:11:13] WARM      bar history loaded for all 1566 contracts
[13:11:20] WARM      bar history loaded for all 1566 contracts
```
</details>

