# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:03 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.71 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | +₹439 (+0.72%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹2,015 (-0.26%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,648 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,361 (-5.78%) | +₹14,554 (+7.14%) | −₹51,526 (-4.98%) | 15 | 10 | ₹2,03,879 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,327 (-7.38%) | ₹0 | 0 | 8 | ₹2,21,096 |
| **Total** | | **−₹47,863** | **−₹3,349** | **+₹9,921** | **22** | **31** | **₹12,62,333** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:56:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:56:36] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:58:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:58:36] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:02:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:02:37] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:59:02] API       rate limited by Dhan - now one call every 15.1 s
[11:59:22] API       rate limited by Dhan - now one call every 15.1 s
[12:00:24] API       rate limited by Dhan - now one call every 15.1 s
[12:01:01] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:01:04] API       rate limited by Dhan - now one call every 15.1 s
[12:01:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:02:34] GAP       2026-10-27 22900 PE: no prices for 5 min - bar history restarts
[12:02:34] GAP       2026-10-27 21500 CE: no prices for 5 min - bar history restarts
[12:02:34] GAP       2026-10-27 21500 PE: no prices for 5 min - bar history restarts
[12:02:34] GAP       2026-10-27 23700 CE: no prices for 5 min - bar history restarts
[12:02:34] GAP       2026-10-27 23700 PE: no prices for 5 min - bar history restarts
[12:02:48] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:00:06] SIGNAL    2026-10-27 24000 CE MACD crossed UP (bar close 10.80, hist -0.01 -> +0.01)
[12:00:06] SKIP      buy 2026-10-27 24000 CE ignored - premium 10.80 is outside 144 - 1600
[12:00:40] API       rate limited by Dhan - now one call every 12.1 s
[12:01:04] API       rate limited by Dhan - now one call every 15.1 s
[12:01:35] API       rate limited by Dhan - now one call every 15.1 s
[12:02:33] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:53:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:55:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:57:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:58:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:00:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:02:31] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:59:39] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:00:14] SIGNAL    HAL 4700 CE 27 Oct crossed EMA 144 at 164.85 - not taken: momentum -5.6%
[12:00:23] SKIP      ADANIENSOL 1360 PE 27 Oct signal at 55.10 skipped - 10 positions already open
[12:00:48] WARM      bar history loaded for all 784 contracts
[12:01:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:02:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:59:18] API       rate limited by Dhan - now one call every 15.1 s
[12:00:03] API       rate limited by Dhan - now one call every 15.1 s
[12:00:18] API       rate limited by Dhan - now one call every 15.1 s
[12:00:48] API       rate limited by Dhan - now one call every 15.1 s
[12:02:00] API       rate limited by Dhan - now one call every 15.1 s
[12:02:02] VIX       India VIX prev close 13.61
```
</details>

