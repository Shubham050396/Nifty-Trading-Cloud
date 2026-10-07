# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:03 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.84 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | +₹1,716 (+3.79%) | +₹16,929 (+4.05%) | 4 | 2 | ₹45,250 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹13,712 (+1.38%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,90,097 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹5,345 (-2.00%) | +₹6,190 (+3.02%) | −₹43,510 (-4.07%) | 17 | 10 | ₹2,05,001 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹22,153 (-9.57%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹59,828** | **−₹535** | **−₹2,045** | **37** | **30** | **₹14,71,820** |

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
[12:56:40] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:57:20] API       rate limited by Dhan - now one call every 15.1 s
[12:58:41] API       rate limited by Dhan - now one call every 15.1 s
[13:00:03] API       rate limited by Dhan - now one call every 15.1 s
[13:01:24] API       rate limited by Dhan - now one call every 15.1 s
[13:02:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:01:34] GAP       2026-10-13 21500 CE: no prices for 4 min - bar history restarts
[13:01:34] GAP       2026-10-13 21500 PE: no prices for 4 min - bar history restarts
[13:01:34] GAP       2026-10-13 23700 CE: no prices for 4 min - bar history restarts
[13:01:34] GAP       2026-10-13 23700 PE: no prices for 4 min - bar history restarts
[13:01:47] API       rate limited by Dhan - now one call every 15.1 s
[13:02:46] SKIP      L2 2026-10-19 22700 PE cross ignored - daily cap
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:58:02] API       rate limited by Dhan - now one call every 15.1 s
[13:00:02] API       rate limited by Dhan - now one call every 15.1 s
[13:00:17] API       rate limited by Dhan - now one call every 15.1 s
[13:01:29] API       rate limited by Dhan - now one call every 15.1 s
[13:02:40] API       rate limited by Dhan - now one call every 15.1 s
[13:03:27] VIX       India VIX prev close 13.61 - entries allowed
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:54:12] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:55:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:57:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:59:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:01:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:02:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:00:58] WARM      bar history loaded for all 788 contracts
[13:01:02] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:01:12] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:01:21] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:02:05] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:03:06] WARM      bar history loaded for all 788 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:58:57] API       rate limited by Dhan - now one call every 15.1 s
[13:00:09] API       rate limited by Dhan - now one call every 15.1 s
[13:00:53] API       rate limited by Dhan - now one call every 15.1 s
[13:01:09] API       rate limited by Dhan - now one call every 15.1 s
[13:01:53] API       rate limited by Dhan - now one call every 15.1 s
[13:02:11] VIX       India VIX prev close 13.61
```
</details>

