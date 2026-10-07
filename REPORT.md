# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 10:32 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.68 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | ₹0 | +₹1,362 (+3.09%) | +₹21,548 (+6.41%) | 0 | 2 | ₹44,116 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | −₹30,790 (-4.50%) | +₹72,306 (+1.54%) | 0 | 6 | ₹6,83,694 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹3,288 (-2.00%) | +₹5,090 (+3.25%) | −₹41,452 (-4.29%) | 11 | 8 | ₹1,56,730 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹16,911 (-7.68%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹3,288** | **−₹41,249** | **+₹54,497** | **11** | **24** | **₹11,04,872** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 10:22:16] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:22:16] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:28:17] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:28:17] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 10:32:18] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 10:32:18] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:27:52] API       rate limited by Dhan - now one call every 15.1 s
[10:28:12] API       rate limited by Dhan - now one call every 15.1 s
[10:29:33] API       rate limited by Dhan - now one call every 15.1 s
[10:30:55] API       rate limited by Dhan - now one call every 15.1 s
[10:31:35] API       rate limited by Dhan - now one call every 15.1 s
[10:32:16] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:28:03] API       rate limited by Dhan - now one call every 15.1 s
[10:29:02] API       rate limited by Dhan - now one call every 15.1 s
[10:30:50] API       rate limited by Dhan - now one call every 15.1 s
[10:31:21] API       rate limited by Dhan - now one call every 15.1 s
[10:31:51] API       rate limited by Dhan - now one call every 15.1 s
[10:32:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:29:27] API       rate limited by Dhan - now one call every 5.1 s
[10:29:32] API       rate limited by Dhan - now one call every 7.1 s
[10:29:53] API       rate limited by Dhan - now one call every 9.1 s
[10:31:08] API       rate limited by Dhan - now one call every 5.1 s
[10:31:13] API       rate limited by Dhan - now one call every 7.1 s
[10:32:01] API       rate limited by Dhan - now one call every 5.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 10:22:38] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:24:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:26:09] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:28:02] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:29:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 10:31:50] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:30:11] SIGNAL    HINDUNILVR 1880 PE 27 Oct crossed EMA 144 at 36.10 - not taken: under EMA 55, momentum 0.1%
[10:30:11] SIGNAL    ASIANPAINT 2360 PE 27 Oct crossed EMA 144 at 32.80 - not taken: under EMA 55, momentum -13.8%
[10:30:11] SIGNAL    HAL 4700 CE 27 Oct crossed EMA 144 at 164.05 - not taken: momentum 2.3%
[10:30:21] SKIP      ICICIBANK 1340 CE 27 Oct signal at 30.70 skipped - already 1 open on ICICIBANK
[10:30:21] SKIP      ETERNAL 330 CE 27 Oct signal at 10.65 skipped - already 1 open on ETERNAL
[10:31:11] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:29:37] API       rate limited by Dhan - now one call every 15.1 s
[10:30:07] API       rate limited by Dhan - now one call every 15.1 s
[10:30:37] API       rate limited by Dhan - now one call every 15.1 s
[10:30:52] API       rate limited by Dhan - now one call every 15.1 s
[10:31:22] API       rate limited by Dhan - now one call every 15.1 s
[10:32:21] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

