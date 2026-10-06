# NIFTY Cloud report

**Running until 15:15 IST** · updated 06 Oct 2026 14:35 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37406688397)

India VIX **-** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 06 Oct 21:29 IST · trading window: 14:35 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹21,548 (+6.41%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹2,844 (+2.05%) | −₹4,904 (-0.44%) | +₹55,282 (+1.30%) | 1 | 9 | ₹11,12,544 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | −₹6,454 (-5.53%) | −₹27,375 (-3.83%) | 0 | 6 | ₹1,16,599 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹18,281 (-11.93%) | ₹0 | 0 | 8 | ₹1,53,295 |
| **Total** | | **+₹2,844** | **−₹29,639** | **+₹51,550** | **1** | **23** | **₹13,82,438** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-06 14:35:17] SCAN      scanner started automatically on launch
serving NIFTY Credit Spreads on http://127.0.0.1:46959
[2026-10-06 14:35:22] BOOT      scrip master downloaded: 4120 NIFTY contracts in 4.7s
[2026-10-06 14:35:22] BOOT      Ready - 18 expiries, 4120 NIFTY contracts
[2026-10-06 14:35:22] VIX       India VIX 13.82 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/status HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:35:18] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:35:19] CANDLES   NIFTY candles unavailable: Too many requests on server from single user breaching rate limits. Try throttling API calls. - retrying
[14:35:21] VIX       India VIX 13.81 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[14:35:22] BOOT      ready - 18 expiries listed, NIFTY lot 65
[14:35:24] SKIP      LONG signal at 2026-10-06 14:05 was missed (the app had no candles then) - not traded late
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:35:25] GAP       2026-10-13 23400 PE: no prices for 1401 min - bar history restarts
[14:35:25] GAP       2026-10-13 22000 PE: no prices for 1401 min - bar history restarts
[14:35:25] GAP       2026-10-13 22900 PE: no prices for 1401 min - bar history restarts
[14:35:25] GAP       2026-10-13 21500 CE: no prices for 1401 min - bar history restarts
[14:35:25] GAP       2026-10-13 21500 PE: no prices for 1401 min - bar history restarts
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:35:22] VIX       India VIX prev close 14.78 - entries allowed
[14:35:24] HISTORY   2026-11-23 23000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[14:35:25] CONTRACT  2026-11-23: watching ATM 23000 +/- 1 strikes of 1000 (CE/PE)
[14:35:25] SIGNAL    2026-11-23 22000 PE: MACD crossed UP while prices were not being watched
[14:35:25] EXIT      SHORT 2026-11-23 22000 PE MACD_UP_MISSED @ 155.25  P&L Rs 2843.75
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
cloud: HALT_ALL 15:25 -> 15:13
serving NIFTY Scalper - IVX-G on http://127.0.0.1:41191
[2026-10-06 14:35:21] RUN       scalper armed - started automatically on launch
[2026-10-06 14:35:22] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-06 14:35:23] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-13
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:35:23] BOOT      scrip master downloaded in 6s: 213 stocks with options
[14:35:23] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[14:35:23] CONTROL   started automatically on launch - 99 stocks
[14:35:23] API       market quote: rate limited by Dhan - now one call every 2.0 s
[14:35:26] API       market quote: rate limited by Dhan - now one call every 3.0 s
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[14:35:19] VIX       India VIX prev close 14.78
[14:35:20] API       rate limited by Dhan - now one call every 5.1 s
[14:35:23] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[14:35:23] VIX       India VIX prev close 14.78
[14:35:25] CONTRACT  2026-10-27: watching ATM 23000 +/- 3 strikes of 1000 (CE/PE)
127.0.0.1 - - [06/Oct/2026 09:05:26] "GET /api/state HTTP/1.1" 200 -
```
</details>

