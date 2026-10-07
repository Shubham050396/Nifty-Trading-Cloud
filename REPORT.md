# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:37 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.68 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹1,232 (-5.36%) | +₹20,280 (+5.68%) | 1 | 1 | ₹22,987 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹17,118 (-2.51%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,82,086 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | +₹1,400 (+0.96%) | −₹45,941 (-4.70%) | 12 | 7 | ₹1,46,099 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹19,956 (-9.06%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹9,044** | **−₹36,906** | **+₹48,740** | **13** | **22** | **₹10,71,504** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:28:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:28:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:32:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:32:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:35:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:35:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:33:37] API       rate limited by Dhan - now one call every 15.1 s
[10:34:38] API       rate limited by Dhan - now one call every 15.1 s
[10:34:54] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:34:59] API       rate limited by Dhan - now one call every 15.1 s
[10:36:20] API       rate limited by Dhan - now one call every 15.1 s
[10:37:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:36:22] GAP       2026-10-27 21500 CE: no prices for 6 min - bar history restarts
[10:36:22] GAP       2026-10-27 21500 PE: no prices for 6 min - bar history restarts
[10:36:22] GAP       2026-10-27 23700 CE: no prices for 6 min - bar history restarts
[10:36:22] GAP       2026-10-27 23700 PE: no prices for 6 min - bar history restarts
[10:36:50] API       rate limited by Dhan - now one call every 15.1 s
[10:37:05] EXIT      L3 2026-10-19 22500 CE TRAIL_STOP @ 305.55  P&L Rs -1267.50
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:34:47] API       rate limited by Dhan - now one call every 5.1 s
[10:34:52] API       rate limited by Dhan - now one call every 7.1 s
[10:35:29] API       rate limited by Dhan - now one call every 6.1 s
[10:35:42] API       rate limited by Dhan - now one call every 8.1 s
[10:36:24] API       rate limited by Dhan - now one call every 8.1 s
[10:37:21] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:28:02] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:29:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:31:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:33:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:35:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:37:16] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:35:18] SKIP      ICICIBANK 1360 CE 27 Oct signal at 22.15 skipped - already 1 open on ICICIBANK
[10:35:42] WARM      bar history loaded for all 780 contracts
[10:36:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:36:44] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:37:14] API       chart history: rate limited by Dhan - now one call every 1.2 s
[10:37:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:30:52] API       rate limited by Dhan - now one call every 15.1 s
[10:31:22] API       rate limited by Dhan - now one call every 15.1 s
[10:32:21] API       rate limited by Dhan - now one call every 15.1 s
[10:33:58] API       rate limited by Dhan - now one call every 15.1 s
[10:35:47] API       rate limited by Dhan - now one call every 15.1 s
[10:37:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

