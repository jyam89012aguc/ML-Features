# Healthcare Beyond Biotech Features — Feature Family Plan

## Sector context
Database: `C:\Users\jyama\Desktop\silver db\trading.duckdb`
- `sep` — daily OHLCV.
- `fundamentals` — quarterly financials.
- `tickers` — `sector='Healthcare'` covers Medical Devices (1,127), Diagnostics & Research (275),
  Health Information Services (299), Medical Instruments & Supplies (197), Drug Mfg
  Specialty/Generic (329), Medical Distribution (78), Medical Care Facilities (488),
  Healthcare Plans (91). 6,114 tickers total — but **we exclude Biotechnology (3,157 tickers)**
  to focus on revenue-generating, non-binary-FDA-event medtech/diagnostics/IT/tools/CROs.

## Investment thesis
Unlike biotech (binary FDA events), **medtech and diagnostics** produce 10x compounders via
**commercialization** — recurring razor-blade-style revenue, installed base growth, gross-margin
expansion, sales force scaling, and roll-up M&A. Healthcare IT shows SaaS-like ARR compounding.
Life science tools combine instrument placements with high-margin consumables. CROs deliver
service-margin compounders with multi-year backlog visibility.

50 families to maximize coverage across these distinct sub-themes.

## File structure (mirrors prior sector builds)
Per family folder `f##_<slug>/`:
1. `f##_<slug>_base_001_075_claude.py`  — 75 base features (v001…v075).
2. `f##_<slug>_base_076_150_claude.py`  — 75 base features (v076…v150).
3. `f##_<slug>_2nd_derivatives_001_150_claude.py` — 150 slope features.
4. `f##_<slug>_3rd_derivatives_001_150_claude.py` — 150 jerk features.

Total per family: 450. Grand total: 50 × 450 = **22,500 features**.

## 50 Healthcare-beyond-biotech feature families

### Medical devices (1–10)
- f01 device_commercialization_growth — revenue acceleration on product launch.
- f02 device_replacement_cycle — razor-blade recurring revenue smoothness.
- f03 device_margin_durability — gross-margin sustainability across cycles.
- f04 device_rd_efficiency — rnd vs revenue growth (R&D productivity).
- f05 device_sales_force_scaling — sgna vs revenue growth (sales leverage).
- f06 device_capital_efficiency — revenue per asset.
- f07 device_pricing_power — revenue per unit asset trend.
- f08 device_installed_base_growth — ppe / asset proxy for installed base.
- f09 device_inventory_management — inventory turnover dynamics.
- f10 device_distribution_quality — receivables / revenue (channel quality).

### Diagnostics (11–15)
- f11 diagnostics_recurring_revenue — revenue smoothness.
- f12 diagnostics_test_volume_growth — revenue growth signature.
- f13 diagnostics_margin_quality — margin durability.
- f14 diagnostics_capital_intensity — capex efficiency.
- f15 diagnostics_pricing_dynamics — revenue per asset.

### Healthcare IT (16–20)
- f16 healthit_subscription_growth — deferred-revenue growth.
- f17 healthit_arr_signature — recurring-revenue proxy.
- f18 healthit_customer_acquisition — sgna efficiency.
- f19 healthit_gross_margin_expansion — software-like margins.
- f20 healthit_platform_scaling — revenue / cost.

### Life science tools (21–25)
- f21 lst_consumables_recurring — high-margin consumables.
- f22 lst_instrument_placement_growth — capex placement signal.
- f23 lst_aftermarket_quality — service revenue stability.
- f24 lst_rd_investment — rnd intensity.
- f25 lst_market_share_growth — revenue compounding.

### CROs (26–30)
- f26 cro_backlog_growth — deferred revenue pipeline.
- f27 cro_book_to_bill_proxy — revenue acceleration.
- f28 cro_margin_stability — service-margin durability.
- f29 cro_client_concentration — revenue smoothness.
- f30 cro_capital_light_compounder — low capex high return.

### Revenue & growth (31–35)
- f31 healthcare_revenue_acceleration — broad medtech accel.
- f32 healthcare_pricing_power — revenue per asset.
- f33 healthcare_volume_vs_price — growth decomposition.
- f34 healthcare_international_growth — multi-region revenue compounding.
- f35 healthcare_market_share — relative growth.

### Margin & operating leverage (36–40)
- f36 healthcare_operating_leverage — margin sensitivity.
- f37 healthcare_gross_margin_quality — margin durability.
- f38 healthcare_sga_leverage — SG&A scaling.
- f39 healthcare_rd_to_growth — rnd vs revenue gap.
- f40 healthcare_margin_expansion — margin compounding.

### M&A and capital allocation (41–45)
- f41 medtech_acquisition_signature — intangibles + capex pulse.
- f42 medtech_consolidation_premium — SOTP signal.
- f43 healthcare_capex_efficiency — capex / revenue.
- f44 healthcare_capital_return — dividend + buyback consistency.
- f45 healthcare_balance_sheet_strength — net debt position.

### Compounders & quality (46–50)
- f46 quiet_medtech_compounder — low vol + steady earnings.
- f47 hidden_medtech_compounder — small base + high quality.
- f48 commercialization_compounder — revenue + margin trajectory.
- f49 healthcare_terminal_compounder — aggregate quality.
- f50 medtech_idiosyncratic_alpha — composite signal.

## Parallel build plan
10 sub-agents (Batch A–J), each owns 5 families.
- A f01–f05, B f06–f10, C f11–f15, D f16–f20, E f21–f25,
- F f26–f30, G f31–f35, H f36–f40, I f41–f45, J f46–f50.

10 × 5 × 4 = **200 files**. 50 × 450 = **22,500 features**.
