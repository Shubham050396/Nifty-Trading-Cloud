# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:53 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.84 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹634 (-1.37%) | +₹3,724 (+10.18%) | +₹19,786 (+7.37%) | 2 | 2 | ₹36,592 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹31,171 (+5.52%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,64,392 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,124 (-2.04%) | −₹4,642 (-4.94%) | −₹2,212 (-0.49%) | 6 | 5 | ₹94,051 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹3,152 (-5.23%) | ₹0 | 0 | 4 | ₹60,314 |
| **Total** | | **−₹2,758** | **+₹27,101** | **+₹55,706** | **8** | **16** | **₹7,55,349** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:37:11] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:50:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:50:14] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:51:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:52:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:53:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:49:34] API       rate limited by Dhan - now one call every 15.1 s
[10:49:54] API       rate limited by Dhan - now one call every 15.1 s
[10:50:15] API       rate limited by Dhan - now one call every 15.1 s
[10:51:16] API       rate limited by Dhan - now one call every 15.1 s
[10:52:37] API       rate limited by Dhan - now one call every 15.1 s
[10:52:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:49:45] API       rate limited by Dhan - now one call every 15.1 s
[10:50:29] API       rate limited by Dhan - now one call every 15.1 s
[10:51:28] API       rate limited by Dhan - now one call every 15.1 s
[10:51:43] API       rate limited by Dhan - now one call every 15.1 s
[10:52:42] API       rate limited by Dhan - now one call every 15.1 s
[10:53:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:50:09] API       rate limited by Dhan - now one call every 15.1 s
[10:50:25] API       rate limited by Dhan - now one call every 15.1 s
[10:50:55] SIGNAL    2026-11-23 24000 CE MACD crossed DOWN (bar close 68.85, hist +0.07 -> -0.01)
[10:50:55] SKIP      short 2026-11-23 24000 CE ignored - premium 68.85 is outside 144 - 1600
[10:52:02] API       rate limited by Dhan - now one call every 15.1 s
[10:53:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:41:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:45:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:46:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:48:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:51:00] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:53:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:49:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:50:21] WARM      bar history loaded for all 740 contracts
[10:50:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:51:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:52:28] WARM      bar history loaded for all 740 contracts
[10:52:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:48:13] API       rate limited by Dhan - now one call every 15.1 s
[10:49:38] API       rate limited by Dhan - now one call every 15.1 s
[10:51:38] API       rate limited by Dhan - now one call every 15.1 s
[10:51:54] API       rate limited by Dhan - now one call every 15.1 s
[10:52:38] API       rate limited by Dhan - now one call every 15.1 s
[10:52:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

