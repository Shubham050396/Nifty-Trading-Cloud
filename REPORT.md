# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:05 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.37** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹471 (+0.20%) | ₹0 | 0 | 4 | ₹2,33,936 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹224 (-0.12%) | ₹0 | 0 | 4 | ₹1,80,430 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹614 (-0.44%) | −₹673 (-0.33%) | −₹614 (-0.44%) | 1 | 2 | ₹2,03,312 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹1,255 (+1.07%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹614** | **+₹829** | **−₹614** | **1** | **15** | **₹7,35,382** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:00:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:00:34] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:01:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:03:45] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:03:45] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:04:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:02:12] API       rate limited by Dhan - now one call every 15.1 s
[10:02:27] API       rate limited by Dhan - now one call every 15.1 s
[10:03:11] API       rate limited by Dhan - now one call every 15.1 s
[10:04:10] API       rate limited by Dhan - now one call every 15.1 s
[10:04:25] API       rate limited by Dhan - now one call every 15.1 s
[10:04:42] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:03:08] API       rate limited by Dhan - now one call every 15.1 s
[10:03:38] API       rate limited by Dhan - now one call every 15.1 s
[10:04:08] API       rate limited by Dhan - now one call every 15.1 s
[10:04:23] API       rate limited by Dhan - now one call every 15.1 s
[10:04:39] API       rate limited by Dhan - now one call every 15.1 s
[10:04:54] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:55:00] ENTRY     SELL SHORT 2026-10-27 22000 CE @ 915.85  (bar close 908.65, MACD hist -0.21, VIX 13.41)
[09:57:21] API       rate limited by Dhan - now one call every 5.1 s
[09:58:20] API       rate limited by Dhan - now one call every 5.1 s
[10:00:02] SIGNAL    2026-10-27 22000 CE MACD crossed UP (bar close 927.00, hist -0.21 -> +0.12)
[10:00:02] EXIT      SHORT 2026-10-27 22000 CE MACD_UP @ 925.30  P&L Rs -614.25
[10:00:02] ENTRY     BUY 2026-10-27 22000 CE @ 925.30  (bar close 927.00, MACD hist +0.12, VIX 13.41)
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
[10:05:05] SIGNAL    TECHM 1600 PE 27 Oct crossed EMA 144 at 82.50 - not taken: under EMA 55, momentum -16.7%
[10:05:05] SIGNAL    WIPRO 155 PE 27 Oct crossed EMA 144 at 2.67 - not taken: under EMA 55, momentum -36.3%, premium under Rs 5
[10:05:05] SIGNAL    BPCL 300 PE 27 Oct crossed EMA 144 at 5.30 - not taken: under EMA 55, momentum -24.3%
[10:05:05] SIGNAL    BPCL 320 PE 27 Oct crossed EMA 144 at 16.50 - not taken: under EMA 55, momentum -17.5%
[10:05:05] SIGNAL    DABUR 390 PE 27 Oct crossed EMA 144 at 12.00 - not taken: momentum -14.6%
[10:05:06] SKIP      KOTAKBANK 410 CE 27 Oct signal at 12.15 skipped - 5 positions already open
```
</details>

