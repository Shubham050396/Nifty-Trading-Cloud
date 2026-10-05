# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:25 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.92 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹198 (-0.02%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,490 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,624 (-7.36%) | −₹5,850 (-3.70%) | −₹23,712 (-3.52%) | 17 | 8 | ₹1,58,174 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6,512 (-4.53%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,268** | **−₹12,560** | **+₹59,731** | **41** | **26** | **₹13,02,508** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:12:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:12:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:22:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:22:07] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:24:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:24:08] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:19:35] API       rate limited by Dhan - now one call every 15.1 s
[14:19:51] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:21:58] API       rate limited by Dhan - now one call every 15.1 s
[14:23:19] API       rate limited by Dhan - now one call every 15.1 s
[14:24:20] API       rate limited by Dhan - now one call every 15.1 s
[14:24:40] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:23:15] GAP       2026-10-06 23600 CE: no prices for 8 min - bar history restarts
[14:23:15] GAP       2026-10-06 23500 CE: no prices for 8 min - bar history restarts
[14:23:15] GAP       2026-10-06 23600 PE: no prices for 8 min - bar history restarts
[14:23:15] GAP       2026-10-06 23500 PE: no prices for 8 min - bar history restarts
[14:24:11] API       rate limited by Dhan - now one call every 15.1 s
[14:24:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:19:19] API       rate limited by Dhan - now one call every 12.1 s
[14:20:06] API       rate limited by Dhan - now one call every 15.1 s
[14:21:04] API       rate limited by Dhan - now one call every 15.1 s
[14:22:03] API       rate limited by Dhan - now one call every 15.1 s
[14:22:18] API       rate limited by Dhan - now one call every 15.1 s
[14:23:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:09:52] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:12:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:14:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:17:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:20:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:21:34] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:20:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:21:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:22:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:23:03] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:23:31] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:24:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:22:49] API       rate limited by Dhan - now one call every 15.1 s
[14:23:04] API       rate limited by Dhan - now one call every 15.1 s
[14:23:49] API       rate limited by Dhan - now one call every 15.1 s
[14:24:04] API       rate limited by Dhan - now one call every 15.1 s
[14:25:03] SIGNAL    2026-10-27 23000 PE VIX Fix crossed above 10.00 (9.98 -> 11.42, bar close 510.00)
[14:25:03] SKIP      buy 2026-10-27 23000 PE ignored - Rs 72,426 in this strike already and this buy needs Rs 33,248 - over the Rs 100,000 limit
```
</details>

