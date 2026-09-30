# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:41 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.96** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,001 (+0.33%) | ₹0 | 0 | 5 | ₹2,98,819 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | ₹0 | +₹1,953 (+5.22%) | 2 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | −₹562 (-0.16%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,163 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | −₹715 (-0.75%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹22,445** | **−₹276** | **−₹22,445** | **22** | **14** | **₹7,55,194** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:35:24] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:36:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:37:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:39:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:39:39] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:40:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:36:55] API       rate limited by Dhan - now one call every 15.1 s
[13:37:56] API       rate limited by Dhan - now one call every 15.1 s
[13:38:16] API       rate limited by Dhan - now one call every 15.1 s
[13:39:17] API       rate limited by Dhan - now one call every 15.1 s
[13:39:38] API       rate limited by Dhan - now one call every 15.1 s
[13:40:39] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:39:37] API       rate limited by Dhan - now one call every 15.1 s
[13:40:07] API       rate limited by Dhan - now one call every 15.1 s
[13:40:22] API       rate limited by Dhan - now one call every 15.1 s
[13:40:38] API       rate limited by Dhan - now one call every 15.1 s
[13:40:53] API       rate limited by Dhan - now one call every 15.1 s
[13:41:23] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:35:02] SKIP      short 2026-10-27 22000 PE ignored - premium 71.15 is outside 144 - 1600
[13:02:43] API       rate limited by Dhan - now one call every 5.1 s
[13:12:11] API       rate limited by Dhan - now one call every 5.1 s
[13:21:41] API       rate limited by Dhan - now one call every 5.1 s
[13:29:54] VIX       India VIX prev close 13.41 - entries allowed
[13:33:52] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
serving NIFTY Scalper - IVX-G on http://127.0.0.1:46175
[2026-09-30 09:29:47] RUN       scalper armed - started automatically on launch
[2026-09-30 09:29:48] BOOT      scrip master: 4036 NIFTY contracts
[2026-09-30 09:29:48] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
[2026-09-30 11:38:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:39:52] WARM      bar history loaded for all 1566 contracts
[13:40:03] SIGNAL    BEL 380 PE 27 Oct crossed EMA 144 at 4.80 - not taken: under EMA 55, momentum 1.1%, premium under Rs 5
[13:40:03] SIGNAL    SBIN 940 PE 27 Oct crossed EMA 144 at 8.05 - not taken: under EMA 55
[13:40:03] SIGNAL    DIVISLAB 9200 PE 27 Oct crossed EMA 144 at 162.60 - not taken: momentum -0.3%
[13:40:03] SIGNAL    IOC 135 PE 27 Oct crossed EMA 144 at 3.26 - not taken: under EMA 55, premium under Rs 5
[13:40:03] SIGNAL    DIVISLAB 9000 PE 27 Oct crossed EMA 144 at 104.60 - not taken: momentum 0.0%
```
</details>

