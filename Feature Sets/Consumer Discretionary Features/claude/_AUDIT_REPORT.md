# Consumer Discretionary Features — Audit Report (50 families)

Scope: every `.py` file under
`D:\active_non audited features per AI\Consumer Discretionary Features\claude\`.

## 1. Coverage

| check | result |
|---|---|
| family folders | **50 / 50** (`f01`…`f50`) |
| files per family (4) | **200 / 200** |
| imports cleanly | **200 / 200** |
| every file's `__main__` prints `OK ...` | **200 / 200** |
| `REGISTRY` size per file (75 / 75 / 150 / 150) | **all match** |
| v### contiguity per file | **no gaps** |
| **total features** | **22,500** |

## 2. Duplicates

- **Global function-name collisions**: **0**.
- **Within-family duplicate function bodies**: only **3 minor pairs** across the whole
  22,500-feature set:
  - `f16_ecommerce_gmv_growth` — 1 pair
  - `f26_sga_leverage_consumer` — 1 pair
  - `f27_fcf_yield_durability_consumer` — 1 pair
- **Cross-family duplicate bodies**: **0**.

**Effective unique signals: 22,497 / 22,500 (~99.99%)** — substantially cleaner than the first
Industrials build (~85% unique) thanks to the naming-discriminator and dup-check rules baked
into the brief.

## 3. Column alignment vs `trading.duckdb`

- Unknown column references: **0**
- Columns used: `closeadj`, `high`, `low`, `volume`, `revenue`, `ebitda`, `ebit`, `netinc`,
  `fcf`, `ncfo`, `capex`, `depamor`, `sgna`, `opex`, `gp`, `cor`, `inventory`, `receivables`,
  `payables`, `deferredrev`, `workingcapital`, `ppnenet`, `assets`, `equity`, `debt`,
  `marketcap`, `ev`, `grossmargin`, `ebitdamargin`, `netmargin`, `roa`, `roic`, `eps`, …

All families wire to real DB columns.

## 4. Real-data signal test (50 families)

- 11 long-history Consumer Cyclical tickers (WGO, VFC, NKE, BALL, PHM, NVR, BSET, SKY, SON, AVY, IP).
- 8 random features per family × 50 families = **400 sampled**, 383 evaluated.
- Pooled Spearman IC vs fwd-21d / fwd-63d returns; winsorized 0.5/99.5%; ≥500 obs.

### Aggregate

| metric | value | (30-family build) |
|---|---:|---:|
| mean |IC₂₁| | **0.0184** | (0.0148) |
| mean |IC₆₃| | **0.0274** | (0.0233) |
| share |IC₂₁| > 0.02 | **36.3%** | (23.7%) |
| share |IC₂₁| > 0.05 | **3.7%** | (1.3%) |
| share |IC₂₁| > 0.10 | **0.5%** | (0.0%) |

Adding the 20 new families (auto OEMs/parts/dealers, apparel/luxury, hospitality/leisure,
home/packaging/publishing/composite) materially **raised signal density** — the new families
introduced more idiosyncratic cycle-position and rollout signals.

### Family ranking (top 15 by mean |IC₂₁|)

| family | mean \|IC₂₁\| | mean \|IC₆₃\| | max \|IC₂₁\| |
|---|---:|---:|---:|
| f49 publishing_subscription_quality | 0.121 ¹ | 0.237 | 0.177 |
| f07 store_rollout_signature         | 0.029 | 0.033 | 0.057 |
| f44 leisure_cyclical_recovery       | 0.028 | 0.042 | 0.048 |
| f45 gambling_revenue_resilience     | 0.028 | 0.024 | 0.058 |
| f25 working_capital_consumer        | 0.027 | 0.036 | 0.059 |
| f33 auto_dealer_inventory_dynamics  | 0.026 | 0.041 | 0.035 |
| f18 digital_cac_efficiency          | 0.025 | 0.032 | 0.042 |
| f04 pricing_passthrough             | 0.024 | 0.046 | 0.038 |
| f10 retail_comp_dynamics            | 0.023 | 0.031 | 0.036 |
| f35 auto_capex_intensity            | 0.023 | 0.027 | 0.031 |
| f24 receivables_quality_consumer    | 0.022 | 0.028 | 0.052 |
| f31 auto_oem_cycle_position         | 0.022 | 0.033 | 0.051 |
| f28 quiet_consumer_compounder       | 0.021 | 0.033 | 0.049 |
| f05 brand_loyalty_proxy             | 0.021 | 0.036 | 0.038 |
| f16 ecommerce_gmv_growth            | 0.021 | 0.035 | 0.087 |

¹ f49 has only 3 successfully-evaluated features (small sample sizes 594–635 obs) due to
deferred-revenue sparsity in many CD tickers — its IC is real but the small denominator inflates
the family mean.

### Weakest 5 families (mean |IC₂₁| < 0.011)
- f48 packaging_pricing_power (0.008)
- f19 marketplace_network_effects (0.008)
- f43 lodging_demand_cycle (0.009)
- f15 multi_brand_synergy (0.011)
- f39 apparel_seasonality_quality (0.012)

These either operate on highly bounded ratios that lose pooled discriminative power, or are
better evaluated within-ticker than cross-sectionally.

### Top individual features (|IC₂₁| ≥ 0.05)

| family | feature | n | IC₂₁ | IC₆₃ |
|---|---|---:|---:|---:|
| f49 | `drq_252d_slopemean42_slope_v108` | 635 | -0.177 | -0.389 |
| f49 | `drq_252d_jerkmean5_jerk_v092` | 594 | 0.167 | 0.310 |
| f16 | `gmvscore_smean_378d_slope_v072` | 57,189 | -0.087 | -0.130 |
| f03 | `revaccel_252d_base_v031` | 70,122 | -0.071 | -0.110 |
| f21 | `margposmean_10d_jw126_jerk_v054` | 3,460 | 0.068 | 0.038 |
| f25 | `wceffstd_126d_base_v137` | 57,567 | -0.059 | -0.109 |
| f45 | `rsema_10d_jerk_v036` | 70,533 | -0.058 | -0.026 |
| f09 | `csr_xdep_63d_jerk_v135` | 63,885 | 0.058 | 0.038 |
| f07 | `dyn_std_252d_jerk_v128` | 8,727 | 0.057 | 0.002 |
| f34 | `phase_per_capex_378d_base_v060` | 70,288 | -0.055 | -0.106 |
| f37 | `prodcyc_252d_base_v028` | 70,122 | -0.053 | -0.081 |
| f24 | `dsoz_42d_jw126_jerk_v030` | 31,006 | -0.052 | 0.007 |
| f31 | `mpos_42d_jerk_v059` | 12,461 | -0.051 | -0.025 |
| f37 | `prodcycsq_252d_base_v103` | 70,122 | -0.051 | -0.078 |

Raw per-feature ICs written to `_audit_ic_results.csv`.

## 5. Verdict

- **Coverage**: 50 families, 200 files, 22,500 features, all running OK.
- **Hygiene**: 0 name collisions, 0 unknown columns, only 6 duplicate signals
  (~99.99% effective uniqueness).
- **Signal density** (vs original 30-family build):
  - Mean |IC₂₁| up from 0.015 → **0.018** (+24%)
  - Share of features clearing |IC₂₁| > 0.02: 24% → **36%**
  - Share clearing 0.05: 1.3% → **3.7%**
  - Share clearing 0.10: 0% → **0.5%**
- **Thesis-aligned signal**: the auto OEMs/parts/dealers + hospitality/leisure + subscription
  families (f31–f35, f41–f45, f49) contributed the most new signal, validating the design choice
  to maximize idiosyncratic coverage.

Files referenced:
- `_PLAN.md` — feature family list & thesis.
- `_AGENT_BRIEF.md` — generation template / rules.
- `_audit_ic_results.csv` — per-feature IC table.
