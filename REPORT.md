# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:10 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.03** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹211 (+0.09%) | ₹0 | 0 | 4 | ₹2,33,676 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹221 (-0.12%) | ₹0 | 0 | 4 | ₹1,80,467 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹1,313 (-0.46%) | +₹75 (+0.10%) | −₹1,313 (-0.46%) | 2 | 2 | ₹75,680 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹2,492 (+2.12%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹1,313** | **+₹2,557** | **−₹1,313** | **2** | **15** | **₹6,07,527** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:04:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:05:53] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:06:57] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:09:04] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:09:04] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:10:08] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:08:09] API       rate limited by Dhan - now one call every 15.1 s
[10:08:25] API       rate limited by Dhan - now one call every 15.1 s
[10:08:26] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:09:09] API       rate limited by Dhan - now one call every 15.1 s
[10:09:24] API       rate limited by Dhan - now one call every 15.1 s
[10:10:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:08:11] API       rate limited by Dhan - now one call every 15.1 s
[10:08:41] API       rate limited by Dhan - now one call every 15.1 s
[10:08:56] API       rate limited by Dhan - now one call every 15.1 s
[10:09:12] API       rate limited by Dhan - now one call every 15.1 s
[10:09:27] API       rate limited by Dhan - now one call every 15.1 s
[10:09:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:00:02] SIGNAL    2026-10-27 22000 CE MACD crossed UP (bar close 927.00, hist -0.21 -> +0.12)
[10:00:02] EXIT      SHORT 2026-10-27 22000 CE MACD_UP @ 925.30  P&L Rs -614.25
[10:00:02] ENTRY     BUY 2026-10-27 22000 CE @ 925.30  (bar close 927.00, MACD hist +0.12, VIX 13.41)
[10:10:01] SIGNAL    2026-10-27 23000 CE MACD crossed UP (bar close 238.50, hist -0.07 -> +0.02)
[10:10:01] EXIT      SHORT 2026-10-27 23000 CE MACD_UP @ 239.00  P&L Rs -698.75
[10:10:01] ENTRY     BUY 2026-10-27 23000 CE @ 239.00  (bar close 238.50, MACD hist +0.02, VIX 13.41)
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
[10:09:23] WARM      bar history loaded for all 1524 contracts
[10:09:41] API       market quote: rate limited by Dhan - now one call every 2.0 s
[10:10:03] SIGNAL    DABUR 380 PE 27 Oct crossed EMA 144 at 6.90 - not taken: momentum -6.1%
[10:10:04] SKIP      BPCL 310 PE 27 Oct signal at 10.35 skipped - 5 positions already open
[10:10:04] SKIP      DLF 650 PE 27 Oct signal at 15.05 skipped - 5 positions already open
[10:10:04] SKIP      ICICIGI 1500 CE 27 Oct signal at 68.65 skipped - 5 positions already open
```
</details>

