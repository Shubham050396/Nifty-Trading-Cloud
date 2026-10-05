# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:59 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹11,365 (+1.47%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,001 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹1,690 (+1.61%) | −₹11,956 (-2.08%) | 12 | 6 | ₹1,04,939 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,173 (-3.86%) | ₹0 | 0 | 7 | ₹1,08,105 |
| **Total** | | **+₹22,543** | **+₹8,882** | **+₹81,007** | **25** | **23** | **₹9,87,045** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:51:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:52:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:56:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:56:46] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:57:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:58:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:54:56] API       rate limited by Dhan - now one call every 15.1 s
[12:55:37] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:56:18] API       rate limited by Dhan - now one call every 15.1 s
[12:57:19] API       rate limited by Dhan - now one call every 15.1 s
[12:57:39] API       rate limited by Dhan - now one call every 15.1 s
[12:59:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:54:05] API       rate limited by Dhan - now one call every 15.1 s
[12:55:17] API       rate limited by Dhan - now one call every 15.1 s
[12:56:02] API       rate limited by Dhan - now one call every 15.1 s
[12:57:00] API       rate limited by Dhan - now one call every 15.1 s
[12:58:38] API       rate limited by Dhan - now one call every 15.1 s
[12:58:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:48:24] API       rate limited by Dhan - now one call every 15.1 s
[12:48:54] API       rate limited by Dhan - now one call every 15.1 s
[12:49:52] API       rate limited by Dhan - now one call every 15.1 s
[12:52:24] API       rate limited by Dhan - now one call every 15.1 s
[12:53:22] API       rate limited by Dhan - now one call every 15.1 s
[12:58:48] API       rate limited by Dhan - now one call every 5.1 s
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
[12:53:46] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:53:55] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:55:17] SIGNAL    TMPV 285 PE 27 Oct crossed EMA 144 at 7.05 - not taken: under EMA 55, momentum -4.7%
[12:55:17] SIGNAL    TMPV 295 PE 27 Oct crossed EMA 144 at 12.15 - not taken: under EMA 55, momentum -5.4%
[12:55:24] ENTRY     BUY INDIGO 4900 PE 27 Oct x150 @ 124.60 (signal close 124.50, EMA 144 121.97, momentum 5.5%)  quick 143.29 till 13:25, target 211.82, stop below EMA 55
[12:56:32] WARM      bar history loaded for all 774 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:54:51] API       rate limited by Dhan - now one call every 15.1 s
[12:55:07] SIGNAL    2026-10-27 23000 PE VIX Fix crossed above 10.00 (9.56 -> 10.41, bar close 565.30)
[12:55:07] ENTRY     BUY 2026-10-27 23000 PE @ 565.95 x 65  (Rs 36,787) - buy 1 of 10, average 565.95, target 848.93
[12:55:50] API       rate limited by Dhan - now one call every 15.1 s
[12:56:49] API       rate limited by Dhan - now one call every 15.1 s
[12:57:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

