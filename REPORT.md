# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:15 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,573 (+0.53%) | ₹0 | 0 | 5 | ₹2,99,391 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 | −₹1,297 (-8.42%) | 1 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹7,264 (-1.01%) | −₹4,134 (-1.70%) | −₹7,264 (-1.01%) | 7 | 4 | ₹2,43,205 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,844 (-5.96%) | −₹299 (-0.33%) | −₹2,844 (-5.96%) | 2 | 4 | ₹91,176 |
| **Total** | | **−₹13,040** | **−₹2,860** | **−₹13,040** | **14** | **13** | **₹6,33,772** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 12:10:21] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:11:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:12:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:14:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:14:36] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:15:40] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:10:15] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:11:14] API       rate limited by Dhan - now one call every 15.1 s
[12:11:34] API       rate limited by Dhan - now one call every 15.1 s
[12:12:35] API       rate limited by Dhan - now one call every 15.1 s
[12:13:56] API       rate limited by Dhan - now one call every 15.1 s
[12:14:19] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:13:53] API       rate limited by Dhan - now one call every 15.1 s
[12:14:23] API       rate limited by Dhan - now one call every 15.1 s
[12:14:39] API       rate limited by Dhan - now one call every 15.1 s
[12:14:54] API       rate limited by Dhan - now one call every 15.1 s
[12:15:09] API       rate limited by Dhan - now one call every 15.1 s
[12:15:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:10:02] SIGNAL    2026-10-27 21000 CE MACD crossed UP (bar close 1845.00, hist -0.19 -> +0.29)
[12:10:02] SKIP      buy 2026-10-27 21000 CE ignored - premium 1845.00 is outside 144 - 1600
[12:10:02] SIGNAL    2026-10-27 24000 PE MACD crossed DOWN (bar close 1159.60, hist +0.19 -> -0.24)
[12:10:02] EXIT      LONG 2026-10-27 24000 PE MACD_DOWN @ 1161.80  P&L Rs -1417.00
[12:10:02] ENTRY     SELL SHORT 2026-10-27 24000 PE @ 1161.80  (bar close 1159.60, MACD hist -0.24, VIX 13.41)
[12:15:18] API       rate limited by Dhan - now one call every 5.1 s
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
[12:15:01] SIGNAL    HDFCBANK 700 PE 27 Oct crossed EMA 144 at 10.05 - not taken: momentum 1.0%
[12:15:01] SIGNAL    ICICIBANK 1320 PE 27 Oct crossed EMA 144 at 22.90 - not taken: under EMA 55, momentum -7.1%
[12:15:01] SIGNAL    ITC 265 PE 27 Oct crossed EMA 144 at 4.45 - not taken: premium under Rs 5
[12:15:01] SIGNAL    TECHM 1500 PE 27 Oct crossed EMA 144 at 32.70 - not taken: under EMA 55, momentum -4.8%
[12:15:01] EXIT      SELL VBL 430 CE 27 Oct EMA_STOP @ 14.85  -2.3%  P&L Rs -446.25
[12:15:01] SIGNAL    INFY 940 PE 27 Oct crossed EMA 144 at 11.45 - not taken: under EMA 55, momentum 1.3%
```
</details>

