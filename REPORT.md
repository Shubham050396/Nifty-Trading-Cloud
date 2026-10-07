# NIFTY Cloud report

**Finished for the day at 14:55 IST** · updated 07 Oct 2026 14:55 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.73 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | −₹43,192 (-1.74%) | −₹10,042 (-1.12%) | +₹29,114 (+0.41%) | 26 | 10 | ₹8,95,363 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | −₹13,420 (-4.18%) | +₹19,588 (+12.94%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | ✅ saved | ₹0 | −₹25,665 (-10.21%) | ₹0 | 0 | 8 | ₹2,51,267 |
| **Total** | | **−₹54,730** | **−₹16,119** | **+₹3,053** | **51** | **26** | **₹12,98,038** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 14:49:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:50:13] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:51:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:52:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 14:53:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:52:33] API       rate limited by Dhan - now one call every 15.1 s
[14:53:54] API       rate limited by Dhan - now one call every 15.1 s
[14:54:00] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:54:35] API       rate limited by Dhan - now one call every 15.1 s
[14:55:16] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:52:11] GAP       2026-10-13 21500 PE: no prices for 5 min - bar history restarts
[14:52:11] GAP       2026-10-13 23700 CE: no prices for 5 min - bar history restarts
[14:52:11] GAP       2026-10-13 23700 PE: no prices for 5 min - bar history restarts
[14:54:07] API       rate limited by Dhan - now one call every 15.1 s
[14:55:31] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:51:32] API       rate limited by Dhan - now one call every 15.1 s
[14:51:47] API       rate limited by Dhan - now one call every 15.1 s
[14:53:12] API       rate limited by Dhan - now one call every 15.1 s
[14:53:27] API       rate limited by Dhan - now one call every 15.1 s
[14:54:39] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 14:49:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:51:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:53:02] HALT      HALTED: session over (15:25)
[2026-10-07 14:53:06] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 14:55:13] DATA      buffer gap > 15s - cleared, re-warming
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:55:27] SIGNAL    RECLTD 305 PE 27 Oct crossed EMA 144 at 10.45 - not taken: under EMA 55, momentum -0.5%
[14:55:27] SIGNAL    SIEMENS 3800 PE 27 Oct crossed EMA 144 at 103.00 - not taken: under EMA 55
[14:55:27] SIGNAL    TCS 2060 PE 27 Oct crossed EMA 144 at 55.20 - not taken: under EMA 55, momentum -0.1%
[14:55:27] SIGNAL    HDFCBANK 690 PE 27 Oct crossed EMA 144 at 7.75 - not taken: under EMA 55, momentum -13.4%
[14:55:45] API       market quote: rate limited by Dhan - now one call every 9.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:53:08] API       rate limited by Dhan - now one call every 15.1 s
[14:54:45] API       rate limited by Dhan - now one call every 15.1 s
[14:55:00] SIGNAL    2026-10-27 23000 CE VIX Fix crossed above 10.00 (8.99 -> 11.06, bar close 127.30)
[14:55:00] ENTRY     BUY 2026-10-27 23000 CE @ 128.25 x 65  (Rs 8,336) - buy 5 of 10, average 143.48, target 215.22
[14:55:43] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

