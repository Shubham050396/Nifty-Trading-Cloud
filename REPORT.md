# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:33 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.82 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | −₹208 (-0.92%) | +₹16,929 (+4.05%) | 4 | 1 | ₹22,640 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹35,220 (-4.22%) | −₹18,814 (-2.41%) | +₹37,086 (+0.67%) | 8 | 10 | ₹7,79,992 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹14,744 (+7.25%) | −₹53,058 (-5.02%) | 16 | 10 | ₹2,03,316 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹21,616 (-9.34%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹54,730** | **−₹25,894** | **+₹3,052** | **28** | **29** | **₹12,37,420** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:23:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:23:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:26:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:26:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:28:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:28:43] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:27:19] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:27:51] API       rate limited by Dhan - now one call every 15.1 s
[12:29:32] API       rate limited by Dhan - now one call every 15.1 s
[12:31:20] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:31:35] API       rate limited by Dhan - now one call every 15.1 s
[12:32:56] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:30:35] API       rate limited by Dhan - now one call every 15.1 s
[12:31:05] ENTRY     L3 BUY 2026-11-03 22800 PE @ 348.30  target 398.30  trail 313.47 (10%)
[12:31:19] API       rate limited by Dhan - now one call every 15.1 s
[12:32:18] API       rate limited by Dhan - now one call every 15.1 s
[12:32:48] API       rate limited by Dhan - now one call every 15.1 s
[12:33:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:30:52] SKIP      short 2026-11-23 24000 CE ignored - premium 62.05 is outside 144 - 1600
[12:30:52] SIGNAL    2026-11-23 22000 PE MACD crossed UP (bar close 166.95, hist -0.13 -> +0.23)
[12:30:52] SKIP      buy 2026-11-23 22000 PE ignored - open-position cap
[12:30:52] SIGNAL    2026-11-23 23000 PE MACD crossed UP (bar close 508.60, hist -0.66 -> +0.08)
[12:30:52] SKIP      buy 2026-11-23 23000 PE ignored - open-position cap
[12:31:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:20:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:23:12] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:25:39] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:27:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:29:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:31:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:30:24] SIGNAL    VEDL 260 PE 27 Oct crossed EMA 144 at 8.65 - not taken: under EMA 55
[12:30:24] SIGNAL    TCS 2060 PE 27 Oct crossed EMA 144 at 54.00 - not taken: under EMA 55, momentum 2.9%
[12:30:24] SIGNAL    PNB 116 PE 27 Oct crossed EMA 144 at 3.95 - not taken: under EMA 55, momentum 3.4%, premium under Rs 5
[12:30:24] SIGNAL    NAUKRI 1200 PE 27 Oct crossed EMA 144 at 24.00 - not taken: under EMA 55
[12:31:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:32:45] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:27:50] API       rate limited by Dhan - now one call every 15.1 s
[12:28:20] API       rate limited by Dhan - now one call every 15.1 s
[12:29:32] API       rate limited by Dhan - now one call every 15.1 s
[12:30:31] API       rate limited by Dhan - now one call every 15.1 s
[12:30:46] API       rate limited by Dhan - now one call every 15.1 s
[12:33:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

