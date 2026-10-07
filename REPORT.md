# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:23 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.84 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹34,505 (+3.49%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,618 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹16,938 (+9.89%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹22,907 (-9.90%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹59,353** | **+₹28,536** | **−₹1,570** | **40** | **27** | **₹13,91,348** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:16:53] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:17:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:18:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:19:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:21:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:21:54] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:19:02] API       rate limited by Dhan - now one call every 15.1 s
[13:19:43] API       rate limited by Dhan - now one call every 15.1 s
[13:20:24] API       rate limited by Dhan - now one call every 15.1 s
[13:20:54] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:21:04] API       rate limited by Dhan - now one call every 15.1 s
[13:21:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:20:29] API       rate limited by Dhan - now one call every 15.1 s
[13:20:59] API       rate limited by Dhan - now one call every 15.1 s
[13:21:57] API       rate limited by Dhan - now one call every 15.1 s
[13:22:27] API       rate limited by Dhan - now one call every 15.1 s
[13:22:57] API       rate limited by Dhan - now one call every 15.1 s
[13:23:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:15:36] API       rate limited by Dhan - now one call every 5.1 s
[13:16:34] API       rate limited by Dhan - now one call every 5.1 s
[13:17:32] API       rate limited by Dhan - now one call every 5.1 s
[13:19:24] API       rate limited by Dhan - now one call every 5.1 s
[13:21:30] API       rate limited by Dhan - now one call every 5.1 s
[13:22:28] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:54:12] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:55:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:57:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:59:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:01:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:02:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:19:59] WARM      bar history loaded for all 790 contracts
[13:20:02] SIGNAL    ETERNAL 330 CE 27 Oct crossed EMA 144 at 10.55 - not taken: momentum -4.1%
[13:20:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:21:26] WARM      bar history loaded for all 790 contracts
[13:22:54] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:22:57] API       market quote: rate limited by Dhan - now one call every 3.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:16:45] API       rate limited by Dhan - now one call every 15.1 s
[13:17:00] API       rate limited by Dhan - now one call every 15.1 s
[13:18:37] API       rate limited by Dhan - now one call every 15.1 s
[13:20:38] API       rate limited by Dhan - now one call every 15.1 s
[13:21:49] API       rate limited by Dhan - now one call every 15.1 s
[13:22:48] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

