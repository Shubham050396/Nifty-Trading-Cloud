# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:08 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **13.60 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹7,917 (+6.92%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | ₹0 | +₹14,544 (+0.84%) | 4 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹4,558 (-17.18%) | +₹16,239 (+24.75%) | −₹17,960 (-10.44%) | 2 | 3 | ₹65,600 |
| **Total** | | **+₹28,501** | **+₹16,239** | **+₹6,132** | **10** | **3** | **₹65,600** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:04:10] VIX       India VIX 13.60 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-01 12:04:13] EXIT      closed 4 position(s) [VIX_KILL]
[2026-10-01 12:05:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:05:14] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:06:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:07:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:05:45] API       rate limited by Dhan - now one call every 15.1 s
[12:07:05] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:07:07] API       rate limited by Dhan - now one call every 15.1 s
[12:07:27] API       rate limited by Dhan - now one call every 15.1 s
[12:07:47] API       rate limited by Dhan - now one call every 15.1 s
[12:08:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:06:32] API       rate limited by Dhan - now one call every 15.1 s
[12:06:47] API       rate limited by Dhan - now one call every 15.1 s
[12:07:03] API       rate limited by Dhan - now one call every 15.1 s
[12:07:18] API       rate limited by Dhan - now one call every 15.1 s
[12:07:48] API       rate limited by Dhan - now one call every 15.1 s
[12:08:03] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:05:15] API       rate limited by Dhan - now one call every 5.1 s
[12:05:25] API       rate limited by Dhan - now one call every 6.1 s
[12:05:37] API       rate limited by Dhan - now one call every 8.1 s
[12:06:14] API       rate limited by Dhan - now one call every 9.1 s
[12:06:48] API       rate limited by Dhan - now one call every 12.1 s
[12:07:34] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:03:05] DATA      buffer cleared: day roll
[2026-10-01 12:03:05] RUN       scalper armed - started automatically on launch
[2026-10-01 12:03:06] BOOT      scrip master: 4064 NIFTY contracts
[2026-10-01 12:03:06] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [01/Oct/2026 06:33:10] "GET /api/state HTTP/1.1" 200 -
[2026-10-01 12:05:49] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:07:14] API       market quote: rate limited by Dhan - now one call every 3.0 s
[12:07:30] API       market quote: rate limited by Dhan - now one call every 2.5 s
[12:07:31] API       chart history: rate limited by Dhan - now one call every 1.2 s
[12:07:57] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:07:58] API       chart history: rate limited by Dhan - now one call every 1.2 s
[12:08:05] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

