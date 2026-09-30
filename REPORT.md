# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:35 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹985 (+0.42%) | ₹0 | 0 | 4 | ₹2,34,450 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹91 (-0.05%) | ₹0 | 0 | 4 | ₹1,80,340 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹1,313 (-0.46%) | −₹2,974 (-3.93%) | −₹1,313 (-0.46%) | 2 | 2 | ₹75,680 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹3,210 (+2.73%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹1,313** | **+₹1,130** | **−₹1,313** | **2** | **15** | **₹6,08,174** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:29:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:31:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:31:25] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:32:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:34:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:34:37] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:32:59] API       rate limited by Dhan - now one call every 15.1 s
[10:33:14] API       rate limited by Dhan - now one call every 15.1 s
[10:33:58] API       rate limited by Dhan - now one call every 15.1 s
[10:34:14] API       rate limited by Dhan - now one call every 15.1 s
[10:34:58] API       rate limited by Dhan - now one call every 15.1 s
[10:35:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:33:14] API       rate limited by Dhan - now one call every 15.1 s
[10:33:44] API       rate limited by Dhan - now one call every 15.1 s
[10:34:14] API       rate limited by Dhan - now one call every 15.1 s
[10:34:44] API       rate limited by Dhan - now one call every 15.1 s
[10:35:00] API       rate limited by Dhan - now one call every 15.1 s
[10:35:15] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:10:01] SIGNAL    2026-10-27 23000 CE MACD crossed UP (bar close 238.50, hist -0.07 -> +0.02)
[10:10:01] EXIT      SHORT 2026-10-27 23000 CE MACD_UP @ 239.00  P&L Rs -698.75
[10:10:01] ENTRY     BUY 2026-10-27 23000 CE @ 239.00  (bar close 238.50, MACD hist +0.02, VIX 13.41)
[10:23:05] API       rate limited by Dhan - now one call every 5.1 s
[10:29:49] VIX       India VIX prev close 13.41 - entries allowed
[10:31:01] API       rate limited by Dhan - now one call every 5.1 s
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
[10:35:03] SIGNAL    TCS 2040 PE 27 Oct crossed EMA 144 at 45.70 - not taken: under EMA 55, momentum -7.6%
[10:35:03] SIGNAL    TCS 2080 PE 27 Oct crossed EMA 144 at 62.50 - not taken: under EMA 55, momentum -6.9%
[10:35:03] SIGNAL    TCS 2100 PE 27 Oct crossed EMA 144 at 72.30 - not taken: under EMA 55, momentum -6.3%
[10:35:03] SIGNAL    WIPRO 155 PE 27 Oct crossed EMA 144 at 2.68 - not taken: under EMA 55, momentum -1.1%, premium under Rs 5
[10:35:03] SIGNAL    DABUR 380 PE 27 Oct crossed EMA 144 at 7.00 - not taken: momentum 0.0%
[10:35:15] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

