# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:38 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.79 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | −₹552 (-2.44%) | +₹16,929 (+4.05%) | 4 | 1 | ₹22,640 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹42,123 (-3.85%) | −₹9,812 (-1.11%) | +₹30,183 (+0.52%) | 12 | 9 | ₹8,84,471 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹17,954 (+8.83%) | −₹53,058 (-5.02%) | 16 | 10 | ₹2,03,316 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹21,259 (-9.18%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹61,633** | **−₹13,669** | **−₹3,851** | **32** | **28** | **₹13,41,899** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:26:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:26:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:28:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:28:43] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:36:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:36:45] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:31:20] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:31:35] API       rate limited by Dhan - now one call every 15.1 s
[12:32:56] API       rate limited by Dhan - now one call every 15.1 s
[12:34:58] API       rate limited by Dhan - now one call every 15.1 s
[12:35:39] API       rate limited by Dhan - now one call every 15.1 s
[12:37:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:36:50] GAP       2026-10-27 21500 PE: no prices for 5 min - bar history restarts
[12:36:50] GAP       2026-10-27 23700 CE: no prices for 5 min - bar history restarts
[12:36:50] GAP       2026-10-27 23700 PE: no prices for 5 min - bar history restarts
[12:37:18] API       rate limited by Dhan - now one call every 15.1 s
[12:38:03] API       rate limited by Dhan - now one call every 15.1 s
[12:38:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:35:23] EXIT      SHORT 2027-03-30 24000 PE MACD_UP @ 1092.00  P&L Rs -1992.25
[12:35:23] ENTRY     BUY 2027-03-30 24000 PE @ 1092.00  (bar close 1100.00, MACD hist +0.34, VIX 13.61)
[12:35:34] API       rate limited by Dhan - now one call every 15.1 s
[12:36:32] SIGNAL    2026-10-27 23000 CE MACD crossed DOWN (bar close 142.85, hist +0.05 -> -0.16)
[12:36:32] EXIT      LONG 2026-10-27 23000 CE MACD_DOWN @ 141.50  P&L Rs -1202.50
[12:36:32] SKIP      short 2026-10-27 23000 CE ignored - premium 142.85 is outside 144 - 1600
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:27:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:29:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:31:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:33:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:35:05] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:37:28] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:35:11] SIGNAL    RECLTD 305 PE 27 Oct crossed EMA 144 at 10.15 - not taken: under EMA 55, momentum 3.0%
[12:35:11] SIGNAL    INDHOTEL 720 CE 27 Oct crossed EMA 144 at 25.00 - not taken: momentum -9.1%
[12:35:20] SKIP      DLF 640 PE 27 Oct signal at 11.60 skipped - 10 positions already open
[12:35:45] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:37:01] WARM      bar history loaded for all 788 contracts
[12:37:53] API       market quote: rate limited by Dhan - now one call every 8.6 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:30:46] API       rate limited by Dhan - now one call every 15.1 s
[12:33:17] API       rate limited by Dhan - now one call every 15.1 s
[12:33:33] API       rate limited by Dhan - now one call every 15.1 s
[12:35:43] API       rate limited by Dhan - now one call every 15.1 s
[12:36:42] API       rate limited by Dhan - now one call every 15.1 s
[12:37:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

