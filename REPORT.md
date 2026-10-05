# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:28 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.64 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹7,426 (+11.92%) | +₹20,420 (+9.20%) | 0 | 3 | ₹62,290 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹37,203 (+6.59%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,401 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹1,468 (-1.60%) | −₹5,061 (-5.38%) | −₹1,556 (-0.35%) | 5 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹1,053 (-9.31%) | ₹0 | 0 | 3 | ₹11,313 |
| **Total** | | **−₹1,468** | **+₹38,515** | **+₹56,996** | **5** | **16** | **₹7,32,055** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:15:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:15:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:16:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:17:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:24:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:24:08] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:24:05] API       rate limited by Dhan - now one call every 15.1 s
[10:25:06] API       rate limited by Dhan - now one call every 15.1 s
[10:25:27] API       rate limited by Dhan - now one call every 15.1 s
[10:26:11] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:26:48] API       rate limited by Dhan - now one call every 15.1 s
[10:28:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:27:22] GAP       2026-10-06 21400 PE: no prices for 6 min - bar history restarts
[10:27:22] GAP       2026-10-06 23600 CE: no prices for 6 min - bar history restarts
[10:27:22] GAP       2026-10-06 23500 CE: no prices for 6 min - bar history restarts
[10:27:22] GAP       2026-10-06 23600 PE: no prices for 6 min - bar history restarts
[10:27:22] GAP       2026-10-06 23500 PE: no prices for 6 min - bar history restarts
[10:28:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:24:57] API       rate limited by Dhan - now one call every 15.1 s
[10:25:28] API       rate limited by Dhan - now one call every 15.1 s
[10:25:43] API       rate limited by Dhan - now one call every 15.1 s
[10:26:13] API       rate limited by Dhan - now one call every 15.1 s
[10:27:12] API       rate limited by Dhan - now one call every 15.1 s
[10:28:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:17:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:17:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:19:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:21:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:22:26] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:25:29] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:26:31] WARM      bar history loaded for all 730 contracts
[10:26:44] WARM      bar history loaded for all 732 contracts
[10:26:57] WARM      bar history loaded for all 732 contracts
[10:27:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:27:37] WARM      bar history loaded for all 736 contracts
[10:28:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:23:23] API       rate limited by Dhan - now one call every 15.1 s
[10:24:22] API       rate limited by Dhan - now one call every 15.1 s
[10:25:06] API       rate limited by Dhan - now one call every 15.1 s
[10:27:07] API       rate limited by Dhan - now one call every 15.1 s
[10:27:37] API       rate limited by Dhan - now one call every 15.1 s
[10:28:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

