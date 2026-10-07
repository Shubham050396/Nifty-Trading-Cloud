# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:54 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.73 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹43,192 (-1.74%) | −₹12,188 (-1.36%) | +₹29,114 (+0.41%) | 26 | 10 | ₹8,95,282 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,420 (-4.18%) | +₹18,730 (+12.37%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹26,072 (-10.73%) | ₹0 | 0 | 8 | ₹2,42,932 |
| **Total** | | **−₹54,730** | **−₹19,530** | **+₹3,053** | **51** | **26** | **₹12,89,622** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 14:48:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:49:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:50:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:51:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:52:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:53:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:49:50] API       rate limited by Dhan - now one call every 15.1 s
[14:51:12] API       rate limited by Dhan - now one call every 15.1 s
[14:51:52] API       rate limited by Dhan - now one call every 15.1 s
[14:52:33] API       rate limited by Dhan - now one call every 15.1 s
[14:53:54] API       rate limited by Dhan - now one call every 15.1 s
[14:54:00] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:52:11] GAP       2026-10-13 22900 PE: no prices for 5 min - bar history restarts
[14:52:11] GAP       2026-10-13 21500 CE: no prices for 5 min - bar history restarts
[14:52:11] GAP       2026-10-13 21500 PE: no prices for 5 min - bar history restarts
[14:52:11] GAP       2026-10-13 23700 CE: no prices for 5 min - bar history restarts
[14:52:11] GAP       2026-10-13 23700 PE: no prices for 5 min - bar history restarts
[14:54:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:49:52] API       rate limited by Dhan - now one call every 15.1 s
[14:51:16] API       rate limited by Dhan - now one call every 15.1 s
[14:51:32] API       rate limited by Dhan - now one call every 15.1 s
[14:51:47] API       rate limited by Dhan - now one call every 15.1 s
[14:53:12] API       rate limited by Dhan - now one call every 15.1 s
[14:53:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:45:26] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:47:29] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:49:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:51:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:53:02] HALT      HALTED: session over (15:25)
[2026-10-07 14:53:06] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:50:38] API       chart history: rate limited by Dhan - now one call every 1.2 s
[14:51:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:51:09] WARM      bar history loaded for all 791 contracts
[14:51:19] WARM      bar history loaded for all 791 contracts
[14:53:44] API       market quote: rate limited by Dhan - now one call every 5.0 s
[14:54:08] API       market quote: rate limited by Dhan - now one call every 7.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:46:22] API       rate limited by Dhan - now one call every 15.1 s
[14:47:07] API       rate limited by Dhan - now one call every 15.1 s
[14:47:51] API       rate limited by Dhan - now one call every 15.1 s
[14:50:31] API       rate limited by Dhan - now one call every 15.1 s
[14:51:43] API       rate limited by Dhan - now one call every 15.1 s
[14:53:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

