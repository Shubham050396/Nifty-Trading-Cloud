# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:17 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.02 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹18,535 (-2.72%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,82,628 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹3,048 (+2.69%) | +₹1,171 (+0.64%) | −₹35,118 (-3.83%) | 8 | 10 | ₹1,82,044 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,673 (-8.71%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹3,048** | **−₹36,037** | **+₹60,831** | **8** | **24** | **₹10,79,050** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:57:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:58:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:03:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:03:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:16:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:16:15] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:12:36] API       rate limited by Dhan - now one call every 15.1 s
[10:13:17] API       rate limited by Dhan - now one call every 15.1 s
[10:13:37] API       rate limited by Dhan - now one call every 15.1 s
[10:14:38] API       rate limited by Dhan - now one call every 15.1 s
[10:15:42] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:16:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:14:21] API       rate limited by Dhan - now one call every 15.1 s
[10:15:08] VIX       India VIX prev close 13.61 -> target 1000 ticks (Rs 50.00)
[10:15:20] API       rate limited by Dhan - now one call every 15.1 s
[10:16:18] API       rate limited by Dhan - now one call every 15.1 s
[10:17:03] API       rate limited by Dhan - now one call every 15.1 s
[10:17:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:07:23] API       rate limited by Dhan - now one call every 15.1 s
[10:09:54] API       rate limited by Dhan - now one call every 15.1 s
[10:13:00] API       rate limited by Dhan - now one call every 12.1 s
[10:13:24] API       rate limited by Dhan - now one call every 15.1 s
[10:15:24] API       rate limited by Dhan - now one call every 15.1 s
[10:15:39] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:09:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:12:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:14:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:14:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:15:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:17:01] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:15:20] ENTRY     BUY ABB 7000 CE 27 Oct x125 @ 269.95 (signal close 265.00, EMA 144 264.53, momentum 14.6%)  quick 310.44 till 10:45, target 458.91, stop below EMA 55
[10:15:30] WARM      bar history loaded for all 780 contracts
[10:15:33] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:15:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:15:53] WARM      bar history loaded for all 780 contracts
[10:17:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:14:52] API       rate limited by Dhan - now one call every 15.1 s
[10:15:37] API       rate limited by Dhan - now one call every 15.1 s
[10:15:52] API       rate limited by Dhan - now one call every 15.1 s
[10:16:08] API       rate limited by Dhan - now one call every 15.1 s
[10:16:38] API       rate limited by Dhan - now one call every 15.1 s
[10:17:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

