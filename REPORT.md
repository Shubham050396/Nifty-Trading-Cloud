# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:04 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹7,751 (+1.00%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,259 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹842 (+0.70%) | −₹11,956 (-2.08%) | 12 | 7 | ₹1,19,616 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,267 (-3.95%) | ₹0 | 0 | 7 | ₹1,08,105 |
| **Total** | | **+₹22,543** | **+₹4,326** | **+₹81,007** | **25** | **24** | **₹10,01,980** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:57:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:58:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:59:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:00:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:01:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:02:48] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:01:24] API       rate limited by Dhan - now one call every 15.1 s
[13:01:44] API       rate limited by Dhan - now one call every 15.1 s
[13:02:25] API       rate limited by Dhan - now one call every 15.1 s
[13:02:45] API       rate limited by Dhan - now one call every 15.1 s
[13:03:06] API       rate limited by Dhan - now one call every 15.1 s
[13:04:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:03:51] GAP       2026-10-06 21400 PE: no prices for 6 min - bar history restarts
[13:03:51] GAP       2026-10-06 23600 CE: no prices for 6 min - bar history restarts
[13:03:51] GAP       2026-10-06 23500 CE: no prices for 6 min - bar history restarts
[13:03:51] GAP       2026-10-06 23600 PE: no prices for 6 min - bar history restarts
[13:03:51] GAP       2026-10-06 23500 PE: no prices for 6 min - bar history restarts
[13:04:29] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:49:52] API       rate limited by Dhan - now one call every 15.1 s
[12:52:24] API       rate limited by Dhan - now one call every 15.1 s
[12:53:22] API       rate limited by Dhan - now one call every 15.1 s
[12:58:48] API       rate limited by Dhan - now one call every 5.1 s
[13:03:37] API       rate limited by Dhan - now one call every 5.1 s
[13:03:56] API       rate limited by Dhan - now one call every 5.1 s
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
[12:55:17] SIGNAL    TMPV 295 PE 27 Oct crossed EMA 144 at 12.15 - not taken: under EMA 55, momentum -5.4%
[12:55:24] ENTRY     BUY INDIGO 4900 PE 27 Oct x150 @ 124.60 (signal close 124.50, EMA 144 121.97, momentum 5.5%)  quick 143.29 till 13:25, target 211.82, stop below EMA 55
[12:56:32] WARM      bar history loaded for all 774 contracts
[13:00:02] SIGNAL    INDIGO 5000 PE 27 Oct crossed EMA 144 at 175.00 - not taken: momentum -3.1%
[13:00:03] ENTRY     BUY DLF 680 CE 27 Oct x950 @ 15.45 (signal close 15.60, EMA 144 15.23, momentum 7.6%)  quick 17.77 till 13:30, target 26.26, stop below EMA 55
[13:03:48] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:55:50] API       rate limited by Dhan - now one call every 15.1 s
[12:56:49] API       rate limited by Dhan - now one call every 15.1 s
[12:57:47] API       rate limited by Dhan - now one call every 15.1 s
[12:59:36] API       rate limited by Dhan - now one call every 15.1 s
[13:01:37] API       rate limited by Dhan - now one call every 15.1 s
[13:03:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

