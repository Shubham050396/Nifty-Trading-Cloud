# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:35 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.31** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,719 (+0.57%) | ₹0 | 0 | 5 | ₹2,99,538 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | −₹868 (-5.64%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | −₹309 (-0.08%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,620 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹4,644 (+4.20%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹8,144** | **+₹5,186** | **−₹8,144** | **9** | **15** | **₹8,14,106** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:29:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:31:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:33:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:33:08] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 11:34:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:35:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:30:56] API       rate limited by Dhan - now one call every 15.1 s
[11:32:17] API       rate limited by Dhan - now one call every 15.1 s
[11:33:18] API       rate limited by Dhan - now one call every 15.1 s
[11:33:38] API       rate limited by Dhan - now one call every 15.1 s
[11:34:39] API       rate limited by Dhan - now one call every 15.1 s
[11:35:00] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:33:55] API       rate limited by Dhan - now one call every 15.1 s
[11:34:25] API       rate limited by Dhan - now one call every 15.1 s
[11:34:41] API       rate limited by Dhan - now one call every 15.1 s
[11:34:56] API       rate limited by Dhan - now one call every 15.1 s
[11:35:11] API       rate limited by Dhan - now one call every 15.1 s
[11:35:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:11:35] API       rate limited by Dhan - now one call every 5.1 s
[11:12:57] API       rate limited by Dhan - now one call every 5.1 s
[11:18:22] API       rate limited by Dhan - now one call every 5.1 s
[11:29:51] VIX       India VIX prev close 13.41 - entries allowed
[11:30:35] API       rate limited by Dhan - now one call every 5.1 s
[11:31:57] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
cloud: HALT_ALL 15:25 -> 15:13
serving NIFTY Scalper - IVX-G on http://127.0.0.1:46175
[2026-09-30 09:29:47] RUN       scalper armed - started automatically on launch
[2026-09-30 09:29:48] BOOT      scrip master: 4036 NIFTY contracts
[2026-09-30 09:29:48] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:30:30] WARM      bar history loaded for all 1560 contracts
[11:30:41] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:32:04] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:32:29] WARM      bar history loaded for all 1562 contracts
[11:35:01] SIGNAL    ADANIPORTS 1760 CE 27 Oct crossed EMA 144 at 55.35 - not taken: momentum 0.2%
[11:35:24] API       chart history: rate limited by Dhan - now one call every 1.2 s
```
</details>

