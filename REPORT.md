# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 12:23 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **13.76 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹630 (+4.12%) | +₹7,917 (+6.92%) | 0 | 1 | ₹15,304 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹344 (+0.96%) | +₹14,544 (+0.84%) | 4 | 1 | ₹35,704 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹4,558 (-17.18%) | +₹15,251 (+16.28%) | −₹17,960 (-10.44%) | 2 | 4 | ₹93,672 |
| **Total** | | **+₹28,501** | **+₹16,225** | **+₹6,132** | **10** | **6** | **₹1,44,680** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 12:09:14] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:11:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:11:15] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 12:12:15] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:23:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 12:23:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:21:40] API       rate limited by Dhan - now one call every 15.1 s
[12:22:00] API       rate limited by Dhan - now one call every 15.1 s
[12:22:16] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:22:20] API       rate limited by Dhan - now one call every 15.1 s
[12:22:40] API       rate limited by Dhan - now one call every 15.1 s
[12:23:01] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:21:26] API       rate limited by Dhan - now one call every 15.1 s
[12:21:42] API       rate limited by Dhan - now one call every 15.1 s
[12:21:57] API       rate limited by Dhan - now one call every 15.1 s
[12:22:27] API       rate limited by Dhan - now one call every 15.1 s
[12:22:42] API       rate limited by Dhan - now one call every 15.1 s
[12:22:58] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:20:22] SKIP      buy 2026-10-27 22000 PE ignored - premium 124.45 is outside 144 - 1600
[12:20:37] API       rate limited by Dhan - now one call every 15.1 s
[12:22:02] API       rate limited by Dhan - now one call every 15.1 s
[12:22:32] API       rate limited by Dhan - now one call every 15.1 s
[12:23:02] API       rate limited by Dhan - now one call every 15.1 s
[12:23:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 12:11:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:13:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:15:27] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:17:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:19:45] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 12:21:55] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:20:27] SIGNAL    ADANIENSOL 1400 PE 27 Oct crossed EMA 144 at 83.10 - not taken: under EMA 55
[12:20:27] SIGNAL    BANKBARODA 230 PE 27 Oct crossed EMA 144 at 4.59 - not taken: under EMA 55, momentum -0.4%, premium under Rs 5
[12:20:36] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:21:43] API       market quote: rate limited by Dhan - now one call every 9.1 s
[12:22:00] API       chart history: rate limited by Dhan - now one call every 1.2 s
[12:22:46] API       chart history: rate limited by Dhan - now one call every 1.2 s
```
</details>

