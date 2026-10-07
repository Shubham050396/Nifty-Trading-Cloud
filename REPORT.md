# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:27 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.73 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | +₹748 (+1.23%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹1,436 (-0.19%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,327 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,068 (-5.53%) | +₹5,619 (+3.10%) | −₹50,232 (-4.92%) | 14 | 9 | ₹1,80,965 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹15,569 (-7.06%) | ₹0 | 0 | 8 | ₹2,20,397 |
| **Total** | | **−₹46,570** | **−₹10,638** | **+₹11,215** | **21** | **30** | **₹12,38,399** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:05:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:06:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:10:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:10:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:23:29] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:23:29] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:22:47] API       rate limited by Dhan - now one call every 15.1 s
[11:23:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:23:48] API       rate limited by Dhan - now one call every 15.1 s
[11:24:28] API       rate limited by Dhan - now one call every 15.1 s
[11:25:09] API       rate limited by Dhan - now one call every 15.1 s
[11:27:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:27:40] GAP       2026-10-27 22000 PE: no prices for 4 min - bar history restarts
[11:27:40] GAP       2026-10-27 22900 PE: no prices for 4 min - bar history restarts
[11:27:40] GAP       2026-10-27 21500 CE: no prices for 4 min - bar history restarts
[11:27:40] GAP       2026-10-27 21500 PE: no prices for 4 min - bar history restarts
[11:27:40] GAP       2026-10-27 23700 CE: no prices for 4 min - bar history restarts
[11:27:40] GAP       2026-10-27 23700 PE: no prices for 4 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:20:59] API       rate limited by Dhan - now one call every 15.1 s
[11:22:47] API       rate limited by Dhan - now one call every 15.1 s
[11:23:46] API       rate limited by Dhan - now one call every 15.1 s
[11:25:35] API       rate limited by Dhan - now one call every 15.1 s
[11:25:50] SIGNAL    2026-11-23 24000 CE MACD crossed UP (bar close 66.80, hist -0.03 -> +0.00)
[11:25:50] SKIP      buy 2026-11-23 24000 CE ignored - premium 66.80 is outside 144 - 1600
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:14:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:17:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:18:46] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:19:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:24:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:26:33] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:26:16] WARM      bar history loaded for all 782 contracts
[11:26:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:26:48] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:26:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:27:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:27:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:23:01] API       rate limited by Dhan - now one call every 15.1 s
[11:25:01] SIGNAL    2026-10-27 26000 CE VIX Fix crossed above 10.00 (9.09 -> 10.61, bar close 0.95)
[11:25:01] ENTRY     BUY 2026-10-27 26000 CE @ 1.00 x 65  (Rs 65) - buy 3 of 10, average 1.32, target 1.98
[11:25:22] API       rate limited by Dhan - now one call every 15.1 s
[11:25:52] API       rate limited by Dhan - now one call every 15.1 s
[11:27:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

