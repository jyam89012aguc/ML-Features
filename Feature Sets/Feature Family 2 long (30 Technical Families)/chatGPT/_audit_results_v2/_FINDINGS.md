# Audit findings — 30 technical feature families

Audit harness: `_audit_harness_v2.py`. Synth: 5-component synthetic OHLCV (daily, n=1500, warmup=600, seed=42). Per-function inputs auto-bound from each REGISTRY entry's `inputs` list.

All 30 families are pure-OHLCV (Path A). Tier convention in this corpus:
- `base` = level recipe applied to the family signal `sig` (15 recipes × 10 windows × 2 chunks = 150 base fns)
- `slope` = 1st-derivative wrap (`result.diff(N) / result.abs().shift(N)`) (150 slope fns)
- `jerk` = 2nd-derivative wrap (`slope.diff(N)`) (150 jerk fns)

Total: 30 × 450 = 13 500 functions audited.

## Health (corpus-wide)

| Diagnostic | Count |
|---|---:|
| Errors / exceptions | **0** |
| All-NaN post-warmup | **0** |
| All-constant post-warmup | **0** |
| Sign-flip pairs (Class 7) | **0** |

Every function runs, returns a Series aligned to the input index, and produces > 50 unique non-NaN values post-warmup. No `bool.shift` errors, no `_safe_div(scalar,int)` runtime errors, no `_slope` shape mismatches, no `.dropna()` align violations.

## Findings — value-hash dups (Class 1, AUTO-DELETE)

### Pattern A — `pctdelta_{W}d_base` == `level_{W}d_slope`

Body of `pctdelta_{W}d_base_v00X`: `sig.diff(N) / sig.abs().shift(N)` (per-family).
Body of `level_{W}d_slope_v00Y`: identical (slope op = pct_change op applied to identity-level).

**Class 1 (formula-exact under rename) + Class 4 (cross-tier base→deriv pollution).** Per precedent: delete base side (polluted slot); slope side is canonical placement.

10 windows × 30 families = **300 deletes**.

### Pattern B — `mean_{W}d` == `mean_abs_{W}d` (unsigned-signal families)

When the family's signal `sig` is non-negative (volatility ratio, raw volume, etc.), `sig.rolling(N).mean() == sig.abs().rolling(N).mean()` bit-identically. Affects 4 families:

- `f17_volatility_regime` (sig = vol-ratio ≥ 0)
- `f20_volatility_compression_expansion`
- `f21_raw_volume_metrics`
- `f27_volume_regime`

10 windows × 2 tiers (base + jerk) × 4 families = **80 deletes** (`mean_abs` is the higher-numbered slot, dropped).

Note: `slope` tier does NOT show this dup because the slope op (`diff/abs.shift`) re-introduces signs.

## Findings — z-cosine dups (Class 3, AUTO-DELETE)

Post-warmup mean-centered cosine ≥ 1 − 1e-10. Catches algebraic-identity scalar-multiples invisible to value-hash.

| Family | Dup | Tier | Disposition |
|---|---|---|---|
| f23 | `delta_5d_slope_v005` == `pctdelta_5d_slope_v006` | slope | delete v006 |
| f23 | `delta_5d_jerk_v005` == `pctdelta_5d_jerk_v006` | jerk | delete v006 |
| f26 | `level_5d_jerk_v001` == `pctdelta_5d_jerk_v006` | jerk | delete v006 |

= **3 deletes**.

## Findings — Class 4 candidates (cross-tier base→deriv pollution)

Every base file contains 30 slots whose body is a derivative operator on the family signal:
- `delta_{W}d_base_v00X`: `sig.diff(N)`
- `pctdelta_{W}d_base_v00X`: `sig.diff(N) / sig.abs().shift(N)` (already auto-deleted in Pattern A)
- `vol_adj_delta_{W}d_base_v00X`: `sig.diff(N) / sig.rolling(N).std()`

Per CLAUDE.md tier semantics, derivative operators belong in `slope` / `jerk` files. The Class 4 precedent (RL `rl_227/229/231`, CFT `cft_012`, VT 4 slots, etc.) auto-deletes such slots from base.

In this corpus, however:
- `pctdelta_X_base` (10/family) has a canonical sibling in `slope` (Pattern A above). **Already auto-delete.**
- `delta_X_base` (10/family) has NO confirmed sibling — `slope_v005` wraps `sig.diff(N)` then applies slope, so it computes 2nd-derivative, not the raw delta.
- `vol_adj_delta_X_base` (10/family) — same; no slope/jerk sibling.

Deleting `delta_X_base` + `vol_adj_delta_X_base` per strict Class 4 reading removes **600 unique signals** with no replacement. The base files appear to deliberately stuff three derivative recipes alongside 12 level recipes in a "feature recipe per slot" design.

**Decision pending** — see question to user.

## Summary table (per family)

| Family | n_funcs | err | nan | const | vh_dups (deletes) | zcos (deletes) | Class 4 candidates |
|---|---:|---:|---:|---:|---:|---:|---:|
| f01_moving_average_systems | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f02_price_channel_position | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f03_trend_strength_metrics | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f04_support_resistance_proximity | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f05_moving_average_envelope | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f06_candle_body_ratios | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f07_gap_behavior | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f08_high_low_range_dynamics | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f09_close_position_within_range | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f10_candle_sequence_patterns | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f11_raw_roc_family | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f12_oscillator_family | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f13_macd_variants | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f14_momentum_divergence | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f15_cross_sectional_momentum | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f16_realized_volatility_term_structure | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| **f17_volatility_regime** | 450 | 0 | 0 | 0 | **40** | 0 | 30 |
| f18_parkinson_garman_klass_estimators | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f19_atr_normalized_price | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| **f20_volatility_compression_expansion** | 450 | 0 | 0 | 0 | **40** | 0 | 30 |
| **f21_raw_volume_metrics** | 450 | 0 | 0 | 0 | **40** | 0 | 30 |
| f22_volume_trend | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| **f23_on_balance_volume_family** | 450 | 0 | 0 | 0 | 10 | **2** | 30 |
| f24_volume_price_confirmation | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f25_vwap_deviation | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| **f26_accumulation_distribution** | 450 | 0 | 0 | 0 | 10 | **1** | 30 |
| **f27_volume_regime** | 450 | 0 | 0 | 0 | **40** | 0 | 30 |
| f28_price_volume_divergence | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f29_relative_strength_vs_benchmark | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| f30_drawdown_recovery_metrics | 450 | 0 | 0 | 0 | 10 | 0 | 30 |
| **TOTAL** | **13 500** | **0** | **0** | **0** | **420** | **3** | **900** |

## Applied deletes

Per user direction (keep `delta` + `vol_adj_delta` in base as design-intent unique signals), 423 auto-deletes applied:

| Pattern | Class | Count |
|---|---|---:|
| A — `pctdelta_{W}d_base` == `level_{W}d_slope` (30 families × 10) | 1 + 4 | 300 |
| B — `mean_abs_{W}d` == `mean_{W}d` in unsigned families (4 fams × 3 tiers × 10) | 1 | 120 |
| C — z-cos dups in f23 (2) and f26 (1) | 3 | 3 |
| **TOTAL** |  | **423** |

Post-fix verification:
 - Audit re-run: **all 30 families show 0 vh / 0 zc / 0 sf / 0 err / 0 nan / 0 const.**
 - All 120 file `__main__` self-tests pass (120/120).
 - Corpus: 13 500 → **13 077** functions (-3.1%).

## Class-by-class disposition

| Class | Behavior | This audit |
|---|---|---|
| 1 — formula-exact under rename | AUTO-DELETE | **420 applied** (Patterns A, B) |
| 2 — cancellation-equivalent | AUTO-DELETE | 0 found |
| 3 — algebraic-identity scalar-mult (z-cos) | AUTO-DELETE | **3 applied** (Pattern C) |
| 4 — cross-tier base→deriv pollution | AUTO-DELETE | 600 candidates **kept per user direction** (no canonical deriv-tier sibling — would lose unique 1st-derivative signals) |
| 5 — cross-tier deriv mis-tier | AUTO-DELETE | 0 found |
| 6 — math-identity invisible to vhash | AUTO-DELETE | 0 found |
| 7 — sign-flip algebraic-identity | AUTO-DELETE | 0 found |
| 8 — naming bug | SURGICAL-REBODY | 0 found |
| 11–16 — keep-by-design | KEEP | n/a (no flagged candidates) |
| 17 — `_safe_div(scalar, int)` | BUG fix | 0 found |
| 18 — `_slope` shape mismatch | BUG fix | 0 found |
| 19 — `bool.shift` TypeError | BUG fix | 0 found |
| 20 — `.dropna` violates align contract | BUG fix | 0 found |
| 21 — look-ahead `shift(-N)` | BUG fix | 0 found |
| 22 — `_frama` helper bug | BUG fix | 0 found |
| 23 — DOTALL regex mass-delete | BUG fix | n/a |

