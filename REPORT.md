# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:26 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹12,922 (-1.90%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,731 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹14,290 (+35.93%) | +₹1,981 (+1.32%) | −₹23,875 (-2.83%) | 2 | 10 | ₹1,49,724 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,977 (-8.39%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹14,290** | **−₹28,918** | **+₹72,074** | **2** | **24** | **₹10,45,833** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:21:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 09:22:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:23:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:24:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:25:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:26:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:22:28] API       rate limited by Dhan - now one call every 15.1 s
[09:23:49] API       rate limited by Dhan - now one call every 15.1 s
[09:25:07] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:25:11] API       rate limited by Dhan - now one call every 15.1 s
[09:25:51] API       rate limited by Dhan - now one call every 15.1 s
[09:26:32] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:24:32] GAP       2026-10-27 23700 CE: no prices for 1090 min - bar history restarts
[09:24:32] GAP       2026-10-27 23700 PE: no prices for 1090 min - bar history restarts
[09:24:58] API       rate limited by Dhan - now one call every 15.1 s
[09:25:28] API       rate limited by Dhan - now one call every 15.1 s
[09:26:13] API       rate limited by Dhan - now one call every 15.1 s
[09:26:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:25:14] API       rate limited by Dhan - now one call every 5.1 s
[09:25:32] API       rate limited by Dhan - now one call every 5.1 s
[09:25:50] API       rate limited by Dhan - now one call every 5.1 s
[09:26:08] API       rate limited by Dhan - now one call every 5.1 s
[09:26:27] API       rate limited by Dhan - now one call every 5.1 s
[09:26:45] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 09:01:44] DAY       new session 2026-10-07 - counters reset (kill switch is NOT cleared)
[2026-10-07 09:01:44] DATA      buffer cleared: day roll
[2026-10-07 09:01:44] RUN       scalper armed - started automatically on launch
[2026-10-07 09:01:45] BOOT      scrip master: 4056 NIFTY contracts
[2026-10-07 09:01:45] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:25:03] SIGNAL    HINDUNILVR 1880 PE 27 Oct crossed EMA 144 at 36.20 - not taken: under EMA 55
[09:25:03] SIGNAL    TATACONSUM 980 PE 27 Oct crossed EMA 144 at 25.30 - not taken: under EMA 55
[09:25:03] SIGNAL    WIPRO 162.5 PE 27 Oct crossed EMA 144 at 5.50 - not taken: under EMA 55, momentum 1.3%
[09:25:03] SIGNAL    ABB 7000 PE 27 Oct crossed EMA 144 at 193.00 - not taken: under EMA 55
[09:25:04] SKIP      DLF 660 PE 27 Oct signal at 16.95 skipped - 10 positions already open
[09:25:41] WARM      bar history loaded for all 772 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:20:01] SIGNAL    2026-10-27 23000 CE VIX Fix crossed above 10.00 (5.93 -> 11.98, bar close 141.80)
[09:20:01] ENTRY     BUY 2026-10-27 23000 CE @ 141.40 x 65  (Rs 9,191) - buy 3 of 10, average 146.57, target 219.85
[09:24:32] API       rate limited by Dhan - now one call every 5.1 s
[09:24:42] API       rate limited by Dhan - now one call every 6.1 s
[09:25:04] SIGNAL    2026-10-27 22000 CE VIX Fix crossed above 10.00 (7.21 -> 11.44, bar close 749.00)
[09:25:04] ENTRY     BUY 2026-10-27 22000 CE @ 750.55 x 65  (Rs 48,786) - buy 2 of 10, average 752.20, target 1128.30
```
</details>

