# Feature Expansion Audit

Audit date: 2026-05-25

## Current Coverage

- 100 feature families: `f01` through `f100`.
- 400 Python files total: each family has two base files, one second-derivative file, and one third-derivative file.
- 45,000 signal functions total.
- Every file follows the generated count pattern: base files contain 75 signals each, derivative files contain 150 signals each.
- No central manifest, loader, test suite, README, or registry file was present in this workspace.

## Structural Finding

The existing feature set is already dense and mechanically complete. Adding `v151+` functions inside existing families would break the visible `001_075` / `076_150` convention unless the whole naming scheme is expanded. The cleaner path is to add new feature families, starting at `f101`, or to add a separate derived-composite layer that consumes the existing 45,000 signals.

## High-Value Feature Gaps

These are the strongest candidates for additional biotech-specific features.

| Candidate family | Uses existing fields? | Notes |
| --- | --- | --- |
| `f101_cash_burn_composite` | Yes | Combine cash, liquid resources, burn, runway, financing, and dilution into near-term funding stress features. |
| `f102_rnd_efficiency` | Yes | R&D spend relative to burn, assets, market cap, revenue, and capital raised. Useful for biotech where R&D is the operating core. |
| `f103_financing_pressure` | Yes | Blend runway, free cash flow, capital raised, issuance cadence, debt, and dilution into financing-risk features. |
| `f104_shareholder_dilution_quality` | Yes | Combine share growth, SBC, convertibles, equity issuance, and market-cap context. |
| `f105_balance_sheet_resilience` | Yes | Composite liquidity, leverage, tangible book, current ratio, and net cash features. |
| `f106_profitability_inflection` | Yes | Combine margin improvement, breakeven proximity, OCF, FCF, net income, and revenue acceleration. |
| `f107_revenue_durability` | Yes | Revenue growth, stability, deferred revenue, receivables, gross margin, and quality proxies. |
| `f108_investor_support_signal` | Yes | Insider flow, institutional ownership, specialist funds, holder concentration, and accumulation/distribution. |
| `f109_valuation_vs_fundamentals` | Yes | EV/revenue, EV/R&D, price/book, market cap/net cash, revenue per share, and R&D intensity. |
| `f110_distress_event_blend` | Yes | Distress flags, event density, capital actions, price context, regime change, and funding pressure. |

## Feature Families Requiring New Upstream Data

These would be very valuable for biotech, but cannot be built honestly from the current financial/market field set alone.

| Candidate family | Required inputs |
| --- | --- |
| Clinical trial catalyst calendar | Trial phase, expected readout dates, enrollment status, indication, primary endpoint, trial status. |
| FDA/regulatory event risk | PDUFA dates, IND/BLA/NDA status, CRL history, advisory committee dates, fast-track/breakthrough designations. |
| Pipeline concentration | Asset count, lead asset phase, indication count, modality, single-asset dependency flag. |
| Partnership quality | Collaboration revenue, milestone structure, partner identity, opt-in/out terms, royalty rates. |
| Patent/exclusivity runway | Patent expiry, orphan exclusivity, composition-of-matter coverage, litigation status. |
| Commercial launch traction | Prescription volume, patient starts, gross-to-net, payer coverage, inventory channel data. |
| Trial financing coverage | Expected trial cost, active study count, phase-specific burn estimates, cash runway to readout date. |

## Recommended Implementation Path

1. Add `f101` through `f110` as composite feature families built only from existing fields.
2. Keep each new family self-contained with the same helper function style used by the current files.
3. Preserve the existing convention: two base files with 75 signals each, one second-derivative file with 150 signals, and one third-derivative file with 150 signals.
4. Add a lightweight manifest before generating many more files. At minimum it should record family id, family name, category, source fields, output files, and signal count.
5. Add a validation script that parses all Python files and checks:
   - every signal name is unique;
   - every signal function returns a pandas-compatible object;
   - every file parses successfully;
   - function counts match the file naming convention;
   - no function references fields outside the accepted input schema.

## Immediate Safe Additions

If the next step is to generate more features immediately, the safest first batch is:

- `f101_cash_burn_composite`
- `f102_rnd_efficiency`
- `f103_financing_pressure`
- `f104_shareholder_dilution_quality`
- `f105_balance_sheet_resilience`

These can be built from fields already present in existing function signatures: `cashneq`, `assets`, `assetsc`, `marketcap`, `debt`, `debtc`, `equity`, `revenue`, `rnd`, `ncfo`, `fcf`, `capex`, `ncff`, `sharesbas`, `shareswa`, `sbcomp`, `prefdivis`, `ncfcommon`, `closeadj`.

## Caution

Several existing high-level families such as `f98_lifecycle_stage`, `f99_sector_relative`, and `f100_composite_distress` appear to use the same generic field templates as earlier financial families. Before adding many more generated functions, it is worth deciding whether the goal is broad numeric coverage or domain-faithful biotech factors. The best incremental value likely comes from cross-family composites and true biotech event data, not more copies of the same transformations.

## Silver DB Expansion Check

Database inspected: `C:\Users\jyama\Desktop\silver db\trading.duckdb`

The silver database materially expands the safe feature space. It contains core source tables for fundamentals, prices, valuation, corporate actions, events, insider transactions, institutional holdings, aggregate 13F ownership, ticker metadata, and data-quality state.

### Relevant Tables

| Table | Rows | Feature relevance |
| --- | ---: | --- |
| `fundamentals` | 3,071,787 | Existing financial fields plus many unused fundamentals and normalized valuation flags. |
| `sep` | 45,758,346 | OHLCV daily prices; current features mostly use `closeadj`, leaving open/high/low/volume unused. |
| `daily_prices` | 39,143,336 | Daily market cap and valuation multiples; `pe`, `ps`, `evebitda` are unused. |
| `metrics` | 30,631 | Beta, moving averages, 52-week/5-year highs/lows, returns, volume averages. |
| `actions` | 633,897 | Dividends, listings, delistings, ticker changes, splits, acquisitions, bankruptcies. |
| `events` | 2,482,700 | Event-code histories suitable for event-density and event-type features. |
| `sf2` | 11,175,881 | Insider transaction details, prices, shares, role flags, derivative/non-derivative codes. |
| `sf3` | 45,597,224 | Institutional holdings by security type. |
| `sf3a` | 621,602 | Aggregate institutional holders, units, and value by security type per ticker/date. |
| `sf3b` | 273,127 | Aggregate institutional holdings by investor/date. |
| `tickers` | 60,081 | Sector, industry, category, delisting, exchange, first/last dates, ticker metadata. |

### Unused Fields That Support New Feature Families

| Feature area | Unused silver fields |
| --- | --- |
| Price technicals | `open`, `high`, `low`, `volume`, `closeunadj`, `ma50d`, `ma200d`, `ma50w`, `ma200w`, `high52w`, `low52w`, `high5y`, `low5y`, `returnytd`, `return1y`, `return5y`, `beta1y`, `beta5y`, `volumeavg1m`, `volumeavg3m` |
| Valuation variants | `pe`, `pe1`, `ps`, `ps1`, `evebitda`, `pb_normalized`, `pe_normalized`, `alternative_valuation_needed` |
| Fundamental depth | `cashnequsd`, `assetsavg`, `assetsnc`, `debtnc`, `debtusd`, `liabilitiesc`, `liabilitiesnc`, `investments`, `investmentsc`, `investmentsnc`, `ppnenet`, `bvps`, `tbvps`, `shareswadil`, `revenueusd`, `ebit`, `ebt`, `gp`, `cor`, `roe`, `ros`, `fcfps`, `payoutratio`, `taxassets`, `taxliabilities` |
| Corporate actions | `action`, `value`, `contraticker`, `contraname`; observed actions include dividends, listings, delistings, ticker changes, splits, acquisitions, bankruptcies, regulatory delistings, and spinoffs. |
| Events | `eventcodes`; observed event-code combinations include `81`, `34`, `22|91`, `81|91`, `35`, `71|91`, `52`, and many multi-code combinations. |
| Insider transactions | `transactioncode`, `securityadcode`, `transactionshares`, `transactionpricepershare`, `sharesownedbeforetransaction`, `priceexercisable`, `isdirector`, `isofficer`, `istenpercentowner`, `officertitle`, `securitytitle`, `directorindirect`, `natureofownership`, `dateexercisable`, `expirationdate` |
| Institutional ownership | `securitytype`, `price`, `shrholders`, `putholders`, `cllholders`, `wntholders`, `dbtholders`, `prfholders`, `fndholders`, `shrunits`, `putunits`, `cllunits`, `wntunits`, `dbtunits`, `prfunits`, `fndunits`, matching value columns, `totalvalue`, `percentoftotal` |
| Ticker metadata | `sector`, `industry`, `sicsector`, `sicindustry`, `category`, `exchange`, `isdelisted`, `firstpricedate`, `lastpricedate`, `firstquarter`, `lastquarter`, `location`, `currency` |

### New Feature Families Enabled By Silver DB

These are genuinely new families rather than small variants of existing features.

| Proposed family | Primary source tables | Duplication risk | Rationale |
| --- | --- | --- | --- |
| `f101_price_volume_technicals` | `sep`, `metrics` | Low | Current feature code mostly ignores OHLCV, beta, moving averages, volume averages, and distance from highs/lows. |
| `f102_trading_liquidity` | `sep`, `metrics`, `daily_prices` | Low | Adds turnover, dollar volume, volume shocks, liquidity droughts, and price-impact proxies. |
| `f103_corporate_action_risk` | `actions`, `sp500` | Low | Uses listed/delisted/split/acquisition/bankruptcy/ticker-change histories not present in current function signatures. |
| `f104_event_code_intensity` | `events` | Medium | Existing `f95_event_density` uses an `eventcount` placeholder, but not raw `eventcodes`; avoid simple count duplicates by encoding event types and transitions. |
| `f105_insider_transaction_microstructure` | `sf2` | Medium | Existing insider families use broad transaction value and ownership fields; unused transaction codes, prices, shares, role flags, derivative flags, and exercise terms can add detail. |
| `f106_institutional_security_mix` | `sf3`, `sf3a`, `sf3b` | Low | Current institutional features use `value` and `units`; aggregate put/call/warrant/debt/preferred/fund holder and value mixes are unused. |
| `f107_listing_lifecycle_metadata` | `tickers`, `actions`, `sep` | Low | First/last price dates, delisting state, exchange, category, and listing-age features are absent. |
| `f108_sector_industry_relative` | `tickers`, `fundamentals`, `daily_prices` | Medium | Existing `f99_sector_relative` exists, but code appears template-based; implement true industry-relative transforms using `sector`, `industry`, and biotech peer groups. |
| `f109_valuation_normalization_flags` | `fundamentals`, `daily_prices` | Low | Uses normalized PE/PB flags and negative valuation flags that are not used by current features. |
| `f110_capital_structure_detail` | `fundamentals`, `sf3a` | Low | Adds debt maturity mix proxies, current/noncurrent liability mix, investments liquidity, preferred/debt institutional holder mix. |

### Safe Additions Inside Existing Families

Yes, more features can also be added inside existing feature families without high duplication risk, but the additions should use silver fields not currently present in that family.

| Existing family | Safe additions from silver DB | Duplication guard |
| --- | --- | --- |
| `f21_total_debt` / `f22_debt_mix` | `debtnc`, `debtusd`, `ncfdebt`, current vs noncurrent debt/liability mixes | Do not duplicate existing `debt`/`debtc` transforms. Require names to include the new source field. |
| `f24_interest_coverage` | `ebit`, `ebt`, `ebitusd`, `ebitdamargin`, `intexp` combinations | Avoid existing `ebitda`-only coverage variants. |
| `f35_total_assets` / `f36_asset_composition` | `assetsavg`, `assetsnc`, `investments`, `investmentsc`, `investmentsnc`, `ppnenet` | Treat as composition subfeatures, not another total-assets smoothing template. |
| `f38_tangible_book` | `bvps`, `tbvps`, `equityusd`, `shareswadil` | Add per-share and diluted tangible-book variants, not duplicate `tangibles` transforms. |
| `f42`-`f47` revenue families | `revenueusd`, `ps`, `ps1`, `deferredrev`, `receivables`, `cor`, `gp` | Use USD revenue, price/sales, gross profit, and cost-of-revenue ratios. |
| `f48`-`f53` margin/profitability families | `gp`, `cor`, `ebit`, `ebt`, `roe`, `ros`, `ebitdamargin` | Avoid repeating `grossmargin`, `netmargin`, `ebitda` transforms. |
| `f55_eps_level` / `f56_earnings_sign` | `epsdil`, `epsusd`, `pe`, `pe1`, negative earnings flags | Separate basic, diluted, USD, and valuation-context EPS features. |
| `f73`-`f79` valuation families | `pe`, `pe1`, `ps`, `ps1`, `evebitda`, `pe_normalized`, `pb_normalized`, `alternative_valuation_needed` | Current features already include EV/revenue, EV/R&D, PB, and standard multiples; only add unused multiple variants and flags. |
| `f85`-`f89` insider families | `transactioncode`, `transactionshares`, `transactionpricepershare`, `sharesownedbeforetransaction`, `isdirector`, `isofficer`, `istenpercentowner`, `priceexercisable`, `expirationdate` | Do not add broad buy/sell value counts already covered by `transactionvalue`; focus on transaction type, role, derivative/exercise structure, and ownership-before/after deltas. |
| `f90`-`f93` institutional families | `securitytype`, `shrholders`, `putholders`, `cllholders`, `wntholders`, `dbtholders`, holder/value/unit mixes | Avoid plain `value`/`units`; use security-type mix, options skew, warrant/debt/preferred exposure, and holder concentration components. |
| `f94_capital_actions` | `action`, `value`, `contraticker`, `contraname` from `actions` | Use action-type-specific cadence and severity; avoid generic event count features. |
| `f95_event_density` | parsed `eventcodes`, event-code transitions, event-code entropy | Existing placeholder `eventcount` makes simple event counts duplicative. Use event-code composition instead. |
| `f97_multi_year_price_context` | `high52w`, `low52w`, `high5y`, `low5y`, `return1y`, `return5y`, `returnytd`, moving averages | Avoid reusing only `close`; compute distance-to-range, drawdown, recovery, beta-adjusted context. |
| `f99_sector_relative` | `sector`, `industry`, `sicsector`, `sicindustry`, `category`, biotech peer flags | Only add if loader can supply peer-relative inputs; otherwise this remains a naming-only family. |

### Duplication-Control Rules

Before adding functions, apply these checks:

1. Parse all existing signal functions and reject any proposed function name already present.
2. Reject any proposed source-field/window/operation tuple already represented in the same family.
3. Require every in-family addition to use at least one source field not already used by that family, unless it is a true cross-field composite.
4. Put `v151+` additions into new files such as `f21_total_debt_base_151_225_claude.py` rather than editing the existing `001_075` or `076_150` files.
5. For families with placeholder arguments that do not directly exist in silver DB, such as `eventcount`, `distressflag`, and `actionvalue`, define the upstream derivation explicitly before generating more downstream features.

### Bottom Line

- More feature families can be added from silver DB with low duplication risk.
- More features can be added inside existing families, also with low duplication risk, if they use currently unused silver DB columns and are placed in new `151+` files.
- The highest-value near-term expansion is not more rolling transforms over the same 58 arguments; it is adding source-aware features from OHLCV, actions, event codes, detailed SF2 transactions, SF3 security-type mixes, and ticker metadata.

### Audition Artifact

A repeatable audition gate now exists in `audition_feature_additions.py`. It parses the existing signal library, checks the silver DB schema, evaluates curated additions for duplicate risk and source-field novelty, and writes:

- `FEATURE_ADDITION_AUDITION.md`
- `feature_addition_audition.json`

### Implemented Additions

The source-aware implementation batches added 486 new signal functions. This includes 9 new families plus `v151-v156` additions inside 9 existing families. Every addition has base, second-derivative slope, and third-derivative acceleration coverage:

| Family | File | Signals | Main source fields |
| --- | --- | ---: | --- |
| `f101_price_volume_technicals` | `f101_price_volume_technicals_base_001_012_claude.py` | 12 | `price`, `high52w`, `low52w`, `high5y`, `low5y`, `ma50d`, `ma200d`, `ma50w`, `ma200w`, `beta1y`, `beta5y`, `return1y`, `return5y` |
| `f102_trading_liquidity` | `f102_trading_liquidity_base_001_012_claude.py` | 12 | `volume`, `volumeavg1m`, `volumeavg3m`, `closeadj`, `marketcap` |
| `f103_corporate_action_risk` | `f103_corporate_action_risk_base_001_012_claude.py` | 12 | `action`, `value` |
| `f104_event_code_intensity` | `f104_event_code_intensity_base_001_012_claude.py` | 12 | `eventcodes` |
| `f105_insider_transaction_microstructure` | `f105_insider_transaction_microstructure_base_001_012_claude.py` | 12 | `transactioncode`, `transactionshares`, `transactionpricepershare`, `transactionvalue`, `securityadcode`, role flags |
| `f106_institutional_security_mix` | `f106_institutional_security_mix_base_001_012_claude.py` | 12 | put/call/warrant/debt/preferred/fund holder and value fields from `sf3a` |
| `f107_listing_lifecycle_metadata` | `f107_listing_lifecycle_metadata_base_001_012_claude.py` | 12 | `date`, `firstpricedate`, `lastpricedate`, `isdelisted`, `exchange`, `category`, `industry`, `sicindustry` |
| `f108_true_sector_industry_relative` | `f108_true_sector_industry_relative_base_001_012_claude.py` | 12 | point-in-time industry peer medians and percentiles |
| `f109_valuation_normalization_flags` | `f109_valuation_normalization_flags_base_001_012_claude.py` | 12 | `has_negative_pe`, `has_negative_pb`, `has_negative_earnings`, `has_negative_equity`, `alternative_valuation_needed`, `pb_normalized`, `pe_normalized` |
| `f21_total_debt` | `f21_total_debt_base_151_156_claude.py` | 6 | `debtnc`, `debtusd`, `ncfdebt` |
| `f22_debt_mix` | `f22_debt_mix_base_151_156_claude.py` | 6 | `debtnc`, `liabilitiesc`, `liabilitiesnc` |
| `f36_asset_composition` | `f36_asset_composition_base_151_156_claude.py` | 6 | `investments`, `investmentsc`, `investmentsnc`, `ppnenet` |
| `f73_market_cap` | `f73_market_cap_base_151_156_claude.py` | 6 | `volume`, `volumeavg1m` |
| `f77_price_book` | `f77_price_book_base_151_156_claude.py` | 6 | `pb_normalized`, `has_negative_pb`, `has_negative_equity` |
| `f95_event_density` | `f95_event_density_base_151_156_claude.py` | 6 | `eventcodes` |
| `f97_multi_year_price_context` | `f97_multi_year_price_context_base_151_156_claude.py` | 6 | `price`, `high52w`, `low52w`, `high5y`, `low5y`, `beta1y`, `beta5y` |
| `f38_tangible_book` | `f38_tangible_book_base_151_156_claude.py` | 6 | `tbvps`, `bvps`, `shareswadil`, `price` |
| `f55_eps_level` | `f55_eps_level_base_151_156_claude.py` | 6 | `epsdil`, `epsusd`, `pe`, `pe1` |

Derivative files added for each new family:

- `*_2nd_derivatives_001_012_claude.py`
- `*_3rd_derivatives_001_012_claude.py`

Post-addition validation found 454 Python feature files, 45,486 total signal functions, and 0 duplicate signal names. Compile and runtime smoke checks passed for all 486 new functions added from the audition.
