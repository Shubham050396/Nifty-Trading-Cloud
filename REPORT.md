# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:55 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹864 (+0.29%) | ₹0 | 0 | 5 | ₹2,98,683 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | −₹497 (-3.23%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | −₹306 (-0.08%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,550 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹2,274 (+1.93%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹5,746** | **+₹2,335** | **−₹5,746** | **8** | **15** | **₹8,20,329** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:48:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:49:30] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:50:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:52:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:52:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:53:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:51:13] API       rate limited by Dhan - now one call every 15.1 s
[10:52:27] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:52:35] API       rate limited by Dhan - now one call every 15.1 s
[10:53:56] API       rate limited by Dhan - now one call every 15.1 s
[10:54:17] API       rate limited by Dhan - now one call every 15.1 s
[10:55:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:53:27] API       rate limited by Dhan - now one call every 15.1 s
[10:53:57] API       rate limited by Dhan - now one call every 15.1 s
[10:54:12] API       rate limited by Dhan - now one call every 15.1 s
[10:54:28] API       rate limited by Dhan - now one call every 15.1 s
[10:54:43] API       rate limited by Dhan - now one call every 15.1 s
[10:55:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:50:00] SIGNAL    2026-10-27 25000 PE MACD crossed UP (bar close 2155.00, hist -0.50 -> +0.38)
[10:50:00] SKIP      buy 2026-10-27 25000 PE ignored - premium 2155.00 is outside 144 - 1600
[10:55:01] SIGNAL    2026-10-27 26000 PE MACD crossed UP (bar close 3136.00, hist -0.06 -> +0.65)
[10:55:01] SKIP      buy 2026-10-27 26000 PE ignored - premium 3136.00 is outside 144 - 1600
[10:55:01] SIGNAL    2026-10-27 23000 PE MACD crossed UP (bar close 392.55, hist -0.15 -> +0.29)
[10:55:01] ENTRY     BUY 2026-10-27 23000 PE @ 392.90  (bar close 392.55, MACD hist +0.29, VIX 13.41)
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
[10:54:49] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:55:01] SIGNAL    HCLTECH 1220 PE 27 Oct crossed EMA 144 at 34.05 - not taken: under EMA 55, momentum 3.3%
[10:55:01] SIGNAL    INFY 1080 PE 27 Oct crossed EMA 144 at 74.35 - not taken: under EMA 55, momentum 3.1%
[10:55:01] SIGNAL    KOTAKBANK 410 CE 27 Oct crossed EMA 144 at 12.20 - not taken: momentum 0.4%
[10:55:05] GAP       1 contract had no prices for 59+ session minutes (NTPC 312.5 PE 27 Oct) - reloading their bar history
[10:55:06] WARM      bar history loaded for all 1548 contracts
```
</details>

