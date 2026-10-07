# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 13:08 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.84 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹4,618 (-5.64%) | +₹3,240 (+7.16%) | +₹16,929 (+4.05%) | 4 | 2 | ₹45,250 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹49,865 (-3.38%) | +₹25,899 (+2.62%) | +₹22,441 (+0.36%) | 16 | 10 | ₹9,88,952 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹5,345 (-2.00%) | +₹6,906 (+3.37%) | −₹43,510 (-4.07%) | 17 | 10 | ₹2,05,001 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹22,556 (-9.74%) | ₹0 | 0 | 8 | ₹2,31,472 |
| **Total** | | **−₹59,828** | **+₹13,489** | **−₹2,045** | **37** | **30** | **₹14,70,675** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:40:45] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:04:50] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:04:50] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:06:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 13:06:51] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 13:07:51] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:04:07] API       rate limited by Dhan - now one call every 15.1 s
[13:04:45] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:05:29] API       rate limited by Dhan - now one call every 15.1 s
[13:06:46] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:06:50] API       rate limited by Dhan - now one call every 15.1 s
[13:08:11] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:04:09] API       rate limited by Dhan - now one call every 15.1 s
[13:05:07] API       rate limited by Dhan - now one call every 15.1 s
[13:06:31] SKIP      L3 2026-10-27 22800 PE cross ignored - daily cap
[13:07:18] API       rate limited by Dhan - now one call every 15.1 s
[13:07:48] API       rate limited by Dhan - now one call every 15.1 s
[13:08:18] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:00:17] API       rate limited by Dhan - now one call every 15.1 s
[13:01:29] API       rate limited by Dhan - now one call every 15.1 s
[13:02:40] API       rate limited by Dhan - now one call every 15.1 s
[13:03:27] VIX       India VIX prev close 13.61 - entries allowed
[13:06:12] API       rate limited by Dhan - now one call every 8.1 s
[13:07:05] API       rate limited by Dhan - now one call every 6.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 12:54:12] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:55:58] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:57:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:59:37] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:01:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 13:02:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:05:04] SKIP      ITC 267.5 PE 27 Oct signal at 6.30 skipped - 20 trades already today
[13:05:18] WARM      bar history loaded for all 788 contracts
[13:05:45] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:05:51] API       market quote: rate limited by Dhan - now one call every 2.0 s
[13:07:57] WARM      bar history loaded for all 788 contracts
[13:08:01] WARM      bar history loaded for all 788 contracts
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[13:02:11] VIX       India VIX prev close 13.61
[13:04:50] API       rate limited by Dhan - now one call every 13.1 s
[13:05:04] SIGNAL    2026-10-27 22000 CE VIX Fix crossed above 10.00 (9.10 -> 10.57, bar close 745.00)
[13:05:04] SKIP      buy 2026-10-27 22000 CE ignored - Rs 97,786 in this strike already and this buy needs Rs 48,191 - over the Rs 100,000 limit
[13:06:33] API       rate limited by Dhan - now one call every 15.1 s
[13:07:31] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

