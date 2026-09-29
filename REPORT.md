# NIFTY Cloud report

**Running until 06:14 IST** · updated 30 Sep 2026 00:25 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36614929896)

India VIX **13.41** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 00:20 → 06:14 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **₹0** | **₹0** | **₹0** | **0** | **0** | **₹0** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 00:20:37] SCAN      scanner started automatically on launch
serving NIFTY Credit Spreads on http://127.0.0.1:48789
[2026-09-30 00:20:41] BOOT      scrip master downloaded: 4104 NIFTY contracts in 4.4s
[2026-09-30 00:20:42] BOOT      Ready - 18 expiries, 4104 NIFTY contracts
127.0.0.1 - - [29/Sep/2026 18:50:47] "GET /api/status HTTP/1.1" 200 -
[2026-09-30 00:20:47] MARKET    heartbeat: pre-open, session starts 09:15 IST; token expires in 22h 20m
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
cloud: expiry-day exit 15:15 -> 06:09
serving NIFTY EMA Breakout Hedge on http://127.0.0.1:53839
[00:20:38] CONTROL   started automatically on launch
[00:20:38] DAY       new session 2026-09-30
[00:20:42] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [29/Sep/2026 18:50:47] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[00:20:39] CONTROL   started automatically on launch
[00:20:39] DAY       new session 2026-09-30 - counters reset
[00:20:39] CONFIG    removed expired expiry 2026-09-29 - now using 2026-10-06 instead
[00:20:42] BOOT      ready - 17 expiries, 4104 contracts in the scrip master
[00:20:43] VIX       India VIX prev close 13.64 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [29/Sep/2026 18:50:47] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
serving NIFTY MACD - Monthly 1000s on http://127.0.0.1:45093
[00:20:39] CONTROL   started automatically on launch
[00:20:39] DAY       new session 2026-09-30 - counters reset
[00:20:42] BOOT      ready - 13 monthly expiries, 4104 contracts in the scrip master
[00:20:42] VIX       India VIX prev close 13.64 - entries allowed
127.0.0.1 - - [29/Sep/2026 18:50:47] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-09-30 00:20:41] DAY       new session 2026-09-30 - counters reset (kill switch is NOT cleared)
[2026-09-30 00:20:41] DATA      buffer cleared: day roll
[2026-09-30 00:20:41] RUN       scalper armed - started automatically on launch
[2026-09-30 00:20:42] BOOT      scrip master: 4104 NIFTY contracts
[2026-09-30 00:20:42] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [29/Sep/2026 18:50:47] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[00:20:42] BOOT      scrip master downloaded in 5s: 210 stocks with options
[00:20:42] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[00:20:43] CONTROL   started automatically on launch - 99 stocks
[00:20:43] API       market quote: rate limited by Dhan - now one call every 2.0 s
[00:20:43] API       share prices unavailable: HTTP 429
127.0.0.1 - - [29/Sep/2026 18:50:47] "GET /api/state HTTP/1.1" 200 -
```
</details>

