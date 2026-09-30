# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 09:34 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.31** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹23 (+0.01%) | ₹0 | 0 | 3 | ₹1,85,032 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹1,358 (-0.75%) | ₹0 | 0 | 4 | ₹1,80,146 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **₹0** | **−₹1,335** | **₹0** | **0** | **7** | **₹3,65,178** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 09:29:49] BOOT      Ready - 18 expiries, 4036 NIFTY contracts
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/status HTTP/1.1" 200 -
[2026-09-30 09:30:53] DEPLOY    auto-deployed 3 spread(s)
[2026-09-30 09:32:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:32:57] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 09:34:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:32:31] ENTRY     BULL 2026-10-27 (slot 4): SELL 22700 PE @ 254.65 + BUY 22500 PE @ 186.75 = credit 67.90 x 65 - max profit Rs 4414, max loss Rs 8586
[09:32:45] API       rate limited by Dhan - now one call every 15.1 s
[09:33:02] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:33:30] API       rate limited by Dhan - now one call every 15.1 s
[09:33:45] API       rate limited by Dhan - now one call every 15.1 s
[09:34:30] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:33:14] API       rate limited by Dhan - now one call every 15.1 s
[09:33:44] API       rate limited by Dhan - now one call every 15.1 s
[09:33:59] API       rate limited by Dhan - now one call every 15.1 s
[09:34:15] API       rate limited by Dhan - now one call every 15.1 s
[09:34:30] API       rate limited by Dhan - now one call every 15.1 s
[09:34:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:29:48] BOOT      ready - 14 monthly expiries, 4036 contracts in the scrip master
[09:29:48] VIX       India VIX prev close 13.41 - entries allowed
[09:29:52] HISTORY   2026-10-27 21000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
[09:30:01] HISTORY   2026-10-27 26000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[09:32:31] API       rate limited by Dhan - now one call every 5.1 s
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
[09:34:05] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:34:10] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:34:23] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:34:32] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:34:38] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:34:46] API       chart history: rate limited by Dhan - now one call every 1.2 s
```
</details>

