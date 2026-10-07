# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:47 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.79 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | −₹1,037 (-4.51%) | +₹20,280 (+5.68%) | 1 | 1 | ₹22,987 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹21,850 (-3.20%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,82,768 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | +₹1,990 (+1.18%) | −₹45,941 (-4.70%) | 12 | 8 | ₹1,68,286 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹19,059 (-8.65%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹9,044** | **−₹39,956** | **+₹48,740** | **13** | **23** | **₹10,94,373** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:32:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:32:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:35:19] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:35:19] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:39:20] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:39:20] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:43:07] API       rate limited by Dhan - now one call every 15.1 s
[10:44:28] API       rate limited by Dhan - now one call every 15.1 s
[10:45:09] API       rate limited by Dhan - now one call every 15.1 s
[10:45:50] API       rate limited by Dhan - now one call every 15.1 s
[10:46:31] API       rate limited by Dhan - now one call every 15.1 s
[10:47:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:42:13] API       rate limited by Dhan - now one call every 15.1 s
[10:42:43] API       rate limited by Dhan - now one call every 15.1 s
[10:44:07] API       rate limited by Dhan - now one call every 15.1 s
[10:44:38] API       rate limited by Dhan - now one call every 15.1 s
[10:46:27] API       rate limited by Dhan - now one call every 15.1 s
[10:47:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:44:46] API       rate limited by Dhan - now one call every 5.1 s
[10:45:45] API       rate limited by Dhan - now one call every 5.1 s
[10:46:10] API       rate limited by Dhan - now one call every 5.1 s
[10:46:32] API       rate limited by Dhan - now one call every 5.1 s
[10:46:57] API       rate limited by Dhan - now one call every 5.1 s
[10:47:02] API       rate limited by Dhan - now one call every 7.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:37:16] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:39:43] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:42:07] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:43:49] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:44:44] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:46:29] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:45:40] SIGNAL    HINDUNILVR 1860 PE 27 Oct crossed EMA 144 at 29.45 - not taken: under EMA 55
[10:46:21] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:46:32] WARM      bar history loaded for all 780 contracts
[10:46:50] WARM      bar history loaded for all 780 contracts
[10:47:13] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:47:22] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:45:04] SKIP      buy 2026-10-27 22000 CE ignored - Rs 97,786 in this strike already and this buy needs Rs 50,944 - over the Rs 100,000 limit
[10:45:18] API       rate limited by Dhan - now one call every 15.1 s
[10:46:03] API       rate limited by Dhan - now one call every 15.1 s
[10:46:18] API       rate limited by Dhan - now one call every 15.1 s
[10:46:48] API       rate limited by Dhan - now one call every 15.1 s
[10:47:04] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

