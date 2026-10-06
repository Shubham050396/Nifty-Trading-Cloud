# NIFTY Cloud report

**Finished for the day at 15:15 IST** · updated 06 Oct 2026 15:15 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **13.67 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | +₹19,867 (+3.47%) | −₹41,652 (-6.09%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,84,452 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | −₹10,790 (-12.22%) | +₹6,980 (+5.68%) | −₹38,165 (-4.76%) | 4 | 7 | ₹1,22,921 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | ✅ saved | ₹0 | −₹19,087 (-12.27%) | ₹0 | 0 | 8 | ₹1,55,606 |
| **Total** | | **+₹9,077** | **−₹53,759** | **+₹57,784** | **8** | **21** | **₹9,62,979** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 14:55:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 15:01:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 15:01:28] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 15:14:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 15:14:31] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:08:11] API       rate limited by Dhan - now one call every 15.1 s
[15:09:32] API       rate limited by Dhan - now one call every 15.1 s
[15:11:48] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[15:11:55] API       rate limited by Dhan - now one call every 15.1 s
[15:13:49] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:14:37] GAP       2026-10-13 22900 PE: no prices for 5 min - bar history restarts
[15:14:37] GAP       2026-10-13 21500 CE: no prices for 5 min - bar history restarts
[15:14:37] GAP       2026-10-13 21500 PE: no prices for 5 min - bar history restarts
[15:14:37] GAP       2026-10-13 23700 CE: no prices for 5 min - bar history restarts
[15:14:37] GAP       2026-10-13 23700 PE: no prices for 5 min - bar history restarts
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[15:11:54] API       rate limited by Dhan - now one call every 5.1 s
[15:13:19] API       rate limited by Dhan - now one call every 5.1 s
[15:13:50] API       rate limited by Dhan - now one call every 5.1 s
[15:14:09] API       rate limited by Dhan - now one call every 5.1 s
[15:14:37] API       rate limited by Dhan - now one call every 5.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 15:07:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:09:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:10:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:12:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:14:17] DATA      buffer gap > 15s - cleared, re-warming
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:14:06] WARM      bar history loaded for all 668 contracts
[15:14:19] WARM      bar history loaded for all 670 contracts
[15:14:32] WARM      bar history loaded for all 672 contracts
[15:14:47] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:14:59] WARM      bar history loaded for all 674 contracts
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[15:12:14] API       rate limited by Dhan - now one call every 15.1 s
[15:13:38] API       rate limited by Dhan - now one call every 15.1 s
[15:14:08] API       rate limited by Dhan - now one call every 15.1 s
[15:14:38] API       rate limited by Dhan - now one call every 15.1 s
[15:14:54] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

