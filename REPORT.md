# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 14:01 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.13** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,511 (+0.50%) | ₹0 | 0 | 5 | ₹2,99,330 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | +₹1,118 (+5.01%) | +₹1,953 (+5.22%) | 2 | 1 | ₹22,311 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | −₹848 (-0.22%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,87,113 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹614 (+0.64%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹27,011** | **+₹2,395** | **−₹27,011** | **26** | **15** | **₹8,03,966** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:55:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:56:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:57:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:58:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:59:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:00:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:57:36] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:58:15] API       rate limited by Dhan - now one call every 15.1 s
[13:58:35] API       rate limited by Dhan - now one call every 15.1 s
[13:59:36] API       rate limited by Dhan - now one call every 15.1 s
[13:59:57] API       rate limited by Dhan - now one call every 15.1 s
[14:00:58] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:00:05] API       rate limited by Dhan - now one call every 15.1 s
[14:00:20] API       rate limited by Dhan - now one call every 15.1 s
[14:00:51] API       rate limited by Dhan - now one call every 15.1 s
[14:01:06] API       rate limited by Dhan - now one call every 15.1 s
[14:01:21] API       rate limited by Dhan - now one call every 15.1 s
[14:01:36] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:55:00] SKIP      buy 2026-10-27 26000 PE ignored - premium 3140.85 is outside 144 - 1600
[13:55:00] SIGNAL    2026-10-27 23000 PE MACD crossed UP (bar close 376.00, hist -0.27 -> +0.31)
[13:55:00] EXIT      SHORT 2026-10-27 23000 PE MACD_UP @ 379.00  P&L Rs -903.50
[13:55:00] ENTRY     BUY 2026-10-27 23000 PE @ 379.00  (bar close 376.00, MACD hist +0.31, VIX 13.41)
[13:55:33] API       rate limited by Dhan - now one call every 5.1 s
[13:56:54] API       rate limited by Dhan - now one call every 5.1 s
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
[14:00:03] SIGNAL    TATASTEEL 182.5 CE 27 Oct crossed EMA 144 at 9.27 - not taken: momentum -3.2%
[14:00:03] SIGNAL    IRFC 80 CE 27 Oct crossed EMA 144 at 2.32 - not taken: momentum -1.7%, premium under Rs 5
[14:00:04] SKIP      DLF 670 CE 27 Oct signal at 19.80 skipped - 5 positions already open
[14:00:04] SKIP      ADANIPORTS 1780 CE 27 Oct signal at 49.95 skipped - 5 positions already open
[14:00:04] SKIP      INDHOTEL 750 CE 27 Oct signal at 12.30 skipped - 5 positions already open
[14:00:09] WARM      bar history loaded for all 1572 contracts
```
</details>

