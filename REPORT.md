# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:13 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.84 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹30,956 (+3.13%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,873 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹5,345 (-2.00%) | +₹12,478 (+6.09%) | −₹43,510 (-4.07%) | 17 | 10 | ₹2,05,001 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹23,323 (-10.08%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹53,328** | **+₹20,111** | **+₹4,455** | **39** | **28** | **₹14,25,346** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 13:07:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:08:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:09:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:10:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:11:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:12:52] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:06:50] API       rate limited by Dhan - now one call every 15.1 s
[13:08:11] API       rate limited by Dhan - now one call every 15.1 s
[13:10:34] API       rate limited by Dhan - now one call every 15.1 s
[13:11:35] API       rate limited by Dhan - now one call every 15.1 s
[13:12:15] API       rate limited by Dhan - now one call every 15.1 s
[13:12:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:10:45] GAP       2026-10-13 21500 PE: no prices for 4 min - bar history restarts
[13:10:45] GAP       2026-10-13 23700 CE: no prices for 4 min - bar history restarts
[13:10:45] GAP       2026-10-13 23700 PE: no prices for 4 min - bar history restarts
[13:11:11] SKIP      L2 2026-10-27 22500 PE cross ignored - daily cap
[13:11:58] API       rate limited by Dhan - now one call every 15.1 s
[13:12:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:01:29] API       rate limited by Dhan - now one call every 15.1 s
[13:02:40] API       rate limited by Dhan - now one call every 15.1 s
[13:03:27] VIX       India VIX prev close 13.61 - entries allowed
[13:06:12] API       rate limited by Dhan - now one call every 8.1 s
[13:07:05] API       rate limited by Dhan - now one call every 6.1 s
[13:10:35] API       rate limited by Dhan - now one call every 5.1 s
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
[13:10:04] SKIP      VEDL 255 PE 27 Oct signal at 6.50 skipped - 20 trades already today
[13:10:30] WARM      bar history loaded for all 790 contracts
[13:10:35] WARM      bar history loaded for all 790 contracts
[13:10:38] WARM      bar history loaded for all 790 contracts
[13:10:55] WARM      bar history loaded for all 790 contracts
[13:10:57] SIGNAL    RECLTD 290 PE 27 Oct crossed EMA 144 at 4.50 - not taken: under EMA 55, premium under Rs 5
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:06:33] API       rate limited by Dhan - now one call every 15.1 s
[13:07:31] API       rate limited by Dhan - now one call every 15.1 s
[13:09:20] API       rate limited by Dhan - now one call every 15.1 s
[13:10:18] API       rate limited by Dhan - now one call every 15.1 s
[13:12:29] API       rate limited by Dhan - now one call every 15.1 s
[13:12:59] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

