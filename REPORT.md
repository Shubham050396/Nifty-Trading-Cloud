# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:17 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.69 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | +₹556 (+0.92%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹878 (-0.11%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,534 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | −₹1,820 (-0.86%) | −₹45,941 (-4.70%) | 12 | 10 | ₹2,12,025 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹15,163 (-6.88%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹42,278** | **−₹17,305** | **+₹15,506** | **19** | **31** | **₹12,69,601** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 11:03:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:04:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:05:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:06:25] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:10:26] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 11:10:26] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[11:11:36] API       rate limited by Dhan - now one call every 15.1 s
[11:12:36] API       rate limited by Dhan - now one call every 15.1 s
[11:12:57] API       rate limited by Dhan - now one call every 15.1 s
[11:14:18] API       rate limited by Dhan - now one call every 15.1 s
[11:17:01] API       rate limited by Dhan - now one call every 15.1 s
[11:17:22] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:14:47] API       rate limited by Dhan - now one call every 15.1 s
[11:15:35] VIX       India VIX prev close 13.61 -> target 1000 ticks (Rs 50.00)
[11:15:46] API       rate limited by Dhan - now one call every 15.1 s
[11:16:02] API       rate limited by Dhan - now one call every 15.1 s
[11:16:46] API       rate limited by Dhan - now one call every 15.1 s
[11:17:45] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:12:09] API       rate limited by Dhan - now one call every 15.1 s
[11:14:30] API       rate limited by Dhan - now one call every 15.1 s
[11:15:41] API       rate limited by Dhan - now one call every 15.1 s
[11:15:57] API       rate limited by Dhan - now one call every 15.1 s
[11:16:12] API       rate limited by Dhan - now one call every 15.1 s
[11:17:10] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:06:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:08:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:10:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:12:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:14:41] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:17:01] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:14:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:15:22] SIGNAL    LODHA 1140 PE 27 Oct crossed EMA 144 at 44.80 - not taken: under EMA 55
[11:15:22] SIGNAL    PIDILITIND 1500 PE 27 Oct crossed EMA 144 at 30.00 - not taken: under EMA 55
[11:15:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:15:30] SKIP      DLF 650 PE 27 Oct signal at 13.50 skipped - 10 positions already open
[11:16:22] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:12:54] API       rate limited by Dhan - now one call every 15.1 s
[11:13:39] API       rate limited by Dhan - now one call every 15.1 s
[11:14:23] API       rate limited by Dhan - now one call every 15.1 s
[11:14:54] API       rate limited by Dhan - now one call every 15.1 s
[11:16:18] API       rate limited by Dhan - now one call every 15.1 s
[11:17:17] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

