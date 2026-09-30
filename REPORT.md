# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 10:45 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **12.99** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹725 (+0.24%) | ₹0 | 0 | 5 | ₹2,98,543 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | −₹458 (-1.02%) | −₹1,115 (-0.82%) | −₹458 (-1.02%) | 1 | 3 | ₹1,35,138 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 (+0.00%) | ₹0 | 0 | 1 | ₹15,392 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹2,288 (-0.77%) | −₹1,970 (-0.97%) | −₹2,288 (-0.77%) | 3 | 2 | ₹2,03,146 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹1,108 (+0.94%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **−₹2,746** | **−₹1,252** | **−₹2,746** | **4** | **16** | **₹7,69,923** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 10:40:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:42:07] DEPLOY    auto-deployed 1 spread(s)
[2026-09-30 10:43:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:43:07] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 10:44:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 10:45:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:44:08] API       rate limited by Dhan - now one call every 15.1 s
[10:44:52] API       rate limited by Dhan - now one call every 15.1 s
[10:45:08] API       rate limited by Dhan - now one call every 15.1 s
[10:45:09] SIGNAL    EXIT LONG at 2026-09-30 10:40: NIFTY closed 22702.75 - closed through the stop EMA
[10:45:23] API       rate limited by Dhan - now one call every 15.1 s
[10:45:23] EXIT      BULL 2026-10-06: SELL 22750 PE @ 146.20 + BUY 22550 PE @ 72.05 - closed through the stop EMA. P&L Rs -458.25 (no live quote - last mark)
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:43:51] API       rate limited by Dhan - now one call every 15.1 s
[10:44:06] API       rate limited by Dhan - now one call every 15.1 s
[10:44:21] API       rate limited by Dhan - now one call every 15.1 s
[10:44:37] API       rate limited by Dhan - now one call every 15.1 s
[10:45:07] API       rate limited by Dhan - now one call every 15.1 s
[10:45:22] ENTRY     L2 BUY 2026-10-06 22900 PE @ 236.80  target 286.80  trail 201.28 (15%)
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:29:49] VIX       India VIX prev close 13.41 - entries allowed
[10:31:01] API       rate limited by Dhan - now one call every 5.1 s
[10:35:58] API       rate limited by Dhan - now one call every 5.1 s
[10:45:00] SIGNAL    2026-10-27 23000 CE MACD crossed DOWN (bar close 225.00, hist +0.11 -> -0.17)
[10:45:00] EXIT      LONG 2026-10-27 23000 CE MACD_DOWN @ 224.00  P&L Rs -975.00
[10:45:00] ENTRY     SELL SHORT 2026-10-27 23000 CE @ 224.00  (bar close 225.00, MACD hist -0.17, VIX 13.41)
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
[10:45:04] SIGNAL    HCLTECH 1250 PE 27 Oct crossed EMA 144 at 47.00 - not taken: under EMA 55, momentum -6.5%
[10:45:04] SIGNAL    TECHM 1600 PE 27 Oct crossed EMA 144 at 80.40 - not taken: under EMA 55, momentum -4.3%
[10:45:04] SIGNAL    ADANIPOWER 205 PE 27 Oct crossed EMA 144 at 7.27 - not taken: under EMA 55, momentum -17.9%
[10:45:04] SIGNAL    GAIL 175 PE 27 Oct crossed EMA 144 at 4.97 - not taken: momentum 1.8%, premium under Rs 5
[10:45:04] SIGNAL    SOLARINDS 20000 PE 27 Oct crossed EMA 144 at 990.00 - not taken: under EMA 55
[10:45:04] SIGNAL    ETERNAL 305 PE 27 Oct crossed EMA 144 at 4.50 - not taken: premium under Rs 5
```
</details>

