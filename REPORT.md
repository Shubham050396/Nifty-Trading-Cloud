# NIFTY Cloud report

**Running until 15:15 IST** · updated 30 Sep 2026 09:55 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36666861472)

India VIX **13.37** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 09:29 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | +₹478 (+0.26%) | ₹0 | 0 | 3 | ₹1,85,487 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | −₹1,216 (-0.67%) | ₹0 | 0 | 4 | ₹1,80,338 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹806 (-0.28%) | ₹0 | 0 | 2 | ₹2,86,238 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | +₹411 (+0.35%) | ₹0 | 0 | 5 | ₹1,17,704 |
| **Total** | | **₹0** | **−₹1,133** | **₹0** | **0** | **14** | **₹7,69,767** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 09:48:54] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:50:00] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:50:59] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:52:03] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:53:07] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-09-30 09:54:11] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:52:22] API       rate limited by Dhan - now one call every 15.1 s
[09:52:37] API       rate limited by Dhan - now one call every 15.1 s
[09:53:22] API       rate limited by Dhan - now one call every 15.1 s
[09:53:37] API       rate limited by Dhan - now one call every 15.1 s
[09:54:22] API       rate limited by Dhan - now one call every 15.1 s
[09:54:37] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:52:59] API       rate limited by Dhan - now one call every 15.1 s
[09:53:29] API       rate limited by Dhan - now one call every 15.1 s
[09:53:59] API       rate limited by Dhan - now one call every 15.1 s
[09:54:15] API       rate limited by Dhan - now one call every 15.1 s
[09:54:30] API       rate limited by Dhan - now one call every 15.1 s
[09:54:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:49:25] API       rate limited by Dhan - now one call every 5.1 s
[09:50:05] SIGNAL    2026-10-27 23000 CE MACD crossed DOWN (bar close 229.00, hist +0.04 -> -0.20)
[09:50:05] ENTRY     SELL SHORT 2026-10-27 23000 CE @ 228.25  (bar close 229.00, MACD hist -0.20, VIX 13.41)
[09:51:24] API       rate limited by Dhan - now one call every 5.1 s
[09:55:00] SIGNAL    2026-10-27 22000 CE MACD crossed DOWN (bar close 908.65, hist +0.04 -> -0.21)
[09:55:00] ENTRY     SELL SHORT 2026-10-27 22000 CE @ 915.85  (bar close 908.65, MACD hist -0.21, VIX 13.41)
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
[09:54:30] API       chart history: rate limited by Dhan - now one call every 1.2 s
[09:55:04] SIGNAL    ITC 260 PE 27 Oct crossed EMA 144 at 2.80 - not taken: premium under Rs 5
[09:55:04] SIGNAL    GAIL 175 PE 27 Oct crossed EMA 144 at 4.88 - not taken: under EMA 55, momentum -13.3%, premium under Rs 5
[09:55:04] SIGNAL    INDHOTEL 700 PE 27 Oct crossed EMA 144 at 8.15 - not taken: momentum -3.0%
[09:55:04] SIGNAL    INDHOTEL 720 PE 27 Oct crossed EMA 144 at 15.65 - not taken: momentum -2.5%
[09:55:04] SIGNAL    IOC 135 PE 27 Oct crossed EMA 144 at 3.31 - not taken: under EMA 55, momentum -12.4%, premium under Rs 5
```
</details>

