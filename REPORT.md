# NIFTY Cloud report

**Finished for the day at 16:07 IST** · updated 07 Oct 2026 16:07 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37608034359)

India VIX **13.89 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 16:02 → 16:07 IST (check run (after the trading day))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | +₹1,882 (+1.48%) | ₹0 | +₹23,429 (+5.06%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | −₹43,192 (-1.74%) | −₹10,042 (-1.09%) | +₹29,114 (+0.41%) | 26 | 10 | ₹9,20,478 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | −₹13,420 (-4.18%) | +₹19,588 (+12.94%) | −₹51,585 (-4.59%) | 19 | 8 | ₹1,51,408 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | ✅ saved | ₹0 | −₹25,665 (-10.21%) | ₹0 | 0 | 8 | ₹2,51,267 |
| **Total** | | **−₹54,730** | **−₹16,119** | **+₹3,053** | **51** | **26** | **₹13,23,153** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 16:02:29] VIX       India VIX 13.89 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-07 16:02:29] BOOT      scrip master downloaded: 4056 NIFTY contracts in 5.5s
[2026-10-07 16:02:29] BOOT      Ready - 18 expiries, 4056 NIFTY contracts
127.0.0.1 - - [07/Oct/2026 10:32:33] "GET /api/status HTTP/1.1" 200 -
[2026-10-07 16:02:34] MARKET    heartbeat: after close; token expires in 5h 48m
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
serving NIFTY EMA Breakout Hedge on http://127.0.0.1:50107
[16:02:25] CONTROL   started automatically on launch
[16:02:25] VIX       India VIX 13.89 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[16:02:29] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [07/Oct/2026 10:32:33] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[16:02:29] BOOT      ready - 18 expiries, 4056 contracts in the scrip master
[16:02:30] VIX       India VIX prev close 13.61 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [07/Oct/2026 10:32:33] "GET /api/state HTTP/1.1" 200 -
127.0.0.1 - - [07/Oct/2026 10:32:33] "[31m[1mPOST /api/config HTTP/1.1[0m" 400 -
127.0.0.1 - - [07/Oct/2026 10:32:33] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[16:02:25] HISTORY   2026-10-27 23000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[16:02:26] CONTROL   started automatically on launch
[16:02:30] BOOT      ready - 14 monthly expiries, 4056 contracts in the scrip master
[16:02:30] VIX       India VIX prev close 13.61 - entries allowed
127.0.0.1 - - [07/Oct/2026 10:32:33] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
serving NIFTY Scalper - IVX-G on http://127.0.0.1:55685
[2026-10-07 16:02:28] RUN       scalper armed - started automatically on launch
[2026-10-07 16:02:29] BOOT      scrip master: 4056 NIFTY contracts
[2026-10-07 16:02:30] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [07/Oct/2026 10:32:33] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[16:02:30] CONTROL   started automatically on launch - 99 stocks
[16:02:30] API       market quote: rate limited by Dhan - now one call every 2.0 s
[16:02:30] API       share prices unavailable: HTTP 429
127.0.0.1 - - [07/Oct/2026 10:32:33] "GET /api/state HTTP/1.1" 200 -
[16:02:33] WARM      bar history loaded for all 8 contracts
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
serving NIFTY VIX Fix - Monthly 1000s on http://127.0.0.1:48303
[16:02:26] CONTROL   started automatically on launch
[16:02:29] BOOT      ready - 14 monthly expiries, 4056 contracts in the scrip master
[16:02:30] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.)
127.0.0.1 - - [07/Oct/2026 10:32:33] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

