# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:29 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.07 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹2,190 (+2.23%) | −₹162 (-1.03%) | +₹22,610 (+7.06%) | 5 | 1 | ₹15,753 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹10,280 (+1.33%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,105 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹10,008 (-5.75%) | +₹34 (+0.03%) | −₹10,096 (-1.92%) | 10 | 6 | ₹1,22,424 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,196 (-6.92%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹25,465** | **+₹5,956** | **+₹83,929** | **22** | **21** | **₹9,72,901** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:15:36] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:15:36] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:20:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:20:37] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:22:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:22:38] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:20:58] API       rate limited by Dhan - now one call every 15.1 s
[12:21:32] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:22:19] API       rate limited by Dhan - now one call every 15.1 s
[12:25:02] API       rate limited by Dhan - now one call every 15.1 s
[12:27:33] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:29:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:29:04] GAP       2026-10-06 21400 CE: no prices for 4 min - bar history restarts
[12:29:04] GAP       2026-10-06 21400 PE: no prices for 4 min - bar history restarts
[12:29:04] GAP       2026-10-06 23600 CE: no prices for 4 min - bar history restarts
[12:29:04] GAP       2026-10-06 23500 CE: no prices for 4 min - bar history restarts
[12:29:04] GAP       2026-10-06 23600 PE: no prices for 4 min - bar history restarts
[12:29:04] GAP       2026-10-06 23500 PE: no prices for 4 min - bar history restarts
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:26:10] API       rate limited by Dhan - now one call every 5.1 s
[12:26:59] API       rate limited by Dhan - now one call every 5.1 s
[12:27:28] API       rate limited by Dhan - now one call every 5.1 s
[12:27:56] API       rate limited by Dhan - now one call every 5.1 s
[12:28:28] API       rate limited by Dhan - now one call every 5.1 s
[12:29:10] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:12:52] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:15:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:17:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:20:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:24:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:27:41] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:25:10] SIGNAL    INFY 1000 PE 27 Oct crossed EMA 144 at 29.10 - not taken: under EMA 55
[12:26:33] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:27:19] WARM      bar history loaded for all 772 contracts
[12:27:41] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:28:43] WARM      bar history loaded for all 774 contracts
[12:29:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:24:56] API       rate limited by Dhan - now one call every 15.1 s
[12:26:57] API       rate limited by Dhan - now one call every 15.1 s
[12:27:12] API       rate limited by Dhan - now one call every 15.1 s
[12:27:27] API       rate limited by Dhan - now one call every 15.1 s
[12:27:43] API       rate limited by Dhan - now one call every 15.1 s
[12:28:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

