# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 14:41 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹3,010 (+1.00%) | ₹0 | +₹3,010 (+1.00%) | 5 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹8,453 (+11.12%) | +₹1,566 (+4.09%) | +₹8,453 (+11.12%) | 4 | 2 | ₹38,327 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹21,733 (+5.64%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,85,655 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | −₹1,120 (-1.18%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹17,501** | **+₹22,179** | **−₹17,501** | **33** | **11** | **₹5,19,194** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 14:36:03] EXIT      closed 5 position(s) [VIX_KILL]
[2026-09-30 14:37:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:37:04] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 14:38:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:39:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:40:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:37:33] API       rate limited by Dhan - now one call every 15.1 s
[14:37:53] API       rate limited by Dhan - now one call every 15.1 s
[14:38:54] API       rate limited by Dhan - now one call every 15.1 s
[14:39:14] API       rate limited by Dhan - now one call every 15.1 s
[14:41:08] VIX       India VIX 13.62 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[14:41:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:40:01] API       rate limited by Dhan - now one call every 15.1 s
[14:40:17] API       rate limited by Dhan - now one call every 15.1 s
[14:40:32] ENTRY     L2 BUY 2026-10-06 22800 PE @ 229.70  target 279.70  trail 195.24 (15%)
[14:40:47] API       rate limited by Dhan - now one call every 15.1 s
[14:41:17] API       rate limited by Dhan - now one call every 15.1 s
[14:41:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:34:50] API       rate limited by Dhan - now one call every 5.1 s
[14:35:00] SIGNAL    2026-10-27 26000 CE MACD crossed UP (bar close 1.75, hist -0.00 -> +0.00)
[14:35:00] SKIP      buy 2026-10-27 26000 CE ignored - premium 1.75 is outside 144 - 1600
[14:40:03] SIGNAL    2026-10-27 26000 CE MACD crossed DOWN (bar close 1.60, hist +0.00 -> -0.00)
[14:40:03] SKIP      short 2026-10-27 26000 CE ignored - premium 1.60 is outside 144 - 1600
[14:40:16] API       rate limited by Dhan - now one call every 5.1 s
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
[14:40:04] SIGNAL    ADANIPOWER 195 PE 27 Oct crossed EMA 144 at 3.70 - not taken: under EMA 55, premium under Rs 5
[14:40:04] SIGNAL    ADANIPOWER 200 PE 27 Oct crossed EMA 144 at 5.55 - not taken: under EMA 55
[14:40:04] SIGNAL    ADANIPOWER 210 PE 27 Oct crossed EMA 144 at 11.13 - not taken: under EMA 55
[14:40:04] SIGNAL    DABUR 370 PE 27 Oct crossed EMA 144 at 4.20 - not taken: premium under Rs 5
[14:41:05] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:41:09] API       market quote: rate limited by Dhan - now one call every 2.5 s
```
</details>

