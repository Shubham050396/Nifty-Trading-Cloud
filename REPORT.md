# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:10 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹982 (+0.33%) | ₹0 | 0 | 5 | ₹2,98,800 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | −₹406 (-2.64%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | −₹699 (-0.18%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,589 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹850 (+0.72%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹5,746** | **+₹727** | **−₹5,746** | **8** | **15** | **₹8,20,485** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:04:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:05:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:06:32] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:07:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:08:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:09:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:04:48] API       rate limited by Dhan - now one call every 15.1 s
[11:06:30] API       rate limited by Dhan - now one call every 15.1 s
[11:06:36] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:07:31] API       rate limited by Dhan - now one call every 15.1 s
[11:08:52] API       rate limited by Dhan - now one call every 15.1 s
[11:10:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:08:23] API       rate limited by Dhan - now one call every 15.1 s
[11:08:53] API       rate limited by Dhan - now one call every 15.1 s
[11:09:23] API       rate limited by Dhan - now one call every 15.1 s
[11:09:53] API       rate limited by Dhan - now one call every 15.1 s
[11:10:09] API       rate limited by Dhan - now one call every 15.1 s
[11:10:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:00:01] SIGNAL    2026-10-27 21000 PE MACD crossed UP (bar close 20.90, hist -0.06 -> +0.01)
[11:00:01] SKIP      buy 2026-10-27 21000 PE ignored - premium 20.90 is outside 144 - 1600
[11:00:01] SIGNAL    2026-10-27 22000 PE MACD crossed UP (bar close 85.60, hist -0.15 -> +0.12)
[11:00:01] SKIP      buy 2026-10-27 22000 PE ignored - premium 85.60 is outside 144 - 1600
[11:02:05] API       rate limited by Dhan - now one call every 5.1 s
[11:06:10] API       rate limited by Dhan - now one call every 5.1 s
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
[11:10:01] SIGNAL    INFY 940 PE 27 Oct crossed EMA 144 at 10.95 - not taken: under EMA 55
[11:10:03] SKIP      HCLTECH 1240 PE 27 Oct signal at 45.75 skipped - 5 positions already open
[11:10:03] SKIP      KOTAKBANK 420 CE 27 Oct signal at 7.80 skipped - 5 positions already open
[11:10:03] SKIP      TECHM 1500 PE 27 Oct signal at 33.15 skipped - 5 positions already open
[11:10:03] SKIP      HEROMOTOCO 5200 PE 27 Oct signal at 94.00 skipped - 5 positions already open
[11:10:03] SKIP      JINDALSTEL 1100 PE 27 Oct signal at 14.95 skipped - 5 positions already open
```
</details>

