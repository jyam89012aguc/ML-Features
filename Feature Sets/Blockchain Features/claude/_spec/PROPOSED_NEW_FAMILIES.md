# Proposed additional feature families (f31+)

The current 30 families use OHLCV + fundamentals(SF1) + 13F aggregates(sf3a/sf3b).
The DB contains THREE strong, currently-unused signal sources. Each supports new
families that are genuinely orthogonal to the existing 30 (verified feasible by
coverage queries on the crypto universe).

## A. Insider transactions — table `main.sf2` (11.2M rows, good crypto coverage)
Columns: transactioncode (P=open-market buy, S=sell, M=option exercise, A=grant,
F=tax), transactionshares/value/pricepershare, isofficer/isdirector/
istenpercentowner, officertitle, ownername. Coverage on crypto names is real:
WULF 258 buys, COIN 43, RIOT 30, MSTR 29, MARA 22; sells far more frequent.
Insider open-market buying is one of the best-documented predictive signals and is
uncorrelated with price/fundamental features.

- **f31_insider_buying_pressure** — net open-market buy/sell ratio (count & $value),
  trailing-3/6/12m buy intensity, # distinct buying insiders, cluster-buy detection,
  days-since-last-buy decay, buy value / marketcap.
- **f32_insider_conviction_quality** — officer/director buys vs 10%-owner buys,
  CEO/CFO-specific buys (officertitle), average purchase size vs insider's holdings,
  buy-at-price vs current price (conviction premium), direct vs indirect ownership.
- **f33_insider_distribution_selling** — selling intensity & acceleration, option-
  exercise-and-dump (M followed by S), 10%-owner liquidation, sell $/marketcap,
  net-share-shrinkage from insider exits, sell-cluster z-score.

## B. Institutional holder breadth — table `main.sf3` long-form (45.6M rows)
Per investor × securitytype holdings (value, units, price). The current f28/f29/f30
use the sf3a/sf3b AGGREGATES; the long form exposes HOLDER-LEVEL breadth that the
aggregates hide. Crypto coverage is rich: distinct holders/quarter COIN ~689,
MSTR ~390, MARA ~194.

- **f34_institutional_breadth_churn** — number of distinct 13F holders & its growth,
  new-holder entry rate, holder exit/churn rate, holder-base HHI (concentration across
  investors, distinct from f29's single-holding percentoftotal), average position size,
  breadth-vs-price divergence, smart-holder accumulation breadth.

## C. Composite distress / manipulation scores — existing SF1 fundamentals
All required fields have 92–100% coverage on the crypto universe. These are classic,
battle-tested multi-factor scores, distinct from the current single-axis fundamental
families (f16–f25) because they COMBINE several inputs into established formulas.

- **f35_financial_distress_score** — Altman-Z (and Z'' for non-manufacturers):
  workingcapital/assets, retearn/assets, ebit/assets, equity/liabilities, revenue/
  assets; Ohlson O-score components; distance-to-default proxies; runway-adjusted
  distress. Highly relevant — many miners are bankruptcy-risk names (CORZ, SDIG, GREE).
- **f36_earnings_manipulation_score** — Beneish M-score components: DSRI (receivables/
  revenue change), GMI (gross-margin index), AQI (asset-quality), SGI (sales growth),
  DEPI (depreciation), SGAI, LVGI (leverage), TATA (total accruals). Flags aggressive
  accounting — important given crypto-mark/impairment games.

## D. Derived cross-sectional / sector-factor family (needs one plumbing change)
- **f37_crypto_sector_relative_strength** — decompose each name vs an equal-weight
  crypto-equity index built from the universe: sector beta, idiosyncratic (residual)
  momentum, up/down beta asymmetry, correlation-to-sector regime, relative strength vs
  sector bellwethers (COIN/MSTR). REQUIRES passing a precomputed `sector_index` Series
  as an extra input column (small pipeline addition) — the only proposal that isn't
  drop-in. High value: separates systematic crypto-beta from stock-specific alpha.

## Recommended priority
1. f31–f33 insider (sf2) — highest orthogonality, strong literature, drop-in.
2. f35–f36 distress/manipulation — drop-in, very relevant to miner blow-up risk.
3. f34 institutional breadth — drop-in.
4. f37 sector-relative — highest analytical value but needs the sector-index input.

Each would follow the exact same 4-file / 450-feature structure and the build_
derivatives.py pipeline, so they slot in as f31…f37 with no rework of f01–f30.
