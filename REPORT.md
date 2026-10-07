# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:42 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.82 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹1,677 (-2.76%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹7,556 (-0.97%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,122 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,068 (-5.53%) | +₹5,536 (+2.85%) | −₹50,232 (-4.92%) | 14 | 10 | ₹1,93,932 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,256 (-7.80%) | ₹0 | 0 | 8 | ₹2,21,096 |
| **Total** | | **−₹46,570** | **−₹20,953** | **+₹11,215** | **21** | **31** | **₹12,51,860** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:34:31] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:38:32] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:38:32] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:41:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:41:33] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:42:33] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:37:21] API       rate limited by Dhan - now one call every 15.1 s
[11:39:23] API       rate limited by Dhan - now one call every 15.1 s
[11:39:43] API       rate limited by Dhan - now one call every 15.1 s
[11:40:03] API       rate limited by Dhan - now one call every 15.1 s
[11:42:05] API       rate limited by Dhan - now one call every 15.1 s
[11:42:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:35:41] API       rate limited by Dhan - now one call every 15.1 s
[11:35:57] API       rate limited by Dhan - now one call every 15.1 s
[11:36:55] API       rate limited by Dhan - now one call every 15.1 s
[11:37:53] API       rate limited by Dhan - now one call every 15.1 s
[11:38:52] API       rate limited by Dhan - now one call every 15.1 s
[11:40:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:37:24] API       rate limited by Dhan - now one call every 15.1 s
[11:38:08] API       rate limited by Dhan - now one call every 15.1 s
[11:38:24] API       rate limited by Dhan - now one call every 15.1 s
[11:39:22] API       rate limited by Dhan - now one call every 15.1 s
[11:39:52] API       rate limited by Dhan - now one call every 15.1 s
[11:41:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:33:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:35:09] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:37:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:39:09] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:41:08] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:42:49] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:38:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:39:49] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:40:33] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:40:33] SKIP      BHARTIARTL 1840 CE 27 Oct signal at 19.40 skipped - 10 positions already open
[11:42:14] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:42:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:38:02] API       rate limited by Dhan - now one call every 15.1 s
[11:38:46] API       rate limited by Dhan - now one call every 15.1 s
[11:40:23] API       rate limited by Dhan - now one call every 15.1 s
[11:41:21] API       rate limited by Dhan - now one call every 15.1 s
[11:42:06] API       rate limited by Dhan - now one call every 15.1 s
[11:42:36] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

