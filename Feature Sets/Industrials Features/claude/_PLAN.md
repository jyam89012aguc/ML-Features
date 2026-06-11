# Industrials Features — Feature Family Plan

## Sector context
Database: `C:\Users\jyama\Desktop\silver db\trading.duckdb`
- `sep` — daily OHLCV (closeadj/closeunadj, volume).
- `fundamentals` — quarterly + trailing financials (revenue, fcf, capex, ebitda, ppnenet, inventory,
  receivables, payables, debt, roic, roa, roe, marketcap, ev, eps, sgna, opex, gp, etc.).
- `tickers` — sector/industry mapping. `sector='Industrials'` covers Aerospace & Defense, Electrical
  Equipment & Parts, Specialty Industrial Machinery, Farm & Heavy Construction Machinery,
  Engineering & Construction, Building Products (via Conglomerates/Diversified Industrials),
  Tools & Accessories, Railroads, Trucking, etc.

## Investment thesis
Industrials are dominated by capital-intensive cyclical businesses with long-cycle backlogs,
replacement demand, and capacity dynamics. The "quiet compounders" (e.g., specialty machinery,
defense primes, aerospace suppliers, building products, electrical infrastructure) compound
earnings through pricing power, replacement cycles, and operating leverage. We design features
that capture (a) cyclical phase, (b) backlog/orderflow visibility, (c) capital allocation quality,
(d) pricing power & margin durability, (e) hidden compounder signatures, (f) distress risk.

## File structure (mirrors `Feature Family 1 long (50 Features)\claude\f01_peak_and_crash\`)
Per family folder `f##_<slug>/`:
1. `f##_<slug>_base_001_075_claude.py`  — 75 base features (v001…v075).
2. `f##_<slug>_base_076_150_claude.py`  — 75 base features (v076…v150).
3. `f##_<slug>_2nd_derivatives_001_150_claude.py` — 150 slope features (v001…v150).
4. `f##_<slug>_3rd_derivatives_001_150_claude.py` — 150 jerk features (v001…v150).

Total per family: 450 features.

## 50 Industrials feature families

### Cyclical cycle position & backlog (1–10)
- f01 industrial_cycle_phase — composite early/mid/late-cycle signal.
- f02 capex_to_depreciation_cycle — reinvestment intensity vs aging base.
- f03 backlog_implied_revenue — revenue-trajectory backlog proxy.
- f04 inventory_destock_signature — inventory days cycle.
- f05 working_capital_intensity — (inv+ar−ap)/rev dynamics.
- f06 capacity_utilization_proxy — asset-turnover near peak.
- f07 replacement_demand_aging — dep/ppe age ratio.
- f08 capex_acceleration — capex growth and inflection.
- f09 inventory_to_sales_dynamics — I/S trajectory.
- f10 receivables_quality — DSO dynamics, dso jerk.

### Defense / Aerospace (11–15)
- f11 defense_revenue_stability — multi-year low-vol revenue.
- f12 long_cycle_visibility — smoothed multi-year growth.
- f13 aerospace_oem_cycle_position — delivery-cycle inflection.
- f14 aftermarket_margin_quality — margin durability through cycle.
- f15 program_revenue_consistency — revenue smoothness.

### Electrical equipment / grid / electrification (16–20)
- f16 grid_electrification_growth — elevated multi-year revenue growth.
- f17 electrical_pricing_power — revenue per unit asset rising.
- f18 transformer_orderflow_proxy — long-cycle backlog acceleration.
- f19 electrification_capex_demand — asset growth signal.
- f20 renewable_grid_buildout_signal — revenue acceleration on small base.

### Specialty machinery & quiet compounders (21–25)
- f21 specialty_machinery_replacement — ppe rejuvenation rate.
- f22 machinery_pricing_durability — margin stability vs input.
- f23 quiet_compounder_signature — low vol + steady earnings.
- f24 steady_eddy_growth — revenue consistency.
- f25 hidden_compounder_detector — low coverage, steady fcf comp.

### Building products & construction (26–30)
- f26 building_products_housing — housing-driven dynamics.
- f27 repair_remodel_durability — non-cyclical share.
- f28 engineering_construction_backlog — project pipeline.
- f29 building_material_pricing — pricing in cost cycles.
- f30 residential_commercial_mix — segment mix proxy.

### Cash, returns, & capital efficiency (31–35)
- f31 cash_conversion_quality — OCF/EBITDA durability.
- f32 fcf_yield_durability — FCF/EV consistency.
- f33 capital_efficiency_compounding — ROIC trajectory.
- f34 roic_vs_wacc_spread_proxy — value-creation proxy.
- f35 asset_turnover_compounding — sales/asset growth.

### Margin & operating leverage (36–40)
- f36 operating_leverage_intensity — margin sensitivity to revenue.
- f37 pricing_power_industrial — price/mix vs volume.
- f38 margin_durability_input — input-cost pass-through.
- f39 margin_trough_to_peak — cyclical margin range.
- f40 fixed_cost_scaling — SG&A leverage.

### Balance sheet, capital allocation, risk (41–45)
- f41 balance_sheet_resilience_cyclical — net debt cycle position.
- f42 dividend_safety_cyclical — dividend coverage.
- f43 buyback_cycle_timing — countercyclical capital return.
- f44 cyclical_distress_signature — downturn vulnerability.
- f45 debt_funded_growth_risk — acquisition leverage.

### Earnings quality, sector relative, terminal (46–50)
- f46 industrial_earnings_quality — accrual vs cash earnings.
- f47 capex_overhang_risk — over-investment signature.
- f48 sector_relative_momentum — vs sector strength.
- f49 conglomerate_premium_discount — SOTP proxy.
- f50 industrial_terminal_compounder — aggregate quality composite.

## Parallel build plan
10 sub-agents (Batch A–J), each owns 5 families.
- Batch A (f01–f05), Batch B (f06–f10), Batch C (f11–f15), Batch D (f16–f20), Batch E (f21–f25),
- Batch F (f26–f30), Batch G (f31–f35), Batch H (f36–f40), Batch I (f41–f45), Batch J (f46–f50).

Each batch produces 5 family folders × 4 files = 20 files.
Total: 50 families × 4 files = 200 files, 50 × 450 = 22,500 features.
