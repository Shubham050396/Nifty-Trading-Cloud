# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 14:55 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.89 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹3,334 (-0.33%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,909 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹23,724 (-6.89%) | −₹6,891 (-5.11%) | −₹23,812 (-3.42%) | 18 | 7 | ₹1,34,974 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6,977 (-4.85%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **+₹1,168** | **−₹17,202** | **+₹59,631** | **42** | **25** | **₹12,79,727** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:46:13] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:50:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:50:14] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:54:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:54:15] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:55:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:51:52] API       rate limited by Dhan - now one call every 15.1 s
[14:52:13] API       rate limited by Dhan - now one call every 15.1 s
[14:53:14] API       rate limited by Dhan - now one call every 15.1 s
[14:54:15] API       rate limited by Dhan - now one call every 15.1 s
[14:54:35] API       rate limited by Dhan - now one call every 15.1 s
[14:54:57] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:51:57] API       rate limited by Dhan - now one call every 15.1 s
[14:52:55] API       rate limited by Dhan - now one call every 15.1 s
[14:53:25] API       rate limited by Dhan - now one call every 15.1 s
[14:53:41] API       rate limited by Dhan - now one call every 15.1 s
[14:53:56] API       rate limited by Dhan - now one call every 15.1 s
[14:54:55] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:46:34] API       rate limited by Dhan - now one call every 15.1 s
[14:48:56] API       rate limited by Dhan - now one call every 15.1 s
[14:49:54] API       rate limited by Dhan - now one call every 15.1 s
[14:50:53] API       rate limited by Dhan - now one call every 15.1 s
[14:52:42] API       rate limited by Dhan - now one call every 15.1 s
[14:55:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:44:15] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:46:30] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:48:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:50:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:52:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:54:35] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:51:16] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:52:15] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:53:15] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:54:57] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:55:11] WARM      bar history loaded for all 791 contracts
[14:55:15] EXIT      SELL KOTAKBANK 415 CE 27 Oct EMA_STOP @ 11.55  -0.4%  P&L Rs -100.00
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:50:53] API       rate limited by Dhan - now one call every 15.1 s
[14:51:52] API       rate limited by Dhan - now one call every 15.1 s
[14:52:22] API       rate limited by Dhan - now one call every 15.1 s
[14:52:52] API       rate limited by Dhan - now one call every 15.1 s
[14:54:17] API       rate limited by Dhan - now one call every 15.1 s
[14:54:32] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

