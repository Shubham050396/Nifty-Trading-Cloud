# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:36 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.96** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,264 (+0.42%) | ₹0 | 0 | 5 | ₹2,99,083 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | ₹0 | +₹1,953 (+5.22%) | 2 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | +₹2,327 (+0.64%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,416 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹840 (+0.88%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹22,445** | **+₹4,431** | **−₹22,445** | **22** | **14** | **₹7,55,711** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:32:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:32:13] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:33:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:35:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:35:24] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:36:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:31:30] API       rate limited by Dhan - now one call every 15.1 s
[13:32:31] API       rate limited by Dhan - now one call every 15.1 s
[13:33:16] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:35:13] API       rate limited by Dhan - now one call every 15.1 s
[13:35:17] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:35:34] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:33:49] API       rate limited by Dhan - now one call every 15.1 s
[13:34:19] API       rate limited by Dhan - now one call every 15.1 s
[13:34:34] API       rate limited by Dhan - now one call every 15.1 s
[13:35:04] API       rate limited by Dhan - now one call every 15.1 s
[13:35:34] API       rate limited by Dhan - now one call every 15.1 s
[13:36:04] API       rate limited by Dhan - now one call every 15.1 s
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
[13:32:15] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:32:26] WARM      bar history loaded for all 1566 contracts
[13:34:17] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:34:21] API       market quote: rate limited by Dhan - now one call every 2.5 s
[13:35:02] SIGNAL    JSWSTEEL 1300 PE 27 Oct crossed EMA 144 at 41.40 - not taken: under EMA 55, momentum -7.8%
[13:35:03] SKIP      DLF 670 CE 27 Oct signal at 20.50 skipped - 5 positions already open
```
</details>

