# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:18 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.76 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,346 (-3.05%) | −₹2,135 (-5.66%) | +₹20,202 (+5.32%) | 2 | 2 | ₹37,723 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹8,710 (-1.12%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,117 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹13,950 (+6.86%) | −₹53,058 (-5.02%) | 16 | 10 | ₹2,03,316 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,937 (-8.09%) | ₹0 | 0 | 8 | ₹2,21,758 |
| **Total** | | **−₹49,472** | **−₹14,832** | **+₹8,311** | **24** | **30** | **₹12,38,914** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:06:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:06:38] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:10:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:10:39] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:14:40] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:14:40] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:15:11] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:15:18] API       rate limited by Dhan - now one call every 15.1 s
[12:15:59] API       rate limited by Dhan - now one call every 15.1 s
[12:16:40] API       rate limited by Dhan - now one call every 15.1 s
[12:17:12] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:18:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:15:42] API       rate limited by Dhan - now one call every 15.1 s
[12:16:12] API       rate limited by Dhan - now one call every 15.1 s
[12:16:30] VIX       India VIX prev close 13.61 -> target 1000 ticks (Rs 50.00)
[12:17:10] API       rate limited by Dhan - now one call every 15.1 s
[12:17:40] API       rate limited by Dhan - now one call every 15.1 s
[12:18:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:10:27] API       rate limited by Dhan - now one call every 15.1 s
[12:12:27] API       rate limited by Dhan - now one call every 15.1 s
[12:13:39] API       rate limited by Dhan - now one call every 15.1 s
[12:13:54] API       rate limited by Dhan - now one call every 15.1 s
[12:15:31] API       rate limited by Dhan - now one call every 15.1 s
[12:16:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:08:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:09:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:11:57] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:13:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:15:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:17:22] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:15:10] SIGNAL    HAL 4700 CE 27 Oct crossed EMA 144 at 168.30 - not taken: momentum 0.7%
[12:15:10] SIGNAL    CANBK 120 PE 27 Oct crossed EMA 144 at 3.25 - not taken: under EMA 55, premium under Rs 5
[12:15:19] ENTRY     BUY LODHA 1120 PE 27 Oct x625 @ 35.30 (signal close 35.50, EMA 144 35.14, momentum 5.5%)  quick 40.59 till 12:45, target 60.01, stop below EMA 55
[12:15:19] SKIP      ADANIPORTS 1780 PE 27 Oct signal at 41.00 skipped - 10 positions already open
[12:15:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:16:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:14:28] API       rate limited by Dhan - now one call every 15.1 s
[12:14:43] API       rate limited by Dhan - now one call every 15.1 s
[12:15:13] SIGNAL    2026-10-27 24000 CE VIX Fix crossed above 10.00 (8.92 -> 10.38, bar close 10.15)
[12:15:13] ENTRY     BUY 2026-10-27 24000 CE @ 10.20 x 65  (Rs 663) - buy 5 of 10, average 12.66, target 18.99
[12:15:27] API       rate limited by Dhan - now one call every 15.1 s
[12:16:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

