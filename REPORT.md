# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:03 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **13.60 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹474 (+0.19%) | +₹3,010 (+1.00%) | 0 | 4 | ₹2,51,092 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹7,917 (+6.92%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | ₹0 | +₹14,544 (+0.84%) | 4 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹3,294 (+3.58%) | −₹13,402 (-9.21%) | 0 | 5 | ₹92,130 |
| **Total** | | **+₹32,802** | **+₹3,768** | **+₹10,434** | **4** | **9** | **₹3,43,222** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
serving NIFTY Credit Spreads on http://127.0.0.1:60817
[2026-10-01 12:03:06] BOOT      scrip master downloaded: 4064 NIFTY contracts in 4.9s
[2026-10-01 12:03:06] BOOT      Ready - 18 expiries, 4064 NIFTY contracts
[2026-10-01 12:03:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:03:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
127.0.0.1 - - [01/Oct/2026 06:33:10] "GET /api/status HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:03:02] CONTROL   started automatically on launch
[12:03:02] DAY       new session 2026-10-01
[12:03:02] VIX       India VIX 13.61 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[12:03:03] API       rate limited by Dhan - now one call every 5.1 s
[12:03:06] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [01/Oct/2026 06:33:10] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:03:09] GAP       2026-10-06 22900 PE: no prices for 1234 min - bar history restarts
[12:03:09] GAP       2026-10-06 23800 CE: no prices for 1234 min - bar history restarts
[12:03:09] GAP       2026-10-06 23800 PE: no prices for 1234 min - bar history restarts
[12:03:09] GAP       2026-10-06 21600 CE: no prices for 1234 min - bar history restarts
[12:03:09] GAP       2026-10-06 21600 PE: no prices for 1234 min - bar history restarts
127.0.0.1 - - [01/Oct/2026 06:33:10] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:03:04] EXIT      LONG 2026-10-27 23000 PE MACD_DOWN_MISSED @ 497.80  P&L Rs 7722.00
[12:03:06] BOOT      ready - 14 monthly expiries, 4064 contracts in the scrip master
[12:03:06] VIX       India VIX prev close 13.49 - entries allowed
[12:03:07] SIGNAL    2026-10-27 24000 PE: MACD crossed DOWN while prices were not being watched
[12:03:07] EXIT      LONG 2026-10-27 24000 PE MACD_DOWN_MISSED @ 1347.50  P&L Rs 11430.25
127.0.0.1 - - [01/Oct/2026 06:33:10] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:03:05] DAY       new session 2026-10-01 - counters reset (kill switch is NOT cleared)
[2026-10-01 12:03:05] DATA      buffer cleared: day roll
[2026-10-01 12:03:05] RUN       scalper armed - started automatically on launch
[2026-10-01 12:03:06] BOOT      scrip master: 4064 NIFTY contracts
[2026-10-01 12:03:06] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [01/Oct/2026 06:33:10] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:03:06] BOOT      scrip master downloaded in 5s: 213 stocks with options
[12:03:06] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[12:03:06] CONTROL   started automatically on launch - 99 stocks
[12:03:06] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:03:08] CONTRACT  watching 1386 contracts on 99 stocks (ATM +/- 3, CE/PE): 1381 added, 0 dropped
127.0.0.1 - - [01/Oct/2026 06:33:10] "GET /api/state HTTP/1.1" 200 -
```
</details>

