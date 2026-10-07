# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:57 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.66 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | +₹413 (+0.91%) | +₹20,280 (+5.68%) | 1 | 2 | ₹45,480 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹32,276 (-4.72%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,83,823 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | +₹4,833 (+2.28%) | −₹45,941 (-4.70%) | 12 | 10 | ₹2,12,025 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,697 (-7.58%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹9,044** | **−₹43,727** | **+₹48,740** | **13** | **26** | **₹11,61,660** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:39:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:39:20] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:51:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:51:22] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:54:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:54:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:49:53] API       rate limited by Dhan - now one call every 15.1 s
[10:51:06] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:52:36] API       rate limited by Dhan - now one call every 15.1 s
[10:53:17] API       rate limited by Dhan - now one call every 15.1 s
[10:54:38] API       rate limited by Dhan - now one call every 15.1 s
[10:56:00] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:57:33] GAP       2026-10-27 22000 PE: no prices for 4 min - bar history restarts
[10:57:33] GAP       2026-10-27 22900 PE: no prices for 4 min - bar history restarts
[10:57:33] GAP       2026-10-27 21500 CE: no prices for 4 min - bar history restarts
[10:57:33] GAP       2026-10-27 21500 PE: no prices for 4 min - bar history restarts
[10:57:33] GAP       2026-10-27 23700 CE: no prices for 4 min - bar history restarts
[10:57:33] GAP       2026-10-27 23700 PE: no prices for 4 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:55:36] API       rate limited by Dhan - now one call every 5.1 s
[10:56:01] API       rate limited by Dhan - now one call every 5.1 s
[10:56:26] API       rate limited by Dhan - now one call every 5.1 s
[10:56:51] API       rate limited by Dhan - now one call every 5.1 s
[10:57:16] API       rate limited by Dhan - now one call every 5.1 s
[10:57:22] API       rate limited by Dhan - now one call every 7.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:46:29] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:48:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:50:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:52:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:54:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:56:24] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:53:56] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:54:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:54:17] WARM      bar history loaded for all 782 contracts
[10:55:13] SIGNAL    WIPRO 165 PE 27 Oct crossed EMA 144 at 7.02 - not taken: under EMA 55, momentum 2.0%
[10:55:20] SKIP      ETERNAL 330 CE 27 Oct signal at 10.60 skipped - 10 positions already open
[10:55:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:50:56] API       rate limited by Dhan - now one call every 15.1 s
[10:51:11] API       rate limited by Dhan - now one call every 15.1 s
[10:51:56] API       rate limited by Dhan - now one call every 15.1 s
[10:53:45] API       rate limited by Dhan - now one call every 15.1 s
[10:55:56] API       rate limited by Dhan - now one call every 15.1 s
[10:56:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

