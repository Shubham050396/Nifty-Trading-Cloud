# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 15:00 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.90 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹23,361 (+1.52%) | −₹8,664 (-0.87%) | +₹59,800 (+1.63%) | 17 | 10 | ₹10,00,301 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹27,286 (-7.52%) | −₹7,851 (-6.73%) | −₹27,375 (-3.83%) | 19 | 6 | ₹1,16,599 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹6,889 (-4.79%) | ₹0 | 0 | 8 | ₹1,43,844 |
| **Total** | | **−₹2,394** | **−₹23,404** | **+₹56,068** | **43** | **24** | **₹12,60,744** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:55:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:57:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:57:16] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 14:59:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 14:59:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 15:00:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:57:18] API       rate limited by Dhan - now one call every 15.1 s
[14:57:38] API       rate limited by Dhan - now one call every 15.1 s
[14:58:19] API       rate limited by Dhan - now one call every 15.1 s
[14:58:39] API       rate limited by Dhan - now one call every 15.1 s
[14:59:00] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[15:00:00] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:57:07] API       rate limited by Dhan - now one call every 15.1 s
[14:57:37] API       rate limited by Dhan - now one call every 15.1 s
[14:57:52] API       rate limited by Dhan - now one call every 15.1 s
[14:58:51] API       rate limited by Dhan - now one call every 15.1 s
[14:59:21] API       rate limited by Dhan - now one call every 15.1 s
[14:59:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:52:42] API       rate limited by Dhan - now one call every 15.1 s
[14:55:13] API       rate limited by Dhan - now one call every 15.1 s
[14:56:12] API       rate limited by Dhan - now one call every 15.1 s
[14:57:10] API       rate limited by Dhan - now one call every 15.1 s
[14:58:59] API       rate limited by Dhan - now one call every 15.1 s
[14:59:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:48:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:50:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:52:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:54:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:57:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 14:59:54] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:00:23] SIGNAL    AXISBANK 1220 PE 27 Oct crossed EMA 144 at 27.85 - not taken: under EMA 55
[15:00:23] EXIT      SELL AXISBANK 1240 CE 27 Oct EMA_STOP @ 23.70  -19.4%  P&L Rs -3562.50
[15:00:23] SIGNAL    ETERNAL 315 PE 27 Oct crossed EMA 144 at 7.55 - not taken: under EMA 55, momentum -2.6%
[15:00:23] SIGNAL    INDIGO 5000 PE 27 Oct crossed EMA 144 at 171.75 - not taken: momentum 3.4%
[15:00:23] SIGNAL    KOTAKBANK 415 CE 27 Oct crossed EMA 144 at 11.90 - not taken: momentum 1.3%
[15:00:23] SIGNAL    KOTAKBANK 425 CE 27 Oct crossed EMA 144 at 7.00 - not taken: momentum 2.9%
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:54:17] API       rate limited by Dhan - now one call every 15.1 s
[14:54:32] API       rate limited by Dhan - now one call every 15.1 s
[14:57:38] API       rate limited by Dhan - now one call every 12.1 s
[14:58:03] API       rate limited by Dhan - now one call every 15.1 s
[14:58:33] API       rate limited by Dhan - now one call every 15.1 s
[14:59:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

