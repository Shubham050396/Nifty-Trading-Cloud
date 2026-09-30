# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:10 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,222 (+0.41%) | ₹0 | 0 | 5 | ₹2,99,040 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 | −₹1,297 (-8.42%) | 1 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹7,264 (-1.01%) | −₹1,232 (-0.51%) | −₹7,264 (-1.01%) | 7 | 4 | ₹2,43,407 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | −₹1,164 (-1.05%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹12,594** | **−₹1,174** | **−₹12,594** | **13** | **14** | **₹6,53,003** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 12:03:58] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 12:05:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:06:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:07:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:10:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:10:21] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:07:30] API       rate limited by Dhan - now one call every 15.1 s
[12:08:31] API       rate limited by Dhan - now one call every 15.1 s
[12:08:51] API       rate limited by Dhan - now one call every 15.1 s
[12:09:53] API       rate limited by Dhan - now one call every 15.1 s
[12:10:13] API       rate limited by Dhan - now one call every 15.1 s
[12:10:15] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:09:05] API       rate limited by Dhan - now one call every 15.1 s
[12:09:35] API       rate limited by Dhan - now one call every 15.1 s
[12:09:50] API       rate limited by Dhan - now one call every 15.1 s
[12:10:06] API       rate limited by Dhan - now one call every 15.1 s
[12:10:21] API       rate limited by Dhan - now one call every 15.1 s
[12:10:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:05:02] ENTRY     BUY 2026-10-27 23000 CE @ 229.10  (bar close 230.00, MACD hist +0.14, VIX 13.41)
[12:10:02] SIGNAL    2026-10-27 21000 CE MACD crossed UP (bar close 1845.00, hist -0.19 -> +0.29)
[12:10:02] SKIP      buy 2026-10-27 21000 CE ignored - premium 1845.00 is outside 144 - 1600
[12:10:02] SIGNAL    2026-10-27 24000 PE MACD crossed DOWN (bar close 1159.60, hist +0.19 -> -0.24)
[12:10:02] EXIT      LONG 2026-10-27 24000 PE MACD_DOWN @ 1161.80  P&L Rs -1417.00
[12:10:02] ENTRY     SELL SHORT 2026-10-27 24000 PE @ 1161.80  (bar close 1159.60, MACD hist -0.24, VIX 13.41)
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
[12:09:15] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:09:17] API       market quote: rate limited by Dhan - now one call every 3.0 s
[12:10:03] SIGNAL    ITC 260 PE 27 Oct crossed EMA 144 at 2.75 - not taken: premium under Rs 5
[12:10:03] SIGNAL    TATASTEEL 195 CE 27 Oct crossed EMA 144 at 3.38 - not taken: premium under Rs 5
[12:10:04] SKIP      ITC 270 PE 27 Oct signal at 7.00 skipped - 5 positions already open
[12:10:04] SKIP      SUNPHARMA 1900 PE 27 Oct signal at 69.00 skipped - 5 positions already open
```
</details>

