# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 15:04 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.67 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹12,503 (+11.62%) | ₹0 | +₹20,420 (+9.20%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹54,698 (+6.98%) | +₹6,497 (+1.15%) | +₹36,439 (+1.71%) | 8 | 5 | ₹5,62,656 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹13,314 (+6.46%) | −₹4,138 (-5.49%) | −₹89 (-0.03%) | 10 | 4 | ₹75,342 |
| **Total** | | **+₹80,834** | **+₹2,359** | **+₹58,463** | **29** | **9** | **₹6,37,998** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 14:51:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:51:49] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 14:53:49] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:53:49] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 15:03:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 15:03:51] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:59:12] API       rate limited by Dhan - now one call every 15.1 s
[15:01:14] API       rate limited by Dhan - now one call every 15.1 s
[15:01:55] API       rate limited by Dhan - now one call every 15.1 s
[15:02:56] API       rate limited by Dhan - now one call every 15.1 s
[15:03:16] API       rate limited by Dhan - now one call every 15.1 s
[15:03:17] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:02:57] API       rate limited by Dhan - now one call every 15.1 s
[15:03:12] API       rate limited by Dhan - now one call every 15.1 s
[15:03:28] API       rate limited by Dhan - now one call every 15.1 s
[15:03:30] VIX       India VIX prev close 13.49 -> target 1000 ticks (Rs 50.00)
[15:03:43] API       rate limited by Dhan - now one call every 15.1 s
[15:04:13] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[15:00:20] API       rate limited by Dhan - now one call every 15.1 s
[15:00:51] API       rate limited by Dhan - now one call every 15.1 s
[15:01:35] API       rate limited by Dhan - now one call every 15.1 s
[15:03:14] VIX       India VIX prev close 13.49 - entries allowed
[15:03:35] API       rate limited by Dhan - now one call every 15.1 s
[15:04:20] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 14:48:14] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:49:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:53:15] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:56:25] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:59:52] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 15:01:50] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:00:19] EXIT      SELL KOTAKBANK 420 CE 27 Oct PRE_HOLIDAY @ 10.00  +20.5%  P&L Rs 3400.00
[15:00:19] SIGNAL    DLF 650 PE 27 Oct crossed EMA 144 at 14.65 - not taken: momentum -10.7%
[15:01:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:01:55] WARM      bar history loaded for all 1582 contracts
[15:02:17] API       market quote: rate limited by Dhan - now one call every 9.1 s
[15:03:59] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

