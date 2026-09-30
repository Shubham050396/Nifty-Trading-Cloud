# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 11:30 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.31** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹1,112 (+0.37%) | ₹0 | 0 | 5 | ₹2,98,930 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | −₹387 (-2.51%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹4,111 (-1.14%) | +₹2,210 (+0.57%) | −₹4,111 (-1.14%) | 4 | 4 | ₹3,88,371 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹2,398 (-8.47%) | +₹5,919 (+5.35%) | −₹2,398 (-8.47%) | 1 | 5 | ₹1,10,556 |
| **Total** | | **−₹8,144** | **+₹8,854** | **−₹8,144** | **9** | **15** | **₹8,13,249** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 11:25:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:25:41] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 11:26:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:28:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 11:28:53] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 11:29:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:24:08] API       rate limited by Dhan - now one call every 15.1 s
[11:25:09] API       rate limited by Dhan - now one call every 15.1 s
[11:26:31] API       rate limited by Dhan - now one call every 15.1 s
[11:26:51] API       rate limited by Dhan - now one call every 15.1 s
[11:27:52] API       rate limited by Dhan - now one call every 15.1 s
[11:29:14] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:28:37] API       rate limited by Dhan - now one call every 15.1 s
[11:28:52] API       rate limited by Dhan - now one call every 15.1 s
[11:29:22] API       rate limited by Dhan - now one call every 15.1 s
[11:29:52] API       rate limited by Dhan - now one call every 15.1 s
[11:30:10] VIX       India VIX prev close 13.41 -> target 1000 ticks (Rs 50.00)
[11:30:22] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:06:10] API       rate limited by Dhan - now one call every 5.1 s
[11:11:35] API       rate limited by Dhan - now one call every 5.1 s
[11:12:57] API       rate limited by Dhan - now one call every 5.1 s
[11:18:22] API       rate limited by Dhan - now one call every 5.1 s
[11:29:51] VIX       India VIX prev close 13.41 - entries allowed
[11:30:35] API       rate limited by Dhan - now one call every 5.1 s
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
[11:28:47] WARM      bar history loaded for all 1560 contracts
[11:30:02] SIGNAL    TATASTEEL 182.5 CE 27 Oct crossed EMA 144 at 9.00 - not taken: under EMA 55, momentum 1.7%
[11:30:02] SIGNAL    DABUR 370 PE 27 Oct crossed EMA 144 at 4.25 - not taken: premium under Rs 5
[11:30:02] SIGNAL    VBL 450 CE 27 Oct crossed EMA 144 at 7.05 - not taken: under EMA 55, momentum 2.2%
[11:30:29] GAP       1 contract had no prices for 103+ session minutes (HINDALCO 930 PE 27 Oct) - reloading their bar history
[11:30:30] WARM      bar history loaded for all 1560 contracts
```
</details>

