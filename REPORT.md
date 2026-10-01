# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 13:58 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **15.20 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,253 (+10.10%) | +₹1,521 (+9.51%) | +₹17,170 (+8.34%) | 5 | 1 | ₹15,993 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹44,850 (+10.96%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,09,049 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | +₹5,985 (+6.51%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹52,288** | **+₹52,356** | **+₹29,918** | **23** | **10** | **₹5,16,984** |

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
[13:55:09] API       rate limited by Dhan - now one call every 15.1 s
[13:55:30] API       rate limited by Dhan - now one call every 15.1 s
[13:55:50] API       rate limited by Dhan - now one call every 15.1 s
[13:56:51] API       rate limited by Dhan - now one call every 15.1 s
[13:58:12] API       rate limited by Dhan - now one call every 15.1 s
[13:58:28] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:56:30] API       rate limited by Dhan - now one call every 15.1 s
[13:57:00] API       rate limited by Dhan - now one call every 15.1 s
[13:57:16] API       rate limited by Dhan - now one call every 15.1 s
[13:57:31] API       rate limited by Dhan - now one call every 15.1 s
[13:58:15] API       rate limited by Dhan - now one call every 15.1 s
[13:58:46] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:51:08] API       rate limited by Dhan - now one call every 15.1 s
[13:52:32] API       rate limited by Dhan - now one call every 15.1 s
[13:53:44] API       rate limited by Dhan - now one call every 15.1 s
[13:55:20] API       rate limited by Dhan - now one call every 15.1 s
[13:56:32] API       rate limited by Dhan - now one call every 15.1 s
[13:58:53] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 13:47:59] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:50:02] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:52:17] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:54:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:56:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:57:50] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:56:19] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:57:21] WARM      bar history loaded for all 1580 contracts
[13:57:42] WARM      bar history loaded for all 1580 contracts
[13:58:02] WARM      bar history loaded for all 1580 contracts
[13:58:06] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:58:50] CONTRACT  watching 1580 contracts on 99 stocks (ATM +/- 3, CE/PE): 10 added, 10 dropped
```
</details>

