# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:55 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.26** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,254 (+0.42%) | ₹0 | 0 | 5 | ₹2,99,073 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 | −₹1,297 (-8.42%) | 1 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | −₹2,528 (-0.65%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,690 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹3,749 (+3.39%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹9,441** | **+₹2,475** | **−₹9,441** | **10** | **14** | **₹7,98,319** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:48:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:49:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:53:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:53:20] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 11:54:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:55:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:52:36] API       rate limited by Dhan - now one call every 15.1 s
[11:53:37] API       rate limited by Dhan - now one call every 15.1 s
[11:53:57] API       rate limited by Dhan - now one call every 15.1 s
[11:54:05] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:54:58] API       rate limited by Dhan - now one call every 15.1 s
[11:55:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:54:09] API       rate limited by Dhan - now one call every 15.1 s
[11:54:24] API       rate limited by Dhan - now one call every 15.1 s
[11:54:40] API       rate limited by Dhan - now one call every 15.1 s
[11:55:10] API       rate limited by Dhan - now one call every 15.1 s
[11:55:25] API       rate limited by Dhan - now one call every 15.1 s
[11:55:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:18:22] API       rate limited by Dhan - now one call every 5.1 s
[11:29:51] VIX       India VIX prev close 13.41 - entries allowed
[11:30:35] API       rate limited by Dhan - now one call every 5.1 s
[11:31:57] API       rate limited by Dhan - now one call every 5.1 s
[11:50:00] SIGNAL    2026-10-27 24000 CE MACD crossed UP (bar close 23.00, hist -0.00 -> +0.04)
[11:50:00] SKIP      buy 2026-10-27 24000 CE ignored - premium 23.00 is outside 144 - 1600
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
[11:52:04] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:52:16] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:53:05] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:55:02] SIGNAL    HDFCBANK 690 PE 27 Oct crossed EMA 144 at 7.20 - not taken: momentum -5.9%
[11:55:02] SIGNAL    HDFCBANK 700 PE 27 Oct crossed EMA 144 at 9.80 - not taken: momentum -5.3%
[11:55:02] SIGNAL    INFY 980 PE 27 Oct crossed EMA 144 at 21.85 - not taken: under EMA 55
```
</details>

