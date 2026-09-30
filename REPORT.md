# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 14:52 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.65 🔴 above the limit** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹3,010 (+1.00%) | ₹0 | +₹3,010 (+1.00%) | 5 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,588 (+9.64%) | −₹708 (-4.75%) | +₹9,588 (+9.64%) | 5 | 1 | ₹14,930 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹16,816 (+4.35%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,86,126 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹271 (+0.28%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹16,366** | **+₹16,379** | **−₹16,366** | **34** | **10** | **₹4,96,268** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 14:46:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:47:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:48:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:49:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:50:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:51:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:48:43] API       rate limited by Dhan - now one call every 15.1 s
[14:49:44] API       rate limited by Dhan - now one call every 15.1 s
[14:50:15] VIX       India VIX 13.49 is back at or below the 13.50 limit - new spreads allowed again
[14:51:05] API       rate limited by Dhan - now one call every 15.1 s
[14:51:16] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:51:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:49:37] API       rate limited by Dhan - now one call every 15.1 s
[14:49:52] API       rate limited by Dhan - now one call every 15.1 s
[14:50:22] API       rate limited by Dhan - now one call every 15.1 s
[14:50:52] API       rate limited by Dhan - now one call every 15.1 s
[14:51:23] API       rate limited by Dhan - now one call every 15.1 s
[14:51:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:35:00] SKIP      buy 2026-10-27 26000 CE ignored - premium 1.75 is outside 144 - 1600
[14:40:03] SIGNAL    2026-10-27 26000 CE MACD crossed DOWN (bar close 1.60, hist +0.00 -> -0.00)
[14:40:03] SKIP      short 2026-10-27 26000 CE ignored - premium 1.60 is outside 144 - 1600
[14:40:16] API       rate limited by Dhan - now one call every 5.1 s
[14:45:01] SIGNAL    2026-10-27 26000 CE MACD crossed UP (bar close 2.00, hist -0.00 -> +0.01)
[14:45:01] SKIP      buy 2026-10-27 26000 CE ignored - premium 2.00 is outside 144 - 1600
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
[14:41:09] API       market quote: rate limited by Dhan - now one call every 2.5 s
[14:42:05] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:45:03] SIGNAL    DLF 660 CE 27 Oct crossed EMA 144 at 22.60 - not taken: under EMA 55, momentum -7.8%
[14:47:01] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:50:02] SIGNAL    KOTAKBANK 415 CE 27 Oct crossed EMA 144 at 10.60 - not taken: momentum -8.2%
[14:50:15] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

