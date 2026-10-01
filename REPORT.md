# NIFTY Cloud report

**Running until 15:15 IST** · updated 01 Oct 2026 13:48 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36825351828)

India VIX **15.20 🔴 above the limit** (limit 13.50) · Dhan token: valid until 01 Oct 20:21 IST · trading window: 12:02 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | +₹9,253 (+10.10%) | ₹0 (+0.00%) | +₹17,170 (+8.34%) | 5 | 1 | ₹15,993 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | +₹32,802 (+8.54%) | +₹35,802 (+8.74%) | +₹14,544 (+0.84%) | 4 | 4 | ₹4,09,491 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | +₹9,914 (+5.23%) | +₹3,865 (+4.20%) | −₹3,489 (-1.04%) | 9 | 5 | ₹91,942 |
| **Total** | | **+₹52,288** | **+₹39,667** | **+₹29,918** | **23** | **10** | **₹5,17,426** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 13:40:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:41:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:42:34] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:44:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-01 13:44:35] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-01 13:45:35] API_ERROR marketfeed/ltp: HTTP 429 rate limited
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[13:44:18] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:44:39] API       rate limited by Dhan - now one call every 15.1 s
[13:46:19] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[13:47:22] API       rate limited by Dhan - now one call every 15.1 s
[13:48:23] API       rate limited by Dhan - now one call every 15.1 s
[13:48:43] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[13:46:25] API       rate limited by Dhan - now one call every 15.1 s
[13:46:40] API       rate limited by Dhan - now one call every 15.1 s
[13:46:55] API       rate limited by Dhan - now one call every 15.1 s
[13:47:26] API       rate limited by Dhan - now one call every 15.1 s
[13:47:41] API       rate limited by Dhan - now one call every 15.1 s
[13:48:25] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[13:42:58] API       rate limited by Dhan - now one call every 7.1 s
[13:43:05] API       rate limited by Dhan - now one call every 11.1 s
[13:43:15] HISTORY   2026-10-27 20000 PE: could not load candles (Too many requests on server from single user breaching rate limits. Try throttling API calls. - building bars from live prices). Bars are built from live prices instead; the MACD needs 75 of them. Retried every 10 min.
[13:43:37] API       rate limited by Dhan - now one call every 15.1 s
[13:45:38] API       rate limited by Dhan - now one call every 15.1 s
[13:46:50] API       rate limited by Dhan - now one call every 15.1 s
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-01 13:19:59] EXIT      SIGNAL_DECAY 22350 65 PUT @ 135.00  gross +136  net +61  (1.8)
[2026-10-01 13:42:51] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:44:11] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:45:19] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:46:18] DATA      buffer gap > 15s - cleared, re-warming
[2026-10-01 13:47:59] DATA      buffer gap > 15s - cleared, re-warming
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[13:45:24] WARM      bar history loaded for all 1580 contracts
[13:45:53] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:48:03] WARM      bar history loaded for all 1580 contracts
[13:48:06] API       market quote: rate limited by Dhan - now one call every 8.1 s
[13:48:30] API       market quote: rate limited by Dhan - now one call every 9.1 s
[13:48:39] API       market quote: rate limited by Dhan - now one call every 9.1 s
```
</details>

