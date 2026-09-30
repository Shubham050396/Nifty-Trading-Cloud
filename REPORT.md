# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:36 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.05** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹380 (+0.13%) | ₹0 | 0 | 5 | ₹2,98,199 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | +₹666 (+3.02%) | −₹1,297 (-8.42%) | 1 | 1 | ₹22,025 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | +₹4,121 (+1.14%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,491 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,844 (-5.96%) | −₹2,849 (-2.64%) | −₹2,844 (-5.96%) | 2 | 5 | ₹1,07,776 |
| **Total** | | **−₹19,468** | **+₹2,318** | **−₹19,468** | **17** | **15** | **₹7,89,491** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 12:30:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:31:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:32:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:33:44] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:34:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:35:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:33:15] API       rate limited by Dhan - now one call every 15.1 s
[12:34:15] API       rate limited by Dhan - now one call every 15.1 s
[12:34:35] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:34:36] API       rate limited by Dhan - now one call every 15.1 s
[12:35:37] API       rate limited by Dhan - now one call every 15.1 s
[12:35:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:34:10] API       rate limited by Dhan - now one call every 15.1 s
[12:34:40] API       rate limited by Dhan - now one call every 15.1 s
[12:35:10] API       rate limited by Dhan - now one call every 15.1 s
[12:35:25] API       rate limited by Dhan - now one call every 15.1 s
[12:35:40] API       rate limited by Dhan - now one call every 15.1 s
[12:35:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:25:00] ENTRY     SELL SHORT 2026-10-27 23000 PE @ 365.10  (bar close 364.10, MACD hist -0.30, VIX 13.41)
[12:29:53] VIX       India VIX prev close 13.41 - entries allowed
[12:30:01] SIGNAL    2026-10-27 26000 PE MACD crossed DOWN (bar close 3105.50, hist +0.24 -> -0.50)
[12:30:01] SKIP      short 2026-10-27 26000 PE ignored - premium 3105.50 is outside 144 - 1600
[12:35:02] SIGNAL    2026-10-27 22000 PE MACD crossed DOWN (bar close 71.15, hist +0.16 -> -0.03)
[12:35:02] SKIP      short 2026-10-27 22000 PE ignored - premium 71.15 is outside 144 - 1600
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
[12:30:04] SIGNAL    VBL 450 CE 27 Oct crossed EMA 144 at 7.25 - not taken: momentum 2.8%
[12:30:04] SIGNAL    ICICIBANK 1350 PE 27 Oct crossed EMA 144 at 36.40 - not taken: under EMA 55, momentum -2.2%
[12:30:04] SIGNAL    ICICIBANK 1360 PE 27 Oct crossed EMA 144 at 42.35 - not taken: under EMA 55, momentum -1.5%
[12:32:33] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:33:34] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:35:04] SKIP      ADANIPORTS 1780 CE 27 Oct signal at 47.85 skipped - 5 positions already open
```
</details>

