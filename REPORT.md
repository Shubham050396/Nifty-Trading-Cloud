# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:58 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.94 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹32,682 (+3.31%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,272 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹15,586 (+9.10%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹22,529 (-9.50%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹59,353** | **+₹25,739** | **−₹1,570** | **40** | **27** | **₹13,96,722** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:49:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:50:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:52:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:52:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:58:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:58:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:55:19] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:55:38] API       rate limited by Dhan - now one call every 15.1 s
[13:56:19] API       rate limited by Dhan - now one call every 15.1 s
[13:56:39] API       rate limited by Dhan - now one call every 15.1 s
[13:56:59] API       rate limited by Dhan - now one call every 15.1 s
[13:58:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:54:02] API       rate limited by Dhan - now one call every 15.1 s
[13:55:51] API       rate limited by Dhan - now one call every 15.1 s
[13:56:06] API       rate limited by Dhan - now one call every 15.1 s
[13:56:21] API       rate limited by Dhan - now one call every 15.1 s
[13:56:52] API       rate limited by Dhan - now one call every 15.1 s
[13:57:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:55:27] API       rate limited by Dhan - now one call every 5.1 s
[13:55:55] API       rate limited by Dhan - now one call every 5.1 s
[13:56:37] API       rate limited by Dhan - now one call every 5.1 s
[13:56:55] API       rate limited by Dhan - now one call every 5.1 s
[13:57:05] API       rate limited by Dhan - now one call every 6.1 s
[13:58:05] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 13:47:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:49:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:51:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:53:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:55:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:57:06] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:55:19] SKIP      LODHA 1100 PE 27 Oct signal at 31.75 skipped - 20 trades already today
[13:56:00] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:57:02] WARM      bar history loaded for all 790 contracts
[13:58:23] API       market quote: rate limited by Dhan - now one call every 7.0 s
[13:58:46] WARM      bar history loaded for all 790 contracts
[13:58:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:56:06] API       rate limited by Dhan - now one call every 15.1 s
[13:56:22] API       rate limited by Dhan - now one call every 15.1 s
[13:56:52] API       rate limited by Dhan - now one call every 15.1 s
[13:57:22] API       rate limited by Dhan - now one call every 15.1 s
[13:57:38] API       rate limited by Dhan - now one call every 15.1 s
[13:58:22] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

