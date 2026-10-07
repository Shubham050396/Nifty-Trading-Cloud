# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:21 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **14.10 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹12,223 (-1.79%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,917 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹14,290 (+35.93%) | +₹769 (+0.51%) | −₹23,875 (-2.83%) | 2 | 10 | ₹1,49,724 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹17,519 (-10.58%) | ₹0 | 0 | 8 | ₹1,65,592 |
| **Total** | | **+₹14,290** | **−₹28,973** | **+₹72,074** | **2** | **24** | **₹9,97,233** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:16:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 09:17:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:18:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:19:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:21:02] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:21:02] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:19:44] API       rate limited by Dhan - now one call every 15.1 s
[09:20:03] SIGNAL    EXIT LONG at 2026-10-07 09:15: NIFTY closed 22622.70 - closed through the stop EMA
[09:20:26] API       rate limited by Dhan - now one call every 15.1 s
[09:21:04] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:21:07] API       rate limited by Dhan - now one call every 15.1 s
[09:21:47] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:19:05] API       rate limited by Dhan - now one call every 15.1 s
[09:19:35] API       rate limited by Dhan - now one call every 15.1 s
[09:20:05] API       rate limited by Dhan - now one call every 15.1 s
[09:20:35] API       rate limited by Dhan - now one call every 15.1 s
[09:21:05] CONTRACT  2026-10-13: watching ATM 22600 +/- 10 strikes (CE/PE)
[09:21:33] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:20:26] API       rate limited by Dhan - now one call every 5.1 s
[09:20:44] API       rate limited by Dhan - now one call every 5.1 s
[09:21:02] API       rate limited by Dhan - now one call every 5.1 s
[09:21:20] API       rate limited by Dhan - now one call every 5.1 s
[09:21:39] API       rate limited by Dhan - now one call every 5.1 s
[09:21:57] API       rate limited by Dhan - now one call every 5.1 s
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
[09:20:04] SKIP      ASIANPAINT 2360 PE 27 Oct signal at 37.35 skipped - 10 positions already open
[09:20:04] SKIP      TMPV 290 PE 27 Oct signal at 11.55 skipped - 10 positions already open
[09:20:04] SKIP      ASIANPAINT 2400 PE 27 Oct signal at 55.15 skipped - 10 positions already open
[09:20:04] SKIP      HDFCBANK 700 PE 27 Oct signal at 11.75 skipped - 10 positions already open
[09:20:10] WARM      bar history loaded for all 766 contracts
[09:20:16] WARM      bar history loaded for all 766 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:15:01] CONTRACT  2026-10-27: watching ATM 23000 +/- 3 strikes of 1000 (CE/PE)
[09:17:46] API       rate limited by Dhan - now one call every 5.1 s
[09:20:01] SIGNAL    2026-10-27 24000 CE VIX Fix crossed above 10.00 (7.70 -> 11.42, bar close 12.25)
[09:20:01] ENTRY     BUY 2026-10-27 24000 CE @ 12.20 x 65  (Rs 793) - buy 3 of 10, average 14.12, target 21.18
[09:20:01] SIGNAL    2026-10-27 23000 CE VIX Fix crossed above 10.00 (5.93 -> 11.98, bar close 141.80)
[09:20:01] ENTRY     BUY 2026-10-27 23000 CE @ 141.40 x 65  (Rs 9,191) - buy 3 of 10, average 146.57, target 219.85
```
</details>

