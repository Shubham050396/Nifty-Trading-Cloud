# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:43 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.72 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹634 (-1.37%) | +₹2,561 (+7.00%) | +₹19,786 (+7.37%) | 2 | 2 | ₹36,592 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹31,054 (+5.50%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,573 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹4,854 (-5.16%) | −₹2,212 (-0.49%) | 6 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹2,509 (-4.16%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹2,758** | **+₹26,252** | **+₹55,706** | **8** | **16** | **₹7,55,530** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:32:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:32:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:34:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:34:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:37:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:37:11] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:40:03] API       rate limited by Dhan - now one call every 15.1 s
[10:40:24] API       rate limited by Dhan - now one call every 15.1 s
[10:41:25] API       rate limited by Dhan - now one call every 15.1 s
[10:41:45] API       rate limited by Dhan - now one call every 15.1 s
[10:42:13] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:42:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:39:02] API       rate limited by Dhan - now one call every 15.1 s
[10:40:00] API       rate limited by Dhan - now one call every 15.1 s
[10:40:45] API       rate limited by Dhan - now one call every 15.1 s
[10:41:00] API       rate limited by Dhan - now one call every 15.1 s
[10:41:58] API       rate limited by Dhan - now one call every 15.1 s
[10:42:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:38:12] API       rate limited by Dhan - now one call every 15.1 s
[10:38:45] VIX       India VIX prev close 14.46 - entries allowed
[10:39:24] API       rate limited by Dhan - now one call every 15.1 s
[10:40:48] API       rate limited by Dhan - now one call every 15.1 s
[10:41:47] API       rate limited by Dhan - now one call every 15.1 s
[10:42:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:29:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:33:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:36:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:38:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:40:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:41:56] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:40:17] SIGNAL    COALINDIA 435 PE 27 Oct crossed EMA 144 at 13.45 - not taken: under EMA 55
[10:40:17] SIGNAL    HDFCLIFE 520 PE 27 Oct crossed EMA 144 at 10.50 - not taken: under EMA 55
[10:40:41] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:40:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:41:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:42:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:38:06] VIX       India VIX prev close 14.46
[10:38:46] API       rate limited by Dhan - now one call every 15.1 s
[10:39:45] API       rate limited by Dhan - now one call every 15.1 s
[10:41:46] API       rate limited by Dhan - now one call every 15.1 s
[10:42:16] API       rate limited by Dhan - now one call every 15.1 s
[10:42:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

