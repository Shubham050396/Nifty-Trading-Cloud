# NIFTY Cloud report

**Running until 15:15 IST** · updated 05 Oct 2026 09:38 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/37262163035)

India VIX **14.41 🔴 above the kill level** (kill above 13.50, trade only above 13.50) · Dhan token: valid until 05 Oct 23:47 IST · trading window: 09:37 → 15:15 IST (trading day)

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | 🟢 running | ₹0 | ₹0 | +₹3,266 (+0.59%) | 0 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | 🟢 running | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | 🟢 running | ₹0 | ₹0 | +₹20,420 (+9.20%) | 0 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | 🟢 running | ₹0 | +₹16,208 (+2.86%) | +₹36,439 (+1.71%) | 0 | 5 | ₹5,65,859 |
| ⚡ NIFTY Scalper - IVX-G | 🟢 running | ₹0 | ₹0 | +₹62 (+0.71%) | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | 🟢 running | ₹0 | −₹4,138 (-4.41%) | −₹89 (-0.03%) | 0 | 5 | ₹93,802 |
| 🌊 NIFTY VIX Fix - Monthly 1000s | 🟢 running | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| **Total** | | **₹0** | **+₹12,070** | **+₹58,463** | **0** | **10** | **₹6,59,661** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
serving NIFTY Credit Spreads on http://127.0.0.1:47929
[2026-10-05 09:37:56] API_ERROR marketfeed/ltp: HTTP 429 rate limited
[2026-10-05 09:37:56] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-10-05 09:37:57] BOOT      scrip master downloaded: 4120 NIFTY contracts in 5.9s
[2026-10-05 09:37:57] BOOT      Ready - 18 expiries, 4120 NIFTY contracts
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/status HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[09:37:52] CONTROL   started automatically on launch
[09:37:52] DAY       new session 2026-10-05
[09:37:52] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[09:37:53] API       rate limited by Dhan - now one call every 5.1 s
[09:37:56] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[09:37:54] GAP       2026-10-06 21400 CE: no prices for 5423 min - bar history restarts
[09:37:54] GAP       2026-10-06 21400 PE: no prices for 5423 min - bar history restarts
[09:37:57] BOOT      ready - 18 expiries, 4120 contracts in the scrip master
[09:37:57] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.) - using the widest target -> target 1400 ticks (Rs 70.00)
[09:37:57] CONTRACT  2026-10-13: watching ATM 22600 +/- 10 strikes (CE/PE)
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[09:37:53] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.) - no new entries until it loads - entries blocked (above 15)
[09:37:54] API       rate limited by Dhan - now one call every 5.1 s
[09:37:57] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[09:37:57] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.) - no new entries until it loads - entries blocked (above 15)
[09:37:59] CONTRACT  2026-11-23: watching ATM 23000 +/- 1 strikes of 1000 (CE/PE)
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
[2026-10-05 09:37:55] DAY       new session 2026-10-05 - counters reset (kill switch is NOT cleared)
[2026-10-05 09:37:55] DATA      buffer cleared: day roll
[2026-10-05 09:37:55] RUN       scalper armed - started automatically on launch
[2026-10-05 09:37:57] BOOT      scrip master: 4120 NIFTY contracts
[2026-10-05 09:37:57] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[09:37:57] BOOT      scrip master downloaded in 6s: 213 stocks with options
[09:37:57] BOOT      99 of 100 listed stocks have options - skipped: LTIM
[09:37:57] CONTROL   started automatically on launch - 99 stocks
[09:37:58] API       market quote: rate limited by Dhan - now one call every 2.0 s
[09:38:00] API       market quote: rate limited by Dhan - now one call every 3.0 s
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/state HTTP/1.1" 200 -
```
</details>

<details><summary>NIFTY VIX Fix - Monthly 1000s - last log lines</summary>

```text
[09:37:53] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.)
[09:37:54] API       rate limited by Dhan - now one call every 5.1 s
[09:37:57] BOOT      ready - 14 monthly expiries, 4120 contracts in the scrip master
[09:37:57] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.)
[09:37:59] API       rate limited by Dhan - now one call every 7.1 s
127.0.0.1 - - [05/Oct/2026 04:08:00] "GET /api/state HTTP/1.1" 200 -
```
</details>

