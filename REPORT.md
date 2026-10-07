# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:53 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹1,670 (-2.75%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹5,798 (-0.75%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,297 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,361 (-5.78%) | +₹9,006 (+4.42%) | −₹51,526 (-4.98%) | 15 | 10 | ₹2,03,879 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,139 (-7.75%) | ₹0 | 0 | 8 | ₹2,21,096 |
| **Total** | | **−₹47,863** | **−₹15,601** | **+₹9,921** | **22** | **31** | **₹12,61,982** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:44:33] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:46:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:46:34] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:47:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:50:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:50:35] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:46:50] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:46:50] API       rate limited by Dhan - now one call every 15.1 s
[11:48:11] API       rate limited by Dhan - now one call every 15.1 s
[11:49:33] API       rate limited by Dhan - now one call every 15.1 s
[11:50:54] API       rate limited by Dhan - now one call every 15.1 s
[11:52:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:49:13] API       rate limited by Dhan - now one call every 15.1 s
[11:49:28] API       rate limited by Dhan - now one call every 15.1 s
[11:50:13] API       rate limited by Dhan - now one call every 15.1 s
[11:50:57] API       rate limited by Dhan - now one call every 15.1 s
[11:51:27] API       rate limited by Dhan - now one call every 15.1 s
[11:52:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:45:47] API       rate limited by Dhan - now one call every 14.1 s
[11:47:57] API       rate limited by Dhan - now one call every 15.1 s
[11:49:21] API       rate limited by Dhan - now one call every 15.1 s
[11:52:35] API       rate limited by Dhan - now one call every 11.1 s
[11:52:46] API       rate limited by Dhan - now one call every 15.1 s
[11:53:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:42:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:44:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:46:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:47:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:49:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:51:37] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:51:23] WARM      bar history loaded for all 782 contracts
[11:51:30] WARM      bar history loaded for all 784 contracts
[11:51:36] API       market quote: rate limited by Dhan - now one call every 5.5 s
[11:52:13] WARM      bar history loaded for all 784 contracts
[11:52:22] API       market quote: rate limited by Dhan - now one call every 5.5 s
[11:52:39] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:48:57] API       rate limited by Dhan - now one call every 15.1 s
[11:49:55] API       rate limited by Dhan - now one call every 15.1 s
[11:50:11] API       rate limited by Dhan - now one call every 15.1 s
[11:51:35] API       rate limited by Dhan - now one call every 15.1 s
[11:52:05] API       rate limited by Dhan - now one call every 15.1 s
[11:52:20] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

