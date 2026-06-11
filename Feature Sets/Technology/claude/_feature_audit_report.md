# Feature Audit Report

## Summary

- Python files scanned: 404
- Public signal functions: 49140
- Feature folders: 101
- Parse errors: 0
- Duplicate function names: 0
- Exact duplicate functions: 0
- Same raw-body groups: 903
- Cross-folder overlap groups: 895
- Redundant signals in de-dup manifest: 905
- Unsanitized signals: 0
- Files without signals: 0

## Interpretation

No syntax, naming, or output-sanitization failures were found. The remaining duplicate risk is cross-domain semantic overlap: different feature folders expose the same calculation under domain-specific names.

## Highest Overlap Pairs

- `f015_interest_and_tax_drag <-> f026_interest_coverage`: 64 matching calculation groups
- `f030_asset_liability_gap <-> f064_return_on_equity`: 64 matching calculation groups
- `f039_enterprise_value <-> f072_cash_adjusted_valuation`: 64 matching calculation groups
- `f042_intangibles_goodwill <-> f062_impairment_and_writedown_risk`: 64 matching calculation groups
- `f087_ohlcv_multi_year_lows <-> f088_ohlcv_multi_year_highs`: 63 matching calculation groups
- `f031_shares_basic <-> f037_float_and_tradeable_scale`: 59 matching calculation groups
- `f011_financing_cash_flow <-> f033_equity_issuance_cash`: 57 matching calculation groups
- `f016_rnd_level <-> f017_rnd_growth`: 48 matching calculation groups
- `f038_market_capitalization <-> f069_ev_sales_valuation`: 48 matching calculation groups
- `f041_tangible_assets <-> f071_price_book_valuation`: 48 matching calculation groups
- `f046_revenue_level <-> f069_ev_sales_valuation`: 48 matching calculation groups
- `f046_revenue_level <-> f066_asset_turnover`: 48 matching calculation groups
- `f051_gross_margin_power <-> f070_ev_gross_profit_valuation`: 48 matching calculation groups
- `f071_price_book_valuation <-> f086_daily_market_metrics`: 48 matching calculation groups
- `f021_stock_based_compensation <-> f060_non_cash_expense_mix`: 33 matching calculation groups
- `f009_free_cash_flow <-> f063_return_on_assets`: 32 matching calculation groups
- `f021_stock_based_compensation <-> f036_sbc_dilution_pressure`: 32 matching calculation groups
- `f051_gross_margin_power <-> f100_index_membership_and_relative_context`: 27 matching calculation groups

## Recommendation

Keep these modules intact if downstream code expects each domain folder to be self-contained. If the registry must be strictly non-duplicative, canonicalize cross-domain overlap families in the registry or generation manifest rather than deleting functions from the modules.

A strict non-duplicate manifest is available in `_feature_dedup_manifest.json`.
