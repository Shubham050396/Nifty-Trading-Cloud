# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:48 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.46 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹4,833 (+12.99%) | ₹0 (+0.00%) | +₹12,750 (+8.41%) | 2 | 1 | ₹15,727 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹21,824 (+5.31%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,10,796 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹7,268 (+9.40%) | +₹9,871 (+12.43%) | −₹6,135 (-2.75%) | 4 | 4 | ₹79,426 |
| **Total** | | **+₹45,160** | **+₹31,695** | **+₹22,790** | **14** | **9** | **₹5,05,949** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:41:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:41:21] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:42:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:43:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:48:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:48:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:46:43] API       rate limited by Dhan - now one call every 15.1 s
[12:47:03] API       rate limited by Dhan - now one call every 15.1 s
[12:47:23] API       rate limited by Dhan - now one call every 15.1 s
[12:47:43] API       rate limited by Dhan - now one call every 15.1 s
[12:48:04] API       rate limited by Dhan - now one call every 15.1 s
[12:48:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:47:00] API       rate limited by Dhan - now one call every 15.1 s
[12:47:15] ENTRY     L2 BUY 2026-10-06 22600 PE @ 241.95  target 291.95  trail 205.66 (15%)
[12:47:30] API       rate limited by Dhan - now one call every 15.1 s
[12:47:45] API       rate limited by Dhan - now one call every 15.1 s
[12:48:01] API       rate limited by Dhan - now one call every 15.1 s
[12:48:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:41:59] API       rate limited by Dhan - now one call every 15.1 s
[12:44:40] API       rate limited by Dhan - now one call every 15.1 s
[12:45:10] SIGNAL    2026-10-27 23000 CE MACD crossed DOWN (bar close 129.75, hist +0.25 -> -0.04)
[12:45:10] SKIP      short 2026-10-27 23000 CE ignored - premium 129.75 is outside 144 - 1600
[12:47:29] API       rate limited by Dhan - now one call every 14.1 s
[12:47:44] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:37:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:40:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:43:00] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:43:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:46:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:48:24] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:46:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:46:44] WARM      bar history loaded for all 1534 contracts
[12:46:58] WARM      bar history loaded for all 1538 contracts
[12:47:45] API       chart history: rate limited by Dhan - now one call every 1.2 s
[12:48:15] WARM      bar history loaded for all 1544 contracts
[12:48:19] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

