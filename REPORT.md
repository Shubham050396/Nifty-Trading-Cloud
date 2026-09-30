# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 09:45 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.32** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹370 (+0.20%) | ₹0 | 0 | 3 | ₹1,85,380 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹998 (-0.55%) | ₹0 | 0 | 4 | ₹1,80,310 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹1,691 (+2.54%) | ₹0 | 0 | 3 | ₹66,562 |
| **Total** | | **₹0** | **+₹1,063** | **₹0** | **0** | **10** | **₹4,32,252** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 09:40:24] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:40:24] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 09:41:28] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:43:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:43:35] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 09:44:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:42:26] API       rate limited by Dhan - now one call every 15.1 s
[09:42:41] API       rate limited by Dhan - now one call every 15.1 s
[09:43:26] API       rate limited by Dhan - now one call every 15.1 s
[09:43:41] API       rate limited by Dhan - now one call every 15.1 s
[09:44:25] API       rate limited by Dhan - now one call every 15.1 s
[09:44:41] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:43:07] API       rate limited by Dhan - now one call every 15.1 s
[09:43:22] API       rate limited by Dhan - now one call every 15.1 s
[09:43:37] API       rate limited by Dhan - now one call every 15.1 s
[09:43:53] API       rate limited by Dhan - now one call every 15.1 s
[09:44:23] API       rate limited by Dhan - now one call every 15.1 s
[09:44:53] API       rate limited by Dhan - now one call every 15.1 s
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
[09:40:02] ENTRY     BUY DIVISLAB 9500 PE 27 Oct x100 @ 297.50 (signal close 293.00, EMA 144 282.19, momentum 22.3%)  quick 342.12 till 10:10, target 505.75, stop below EMA 55
[09:40:02] ENTRY     BUY VBL 430 CE 27 Oct x1275 @ 15.20 (signal close 15.00, EMA 144 14.37, momentum 7.9%)  quick 17.48 till 10:10, target 25.84, stop below EMA 55
[09:40:29] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:42:22] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:42:30] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:42:32] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

