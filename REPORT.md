# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:23 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.77 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹2,454 (-3.68%) | −₹1,625 (-10.67%) | +₹19,094 (+4.74%) | 3 | 1 | ₹15,230 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹11,086 (-1.43%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,75,891 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹14,834 (+7.30%) | −₹53,058 (-5.02%) | 16 | 10 | ₹2,03,316 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹19,218 (-8.30%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹50,580** | **−₹17,095** | **+₹7,203** | **25** | **29** | **₹12,25,909** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:14:40] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:14:40] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:19:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:19:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:21:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:21:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:18:42] API       rate limited by Dhan - now one call every 15.1 s
[12:19:22] API       rate limited by Dhan - now one call every 15.1 s
[12:20:44] API       rate limited by Dhan - now one call every 15.1 s
[12:22:05] API       rate limited by Dhan - now one call every 15.1 s
[12:22:16] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:22:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:20:40] API       rate limited by Dhan - now one call every 15.1 s
[12:21:10] API       rate limited by Dhan - now one call every 15.1 s
[12:21:40] API       rate limited by Dhan - now one call every 15.1 s
[12:21:55] API       rate limited by Dhan - now one call every 15.1 s
[12:22:11] API       rate limited by Dhan - now one call every 15.1 s
[12:22:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:13:54] API       rate limited by Dhan - now one call every 15.1 s
[12:15:31] API       rate limited by Dhan - now one call every 15.1 s
[12:16:42] API       rate limited by Dhan - now one call every 15.1 s
[12:19:14] API       rate limited by Dhan - now one call every 15.1 s
[12:20:38] API       rate limited by Dhan - now one call every 15.1 s
[12:21:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:13:47] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:15:40] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:17:22] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:19:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:20:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:23:12] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:20:19] SKIP      ADANIPORTS 1760 PE 27 Oct signal at 32.55 skipped - 10 positions already open
[12:20:28] WARM      bar history loaded for all 786 contracts
[12:20:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:21:01] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:21:46] WARM      bar history loaded for all 786 contracts
[12:22:42] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:19:31] API       rate limited by Dhan - now one call every 12.1 s
[12:20:07] SIGNAL    2026-10-27 23000 CE VIX Fix crossed above 10.00 (8.99 -> 10.90, bar close 148.75)
[12:20:07] ENTRY     BUY 2026-10-27 23000 CE @ 149.45 x 65  (Rs 9,714) - buy 4 of 10, average 147.29, target 220.94
[12:20:18] API       rate limited by Dhan - now one call every 15.1 s
[12:20:33] API       rate limited by Dhan - now one call every 15.1 s
[12:23:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

