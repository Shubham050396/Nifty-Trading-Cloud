# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:24 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.07 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹2,190 (+2.23%) | +₹214 (+1.36%) | +₹22,610 (+7.06%) | 5 | 1 | ₹15,753 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹12,402 (+1.60%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,026 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹8,590 (-5.56%) | −₹646 (-0.46%) | −₹8,679 (-1.71%) | 9 | 7 | ₹1,41,819 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,628 (-7.63%) | ₹0 | 0 | 4 | ₹60,619 |
| **Total** | | **+₹26,883** | **+₹7,342** | **+₹85,346** | **21** | **22** | **₹9,92,217** |

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
[12:17:32] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:18:55] API       rate limited by Dhan - now one call every 15.1 s
[12:19:36] API       rate limited by Dhan - now one call every 15.1 s
[12:20:58] API       rate limited by Dhan - now one call every 15.1 s
[12:21:32] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:22:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:21:20] API       rate limited by Dhan - now one call every 15.1 s
[12:22:05] API       rate limited by Dhan - now one call every 15.1 s
[12:22:20] API       rate limited by Dhan - now one call every 15.1 s
[12:22:36] EXIT      L2 2026-10-13 22600 PE PUSH_FAILED @ 250.10  P&L Rs 1062.75
[12:23:19] API       rate limited by Dhan - now one call every 15.1 s
[12:23:49] SKIP      L3 2026-10-19 22400 CE cross ignored - daily cap
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:21:05] API       rate limited by Dhan - now one call every 6.1 s
[12:21:36] API       rate limited by Dhan - now one call every 5.1 s
[12:22:04] API       rate limited by Dhan - now one call every 5.1 s
[12:22:10] API       rate limited by Dhan - now one call every 7.1 s
[12:22:36] API       rate limited by Dhan - now one call every 8.1 s
[12:23:07] API       rate limited by Dhan - now one call every 10.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:09:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:12:52] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:15:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:17:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:20:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:24:05] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:19:24] WARM      bar history loaded for all 772 contracts
[12:19:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:20:18] SIGNAL    VBL 430 CE 27 Oct crossed EMA 144 at 14.25 - not taken: momentum 2.9%
[12:21:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:22:19] WARM      bar history loaded for all 772 contracts
[12:22:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:18:21] API       rate limited by Dhan - now one call every 15.1 s
[12:19:20] API       rate limited by Dhan - now one call every 15.1 s
[12:20:18] API       rate limited by Dhan - now one call every 15.1 s
[12:20:48] API       rate limited by Dhan - now one call every 15.1 s
[12:21:19] API       rate limited by Dhan - now one call every 15.1 s
[12:22:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

