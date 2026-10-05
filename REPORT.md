# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:38 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.67 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+1.36%) | ₹0 | +₹21,548 (+7.07%) | 4 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹34,746 (+5.68%) | +₹309 (+0.06%) | +₹71,185 (+2.60%) | 6 | 5 | ₹5,48,990 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹6,489 (-5.94%) | −₹2,212 (-0.49%) | 6 | 6 | ₹1,09,151 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹2,606 (-4.30%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹33,750** | **−₹8,786** | **+₹92,214** | **16** | **15** | **₹7,18,760** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:19:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:27:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:27:24] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:36:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:36:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:37:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:33:26] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:34:46] API       rate limited by Dhan - now one call every 15.1 s
[11:37:29] API       rate limited by Dhan - now one call every 15.1 s
[11:38:10] API       rate limited by Dhan - now one call every 15.1 s
[11:38:30] API       rate limited by Dhan - now one call every 15.1 s
[11:38:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:37:25] GAP       2026-10-27 22000 PE: no prices for 4 min - bar history restarts
[11:37:25] GAP       2026-10-27 22900 PE: no prices for 4 min - bar history restarts
[11:37:25] GAP       2026-10-27 21500 CE: no prices for 4 min - bar history restarts
[11:37:25] GAP       2026-10-27 21500 PE: no prices for 4 min - bar history restarts
[11:37:39] API       rate limited by Dhan - now one call every 15.1 s
[11:38:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:35:43] EXIT      SHORT 2026-10-27 22000 PE MACD_UP @ 122.85  P&L Rs 3185.00
[11:35:43] SKIP      buy 2026-10-27 22000 PE ignored - premium 128.65 is outside 144 - 1600
[11:35:43] SIGNAL    2026-10-27 23000 CE MACD crossed DOWN (bar close 140.60, hist +0.19 -> -0.02)
[11:35:43] SKIP      short 2026-10-27 23000 CE ignored - premium 140.60 is outside 144 - 1600
[11:38:35] API       rate limited by Dhan - now one call every 5.1 s
[11:38:52] VIX       India VIX prev close 14.46 - entries allowed
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:25:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:26:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:31:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:34:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:35:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:37:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:35:18] SIGNAL    VBL 430 CE 27 Oct crossed EMA 144 at 14.35 - not taken: momentum -6.5%
[11:35:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:35:56] WARM      bar history loaded for all 756 contracts
[11:36:28] WARM      bar history loaded for all 756 contracts
[11:37:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:37:20] WARM      bar history loaded for all 758 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:34:26] API       rate limited by Dhan - now one call every 15.1 s
[11:35:38] API       rate limited by Dhan - now one call every 15.1 s
[11:36:50] API       rate limited by Dhan - now one call every 15.1 s
[11:37:49] API       rate limited by Dhan - now one call every 15.1 s
[11:38:06] VIX       India VIX prev close 14.46
[11:38:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

