# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:20 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,436 (+0.48%) | ₹0 | 0 | 5 | ₹2,99,255 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹926 (+6.02%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | +₹4,186 (+1.08%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,232 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹3,475 (+3.14%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹8,144** | **+₹10,023** | **−₹8,144** | **9** | **15** | **₹8,13,435** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:13:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:16:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:16:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 11:17:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:18:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:19:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:16:00] API       rate limited by Dhan - now one call every 15.1 s
[11:17:01] API       rate limited by Dhan - now one call every 15.1 s
[11:17:21] API       rate limited by Dhan - now one call every 15.1 s
[11:18:42] API       rate limited by Dhan - now one call every 15.1 s
[11:19:43] API       rate limited by Dhan - now one call every 15.1 s
[11:20:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:18:30] API       rate limited by Dhan - now one call every 15.1 s
[11:19:00] API       rate limited by Dhan - now one call every 15.1 s
[11:19:30] API       rate limited by Dhan - now one call every 15.1 s
[11:20:00] API       rate limited by Dhan - now one call every 15.1 s
[11:20:15] API       rate limited by Dhan - now one call every 15.1 s
[11:20:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:00:01] SKIP      buy 2026-10-27 22000 PE ignored - premium 85.60 is outside 144 - 1600
[11:02:05] API       rate limited by Dhan - now one call every 5.1 s
[11:06:10] API       rate limited by Dhan - now one call every 5.1 s
[11:11:35] API       rate limited by Dhan - now one call every 5.1 s
[11:12:57] API       rate limited by Dhan - now one call every 5.1 s
[11:18:22] API       rate limited by Dhan - now one call every 5.1 s
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
[11:15:58] WARM      bar history loaded for all 1558 contracts
[11:16:48] WARM      bar history loaded for all 1558 contracts
[11:20:01] SIGNAL    BPCL 300 PE 27 Oct crossed EMA 144 at 5.30 - not taken: under EMA 55
[11:20:01] SIGNAL    INFY 940 PE 27 Oct crossed EMA 144 at 11.25 - not taken: under EMA 55
[11:20:03] SKIP      INDIGO 5000 PE 27 Oct signal at 180.00 skipped - 5 positions already open
[11:20:22] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

