# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:52 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹14,840 (-2.18%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,82,041 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹8,454 (+11.85%) | +₹6,715 (+4.74%) | −₹29,711 (-3.40%) | 5 | 9 | ₹1,41,681 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,854 (-8.33%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹8,454** | **−₹25,979** | **+₹66,238** | **5** | **23** | **₹10,38,100** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:47:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:48:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:49:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:50:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:51:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:52:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:48:53] API       rate limited by Dhan - now one call every 15.1 s
[09:50:14] API       rate limited by Dhan - now one call every 15.1 s
[09:50:55] API       rate limited by Dhan - now one call every 15.1 s
[09:51:15] API       rate limited by Dhan - now one call every 15.1 s
[09:51:36] API       rate limited by Dhan - now one call every 15.1 s
[09:51:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:47:10] API       rate limited by Dhan - now one call every 15.1 s
[09:47:41] API       rate limited by Dhan - now one call every 15.1 s
[09:48:11] API       rate limited by Dhan - now one call every 15.1 s
[09:48:41] API       rate limited by Dhan - now one call every 15.1 s
[09:49:25] API       rate limited by Dhan - now one call every 15.1 s
[09:51:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:47:56] API       rate limited by Dhan - now one call every 6.1 s
[09:48:03] API       rate limited by Dhan - now one call every 9.1 s
[09:49:03] API       rate limited by Dhan - now one call every 8.1 s
[09:49:12] API       rate limited by Dhan - now one call every 13.1 s
[09:49:25] API       rate limited by Dhan - now one call every 15.1 s
[09:51:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 09:41:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:43:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:45:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:47:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:49:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 09:51:29] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:51:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:51:26] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:51:38] WARM      bar history loaded for all 776 contracts
[09:51:44] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:51:54] API       market quote: rate limited by Dhan - now one call every 9.1 s
[09:52:03] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:46:37] API       rate limited by Dhan - now one call every 15.1 s
[09:46:53] API       rate limited by Dhan - now one call every 15.1 s
[09:49:14] API       rate limited by Dhan - now one call every 15.1 s
[09:49:59] API       rate limited by Dhan - now one call every 15.1 s
[09:50:57] API       rate limited by Dhan - now one call every 15.1 s
[09:51:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

