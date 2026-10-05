# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 10:23 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.60 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | +₹1,547 (+4.03%) | +₹20,420 (+9.20%) | 0 | 2 | ₹38,418 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹43,986 (+7.78%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,65,115 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹635 (-1.14%) | −₹6,242 (-4.79%) | −₹724 (-0.18%) | 3 | 7 | ₹1,30,299 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹377 (-3.33%) | ₹0 | 0 | 3 | ₹11,313 |
| **Total** | | **−₹635** | **+₹38,914** | **+₹57,828** | **3** | **17** | **₹7,45,145** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-05 10:12:05] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:12:05] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:15:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:15:06] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 10:16:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 10:17:06] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[10:18:19] API       rate limited by Dhan - now one call every 15.1 s
[10:19:40] API       rate limited by Dhan - now one call every 15.1 s
[10:20:00] API       rate limited by Dhan - now one call every 15.1 s
[10:21:22] API       rate limited by Dhan - now one call every 15.1 s
[10:22:11] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[10:22:43] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[10:17:53] API       rate limited by Dhan - now one call every 15.1 s
[10:18:38] API       rate limited by Dhan - now one call every 15.1 s
[10:19:36] API       rate limited by Dhan - now one call every 15.1 s
[10:21:13] API       rate limited by Dhan - now one call every 15.1 s
[10:21:43] API       rate limited by Dhan - now one call every 15.1 s
[10:22:28] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[10:18:56] API       rate limited by Dhan - now one call every 15.1 s
[10:19:41] API       rate limited by Dhan - now one call every 15.1 s
[10:20:39] SIGNAL    2026-10-27 24000 CE MACD crossed DOWN (bar close 16.25, hist +0.01 -> -0.03)
[10:20:39] SKIP      short 2026-10-27 24000 CE ignored - premium 16.25 is outside 144 - 1600
[10:20:53] API       rate limited by Dhan - now one call every 15.1 s
[10:22:42] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 10:16:21] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:17:33] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:17:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:19:53] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:21:48] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-05 10:22:26] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[10:21:20] WARM      bar history loaded for all 713 contracts
[10:21:37] WARM      bar history loaded for all 713 contracts
[10:22:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
[10:22:39] WARM      bar history loaded for all 715 contracts
[10:22:54] WARM      bar history loaded for all 717 contracts
[10:23:08] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[10:19:55] API       rate limited by Dhan - now one call every 15.1 s
[10:20:25] API       rate limited by Dhan - now one call every 15.1 s
[10:20:40] API       rate limited by Dhan - now one call every 15.1 s
[10:21:25] API       rate limited by Dhan - now one call every 15.1 s
[10:21:40] API       rate limited by Dhan - now one call every 15.1 s
[10:22:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

