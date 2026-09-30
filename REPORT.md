# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:25 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,238 (+0.41%) | ₹0 | 0 | 5 | ₹2,99,057 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹803 (+5.22%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | +₹5,447 (+1.40%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,192 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹6,134 (+5.55%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹8,144** | **+₹13,622** | **−₹8,144** | **9** | **15** | **₹8,13,197** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:17:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:18:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:19:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:21:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:21:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 11:22:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:21:25] API       rate limited by Dhan - now one call every 15.1 s
[11:22:26] API       rate limited by Dhan - now one call every 15.1 s
[11:22:47] API       rate limited by Dhan - now one call every 15.1 s
[11:23:48] API       rate limited by Dhan - now one call every 15.1 s
[11:24:08] API       rate limited by Dhan - now one call every 15.1 s
[11:25:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:23:33] API       rate limited by Dhan - now one call every 15.1 s
[11:23:48] API       rate limited by Dhan - now one call every 15.1 s
[11:24:04] API       rate limited by Dhan - now one call every 15.1 s
[11:24:19] API       rate limited by Dhan - now one call every 15.1 s
[11:24:49] API       rate limited by Dhan - now one call every 15.1 s
[11:25:19] API       rate limited by Dhan - now one call every 15.1 s
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
[11:23:33] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:23:58] WARM      bar history loaded for all 1560 contracts
[11:24:37] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:25:02] SIGNAL    ADANIENT 2900 PE 27 Oct crossed EMA 144 at 81.35 - not taken: under EMA 55
[11:25:02] SIGNAL    AXISBANK 1220 PE 27 Oct crossed EMA 144 at 28.85 - not taken: under EMA 55, momentum -7.1%
[11:25:02] SIGNAL    AXISBANK 1240 PE 27 Oct crossed EMA 144 at 38.90 - not taken: under EMA 55, momentum -5.6%
```
</details>

