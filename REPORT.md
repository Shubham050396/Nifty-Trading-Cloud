# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:39 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.19 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,984 (+3.17%) | −₹3,500 (-0.60%) | +₹69,423 (+2.19%) | 9 | 10 | ₹5,80,633 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | +₹1,521 (+1.07%) | −₹11,956 (-2.08%) | 12 | 8 | ₹1,42,816 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹7,848 (-5.46%) | ₹0 | 0 | 7 | ₹1,43,744 |
| **Total** | | **+₹22,244** | **−₹9,827** | **+₹80,708** | **27** | **25** | **₹8,67,193** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:32:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:32:55] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:33:55] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:34:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:35:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:36:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:33:00] API       rate limited by Dhan - now one call every 15.1 s
[13:34:01] API       rate limited by Dhan - now one call every 15.1 s
[13:34:22] API       rate limited by Dhan - now one call every 15.1 s
[13:35:24] API       rate limited by Dhan - now one call every 15.1 s
[13:36:45] API       rate limited by Dhan - now one call every 15.1 s
[13:39:45] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:37:11] API       rate limited by Dhan - now one call every 15.1 s
[13:37:26] API       rate limited by Dhan - now one call every 15.1 s
[13:37:56] API       rate limited by Dhan - now one call every 15.1 s
[13:38:12] API       rate limited by Dhan - now one call every 15.1 s
[13:38:56] API       rate limited by Dhan - now one call every 15.1 s
[13:39:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:31:11] API       rate limited by Dhan - now one call every 5.1 s
[13:34:26] API       rate limited by Dhan - now one call every 5.1 s
[13:35:12] SIGNAL    2026-10-27 21000 CE MACD crossed UP (bar close 1624.25, hist -0.03 -> +0.53)
[13:35:12] SKIP      buy 2026-10-27 21000 CE ignored - premium 1624.25 is outside 144 - 1600
[13:36:46] API       rate limited by Dhan - now one call every 5.1 s
[13:38:26] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:42:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:44:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:47:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:48:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:50:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:52:43] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:35:03] SIGNAL    COALINDIA 430 PE 27 Oct crossed EMA 144 at 11.45 - not taken: momentum -5.0%
[13:37:56] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:38:21] WARM      bar history loaded for all 774 contracts
[13:38:26] WARM      bar history loaded for all 774 contracts
[13:38:45] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:38:57] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:33:11] API       rate limited by Dhan - now one call every 15.1 s
[13:34:10] API       rate limited by Dhan - now one call every 15.1 s
[13:35:59] API       rate limited by Dhan - now one call every 15.1 s
[13:36:57] API       rate limited by Dhan - now one call every 15.1 s
[13:38:09] API       rate limited by Dhan - now one call every 15.1 s
[13:38:27] VIX       India VIX prev close 14.46
```
</details>

