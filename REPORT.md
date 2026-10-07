# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:27 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | +₹159 (+0.36%) | +₹21,548 (+6.41%) | 0 | 2 | ₹44,116 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹28,200 (-4.13%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,83,568 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹3,288 (-2.00%) | +₹4,179 (+2.67%) | −₹41,452 (-4.29%) | 11 | 8 | ₹1,56,730 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,076 (-7.30%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹3,288** | **−₹39,938** | **+₹54,497** | **11** | **24** | **₹11,04,746** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:03:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:03:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:16:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:16:15] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:22:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:22:16] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:20:24] API       rate limited by Dhan - now one call every 15.1 s
[10:20:44] API       rate limited by Dhan - now one call every 15.1 s
[10:20:45] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:21:05] API       rate limited by Dhan - now one call every 15.1 s
[10:24:28] API       rate limited by Dhan - now one call every 15.1 s
[10:26:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:23:28] ENTRY     L3 BUY 2026-10-19 22500 CE @ 325.05  target 375.05  trail 292.55 (10%)
[10:24:11] API       rate limited by Dhan - now one call every 15.1 s
[10:25:35] API       rate limited by Dhan - now one call every 15.1 s
[10:25:50] API       rate limited by Dhan - now one call every 15.1 s
[10:26:20] API       rate limited by Dhan - now one call every 15.1 s
[10:27:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:19:11] API       rate limited by Dhan - now one call every 15.1 s
[10:19:26] API       rate limited by Dhan - now one call every 15.1 s
[10:21:47] API       rate limited by Dhan - now one call every 15.1 s
[10:22:45] API       rate limited by Dhan - now one call every 15.1 s
[10:23:44] API       rate limited by Dhan - now one call every 15.1 s
[10:24:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:17:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:18:46] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:21:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:22:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:24:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:26:09] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:25:18] SIGNAL    SOLARINDS 20250 CE 27 Oct crossed EMA 144 at 540.00 - not taken: momentum 0.8%
[10:25:18] SIGNAL    ADANIENSOL 1400 CE 27 Oct crossed EMA 144 at 38.20 - not taken: momentum 3.2%
[10:25:18] SIGNAL    PNB 115 PE 27 Oct crossed EMA 144 at 4.22 - not taken: under EMA 55, momentum -17.6%, premium under Rs 5
[10:25:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:26:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:26:36] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:22:36] API       rate limited by Dhan - now one call every 15.1 s
[10:24:36] API       rate limited by Dhan - now one call every 15.1 s
[10:25:06] SIGNAL    2026-10-27 23000 PE VIX Fix crossed above 10.00 (7.98 -> 11.06, bar close 426.60)
[10:25:06] SKIP      buy 2026-10-27 23000 PE ignored - Rs 72,426 in this strike already and this buy needs Rs 27,807 - over the Rs 100,000 limit
[10:26:37] API       rate limited by Dhan - now one call every 15.1 s
[10:26:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

