# NIFTY Cloud report

**Finished for the day at 08:33 IST** · updated 06 Oct 2026 08:33 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **14.78 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 08:27 → 08:32 IST (check run (before the market opens))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | ₹0 | −₹6,487 (-0.52%) | +₹52,439 (+1.28%) | 0 | 10 | ₹12,58,429 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | ₹0 | −₹6,454 (-5.53%) | −₹27,375 (-3.83%) | 0 | 6 | ₹1,16,599 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | ✅ saved | ₹0 | −₹6,902 (-4.50%) | ₹0 | 0 | 8 | ₹1,53,295 |
| **Total** | | **₹0** | **−₹19,843** | **+₹48,707** | **0** | **24** | **₹15,28,323** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 08:28:04] BOOT      scrip master downloaded: 4120 NIFTY contracts in 5.2s
[2026-10-06 08:28:04] VIX       India VIX 14.78 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-06 08:28:04] BOOT      Ready - 18 expiries, 4120 NIFTY contracts
127.0.0.1 - - [06/Oct/2026 02:58:08] "GET /api/status HTTP/1.1" 200 -
[2026-10-06 08:28:09] MARKET    heartbeat: pre-open, session starts 09:15 IST; token expires in 13h 1m
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[08:27:59] DAY       new session 2026-10-06
[08:28:00] VIX       India VIX 14.78 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[08:28:00] CANDLES   NIFTY candles unavailable: Too many requests on server from single user breaching rate limits. Try throttling API calls. - retrying
[08:28:04] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [06/Oct/2026 02:58:08] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[08:28:00] CONTROL   started automatically on launch
[08:28:00] DAY       new session 2026-10-06 - counters reset
[08:28:04] BOOT      ready - 18 expiries, 4120 contracts in the scrip master
[08:28:04] VIX       India VIX prev close 14.78 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [06/Oct/2026 02:58:08] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[08:28:00] CONTROL   started automatically on launch
[08:28:00] DAY       new session 2026-10-06 - counters reset
[08:28:04] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[08:28:04] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.) - no new entries until it loads - entries blocked (above 15)
127.0.0.1 - - [06/Oct/2026 02:58:08] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-06 08:28:02] RUN       scalper armed - started automatically on launch
[2026-10-06 08:28:04] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-06 08:28:04] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [06/Oct/2026 02:58:08] "GET /api/state HTTP/1.1" 200 -
[2026-10-06 08:30:01] HALT      HALTED: session over (15:25)
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[08:28:05] API       share prices unavailable: HTTP 429
[08:28:05] API       chart history: rate limited by Dhan - now one call every 1.2 s
127.0.0.1 - - [06/Oct/2026 02:58:08] "GET /api/state HTTP/1.1" 200 -
[08:28:36] WARM      bar history loaded for all 6 contracts
[08:30:00] CONTRACT  watching 596 contracts on 99 stocks (ATM +/- 1, CE/PE): 590 added, 0 dropped
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[08:28:00] DAY       new session 2026-10-06 - counters reset
[08:28:04] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[08:28:04] VIX       India VIX prev close 14.78
[08:28:05] HISTORY   2026-10-27 26000 CE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the VIX Fix needs 25 of them. Retried every 10 min.
127.0.0.1 - - [06/Oct/2026 02:58:08] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

