# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 13:49 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | +₹6,019 (+0.60%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,635 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,125 (-5.58%) | +₹5,128 (+2.80%) | −₹14,214 (-2.35%) | 14 | 9 | ₹1,82,964 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹8,563 (-5.96%) | ₹0 | 0 | 7 | ₹1,43,744 |
| **Total** | | **+₹10,767** | **+₹2,584** | **+₹69,229** | **38** | **26** | **₹13,27,343** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 13:40:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:40:57] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:45:58] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:45:58] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 13:47:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 13:47:59] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:46:46] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:47:18] API       rate limited by Dhan - now one call every 15.1 s
[13:47:38] API       rate limited by Dhan - now one call every 15.1 s
[13:47:58] API       rate limited by Dhan - now one call every 15.1 s
[13:48:46] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:48:59] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:46:16] SKIP      L3 2026-10-13 22400 CE cross ignored - daily cap
[13:46:30] SKIP      L3 2026-10-19 22500 CE cross ignored - daily cap
[13:46:44] API       rate limited by Dhan - now one call every 15.1 s
[13:47:56] API       rate limited by Dhan - now one call every 15.1 s
[13:48:40] API       rate limited by Dhan - now one call every 15.1 s
[13:48:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:47:28] API       rate limited by Dhan - now one call every 5.1 s
[13:47:38] API       rate limited by Dhan - now one call every 6.1 s
[13:47:50] API       rate limited by Dhan - now one call every 8.1 s
[13:48:20] API       rate limited by Dhan - now one call every 10.1 s
[13:49:07] API       rate limited by Dhan - now one call every 13.1 s
[13:49:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 13:41:19] EXIT      SIGNAL_DECAY 22550 195 CALL @ 107.55  gross +478  net +403  (0.7)
[2026-10-05 13:42:32] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:44:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:46:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:47:13] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 13:49:42] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:48:48] API       market quote: rate limited by Dhan - now one call every 2.5 s
[13:48:59] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:49:08] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:49:16] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:49:24] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:49:32] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:42:40] API       rate limited by Dhan - now one call every 15.1 s
[13:42:55] API       rate limited by Dhan - now one call every 15.1 s
[13:43:25] API       rate limited by Dhan - now one call every 15.1 s
[13:44:37] API       rate limited by Dhan - now one call every 15.1 s
[13:45:36] API       rate limited by Dhan - now one call every 15.1 s
[13:48:08] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

