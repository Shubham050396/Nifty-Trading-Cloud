# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:26 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹696 (+0.23%) | ₹0 | 0 | 5 | ₹2,98,514 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 (+0.00%) | −₹1,297 (-8.42%) | 1 | 1 | ₹22,025 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | +₹78 (+0.02%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,275 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,844 (-5.96%) | −₹2,162 (-2.01%) | −₹2,844 (-5.96%) | 2 | 5 | ₹1,07,776 |
| **Total** | | **−₹19,468** | **−₹1,388** | **−₹19,468** | **17** | **15** | **₹7,89,590** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 12:20:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:20:59] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:23:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:23:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:25:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:25:14] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:19:42] API       rate limited by Dhan - now one call every 15.1 s
[12:20:24] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:22:04] API       rate limited by Dhan - now one call every 15.1 s
[12:24:46] API       rate limited by Dhan - now one call every 15.1 s
[12:25:07] API       rate limited by Dhan - now one call every 15.1 s
[12:25:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:24:32] API       rate limited by Dhan - now one call every 15.1 s
[12:24:48] API       rate limited by Dhan - now one call every 15.1 s
[12:25:03] API       rate limited by Dhan - now one call every 15.1 s
[12:25:18] ENTRY     L3 BUY 2026-10-06 22500 CE @ 338.85  target 388.85  trail 304.97 (10%)
[12:25:33] API       rate limited by Dhan - now one call every 15.1 s
[12:25:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:25:00] ENTRY     SELL SHORT 2026-10-27 24000 PE @ 1138.70  (bar close 1137.00, MACD hist -0.89, VIX 13.41)
[12:25:00] SIGNAL    2026-10-27 25000 PE MACD crossed DOWN (bar close 2120.00, hist +0.22 -> -0.66)
[12:25:00] SKIP      short 2026-10-27 25000 PE ignored - premium 2120.00 is outside 144 - 1600
[12:25:00] SIGNAL    2026-10-27 23000 PE MACD crossed DOWN (bar close 364.10, hist +0.43 -> -0.30)
[12:25:00] EXIT      LONG 2026-10-27 23000 PE MACD_DOWN @ 365.10  P&L Rs -1807.00
[12:25:00] ENTRY     SELL SHORT 2026-10-27 23000 PE @ 365.10  (bar close 364.10, MACD hist -0.30, VIX 13.41)
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
[12:24:11] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:24:27] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:25:03] ENTRY     BUY KOTAKBANK 420 CE 27 Oct x2000 @ 8.30 (signal close 8.20, EMA 144 7.77, momentum 13.9%)  quick 9.54 till 12:55, target 14.11, stop below EMA 55
[12:25:03] SKIP      INDIGO 5000 CE 27 Oct signal at 139.50 skipped - 5 positions already open
[12:25:03] SKIP      ADANIPORTS 1780 CE 27 Oct signal at 47.80 skipped - 5 positions already open
[12:25:03] SKIP      TVSMOTOR 4100 CE 27 Oct signal at 160.00 skipped - 5 positions already open
```
</details>

