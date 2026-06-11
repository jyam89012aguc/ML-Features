# Energy Features — Feature Family Plan

## Sector context
Database: `C:\Users\jyama\Desktop\silver db\trading.duckdb`
- `sep` — daily OHLCV.
- `fundamentals` — quarterly financials.
- `tickers` — `sector='Energy'` covers Oil & Gas E&P (857), Midstream (379), Equipment &
  Services (271), Refining & Marketing (139), Drilling (109), Integrated (59). 1,814 tickers.
  Uranium miners are in `Basic Materials` but commodity-cycle features apply equally.

## Investment thesis
Energy is **commodity-cycle driven** with lumpy/clustered returns. 10x setups concentrate at
**cycle bottoms** in:
- E&P revenue/margin recovery from commodity-price troughs
- Oilfield services backlog & dayrate inflection
- Drilling rig utilization cycle
- Midstream/LNG long-cycle contracted revenue (more compounder-like)
- Uranium / nuclear long-cycle inflection (post-Fukushima recovery, AI-driven nuclear demand)

50 families to maximize cross-coverage of these distinct cycle dynamics.

## File structure (mirrors prior sector builds)
Per family folder `f##_<slug>/`:
1. `f##_<slug>_base_001_075_claude.py`  — 75 base features.
2. `f##_<slug>_base_076_150_claude.py`  — 75 base features.
3. `f##_<slug>_2nd_derivatives_001_150_claude.py` — 150 slope features.
4. `f##_<slug>_3rd_derivatives_001_150_claude.py` — 150 jerk features.

Total per family: 450. Grand total: 50 × 450 = **22,500 features**.

## 50 Energy feature families

### E&P fundamentals (1–10)
- f01 reserve_growth_signature — asset growth as reserves growth proxy.
- f02 production_growth_acceleration — revenue acceleration on production ramp.
- f03 lifting_cost_efficiency — cor / revenue (lifting cost intensity).
- f04 finding_development_cost — capex / asset growth (F&D cost).
- f05 ep_capex_intensity — capex / revenue.
- f06 ep_drilling_efficiency — capex / production proxy.
- f07 ep_balance_sheet_resilience — leverage cycle position.
- f08 ep_breakeven_signature — margin durability through commodity cycle.
- f09 ep_inventory_management — inventory (oil reserves) dynamics.
- f10 ep_production_quality — revenue per asset.

### Oilfield services (11–15)
- f11 ofs_utilization_proxy — revenue per asset.
- f12 ofs_dayrate_dynamics — revenue growth in commodity rallies.
- f13 ofs_backlog_growth — deferred revenue / pipeline.
- f14 ofs_margin_cyclical — margin sensitivity to cycle.
- f15 ofs_consolidation_signature — M&A in services.

### Midstream / LNG (16–20)
- f16 midstream_throughput_growth — revenue stability.
- f17 lng_volume_pricing — revenue per asset.
- f18 pipeline_capex_cycle — capex / revenue cycle.
- f19 midstream_contracted_revenue — revenue smoothness (long-term contracts).
- f20 lng_export_acceleration — revenue acceleration on LNG demand.

### Uranium / nuclear / long-cycle commodity (21–25)
- f21 uranium_price_leverage — revenue sensitivity to commodity prices.
- f22 uranium_production_growth — revenue growth on small base.
- f23 uranium_inventory_cycle — inventory dynamics.
- f24 uranium_long_cycle — multi-year revenue compounding.
- f25 nuclear_capex_cycle — capex cycle.

### Drilling / rig (26–30)
- f26 drilling_rig_utilization — revenue per asset.
- f27 rig_dayrate_cycle — revenue growth signature.
- f28 drilling_backlog — deferred revenue.
- f29 drilling_balance_sheet — leverage cycle.
- f30 drilling_recovery_signature — cycle bottoming.

### Commodity cycle / macro (31–35)
- f31 commodity_price_leverage — revenue sensitivity.
- f32 oil_gas_cycle_position — revenue / margin cycle position.
- f33 commodity_cycle_recovery — trough recovery.
- f34 commodity_distress_signature — downturn vulnerability.
- f35 commodity_cycle_late_signature — cycle-peak signal.

### Capital allocation (36–40)
- f36 energy_buyback_cycle — countercyclical capital return.
- f37 energy_dividend_growth — dividend compounding.
- f38 energy_capex_discipline — capex / fcf ratio.
- f39 energy_capital_return_quality — return consistency.
- f40 energy_payout_durability — payout in down cycles.

### Returns & quality (41–45)
- f41 energy_roic_compounding — ROIC trajectory.
- f42 energy_fcf_yield — FCF / EV.
- f43 energy_capital_efficiency — asset turnover.
- f44 energy_earnings_quality — cash vs accrual.
- f45 energy_balance_sheet_strength — net debt position.

### Quiet compounders / 10x setups (46–50)
- f46 quiet_energy_compounder — low vol + steady growth (rare in energy).
- f47 hidden_energy_compounder — small base + high quality.
- f48 commodity_bottom_to_top — cycle-bottom signature.
- f49 energy_terminal_compounder — aggregate quality composite.
- f50 energy_idiosyncratic_alpha — composite signal.

## Parallel build plan
10 sub-agents (Batch A–J), each owns 5 families.
- A f01–f05, B f06–f10, C f11–f15, D f16–f20, E f21–f25,
- F f26–f30, G f31–f35, H f36–f40, I f41–f45, J f46–f50.

10 × 5 × 4 = **200 files**. 50 × 450 = **22,500 features**.
