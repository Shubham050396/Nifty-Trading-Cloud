# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:58 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | +₹39 (+0.17%) | +₹16,929 (+4.05%) | 4 | 1 | ₹22,640 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹3,923 (+0.40%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,90,435 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹5,345 (-2.00%) | +₹7,725 (+4.07%) | −₹43,510 (-4.07%) | 17 | 9 | ₹1,89,874 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹22,770 (-9.84%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹59,828** | **−₹11,083** | **−₹2,045** | **37** | **28** | **₹14,34,421** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:36:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:36:45] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:38:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:38:45] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:40:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:40:45] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:50:33] API       rate limited by Dhan - now one call every 15.1 s
[12:51:54] API       rate limited by Dhan - now one call every 15.1 s
[12:55:18] API       rate limited by Dhan - now one call every 15.1 s
[12:55:59] API       rate limited by Dhan - now one call every 15.1 s
[12:56:40] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:57:20] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:54:58] API       rate limited by Dhan - now one call every 15.1 s
[12:55:14] API       rate limited by Dhan - now one call every 15.1 s
[12:55:44] API       rate limited by Dhan - now one call every 15.1 s
[12:56:56] API       rate limited by Dhan - now one call every 15.1 s
[12:58:07] API       rate limited by Dhan - now one call every 15.1 s
[12:58:22] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:52:31] API       rate limited by Dhan - now one call every 15.1 s
[12:54:19] API       rate limited by Dhan - now one call every 15.1 s
[12:56:19] API       rate limited by Dhan - now one call every 15.1 s
[12:57:31] API       rate limited by Dhan - now one call every 15.1 s
[12:57:46] API       rate limited by Dhan - now one call every 15.1 s
[12:58:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:48:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:50:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:51:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:54:12] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:55:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:57:51] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:54:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:54:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:55:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:56:24] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:57:59] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:58:28] WARM      bar history loaded for all 788 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:50:40] API       rate limited by Dhan - now one call every 15.1 s
[12:53:21] API       rate limited by Dhan - now one call every 15.1 s
[12:54:05] API       rate limited by Dhan - now one call every 15.1 s
[12:54:35] API       rate limited by Dhan - now one call every 15.1 s
[12:55:20] API       rate limited by Dhan - now one call every 15.1 s
[12:57:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

