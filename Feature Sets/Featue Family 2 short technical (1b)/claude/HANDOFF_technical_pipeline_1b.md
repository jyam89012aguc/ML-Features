# PIPELINE 1B-TECHNICAL — Short-Side Overbought/Blowoff Feature Generation (Technical-Only)

**Mission:** Generate 30,000 candidate features (50 families × 600 features) for ML to detect Nasdaq stocks at multi-year peaks that will be "stuck" — touched −80% drawdown AND never recovered above −50% within 5 years. This pipeline is the **technical-only counterpart** to pipeline 1a-inverse (which mixes price action with fundamentals).

**Output root:** `C:\Users\jyama\Desktop\short_technical_features_1b\`

**Why a separate technical-only project:** features in 1b are *strictly* derivable from daily OHLCV (plus optional NSIR / OPT2 / ETFF). No SF1 / SF2 / SF3 / DAILY / TICKERS / ACTIONS / EVENTS dependencies. This makes 1b features:
- runnable on any Nasdaq ticker with sufficient SEP history (no PIT-lagged fundamentals required),
- usable as a standalone ML feature set OR as a complement to 1a-inverse features,
- easier to compute at scale (single data table per feature),
- easier to validate (price action is observable; no accounting interpretation).

---

## 1. UNIVERSE

```python
# Same filter as 1a-inverse (Sharadar TICKERS)
category   = 'Domestic Common Stock'
exchange  LIKE 'NASDAQ%'                          # Nasdaq-listed only
50_000_000 <= entry_market_cap <= 3_000_000_000   # at peak (PIT)
# Includes delisted / halted / bankrupt names — the blowups are the training signal.
```

## 2. DATA SOURCE

```python
SOURCE_DB = r"E:\trading_system\data\silver\trading.duckdb"   # READ-ONLY
```

| Tables (required) | Purpose | Columns used |
|---|---|---|
| **SEP** | Daily OHLCV | open, high, low, close, volume |

| Tables (optional — NaN-stub if absent) | Used by families |
|---|---|
| NSIR | 48 (short_squeeze_aftermath_technical) |
| OPT2 (ORATS skew) | _not used in 1b_ — pure-technical scope |
| ETFF (ETF flows) | _not used in 1b_ |

**Strict rule:** families 01-47, 49, 50 use **SEP only**. Family 48 may use NSIR if available, else NaN-stub. There are no fundamentals, no options skew, no ETF flows in 1b. Use 1a-inverse for those.

## 3. PIT MECHANICS (mirrors 1a-inverse)

**Snap point:** absolute HIGH per ticker per train/test window
- Tie-break: earliest date
- Min history before snap: 252 trading days
- Price filter: $0.20 ≤ entry_high ≤ $1,000
- Artifact filter: `high/low > 20` within ±2 days of snap → SKIP

**Forward window:** 1260 trading days (5 years) from snap

**Label (binary):**
```python
fwd_lows  = price.low[snap_idx + 1 : snap_idx + 1 + 1260]
fwd_highs = price.high[snap_idx + 1 : snap_idx + 1 + 1260]
entry_high = price.high[snap_idx]

touched_minus_80 = (fwd_lows / entry_high).min() <= 0.20
if touched_minus_80:
    touch_idx = first index where fwd_lows / entry_high <= 0.20
    recovered = (fwd_highs[touch_idx + 1:] / entry_high).max() > 0.50
else:
    recovered = True

stuck = 1 if (touched_minus_80 and not recovered) else 0
```

## 4. TRAIN / TEST (same as 1a-inverse)

```python
TRAIN_START = "2010-01-01"
TRAIN_END   = "2013-07-01"
GAP_DAYS    = 14
TEST_START  = "2013-07-15"
TEST_END    = "2019-12-31"
REGIME_END  = "2024-12-31"   # = TEST_END + 1260 trading days
```

## 5. SCHEMA — Per Family

Each family is one folder containing **8 Python files**, 75 features each = **600 features per family**.

```
NN_<family_name>/
├── NN_<family_name>__base__001_075.py     # 75 BASE feature ideas, indices 001-075
├── NN_<family_name>__base__076_150.py     # 75 BASE feature ideas, indices 076-150
├── NN_<family_name>__d1__001_075.py       # 75 d1 features (rate of base 001-075)
├── NN_<family_name>__d1__076_150.py       # 75 d1 features (rate of base 076-150)
├── NN_<family_name>__d2__001_075.py       # 75 d2 features (acceleration)
├── NN_<family_name>__d2__076_150.py
├── NN_<family_name>__d3__001_075.py       # 75 d3 features (jerk)
└── NN_<family_name>__d3__076_150.py
```

**Cross-family total: 50 × 600 = 30,000 candidate features. ML selects ~200.**

## 6. SIGNAL QUALITY RULES (NON-NEGOTIABLE)

1. **150 DISTINCT signal hypotheses per family.** Each base feature = a different *concept*.
2. **No parameter sweeps.** `RSI(7)`, `RSI(14)`, `RSI(21)` as three separate features is BANNED.
3. **Multi-horizon variants ARE allowed** when each horizon encodes a different *hypothesis*:
   - `breakdown_from_21d_high` = short-term failure pattern
   - `distribution_under_63d_high` = medium-term topping
   - `structural_break_252d` = long-term regime change
   These are three different *concepts*, not three sweeps of one. Acceptable.
4. **Each base hypothesis gets exactly 4 versions:** base (level/state) + d1 (rate) + d2 (acceleration) + d3 (jerk). The d1/d2/d3 files compute the derivatives of the corresponding base feature.
5. **ML decides importance.** Do NOT pre-filter. Do NOT curate. Generate distinct ideas at volume.

## 7. FUNCTION & REGISTRY CONVENTIONS

```python
# Function signature: takes named pandas Series
# Name format: f<NN>_<abbrev>_<NNN>_<descriptive_snake_case>
def f01_athx_001_log_dist_above_252d_high(high: pd.Series) -> pd.Series:
    """Distance of current high above its 252d trailing max, in log units."""
    rmax = high.rolling(252, min_periods=63).max()
    return _safe_log(high) - _safe_log(rmax)

# Naming: f<NN>_<abbrev>_<NNN>_<descriptive_name>
#   - NN = 01-50 family number (zero-padded)
#   - abbrev = 4-letter family abbreviation (see §9 table)
#   - NNN = 001-150 feature index within family
# Numbering: continuous 001-150 across the two base files in a family
# d1/d2/d3 functions: same base body, append `.diff()` / `.diff().diff()` / `.diff().diff().diff()` at return
def f01_athx_001_log_dist_above_252d_high_d1(high: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=63).max()
    return (_safe_log(high) - _safe_log(rmax)).diff()
```

**Registry naming per file:**
```python
ATH_PROXIMITY_EXTENSION_BASE_REGISTRY_001_075 = {
    "f01_athx_001_log_dist_above_252d_high": {
        "inputs": ["high"],
        "func": f01_athx_001_log_dist_above_252d_high,
    },
    # ... 74 more
}
```

Registry pattern: `{FAMILY_UPPER}_{ORDER}_REGISTRY_{NNN}_{MMM}` where ORDER ∈ {BASE, D1, D2, D3}.

## 8. TECHNICAL RULES

- Every file must pass `ast.parse()`. No syntax errors.
- Every file < 75 KB.
- Trading-day constants: `YDAYS=252, QDAYS=63, MDAYS=21, WDAYS=5`. Also `DDAYS_2Y=504`, `DDAYS_5Y=1260` where useful.
- Utility helpers (`_safe_log`, `_safe_div`, `_rolling_zscore`, `_true_range`, `_atr`, `_rolling_slope`) defined at top of **each** file. **Do not import across families.** Self-contained files.
- **`_rolling_slope` reference implementation** (use this — earlier variants had warmup-broadcast bugs):
  ```python
  def _rolling_slope(s, n, min_periods=None):
      if min_periods is None:
          min_periods = max(n // 3, 2)
      def _slope(w):
          valid = ~np.isnan(w)
          if valid.sum() < min_periods:
              return np.nan
          x = np.arange(len(w), dtype=float)
          if valid.all():
              wv = w
          else:
              x = x[valid]
              wv = w[valid]
          xm = x.mean(); wm = wv.mean()
          num = ((x - xm) * (wv - wm)).sum()
          den = ((x - xm) ** 2).sum()
          return num / den if den != 0 else np.nan
      return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)
  ```
- **PIT discipline absolute:** NO centered rolling windows. NO forward-looking smoothing. NO peeking past the snap date. Use `rolling()` defaults (right-anchored) and `min_periods` parameter explicitly. NO `.shift(-N)`.
- **Missing-data contract:** return `pd.Series(np.nan, index=input.index)` — NEVER zero-fill, NEVER forward-fill across NaN gaps unless that's specifically the hypothesis (and document it).
- **Multi-column DataFrame .idxmax(axis=1) gotcha:** when building a DataFrame via `pd.concat([series_a, series_b, ...], axis=1)` where each series inherits its name from a shared input, the columns will have duplicate names. `.idxmax(axis=1).astype(float)` will fail on the duplicated string name. Always rename pieces uniquely:
  ```python
  diffs = pd.concat([(piece_for_k).rename(k) for k in range(2, 11)], axis=1)
  result = diffs.idxmax(axis=1).where(a.notna(), np.nan).astype(float)
  ```
- Vectorize with numpy. Avoid `df.apply(lambda x: ...)` over rows. Avoid Python loops in hot paths. Inner row-loops are tolerable only inside `rolling().apply(_fn, raw=True)` when the operation truly requires per-window logic (e.g., longest-run, structural-break, PSAR).
- Hardware target: AMD Ryzen 7600 / 64 GB RAM / RTX 5060 16 GB. Features are CPU-side. **NO GPU code** in feature functions — GPU is reserved for downstream model training.

## 9. THE 50 FEATURE FAMILIES

All families use SEP only unless noted. Family 48 may use NSIR if available.

### Wave 1 — Price level / structure (10 families, SEP)

| #  | Folder name                                      | Abbrev | Theme |
|----|--------------------------------------------------|--------|---|
| 01 | ath_proximity_extension                          | athx   | distance above N-day high, multi-window, in price/ATR/log units |
| 02 | parabolic_blowoff_signature                      | pblo   | log-quadratic curvature, LPPL proxies, hyperbolic singularity |
| 03 | topping_pattern_classical                        | tpcl   | H&S, double/triple top, broadening, descending triangle |
| 04 | distribution_top_signature                       | dtsg   | rolling-top dwell, lower-high formation, neckline timing |
| 05 | failed_breakout_dynamics                         | fbkd   | bull traps, false-break counts, breakaway gap failures |
| 06 | candlestick_reversal_catalog                     | cscr   | engulfing, doji, hammer, tweezer, three-line-strike — at high |
| 07 | lower_high_lower_low_structure                   | lhll   | Dow theory breakdown sequence, swing-low sequence |
| 08 | fibonacci_extension_signature                    | fibx   | 1.618 / 2.618 / 4.236 prior-swing overshoot detectors |
| 09 | island_reversal_gap_dynamics                     | irgd   | island tops, exhaustion gap, breakaway / runaway gaps |
| 10 | swing_pivot_topology                             | swpv   | pivot-N swing count, swing amplitude decay, zigzag compression |

### Wave 2 — Moving averages / trend (8 families, SEP)

| #  | Folder name                                      | Abbrev | Theme |
|----|--------------------------------------------------|--------|---|
| 11 | sma_ema_extension_dynamics                       | smae   | SMA/EMA/DEMA/TEMA/HMA/KAMA distance and ATR-normalized extension |
| 12 | moving_average_ribbon_structure                  | mrib   | ribbon order, stacking, compression, entropy |
| 13 | ma_crossover_failure_dynamics                    | mcxf   | death cross, golden cross failure, recross frequency |
| 14 | supertrend_psar_chandelier                       | stps   | trailing-stop distance, flip event count, post-flip behavior |
| 15 | anchored_vwap_extension                          | avwx   | anchored from 52w low / peak / IPO date — distance and velocity |
| 16 | donchian_bollinger_keltner_bands                 | dbkb   | band break failures, squeeze, walking-the-band |
| 17 | trend_line_break_dynamics                        | tlbk   | rolling trendline slope, break events, retest failures |
| 18 | linear_regression_channel                        | lrch   | LR slope / R² / residual / channel-width / band-touch |

### Wave 3 — Volume / dollar volume (6 families, SEP)

| #  | Folder name                                      | Abbrev | Theme |
|----|--------------------------------------------------|--------|---|
| 19 | volume_blowoff_climax                            | vblc   | peak volume + post-climax decay, volume pyramid |
| 20 | volume_dryup_at_high                             | vdah   | low-vol breakouts, dryup after climax, entropy collapse |
| 21 | dollar_volume_intensity                          | dvit   | $-vol z-scores, percentile ranks, regime ratios |
| 22 | on_balance_volume_dynamics                       | obvd   | OBV slope, divergence, regime, decay |
| 23 | accumulation_distribution_line                   | adld   | AD line, CMF, MFI, force index, KVO |
| 24 | turnover_and_churn                               | tnch   | turnover proxies, wide-range bars, churning index |

### Wave 4 — Momentum / oscillators (10 families, SEP)

| #  | Folder name                                      | Abbrev | Theme |
|----|--------------------------------------------------|--------|---|
| 25 | rsi_exhaustion_family                            | rsxh   | Wilder/Cutler/Connors RSI, RSI-of-RSI, overbought-exit events |
| 26 | stochastic_williams_family                       | stwf   | Stoch K/D, Stoch RSI, Williams %R, Ultimate Stoch |
| 27 | macd_topping_dynamics                            | mcdt   | MACD, MACD-H, divergence, rollover events |
| 28 | trix_tsi_cci_family                              | ttcf   | TRIX, TSI, CCI, DPO, KST, CMO — overbought-exit detectors |
| 29 | ultimate_aroon_vortex                            | uarn   | Ultimate Oscillator, Aroon, Vortex, ADX/DI, Choppiness, Mass Index |
| 30 | wave_trend_oscillator_family                     | wtof   | WTO, LazyBear squeeze momentum, BB-squeeze states |
| 31 | roc_momentum_family                              | rcmf   | rate-of-change at multiple horizons, ROC-zscore, ROC-rank |
| 32 | divergence_detection                             | divd   | price vs RSI/MACD/OBV/AD/Stoch divergences (bearish-only) |
| 33 | coppock_curve_kst                                | cpkt   | Coppock, KST, smoothed long-term momentum sign changes |
| 34 | td_sequential_demark                             | tdsq   | TD 9-setup, TD-13 countdown, sequential signals at high |

### Wave 5 — Volatility (6 families, SEP)

| #  | Folder name                                      | Abbrev | Theme |
|----|--------------------------------------------------|--------|---|
| 35 | realized_volatility_regime                       | rvre   | RV at multiple horizons, percentile rank, vol-cone position |
| 36 | semi_variance_asymmetry                          | svas   | upside / downside semi-variance, skew, asymmetry ratios |
| 37 | range_estimators_family                          | rges   | Parkinson, Garman-Klass, Yang-Zhang, Rogers-Satchell |
| 38 | jump_detection_signature                         | jpdt   | extreme-return counts, statistical jump tests |
| 39 | volatility_clustering                            | vclu   | ARCH/GARCH proxies, vol-of-vol, vol persistence |
| 40 | atr_expansion_dynamics                           | atxd   | ATR ratios, expansion-at-top, ATR-percentile-rank |

### Wave 6 — Statistical / spectral (4 families, SEP)

| #  | Folder name                                      | Abbrev | Theme |
|----|--------------------------------------------------|--------|---|
| 41 | return_distribution_moments                      | rdmm   | skew, kurt, normality tests (JB, AD, KS) on returns |
| 42 | autocorrelation_persistence                      | acpe   | Hurst exponent, DFA, variance ratio test, AR(1) persistence |
| 43 | tail_risk_var_es                                 | trve   | VaR, ES, Cornish-Fisher VaR, expected shortfall |
| 44 | spectral_cycle_analysis                          | spca   | Fisher transform, Ehlers MESA period, dominant cycle |

### Wave 7 — Microstructure / session (3 families, SEP)

| #  | Folder name                                      | Abbrev | Theme |
|----|--------------------------------------------------|--------|---|
| 45 | amihud_roll_kyle_liquidity                       | arkl   | Amihud illiquidity, Roll spread, Kyle's lambda proxy |
| 46 | session_open_close_dynamics                      | socd   | open strength, close strength, intraday reversal, close-in-range position |
| 47 | atr_extension_signature                          | atxs   | multi-horizon ATR-normalized extension from MA/VWAP/anchor |

### Wave 8 — Short-side composites (3 families)

| #  | Folder name                                      | Abbrev | Data |
|----|--------------------------------------------------|--------|---|
| 48 | short_squeeze_aftermath_technical                | ssat   | NSIR + SEP (NSIR optional — NaN-stub) |
| 49 | blowoff_climax_composite                         | bcco   | SEP (multi-signal blowoff composites) |
| 50 | terminal_distribution_composite                  | tdco   | SEP (multi-signal distribution + breakdown composites) |

## 10. PER-FAMILY GENERATION PROMPT (paste into Claude Code)

**Before pasting:** make sure Claude Code's working directory is `C:\Users\jyama\Desktop\short_technical_features_1b\`. The family subfolder already exists.

Replace the bracketed values per family from the §9 table:

```
TASK: Generate the [FAMILY_NAME] feature family for pipeline 1b-technical.

Reference: HANDOFF_technical_pipeline_1b.md (in project root). Read it before generating.

Generate exactly 8 Python files in folder:
  C:\Users\jyama\Desktop\short_technical_features_1b\[NN_FAMILY_NAME]\

  [NN_FAMILY_NAME]__base__001_075.py    (75 base features, ideas 001-075)
  [NN_FAMILY_NAME]__base__076_150.py    (75 base features, ideas 076-150)
  [NN_FAMILY_NAME]__d1__001_075.py      (75 first derivatives of base 001-075)
  [NN_FAMILY_NAME]__d1__076_150.py      (75 first derivatives of base 076-150)
  [NN_FAMILY_NAME]__d2__001_075.py      (75 second derivatives of base 001-075)
  [NN_FAMILY_NAME]__d2__076_150.py      (75 second derivatives of base 076-150)
  [NN_FAMILY_NAME]__d3__001_075.py      (75 third derivatives of base 001-075)
  [NN_FAMILY_NAME]__d3__076_150.py      (75 third derivatives of base 076-150)

Function prefix: f[NN]_[ABBREV]_
Data tables used by this family: SEP (open, high, low, close, volume).
  (For family 48 only: also accept NSIR shortinterest, daystocover, shortpctfloat, shortpctshares —
   NaN-stub when absent.)

TARGET PHENOMENON (what these features should detect):
Nasdaq-listed stocks at multi-year peaks (snap = absolute high in train/test window) that
subsequently became "stuck" — touched −80% drawdown AND never recovered above −50% of peak
within 5 years (1260 trading days). Universe: $50M-$3B market cap at peak.

SIGNAL DENSITY:
- 150 distinct signal HYPOTHESES (different concepts), NOT parameter sweeps
- Each hypothesis encoded as base feature + d1 + d2 + d3 = 4 features per idea
- Multi-horizon variants allowed only when each horizon = a different hypothesis
  (short-term breakdown != medium-term distribution != long-term regime change)

FUNCTION CONTRACT:
- Each function: named pandas Series input(s) → pandas Series output of same length
- Function name format: f[NN]_[ABBREV]_NNN_<descriptive_snake_case>
- Inputs are SEP columns: open, high, low, close, volume

REGISTRY CONTRACT (per file, at bottom):
[FAMILY_UPPER]_BASE_REGISTRY_001_075 = {
    "f[NN]_[abbrev]_001_descriptive_name": {"inputs": ["close", "volume"], "func": fn},
    ...
}
For d1/d2/d3 files: replace BASE with D1/D2/D3 in registry name, and the function names
take the matching _d1 / _d2 / _d3 suffix.

PIT DISCIPLINE (absolute):
- NO centered rolling windows
- NO forward-looking smoothing
- NO peeking past snap_date (no .shift(-N))
- Use right-anchored .rolling() with explicit min_periods
- Missing data: return pd.Series(np.nan, index=input.index) — never zero-fill

REFERENCE _rolling_slope HELPER (copy verbatim — avoids the warmup-broadcast bug found in 1a-inverse):
[see HANDOFF §8 for the implementation]

REFERENCE pd.concat .idxmax(axis=1) IDIOM (avoids string-name bug):
diffs = pd.concat([(piece_for_k).rename(k) for k in range(2, 11)], axis=1)
result = diffs.idxmax(axis=1).where(a.notna(), np.nan).astype(float)

TECHNICAL:
- Trading days: 252/yr, 63/qtr, 21/mo, 5/wk (plus 504, 1260 for multi-year)
- Utility helpers (_safe_log, _safe_div, _rolling_zscore, _true_range, _atr, _rolling_slope)
  at top of EACH file — no imports across families
- Every file must pass ast.parse(); each file < 75 KB
- Vectorize with numpy. No row-iteration in hot paths. No GPU code.

CRITICAL — DO NOT:
- Generate a README, markdown explanation, or commentary file
- Filter, rank, or curate features before output
- Use centered windows or any forward-looking calc
- Import functions across family boundaries
- Reproduce hypotheses already covered by other families in the 50-family list
- Use parameter sweeps of one metric (RSI(7), RSI(14), RSI(21) = banned)
- Use any SF1 / SF2 / SF3 / DAILY / TICKERS / ACTIONS / EVENTS inputs (technical-only pipeline)

OUTPUT: 8 .py files only. Nothing else. No companion files. No README.
```

## 11. TESTING PROTOCOL — DO THIS FIRST

Before generating all 50 families, validate the architecture with ONE family:

1. **Pick `01_ath_proximity_extension`** as the test family — purely OHLC, easiest to verify
2. Generate that family per §10 prompt
3. **Verify:**
   - 8 files exist in `01_ath_proximity_extension/`
   - Each file passes `ast.parse()`
   - Total feature count across all 8 registries = 600
   - Function names are unique within the family
   - No duplicates of the same hypothesis (manual scan of registries)
   - At least one feature spot-checked against a real ticker (e.g. compute `f01_athx_001_log_dist_above_252d_high` on AAPL's history and verify it's sensible)
   - File sizes all < 75 KB
4. **If any check fails:** revise the §10 prompt before proceeding to remaining 49 families
5. **If all pass:** generate the remaining 49 families in batches of 3-5 per Claude Code session

## 12. BATCH ORDER RECOMMENDATION

Generate in waves to test architectural integrity progressively:

**Wave 1 — Price level / structure (10 families):** 01-10
**Wave 2 — Moving averages / trend (8 families):** 11-18
**Wave 3 — Volume (6 families):** 19-24
**Wave 4 — Momentum / oscillators (10 families):** 25-34
**Wave 5 — Volatility (6 families):** 35-40
**Wave 6 — Statistical / spectral (4 families):** 41-44
**Wave 7 — Microstructure / session (3 families):** 45-47
**Wave 8 — Composites (3 families):** 48-50

After each wave, run the validation checks before proceeding.

## 13. WHAT THIS HANDOFF DOES NOT INCLUDE (yet)

These are next-stage deliverables, NOT part of feature generation:

- `00_pipeline_config_1b.py` (technical config: paths, label window, train/test dates)
- `01a_load_data_1b.py` (loads Nasdaq SEP universe; optional NSIR staging for family 48)
- `01b_find_peaks_1b.py` (mirror of 1a-inverse's peak finder — absolute high)
- `01c_classify_blowups_1b.py` (compute stuck label — identical to 1a-inverse since label uses SEP only)
- `02_find_controls_1b.py` (matched controls — tickers that did NOT get stuck)
- `03_build_features_1b.py` (feature computation runner — calls registries; uses the `f<NN>_<abbrev>_NNN_` registry naming)

Generate these AFTER feature families pass validation. Pipeline scripts depend on the feature registries existing.

## 14. RELATIONSHIP TO 1A-INVERSE

1b is **independent** of 1a-inverse — same universe, same label, same train/test, same PIT discipline, but entirely separate feature universe (technical-only vs. fundamentals+technical mixed).

**Combining the two feature sets:** trivial — both register their features under the `f<NN>_<abbrev>_NNN_...` namespace. 1a-inverse uses families 01-50 (+ 40q). 1b uses families 01-50 with different abbreviations, so namespaces don't collide. Downstream pipeline can `import` both registry sets and pass the union to ML.

**No cross-pipeline imports.** Each pipeline's features are self-contained per HANDOFF §8.

---

**Total deliverable count when complete:**
- 50 family folders (already created)
- 400 .py files (8 per family)
- ~30,000 candidate features
- ML downstream selects ~200 from the combined 1a+1b feature universe (~60,000+ features)

**No README. No markdown commentary in feature files. Files only.**
