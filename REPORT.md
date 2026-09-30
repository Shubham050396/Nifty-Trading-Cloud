# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:40 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹809 (+0.35%) | ₹0 | 0 | 4 | ₹2,34,274 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹1,092 (-0.61%) | ₹0 | 0 | 4 | ₹1,80,348 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹1,313 (-0.46%) | −₹1,303 (-1.72%) | −₹1,313 (-0.46%) | 2 | 2 | ₹75,680 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹1,198 (+1.02%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹1,313** | **−₹388** | **−₹1,313** | **2** | **15** | **₹6,08,006** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:34:37] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:35:40] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:36:44] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:37:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:38:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:39:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:37:12] API       rate limited by Dhan - now one call every 15.1 s
[10:37:56] API       rate limited by Dhan - now one call every 15.1 s
[10:38:55] API       rate limited by Dhan - now one call every 15.1 s
[10:39:10] API       rate limited by Dhan - now one call every 15.1 s
[10:39:54] API       rate limited by Dhan - now one call every 15.1 s
[10:40:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:38:18] API       rate limited by Dhan - now one call every 15.1 s
[10:38:48] API       rate limited by Dhan - now one call every 15.1 s
[10:39:18] API       rate limited by Dhan - now one call every 15.1 s
[10:39:34] API       rate limited by Dhan - now one call every 15.1 s
[10:39:49] API       rate limited by Dhan - now one call every 15.1 s
[10:40:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:10:01] EXIT      SHORT 2026-10-27 23000 CE MACD_UP @ 239.00  P&L Rs -698.75
[10:10:01] ENTRY     BUY 2026-10-27 23000 CE @ 239.00  (bar close 238.50, MACD hist +0.02, VIX 13.41)
[10:23:05] API       rate limited by Dhan - now one call every 5.1 s
[10:29:49] VIX       India VIX prev close 13.41 - entries allowed
[10:31:01] API       rate limited by Dhan - now one call every 5.1 s
[10:35:58] API       rate limited by Dhan - now one call every 5.1 s
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
[10:38:08] WARM      bar history loaded for all 1540 contracts
[10:40:02] SIGNAL    INFY 1080 PE 27 Oct crossed EMA 144 at 72.60 - not taken: under EMA 55, momentum -6.3%
[10:40:02] SIGNAL    ITC 265 PE 27 Oct crossed EMA 144 at 4.40 - not taken: momentum -2.2%, premium under Rs 5
[10:40:02] SIGNAL    BPCL 300 PE 27 Oct crossed EMA 144 at 5.30 - not taken: under EMA 55
[10:40:03] SKIP      KOTAKBANK 400 CE 27 Oct signal at 18.20 skipped - 5 positions already open
[10:40:15] WARM      bar history loaded for all 1540 contracts
```
</details>

