# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:51 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.13** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹2,096 (+0.70%) | ₹0 | 0 | 5 | ₹2,99,915 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | +₹1,066 (+4.78%) | +₹1,953 (+5.22%) | 2 | 1 | ₹22,311 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | −₹3,045 (-0.84%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,60,951 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹984 (+1.03%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹22,445** | **+₹1,101** | **−₹22,445** | **22** | **15** | **₹7,78,389** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:47:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:47:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:48:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:49:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:50:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:51:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:46:24] API       rate limited by Dhan - now one call every 15.1 s
[13:46:25] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:47:25] API       rate limited by Dhan - now one call every 15.1 s
[13:49:07] API       rate limited by Dhan - now one call every 15.1 s
[13:50:28] API       rate limited by Dhan - now one call every 15.1 s
[13:51:29] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:49:45] API       rate limited by Dhan - now one call every 15.1 s
[13:50:00] API       rate limited by Dhan - now one call every 15.1 s
[13:50:15] API       rate limited by Dhan - now one call every 15.1 s
[13:50:46] API       rate limited by Dhan - now one call every 15.1 s
[13:51:16] API       rate limited by Dhan - now one call every 15.1 s
[13:51:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:29:54] VIX       India VIX prev close 13.41 - entries allowed
[13:33:52] API       rate limited by Dhan - now one call every 5.1 s
[13:48:47] API       rate limited by Dhan - now one call every 5.1 s
[13:50:01] SIGNAL    2026-10-27 22000 PE MACD crossed UP (bar close 77.20, hist -0.08 -> +0.16)
[13:50:01] SKIP      buy 2026-10-27 22000 PE ignored - premium 77.20 is outside 144 - 1600
[13:50:08] API       rate limited by Dhan - now one call every 5.1 s
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
[13:50:02] SIGNAL    SHRIRAMFIN 960 PE 27 Oct crossed EMA 144 at 18.55 - not taken: under EMA 55, momentum 1.4%
[13:50:02] SIGNAL    TATASTEEL 180 CE 27 Oct crossed EMA 144 at 10.95 - not taken: under EMA 55, momentum -4.4%
[13:50:02] SIGNAL    BEL 370 PE 27 Oct crossed EMA 144 at 2.90 - not taken: under EMA 55, premium under Rs 5
[13:50:04] SKIP      DABUR 380 PE 27 Oct signal at 7.20 skipped - 5 positions already open
[13:50:04] SKIP      DABUR 390 PE 27 Oct signal at 12.45 skipped - 5 positions already open
[13:51:30] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

