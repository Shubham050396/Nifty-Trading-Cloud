# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 15:10 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.00 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹19,227 (+1.05%) | −₹10,273 (-0.78%) | +₹55,666 (+1.41%) | 22 | 10 | ₹13,12,072 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹27,286 (-7.52%) | −₹7,536 (-6.46%) | −₹27,375 (-3.83%) | 19 | 6 | ₹1,16,599 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹5,817 (-3.79%) | ₹0 | 0 | 8 | ₹1,53,295 |
| **Total** | | **−₹6,528** | **−₹23,626** | **+₹51,934** | **48** | **24** | **₹15,81,966** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 14:59:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 15:00:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 15:03:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 15:03:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 15:07:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 15:07:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:04:05] API       rate limited by Dhan - now one call every 15.1 s
[15:05:07] API       rate limited by Dhan - now one call every 15.1 s
[15:05:27] API       rate limited by Dhan - now one call every 15.1 s
[15:06:48] API       rate limited by Dhan - now one call every 15.1 s
[15:08:10] API       rate limited by Dhan - now one call every 15.1 s
[15:09:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:07:25] GAP       2026-10-27 21400 CE: no prices for 5 min - bar history restarts
[15:07:25] GAP       2026-10-27 21400 PE: no prices for 5 min - bar history restarts
[15:08:18] API       rate limited by Dhan - now one call every 15.1 s
[15:08:33] API       rate limited by Dhan - now one call every 15.1 s
[15:09:32] API       rate limited by Dhan - now one call every 15.1 s
[15:10:30] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[15:10:13] SIGNAL    2026-12-29 23000 CE MACD crossed DOWN (bar close 468.00, hist +0.46 -> -0.03)
[15:10:13] EXIT      LONG 2026-12-29 23000 CE MACD_DOWN @ 471.20  P&L Rs -143.00
[15:10:13] ENTRY     SELL SHORT 2026-12-29 23000 CE @ 471.20  (bar close 468.00, MACD hist -0.03, VIX 14.46)
[15:10:13] SIGNAL    2026-12-29 24000 CE MACD crossed DOWN (bar close 154.00, hist +0.08 -> -0.12)
[15:10:13] EXIT      LONG 2026-12-29 24000 CE MACD_DOWN @ 154.55  P&L Rs -539.50
[15:10:13] ENTRY     SELL SHORT 2026-12-29 24000 CE @ 154.55  (bar close 154.00, MACD hist -0.12, VIX 14.46)
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 14:59:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:02:06] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:04:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:06:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:07:46] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 15:09:41] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:08:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:09:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:10:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:10:24] SIGNAL    KOTAKBANK 415 CE 27 Oct crossed EMA 144 at 11.50 - not taken: momentum -2.5%
[15:10:24] SIGNAL    KOTAKBANK 420 CE 27 Oct crossed EMA 144 at 8.95 - not taken: momentum -1.6%
[15:10:24] SIGNAL    KOTAKBANK 410 CE 27 Oct crossed EMA 144 at 14.70 - not taken: momentum 1.7%
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[15:06:38] API       rate limited by Dhan - now one call every 15.1 s
[15:07:23] API       rate limited by Dhan - now one call every 15.1 s
[15:09:12] API       rate limited by Dhan - now one call every 15.1 s
[15:09:27] API       rate limited by Dhan - now one call every 15.1 s
[15:09:58] API       rate limited by Dhan - now one call every 15.1 s
[15:10:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

