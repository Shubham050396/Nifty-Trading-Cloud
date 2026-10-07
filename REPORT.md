# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:28 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.77 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | ₹0 | +₹16,929 (+4.05%) | 4 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹17,732 (-2.29%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,75,535 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹13,660 (+6.72%) | −₹53,058 (-5.02%) | 16 | 10 | ₹2,03,316 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹20,157 (-8.71%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹52,744** | **−₹24,229** | **+₹5,038** | **26** | **28** | **₹12,10,323** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:21:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:21:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:23:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:23:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:26:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:26:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:24:27] API       rate limited by Dhan - now one call every 15.1 s
[12:24:48] API       rate limited by Dhan - now one call every 15.1 s
[12:26:09] API       rate limited by Dhan - now one call every 15.1 s
[12:26:50] API       rate limited by Dhan - now one call every 15.1 s
[12:27:19] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:27:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:25:36] GAP       2026-10-13 21500 PE: no prices for 9 min - bar history restarts
[12:25:36] GAP       2026-10-13 23700 CE: no prices for 9 min - bar history restarts
[12:25:36] GAP       2026-10-13 23700 PE: no prices for 9 min - bar history restarts
[12:26:02] API       rate limited by Dhan - now one call every 15.1 s
[12:26:47] EXIT      L2 2026-10-19 22700 CE TRAIL_STOP @ 201.00  P&L Rs -2164.50
[12:27:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:19:14] API       rate limited by Dhan - now one call every 15.1 s
[12:20:38] API       rate limited by Dhan - now one call every 15.1 s
[12:21:50] API       rate limited by Dhan - now one call every 15.1 s
[12:23:50] API       rate limited by Dhan - now one call every 15.1 s
[12:24:48] API       rate limited by Dhan - now one call every 15.1 s
[12:25:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:17:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:19:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:20:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:23:12] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:25:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:27:37] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:27:13] WARM      bar history loaded for all 786 contracts
[12:27:16] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:27:25] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:27:43] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:27:52] API       market quote: rate limited by Dhan - now one call every 2.0 s
[12:28:00] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:20:33] API       rate limited by Dhan - now one call every 15.1 s
[12:23:04] API       rate limited by Dhan - now one call every 15.1 s
[12:23:34] API       rate limited by Dhan - now one call every 15.1 s
[12:24:59] API       rate limited by Dhan - now one call every 15.1 s
[12:25:29] API       rate limited by Dhan - now one call every 15.1 s
[12:27:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

