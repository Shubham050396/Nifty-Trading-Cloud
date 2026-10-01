# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 14:04 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **15.68 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹12,503 (+11.62%) | ₹0 | +₹20,420 (+9.20%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹51,106 (+12.51%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,08,642 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | +₹5,142 (+5.59%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹55,538** | **+₹56,248** | **+₹33,168** | **24** | **9** | **₹5,00,584** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 13:44:35] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 13:45:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:53:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:53:37] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 13:56:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:56:37] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:58:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:59:34] API       rate limited by Dhan - now one call every 15.1 s
[14:00:55] API       rate limited by Dhan - now one call every 15.1 s
[14:02:16] API       rate limited by Dhan - now one call every 15.1 s
[14:03:31] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[14:03:38] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[14:02:16] API       rate limited by Dhan - now one call every 15.1 s
[14:02:32] EXIT      L2 2026-10-06 22500 PE TARGET @ 296.05  P&L Rs 3250.00
[14:02:46] API       rate limited by Dhan - now one call every 15.1 s
[14:03:02] API       rate limited by Dhan - now one call every 15.1 s
[14:03:17] API       rate limited by Dhan - now one call every 15.1 s
[14:03:19] VIX       India VIX prev close 13.49 -> target 1000 ticks (Rs 50.00)
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:56:32] API       rate limited by Dhan - now one call every 15.1 s
[13:58:53] API       rate limited by Dhan - now one call every 15.1 s
[13:59:24] API       rate limited by Dhan - now one call every 15.1 s
[14:00:35] API       rate limited by Dhan - now one call every 15.1 s
[14:02:57] API       rate limited by Dhan - now one call every 15.1 s
[14:03:14] VIX       India VIX prev close 13.49 - entries allowed
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 13:54:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:56:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:57:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:59:35] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:01:50] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 14:03:36] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[14:01:41] API       market quote: rate limited by Dhan - now one call every 9.1 s
[14:01:44] WARM      bar history loaded for all 1582 contracts
[14:02:12] WARM      bar history loaded for all 1582 contracts
[14:02:39] WARM      bar history loaded for all 1582 contracts
[14:03:02] WARM      bar history loaded for all 1582 contracts
[14:03:10] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

