# NIFTY Cloud report

**Finished for the day at 15:33 IST** · updated 30 Sep 2026 15:33 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36699489409)

India VIX **13.41** (limit 13.50) · Dhan token: valid until 30 Sep 22:41 IST · trading window: 15:28 → 15:33 IST (check run (after the trading day))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | +₹3,010 (+1.00%) | ₹0 (+0.00%) | +₹3,010 (+1.00%) | 5 | 4 | ₹2,50,617 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | −₹1,635 (-0.91%) | ₹0 | −₹1,635 (-0.91%) | 4 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | +₹7,917 (+6.92%) | ₹0 | +₹7,917 (+6.92%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | −₹18,258 (-1.36%) | +₹20,875 (+5.41%) | −₹18,258 (-1.36%) | 14 | 4 | ₹3,85,742 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | ₹0 | ₹0 | ₹0 | 0 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | −₹13,402 (-9.21%) | +₹3,294 (+3.58%) | −₹13,402 (-9.21%) | 7 | 5 | ₹92,130 |
| **Total** | | **−₹22,368** | **+₹24,169** | **−₹22,368** | **36** | **13** | **₹7,28,489** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-09-30 15:28:30] VIX       India VIX unavailable (rate limited by Dhan) - no new trades until it can be read
[2026-09-30 15:28:31] BOOT      Ready - 18 expiries, 4036 NIFTY contracts
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/status HTTP/1.1" 200 -
[2026-09-30 15:29:34] DEPLOY    auto-deployed 4 spread(s)
[2026-09-30 15:30:09] MARKET    heartbeat: after close; token expires in 7h 11m
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
[15:28:30] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/state HTTP/1.1" 200 -
[15:29:27] VIX       India VIX unavailable (HTTP 429) - no new spreads until it can be read
[15:29:28] API       rate limited by Dhan - now one call every 5.1 s
[15:29:48] API       rate limited by Dhan - now one call every 7.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
[15:28:55] API       rate limited by Dhan - now one call every 11.1 s
[15:29:06] API       rate limited by Dhan - now one call every 15.1 s
[15:29:21] API       rate limited by Dhan - now one call every 15.1 s
[15:29:52] API       rate limited by Dhan - now one call every 15.1 s
[15:30:07] API       rate limited by Dhan - now one call every 15.1 s
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
[15:28:28] VIX       India VIX unavailable (Too many requests on server from single user breaching rate limits. Try throttling API calls.) - no new entries until it loads - entries blocked (above 15)
[15:28:28] CONTRACT  2026-10-27: watching ATM 23000 +/- 3 strikes of 1000 (CE/PE)
[15:28:31] BOOT      ready - 14 monthly expiries, 4036 contracts in the scrip master
[15:28:31] VIX       India VIX prev close 13.41 - entries allowed
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
serving NIFTY Scalper - IVX-G on http://127.0.0.1:49191
[2026-09-30 15:28:29] RUN       scalper armed - started automatically on launch
[2026-09-30 15:28:30] BOOT      scrip master: 4036 NIFTY contracts
[2026-09-30 15:28:30] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [30/Sep/2026 09:58:35] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[15:29:31] API       market quote: rate limited by Dhan - now one call every 2.0 s
[15:30:01] EXIT      SELL TVSMOTOR 4200 CE 27 Oct EMA_STOP @ 96.55  -20.4%  P&L Rs -4331.25
[15:30:01] SIGNAL    ADANIPORTS 1800 CE 27 Oct crossed EMA 144 at 34.45 - not taken: momentum -5.6%
[15:30:01] SIGNAL    GAIL 170 PE 27 Oct crossed EMA 144 at 2.74 - not taken: momentum -4.9%, premium under Rs 5
[15:30:03] ENTRY     BUY DLF 670 CE 27 Oct x950 @ 19.10 (signal close 19.30, EMA 144 19.04, momentum 13.5%)  quick 21.96 till 16:00, target 32.47, stop below EMA 55
cloud: shutdown requested - saving state
```
</details>

