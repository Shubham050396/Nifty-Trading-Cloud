# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:54 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹11,356 (+1.47%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,73,725 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹1,405 (+1.63%) | −₹11,956 (-2.08%) | 12 | 5 | ₹86,249 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,436 (-6.22%) | ₹0 | 0 | 6 | ₹71,318 |
| **Total** | | **+₹22,543** | **+₹8,325** | **+₹81,007** | **25** | **21** | **₹9,31,292** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:43:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:43:43] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:50:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:50:45] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:51:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:52:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:49:10] API       rate limited by Dhan - now one call every 15.1 s
[12:49:36] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:51:53] API       rate limited by Dhan - now one call every 15.1 s
[12:52:13] API       rate limited by Dhan - now one call every 15.1 s
[12:53:34] API       rate limited by Dhan - now one call every 15.1 s
[12:53:37] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:51:21] API       rate limited by Dhan - now one call every 15.1 s
[12:52:20] API       rate limited by Dhan - now one call every 15.1 s
[12:52:35] API       rate limited by Dhan - now one call every 15.1 s
[12:53:05] API       rate limited by Dhan - now one call every 15.1 s
[12:53:50] API       rate limited by Dhan - now one call every 15.1 s
[12:54:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:48:03] API       rate limited by Dhan - now one call every 10.1 s
[12:48:24] API       rate limited by Dhan - now one call every 15.1 s
[12:48:54] API       rate limited by Dhan - now one call every 15.1 s
[12:49:52] API       rate limited by Dhan - now one call every 15.1 s
[12:52:24] API       rate limited by Dhan - now one call every 15.1 s
[12:53:22] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:42:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:44:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:47:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:48:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:50:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:52:43] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:50:17] SIGNAL    HDFCLIFE 520 PE 27 Oct crossed EMA 144 at 10.20 - not taken: under EMA 55, momentum -11.7%
[12:50:59] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:51:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:53:42] WARM      bar history loaded for all 774 contracts
[12:53:46] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:53:55] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:51:07] API       rate limited by Dhan - now one call every 15.1 s
[12:51:52] API       rate limited by Dhan - now one call every 15.1 s
[12:52:07] API       rate limited by Dhan - now one call every 15.1 s
[12:52:51] API       rate limited by Dhan - now one call every 15.1 s
[12:53:36] API       rate limited by Dhan - now one call every 15.1 s
[12:54:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

