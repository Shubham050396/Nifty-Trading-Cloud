# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:38 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.06 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹1,424 (+3.83%) | +₹7,917 (+6.92%) | 0 | 2 | ₹37,193 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹2,785 (+0.68%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,11,809 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹5,142 (-10.81%) | +₹15,208 (+13.93%) | −₹18,545 (-9.61%) | 3 | 5 | ₹1,09,176 |
| **Total** | | **+₹27,917** | **+₹19,417** | **+₹5,547** | **11** | **11** | **₹5,58,178** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:30:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:30:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:36:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:36:20] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:38:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:38:21] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:36:33] API       rate limited by Dhan - now one call every 15.1 s
[12:36:54] API       rate limited by Dhan - now one call every 15.1 s
[12:37:14] API       rate limited by Dhan - now one call every 15.1 s
[12:37:34] API       rate limited by Dhan - now one call every 15.1 s
[12:37:54] API       rate limited by Dhan - now one call every 15.1 s
[12:38:15] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:36:37] API       rate limited by Dhan - now one call every 15.1 s
[12:36:52] API       rate limited by Dhan - now one call every 15.1 s
[12:37:22] API       rate limited by Dhan - now one call every 15.1 s
[12:37:38] API       rate limited by Dhan - now one call every 15.1 s
[12:38:08] API       rate limited by Dhan - now one call every 15.1 s
[12:38:23] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:31:42] API       rate limited by Dhan - now one call every 15.1 s
[12:33:42] API       rate limited by Dhan - now one call every 15.1 s
[12:36:03] API       rate limited by Dhan - now one call every 15.1 s
[12:36:33] API       rate limited by Dhan - now one call every 15.1 s
[12:37:18] API       rate limited by Dhan - now one call every 15.1 s
[12:38:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:26:34] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:29:01] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:31:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:33:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:35:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:37:56] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:35:38] ENTRY     BUY BPCL 305 PE 27 Oct x1975 @ 7.85 (signal close 8.25, EMA 144 7.92, momentum 13.8%)  quick 9.03 till 13:05, target 13.34, stop below EMA 55
[12:35:38] SKIP      BPCL 310 PE 27 Oct signal at 10.70 skipped - 5 positions already open
[12:36:12] SKIP      INDHOTEL 720 PE 27 Oct signal at 14.40 skipped - 5 positions already open
[12:36:30] WARM      bar history loaded for all 1490 contracts
[12:37:57] API       market quote: rate limited by Dhan - now one call every 5.0 s
[12:38:12] API       market quote: rate limited by Dhan - now one call every 8.1 s
```
</details>

