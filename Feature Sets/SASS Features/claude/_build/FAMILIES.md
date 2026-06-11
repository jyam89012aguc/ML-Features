# 44 feature families — domain, short code, input columns, seed primitives

Each family is a DISTINCT economic signal. Math derivatives (accel/jerk) come from the
slope/jerk files, so there are NO standalone accel/jerk *base* families. Seed primitives are
starting ideas — expand each family to 150 base + 150 slope + 150 jerk distinct features.

## PRICE / PRICE-ACTION  (inputs: subset of open,high,low,close,closeadj,volume)
- f01_trend_structure  | short f01ts | inputs closeadj(,volume) | price vs MA(21/63/126/252), MA alignment/stacking, % above MA, MA-distance z-score, trend slope sign, price-vs-MA persistence.
- f02_momentum_rotation | short f02mr | closeadj(,volume) | ROC(5/21/63/126/252), momentum strength, 12-1 momentum, momentum rank, momentum consistency (hit-rate of up days), risk-adj momentum (ROC/vol).
- f03_trend_persistence | short f03tp | closeadj | efficiency ratio (net/sum abs moves), Hurst-like R/S, autocorrelation of returns, run-length of up/down, fraction of trend days, variance ratio.
- f04_breakout_proximity | short f04bp | high,low,close,closeadj | Donchian channel position, distance to N-day high/low, days since N-day high, new-high frequency, squeeze-then-break, range-position.
- f05_fiftytwo_week_anchor | short f05fw | closeadj,high,low | proximity to 252d/504d/1260d high & low, recovery off 252d low, drawdown from 252d high, anchoring gap, % of 52w range.
- f06_drawdown_recovery | short f06dr | closeadj | max drawdown over N, underwater duration, recovery slope from trough, time-to-recover, drawdown frequency, pain index (avg dd), Calmar-like.
- f07_gap_dynamics | short f07gd | open,high,low,close | open-vs-prior-close gap %, gap-up/down frequency, gap fill ratio, overnight vs intraday return, gap magnitude z, cumulative overnight drift. (window<=5d -> unadjusted OHLC)
- f08_candle_range_structure | short f08cr | open,high,low,close | body/range ratio, upper/lower wick ratio, close position in range, candle direction sequence, doji frequency, body z-score, range expansion vs body. (intraday, unadjusted)
- f09_volatility_term_structure | short f09vt | closeadj | realized vol(5/21/63/126/252), vol ratio short/long, vol slope, vol cone position, downside vol vs upside (semi-dev), vol-adjusted return.
- f10_range_vol_estimators | short f10rv | open,high,low,close,closeadj | Parkinson, Garman-Klass, Rogers-Satchell, Yang-Zhang-ish, ATR & ATR/price, true-range z, hi-lo range vs close. (>21d normalize by closeadj)
- f11_volatility_regime_shift | short f11vr | closeadj,high,low | vol compression/expansion ratio, Bollinger band width & squeeze, vol-of-vol, vol regime z, range contraction streak, breakout-from-squeeze flag.

## VOLUME / LIQUIDITY
- f12_volume_pressure | short f12vp | volume,closeadj | volume z-score, dollar-volume(closeadj*volume) trend, volume surge ratio, up/down volume ratio, volume trend slope, relative volume vs 63d avg.
- f13_volume_price_confirmation | short f13vc | close,closeadj,high,low,volume | OBV slope, Accumulation/Distribution line, Chaikin money flow, money-flow index, volume-price divergence (price up/vol down), force index.
- f14_liquidity_profile | short f14lq | close,closeadj,high,low,volume | Amihud illiquidity (|ret|/dollar-vol), turnover (volume/shares proxy), VWAP deviation (typical-price), dollar-liquidity level, liquidity trend, zero-volume/illiquidity streak.

## FUNDAMENTAL — LEVEL & QUALITY  (every feature uses >=1 fundamental column)
- f15_profitability_quality | short f15pq | revenue,gp,opinc,netinc,ebitda,ebit,equity,assets | gross/op/net/ebitda margin levels, ROE(netinc/equity), ROA(netinc/assets), ROIC, ROS, margin dispersion across types.
- f16_cash_generation | short f16cg | fcf,ncfo,netinc,capex,revenue,ebitda | FCF margin(fcf/revenue), OCF margin, cash conversion (ncfo/netinc), FCF/EBITDA, capex coverage (ncfo/capex), accrual-free earnings proxy.
- f17_balance_sheet_strength | short f17bs | debt,debtusd,equity,assets,liabilities,currentratio,workingcapital,cashneq | net debt/equity, debt/assets, current & quick ratio, working-capital/assets, cash/assets, equity/assets, leverage z.
- f18_interest_coverage_solvency | short f18ic | ebit,ebitda,intexp,debt,debtc,liabilities,opinc | interest coverage (ebit/intexp), ebitda/intexp, debt/ebitda, short-term debt share (debtc/debt), liabilities/ebitda, coverage cushion.
- f19_capital_efficiency | short f19ce | revenue,assets,assetsavg,invcap,invcapavg,equity,ppnenet | asset turnover (revenue/assets), invcap turnover, fixed-asset turnover (revenue/ppnenet), equity turnover, sales/invested-capital, efficiency z.
- f20_working_capital_dynamics | short f20wc | receivables,inventory,payables,revenue,cor,assetsc,liabilitiesc | DSO(receivables/revenue), DIO(inventory/cor), DPO(payables/cor), cash-conversion-cycle, working-capital intensity, receivables/revenue trend.
- f21_asset_composition | short f21ac | intangibles,tangibles,ppnenet,assets,inventory,investments | intangibles/assets, goodwill-heavy proxy, ppnenet/assets (capital intensity), tangible-book share, inventory/assets, investment-asset share.
- f22_dividend_payout_policy | short f22dp | dps,divyield,payoutratio,ncfdiv,netinc,fcf | dividend yield level, payout ratio, dividend/FCF coverage, ncfdiv/netinc, dps level, dividend sustainability (fcf - dividends).

## FUNDAMENTAL — GROWTH & TRAJECTORY  (>=1 fundamental column)
- f23_revenue_growth_engine | short f23rg | revenue,revenueusd | revenue growth(21/63/252/504d windows on the series), growth stability (std of growth), CAGR proxy, growth vs prior, sequential growth, growth rank.
- f24_margin_trajectory | short f24mt | grossmargin,netmargin,ebitdamargin,opinc,revenue,gp | margin trend (slope of margin over N), margin change vs base, margin stability, gross-vs-net margin spread trend, op-margin direction.
- f25_fcf_trajectory | short f25ft | fcf,fcfps,ncfo,revenue | FCF growth, FCF-margin trend, FCF consistency (positive streak), ncfo trend, FCF/revenue change, FCF inflection.
- f26_earnings_power_trajectory | short f26ep | netinc,eps,epsdil,netinccmn,shareswa | EPS growth, net-income growth, earnings stability, eps acceleration-as-level, diluted-vs-basic eps spread, earnings positive streak.
- f27_reinvestment_dynamics | short f27ri | capex,rnd,sbcomp,revenue,assets,ppnenet | capex/revenue, R&D intensity(rnd/revenue), R&D growth, SBC/revenue, reinvestment rate (capex+rnd)/ocf-proxy, capex/ppnenet (growth capex).
- f28_share_count_dynamics | short f28sc | sharesbas,shareswa,shareswadil,ncfcommon | share-count change (dilution/buyback), buyback intensity(-ncfcommon), diluted-share creep, share-count trend, net issuance, dilution streak.
- f29_debt_trajectory | short f29dt | debt,debtusd,debtc,debtnc,ncfdebt,cashneq | debt growth, net-debt change (debt-cashneq), deleveraging slope, ncfdebt flow, short-vs-long debt shift, debt-paydown streak.
- f30_return_on_capital_trajectory | short f30rc | roic,roe,roa,ros,invcap,netinc,equity | ROIC trend, ROE trend, ROA trend, return-on-capital improvement, ROIC stability, ROIC-minus-prior, quality-improvement slope.

## FUNDAMENTAL COMPOSITES  (alpha signatures; >=1 fundamental column)
- f31_hypergrowth_signature | short f31hg | revenue,grossmargin,gp,rnd,ncfo | revenue-growth × gross-margin-level, growth-with-expanding-margin, Rule-of-40 (growth+fcf-margin), reinvestment-funded growth, durable-growth composite.
- f32_operating_leverage | short f32ol | opinc,revenue,opex,gp,ebit | incremental margin (Δopinc/Δrevenue), opinc-growth minus revenue-growth, opex/revenue trend (scale), fixed-cost absorption, contribution-margin proxy.
- f33_quality_compounder | short f33qc | roic,fcf,sharesbas,revenue,equity,netinc | high-stable-ROIC × low-dilution, FCF-ROIC composite, reinvestment-at-high-returns, compounding score (roic×reinvestment), quality-minus-dilution.
- f34_piotroski_fscore | short f34pf | netinc,ncfo,roa,assets,debt,currentratio,sharesbas,grossmargin,assetturnover | the 9 Piotroski binaries (positive netinc, positive ncfo, ΔROA>0, ncfo>netinc, Δleverage<0, Δcurrentratio>0, no dilution, Δgrossmargin>0, Δassetturnover>0) and their rolling sums/subsets.
- f35_earnings_quality_accruals | short f35eq | netinc,ncfo,assets,receivables,revenue,workingcapital | Sloan total accruals((netinc-ncfo)/assets), accrual ratio trend, ΔWC accruals, receivables-growth vs revenue-growth, cash-earnings spread, accrual reversal.
- f36_manipulation_beneish | short f36mb | receivables,revenue,gp,assets,ppnenet,depamor,sgna,debt,netinc,ncfo | Beneish-style indices: DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA, and the composite M-score and its components.
- f37_distress_risk_altman | short f37da | workingcapital,retearn,ebit,equity,liabilities,assets,revenue,cashneq,opex | Altman-Z components & Z, cash runway (cashneq/(opex-ncfo burn)), interest-burden stress, negative-equity flag, deterioration composite.
- f38_turnaround_signature | short f38ts | netinc,grossmargin,revenue,debt,fcf,equity,ncfo | margin-inflection off low base, return-to-positive-FCF, deleveraging-with-stabilizing-revenue, loss-narrowing slope, recovery composite.

## VALUATION  (every feature uses >=1 metrics or fundamental column)
- f39_valuation_entry | short f39ve | pe,pb,ps,ev,evebit,evebitda,marketcap,fcf,netinc,revenue,equity | cheapness z-scores of pe/pb/ps/evebitda, earnings yield(netinc/marketcap), FCF yield(fcf/marketcap), EV/sales, EV/FCF, book-yield, blended-cheapness rank.
- f40_valuation_vs_growth | short f40vg | pe,evebitda,ev,ps,marketcap,revenue,fcf,netinc,ebitda | PEG(pe/growth), EV/EBITDA-to-growth, EV/Sales-to-growth, FCF-yield-plus-growth, growth-adjusted earnings yield, GARP composite. (growth computed from the fundamental series)
- f41_valuation_trajectory | short f41vj | pe,pb,ps,evebitda,ev,marketcap | multiple re-rating slope, multiple compression/expansion, valuation z vs own history, EV trend vs fundamentals, multiple mean-reversion gap, re-rating momentum.

## OWNERSHIP  (every feature uses >=1 ownership/metrics column)
- f42_institutional_ownership_flow | short f42io | shrholders,shrvalue,totalvalue,shrunits,marketcap | inst-holder-count trend, inst-value trend, ownership-value growth, value/marketcap (inst ownership %), units trend, ownership-flow momentum.  (sf3a aggregate; series named shrholders/shrvalue/totalvalue/shrunits)
- f43_ownership_concentration_breadth | short f43oc | fndholders,undholders,prfholders,dbtholders,shrholders,percentoftotal,totalvalue | holder-type mix (fund/underwriter/preferred/debt share), top-holder concentration (percentoftotal), breadth = total holders, concentration trend, smart-vs-dumb holder ratio.
- f44_smart_money_flow | short f44sm | shrholdings,shrvalue,totalvalue,shrunits | 13F position change (Δshrholdings), conviction (shrvalue/totalvalue), position-build streak, value-weighted accumulation, new-vs-exit proxy, smart-money momentum. (sf3b investor-level; series named shrholdings/shrvalue/totalvalue/shrunits)
