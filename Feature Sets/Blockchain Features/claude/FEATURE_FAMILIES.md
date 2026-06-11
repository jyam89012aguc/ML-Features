# Blockchain-Equity Feature Families (claude)

Asset class: US equities, **blockchain/crypto-exposed universe** (bitcoin miners,
crypto exchanges, bitcoin-treasury companies, mining-hardware makers — e.g. MARA,
RIOT, COIN, MSTR, CLSK, HUT, BITF, CIFR, WULF, HIVE, IREN, BTDR, CORZ, GLXY, CAN).

Data source: `C:\Users\remoteuser\Downloads\trading.duckdb`
  - main.sep_validated         (split-adj OHLCV: open, high, low, close, closeadj, closeunadj, volume)
  - main.fundamentals_validated(Sharadar SF1: revenue, netinc, fcf, equity, debt, assets, ebitda,
                                capex, sharesbas, eps, ncfo, ncfi, ncff, gp, opinc, grossmargin,
                                ppnenet, cashneq, currentratio, de, sbcomp, workingcapital, ...)
  - main.metrics               (beta1y, beta5y, marketcap proxy via fundamentals; ev, evebit, evebitda, pe, pb, ps)
  - main.sf3a / main.sf3b       (institutional ownership: shrvalue, shrunits, totalvalue, percentoftotal, investorname)

Target: 10x stocks over 5-year holds, all market caps. Each family = 450 features
(75 + 75 base, 150 slope (1st math derivative), 150 jerk (2nd math derivative)).

Input assignment (HARD):
  - f01-f15 : OHLCV-derived  -> {open, high, low, close, closeadj, volume}
  - f16-f25 : >=1 fundamental column per feature
  - f26-f30 : >=1 ownership/metrics column per feature

## OHLCV / price-action families (f01-f15)
f01_crypto_beta_momentum          Amplified directional momentum — these names trade as leveraged BTC proxies (multi-horizon ROC, momentum quality, beta-style amplified return signatures).
f02_halving_cycle_phase           4-year-cycle positioning via long-window oscillators (252/504/1008d) mapping price to halving cadence.
f03_parabolic_blowoff_top         Vertical price acceleration / blowoff-top exhaustion (distance-above-MA stretch, convexity of ascent, climax detection).
f04_crypto_winter_drawdown        Deep-drawdown depth, duration, underwater time, and recovery slope (crypto-winter dynamics).
f05_reflexive_volatility_regime   Realized-volatility level, regime shifts, and term structure (extreme in crypto equities).
f06_volatility_squeeze_breakout   Volatility compression (coil) then expansion (breakout) — Bollinger/Keltner squeeze logic.
f07_overnight_gap_dynamics        Open-vs-prior-close gaps to 24/7 crypto moves; gap frequency, fill, and continuation.
f08_capitulation_volume_spike     Volume capitulation/blowoff spikes; volume z-scores and surge clustering.
f09_range_expansion_atr           Parkinson / Garman-Klass intraday range estimators and range-expansion regime.
f10_relative_strength_leadership  Relative strength vs benchmark proxy & cross-sectional momentum leadership rotation.
f11_trend_persistence             Trend strength / efficiency ratio / persistence (ADX-style, Kaufman efficiency).
f12_oversold_reversion_oscillator RSI / stochastic / Williams extremes and mean-reversion from oversold.
f13_liquidity_dollar_volume       Dollar-volume liquidity, turnover, and Amihud-style illiquidity dynamics.
f14_short_squeeze_thrust          Sharp upside thrust + volume-surge squeeze signatures (heavily-shorted crypto names).
f15_accumulation_distribution_flow On-balance-volume, accumulation/distribution line, money-flow confirmation.

## Fundamental families (f16-f25, >=1 fundamental column each)
f16_bitcoin_treasury_premium      Market-cap-to-book / mNAV premium of treasury companies (equity vs marketcap stretch).
f17_share_dilution_machine        sharesbas / shareswa expansion — ATM-offering dilution that funds miners.
f18_cash_burn_runway              cashneq vs ncfo burn rate and months-of-runway.
f19_mining_capex_intensity        capex / ppnenet intensity — rig & data-center buildout cadence.
f20_operating_leverage_to_crypto  revenue / opinc / opex operating-leverage swings with crypto price.
f21_gross_margin_volatility       gp / grossmargin / cor mining-margin level and volatility (power cost vs coin price).
f22_balance_sheet_leverage        debt / equity / de / currentratio leverage and solvency stress.
f23_revenue_hypergrowth           revenue growth and acceleration (hypergrowth signature).
f24_cash_earnings_divergence      netinc vs ncfo divergence — non-cash crypto impairments & mark-to-market.
f25_dilution_adjusted_growth      per-share (revenue/sharesbas, fcf/sharesbas) growth despite dilution.

## Valuation / ownership families (f26-f30, >=1 metrics/ownership column each)
f26_ev_valuation_regime           ev / evebitda / evebit valuation regime and compression.
f27_speculative_multiple_decay    ps / pb / pe speculative-premium level and mean-reversion decay.
f28_institutional_accumulation    sf3a totalvalue / shrvalue institutional accumulation flow.
f29_ownership_concentration       sf3a percentoftotal / holder-mix concentration shifts.
f30_smart_money_positioning       sf3b investor-level shrvalue / shrunits smart-money positioning dynamics.

## Added families (f31-f37, after the real-data signal audit)
New data sources beyond OHLCV/SF1/sf3a-b.
f31_insider_buying_pressure       Insider open-market buy/sell pressure (sf2): net-buy $/mktcap, buy intensity, cluster buying.
f32_insider_conviction_quality    Quality of insider buying (sf2): officer/director vs 10%-owner, purchase size, conviction.
f33_insider_distribution_selling  Insider selling/distribution (sf2): sell intensity, option-exercise-and-dump, 10%-owner liquidation.
f34_institutional_breadth_churn   13F holder breadth (sf3 long-form): #holders growth, entry/exit churn, HHI concentration.
f35_financial_distress_score      Altman-Z distress + components (workingcapital/retearn/ebit/equity/liabilities) - miner blow-up risk.
f36_earnings_manipulation_score   Beneish M-score components (DSRI/GMI/AQI/SGI/DEPI/SGAI/LVGI/TATA) - accounting aggressiveness.
f37_crypto_sector_relative_strength  Decompose vs equal-weight crypto-equity index: beta, idiosyncratic alpha, relative strength.

Total: 37 families x 450 features = 16,650 features.
Inputs added: insider daily aggregates (sf2), holder-breadth nholders/hhi/churn (sf3),
equal-weight sector_index. f31-f33 inputs are insider series; f34 holder-breadth series;
f35/f36 fundamentals; f37 uses closeadj + sector_index.
