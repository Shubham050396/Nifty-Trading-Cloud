# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:50 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.91 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹6,136 (-0.61%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,288 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,624 (-7.36%) | −₹5,456 (-3.45%) | −₹23,712 (-3.52%) | 17 | 8 | ₹1,58,174 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6,642 (-4.62%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,268** | **−₹18,234** | **+₹59,731** | **41** | **26** | **₹13,02,306** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:39:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:39:12] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:46:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:46:13] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:50:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:50:14] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:45:45] API       rate limited by Dhan - now one call every 15.1 s
[14:46:26] API       rate limited by Dhan - now one call every 15.1 s
[14:47:27] API       rate limited by Dhan - now one call every 15.1 s
[14:47:47] API       rate limited by Dhan - now one call every 15.1 s
[14:48:49] API       rate limited by Dhan - now one call every 15.1 s
[14:49:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:46:12] API       rate limited by Dhan - now one call every 15.1 s
[14:47:11] API       rate limited by Dhan - now one call every 15.1 s
[14:47:55] API       rate limited by Dhan - now one call every 15.1 s
[14:48:11] API       rate limited by Dhan - now one call every 15.1 s
[14:49:09] API       rate limited by Dhan - now one call every 15.1 s
[14:50:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:44:07] API       rate limited by Dhan - now one call every 15.1 s
[14:44:37] API       rate limited by Dhan - now one call every 15.1 s
[14:45:36] API       rate limited by Dhan - now one call every 15.1 s
[14:46:34] API       rate limited by Dhan - now one call every 15.1 s
[14:48:56] API       rate limited by Dhan - now one call every 15.1 s
[14:49:54] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:33:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:40:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:42:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:44:15] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:46:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:48:42] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:45:20] SIGNAL    NTPC 325 PE 27 Oct crossed EMA 144 at 6.95 - not taken: under EMA 55
[14:46:02] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:47:24] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:48:00] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:49:00] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:49:29] WARM      bar history loaded for all 791 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:44:04] API       rate limited by Dhan - now one call every 15.1 s
[14:45:02] API       rate limited by Dhan - now one call every 15.1 s
[14:45:18] API       rate limited by Dhan - now one call every 15.1 s
[14:46:30] API       rate limited by Dhan - now one call every 15.1 s
[14:48:19] API       rate limited by Dhan - now one call every 15.1 s
[14:48:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

