# NIFTY Cloud report

**Finished for the day at 15:15 IST** · updated 30 Sep 2026 15:15 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.57 🔴 above the limit** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | +₹3,010 (+1.00%) | ₹0 | +₹3,010 (+1.00%) | 5 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | +₹7,917 (+6.92%) | ₹0 | +₹7,917 (+6.92%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | −₹18,258 (-1.36%) | +₹22,776 (+5.91%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,85,694 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | −₹9,071 (-7.30%) | −₹1,654 (-1.74%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹18,037** | **+₹21,122** | **−₹18,037** | **35** | **9** | **₹4,80,906** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 15:10:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:12:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:12:11] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 15:13:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:14:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:12:31] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[15:12:46] API       rate limited by Dhan - now one call every 15.1 s
[15:13:06] API       rate limited by Dhan - now one call every 15.1 s
[15:14:07] API       rate limited by Dhan - now one call every 15.1 s
[15:14:27] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:13:37] API       rate limited by Dhan - now one call every 15.1 s
[15:13:52] API       rate limited by Dhan - now one call every 15.1 s
[15:14:22] API       rate limited by Dhan - now one call every 15.1 s
[15:14:37] API       rate limited by Dhan - now one call every 15.1 s
[15:14:53] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:40:03] SKIP      short 2026-10-27 26000 CE ignored - premium 1.60 is outside 144 - 1600
[14:40:16] API       rate limited by Dhan - now one call every 5.1 s
[14:45:01] SIGNAL    2026-10-27 26000 CE MACD crossed UP (bar close 2.00, hist -0.00 -> +0.01)
[14:45:01] SKIP      buy 2026-10-27 26000 CE ignored - premium 2.00 is outside 144 - 1600
[14:53:48] API       rate limited by Dhan - now one call every 5.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-09-30 09:29:47] RUN       scalper armed - started automatically on launch
[2026-09-30 09:29:48] BOOT      scrip master: 4036 NIFTY contracts
[2026-09-30 09:29:48] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
[2026-09-30 11:38:25] DATA      buffer gap > 15s - cleared, re-warming
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:12:56] API       chart history: rate limited by Dhan - now one call every 1.2 s
[15:13:27] WARM      bar history loaded for all 1584 contracts
[15:14:33] API       market quote: rate limited by Dhan - now one call every 2.0 s
[15:14:50] WARM      bar history loaded for all 1584 contracts
[15:14:58] WARM      bar history loaded for all 1584 contracts
cloud: shutdown requested - saving state
```
</details>

