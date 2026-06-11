# Signal audit — findings (real crypto-equity data, post-2019)

Universe: 21 real blockchain-exposed names (MARA, RIOT, CLSK, HUT, BITF, CIFR, WULF,
HIVE, IREN, BTDR, CORZ, BTBT, COIN, MSTR, CAN, BKKT, GREE, ARBK, SDIG, BTM, APLD).
Real OHLCV + fundamentals (forward-filled by filing datekey, no look-ahead) + 13F
ownership (lagged 45d). Audited the 150 BASE features per family (levels are where
contamination/redundancy live; slope/jerk are differenced → less contaminated).

## What is CONFIRMED (robust, not dependent on forward returns)

1. **NOT price-contaminated** — the key prior failure mode is fixed.
   - Median |corr(feature, log price)| = **0.26**; **0/30 families** have >50% of features
     above 0.9; essentially no feature is a raw price proxy.
   - (Contrast: the earlier tech set was flagged ~99.9% price-contaminated.)
   - Worst case f02_halving_cycle (med 0.58) is expected — cycle-position tracks price
     within long ranges — but still 0% above 0.9.

2. **LOW redundancy** — median within-family |corr| = **0.25**, median near-duplicate
   pairs (|corr|>0.95) = **0%**. Most redundant: f12_oversold (0.55), f10_rel_strength
   (0.51), f03_parabolic (0.40) — variant-heavy oscillator families, but still <2% dups.

3. **Coverage** — median NaN = 11% (technical 2–9%, fundamental 13–26% from quarterly
   data + warm-up). Expected; ML drops warm-up rows.

## What is INDICATIVE (predictive IC — treat with caution)

Cross-sectional Spearman IC vs forward-252d return, monthly. **Caveats: the universe is
small (~21 names) and young (most listed 2021+); overlapping 252d windows inflate IC
t-stats; the true target (10x / 5y) has too few labels to test directly.** So IC RANKING
across families is informative; absolute magnitudes are optimistic.

- Median |IC| ≈ 0.04; ~21% of features show |IC-IR|>2; 21/30 families have ≥15% such
  features.
- **Fundamental / ownership / liquidity families carry the most cross-sectional signal**
  (sensible for a long-horizon fundamental "10x" target):
  strongest = f21_gross_margin_volatility (63% strong, |IC|med 0.119),
  f13_liquidity_dollar_volume (51%, 0.083), f19_mining_capex_intensity (50%, 0.079),
  f29_ownership_concentration (47%, 0.085), f26_ev_valuation_regime (39%),
  f24_cash_earnings_divergence (37%), f18_cash_burn_runway (31%),
  f20_operating_leverage (31%), f07_overnight_gap (28%).
- **Weak at this horizon — short-term price-pattern families:**
  f14_short_squeeze_thrust (1% strong, best |IC| 0.095), f03_parabolic_blowoff (2%),
  f10_relative_strength_leadership (3%, also most redundant), f11_trend_persistence (7%),
  f12_oversold_reversion (8%, redundant). These predict short-term moves, not 5y 10x.

## Verdict
- Hygiene/validity: **excellent** — features are real, distinct, non-redundant, and
  (critically) not price proxies. The "generate volume, let ML select" design is sound.
- Predictive signal: **real but modest and concentrated** — a meaningful minority of
  features (esp. fundamental/ownership/liquidity) show cross-sectional signal; ~5–6
  short-horizon technical families are weak for the 5-year target. Magnitudes are not
  robustly established on this small/young universe — they need confirmation on a broader
  universe and a true multi-year label before being called "high signal."

## Recommended actions
1. Keep all families (ML handles selection) but DOWN-WEIGHT / candidate-prune the weak
   technical set (f03, f10, f11, f12, f14) if compute matters.
2. ADD the orthogonal families that target the 5-year fundamental thesis — see
   PROPOSED_NEW_FAMILIES.md: insider (f31–f33), distress/manipulation (f35–f36),
   institutional breadth (f34), sector-relative (f37). Insider buying and distress
   scores are exactly the kind of long-horizon, non-price signal the audit shows is
   scarce in the current technical families.

## ADDED: insider families f31–f33 (built from sf2, audited on real insider data)
Real per-day insider aggregates (open-market buys/sells, officer/director/10%-owner
flags, option exercises) built for the 16/21 names with insider activity.
- f31_insider_buying_pressure  : contam 0.25, redund 0.19, NaN 17%, |IC|med 0.076, 37% strong
- f32_insider_conviction_quality: contam 0.32, redund 0.24, NaN **73%**, |IC|med 0.113, 38% strong
- f33_insider_distribution_selling: contam 0.26, redund 0.21, NaN 13%, |IC|med 0.081, 44% strong
Clean (not price-contaminated) and orthogonal, with higher |IC| than typical technical
families. CAVEATS: insider events are SPARSE on a 16-name universe → IC magnitudes
(best |IC| 0.59–0.84) are inflated by tiny effective samples; do not read as alpha.
f32 is a SPECIALIST family — 73% NaN because officer/director-buy-specific ratios are
undefined when no recent insider buying exists (high signal only when present).

Raw per-feature data: _spec/audit_parts/*.json ; table: _spec/audit_results.csv
