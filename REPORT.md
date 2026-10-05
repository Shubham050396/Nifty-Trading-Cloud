# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 12:44 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **15.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹2,190 (+2.23%) | −₹507 (-3.22%) | +₹22,610 (+7.06%) | 5 | 1 | ₹15,753 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹33,283 (+4.40%) | +₹4,209 (+0.54%) | +₹69,722 (+2.42%) | 7 | 10 | ₹7,74,158 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,868 (-5.33%) | −₹79 (-0.09%) | −₹11,956 (-2.08%) | 12 | 5 | ₹86,249 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹3,481 (-4.88%) | ₹0 | 0 | 6 | ₹71,318 |
| **Total** | | **+₹23,605** | **+₹142** | **+₹82,069** | **24** | **22** | **₹9,47,478** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 12:34:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:34:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:37:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:37:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 12:43:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 12:43:43] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:37:16] API       rate limited by Dhan - now one call every 15.1 s
[12:37:34] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:41:01] API       rate limited by Dhan - now one call every 15.1 s
[12:42:22] API       rate limited by Dhan - now one call every 15.1 s
[12:43:35] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:44:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:42:34] GAP       2026-10-06 21400 PE: no prices for 5 min - bar history restarts
[12:42:34] GAP       2026-10-06 23600 CE: no prices for 5 min - bar history restarts
[12:42:34] GAP       2026-10-06 23500 CE: no prices for 5 min - bar history restarts
[12:42:34] GAP       2026-10-06 23600 PE: no prices for 5 min - bar history restarts
[12:42:34] GAP       2026-10-06 23500 PE: no prices for 5 min - bar history restarts
[12:43:29] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:39:44] VIX       India VIX prev close 14.46 - entries allowed
[12:40:29] API       rate limited by Dhan - now one call every 15.1 s
[12:40:44] API       rate limited by Dhan - now one call every 15.1 s
[12:40:59] API       rate limited by Dhan - now one call every 15.1 s
[12:41:15] API       rate limited by Dhan - now one call every 15.1 s
[12:44:04] API       rate limited by Dhan - now one call every 14.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 12:33:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:34:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:37:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:38:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:40:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 12:42:14] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:40:15] SIGNAL    DLF 680 CE 27 Oct crossed EMA 144 at 15.40 - not taken: momentum 1.7%
[12:40:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:40:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:41:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:42:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:44:11] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:37:29] API       rate limited by Dhan - now one call every 15.1 s
[12:38:16] VIX       India VIX prev close 14.46
[12:39:18] API       rate limited by Dhan - now one call every 15.1 s
[12:39:49] API       rate limited by Dhan - now one call every 15.1 s
[12:42:20] API       rate limited by Dhan - now one call every 15.1 s
[12:43:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

