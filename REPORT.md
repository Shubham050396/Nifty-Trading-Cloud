# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 14:29 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹6,510 (+0.66%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,90,531 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹13,420 (-4.18%) | +₹15,778 (+10.42%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,364 (-9.85%) | ₹0 | 0 | 8 | ₹2,37,192 |
| **Total** | | **−₹61,403** | **−₹1,076** | **−₹3,620** | **41** | **26** | **₹13,79,131** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 14:20:07] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:25:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:25:08] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:27:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:27:09] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 14:28:09] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:27:49] API       rate limited by Dhan - now one call every 15.1 s
[14:28:09] API       rate limited by Dhan - now one call every 15.1 s
[14:28:30] API       rate limited by Dhan - now one call every 15.1 s
[14:28:42] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:28:50] API       rate limited by Dhan - now one call every 15.1 s
[14:29:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:27:06] API       rate limited by Dhan - now one call every 15.1 s
[14:27:50] API       rate limited by Dhan - now one call every 15.1 s
[14:28:05] API       rate limited by Dhan - now one call every 15.1 s
[14:28:21] SKIP      L2 2026-10-19 22600 CE cross ignored - daily cap
[14:28:36] API       rate limited by Dhan - now one call every 15.1 s
[14:29:06] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:25:46] API       rate limited by Dhan - now one call every 15.1 s
[14:26:44] API       rate limited by Dhan - now one call every 15.1 s
[14:27:29] API       rate limited by Dhan - now one call every 15.1 s
[14:27:44] SIGNAL    2026-11-23 24000 CE MACD crossed UP (bar close 60.70, hist -0.04 -> +0.02)
[14:27:44] SKIP      buy 2026-11-23 24000 CE ignored - premium 60.70 is outside 144 - 1600
[14:28:27] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:18:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:21:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:23:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:25:24] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:27:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:29:08] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:28:21] WARM      bar history loaded for all 791 contracts
[14:28:51] WARM      bar history loaded for all 791 contracts
[14:28:54] WARM      bar history loaded for all 791 contracts
[14:29:01] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:29:01] WARM      bar history loaded for all 791 contracts
[14:29:05] API       market quote: rate limited by Dhan - now one call every 2.5 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:23:25] API       rate limited by Dhan - now one call every 15.1 s
[14:23:55] API       rate limited by Dhan - now one call every 15.1 s
[14:25:32] API       rate limited by Dhan - now one call every 15.1 s
[14:26:31] API       rate limited by Dhan - now one call every 15.1 s
[14:27:01] API       rate limited by Dhan - now one call every 15.1 s
[14:28:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

