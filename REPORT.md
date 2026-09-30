# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:30 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹36 (+0.02%) | ₹0 | 0 | 4 | ₹2,33,501 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | +₹734 (+0.41%) | ₹0 | 0 | 4 | ₹1,80,600 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹1,313 (-0.46%) | +₹1,121 (+1.48%) | −₹1,313 (-0.46%) | 2 | 2 | ₹75,680 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹5,220 (+4.43%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹1,313** | **+₹7,111** | **−₹1,313** | **2** | **15** | **₹6,07,485** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:23:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:25:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:26:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:27:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:29:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:29:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:28:02] API       rate limited by Dhan - now one call every 15.1 s
[10:28:18] API       rate limited by Dhan - now one call every 15.1 s
[10:29:02] API       rate limited by Dhan - now one call every 15.1 s
[10:29:03] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:30:00] API       rate limited by Dhan - now one call every 15.1 s
[10:30:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:28:40] API       rate limited by Dhan - now one call every 15.1 s
[10:28:56] API       rate limited by Dhan - now one call every 15.1 s
[10:29:11] API       rate limited by Dhan - now one call every 15.1 s
[10:29:41] API       rate limited by Dhan - now one call every 15.1 s
[10:29:59] VIX       India VIX prev close 13.41 -> target 1000 ticks (Rs 50.00)
[10:30:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:00:02] ENTRY     BUY 2026-10-27 22000 CE @ 925.30  (bar close 927.00, MACD hist +0.12, VIX 13.41)
[10:10:01] SIGNAL    2026-10-27 23000 CE MACD crossed UP (bar close 238.50, hist -0.07 -> +0.02)
[10:10:01] EXIT      SHORT 2026-10-27 23000 CE MACD_UP @ 239.00  P&L Rs -698.75
[10:10:01] ENTRY     BUY 2026-10-27 23000 CE @ 239.00  (bar close 238.50, MACD hist +0.02, VIX 13.41)
[10:23:05] API       rate limited by Dhan - now one call every 5.1 s
[10:29:49] VIX       India VIX prev close 13.41 - entries allowed
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
[10:25:04] SKIP      HCLTECH 1240 CE 27 Oct signal at 51.20 skipped - 5 positions already open
[10:25:20] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:27:49] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:28:14] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:28:34] WARM      bar history loaded for all 1534 contracts
[10:30:02] SIGNAL    HCLTECH 1260 PE 27 Oct crossed EMA 144 at 49.65 - not taken: under EMA 55, momentum -7.5%
```
</details>

