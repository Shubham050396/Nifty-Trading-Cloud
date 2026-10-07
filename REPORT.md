# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:43 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.74 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | −₹1,086 (-4.79%) | +₹16,929 (+4.05%) | 4 | 1 | ₹22,640 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | −₹5,584 (-0.61%) | +₹22,441 (+0.36%) | 16 | 9 | ₹9,11,173 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹18,780 (+9.24%) | −₹53,058 (-5.02%) | 16 | 10 | ₹2,03,316 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹20,235 (-8.74%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹69,375** | **−₹8,125** | **−₹11,593** | **36** | **28** | **₹13,68,601** |

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
[12:35:39] API       rate limited by Dhan - now one call every 15.1 s
[12:37:41] API       rate limited by Dhan - now one call every 15.1 s
[12:40:23] API       rate limited by Dhan - now one call every 15.1 s
[12:40:26] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:42:25] API       rate limited by Dhan - now one call every 15.1 s
[12:43:06] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:40:13] API       rate limited by Dhan - now one call every 15.1 s
[12:41:25] API       rate limited by Dhan - now one call every 15.1 s
[12:41:40] API       rate limited by Dhan - now one call every 15.1 s
[12:41:55] API       rate limited by Dhan - now one call every 15.1 s
[12:42:11] API       rate limited by Dhan - now one call every 15.1 s
[12:43:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:40:24] SIGNAL    2026-10-27 24000 PE MACD crossed UP (bar close 1285.00, hist -0.19 -> +0.42)
[12:40:24] EXIT      SHORT 2026-10-27 24000 PE MACD_UP @ 1285.40  P&L Rs -2749.50
[12:40:24] ENTRY     BUY 2026-10-27 24000 PE @ 1285.40  (bar close 1285.00, MACD hist +0.42, VIX 13.61)
[12:41:25] API       rate limited by Dhan - now one call every 8.1 s
[12:41:33] API       rate limited by Dhan - now one call every 13.1 s
[12:41:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:33:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:35:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:37:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:39:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:41:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:43:22] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:40:09] SIGNAL    SHREECEM 22000 PE 27 Oct crossed EMA 144 at 534.15 - not taken: under EMA 55
[12:40:09] SIGNAL    ICICIBANK 1360 CE 27 Oct crossed EMA 144 at 22.25 - not taken: momentum 0.2%
[12:41:12] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:41:21] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:41:57] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:42:57] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:38:52] API       rate limited by Dhan - now one call every 15.1 s
[12:39:22] API       rate limited by Dhan - now one call every 15.1 s
[12:39:52] API       rate limited by Dhan - now one call every 15.1 s
[12:40:22] API       rate limited by Dhan - now one call every 15.1 s
[12:41:07] API       rate limited by Dhan - now one call every 15.1 s
[12:42:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

