# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 14:24 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **15.29 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹12,503 (+11.62%) | ₹0 | +₹20,420 (+9.20%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹39,292 (+9.60%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,09,352 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | −₹558 (-0.61%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹55,538** | **+₹38,734** | **+₹33,168** | **24** | **9** | **₹5,01,294** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 14:14:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:17:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:17:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 14:20:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:20:42] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 14:21:42] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:19:53] API       rate limited by Dhan - now one call every 15.1 s
[14:20:54] API       rate limited by Dhan - now one call every 15.1 s
[14:21:14] API       rate limited by Dhan - now one call every 15.1 s
[14:21:44] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:22:35] API       rate limited by Dhan - now one call every 15.1 s
[14:23:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:22:30] API       rate limited by Dhan - now one call every 15.1 s
[14:22:45] API       rate limited by Dhan - now one call every 15.1 s
[14:23:01] API       rate limited by Dhan - now one call every 15.1 s
[14:23:31] API       rate limited by Dhan - now one call every 15.1 s
[14:23:46] API       rate limited by Dhan - now one call every 15.1 s
[14:24:02] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:19:11] API       rate limited by Dhan - now one call every 15.1 s
[14:19:27] API       rate limited by Dhan - now one call every 15.1 s
[14:19:42] API       rate limited by Dhan - now one call every 15.1 s
[14:21:06] API       rate limited by Dhan - now one call every 15.1 s
[14:22:18] API       rate limited by Dhan - now one call every 15.1 s
[14:23:30] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 14:12:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:14:29] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:16:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:19:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:20:02] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:23:25] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:20:09] SIGNAL    DLF 630 PE 27 Oct crossed EMA 144 at 9.55 - not taken: momentum 3.2%
[14:20:09] SIGNAL    DMART 3900 CE 27 Oct crossed EMA 144 at 96.85 - not taken: under EMA 55, momentum 3.0%
[14:21:24] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:21:51] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:22:09] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:22:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

