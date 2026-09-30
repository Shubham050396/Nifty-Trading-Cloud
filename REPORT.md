# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 12:21 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹2,051 (+0.68%) | ₹0 | 0 | 5 | ₹2,99,869 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 | −₹1,297 (-8.42%) | 1 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹8,824 (-1.01%) | −₹2,668 (-1.51%) | −₹8,824 (-1.01%) | 8 | 4 | ₹1,77,232 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,844 (-5.96%) | −₹384 (-0.42%) | −₹2,844 (-5.96%) | 2 | 4 | ₹91,176 |
| **Total** | | **−₹14,600** | **−₹1,001** | **−₹14,600** | **15** | **13** | **₹5,68,277** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 12:15:40] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:16:44] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:17:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:18:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:20:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 12:20:59] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:16:59] API       rate limited by Dhan - now one call every 15.1 s
[12:18:00] API       rate limited by Dhan - now one call every 15.1 s
[12:18:20] API       rate limited by Dhan - now one call every 15.1 s
[12:19:21] API       rate limited by Dhan - now one call every 15.1 s
[12:19:42] API       rate limited by Dhan - now one call every 15.1 s
[12:20:24] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:19:13] API       rate limited by Dhan - now one call every 15.1 s
[12:19:28] API       rate limited by Dhan - now one call every 15.1 s
[12:19:58] API       rate limited by Dhan - now one call every 15.1 s
[12:20:14] API       rate limited by Dhan - now one call every 15.1 s
[12:20:29] API       rate limited by Dhan - now one call every 15.1 s
[12:20:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:10:02] ENTRY     SELL SHORT 2026-10-27 24000 PE @ 1161.80  (bar close 1159.60, MACD hist -0.24, VIX 13.41)
[12:15:18] API       rate limited by Dhan - now one call every 5.1 s
[12:20:00] SIGNAL    2026-10-27 24000 PE MACD crossed UP (bar close 1182.30, hist -0.07 -> +0.18)
[12:20:00] EXIT      SHORT 2026-10-27 24000 PE MACD_UP @ 1185.80  P&L Rs -1560.00
[12:20:00] ENTRY     BUY 2026-10-27 24000 PE @ 1185.80  (bar close 1182.30, MACD hist +0.18, VIX 13.41)
[12:20:43] API       rate limited by Dhan - now one call every 5.1 s
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
[12:20:04] SIGNAL    ICICIBANK 1300 PE 27 Oct crossed EMA 144 at 16.50 - not taken: under EMA 55, momentum -1.5%
[12:20:04] SIGNAL    ITC 260 PE 27 Oct crossed EMA 144 at 2.75 - not taken: premium under Rs 5
[12:20:04] SIGNAL    DABUR 370 PE 27 Oct crossed EMA 144 at 4.20 - not taken: momentum -1.2%, premium under Rs 5
[12:20:04] SIGNAL    VBL 440 CE 27 Oct crossed EMA 144 at 10.35 - not taken: under EMA 55, momentum -3.3%
[12:20:04] SIGNAL    VEDL 250 PE 27 Oct crossed EMA 144 at 4.05 - not taken: momentum -15.6%, premium under Rs 5
[12:20:04] SIGNAL    TATAPOWER 350 PE 27 Oct crossed EMA 144 at 3.70 - not taken: momentum -9.8%, premium under Rs 5
```
</details>

