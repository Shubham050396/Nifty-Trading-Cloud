# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:43 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **14.10 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹1,583 (+10.34%) | +₹656 (+3.00%) | +₹9,500 (+7.33%) | 1 | 1 | ₹21,889 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹6,146 (+1.49%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,11,690 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹5,142 (-10.81%) | +₹17,524 (+16.05%) | −₹18,545 (-9.61%) | 3 | 5 | ₹1,09,176 |
| **Total** | | **+₹29,500** | **+₹24,326** | **+₹7,130** | **12** | **10** | **₹5,42,755** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:38:21] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:39:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:41:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:41:21] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:42:21] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:43:22] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:41:17] API       rate limited by Dhan - now one call every 15.1 s
[12:41:38] API       rate limited by Dhan - now one call every 15.1 s
[12:41:58] API       rate limited by Dhan - now one call every 15.1 s
[12:42:18] API       rate limited by Dhan - now one call every 15.1 s
[12:42:59] API       rate limited by Dhan - now one call every 15.1 s
[12:43:19] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:41:41] API       rate limited by Dhan - now one call every 15.1 s
[12:41:57] API       rate limited by Dhan - now one call every 15.1 s
[12:42:12] EXIT      L2 2026-10-06 22700 PE PUSH_FAILED @ 259.80  P&L Rs 1582.75
[12:42:27] API       rate limited by Dhan - now one call every 15.1 s
[12:42:42] API       rate limited by Dhan - now one call every 15.1 s
[12:42:57] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:36:33] API       rate limited by Dhan - now one call every 15.1 s
[12:37:18] API       rate limited by Dhan - now one call every 15.1 s
[12:38:16] API       rate limited by Dhan - now one call every 15.1 s
[12:39:14] API       rate limited by Dhan - now one call every 15.1 s
[12:41:15] API       rate limited by Dhan - now one call every 15.1 s
[12:41:59] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:31:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:33:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:35:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:37:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:40:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:43:00] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:41:29] SKIP      DLF 650 PE 27 Oct signal at 14.65 skipped - 5 positions already open
[12:41:29] SKIP      VBL 420 PE 27 Oct signal at 9.50 skipped - 5 positions already open
[12:41:37] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:42:39] WARM      bar history loaded for all 1494 contracts
[12:43:01] WARM      bar history loaded for all 1494 contracts
[12:43:12] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

