# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:02 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.69 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | +₹1,238 (+2.72%) | +₹20,280 (+5.68%) | 1 | 2 | ₹45,480 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹34,177 (-3.98%) | +₹72,306 (+1.54%) | 0 | 8 | ₹8,58,285 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | +₹4,642 (+2.19%) | −₹45,941 (-4.70%) | 12 | 10 | ₹2,12,025 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹15,215 (-6.91%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹9,044** | **−₹43,512** | **+₹48,740** | **13** | **28** | **₹13,36,122** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:54:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:59:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:59:24] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 11:00:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:02:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:02:24] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:56:00] API       rate limited by Dhan - now one call every 15.1 s
[10:58:42] API       rate limited by Dhan - now one call every 15.1 s
[10:59:12] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:00:04] API       rate limited by Dhan - now one call every 15.1 s
[11:01:25] API       rate limited by Dhan - now one call every 15.1 s
[11:02:06] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:58:59] API       rate limited by Dhan - now one call every 15.1 s
[10:59:30] API       rate limited by Dhan - now one call every 15.1 s
[11:00:28] API       rate limited by Dhan - now one call every 15.1 s
[11:00:58] API       rate limited by Dhan - now one call every 15.1 s
[11:01:56] API       rate limited by Dhan - now one call every 15.1 s
[11:02:26] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:00:04] SIGNAL    2027-03-30 24000 CE MACD crossed UP (bar close 481.90, hist -0.28 -> +0.21)
[11:00:04] ENTRY     BUY 2027-03-30 24000 CE @ 484.90  (bar close 481.90, MACD hist +0.21, VIX 13.61)
[11:00:18] API       rate limited by Dhan - now one call every 15.1 s
[11:00:48] SIGNAL    2026-12-29 22000 PE MACD crossed DOWN (bar close 212.00, hist +0.37 -> -0.06)
[11:00:48] ENTRY     SELL SHORT 2026-12-29 22000 PE @ 212.65  (bar close 212.00, MACD hist -0.06, VIX 13.61)
[11:01:43] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:52:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:54:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:56:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:58:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:00:03] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:02:18] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:01:20] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:01:25] API       market quote: rate limited by Dhan - now one call every 2.5 s
[11:01:30] API       market quote: rate limited by Dhan - now one call every 3.5 s
[11:01:49] WARM      bar history loaded for all 782 contracts
[11:02:13] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:02:30] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:59:42] API       rate limited by Dhan - now one call every 15.1 s
[11:00:54] API       rate limited by Dhan - now one call every 15.1 s
[11:01:38] API       rate limited by Dhan - now one call every 15.1 s
[11:01:54] API       rate limited by Dhan - now one call every 15.1 s
[11:01:56] VIX       India VIX prev close 13.61
[11:02:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

