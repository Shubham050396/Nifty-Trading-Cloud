# NIFTY Cloud report

**Running until 15:15 IST** · updated 06 Oct 2026 15:05 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **13.67 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹19,867 (+3.47%) | −₹40,849 (-5.97%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,84,206 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,415 (-22.41%) | +₹8,552 (+6.13%) | −₹41,790 (-5.37%) | 3 | 7 | ₹1,39,441 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,885 (-12.14%) | ₹0 | 0 | 8 | ₹1,55,606 |
| **Total** | | **+₹5,452** | **−₹51,182** | **+₹54,159** | **7** | **21** | **₹9,79,253** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 14:47:25] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:54:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:54:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:55:27] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 15:01:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 15:01:28] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:00:44] API       rate limited by Dhan - now one call every 15.1 s
[15:01:25] API       rate limited by Dhan - now one call every 15.1 s
[15:02:06] API       rate limited by Dhan - now one call every 15.1 s
[15:02:46] API       rate limited by Dhan - now one call every 15.1 s
[15:04:07] API       rate limited by Dhan - now one call every 15.1 s
[15:05:29] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:00:11] API       rate limited by Dhan - now one call every 15.1 s
[15:00:26] API       rate limited by Dhan - now one call every 15.1 s
[15:01:38] API       rate limited by Dhan - now one call every 15.1 s
[15:02:08] API       rate limited by Dhan - now one call every 15.1 s
[15:03:07] API       rate limited by Dhan - now one call every 15.1 s
[15:04:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:57:50] API       rate limited by Dhan - now one call every 15.1 s
[14:58:20] API       rate limited by Dhan - now one call every 15.1 s
[14:59:57] API       rate limited by Dhan - now one call every 15.1 s
[15:00:12] API       rate limited by Dhan - now one call every 15.1 s
[15:03:32] API       rate limited by Dhan - now one call every 10.1 s
[15:04:47] API       rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 14:56:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:58:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:00:06] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:01:26] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:03:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 15:05:34] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:03:21] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:03:48] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:04:15] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:04:26] WARM      bar history loaded for all 646 contracts
[15:05:22] SIGNAL    HAVELLS 1040 PE 27 Oct crossed EMA 144 at 20.90 - not taken: under EMA 55
[15:05:29] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[15:03:29] API       rate limited by Dhan - now one call every 15.1 s
[15:04:27] API       rate limited by Dhan - now one call every 15.1 s
[15:04:42] API       rate limited by Dhan - now one call every 15.1 s
[15:04:57] API       rate limited by Dhan - now one call every 15.1 s
[15:05:13] API       rate limited by Dhan - now one call every 15.1 s
[15:05:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

