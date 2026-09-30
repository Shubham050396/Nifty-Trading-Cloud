# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:25 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹58 (+0.03%) | ₹0 | 0 | 4 | ₹2,33,523 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | +₹764 (+0.42%) | ₹0 | 0 | 4 | ₹1,80,591 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹1,313 (-0.46%) | +₹1,352 (+1.79%) | −₹1,313 (-0.46%) | 2 | 2 | ₹75,680 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹4,110 (+3.49%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹1,313** | **+₹6,284** | **−₹1,313** | **2** | **15** | **₹6,07,498** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:19:43] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:21:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:21:50] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:22:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:23:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:25:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:22:05] API       rate limited by Dhan - now one call every 15.1 s
[10:22:20] API       rate limited by Dhan - now one call every 15.1 s
[10:23:18] API       rate limited by Dhan - now one call every 15.1 s
[10:24:03] API       rate limited by Dhan - now one call every 15.1 s
[10:24:18] API       rate limited by Dhan - now one call every 15.1 s
[10:25:03] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:23:22] API       rate limited by Dhan - now one call every 15.1 s
[10:23:52] API       rate limited by Dhan - now one call every 15.1 s
[10:24:22] API       rate limited by Dhan - now one call every 15.1 s
[10:24:37] API       rate limited by Dhan - now one call every 15.1 s
[10:24:53] API       rate limited by Dhan - now one call every 15.1 s
[10:25:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:00:02] EXIT      SHORT 2026-10-27 22000 CE MACD_UP @ 925.30  P&L Rs -614.25
[10:00:02] ENTRY     BUY 2026-10-27 22000 CE @ 925.30  (bar close 927.00, MACD hist +0.12, VIX 13.41)
[10:10:01] SIGNAL    2026-10-27 23000 CE MACD crossed UP (bar close 238.50, hist -0.07 -> +0.02)
[10:10:01] EXIT      SHORT 2026-10-27 23000 CE MACD_UP @ 239.00  P&L Rs -698.75
[10:10:01] ENTRY     BUY 2026-10-27 23000 CE @ 239.00  (bar close 238.50, MACD hist +0.02, VIX 13.41)
[10:23:05] API       rate limited by Dhan - now one call every 5.1 s
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
[10:24:09] WARM      bar history loaded for all 1532 contracts
[10:25:03] SIGNAL    WIPRO 160 PE 27 Oct crossed EMA 144 at 4.38 - not taken: under EMA 55, momentum -8.2%, premium under Rs 5
[10:25:03] SIGNAL    GAIL 175 PE 27 Oct crossed EMA 144 at 4.92 - not taken: under EMA 55, momentum 0.4%, premium under Rs 5
[10:25:04] SKIP      HCLTECH 1260 CE 27 Oct signal at 41.40 skipped - 5 positions already open
[10:25:04] SKIP      DLF 650 PE 27 Oct signal at 15.00 skipped - 5 positions already open
[10:25:04] SKIP      HCLTECH 1240 CE 27 Oct signal at 51.20 skipped - 5 positions already open
```
</details>

