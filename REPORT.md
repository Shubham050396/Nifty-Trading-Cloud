# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 15:05 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.02 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹15,379 (-1.54%) | +₹59,800 (+1.63%) | 17 | 10 | ₹9,99,766 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹27,286 (-7.52%) | −₹6,762 (-5.80%) | −₹27,375 (-3.83%) | 19 | 6 | ₹1,16,599 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹5,440 (-3.55%) | ₹0 | 0 | 8 | ₹1,53,295 |
| **Total** | | **−₹2,394** | **−₹27,581** | **+₹56,068** | **43** | **24** | **₹12,69,660** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:57:16] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:59:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:59:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 15:00:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 15:03:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 15:03:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:01:22] API       rate limited by Dhan - now one call every 15.1 s
[15:02:44] API       rate limited by Dhan - now one call every 15.1 s
[15:03:45] API       rate limited by Dhan - now one call every 15.1 s
[15:04:05] API       rate limited by Dhan - now one call every 15.1 s
[15:05:07] API       rate limited by Dhan - now one call every 15.1 s
[15:05:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:01:49] API       rate limited by Dhan - now one call every 15.1 s
[15:03:26] API       rate limited by Dhan - now one call every 15.1 s
[15:03:41] API       rate limited by Dhan - now one call every 15.1 s
[15:04:26] API       rate limited by Dhan - now one call every 15.1 s
[15:04:41] API       rate limited by Dhan - now one call every 15.1 s
[15:05:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:57:10] API       rate limited by Dhan - now one call every 15.1 s
[14:58:59] API       rate limited by Dhan - now one call every 15.1 s
[14:59:57] API       rate limited by Dhan - now one call every 15.1 s
[15:00:56] API       rate limited by Dhan - now one call every 15.1 s
[15:03:27] API       rate limited by Dhan - now one call every 15.1 s
[15:04:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:52:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:54:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:57:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:59:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:02:06] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:04:43] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:03:05] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:04:05] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:05:12] SIGNAL    NTPC 320 PE 27 Oct crossed EMA 144 at 4.85 - not taken: under EMA 55, premium under Rs 5
[15:05:12] SIGNAL    ULTRACEMCO 11000 PE 27 Oct crossed EMA 144 at 290.00 - not taken: under EMA 55, momentum -1.0%
[15:05:12] SIGNAL    BANKBARODA 235 PE 27 Oct crossed EMA 144 at 6.80 - not taken: under EMA 55
[15:05:12] SIGNAL    BANKBARODA 230 PE 27 Oct crossed EMA 144 at 4.60 - not taken: under EMA 55, premium under Rs 5
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[15:01:00] API       rate limited by Dhan - now one call every 15.1 s
[15:02:24] API       rate limited by Dhan - now one call every 15.1 s
[15:02:55] API       rate limited by Dhan - now one call every 15.1 s
[15:03:53] API       rate limited by Dhan - now one call every 15.1 s
[15:05:05] SIGNAL    2026-10-27 23000 CE VIX Fix crossed above 10.00 (9.62 -> 10.92, bar close 145.10)
[15:05:05] ENTRY     BUY 2026-10-27 23000 CE @ 145.40 x 65  (Rs 9,451) - buy 2 of 10, average 149.15, target 223.73
```
</details>

