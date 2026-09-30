# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:15 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹185 (+0.08%) | ₹0 | 0 | 4 | ₹2,33,650 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | +₹280 (+0.15%) | ₹0 | 0 | 4 | ₹1,80,569 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹1,313 (-0.46%) | +₹1,580 (+2.09%) | −₹1,313 (-0.46%) | 2 | 2 | ₹75,680 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹6,305 (+5.36%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹1,313** | **+₹8,350** | **−₹1,313** | **2** | **15** | **₹6,07,603** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:09:04] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:10:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:11:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:12:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:13:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:14:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:12:22] API       rate limited by Dhan - now one call every 15.1 s
[10:13:07] API       rate limited by Dhan - now one call every 15.1 s
[10:13:22] API       rate limited by Dhan - now one call every 15.1 s
[10:14:07] API       rate limited by Dhan - now one call every 15.1 s
[10:14:22] API       rate limited by Dhan - now one call every 15.1 s
[10:15:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:13:00] API       rate limited by Dhan - now one call every 15.1 s
[10:13:30] API       rate limited by Dhan - now one call every 15.1 s
[10:14:00] API       rate limited by Dhan - now one call every 15.1 s
[10:14:30] API       rate limited by Dhan - now one call every 15.1 s
[10:14:45] API       rate limited by Dhan - now one call every 15.1 s
[10:15:01] API       rate limited by Dhan - now one call every 15.1 s
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
[10:14:39] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:15:04] SKIP      TATASTEEL 190 CE 27 Oct signal at 5.31 skipped - 5 positions already open
[10:15:04] SKIP      TECHM 1600 CE 27 Oct signal at 34.05 skipped - 5 positions already open
[10:15:04] SKIP      TECHM 1500 CE 27 Oct signal at 86.25 skipped - 5 positions already open
[10:15:08] GAP       1 contract had no prices for 25+ session minutes (VBL 445 PE 27 Oct) - reloading their bar history
[10:15:10] WARM      bar history loaded for all 1526 contracts
```
</details>

