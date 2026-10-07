# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:48 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.77 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | −₹770 (-3.40%) | +₹16,929 (+4.05%) | 4 | 1 | ₹22,640 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | −₹3,003 (-0.33%) | +₹22,441 (+0.36%) | 16 | 9 | ₹9,10,838 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹16,741 (+8.23%) | −₹53,058 (-5.02%) | 16 | 10 | ₹2,03,316 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹20,723 (-8.95%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹69,375** | **−₹7,755** | **−₹11,593** | **36** | **28** | **₹13,68,266** |

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
[12:40:26] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:42:25] API       rate limited by Dhan - now one call every 15.1 s
[12:43:06] API       rate limited by Dhan - now one call every 15.1 s
[12:43:46] API       rate limited by Dhan - now one call every 15.1 s
[12:44:47] API       rate limited by Dhan - now one call every 15.1 s
[12:45:48] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:44:33] API       rate limited by Dhan - now one call every 15.1 s
[12:44:49] API       rate limited by Dhan - now one call every 15.1 s
[12:45:04] API       rate limited by Dhan - now one call every 15.1 s
[12:46:02] API       rate limited by Dhan - now one call every 15.1 s
[12:47:51] API       rate limited by Dhan - now one call every 15.1 s
[12:48:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:44:27] API       rate limited by Dhan - now one call every 15.1 s
[12:45:26] API       rate limited by Dhan - now one call every 15.1 s
[12:46:37] API       rate limited by Dhan - now one call every 15.1 s
[12:46:53] API       rate limited by Dhan - now one call every 15.1 s
[12:47:08] API       rate limited by Dhan - now one call every 15.1 s
[12:47:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:37:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:39:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:41:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:43:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:45:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:46:32] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:44:10] WARM      bar history loaded for all 788 contracts
[12:44:31] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:45:31] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:45:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:46:57] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:47:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:44:59] API       rate limited by Dhan - now one call every 15.1 s
[12:45:43] API       rate limited by Dhan - now one call every 15.1 s
[12:45:59] API       rate limited by Dhan - now one call every 15.1 s
[12:46:14] API       rate limited by Dhan - now one call every 15.1 s
[12:46:29] API       rate limited by Dhan - now one call every 15.1 s
[12:47:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

