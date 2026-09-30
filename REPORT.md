# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:00 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹852 (+0.29%) | ₹0 | 0 | 5 | ₹2,98,670 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 | −₹1,297 (-8.42%) | 1 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | −₹5,762 (-1.48%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,969 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹1,541 (+1.39%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹9,441** | **−₹3,369** | **−₹9,441** | **10** | **14** | **₹7,98,195** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:55:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:56:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:57:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:58:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:00:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:00:46] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:55:19] API       rate limited by Dhan - now one call every 15.1 s
[11:56:20] API       rate limited by Dhan - now one call every 15.1 s
[11:57:41] API       rate limited by Dhan - now one call every 15.1 s
[11:59:02] API       rate limited by Dhan - now one call every 15.1 s
[11:59:22] API       rate limited by Dhan - now one call every 15.1 s
[12:00:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:58:58] API       rate limited by Dhan - now one call every 15.1 s
[11:59:28] API       rate limited by Dhan - now one call every 15.1 s
[11:59:43] API       rate limited by Dhan - now one call every 15.1 s
[11:59:58] API       rate limited by Dhan - now one call every 15.1 s
[12:00:14] API       rate limited by Dhan - now one call every 15.1 s
[12:00:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:29:51] VIX       India VIX prev close 13.41 - entries allowed
[11:30:35] API       rate limited by Dhan - now one call every 5.1 s
[11:31:57] API       rate limited by Dhan - now one call every 5.1 s
[11:50:00] SIGNAL    2026-10-27 24000 CE MACD crossed UP (bar close 23.00, hist -0.00 -> +0.04)
[11:50:00] SKIP      buy 2026-10-27 24000 CE ignored - premium 23.00 is outside 144 - 1600
[12:00:24] API       rate limited by Dhan - now one call every 5.1 s
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
[12:00:03] SIGNAL    HEROMOTOCO 5200 PE 27 Oct crossed EMA 144 at 96.80 - not taken: momentum 3.0%
[12:00:04] SKIP      TATASTEEL 190 CE 27 Oct signal at 5.62 skipped - 5 positions already open
[12:00:04] SKIP      INDIGO 5000 CE 27 Oct signal at 136.75 skipped - 5 positions already open
[12:00:04] SKIP      TATASTEEL 185 CE 27 Oct signal at 8.59 skipped - 5 positions already open
[12:00:09] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:00:53] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

