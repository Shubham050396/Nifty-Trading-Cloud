# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 15:12 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.57 🔴 above the limit** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹3,010 (+1.00%) | ₹0 | +₹3,010 (+1.00%) | 5 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹7,917 (+6.92%) | ₹0 | +₹7,917 (+6.92%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹20,784 (+5.39%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,85,797 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | −₹759 (-0.80%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹18,037** | **+₹20,025** | **−₹18,037** | **35** | **9** | **₹4,81,009** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 15:05:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 15:06:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:08:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:08:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 15:09:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:10:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:08:42] API       rate limited by Dhan - now one call every 15.1 s
[15:10:04] API       rate limited by Dhan - now one call every 15.1 s
[15:10:24] API       rate limited by Dhan - now one call every 15.1 s
[15:10:29] VIX       India VIX 13.58 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[15:11:25] API       rate limited by Dhan - now one call every 15.1 s
[15:11:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:10:04] API       rate limited by Dhan - now one call every 15.1 s
[15:10:34] API       rate limited by Dhan - now one call every 15.1 s
[15:10:50] API       rate limited by Dhan - now one call every 15.1 s
[15:11:20] API       rate limited by Dhan - now one call every 15.1 s
[15:11:50] API       rate limited by Dhan - now one call every 15.1 s
[15:12:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:40:03] SIGNAL    2026-10-27 26000 CE MACD crossed DOWN (bar close 1.60, hist +0.00 -> -0.00)
[14:40:03] SKIP      short 2026-10-27 26000 CE ignored - premium 1.60 is outside 144 - 1600
[14:40:16] API       rate limited by Dhan - now one call every 5.1 s
[14:45:01] SIGNAL    2026-10-27 26000 CE MACD crossed UP (bar close 2.00, hist -0.00 -> +0.01)
[14:45:01] SKIP      buy 2026-10-27 26000 CE ignored - premium 2.00 is outside 144 - 1600
[14:53:48] API       rate limited by Dhan - now one call every 5.1 s
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
[15:10:04] SIGNAL    SHRIRAMFIN 960 PE 27 Oct crossed EMA 144 at 19.25 - not taken: under EMA 55, momentum 2.9%
[15:10:05] SKIP      TATASTEEL 190 PE 27 Oct signal at 7.09 skipped - 5 positions already open
[15:10:29] API       market quote: rate limited by Dhan - now one call every 2.0 s
[15:11:11] API       market quote: rate limited by Dhan - now one call every 2.0 s
[15:11:30] API       market quote: rate limited by Dhan - now one call every 2.0 s
[15:11:31] WARM      bar history loaded for all 1582 contracts
```
</details>

