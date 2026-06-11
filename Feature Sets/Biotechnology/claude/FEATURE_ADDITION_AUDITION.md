# Feature Addition Audition

Silver DB: `C:\Users\jyama\Desktop\silver db\trading.duckdb`

## Gate Summary

- Existing signal names parsed: 45,486
- Existing target families parsed: 109
- Curated candidates evaluated: 24
- Implemented candidates detected: 24
- Approved high-signal candidates still pending: 0
- Rejected candidates: 0

This is a curated audition set, not a broad combinatorial expansion. A candidate is approved only if it has a unique proposed name, valid silver DB source fields, a unique source-field/operation/horizon signature, and either introduces fields unused by the target family or is a true peer/cross-field composite.

## Implemented Candidates

| Rank | Family | Candidate | Score | Source fields now present in family |
| ---: | --- | --- | ---: | --- |
| 1 | `f105_insider_transaction_microstructure` | `open_market_purchase_pressure` | 97 | `transactioncode`, `transactionshares`, `transactionpricepershare`, `transactionvalue` |
| 2 | `f103_corporate_action_risk` | `delisting_bankruptcy_cadence` | 96 | `action`, `value` |
| 3 | `f102_trading_liquidity` | `dollar_volume_liquidity` | 95 | `closeadj`, `volume`, `marketcap` |
| 4 | `f108_true_sector_industry_relative` | `biotech_peer_relative_cash_runway` | 95 | `cashneq`, `ncfo`, `marketcap` |
| 5 | `f101_price_volume_technicals` | `distance_to_52w_high_low` | 94 | `price`, `high52w`, `low52w` |
| 6 | `f106_institutional_security_mix` | `put_call_ownership_skew` | 94 | `putholders`, `cllholders`, `putvalue`, `cllvalue`, `totalvalue` |
| 7 | `f105_insider_transaction_microstructure` | `officer_director_alignment` | 93 | `isdirector`, `isofficer`, `istenpercentowner`, `transactioncode`, `transactionvalue` |
| 8 | `f97_multi_year_price_context` | `beta_adjusted_drawdown_context` | 93 | `price`, `high52w`, `low52w`, `high5y`, `low5y`, `beta1y`, `beta5y` |
| 9 | `f101_price_volume_technicals` | `moving_average_stack` | 92 | `price`, `ma50d`, `ma200d`, `ma50w`, `ma200w` |
| 10 | `f36_asset_composition` | `investment_liquidity_mix` | 92 | `investments`, `investmentsc`, `investmentsnc`, `assets`, `cashneq` |
| 11 | `f102_trading_liquidity` | `volume_shock_vs_average` | 91 | `volume`, `volumeavg1m`, `volumeavg3m` |
| 12 | `f22_debt_mix` | `current_noncurrent_debt_mix` | 91 | `debtc`, `debtnc`, `debt` |
| 13 | `f103_corporate_action_risk` | `split_ticker_change_instability` | 90 | `action`, `value` |
| 14 | `f106_institutional_security_mix` | `warrant_debt_preferred_overhang` | 90 | `wntholders`, `dbtholders`, `prfholders`, `wntvalue`, `dbtvalue`, `prfvalue`, `totalvalue` |
| 15 | `f104_event_code_intensity` | `event_code_entropy` | 89 | `eventcodes` |
| 16 | `f73_market_cap` | `marketcap_liquidity_turnover` | 89 | `marketcap`, `closeadj`, `volume` |
| 17 | `f107_listing_lifecycle_metadata` | `public_age_and_delisting_pressure` | 88 | `firstpricedate`, `lastpricedate`, `isdelisted`, `date` |
| 18 | `f77_price_book` | `normalized_price_book_validity` | 88 | `pb`, `pb_normalized`, `has_negative_pb`, `has_negative_equity` |
| 19 | `f104_event_code_intensity` | `event_code_transition_rate` | 87 | `eventcodes` |
| 20 | `f109_valuation_normalization_flags` | `negative_valuation_flag_blend` | 87 | `has_negative_pe`, `has_negative_pb`, `has_negative_earnings`, `has_negative_equity`, `alternative_valuation_needed` |
| 21 | `f21_total_debt` | `noncurrent_debt_load` | 86 | `debtnc`, `debt`, `assets`, `marketcap` |
| 22 | `f95_event_density` | `event_code_specific_density` | 86 | `eventcodes` |
| 23 | `f38_tangible_book` | `diluted_tangible_book_per_share` | 85 | `tbvps`, `bvps`, `shareswadil`, `equity`, `intangibles` |
| 24 | `f55_eps_level` | `diluted_usd_eps_context` | 84 | `eps`, `epsdil`, `epsusd`, `pe`, `pe1` |

## Approved Pending Candidates

| Rank | Family | Placement | Candidate | Score | Novel source fields | Expected signal | Guard |
| ---: | --- | --- | --- | ---: | --- | --- | --- |

## Implementation Bias

The best first implementation batch should be small and source-aware, not a broad mechanical template expansion. Prioritize:

1. `f105_insider_transaction_microstructure`: transaction-code-weighted Form 4 flow is strongly differentiated from existing broad insider value signals.
2. `f103_corporate_action_risk`: bankruptcy, delisting, split, and ticker-change histories add real distress/event content.
3. `f102_trading_liquidity`: volume and dollar-volume turnover add an important tradability layer missing from the current features.
4. `f106_institutional_security_mix`: put/call/warrant/debt/preferred mixes are materially different from current value/unit ownership features.
5. `f108_true_sector_industry_relative`: only if the feature pipeline can perform point-in-time peer grouping without lookahead.

## Rejected Candidates

No candidates were rejected in this audition pass.

## Next Gate Before Code Generation

- Define upstream derived columns for categorical sources before writing signal functions: action-type indicators, parsed event-code indicators, transaction-code buckets, and security-type mixes.
- Generate additions into new files only: new families as `f101+`, existing-family additions as `*_151_225_claude.py` files.
- Re-run this audition script after any generated feature files are added; any newly duplicated name or signature should fail the gate before more code is produced.
