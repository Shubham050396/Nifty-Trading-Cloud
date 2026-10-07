# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:09 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.00 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹27,768 (+2.81%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,703 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹15,538 (+9.07%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,283 (-9.82%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹59,353** | **+₹20,023** | **−₹1,570** | **40** | **27** | **₹13,97,153** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:52:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:52:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:58:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:58:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:05:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:05:04] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:59:42] API       rate limited by Dhan - now one call every 15.1 s
[14:00:03] API       rate limited by Dhan - now one call every 15.1 s
[14:06:49] API       rate limited by Dhan - now one call every 8.1 s
[14:07:10] API       rate limited by Dhan - now one call every 13.1 s
[14:07:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:07:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:04:08] API       rate limited by Dhan - now one call every 15.1 s
[14:04:24] API       rate limited by Dhan - now one call every 15.1 s
[14:05:36] API       rate limited by Dhan - now one call every 15.1 s
[14:06:34] API       rate limited by Dhan - now one call every 15.1 s
[14:07:32] API       rate limited by Dhan - now one call every 15.1 s
[14:08:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:04:08] VIX       India VIX prev close 13.61 - entries allowed
[14:04:16] API       rate limited by Dhan - now one call every 15.1 s
[14:05:14] API       rate limited by Dhan - now one call every 15.1 s
[14:06:12] API       rate limited by Dhan - now one call every 15.1 s
[14:07:10] API       rate limited by Dhan - now one call every 15.1 s
[14:07:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 13:57:06] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:59:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:01:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:03:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:05:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:07:51] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:05:15] SKIP      ICICIBANK 1360 CE 27 Oct signal at 22.70 skipped - 20 trades already today
[14:05:15] SKIP      DLF 640 PE 27 Oct signal at 11.40 skipped - 20 trades already today
[14:05:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:06:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:08:00] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:08:47] WARM      bar history loaded for all 790 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:03:44] API       rate limited by Dhan - now one call every 15.1 s
[14:04:28] API       rate limited by Dhan - now one call every 15.1 s
[14:04:58] API       rate limited by Dhan - now one call every 15.1 s
[14:07:20] API       rate limited by Dhan - now one call every 15.1 s
[14:08:04] API       rate limited by Dhan - now one call every 15.1 s
[14:09:03] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

