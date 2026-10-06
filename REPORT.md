# NIFTY Cloud report

**Finished for the day at 16:18 IST** · updated 06 Oct 2026 16:18 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37451687112)

India VIX **13.61 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 16:13 → 16:18 IST (check run (after the trading day))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | +₹19,867 (+3.47%) | −₹41,652 (-6.08%) | +₹72,306 (+1.54%) | 4 | 6 | ₹6,85,266 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | −₹10,790 (-12.22%) | +₹6,980 (+5.68%) | −₹38,165 (-4.76%) | 4 | 7 | ₹1,22,921 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | ✅ saved | ₹0 | −₹19,087 (-12.27%) | ₹0 | 0 | 8 | ₹1,55,606 |
| **Total** | | **+₹9,077** | **−₹53,759** | **+₹57,784** | **8** | **21** | **₹9,63,793** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 16:13:56] VIX       India VIX 13.61 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-06 16:13:56] BOOT      scrip master downloaded: 4120 NIFTY contracts in 5.7s
[2026-10-06 16:13:56] BOOT      Ready - 18 expiries, 4120 NIFTY contracts
127.0.0.1 - - [06/Oct/2026 10:44:00] "GET /api/status HTTP/1.1" 200 -
[2026-10-06 16:14:01] MARKET    heartbeat: after close; token expires in 5h 15m
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[16:13:52] CONTROL   started automatically on launch
[16:13:52] VIX       India VIX 13.61 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[16:13:52] CANDLES   NIFTY candles unavailable: Too many requests on server from single user breaching rate limits. Try throttling API calls. - retrying
[16:13:57] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [06/Oct/2026 10:44:00] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
serving NIFTY 2-Level Cross on http://127.0.0.1:58801
[16:13:53] CONTROL   started automatically on launch
[16:13:56] BOOT      ready - 18 expiries, 4120 contracts in the scrip master
[16:13:56] VIX       India VIX prev close 14.78 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [06/Oct/2026 10:44:00] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[16:13:52] HISTORY   2026-10-27 23000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[16:13:53] CONTROL   started automatically on launch
[16:13:56] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[16:13:57] VIX       India VIX prev close 14.78 - entries allowed
127.0.0.1 - - [06/Oct/2026 10:44:00] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 16:13:56] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-06 16:13:56] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [06/Oct/2026 10:44:00] "GET /api/state HTTP/1.1" 200 -
[2026-10-06 16:16:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-06 16:18:03] DATA      buffer gap > 15s - cleared, re-warming
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[16:13:57] API       chart history: rate limited by Dhan - now one call every 1.2 s
[16:13:57] API       market quote: rate limited by Dhan - now one call every 2.0 s
[16:13:57] API       share prices unavailable: HTTP 429
127.0.0.1 - - [06/Oct/2026 10:44:00] "GET /api/state HTTP/1.1" 200 -
[16:14:28] WARM      bar history loaded for all 7 contracts
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
serving NIFTY VIX Fix - Monthly 1000s on http://127.0.0.1:49861
[16:13:53] CONTROL   started automatically on launch
[16:13:56] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[16:13:57] VIX       India VIX prev close 14.78
127.0.0.1 - - [06/Oct/2026 10:44:00] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

