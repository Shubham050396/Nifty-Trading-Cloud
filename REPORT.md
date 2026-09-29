# NIFTY Cloud report

**Finished for the day at 22:55 IST** · updated 29 Sep 2026 22:55 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36604204667)

India VIX **13.41** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 22:50 → 22:55 IST (check run (outside trading hours))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **₹0** | **₹0** | **₹0** | **0** | **0** | **₹0** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-29 22:50:24] SCAN      scanner started automatically on launch
serving NIFTY Credit Spreads on http://127.0.0.1:50483
[2026-09-29 22:50:29] BOOT      scrip master downloaded: 4104 NIFTY contracts in 5.1s
[2026-09-29 22:50:29] BOOT      Ready - 18 expiries, 4104 NIFTY contracts
[2026-09-29 22:50:34] MARKET    heartbeat: after close; token expires in 23h 50m
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[22:50:24] BOOT      ema-hedge app up (pid 2306, DATA_DIR=/home/runner/work/Nifty-Trading-Cloud/Nifty-Trading-Cloud/strategies/ema_hedge/data)
serving NIFTY EMA Breakout Hedge on http://127.0.0.1:42995
[22:50:25] CONTROL   started automatically on launch
[22:50:25] CANDLES   loaded 825 NIFTY 5-minute candles. The script's position right now: FLAT
[22:50:29] BOOT      ready - 18 expiries listed, NIFTY lot 65
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
serving NIFTY 2-Level Cross on http://127.0.0.1:55045
[22:50:29] CONFIG    no expiry chosen - using 2026-09-29
[22:50:29] BOOT      ready - 18 expiries, 4104 contracts in the scrip master
[22:50:29] VIX       India VIX prev close 13.64 -> target 1000 ticks (Rs 50.00)
[22:50:30] CONTROL   started automatically on launch
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
serving NIFTY MACD - Monthly 1000s on http://127.0.0.1:59059
[22:50:29] CONFIG    no monthly expiry chosen - using 2026-10-27
[22:50:29] BOOT      ready - 14 monthly expiries, 4104 contracts in the scrip master
[22:50:29] VIX       India VIX prev close 13.64 - entries allowed
[22:50:30] CONTROL   started automatically on launch
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
serving NIFTY Scalper - IVX-G on http://127.0.0.1:47871
[2026-09-29 22:50:28] HALT      HALTED: session over (15:25)
[2026-09-29 22:50:28] RUN       scalper armed - started automatically on launch
[2026-09-29 22:50:28] BOOT      scrip master: 4104 NIFTY contracts
[2026-09-29 22:50:29] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[22:50:29] BOOT      scrip master downloaded in 5s: 210 stocks with options
[22:50:29] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[22:50:29] CONTROL   started automatically on launch - 99 stocks
[22:50:29] API       market quote: rate limited by Dhan - now one call every 2.0 s
[22:50:29] API       share prices unavailable: HTTP 429
cloud: shutdown requested - saving state
```
</details>

