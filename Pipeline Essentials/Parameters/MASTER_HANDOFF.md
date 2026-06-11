# MASTER HANDOFF — 10-bagger feature pipeline (complete spec, all parameters, 7-yr/28-quarter, SEC granular)
*2026-06-04. Consolidates the Technology Features run + every correction. This is the single source of truth.
Companion docs: SEVEN_YEAR_RECOMPUTE_SPEC.md, TRAIN_TEST_WINDOW_TEMPLATE.md, IMPROVEMENT_HANDOFF.md,
NEXT_PIPELINE_NOTES.md. Where they conflict, THIS doc wins.*

====================================================================================================
## PART 1 — ALL PARAMETERS & THRESHOLDS (exact)
====================================================================================================
| Parameter | Value used (TF) | Notes / recommended |
|---|---|---|
| REGIME_START | 2010-01-01 | No window may cross before this (2009 = different regime). Hard rule. |
| Pit (q0) | multi-year-low capitulation | min daily LOW within the split window; verified at the 3-yr low. |
| Split windows (pit selection) | train 2010-01→2013-07, test 2013-07→2019-12 | from `build_winners_controls_wide_panel.py`. |
| WINNER_THRESHOLD (panel) | 3.0× | loose pool for breadth. |
| WINNER_THRESHOLD (strict, Stage-4) | **10.0×** | the real 10-bagger cut, applied in `regime_clean`. |
| Control definition | < 3× (median ~1.9×, 1.0–3.0×) | matched 1:1. **BUG: matched on mcap only — must add date (Part 4).** |
| FORWARD_WINDOW_DAYS | 1260 (5 yr) | window to measure peak/return_multiple. |
| PIT_BUFFER_DAYS | 20 | mcap read lagged 20d before entry (no look-ahead). |
| MIN_ENTRY_PRICE | 0.01 | drop sub-penny entries. |
| MIN_HISTORY_DAYS | 50 | need ≥50 days before the pit. |
| ARTIFACT_RATIO_THRESHOLD | 20.0 | drop bad-print spikes (high/low > 20×). |
| Market-cap band (target) | $50M–$3B (winners median **$14M** at pit) | winners are nano/micro-cap. |
| Coverage filter | ≥ 0.80 | drop sparse features before importance. |
| Bootstrap rounds | 15 | XGB + LGBM gain consensus. |
| XGB params | max_depth 4, eta 0.1, subsample 0.8, colsample 0.3, aucpr | |
| Cannibalization corr | |r| ≥ 0.92 | keep highest-rank rep per cluster. |
| TARGET significant K | **~500–1,500** (NOT 10k) | validation peaks ~500, dilutes past ~1,500. |
| Hash precision | 12 sig figs | dedup hashing. |
| Workers | **8 max** (64GB box) | 10 OOMs; recycling OFF (deadlocks). |
| Validation | **chronological only** | random CV inflates ROC-AUC ~+0.14. |

**Result snapshot:** 138,744 registered → 122,541 computed → 84,619 distinct → 500 significant → 329 reps.
Random-CV ROC 0.887 / PR 0.898; **honest chronological out-of-time ROC ≈ 0.74**. Winners: 452 ≥3× → **220 ≥10×** → 208 post-mask.

====================================================================================================
## PART 2 — 7-YEAR / 28-QUARTER TEST (no data left out)
====================================================================================================
**Goal:** use the FULL chronological history so no quarter is left out — stable derivatives + lifecycle signal.
Panel already holds **15 yrs of daily data (2010-01-04 → 2024-12-31)**; 9,296 features already use ≥8q windows at
51% coverage, only 2% NaN → the long data is REAL.

**Window set (compute ALL of these per metric — leave no quarter out):**
`1q(63d), 2q(126d), 4q(252d), 8q(504d), 12q(756d), 20q(1260d), 28q(1764d)` + an EXPANDING "all-available-history-
to-28q" window for partial-history (early) pits.

**Derivatives — replace the broken `diff().diff()`:** fit a least-squares polynomial (deg 1/2/3) over each
window → leading coefficient = slope/accel/jerk, computed from MANY points (12–28q), not 3. Savitzky-Golay
(`scipy.signal.savgol_filter(deriv=k)`) is the fast equivalent. (Old d2/d3 were 3-point spikes → noise → low signal.)

**Regime gating (keeps no-cross-2010):** 28q clean only for pits ≥ 2017 (104 of 440 strict). Earlier pits use the
expanding window (available history back to 2010 only); `regime_clean` NaN-masks any cell reaching pre-2010. No
pre-2010 data is ever fed. `parse_win` must read up to `1764d`/`28q` tokens.

**ADDITIVE build (no recompute, no delete):** author the new long-window + polynomial files → register as
**build 12 = additions only** (source-json points at ONLY the new files) → compute `--registry-build-id 12
--data-snapshot-id snapshot_tech_build11 --skip-existing` → only new features compute → re-dedup → re-rank over
the combined set. New artifacts ≈ 0.7–0.9 TB; **E: free = 1.78 TB → fits, keep the old data.**

====================================================================================================
## PART 3 — VALIDATION (balanced + unbiased + chronological)
====================================================================================================
- **Target:** prefer **continuous `log(return_multiple)`** (XGB regressor / LambdaMART). Ranks size-of-win; the
  out-of-time top-10 had **median 54× actual return** vs 8× baseline. Keep a binary ≥10× model for comparison.
- **Split:** chronological by pit date. **Do NOT use the naive matched-pair split** — controls sit a median ~4 yrs
  from their winners (mcap-only matching) → era confound (model cheats on era). See Part 4 fix.
  - On existing data: TRAIN 2011-01→2017-01 (101W/102C ≈ 1:1, drop control-heavy 2010); TEST 2017-01→2020-01
    (81W/23C, winner-heavy → score with **ROC-AUC**, base-rate-invariant). Or continuous target (no ratio).
- **Metrics:** ROC-AUC (base-rate-invariant), Spearman(pred,return), NDCG@k, precision@k WITH counts, top-k median
  actual return. Never PR-AUC/precision on a winner-heavy test.
- **Per-pipeline:** re-run the window search (TRAIN_TEST_WINDOW_TEMPLATE.md) — don't hard-code TF years.

====================================================================================================
## PART 4 — DATA GAPS TO FILL (why the current analysis is "not complete")
====================================================================================================
1. **Date-matched controls (fixes the bias):** in `build_winners_controls_wide_panel.py`, match each winner to a
   control with similar mcap **AND a pit within the same ~quarter/year**. Then date splits are balanced AND unbiased.
2. **16,016 missing-input features (12% dropped):** engineer the columns they need (Part 5 cross-sectionals + events).
3. **Company-age / lifecycle (your year-2-vs-7 point — never computed):** years_since_IPO, history_length,
   quarters_since_first_revenue, growth-stage flags, age-relative windows, metrics normalized among same-age peers.
4. **Drop the worthless families:** f081–f085 metadata (ticker/currency/listing flags) — 191 failures, ~0 signal.
5. **Continuous target + the 7-yr depth** (Parts 2–3).

====================================================================================================
## PART 5 — SEC GRANULAR ANALYSIS (the deep accounting layer to ADD)
====================================================================================================
Source = Sharadar tables in the silver DuckDB (`E:\trading_system\data\silver\trading.duckdb`):
`SF1` (fundamentals, dimensions ARQ/ART/ARY/MRQ), `SEP` (prices), `DAILY` (mcap/ev/ratios), `TICKERS` (meta+IPO+
sector), `SF2` (insider txns), `SF3A/SF3B` (13F institutional/fund holdings), `EVENTS` (SEC event codes),
`ACTIONS` (splits/divs). Point-in-time: lag every fundamental to its **datekey (filing date)**, never period-end.

### 5A. Every line item, quarterly, with the full transform stack
For EACH SF1 line item below, compute at quarterly granularity, **across ALL 1q–28q windows**, with: level
(normalized by assets/mcap/revenue), QoQ & YoY growth, multi-quarter polynomial slope/accel/jerk, volatility,
distance-from-trailing-extreme, and **sector-cross-sectional percentile** (within-regime, by date×industry).
- **Income:** revenue, cor/cogs, grossprofit, opex, sgna, rnd, ebit, ebitda, ebt, netinc, eps, epsdil, dps.
- **Balance — assets:** assets, assetsc, cashneq, investments(STI), receivables, inventory, ppe(net), intangibles,
  goodwill, taxassets, assetsnc.
- **Balance — liab/equity:** liabilities, liabilitiesc, debt, debtc, debtnc, payables, deferredrev, taxliabilities,
  equity, retearn, accoci, sharesbas, sharefactor.
- **Cash flow:** ncfo(OCF), ncfi, ncff, capex, fcf, sbcomp, depamor, ncfcommon(buyback/issuance), ncfdebt, ncfdiv.

### 5B. Derived ratios (each with the same window/derivative stack)
- **Margins:** gross, ebitda, operating, net, fcf margin.
- **Returns:** ROE, ROA, ROIC, ROC, gross-profitability (GP/assets, Novy-Marx).
- **Liquidity:** current, quick, cash ratios; net-working-capital / mcap (a top TF signal); cash-runway months.
- **Leverage/solvency:** debt/equity, debt/ebitda, net-debt/ebitda, interest coverage, debt-maturity wall.
- **Efficiency:** asset turnover, receivables/inventory/payables days, cash-conversion cycle.
- **Valuation (from DAILY, point-in-time):** P/E, P/S, P/B, EV/EBITDA, EV/sales, FCF yield, mcap/netcash (top signal).
- **Growth/quality:** revenue CAGR (4/8/12/28q), asset growth, accrual ratio, net-share-issuance / dilution CAGR.

### 5C. Forensic / manipulation scores (point-in-time)
- **Beneish M-score** (8 inputs: DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, TATA) — earnings manipulation.
- **Altman Z / Z''-score** — bankruptcy distress (critical for micro-cap survival → 10×).
- **Piotroski F-score (0–9)** — fundamental strength.
- **Dechow F-score, Montier C-score, Sloan total-accruals ratio** — accrual quality / red flags.

### 5D. Ownership, insider, flow (SF2 / SF3 / DAILY)
- 13F institutional ownership level + Δholders (accumulation) over 1–8q; concentration (top-holder share).
- Insider: net buy/sell, cluster-buying score, buy/sell count, $-value, days-since-last-insider-buy.
- Short interest: level, days-to-cover, ΔSI; float rotation; share-count trajectory (dilution vs buyback).

### 5E. Events / filings (EVENTS table + text)
- 8-K item density (1/2/4q), Item 4.02 restatement flag, auditor-change flag, going-concern language flag.
- Days-since: last 10-K, last 8-K, last guidance, IPO; corporate actions (splits, reverse splits — common pre-10×).
- (Stretch) 10-K/10-Q NLP: MD&A sentiment, YoY risk-factor delta, liquidity-language flag.

### 5F. Niche conditioning (proven patterns to exploit)
- **Micro-cap focus:** winners median $14M vs $197M — add mcap-bucket feature and/or a separate <$100M model.
- **Sub-sector:** Solar 75% win-rate (predicted by balance-sheet *survival* — retained earnings, liquidity,
  leverage), Infra-Software 33%, pure Semis/Hardware 15%. Add industry feature and/or per-sub-sector models.

====================================================================================================
## PART 6 — ORDER OF OPERATIONS (the complete build)
====================================================================================================
1. **Panel build v2:** add date-matched controls (Part 4.1) + 16k missing cols (Part 5 cross-sectionals/events).
2. **Author features:** long-window (Part 2) + polynomial derivatives (Part 2) + lifecycle (Part 4.3) + SEC granular
   (Part 5). Drop f081–f085. Use q0-only hashing (≈4–5× faster, tiny artifacts).
3. **Register build 12 = additions only.** 4. **Compute --skip-existing into snapshot_tech_build11** (only new). 
5. **Dedup. 6. Stage 4** (build_q0_matrix → regime_clean → importance → finalize) over the combined set.
7. **Validate:** continuous target + chronological date split (date-matched controls now balanced) + per-quarter
   walk-forward. Report ROC-AUC, Spearman, NDCG@k, precision@k(counts), top-k median return.
8. **Compare to baseline 0.74 out-of-time** — did depth + polynomial derivatives + SEC granular + lifecycle lift it?

KEEP ALL DATA. Nothing is deleted; the recompute is additive and fits the free space.
