# NIFTY Cloud report

**Finished for the day at 15:15 IST** · updated 05 Oct 2026 15:15 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.00 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | +₹16,000 (+0.81%) | −₹6,487 (-0.52%) | +₹52,439 (+1.28%) | 23 | 10 | ₹12,47,619 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | −₹27,286 (-7.52%) | −₹6,454 (-5.53%) | −₹27,375 (-3.83%) | 19 | 6 | ₹1,16,599 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | ✅ saved | ₹0 | −₹6,902 (-4.50%) | ₹0 | 0 | 8 | ₹1,53,295 |
| **Total** | | **−₹9,755** | **−₹19,843** | **+₹48,707** | **49** | **24** | **₹15,17,513** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 15:03:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 15:07:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 15:07:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 15:13:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 15:13:20] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:09:31] API       rate limited by Dhan - now one call every 15.1 s
[15:10:53] API       rate limited by Dhan - now one call every 15.1 s
[15:12:15] API       rate limited by Dhan - now one call every 15.1 s
[15:12:35] API       rate limited by Dhan - now one call every 15.1 s
[15:13:36] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:11:29] GAP       2026-10-06 23500 PE: no prices for 4 min - bar history restarts
[15:12:19] API       rate limited by Dhan - now one call every 15.1 s
[15:13:04] API       rate limited by Dhan - now one call every 15.1 s
[15:14:02] API       rate limited by Dhan - now one call every 15.1 s
[15:14:18] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[15:15:01] SIGNAL    2027-03-30 24000 PE MACD crossed UP (bar close 1184.95, hist -0.21 -> +0.06)
[15:15:01] EXIT      SHORT 2027-03-30 24000 PE MACD_UP @ 1187.90  P&L Rs -3227.25
[15:15:01] ENTRY     BUY 2027-03-30 24000 PE @ 1187.90  (bar close 1184.95, MACD hist +0.06, VIX 14.46)
[15:15:01] SIGNAL    2027-03-30 24000 CE MACD crossed DOWN (bar close 457.80, hist +0.07 -> -0.12)
[15:15:01] SKIP      short 2027-03-30 24000 CE ignored - open-position cap
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 15:07:46] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:09:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:11:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:13:01] HALT      HALTED: session over (15:25)
[2026-10-05 15:13:22] DATA      buffer gap > 15s - cleared, re-warming
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:11:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:12:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:13:04] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:13:57] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:14:59] WARM      bar history loaded for all 791 contracts
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[15:10:13] API       rate limited by Dhan - now one call every 15.1 s
[15:11:11] API       rate limited by Dhan - now one call every 15.1 s
[15:11:56] API       rate limited by Dhan - now one call every 15.1 s
[15:13:56] API       rate limited by Dhan - now one call every 15.1 s
[15:14:27] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

