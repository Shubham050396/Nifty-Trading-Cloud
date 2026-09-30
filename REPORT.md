# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:56 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.05** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | −₹124 (-0.04%) | ₹0 | 0 | 5 | ₹2,97,695 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | ₹0 | +₹1,953 (+5.22%) | 2 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | +₹9,214 (+2.55%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,707 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹5,759 (-5.68%) | −₹2,256 (-2.55%) | −₹5,759 (-5.68%) | 5 | 4 | ₹88,444 |
| **Total** | | **−₹19,133** | **+₹6,834** | **−₹19,133** | **21** | **13** | **₹7,47,846** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 12:50:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:52:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:52:53] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:53:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:55:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:56:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:53:14] API       rate limited by Dhan - now one call every 15.1 s
[12:53:34] API       rate limited by Dhan - now one call every 15.1 s
[12:54:35] API       rate limited by Dhan - now one call every 15.1 s
[12:54:55] API       rate limited by Dhan - now one call every 15.1 s
[12:55:48] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:55:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:54:38] API       rate limited by Dhan - now one call every 15.1 s
[12:54:53] API       rate limited by Dhan - now one call every 15.1 s
[12:55:08] API       rate limited by Dhan - now one call every 15.1 s
[12:55:24] API       rate limited by Dhan - now one call every 15.1 s
[12:55:54] API       rate limited by Dhan - now one call every 15.1 s
[12:56:09] API       rate limited by Dhan - now one call every 15.1 s
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
[12:51:50] API       market quote: rate limited by Dhan - now one call every 2.5 s
[12:53:47] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:54:48] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:55:02] SIGNAL    BEL 380 PE 27 Oct crossed EMA 144 at 4.90 - not taken: under EMA 55, momentum -5.8%, premium under Rs 5
[12:55:02] SIGNAL    SBIN 940 PE 27 Oct crossed EMA 144 at 7.55 - not taken: under EMA 55, momentum -10.7%
[12:55:02] EXIT      SELL HEROMOTOCO 5300 PE 27 Oct EMA_STOP @ 118.60  -15.9%  P&L Rs -3360.00
```
</details>

