# Blockchain feature build — final report

Generated 2026-06-07. Output root: `D:\Features\claude\`

## Scope
30 blockchain-equity feature families (crypto miners, exchanges, BTC-treasury cos,
mining-hardware makers). Each family = 4 files (75 + 75 base, 150 slope = 1st math
derivative, 150 jerk = 2nd math derivative) = **450 features/family**.

- Families: 37  (f01 … f37; f31–f37 added after the signal audit)
- Files: 148  (4 per family)
- Total features: **16,650**
- Unique function names: **16,650 (zero duplicates across the entire set)**
- f31–f33 = insider transactions (sf2); f34 = institutional breadth (sf3 long-form);
  f35 = Altman-Z distress; f36 = Beneish manipulation; f37 = crypto-sector relative strength.

## Verification (all independently re-run, not self-reported)
- [PASS] 120/120 self-tests print `OK ...` (synthetic n=1500, seed=42): no all-NaN/
  zero/constant feature; nunique>50 on warm-up tail; >=80% features <50% NaN;
  determinism; every feature references its family domain primitive.
- [PASS] Structure: every folder has the 4 correctly-named files; base files <=75KB;
  derivative files within 30–75KB.
- [PASS] No forbidden patterns in any file (no importlib/exec/globals/setattr loops,
  no `_core()`, no `formulas[i % N]` indexing). Derivative files are fully-expanded
  literal defs.
- [PASS] Real-data: all 13,500 features executed on real MARA series (OHLCV from
  sep_validated; fundamentals forward-filled from fundamentals_validated ARQ;
  ownership forward-filled from sf3a) — 0 errors, 13 low-variance (0.1%, expected on
  a single ticker), 0 missing columns.

## Input assignment
- f01–f15 OHLCV: {open, high, low, close, closeadj, volume}
- f16–f25 fundamentals: >=1 of {revenue, netinc, fcf, equity, debt, assets, ebitda,
  capex, sharesbas, ncfo, opinc, gp, grossmargin, cor, ppnenet, cashneq, currentratio,
  de, sbcomp, ...}
- f26–f30 metrics/ownership: >=1 of {marketcap, ev, evebit, evebitda, pe, pb, ps,
  shrvalue, shrunits, totalvalue, percentoftotal}

## Naming
`{short}_{fNN_full}_{calc}_{w}d_{base|slope|jerk}_v{NNN}_signal`
e.g. `f01cb_f01_crypto_beta_momentum_roc_21d_base_v001_signal`

## Tooling (in `_spec/`, not feature files)
- `SPEC.md` — the build rulebook each generator followed.
- `build_derivatives.py` — deterministic expander that inlines each base feature and
  emits the slope/jerk files as literal code (window-appropriate discrete derivative
  scaled by base dispersion; jerk = derivative applied twice).
- `FEATURE_FAMILIES.md` — the family list / domain definitions.

## Family list
f01 crypto_beta_momentum · f02 halving_cycle_phase · f03 parabolic_blowoff_top ·
f04 crypto_winter_drawdown · f05 reflexive_volatility_regime · f06 volatility_squeeze_breakout ·
f07 overnight_gap_dynamics · f08 capitulation_volume_spike · f09 range_expansion_atr ·
f10 relative_strength_leadership · f11 trend_persistence · f12 oversold_reversion_oscillator ·
f13 liquidity_dollar_volume · f14 short_squeeze_thrust · f15 accumulation_distribution_flow ·
f16 bitcoin_treasury_premium · f17 share_dilution_machine · f18 cash_burn_runway ·
f19 mining_capex_intensity · f20 operating_leverage_to_crypto · f21 gross_margin_volatility ·
f22 balance_sheet_leverage · f23 revenue_hypergrowth · f24 cash_earnings_divergence ·
f25 dilution_adjusted_growth · f26 ev_valuation_regime · f27 speculative_multiple_decay ·
f28 institutional_accumulation · f29 ownership_concentration · f30 smart_money_positioning ·
f31 insider_buying_pressure · f32 insider_conviction_quality · f33 insider_distribution_selling

## Added families f31–f37 — real-data audit (post-2019 crypto universe)
All clean (not price-contaminated), low redundancy; audited on real data:
- f31 insider_buying_pressure   : contam 0.25 redund 0.19 NaN 17%  37% strong-IC
- f32 insider_conviction_quality: contam 0.32 redund 0.24 NaN 73%* 38% strong-IC (*specialist: sparse)
- f33 insider_distribution_selling: contam 0.26 redund 0.21 NaN 13% 44% strong-IC
- f34 institutional_breadth_churn: contam 0.33 redund 0.25 NaN 14% 26% strong-IC
- f35 financial_distress_score   : contam 0.33 redund 0.23 NaN 9%  43% strong-IC
- f36 earnings_manipulation_score: contam 0.23 redund 0.11 NaN 19% 34% strong-IC (lowest redundancy of any family)
- f37 crypto_sector_relative_strength: contam 0.26 redund 0.22 NaN 8% 25% strong-IC
f35/f36/f34/f37 use dense data → credible IC (best 0.18–0.24). Insider IC magnitudes
inflated by sparse 16-name coverage — treat as directional. New real-data inputs built:
insider daily aggregates (sf2), holder breadth nholders/hhi/churn (sf3 long-form),
equal-weight crypto sector_index. See _spec/AUDIT_FINDINGS.md.

## Insider families (f31–f33) — added after the signal audit
Built from `main.sf2` (insider Form-4 transactions). Real per-day aggregates: open-market
buys/sells ($ + shares + counts), officer/director/10%-owner-flagged buys, option exercises.
All 12 files pass self-tests; audited on real insider data for 16/21 names. Clean
(not price-contaminated) and orthogonal to the OHLCV/fundamental/13F families. f32 is a
specialist family (73% NaN — defined only when recent insider buying exists). See
_spec/AUDIT_FINDINGS.md for caveats (sparse universe inflates IC magnitudes).
