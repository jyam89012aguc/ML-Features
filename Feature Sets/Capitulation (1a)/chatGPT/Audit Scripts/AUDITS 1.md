# AUDITS.md

Detailed per-family audit writeups. The summary table and outstanding-work list live in `CLAUDE.md`; this file is the deep-reference companion. Read on demand for the specific family you're working on.

### `price_momentum_base` (commits `78f3def`, `6ad3224`)

Removed (6 duplicate functions, commit `78f3def`):
- `pm_036_macd_histogram_norm` -- `close.abs() == close` for equities; identical to `pm_035_macd_signal_spread`
- `pm_170_rolling_calmar_252d` -- same math as `pm_069_momentum_quality_252d`
- `pm_176_high_low_range_position_21d` -- identical body to `pm_098_donchian_position_21`
- `pm_209_roc_roc_21d` -- ROC-of-ROC == acceleration; same as `pm_059_ret_acceleration_21d`
- `pm_222_recovery_factor_63d` -- identical to `pm_068_momentum_quality_63d`
- `pm_294_ret_126d` -- literal copy-paste of `pm_007_ret_126d`

Naming debt left in place: `pm_069_momentum_quality_252d` actually computes Calmar 252d, and `pm_068_momentum_quality_63d` computes a Pain-ratio variant. Names left unchanged; rename if/when a wider naming pass is done.

### `basing_pattern_base` (commits `b0203c3`, `aa09779`, `d304409`, `2784a59`, `74e0b1f`)

**Family is hybrid, not pure-price** (correcting initial classification): 280 of 300 bp_ functions take only `close/high/low/open/volume`; the remaining 20 need fundamentals (`revenue`, `netinc`, `fcf`, `debt`, `equity`, `assets`). The db-direct harness skips those 20 with `missing_inputs=[...]` errors -- they need a fundamentals harness pass.

**Performance vectorizations** (commits `b0203c3`, `aa09779`, `d304409`, `2784a59`):

- `_sample_entropy` (file 3 helper): nested-for `_count_matches` -> `sliding_window_view + 4-D broadcast`. Originally caused multi-hour stuck runs; now ~30x faster per call.
- `bp_212/bp_213 _mem` (file 3): same nested-for pattern, same fix.
- `bp_092/bp_093` (file 2): `rolling(W).apply(autocorr, raw=False)` -> `rolling(W-1).corr(ret.shift(1))`. ~240x speedup.
- `_permutation_entropy` (file 3 helper): `sliding_window_view` + factorial-base perm encoding + `bincount`. Used by bp_153/bp_154; ~5-10x faster transitively.
- `_higuchi_fd` (file 3 helper): inner indexing list-comp -> `arange + advanced indexing`. ~1.0-1.2x; cleaner code, kmax loop still dominates.
- `_sample_entropy_series` (new helper): batched outer-vec for `bp_155` (W=21). bp_156 (W=63) keeps per-window inner-vec since outer-vec is memory-bound there (130 MB diff tensor).
- `bp_190/bp_191` (file 3): `for b, vol in zip(...)` -> `np.bincount(weights=...)`. Marginal speedup, cleaner.
- `bp_214/bp_215/bp_216` (file 3 spectral): pre-compute `ret = close.pct_change()` once outside per-i loop. ~15-25x.
- `bp_277` (file 4): same pre-compute pattern. ~5x.

All replacements verified at <1e-9 absolute tolerance against rand walk + flat + sinusoid before commit.

**Audit-driven deletes** (commit `74e0b1f`, 7 functions):
- `bp_069_consecutive_inside_bars` -- always returns 0 at entry-day across the 100-entry sample (low-signal metric)
- `bp_224_zero_crossing_rate_21d` -- identical to `bp_096_price_oscillation_freq_21d`
- `bp_225_zero_crossing_rate_63d` -- identical to `bp_097_price_oscillation_freq_63d`
- `bp_261_donchian_width_21` -- identical to `bp_001_range_pct_21d`
- `bp_262_donchian_width_63` -- identical to `bp_002_range_pct_63d`
- `bp_263_donchian_position_21` -- identical to `bp_026_close_position_in_21d_range`
- `bp_264_donchian_width_contraction_21_63` -- equivalent to `bp_005_range_contraction_21_63`

File 3 still takes ~13 min in the audit even after the perf fixes (entropy + spectral functions are inherently O(N) per call across 1500 windows). Acceptable; not pursuing further outer-vec.

### `moving_average_dynamics_base` (commits `8ed97f0`, `91a91d7`)

**Hybrid family**: 287 of 300 mad_ functions take only `close/high/low/open/volume`; 13 need fundamentals (`revenue`, `netinc`, `fcf`, `debt`, `equity`, `assets`). All 13 unbindables are in `_076_150.py` (mad_129-134) and `_076_150_expanded.py` (mad_e136-142).

**Harness clean baseline**: 287 features ran with 0 echoes / 0 constants / 0 formula-exact dups / 0 value-exact dups. Total runtime ~11 min (slowest: `_001_075_expanded.py` at 5.8 min, dominated by LSMA / FRAMA / ALMA per-window apply, and `_076_150*.py` at ~2 min each).

**Audit-driven deletes (5 functions)** — caught by AUC+Spearman tie analysis, not by the harness's value-hash check, because the values differ by a constant scalar but are rank-equivalent (Pearson=1.0, Spearman=1.0). Verified at float-precision noise (ratio std 1e-11 to 1e-18 on 1500-row rand walk):

- `mad_148_sma200_slope_acceleration` -- = `mad_102_sma200_curvature` / 21 (commit `8ed97f0`)
- `mad_149_ema21_slope_acceleration`  -- = `mad_103_ema21_curvature` / 5  (commit `8ed97f0`)
- `mad_e097_price_osc_10_50`          -- = `mad_063_sma10_sma50_spread` * 100  (commit `91a91d7`)
- `mad_e099_price_osc_50_200`         -- = `mad_059_sma50_sma200_spread` * 100 (commit `91a91d7`)
- `mad_e103_lr_slope_21_normalized`   -- = `mad_e067_lsma21_sma21_spread` / 10 (commit `91a91d7`)

**New finding pattern: scalar-multiple rank-equivalent dups.** The harness's value_hash check uses np.allclose-style equality, which misses constant-multiple pairs. Future audits: cross-reference top features for AUC+Spearman ties at 4 dp, then verify scalar-multiple via `(a/b).std()` on synthetic data. If std at float-precision noise (<1e-10), it's a scalar-multiple dup -- ASK FIRST per HANDOFF policy ("value-exact dups that aren't formula-exact").

### `peak_and_crash_base` (commits `0c1443d`, `cfba2e7`, `5c0492d`, `e8888f7`)

**Hybrid family** (re-classified from initial "price-only" assumption): 269 of 297 pc_ functions take only `close/high/low/open/volume`; 28 need fundamentals (`revenue`, `netinc`, `fcf`, `debt`, `equity`, `assets`). All 28 unbindables are in `_151_300.py` (pc_166-176, pc_216-218, pc_225, pc_237-242, pc_249, pc_267-272, pc_271).

**Performance vectorizations** (commit `0c1443d`): three rolling-apply autocorrelations matched the standard `bp_092/bp_093` pattern:
- `pc_117_return_autocorrelation_1_63d` -- ~410x speedup (188ms -> 0.6ms)
- `pc_118_return_autocorrelation_5_252d` -- ~390x speedup (177ms -> 0.8ms)
- `pc_119_crash_serial_correlation_63d`  -- ~224x speedup (140ms -> 1.0ms)

`rolling(W).apply(s.autocorr(lag=k), raw=False)` -> `rolling(W-k, min_periods=W-k-5).corr(s.shift(k))`. min_periods set to W-k-5 (not the policy default mp=10) was needed to match warmup-edge NaN positions exactly. All verified <1e-9 vs old.

**Audit-driven deletes (3 dups + 1 helper)**:
- `pc_207_double_top_proximity` -- formula-exact dup of `pc_002_drawdown_from_52w_high`. `(close/rh - 1) == (close - rh)/rh`. (commit `cfba2e7`)
- `pc_208_double_bottom_proximity` -- formula-exact dup of `pc_011_rally_from_52w_low`. Same identity vs rolling min. (commit `cfba2e7`)
- `pc_300_recovery_return_from_trough` -- formula-exact dup of `pc_014_rally_from_atl` (across files). (commit `5c0492d`)
- `pc_029_drawdown_from_ath_helper` -- not a dup of anything *exposed* in registry, but its body (with `window=` keyword vs positional) was textually different from `pc_029_max_drawdown_1y` in file 1. Inlined the `_mdd` math directly into its only caller `pc_276_drawdown_to_volatility_ratio`. (commit `e8888f7`)

**9 conditional indicators are always-zero on the harness sample but kept by design** (per user direction): pc_020/022/024 (new-high flags), pc_064 (vol_at_peak), pc_198 (peak_vol_divergence), pc_205 (v_bottom), pc_206 (dead_cat_bounce), pc_231 (peak_momentum_divergence), pc_261 (peak_above_bollinger). All are mathematically valid AND-of-low-probability-conditions or running-max-binary flags; the 100-entry winners+controls sample just rarely catches the trigger. Different from `bp_069_consecutive_inside_bars` (which was deleted) -- that one used `close.abs() == close` no-op-style logic; these are real conditional triggers with low base rate.

**Hybrid auto-classification trap** (lesson for future audits): `inventory grep` on `"inputs":` text only sees explicit registry literals. File 1 has a literal dict, so its inputs were visible. File 2 builds the registry programmatically via `inspect.signature` on a `_ALL_FUNCS` list, so its inputs were NOT visible to grep -- which made the family look pure-OHLCV. Always run the inspector-based inventory (load both files, walk `vars()`, check `inspect.signature`) before classifying as price-only.

Total runtime: 17.5 min (file 1: 11.3 min, file 2: 6.2 min). File 1 dominated by `pc_246_crash_return_concentration` (433ms/call), `pc_084/pc_085_cdar_*_252d` (~230ms/call), `pc_029-pc_032_max_drawdown_*` (~125ms/call), and the (now-vectorized) autocorr trio.

**Re-audit verify pass 2026-05-10 (commit `ad9955a`)**: Path B daily-cadence harness (5 profiles incl. crash_recovery × 2800d × 11 input cols, warmup=1300d for 5y shift). 4 cross-tier vhash dup groups found and auto-deleted (all Class 1/2/4 per AUTO-DELETE precedent):
- `pc_049_drawdown_duration_current` == `pc_006_days_since_ath` (Class 1; cumcount-within-at_ATH-groups == cumsum-of-in_dd-within-recovery-groups; caller `pc_131` updated to `pc_006`)
- `pc_132_drawdown_convexity` == `pc_351_jerk_dd_ath_5d` (Class 1 + Class 4 cross-tier base→deriv pollution; 2nd-diff_5d_5d(dd_ath) is a 3rd-deriv tier operation, RL `rl_227/229/231` precedent)
- `pc_265_up_down_capture_ratio` == `pc_250_omega_ratio_proxy` (Class 2 cancellation-equiv; `(sum/W)/(sum/W) = sum/sum` on identical windows, RL `rl_080/081/082` + CAS `cas_182/183` precedent)
- `pc_284_drawdown_acceleration_21d` == `pc_365_jerk_ema21_5d` (Class 1 + Class 4; `ema(2nd_diff(dd)) = 2nd_diff(ema(dd))` by LTI commutation; base-side 3rd-deriv operation belongs in derivative file)

KEEP Class 16 unit-conversion scalar-mults (not deleted, both verified at FP precision):
- `pc_079_martin_ratio_252d` / `pc_083_burke_ratio_proxy_252d` ratio=100 (Martin uses Ulcer Index in percent units `(100*dd/rh)^2`; Burke uses fractional dd `(dd/rh)^2`; LS `ls_023/297` days-conversion + CFT cumulative-vs-yield precedent for ×100 unit-conversion)
- `pc_090_downside_potential_63d` / `pc_147_cumulative_crash_return_1q` ratio=1/63 (mean vs cumulative over W=63 quarter; CFT `cft_*` mean-vs-sum precedent)

Post-fix: 389/389 fns (was 393), 0 errors, 0 all-NaN, 0 unexplained dups, 10 synth-bias constants (6 overnight-gap / intraday-symmetric flags from `open=close.shift(1)` synth: pc_062/073/074/120/121/124/243; 3 fundamental-vs-price flags sample-bias on healthy profile: pc_174/267/268). Cross-chain dedup connectivity lesson: original tab-1/tab-4 PC audits each scanned within their tier set (base+base for tab-1; deriv+deriv for tab-4) but missed cross-tier base↔deriv mathematical-identity pairs — same lesson as RL tab 7-cont (commit `aa25895`) and pricing_power_signal re-audit (commit `47e0bee`).

### `price_moving_averages_base` (commit `046a589`)

**Pure-price family** (confirmed via inventory grep): all 300 pma_ functions take only `close/high/low/open/volume`. 0 unbindables, 0 errors, 0 echoes after fix, 0 dup groups, 0 constants.

**Pre-fn timing audit clean** -- 0 functions > 100 ms threshold on 1500-row synthetic close. Slowest: `pma_168_frama16_frama32_spread` @ 84.6 ms; bulk of the heavy ones cluster around `_lsma`/`_alma`/`_kama`/`_frama` rolling-apply patterns at 30-85 ms. Total per-fn cost across the family ~1.2 s on 1500 rows. No perf vectorizations applied.

**Audit-driven helper bug fix** (commit `046a589`, single root cause behind 3 constants + 2 dup groups): the `_frama` helper in `_151_225.py` was missing length normalization on `n1`/`n2`/`n3`. Without dividing by segment lengths, the fractal dimension `d` lived in `[0,1]` instead of the canonical `[1,2]`, `alpha = exp(-4.6 * (d-1))` clamped to 1.0 every step, and FRAMA collapsed to identity (`_frama(close, w) == close`). Symptom propagation:
- `pma_164_frama_16` and `pma_165_frama_32` -> identical (both equal `close`) -> value-exact dup group
- `pma_166_close_vs_frama16_pct` = `pma_167_close_vs_frama32_pct` = `pma_168_frama16_frama32_spread` = 0 -> 3 constants AND a value-exact dup group
- `pma_169_frama16_slope_5d` and `pma_170_frama32_slope_21d` -> degenerated to `close.pct_change(5/21)` (returns in disguise; not flagged by harness because they happen to differ from any other pma_ function)

Fix: divide each range by its segment length (`half`, `w-half`, `w`) -- canonical Ehlers FRAMA. Verified with assertions on rand-walk + flat + sinusoid: OLD == close (the bug), NEW != close on rand-walk/sinusoid (smoothing happens), NEW == 100 on flat, no NaN past warmup. `d_new` does dip below 1.0 on smooth signals but the alpha clamp handles it, which is standard Ehlers behavior. Re-ran harness post-fix: 0 echoes / 0 constants / 0 dup groups / 0 errors. Runtime 9.8 min (file 3: 5.7 min still dominates due to the per-window FRAMA + LSMA + ALMA inner loops; not pursuing further vectorization since post-fix functions are real signals now and per-fn cost stays under 100 ms).

**McGinley overflow noise** (`_mcginley` at line 98): RuntimeWarnings for `overflow encountered in scalar divide` and `invalid value encountered in scalar add` when `prev` becomes very small and `ratio**4` blows up. The math degrades safely (denom -> inf -> increment -> 0 -> prev unchanged), so output values are sensible and the harness reports 0 errors / 0 constants / 0 dups for all McGinley features. Not addressed (out of triage scope; no observable downstream effect on signal values).

**Lesson for future audits:** when the harness reports a cluster of constants AND dup groups all touching the same helper, treat it as one bug, not N independent findings. Asking "fix the helper vs delete the features" upfront avoided 7 separate triage decisions and preserved 7 signals' worth of mathematical content.

### `volatility_regime_base` (commits `0784a3c`, `f3d019b`, `2f1f4dd`, `f65a8cb`, `0e4649c`, `830807e`, `878a752`, `ff29fda`, `a01d3e0`)

**Hybrid family**: 273 of 291 vr_ functions take only `close/high/low/open/volume`; 18 need fundamentals (`revenue`, `netinc`, `fcf`, `debt`, `equity`, `assets`). Unbindables in `_076_150.py` (vr_117-121, 147-148) and `_226_300.py` (vr_250-260).

**Performance vectorizations** (commits `0784a3c`, `f3d019b`, `2f1f4dd`): 7 rolling-apply autocorrelations matched the standard `bp_092/bp_093` pattern. All `rolling(W).apply(s.autocorr(lag=k))` -> `rolling(W-k).corr(s.shift(k))`, verified <1e-9 vs old:
- `vr_030/031/032_vol_autocorr_*` -- ~270x avg speedup
- `vr_075_vol_persistence_ratio_63d` -- ~210x speedup
- `vr_207_vol_half_life_proxy_252d` -- ~145x speedup
- `vr_286/287_squared_return_autocorr_*` -- ~270x avg speedup

**Pandas 2.x compatibility fix** (commit `f65a8cb`): `vr_285_vol_regime_quintile_252d` raised "Array conditional must be same shape as self" because `out.where(False, 4.0)` is no longer accepted. Replaced with `pd.Series(4.0, ...)` direct construction. Also added explicit `out.where(~v21.isna(), np.nan)` so the 21d vol-warmup window returns NaN instead of a fake top-quintile.

**Look-ahead bug fix** (commit `ff29fda`): `vr_169_leverage_effect_21d` and `vr_170_leverage_effect_63d` used `v_chg = v5.shift(-5) - v5` -- looking 5 days into the future. Last 5 rows always NaN, so at any "as-of" date the rolling correlation produces NaN at the prediction horizon -- harness flagged both as 100% null. Fixed by flipping shift direction: `v_chg = v5 - v5.shift(5)` (correlation of returns with PRIOR vol change, same financial interpretation, no look-ahead).

**Audit-driven deletes (9 functions across 3 commits)**:

Formula-exact dups (commits `0e4649c`, `830807e`):
- `vr_195_drift_vol_ratio_21d` -- = `vr_055_abs_return_vol_ratio_21d`
- `vr_196_drift_vol_ratio_63d` -- = `vr_056_abs_return_vol_ratio_63d`
- `vr_292_log_range_alizadeh_21d` -- = `vr_199_normalized_range_vol_21d`

Variable-rename value-exact dups (caught by value_hash, missed by formula_hash; commits `878a752`, `a01d3e0`):
- `vr_028_vol_mean_reversion_ratio_63d` -- = `vr_021_vol_term_structure_5_63` (rename `v63`→`v63_mean`)
- `vr_240_body_to_range_ratio_21d` -- = `vr_237_close_drive_ratio_21d` (rename `intra`→`body`)

Scalar-multiple rank-equivalents (caught by AUC+Spearman tie analysis, not by harness; commit `a01d3e0`):
- `vr_226_beckers_vol_21d` -- = `vr_221_realized_abs_variation_21d` × √(π/2)
- `vr_227_beckers_vol_63d` -- = `vr_222_realized_abs_variation_63d` × √(π/2)
- `vr_297_realized_kurtosis_21d` -- = `vr_159_quarticity_variance_ratio_21d` ÷ 3

Harness-missed value-exact (caught only by AUC+Spearman tie; commit `a01d3e0`):
- `vr_262_overnight_gap_vol_21d` -- = `vr_037_overnight_vol_21d` (max|a-b|=0; harness's value_hash failed because Pearson=NaN due to low post-warmup variance)

**Lessons for future audits:**
- **Look-ahead detection.** Look for `.shift(-N)` patterns. The harness's "100% null at entry day" finding is a strong signal of a look-ahead feature. Convert to `.shift(+N)` if the financial interpretation is preserved; otherwise delete.
- **Pandas 2.x scalar conditionals.** `Series.where(False, x)` no longer works -- replace with `pd.Series(x, index=...)`. Same for `Series.mask(True, x)` etc. Watch for these patterns in older feature code.
- **Confirming MAD's scalar-multiple finding pattern.** This is the second family where AUC+Spearman tie cross-reference caught dups invisible to value_hash. Now considered standard practice; recipe lives in MAD section above.

### `crash_speed_base` (commits `15a82fb`, `3994d3c`)

**Hybrid family**: 211 of 221 cs_ functions take only `close/high/low/open/volume` (215 bindable initially, 4 deleted post-fix); 10 need fundamentals (cs_101-cs_110 in `_076_150.py`: `revenue`, `netinc`, `fcf`, `debt`, `equity`, `assets`).

**Audit-driven deletes (4 dups + 1 constant)**:

Formula-exact dups under variable-rename (commit `15a82fb`; harness's lexical formula_hash missed them):
- `cs_082_waterfall_count_63d` -- = `cs_065_new_low_frequency_63d` (rename `low_63`→`low`; both: at_low = close ≤ rolling_min(close,63)*1.001; rolling(63).sum())
- `cs_133_max_5day_drop_63d` -- = `cs_068_worst_week_in_63d` (rename `r5`→`weekly_r`; both: close.pct_change(5).rolling(63,30).min())

Degenerate-CVaR value-exact dup (commit `3994d3c`):
- `cs_159_cvar_1pct_63d` -- value-equiv to `cs_004_max_daily_drop_63d` (rolling 63d min). With W=63 and percentile=0.01, np.percentile interpolates strictly between sorted[0] and sorted[1], so `tail = {min}` and `mean(tail) = min`. The "1% CVaR" implementation degenerates to rolling min for any window where percentile(0.01) lies between min and 2nd-min — i.e. any non-tied 63d window. Same disposition as a formula-exact dup since the math identity holds for the realistic data regime.

Always-zero constant (commit `3994d3c`):
- `cs_222_negative_surprise_magnitude_63d` -- 100% sample tickers return constant 0 at entry-day. Mean of returns < mu-2σ is NaN for windows with no extreme events; trailing `.fillna(0.0)` collapses to constant. Same disposition as `bp_069_consecutive_inside_bars` and `vr_*` always-zeros.

**Pre-fn timing audit**: 7 functions > 100 ms threshold on 1500-row synthetic close (Hurst exponent cs_174/175, Cornish-Fisher VaR cs_181-183, modified Sharpe cs_225, superexp test cs_200), all in file 3 — totalling ~6 s. No multi-hour-stuck risk; harness completed without intervention. Total runtime 50.2 min on 100 entries × 1500 days (file 3 dominates at 45.8 min due to scipy.stats per-window calls). Acceptable; not pursuing perf fixes.

**Lesson for future audits:**
- **Lexical-rename invisible to formula_hash.** Two of three dup pairs here were textually identical except for variable names (`low_63`/`low`, `r5`/`weekly_r`). The harness reports them as value-exact (which they are), but they're ALSO formula-exact under alpha-renaming — qualifying for AUTO-APPLY. When manual inspection confirms textual equivalence up to renaming, treat as auto-apply rather than ask-first.
- **Degenerate quantile + tail for short windows.** `np.percentile(x, p)` with `p*n_samples < 1` always yields a value strictly between sorted[0] and sorted[1] (linear interpolation), making `x[x <= threshold]` collapse to `{min}`. cs_159 was a CVaR but degenerate to rolling min. Future: flag any rolling-apply CVaR/quantile pattern with percentile × window < 1 as a likely degeneracy.

### `volume_at_capitulation_base` (commits `33000f3`, `8611993`)

**Hybrid family**: 282 of 300 vac_ functions take only `close/high/low/open/volume`; 18 need fundamentals (`revenue`, `netinc`, `fcf`, `debt`, `equity`, `assets`, and the new `instownpct` column). Unbindables: file 2 has vac_116, 121-123, 125, 146-150 (vac_146-150 are the `instownpct` ones); file 4 has vac_256-259, 262-265.

**Performance vectorizations (commit `33000f3`)**: 3 standard-pattern autocorrs in file 3:
- `vac_211_vol_autocorr_lag1_21d`: 135 → 0.4 ms (~380x)
- `vac_212_vol_autocorr_lag5_63d`: 136 → 0.4 ms (~370x)
- `vac_213_vol_autocorr_lag1_63d`: 143 → 0.5 ms (~280x)

`rolling(W).apply(autocorr(lag=k))` → `rolling(W-k, min_periods=mp-k).corr(s.shift(k))`. min_periods adjusted by `lag` (autocorr inside the window operates on `W-k` pairs, so the new corr's mp counts pairs not raw obs). Verified <1e-9 vs source on rand_walk + sinusoid + volume signals.

**vac_222 left as-is**: same per-call cost (~145 ms, ~3.6 min on 1500 stocks — not a bottleneck) but inlines the same lag-1 21d autocorr inside `-log(2)/log(clip(ac, 0.01, 0.99))`. The downstream log near 0.99 amplifies tiny FP autocorr differences (~1e-11 at the autocorr layer) to ~1e-8 at the function output, exceeding the <1e-9 verification gate. Pure FP propagation, not algorithmic — but per HANDOFF policy, escalate rather than apply.

**Surgical edit (commit `8611993`)**: 1 formula-exact + value-exact dup pair flagged.
- `vac_118_cap_vol_to_float_turnover(close, volume)` body was `_safe_div(volume, _sma(volume, 252))` — identical to `vac_003_vol_spike_252d`. Function name promised something more specific ("Capitulation day turnover proxy") and the signature took `close` (unused). Rather than auto-delete, **rebodied to match the name's promise**: mask the 252d float-rotation turnover by the family's existing strict cap-day definition (`vol_spike > 2 AND ret < 0`, mirroring vac_025/026). Resulting signal is sparse — returns 0 on most days, retains turnover magnitude on flagged cap days. User confirmed surgical-edit choice over delete.

**Lesson for future audits:**
- **When a dup body is generic but the function name promises specificity, propose a surgical edit before auto-deleting.** The name `cap_vol_to_float_turnover` carries semantic intent the body never delivered (mirror to vac_011-017 cap-day-masked turnover features but at 252d cadence). Surgical rebody preserves the slot AND the implied feature instead of dropping it. Only viable when the family already has a consistent definition to mirror — vac_025/026 supplied it here.

### `revenue_level_base` (commits `5e7ad38`, `407908a`, `ec6f05c`, `c65fbb3`)

**First Path B audit.** Family is 100% fundamentals — every rl_ function takes `revenue` plus other Sharadar SF1 columns (no OHLCV-only signal). The db-direct harness skips the entire family with `missing_inputs=[revenue, ...]`. Built a **synthetic-fundamentals mini-harness** at `%TEMP%\temp_rl_mini_harness.py` (delete after use): deterministic Series for ~50 input columns (`_walk` for prices/volume; `_step` with quarterly jumps for fundamentals like revenue/assets/equity/netinc/etc.), runs every function, captures errors / all-NaN / constants / formula-exact (sha256 of body) / value-exact (sha256 of rounded values).

**Initial run (300 fns)**: 0 errors, 0 all-NaN, 0 constants, 0 formula-exact dups, 7 value-exact dup groups.

**Triage of 7 dup groups:**

*Auto-applied (4 formula-exact-under-rename — same body, different name/docstring/local-var):*
- `rl_119_revenue_level_regime_252` — same body as `rl_039_revenue_vs_trailing_4q_mean` (`mu` → `sma`)
- `rl_120_revenue_level_regime_504` — same body as `rl_040_revenue_vs_trailing_8q_mean`
- `rl_224_revenue_to_assets_power` — literal-identical body to `rl_052_log_revenue_to_log_assets`
- `rl_281_revenue_per_diluted_share_to_close_ratio` — literal-identical body to `rl_187_dilution_adjusted_revenue_yield`

*User-approved (3 cancellation-equivalent — `(rev/shares)/(X/shares) == rev/X` algebraic identity):*
- `rl_080_revenue_per_share_to_book_per_share` == `rl_005_revenue_to_equity`
- `rl_081_revenue_per_share_to_fcf_per_share` == `rl_019_revenue_to_fcf`
- `rl_082_revenue_per_share_to_earnings_per_share` == `rl_020_revenue_to_netinc`

The per-share normalization adds zero information when both numerator and denominator are scaled by the same `sharesbas`. Edge case where `shares == 0` differs (per-share variant returns NaN; basic ratio finite), but on Sharadar SF1 with live tickers shares is always positive.

**Synthetic-data false positive caught**: scalar-multiple scan flagged `rl_042` / `rl_043` / `rl_140` as a 3-clique with cosine-sim=1, ratio=1, std=0. Body inspection showed they compute `revenue / max(W-day window)` for W ∈ {504, 1260, ∞}. The false positive came from the synthetic revenue series having predominantly positive drift (jump mean +0.02), so the running max keeps refreshing to recent peak ≈ current revenue and all 3 windows converge. Verification on a custom drawdown signal (4 cycles: up/down/up/down) showed actual divergence up to 0.41 between windows. **Not real dups**, kept all 3.

**Lesson for future Path B audits:**
- The synthetic-data driver is good for *flagging* candidates but bad at distinguishing real dups from synth-bias artifacts when the function pair is sensitive to specific signal characteristics (drawdowns, sign changes, regime shifts). For any flagged dup group, always sanity-check by reading the bodies; if the math could plausibly differ on a different input regime, build a targeted verification signal before deciding. Cost: ~30 sec to write a stress signal vs ~1 min to delete a working feature in error.
- The Path B mini-harness pattern is reusable for any family where every function takes fundamentals. The synthetic input dict (~50 Series) is the only family-specific bit; the dup-group + constant + error machinery is family-agnostic. Future Path B audits can reuse `%TEMP%\temp_rl_mini_harness.py` as a starting template.

**Final state**: 293 / 293 clean within base set (registry counts: file 1 = 75, file 2 = 70, file 3 = 74, file 4 = 74). Re-ran mini-harness post-fix: 0 errors / 0 all-NaN / 0 constants / 0 formula-exact dups / 0 value-exact dups.

### `revenue_level` cross-tier dedup (tab 7-cont, commit `aa25895`)

After tab 10's deriv-only audit reported "100/100 clean as audited, no source changes", tab 7-cont independently re-verified by extending the mini-harness to scan **base ↔ derivative** registries together (393 total functions: 293 base + 100 deriv). The deriv-only scope had missed cross-tier overlap.

**Found and fixed:** 3 cross-tier formula-exact dups — `rl_227_revenue_to_sgna_roc_252`, `rl_229_revenue_to_rnd_roc_252`, `rl_231_revenue_to_ebitda_roc_252` in base (`rl_226_300` chunk) had literal-identical bodies to `rl_2d_v2_001/002/003` in `revenue_level_2nd_derivatives_v2.py` (same `_safe_div` and `_roc` inline helpers; same `raw = _safe_div(rev, X)` then `_roc(raw, TRADING_DAYS_YEAR)` pattern). Per CLAUDE.md tier semantics (`base = level/raw ratios; 2nd_derivatives = QoQ ROC of base`) these belonged in the derivative tier; user chose delete-from-base. Base `_226_300` registry: 74 → 71. Final base count 290 / 290.

**1 scalar-multiple near-miss kept by design:** `rl_291_log_revenue_diff_63` (= `log(rev) - log(rev.shift(63))`) ↔ `rl_2d_013_log_revenue_roc_63` (= `_roc(log(rev), 63)` = `(log(rev) - log(rev.shift(63))) / |log(rev.shift(63))|`). Cosine sim = 0.999992, ratio_mean = 21.06, ratio_std_rel = 3.78e-3. The ratio is exactly `1 / |log(rev.shift(63))|` — on synthetic data with revenue ~1e9, `log(rev) ≈ 20.7` and the ratio is near-constant; on real data with revenue varying 2-3x across years, `log(rev)` varies ±0.7 and the ratio varies ~3.5%. Conceptually distinct features (log-return is a standard quantity; ROC-of-log applies an unusual scaling), kept both.

**Lessons:**
1. **Cross-tier scope must be explicit.** A "derivative audit" that scans only the 4 derivative files will miss base-vs-deriv overlap. Always include the base registry when verifying derivatives, and include the derivative registries when verifying the base. The harness change is one line: load both registry sets before the dup-hash pass.
2. **Misplaced ROC features in base are an audit hazard for `_roc_X` named base functions.** When a base file contains functions named `*_roc_*`, treat them as suspect-tier-misplacement candidates and explicitly cross-check against any sibling derivative file before declaring the base done.

**Cleanup**: deleted scratch `temp_rl_deriv_verify.py` + outputs per `feedback_temp_scripts.md`.

---

## `capital_allocation_snapshot` (all tiers, tab 18, Path B)

**Date:** 2026-05-09. **Files:** 8 (4 base × 75 + 2 2nd-deriv × 25 + 2 3rd-deriv × 25). **Functions:** 400 → 395 post-fix. **Commits:** `447528c`, `59c486d`, `a3964b2` (3 fix commits, one per file affected) + `d2a3537` (HANDOFF claim).

**Cadence:** quarterly Series. `periods=4` means 4 quarters (YoY), max window = 20 quarters. The TRADING_DAYS_* constants exist in helpers but no feature body uses them — every period in the bodies is a small int (1, 4, 8, 12, 20). Same convention as `profitability_snapshot` and `rd_and_intangibles`.

**Inputs union (36 cols):** `assets`, `capex`, `cashnequsd`, `cor`, `debt`, `deferredrev`, `depamor`, `dividends`, `equity`, `fcf`, `goodwill`, `gp`, `intangibles`, `intexp`, `inventory`, `investments`, `liabilities`, `marketcap`, `ncff`, `ncfi`, `ncfo`, `netinc`, `opex`, `opinc`, `payables`, `receivables`, `retainedearnings`, `revenue`, `rnd`, `sbcomp`, `sgna`, `sharesbiz`, `shareswa`, `tangibles`, `taxexp`, `workingcapital`. Non-Sharadar names (binding-layer translation flag, LS precedent): `cashnequsd`, `retainedearnings`, `dividends`, `marketcap`, `shareswa`, `sharesbiz`.

### Multi-tab race notice

When my session started, `%TEMP%\temp_cas_mini_harness.py` already existed (timestamped ~30s before my session). Another tab had begun the family but had no commits, and the pre-existing harness was daily-cadence (would misreport every YoY/QoQ function as constant-zero). Asked the user; user directed "Keep working on row 20." Replaced the temp harness with a quarterly-cadence version.

### Triage (single ASK with 4 options; user chose "All 3 deletes + surgical edit")

**5 dup deletes:**
1. `cas_078_total_reinvestment_to_revenue` == `cas_017_rnd_plus_capex_to_revenue` — both `_safe_div(rnd + capex.abs(), revenue)`. Formula-exact. **AUTO-APPLY** (file 2 commit `447528c`).
2. `cas_289_revenue_per_dollar_invested_capital` == `cas_089_capital_turnover` — both `_safe_div(revenue, debt + equity)`. Formula-exact. **AUTO-APPLY** (file 4 commit `a3964b2`).
3. `cas_158_eva_to_invested_capital` == `cas_155_eva_spread_proxy`. Algebraic identity: `(NOPAT − IC·iw) / IC = NOPAT/IC − iw = roic − iw`. ASK FIRST → user-approved (file 3 commit `59c486d`).
4. `cas_182_roe_dupont` == `cas_221_roe`. DuPont 3-factor cancellation: `(N/R)(R/A)(A/E) = N/E`. ASK FIRST → approved (commit `59c486d`).
5. `cas_183_roe_5factor` == `cas_221_roe`. DuPont 5-factor: `(N/EBT)(EBT/OI)(OI/R)(R/A)(A/E) = N/E`. ASK FIRST → approved (commit `59c486d`).

**1 surgical edit (preserves naming intent for value-dup):**
- `cas_141_net_equity_issuance` was literal `_pct_change(shareswa, periods=1)` — value-exact dup of `cas_031_share_change_qoq`, but the function name promised "issuance flag / dilution event" not raw qoq. Rebodied to `_pct_change(shareswa, periods=1).clip(lower=0)` → positive-only dilution magnitude. Mirrors `cas_050_debt_issuance_to_assets` pattern (`debt_chg.clip(lower=0)`). ls_148 / vac_118 naming-bug precedent. (file 2 commit `447528c`).

### Kept by design

**2 academic-trace value-exact pairs:**
- `cas_062_wc_to_assets` == `cas_226_altman_x1` (working capital / assets, Altman X1 liquidity component).
- `cas_090_asset_turnover` == `cas_230_altman_x5` (revenue / assets, Altman X5 asset utilization component).

Composite `cas_231_altman_z_composite` literally inlines x1–x5: `1.2*x1 + 1.4*x2 + 3.3*x3 + 0.6*x4 + 1.0*x5`. Each model variable must be individually addressable for distress-model traceability. Same disposition as `ls_061/151/170/188` (Altman X1 / Springate A / Ohlson WCTA / generic NWC/Assets in leverage_and_solvency).

**1 NOPAT-precedent scalar-mult pair:**
- `cas_025_div_to_equity` (quarterly) vs `cas_136_div_yield_on_equity` (annualized = `dividends.abs() * 4 / equity`). Ratio = 4 exactly. Deliberate domain reformulation per the same precedent as profitability_snapshot's 14 NOPAT pairs at ratio 1.265823 = 1/0.79 and leverage_and_solvency's `ls_023/297` at 1/252 days unit conversion.

### Re-run post-fix

`temp_cas_mini_harness.py` re-run on the post-fix tree:

| Metric | Pre-fix | Post-fix |
|---|---:|---:|
| Functions | 400 | 395 |
| Errors | 0 | 0 |
| All-NaN past warmup | 0 | 0 |
| Constants past warmup | 0 | 0 |
| Formula-exact dup groups | 0 | 0 |
| Value-exact dup groups | 7 | **2** (both academic-trace KEEP) |
| Scalar-mult pairs | 10 | **3** (1 NOPAT-annualization + 2 academic-trace at ratio=1) |

### Lessons

1. **Quarterly-cadence detection is critical for Path B harness design.** Three families to date are quarterly: `profitability_snapshot`, `rd_and_intangibles`, `capital_allocation_snapshot`. Tell from period args (small ints 1/4/8/12/20 + docstring annotations like "(4 quarters)" / "8q vol"). A quarterly family fed daily-fwd-fill data computes 4-day pct_change instead of YoY, yielding a flood of false constants and false value-exact dups.

2. **Multi-tab race resolution is judgment, not policy.** Per HANDOFF "second to start should release", I would have released. But the user noted (a) the other tab had no fix commits, (b) the pre-existing harness had a cadence bug that would have produced wrong audit results, so directed me to keep working. Surface the conflict explicitly rather than racing or releasing automatically.

3. **DuPont-decomposition collapses are cancellation-equivalent dups.** When a k-factor identity `Π(s_i / s_{i-1}) = s_n / s_0` telescopes, the multiplied-out feature is value-exact to the bottom-line ratio. The decomposition's analytical value lives in the *components* (which are addressable as separate features here: cas_021 / cas_090 / cas_041 etc.), not in the multiplied-out aggregate. Auto-applicable per RL `rl_080/081/082` precedent.

4. **EVA framing dups: spread vs ratio.** `EVA = NOPAT − IC·iw` is the underlying. `EVA / IC = roic − iw` (spread form, `cas_155`) and `(NOPAT − IC·iw) / IC` (literal divided form, `cas_158`) are algebraically identical. Prefer the spread form for numerical stability and semantic clarity.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_cas_mini_harness.py`
- `%TEMP%\temp_cas_results.json`


---

### `debt_trajectory` (all tiers, tab 22, surgical-rebody-everything per LS / CAS / VAC precedent; commits `dad0256`, `b5db6af`, `2516c4b`, `abb7bab`, `3325c5e`, `bba1477`, `c601f02`, `b8aa5dd`, `95bd8a5`, `30d9761`, `73de82f`, `6030811`, `3725177`, `796e957`, `ea6c55a`, `de68b98`, `28fce41`)

**Family scope.** 14 files / 750 functions = 8 base (chunks 001-600, 75 fns each) + 3 second-deriv (idx 001-025/026-050/051-075; 25 each) + 3 third-deriv (same split). Daily-cadence (uses `TRADING_DAYS_*` constants for `.shift(63/252)`/rolling).

**Path B mini-harness.** 5 profiles (healthy growth / leveraging up / deleveraging / distressed / cash-rich) x 1500 daily obs forward-filled from quarterly anchors. 31 input columns including Path-B-first non-Sharadar columns:
- `cashnequsd` (vs prior audits' `cashneq`).
- `currentassets` / `currentliabilities` (vs prior `assetsc` / `liabilitiesc`).
- `divyield` (annual dividend yield as decimal -- used by 3 functions: `dt_473_dividend_payout_to_debt_service`, `dt_474_dividend_vs_interest_priority`, `dt_488_debt_to_total_payout`). Not in Sharadar SF1 -- needs binding-layer translation map (LS `cashnequiv`/`retainedearnings`/`ltdebt` precedent).
- `depreciation` (alias for `depamor` per registry).

### User direction: ZERO DELETES, surgical-rebody all `_ex_` slots

Initial harness pass returned 67 dup groups + 16 scalar-mult candidates. Asked user how to handle the systemic naming-collision in the `_ex_` derivative files (~30+ slots whose bodies didn't match their docstrings -- e.g., `dt_2d_ex_028_altman_z_roc` returned `CA / revenue` not Altman Z). User chose option 3: surgical-rebody everything per LS tab 14 / CAS tab 18 / VAC tab 6 precedent -- "preserves every slot semantically."

This drove a much larger surgical-edit campaign (~80 rebodies across 12 files) than past audits, which typically had 5-15 deletes + a few surgical edits.

### Two-pass surgical-rebody campaign

**Pass 1** (commits `b5db6af` through `73de82f`):

*Base-file rebodies* (25 surgical edits across 5 files):
- `base_076_150`: `dt_128_equity_multiplier_chg` -> `_diff` (absolute YoY delta) instead of `_pct_change`; `dt_135_debt_growth_acceleration_2yr` -> 2yr-stride growth accel instead of 1yr-stride.
- `base_151_225`: `dt_155` cash/(CL+intexp.abs()); `dt_171` cash/(CL+debt); `dt_172` `_diff` instead of `_pct_change`; `dt_183` NWC/liabilities (broader denom); `dt_212` cash + 0.75*receivables / CL (Penman-style 25% AR haircut).
- `base_226_300` (8 EV/leverage rebodies): `dt_226` smoothed-debt EV; `dt_246` gross-EV (mcap+debt)/revenue; `dt_250` (debt-cash)/EV [later re-rebodied to debt/252d-mean(EV)]; `dt_263` 2yr-mean smoothed market leverage; `dt_265` EV/TTM-NI; `dt_271` (debt-cash)/EV [later re-rebodied to (debt-cash)/252d-mean(mcap)]; `dt_286` EV/TTM-equity; `dt_297` EV/(equity-retearn) contributed-capital denom.
- `base_376_450` (6 rebodies): `dt_391` 2yr-stride debt-intensity; `dt_400` net-investment / NET debt; `dt_432` `roe-roa` absolute spread (drop /roa normalization that algebraically collapses to L/E); `dt_437` revenue/(debt+CL); `dt_438` `_diff` instead of `_pct_change`; `dt_444` intexp/(ebitda-|capex|).
- `base_451_525` (4 rebodies): `dt_481` opinc / capitalized debt service (debt + 5*intexp.abs()); `dt_489` (debt+equity)/revenue total-capital intensity; `dt_496` debt/(debt+equity+CL) broader funding denom; `dt_498` 2yr-IQR robust dispersion (vs `_053`'s rolling std).

*Main 2nd-derivatives rebodies* (3 surgical edits): `dt_2d_151/152/160` switched to 2-stride (semiannual or 2yr) windows so they're distinct from base-tier `dt_016/017/021` 1-stride forms.

*`_ex_` derivative-file full-rebody passes* (~50 surgical edits across 4 files):
- All 25 slots in `2nd_derivatives_026_050` rewritten so each body computes its named formula. Examples:
  - `dt_2d_ex_028_altman_z_roc`: full `1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5` Altman Z then ROC. Was returning `CA/revenue`.
  - `dt_2d_ex_029_ohlson_o_roc`: full Ohlson O composite (-0.407*ln(A) + 6.03*L/A + ... 6 terms) then ROC. Was returning `A/NCFO`.
  - `dt_2d_ex_030_merton_dd_roc`: `ln(V/D)/sigma` where `sigma = annualized 1yr close-return vol`; uses `close` (was being ignored).
  - `dt_2d_ex_032_tobins_q_roc`: `(mcap+debt)/assets` (uses `assets` denom). Was returning `mcap/debt`.
  - `dt_2d_ex_033_roic_roc`: NOPAT-style `(NI + 0.79*intexp.abs()) / (debt+equity)`. Was ignoring `intexp` + `debt`, returning `NI/E`.
  - `dt_2d_ex_040_fixed_charge_coverage_roc`: `ebitda / (intexp.abs() + 0.05*CL)` where `0.05*CL` approximates lease commitments.
  - `dt_2d_ex_043_springate_s_roc`: full `1.03*A + 3.07*B + 0.66*C + 0.4*D` Springate S composite.
  - `dt_2d_ex_047_debt_to_tangible_roc`: `debt / (assets - intangibles)`. Was ignoring `intangibles` [later re-rebodied to use 252d-mean(tangible) -- see Pass 2].
  - `dt_2d_ex_049_lt_debt_to_equity_roc`: `(debt - 0.30*CL) / equity` LT-debt approximation. Was returning `debt/CL`.
- All 25 slots in `2nd_derivatives_051_075` rewritten similarly:
  - `dt_2d_ex_052_debt_coverage_margin_roc`: `(ebitda - intexp.abs())/debt` cushion (uses all three inputs).
  - `dt_2d_ex_055_total_capital_efficiency_roc`: `revenue / (mcap + debt)`.
  - `dt_2d_ex_056_debt_to_opex_roc`: `debt / (revenue - opinc)` where `opex = revenue - opinc`.
  - `dt_2d_ex_060_zmijewski_x_roc`: full `-4.336 - 4.513*X1 + 5.679*X2 - 0.004*X3` Zmijewski composite.
  - `dt_2d_ex_061_debt_to_avg_ebitda_3yr_roc`: `debt / 3yr-rolling-mean(ebitda)` (was point-in-time).
  - `dt_2d_ex_064_accruals_to_debt_roc`: `(NI - NCFO) / debt`.
  - `dt_2d_ex_071_book_vs_market_leverage_roc`: `D/(D+E) - D/(D+M)` spread (was returning `D/E`).
  - `dt_2d_ex_073_financial_leverage_effect_roc`: `NI/OpInc` (matches name; broken from `_ex_064` dup by separately rebodying `_ex_064`).
  - `dt_2d_ex_074_invested_capital_growth_roc`: `pct_change(D+E, YR)` then `pct_change(QTR)` (proper acceleration of IC growth).
  - `dt_2d_ex_075_debt_to_peak_ebitda_roc`: `debt / 5yr-rolling-max(ebitda)`.
- All 25 slots in `3rd_derivatives_026_050` and `3rd_derivatives_051_075` mirror the 2nd-deriv rebodies but use a shared `_jerk(level)` helper = `pct_change(QTR).diff(QTR).diff(QTR)`. Single-helper-per-file pattern reduces noise.

**Pass 2** (commits `6030811` through `28fce41`): re-running the harness post-Pass-1 caught 7 secondary collisions where Pass-1 rebodies happened to match an existing main-tier sibling that I hadn't rebodied (because it was already canonical). Re-rebodied to use 252d-trailing-mean smoothed-denom variants (`ls_121` precedent):
- `dt_2d_ex_047` vs `dt_2d_166` (both `debt/(assets-intangibles)`): switched `_ex_047` to `debt / 252d-mean(assets-intangibles)`.
- `dt_2d_ex_053` vs `dt_2d_174` (both `(debt-cash)/mcap`): switched `_ex_053` to `(debt-cash)/EV` (full denom, bounded `[-1, 1]`).
- `dt_2d_ex_057` vs `dt_2d_163` (both `intexp.abs()/revenue`): switched `_ex_057` to `intexp.abs() / 252d-mean(revenue)`.
- `dt_3d_ex_047/053/057` mirror the same swaps for the jerk operator.
- `dt_250` + `dt_271` in `base_226_300` (both Pass-1 rebodies happened to match `dt_061`'s `(debt-cash)/EV` form): switched `dt_250` to `debt / 252d-mean(EV)` and `dt_271` to `(debt-cash) / 252d-mean(mcap)`.
- `dt_370` in `base_301_375` was literal-identical to `dt_317_ohlson_o7`: switched `dt_370` to `ncfo / LT-only-liabilities` (`liabilities - currentliabilities`).
- `dt_478` in `base_451_525` was literal-identical to `dt_410`: switched `dt_478` to `debt / 252d-mean(sgna.abs())`.

### Final findings

**750 / 750 functions ok.** 0 errors / 0 all-NaN. **Down from 67 -> 26 dup groups (-41); 750 fn slots PRESERVED; zero deletes.**

**26 KEEP-BY-DESIGN dup groups remain:**
- **10 academic-trace dup groups**: Altman X1 (in `dt_169` / `dt_301` / `dt_313`), Altman X3 (`dt_106` / `dt_303`), Altman X4 (`dt_107` / `dt_304`), Altman X5 (`dt_108` / `dt_305` / `dt_430`); Ohlson O2 (`dt_070` / `dt_312` / `dt_324`), Ohlson O3 (in same group as Altman X1), Ohlson O6 (`dt_316` / `dt_323`), Ohlson O7 (`dt_317`); Zmijewski X1 (in same group as Ohlson O6), Zmijewski X2 (in same group as Ohlson O2), Zmijewski X3 (`dt_090` / `dt_325`). Each model variable individually addressable for explainability per `ls_061/151/170/188` precedent.
- **14 sample-bias dup groups**: different X/Y inputs that coincide on healthy-synth because synthetic uses constant relations (`intexp = const*debt`, `ncfo ~ const*ebitda`, `opinc = 0.78*ebitda`). All real-data divergent. Examples: `dt_109_debt_to_ncfo` vs `dt_004_debt_to_ebitda`; `dt_2d_153_interest_coverage_roc_qoq` vs `dt_2d_170_ncfo_to_debt_roc_qoq`; `dt_3d_184_interest_burden_jerk` vs `dt_3d_195_debt_gp_jerk`.
- **2 clip-differentiated dup groups**: `dt_137` cash on `equity.clip(lower=0)` (vs `dt_001`'s raw `D/E`); `dt_198` `.clip(upper=50).fillna(50.0)` cap on near-term-pressure (vs `dt_208`'s uncapped form). Both diverge on real distressed firms.

**27 sample-bias constants kept**: negative-equity / distress / buyback flags (always 0 on healthy synth); Merton DD saturated at 10 on healthy synth; Merton percentiles ~0.5; cash-burn-runway needs sustained negative `ncfo`. Same disposition as `bss_223-228` / `cfs_d3_046` / `ps_270`.

**13 KEEP-BY-DESIGN scalar-mults**:
- 4 sample-bias `0.78` / `1.282` family (synth `opinc = 0.78*ebitda` choice produces deterministic ratio).
- 4 stress-test thresholds: `interest_coverage_stress_50/75` are `ic/2` and `ic/1.33` by intent; `debt_service_stress_50` similarly; `chs_excess_return` vs `distress_risk_premium` ratio = 10. NOPAT-precedent KEEP.
- 1 unit-conversion `1/12` (`cash_burn_months` from cash/CL).
- 1 stress `0.667` between two stress thresholds.

### Lessons worth carrying

1. **`_ex_` derivative files in this repo systematically have buggy bodies that don't match docstrings.** Pattern: function accepts the proper input columns for the named formula (e.g., 8 args for Altman Z) but body computes a simpler 2-input ratio. Probably auto-generated stubs that were never finished. Other audits should grep for this pattern before harness time.

2. **Surgical-rebody-everything (zero-deletes) campaigns can drive ~80 edits in a single family.** Two-pass approach is essential: Pass 1 rebodies all naming-collision dups; Pass 2 fixes the secondary collisions where Pass-1 happened to match an existing sibling. Plan time accordingly.

3. **252d-trailing-mean smoothed denominator (`ls_121` precedent) is the workhorse second-pass differentiator.** When two slots both compute `X/Y` at point-in-time, switching one to `X / 252d-mean(Y)` gives a meaningful "smoothed" variant bounded by the same scale and conceptually related, without inventing a new formula.

4. **Sample-bias dups are unavoidable on healthy-synth.** Any feature pair `X/Y` vs `X/Z` where `Z` is a constant fraction of `Y` on synth will show as value-exact (because `pct_change` cancels constants) on rolling/derivative tiers. Real-data variants always diverge. Documenting "sample-bias" as KEEP-BY-DESIGN per `ps_270` / `cfs_d3_046` precedent is critical.

5. **`divyield` isn't a Sharadar SF1 column** but appears in `dt_473_dividend_payout_to_debt_service`, `dt_474_dividend_vs_interest_priority`, and `dt_488_debt_to_total_payout`. Need binding-layer translation map (similar to `cashnequiv`/`retainedearnings`/`ltdebt` precedent from LS tab 14). Pipeline-side issue, flagged for future work.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_dt_mini_harness.py`
- `%TEMP%\temp_dt_results.json`
- `%TEMP%\temp_dt_dump_dups.py`
- `%TEMP%\temp_dt_dups_dump.txt`
- `%TEMP%\temp_dt_journal_entry.md`
- `%TEMP%\temp_dt_audits_entry.md`

## `cash_flow_acceleration` (all tiers, this-tab, Path B)

**Family scope.** 14 files / 750 functions = 8 base (chunks 001-600, 75 fns each) + 3 second-deriv (idx 001-025/026-050/051-075; 25 each) + 3 third-deriv (same split). Daily-cadence (uses `.shift(63/252/504/1008/1260)`). Function prefix `cfa_`. 100% Path B (every fn takes `fcf`/`ncfo`/`capex` family); hybrid only via `close`/`volume`/`shareswa`. 41 input cols, all standard Sharadar SF1 + OHLCV.

**Path B mini-harness.** 5 profiles × 1500 daily rows × 41 input cols, daily-cadence quarterly-anchor forward-fill. Per-profile scaling (1.0 + 0.3·idx) and drift (0.5%-2.5%/qtr). `ncfo` allowed 20% sign-flip per-quarter to exercise sign-divergent cases. Warmup=800 (clears 504d shifts; 5y `.shift(1260)` features run with reduced support — no false-positive constants observed there).

### Triage outcome

40 algebraic-identity dup deletes auto-applied per HANDOFF policy + ve/sd/cas precedent. 11 commits across 10 affected files (commit `f17c097` was incomplete due to a transient editor race; `ea04d4f` finished the work for cfa_311). 750 → 710 fns. 0 errors / 0 all-NaN / 0 unexplained dups post-fix.

| Pattern | Count | Notes |
|---|---:|---|
| ufcf-* aliases of fcf-* under Sharadar `fcf = ncfo + capex` | 8 | cfa_095/096/097, cfa_463/464/465/466/467 — `(ncfo - \|capex\|) == (ncfo + capex) == fcf` since capex signed negative |
| Verbose-rename of fundamentals ratios (literal formula-exact) | 19 | cfa_041=cfa_015, cfa_043/044/045=cfa_005/007/008, cfa_092=cfa_558, cfa_134=cfa_311, cfa_151=cfa_418, cfa_212=cfa_292, cfa_073=cfa_347, cfa_032=cfa_156, cfa_054=cfa_193, cfa_013=cfa_562, cfa_218=cfa_563, cfa_059=cfa_477, cfa_060/061=cfa_545/547, cfa_475/476=cfa_556/557, cfa_225=cfa_559 |
| Net-op-cycle = CCC algebra `dso+dio-dpo == (R+I-P)*252/rev` | 3 | cfa_235/236/237 = cfa_033/034/035 |
| Z-score = surprise alias `(s - mean) / std` | 4 | cfa_069/070=cfa_297/298, cfa_299/300=cfa_481/482 |
| Per-share growth `_pct_chg(X/shareswa, 252)` repeated under "dilution-adj" name | 2 | cfa_389/390 = cfa_019/022 |
| Base "_acceleration_1y" = deriv-tier "_yoy_growth_roc" pollution | 2 | cfa_027/028 → cfa_2d_003/004 (delete-from-base per RI/CFS/RL precedent) |
| Deriv tiers follow base | 2 | cfa_2d_010/cfa_3d_010 = cfa_2d_008/cfa_3d_008 |

### KEEP-BY-DESIGN

- **3 sample-bias constants** (real-data variants — same disposition as ps_270 / cfs_d3_046 / bss_288):
  - cfa_201_cash_tax_rate_proxy = `taxexp/ebt` constant 0.21 on synth (taxexp = ebt × 0.21 by design)
  - cfa_202_cash_tax_rate_chg_1y = same diff, identically 0
  - cfa_420_beneish_gmi_proxy = `gm_prev/gm` = 1 on constant-margin synth (gp = revenue × const within profile)
- **1 academic-trace pair**: cfa_167_altman_wc_ta / cfa_242_wc_to_assets — composite cfa_427_altman_composite_cf_adj inlines wc/a directly. Per ls_061/cas_062 precedent each model variable is individually addressable.
- **1 clip-differentiated pair**: cfa_105_ncfo_to_netinc_chg_1q / cfa_166_cash_earnings_quality_chg — `(ncfo-netinc)/|netinc|.diff(63) == (ncfo/netinc).diff(63)` only when netinc>0; `|netinc|` flips sign relation when netinc<0. LS ls_022/296 precedent.
- **7 synth-coincidence pairs** (real-data divergent):
  - cfa_010/cfa_267, cfa_223/cfa_478 — `netinc/revenue` constant within profile causes synth value-equality
  - cfa_025/cfa_026, cfa_060/cfa_061, cfa_216/cfa_217, cfa_325/cfa_326, cfa_590/cfa_591 — adjacent fcf↔ncfo where `|ncfo| > |capex|` always in synth → `sign(fcf) = sign(ncfo)` every day
- **21 NOPAT/days-conversion scalar-mult pairs** kept (per cas/ls precedents):
  - cfa_011/132/199 ratios `1.480494=1/(0.711)` (opinc/netinc) + `1.265823=1/0.79` (ebt/netinc) post-tax NOPAT
  - cfa_120-125 ↔ cfa_226-233 ratio `0.003968=1/252` days-conversion
  - cfa_168/426 ratio `0.714286=5/7` altman_re weight differential

### Commits

| File | Deletes | Final count | Commit |
|---|---:|---:|---|
| `_base_001_075` | 6 | 69 | `46c16b0` |
| `_base_076_150` | 3 | 72 | `ee4525d` |
| `_base_151_225` | 2 | 73 | `6e4d132` |
| `_base_226_300` | 6 | 69 | `c35300c` |
| `_base_301_375` | 1 → 2 | 73 | `f17c097` (cfa_347 only — race) + `ea04d4f` (cfa_311 follow-up) |
| `_base_376_450` | 3 | 72 | `d898eb5` |
| `_base_451_525` | 8 | 67 | `aacabea` |
| `_base_526_600` | 8 | 67 | `b946a94` |
| `_2nd_derivatives` | 1 | 24 | `83373a9` |
| `_3rd_derivatives` | 1 | 24 | `a2ff72a` |
| **Total** | **40** | **710** | |

### Lessons worth carrying

1. **Sharadar `fcf = ncfo + capex` produces a class of algebraic-identity dups** that look distinct by name (ufcf-* / "ncfo-minus-capex-*") but reduce algebraically under `capex` signed negative. With harness profiles where `fcf` is computed from `ncfo + capex`, value-hash catches them all on the first run. 8 of 40 deletes in this family were of this form.

2. **fcf-vs-ncfo sign-coincidence on healthy synth is sample-bias, not real dup.** With `|ncfo| > |capex|` always in synthetic, `sign(fcf) = sign(ncfo)` every day → `_consecutive_positive(fcf) == _consecutive_positive(ncfo)` and `_expanding_positive_pct(fcf, W) == _expanding_positive_pct(ncfo, W)`. Real-data divergent on capital-intensive firms or growth phases. Same disposition as cft fcf↔ncfo coincidence pairs.

3. **netinc/revenue constant within profile is a synth artifact** that masks real-data feature distinctions. Synth uses `netinc = revenue × (0.15+0.02p) × 0.711`, so `(netinc/revenue).diff(N) = 0` → many "X minus netinc-margin diff" features collapse to "X diff" alone. Real Sharadar has time-varying margins, so these are genuinely distinct features (cfa_010/267, cfa_223/478).

4. **Editor-race on multi-edit-per-file batches.** Initial cfa_311 + cfa_347 batch in file `_base_301_375` produced commit `f17c097` with only 1 deletion (10 lines) instead of intended 2 (28 lines); follow-up `ea04d4f` finished. The Edit tool's "file modified since read" guardrail caught the second-edit conflict but the first apparently succeeded silently against stale state. **Recommendation**: re-grep + re-Read before every Edit when batching multiple deletes per file, even if the previous Edit reported success.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_cfa_harness.py`
- `temp_cfa_harness_out.json`

## `efficiency_acceleration` all tiers (commits `6c429f8`, `153e9e7`, `282de11`, `1c89de5`)

**Family scope.** 8 files, 400 features → 382 post-fix:
- 4 base files × 75 functions (`ea_001_*` .. `ea_300_*`).
- 1 + 1 second-deriv files (`ea_2d_001..025` + `ea_2d_026..050`) — 50 fns.
- 1 + 1 third-deriv files (`ea_3d_001..025` + `ea_3d_026..050`) — 50 fns.

100 % Path B (every function takes Sharadar fundamentals; no OHLCV).

### Cadence: quarterly

Every file declares `TRADING_DAYS_*` constants but never uses them. The actual
periods passed to `.shift()`, `_delta(s, n)`, `_pct_change(s, n)`,
`_rolling_slope(s, w)` are 1, 2, 4, 8, 12 — quarters, not days.
`_annualize_qtr` sums over `rolling(4, min_periods=4)`. Same convention as
`margin_trajectory`, `capital_allocation_snapshot`, `cash_flow_trajectory`.
Path B mini-harness generates 5 profiles × 80 quarters; warmup discards first
16 rows per profile to clear the 12-quarter shifts.

### Path B mini-harness — synth gotcha

50 input columns synthesized as deterministic per-profile Series. v1 synth
produced **13 false-positive constants** (entire effective-tax / debt-mix /
asset-mix / liab-mix / netinccmn-vs-netinc clusters) and **4 false-positive
scalar-mult pairs** at ratio = 4.76 (= 1/0.21) and 0.97. Root cause: all five
mix proportions were constant scalars in synth (e.g. `taxexp = ebit*0.21`
makes `tax/ebit` mathematically constant; `debtc = debt*0.25` makes
`debtc/debt` constant; `netinccmn = netinc*0.97` makes their ratio constant).
Fix: replace each constant proportion with `np.clip(midpoint + amp*sin(...) +
noise, lo, hi)`. After regenerating, all 13 constants disappeared and the 4
false-positive scalar-mults collapsed to real signal.

**Lesson worth carrying:** any audit harness that synthesizes ratio components
with a constant scalar will mass-produce false-positive constants and
false-positive scalar-mult pairs. Make every mix proportion vary over time.
Documented in CLAUDE.md table for future Path B audits.

### Triage outcome

| Class | Count | Disposition |
|---|---:|---|
| Errors | 0 | clean |
| All-NaN | 0 | clean |
| Constants past warmup | 0 | clean (after synth fix) |
| Value-exact dup groups | 16 → 0 | 16 deleted (auto-apply) |
| Sign-flip scalar-mults (ratio=−1) | 2 | deleted (auto-apply per gc/mt precedent) |
| NOPAT scalar-mults (ratio=0.75) | 3 | KEEP BY DESIGN |

### 18 dup deletes — full enumeration

**File 1 — `efficiency_acceleration_base_001_075.py` (commit `6c429f8`, 2 deletes)**
- `ea_071_dupont_asset_turnover` ≡ `ea_022_asset_turnover` (literal-identical body
  `_safe_div(_annualize_qtr(revenue), assets)`).
- `ea_074_dupont_decomp_turnover_slope` ≡ `ea_025_asset_turnover_slope_8q` (literal-identical
  `_rolling_slope(_safe_div(_annualize_qtr(revenue), assets), 8)`).

**File 2 — `efficiency_acceleration_base_076_150.py` (commit `153e9e7`, 5 deletes)**
- `ea_076_cogs_to_revenue_trend` = `−ea_005_gross_margin_slope_8q` via algebraic
  identity GM = (R−C)/R = 1 − C/R, so slope(GM) = −slope(C/R).
- `ea_077_cogs_to_revenue_chg_1y` = `−ea_002_gross_margin_chg_1y` (same identity at delta).
- `ea_106_equity_efficiency` ≡ `ea_041_roe_level` (literal-identical
  `_safe_div(_annualize_qtr(netinc), equity)`).
- `ea_107_equity_efficiency_slope_8q` ≡ `ea_043_roe_slope_8q` (slope of same expression).
- `ea_148_gross_margin_vs_op_margin_gap_trend` ≡ `ea_080_opex_to_revenue_slope_8q`
  via algebraic identity GM − OM = (R−C)/R − opinc/R = (sgna+rnd)/R = opex/R
  (since opinc = R − C − sgna − rnd by definition of operating income).

**File 3 — `efficiency_acceleration_base_151_225.py` (commit `282de11`, 5 deletes)**
- `ea_197_ebit_ebitda_gap` ≡ `ea_124_depreciation_to_revenue` via Sharadar identity
  ebitda − ebit = depamor (depamor reported positive in Sharadar, so `depamor.abs() = depamor`).
- `ea_198_ebit_ebitda_gap_slope_8q` ≡ `ea_125_depreciation_to_revenue_slope_8q` (slope of same).
- `ea_202_gp_to_assets` ≡ `ea_100_gp_per_asset` via Sharadar identity gp = revenue − cor.
- `ea_203_gp_to_assets_chg_1y` ≡ `ea_101_gp_per_asset_chg_1y` (same identity at delta).
- `ea_204_gp_to_assets_slope_8q` ≡ `ea_102_gp_per_asset_slope_8q` (same identity at slope).

**File 4 — `efficiency_acceleration_base_226_300.py` (commit `1c89de5`, 6 deletes)**
- `ea_242_netinc_per_diluted_share_growth` ≡ `ea_220_epsdil_growth_1y` via Sharadar
  definition epsdil = netinc/shareswadil.
- `ea_257_capex_to_ncfo` ≡ `ea_252_reinvestment_rate` (literal `_safe_div(capex.abs(), ncfo)`).
- `ea_258_capex_to_ncfo_slope_8q` ≡ `ea_254_reinvestment_rate_slope_8q` (slope of same).
- `ea_290_ncfo_minus_capex_to_revenue` ≡ `ea_015_fcf_margin_level` via Sharadar identity
  fcf = ncfo + capex (capex signed negative in Sharadar), so ncfo − |capex| = fcf.
- `ea_291_ncfo_minus_capex_to_rev_slope_8q` ≡ `ea_018_fcf_margin_slope_8q` (slope of same).
- `ea_298_ev_to_ncfo_inverse_trend` ≡ `ea_236_ncfo_to_ev_slope_8q` — body is
  `_rolling_slope(_safe_div(_annualize_qtr(ncfo), ev), 8)` despite "inverse" in name.
  The "inverse" likely refers to inverting EV/NCFO into NCFO/EV, which is exactly the body —
  the function is body-identical to ea_236.

### KEEP BY DESIGN

**3 NOPAT scalar-mult pairs at ratio = 0.75** (after-tax operating-margin variant):
- `ea_006_operating_margin_level` vs `ea_103_nopat_margin` (`opinc*0.75/revenue`).
- `ea_007_operating_margin_chg_1y` vs `ea_104_nopat_margin_chg_1y`.
- `ea_010_operating_margin_slope_8q` vs `ea_105_nopat_margin_slope_8q`.

Same precedent as `ls_127`/`ls_212` (after-tax interest coverage at 1−0.21=0.79),
profitability_snapshot's 14 NOPAT pairs, `cas_025`/`cas_136` annualized vs quarterly.
Each NOPAT slot is the deliberate after-tax companion to the pre-tax operating-margin
slot — kept addressable for downstream models that want the after-tax variant directly.

### Derivative tiers — no source changes

- `ea_2d_001..050`: 50 functions, all clean (no errors, no all-NaN, no constants,
  no value-exact dups, no scalar-mult dups beyond the expected NOPAT cluster).
- `ea_3d_001..050`: 50 functions, all clean.

The two derivative files (and their `_026_050` extensions) inline their own ratio
builders (`_gm`, `_om`, `_nm`, `_fm`, `_at`, `_roic`, `_roe`, etc.) and apply
`_delta(r, n)` for 2nd-deriv (velocity) and `_delta(_delta(r, n), n)` for 3rd-deriv
(acceleration). Same self-contained pattern as `volatility_regime_2nd/3rd_derivatives`.

### Final harness state

- 382 fns registered (was 400, −18).
- 0 errors / 0 all-NaN / 0 constants / 0 value-exact dups.
- 3 NOPAT scalar-mult pairs (kept).

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_ea_harness.py`
- `temp_ea_harness_out.json`

---

## `revenue_growth` (all tiers, tab 19, Path B)

**Date:** 2026-05-09. **Files:** 8 (4 base × 75 + 2 2nd-deriv × 25 + 2 3rd-deriv × 25). **Functions:** 400 → 388 post-fix. **Commits:** `4e64424` (claim), `53196cd`, `908244b`, `020a41f`, `c0ff1a6`, `6bd94c6`, `4d56d12`, `eaaae2c`, `f35aa8d`.

**Cadence:** daily Series; `DAYS_YR=252`, `DAYS_QTR=63`. Max lookback 5yr CAGR (1260 days); synth used 1700 days for warmup margin.

**Inputs union (36 cols):** every fn takes `revenue`. Non-revenue cols span the standard fundamentals + `close`/`volume`/`sharesbas` for cap-flag/price-validation features. All Sharadar-standard; no binding-layer translation needed.

### Path B mini-harness — v1 → v2 rebuild

**v1 mistake:** built fundamentals as multiplicative scalings of revenue (`assets = revenue × 2.5`, etc.). Produced **26 false-positive constants** because `_pct_change(rev, n) − _pct_change(α·rev, n) = 0` (multiplier cancels). Every `rg_growth_vs_X_growth` feature collapsed to identically zero.

**v2 fix (RI tab 16 lesson reconfirmed):** independent random walks per fundamental column. Each col has its own (drift_extra, vol, level0); quarterly anchors via `cumprod(1 + log_steps)` with col-specific drift; 20% sign-flip injection on `CAN_BE_NEGATIVE` cols. Eliminated 25/26 false-positive constants. 5 profile types seed independent realizations.

### Triage (12 deletes + 2 rebodies)

**Cat 1 — Auto-apply formula-exact / helper-expansion (8 deletes):**

| Lower (kept) | Higher (deleted) | File | Identity |
|---|---|---|---|
| rg_039 | rg_067 | 001_075 | var-rename `ttm_prev` → `prior` |
| rg_039 | rg_139 | 076_150 | helper-expansion of `_pct_change(ttm,252)` |
| rg_053 | rg_068 | 001_075 | var-rename + `.copy()` no-op |
| rg_081 | rg_176 | 151_225 | var-rename only |
| rg_050 | rg_086 | 076_150 | var-rename `intensity` → `turnover` |
| rg_117 | rg_269 | 226_300 | var-rename `pg` → `tr` |
| rg_2d_003 | rg_009 | 001_075 (base) | base-vs-deriv pollution; accel → deriv tier |
| rg_2d_002 | rg_010 | 001_075 (base) | base-vs-deriv pollution; same precedent |

**Cat 2 — User-approved NDR-proxy algebraic-identity (3 deletes):** for positive revenue, `ndr = rev/rev.shift(252) = yoy + 1`, so `ndr.diff(N) ≡ yoy.diff(N)` for any N. Deleted rg_2d_032/033 + rg_3d_032. `_base_ndr_proxy` orphan helper removed; `_2d_ndr_roc` retained for rg_3d_033 (distinct stride).

**Cat 3 — User-approved value-exact-via-positive-revenue-identity (1 delete):** rg_034 ≡ rg_036 since `(g > 0) ⟺ (rev > rev.shift(63))` for revenue ≥ 0 (Sharadar pre-IPO is NaN not 0). User chose %-growth form: kept rg_034.

**Cat 4 — User-approved surgical rebody for naming-bug (2 rebodies):** rg_126/127 monotonic_score_4q/8q originally produced [0, 63] (divisor `/4`, `/8` over 252d/504d rolling sums) when names promised [0, 1]. Same naming-bug class as ls_148, vac_118, cas_141, ve_424. Rebodied to longest-consecutive-up-streak normalized to [0, 1] via run-length encoding (`np.diff` on padded boundary, O(window) inner). New shared helper `_longest_up_streak_norm`.

### Kept by design

- **rg_166_rev_growth_determinism_proxy** sample-bias constant: fwd-fill artifact (`g.diff()` non-zero only at quarter boundaries → `same_sign` ≈ 0.96 always). Real daily-varying data fluctuates. Same disposition as ps_270/cfs_d3_046/bss_288/ri_044/es_503/504.
- **rg_002 ≡ rg_262 ≡ rg_263** (yoy × small/micro_cap_flag): synth `mcap ≈ 5000` < 2B/300M always. LS distress-flag precedent.
- **rg_222 ≡ rg_223** (above_50pct vs triple_accel): different formulas, both ≈ 0 on smooth synth.

### Lessons worth carrying

1. **Multiplicative-from-revenue scaling is a Path B trap for revenue-growth-vs-X-growth families.** Always use independent random walks per col. v1 → v2 went from 26 false-positive constants to 1.
2. **The "yoy = ndr − 1" algebraic identity is a recurrent pattern.** When `f(x) = x/x.shift(n)` and `g(x) = (x − x.shift(n))/x.shift(n).abs()`, then `f.diff(m) ≡ g.diff(m)` for any m. Same template as RI ri_2d_031, RL rl_080-082, ve's 17 clusters.
3. **`_safe_div(.., .abs()).fillna(0.0)` creates clip-differentiated edge cases.** Diverges from raw boolean only when denominator is 0; Sharadar represents pre-IPO/missing as NaN, so divergence never triggers in practice. Same as RI ri_003/090, LS ls_022/296.
4. **Harness fingerprint bug to fix next session.** `fingerprint_func` skips body lines after a multiline docstring whose closing `"""` is mid-line. Detect closing `"""` anywhere in the line, not just `startswith`. Value-hash check still works.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_revenue_growth_pathb_harness.py`
- `temp_revenue_growth_audit_results.json`

---

## Family writeups migrated from CLAUDE.md table

Sections below were originally inlined as CLAUDE.md "Findings so far" table Notes-column paragraphs and migrated here verbatim (with light formatting only — no content edits) to slim the auto-loaded CLAUDE.md back to a precedent index + status summary. Each section below is the full audit detail for that family.

### `moving_average_dynamics_2nd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 49/49. **Removed:** 1 scalar-mult dup.

Pure-price (close/volume only). `mad_e2d_015_price_osc_50_200_roc_10d` = `mad_2d_009 × 100` (same osc-vs-spread pattern as base). Auto-applied per established precedent.

### `moving_average_dynamics_3rd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 49/49. **Removed:** 1 scalar-mult dup.

Pure-price. `mad_e3d_015_price_osc_50_200_jerk_10d` = `mad_3d_009 × 100`. Removed orphan helper `_e2d_price_osc_50_200_roc`.

### `volatility_regime_2nd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50. **Removed:** 0 (helper fixes only).

Pure-OHLC; 1 perf vec (`_vol_autocorr` helper, ~130x); 1 lookback fix (`_leverage_effect` helper, same `.shift(-5)` pattern as VR base, applied per precedent).

### `volatility_regime_3rd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50. **Removed:** 0 (helper fixes only).

Pure-OHLC; 1 perf vec (`_vol_autocorr` helper); 1 lookback fix (`_leverage_effect` helper). Same fixes as VR 2nd; helpers are duplicated per file by design.

### `price_moving_averages_2nd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50.

Pure-close; no slow functions; no dups. Fully clean as audited.

### `price_moving_averages_3rd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50.

Pure-close; fully clean.

### `peak_and_crash_2nd_derivatives` (2026-05-09)

**Files:** 1. **Bindable:** 47/47. **Removed:** 3 mathematical-identity dups.

Pure-OHLC. 3 ROC dups removed: `pc_317`/`pc_318` (close/ATH ratio == `dd_ath` up to constant +1, cancels in `.diff()`) and `pc_344` (Fibonacci 0.618 prox == position-in-range up to constant -0.382, cancels in `.diff()`). Identities verified at max\|a−b\|=1e-15. Same harness-missed pattern as VR `vr_262`.

### `peak_and_crash_3rd_derivatives` (2026-05-09)

**Files:** 1. **Bindable:** 49/49. **Removed:** 1 mathematical-identity dup + 1 helper.

Pure-OHLC. `pc_364_jerk_ath_ratio_21d` == `pc_352_jerk_dd_ath_21d` via the same `(close/ATH).diff().diff() == dd_ath.diff().diff()` identity. Removed orphan helper `_d2_ath_ratio_21d`.

### `price_momentum_2nd_derivatives` (2026-05-09)

**Files:** 1. **Bindable:** 49/49. **Removed:** 1 scalar-mult dup.

Pure-OHLC. `pm_2d_042_roc_cmo_21_over_21d` = `pm_2d_015_roc_trend_intensity_21d × 100` (algebraic identity: CMO formula `(sum_up − sum_down)/(sum_up + sum_down) * 100` reduces to `(close − close.shift(W)) / sum(|diff|) * 100` = `trend_intensity * 100` via telescoping diff sum).

### `price_momentum_3rd_derivatives` (2026-05-09)

**Files:** 1. **Bindable:** 49/49. **Removed:** 1 scalar-mult dup.

Pure-OHLC; same CMO/trend_intensity identity at jerk level. `pm_3d_042` = `pm_3d_015 × 100`.

### `basing_pattern_2nd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50. **Removed:** 0 (helper perf only).

Pure-OHLCV; 1 helper perf vec (`_base_autocorr_21d`, ~120x). 0 dups, 0 AUC ties.

### `basing_pattern_3rd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50. **Removed:** 0 (helper perf only).

Pure-OHLCV; 1 helper perf vec (`_2d_autocorr_roc10`, ~120x). 0 dups, 0 AUC ties.

### `crash_speed_2nd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50.

Pure-OHLC; clean. **70 min runtime** dominated by `cs_2d_033_hurst_63d_roc` + `cs_2d_036_cornish_fisher_var_63d_roc` (non-standard `rolling.apply` patterns; vec would need ASK FIRST per HANDOFF). 0 dups, 0 AUC ties.

### `crash_speed_3rd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50.

Pure-OHLC; clean. Same 70 min runtime caveat as 2nd-deriv (`cs_3d_033`/`036` same Hurst/Cornish-Fisher pattern at jerk level). 0 dups, 0 AUC ties.

### `volume_at_capitulation_2nd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50.

Pure-OHLCV (drops base hybrid fundamentals branches). Clean. 1 slow autocorr (`vac_2d_041`) escalated NOT vectorized — `_roc(autocorr,5)` divides by `autocorr.shift(5).abs()` which goes near zero on sign-crossings, propagating <1e-11 input diffs to ~1e-6. Same FP-amp class as base `vac_222` but worse (denominator can hit zero, not bounded by clip). Runtime 2.1 min.

### `volume_at_capitulation_3rd_derivatives` (2026-05-09)

**Files:** 2. **Bindable:** 50/50.

Pure-OHLCV. Clean. 1 slow autocorr (`vac_3d_041`) same FP-amp escalation as 2nd-deriv but compounded through `_roc_of_roc` — diffs reach ~1e+12 on sinusoid. Runtime 2.2 min.

### `volume_accumulation_2nd_derivatives` (+ `_v2`) (2026-05-09)

**Files:** 2. **Bindable:** 49/50. **Removed:** 4 surgical edits across two passes (zero deletes).

Hybrid (1 fn `va_2d_039_turnover_roc_21` needs `sharesbas`).

**Pass 1** (commits `01e4616`, `a58f885`): `va_2d_021` (Bostian II% to break dup of `va_2d_014` raw $-vol II).

**Pass 2** (commits `a5e51ea`, `56ca09e`): AUC+Spearman tie scan caught 2 more rank-equiv dups missed by value_hash. `va_2d_034` (DI = (CMF+1)/2, scalar×2): switched to canonical Williams bp/sp ratio per VA-base `va_202`/`va_203` precedent. `va_2d_021` (pass-1 Bostian II% turned out to equal CMF at any matching SMA window): revised to PVI-style II% (`vol > vol.shift(1)` mask on numerator AND denominator — breaks the algebra at any window).

Final: 0 echoes / 0 constants / 0 dup groups / 0 AUC ties.

### `volume_accumulation_3rd_derivatives` (+ `_v2`) (2026-05-09)

**Files:** 2. **Bindable:** 50/50. **Removed:** 4 surgical edits across two passes (zero deletes).

Pure-OHLCV (`_v2` extends index range 026-050). Same multi-pass story as 2nd-deriv.

**Pass 1** (commit `a58f885`): `va_3d_002`/`va_3d_005` (3-nested `.diff(21)` collapses to identity → short-stride 5d-twice acceleration on 21d ROC, distinct operator from `jerk_21`); `va_3d_018` (Bostian II% jerk to break dup of `va_3d_023`).

**Pass 2** (commits `7ea5532`, `7bf90b4`): `va_3d_034` (canonical Williams bp/sp DI per pass-1 sibling); `va_3d_018` revised to PVI-style II% jerk for the same algebraic reason as `va_2d_021`.

Final: 0 dups, 0 AUC ties.

### `balance_sheet_snapshot` (all tiers) (2026-05-09)

**Files:** 4. **Bindable:** 386/400. **Removed:** 14 dups + 1 bug fix. **KEEP-by-design:** 9 sample-bias constants.

Path B mini-harness (38 input cols, 1500 days, 3-regime quarterly drift to break monotonicity). Tab 12.

**Bug fix:** `bss_055` inner `_safe_div(revenue, 4)` errored on int-as-denom on every call (`(4).replace(...)`); replaced with `revenue / 4` (math identity preserved).

**13 formula-exact dup deletes** (auto-apply, lower-numbered wins):
- `bss_017` = `bss_013` (cash_to_current_liab = cash_ratio)
- `bss_089` = `bss_044` (operating_liabilities = non_debt_liabilities)
- `bss_119`/`bss_120` = `bss_004`/`bss_015` (Ohlson tlta/wcta = tlta/wcta — composite `bss_125` inlines anyway)
- `bss_139` = `bss_062` (dilution_adjusted_equity = equity_per_share)
- `bss_216`/`bss_217`/`bss_220` = `bss_015`/`bss_060`/`bss_191` (Altman x1/x2/x5 = wc_ratio/retearn_ratio/asset_turnover — composite `bss_221` inlines)
- `bss_230` = `bss_187` (equity_erosion_rate = equity_yoy_chg)
- `bss_268` = `bss_118` (log_assets = ohlson_size)
- `bss_274` = `bss_006` (equity_multiplier = financial_leverage)
- `bss_275` = `bss_005` (financial_risk_ratio = liabilities_to_equity)
- `bss_285` = `bss_214` (fcf_yield_on_invested_capital = fcf_to_invested_capital)

**1 user-approved value-exact-via-domain-identity delete:** `bss_266` = `bss_131` (`goodwill/equity` = `goodwill/min(assets, equity)` because liabilities ≥ 0 → equity ≤ assets always; `min(assets,equity)` collapses to `equity` in any valid Sharadar SF1 row).

**Kept by design:** 9 sample-bias-constants — Piotroski (`bss_114`/`bss_115`), Ohlson (`bss_122`), distress flags (`bss_223`/`224`/`225`/`226`/`227`/`228`) — different conditions on different cols, all evaluate to 0 (or 1 for `cfo_gt_ni`) on healthy synthetic. The 8-member zero-clique value-exact group is a synth-bias artifact, not real dups (math is genuinely distinct).

1 sample-bias all-NaN: `bss_288_cash_runway_quarters` needs sustained negative `ncfo` to compute. Same disposition as PC's 9 always-zeros and CFS's `cfs_d3_046`.

### `rd_and_intangibles` (all tiers) (2026-05-09)

**Files:** 7. **Bindable:** 271/275. **Removed:** 4 deletes. **KEEP-by-design:** 1 sample-bias constant + 2 value-exact pairs.

Path B mini-harness (5 independent fundamental profiles × 60 quarterly observations, 19 input cols incl. PIM-stock seeds for Hall-Jaffe-Trachtenberg knowledge capital + Eisfeldt-Papanikolaou organizational capital). Tab 16.

**4 dup deletes** (3 commits): 2 formula-exact auto-applied (`ri_161` == `ri_025` fcf/rnd, `ri_162` == `ri_023` opinc/rnd; commit `5e62896`), 1 base-vs-derivative pollution deleted-from-base per CFS/RL precedent (`ri_036` == `ri_2d_016` YoY R&D acceleration; differ in `fillna` NaN handling rows 4-7 only; commit `9845a0f`), 1 algebraic-identity scalar-mult (`ri_2d_031` == `ri_2d_002`/4 via `_diff(MA_W(s),1) = _diff(s,W)/W` telescoping; `_roc_1q` name was misleading — operator is really 4q-strided; commit `c525cab`).

**2 KEEP-BY-DESIGN value-exact pairs:** `ri_003`/`ri_090` (rnd/equity vs rnd/equity.abs()) and `ri_107`/`ri_115` (gw/equity vs gw/equity.abs()) — clip-differentiated, diverge on negative-equity firms (LS `ls_022`/`ls_296` precedent).

**1 KEEP-BY-DESIGN constant:** `ri_044_rnd_positive_streak` (capped at 20 on always-positive synth R&D — sample-bias, real signal on firms with R&D pauses; `ps_270`/`cfs_d3_046`/`bss_288` precedent).

0 errors / 0 all-NaN / 0 formula-exact dups post-fix.

### `leverage_and_solvency` (all tiers) (2026-05-09)

**Files:** 8. **Bindable:** 400/400. **Removed:** 0 deletes (surgical edits only). **KEEP-by-design:** 9 dup groups, 20 sample-bias constants.

Surgical-edits-only audit per user direction. Tab 14. Path B mini-harness (25 cols incl. non-Sharadar `cashnequiv`/`retainedearnings`/`ltdebt`/`ebt`).

**7 surgical rebodies preserve intent for naming-collision dups** (commits `377c6ab`, `1188999`, `2b7da4d`, `592d891`):
- `ls_084` (DuPont period-avg vs `ls_005` point-in-time)
- `ls_121` (FCF on 252d-avg debt, banker's convention vs `ls_019`)
- `ls_130` (symmetric bounded cushion (NCFO−CL)/(NCFO+CL) vs `ls_108` raw ratio)
- `ls_148` (binary regime flag vs `ls_035` continuous z-score, fulfills "flag" name)
- `ls_187` (net-D/net-E with cash netted both sides vs `ls_010` and `ls_085`)
- `ls_212` (after-tax interest coverage vs `ls_127` — scalar mult by 0.79, kept by NOPAT precedent)
- `ls_291` (5/95 NCFO−CapEx blend vs literal FCF/debt)

**9 value-exact dup groups KEEP BY DESIGN:** 4 academic-distress-model (Zmijewski X1/X2 = Ohlson NITA/TLTA; Beaver = Ohlson CFOTL = direct ncfo/liab; Altman X1 = Springate A = Ohlson WCTA = generic NWC/Assets — each model variable individually addressable for explainability); 3 clip-differentiated (`ls_073`/`ls_111`, `ls_112`/`ls_115`, `ls_022`/`ls_296` — diverge on real data when ncfo<0 or inventory<0); 2 deriv academic-trace (Beaver-ROC, Beaver-jerk).

**20 sample-bias constants kept** (distress flags / Z-thresholds — synthetic is healthy company, all real-data variants).

1 formula-exact pair (`ls_061`/`ls_188` WC/A) is academic-trace too. 5 scalar-mult pairs kept: `ls_002`/`ls_083` (60% capacity), `ls_023`/`ls_297` (1/252 days unit), `ls_127`/`ls_212` (NOPAT-precedent after-tax), `ls_161`/`ls_162` + `ls_196`/`ls_197` (synth-collapse mktcap≫debt).

### `valuation_at_entry` (all tiers) (2026-05-09)

**Files:** 8. **Bindable:** 379/400. **Removed:** 20 dups + 6 bug fixes + 1 surgical edit. **KEEP-by-design:** 5 always-positive flags.

Path B mini-harness (35 cols + `close` + `shareswa`; `ncfo` new for surgical edit). Tab 13. Commits `abe9e9a`, `48dc778`, `e27ef3e`, `15b3d34`, `eb6c346`, `f837537`, `2fa5c09`, `1e5cd37`.

**20 algebraic-identity dup deletes** (17 clusters): PE family {`ve_001`, `ve_083`×100, `ve_094`}, PS {`ve_003`, `ve_019`}, PB {`ve_005`, `ve_022`, `ve_419`}, book/market {`ve_006`, `ve_434`}, P/FCF {`ve_007`, `ve_056`}, EV/GP {`ve_012`, `ve_080`}, EV/opinc 4-way {`ve_013`, `ve_059`, `ve_081`, `ve_084`×100}, P/GP {`ve_014`, `ve_058`}, P/opinc {`ve_015`, `ve_057`}, mcap/tangibles {`ve_016`, `ve_132`}, P/EBITDA {`ve_020`, `ve_125`}, log_ps {`ve_040`, `ve_368`}, Shiller_PE {`ve_068`, `ve_112`}, EV/(EBITDA−capex) {`ve_124`, `ve_398`}, lev_adj {`ve_346`, `ve_423`}, book_yield_roc {`ve_2d_023`, `ve_2d_075`}, book_yield_jerk {`ve_3d_020`, `ve_3d_068`}.

Cluster expansions `ve_083`, `ve_419`, `ve_084` caught by post-warmup cosine-similarity scan at sim=1.0 ratio_std<1e-12 (FP-noise scalar multiples invisible to value-hash because of ×100 scale factor).

**6 bug fixes**: `_slope` helper shape mismatch (`x_demean=arange(window)` mismatched warmup-edge variable-length arrays under `min_periods<window`) repaired in 4 copies, restoring 10 broken `*_slope_*` derivative functions; `_safe_div(scalar_int, 12)` int-as-denom in `ve_385`/`ve_387` cash_burn → direct `/12`.

**1 surgical edit** `ve_424`/`ve_425` ev_to_ocf input ncf→ncfo to match name promise (`vac_118` precedent); `ve_398` inlined into `ve_399` before delete.

**Kept by design**: 5 always-positive flags (`ve_060`/`061`/`062`/`312`/`448` — real on live data); 2 cash-burn-NaN-on-healthy-synth (`ve_385`/`386` — by design only fires under negative ncf, same disposition as PC always-zeros and CFS `cfs_d3_046`).

**Next-session TODO**: `ve_426_log_ev_to_ocf` + 5 deriv-tier functions (`ve_2d_062`/`063`, `ve_3d_060`/`061`/`072`) have same `ncf→ncfo` naming bug as `ve_424`; flagged but not fixed to keep ASK-FIRST scope tight.

### `efficiency_snapshot` (all tiers) (2026-05-09)

**Files:** 15. **Bindable:** 775/775. **Removed:** 0 deletes / 24 surgical rebodies + 2 bug fixes. **KEEP-by-design:** 4 sample-bias constants, 3 value-hash dup groups.

Surgical-edits-only Path B audit per user direction. Tab 15. Path B mini-harness (67 cols, 5 profiles × 1500 days, daily-fwd-fill from quarterly anchors). Commits `d94a44b`, `6308e78`, `e964875`, `297d4f3` + 5 reverts of concurrent-tab auto-deletes (`aca99c9`/`620e7f0`/`e03ce7d`/`84b1fce`/`faf5dc0`).

**24 surgical rebodies preserve naming intent**: 4 DuPont decomp slots use TTM-avg or EMA inputs (`es_047`/`048`/`050` + `es_064` opex/gp + `es_222`/`223` + `es_2d_018` + `es_3d_018`), 5 within-base yoy clusters differentiated via TTM-smoothed YoY (`es_279`/`280`) or trailing-1y mean baseline (`es_475`/`477`/`480`), 5 deriv-side `_roc` slots switched `_diff` → `_pct_change` to match name promise (`es_2d_008`/`009`/`010`/`011`/`085`), 5 scalar-mult slots (`es_468`/`469`/`470` → range-based bband; `es_471`/`473` → Williams %D), 2 sign-flip slots → ratio form (`es_413`/`547`), 1 streak rebody (`es_395` above-median), 2 per-share-lens slots use TTM-avg inputs (`es_324`/`331`).

**Bug fixes**: `es_503`/`504` `_log_safe(scalar)` → `np.log1p` (Series-helper-on-scalar bug, same class as `bss_055` / `ve_385`/`387` from prior Path B audits).

**Kept by design**: 4 sample-bias constants (`es_503`/`504`/`2d_098`/`3d_070` — Petrosian fractal sign-change proxies need real daily variation, sample-bias on smooth fwd-fill synthetic; same disposition as `ps_270`/`cfs_d3_046`/`bss_288`); 3 value-hash dup groups (`es_182`/`339` = clip-vs-abs-clip on equity, distress-divergent; `es_503`/`504` same fractal on different ratios; `es_2d_098`/`3d_070` same fractal at deriv level).

**Concurrent-tab conflict**: another tab auto-deleted 13 dup slots while harness was being built; reverted per user "surgically edit to keep as features" direction.

### `share_and_dilution_snapshot` (all tiers) (2026-05-09)

**Files:** 8. **Bindable:** 376/400. **Removed:** 24 dups. **KEEP-by-design:** 2 sample-bias constants + 1 algebraic-coincidence pair.

Path B mini-harness (37 cols incl. new `sharesbas`/`shareswadil`/`sharefactor`/`dps` + `ncf*` family; 1500 days; warmup=800 to clear 504d shifts). Tab 17. Commits `d5f21c4`, `8092874`, `0ba2042`, `5fb2597`, `88a21d0`, `2445b86`, `adef6b3`, `68104fc`, `f3791cd`.

**24 dup deletes auto-applied** per user direction (mirrors valuation_at_entry tab 13 algebraic-identity precedent):
- **2 formula-exact** (`sd_049`==`sd_009` pct_chg_504d, `sd_248`==`sd_183` ncfcommon/capex)
- **13 body-identical-mod-docstring/var-rename** (`sd_124`, `sd_125`, `sd_139`, `sd_140`, `sd_266`, `sd_273`, `sd_2d_001`, `sd_2d_005`, `sd_2d_009`, `sd_2d_024`, `sd_3d_016` + 2 registry-only collapses)
- **11 algebraic-identity** in 3 classes:
  (a) `s/b` vs `(s−b)/b` collapses under `.diff()`/`_compute_3d` because constant −1 cancels (`sd_120`, `sd_121`, `sd_2d_020`, `sd_3d_020`);
  (b) `close` factor cancels in mktcap normalization `((s−b)*c)/(c*b) = (s−b)/b` (`sd_219`, `sd_220`, `sd_2d_v2_012`, `sd_3d_v2_012`);
  (c) cross-tier `pct_change + 2 deltas` reduces uniformly via `_compute_3d` semantics (`sd_3d_001`, `sd_3d_005`, `sd_3d_024`).

**Kept by design (2+1)**: `sd_083_ncfcommon_positive_ratio_504d` + `sd_188_issuance_cash_to_debt` — both `clip(>0)`/`clip(>=0)` sample-bias constants on synth with mostly-negative `ncfcommon` (real issuance regimes fire); `sd_131` simple-return rank ≡ `sd_156` log-return rank by small-x algebraic coincidence on synth dilution ≤5%/yr (diverge meaningfully on growth firms with 10%+/yr dilution — `log(1+x) ≠ x` at higher x).

0 errors / 0 all-NaN / 0 formula-exact dups post-fix.

### `margin_trajectory` (all tiers) (2026-05-09)

**Files:** 8. **Bindable:** 385/400. **Removed:** 15 algebraic-identity dups.

Path B mini-harness (14 cols only, 5 profiles × 80 quarterly rows; **quarterly cadence** per CLAUDE.md note). Tab 20. Commits `7caaf78`, `286cf3d`, `17124bf`.

**15 algebraic-identity dup deletes** in 2 clusters:
1. `mt_151..155` == `mt_021..025 / 4` via telescoping identity `_diff(rolling_mean(s,4),1) = _diff(s,4)/4` — auto-applied per RI `ri_2d_031` precedent (commit `7caaf78`).
2. `mt_371..375` == `mt_161..165 / 4` and `mt_396..400` == `mt_186..190 / 4` via `_bollinger_pctb(s,w) = z(s)/4 + 0.5` and linearity of `_d`/`_dd` (offset cancels) (commits `286cf3d`, `17124bf`).

All caught by post-warmup z-cosine scan at sim=1.0, `ratio_std_rel<1e-13`.

**Unusual naming**: derivative tiers reuse the integrated `mt_NNN` namespace via `_d_`/`_dd_` infixes rather than `_2d_`/`_3d_` prefixes used elsewhere (`mt_151-175` + `351-375` are first-deriv; `mt_176-200` + `376-400` are second-deriv).

0 errors / 0 all-NaN / 0 constants / 0 dup groups post-fix.

**Cadence lesson confirmed**: first harness run on daily-forward-fill produced 35 false-positive constants + 5 false-positive all-NaN, all eliminated by switching to 80-row quarterly synthetic. Same disposition as CAS — always check `.shift(N)` semantics (days vs quarters) before building harness.

### `cash_flow_trajectory` (all tiers) (2026-05-09)

**Files:** 8. **Bindable:** 393/400. **Removed:** 7 dups. **KEEP-by-design:** 12 sample-bias constants + 3 value-exact pairs + 9 scalar-mult pairs.

Path B mini-harness (5 profiles × 80 quarterly rows; **quarterly cadence** per `mt` precedent — 43× `shift(4)`/rolling 4/8/12/20q). Commits `42bf7d3`, `c281a8f`, `2aeb4d1`, `c9732d2`, `5b1804d`. 33 input cols incl. non-Sharadar `cur_liab` and synthetic alias `depamor_prev_proxy` (used only by `cft_204`; pass `depamor`).

**7 dup deletes** all auto-applied per established precedent: 4 base-vs-deriv-pollution where `_delta(level, n) = level − level.shift(n)` aliasing matches base "trend"/"expansion"/"change" features (`cft_2d_002`==`cft_005`, `cft_2d_010`==`cft_029`, `cft_2d_028`==`cft_158`, `cft_2d_039`==`cft_246`; CFS `cfs_d2_002` precedent); 2 cross-tier "acceleration → deriv" deletes (`cft_012`==`cft_2d_004`, `cft_284`==`cft_3d_001`; RI `ri_036` precedent); 1 algebraic-identity scalar-mult `cft_3d_002`==`cft_218`×4 via `mean(d²,4) = jerk_yoy/4` telescoping (`mt_151..155` / `ri_2d_031` precedent). Removed orphan helper `_fcf_margin_roc_yoy`.

**Kept by design**: 12 sample-bias constants on healthy-firm synthetic (7-fn cash-burn family — `clip(upper=0)` zeroes positive `ncfo`; sign-transition flags `cft_108`/`229`; positive-mean durability `cft_117`; mixed-cadence `cft_206`/`207` where `_x_price_momentum_252/126` `.shift(252)` exceeds 80-row quarterly window → `_safe_div(NaN,NaN)=0` via `fillna(0.0)`); 3 winsorized/synth-coincidence value-exact pairs (`cft_008`↔`cft_051` fcf=ncfo−|capex| coincidence, `cft_049`↔`cft_288` + `cft_072`↔`cft_289` `clip(±3)` doesn't fire on synthetic — `ps_006`/`312` / LS clip-differentiated precedent); 9 NOPAT/days-conversion scalar-mult pairs (CCC vs wc/rev ratio=90, yield_3y vs cumulative ratio=3, `cft_021`~`cft_105` telescoping product; `cas_025`/`136` + `ls_023`/`297` precedent).

**`_safe_div` quirk** unique to this family: `_safe_div(num, den, fill=0.0)` — fills NaN with 0 (other audited families return NaN); relevant when this family's output drives `*_x_*` interaction features.

### `valuation_trajectory` (all tiers) (2026-05-09)

**Files:** 14. **Bindable:** 726/750. **Removed:** 24 dups + 2 surgical edits + 1 bug fix. **KEEP-by-design:** 1 value-dup pair.

Path B mini-harness (47 input cols, 5 profiles × 2000 days, daily forward-fill from quarterly anchors; max window `TD_Y*5=1260d` so 2000-day synth needed). Tab 28. Commits `0f154d6`, `246d8a3`, `1a63b32`, `0816109`, `f1d13a2`, `093981c`, `521f953`, `e426bf6`.

**24 dup deletes**:
- 8 mcap-X aliases (`vt_103`/`104`/`105`/`107`/`108`/`109`/`110`/`111` == `vt_001`/`002`/`003`/`004`/`015`/`019`/`032`/`033` since `marketcap=close*sharesbas` makes `mcap/X == close/(X/sharesbas)`)
- 9 within-base body-identical-mod-rename / mathematical-identity (`vt_306`==`vt_305` E/P*100; `vt_319`/`320`==`vt_153`/`154` mcap_ncfo aliases; `vt_433`==`vt_122` via `_pc(_rstd(W),W)=_sd(v1−v2,v2)`; `vt_440`==`vt_093` IQR alias; `vt_483`==`vt_340` PE_vol_1q==PE_vol_63 alias; `vt_489`/`490`==`vt_279`/`280` z-spread aliases; `vt_524`==`vt_116` via mult-commutative; `vt_552`==`vt_418` via `f−2*f(t−21)+f(t−42)=f.diff(21).diff(21)`; `vt_583`/`584`==`vt_062`/`063` mean_reversion-vs-sma_distance same body)
- 5 cross-tier base→deriv (`vt_114`→`vt_601_d2`, `vt_418`→`vt_687_d3`, `vt_575`→`vt_612_d2`, `vt_576`→`vt_615_d2`, plus `vt_552` chained via `vt_418` — delete-from-base per CFS/RL/RI precedent; acceleration belongs in derivative tier)

**1 bug fix**: `vt_400_pe_entropy_63` had `pe.diff().dropna()` violating CLAUDE.md "Functions return Series aligned to the input index" contract (output 1 row short, corrupting downstream alignment); removed `.dropna()`.

**2 surgical-edit rebodies** (user-approved per `ls_148`/`vac_118`/`cas_141`/`ve_424` naming-bug precedent): `vt_296_pe_mass_index` window=1 made `_rmax(pe,1)−_rmin(pe,1)` identically zero (function was always NaN) — rebodied to canonical Dorsey Mass Index `EMA(pe.diff().abs(),9)/EMA(EMA(...),9)` summed over 25 periods; `vt_511_graham_number_ratio` had `_sd(pe*pb,gn**2)*100` which trivially reduces to `100/22.5 = 4.444` by algebra — rebodied to canonical `close/sqrt(22.5*EPS*BVPS)` Graham fair-value ratio.

**1 KEEP-BY-DESIGN value-dup pair**: `vt_031_pe_chg_1y` vs `vt_064_pe_expansion_rate_1y` (`_pc(pe,TD_Y)` vs `_sd(pe−pe.shift(TD_Y), pe.shift(TD_Y).abs())`) — clip-differentiated, diverge on negative-PE rows (unprofitable firms); RI `ri_003`/`090` + LS `ls_022`/`296` precedent.

**Tier numbering**: deriv files use `vt_601..vt_675` (d2 = `base.diff(TD_M)`) and `vt_676..vt_750` (d3 = `base.diff(TD_M).diff(TD_M)`); each deriv file inlines copies of the base function it wraps.

### `revenue_acceleration` (all tiers) (2026-05-09)

**Files:** 14. **Bindable:** 708/750. **Removed:** 42 dups + 6 bug fixes. **KEEP-by-design:** 5 sample-bias constants + 2 dup groups.

Path B mini-harness (5 profiles × 3500 days × 26 input cols, daily-cadence; warmup=2600 to clear max 10y CAGR shift = 2520 days). Tab 29. 14 commits across 9 affected files (`294034d`, `3c83871`, `2a93a1c`, `be2fd24`, `c78a350`, `f355d20`, `60b70da`, `0eaa0c2`, `5760564`, `8c9214f`, `1120a91`, `5c3eaba`, `f37d5a9`, `1573210`).

**6 bug fixes**: `ra_2d_025`/`ra_3d_025` missing `return` + undefined `d2` (3yr_cagr family bare-statement bug, same class as `bss_055`/`ve_385`/`es_503`/`ve_424`); `ra_139`/`140`/`571`/`572`/`573` `~bool_series.shift(WK)` TypeError (pandas converts shifted bool → object/float, fixed via explicit `.fillna(False).astype(bool)`).

**42 dup deletes auto-applied** per established precedent:
- **12 cross-tier base→deriv pollution** (`ra_011`/`013`/`033`/`035`/`042`/`066`/`154`/`253`/`286`/`287`/`488`/`570` — base "_qoq/_accel/_jerk/_change" features value-exact equal to canonical deriv-tier `_roc_*`/`_roc2_*` operators; CFS `cfs_d2_002` / RI `ri_036` / RL `rl_227-231` / `cft_012`==`cft_2d_004` precedent)
- **1 cross-tier deriv mis-tier** (`ra_2d_003` was 3-diff jerk operator placed in 2d file = body-identical to `ra_3d_002` in correct 3d tier)
- **29 within-base formula-exact + cancellation-equivalent + algebraic-identity** (`ra_116`/`129`/`189`/`190`/`237`/`244`/`262`/`291`/`292`/`341`/`381`/`382`/`413`/`416`/`422`/`424`/`451`/`461`/`470`/`471`/`490`/`492`/`506`/`515`/`517`/`534`/`548`/`555` — incl. RL `rl_080`/`081`/`082` share-cancellation for `{ra_022,ra_517}`/`{ra_041,ra_381}`/`{ra_088,ra_341}`; algebraic-identity for `{ra_072,ra_237}` since YR/QTR=4 exactly, `{ra_336,ra_420}` since same-window mean/sum cancels in division, `{ra_299,ra_422}` since `1+pct_change=rev/rev.shift(YR)` on positive rev)

**2 KEEP-BY-DESIGN dup groups**: `{ra_002,ra_325}` winsorized synth-coincidence (`clip(p01,p99)` doesn't fire on bounded synth growth — `ps_006`/`312` precedent); `{ra_365,ra_366,ra_367,ra_369}` 4-way always-zero binary growth-threshold indicators (25%/50%/100%/deeply-neg, all zero on healthy 5%/yr synth — `ps_270`/`cfs_d3_046`/`bss_288`/`ri_044` precedent).

**5 KEEP-BY-DESIGN constants**: same 4-way set + `ra_587_rev_growth_cummin` (expanding YoY-growth min stair-steps to floor on healthy synth, signals on volatile firms).

**Forward-fix note**: `c78a350` used a buggy DOTALL-flag regex (`(?s)`) that mass-deleted `ra_2d_004..ra_2d_025` along with intended `ra_2d_003` target; `f355d20` restored 22 erroneously-deleted defs and re-applied single delete with corrected line-walk algorithm. Net effect: only `ra_2d_003` removed.

Harness post-fix: 0 errors / 0 all-NaN / 5 sample-bias constants kept / 2 dup groups kept / 708 functions registered (= 750 − 42).

### `growth_vs_cost` (all tiers) (2026-05-09)

**Files:** 11. **Bindable:** 562/575. **Removed:** 13 dups + 1 bug fix. **KEEP-by-design:** 2 sample-bias constants + 11 value-exact pairs.

Path B mini-harness (5 profiles × 1500 days × 54 input cols; daily-cadence quarterly-anchor forward-fill — file uses `TRADING_DAYS_QTR=63`/`TRADING_DAYS_YR=252` for shifts/rolling). Tab 25. Commits `5bf9883`, `70bf8be`, `b72acf0`, `538de8e`, `286605c`, `f4baf48`.

**13 dup deletes** auto-applied per HANDOFF formula-exact + algebraic-identity precedent (SD/CAS/MT/RI):
- **9 within-base** (`gc_005`/`431` literal pct_change rev_growth_3y; `gc_017`/`137` algebraic identity `_delta(om,252)/252*252 = *1`; `gc_025`/`304`, `gc_026`/`301`, `gc_027`/`306` DOL/DTL helper-rename `_safe_div`/`_pct_change` ↔ `_sd`/`_pc`; `gc_062`/`389` rev_growth_rank_3y; `gc_140`/`392` cost_ratio_rank_3y; `gc_192`/{`398`,`403`} vol-scaled rev growth — `gc_398` algebraic `rg*(1/vol)=rg/vol`; `gc_216`/`404` risk_adj_margin_expansion)
- **1 cross-tier base-vs-deriv pollution** (`gc_066_margin_expansion_acceleration` body `d1 − om.shift(63).diff(63)` = literal 2nd diff of operating margin = `gc_2d_003` — RI `ri_036` / CFS `cfs_d2` / RL `rl_227-231` precedent: delete from base)
- **3 within-deriv** (`gc_2d_007`/`2d_033` DOL_roc helper-rename; `gc_3d_010`/`3d_069` asset turnover IS revenue/assets — same body via `_d` thrice)

**Bug fix**: `gc_331_rsi_proxy_21d` called `_sd(gain, loss, fill=1.0)` but helper signature is `_sd(n, d, f=0.0)` (kwarg name mismatch — same class as `bss_055`/`ve_385`/`es_503`); switched to positional `_sd(gain, loss, 1.0)`.

**11 KEEP-BY-DESIGN value-exact pairs** (synth-bias only, diverge on real Sharadar): 6 from `opinc==ebit` synth artifact (`gc_015`/`199`, `gc_017`/`200`, `gc_051`/`198`, `gc_052`/`201`, `gc_2d_003`/`2d_043`, `gc_3d_003`/`3d_043` — real EBIT includes non-operating items); 3 from `eps=netinc/100` constant-divisor (`gc_040`/`210`, `gc_053`/`194`, `gc_105`/`196` — real `shareswa` is time-varying); 1 from `shareswa=sharesbas*0.99` constant-scalar (`gc_086`/`285`); 1 from `debtc=debt*0.20`/`debtnc=debt*0.80` constant-proportion (`gc_079`/`280`/`281`).

**2 KEEP-BY-DESIGN sample-bias constants**: `gc_405`/`406` revenue-growth threshold flags (within-profile constant on smooth synth — real cross-section signal; `ps_270`/`cfs_d3_046`/`bss_288` precedent).

**1 scalar near-miss DROP**: `gc_054`/`087` fcf_growth vs fcf_per_share_growth (sim=0.99999 but ratio_std_rel=0.05 = correlation only, not scalar mult).

0 errors / 0 all-NaN / 0 unexplained dups post-fix.

### `dilution_rate` (all tiers) (2026-05-09)

**Files:** 14. **Bindable:** 714/750. **Removed:** 36 deletes + 2 raw=True bug fixes. **KEEP-by-design:** 17 sample-bias-coincidence dup groups + 1 sample-bias all-NaN.

Path B mini-harness (5 profiles × 1500 days × ~52 input cols, daily-cadence with quarterly-anchor fwd-fill, warmup=800 to clear 1260d shifts; mix of issuer/buyback/stable/sbc-heavy/distress profiles to break `ncfcommon`-clip sample-bias). Tab 26. Commits `e939567`, `6143924`, `7ad14fb`, `557d261`, `3120a65`, `99ac9df`, `9881878`, `07f3a94`, `6dbbafe`, `16c5cba`, `483b42c`, `650e228`.

**Bug fixes**: `dr_344`/`dr_345` `lambda x: x.iloc[0]` with `raw=True` → `x[0]` (raw=True passes ndarray, `.iloc` fails — `bss_055`/`ve_385`/`es_503` helper-on-wrong-type precedent).

**36 dup deletes** auto-applied per SD tab 17 precedent:
- **4 formula-exact** (`dr_015`==`dr_003`, `dr_079`==`dr_011`, `dr_145`==`dr_022`, `dr_528`==`dr_343`)
- **10 cross-tier base→deriv** delete-from-base (`dr_017`/`019`/`012`/`077`/`352`/`152`/`319`/`473`/`452`/`511`/`476` == `dr_d2_152`/`155`/`157`/`158`/`177`/`200`/`205`/`206`/`209` — operators belong in deriv tier per CFS/RL/RI precedent)
- **17 within-base body-identical-mod-rename + algebraic-identity** (`dr_330`/`331`/`027`/`028` cumulative-vs-pct_change collapse; `dr_080`/`078`/`075`/`339`/`449`/`546`/`570`/`453`/`576` body-identical mod docstring/var-rename; `dr_014` annualized=raw×4 scalar; `dr_410` streak/4 = regime_duration scalar)
- **4 deriv-side scalar-mult** (`dr_d2_153` = `dr_016`×4 annualization; `dr_d2_158` cross-deriv-tier 3rd-order-in-2nd-tier == `dr_d3_178`; `dr_d2_214`/`dr_d3_239` = bollinger position = z-score/2 — lower-numbered z-score canonical kept per VAL `ve_083` precedent)

**Kept by design**: 17 sample-bias coincidence value-dup groups (clip-collapse on synth tiny per-share/yield denoms; constant-multiple synth balance sheet; sign-mask / profile-sign / clip-differentiated; non-linear under tiny-x; constant-ratio shareswa-vs-shareswadil; clip-vs-no-clip vol; telescoping fwd-fill; median-zero; multi-mech zero-collapse), 3 scalar-mult sample-bias (`dr_160`/`dr_184` sign-vs-mean; `dr_050`/`dr_231` + `dr_245`/`dr_247` clip-collapse on tiny-eps), 1 sample-bias all-NaN `dr_137_dilution_half_life` (needs reverse-split data; `ps_270`/`cfs_d3_046`/`bss_288` precedent).

0 errors / 0 missing inputs / 0 formula-exact dups / 0 unexplained value-exact dups post-fix.

**No new col types vs prior Path B**: eps/fcfps/sps synth as netinc/sharesbas, fcf/sharesbas, revenue/sharesbas.

### `leverage_acceleration` (all tiers) (2026-05-09)

**Files:** 15. **Bindable:** 740/775. **Removed:** 35 dup deletes + 9 surgical Beaver-rebodies + 4 bug fixes. **KEEP-by-design:** 13 dup groups + 1 sample-bias all-NaN + 3 sample-bias constants.

Path B mini-harness (5 profiles × 2000 days × 33 input cols, daily-cadence, warmup=1000 to clear `TRADING_DAYS_YR*3=756d` rolling — non-Sharadar `cashnequsd`/`costrev`/`currentassets`/`currentliabilities`/`dividends` per LS precedent).

15 files: 8 base × 75 (`la_001..600`) + 4 2nd-deriv × 25 (`la_d1_001..100`) + 3 3rd-deriv × 25 (`la_d2_001..075`) = 775 features. Function-prefix tier convention: base = `la_NNN`, 2nd-deriv-file = `la_d1_NNN` (ROC of base), 3rd-deriv-file = `la_d2_NNN` (accel of base).

Commits `ac2cf07`, `8236efa`, `c4d2201`, `4a6996e`, `27c1213`, `5ae1bc0`, `80bbb60`, `dab7ebf`, `ceeb659`, `928b002`, `0fd4814`, `84e6198`, `01f5aa8`, `1199bf2`, `7bdbd49`.

**35 dup deletes**:
- 25 within-base alpha-rename / algebraic-identity / cancellation-equiv (`la_013`, `la_068`, `la_069`, `la_096`, `la_109`, `la_110`, `la_168`, `la_170`, `la_207`, `la_244`, `la_285`, `la_286`, `la_290`, `la_291`, `la_292`, `la_327`, `la_328`, `la_444`, `la_445`, `la_449`, `la_456`, `la_457`, `la_475`, `la_476`, `la_482`, `la_483`, `la_484`, `la_549`, `la_554`) — incl. `la_011`/`285` cancellation-equiv `(netinc/equity)/(netinc/assets) = assets/equity` (RL `rl_080-082` precedent), `la_278`/`549` cancellation `(debt/equity)/(debt/(close*sharesbas)) = mktcap/equity` (CAS `cas_182-183` precedent)
- 6 cross-tier base-vs-d1 ROC pollution (`la_494`/`495`/`496`/`497`/`498`/`499` == `la_d1_001`/`002`/`005`/`006`/`009`/`010` — base names literally `*_pct_change_*`, ROC features belong in deriv tier per RI `ri_036` / CFS / RL precedent)

**9 surgical Beaver-rebodies** (user-approved per HANDOFF "ASK FIRST naming corrections"): `la_199`/`la_200` + `la_d1_065`/`066`/`067`/`068` + `la_d2_049`/`050`/`051` — bodies were `_safe_div(fcf, debt)` (literally identical to `la_078`/`079`, `la_d1_037-040`, `la_d2_028-030`) but names say "beaver_ratio". Beaver (1966) academically = NCFO/total_liabilities. Rebodied with signature/registry-input changes from `(fcf, debt)` to `(ncfo, liabilities)`. Mirrors `ls_148`/`vac_118`/`ve_424`/`cas_141` naming-bug-surgical-edit precedent. Post-rebody, `la_475`/`476` (literal opcf_to_liab) became formula-exact dups of `la_199`/`200` and were auto-deleted.

**4 bug fixes** (`_safe_div(debt, N)` int-as-denom — same class as `bss_055`/`ve_385`/`387`; replaced with direct `debt / N` to preserve algebra): `la_204` `debt/5`, `la_316` `debt/5`, `la_555` + `la_556` `debt/7`.

**13 KEEP-by-design dup groups**:
- 7 clip-differentiated (`la_001`/`547` debt/eq vs eq.clip(1); `la_004`/`126` debt/fcf vs fcf.clip(1); `la_060`/`108` cancellation-clip cashnequsd/debt vs (cashnequsd/cl)/(debt/cl).clip(0.01) — diverge on real low-leverage; `la_076`/`077` cancellation-clip roa/da vs roe/de — diverge on real low-leverage; `la_227`/`492` + `la_228`/`493` tang vs tang.clip(1) — diverge on intangibles+goodwill ≈ assets; `la_400`/`571` + `la_402`/`572` log-de clip 0.001 vs clip 1 — diverge on negative-equity firms)
- 4 academic-distress traces (`la_002`/`196` zmijewski_x2 = debt_to_assets; `la_176`/`190` altman_x1 = springate_a = WC/A; `la_178`/`191` altman_x3 = springate_b = ebitda/A; `la_181`/`193` altman_x5 = springate_d = revenue/A; composites `la_182_altman_zscore_proxy` / `la_194_springate_score_proxy` / `la_198_zmijewski_score_proxy` inline x1-x5 directly per LS `ls_061`/`151`/`170`/`188` precedent)
- 1 sample-bias 3-clique constants (`la_324`/`380`/`385` — ncff_positive/zero_debt/ic_below_1 all 0 on healthy synth; `ps_270`/`cfs_d3_046`/`bss_288` precedent)

**1 KEEP-by-design all-NaN** (`la_530_debt_growth_cvar_5pct` rolling CVaR on debt growth; needs real-data outliers; same disposition as `bss_288` / `cfs_d3_046` / `dr_137`).

0 errors / 13 KEEP dup groups / 1 sample-bias all-NaN / 3 sample-bias constants post-fix.


## `revenue_jerk` (all tiers, tab-rj, Path B)

Commits: `03e5224`, `b701466`, `1c2ff0a`, `8dea87b`, `f36ce61`, `2939f43`, `948766b`.

14 files: 8 base x 75 (chunks 001-600) + 3 2nd-deriv x 25 (idx 001-025/026-050/051-075) + 3 3rd-deriv x 25 = 750 features. Daily-cadence (uses 21d/63d/126d/252d/504d). 100% Path B (every fn takes a fundamental; hybrid only via `close`/`volume`). Function prefix `rj_`.

**Path B mini-harness**: 5 profiles x 2500 daily rows x 28 input cols (assets/capex/cashneq/close/cor/debt/depamor/ebit/ebitda/equity/fcf/gp/intangibles/inventory/liabilities/ncfo/netinc/opex/opinc/payables/ppnenet/receivables/retearn/revenue/rnd/sgna/volume/workingcapital), warmup=1800 to clear 1638d max lookback (deriv `_roc(_jerk(s, 504), 63)` = 5 nested W-shifts).

**Initial harness state**: 0 errors / 0 missing inputs / 0 all-NaN / 0 constants / **21 body-exact dup groups** / **36 value-exact dup groups** / 1 scalar-mult.

**Disposition**: surgical-rebody-everything per user direction (LS tab 14 / debt_trajectory tab 22 / efficiency_snapshot tab 15 precedent). **Zero deletes; ~155 surgical edits across 14 files preserve all 750 slots.**

### Cluster 1: 10 `_1y/_2y` body-exact pairs (commit `03e5224`)
Both halves were literal copy-paste duplicates whose bodies hardcoded the same window even though the names suggested distinct 1y/2y timeframes. Per ls_148/cas_141/ve_424/vt_296 naming-bug surgical-edit precedent.

- `rj_524/525_rev_jerk_(peak|trough)_to_current`: was W=504 (= 2y), now W=252 (= 1y). `rj_534/535` are the canonical `_2y` variants and keep W=504.
- `rj_526/527/528/529` (gp/ebitda/opinc/ncfo)`_jerk_pos_ratio_1y`: was W=252 (literal dup of `rj_516/517/518/519`), now W=126 = SEMI-ANNUAL. Docstring annotates `rj_516..519` as canonical 1y variants.
- `rj_530/531/532` (gp/ebitda/ncfo)`_jerk_asymmetry_1y`: same shift to W=126.
- `rj_533_rev_jerk_abs_log_energy_1y`: same shift to W=126.
- `rj_536_liabilities_jerk_q`: was W=63 (dup of `rj_248`), now W=126.
- `rj_537_liabilities_jerk_annual`: was W=252 (dup of `rj_249`), now W=504.

### Cluster 2: 7 cross-tier mathematical-identity collisions (commit `b701466`)
Each base fn collides with a deriv-tier sibling because `_jerk = _roc(_acceleration)` and `_snap = _roc(_jerk)` by helper definitions:

- `rj_021_revenue_snap_q == rj_2d_001_roc_revenue_jerk_q`
- `rj_151_gp_jerk_q == rj_2d_026_roc_gp_accel_q`
- `rj_232_cashneq_jerk_q == rj_3d_037_roc2_cashneq_velocity_q`
- `rj_236_receivables_jerk_q == rj_2d_039_roc_receivables_accel_q`
- `rj_246_retearn_jerk_q == rj_3d_038_roc2_retearn_velocity_q`
- `rj_264_cashneq_accel_q == rj_2d_037_roc_cashneq_velocity_q`
- `rj_547_gp_snap_q == rj_3d_026_roc2_gp_accel_q`

Each base fn rebodied to add level-relative normalization: `_safe_div(deriv, _roll_mean(input.abs(), 252))`. Result is a unit-free scale-relative magnitude (real signal, jerk normalized to firm scale) and not algebraically equivalent to the deriv tier. Deriv-tier slots unchanged.

### Cluster 3: 11 within-base value-exact pairs (commit `1c2ff0a`)
- `rj_072/rj_132` percentile_1y -> `rj_132` = 2y/504d window
- `rj_070/rj_140` ema_cross_signal -> `rj_140` = (21,126) EMA cross
- `rj_041/rj_142` cumsum/integral_1y -> `rj_142` = energy-weighted 1y integral (`sum |j|*|j|.shift(1)`)
- `rj_113/rj_297` equity_turnover_jerk_q -> `rj_297` = jerk on 1y-trailing-mean equity
- `rj_240/rj_290` + `rj_241/rj_291` wc/cash_conversion_proxy_jerk -> `rj_290/rj_291` = jerk of EMA-smoothed cc
- `rj_107/rj_505` jerk_autocorr_1 / trend_vs_mean_revert -> `rj_505` = lag-21 autocorr
- `rj_468/rj_506` recovery_ratio / breakout_indicator -> `rj_506` = binary 1y-high breakout flag
- `rj_504/rj_507` vol_regime / compression_indicator -> `rj_507` = (21,126) vol ratio
- `rj_121/rj_511` mean_reversion_dist / q1_residual -> `rj_511` = robust IQR-based residual
- `rj_351/rj_599` multi_avg / zscore_multi_timeframe -> `rj_599` = recency-weighted (4:3:2:1) blend

### Cluster 4: 124 mass-bomb placeholder slots (commits `8dea87b`, `f36ce61`, `2939f43`)
Six clusters of identical-name + identical-body + identical-`specifics` slots. No name-encoded intent. Per user surgical-rebody direction, invented distinct signals along window/statistic/transformation axes:

- **`rj_2d_031..033` + `rj_3d_031..033` (6 slots, sgna/rev jerk roc)**: vary outer ROC stride. `_030` keeps canonical 63d; `_031` -> 126d; `_032` -> 252d; `_033` -> 21d.
- **`rj_2d_056..065` + `rj_3d_056..065` (20 slots, ev_jerk_expanding_mean)**: vary expanding statistic on revenue jerk. `_055` keeps canonical expanding-mean; `_056` -> median, `_057` -> std, `_058` -> expanding-q95 (replaced expanding-max which went constant on synth), `_059` -> expanding-q05 (same fix), `_060` -> sum |j|, `_061` -> sum j-squared, `_062` -> fraction positive, `_063` -> skew, `_064` -> kurt, `_065` -> mean of sign(j).
- **`rj_201..rj_225` (24 slots, sgna/rev jerk)**: `rj_201` keeps canonical `_jerk(sgna/rev, 63)`; remaining 24 vary jerk stride (W=126/252/504), 1y rolling stats (mean/std/sum/max/min/median/skew/kurt/zscore/percentile/pos_ratio/abs_mean/energy/sign_mean), EMAs (21d/63d/252d), autocorr (lag-1, lag-21), and cross-window ratios.
- **`rj_374..rj_450` (76 slots, rev_jerk_expanding_mean)**: `rj_374` keeps canonical expanding-mean. `rj_375` -> expanding std. The 75 fns in chunk 376_450 are rewritten as **expanding-window statistics throughout** (no rolling-window stats - those slots are already filled in chunks 001_075/076_150). Seven thematic blocks:
  - A 376-389: expanding sums/means of transformed jerk (|j|, j-squared, sign, log1p, positive-only, negative-only, activity counts)
  - B 390-399: expanding distributional shape (median/quantiles q05/q95/q01/q99/q25/q75/skew/kurt/range)
  - C 400-409: current-vs-expanding-distribution normalized signals (deviation, cumulative z-score, IQR-normalized, magnitude-normalized, deviation sign, binary outlier flags)
  - D 410-419: adaptive-sigma exceedance counts (1/2/3-sigma where sigma is expanding-std), expanding sign-flip counts, asymmetric upside/downside dispersion
  - E 420-429: signal-to-noise / asymmetry ratios (positive share, negative share, signed/abs ratio, Sharpe-like, RMS proxy, signed skew/kurt, average tail magnitude)
  - F 430-444: expanding-vs-rolling cross-window comparisons (expanding mean/std/median minus rolling 21/63/252d, current-vs-cumulative ratios, fraction-above-prior-expanding-mean, fraction monotone-up)
  - G 445-450: ROCs of expanding mean/std at 21/63/252d strides + composite (mean x std)

### Second-pass fixes (commit `948766b`)
After first-pass rebodies, harness re-run surfaced cross-file collisions where my new 376_450 expanding-mean cluster overlapped existing 001_075 rolling-window stats. Plus 2 pre-existing scalar-mult pairs and 2 expanding-max ROC constants on synth.

- 376_450 file completely rewritten from rolling-window to expanding-window-based statistics.
- `rj_142`: 2y plain sum was dup of `rj_042` cumsum_2y -> energy-weighted 1y integral.
- `rj_505`: lag-5 autocorr was dup of `rj_108` -> lag-21 autocorr.
- `rj_511`: 252d z-score was algebraic-identity dup of `rj_033` -> robust IQR-based residual.
- `rj_446/449`: my expanding-mean ROC variants clashed with my deriv-tier rebodies (`rj_2d_055/057`) -> expanding sum log1p / expanding mean |j| respectively.
- `rj_2d_058/3d_058`: ROC of expanding-max -> ROC of expanding-q95.
- `rj_2d_059/3d_059`: ROC of expanding-min -> ROC of expanding-q05.

### Pre-existing scalar-mult pairs surgically rebodied (commit `948766b`)
- `rj_118 vs rj_479`: rj_479 body was `_safe_div(|m|, s) * sign(m) = m/s = rj_118` by algebra. Rebodied `rj_479` to MAD-based trend strength: `(|median|/MAD) * sign(median)` over 1y window.
- `rj_070 vs rj_2d_011`: deriv-tier `rj_2d_011 = _roc(_ema(_accel,63) - _ema(_accel,252), 63)` collapses to `rj_070 = _ema(_jerk,63) - _ema(_jerk,252)` by EMA/diff linearity. Rebodied `rj_2d_011` to use shorter (21,63) EMA pair.

### Function-name typo preserved
124 placeholder slots have function names like `rj_201sgna_to_rev_jerk_q` and `rj_374rev_jerk_expanding_mean` (missing underscore between number and slot). Preserved verbatim for binding-layer backward compatibility - registry keys + Python identifiers untouched, only bodies + docstrings + registry `specifics` text changed.

### Final state
0 errors / 0 missing inputs / 0 all-NaN / 0 constants / 0 body-dup groups / 0 value-dup groups / 0 scalar-mult pairs. 750/750 slots preserved.

### Lessons
1. **Mass-placeholder rebodies need cross-file dup awareness.** First-pass design of 376_450 rebodies as 1y rolling stats collided with 16 existing 001_075/076_150 slots. Always check what statistical patterns are already covered in earlier chunks before designing rebodies for placeholder clusters. For "expanding_mean" placeholder name, expanding-window stats were the natural answer (and don't collide with rolling-window).
2. **Expanding-max/min ROC goes constant on synth.** Monotonic expanding stats only update at boundary-crossing points; ROC is mostly 0. Use expanding-q95/q05 for smoother proxies.
3. **Missing-underscore typos are binding-layer hazards.** The harness binds by registry key so the typos don't break runs, but any external consumer that grep'd for `rj_2[0-2][0-9]_` would silently miss these slots. Preserved per user direction; flagged for future awareness.
4. **EMA/diff linearity creates cross-tier scalar-mult.** `_diff(_ema(s, W1) - _ema(s, W2), N)` approximately equals `_ema(_diff(s, N), W1) - _ema(_diff(s, N), W2)` to FP precision. Cross-tier `_roc` of EMA-cross of `_acceleration` tends to scalar-mult the same EMA-cross of `_jerk`. Use distinct EMA windows when designing deriv-tier features that wrap base EMA-cross signals.

---

## moat_trajectory (all tiers) — tab-mt 2026-05-09

12 files: 6 base x 75 (chunks 001-450) + 3 2nd-deriv x 25 + 3 3rd-deriv x 25 = 600 features. Quarterly-cadence dominant (528 fns) + 72 daily-cadence price-only fns in `moat_trajectory_base_226_300.py` plus mixed-cadence price-vs-fundamental ratios in deriv files. Function prefix `mt_` collides with `margin_trajectory` family at the prefix layer but each file is self-contained at runtime.

### Harness
Path B mini-harness with **dual-cadence synthetic**:
- Quarterly profiles: 5 profiles x 100 quarters x 31 fundamental cols.
- Each quarterly profile also includes a co-sampled OHLCV synthetic (`close`/`high`/`low`/`open`/`volume` generated as quarterly-cadence series at the quarter end so mixed-cadence functions whose registry says quarterly but signature includes price cols can still bind).
- warmup = 20 quarters (clears max 20q lookback in `mt_352_revenue_cagr_20q` + 12q rolling windows).
- post-warmup z-cosine scan + value-hash rounded to 1e-9.

This dual-injection avoids the `KeyError('close')` failures that the first harness pass surfaced for 6 mixed-cadence fns (mt_2d_043, mt_3d_041, mt_348, mt_349, mt_410, mt_411).

### Findings & deletes (33 total)

All deletes auto-applied per HANDOFF AUTO-APPLY classes 1-3. One commit per file affected (12 commits: bf6ba0e, ec30b30, 48adc34, d367739, 3c736e0, 282560f, 91198a3, 60f3d54, 5137733, fffd85c, ee06158, 6f69048).

**8 DuPont decomposition aliases (CAS cas_182/183 cancellation-equivalent precedent):**
- mt_076_dupont_profit_margin == mt_026_net_margin (NI/R)
- mt_077_dupont_asset_turnover == mt_056_asset_turnover (R/A; also academic Altman X5 mt_194 KEEP)
- mt_078_dupont_equity_multiplier == mt_368_assets_to_equity (A/E)
- mt_079_dupont_margin_contribution_slope == mt_028_net_margin_slope_8q
- mt_080_dupont_turnover_contribution_slope == mt_057_asset_turnover_slope_8q
- mt_081_dupont_leverage_contribution_slope == mt_369_assets_to_equity_slope_8q
- mt_2d_015_dupont_margin_accel == mt_2d_003_net_margin_accel
- mt_3d_015_dupont_margin_jerk == mt_3d_003_net_margin_jerk

DuPont 3-factor (NI/R) x (R/A) x (A/E) = NI/E telescopes to ROE; each component is the underlying ratio; composite mt_083_dupont_quality_flag uses INLINE slope clips so deleting the component aliases doesn't break explainability.

**4 SGR=ROE aliases (formula-exact under retention=1):**
- mt_176_sustainable_growth_rate body literally returns ROE (docstring acknowledges "1 - payout assumed 100% retention")
- mt_177_sgr_slope_8q == mt_047_roe_slope_8q
- mt_2d_029_sgr_accel == mt_2d_005_roe_accel
- mt_3d_029_sgr_jerk == mt_3d_005_roe_jerk

Composite mt_178_sgr_vs_actual_growth and mt_179_sgr_vs_actual_slope_8q still inline `_safe_div(netinc,equity) - _pct_change_n(revenue,4)` directly -- KEEP.

**3 EVA-spread aliases (CAS cas_158 algebraic-identity precedent):**
- mt_152_eva_spread_slope_8q == mt_055_roic_proxy_slope_8q since slope(roic - HURDLE) = slope(roic) (HURDLE=0.025 constant).
- mt_2d_026_eva_spread_accel == mt_2d_007_roic_proxy_accel (constant cancels under .diff()).
- mt_3d_026_eva_spread_jerk == mt_3d_007_roic_proxy_jerk (constant cancels under _d3 = slope o slope o diff).

EVA-dollar variants (mt_154/155/156/157/161-165) all inline the (roic-HURDLE)*ic computation, no composite breakage.

**4 Greenblatt EY = ROIC aliases:**
- mt_392_greenblatt_earnings_yield body `_safe_div(opinc, equity+debt)` literally == mt_054_roic_proxy. Greenblatt EY academically uses EBIT/EV (where EV = market_cap + debt - cash) but the body uses BOOK equity + debt = invested capital, collapsing to ROIC.
- mt_393_greenblatt_earnings_yield_slope_8q == mt_055_roic_proxy_slope_8q.
- mt_2d_067_greenblatt_ey_accel == mt_2d_007_roic_proxy_accel.
- mt_3d_066_greenblatt_ey_jerk == mt_3d_007_roic_proxy_jerk.

Composite mt_394_greenblatt_combined_rank_proxy inlines roc + ey directly; still works.

Could be considered a naming-bug surgical-rebody (replace book equity with marketcap to recover true Greenblatt EY) but body-as-written is formula-exact dup so auto-deleted; flagged in journal as a candidate for surgical-rebody if user later prefers true EV-based EY.

**12 pure alpha-rename:**
- mt_075_retained_earnings_proxy_slope == mt_047_roe_slope_8q
- mt_273_price_momentum_252d == mt_236_total_return_252d (both close.pct_change(252))
- mt_293_moat_momentum_quality == mt_238_risk_adjusted_return_252d (both Sharpe ratio)
- mt_402_operating_leverage_degree == mt_065_opex_leverage_ratio (both `_safe_div(_pct_change_n(opinc,4), _pct_change_n(revenue,4))`)
- mt_446_fcf_to_total_debt_plus_equity == mt_092_fcf_yield_on_invested_capital
- mt_447_fcf_yield_total_slope_8q == mt_093_fcf_yield_on_ic_slope_8q
- mt_346_shareholder_yield_proxy == mt_094_retained_fcf_ratio == mt_366_fcf_to_equity (3-clique; lower wins)
- mt_367_fcf_to_equity_slope_8q == mt_347_shareholder_yield_slope_8q
- mt_332_maintenance_capex_proxy == mt_326_da_to_revenue (both `_safe_div(depamor.abs(), revenue)`)
- mt_2d_062_fcf_to_equity_accel == mt_2d_059_shareholder_yield_accel
- mt_3d_061_fcf_to_equity_jerk == mt_3d_059_shareholder_yield_jerk
- mt_3d_074_fcf_total_capital_jerk == mt_3d_018_fcf_yield_on_ic_jerk

**1 algebraic-identity via Sharadar fcf=ncfo+capex (CFA cfa_015/041 precedent):**
- mt_311_ocf_vs_capex_slope_8q == mt_183_self_funding_slope_8q since slope(fcf/|capex|) = slope((ncfo+capex)/|capex|) = slope(ncfo/|capex| + sign(capex)) = slope(ncfo/|capex|) (sign constant cancels under slope; on Sharadar capex < 0 always so sign=-1).

### KEEP-by-design (13 academic-trace dup groups)

Per ls_061/151/170/188 + cas_062/090 + ls_188 Beaver precedent -- academic distress-model components individually addressable for explainability when the composite inlines x1-x5+:

- [mt_002, mt_172] GM YoY change == Piotroski margin change (mt_174 composite inlines gm_chg)
- [mt_051, mt_166, mt_382] ROA == Piotroski ROA == Ohlson NITA (mt_174 + mt_385 composites both inline NI/A)
- [mt_053, mt_168] ROA YoY == Piotroski ROA change
- [mt_064, mt_173] turnover YoY == Piotroski turnover change
- [mt_105, mt_191] opinc/A slope == Altman X3 slope (mt_196 composite inlines x3 slope)
- [mt_141, mt_408] growth_quality_composite == AQR QMJ growth (mt_412 inlines)
- [mt_142, mt_409] slope of above == QMJ growth slope (mt_413 inlines)
- [mt_143, mt_206] Sloan accruals == Beneish TATA (mt_207 inlines tata)
- [mt_186, mt_379] Altman X1 == Ohlson WCTA (different academic models, both KEEP per ls precedent)
- [mt_2d_025, mt_2d_033] Sloan-accrual accel == Beneish TATA accel
- [mt_3d_006, mt_3d_049] ROA jerk == Ohlson NITA jerk (LS ls_3d_032/040 Beaver-jerk precedent)
- [mt_3d_025, mt_3d_033] Sloan jerk == Beneish TATA jerk

### KEEP-by-design (4 sample-bias / synth-symmetry constants)

- mt_287_close_position_in_range: synthetic OHLC scheme high = close*(1+x), low = close*(1-x) makes (close-low)/(high-low) == 0.5 always. Real OHLC is asymmetric so this fires on production data.
- mt_309_ocf_positive_ratio_12q: synthetic ncfo always positive (healthy-firm profile). Same disposition as ps_270/cfs_d3_046/bss_288.
- mt_381_ohlson_oeneg_flag: synthetic assets >> debt always so the distress flag never fires. LS distress-flag precedent.
- mt_420_revenue_entropy_8q: 8q rolling entropy of YoY revenue growth bins values into 5 quintiles; on smooth synthetic the within-window distribution lands in <=2 bins producing constant entropy. Real volatile growth diverges.

### KEEP-by-design (1 harness-limitation all-NaN)

- mt_410_qmj_safety body uses 1/close.pct_change().rolling(252,min_periods=126).std() which needs at least 126 daily observations. Quarterly profile has 100 obs -> all-NaN. In production with daily-cadence close + quarterly fwd-filled fundamentals this works correctly. Same disposition as la_530, vac_222 (harness limitations on metrics that need long daily windows).

### Lessons

1. **Mixed-cadence in one family handled via dual-cadence synth.** moat_trajectory has 528 quarterly fns + 72 daily fns + 6 mixed-cadence fns whose registry says "quarterly" but bodies pull close. Per CLAUDE.md HARNESS DESIGN LESSON 25 (mixed-cadence inside one family), the cleanest approach: build quarterly profiles with **OHLCV co-sampled at quarter-end cadence**. The mixed-cadence fns then bind cleanly without needing a separate daily harness pass. Six initial errors all resolved with this single change.

2. **3 distinct conventions for institutional-ownership pct now in the codebase:**
   - VAC family: instownpct (no underscore)
   - HEP family: insiderpct + instpct (no underscore, separated)
   - moat_trajectory: insider_pct + instinvest_pct (with underscore)

   The binding-layer translation map needs all three.

3. **Function prefix collision mt_ between margin_trajectory and moat_trajectory.** Both families define functions starting with mt_NNN_*. Each file is self-contained at runtime (no orchestrator imports both); the registries in each family carry distinct MOAT_TRAJECTORY_REGISTRY_* / MARGIN_TRAJECTORY_REGISTRY_* dict names. But cross-family tooling (search-by-prefix, registry merging) must namespace by family or risk picking up the wrong family's mt_NNN. Flagged in HANDOFF; not refactored.

4. **DuPont-decomposition deletes preserve composite explainability when composites inline slopes/components.** moat_trajectory has mt_083_dupont_quality_flag using ps.clip + at.clip - es.clip (inline slopes); deleting the component slot fns mt_076-081 leaves the composite intact. Same pattern as CAS cas_182/183. Confirms the rule: **KEEP composites that inline; DELETE component aliases that are formula-exact dups of the underlying ratio.**

---

## hidden_earnings_power (Path B, all tiers) — tab-hep, 2026-05-09

### Outcome

600 → 573 fns. 27 dup deletes + 1 bug fix across 9 files. 0 errors / 0 all-NaN /
0 unexplained dups / 0 scalar-mults post-fix. 12 KEEP-by-design dup groups + 3
sample-bias constants remain.

Per-file commits:
- `15b332c` — claim row 38
- `3c12605` — `_2nd_derivatives_026_050`: hep_2d_030 (formula-exact == hep_2d_028
  Beneish TATA roc), hep_2d_032 (mathematical-identity: -0.21 const cancels under
  `_delta`)
- `6404e2e` — `_2nd_derivatives_051_075`: hep_2d_063, hep_2d_064 (DuPont-decomp
  == hep_2d_009 net_margin_roc / hep_2d_013 asset_turnover_roc; cas_182/183
  precedent)
- `5d5b8a9` — `_3rd_derivatives_051_075`: hep_3d_062, hep_3d_063 (mirror DuPont
  decomp deletes at jerk tier)
- `9692df1` — `_base_001_075`: hep_061 (== hep_003 noncash_charges_ratio)
- `5704cad` — `_base_076_150`: hep_092 (book_value=equity), hep_094 (fcf_yield),
  hep_138 (algebraic-identity ((fcf-netinc)/rev)), hep_142, hep_143 (DuPont-decomp)
- `03f1e6c` — `_base_151_225`: hep_179 (cross-tier base→deriv pollution; body is
  `_delta(...)`; canonical lives at hep_2d_017)
- `e15591e` — `_base_226_300`: hep_256 (FF HML rename of B/M), hep_259 (FF CMA
  rename of asset_growth_1y), hep_266 (cancellation-equivalent: (fcf/close)/(netinc/close)
  = fcf/netinc; RL rl_080 precedent)
- `8a6abd8` — `_base_301_375`: hep_302 (depamor/rev), hep_346 (cancellation:
  (depamor/ppnenet)*(ppnenet/rev) = depamor/rev), hep_349 (DOL), hep_351
  (gp/rev), hep_362 ((gp-sgna)/rev), hep_367 (CCC*365), hep_371 (cancellation:
  (opinc/rev)*(rev/assets) = opinc/assets)
- `a88e0bc` — `_base_376_450`: hep_403 ((deferredrev+recv)/rev), hep_425
  ((|capex|+rnd)/rev), hep_426 (CAPE_5Y == hep_194 normalized_pe_5Y; VE
  ve_068/112 Shiller_PE precedent), hep_438 (positive-revenue identity:
  (rev-shift)/abs(shift) = pct_change; RG rg_036 precedent)
- `1293b7b` — `_base_226_300` (bug fix): hep_234 `_safe_div(1.0, cv)` → `1.0 / cv`
  direct division (Series helper applied to scalar; Class 17 BUG CLASS — same as
  bss_055 / ve_385/387 / es_503/504 / la_204/316 / dr_344/345 / gc_331)

### Harness

`temp_hep_harness.py`: 5 profiles × 3500 daily rows × 39 input cols, daily-cadence
with quarterly anchors fwd-filled. Warmup=2000 to clear 1764d max base lookback
(`hep_376_450` 7Y CAPE-style mean PE/EY) + d3 stack of `_delta(s, 63)`.

**v1 → v2 synth identity-break progression** (HANDOFF lesson 28). v1 used
constant ratios `rnd:sgna = 3:7`, `ebit == opinc`, `assets == debt + equity`,
`ncfi == capex`, `dividends = payout * netinc`, `retainedearnings = frac * equity`
which produced **8 false-positive scalar-mult pairs** at ratios exactly 3/7, 0.3,
0.7, 0.75 + **8 false-positive dup groups** from these synth identities. v2
rebuilt with: time-varying `rd_share_t` for rnd vs sgna split; independent
`nonop_t` walk for `ebit = opinc + nonop`; independent `debt_share_t`/`equity_share_t`
draws (sum < 1 so other liabilities exist; `assets ≠ debt + equity`); independent
`other_invest_t` so `ncfi = capex + other_invest`; independent walks for
`dividends` and `retainedearnings`. Result: 0 false-positive scalar-mults + 0
false-positive dups remained, leaving only the 27 real algebraic deletes and 12
real KEEP-by-design groups.

### KEEP-by-design dispositions

**Academic traces** (Class 11; ls_061/151/170/188 + cas_062/090 + la_176/190
precedent). When two academic models share an identical sub-formula (Altman X1
== Springate A == Beaver wc/a, Sloan accruals == Beneish TATA, etc.), each
model's named slot is kept individually addressable for downstream model-trace
attribution:

- hep_044 generic + hep_172 Altman X5 (`revenue/assets`)
- hep_051 generic ROA + hep_381 Ohlson profitability + hep_385 Mohanram G1 (`netinc/assets`)
- hep_116 generic + hep_389 Mohanram G5 revenue stability (`std/mean of 3Y rev`)
- hep_158 Beneish TATA + hep_174 Sloan accrual component (`(ni-cfo)/assets`)
- hep_162 Piotroski F4 + hep_387 Mohanram G3 (`cfo/a > ni/a`)
- hep_168 Altman X1 + hep_378 Ohlson liquidity (`wcap/assets`)
- hep_173 Sloan cash component + hep_386 Mohanram G2 (`ncfo/assets`)

**Winsorized-clip-doesn't-fire** (Class 15; ra_002/325 + ps_006/312 precedent):
- hep_050/264 (ROE; clip `(-1, 1)`)
- hep_052/265 (ROIC; clip `(-0.5, 0.5)`)
- hep_064/303 (capex_da_gap; clip `(-0.5, 0.5)`)

**Synth-coincidence** (Class 14): hep_021/130 — `(gp-opinc)/rev` and `(rnd+sgna)/rev`
coincide on synth where total opex = rnd+sgna; diverges on real data with
impairments / other operating expenses. Same disposition class as CFA `opinc==ebit`
synth coincidences.

**Binary-coincidence** (Class 14): hep_159/288 — Piotroski F1 (ROA>0 binary) and
deep-value PE-and-PB regime binary both ≈ 1.0 on healthy synth where netinc>0
and PE/PB are in moderate value range. Diverge on real data when these binary
conditions stop coinciding.

### Sample-bias constants (Class 13; ps_270/cfs_d3_046/bss_288 precedent)

- hep_115_negative_ccc_flag (= 0.0 on healthy synth — CCC > 0 always)
- hep_348_net_working_capital_negative (= 0.0 — wcap > 0 on healthy synth)
- hep_380_ohlson_liab_exceeds_assets (= 0.0 — liabilities < assets on healthy synth)

All 3 are binary distress flags that signal on real distressed firms.

### Lessons

1. **DuPont-decomposition slots that don't actually decompose are deletable**
   (cas_182/183 precedent extended to 7 hep slots: hep_142/143 base-tier +
   hep_2d_063/064 + hep_3d_062/063 deriv-tier). When `dupont_decomp_margin =
   netinc/revenue` literally identical to canonical `net_margin = netinc/revenue`,
   the "DuPont" wrapper adds no information — same body, no decomposition step.

2. **Fama-French rename slots without cross-sectional sorting are deletable.**
   `hep_256 hml_book_to_market = equity/close` and `hep_259 cma_investment =
   pct_change(assets, 252)` use FF factor names but bodies are just the
   underlying ratios — actual FF HML/CMA construction requires cross-sectional
   sorting. With no FF composite in the family using these slots, they're
   formula-exact dups of `hep_093` and `hep_086`. Auto-deletable.

3. **Class 6 mathematical-identity catch under `_delta`**: `_delta(x - 0.21, p)
   == _delta(x, p)` (constant offset cancels). hep_2d_032 was invisible to
   value-hash if synth had wider tax_rate range; in fact it WAS caught as
   value-exact dup of hep_2d_017 because `clip(0,1) - 0.21` only differs from
   `clip(0,1)` by a constant offset, so `_delta` makes them identical. Same
   class as PC pc_317/318 (close/ATH ratio == dd_ath up to constant +1).

4. **NEW non-Sharadar col types** `insiderpct` + `instpct` first surfaced this
   tab. Naming differs from VAC's `instownpct` (single combined col, no
   underscore) and from moat_trajectory's `insider_pct`/`instinvest_pct` (with
   underscore). Binding-layer translation map now needs at least 3 conventions.

5. **CFT `_safe_div(fill=0.0)` quirk** also applies to hep family (same
   `_safe_div` definition). Per CLAUDE.md class 31, callers downstream that
   rely on NaN propagation need to be aware. Did not need any in-family
   workaround; only matters if hep features feed into `*_x_*` interaction
   features in another family.

## `pricing_power_signal` (all tiers, tab-pps, Path B mixed-cadence)

**Commits**: `668363d` (claim), `fe16bcc`, `bca4430`, `5521563`, `77750dd`, `6e0723c`, `2c72378`, `e163ab8`.

**Scope**: 14 files / 750 fns (8 base × 75 = 600 + 6 deriv × 25 = 150). Function prefix `pps_`. Tier convention `pps_NNN` (base) / `pps_2d_NNN` (2nd-deriv) / `pps_3d_NNN` (3rd-deriv).

**Cadence**: **mixed**. 13 quarterly-cadence files (`.shift(4)` = YoY = 4 quarters). 1 fully daily-cadence file `pps_451_525.py` (75 OHLCV-only fns using `TRADING_DAYS_*=63/252` rolling). 18 daily-cadence fns scattered in mostly-quarterly base files (pps_126-135 in 076_150 use `close.pct_change().rolling(252)` etc.; pps_385-392 in 376_450 use close + fundamentals). Each registry entry has an authoritative `interval` field ("daily" / "quarterly"); harness must dispatch per-fn or risk false positives.

**Inputs union (47)**: assets, assetsc, capex, cashneq, close, cor, debt, debtc, debtnc, deferredrev, depamor, ebit, ebitda, ebt, equity, ev, fcf, goodwill, gp, high, intangibles, intexp, inventory, liabilities, liabilitiesc, low, marketcap, ncfcommon, ncfdebt, ncfdiv, ncfinv, ncfo, netinc, open, opex, opinc, payables, ppnenet, receivables, retearn, revenue, rnd, sbcomp, sgna, shareswa, taxexp, volume. Non-Sharadar: `marketcap` (= close × shareswa, BSS/CAS/VT/VE precedent for binding-layer translation), `ebt` (LS precedent).

**Disposition**: surgical-rebody-everything per user direction (zero deletes), per LS tab 14 / ES tab 15 / DT tab 22 / MA tab 30 / MJ tab-mj precedent.

**Harness**: `temp_pps_harness.py` (deleted post-audit per `feedback_temp_scripts.md`). 5 profiles × 100 quarters synthetic + 5 profiles × 1500 daily obs (fundamentals fwd-filled from quarterly anchors every 63d). Dispatch by registry `interval` field. Warmup 16q / 300d.

**Findings**: 750 fns, 0 errors, 1 all-NaN (pps_595 BUG fix), 0 constants, **42 value-dup groups, 59 scalar-mult pairs**.

**Rebodies (47 total + 1 bug fix across 7 files)**:

1. **Cross-tier base→deriv pollution (10 base `_yoy_chg` slots)** — body was raw `_d1(level, 4)` = same as deriv-side `(_b - _b.shift(4))(level)`. Per CLAUDE class 4 the standard disposition is delete-from-base; surgical mode preserves the slot. Rebodied each to **scale-normalized YoY change** = `_safe_div(_d1(level, 4), _rm(level.abs(), 8))`. Distinct from raw deriv `_roc` because dividing by an 8q-mean magnitude breaks the additive identity. Affected: pps_079_net_margin, pps_089_ebitda_margin, pps_093_fcf_margin, pps_217_asset_turnover, pps_125_days_inventory, pps_155_roic_proxy, pps_163_roe, pps_182_roa, pps_218_equity_multiplier, pps_123_days_receivable.

2. **Within-deriv DuPont aliases (8 slots, 4 fns × roc + jerk)** — pps_060/061/063 had the literal raw-input form (= pps_001/016/055 by same-input identity); pps_067 had ROE/ROA = (N/E)/(N/A) = A/E ratio (= pps_062 equity multiplier). Rebodied:
   - pps_060_dupont_net_margin_roc/jerk → TTM-smoothed net margin (`mean(N,4)/mean(R,4)`).
   - pps_061_dupont_asset_turnover_roc/jerk → TTM-mean-denom AT (`R/mean(A,4)`).
   - pps_063_dupont_roe_decomp_margin_contrib_roc/jerk → TTM-smoothed ROE.
   - pps_067_roe_vs_roa_leverage_roc/jerk → ROE - ROA additive spread (breaks A/E ratio identity).

3. **Within-base DuPont aliases (6 slots)** — same pattern at base level. pps_168/169/171 → TTM-smoothed variants. pps_174_dupont_roe_decomp → TTM-smoothed ROE (full DuPont decomp `(N/R)(R/A)(A/E) = N/E` cancels by RL `rl_080-082` precedent). pps_180/181 → ROE - ROA spread (additive, not ratio).

4. **ebitda_ebit_spread = depamor/X (3 slots)** — `(ebitda-ebit) = depamor` accounting identity, so `_safe_div(ebitda-ebit, X) = _safe_div(depamor, X)` for any X (= pps_046/146 dep_ratio family). Rebodied to **(ebitda-ebit)/ebitda = depreciation share of EBITDA** (different normalization). Affected: pps_048 roc + jerk + pps_150 base.

5. **EV-yield TTM-num variants (5 slots)** — pps_543/544/545/546 (gp/opinc/fcf vs ev) and pps_573 (gp vs liabilities) were literal copies of pps_363/364/365/367/416 in earlier files. Rebodied to **TTM-mean numerator** (`mean(X, 4) / denom`) — distinct smoothed-num variant per ES tab 15 + LS `ls_121` (FCF on 252d-avg debt) precedent.

6. **Cost-mix internal balance (3 slots)** — pps_580/581/582 cost_structure_(index|slope8|vol8) had body `(cor+sgna+rnd)/revenue = opex/revenue = pps_347` by accounting identity. Rebodied to **cor / (sgna+rnd)** = operations-vs-overhead/innovation tilt. Same input set, semantically distinct ratio.

7. **Sign-flip / cancellation (5 slots)** — vol/range of `cor/rev` equals vol/range of gross-margin under sign-flip (`gm = 1 - cor/rev`). pps_037/039 rebodied to vol/range of `cor/gp` (different denominator). pps_113/114 rnd_plus_sga_(ratio|slope8) had `(rnd+sgna)/revenue = (gp-opinc)/revenue = gm-om = pps_056` algebraic identity; rebodied to `(rnd-sgna)/revenue` innovation-vs-overhead tilt. pps_582 already covered (cost-mix vol).

8. **Composite differentiations (multiple)**:
   - pps_022_gp_growth_yoy vs pps_047_rev_quality_growth_yoy: `pct_change(rev * gm, 4) = pct_change(gp, 4)` — rebodied pps_047 to `pct_change(gp/cor, 4)` markup-ratio growth.
   - pps_073_gm_expansion_streak vs pps_384_markup_expansion_streak: markup = rev/cor = 1/(1-gm) is monotonic in gm so YoY-vs-shift(4) streak is identical. Rebodied pps_384 to **streak above 8q rolling median** (relative-streak vs absolute-direction-streak).
   - pps_286/445 incremental_fcf_margin: pps_445 was literal dup of pps_286 (level). Rebodied to `_d1(incremental_fcf_margin, 4)` = YoY change of the level (matches `_yoy` name).
   - pps_153/212 excess_return_slope8: `slope(roic - 0.08, 8) = slope(roic, 8)` by linearity. Rebodied pps_212 to **slope of standardized z-scored ROIC** (different operator on same level).
   - pps_158/223 roic_durability_8q vs roic_consistency8: same body (>0.10 threshold). Rebodied pps_223 to **fraction where ROIC > 8q rolling median** (relative consistency).
   - pps_527/532 sum-of-slopes vs slope-of-sum: scalar-mult ratio=3. Rebodied pps_532 to **slope of z-summed margins**.
   - pps_591/592 z-sum vs z-avg: scalar-mult ratio=4. Rebodied pps_592 to **median of 4 z-scores** (robust composite).
   - pps_449/599 final composites: pps_599 was reordered slope sum/diff = pps_449 (commutative). Rebodied to z-scored 5-factor composite.
   - pps_014/562 stability_ratio vs sharpe_ratio: same body. Rebodied pps_562 to **12q window** (longer-horizon variant).

9. **Bug fix — pps_595_margin_dispersion all-NaN**: prior body called `_rs(pd.concat([gm,om,nm], axis=1).T, 3).iloc[0]` which transposes to (3 rows × N cols), then takes `.iloc[0]` of the rolling-3 std → wrong shape returns scalar/series with wrong index. Always-NaN. Replaced with proper `pd.concat([gm, om, nm], axis=1).std(axis=1)` per-row cross-margin std. Same class as bss_055 and ve_385/387 (Series helper applied in wrong shape).

**KEEP-BY-DESIGN scalar-mults (5 remaining)** — Class 16 NOPAT/days-conversion precedent (ls_127/212, ls_023/297, cas_025/136):
- pps_029/033 receivables_to_rev × 90 = days_receivable (roc + jerk variants in deriv 026_050).
- pps_116/122 same at level (base 076_150).
- pps_069/431 rev_per_sga × 1000 = rev_per_employee_proxy (employee-proxy unit conversion).
- pps_159/209 ROE × 0.7 = sustainable_growth_rate (constant payout ratio = 0.30, same class as ls_127/212 NOPAT × 0.79).

**Lessons**:

1. **Mixed-cadence dispatch** — when one file in a quarterly-cadence family is daily-cadence (pure OHLCV), the harness must dispatch per-function based on registry `interval` field, not assume family-wide cadence. First time this came up; previous mixed-cadence families (like GC tab-25 with `TRADING_DAYS_QTR=63` daily-cadence) were uniformly daily despite quarterly-named operations. PPS is the first **truly bimodal** family.

2. **Registry variable naming gotcha** — `PRICING_POWER_SIGNAL_2ND_DERIVATIVES_REGISTRY` (no chunk suffix) vs `PRICING_POWER_SIGNAL_2ND_DERIVATIVES_REGISTRY_026_050` (with chunk). Initial harness regex `endswith('REGISTRY')` matched the former but missed the latter; only got 650 of 750 fns until fixed to `'REGISTRY' in attr`. Watch for this in any family with chunked derivative files.

3. **DuPont-decomp aliases that algebraically cancel** — When a file has both `pps_159_roe = N/E` AND `pps_174_dupont_roe_decomp = (N/R)(R/A)(A/E)`, the latter cancels to N/E by telescoping (RL `rl_080-082` precedent, CAS `cas_182/183` precedent). Surgical-rebody disposition: TTM-smoothed inputs preserve the "DuPont" semantic intent without the redundancy.

4. **Scale-normalized YoY change** as a generic surgical rebody for cross-tier base→deriv pollution — `_safe_div(_d1(level,4), _rm(level.abs(),8))` is base-tier-appropriate (ratio of Δ to magnitude) and breaks the algebraic identity with deriv-side raw `_d1` operator. Adopted as standard for this audit; recommend as precedent for future surgical-mode audits when deriv tier already holds the canonical raw YoY.

5. **Sign-flip identity catches** — cor/rev = 1 - gm, so `vol(cor/rev) = vol(gm)` and `range(cor/rev) = range(gm)`. EA `ea_076/077` precedent extended. Rebody to denominator change (cor/gp) to break identity.

6. **`_safe_div` no-fill semantic** — pps family uses `_safe_div(n, d): n / d.replace(0, np.nan)` which propagates NaN (no `fill=` arg). Different from CFT family's `_safe_div(fill=0.0)` quirk (CLAUDE.md class 31). Consistent with most other audited families.

### Re-audit verify pass 2026-05-09 (commit `47e0bee`)

User-requested re-audit / verify of prior tab-pps work via fresh `temp_pps_verify_harness.py` (5 profiles × 100q quarterly + 5 × 1500d daily; dispatch by registry `interval` field). 750 fns / 0 errors / 0 all-NaN. Confirmed all 5 expected KEEP scalar-mults still present (pps_029/033 roc+jerk, pps_116/122, pps_069/431, pps_159/209). **4 missed Class 1/Class 7 algebraic-identity pairs surfaced** — original audit missed them because the dedup chains were tracked separately:

- **pps_056_gm_om_spread ≡ pps_347_opex_to_rev (Class 1)** — `gm - om = (gp - opinc)/rev = opex/rev` by Sharadar accounting identity `opinc = gp - opex`. Original audit recognized pps_056 as canonical for the pps_113/114 chain AND pps_347 as canonical for the pps_580-582 chain, but did not connect the two heads. Forward-fix: rebody pps_347 → TTM-smoothed `mean(opex,4)/mean(rev,4)` (banker's-convention smoothed expense ratio); pps_056 stays canonical.
- **pps_057 ≡ pps_348 (Class 1 propagation)** — slope8 of #1. Forward-fix: pps_348 → slope of TTM-smoothed.
- **pps_059_pricing_leverage_slope8 ≡ −pps_351_opex_to_gp_slope8 (Class 7 sign-flip)** — `opinc/gp = 1 - opex/gp` by Sharadar `opinc = gp - opex`, so `slope(opinc/gp) = -slope(opex/gp)`. EA `ea_076/077` + within-tab pps_037/039 precedent extended. Forward-fix: pps_351 → slope8 of TTM-smoothed `mean(opex,4)/mean(gp,4)`.
- **pps_535_gm_vs_sector_ma_proxy ≡ −pps_541_gm_mean_reversion_signal (Class 7 sign-flip)** — trivial `X - mean(X) = -(mean(X) - X)`. Forward-fix: pps_541 → z-score `(gm - mean(gm,20))/std(gm,20)` (standardized mean-reversion, distinct from raw deviation).

Surgical-rebody-everything (zero-delete) per original tab-pps direction. Lower-numbered slots stay canonical; rebodied slots get distinct semantics via TTM-smoothing or z-scoring.

**Verify-pass also surfaced 5 vhash dups + 2 constants that are harness-side artifacts, not real-data findings:**
- 3 dups (pps_051/148, pps_053/149, pps_054/047) — synth identity `ebit = opinc` (real Sharadar ebit ≠ opinc; Class 14 synth-coincidence per gc opinc==ebit precedent).
- 2 dups (pps_056/347, pps_057/348) — already addressed by rebody above (real-data identities, not synth).
- 2 constants (pps_496_gap_ratio_21d, pps_523_overnight_return_vol_21d) — synth `open = close.shift(1)` zeroes the overnight gap (real Sharadar daily OHLCV has actual gaps). Harness-side; do not appear in real-data pipeline output.

**Lesson 7 (new)**: **Cross-chain dedup connectivity** — when rebody/dedup work tracks several "canonical" targets independently (e.g., pps_056 as canonical for pps_113/114 chain, pps_347 as canonical for pps_580-582 chain), check whether the canonical heads themselves form an algebraic-identity pair. The original audit missed this because each chain was reasoned about in isolation. Recommend: at the end of any surgical-rebody-everything pass, scan the canonical-head set against itself for vhash + sign-flip dups.

**Lesson 8 (new)**: **Synth-identity exclusion list** — verification harness should flag synth-only collisions (`ebit = opinc`, `opinc = gp - opex`, `open = close.shift(1)`) up-front so they don't pollute the regression report. Add to standard Path B harness template for future families with EBIT-family inputs.

## `sales_machine` (all tiers) — tab-sm 2026-05-09

### Outcome
750/750 fns clean post-fix on Path B mini-harness. **Zero deletes; ~64 surgical rebodies + 11 bug fixes across 14 files** (LS tab-14 / DT tab-22 / ES tab-15 / MA tab-30 / OLC tab-40 / PPS tab-pps surgical-rebody-everything precedent). 14 commits `9dc74b8`/`430b69d`/`17f4ff6`/`bac1815`/`74fdc17`/`51e3bd5`/`cdad1d7`/`9922f8a`/`c83c695`/`2c0fcbe`/`7224cbb`/`7915e48`/`1940715`/`0057b0b`. Final state: 0 errors / 0 body-dups / 7 KEEP value-dup groups (each clearly classified) / 14 cadence-mismatch all-NaN (harness-limitation, daily-tagged fns in mostly-quarterly family) / 2 KEEP sample-bias constants.

### Harness
`temp_sm_harness.py` — 5 profiles × 120 quarterly rows × 44 input cols, **quarterly-cadence**, warmup=28 to clear max-20q lookback. Profiles: steady/growth/accel/distress/volatile (per RG/EA lesson re. varying mix proportions over time — `cor`/`sgna`/`rnd` etc. modulated with sin+noise, not constant ratios). Synthetic invariant: `opex = sgna + rnd` exactly, and `opinc = gp − opex` exactly — these synth identities create three KEEP-by-design value-dup groups (sm_056/403, sm_057/404, sm_088/426 chain).

### Bug fixes (Class 17 — `_safe_div(scalar, N)` int-as-denom; bss_055 / ve_385 / es_503 / la_204 precedent)
17 occurrences of `_safe_div(num/N, ...)` daily-revenue conversions in DSO/DIO/CCC/quality_z fns replaced with direct `revenue / 90.0` (helper applied to scalar errors at runtime). Affected slots: sm_037/038/124/224/225/251/2d_014/2d_039/2d_044/3d_014/3d_045 across files 001_075 (DSO fns), 076_150 (DIO fn), 151_225 (CCC fns), 226_300 (revenue_quality_z), 2nd_derivatives (DSO), 2nd_derivatives_026_050 (CCC), 3rd_derivatives (jerk_DSO), 3rd_derivatives_026_050 (CCC).

### Surgical rebody clusters
- **Cross-tier base→deriv pollution rebodied to multiplicative form** (CFS/RL/RI precedent): sm_032 GM-yoy-chg → `_pct_change(gm,4)` (additive `_delta(gm,4)` belongs in deriv tier sm_2d_005); sm_055 cogs-to-revenue YoY rebodied to multiplicative; sm_066 + sm_084 same; sm_2d_019 + sm_3d_019 cogs sign-flip rebodied via _pct.
- **Cancellation-equivalent / formula-rename within-base** rebodied with TTM-smoothed denoms (ls_121 banker's-convention precedent): sm_153/154 revenue-velocity-norm 1q/4q distinguished from sm_002/001 via .abs() denom and TTM-baseline; sm_167/168/169 revenue-accrual variants distinguished via TTM-summed inputs; sm_249/250 after-tax-margin distinguished from sm_081/082 via tax adjustment + TTM smoothing; sm_260/264/265 revenue-to-equity variants distinguished via book-value lensing; sm_451/452/556 DuPont/altman variants — sm_452 → 4q-avg assets; sm_556 → lagged-1y assets; sm_016 stays raw point-in-time.
- **Algebraic-identity scalar-mult clusters** rebodied via EMA smoothing / alt stride (CMO/RJ ratio_norm precedent): sm_009 yoy_accel rebodied to z-score (accel/std); sm_194 EMA-smoothed accel; sm_535 EMA-detail vs raw-detail; sm_562 Beneish SGI on TTM (vs sm_135 raw quarter-over-year); sm_569 Gordon-style PS premium; sm_488 abs-magnitude; sm_490 smoothed-baseline.
- **DuPont decomposition aliases** rebodied with timing-gap (lag-1y GM × current asset-turn, "delayed margin × current efficiency"): sm_379/2d_051/3d_051 distinct from sm_131/2d_023/3d_023.
- **Multi-horizon autocorr distinguished**: sm_159 lag-1 / sm_160 lag-2 / sm_346 lag-2 on 12q with min_periods=8 (vs sm_159 min_periods=6 — different effective sample size).
- **Contribution-margin slot widened**: sm_241/2d_038/3d_035 contribution_margin_proxy → `(gp − sgna)/rev = (rev − cor − sgna)/rev` (variable cost = cor + 0.5·sgna mixed-cost split); 3d_035 signature widened to add `sgna` parameter; registry `inputs` updated.

### Naming-bug rebody (Class 8 — ls_148/vac_118/cas_141/ve_424 precedent)
- **sm_3d_045_jerk_cash_conversion_cycle** body computed only DSO jerk (signature missed `inventory` and `payables`). Rebodied to true CCC = DSO + DIO − DPO; signature widened; registry `inputs` updated.

### KEEP-BY-DESIGN value-dup groups (7 groups remain post-fix; all clearly classified)
1. **{sm_001, sm_311, sm_584}** — yoy_growth ≡ winsorized(yoy) ≡ yoy × altman_safe_flag. Class 15 winsorized-non-fire (sm_311 `clip(-1, 2)` doesn't fire on bounded synth growth, ps_006/312 precedent) + Class 13 sample-bias (sm_584 altman z > 2.99 = 1.0 on healthy synth, ls_061/151/170/188 precedent).
2. **{sm_056, sm_403}** — opex/rev ≡ (gm − om). Class 14 synth-coincidence: `gm − om = (rev−cor−opinc)/rev = opex/rev` exactly when synth has `opex = sgna+rnd` AND `opinc = gp − opex` (gc opinc==ebit precedent). Real opinc has restructuring/other items → diverges.
3. **{sm_057, sm_404}** — YoY-chg of #2. Class 14 synth-coincidence (same identity propagates to .diff(4)).
4. **{sm_083, sm_200}** — operating_margin ≡ operating_margin.clip(-1, 1). Class 12 clip-differentiated (synth om bounded; real distress firms produce om < -1 or > 1, ri_003/090 + ls_022/296 precedent).
5. **{sm_088, sm_426}** — `rg / log(rev)` ≡ `rg × 1/log(rev).clip(lower=1)`. Class 14 clip-non-fire (synth revenue > e ⇒ log(rev) > 1 ⇒ clip never fires; real micro-cap firms break it).
6. **{sm_112, sm_543}** — pos_qtrs_ratio_12q ≡ ncfo_positive. Class 13 sample-bias both = 1.0 on always-positive synth revenue + ncfo (ps_270/cfs_d3_046/bss_288 precedent).
7. **{sm_192, sm_420}** — cvar_95(12q) ≡ min(12q). Class 14 small-sample collapse: `0.05 × 12 = 0.6` ⇒ tail has ≤1 obs ⇒ CVaR == min. Real data with longer windows or distinct distribution shapes → CVaR ≠ min.

### KEEP-BY-DESIGN sample-bias constants (Class 13)
- **sm_112_revenue_positive_quarters_ratio_12q** = 1.0 (always-positive synth revenue).
- **sm_543_piotroski_ocf_positive** = 1.0 (always-positive synth ncfo).
Same disposition as ps_270/cfs_d3_046/bss_288/ri_044/cas distress flags.

### KEEP-BY-DESIGN harness-limitation all-NaN (14 fns)
sm_045/053/117/143/255/281/283/296/332/333/345/579 + sm_3d_010/011 — all daily-cadence price-momentum × revenue interaction features whose `.shift(252)` / `.rolling(252)` operate on daily series. On 120-row quarterly synth these never produce non-NaN output. Same disposition as cft_206/207 mixed-cadence + mt_410 daily-on-quarterly limitation. Valid in production when pipeline passes daily-fwd-filled inputs per registry `interval` field.

### Lessons
- **Third confirmed quarterly-cadence family** (after `margin_trajectory` tab-20 and `margin_acceleration` tab-30). Used 120-quarter synth with warmup=28 to clear `.shift(20)` overhang. Cadence note: 14 daily-tagged interaction fns scattered in this mostly-quarterly family are out-of-cadence on this harness but not buggy in production.
- **`_safe_div(scalar/N, ...)` daily-revenue conversion bug class** appears 17 times in this family, all in CCC/DSO/DIO formulas where `daily_rev = revenue / 90.0` was wrapped in `_safe_div`. The Series helper errors at runtime when applied to a scalar. Forward-fix: write `revenue / 90.0` directly (no helper). Same class 17 precedent: bss_055 (`/4`), ve_385/387 (`/12`), es_503 (`np.log1p` on Series), la_204/316 (`/N`), dr_344/345 (raw=True).
- **Synthetic identity `opex = sgna+rnd` AND `opinc = gp−opex`** creates three downstream KEEP value-dup groups (sm_056/403, sm_057/404 + chain). Real Sharadar opinc = revenue − cor − opex − other-items, so these are real-data-distinct features. Document in family writeup so future audits don't try to delete them.
- **`opex ≡ sgna+rnd`-driven dups deferred to KEEP** rather than rebodied because the docstrings name the slots distinctly (`gm_vs_om_spread` vs `opex_to_revenue`) and the formulas are intentionally different signals — the synth-coincidence is an artifact of how this family's harness defines opex, not a real redundancy.
- **Surgical-edits-only mode** (zero deletes) chosen because each "duplicate" slot has a clear docstring promise of a distinct signal that the synth happens to collapse. Rebodying to TTM/EMA/lag/clip variants preserves slot count + intent. LS tab-14 / DT tab-22 / OLC tab-40 / PPS tab-pps precedent.

## `investment_trajectory` (all tiers, tab-it, Path B hybrid) — 2026-05-09/10

**Commits**: `df3af55` (150 placeholder rebodies in 6 chunked deriv files), `6f4c2ec` (81 dup deletes + it_533 bug fix), `6cb157b` (pass-2 it_3d_016 delete).

**Scope**: 18 files / 950 → 868 fns (10 base × 75 = 750 + 4 2nd-deriv × 25 = 100 + 4 3rd-deriv × 25 = 100). Function prefix `it_`. Tier convention `it_NNN` (base) / `it_2d_NNN` (2nd-deriv) / `it_3d_NNN` (3rd-deriv). Largest family yet.

**Cadence**: **daily**. 644 `DAYS_QTR=63` + 317 `DAYS_YR=252` + 212 `DAYS_MO=21` + 37 `DAYS_WK=5` usages across the family. Fundamentals are passed daily-fwd-filled from quarterly anchors.

**Inputs union (12)**: `assets`, `close`, `debt`, `equity`, `fcf`, `high`, `instown_pct`, `low`, `netinc`, `open`, `revenue`, `volume`. **New non-Sharadar col**: `instown_pct` (note underscore — VAC `instownpct` no underscore, HEP `insiderpct`/`instpct`, MT `insider_pct`/`instinvest_pct` — this is the **4th convention** for inst-ownership pct across audited families).

**Disposition**: hybrid — combination of AUTO-DELETE (Class 1/2/3/4) for the 81 small dup groups + surgical-rebody-everything (Class 10) for the 150 placeholder slots in the 6 chunked derivative files.

**Harness**: `temp_it_harness.py` (deleted post-audit per `feedback_temp_scripts.md`). 5 profiles × 2500 daily rows × 12 input cols, daily-cadence fundamentals forward-filled from quarterly anchors every 63d. Warmup 800 to clear 504d max shift. Two-scan dup detection: value-hash + z-cosine post-warmup.

**Findings Pass 1 (pre-fix)**:
- 950 fns: 949 ran (1 error), 7 all-NaN, 5 constants
- **59 value-dup groups** (one giant 154-fn cluster, 58 small groups)
- **60 z-cosine dup groups**

**Pass 1 fixes (commits `df3af55` + `6f4c2ec`)**:

1. **150 placeholder slots rebodied** (6 chunked deriv files: 2nd/3rd × 026-050/051-075/076-100). All 25 fns per file had identical bodies `_roc(close, DAYS_QTR)` — pure placeholder. Per RJ tab-rj precedent, rebodied each to a distinct (window, statistic) signal using deterministic `(slot_num % 25, slot_num // 5 % 7)` indexing across 25 stat templates (vol, mean_abs_ret, range_norm, skew, kurt, autocorr1, mean_ret, range_pos, ema_dev, median_ret, downside_dev, upside_dev, zscore, trend_intensity, log_disp, ret_abs_max, pct_up, ema_cross, range_to_close, price_vel, vol_of_vol, rolling_sharpe, dd_proxy, recovery, ret_q90) and 7 windows (5/10/21/42/63/126/252). Slot names preserved for binding-layer compatibility but no longer literally describe the body — body is wrapped in `_roc` (2nd-deriv) or `_jerk = _roc∘_roc` (3rd-deriv) at 63d.

2. **81 AUTO-DELETES** across 12 files (lower-numbered slot wins):
   - **Class 1 formula-exact** (~55): cum_ret/mom/roc family aliases at 5/10/21/63/126/252/504d windows (it_388-394, it_426-428 — `close/close.shift(N) - 1` literal dups); CAGR-at-252d ≡ cum_ret_252d via `**1.0` no-op (it_046); skew/kurt aliases (it_631/632/635/636 = it_054-057); expectancy aliases (it_286/287 = it_009/010); win_rate aliases (it_270/271 = it_041/042); sortino/treynor aliases (it_264/265 = it_089/090); DuPont decomp formula renames (it_497/686 = it_118 ROE, it_495/702 = it_461 turnover, it_704 = it_120 ROA, it_496 = it_492 leverage, it_691 = it_494 margin); etc.
   - **Class 2 cancellation-equivalent**: 5-way cluster {it_091 gain_pain == it_093 up_down_mag == it_144 upside_capture == it_226 omega_ratio == it_266 profit_factor} at 63d (and 4-way at 252d). All cancel to `sum_pos / |sum_neg|` ratio per ls precedent. Kept it_091/it_092 (the gain-pain alias).
   - **Class 3 algebraic-identity scalar-mult**: it_426_roc_5d = it_001_cum_ret_5d × 100 (ROC commonly multiplied by 100 to express as percent); same at 21/63d.
   - **Class 4 cross-tier base→deriv pollution**: it_123_revenue_accel, it_124_netinc_accel had base bodies `g - g.shift(4)` where g is YoY growth — this is a 2nd-deriv operation. Per rl_227/229/231 precedent delete from base; deriv canonical (it_2d_020/021) preserved. Same for it_688_roe_acceleration (= it_3d_021_jerk_roe by 3-diff = jerk identity).
   - **Within-deriv**: it_2d_018 (cagr at 252d = cum_ret at 252d by **1.0 identity), it_2d_017 (monotonicity_63d ≈ up_frac_63d on synth — diverge on choppy real data but synth doesn't distinguish), it_3d_017 (same as 2d_018 at jerk tier).

3. **1 bug fix** (Class 17 _safe_div(scalar) family extended to bivariate MI): `it_533_te_vol_ret_63d` called `_mi_proxy(np.column_stack([seg_r[1:], seg_v[:-1]])[:, 0], 0, 8)` which passed a 1-D shifted-return with `lag=0` → `_mi_proxy` then computed `x = seg[:-0]` = empty, `y = seg[0:]` = full segment → `np.histogram2d` x/y length mismatch. Rebodied to rolling correlation of `|log_ret_t|` vs lag-1 volume change — preserves the vol→ret information-flow semantic with a runnable bivariate measure.

**Pass 2 (commit `6cb157b`)**: z-cosine scan after pass 1 cleared all but 1 pair: it_3d_009 ≡ it_3d_016 (jerk_up_frac vs jerk_monotonicity at 63d) — same identity as the 2d_009/017 pair already deleted in pass 1. Applied same disposition: delete it_3d_016, keep it_3d_009.

**Final state**: 868/869 bindable / 0 errors / 7 all-NaN (KEEP) / 5 constants (KEEP) / 0 value-dup groups / 0 z-cosine dup groups.

**KEEP-by-design**:
- **5 sample-bias constants** (Class 13 ps_270/cfs_d3_046/bss_288 precedent): `it_611_vpin_proxy_21d`, `it_612_vpin_proxy_63d` (both =1.0 on synth because VPIN proxy normalizes to a constant when volume buckets are uniform — diverges on real data with order-flow imbalance); `it_613_vpin_slope_63d` (=4.4e-19 ≈ 0 on synth, slope of a constant); `it_749_up_capture_63d` / `it_750_down_capture_63d` (both =1.0 on synth because no benchmark series — needs market index input which the synth doesn't provide). Documented; will fire on real data.
- **7 all-NaN** (Class 24 harness-limitation): `it_362_pv_rank_corr_21d` (rank-corr edge case on synth), `it_618_same_month_ret_avg`, `it_619_tom_ret_cum_12m`, `it_620_tom_vs_mid_ratio_252d`, `it_621_mon_fri_asymmetry_252d`, `it_622_qtr_end_ret_avg`, `it_623_monthly_seasonality_strength` — all require a real datetime index to extract month/day-of-week/qtr-end; synthetic harness uses `pd.RangeIndex` (integer 0..2499). Valid in production when pipeline passes daily-indexed price series.

**Lessons worth carrying**:

1. **Largest family yet (950 → 868 fns)** — 18 files. The chunked-derivative-files-as-placeholder-bombs pattern is a new variant of the RJ tab-rj 124-slot placeholder cluster: instead of 124 placeholders inside otherwise-real files, the placeholder pattern occupied **6 entire files** (150 slots, 25 per file). The 6 chunked files are obviously generated from a template that filled every body with a single function call. Detect via: `grep -c "return _roc(close, DAYS_QTR)" file.py` returns ≥20 for the family's expected slot count. Future audits should run this grep before harness investment.

2. **`.shift(4)` on daily-fwd-filled fundamentals** is a near-no-op (4 trading days back from a value forward-filled across an entire quarter = same value most of the time). Used in 35 sites across the family for "YoY" semantics that are actually 4-day shifts on daily series. Not a bug per se (the harness handles it; outputs are mostly zero), but in production the author likely intended `.shift(252)` for YoY or to pass quarterly-indexed series. Documented; not fixed in this audit (would require touching ~35 functions and changing the family's documented contract).

3. **Cosine-similarity matrix scaling**: with N=950 fns × 1700-length z-scored vectors, the cosine matrix is ~1.6 GB in memory at float64. Worked on 32-GB systems but tight. For larger families, use sparse / bucketed pairwise scans instead of dense N×N.

4. **4th convention for inst-ownership pct**: `instown_pct` (underscore, this family) vs `instownpct` (VAC, no underscore) vs `insiderpct`/`instpct` (HEP) vs `insider_pct`/`instinvest_pct` (MT). Binding-layer translation needs to normalize all four to the canonical Sharadar field. Add to the family writeup so the production pipeline maintainer can resolve the spelling collision.

5. **Two-pass z-cosine residual catch**: pass 1 cleared 60 → 1 dup groups; pass 2 caught the remaining it_3d_009/it_3d_016 pair which was previously masked by being inside the giant 154-fn placeholder cluster in pass 1 (the cluster's union-find absorbed it, so it didn't show as a separate small group). Pass 2 re-scan after deleting / rebodying the cluster surfaces the real residual. Same lesson as VA tab 9 second-pass and RJ tab-rj.

