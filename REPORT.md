# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 11:23 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.86 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹367 (+0.55%) | +₹3,286 (+20.69%) | +₹20,787 (+7.19%) | 3 | 1 | ₹15,883 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹29,244 (+4.15%) | +₹36,439 (+1.71%) | 0 | 6 | ₹7,05,235 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹6,415 (-5.88%) | −₹2,212 (-0.49%) | 6 | 6 | ₹1,09,151 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹4,537 (-7.52%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹1,757** | **+₹21,578** | **+₹56,707** | **9** | **17** | **₹8,90,583** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 11:14:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:14:21] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:15:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:18:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 11:18:22] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 11:19:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:18:26] API       rate limited by Dhan - now one call every 15.1 s
[11:19:48] API       rate limited by Dhan - now one call every 15.1 s
[11:20:24] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:20:29] API       rate limited by Dhan - now one call every 15.1 s
[11:21:09] API       rate limited by Dhan - now one call every 15.1 s
[11:22:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:21:40] GAP       2026-10-27 22900 PE: no prices for 6 min - bar history restarts
[11:21:40] GAP       2026-10-27 21500 CE: no prices for 6 min - bar history restarts
[11:21:40] GAP       2026-10-27 21500 PE: no prices for 6 min - bar history restarts
[11:21:54] API       rate limited by Dhan - now one call every 15.1 s
[11:22:38] API       rate limited by Dhan - now one call every 15.1 s
[11:23:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:17:22] API       rate limited by Dhan - now one call every 15.1 s
[11:17:53] API       rate limited by Dhan - now one call every 15.1 s
[11:19:42] API       rate limited by Dhan - now one call every 15.1 s
[11:20:40] API       rate limited by Dhan - now one call every 15.1 s
[11:21:39] API       rate limited by Dhan - now one call every 15.1 s
[11:23:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 11:12:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:14:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:15:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:18:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:21:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 11:23:30] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:20:23] SIGNAL    TMPV 280 PE 27 Oct crossed EMA 144 at 5.90 - not taken: under EMA 55, momentum -5.6%
[11:20:23] SIGNAL    KOTAKBANK 410 CE 27 Oct crossed EMA 144 at 14.20 - not taken: momentum -7.2%
[11:20:47] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:21:23] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:22:23] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:23:23] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:18:56] API       rate limited by Dhan - now one call every 15.1 s
[11:19:26] API       rate limited by Dhan - now one call every 15.1 s
[11:20:25] API       rate limited by Dhan - now one call every 15.1 s
[11:21:49] API       rate limited by Dhan - now one call every 15.1 s
[11:23:27] API       rate limited by Dhan - now one call every 15.1 s
[11:23:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

