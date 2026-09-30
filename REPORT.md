# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 13:31 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.96** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹946 (+0.32%) | ₹0 | 0 | 5 | ₹2,98,764 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,953 (+5.22%) | ₹0 | +₹1,953 (+5.22%) | 2 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹13,692 (-1.41%) | +₹5,778 (+1.60%) | −₹13,692 (-1.41%) | 10 | 4 | ₹3,61,578 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | +₹259 (+0.27%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹22,445** | **+₹6,983** | **−₹22,445** | **22** | **14** | **₹7,55,554** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 13:23:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:24:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:25:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:27:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 13:27:57] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 13:29:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:27:26] API       rate limited by Dhan - now one call every 15.1 s
[13:28:27] API       rate limited by Dhan - now one call every 15.1 s
[13:28:47] API       rate limited by Dhan - now one call every 15.1 s
[13:29:48] API       rate limited by Dhan - now one call every 15.1 s
[13:30:09] API       rate limited by Dhan - now one call every 15.1 s
[13:31:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:29:47] API       rate limited by Dhan - now one call every 15.1 s
[13:30:17] API       rate limited by Dhan - now one call every 15.1 s
[13:30:34] VIX       India VIX prev close 13.41 -> target 1000 ticks (Rs 50.00)
[13:30:47] API       rate limited by Dhan - now one call every 15.1 s
[13:31:02] API       rate limited by Dhan - now one call every 15.1 s
[13:31:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:35:02] SIGNAL    2026-10-27 22000 PE MACD crossed DOWN (bar close 71.15, hist +0.16 -> -0.03)
[12:35:02] SKIP      short 2026-10-27 22000 PE ignored - premium 71.15 is outside 144 - 1600
[13:02:43] API       rate limited by Dhan - now one call every 5.1 s
[13:12:11] API       rate limited by Dhan - now one call every 5.1 s
[13:21:41] API       rate limited by Dhan - now one call every 5.1 s
[13:29:54] VIX       India VIX prev close 13.41 - entries allowed
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
[13:30:02] SIGNAL    ICICIBANK 1340 PE 27 Oct crossed EMA 144 at 30.55 - not taken: under EMA 55
[13:30:02] SIGNAL    HAL 4500 PE 27 Oct crossed EMA 144 at 40.75 - not taken: momentum -2.6%
[13:30:02] SIGNAL    ICICIBANK 1360 PE 27 Oct crossed EMA 144 at 41.70 - not taken: under EMA 55, momentum 2.3%
[13:30:04] SKIP      HDFCBANK 720 PE 27 Oct signal at 17.20 skipped - 5 positions already open
[13:30:05] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:31:09] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

