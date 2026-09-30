# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 09:50 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.37** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹604 (+0.33%) | ₹0 | 0 | 3 | ₹1,85,614 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹1,268 (-0.70%) | ₹0 | 0 | 4 | ₹1,80,235 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹632 (+0.95%) | ₹0 | 0 | 3 | ₹66,562 |
| **Total** | | **₹0** | **−₹32** | **₹0** | **0** | **10** | **₹4,32,411** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 09:44:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:45:43] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:46:47] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:47:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:48:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:50:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:46:40] API       rate limited by Dhan - now one call every 15.1 s
[09:47:25] API       rate limited by Dhan - now one call every 15.1 s
[09:47:40] API       rate limited by Dhan - now one call every 15.1 s
[09:48:25] API       rate limited by Dhan - now one call every 15.1 s
[09:48:40] API       rate limited by Dhan - now one call every 15.1 s
[09:49:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:48:10] API       rate limited by Dhan - now one call every 15.1 s
[09:48:26] API       rate limited by Dhan - now one call every 15.1 s
[09:48:56] API       rate limited by Dhan - now one call every 15.1 s
[09:49:26] API       rate limited by Dhan - now one call every 15.1 s
[09:49:41] API       rate limited by Dhan - now one call every 15.1 s
[09:49:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:29:48] VIX       India VIX prev close 13.41 - entries allowed
[09:29:52] HISTORY   2026-10-27 21000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
[09:30:01] HISTORY   2026-10-27 26000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[09:32:31] API       rate limited by Dhan - now one call every 5.1 s
[09:49:25] API       rate limited by Dhan - now one call every 5.1 s
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
[09:42:22] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:42:30] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:42:32] API       market quote: rate limited by Dhan - now one call every 2.0 s
[09:45:01] API       market quote: rate limited by Dhan - now one call every 2.0 s
[09:45:10] SKIP      VBL 440 CE 27 Oct signal at 10.75 skipped - already 1 open on VBL
[09:45:21] API       chart history: rate limited by Dhan - now one call every 1.2 s
```
</details>

