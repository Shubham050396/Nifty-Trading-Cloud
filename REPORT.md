# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:56 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.13** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,869 (+0.62%) | ₹0 | 0 | 5 | ₹2,99,687 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | +₹517 (+2.32%) | +₹1,953 (+5.22%) | 2 | 1 | ₹22,311 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | −₹2,724 (-0.70%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,87,197 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹1,778 (+1.87%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹27,011** | **+₹1,440** | **−₹27,011** | **26** | **15** | **₹8,04,407** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:51:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:52:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:54:32] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:54:32] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:55:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:56:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:51:29] API       rate limited by Dhan - now one call every 15.1 s
[13:52:50] API       rate limited by Dhan - now one call every 15.1 s
[13:53:10] API       rate limited by Dhan - now one call every 15.1 s
[13:54:11] API       rate limited by Dhan - now one call every 15.1 s
[13:54:32] API       rate limited by Dhan - now one call every 15.1 s
[13:54:33] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:54:17] API       rate limited by Dhan - now one call every 15.1 s
[13:54:47] API       rate limited by Dhan - now one call every 15.1 s
[13:55:17] API       rate limited by Dhan - now one call every 15.1 s
[13:55:33] API       rate limited by Dhan - now one call every 15.1 s
[13:56:03] API       rate limited by Dhan - now one call every 15.1 s
[13:56:33] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:55:00] SIGNAL    2026-10-27 26000 PE MACD crossed UP (bar close 3140.85, hist -0.87 -> +0.60)
[13:55:00] SKIP      buy 2026-10-27 26000 PE ignored - premium 3140.85 is outside 144 - 1600
[13:55:00] SIGNAL    2026-10-27 23000 PE MACD crossed UP (bar close 376.00, hist -0.27 -> +0.31)
[13:55:00] EXIT      SHORT 2026-10-27 23000 PE MACD_UP @ 379.00  P&L Rs -903.50
[13:55:00] ENTRY     BUY 2026-10-27 23000 PE @ 379.00  (bar close 376.00, MACD hist +0.31, VIX 13.41)
[13:55:33] API       rate limited by Dhan - now one call every 5.1 s
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
[13:52:31] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:53:28] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:53:32] API       market quote: rate limited by Dhan - now one call every 2.5 s
[13:55:02] SIGNAL    BOSCHLTD 48000 PE 27 Oct crossed EMA 144 at 1390.10 - not taken: under EMA 55
[13:55:02] SIGNAL    VBL 440 CE 27 Oct crossed EMA 144 at 10.40 - not taken: momentum -8.8%
[13:56:35] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

