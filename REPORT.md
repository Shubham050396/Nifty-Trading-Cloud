# NIFTY Cloud report

**Running until 15:33 IST** · updated 30 Sep 2026 15:28 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36699489409)

India VIX **13.41** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 15:28 → 15:33 IST (check run (after the trading day))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹3,010 (+1.00%) | ₹0 | +₹3,010 (+1.00%) | 5 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹7,917 (+6.92%) | ₹0 | +₹7,917 (+6.92%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹18,258 (-1.36%) | +₹20,394 (+5.29%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,85,742 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹9,071 (-7.30%) | −₹1,435 (-1.51%) | −₹9,071 (-7.30%) | 6 | 5 | ₹95,212 |
| **Total** | | **−₹18,037** | **+₹18,959** | **−₹18,037** | **35** | **9** | **₹4,80,954** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 15:28:25] SCAN      scanner started automatically on launch
[2026-09-30 15:28:30] BOOT      scrip master downloaded: 4036 NIFTY contracts in 5.3s
[2026-09-30 15:28:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 15:28:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 15:28:31] BOOT      Ready - 18 expiries, 4036 NIFTY contracts
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/status HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:28:25] BOOT      engine thread started
[15:28:25] BOOT      ema-hedge app up (pid 2310, DATA_DIR=/home/runner/work/Nifty-Trading-Cloud/Nifty-Trading-Cloud/strategies/ema_hedge/data)
serving NIFTY EMA Breakout Hedge on http://127.0.0.1:50861
[15:28:26] CONTROL   started automatically on launch
[15:28:30] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:28:33] GAP       2026-10-06 22900 PE: no prices for 14 min - bar history restarts
[15:28:33] GAP       2026-10-06 23800 CE: no prices for 14 min - bar history restarts
[15:28:33] GAP       2026-10-06 23800 PE: no prices for 14 min - bar history restarts
[15:28:33] GAP       2026-10-06 21600 CE: no prices for 14 min - bar history restarts
[15:28:33] GAP       2026-10-06 21600 PE: no prices for 14 min - bar history restarts
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[15:28:27] CONTROL   started automatically on launch
[15:28:28] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.) - no new entries until it loads - entries blocked (above 15)
[15:28:28] CONTRACT  2026-10-27: watching ATM 23000 +/- 3 strikes of 1000 (CE/PE)
[15:28:31] BOOT      ready - 14 monthly expiries, 4036 contracts in the scrip master
[15:28:31] VIX       India VIX prev close 13.41 - entries allowed
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-09-30 15:28:25] BOOT      scalper up (pid 2313, DATA_DIR=/home/runner/work/Nifty-Trading-Cloud/Nifty-Trading-Cloud/strategies/scalper/data, auth=off)
serving NIFTY Scalper - IVX-G on http://127.0.0.1:49191
[2026-09-30 15:28:29] RUN       scalper armed - started automatically on launch
[2026-09-30 15:28:30] BOOT      scrip master: 4036 NIFTY contracts
[2026-09-30 15:28:30] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:28:30] BOOT      scrip master downloaded in 5s: 213 stocks with options
[15:28:30] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[15:28:30] CONTROL   started automatically on launch - 99 stocks
[15:28:30] CONTRACT  watching 1386 contracts on 99 stocks (ATM +/- 3, CE/PE): 1381 added, 0 dropped
[15:28:31] API       chart history: rate limited by Dhan - now one call every 1.2 s
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/state HTTP/1.1" 200 -
```
</details>

