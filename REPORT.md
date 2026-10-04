# NIFTY Cloud report

**Running until 23:53 IST** · updated 04 Oct 2026 23:49 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37223944793)

India VIX **14.46 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 23:48 → 23:53 IST (check run (weekend))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹20,420 (+9.20%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹16,208 (+2.82%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,74,142 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | −₹4,138 (-4.41%) | −₹89 (-0.03%) | 0 | 5 | ₹93,802 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **₹0** | **+₹12,070** | **+₹58,463** | **0** | **10** | **₹6,67,944** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
serving NIFTY Credit Spreads on http://127.0.0.1:43819
[2026-10-04 23:48:56] SCAN      scanner started automatically on launch
[2026-10-04 23:49:01] BOOT      scrip master downloaded: 4120 NIFTY contracts in 5.3s
[2026-10-04 23:49:01] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-04 23:49:01] BOOT      Ready - 18 expiries, 4120 NIFTY contracts
127.0.0.1 - - [04/Oct/2026 18:19:05] "GET /api/status HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[23:48:56] BOOT      ema-hedge app up (pid 2358, DATA_DIR=/home/runner/work/Nifty-Trading-Cloud/Nifty-Trading-Cloud/strategies/ema_hedge/data)
serving NIFTY EMA Breakout Hedge on http://127.0.0.1:45975
[23:48:57] CONTROL   started automatically on launch
[23:48:57] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[23:49:01] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [04/Oct/2026 18:19:05] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[23:48:56] BOOT      level-cross app up (pid 2359, DATA_DIR=/home/runner/work/Nifty-Trading-Cloud/Nifty-Trading-Cloud/strategies/level_cross/data)
serving NIFTY 2-Level Cross on http://127.0.0.1:58891
[23:48:58] CONTROL   started automatically on launch
[23:49:01] BOOT      ready - 18 expiries, 4120 contracts in the scrip master
[23:49:01] VIX       India VIX prev close 14.46 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [04/Oct/2026 18:19:05] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
serving NIFTY MACD - Monthly 1000s on http://127.0.0.1:52737
[23:48:56] HISTORY   2026-10-27 21000 CE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[23:48:58] CONTROL   started automatically on launch
[23:49:01] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[23:49:01] VIX       India VIX prev close 14.46 - entries allowed
127.0.0.1 - - [04/Oct/2026 18:19:05] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-04 23:48:56] BOOT      scalper up (pid 2361, DATA_DIR=/home/runner/work/Nifty-Trading-Cloud/Nifty-Trading-Cloud/strategies/scalper/data, auth=off)
serving NIFTY Scalper - IVX-G on http://127.0.0.1:37605
[2026-10-04 23:49:00] RUN       scalper armed - started automatically on launch
[2026-10-04 23:49:01] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-04 23:49:01] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [04/Oct/2026 18:19:05] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[23:49:01] BOOT      scrip master downloaded in 6s: 213 stocks with options
[23:49:01] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[23:49:02] CONTROL   started automatically on launch - 99 stocks
[23:49:02] API       market quote: rate limited by Dhan - now one call every 2.0 s
[23:49:02] API       share prices unavailable: HTTP 429
127.0.0.1 - - [04/Oct/2026 18:19:05] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[23:48:56] BOOT      VIX Fix app up (pid 2363, DATA_DIR=/home/runner/work/Nifty-Trading-Cloud/Nifty-Trading-Cloud/strategies/vix_fix/data)
serving NIFTY VIX Fix - Monthly 1000s on http://127.0.0.1:50381
[23:48:58] CONTROL   started automatically on launch
[23:49:01] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[23:49:01] VIX       India VIX prev close 14.46
127.0.0.1 - - [04/Oct/2026 18:19:05] "GET /api/state HTTP/1.1" 200 -
```
</details>

