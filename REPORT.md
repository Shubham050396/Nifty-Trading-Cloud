# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:13 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.71 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,346 (-3.05%) | −₹2,272 (-6.02%) | +₹20,202 (+5.32%) | 2 | 2 | ₹37,723 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹8,638 (-1.11%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,156 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹12,618 (+6.96%) | −₹53,058 (-5.02%) | 16 | 9 | ₹1,81,254 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,195 (-8.23%) | ₹0 | 0 | 8 | ₹2,21,096 |
| **Total** | | **−₹49,472** | **−₹16,487** | **+₹8,311** | **24** | **29** | **₹12,16,229** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:04:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:04:38] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:06:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:06:38] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:10:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:10:39] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:07:51] API       rate limited by Dhan - now one call every 15.1 s
[12:08:31] API       rate limited by Dhan - now one call every 15.1 s
[12:09:53] API       rate limited by Dhan - now one call every 15.1 s
[12:10:54] API       rate limited by Dhan - now one call every 15.1 s
[12:11:14] API       rate limited by Dhan - now one call every 15.1 s
[12:12:35] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:10:54] API       rate limited by Dhan - now one call every 15.1 s
[12:11:38] SIGNAL    2026-11-03 22700 CE held above 373.65 for 5 min - fall-back exit is armed
[12:11:52] API       rate limited by Dhan - now one call every 15.1 s
[12:12:22] API       rate limited by Dhan - now one call every 15.1 s
[12:12:37] EXIT      L3 2026-11-03 22700 CE PUSH_FAILED @ 352.45  P&L Rs -78.00
[12:12:52] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:07:09] API       rate limited by Dhan - now one call every 15.1 s
[12:07:25] API       rate limited by Dhan - now one call every 15.1 s
[12:09:13] API       rate limited by Dhan - now one call every 15.1 s
[12:09:29] API       rate limited by Dhan - now one call every 15.1 s
[12:10:27] API       rate limited by Dhan - now one call every 15.1 s
[12:12:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:02:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:04:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:06:28] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:08:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:09:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:11:57] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:09:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:10:11] SIGNAL    JIOFIN 220 PE 27 Oct crossed EMA 144 at 6.65 - not taken: under EMA 55, momentum 0.2%
[12:10:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:11:27] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:11:38] WARM      bar history loaded for all 786 contracts
[12:12:33] WARM      bar history loaded for all 786 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:09:44] API       rate limited by Dhan - now one call every 15.1 s
[12:09:59] API       rate limited by Dhan - now one call every 15.1 s
[12:10:14] API       rate limited by Dhan - now one call every 15.1 s
[12:10:59] API       rate limited by Dhan - now one call every 15.1 s
[12:11:14] API       rate limited by Dhan - now one call every 15.1 s
[12:12:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

