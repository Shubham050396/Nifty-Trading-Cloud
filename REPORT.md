# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 15:07 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.57 🔴 above the limit** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹3,010 (+1.00%) | ₹0 | +₹3,010 (+1.00%) | 5 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹7,917 (+6.92%) | ₹0 | +₹7,917 (+6.92%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹19,506 (+5.05%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,85,917 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹158 (+0.17%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹18,037** | **+₹19,664** | **−₹18,037** | **35** | **9** | **₹4,81,129** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 15:01:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:02:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:03:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:05:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:05:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 15:06:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:02:23] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[15:03:17] API       rate limited by Dhan - now one call every 15.1 s
[15:04:38] API       rate limited by Dhan - now one call every 15.1 s
[15:04:58] API       rate limited by Dhan - now one call every 15.1 s
[15:06:00] API       rate limited by Dhan - now one call every 15.1 s
[15:06:20] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:05:16] API       rate limited by Dhan - now one call every 15.1 s
[15:05:46] API       rate limited by Dhan - now one call every 15.1 s
[15:06:02] API       rate limited by Dhan - now one call every 15.1 s
[15:06:17] API       rate limited by Dhan - now one call every 15.1 s
[15:06:32] API       rate limited by Dhan - now one call every 15.1 s
[15:07:02] API       rate limited by Dhan - now one call every 15.1 s
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
[15:05:04] SIGNAL    DMART 3900 CE 27 Oct crossed EMA 144 at 97.40 - not taken: momentum -3.8%
[15:05:04] SIGNAL    VBL 430 CE 27 Oct crossed EMA 144 at 14.80 - not taken: under EMA 55, momentum -2.6%
[15:05:05] SKIP      DLF 670 CE 27 Oct signal at 19.75 skipped - 5 positions already open
[15:05:18] WARM      bar history loaded for all 1582 contracts
[15:05:48] WARM      bar history loaded for all 1582 contracts
[15:06:15] WARM      bar history loaded for all 1582 contracts
```
</details>

