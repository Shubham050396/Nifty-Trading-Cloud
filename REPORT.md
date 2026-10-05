# NIFTY Cloud report

**Finished for the day at 16:23 IST** · updated 05 Oct 2026 16:23 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37298895549)

India VIX **14.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 16:18 → 16:23 IST (check run (after the trading day))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | +₹1,128 (+0.99%) | ₹0 | +₹21,548 (+6.41%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | +₹16,000 (+0.81%) | −₹6,487 (-0.52%) | +₹52,439 (+1.28%) | 23 | 10 | ₹12,58,429 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | +₹403 (+1.97%) | ₹0 | +₹464 (+1.59%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | −₹27,286 (-7.52%) | −₹6,454 (-5.53%) | −₹27,375 (-3.83%) | 19 | 6 | ₹1,16,599 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | ✅ saved | ₹0 | −₹6,902 (-4.50%) | ₹0 | 0 | 8 | ₹1,53,295 |
| **Total** | | **−₹9,755** | **−₹19,843** | **+₹48,707** | **49** | **24** | **₹15,28,323** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 16:18:34] VIX       India VIX 14.78 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-05 16:18:35] BOOT      scrip master downloaded: 4120 NIFTY contracts in 5.9s
[2026-10-05 16:18:35] BOOT      Ready - 18 expiries, 4120 NIFTY contracts
127.0.0.1 - - [05/Oct/2026 10:48:38] "GET /api/status HTTP/1.1" 200 -
[2026-10-05 16:18:39] MARKET    heartbeat: after close; token expires in 7h 29m
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[16:18:30] CONTROL   started automatically on launch
[16:18:30] VIX       India VIX 14.78 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[16:18:30] CANDLES   NIFTY candles unavailable: Too many requests on server from single user breaching rate limits. Try throttling API calls. - retrying
[16:18:35] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [05/Oct/2026 10:48:38] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
serving NIFTY 2-Level Cross on http://127.0.0.1:49711
[16:18:31] CONTROL   started automatically on launch
[16:18:35] BOOT      ready - 18 expiries, 4120 contracts in the scrip master
[16:18:35] VIX       India VIX prev close 14.46 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [05/Oct/2026 10:48:38] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[16:18:30] HISTORY   2026-10-27 23000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[16:18:31] CONTROL   started automatically on launch
[16:18:35] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[16:18:35] VIX       India VIX prev close 14.46 - entries allowed
127.0.0.1 - - [05/Oct/2026 10:48:38] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 16:18:33] RUN       scalper armed - started automatically on launch
[2026-10-05 16:18:34] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-05 16:18:35] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [05/Oct/2026 10:48:38] "GET /api/state HTTP/1.1" 200 -
[2026-10-05 16:22:26] DATA      buffer gap > 15s - cleared, re-warming
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[16:18:35] BOOT      scrip master downloaded in 6s: 213 stocks with options
[16:18:35] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[16:18:35] CONTROL   started automatically on launch - 99 stocks
[16:18:36] CONTRACT  watching 596 contracts on 99 stocks (ATM +/- 1, CE/PE): 590 added, 0 dropped
127.0.0.1 - - [05/Oct/2026 10:48:38] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[16:18:31] CONTROL   started automatically on launch
[16:18:35] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[16:18:35] HISTORY   2026-10-27 25000 CE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the VIX Fix needs 25 of them. Retried every 10 min.
[16:18:35] VIX       India VIX prev close 14.46
127.0.0.1 - - [05/Oct/2026 10:48:38] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

