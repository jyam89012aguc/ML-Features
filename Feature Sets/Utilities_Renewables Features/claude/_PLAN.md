# Utilities & Renewables Features — Feature Family Plan

## Sector context
Database: `C:\Users\jyama\Desktop\silver db\trading.duckdb`
- `sep` — daily OHLCV.
- `fundamentals` — quarterly financials.
- Sector coverage:
  - `Utilities` (696 tickers): Regulated Electric (327), Regulated Gas (133), Renewable (84),
    Regulated Water (62), Diversified (56), Independent Power Producers (34).
  - Solar producers live under `Technology / Solar` (89 tickers) — these are included for
    feature design and the IC test.

## Investment thesis
Utilities/Renewables is **regime-driven**:
- Regulated utilities = steady but slow compounders (rate-base growth + allowed ROE).
- Solar / clean energy = **2020–21 spike then collapse** ("lots of zeros after") —
  growth-stock regime change.
- Grid modernization & electrification = long-cycle capex-driven secular tailwind.
- Independent power producers = merchant-power cyclical exposure.

10x setups concentrate at **regime inflections**: bottoming after collapse, electrification
wave onset, grid capex cycles, and (rarely) small-cap renewable players hitting commercial
inflection. Many features will produce strong negative IC against forward returns in the
post-2021 zeros regime — which is itself the signal.

## File structure (mirrors prior sector builds)
Per family folder `f##_<slug>/`:
1. `f##_<slug>_base_001_075_claude.py`  — 75 base features.
2. `f##_<slug>_base_076_150_claude.py`  — 75 base features.
3. `f##_<slug>_2nd_derivatives_001_150_claude.py` — 150 slope features.
4. `f##_<slug>_3rd_derivatives_001_150_claude.py` — 150 jerk features.

Total per family: 450. Grand total: 50 × 450 = **22,500 features**.

## 50 Utilities/Renewables feature families

### Regulated utilities (1–10)
- f01 regulated_rate_base_growth — asset growth as rate-base growth proxy.
- f02 allowed_roe_proxy — netinc / equity (allowed ROE realization).
- f03 utility_capex_intensity — capex / revenue (heavy capex sector).
- f04 utility_dividend_growth — dividend compounding signal.
- f05 utility_revenue_stability — regulated revenue smoothness (low CV).
- f06 utility_credit_quality — debt / ebitda + de.
- f07 utility_efficiency — opex / revenue dynamics.
- f08 utility_payout_durability — payout ratio sustainability.
- f09 utility_rate_case_signature — margin durability through rate cases.
- f10 utility_regulated_growth — long-cycle revenue compounding.

### Solar / clean energy (11–20)
- f11 solar_revenue_acceleration — revenue growth (2020-21 spike).
- f12 solar_margin_durability — gross margin (solar commoditization signal).
- f13 solar_inventory_cycle — inventory dynamics (oversupply / undersupply).
- f14 solar_capex_intensity — capex burn rate.
- f15 solar_module_pricing — revenue per asset proxy.
- f16 clean_energy_growth — revenue acceleration broad.
- f17 clean_energy_burn_rate — cash burn from negative fcf.
- f18 clean_energy_dilution — share growth as dilution proxy.
- f19 clean_energy_runway — cashneq / burn = runway months.
- f20 clean_energy_inflection — revenue inflection signal.

### Grid / electrification infrastructure (21–25)
- f21 grid_capex_cycle — capex / asset cycle.
- f22 grid_revenue_growth — revenue acceleration (grid modernization tailwind).
- f23 transmission_revenue — regulated revenue smoothness.
- f24 grid_modernization_signal — asset + capex growth tandem.
- f25 transmission_capital_efficiency — revenue / asset.

### Independent power producers / wholesale (26–30)
- f26 ipp_revenue_volatility — merchant power revenue cv.
- f27 ipp_capacity_growth — asset growth (capacity build).
- f28 power_pricing_dynamics — revenue per asset.
- f29 ipp_margin_cycle — cyclical margin signature.
- f30 wholesale_power_growth — revenue acceleration in pricing rallies.

### Regime / boom-bust (31–35)
- f31 regime_spike_signature — revenue spike + mean reversion proxy.
- f32 boom_bust_signature — growth + price drawdown pairing.
- f33 clean_energy_winter — revenue collapse signature post-2021.
- f34 regime_recovery_signal — bottoming after multi-year decline.
- f35 regulatory_subsidy_cycle — revenue tied to policy regime.

### Capital structure (36–40)
- f36 utility_leverage_cycle — debt / equity dynamics.
- f37 utility_debt_capacity — debt / ebitda coverage.
- f38 utility_capital_raise — share issuance as capital-raise proxy.
- f39 renewable_capital_intensity — capex / equity for renewables.
- f40 renewable_funding_quality — debt growth + equity growth quality.

### Returns & quality (41–45)
- f41 utility_roic_stability — ROIC compounding (rare in utilities).
- f42 utility_fcf_yield — FCF / EV.
- f43 renewable_capital_efficiency — asset turnover for renewables.
- f44 utility_earnings_quality — cash vs accrual.
- f45 utility_balance_sheet_strength — net debt position.

### Compounders & 10x setups (46–50)
- f46 quiet_utility_compounder — low vol + steady growth (utility classic).
- f47 hidden_renewable_compounder — small base + high quality.
- f48 utility_regime_bottom — bottoming signal after sell-off.
- f49 utility_terminal_compounder — aggregate quality.
- f50 renewable_idiosyncratic_alpha — composite signal.

## Parallel build plan
10 sub-agents (Batch A–J), each owns 5 families.
- A f01–f05, B f06–f10, C f11–f15, D f16–f20, E f21–f25,
- F f26–f30, G f31–f35, H f36–f40, I f41–f45, J f46–f50.

10 × 5 × 4 = **200 files**. 50 × 450 = **22,500 features**.

## DB column alignment
**Every feature input must come from these `trading.duckdb` columns** (sep + fundamentals):
`closeadj, high, low, volume, revenue, ebitda, ebit, netinc, fcf, ncfo, capex, depamor, sgna,
opex, gp, cor, rnd, assets, assetsc, assetsnc, liabilities, liabilitiesc, liabilitiesnc,
equity, equityusd, debt, debtc, debtnc, cashneq, inventory, receivables, payables,
deferredrev, workingcapital, ppnenet, intangibles, tangibles, invcap, retearn, sbcomp,
sharesbas, shareswa, shareswadil, eps, epsdil, bvps, fcfps, sps, dps, marketcap, ev, pe, pb,
ps, evebit, evebitda, grossmargin, ebitdamargin, netmargin, roa, roe, roic, ros,
currentratio, de, payoutratio, divyield, assetturnover`.

No invented column names. No `deposits` (bank-only). Solar / clean-energy renewables
typically have no `deferredrev` but use it where modeled.
