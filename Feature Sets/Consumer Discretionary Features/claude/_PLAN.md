# Consumer Discretionary Features — Feature Family Plan

## Sector context
Database: `C:\Users\jyama\Desktop\silver db\trading.duckdb`
- `sep` — daily OHLCV (closeadj, volume).
- `fundamentals` — quarterly financials.
- `tickers` — `sector='Consumer Cyclical'` covers Specialty Retail (478), Restaurants (417),
  Auto Parts (360), Apparel Retail (247), Internet Retail (237), Apparel Manufacturing (137),
  Luxury Goods (77), Footwear (80), Home Improvement Retail (49), etc. 3,853 tickers total.

## Investment thesis
Consumer Discretionary winners are **idiosyncratic** — niche brand pricing power, specialty-retail
comps, early-stage restaurant rollouts, and e-commerce unit economics drive 5-year compounders.
Unlike Industrials' macro cycle, CD signals are bottom-up:
- **Niche brand pricing power** — gross margin durability + revenue growth on small base.
- **Specialty retail comps** — same-store sales proxy via revenue smoothness vs unit growth.
- **Early-stage restaurant rollouts** — capex growth + revenue acceleration without margin dilution.
- **E-commerce unit economics** — revenue per dollar of capex/sga, take-rate proxies, retention.

Originally scoped at 30 families; extended to 50 to maximize family coverage across the
heterogeneous CD industries (auto OEMs/parts/dealers, apparel, luxury, hospitality, leisure,
home/furniture, packaging, publishing, personal services).

## File structure (mirrors `Industrials Features\claude\f01_...\`)
Per family folder `f##_<slug>/`:
1. `f##_<slug>_base_001_075_claude.py`  — 75 base features (v001…v075).
2. `f##_<slug>_base_076_150_claude.py`  — 75 base features (v076…v150).
3. `f##_<slug>_2nd_derivatives_001_150_claude.py` — 150 slope features.
4. `f##_<slug>_3rd_derivatives_001_150_claude.py` — 150 jerk features.

Total per family: 450. Grand total: 30 × 450 = 13,500 features.

## 30 Consumer Discretionary feature families

### Brand & pricing power (1–5)
- f01 brand_equity_pricing — gross margin durability + price uplift signature.
- f02 brand_premium_durability — multi-year margin maintenance.
- f03 niche_brand_growth — high revenue growth on small revenue base.
- f04 pricing_passthrough — input-cost vs revenue/margin reaction.
- f05 brand_loyalty_proxy — revenue stability (low CV) as retention proxy.

### Specialty retail (6–10)
- f06 same_store_sales_proxy — revenue growth net of store-count growth (capex proxy).
- f07 store_rollout_signature — capex pulses + revenue acceleration.
- f08 retail_inventory_freshness — inventory turnover dynamics.
- f09 retail_capex_per_store — capex relative to PP&E base.
- f10 retail_comp_dynamics — same-store growth durability through cycles.

### Restaurants & rollouts (11–15)
- f11 restaurant_unit_economics — revenue/asset & ebitda/asset.
- f12 rollout_velocity — capex acceleration + revenue growth in tandem.
- f13 auv_growth_proxy — revenue per dollar of fixed asset growth.
- f14 restaurant_margin_durability — ebitda margin stability through revenue growth.
- f15 multi_brand_synergy — diversified-revenue compounding (low-vol high-growth).

### E-commerce & digital (16–20)
- f16 ecommerce_gmv_growth — high revenue growth + low working-capital intensity.
- f17 ecommerce_take_rate_proxy — gross profit / revenue rising.
- f18 digital_cac_efficiency — sg&a vs revenue growth tradeoff.
- f19 marketplace_network_effects — accelerating revenue growth on flat sg&a.
- f20 dtc_brand_acceleration — direct-to-consumer revenue compounding.

### Consumer cycle & working capital (21–25)
- f21 consumer_cycle_phase — revenue + margin position in cycle.
- f22 discretionary_demand_resilience — revenue stability in down cycles.
- f23 inventory_to_sales_consumer — inventory days dynamics for retail.
- f24 receivables_quality_consumer — DSO + earnings quality.
- f25 working_capital_consumer — operating cycle dynamics.

### Quality / compounders / cash (26–30)
- f26 sga_leverage_consumer — sg&a scaling with revenue.
- f27 fcf_yield_durability_consumer — fcf/ev consistency.
- f28 quiet_consumer_compounder — low vol + steady earnings growth.
- f29 hidden_brand_compounder — small base + high returns + low coverage.
- f30 consumer_terminal_compounder — aggregate quality composite.

### Auto OEMs / parts / dealers (31–35)
- f31 auto_oem_cycle_position — OEM revenue/margin cycle phase.
- f32 auto_parts_aftermarket_durability — aftermarket margin sustainability.
- f33 auto_dealer_inventory_dynamics — dealer floor-plan inventory.
- f34 ev_growth_acceleration — EV-driven revenue acceleration.
- f35 auto_capex_intensity — auto-sector capex cycle.

### Apparel / luxury / footwear (36–40)
- f36 apparel_inventory_markdown_risk — inventory aging.
- f37 footwear_brand_cycle — product cycle for footwear.
- f38 luxury_brand_premium_durability — luxury margin sustainability.
- f39 apparel_seasonality_quality — seasonal-stock smoothness.
- f40 textile_input_cost_sensitivity — input cost transmission.

### Hospitality / leisure / lodging (41–45)
- f41 hospitality_revpar_proxy — revenue per asset proxy for lodging.
- f42 resort_casino_capex_intensity — property capex burn.
- f43 lodging_demand_cycle — revenue volatility / recovery.
- f44 leisure_cyclical_recovery — cycle bottoming signal.
- f45 gambling_revenue_resilience — gaming revenue stability.

### Home / furniture / packaging / publishing / services (46–50)
- f46 furniture_housing_cycle — housing-driven furniture revenue.
- f47 home_improvement_durability — repair/remodel-driven retail share.
- f48 packaging_pricing_power — packaging margin durability.
- f49 publishing_subscription_quality — deferred-revenue subscription proxy.
- f50 cd_idiosyncratic_alpha — composite quality + low-vol + high-growth signal.

## Parallel build plan
10 sub-agents (Batch A–J), each owns 5 families.
- Batch A f01–f05 — brand & pricing
- Batch B f06–f10 — specialty retail
- Batch C f11–f15 — restaurants
- Batch D f16–f20 — e-commerce
- Batch E f21–f25 — cycle / working capital
- Batch F f26–f30 — quality / cash / compounders
- Batch G f31–f35 — auto OEMs / parts / dealers
- Batch H f36–f40 — apparel / luxury / footwear
- Batch I f41–f45 — hospitality / leisure / lodging
- Batch J f46–f50 — home / packaging / publishing / services / composite

10 batches × 5 families × 4 files = 200 files. 50 × 450 = 22,500 features.
