# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:54 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | +₹9,763 (+0.98%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,01,115 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,125 (-5.58%) | −₹248 (-0.12%) | −₹14,214 (-2.35%) | 14 | 10 | ₹2,07,996 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹9,142 (-6.36%) | ₹0 | 0 | 7 | ₹1,43,744 |
| **Total** | | **+₹10,767** | **+₹373** | **+₹69,229** | **38** | **27** | **₹13,52,855** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:45:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:45:58] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:47:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:47:59] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:49:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:49:59] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:51:47] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:52:03] API       rate limited by Dhan - now one call every 15.1 s
[13:53:04] API       rate limited by Dhan - now one call every 15.1 s
[13:53:24] API       rate limited by Dhan - now one call every 15.1 s
[13:54:26] API       rate limited by Dhan - now one call every 15.1 s
[13:54:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:54:41] GAP       2026-10-06 21400 CE: no prices for 4 min - bar history restarts
[13:54:41] GAP       2026-10-06 21400 PE: no prices for 4 min - bar history restarts
[13:54:41] GAP       2026-10-06 23600 CE: no prices for 4 min - bar history restarts
[13:54:41] GAP       2026-10-06 23500 CE: no prices for 4 min - bar history restarts
[13:54:41] GAP       2026-10-06 23600 PE: no prices for 4 min - bar history restarts
[13:54:41] GAP       2026-10-06 23500 PE: no prices for 4 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:49:07] API       rate limited by Dhan - now one call every 13.1 s
[13:49:46] API       rate limited by Dhan - now one call every 15.1 s
[13:50:01] SIGNAL    2026-11-23 21000 CE MACD crossed UP (bar close 1815.20, hist -0.09 -> +1.81)
[13:50:01] SKIP      buy 2026-11-23 21000 CE ignored - premium 1815.20 is outside 144 - 1600
[13:52:18] API       rate limited by Dhan - now one call every 15.1 s
[13:54:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 13:47:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:49:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:50:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:50:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:52:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:54:45] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:53:03] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:53:38] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:53:48] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:53:57] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:54:26] WARM      bar history loaded for all 784 contracts
[13:54:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:48:08] API       rate limited by Dhan - now one call every 15.1 s
[13:51:28] API       rate limited by Dhan - now one call every 10.1 s
[13:52:31] API       rate limited by Dhan - now one call every 11.1 s
[13:53:40] API       rate limited by Dhan - now one call every 13.1 s
[13:54:06] API       rate limited by Dhan - now one call every 15.1 s
[13:54:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

