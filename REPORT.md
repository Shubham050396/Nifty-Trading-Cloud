# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:52 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.79 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹494 (-2.15%) | +₹20,280 (+5.68%) | 1 | 1 | ₹22,987 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹26,748 (-3.92%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,83,163 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | +₹2,570 (+1.21%) | −₹45,941 (-4.70%) | 12 | 10 | ₹2,12,025 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,867 (-8.11%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹9,044** | **−₹42,539** | **+₹48,740** | **13** | **25** | **₹11,38,507** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:35:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:35:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:39:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:39:20] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:51:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:51:22] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:46:31] API       rate limited by Dhan - now one call every 15.1 s
[10:47:11] API       rate limited by Dhan - now one call every 15.1 s
[10:48:12] API       rate limited by Dhan - now one call every 15.1 s
[10:48:32] API       rate limited by Dhan - now one call every 15.1 s
[10:49:53] API       rate limited by Dhan - now one call every 15.1 s
[10:51:06] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:49:29] API       rate limited by Dhan - now one call every 15.1 s
[10:49:45] API       rate limited by Dhan - now one call every 15.1 s
[10:50:15] API       rate limited by Dhan - now one call every 15.1 s
[10:51:13] API       rate limited by Dhan - now one call every 15.1 s
[10:51:43] API       rate limited by Dhan - now one call every 15.1 s
[10:52:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:49:46] API       rate limited by Dhan - now one call every 6.1 s
[10:50:30] API       rate limited by Dhan - now one call every 5.1 s
[10:50:55] API       rate limited by Dhan - now one call every 5.1 s
[10:51:17] API       rate limited by Dhan - now one call every 5.1 s
[10:51:42] API       rate limited by Dhan - now one call every 5.1 s
[10:52:30] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:43:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:44:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:46:29] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:48:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:50:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:52:27] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:48:22] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:48:33] WARM      bar history loaded for all 782 contracts
[10:49:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:50:05] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:50:32] ENTRY     BUY DRREDDY 1220 CE 27 Oct x625 @ 28.60 (signal close 28.65, EMA 144 28.04, momentum 6.1%)  quick 32.89 till 11:20, target 48.62, stop below EMA 55
[10:50:32] ENTRY     BUY ADANIPORTS 1760 CE 27 Oct x475 @ 54.45 (signal close 52.20, EMA 144 51.96, momentum 8.8%)  quick 62.62 till 11:20, target 92.56, stop below EMA 55
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:49:14] API       rate limited by Dhan - now one call every 15.1 s
[10:49:29] API       rate limited by Dhan - now one call every 15.1 s
[10:50:41] API       rate limited by Dhan - now one call every 15.1 s
[10:50:56] API       rate limited by Dhan - now one call every 15.1 s
[10:51:11] API       rate limited by Dhan - now one call every 15.1 s
[10:51:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

