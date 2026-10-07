# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:32 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹16,676 (-2.44%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,82,289 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹12,459 (+24.54%) | +₹3,966 (+2.66%) | −₹25,706 (-3.01%) | 3 | 10 | ₹1,49,361 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,522 (-8.17%) | ₹0 | 0 | 8 | ₹2,14,378 |
| **Total** | | **+₹12,459** | **−₹30,232** | **+₹70,243** | **3** | **24** | **₹10,46,028** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:26:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:27:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:28:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:29:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:30:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:31:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:27:53] API       rate limited by Dhan - now one call every 15.1 s
[09:28:33] API       rate limited by Dhan - now one call every 15.1 s
[09:29:14] API       rate limited by Dhan - now one call every 15.1 s
[09:29:55] API       rate limited by Dhan - now one call every 15.1 s
[09:30:35] API       rate limited by Dhan - now one call every 15.1 s
[09:31:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:28:26] API       rate limited by Dhan - now one call every 15.1 s
[09:29:25] API       rate limited by Dhan - now one call every 15.1 s
[09:30:23] API       rate limited by Dhan - now one call every 15.1 s
[09:30:53] API       rate limited by Dhan - now one call every 15.1 s
[09:31:23] API       rate limited by Dhan - now one call every 15.1 s
[09:31:54] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:30:25] API       rate limited by Dhan - now one call every 5.1 s
[09:30:43] API       rate limited by Dhan - now one call every 5.1 s
[09:31:01] API       rate limited by Dhan - now one call every 5.1 s
[09:31:19] API       rate limited by Dhan - now one call every 5.1 s
[09:31:38] API       rate limited by Dhan - now one call every 5.1 s
[09:31:56] API       rate limited by Dhan - now one call every 5.1 s
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
[09:28:59] WARM      bar history loaded for all 772 contracts
[09:30:01] SIGNAL    ABB 7200 PE 27 Oct crossed EMA 144 at 304.80 - not taken: under EMA 55
[09:30:01] SIGNAL    JSWENERGY 480 PE 27 Oct crossed EMA 144 at 7.90 - not taken: under EMA 55
[09:30:01] EXIT      SELL BRITANNIA 4800 PE 27 Oct EMA_STOP @ 73.30  -16.7%  P&L Rs -1831.25
[09:30:02] ENTRY     BUY RECLTD 310 CE 27 Oct x1575 @ 6.75 (signal close 6.70, EMA 144 6.30, momentum 61.4%)  quick 7.76 till 10:00, target 11.47, stop below EMA 55
[09:30:02] SKIP      RECLTD 300 CE 27 Oct signal at 12.05 skipped - 10 positions already open
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

