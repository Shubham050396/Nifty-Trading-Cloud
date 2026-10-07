# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:18 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.84 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹25,932 (+2.62%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,89,231 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹11,370 (-3.78%) | +₹17,256 (+10.08%) | −₹49,535 (-4.49%) | 18 | 9 | ₹1,71,258 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,479 (-10.14%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹59,353** | **+₹19,709** | **−₹1,570** | **40** | **27** | **₹13,91,961** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:12:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:14:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:14:53] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:16:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:16:53] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:17:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:10:34] API       rate limited by Dhan - now one call every 15.1 s
[13:11:35] API       rate limited by Dhan - now one call every 15.1 s
[13:12:15] API       rate limited by Dhan - now one call every 15.1 s
[13:12:56] API       rate limited by Dhan - now one call every 15.1 s
[13:13:36] API       rate limited by Dhan - now one call every 15.1 s
[13:14:58] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:12:28] API       rate limited by Dhan - now one call every 15.1 s
[13:14:17] API       rate limited by Dhan - now one call every 15.1 s
[13:15:15] API       rate limited by Dhan - now one call every 15.1 s
[13:16:00] API       rate limited by Dhan - now one call every 15.1 s
[13:17:00] VIX       India VIX prev close 13.61 -> target 1000 ticks (Rs 50.00)
[13:17:12] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:14:00] API       rate limited by Dhan - now one call every 5.1 s
[13:14:19] API       rate limited by Dhan - now one call every 5.1 s
[13:14:37] API       rate limited by Dhan - now one call every 5.1 s
[13:15:36] API       rate limited by Dhan - now one call every 5.1 s
[13:16:34] API       rate limited by Dhan - now one call every 5.1 s
[13:17:32] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:54:12] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:55:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:57:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:59:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:01:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:02:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:14:59] WARM      bar history loaded for all 790 contracts
[13:15:01] SIGNAL    ICICIBANK 1340 CE 27 Oct crossed EMA 144 at 31.70 - not taken: momentum -4.8%
[13:15:01] EXIT      SELL ABB 7000 CE 27 Oct EMA_STOP @ 221.75  -17.9%  P&L Rs -6025.00
[13:15:02] SKIP      LODHA 1100 PE 27 Oct signal at 31.50 skipped - 20 trades already today
[13:15:14] WARM      bar history loaded for all 790 contracts
[13:15:53] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:12:59] API       rate limited by Dhan - now one call every 15.1 s
[13:14:48] API       rate limited by Dhan - now one call every 15.1 s
[13:15:47] API       rate limited by Dhan - now one call every 15.1 s
[13:16:45] API       rate limited by Dhan - now one call every 15.1 s
[13:17:00] API       rate limited by Dhan - now one call every 15.1 s
[13:18:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

