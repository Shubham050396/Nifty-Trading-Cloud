# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:05 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,245 (+0.42%) | ₹0 | 0 | 5 | ₹2,99,063 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 | −₹1,297 (-8.42%) | 1 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹5,847 (-0.91%) | −₹2,717 (-1.53%) | −₹5,847 (-0.91%) | 6 | 4 | ₹1,77,089 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | −₹586 (-0.53%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹11,177** | **−₹2,058** | **−₹11,177** | **12** | **14** | **₹5,86,708** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 12:00:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:00:46] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:01:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:03:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:03:58] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:05:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:02:05] API       rate limited by Dhan - now one call every 15.1 s
[12:03:06] API       rate limited by Dhan - now one call every 15.1 s
[12:03:26] API       rate limited by Dhan - now one call every 15.1 s
[12:04:27] API       rate limited by Dhan - now one call every 15.1 s
[12:04:48] API       rate limited by Dhan - now one call every 15.1 s
[12:05:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:03:31] API       rate limited by Dhan - now one call every 15.1 s
[12:03:46] API       rate limited by Dhan - now one call every 15.1 s
[12:04:17] API       rate limited by Dhan - now one call every 15.1 s
[12:04:32] API       rate limited by Dhan - now one call every 15.1 s
[12:05:02] API       rate limited by Dhan - now one call every 15.1 s
[12:05:33] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:05:02] SIGNAL    2026-10-27 22000 CE MACD crossed UP (bar close 927.60, hist -0.22 -> +0.60)
[12:05:02] EXIT      SHORT 2026-10-27 22000 CE MACD_UP @ 918.85  P&L Rs -1404.00
[12:05:02] ENTRY     BUY 2026-10-27 22000 CE @ 918.85  (bar close 927.60, MACD hist +0.60, VIX 13.41)
[12:05:02] SIGNAL    2026-10-27 23000 CE MACD crossed UP (bar close 230.00, hist -0.13 -> +0.14)
[12:05:02] EXIT      SHORT 2026-10-27 23000 CE MACD_UP @ 229.10  P&L Rs -331.50
[12:05:02] ENTRY     BUY 2026-10-27 23000 CE @ 229.10  (bar close 230.00, MACD hist +0.14, VIX 13.41)
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
[12:01:53] WARM      bar history loaded for all 1564 contracts
[12:02:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:05:01] SIGNAL    INFY 960 PE 27 Oct crossed EMA 144 at 15.60 - not taken: under EMA 55, momentum -0.3%
[12:05:01] SIGNAL    INFY 980 PE 27 Oct crossed EMA 144 at 21.85 - not taken: under EMA 55, momentum 0.9%
[12:05:01] SIGNAL    VBL 450 CE 27 Oct crossed EMA 144 at 7.10 - not taken: under EMA 55, momentum -2.7%
[12:05:02] SKIP      TVSMOTOR 4100 CE 27 Oct signal at 162.10 skipped - 5 positions already open
```
</details>

