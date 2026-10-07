# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:11 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.61 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹41,652 (-6.08%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,85,266 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹6,980 (+5.68%) | −₹38,165 (-4.76%) | 0 | 7 | ₹1,22,921 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹19,087 (-12.27%) | ₹0 | 0 | 8 | ₹1,55,606 |
| **Total** | | **₹0** | **−₹53,759** | **+₹57,784** | **0** | **21** | **₹9,63,793** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
serving NIFTY Credit Spreads on http://127.0.0.1:41829
[2026-10-07 09:01:46] BOOT      scrip master downloaded: 4056 NIFTY contracts in 5.2s
[2026-10-07 09:01:46] VIX       India VIX 13.61 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-07 09:01:46] BOOT      Ready - 18 expiries, 4056 NIFTY contracts
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/status HTTP/1.1" 200 -
[2026-10-07 09:01:51] MARKET    heartbeat: pre-open, session starts 09:15 IST; token expires in 12h 49m
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:01:41] CONTROL   started automatically on launch
[09:01:41] DAY       new session 2026-10-07
[09:01:42] VIX       India VIX 13.61 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[09:01:42] CANDLES   NIFTY candles unavailable: Too many requests on server from single user breaching rate limits. Try throttling API calls. - retrying
[09:01:46] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:01:43] CONFIG    removed expired expiry 2026-10-06 - now using 2026-11-03 instead
[09:01:46] BOOT      ready - 18 expiries, 4056 contracts in the scrip master
[09:01:46] VIX       India VIX prev close 13.61 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
127.0.0.1 - - [07/Oct/2026 03:31:50] "[31m[1mPOST /api/config HTTP/1.1[0m" 400 -
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:01:42] HISTORY   2026-10-27 23000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[09:01:42] CONTROL   started automatically on launch
[09:01:42] DAY       new session 2026-10-07 - counters reset
[09:01:45] BOOT      ready - 14 monthly expiries, 4056 contracts in the scrip master
[09:01:46] VIX       India VIX prev close 13.61 - entries allowed
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
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
[09:01:46] API       market quote: rate limited by Dhan - now one call every 2.0 s
[09:01:46] API       share prices unavailable: HTTP 429
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
[09:02:13] WARM      bar history loaded for all 7 contracts
[09:02:16] CONTRACT  watching 594 contracts on 99 stocks (ATM +/- 1, CE/PE): 587 added, 0 dropped
[09:08:50] CONTRACT  watching 674 contracts on 99 stocks (ATM +/- 1, CE/PE): 84 added, 4 dropped
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:01:42] CONTROL   started automatically on launch
[09:01:42] DAY       new session 2026-10-07 - counters reset
[09:01:46] BOOT      ready - 14 monthly expiries, 4056 contracts in the scrip master
[09:01:46] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.)
[09:01:46] HISTORY   2026-10-27 25000 CE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the VIX Fix needs 25 of them. Retried every 10 min.
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
```
</details>

