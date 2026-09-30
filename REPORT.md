# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:45 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.31** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹822 (+0.28%) | ₹0 | 0 | 5 | ₹2,98,641 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 | −₹1,297 (-8.42%) | 1 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | −₹478 (-0.12%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,508 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹4,410 (+3.99%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹9,441** | **+₹4,754** | **−₹9,441** | **10** | **14** | **₹7,97,705** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:38:37] API_ERROR marketfeed/ltp: ReadTimeout
[2026-09-30 11:38:37] VIX       India VIX unavailable (network error: HTTPSConnectionPool(host='api.dhan.co', port=443): Read timed out. (read timeout=10)) - no new trades until it can be read
[2026-09-30 11:41:39] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:41:39] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 11:42:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:43:46] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:41:26] API       rate limited by Dhan - now one call every 15.1 s
[11:41:46] API       rate limited by Dhan - now one call every 15.1 s
[11:42:47] API       rate limited by Dhan - now one call every 15.1 s
[11:43:07] API       rate limited by Dhan - now one call every 15.1 s
[11:44:08] API       rate limited by Dhan - now one call every 15.1 s
[11:45:30] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:43:01] API       rate limited by Dhan - now one call every 15.1 s
[11:43:31] API       rate limited by Dhan - now one call every 15.1 s
[11:44:01] API       rate limited by Dhan - now one call every 15.1 s
[11:44:31] API       rate limited by Dhan - now one call every 15.1 s
[11:44:47] API       rate limited by Dhan - now one call every 15.1 s
[11:45:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:11:35] API       rate limited by Dhan - now one call every 5.1 s
[11:12:57] API       rate limited by Dhan - now one call every 5.1 s
[11:18:22] API       rate limited by Dhan - now one call every 5.1 s
[11:29:51] VIX       India VIX prev close 13.41 - entries allowed
[11:30:35] API       rate limited by Dhan - now one call every 5.1 s
[11:31:57] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
serving NIFTY Scalper - IVX-G on http://127.0.0.1:46175
[2026-09-30 09:29:47] RUN       scalper armed - started automatically on launch
[2026-09-30 09:29:48] BOOT      scrip master: 4036 NIFTY contracts
[2026-09-30 09:29:48] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [30/Sep/2026 03:59:53] "GET /api/state HTTP/1.1" 200 -
[2026-09-30 11:38:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:44:31] GAP       1 contract had no prices for 124+ session minutes (HEROMOTOCO 5250 CE 27 Oct) - reloading their bar history
[11:44:32] WARM      bar history loaded for all 1564 contracts
[11:44:50] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:45:04] SIGNAL    ADANIPORTS 1800 CE 27 Oct crossed EMA 144 at 34.50 - not taken: momentum 1.5%
[11:45:04] SIGNAL    SOLARINDS 20000 PE 27 Oct crossed EMA 144 at 980.95 - not taken: under EMA 55
[11:45:40] WARM      bar history loaded for all 1564 contracts
```
</details>

