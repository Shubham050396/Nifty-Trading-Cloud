# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 14:31 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.21** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹3,640 (+1.21%) | ₹0 | 0 | 5 | ₹3,01,458 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹5,203 (+8.71%) | +₹3,679 (+9.27%) | +₹5,203 (+8.71%) | 3 | 2 | ₹39,708 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹14,878 (+3.85%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,86,057 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | −₹1,272 (-1.34%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹23,761** | **+₹20,925** | **−₹23,761** | **27** | **16** | **₹8,22,435** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 14:27:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:27:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 14:28:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:29:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:30:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 14:31:44] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:28:04] API       rate limited by Dhan - now one call every 15.1 s
[14:29:25] API       rate limited by Dhan - now one call every 15.1 s
[14:29:45] API       rate limited by Dhan - now one call every 15.1 s
[14:30:47] API       rate limited by Dhan - now one call every 15.1 s
[14:31:00] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:31:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:30:25] API       rate limited by Dhan - now one call every 15.1 s
[14:30:42] VIX       India VIX prev close 13.41 -> target 1000 ticks (Rs 50.00)
[14:30:55] API       rate limited by Dhan - now one call every 15.1 s
[14:31:10] API       rate limited by Dhan - now one call every 15.1 s
[14:31:25] API       rate limited by Dhan - now one call every 15.1 s
[14:31:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:56:54] API       rate limited by Dhan - now one call every 5.1 s
[14:09:06] API       rate limited by Dhan - now one call every 5.1 s
[14:10:27] API       rate limited by Dhan - now one call every 5.1 s
[14:29:56] VIX       India VIX prev close 13.41 - entries allowed
[14:30:01] SIGNAL    2026-10-27 24000 CE MACD crossed DOWN (bar close 20.80, hist +0.01 -> -0.02)
[14:30:01] SKIP      short 2026-10-27 24000 CE ignored - premium 20.80 is outside 144 - 1600
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
[14:30:06] SIGNAL    DABUR 370 PE 27 Oct crossed EMA 144 at 4.25 - not taken: premium under Rs 5
[14:30:06] SIGNAL    GAIL 175 PE 27 Oct crossed EMA 144 at 5.00 - not taken: premium under Rs 5
[14:30:07] SKIP      LICI 390 PE 27 Oct signal at 5.30 skipped - 5 positions already open
[14:30:07] SKIP      ULTRACEMCO 11000 PE 27 Oct signal at 276.70 skipped - 5 positions already open
[14:30:24] WARM      bar history loaded for all 1580 contracts
[14:30:50] WARM      bar history loaded for all 1580 contracts
```
</details>

