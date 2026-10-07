# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:38 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.92 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹22,396 (+2.26%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,89,402 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹13,831 (+8.08%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,293 (-10.06%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹59,353** | **+₹12,934** | **−₹1,570** | **40** | **27** | **₹13,92,132** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:32:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:32:56] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:34:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:34:57] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:37:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:37:58] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:35:59] API       rate limited by Dhan - now one call every 15.1 s
[13:36:04] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:36:39] API       rate limited by Dhan - now one call every 15.1 s
[13:38:01] API       rate limited by Dhan - now one call every 15.1 s
[13:38:06] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:38:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:35:49] API       rate limited by Dhan - now one call every 15.1 s
[13:36:04] API       rate limited by Dhan - now one call every 15.1 s
[13:36:20] API       rate limited by Dhan - now one call every 15.1 s
[13:36:35] API       rate limited by Dhan - now one call every 15.1 s
[13:37:33] API       rate limited by Dhan - now one call every 15.1 s
[13:38:32] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:32:11] API       rate limited by Dhan - now one call every 5.1 s
[13:32:17] API       rate limited by Dhan - now one call every 7.1 s
[13:32:31] API       rate limited by Dhan - now one call every 10.1 s
[13:33:17] API       rate limited by Dhan - now one call every 13.1 s
[13:35:08] API       rate limited by Dhan - now one call every 14.1 s
[13:38:45] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 13:02:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:30:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:32:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:34:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:36:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:37:58] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:35:08] SIGNAL    SOLARINDS 20000 CE 27 Oct crossed EMA 144 at 647.60 - not taken: momentum -8.9%
[13:35:08] SIGNAL    ITC 262.5 PE 27 Oct crossed EMA 144 at 3.75 - not taken: under EMA 55, premium under Rs 5
[13:36:34] API       market quote: rate limited by Dhan - now one call every 3.0 s
[13:36:43] API       market quote: rate limited by Dhan - now one call every 4.0 s
[13:36:51] API       market quote: rate limited by Dhan - now one call every 6.5 s
[13:36:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:34:29] API       rate limited by Dhan - now one call every 15.1 s
[13:34:44] API       rate limited by Dhan - now one call every 15.1 s
[13:36:45] API       rate limited by Dhan - now one call every 15.1 s
[13:37:29] API       rate limited by Dhan - now one call every 15.1 s
[13:37:44] API       rate limited by Dhan - now one call every 15.1 s
[13:38:29] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

