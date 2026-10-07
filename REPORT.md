# NIFTY Cloud report

**Running until 14:55 IST** · updated 07 Oct 2026 12:08 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37567149099)

India VIX **13.71 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 07 Oct 21:50 IST · trading window: 09:01 → 14:55 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running ⚠️ cloud/config.json was refused: {"error":"No longer listed (expired?): 2026-10-06. Untick it."}
 | −₹1,268 (-6.00%) | +₹2,239 (+3.69%) | +₹20,280 (+5.68%) | 1 | 3 | ₹60,710 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | −₹33,234 (-4.85%) | +₹5,376 (+0.69%) | +₹39,072 (+0.73%) | 6 | 10 | ₹7,76,794 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹464 (+1.59%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | −₹14,892 (-5.87%) | +₹12,690 (+7.00%) | −₹53,058 (-5.02%) | 16 | 9 | ₹1,81,254 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | −₹15,488 (-7.01%) | ₹0 | 0 | 8 | ₹2,21,096 |
| **Total** | | **−₹49,394** | **+₹4,817** | **+₹8,389** | **23** | **30** | **₹12,39,854** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-07 12:02:37] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:02:37] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:04:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:04:38] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-07 12:06:38] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-07 12:06:38] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[12:05:09] API       rate limited by Dhan - now one call every 15.1 s
[12:05:49] API       rate limited by Dhan - now one call every 15.1 s
[12:06:50] API       rate limited by Dhan - now one call every 15.1 s
[12:07:05] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[12:07:10] API       rate limited by Dhan - now one call every 15.1 s
[12:07:51] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[12:04:33] API       rate limited by Dhan - now one call every 15.1 s
[12:05:04] API       rate limited by Dhan - now one call every 15.1 s
[12:06:02] API       rate limited by Dhan - now one call every 15.1 s
[12:06:32] API       rate limited by Dhan - now one call every 15.1 s
[12:07:02] API       rate limited by Dhan - now one call every 15.1 s
[12:08:00] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[12:02:33] API       rate limited by Dhan - now one call every 15.1 s
[12:03:19] VIX       India VIX prev close 13.61 - entries allowed
[12:05:39] API       rate limited by Dhan - now one call every 12.1 s
[12:06:25] API       rate limited by Dhan - now one call every 15.1 s
[12:07:09] API       rate limited by Dhan - now one call every 15.1 s
[12:07:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-07 11:57:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 11:58:56] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:00:54] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:02:31] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:04:42] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-07 12:06:28] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[12:05:22] SIGNAL    INDIGO 5100 CE 27 Oct crossed EMA 144 at 96.50 - not taken: momentum -5.0%
[12:05:22] EXIT      SELL LODHA 1120 PE 27 Oct EMA_STOP @ 33.75  -6.8%  P&L Rs -1531.25
[12:05:22] SIGNAL    MOTHERSON 155 PE 27 Oct crossed EMA 144 at 2.49 - not taken: under EMA 55, premium under Rs 5
[12:05:22] SIGNAL    CANBK 120 PE 27 Oct crossed EMA 144 at 3.07 - not taken: under EMA 55, momentum -2.5%, premium under Rs 5
[12:05:22] SIGNAL    SBILIFE 1760 PE 27 Oct crossed EMA 144 at 56.00 - not taken: under EMA 55
[12:06:50] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[12:03:12] API       rate limited by Dhan - now one call every 15.1 s
[12:04:23] API       rate limited by Dhan - now one call every 15.1 s
[12:05:22] API       rate limited by Dhan - now one call every 15.1 s
[12:06:07] API       rate limited by Dhan - now one call every 15.1 s
[12:07:18] API       rate limited by Dhan - now one call every 15.1 s
[12:07:34] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

