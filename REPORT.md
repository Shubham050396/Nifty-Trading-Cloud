# NIFTY Cloud report

**Running until 15:15 IST** · updated 06 Oct 2026 14:45 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **13.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹19,867 (+3.47%) | −₹39,117 (-5.72%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,84,103 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,415 (-22.41%) | +₹5,801 (+7.61%) | −₹41,790 (-5.37%) | 3 | 4 | ₹76,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,381 (-11.99%) | ₹0 | 0 | 8 | ₹1,53,295 |
| **Total** | | **+₹5,452** | **−₹51,697** | **+₹54,159** | **7** | **18** | **₹9,13,656** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 14:37:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:38:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:40:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:40:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:41:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:42:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:40:24] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:41:05] API       rate limited by Dhan - now one call every 15.1 s
[14:42:06] API       rate limited by Dhan - now one call every 15.1 s
[14:43:07] API       rate limited by Dhan - now one call every 15.1 s
[14:43:48] API       rate limited by Dhan - now one call every 15.1 s
[14:44:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:42:52] GAP       2026-10-13 21500 CE: no prices for 4 min - bar history restarts
[14:42:52] GAP       2026-10-13 21500 PE: no prices for 4 min - bar history restarts
[14:42:52] GAP       2026-10-13 23700 CE: no prices for 4 min - bar history restarts
[14:42:52] GAP       2026-10-13 23700 PE: no prices for 4 min - bar history restarts
[14:43:42] API       rate limited by Dhan - now one call every 15.1 s
[14:45:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:36:54] API       rate limited by Dhan - now one call every 11.1 s
[14:37:16] API       rate limited by Dhan - now one call every 15.1 s
[14:38:28] API       rate limited by Dhan - now one call every 15.1 s
[14:41:00] API       rate limited by Dhan - now one call every 15.1 s
[14:41:58] API       rate limited by Dhan - now one call every 15.1 s
[14:42:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/state HTTP/1.1" 200 -
[2026-10-06 14:36:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:38:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:40:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:42:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:44:08] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:43:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:43:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:43:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:44:19] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:45:10] SIGNAL    ABB 7100 CE 27 Oct crossed EMA 144 at 225.35 - not taken: momentum -2.9%
[14:45:18] SKIP      DIVISLAB 9600 CE 27 Oct signal at 200.60 skipped - already 1 open on DIVISLAB
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:39:07] API       rate limited by Dhan - now one call every 15.1 s
[14:40:05] API       rate limited by Dhan - now one call every 15.1 s
[14:41:42] API       rate limited by Dhan - now one call every 15.1 s
[14:43:07] API       rate limited by Dhan - now one call every 15.1 s
[14:44:05] API       rate limited by Dhan - now one call every 15.1 s
[14:44:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

