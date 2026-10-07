# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:37 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.68 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹942 (-1.55%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹7,342 (-0.95%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,385 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹12,068 (-5.53%) | +₹7,110 (+3.67%) | −₹50,232 (-4.92%) | 14 | 10 | ₹1,93,932 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,476 (-7.45%) | ₹0 | 0 | 8 | ₹2,21,096 |
| **Total** | | **−₹46,570** | **−₹17,650** | **+₹11,215** | **21** | **31** | **₹12,52,123** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:29:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:29:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:32:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:32:31] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:34:31] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:34:31] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:33:17] API       rate limited by Dhan - now one call every 15.1 s
[11:34:38] API       rate limited by Dhan - now one call every 15.1 s
[11:34:39] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:35:19] API       rate limited by Dhan - now one call every 15.1 s
[11:35:59] API       rate limited by Dhan - now one call every 15.1 s
[11:37:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:33:58] API       rate limited by Dhan - now one call every 15.1 s
[11:34:57] API       rate limited by Dhan - now one call every 15.1 s
[11:35:41] API       rate limited by Dhan - now one call every 15.1 s
[11:35:57] API       rate limited by Dhan - now one call every 15.1 s
[11:36:55] API       rate limited by Dhan - now one call every 15.1 s
[11:37:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:34:42] API       rate limited by Dhan - now one call every 11.1 s
[11:35:24] API       rate limited by Dhan - now one call every 15.1 s
[11:35:39] API       rate limited by Dhan - now one call every 15.1 s
[11:36:24] API       rate limited by Dhan - now one call every 15.1 s
[11:36:54] API       rate limited by Dhan - now one call every 15.1 s
[11:37:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:28:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:30:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:31:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:33:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:35:09] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:37:03] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:35:18] SIGNAL    PFC 320 PE 27 Oct crossed EMA 144 at 4.85 - not taken: under EMA 55, momentum -3.0%, premium under Rs 5
[11:35:18] SIGNAL    SOLARINDS 20250 CE 27 Oct crossed EMA 144 at 534.95 - not taken: momentum -9.3%
[11:35:18] SIGNAL    WIPRO 157.5 PE 27 Oct crossed EMA 144 at 3.50 - not taken: premium under Rs 5
[11:35:49] API       market quote: rate limited by Dhan - now one call every 7.5 s
[11:36:32] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:36:41] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:34:25] API       rate limited by Dhan - now one call every 15.1 s
[11:35:10] SIGNAL    2026-10-27 24000 CE VIX Fix crossed above 10.00 (9.56 -> 10.69, bar close 10.65)
[11:35:10] ENTRY     BUY 2026-10-27 24000 CE @ 10.75 x 65  (Rs 699) - buy 4 of 10, average 13.28, target 19.92
[11:35:24] API       rate limited by Dhan - now one call every 15.1 s
[11:36:22] API       rate limited by Dhan - now one call every 15.1 s
[11:36:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

