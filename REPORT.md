# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:40 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.31** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹949 (+0.32%) | ₹0 | 0 | 5 | ₹2,98,767 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | −₹1,297 (-8.42%) | ₹0 | −₹1,297 (-8.42%) | 1 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | +₹166 (+0.04%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,484 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹5,785 (+5.23%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹9,441** | **+₹6,900** | **−₹9,441** | **10** | **14** | **₹7,97,807** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:34:12] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:35:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:36:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:37:23] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:38:37] API_ERROR marketfeed/ltp: ReadTimeout
[2026-09-30 11:38:37] VIX       India VIX unavailable (network error: HTTPSConnectionPool(host='api.dhan.co', port=443): Read timed out. (read timeout=10)) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:37:22] API       rate limited by Dhan - now one call every 15.1 s
[11:37:43] API       rate limited by Dhan - now one call every 15.1 s
[11:38:53] API       rate limited by Dhan - now one call every 15.1 s
[11:39:08] API       rate limited by Dhan - now one call every 15.1 s
[11:40:05] API       rate limited by Dhan - now one call every 15.1 s
[11:40:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:38:43] API       rate limited by Dhan - now one call every 15.1 s
[11:39:13] API       rate limited by Dhan - now one call every 15.1 s
[11:39:43] API       rate limited by Dhan - now one call every 15.1 s
[11:39:58] API       rate limited by Dhan - now one call every 15.1 s
[11:40:14] API       rate limited by Dhan - now one call every 15.1 s
[11:40:29] API       rate limited by Dhan - now one call every 15.1 s
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
[11:39:03] GAP       1 contract had no prices for 112+ session minutes (HINDALCO 930 CE 27 Oct) - reloading their bar history
[11:39:04] WARM      bar history loaded for all 1564 contracts
[11:39:31] API       market quote: rate limited by Dhan - now one call every 2.0 s
[11:40:03] SIGNAL    HDFCBANK 710 PE 27 Oct crossed EMA 144 at 13.05 - not taken: momentum -8.1%
[11:40:03] SIGNAL    VBL 450 CE 27 Oct crossed EMA 144 at 7.05 - not taken: under EMA 55, momentum -1.4%
[11:40:35] API       market quote: rate limited by Dhan - now one call every 2.0 s
```
</details>

