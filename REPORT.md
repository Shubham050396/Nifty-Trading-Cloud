# NIFTY Cloud report

**Finished for the day at 22:45 IST** · updated 02 Oct 2026 22:45 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37038877640)

India VIX **14.46 🔴 above the limit** (limit 13.50) · Dhan token: valid until 03 Oct 22:38 IST · trading window: 22:40 → 22:45 IST (check run (after the trading day))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | ₹0 | ₹0 | +₹20,420 (+9.20%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | ₹0 | +₹16,208 (+2.82%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,74,142 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | ₹0 | −₹4,138 (-4.41%) | −₹89 (-0.03%) | 0 | 5 | ₹93,802 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **₹0** | **+₹12,070** | **+₹58,463** | **0** | **10** | **₹6,67,944** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-02 22:40:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-02 22:40:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
127.0.0.1 - - [02/Oct/2026 17:10:45] "GET /api/status HTTP/1.1" 200 -
[2026-10-02 22:40:47] MARKET    heartbeat: after close; token expires in 23h 57m
[2026-10-02 22:41:42] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
serving NIFTY EMA Breakout Hedge on http://127.0.0.1:38267
[22:40:37] CONTROL   started automatically on launch
[22:40:37] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[22:40:41] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [02/Oct/2026 17:10:45] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
serving NIFTY 2-Level Cross on http://127.0.0.1:34795
[22:40:38] CONTROL   started automatically on launch
[22:40:41] BOOT      ready - 18 expiries, 4120 contracts in the scrip master
[22:40:41] VIX       India VIX prev close 14.46 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [02/Oct/2026 17:10:45] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
serving NIFTY MACD - Monthly 1000s on http://127.0.0.1:59095
[22:40:38] CONTROL   started automatically on launch
[22:40:41] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[22:40:41] VIX       India VIX prev close 14.46 - entries allowed
127.0.0.1 - - [02/Oct/2026 17:10:45] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
serving NIFTY Scalper - IVX-G on http://127.0.0.1:50345
[2026-10-02 22:40:40] RUN       scalper armed - started automatically on launch
[2026-10-02 22:40:41] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-02 22:40:41] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [02/Oct/2026 17:10:45] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[22:40:41] BOOT      scrip master downloaded in 5s: 213 stocks with options
[22:40:41] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[22:40:41] CONTROL   started automatically on launch - 99 stocks
[22:40:41] CONTRACT  watching 1386 contracts on 99 stocks (ATM +/- 3, CE/PE): 1381 added, 0 dropped
127.0.0.1 - - [02/Oct/2026 17:10:45] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
serving NIFTY VIX Fix - Monthly 1000s on http://127.0.0.1:49349
[22:40:38] CONTROL   started automatically on launch
[22:40:41] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[22:40:41] VIX       India VIX prev close 14.46
127.0.0.1 - - [02/Oct/2026 17:10:45] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

