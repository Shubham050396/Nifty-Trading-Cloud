# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:35 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.94 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | +₹3,377 (+0.34%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,871 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,624 (-7.36%) | −₹5,495 (-3.47%) | −₹23,712 (-3.52%) | 17 | 8 | ₹1,58,174 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6,974 (-4.85%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,268** | **−₹9,092** | **+₹59,731** | **41** | **26** | **₹13,02,889** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:24:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:24:08] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:27:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:27:09] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:32:10] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:32:10] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:28:45] API       rate limited by Dhan - now one call every 15.1 s
[14:31:08] API       rate limited by Dhan - now one call every 15.1 s
[14:31:54] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:32:50] API       rate limited by Dhan - now one call every 15.1 s
[14:33:31] API       rate limited by Dhan - now one call every 15.1 s
[14:34:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:31:46] API       rate limited by Dhan - now one call every 15.1 s
[14:32:44] API       rate limited by Dhan - now one call every 15.1 s
[14:33:00] API       rate limited by Dhan - now one call every 15.1 s
[14:33:58] API       rate limited by Dhan - now one call every 15.1 s
[14:34:28] API       rate limited by Dhan - now one call every 15.1 s
[14:34:59] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:30:13] API       rate limited by Dhan - now one call every 15.1 s
[14:33:45] API       rate limited by Dhan - now one call every 8.1 s
[14:34:01] API       rate limited by Dhan - now one call every 12.1 s
[14:34:14] API       rate limited by Dhan - now one call every 15.1 s
[14:34:29] API       rate limited by Dhan - now one call every 15.1 s
[14:34:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:26:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:27:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:28:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:29:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:30:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:33:33] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:30:22] SIGNAL    BANKBARODA 230 PE 27 Oct crossed EMA 144 at 4.57 - not taken: under EMA 55, premium under Rs 5
[14:30:46] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:31:38] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:31:56] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:33:11] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:33:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:32:44] API       rate limited by Dhan - now one call every 14.1 s
[14:32:59] API       rate limited by Dhan - now one call every 15.1 s
[14:33:29] API       rate limited by Dhan - now one call every 15.1 s
[14:33:44] API       rate limited by Dhan - now one call every 15.1 s
[14:34:29] API       rate limited by Dhan - now one call every 15.1 s
[14:34:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

