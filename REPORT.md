# NIFTY Cloud report

**Running until 15:15 IST** · updated 06 Oct 2026 14:40 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **13.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹19,867 (+3.47%) | −₹38,743 (-5.66%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,83,919 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹8,370 (-28.31%) | −₹756 (-0.87%) | −₹35,745 (-4.81%) | 1 | 5 | ₹87,034 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,261 (-11.91%) | ₹0 | 0 | 8 | ₹1,53,295 |
| **Total** | | **+₹11,497** | **−₹57,760** | **+₹60,204** | **5** | **19** | **₹9,24,248** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 14:36:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:36:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-06 14:37:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:38:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:40:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-06 14:40:23] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:36:22] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:36:41] API       rate limited by Dhan - now one call every 10.1 s
[14:37:01] API       rate limited by Dhan - now one call every 15.1 s
[14:38:22] API       rate limited by Dhan - now one call every 15.1 s
[14:39:43] API       rate limited by Dhan - now one call every 15.1 s
[14:40:24] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:38:10] API       rate limited by Dhan - now one call every 15.1 s
[14:38:26] API       rate limited by Dhan - now one call every 15.1 s
[14:39:24] API       rate limited by Dhan - now one call every 15.1 s
[14:39:39] API       rate limited by Dhan - now one call every 15.1 s
[14:39:55] API       rate limited by Dhan - now one call every 15.1 s
[14:40:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:35:55] API       rate limited by Dhan - now one call every 6.1 s
[14:36:42] API       rate limited by Dhan - now one call every 5.1 s
[14:36:47] API       rate limited by Dhan - now one call every 7.1 s
[14:36:54] API       rate limited by Dhan - now one call every 11.1 s
[14:37:16] API       rate limited by Dhan - now one call every 15.1 s
[14:38:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 14:35:21] RUN       scalper armed - started automatically on launch
[2026-10-06 14:35:22] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-06 14:35:23] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/state HTTP/1.1" 200 -
[2026-10-06 14:36:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 14:38:44] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:39:34] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:39:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:39:52] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:40:02] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:40:11] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:40:20] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:35:36] API       rate limited by Dhan - now one call every 9.1 s
[14:36:11] API       rate limited by Dhan - now one call every 12.1 s
[14:36:23] API       rate limited by Dhan - now one call every 15.1 s
[14:37:07] API       rate limited by Dhan - now one call every 15.1 s
[14:39:07] API       rate limited by Dhan - now one call every 15.1 s
[14:40:05] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

