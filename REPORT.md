# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 11:12 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.70 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | +₹1,144 (+1.88%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | −₹211 (-0.03%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,603 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹7,776 (-4.45%) | +₹2,454 (+1.16%) | −₹45,941 (-4.70%) | 12 | 10 | ₹2,12,025 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹14,929 (-6.78%) | ₹0 | 0 | 8 | ₹2,20,332 |
| **Total** | | **−₹42,278** | **−₹11,542** | **+₹15,506** | **19** | **31** | **₹12,69,670** |

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
[11:08:53] API       rate limited by Dhan - now one call every 15.1 s
[11:09:13] API       rate limited by Dhan - now one call every 15.1 s
[11:10:14] API       rate limited by Dhan - now one call every 15.1 s
[11:11:17] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[11:11:36] API       rate limited by Dhan - now one call every 15.1 s
[11:12:36] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[11:08:50] API       rate limited by Dhan - now one call every 15.1 s
[11:09:20] API       rate limited by Dhan - now one call every 15.1 s
[11:09:51] API       rate limited by Dhan - now one call every 15.1 s
[11:10:21] API       rate limited by Dhan - now one call every 15.1 s
[11:10:51] API       rate limited by Dhan - now one call every 15.1 s
[11:11:49] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[11:10:29] API       rate limited by Dhan - now one call every 15.1 s
[11:11:27] SIGNAL    2026-12-29 24000 CE MACD crossed UP (bar close 165.05, hist -0.15 -> +0.07)
[11:11:27] EXIT      SHORT 2026-12-29 24000 CE MACD_UP @ 163.40  P&L Rs -575.25
[11:11:27] ENTRY     BUY 2026-12-29 24000 CE @ 163.40  (bar close 165.05, MACD hist +0.07, VIX 13.61)
[11:11:53] API       rate limited by Dhan - now one call every 15.1 s
[11:12:09] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:02:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:03:55] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:06:23] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:08:04] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:10:36] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:12:38] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[11:10:18] SIGNAL    TMPV 280 PE 27 Oct crossed EMA 144 at 5.60 - not taken: under EMA 55, momentum -8.2%
[11:10:26] SKIP      DLF 660 PE 27 Oct signal at 17.00 skipped - 10 positions already open
[11:10:39] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:11:15] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:11:24] API       market quote: rate limited by Dhan - now one call every 9.1 s
[11:12:31] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[11:07:23] API       rate limited by Dhan - now one call every 15.1 s
[11:08:21] API       rate limited by Dhan - now one call every 15.1 s
[11:09:33] API       rate limited by Dhan - now one call every 15.1 s
[11:10:03] API       rate limited by Dhan - now one call every 15.1 s
[11:10:47] API       rate limited by Dhan - now one call every 15.1 s
[11:12:24] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

