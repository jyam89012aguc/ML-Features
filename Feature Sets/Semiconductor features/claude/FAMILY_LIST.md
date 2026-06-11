# Semiconductor Feature Families (claude regen)

## Retired Families

The following families were removed because no usable data source exists in `trading.duckdb` and they cannot be salvaged with available feeds:
- f21_semi_short_interest_dynamics — needs `short_interest` (not in DB; would require FINRA biweekly data feed).
- f22_semi_borrow_cost_signal — needs `borrow_fee` (expensive IBKR/S3 feed, not subscribed).
- f100_semi_export_control_overhang — needs `export_control_index` (no clean signal source).

Active family count: **97** (originally 100).

Layout: flat `f##_<name>\` folders at this directory's root. Each folder contains:
- `f##_<name>_base_001_075_claude.py` — 75 base features
- `f##_<name>_base_076_150_claude.py` — 75 base features
- `f##_<name>_2nd_derivatives_001_150_claude.py` — 150 slope features
- `f##_<name>_3rd_derivatives_001_150_claude.py` — 150 curvature features

Style matches `D:\active_non audited features per AI\Feature Family 1 long (50 Features)\claude` reference:
casual Python, helpers (_z, _mean, _std, _safe_div, _slope_diff_norm), domain primitives, one `def` per feature, return `.replace([np.inf,-np.inf], np.nan)`.

## Families

### Price / peer / market action (1-15)
- f01_semi_peer_relative_strength
- f02_semi_basket_beta
- f03_semi_basket_correlation
- f04_semi_sector_rotation
- f05_semi_peak_drawdown
- f06_semi_volatility_regime
- f07_semi_dispersion
- f08_semi_intra_peer_lead_lag
- f09_semi_breadth
- f10_semi_momentum_persistence
- f11_semi_acceleration
- f12_semi_overnight_gap
- f13_semi_intraday_range_dynamics
- f14_semi_idiosyncratic_volatility
- f15_semi_correlation_breakdown

### Volume / liquidity (16-20)
- f16_semi_volume_surge
- f17_semi_dollar_volume_dynamics
- f18_semi_amihud_illiquidity
- f19_semi_turnover_regime
- f20_semi_volume_price_divergence

### Capex cycle (23-32)
- f23_semi_capex_intensity
- f24_semi_capex_yoy_growth
- f25_semi_capex_acceleration
- f26_semi_capex_to_depreciation
- f27_semi_capex_to_revenue_cycle
- f28_semi_capex_drawdown
- f29_semi_capex_peer_relative
- f30_semi_capex_lead_revenue
- f31_semi_capex_ppe_efficiency
- f32_semi_capex_surprise

### Inventory cycle (33-40)
- f33_semi_inventory_days
- f34_semi_inventory_growth_vs_revenue
- f35_semi_inventory_burn
- f36_semi_dio_trend
- f37_semi_inventory_to_assets
- f38_semi_inventory_acceleration
- f39_semi_dso_dynamics
- f40_semi_cash_conv_cycle

### ASP / gross margin (41-46)
- f41_semi_asp_proxy_revenue_per_unit
- f42_semi_gross_margin_level
- f43_semi_gross_margin_trajectory
- f44_semi_gross_margin_volatility
- f45_semi_gross_margin_acceleration
- f46_semi_pricing_power_signal

### Operating efficiency / mix (47-54)
- f47_semi_operating_margin_level
- f48_semi_operating_margin_trajectory
- f49_semi_operating_leverage
- f50_semi_opex_intensity
- f51_semi_sga_to_revenue
- f52_semi_fixed_cost_absorption
- f53_semi_revenue_per_employee
- f54_semi_unit_economics_composite

### R&D / process tech (55-61)
- f55_semi_rd_intensity
- f56_semi_rd_growth_streak
- f57_semi_rd_cycle_resilience
- f58_semi_rd_capex_mix
- f59_semi_rd_acceleration
- f60_semi_rd_per_share
- f61_semi_rd_to_gross_profit

### Cash flow & quality (62-70)
- f62_semi_fcf_margin
- f63_semi_fcf_acceleration
- f64_semi_cash_conv_quality
- f65_semi_ocf_capex
- f66_semi_fcf_yield
- f67_semi_sbc_burden
- f68_semi_wc_intensity
- f69_semi_cash_to_mcap
- f70_semi_earnings_quality_accruals

### Balance sheet (71-78)
- f71_semi_net_debt_ebitda
- f72_semi_debt_trajectory
- f73_semi_goodwill_share
- f74_semi_intangibles_to_equity
- f75_semi_asset_turnover_trend
- f76_semi_quick_ratio
- f77_semi_current_ratio_dynamics
- f78_semi_liquidity_buffer

### Valuation (79-87)
- f79_semi_pe_5y_band
- f80_semi_ev_ebitda_z
- f81_semi_ev_sales_cycle
- f82_semi_pb_5y_range
- f83_semi_pfcf_cohort
- f84_semi_ey_spread
- f85_semi_fwd_pe_reset
- f86_semi_ev_to_capex
- f87_semi_valuation_drawdown

### Cycle / orders (88-92)
- f88_semi_book_to_bill_proxy
- f89_semi_order_growth_signal
- f90_semi_revenue_cycle_phase
- f91_semi_cycle_amplitude
- f92_semi_revenue_acceleration

### Domain-specific (93-99)
- f93_semi_memory_cycle_proxy
- f94_semi_wfe_demand_proxy
- f95_semi_foundry_fabless_split
- f96_semi_china_exposure_proxy
- f97_semi_ai_compute_demand_proxy
- f98_semi_hbm_advanced_packaging_signal
- f99_semi_litho_intensity
