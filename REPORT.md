# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:00 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,098 (+0.37%) | ₹0 | 0 | 5 | ₹2,98,917 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹618 (+4.01%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | +₹1,823 (+0.47%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,383 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹2,148 (+1.82%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹5,746** | **+₹5,687** | **−₹5,746** | **8** | **15** | **₹8,20,396** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:52:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:53:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:56:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:56:57] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:58:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:59:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:56:39] API       rate limited by Dhan - now one call every 15.1 s
[10:56:59] API       rate limited by Dhan - now one call every 15.1 s
[10:58:01] API       rate limited by Dhan - now one call every 15.1 s
[10:58:21] API       rate limited by Dhan - now one call every 15.1 s
[10:59:22] API       rate limited by Dhan - now one call every 15.1 s
[10:59:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:58:30] API       rate limited by Dhan - now one call every 15.1 s
[10:59:01] API       rate limited by Dhan - now one call every 15.1 s
[10:59:31] API       rate limited by Dhan - now one call every 15.1 s
[10:59:46] API       rate limited by Dhan - now one call every 15.1 s
[11:00:01] API       rate limited by Dhan - now one call every 15.1 s
[11:00:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:00:01] SIGNAL    2026-10-27 25000 CE MACD crossed UP (bar close 5.40, hist -0.00 -> +0.00)
[11:00:01] SKIP      buy 2026-10-27 25000 CE ignored - premium 5.40 is outside 144 - 1600
[11:00:01] SIGNAL    2026-10-27 21000 PE MACD crossed UP (bar close 20.90, hist -0.06 -> +0.01)
[11:00:01] SKIP      buy 2026-10-27 21000 PE ignored - premium 20.90 is outside 144 - 1600
[11:00:01] SIGNAL    2026-10-27 22000 PE MACD crossed UP (bar close 85.60, hist -0.15 -> +0.12)
[11:00:01] SKIP      buy 2026-10-27 22000 PE ignored - premium 85.60 is outside 144 - 1600
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
[10:55:53] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:59:33] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:00:03] SIGNAL    AXISBANK 1240 PE 27 Oct crossed EMA 144 at 39.30 - not taken: under EMA 55, momentum -5.4%
[11:00:03] SIGNAL    INFY 1040 PE 27 Oct crossed EMA 144 at 47.60 - not taken: under EMA 55
[11:00:03] SIGNAL    ADANIPOWER 205 PE 27 Oct crossed EMA 144 at 7.48 - not taken: under EMA 55, momentum 1.6%
[11:00:09] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

