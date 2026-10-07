# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:53 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.79 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | −₹36 (-0.16%) | +₹16,929 (+4.05%) | 4 | 1 | ₹22,640 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | −₹237 (-0.02%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,91,043 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹18,266 (+8.98%) | −₹53,058 (-5.02%) | 16 | 10 | ₹2,03,316 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹21,607 (-9.33%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹69,375** | **−₹3,614** | **−₹11,593** | **36** | **29** | **₹14,48,471** |

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
[12:44:47] API       rate limited by Dhan - now one call every 15.1 s
[12:45:48] API       rate limited by Dhan - now one call every 15.1 s
[12:49:33] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:49:52] API       rate limited by Dhan - now one call every 15.1 s
[12:50:33] API       rate limited by Dhan - now one call every 15.1 s
[12:51:54] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:49:22] API       rate limited by Dhan - now one call every 15.1 s
[12:49:52] API       rate limited by Dhan - now one call every 15.1 s
[12:50:50] API       rate limited by Dhan - now one call every 15.1 s
[12:51:35] API       rate limited by Dhan - now one call every 15.1 s
[12:51:50] API       rate limited by Dhan - now one call every 15.1 s
[12:52:48] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:48:37] API       rate limited by Dhan - now one call every 15.1 s
[12:50:02] SIGNAL    2026-11-23 24000 PE MACD crossed UP (bar close 1219.40, hist -0.13 -> +0.33)
[12:50:02] ENTRY     BUY 2026-11-23 24000 PE @ 1238.00  (bar close 1219.40, MACD hist +0.33, VIX 13.61)
[12:50:48] API       rate limited by Dhan - now one call every 15.1 s
[12:51:32] API       rate limited by Dhan - now one call every 15.1 s
[12:52:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:43:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:45:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:46:32] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:48:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:50:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:51:44] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:50:16] SIGNAL    TCS 2120 PE 27 Oct crossed EMA 144 at 84.90 - not taken: under EMA 55, momentum 2.3%
[12:50:25] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:50:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:51:12] WARM      bar history loaded for all 788 contracts
[12:51:32] WARM      bar history loaded for all 788 contracts
[12:51:58] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:48:55] API       rate limited by Dhan - now one call every 15.1 s
[12:49:10] API       rate limited by Dhan - now one call every 15.1 s
[12:49:54] API       rate limited by Dhan - now one call every 15.1 s
[12:50:25] API       rate limited by Dhan - now one call every 15.1 s
[12:50:40] API       rate limited by Dhan - now one call every 15.1 s
[12:53:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

