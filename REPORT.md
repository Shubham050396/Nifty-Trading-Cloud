# NIFTY Cloud report

**Running until 17:32 IST** · updated 04 Oct 2026 17:27 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37200456235)

India VIX **14.46 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 08:01 IST · trading window: 17:27 → 17:32 IST (check run (weekend))

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
serving NIFTY Credit Spreads on http://127.0.0.1:44429
[2026-10-04 17:27:30] SCAN      scanner started automatically on launch
[2026-10-04 17:27:35] BOOT      scrip master downloaded: 4120 NIFTY contracts in 5.0s
[2026-10-04 17:27:36] BOOT      Ready - 18 expiries, 4120 NIFTY contracts
[2026-10-04 17:27:36] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/status HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[17:27:32] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[17:27:36] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
[17:27:40] CONFIG    settings saved - 5-min candles, EMA 500/200, lookback 25; credit spreads, hedge 4 strikes (400 pts), expiries 1,2,3,4 - signal restarts from history
127.0.0.1 - - [04/Oct/2026 11:57:40] "POST /api/config HTTP/1.1" 200 -
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[17:27:36] BOOT      ready - 18 expiries, 4120 contracts in the scrip master
[17:27:37] VIX       India VIX prev close 14.46 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
[17:27:40] CONFIG    settings saved - 4 expiries x CE/PE, ATM +/- 10 strikes
127.0.0.1 - - [04/Oct/2026 11:57:40] "POST /api/config HTTP/1.1" 200 -
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[17:27:31] HISTORY   2026-10-27 21000 CE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[17:27:32] CONTROL   started automatically on launch
[17:27:32] DAY       new session 2026-10-04 - counters reset
[17:27:36] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[17:27:37] VIX       India VIX prev close 14.46 - entries allowed
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-04 17:27:36] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-04 17:27:36] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
[2026-10-04 17:27:40] CFG       settings updated
127.0.0.1 - - [04/Oct/2026 11:57:40] "POST /api/config HTTP/1.1" 200 -
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[17:27:36] API       share prices unavailable: HTTP 429
[17:27:38] API       chart history: rate limited by Dhan - now one call every 3.8 s
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
[17:27:40] CONFIG    settings saved - 100 stocks (99 with options), ATM +/- 1, CE/PE, 5-min bars, EMA 55/144 on 30 min
127.0.0.1 - - [04/Oct/2026 11:57:40] "POST /api/config HTTP/1.1" 200 -
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
serving NIFTY VIX Fix - Monthly 1000s on http://127.0.0.1:36871
[17:27:32] CONTROL   started automatically on launch
[17:27:32] DAY       new session 2026-10-04 - counters reset
[17:27:36] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[17:27:37] VIX       India VIX prev close 14.46
127.0.0.1 - - [04/Oct/2026 11:57:40] "GET /api/state HTTP/1.1" 200 -
```
</details>

