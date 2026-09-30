# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:20 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | −₹543 (-0.23%) | ₹0 | 0 | 4 | ₹2,32,922 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | +₹536 (+0.30%) | ₹0 | 0 | 4 | ₹1,80,573 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹1,313 (-0.46%) | +₹1,781 (+2.35%) | −₹1,313 (-0.46%) | 2 | 2 | ₹75,680 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹4,629 (+3.93%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹1,313** | **+₹6,403** | **−₹1,313** | **2** | **15** | **₹6,06,879** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:14:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:16:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:16:31] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:17:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:19:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:19:43] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:17:22] API       rate limited by Dhan - now one call every 15.1 s
[10:18:07] API       rate limited by Dhan - now one call every 15.1 s
[10:18:08] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:19:05] API       rate limited by Dhan - now one call every 15.1 s
[10:19:20] API       rate limited by Dhan - now one call every 15.1 s
[10:20:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:18:03] API       rate limited by Dhan - now one call every 15.1 s
[10:18:33] API       rate limited by Dhan - now one call every 15.1 s
[10:19:03] API       rate limited by Dhan - now one call every 15.1 s
[10:19:19] API       rate limited by Dhan - now one call every 15.1 s
[10:19:34] API       rate limited by Dhan - now one call every 15.1 s
[10:19:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:00:02] SIGNAL    2026-10-27 22000 CE MACD crossed UP (bar close 927.00, hist -0.21 -> +0.12)
[10:00:02] EXIT      SHORT 2026-10-27 22000 CE MACD_UP @ 925.30  P&L Rs -614.25
[10:00:02] ENTRY     BUY 2026-10-27 22000 CE @ 925.30  (bar close 927.00, MACD hist +0.12, VIX 13.41)
[10:10:01] SIGNAL    2026-10-27 23000 CE MACD crossed UP (bar close 238.50, hist -0.07 -> +0.02)
[10:10:01] EXIT      SHORT 2026-10-27 23000 CE MACD_UP @ 239.00  P&L Rs -698.75
[10:10:01] ENTRY     BUY 2026-10-27 23000 CE @ 239.00  (bar close 238.50, MACD hist +0.02, VIX 13.41)
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
[10:18:39] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:18:59] WARM      bar history loaded for all 1530 contracts
[10:19:22] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:19:22] WARM      bar history loaded for all 1530 contracts
[10:20:03] SIGNAL    INDIGO 5100 CE 27 Oct crossed EMA 144 at 101.75 - not taken: momentum -0.6%
[10:20:03] SIGNAL    TCS 2040 PE 27 Oct crossed EMA 144 at 46.05 - not taken: under EMA 55, momentum -9.5%
```
</details>

