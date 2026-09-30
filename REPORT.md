# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:50 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,196 (+0.40%) | ₹0 | 0 | 5 | ₹2,99,014 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | −₹315 (-2.05%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | −₹536 (-0.15%) | −₹4,111 (-1.14%) | 4 | 3 | ₹3,63,011 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹578 (+0.49%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹5,746** | **+₹923** | **−₹5,746** | **8** | **14** | **₹7,95,121** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:44:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:45:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:47:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:47:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:48:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:49:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:47:09] API       rate limited by Dhan - now one call every 15.1 s
[10:47:30] API       rate limited by Dhan - now one call every 15.1 s
[10:48:31] API       rate limited by Dhan - now one call every 15.1 s
[10:48:51] API       rate limited by Dhan - now one call every 15.1 s
[10:49:52] API       rate limited by Dhan - now one call every 15.1 s
[10:50:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:48:24] API       rate limited by Dhan - now one call every 15.1 s
[10:48:54] API       rate limited by Dhan - now one call every 15.1 s
[10:49:09] API       rate limited by Dhan - now one call every 15.1 s
[10:49:25] API       rate limited by Dhan - now one call every 15.1 s
[10:49:40] API       rate limited by Dhan - now one call every 15.1 s
[10:50:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:50:00] EXIT      LONG 2026-10-27 22000 CE MACD_DOWN @ 897.25  P&L Rs -1823.25
[10:50:00] ENTRY     SELL SHORT 2026-10-27 22000 CE @ 897.25  (bar close 898.80, MACD hist -0.39, VIX 13.41)
[10:50:00] SIGNAL    2026-10-27 24000 PE MACD crossed UP (bar close 1178.35, hist -0.76 -> +0.05)
[10:50:00] ENTRY     BUY 2026-10-27 24000 PE @ 1183.60  (bar close 1178.35, MACD hist +0.05, VIX 13.41)
[10:50:00] SIGNAL    2026-10-27 25000 PE MACD crossed UP (bar close 2155.00, hist -0.50 -> +0.38)
[10:50:00] SKIP      buy 2026-10-27 25000 PE ignored - premium 2155.00 is outside 144 - 1600
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
[10:50:03] SIGNAL    TECHM 1560 PE 27 Oct crossed EMA 144 at 57.50 - not taken: under EMA 55
[10:50:03] SIGNAL    TATAPOWER 350 PE 27 Oct crossed EMA 144 at 3.50 - not taken: momentum -10.3%, premium under Rs 5
[10:50:03] SIGNAL    VBL 450 CE 27 Oct crossed EMA 144 at 7.15 - not taken: momentum -5.3%
[10:50:03] GAP       1 contract had no prices for 58+ session minutes (JSWSTEEL 1290 CE 27 Oct) - reloading their bar history
[10:50:04] WARM      bar history loaded for all 1546 contracts
[10:50:11] WARM      bar history loaded for all 1546 contracts
```
</details>

