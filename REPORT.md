# NIFTY Cloud report

**Running until 15:36 IST** · updated 02 Oct 2026 15:31 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36993095963)

India VIX **14.46 🔴 above the limit** (limit 13.50) · Dhan token: valid until 03 Oct 11:03 IST · trading window: 15:31 → 15:36 IST (check run (after the trading day))

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
[2026-10-02 15:31:10] SCAN      scanner started automatically on launch
serving NIFTY Credit Spreads on http://127.0.0.1:45723
[2026-10-02 15:31:16] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
[2026-10-02 15:31:16] BOOT      scrip master downloaded: 4120 NIFTY contracts in 5.4s
[2026-10-02 15:31:16] BOOT      Ready - 18 expiries, 4120 NIFTY contracts
127.0.0.1 - - [02/Oct/2026 10:01:20] "GET /api/status HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
serving NIFTY EMA Breakout Hedge on http://127.0.0.1:50703
[15:31:11] CONTROL   started automatically on launch
[15:31:11] DAY       new session 2026-10-02
[15:31:12] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[15:31:16] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [02/Oct/2026 10:01:20] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
serving NIFTY 2-Level Cross on http://127.0.0.1:39651
[15:31:12] CONTROL   started automatically on launch
[15:31:12] DAY       new session 2026-10-02 - counters reset
[15:31:15] BOOT      ready - 18 expiries, 4120 contracts in the scrip master
[15:31:15] VIX       India VIX prev close 14.46 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [02/Oct/2026 10:01:20] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[15:31:16] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[15:31:16] VIX       India VIX prev close 14.46 - entries allowed
127.0.0.1 - - [02/Oct/2026 10:01:20] "GET /api/state HTTP/1.1" 200 -
[15:31:20] CONFIG    settings saved - 4 monthly expiries x CE/PE, ATM +/- 1 strikes, 5 min bars, MACD 30/60/15, long and short
127.0.0.1 - - [02/Oct/2026 10:01:20] "POST /api/config HTTP/1.1" 200 -
127.0.0.1 - - [02/Oct/2026 10:01:20] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-02 15:31:14] DATA      buffer cleared: day roll
[2026-10-02 15:31:14] HALT      HALTED: session over (15:25)
[2026-10-02 15:31:14] RUN       scalper armed - started automatically on launch
[2026-10-02 15:31:15] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-02 15:31:15] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [02/Oct/2026 10:01:20] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:31:16] BOOT      scrip master downloaded in 6s: 213 stocks with options
[15:31:16] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[15:31:16] CONTROL   started automatically on launch - 99 stocks
[15:31:17] API       market quote: rate limited by Dhan - now one call every 2.0 s
[15:31:17] API       share prices unavailable: HTTP 429
127.0.0.1 - - [02/Oct/2026 10:01:20] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
serving NIFTY VIX Fix - Monthly 1000s on http://127.0.0.1:60983
[15:31:16] CONFIG    no monthly expiry chosen - using 2026-10-27
[15:31:16] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[15:31:16] VIX       India VIX prev close 14.46
[15:31:16] CONTROL   started automatically on launch
127.0.0.1 - - [02/Oct/2026 10:01:20] "GET /api/state HTTP/1.1" 200 -
```
</details>

