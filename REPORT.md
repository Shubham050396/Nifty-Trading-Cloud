# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:15 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,381 (+0.46%) | ₹0 | 0 | 5 | ₹2,99,200 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹1,150 (+7.47%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | +₹6,321 (+1.63%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,074 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹3,491 (+3.16%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹8,144** | **+₹12,343** | **−₹8,144** | **9** | **15** | **₹8,13,222** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:08:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:09:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:10:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:12:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:12:55] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 11:13:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:10:14] API       rate limited by Dhan - now one call every 15.1 s
[11:11:55] API       rate limited by Dhan - now one call every 15.1 s
[11:13:17] API       rate limited by Dhan - now one call every 15.1 s
[11:14:18] API       rate limited by Dhan - now one call every 15.1 s
[11:14:38] API       rate limited by Dhan - now one call every 15.1 s
[11:14:42] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:12:56] API       rate limited by Dhan - now one call every 15.1 s
[11:13:26] API       rate limited by Dhan - now one call every 15.1 s
[11:13:57] API       rate limited by Dhan - now one call every 15.1 s
[11:14:12] API       rate limited by Dhan - now one call every 15.1 s
[11:14:42] API       rate limited by Dhan - now one call every 15.1 s
[11:15:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:00:01] SIGNAL    2026-10-27 22000 PE MACD crossed UP (bar close 85.60, hist -0.15 -> +0.12)
[11:00:01] SKIP      buy 2026-10-27 22000 PE ignored - premium 85.60 is outside 144 - 1600
[11:02:05] API       rate limited by Dhan - now one call every 5.1 s
[11:06:10] API       rate limited by Dhan - now one call every 5.1 s
[11:11:35] API       rate limited by Dhan - now one call every 5.1 s
[11:12:57] API       rate limited by Dhan - now one call every 5.1 s
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
[11:15:05] SIGNAL    TATASTEEL 182.5 CE 27 Oct crossed EMA 144 at 9.07 - not taken: under EMA 55, momentum -4.3%
[11:15:05] SIGNAL    ADANIPOWER 195 PE 27 Oct crossed EMA 144 at 3.52 - not taken: under EMA 55, premium under Rs 5
[11:15:05] SIGNAL    DIVISLAB 9200 PE 27 Oct crossed EMA 144 at 163.90 - not taken: momentum -6.3%
[11:15:10] EXIT      SELL TVSMOTOR 4100 CE 27 Oct EMA_STOP @ 148.00  -8.5%  P&L Rs -2397.50
[11:15:11] ENTRY     BUY HEROMOTOCO 5300 PE 27 Oct x150 @ 141.00 (signal close 138.00, EMA 144 134.87, momentum 17.2%)  quick 162.15 till 11:45, target 239.70, stop below EMA 55
[11:15:27] WARM      bar history loaded for all 1558 contracts
```
</details>

