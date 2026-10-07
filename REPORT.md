# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:58 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.77 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹526 (-0.87%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹3,972 (-0.51%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,358 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,361 (-5.78%) | +₹13,912 (+6.82%) | −₹51,526 (-4.98%) | 15 | 10 | ₹2,03,879 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,661 (-7.54%) | ₹0 | 0 | 8 | ₹2,21,096 |
| **Total** | | **−₹47,863** | **−₹7,247** | **+₹9,921** | **22** | **31** | **₹12,62,043** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:46:34] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:47:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:50:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:50:35] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:56:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:56:36] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:54:17] API       rate limited by Dhan - now one call every 15.1 s
[11:54:58] API       rate limited by Dhan - now one call every 15.1 s
[11:55:39] API       rate limited by Dhan - now one call every 15.1 s
[11:56:19] API       rate limited by Dhan - now one call every 15.1 s
[11:57:41] API       rate limited by Dhan - now one call every 15.1 s
[11:57:59] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:52:52] API       rate limited by Dhan - now one call every 15.1 s
[11:53:22] API       rate limited by Dhan - now one call every 15.1 s
[11:54:46] API       rate limited by Dhan - now one call every 15.1 s
[11:55:17] API       rate limited by Dhan - now one call every 15.1 s
[11:56:01] API       rate limited by Dhan - now one call every 15.1 s
[11:56:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:53:01] API       rate limited by Dhan - now one call every 15.1 s
[11:53:17] API       rate limited by Dhan - now one call every 15.1 s
[11:53:47] API       rate limited by Dhan - now one call every 15.1 s
[11:54:02] API       rate limited by Dhan - now one call every 15.1 s
[11:55:14] API       rate limited by Dhan - now one call every 15.1 s
[11:57:35] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:47:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:49:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:51:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:53:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:55:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:57:19] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:55:25] SKIP      SIEMENS 3800 CE 27 Oct signal at 122.50 skipped - 10 positions already open
[11:55:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:56:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:56:59] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:57:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:57:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:53:45] API       rate limited by Dhan - now one call every 15.1 s
[11:54:00] API       rate limited by Dhan - now one call every 15.1 s
[11:54:59] API       rate limited by Dhan - now one call every 15.1 s
[11:55:43] API       rate limited by Dhan - now one call every 15.1 s
[11:55:58] API       rate limited by Dhan - now one call every 15.1 s
[11:57:35] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

