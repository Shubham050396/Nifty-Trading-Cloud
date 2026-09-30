# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 09:29 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.31** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹390 (-0.29%) | ₹0 | 0 | 3 | ₹1,35,307 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **₹0** | **−₹390** | **₹0** | **0** | **3** | **₹1,35,307** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 09:29:43] BOOT      started (pid 2268, DATA_DIR=/home/runner/work/Nifty-Trading-Cloud/Nifty-Trading-Cloud/strategies/credit_spreads/data, auth=off)
[2026-09-30 09:29:43] SCAN      scanner started automatically on launch
serving NIFTY Credit Spreads on http://127.0.0.1:48559
[2026-09-30 09:29:49] BOOT      scrip master downloaded: 4036 NIFTY contracts in 5.3s
[2026-09-30 09:29:49] BOOT      Ready - 18 expiries, 4036 NIFTY contracts
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/status HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:29:45] SIGNAL    LONG signal at 2026-09-30 09:20: NIFTY closed 22727.95 above the 100 EMA after 25+ bars under it - opening bullish spreads
[09:29:45] ENTRY     BULL 2026-10-06 (slot 1): SELL 22750 PE @ 136.15 + BUY 22550 PE @ 69.05 = credit 67.10 x 65 - max profit Rs 4362, max loss Rs 8638
[09:29:49] ENTRY     BULL 2026-10-13 (slot 2): SELL 22750 PE @ 189.65 + BUY 22550 PE @ 121.70 = credit 67.95 x 65 - max profit Rs 4417, max loss Rs 8583
[09:29:49] BOOT      ready - 18 expiries listed, NIFTY lot 65
[09:29:52] ENTRY     BULL 2026-10-19 (slot 3): SELL 22750 PE @ 224.40 + BUY 22550 PE @ 157.15 = credit 67.25 x 65 - max profit Rs 4371, max loss Rs 8629
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:29:46] VIX       India VIX prev close 13.41 -> target 1000 ticks (Rs 50.00)
[09:29:46] API       rate limited by Dhan - now one call every 5.1 s
[09:29:49] BOOT      ready - 18 expiries, 4036 contracts in the scrip master
[09:29:49] VIX       India VIX prev close 13.41 -> target 1000 ticks (Rs 50.00)
[09:29:51] CONTRACT  2026-10-06: watching ATM 22700 +/- 10 strikes (CE/PE)
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:29:46] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.) - no new entries until it loads - entries blocked (above 15)
[09:29:46] CONTRACT  2026-10-27: watching ATM 23000 +/- 3 strikes of 1000 (CE/PE)
[09:29:48] BOOT      ready - 14 monthly expiries, 4036 contracts in the scrip master
[09:29:48] VIX       India VIX prev close 13.41 - entries allowed
[09:29:52] HISTORY   2026-10-27 21000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
cloud: HALT_ALL 15:25 -> 15:13
serving NIFTY Scalper - IVX-G on http://127.0.0.1:46175
[2026-09-30 09:29:47] RUN       scalper armed - started automatically on launch
[2026-09-30 09:29:48] BOOT      scrip master: 4036 NIFTY contracts
[2026-09-30 09:29:48] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:29:49] BOOT      scrip master downloaded in 5s: 213 stocks with options
[09:29:49] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[09:29:49] CONTROL   started automatically on launch - 99 stocks
[09:29:49] API       market quote: rate limited by Dhan - now one call every 2.0 s
[09:29:51] CONTRACT  watching 1386 contracts on 99 stocks (ATM +/- 3, CE/PE): 1386 added, 0 dropped
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
```
</details>

