# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 14:14 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **15.33 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹12,503 (+11.62%) | ₹0 | +₹20,420 (+9.20%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹37,817 (+9.24%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,09,394 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | +₹1,058 (+1.15%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹55,538** | **+₹38,875** | **+₹33,168** | **24** | **9** | **₹5,01,336** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 14:04:39] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 14:09:40] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:09:40] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 14:12:40] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 14:12:40] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 14:13:41] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[14:08:34] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:09:03] API       rate limited by Dhan - now one call every 15.1 s
[14:10:04] API       rate limited by Dhan - now one call every 15.1 s
[14:11:46] API       rate limited by Dhan - now one call every 15.1 s
[14:12:37] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:13:07] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:12:08] API       rate limited by Dhan - now one call every 15.1 s
[14:12:38] API       rate limited by Dhan - now one call every 15.1 s
[14:12:53] API       rate limited by Dhan - now one call every 15.1 s
[14:13:09] API       rate limited by Dhan - now one call every 15.1 s
[14:13:39] API       rate limited by Dhan - now one call every 15.1 s
[14:13:54] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[14:05:48] API       rate limited by Dhan - now one call every 15.1 s
[14:07:13] API       rate limited by Dhan - now one call every 15.1 s
[14:09:02] API       rate limited by Dhan - now one call every 15.1 s
[14:11:23] API       rate limited by Dhan - now one call every 15.1 s
[14:12:47] API       rate limited by Dhan - now one call every 15.1 s
[14:13:59] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 14:03:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:05:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:07:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:09:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:10:20] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:12:27] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:09:02] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:10:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:10:54] SIGNAL    DMART 3800 CE 27 Oct crossed EMA 144 at 142.20 - not taken: under EMA 55, momentum 0.0%
[14:12:04] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:12:13] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:13:48] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

