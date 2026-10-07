# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:07 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.69 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | +₹2,174 (+3.58%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹32,659 (-6.11%) | +₹2,018 (+0.22%) | +₹39,647 (+0.76%) | 5 | 10 | ₹9,09,306 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | +₹3,842 (+1.81%) | −₹45,941 (-4.70%) | 12 | 10 | ₹2,12,025 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹14,256 (-6.47%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹41,703** | **−₹6,222** | **+₹16,081** | **18** | **31** | **₹14,02,373** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:02:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:02:24] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:03:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:04:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:05:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:06:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:02:06] API       rate limited by Dhan - now one call every 15.1 s
[11:04:13] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:04:49] API       rate limited by Dhan - now one call every 15.1 s
[11:05:50] API       rate limited by Dhan - now one call every 15.1 s
[11:06:10] API       rate limited by Dhan - now one call every 15.1 s
[11:07:32] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:07:24] GAP       2026-10-27 22000 PE: no prices for 4 min - bar history restarts
[11:07:24] GAP       2026-10-27 22900 PE: no prices for 4 min - bar history restarts
[11:07:24] GAP       2026-10-27 21500 CE: no prices for 4 min - bar history restarts
[11:07:24] GAP       2026-10-27 21500 PE: no prices for 4 min - bar history restarts
[11:07:24] GAP       2026-10-27 23700 CE: no prices for 4 min - bar history restarts
[11:07:24] GAP       2026-10-27 23700 PE: no prices for 4 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:05:38] EXIT      LONG 2027-03-30 24000 PE MACD_DOWN @ 1061.35  P&L Rs -8225.75
[11:05:38] ENTRY     SELL SHORT 2027-03-30 24000 PE @ 1061.35  (bar close 1065.00, MACD hist -0.17, VIX 13.61)
[11:06:57] API       rate limited by Dhan - now one call every 5.1 s
[11:07:03] API       rate limited by Dhan - now one call every 7.1 s
[11:07:29] API       rate limited by Dhan - now one call every 8.1 s
[11:07:37] API       rate limited by Dhan - now one call every 13.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:56:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:58:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:00:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:02:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:03:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:06:23] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:07:14] WARM      bar history loaded for all 782 contracts
[11:07:15] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:07:26] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:07:28] API       market quote: rate limited by Dhan - now one call every 3.0 s
[11:07:31] API       market quote: rate limited by Dhan - now one call every 5.0 s
[11:07:36] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:05:09] API       rate limited by Dhan - now one call every 15.1 s
[11:05:25] API       rate limited by Dhan - now one call every 15.1 s
[11:06:37] API       rate limited by Dhan - now one call every 15.1 s
[11:06:52] API       rate limited by Dhan - now one call every 15.1 s
[11:07:07] API       rate limited by Dhan - now one call every 15.1 s
[11:07:23] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

