# DEEP signal audit — findings (the honest verdict)

Method upgrades over the first pass: Newey-West (HAC) t-stats on the monthly IC series
(corrects overlapping-window inflation), out-of-sample sign stability (time-split),
quantile long-short spread + its HAC t, horizon profile (126/252/**504d**), a PERMUTATION
NULL (shuffle ticker labels of forward returns within each month → false-positive floor),
and PCA effective-dimensionality. Universe: 21 crypto-equity names, post-2019.

## Headline: aggregate alpha is NOT demonstrable on this universe
- OBSERVED "robust" feature share (HAC|t|>=2 AND OOS-sign-stable AND LS-spread significant):
  **0.9%**.
- PERMUTATION-NULL robust share (pure chance): **3.6%**.
- Observed HAC|t|>2 share **13.2%** vs null **12.6%** — essentially identical.
- **Signal lift over chance: 0.3x.** The strict criterion finds FEWER real "robust" features
  than random data does. → On this 21-name, post-2021 universe the feature set as a whole is
  **statistically indistinguishable from noise.**
- This means the FIRST audit's "21% strong-IC / 63% for f21" numbers were **overlap-inflation
  artifacts**, not alpha. Corrected, they collapse.

## But it is NOT just noise — three real, positive findings
1. **Signal strengthens with horizon.** Median |IC| 0.044 @252d → **0.063 @504d**; many
   fundamental families roughly double (f24 0.067→0.165, f07 0.054→0.131, f35 0.073→0.124,
   f22 0.044→0.098). Consistent with these being LONG-horizon (5y/10x) features, not short-term.
2. **Direction is consistent even when significance isn't.** Horizon sign-agreement (252 vs
   504) is high in fundamental families: f21 94%, f24 91%, f19 88%, f35 83%, f17 79%, f20 77%.
   A faint, directionally-stable signal the small sample just can't certify.
3. **Genuine high dimensionality (PCA).** 1,467 sampled base features → **139 PCs for 80% var,
   265 for 90%, 404 for 95%**; top PC only 10.4%, top 10 only 34.8%. The set is NOT a few
   factors in disguise — it spans hundreds of independent directions. The "generate volume,
   let ML select" design has real diversity to exploit.

## One family clears the null — but treat as SUSPECT
f29_ownership_concentration: robust 12% vs null 6%, HAC|t| up to **15.2**, ic252≈0.31 /
ic504≈0.35, dominates the leaderboard. LIKELY STRUCTURAL/SPURIOUS: concentration is highly
persistent, ic252_absmed is NaN (many features have too few valid cross-sections), so a single
persistent cross-sectional ordering on 21 names can manufacture huge t-stats. Needs manual
scrutiny before being trusted. Same caveat for insider families (f31-f33: HAC|t|>2 of 37-48%
but robust≈null, NaN median IC) — high t on SPARSE data, not credible.

## Why the test is underpowered (not the features' fault)
21 names, most <4y history, data ends 2025 → 504d-forward labels exist only through ~2023;
each monthly cross-section ranks ~10-21 names. The real target (10x / 5y) needs a broad,
survivorship-free universe of thousands of names. This audit can certify the features are
**well-built, clean, non-redundant, diverse, and not price-contaminated** — it CANNOT certify
predictive alpha, and at face value alpha doesn't beat chance here.

## Recommendation
The only way to actually answer "high signal?" is to compute these features on the FULL equity
universe (thousands of names) where cross-sectional IC is statistically powerful — the OHLCV/
fundamental/ownership families are generic and will compute there. On the crypto-only universe,
lean on (a) the confirmed diversity (PCA) with a strongly-regularized ML model, (b) the long-
horizon (504d+) framing where the faint signal concentrates, and (c) fundamental/ownership
families over short-horizon price-pattern families (f03/f10/f11/f12/f14 add least).

Data: _spec/deep_audit_results.csv ; per-feature: _spec/deep_parts/*.json
