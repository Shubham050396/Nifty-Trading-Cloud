# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:16 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.96** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,079 (+0.36%) | ₹0 | 0 | 5 | ₹2,98,897 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | ₹0 | +₹1,953 (+5.22%) | 2 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | +₹6,692 (+1.85%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,654 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹680 (+0.92%) | −₹9,071 (-7.30%) | 6 | 4 | ₹73,985 |
| **Total** | | **−₹22,445** | **+₹8,451** | **−₹22,445** | **22** | **13** | **₹7,34,536** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:10:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:13:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:13:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:14:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:15:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:16:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:10:50] API       rate limited by Dhan - now one call every 15.1 s
[13:13:33] API       rate limited by Dhan - now one call every 15.1 s
[13:13:53] API       rate limited by Dhan - now one call every 15.1 s
[13:14:54] API       rate limited by Dhan - now one call every 15.1 s
[13:15:14] API       rate limited by Dhan - now one call every 15.1 s
[13:16:15] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:14:22] API       rate limited by Dhan - now one call every 15.1 s
[13:14:37] API       rate limited by Dhan - now one call every 15.1 s
[13:14:53] API       rate limited by Dhan - now one call every 15.1 s
[13:15:23] API       rate limited by Dhan - now one call every 15.1 s
[13:15:53] API       rate limited by Dhan - now one call every 15.1 s
[13:16:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:30:01] SIGNAL    2026-10-27 26000 PE MACD crossed DOWN (bar close 3105.50, hist +0.24 -> -0.50)
[12:30:01] SKIP      short 2026-10-27 26000 PE ignored - premium 3105.50 is outside 144 - 1600
[12:35:02] SIGNAL    2026-10-27 22000 PE MACD crossed DOWN (bar close 71.15, hist +0.16 -> -0.03)
[12:35:02] SKIP      short 2026-10-27 22000 PE ignored - premium 71.15 is outside 144 - 1600
[13:02:43] API       rate limited by Dhan - now one call every 5.1 s
[13:12:11] API       rate limited by Dhan - now one call every 5.1 s
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
[13:12:12] WARM      bar history loaded for all 1566 contracts
[13:14:29] WARM      bar history loaded for all 1566 contracts
[13:14:33] WARM      bar history loaded for all 1566 contracts
[13:15:03] SIGNAL    ADANIPORTS 1780 CE 27 Oct crossed EMA 144 at 47.75 - not taken: momentum -0.1%
[13:15:03] SIGNAL    HDFCBANK 720 PE 27 Oct crossed EMA 144 at 17.15 - not taken: momentum 3.3%
[13:15:04] ENTRY     BUY HDFCBANK 710 PE 27 Oct x650 @ 12.90 (signal close 12.90, EMA 144 12.76, momentum 4.0%)  quick 14.83 till 13:45, target 21.93, stop below EMA 55
```
</details>

