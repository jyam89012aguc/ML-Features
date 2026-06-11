# Biotech Feature Gap Review

SilverDB reference: `C:\Users\jyama\Desktop\silver db\trading.duckdb`

Reviewed tables: `fundamentals`, `sep`, `sfp`, `daily_prices`, `metrics`, `sf2`, `sf3`, `sf3a`, `sf3b`, `tickers`, `events`, `actions`, `sp500`, `indicators`.

## Additions And Fixes

- Added `f101_market_momentum_risk`, a source-backed family using the unused `metrics` table fields: beta, moving averages, high/low ranges, trailing returns, average volume, and dividend yield.
- Added `f102_institutional_derivative_positioning`, using SF3A/SF3B holder-type fields for call/put, warrant, debt, preferred, fund, and non-common exposure.
- Added `f103_insider_code_and_role_signals`, using SF2 transaction codes, derivative/non-derivative security codes, insider roles, restated form flags, exercise moneyness, and ownership changes.
- Added `f104_event_action_categorical_signals`, using EVENTS/ACTIONS/SP500 categorical codes for event-code groups, delistings, splits, ticker changes, M&A, distress, and index changes.
- Added `f105_security_master_quality_flags`, using TICKERS and validated table flags for exchange/listing status, biotech filters, shell/SPAC flags, data-quality flags, negative fundamental flags, and listing age.
- Added `f106_underused_fundamental_fields`, using previously underused FUNDAMENTALS fields: `accoci`, non-current assets/liabilities/investments, USD-normalized metrics, FX, discontinued/non-controlling income, full cash-flow fields, tax liabilities, forward valuation fields, and `ros`.
- Added `f107_text_category_and_specialist_signals`, using remaining SF2/SF3/TICKERS/INDICATORS text and category fields for specialist investors, passive holders, activist/event investors, officer titles, ownership nature, security type, indicator metadata, SIC/Fama healthcare tags, currency, CUSIP, and permaticker availability.
- Rebound `f092_insider_transaction_flow` from non-existent `transactionprice` to silverdb `transactionpricepershare`.
- Rebound `f098_corporate_action_events` from non-existent `actionvalue` to silverdb `actions.value`.
- Recovered and source-bound accounting alias families:
  - `f026_preferred_and_convertible_overhang`: `prefdivis`, `debtusd`, `assets`, `marketcap`, `equity`, `debt`.
  - `f041_intangibles_goodwill`: `intangibles`, `depamor`, `assets`, `equity`.
  - `f052_operating_margin`: `opinc`, `revenue`, `opex`, `assets`.
  - `f062_impairment_risk_proxy`: `intangibles`, `depamor`, `assets`, `equity`.
  - `f074_dividend_and_payout_valuation`: `dps`, `ncfdiv`, `payoutratio`, `value`.

## Best Set

Use the family set below as the first-pass model feature set. It favors fields that are present in silverdb and economically meaningful for biotech, where liquidity, runway, dilution, R&D intensity, ownership, catalysts, and market context generally matter more than stable-profitability ratios.

Core liquidity/runway:
`f001` through `f015`

R&D and operating spend:
`f016` through `f021`, plus `f055`

Capital structure and dilution:
`f022` through `f038`

Balance-sheet quality:
`f039` through `f045`, plus `f058` through `f062`

Commercialization and margins:
`f046` through `f054`, but treat EPS families `f056` and `f057` as secondary for pre-revenue biotech.

Efficiency and valuation:
`f063` through `f073`, with emphasis on `f069`, `f070`, `f071`, and `f072`.

Fundamental dynamics:
`f075` through `f079`.

Security master and tradability:
`f081` through `f091`.

Ownership, events, and index context:
`f092` through `f100`.

New market context:
`f101_market_momentum_risk`.

Additional source-backed gap-fill batches:
`f102_institutional_derivative_positioning`, `f103_insider_code_and_role_signals`, `f104_event_action_categorical_signals`, `f105_security_master_quality_flags`, `f106_underused_fundamental_fields`, and `f107_text_category_and_specialist_signals`.

## Batch Review Results

Batch 1, SF1 fundamentals:
The original 100 families cover most core liquidity, runway, valuation, profitability, R&D, dilution, and balance-sheet fields. Remaining useful SF1 gaps were added in `f106`, mainly USD normalization, non-current composition, OCI, discontinued/non-controlling income, FX, tax liability, and forward valuation fields.

Batch 2, SEP/SFP/DAILY/METRICS market data:
The original market families cover OHLCV and daily valuation context. `metrics` was unused, so `f101` adds beta, moving-average trend, high/low range position, trailing returns, average volume, and dividend-yield maturity flags.

Batch 3, SF2 insider data:
The original insider families used generic transaction flow and ownership amounts, but did not model transaction codes or roles explicitly. `f103` adds purchase/sale/award/exercise flags, role-weighted net value, derivative security flags, exercise moneyness, ownership change, and restated-form flags.

Batch 4, SF3/SF3A/SF3B institutional ownership:
The original ownership families used aggregate `value`, `units`, and `price`, but left SF3A/SF3B holder-type matrices mostly untouched. `f102` adds option, warrant, debt/preferred, fund, non-common, breadth, and short-bias signals.

Batch 5, EVENTS/ACTIONS/SP500:
The original event/action families modeled generic density/value. `f104` adds categorical event-code and action-type signals for distress, listing changes, splits, ticker changes, M&A, spinoffs, counterparty presence, and index additions/removals.

Batch 6, TICKERS/quality metadata:
The original metadata families are broad but mostly numeric. `f105` adds explicit exchange, delisting, biotech/medical-device/shell flags, listing age, related ticker/site/filing coverage, quality flags, negative fundamental flags, and normalized valuation fallbacks.

Batch 7, text/category fields:
After batches 1-6, the remaining unused silverdb fields were text identifiers, security types, officer titles, ownership nature, indicator metadata, SIC/Fama tags, and date/flag metadata. `f107` adds compact category features from those fields, while `f103` and `f105` now also cover the remaining date and flagged-reason fields.

Final direct-source audit:
All non-internal silverdb columns across the reviewed tables are now represented by at least one feature input, excluding row identifiers and the intentionally ignored universal join keys (`ticker`, `date`, `name`, `lastupdated`). The only remaining non-source parameters in the repo are derived fields expected by older generated families: `filingage`, `revisioncount`, `sector_rank`, `listingage`, `ticker_change_count`, `field_coverage`, and `eventcount`.

## Lower Priority Or Derived Inputs

These families can still be useful, but they require derived fields or careful pre-aggregation before direct silverdb binding:

- `f079_reporting_recency`: expects `filingage`, which should be derived from `datekey` versus `reportperiod` or the feature date.
- `f080_restatement_and_revision_proxy`: expects `revisioncount`, derivable from repeated `lastupdated` or filing revisions.
- `f082_sector_industry_biotech_filter`: expects `sector_rank`, derivable from `tickers.sector`, `industry`, and `sicindustry`.
- `f083_listing_status_and_dates`: expects `listingage`, derivable from `firstpricedate`.
- `f084_ticker_changes_and_permaticker`: expects `ticker_change_count`, derivable from ticker history/related tickers.
- `f085_indicator_availability`: expects `field_coverage`, derivable from `indicators` and table-level non-null coverage.
- `f099_sec_8k_event_density`: expects `eventcount`, derivable from `events.eventcodes`.

Do not add clinical-trial, FDA-calendar, patent, grant, publication, or pipeline-stage features from this silverdb alone. Those would be good biotech features, but this database does not contain the required source tables.
