# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:39 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.14 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹2,190 (+2.23%) | −₹270 (-1.71%) | +₹22,610 (+7.06%) | 5 | 1 | ₹15,753 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹8,853 (+1.14%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,73,968 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹560 (+0.65%) | −₹11,956 (-2.08%) | 12 | 5 | ₹86,249 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹3,994 (-5.60%) | ₹0 | 0 | 6 | ₹71,318 |
| **Total** | | **+₹23,605** | **+₹5,149** | **+₹82,069** | **24** | **22** | **₹9,47,288** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:22:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:22:38] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:34:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:34:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:37:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:37:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:32:51] API       rate limited by Dhan - now one call every 15.1 s
[12:33:11] API       rate limited by Dhan - now one call every 15.1 s
[12:34:12] API       rate limited by Dhan - now one call every 15.1 s
[12:35:55] API       rate limited by Dhan - now one call every 15.1 s
[12:37:16] API       rate limited by Dhan - now one call every 15.1 s
[12:37:34] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:36:29] GAP       2026-10-27 21400 PE: no prices for 4 min - bar history restarts
[12:36:42] API       rate limited by Dhan - now one call every 15.1 s
[12:38:19] API       rate limited by Dhan - now one call every 15.1 s
[12:38:35] API       rate limited by Dhan - now one call every 15.1 s
[12:38:50] API       rate limited by Dhan - now one call every 15.1 s
[12:39:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:36:34] API       rate limited by Dhan - now one call every 6.1 s
[12:36:47] API       rate limited by Dhan - now one call every 8.1 s
[12:37:17] API       rate limited by Dhan - now one call every 10.1 s
[12:37:47] API       rate limited by Dhan - now one call every 15.1 s
[12:38:02] API       rate limited by Dhan - now one call every 15.1 s
[12:38:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:29:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:31:52] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:33:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:34:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:37:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:38:58] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:34:34] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:35:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:35:29] SKIP      COALINDIA 415 PE 27 Oct signal at 5.25 skipped - already 1 open on COALINDIA
[12:37:11] API       market quote: rate limited by Dhan - now one call every 8.6 s
[12:38:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:39:07] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:35:17] API       rate limited by Dhan - now one call every 15.1 s
[12:35:32] API       rate limited by Dhan - now one call every 15.1 s
[12:36:31] API       rate limited by Dhan - now one call every 15.1 s
[12:37:29] API       rate limited by Dhan - now one call every 15.1 s
[12:38:16] VIX       India VIX prev close 14.46
[12:39:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

