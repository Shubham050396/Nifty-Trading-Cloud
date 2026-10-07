# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 09:16 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.61 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹25,389 (-3.72%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,81,798 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹14,290 (+35.93%) | −₹2,460 (-2.96%) | −₹23,875 (-2.83%) | 2 | 5 | ₹83,154 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,509 (-10.61%) | ₹0 | 0 | 8 | ₹1,55,606 |
| **Total** | | **+₹14,290** | **−₹44,358** | **+₹72,074** | **2** | **19** | **₹9,20,558** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 09:01:46] VIX       India VIX 13.61 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-07 09:01:46] BOOT      Ready - 18 expiries, 4056 NIFTY contracts
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/status HTTP/1.1" 200 -
[2026-10-07 09:01:51] MARKET    heartbeat: pre-open, session starts 09:15 IST; token expires in 12h 49m
[2026-10-07 09:16:01] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 09:16:01] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:01:46] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
[09:15:00] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:15:00] API       rate limited by Dhan - now one call every 5.1 s
[09:15:41] API       rate limited by Dhan - now one call every 6.1 s
[09:16:21] API       rate limited by Dhan - now one call every 8.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:15:11] API       rate limited by Dhan - now one call every 6.1 s
[09:15:18] CONTRACT  2026-11-03: watching ATM 22600 +/- 10 strikes (CE/PE)
[09:15:23] API       rate limited by Dhan - now one call every 8.1 s
[09:15:40] API       rate limited by Dhan - now one call every 12.1 s
[09:16:04] API       rate limited by Dhan - now one call every 15.1 s
[09:16:34] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:15:19] API       rate limited by Dhan - now one call every 5.1 s
[09:15:37] API       rate limited by Dhan - now one call every 5.1 s
[09:15:56] API       rate limited by Dhan - now one call every 5.1 s
[09:16:14] API       rate limited by Dhan - now one call every 5.1 s
[09:16:32] API       rate limited by Dhan - now one call every 5.1 s
[09:16:51] API       rate limited by Dhan - now one call every 5.1 s
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
[09:12:59] WARM      bar history loaded for all 674 contracts
[09:15:01] API       market quote: rate limited by Dhan - now one call every 2.0 s
[09:15:01] EXIT      SELL HDFCBANK 720 PE 27 Oct EMA_STOP @ 19.75  +4.2%  P&L Rs 520.00
[09:15:04] CONTRACT  watching 700 contracts on 99 stocks (ATM +/- 1, CE/PE): 32 added, 6 dropped
[09:16:44] EXIT      SELL ADANIGREEN 1300 CE 27 Oct PROFIT_TARGET @ 68.70  +50.2%  P&L Rs 13770.00
[09:16:49] WARM      bar history loaded for all 756 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:01:42] DAY       new session 2026-10-07 - counters reset
[09:01:46] BOOT      ready - 14 monthly expiries, 4056 contracts in the scrip master
[09:01:46] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.)
[09:01:46] HISTORY   2026-10-27 25000 CE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the VIX Fix needs 25 of them. Retried every 10 min.
127.0.0.1 - - [07/Oct/2026 03:31:50] "GET /api/state HTTP/1.1" 200 -
[09:15:01] CONTRACT  2026-10-27: watching ATM 23000 +/- 3 strikes of 1000 (CE/PE)
```
</details>

