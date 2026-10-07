# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:44 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹43,885 (-1.82%) | −₹566 (-0.07%) | +₹28,421 (+0.40%) | 25 | 10 | ₹8,24,361 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,420 (-4.18%) | +₹16,664 (+11.01%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹24,863 (-10.23%) | ₹0 | 0 | 8 | ₹2,42,932 |
| **Total** | | **−₹55,423** | **−₹8,765** | **+₹2,360** | **50** | **26** | **₹12,18,701** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 14:33:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:34:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:40:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:40:11] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:44:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:44:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:36:47] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:40:21] API       rate limited by Dhan - now one call every 13.1 s
[14:41:42] API       rate limited by Dhan - now one call every 15.1 s
[14:42:23] API       rate limited by Dhan - now one call every 15.1 s
[14:43:04] API       rate limited by Dhan - now one call every 15.1 s
[14:43:52] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:37:49] API       rate limited by Dhan - now one call every 15.1 s
[14:38:19] API       rate limited by Dhan - now one call every 15.1 s
[14:38:49] API       rate limited by Dhan - now one call every 15.1 s
[14:39:47] API       rate limited by Dhan - now one call every 15.1 s
[14:41:24] API       rate limited by Dhan - now one call every 15.1 s
[14:43:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:40:28] SIGNAL    2026-12-29 23000 PE MACD crossed DOWN (bar close 561.15, hist +0.28 -> -0.43)
[14:40:28] SKIP      short 2026-12-29 23000 PE ignored - open-position cap
[14:40:28] SIGNAL    2026-12-29 24000 PE MACD crossed DOWN (bar close 1192.70, hist +0.42 -> -0.47)
[14:40:28] SKIP      short 2026-12-29 24000 PE ignored - open-position cap
[14:41:37] API       rate limited by Dhan - now one call every 15.1 s
[14:41:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:33:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:36:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:37:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:39:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:42:08] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:43:57] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:40:20] SKIP      INDIGO 5100 CE 27 Oct signal at 96.40 skipped - 20 trades already today
[14:40:28] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:41:12] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:41:21] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:41:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:42:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:41:18] API       rate limited by Dhan - now one call every 15.1 s
[14:41:34] API       rate limited by Dhan - now one call every 15.1 s
[14:43:10] API       rate limited by Dhan - now one call every 15.1 s
[14:43:41] API       rate limited by Dhan - now one call every 15.1 s
[14:43:56] API       rate limited by Dhan - now one call every 15.1 s
[14:44:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

