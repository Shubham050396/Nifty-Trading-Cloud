# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:31 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹991 (+0.33%) | ₹0 | 0 | 5 | ₹2,98,810 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | −₹634 (-2.88%) | −₹1,297 (-8.42%) | 1 | 1 | ₹22,025 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | −₹364 (-0.10%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,241 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,844 (-5.96%) | −₹1,645 (-1.53%) | −₹2,844 (-5.96%) | 2 | 5 | ₹1,07,776 |
| **Total** | | **−₹19,468** | **−₹1,652** | **−₹19,468** | **17** | **15** | **₹7,89,852** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 12:25:14] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:26:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:28:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:28:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:29:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:30:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:27:29] API       rate limited by Dhan - now one call every 15.1 s
[12:27:49] API       rate limited by Dhan - now one call every 15.1 s
[12:28:50] API       rate limited by Dhan - now one call every 15.1 s
[12:29:10] API       rate limited by Dhan - now one call every 15.1 s
[12:29:32] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:30:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:29:21] API       rate limited by Dhan - now one call every 15.1 s
[12:29:52] API       rate limited by Dhan - now one call every 15.1 s
[12:30:22] API       rate limited by Dhan - now one call every 15.1 s
[12:30:24] VIX       India VIX prev close 13.41 -> target 1000 ticks (Rs 50.00)
[12:30:37] API       rate limited by Dhan - now one call every 15.1 s
[12:30:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:25:00] SIGNAL    2026-10-27 23000 PE MACD crossed DOWN (bar close 364.10, hist +0.43 -> -0.30)
[12:25:00] EXIT      LONG 2026-10-27 23000 PE MACD_DOWN @ 365.10  P&L Rs -1807.00
[12:25:00] ENTRY     SELL SHORT 2026-10-27 23000 PE @ 365.10  (bar close 364.10, MACD hist -0.30, VIX 13.41)
[12:29:53] VIX       India VIX prev close 13.41 - entries allowed
[12:30:01] SIGNAL    2026-10-27 26000 PE MACD crossed DOWN (bar close 3105.50, hist +0.24 -> -0.50)
[12:30:01] SKIP      short 2026-10-27 26000 PE ignored - premium 3105.50 is outside 144 - 1600
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
[12:27:22] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:28:31] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:29:22] WARM      bar history loaded for all 1564 contracts
[12:30:04] SIGNAL    VBL 450 CE 27 Oct crossed EMA 144 at 7.25 - not taken: momentum 2.8%
[12:30:04] SIGNAL    ICICIBANK 1350 PE 27 Oct crossed EMA 144 at 36.40 - not taken: under EMA 55, momentum -2.2%
[12:30:04] SIGNAL    ICICIBANK 1360 PE 27 Oct crossed EMA 144 at 42.35 - not taken: under EMA 55, momentum -1.5%
```
</details>

