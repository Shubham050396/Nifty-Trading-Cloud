# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 14:36 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹3,010 (+1.00%) | ₹0 | +₹3,010 (+1.00%) | 5 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹5,203 (+8.71%) | +₹2,993 (+7.54%) | +₹5,203 (+8.71%) | 3 | 2 | ₹39,708 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹18,811 (+4.88%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,85,842 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | −₹326 (-0.34%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹20,751** | **+₹21,478** | **−₹20,751** | **32** | **11** | **₹5,20,762** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 14:31:44] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:32:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:33:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:34:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:36:00] VIX       India VIX 13.61 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-09-30 14:36:03] EXIT      closed 5 position(s) [VIX_KILL]
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:31:07] API       rate limited by Dhan - now one call every 15.1 s
[14:32:28] API       rate limited by Dhan - now one call every 15.1 s
[14:33:29] API       rate limited by Dhan - now one call every 15.1 s
[14:33:49] API       rate limited by Dhan - now one call every 15.1 s
[14:36:12] API       rate limited by Dhan - now one call every 15.1 s
[14:36:32] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:35:28] API       rate limited by Dhan - now one call every 15.1 s
[14:35:43] API       rate limited by Dhan - now one call every 15.1 s
[14:35:59] API       rate limited by Dhan - now one call every 15.1 s
[14:36:14] SIGNAL    2026-10-06 22900 PE held above 270.95 for 5 min - fall-back exit is armed
[14:36:29] API       rate limited by Dhan - now one call every 15.1 s
[14:36:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:30:01] SIGNAL    2026-10-27 24000 CE MACD crossed DOWN (bar close 20.80, hist +0.01 -> -0.02)
[14:30:01] SKIP      short 2026-10-27 24000 CE ignored - premium 20.80 is outside 144 - 1600
[14:32:08] API       rate limited by Dhan - now one call every 5.1 s
[14:34:50] API       rate limited by Dhan - now one call every 5.1 s
[14:35:00] SIGNAL    2026-10-27 26000 CE MACD crossed UP (bar close 1.75, hist -0.00 -> +0.00)
[14:35:00] SKIP      buy 2026-10-27 26000 CE ignored - premium 1.75 is outside 144 - 1600
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
[14:30:24] WARM      bar history loaded for all 1580 contracts
[14:30:50] WARM      bar history loaded for all 1580 contracts
[14:35:04] SIGNAL    ADANIENT 2800 PE 27 Oct crossed EMA 144 at 47.00 - not taken: under EMA 55
[14:35:04] SIGNAL    GAIL 170 PE 27 Oct crossed EMA 144 at 2.69 - not taken: premium under Rs 5
[14:36:00] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:36:27] WARM      bar history loaded for all 1580 contracts
```
</details>

