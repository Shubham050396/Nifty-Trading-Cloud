# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:24 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.08 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹21,671 (+2.19%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,914 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,420 (-4.18%) | +₹16,213 (+10.71%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,900 (-10.08%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹61,403** | **+₹13,984** | **−₹3,620** | **41** | **26** | **₹13,77,514** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 14:11:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:12:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:14:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:14:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:20:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:20:07] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:22:45] API       rate limited by Dhan - now one call every 15.1 s
[14:23:05] API       rate limited by Dhan - now one call every 15.1 s
[14:23:25] API       rate limited by Dhan - now one call every 15.1 s
[14:23:38] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:23:45] API       rate limited by Dhan - now one call every 15.1 s
[14:24:06] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:21:10] API       rate limited by Dhan - now one call every 15.1 s
[14:21:40] API       rate limited by Dhan - now one call every 15.1 s
[14:22:10] API       rate limited by Dhan - now one call every 15.1 s
[14:23:08] API       rate limited by Dhan - now one call every 15.1 s
[14:23:39] API       rate limited by Dhan - now one call every 15.1 s
[14:24:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:16:21] API       rate limited by Dhan - now one call every 15.1 s
[14:16:36] API       rate limited by Dhan - now one call every 15.1 s
[14:16:52] API       rate limited by Dhan - now one call every 15.1 s
[14:18:28] API       rate limited by Dhan - now one call every 15.1 s
[14:20:17] API       rate limited by Dhan - now one call every 15.1 s
[14:22:06] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:11:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:14:10] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:16:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:18:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:21:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:23:22] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:23:04] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:23:08] API       market quote: rate limited by Dhan - now one call every 2.5 s
[14:23:21] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:23:48] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:23:57] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:24:08] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:17:38] API       rate limited by Dhan - now one call every 15.1 s
[14:19:02] API       rate limited by Dhan - now one call every 15.1 s
[14:20:01] API       rate limited by Dhan - now one call every 15.1 s
[14:22:41] API       rate limited by Dhan - now one call every 15.1 s
[14:23:25] API       rate limited by Dhan - now one call every 15.1 s
[14:23:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

