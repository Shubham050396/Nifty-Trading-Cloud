# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:33 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.96 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹23,494 (+2.37%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,89,251 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹15,245 (+8.90%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,287 (-10.06%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹59,353** | **+₹15,452** | **−₹1,570** | **40** | **27** | **₹13,91,981** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:27:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:29:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:29:56] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:30:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:32:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:32:56] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:28:52] API       rate limited by Dhan - now one call every 15.1 s
[13:29:52] API       rate limited by Dhan - now one call every 15.1 s
[13:30:33] API       rate limited by Dhan - now one call every 15.1 s
[13:31:14] API       rate limited by Dhan - now one call every 15.1 s
[13:31:55] API       rate limited by Dhan - now one call every 15.1 s
[13:32:35] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:29:48] API       rate limited by Dhan - now one call every 15.1 s
[13:30:47] API       rate limited by Dhan - now one call every 15.1 s
[13:32:12] API       rate limited by Dhan - now one call every 15.1 s
[13:32:56] API       rate limited by Dhan - now one call every 15.1 s
[13:33:11] API       rate limited by Dhan - now one call every 15.1 s
[13:33:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:31:17] API       rate limited by Dhan - now one call every 5.1 s
[13:31:28] API       rate limited by Dhan - now one call every 6.1 s
[13:32:11] API       rate limited by Dhan - now one call every 5.1 s
[13:32:17] API       rate limited by Dhan - now one call every 7.1 s
[13:32:31] API       rate limited by Dhan - now one call every 10.1 s
[13:33:17] API       rate limited by Dhan - now one call every 13.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:57:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:59:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:01:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:02:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:30:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:32:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:30:39] SIGNAL    AXISBANK 1260 CE 27 Oct crossed EMA 144 at 23.55 - not taken: momentum -7.1%
[13:30:39] SIGNAL    ICICIBANK 1360 CE 27 Oct crossed EMA 144 at 22.50 - not taken: momentum 1.1%
[13:30:47] SKIP      LODHA 1100 PE 27 Oct signal at 31.55 skipped - 20 trades already today
[13:32:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:32:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:33:02] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:28:23] API       rate limited by Dhan - now one call every 15.1 s
[13:29:08] API       rate limited by Dhan - now one call every 15.1 s
[13:30:06] API       rate limited by Dhan - now one call every 15.1 s
[13:30:21] API       rate limited by Dhan - now one call every 15.1 s
[13:31:20] API       rate limited by Dhan - now one call every 15.1 s
[13:33:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

