# NIFTY Cloud report

**Finished for the day at 21:16 IST** · updated 01 Oct 2026 21:16 IST · [this run](https://github.com/Shubham050396/Nifty-Trading-Cloud/actions/runs/36886226484)

India VIX **14.46 🔴 above the limit** (limit 13.50) · Dhan token: valid until 02 Oct 20:36 IST · trading window: 21:11 → 21:16 IST (check run (after the trading day))

| Strategy | State | P&L today | Open P&L | All-time P&L | Trades today | Open | Margin blocked |
|---|---|--:|--:|--:|--:|--:|--:|
| ⚖️ NIFTY Credit Spreads | ✅ saved | +₹257 (+0.10%) | ₹0 | +₹3,266 (+0.59%) | 4 | 0 | ₹0 |
| 🛡️ NIFTY EMA Breakout Hedge | ✅ saved | ₹0 | ₹0 | −₹1,635 (-0.91%) | 0 | 0 | ₹0 |
| 🎯 NIFTY 2-Level Cross | ✅ saved | +₹12,503 (+11.62%) | ₹0 | +₹20,420 (+9.20%) | 6 | 0 | ₹0 |
| 📈 NIFTY MACD - Monthly 1000s | ✅ saved | +₹54,698 (+6.98%) | +₹16,208 (+2.82%) | +₹36,439 (+1.71%) | 8 | 5 | ₹5,74,142 |
| ⚡ NIFTY Scalper - IVX-G | ✅ saved | +₹62 (+0.71%) | ₹0 | +₹62 (+0.71%) | 1 | 0 | ₹0 |
| 📊 Stock Options EMA Cross | ✅ saved | +₹13,314 (+6.46%) | −₹4,138 (-4.41%) | −₹89 (-0.03%) | 10 | 5 | ₹93,802 |
| **Total** | | **+₹80,834** | **+₹12,070** | **+₹58,463** | **29** | **10** | **₹6,67,944** |

Paper trading only. Margin figures are estimates, as in the desktop app. Trades and state for each strategy are in the [state](state) folder.

<details><summary>NIFTY Credit Spreads - last log lines</summary>

```text
[2026-10-01 21:11:50] BOOT      scrip master downloaded: 4064 NIFTY contracts in 4.0s
[2026-10-01 21:11:50] BOOT      Ready - 18 expiries, 4064 NIFTY contracts
[2026-10-01 21:11:51] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new trades, closing every open spread
127.0.0.1 - - [01/Oct/2026 15:41:55] "GET /api/status HTTP/1.1" 200 -
[2026-10-01 21:11:56] MARKET    heartbeat: after close; token expires in 23h 24m
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY EMA Breakout Hedge - last log lines</summary>

```text
serving NIFTY EMA Breakout Hedge on http://127.0.0.1:33437
[21:11:47] CONTROL   started automatically on launch
[21:11:47] VIX       India VIX 14.46 crossed ABOVE the 13.50 limit - KILL SWITCH ON: no new spreads, closing every open one
[21:11:51] BOOT      ready - 18 expiries listed, NIFTY lot 65
127.0.0.1 - - [01/Oct/2026 15:41:55] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY 2-Level Cross - last log lines</summary>

```text
serving NIFTY 2-Level Cross on http://127.0.0.1:59875
[21:11:48] CONTROL   started automatically on launch
[21:11:51] BOOT      ready - 18 expiries, 4064 contracts in the scrip master
[21:11:51] VIX       India VIX prev close 13.49 -> target 1000 ticks (Rs 50.00)
127.0.0.1 - - [01/Oct/2026 15:41:55] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY MACD - Monthly 1000s - last log lines</summary>

```text
serving NIFTY MACD - Monthly 1000s on http://127.0.0.1:34743
[21:11:48] CONTROL   started automatically on launch
[21:11:51] BOOT      ready - 14 monthly expiries, 4064 contracts in the scrip master
[21:11:51] VIX       India VIX prev close 13.49 - entries allowed
127.0.0.1 - - [01/Oct/2026 15:41:55] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>NIFTY Scalper - IVX-G - last log lines</summary>

```text
serving NIFTY Scalper - IVX-G on http://127.0.0.1:36009
[2026-10-01 21:11:50] RUN       scalper armed - started automatically on launch
[2026-10-01 21:11:50] BOOT      scrip master: 4064 NIFTY contracts
[2026-10-01 21:11:51] BOOT      Ready - lot 65, 18 expiries, trading 2026-10-06
127.0.0.1 - - [01/Oct/2026 15:41:55] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

<details><summary>Stock Options EMA Cross - last log lines</summary>

```text
[21:11:51] WARM      bar history loaded for all 5 contracts
[21:11:51] CONTROL   started automatically on launch - 99 stocks
[21:11:51] API       market quote: rate limited by Dhan - now one call every 2.0 s
[21:11:51] API       share prices unavailable: HTTP 429
127.0.0.1 - - [01/Oct/2026 15:41:55] "GET /api/state HTTP/1.1" 200 -
cloud: shutdown requested - saving state
```
</details>

