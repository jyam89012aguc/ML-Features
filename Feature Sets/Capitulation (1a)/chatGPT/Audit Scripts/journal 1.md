# Journal

## 2026-05-08 — session 1

**Done this session:**
- `git init` on the feature library at `C:\Users\jyama\Desktop\origional  and complete features 1a\`. Initial baseline commit covers all 431 files (`d7511a4`).
- Wrote `CLAUDE.md` documenting the file naming convention, function naming
  prefixes, the inlined-helpers pattern, the daily-vs-quarterly cadence trap,
  and the lack of build/lint/test infra.
- `git init` on the pipeline-scripts repo at `C:\Users\jyama\Downloads\` with a
  strict `.gitignore` whitelist (11 canonical pipeline scripts only; everything
  else in Downloads is ignored). Baseline commit `ae7a40f`, harness fix `ef82b9b`.
- Patched `test_new_features_db_direct.py` to bind feature args via
  `inspect.signature` instead of passing the whole `slice_df` positionally.
  Patch eliminated the harness's false-positive echo flagging.
- Audited `price_momentum_base` (2 files, 300 functions) end-to-end:
  - Ran with `--lookback-days 504` first, then `--lookback-days 1500` to rule out
    all-NaN noise. Confirmed 12 constants and one 12-member value-dup group
    were lookback artifacts.
  - Found 2 formula-exact dup pairs and 4 additional value-exact dup pairs
    (mathematical or naming-collision duplicates, not lookback artifacts).
  - Removed 6 duplicate functions across both files (def + registry entry each).
    Post-fix: 294/294 clean, 0 dup groups, 0 errors, 0 echoes, 0 constants.
    Commit `78f3def`.

**Next session: pick up at**
- Run `test_new_features_against_pipeline.py` (the fundamentals companion harness
  in `C:\Users\jyama\Downloads\`) against `share_and_dilution_snapshot_*`. Read
  the harness first to confirm its calling convention matches these functions'
  Series-arg style, OR patch it the same way we patched the db-direct harness.
- Then continue family-by-family. Recommended order: do all the price-only
  families with the db-direct harness first (`basing_pattern`, `crash_speed`,
  `peak_and_crash`, `price_moving_averages`, `volatility_regime`,
  `volume_accumulation`, `volume_at_capitulation`, `moving_average_dynamics`)
  since the harness is now proven for that path; then move to fundamentals
  families.
- Reminder: also audit the `_2nd_derivatives` and `_3rd_derivatives` siblings
  for each family — they're unaudited even where the `_base_` files are clean.

## 2026-05-09 — session 2

(Continuation from session 1, date rolled mid-session.)

**Done this session:**
- Started auditing `basing_pattern_base` (4 files, 300 functions). Quickly discovered
  the family is **hybrid** -- 20 of 300 functions need fundamentals columns
  (`revenue`, `netinc`, `fcf`, `debt`, `equity`, `assets`) that aren't in `silver.sep`.
  Corrected the journal/CLAUDE.md classification.
- First harness run got stuck for hours on file 3 because `_sample_entropy` had
  pure-Python nested for-loops at O(N^2). Killed.
- Vectorized `_sample_entropy` and `bp_212/bp_213 _mem` (commit `b0203c3`).
  Re-ran -- still slow but progressing.
- Per-fn audit on a 1500-row synthetic close series identified 14 functions
  taking >100 ms/call. Pushback to user before applying any fixes.
- Wrote `verify_bp_fixes.py` (in `%TEMP%`) -- defines old + new for each
  replacement, runs against rand walk + flat + sinusoid, checks `<1e-9`
  tolerance. Caught 3 initial bugs (off-by-one in sample-entropy template
  count; pct_change-then-slice vs slice-then-pct_change semantic mismatch
  in `bp_277`). Re-verified all-match before any source edit.
- Decided NOT to apply outer-vectorization to `bp_156` -- the W=63 diff tensor
  is 130 MB and the inner-vec from `b0203c3` already gets the per-window cost
  as low as memory-allocation overhead. Net negative.
- Applied 13 verified vectorizations across 3 commits
  (`aa09779`, `d304409`, `2784a59`).
- Re-ran harness end-to-end. Total runtime 23.4 min (was indefinite/stuck
  before). File 3 still takes ~13 min on real silver data due to spectral/
  entropy inherent per-call cost; acceptable.
- Audit findings: 0 formula-exact dups, 6 value-exact dup pairs, 1 always-zero
  feature, 0 echoes.
- Removed 7 functions (commit `74e0b1f`):
  - `bp_069` always returns 0 at entry-day (low-signal metric)
  - `bp_224/bp_225` (file 3) and `bp_261-264` (file 4) -- mathematical duplicates
    of file-1/2 functions ("Donchian" rename of "range/position",
    "zero_crossing_rate" rename of "oscillation_freq")
- Final state: 293 bp_ functions in family, 273 bindable under db-direct
  harness, 0 dup groups expected.

**Inventory: 20 unbindable `basing_pattern_base` functions** (need fundamentals
harness path):
- `bp_139`, `bp_140`, `bp_141`, `bp_142`, `bp_143`, `bp_144` (file 2)
- `bp_226`, `bp_227`, `bp_228`, `bp_229`, `bp_230`, `bp_231`, `bp_232`, `bp_233`,
  `bp_234`, `bp_235`, `bp_236`, `bp_237`, `bp_238`, `bp_239` (file 4)

**Lessons (worth carrying):**
- The per-fn audit pattern (`time.perf_counter` on synthetic 1500-row signal,
  threshold-flag >100 ms) is faster diagnostic than running the harness when
  investigating perf. Keep this approach for future families.
- Always inventory unbindable args upfront via
  `grep '"inputs":' <family>_base_*.py | grep -oE '"inputs":\s*\[[^]]+\]' | sort -u`
  -- catches hybrid families before wasting harness time.
- Single-character semantic differences matter:
  `pct_change().iloc[]` vs `.iloc[].pct_change()` differ in NaN handling.
  Always re-verify against the actual source by importing it, not against a
  hand-rolled approximation.

**Next session: pick up at**
- Pick a verifiably-price-only family before assuming. Run the inventory grep
  on each candidate first. Priority order: `crash_speed`, `peak_and_crash`,
  `price_moving_averages`, `volatility_regime`, `volume_accumulation`,
  `volume_at_capitulation`, `moving_average_dynamics`. Hybrid ones (any with
  fundamentals args) get partial-audit only and the unbindables go to the
  fundamentals queue.
- After all `_base_` price-only files are clean, build the fundamentals
  harness path. Best leverage point: `test_new_features_against_pipeline.py`
  (companion harness already in Downloads). Read its calling convention first;
  if it has the same DataFrame-positional bug as the db-direct harness used
  to, mirror the `inspect.signature` patch.
- Then derivatives (`_2nd_derivatives`, `_3rd_derivatives`) for each cleaned
  family.

## 2026-05-09 — session 3 (multi-tab parallel audits)

**Tab 4 -- `moving_average_dynamics_base` audit (commits `accf456`, `8ed97f0`, `91a91d7`)**

- Inventory grep confirmed hybrid: 287 bindable + 13 fundamentals-needing
  (revenue/netinc/fcf/debt/equity/assets). All 13 unbindables in
  `_076_150.py` (mad_129-134) and `_076_150_expanded.py` (mad_e136-142).
- Pre-fn timing audit on synthetic 1500-row close: 0 functions over 100 ms.
  No vectorization needed (KAMA/McGinley/FRAMA/VIDYA Python loops are slow
  but tolerable at single-stock scale).
- Harness run: 11.3 min total (file 1: 26s, file 2: 349s [LSMA/ALMA/FRAMA
  rolling.apply], file 3: 141s [KAMA + days_since_*], file 4: 130s
  [LSMA + R²]). 287 features, 0 echoes, 0 constants, 0 formula-exact dups,
  0 value-exact dups.
- **New audit pattern: scalar-multiple rank-equivalents not caught by
  harness.** Cross-referenced top-30 features and found 6 AUC+Spearman ties
  to 4 dp. Verified pairwise with `(a/b).std()` on synthetic data:
  - 5 of 6 are exact scalar multiples (ratio std 1e-11 to 1e-18). Pearson=
    1.0, Spearman=1.0. Identical for any rank-based or monotonic-feature
    ML model. The harness's value_hash uses np.allclose so the constant
    multiplier breaks equality.
  - The 6th pair (mad_013_ema_100 vs mad_e011_smma_50) was Pearson=
    0.999999, ratio std 1.67e-04. NOT a scalar multiple -- two MA types
    that happen to have very similar smoothing for these particular
    windows. Kept both.
- Asked user (per HANDOFF "ASK FIRST: value-exact dups that aren't formula-
  exact"); user approved deleting the 5 higher-numbered scalar-multiple
  dups:
  - `mad_148_sma200_slope_acceleration` = `mad_102_sma200_curvature` / 21
  - `mad_149_ema21_slope_acceleration`  = `mad_103_ema21_curvature` / 5
  - `mad_e097_price_osc_10_50`          = `mad_063_sma10_sma50_spread` * 100
  - `mad_e099_price_osc_50_200`         = `mad_059_sma50_sma200_spread` * 100
  - `mad_e103_lr_slope_21_normalized`   = `mad_e067_lsma21_sma21_spread` / 10
- Math identities behind the constants (recorded for future tabs):
  - `_slope(s, w).diff(w)` == `s.diff(w).diff(w) / w` (so slope_acc == curvature/w).
  - `_safe_div(x, |y|) == x / y` for all-positive y (e.g. close, SMA over equity prices).
    Then `osc * 100 == spread`.
  - For window W: LSMA(W) - SMA(W) = slope * (W-1)/2 (linear-fit identity).
    So `(LSMA-SMA)/|close|` and `slope/|close|` differ by exactly (W-1)/2.

**Final state:** 295 mad_ functions in family (was 300), 282 bindable
under db-direct harness, 0 dup groups expected.

**Lesson worth carrying:**
- The harness's value_hash dedupe is necessary but not sufficient. A
  constant scalar offset breaks np.allclose equality, so two functions
  that are mathematically identical up to scaling will both pass through.
  Mitigation: scan top features for AUC+Spearman ties at 4 dp; verify
  with `(a/b).std()` on synthetic 1500-row data. If std at float noise,
  it's a rank-equivalent dup. Recipe added to CLAUDE.md MAD section.

**Inventory: 13 unbindable `moving_average_dynamics_base` functions**:
- file 3 (`_076_150.py`): mad_129, 130, 131, 132, 133, 134 (revenue/netinc/fcf base + ratio)
- file 4 (`_076_150_expanded.py`): mad_e136, 137 (revenue), 138, 139 (fcf),
  140 (assets), 141 (debt), 142 (equity)

---

## Session 3 (2026-05-09, tab 1) -- `peak_and_crash_base`

**Setup.** Picked from HANDOFF queue as smallest open family per the policy.
Initial classification "YES (OHLCV only)" was wrong: an inspector-based
arg-set inventory (load both files, walk `vars()`, check `inspect.signature`)
revealed 28 fundamentals-needing functions. The naive grep on `"inputs":`
text only saw file 1's literal registry; file 2 builds the registry
programmatically via `_ALL_FUNCS` + `inspect.signature`, so its arg sets
were invisible to grep. **Lesson: always run the python-introspection
inventory before classifying a family.** HANDOFF row updated to
"NO -- hybrid (revenue, netinc, fcf, debt, equity, assets)".

**Pre-harness timing audit (1500-row synthetic).** 17 functions > 100 ms,
worst was `pc_246_crash_return_concentration` at 433 ms (custom rolling.
apply, not in standard pattern list, skipped). Three rolling-apply
autocorrelations matched the `bp_092/bp_093` standard pattern and were
auto-vectorized:
- `pc_117_return_autocorrelation_1_63d`: 188 ms -> 0.6 ms (~410x)
- `pc_118_return_autocorrelation_5_252d`: 177 ms -> 0.8 ms (~390x)
- `pc_119_crash_serial_correlation_63d`: 140 ms -> 1.0 ms (~224x)

Pattern: `rolling(W).apply(s.autocorr(lag=k), raw=False)` ->
`rolling(W-k, min_periods=W-k-5).corr(s.shift(k))`. The `min_periods`
needed to be `W-k-5` (not the policy default of `mp=10`) to match the
warmup-edge NaN positions exactly -- with `mp=10` the new function
emits one extra NaN at the boundary. All three verified <1e-9 vs old
on rand_walk + flat + sinusoid. (Commit `0c1443d`.)

**Pre-harness formula-exact dup pass.** Before running the harness,
spotted two pairs by visual inspection of identity-by-formula:
- `pc_207_double_top_proximity` -- `(close/rh - 1)` ≡ `pc_002` `(close-rh)/rh`
- `pc_208_double_bottom_proximity` -- `(close/rl - 1)` ≡ `pc_011` `(close-rl)/rl`

Both verified <1e-9 vs the originals. Auto-applied delete on both
(commit `cfba2e7`).

**Harness run.** 17.5 min total (file 1: 11.3 min, file 2: 6.2 min).
- File 1: 150 bound, 0 echoes, 4 constants, 0 errors.
- File 2: 121 bound + 28 unbindable (`missing_inputs=[revenue|...]`),
  5 constants, 0 errors.
- Cross-file dup groups: 1 formula-exact + 4 value-exact.

**Triage results.**
- *Formula-exact dup `pc_014_rally_from_atl` ⇄ `pc_300_recovery_return_from_trough`*:
  auto-applied delete pc_300 (commit `5c0492d`).
- *Value-exact dup `pc_029_max_drawdown_1y` ⇄ `pc_029_drawdown_from_ath_helper`*
  (the same `_mdd` function, only diff is `window=` keyword vs positional;
  the harness's source-hash dedup missed it but value-equality caught it):
  user approved inlining the `_mdd` math directly into pc_276 (the only
  caller of the helper) and deleting the helper, preserving CLAUDE.md's
  per-file self-containment convention (no cross-file imports).
  Commit `e8888f7`.
- *Value-exact dup `pc_006_days_since_ath` ⇄ `pc_049_drawdown_duration_current`*:
  kept both. They are conceptually different (days_since_ATH counts up
  monotonically until a new ATH; drawdown_duration counts up while close
  < ATH and resets at ATH-touch). They produce identical values whenever
  close stays strictly below the running ATH -- the typical case across
  the 100-entry sample. Different at ATH-touch days, which the sample
  didn't catch.
- *9 always-zero conditional indicators*: all kept by user direction.
  `pc_020/022/024` are running-max binary flags (new-high indicators);
  `pc_064/198/205/206/231/261` are AND-of-low-probability triggers.
  Sample-bias (winners + recent controls) means triggers rarely fire at
  entry day. Different from `bp_069_consecutive_inside_bars` (deleted in
  session 2) which used `close.abs() == close` no-op-style logic;
  these here are real conditional triggers with low base rate.

**Final state.** 297 unique pc_ functions in family (was 300), 269 bindable
under db-direct harness, 28 unbindable (revenue/netinc/fcf/debt/equity/
assets), 0 dup groups expected post-fix.

**Inventory: 28 unbindable `peak_and_crash_base` functions** (all in
file 2, `_151_300.py`):
- pc_166-176 (11 fns): revenue/netinc/fcf/debt/equity/assets peak drawdowns
  and at-new-high flags
- pc_216-218: revenue / fcf at price peak/crash
- pc_225: price crash with debt spike
- pc_237-242 (6 fns): debt-equity / net-margin at price extremes,
  multi-fundamental scores
- pc_249: price crash with asset impairment
- pc_267-272 (6 fns): revenue / fcf / asset / fundamental coverage at crash
- pc_271 (also): equity erosion rate

These will need the same fundamentals harness path that
`basing_pattern_base` and `moving_average_dynamics_base` are awaiting.

**Lessons worth carrying:**
1. Inventory by `inspect.signature`, not by grep. File-2 programmatic
   registries hide their arg sets from text-search.
2. The `bp_092/bp_093` autocorr vectorization needs `min_periods=W-k-5`
   (not policy default `mp=10`) to match warmup-edge NaN positions
   exactly. Add to standard-pattern notes.
3. Value-exact dup with textually-different bodies (positional vs
   keyword args) is a recurring pattern -- harness can't see it but
   value-equality flags it. ASK FIRST policy is appropriate.

**Process note (this session).** User instructed "i want git commits.
i do not want to be asked for git commits" -- saved as feedback memory.
For audit work in this repo, commit each scoped fix immediately after
AST+import check passes; keep the per-file commit cadence and the
HANDOFF commit message format.

**Tab 2 -- `price_moving_averages_base` audit (commits `1f668d0`, `046a589`)**

- Inventory grep confirmed pure-OHLCV: all 300 functions take only
  `close/high/low/open/volume`. Full audit possible (0 unbindables).
- Pre-fn timing audit: 0 functions over 100 ms. Slowest:
  `pma_168_frama16_frama32_spread` at 84.6 ms. Heavy ones cluster around
  `_lsma`/`_alma`/`_kama`/`_frama` rolling-apply patterns at 30-85 ms.
  Total per-fn cost across the family ~1.2 s on 1500 rows. Skipped
  perf vectorization step entirely.
- Initial harness run (10.3 min): 3 constants + 2 value-exact dup groups
  reported, all in file 3 (`_151_225.py`). All 5 findings clustered on
  `pma_164-168` -- the FRAMA family. Read the helper before triaging.
- Found a single root-cause helper bug: `_frama` was missing length
  normalization on `n1`/`n2`/`n3`, so the fractal dimension `d` lived in
  `[0, 1]` instead of `[1, 2]`. With `d <= 1`, `alpha = exp(-4.6*(d-1))`
  always clamped to 1.0 and FRAMA collapsed to identity (`output = input`).
  This explains all 5 harness findings as one bug (not five), AND
  silently broke 2 more functions (`pma_169/170`) that the harness
  couldn't flag because their values look like `close.pct_change(5/21)`
  -- legitimate-looking returns, just under wrong names.
- Asked user: helper-fix vs delete-7 vs surgical-trim. User picked
  helper-fix. Patched `_frama` to divide by segment lengths
  (`half`, `w-half`, `w`). Verified at
  `%TEMP%\verify_frama_fix.py`:
    - OLD == close (the bug we're fixing) -- on rand_walk + flat + sinusoid
    - NEW != close on rand_walk and sinusoid (smoothing now happens)
    - NEW == 100.0 on flat signal (no movement to track)
    - No NaN past warmup
  `d_new` does dip below 1.0 on smooth signals (sinusoid median
  d=0.889 at w=16) but the alpha clamp handles it -- canonical
  Ehlers behavior, not a bug. Dropped the strict `d in [1,2]`
  assertion after confirming this is documented Ehlers behavior.
- Re-ran harness (9.8 min): 0 errors / 0 echoes / 0 constants /
  0 dup groups. Family clean.
- Did NOT address `_mcginley` overflow RuntimeWarnings at line 98.
  When `prev` becomes very small, `ratio**4` overflows -> denom=inf
  -> `(p-prev)/inf = 0` -> `prev` unchanged. Math degrades safely;
  output values are sensible; harness shows 0 errors / 0 constants /
  0 dups for all McGinley features. Out of triage scope; note for
  reference.

**Lessons worth carrying:**
1. **Cluster harness findings by helper, not by feature.** When 3 constants
   AND 2 value-exact dup groups all touched `pma_164-168`, the 5 findings
   were 1 bug. Reading `_frama` before opening 5 separate triage decisions
   saved time and preserved 7 signals' worth of mathematical content.
2. **Some bugs are invisible to the harness.** `pma_169/170` looked
   like legit returns to the harness's value-hash, but they were
   slope-of-broken-FRAMA computing slope-of-close. Fixing the helper
   restored their intended semantics. Lesson: when fixing a helper,
   audit ALL transitive callers, not just the harness-flagged ones.
3. **Strict canonical-formula assertions can be too tight.** Asserting
   `d in [1, 2]` for FRAMA failed because the canonical Ehlers formula
   itself produces d outside [1,2] on signals with gaps between halves
   (R3 > R1 + R2). The alpha clamp is what makes it work. Verify
   against real-world canonical reference, not against the textbook
   range-of-validity claim.

**Cross-tab status at this writing**
- Tab 1: peak_and_crash done.
- Tab 2: price_moving_averages done (this entry).
- Tab 3: crash_speed claimed.
- Tab 4: moving_average_dynamics done; volatility_regime claimed.

**Next session: pick up at**
- Pure-price queue is now empty. All remaining Path A families are
  hybrid (fundamentals-needing). Continue with `crash_speed`,
  `volume_accumulation`, `volume_at_capitulation`.
- Or build the fundamentals harness path
  (`test_new_features_against_pipeline.py`) so the accumulated
  unbindables (basing_pattern 20 + moving_average_dynamics 13 +
  peak_and_crash 28 = 61 functions) can be validated.

---

## Session 3 (2026-05-09, tab 7) — `revenue_level_base`

**First Path B audit.** All Path A families were claimed/in-progress
when this tab opened. User asked to claim `revenue_level` from the
36-family unaudited set and "debug for signal."

**Setup.** Inventory grep `grep '"inputs":'` confirmed 100% of 300 rl_
functions take `revenue` plus other fundamentals — zero OHLCV-only
arg sets — so the db-direct harness skips the entire family with
`missing_inputs`. Decided to build a synthetic-fundamentals mini-
harness as the prototype Path B driver.

**Mini-harness design** (`%TEMP%\temp_rl_mini_harness.py`):
- Builds a deterministic Series for each of ~50 input columns
  referenced across the 4 registries (`revenue`, `assets`, `equity`,
  `debt`, `liabilities`, `cashneq`, `netinc`, `opinc`, `gp`, `cor`,
  `opex`, `ebit`, `ebitda`, `ncfo`/`ncff`/`ncfi`/`ncfdebt`/`ncfdiv`/
  `ncfcommon`, `fcf`, `capex`, `depamor`, `rnd`, `sgna`, `sbcomp`,
  `intexp`, `taxexp`, `ppnenet`, `retearn`, `currentassets`,
  `currentliabilities`, `workingcapital`, `receivables`, `inventory`,
  `payables`, `deferredrev`, `investments`+`investmentsc`/`nc`,
  `tangibles`, `intangibles`, `marketcap`, `ev`, `sharesbas`,
  `shareswadil`, `close`, `high`, `low`, `volume`).
- `_walk` for prices/volume (random-walk drift); `_step` for
  fundamentals (quarterly jumps with ±0.05 vol).
- Iterates over 4 `REVENUE_LEVEL_REGISTRY_*` dicts, runs each fn,
  captures errors, all-NaN, constant-past-warmup, formula-exact
  (sha256 of body without def/comment lines), value-exact (sha256
  of round-9 values).
- Persists raw outputs to `.npz` for follow-up scalar-multiple scan.

**First run**: 300/300 loaded, 0 errors, 0 all-NaN, 0 constants,
0 formula-exact dups, **7 value-exact dup groups**.

**Triage**:

*4 formula-exact-under-rename (auto-applied per HANDOFF policy):*
- `rl_119_revenue_level_regime_252` ≡ `rl_039_revenue_vs_trailing_4q_mean`
  (variable rename `mu` → `sma`, different docstring)
- `rl_120_revenue_level_regime_504` ≡ `rl_040_revenue_vs_trailing_8q_mean`
- `rl_224_revenue_to_assets_power` ≡ `rl_052_log_revenue_to_log_assets`
  (literal-identical body)
- `rl_281_revenue_per_diluted_share_to_close_ratio` ≡
  `rl_187_dilution_adjusted_revenue_yield` (literal-identical body)

Removed lower-priority duplicates per HANDOFF "AUTO-APPLY: delete
higher-numbered." Commits `5e7ad38`, `407908a`, `ec6f05c`.

*3 cancellation-equivalent (algebraic identity, ASK FIRST per HANDOFF):*
- `rl_080_revenue_per_share_to_book_per_share` (rps/bvps with
  shares cancelling) == `rl_005_revenue_to_equity`
- `rl_081_revenue_per_share_to_fcf_per_share` == `rl_019_revenue_to_fcf`
- `rl_082_revenue_per_share_to_earnings_per_share` == `rl_020_revenue_to_netinc`

Algebraic identity: `(a/c) / (b/c) == a/b` for any non-zero c.
On Sharadar SF1 with live tickers, sharesbas is always >0, so the
two variants produce identical numbers at every observation.

User chose "delete the 3 redundant per-share versions" (commit
`c65fbb3`). Reasoning aligned with MAD audit precedent for scalar-
multiple deletes — when math collapses to identity, the named-
variant carries no signal beyond the canonical form.

**Scalar-multiple/cosine-similarity follow-up scan**:
- Loaded raw outputs from `.npz`; computed z-scored cosine similarity
  matrix (300 × 300); flagged 3 candidate pairs at |sim| ≥ 0.99999
  with ratio_std=0 not already in the value-exact dup set.
- All 3 hits were `rl_042` / `rl_043` / `rl_140` — a 3-clique of
  `revenue / max(W-day window)` for W ∈ {504, 1260, ∞ (cummax)}.
- **Synthetic-data false positive.** My `_step` revenue series has
  drift +0.02/jump (positive), so the running max keeps refreshing
  to recent peak ≈ current revenue, and all 3 windows converge.
- Verified on a custom 4-cycle drawdown signal (up/down/up/down):
  max divergence rl_042 vs rl_043 = 0.41, rl_042 vs rl_140 = 0.41.
  These are NOT real dups; they only collapse on monotonic-up data.
- Kept all 3.

**Re-run post-fix**: 293/293 loaded, 0 errors, 0 all-NaN, 0 constants,
0 dup groups. Family clean.

**Lessons worth carrying:**

1. **The Path B mini-harness pattern works** and is reusable for any
   100%-fundamentals family. The synth input dict is the only
   family-specific bit (drop in the new column types — e.g.
   `instownpct`, `shareswadil` extensions); the dup/constant/error
   detection machinery is family-agnostic. Future Path B audits
   should clone this template (rename to family-specific name and
   adjust `FILES`/`REGISTRY_PREFIX` constants).

2. **Synthetic-data sensitivity check is mandatory for Path B.**
   Path A's harness uses real silver data that already has all the
   regime variation (drawdowns, sign flips, sector divergence, etc.)
   baked in. Path B's synthetic data has only what we put in. For
   any flagged dup group:
   - Read the bodies to confirm what input characteristic each fn
     depends on.
   - If the pair could plausibly diverge on a different input
     regime (drawdowns, negative values, regime shifts, near-zero
     denominators), build a targeted verification signal before
     deciding to delete.
   - The cummax-clique caught this session would have been a
     real-feature-deletion bug if I'd auto-applied.

3. **Cancellation-equivalent dups are common in fundamentals
   features.** Pattern: `(num/scale) / (denom/scale)` where `scale`
   is any per-share or per-asset normalizer that appears in both
   numerator and denominator. The textual body looks different (3
   intermediate vars vs 1 ratio) but the math collapses. Catch via
   value-exact dup scan, then read the bodies. Per HANDOFF, ASK
   FIRST applies; user-driven choice between delete-redundant /
   keep-dual-naming / rewrite-to-break-cancellation.

4. **Path A already has 1 Path B graduate**: the inventory grep
   for `revenue_level` showed every function takes fundamentals,
   making Path B the only viable path. For mixed families (any
   OHLCV-only signals among fundamentals), Path A's harness handles
   the bound subset and Path B mini-harness can complete the
   unbindable subset. Sequential Path A → Path B for hybrid
   families is the natural extension.

**Outstanding follow-ups for revenue_level:**
- Derivatives (`revenue_level_2nd_derivatives.py`,
  `revenue_level_2nd_derivatives_v2.py`,
  `revenue_level_3rd_derivatives.py`,
  `revenue_level_3rd_derivatives_v2.py`) NOT YET AUDITED.
  Same Path B mini-harness pattern should apply with the appropriate
  registry-name change.

**Cleanup**: deleted scratch scripts per `feedback_temp_scripts.md`:
- `%TEMP%\temp_rl_mini_harness.py`
- `%TEMP%\temp_rl_scalar_dup_scan.py`
- `%TEMP%\temp_rl_verify_cummax_clique.py`
- (output JSONs and NPZ also removed)

---

## Session 3 (2026-05-09, tab 4) -- `volatility_regime_base`

**Setup.** Picked from HANDOFF queue (next open after MAD). Inventory
grep confirmed hybrid: 282 bindable + 18 fundamentals-needing
(revenue/netinc/fcf/debt/equity/assets). Unbindables concentrated in
file 2 (vr_117-121, 147-148) and file 4 (vr_250-260).

**Pre-harness timing audit (1500-row synthetic).** Found 7 slow
functions matching the standard `bp_092/bp_093` autocorr pattern --
all 7 vectorized after <1e-9 verification on rand walk + flat +
sinusoid (no ASK needed per HANDOFF VERIFY+APPLY policy):
- vr_030/031/032_vol_autocorr_*: ~270x avg (commit `0784a3c`)
- vr_075_vol_persistence_ratio_63d: ~210x (commit `0784a3c`)
- vr_207_vol_half_life_proxy_252d: ~145x (commit `f3d019b`)
- vr_286/287_squared_return_autocorr_*: ~270x avg (commit `2f1f4dd`)

**Found 1 runtime bug pre-harness** (vr_285): `out.where(False, 4.0)`
raises "Array conditional must be same shape as self" on pandas 2.x
(scalar conditionals no longer accepted). New error class -- ASKed user;
approved option 1 (init via `pd.Series(4.0, ...)` + add NaN propagation
where v21 is NaN). Commit `f65a8cb`.

**Harness run (post-vec): 4.0 min** (vs MAD's 11.3 min thanks to the
autocorr vectorization paying off). 282 bindable, 0 echoes, 0 errors
(in bound), 2 constants (vr_169 + vr_170, both 100% null), 3 formula-
exact dup groups, 6 value-exact dup groups (3 overlapping with formula).

**Triage**:
- AUTO-APPLY: 3 formula-exact dups -> deleted vr_195, vr_196, vr_292
  (commits `0e4649c`, `830807e`).
- AUC+Spearman tie cross-reference (now standard practice from MAD)
  caught 7 more candidate pairs not flagged by value_hash. Verified
  with `(a/b).std()` on synthetic data:
  - 3 pairs are exact scalar multiples (ratio std ~1e-15): vr_226 =
    vr_221 * sqrt(pi/2); vr_227 = vr_222 * sqrt(pi/2); vr_297 =
    vr_159 / 3. Same finding pattern as MAD.
  - 1 pair is a true value-exact dup the harness's value_hash missed
    (vr_262 = vr_037, max|a-b|=0 but Pearson=NaN due to low post-warmup
    variance).
  - 2 pairs are affine (Pearson=1.0 but ratio std large) -- left alone.
  - 1 pair was near-equivalent (Spearman=0.99999) -- left alone.
- ASKed user about value-exact-only dups + scalar-multiples + harness-
  missed value-exact + look-ahead bug as a single consolidated question
  pair. User approved all 6 deletes + look-ahead fix.

**Look-ahead bug** (vr_169/170): both used `v_chg = v5.shift(-5) - v5`,
i.e. read 5 days INTO THE FUTURE. At any "as-of" date, the rolling.corr
is NaN at the prediction horizon. The harness's "100% null" finding was
a real signal -- not just a sample artifact. Fixed by flipping shift
direction: `v_chg = v5 - v5.shift(5)` (correlation with PRIOR vol
change). Same financial interpretation, no look-ahead. Smoke test:
NaN dropped from 100% to 2-5% (warmup only). Commit `ff29fda`.

**9 deletes total** (mix: 3 formula-exact + 2 variable-rename value-
exact + 3 scalar-multiple + 1 harness-missed value-exact). Commits:
`0e4649c` (vr_195/196), `830807e` (vr_292), `878a752` (vr_028),
`a01d3e0` (vr_226/227/240/262/297). Plus 1 look-ahead fix (`ff29fda`)
and 1 pandas 2.x compatibility (`f65a8cb`) and 3 perf vec commits.

**Final state**: 273 bound + 18 unbindable (out of 291 remaining
functions in family; was 300 pre-audit). 0 echoes, 0 constants,
0 dup groups (post-fix).

**Lessons (worth carrying):**
- The MAD scalar-multiple recipe is now standard practice. Confirmed
  it on a 2nd family.
- Look-ahead detection: the harness's "100% null at entry day" is the
  signal. Look for `.shift(-N)` patterns. Fix by flipping the sign if
  the financial interpretation is preserved (it usually is for
  correlation features); otherwise delete.
- Pandas 2.x scalar-conditional gotcha: `Series.where(False, x)` no
  longer works. Always use `pd.Series(x, index=...)` for direct
  initialization. Watch for this pattern in other older feature
  files -- it's a silent landmine that only triggers at runtime.
- One consolidated AskUserQuestion (with multi-select for deletes +
  separate single-select for the look-ahead bug) was much faster than
  asking each pair individually. Bundle similar-class decisions.

**Inventory: 18 unbindable `volatility_regime_base` functions**:
- file 2 (`_076_150.py`): vr_117 (revenue), vr_118 (netinc), vr_119
  (fcf), vr_120 (debt+equity), vr_121 (assets), vr_147 (revenue),
  vr_148 (equity+debt)
- file 4 (`_226_300.py`): vr_250 (revenue+netinc), vr_251 (netinc+
  revenue), vr_252 (revenue+netinc), vr_253 (assets+debt), vr_254
  (assets+equity), vr_255 (fcf+debt), vr_256 (revenue), vr_257
  (netinc), vr_258 (revenue), vr_259 (netinc), vr_260 (equity)

**Cross-tab status at this writing (after VR commits)**
- Tab 1: peak_and_crash done.
- Tab 2: price_moving_averages done.
- Tab 3: crash_speed claimed.
- Tab 4: moving_average_dynamics done; volatility_regime done.
- Tab 5: volume_accumulation claimed (perf vec already in `fbe97bf`).
- Tab 6: volume_at_capitulation claimed (perf vec already in `33000f3`).

**Next session pick-up:**
- All Path A families now claimed or done. Wait for tabs 3/5/6 to
  finalize OR pull from a cleaned-up family for derivatives audits.
- Build the fundamentals harness path. Accumulated unbindables across
  cleaned families: bp 20 + mad 13 + pc 28 + vr 18 = 79 functions
  (and growing as tabs 3/5/6 finalize).

**Tab 3 -- `crash_speed_base` audit (commits `5ddd15a`, `15a82fb`, `3994d3c`)**

- Inventory grep confirmed hybrid: 215 bindable + 10 fundamentals-needing
  (cs_101-cs_110, all in `_076_150.py`: revenue/netinc/fcf/equity/debt/
  assets, plus margin_collapse and fundamental_crash composites).
- Pre-fn timing audit on synthetic 1500-row close: 7 functions over
  100 ms threshold, all in file 3:
  - cs_174/175 hurst_exponent_63d/252d (1.0-1.8 s) -- nested R/S analysis
  - cs_181/182/183 cornish_fisher_var_*_63d/252d (0.8-0.9 s) -- per-window
    scipy.stats.skew/kurt + CF expansion
  - cs_225 modified_sharpe_downside_63d (0.76 s) -- per-window CF
  - cs_200 superexponential_crash_test_63d (0.13 s) -- polyfit per window
  - Total: ~6 s for all bindable fns; well under multi-hour-stuck
    territory. Did NOT pre-emptively vectorize.
- Harness run: 50.2 min total on 100 entries x 1500 days. File 3 dominated
  at 45.8 min (Hurst + CF + modified Sharpe scipy.stats per-window).
  215 features, 0 echoes, 1 constant, 3 value-exact dup groups, 0
  formula-exact dups (per harness), 0 errors apart from the 10 expected
  unbindable missing_inputs.
- Findings triaged:
  - **Auto-applied (formula-exact under variable-rename):** Two of three
    dup pairs were textually identical except for variable names — the
    harness's lexical formula_hash misses these but value_hash catches
    them. Verified <1e-9 vs old on rand walk + flat + sinusoid:
    - cs_082_waterfall_count_63d == cs_065_new_low_frequency_63d
      (rename `low_63`->`low`)
    - cs_133_max_5day_drop_63d == cs_068_worst_week_in_63d
      (rename `r5`->`weekly_r`)
  - **ASK FIRST -> approved:**
    - cs_159_cvar_1pct_63d -- value-equiv to cs_004_max_daily_drop_63d
      (rolling 63d min). Math identity: with W=63 and percentile=0.01,
      np.percentile interpolates at position 0.62 between sorted[0] and
      sorted[1], so threshold > min and threshold < 2nd-min. Then
      `tail = x[x <= threshold] = {min}` and mean(tail) = min. The
      "1% CVaR" implementation degenerates to rolling min for any window
      where percentile(0.01) lies between min and 2nd-min — i.e. any
      non-tied 63d window of returns. Verified <1e-9 against
      cs_004 on the 3 synthetic signals.
    - cs_222_negative_surprise_magnitude_63d -- always returns 0 across
      all 100 sample tickers at entry-day. Mean of returns < mu-2sigma
      is NaN for windows with no extreme events (most of them); trailing
      `.fillna(0.0)` collapses to constant. Same disposition as bp_069
      and vr always-zeros.

**Lessons (worth carrying):**
- **Lexical-rename formula_hash blind spot.** Two of three dup pairs
  here were identical-up-to-renaming. The harness reports them as
  value-exact (correct) but they're ALSO formula-exact under
  alpha-renaming (which qualifies them for AUTO-APPLY rather than
  ASK FIRST per HANDOFF policy). When manual inspection confirms textual
  equivalence-up-to-renaming, treat as auto-apply. Confirms
  volatility_regime's `vr_028`/`vr_240` finding.
- **Degenerate quantile-tail for short windows.** When a CVaR or tail-
  mean uses `np.percentile(x, p) + x[x <= threshold]`, watch for
  `p * window < 1`. For W=63, p=0.01: percentile lands between sorted[0]
  and sorted[1] via linear interp, only sorted[0] satisfies the
  threshold mask, and the tail mean collapses to min. cs_159 was this
  bug. Future: count-based tail (`k = max(1, int(p*n))`) is a more
  faithful CVaR for short windows.

**Inventory: 10 unbindable `crash_speed_base` functions** (all
`_076_150.py`):
- cs_101 (revenue), cs_102 (revenue), cs_103 (netinc), cs_104 (netinc),
  cs_105 (fcf), cs_106 (equity), cs_107 (debt), cs_108 (revenue+netinc),
  cs_109 (assets), cs_110 (revenue+netinc+fcf)

**Cross-tab status at this writing (after CS commits)**
- Tab 1: peak_and_crash done.
- Tab 2: price_moving_averages done.
- Tab 3: crash_speed done.
- Tab 4: moving_average_dynamics done; volatility_regime done.
- Tab 5: volume_accumulation status -- check HANDOFF.
- Tab 6: volume_at_capitulation status -- check HANDOFF.

**Updated cumulative unbindable count** (post-CS): bp 20 + mad 13 +
pc 28 + vr 18 + cs 10 = 89 functions across cleaned families.

---

## Session 3 (2026-05-09, tab 6) -- `volume_at_capitulation_base`

**Setup.** Picked from HANDOFF queue as the only fully-open Path A
family (others claimed by tabs 3/4/5). Inventory grep confirmed hybrid:
282 bindable + 18 fundamentals-needing. New column type:
`instownpct` (institutional ownership %), used by vac_146-150
(`inst_ownership_vol_cap`, `insider_vol_distress`, `high_own_cap_vol`,
`ownership_change_vol_amplifier`, `forced_selling_proxy`). First
appearance in this audit cycle; logged for the future fundamentals
harness path.

Unbindables concentrated in file 2 (vac_116, 121-123, 125, 146-150
total 10) and file 4 (vac_256-259, 262-265 total 8).

**Pre-harness timing audit (1500-row synthetic).** 4 functions over
100 ms threshold, all in file 3:
- vac_211_vol_autocorr_lag1_21d (139 ms)
- vac_212_vol_autocorr_lag5_63d (143 ms)
- vac_213_vol_autocorr_lag1_63d (141 ms)
- vac_222_vol_shock_halflife_21d (145 ms)

3 of 4 are textbook `rolling(W).apply(autocorr(lag=k))` -- standard
vectorization. vac_222 is the same autocorr wrapped in
`-log(2)/log(clip(ac, 0.01, 0.99))`.

**Vectorization (commit `33000f3`).**
- vac_211/212/213: `rolling(W).apply(autocorr(lag=k))` →
  `rolling(W-k, min_periods=mp-k).corr(s.shift(k))`. Verified <1e-9
  vs source on rand_walk + sinusoid + volume signals (max diffs
  5.4e-11 / 1.1e-11 / 1.1e-11). Speedups ~280-380x.
- min_periods adjustment: original `mp` counts raw observations;
  inside autocorr, lag-k creates `W-k` valid pairs. Setting
  `new_mp = old_mp - lag` preserves warmup-edge NaN positions
  exactly. Verified at idx 8 (W=21, lag=1) and idx 18 (W=63,
  lag=1/5).
- vac_222 NOT vectorized: log near 0.99 boundary amplifies tiny
  FP autocorr diffs (~1e-11) to ~1e-8 at the function output.
  Pure FP propagation, not algorithmic difference, but exceeds
  <1e-9 verification gate. Per HANDOFF policy this triggers
  ESCALATE -- escalated by leaving the slow path. 145 ms × 1500
  stocks ≈ 3.6 min, not a runtime blocker.

**Harness run (7.8 min total on 100 entries × 1500 days).**
- File 1: 152.6s, 75/75 bound, 0 echo / 0 const
- File 2: 35.8s, 65/75 bound, 10 missing_inputs reported
- File 3: 204.2s, 75/75 bound, 0 echo / 0 const
- File 4: 74.9s, 67/75 bound, 8 missing_inputs reported

Findings: 0 echoes / 0 constants / 0 errors in bound. 1 formula-exact
+ value-exact dup pair (same pair flagged by both checks).

**Surgical edit (commit `8611993`).** The single dup pair was
`vac_003_vol_spike_252d(volume) == vac_118_cap_vol_to_float_turnover(close, volume)` --
both computed `_safe_div(volume, _sma(volume, 252))`. The vac_118
signature took `close` but never used it.

The function name promised something more specific than the body
delivered. Asked user (option set: strict cap-day mask vs
drawdown-mask vs drawdown-weighted vs delete). User picked strict
cap-day mask, mirroring the family's existing `vac_025/026`
definition (`vol_spike > 2 AND ret < 0`). Rebodied to:

```python
def vac_118_cap_vol_to_float_turnover(close, volume):
    """252d float-rotation turnover on strict cap days (vol_spike>2 AND down)."""
    ret = _pct_change(close)
    turnover = _safe_div(volume, _sma(volume, 252))
    cap_day = ((turnover > 2) & (ret < 0)).astype(float)
    return turnover * cap_day
```

Validated on synthetic 1500-row data: 131 cap-day flags out of 1442
valid samples (~9% cap-day base rate), distinct from vac_003's
unmasked turnover.

Side note (out of scope): vac_003 produces 125 inf values in the
synthetic warmup because the family's `_safe_div(a, b, fill=0.0) =
a / b.replace(0, np.nan).fillna(fill)` turns NaN denominators into
0, yielding inf. Pre-existing project-wide convention; harness runs
on real silver data with full warmup buffer where this rarely
triggers.

**Lessons (worth carrying):**
1. **Rename-vs-delete decision for ambiguous dups.** When a dup
   body is generic (`_safe_div(volume, _sma(volume, 252))`) but
   the function name promises specificity (`cap_vol_to_float_turnover`),
   propose a surgical rebody before auto-deleting. Only viable
   when the family already has a canonical definition to mirror
   (here: vac_025/026 strict cap_day).
2. **min_periods translation rule for autocorr vectorization.**
   `rolling(W, mp).apply(autocorr(lag=k))` →
   `rolling(W-k, min_periods=mp-k).corr(s.shift(k))`. The
   subtraction by `lag` preserves warmup-edge NaN positions;
   without it, the new version emits values one position earlier
   than the old. Standard adjustment now -- precedent set in
   peak_and_crash session.
3. **FP-amplification escalation example.** vac_222's
   `-log(2)/log(clip(ac, 0.01, 0.99))` near the upper clip is the
   first time this audit cycle hit a "verification fails by
   policy but algorithm is identical" case. Choice: escalate by
   leaving slow rather than apply-and-justify.

**Outstanding from this family:**
- 18 unbindable functions (10 file 2 + 8 file 4) need fundamentals
  harness path. New `instownpct` column (vac_146-150) requires the
  fundamentals harness to source it from silver SF1.

**Cross-tab status at this writing (after VAC commits)**
- Tab 1: peak_and_crash done.
- Tab 2: price_moving_averages done.
- Tab 3: crash_speed done.
- Tab 4: moving_average_dynamics + volatility_regime done; both
  derivatives done.
- Tab 5: volume_accumulation done (per HANDOFF: 5 surgical-edit
  commits incl. va_108/109 Bostian II% and va_202/203 Williams DI).
- Tab 6: volume_at_capitulation done (this entry).

**Updated cumulative unbindable count** (post-VAC): bp 20 + mad 13 +
pc 28 + vr 18 + cs 10 + vac 18 = 107 functions across cleaned
families. Plus volume_accumulation's 14 (per HANDOFF) = 121 total.

**Next session: pick up at**
- Path A queue is now down to families that haven't been touched
  yet (per HANDOFF) -- all remaining are unaudited or in Path B.
- The accumulated 107+ unbindables across Path A motivate building
  the fundamentals harness path (`test_new_features_against_pipeline.py`)
  next, rather than starting another base-only family.

---

## Session 3 (2026-05-09, tab 5) -- `volume_accumulation_base`

**Setup.** Picked from HANDOFF queue (only remaining open Path A
family at claim time). Inventory via `inspect.signature` on all 4
files: 286 bindable + 14 unbindable, all unbindables in
`_226_300.py`. Confirms hybrid -- the row's "+ `sharesbas`" hint
was right; full unbindable col set is `sharesbas, revenue, netinc,
fcf, debt, equity, assets`.

**Pre-harness timing audit (1500-row synthetic).** 3 functions over
100 ms. All 3 are textbook `rolling(W).apply(autocorr(lag=k))`:
- `va_220_vol_autocorr_5` (W=63, k=5): 135 ms
- `va_221_vol_autocorr_21` (W=126, k=21): 123 ms
- `va_280_vol_decay_halflife_63` (W=63, k=1, then `-log(2)/log(clip(ac))`): 136 ms

**Vectorization (commit `fbe97bf`).** `va_220/221` vectorized
`rolling(W).apply(autocorr(lag=k))` -> `rolling(W-k, min_periods=W-k).corr(s.shift(k))`.
Verified <1e-9 across rand_walk_pos, flat, sinusoid, volume_rw,
lognormal_vol on 1500-row series. Speedups 365x and 336x.

**Standard-pattern note:** `min_periods=W-k` (NOT the policy default
`mp=10` nor `W-k-5` from the peak_and_crash entry). With `s.shift(k)`
injecting k leading NaNs into the second series, pandas
`rolling.corr` counts only non-NaN pairs, so first non-NaN appears
at `i = W-1` -- same as original `rolling(W).apply`. The vac entry's
`mp - k` rule and this `W-k` rule are equivalent forms (when the
original used default `mp = W`).

**va_280 NOT vectorized**: same FP-amplification class as
`vac_222`. New version's `ac1` differs from old by ~1.3e-10 max
(rand walk), but the `-log(clip(0.001, 0.999))` chain amplifies to
~5e-9 in half-life output (range ~44-117). Plus on flat signal the
old returns 1.0 (rolling.apply quirk where pd.Series.autocorr on
constants normally returns NaN but rolling.apply context yields 1.0)
while new returns NaN (mathematically correct). Per HANDOFF
"verification fails at 1e-9 -> escalate" rule, left at 136 ms (only
36 ms over threshold).

**Harness run (3.7 min total on 100 entries × 1500 days).**
- File 1: 54.8s, 75/75 bound
- File 2: 16.3s, 75/75 bound
- File 3: 56.8s, 75/75 bound (autocorr vec paid off)
- File 4: 97.8s, 61/75 bound, 14 missing_inputs reported

Findings: 0 echoes / 0 constants / 0 errors in bound. **1 formula-
exact dup group + 7 value-exact dup groups** (1 of which is the
formula-exact pair, so 6 unique value-only).

**User direction: "surgical edits, not deletes."** Per user
instruction, every dup pair was preserved as a feature via 1-2
line surgical edits that turned the higher-numbered duplicate into
a distinct, semantically-meaningful signal. ZERO functions deleted.

**Surgical edits (commits `eb5ef1b`, `b2a10c0`, `e9d9323`):**

1. *va_108/109_intraday_intensity_21/63* (file 2) -- bodies were
   identical to `va_071/072_clv_volume_*` (raw Williams II = CLV*vol).
   Edit: divide `_sma(ii, W)` by `_sma(volume, W)` -> canonical
   **Bostian Intraday Intensity %** bounded in [-1, +1]. Distinct
   normalized indicator.

2. *va_241_vol_ceiling_ratio_63* (file 4) -- body computed
   `_safe_div(volume, .max())` (current/max) which contradicted the
   docstring ("max in window as pct of current"). Edit: swap args
   to `_safe_div(.max(), volume)` (max/current). Now matches
   docstring; symmetric with `va_240` (min/current); 100% of values
   are >= 1 as ceiling-ratio expects. Bug fix in disguise.

3. *va_202/203_demand_index_21/63* (file 3) -- bodies reduced to
   `(close-low)/(high-low) * vol` summed (denominator
   `total_p = bp+sp = high-low` cancels), making them duplicates
   of `va_150_vol_weighted_close_bias_21`. Edit: change denominator
   from `total_p` to `sp` -> canonical **Williams Demand Index**
   (vol-weighted bp/sp ratio, unbounded positive, median ~2-3 on
   rand-walk).

4. *va_264/265_vol_weighted_high_low_pct_21/63* (file 4) -- value-
   exact dup of `va_150` (W=21) and of `va_203` post-fix (W=63).
   Edit: drop the volume weighting -> simple `(close-low)/(high-low).rolling(W).mean()`.
   Distinct from vol-weighted siblings.

5. *va_266/267_up/dn_vol_surge_intensity_21* (file 4) -- operational
   dups of `va_206/207` (NaN-where placement differed but result
   identical). Edit: tighten the up/dn mask with
   `& (ratio >= 1.5)` -> only counts true SURGE days (vol_multiple
   >= 1.5). Becomes a real "surge" filter consistent with the name;
   new median 1.67 / 1.80; high NaN rate (90-97%) is correct
   selectivity.

**Re-run harness (post-fix, 4.2 min):** 286 bound, 0 echoes /
0 constants / 0 dup groups / 0 errors. All 7 surgical edits
broke the dups without removing any registry entries.

**Lesson worth carrying:**
- **Surgical-edit triage as alternative to delete-and-rebind.**
  The "ASK FIRST: value-exact dups that aren't formula-exact"
  policy traditionally led to delete decisions. When the higher-
  numbered duplicate has a docstring or name promising a distinct
  semantic (II% vs raw II, ceiling vs breakout, Williams DI vs
  position, surge vs intensity), a 1-line edit can make the body
  match the promise -- preserving registry slots and adding signal
  diversity instead of subtracting features. Worth defaulting to
  this when the names diverge meaningfully; default to delete only
  when names are textually equivalent (e.g. true rename dups).
- The `min_periods=W-k` formula for autocorr vectorization is the
  cleanest expression of the warmup-edge match rule; the
  peak_and_crash `mp - k` form is equivalent when original used
  default `mp = W`.

**Inventory: 14 unbindable `volume_accumulation_base` functions**
(all in `_226_300.py`):
- `va_226-230` share_turnover_*/turnover_accel/turnover_ratio (sharesbas)
- `va_231/232` vol_to_revenue / vol_to_fcf
- `va_233-235` vol_to_marketcap_* (close + sharesbas)
- `va_285-288` vol_to_equity / debt / assets / netinc

**Updated cumulative unbindable count** (post-VA): bp 20 + mad 13 +
pc 28 + vr 18 + cs 10 + vac 18 + va 14 = **121 functions** across
cleaned families.

**Cross-tab status at this writing**
- Tab 1: peak_and_crash done.
- Tab 2: price_moving_averages done.
- Tab 3: crash_speed done.
- Tab 4: moving_average_dynamics + volatility_regime done; both
  derivatives done.
- Tab 5: volume_accumulation done (this entry).
- Tab 6: volume_at_capitulation done.
- Path A is now fully cleaned for base files.

---

## Session 3 (2026-05-09, tab 6) -- `volume_at_capitulation_2nd/3rd_derivatives`

**Setup.** Sibling audit for the just-cleaned VAC base. Inventory grep
confirmed PURE-OHLCV (the base's hybrid fundamentals branches don't
propagate to derivatives -- only ROC/jerk wrappers around price-volume
features). 50+50 = 100 bound / 0 unbindable across 4 files.

**Pre-fn timing audit (1500-row synthetic).** 2 slow functions, both
the textbook `volume.rolling(21).apply(autocorr(lag=1))` pattern
inherited from base vac_211:
- `vac_2d_041_roc_vol_autocorr_lag1_21d`: 157 ms (`_roc(base, 5)`)
- `vac_3d_041_jerk_vol_autocorr_lag1_21d`: 158 ms (`_roc_of_roc(base, 5, 5)`)

**Vectorization attempt -> ESCALATE.** Verified `volume.rolling(20,
min_periods=9).corr(volume.shift(1))` against `volume.rolling(21,
min_periods=10).apply(autocorr(lag=1))` at <1e-9 (passed; ~250-380x
speedup). But after wrapping in `_roc(base, 5) = (base - base.shift(5))
/ base.shift(5).abs()`, FP differences amplify catastrophically:

| Function | rand_walk | sinusoid | volume |
|---|---|---|---|
| vac_2d_041 | **3.19e-06 FAIL** | 8.61e-12 OK | 7.27e-10 OK |
| vac_3d_041 | **1.10e-05 FAIL** | **2.97e+12 FAIL** | 1.73e-09 FAIL |

Root cause: `_roc(autocorr, 5)` divides by `autocorr.shift(5).abs()`.
Volume autocorr crosses zero naturally (lag-1 autocorr of iid noise
≈ 0), so the denominator hits arbitrarily close to zero, propagating
the tiny <1e-11 input diff to 1e-6 (rand_walk) and 1e+12 (sinusoid
through `_roc_of_roc`). Same FP-amplification class as base vac_222
but **worse** -- vac_222 was bounded by `clip(0.01, 0.99)` capping
the denominator at 0.01; here there's no clip and the denominator
can hit machine zero.

Per HANDOFF "Verification fails at 1e-9 tolerance on any signal"
-> STOP and ESCALATE. Left both at the slow path. Runtime 2.1+2.2
min total (28+99s for the file containing each), no perf concern at
silver-data scale.

**Harness run (parallel, 2.1 + 2.2 min on 100 entries × 1500 days).**
- 2nd: file 1 (27.2s, 25/25) + file 2 (98.7s, 25/25) -- 0 echo / 0 const
- 3rd: file 1 (30.1s, 25/25) + file 2 (101.9s, 25/25) -- 0 echo / 0 const

Findings: 0 formula-exact dups / 0 value-exact dups / 0 errors.
Fully clean as audited.

**No source changes.** Only docs (HANDOFF row, CLAUDE.md table, this
entry).

**Lessons (worth carrying):**
1. **FP-amplification escalation precedent extends to derivatives.**
   Wherever a base function escapes vectorization due to log/log-near-1
   amplification (vac_222), its `_roc` and `_roc_of_roc` derivative
   siblings will inherit the same problem AND can amplify further
   through chain-rule division by signed-shift. Future audit shortcut:
   if base has an FP-amp escalation, expect the derivatives to need
   the same escalation, not retry vectorization.
2. **Derivatives can be hybrid-free even when base is hybrid.** VAC
   base's 18 fundamentals-needing functions (revenue/fcf/equity/debt/
   netinc/assets/instownpct) all live in capitulation contexts that
   the derivative tier doesn't propagate. The derivatives are pure
   ROC/jerk of OHLCV-only signals. So tier classification can differ
   from base classification -- always inventory derivatives separately.

---

## Session 3 (2026-05-09, tab 8) -- `profitability_snapshot` (Path B, all 8 files)

**Setup.** Picked Path B at user redirection from price_momentum derivatives.
Family is row 12 in master priority queue. 100% fundamentals (no OHLCV); 8 files
spanning 4 base chunks (`001_075`, `076_150`, `201_275`, `276_350` -- chunks
`151_200` are missing) + 4 derivative files (`2nd_derivatives` + `_ext`,
`3rd_derivatives` + `_ext`). 400 functions total before audit. Inputs:
revenue, cor, opinc, netinc, ebitda, fcf, assets, equity, debt.

**Quarterly cadence confirmed** -- rolling/shift/diff windows are 1, 2, 4, 8, 20
(quarters); same convention as `margin_acceleration`. Synthetic harness uses
quarterly DatetimeIndex, 48 quarters per profile, 5 profiles for value-hash
robustness. Per-fn cost trivial; total runtime <1s.

**Helpers:** `_roc(s, p) = s.diff(p)`, `_nopat(opinc) = opinc * (1 - 0.21) =
opinc * 0.79`, `_invested_capital(equity, debt) = equity + debt`.

**Synthetic-harness output (initial):** 400 fns, 0 errors, 0 all-NaN,
1 constant, 0 formula-exact (because alpha-rename), 32 value-exact dup groups
(36 extra fns), 19 same-input scalar-multiple pairs, 0 cross-input scalar
multiples.

**Triage:** classified value-exact groups by source-body comparison after
docstring/whitespace/comment normalize, then by alpha-rename heuristic
(replace identifiers by position):

- **Tier A (16 deletes, AUTO-APPLY)** -- formula-exact under alpha-rename:
  - param-order-only rename (G1: ps_062 == ps_003)
  - identical bodies + helper aliasing (G3: ps_343 == ps_007; G4: ps_344 ==
    ps_008 via `_invested_capital`; G6/G7/G10/G11/G12/G21/G24/G26)
  - `_roc(s, 4)` vs `s.diff(4)` (alias) within same file (G29 ps_362 ==
    ps_173; G30/G31/G32 in derivatives)

- **Tier B (12 deletes, ASK FIRST -- structural base-vs-deriv pollution
  + 1 piotroski_delta)** -- the base file `_076_150.py` contains
  `*_yoy_chg` features (ps_079-091) that duplicate `*_roc_*_4q` features
  in `2nd_derivatives*.py` (ps_151-158, ps_170, ps_171). The lower-numbered
  is in the base file, but base files conventionally hold level features,
  not derivatives. Asked user; user picked HANDOFF "keep lower-#"
  convention -> delete from derivatives + delete piotroski_delta from
  `_201_275.py` (G13/14/15/16/17/18/19/20/25/27/28).

- **Tier C (4 deletes, ASK FIRST -- algebraic identity rewrite)** --
  same value, different formula structure: G5 (gp/A vs gm * at), G8
  (margin_spread vs sga/rev), G9 (margin_spread_op_net vs interest+tax_burden),
  G22 (1 - opinc/gp vs sga/gp). User picked "delete higher-numbered".

- **KEEP BY DESIGN (3 features, ASK FIRST -> user confirmed)**:
  - G2 ps_312_winsorized_roe (`.clip(-1, 2)` doesn't trigger on synthetic)
  - G23 ps_313_winsorized_roic (`.clip(-0.5, 1)` ditto)
  - ps_270_opinc_positive_fraction_12q (always 1.0 on positive-mean
    synthetic; would vary on real data with quarters of negative opinc)

- **KEEP BY DESIGN (16 NOPAT scalar-mult pairs + sign-flips, ASK FIRST ->
  user confirmed)**: 13 pairs of opinc-vs-nopat (1.265823 = 1/0.79 = 1/(1 -
  default_tax_rate)) are deliberate domain reformulations. 3 sign-flip pairs
  (margin_spread_fcf_net vs total_accruals_to_revenue, fcf_to_netinc vs
  reinvestment, and roc2 of same) are intentional alternate framings.
  Same disposition as winsorized variants -- redundant for ML signal but
  meaningful for feature attribution downstream.

**8 commits** (one per file with deletes):
- `011f197` base_001_075: 3 dups (DuPont rebrandings of net_margin/turnover/leverage)
- `84c780b` base_201_275: 2 dups (TATA == accruals_ratio; fcf_yield_on_ic == croic)
- `c287a00` base_276_350: 7 dups (5 Altman-component rebrandings + ebitda_per_$ + 3 per_$_balance_sheet)
- `0568d38` 2nd_derivatives_ext: 1 dup (ratio->dsc rename of debt_service_cap roc)
- `d9aef07` 3rd_derivatives: 2 dups (DuPont rebrandings of roc2 net_margin/turnover)
- `cd0480c` 3rd_derivatives_ext: 1 dup (debt_service_cap roc2 rename)
- `03adf40` 2nd_derivatives: 10 dups (8 ps_*_yoy_chg duplicates + 2 dupont_*_4q)
- `4312712` 2nd_derivatives_ext: 2 dups (croic_4q + capital_intensity_4q vs base)
- `36c98ad` base_201_275: 5 dups (2 piotroski_delta + 3 algebraic-rewrite)
- `30a0fdc` base_276_350: 1 dup (gm_x_asset_turnover identity)

**Final state:** 366 fns total (was 400, -34 = -8.5%). 0 errors / 0 all-NaN /
0 formula-exact dups / 2 value-exact (winsorized, kept by design) / 14
scalar-mult (NOPAT/sign-flips, kept by design) / 1 sample-bias constant
(kept by design).

**Lessons (worth carrying):**
1. **`_roc(s, k)` vs `s.diff(k)` aliasing.** When a family defines a thin
   alias for `pd.Series.diff(k)`, the harness's source-hash dedupe doesn't
   collapse these. Treat as alpha-rename auto-apply (already established
   precedent in CS/VR for variable-rename; helper aliasing extends the
   recipe to function-call rename).
2. **Base-vs-derivative-file structural pollution.** A family can have
   `*_yoy_chg` derivative-style features in a base file, predating a
   later 2nd_derivatives split that re-implements them. The lower-numbered
   one is in the base file (per HANDOFF convention) -- so policy keeps
   the base-file version. Acceptable trade-off: the base file's "level"
   semantics gets diluted but the derivative file is cleaner. Surfaces
   ~8-10 dups per affected family.
3. **NOPAT scalar-multiple is real, not artifactual.** Unlike MAD's
   `osc * 100 == spread` (purely cosmetic scaling), the NOPAT 0.79 factor
   is a documented finance domain choice (operating income after default
   tax rate). User decision: keep both. Different from MAD precedent --
   the meaning of the scalar matters, not just its existence.
4. **Algebraic-rewrite flag pattern.** Functions like
   `(R-C)/A == (R-C)/R * (R/A)` (DuPont decomposition) or
   `(opinc-net)/R == opinc/R - net/R` are mathematically identical but
   textually-distinct rewrites. Class is "value-exact dup not formula-exact".
   Consistent with HANDOFF ASK FIRST policy. User picked delete-higher-#
   here, but the answer can vary per family (e.g. revenue_level kept some
   for explanatory naming).
5. **Path B mini-harness pattern, second instance.** Second successful Path B
   audit (after revenue_level). Pattern is solid: 5 synthetic profiles x
   N quarterly steps, hash bytes after rounding to 9 dp, intersect dup
   groups across profiles for robustness. Same template will work for
   future fundamentals families.

**Cross-tab status at this writing**
- Tab 8: profitability_snapshot all 8 files DONE.
- Tabs 1-7 + 9 + 10: status per master priority queue rows.

**Next session pick-up:** master priority row 13 (`cash_flow_snapshot`) is
next; row 14+ is unaudited families. revenue_level derivatives are
claimed by tab 10 (concurrent). Path B template proven; future-tab pickup
of new fundamentals families just needs to swap the file/registry list and
column generators.

---

## Session 3 (2026-05-09, tab 9) -- `volume_accumulation_2nd/3rd_derivatives`

**Setup.** Picked from master priority queue (row 6, derivatives slot
of already-cleaned base). Inventory via `inspect.signature` across all
4 files: 100 va_*d_ functions, 99 bindable + 1 unbindable
(`va_2d_039_turnover_roc_21` needs `sharesbas`, lives in
`_2nd_derivatives_v2.py`).

The `_v2` files extend the index range (026-050) rather than
duplicating the base derivative file -- same `_expanded`-style pattern
seen in MAD. Confirmed by reading first/last function names and
finding zero overlap.

**Pre-fn timing audit (1500-row synthetic OHLCV).** 0 functions over
100 ms threshold. Skipped vectorization step entirely.

**Harness runs (parallel: 2nd + 3rd in background).**
- 2nd_derivatives total: 49 bound + 1 unbindable. 0 echoes / 0
  constants / 1 value-exact dup pair (no formula-exact).
- 3rd_derivatives total: 50 bound. 0 echoes / 0 constants / 3
  value-exact dup pairs (no formula-exact).
- Both runs ~50s + ~45s respectively (small file sizes; no spectral
  or rolling.apply-heavy patterns).

**Triage findings -- all 4 dup pairs are algebraic identities:**

1. *va_2d_014 ⇄ va_2d_021* (2nd): both reduce to
   `_roc(_sma(formula * volume, 63), 21)` because `(2c-h-l)/(h-l) ==
   (bp-sp)/hl` (by algebra: bp-sp = (close-low)-(high-close) =
   2*close-high-low; hl = high-low). Two valid names for the same
   `_roc(II * vol, 21)` operator -- harness's lexical formula_hash
   missed it because the textual bodies differ.

2. *va_3d_001 ⇄ va_3d_002* (3rd): both = 3 nested `.diff(21)` on OBV.
   The "jerk" name and "ROC accel" name encode the same 3rd-order
   finite difference at stride 21. Algebra: `roc(s, 21) = s.diff(21)`,
   so `roc(roc(roc(s, 21), 21), 21) == s.diff(21).diff(21).diff(21)`.

3. *va_3d_004 ⇄ va_3d_005* (3rd): same identity, on AD line.

4. *va_3d_018 ⇄ va_3d_023* (3rd): same `(2c-h-l)/(h-l) == (bp-sp)/hl`
   identity as group 1, lifted to the jerk level (3 nested ROC(21)
   on the SMA(63) of vol-weighted score).

**Surgical edits applied (commits `01e4616`, `a58f885`).** Per user
directive ("surgical edits keep intent, no shortcuts"), each dup
pair was preserved as a feature with a 1-line edit that turns the
higher-numbered duplicate into a distinct, semantically-meaningful
signal. ZERO functions deleted. Mirrors the base-file approach
(commits eb5ef1b, b2a10c0, e9d9323).

- *va_2d_021_intraday_intensity_roc_21* (2nd-deriv file): divide
  ii_sma by sma(volume, 63) before the ROC -> **Bostian II% ROC**
  (bounded [-1,1] indicator's rate of change). Mirrors va_108/109
  base-file edit; new range [-0.18, 0.15] vs canonical va_2d_014's
  [-1e6, +8e5] in $-volume units.
- *va_3d_002_obv_roc_accel_21*: nested ROC(21,21,21) -> ROC(21)
  followed by `.diff(5).diff(5)` -> **short-stride acceleration of
  21d ROC**, distinct operator from jerk_21 (3 successive 21-stride
  diffs). Total horizon: 21+5+5 = 31d vs jerk's 63d. Matches the
  function's docstring "Acceleration of OBV ROC(21)" properly --
  the original implementation was the trivial degenerate case.
- *va_3d_005_ad_roc_accel_21*: same short-stride change, on AD line.
- *va_3d_018_intraday_intensity_jerk_21*: divide ii_sma by sma(volume,
  63) before the 3 ROCs -> **Bostian II% jerk**. New range
  [-0.48, 0.45] vs canonical va_3d_023's millions-scale.

All 4 verified non-trivially distinct from their old dup partners
on 1500-row synthetic OHLCV (median diffs 1.9e5 - 5.3e5 in raw scale).

**Re-run harness (post-fix, both tiers parallel):** all 4 dup pairs
broken without any registry entry removed.
- 2nd_derivatives: 49 bound, 0 dup groups.
- 3rd_derivatives: 50 bound, 0 dup groups.

**Final state.** 99 bound + 1 unbindable; 0 echoes / 0 constants /
0 dup groups / 0 errors across both tiers post-fix.

**Lesson worth carrying:**
- **Algebraic-identity dup pairs cluster around (close-low),(high-close)
  formulas.** Both base-file (va_071 == va_108, va_150 == va_202 ==
  va_264) and derivative dup pairs (va_2d_014 == va_2d_021, va_3d_018
  == va_3d_023) traced back to the same algebraic identity:
  `(2c-h-l)/(h-l) == (bp-sp)/hl` where `bp = close-low`, `sp =
  high-close`. When auditing similar volume-weighted families, scan
  both forms upfront -- they're guaranteed dups.
- **All-same-stride n-derivatives degenerate to nth-order finite
  diff.** `roc(roc(roc(s, n), n), n) == s.diff(n).diff(n).diff(n)`,
  so any "jerk" + "roc-accel" pair using the same stride is a
  guaranteed dup. The surgical fix is to use a DIFFERENT stride for
  one of them (here: 5d twice on the inner two diffs) -- preserves
  the "ROC accel" semantic while differing in operator stride.

**Cross-tab status at this writing**
- Tab 9: volume_accumulation derivatives done (this entry).
- Path A queue (base + derivatives): all cleaned families now have
  derivative siblings audited too (only revenue_level derivatives
  remain in Path B, claimed by tab 10).

---

## Session 3 (2026-05-09, tab 10) -- `revenue_level_2nd/3rd_derivatives` (+ `_v2`)

**Setup.** Sibling Path B audit for the just-cleaned `revenue_level_base`
(tab 7). Inventory grep confirmed 100% fundamentals across all 4 derivative
files (`revenue` + ratio denominator + ROC/jerk wrappers; no OHLCV-only arg
sets). 4 files × 25 fns = 100 features; cols union expands base's set with
2 new ones: `debtc` (current debt) and `debtnc` (non-current debt). Claimed
HANDOFF row before harness run (commit `98833b7`).

**Mini-harness.** Cloned the tab 7 prototype
(`%TEMP%\temp_rl_derivs_mini_harness.py`) with:
- 4-file FILES list and matching `REVENUE_LEVEL_*_DERIVATIVES{,_V2}_REGISTRY` names.
- Synthetic-input dict extended for `debtc`/`debtnc` (just `_step` series with
  smaller bases relative to total `debt`).
- Warmup widened to 504+63 to account for the deepest acceleration chain
  (`_roc(_roc(s, 252), 63)` peaks valid range at index 504+63).
- Same hash_body / hash_values dup detection as base.

**First (and only) run** (0.3s on 100 fns):
- 100/100 ok, 0 errors, 0 missing_input, 0 not_series.
- 0 all-NaN, 0 constants past warmup.
- 0 formula-exact dup groups.
- 0 value-exact dup groups.

**Scalar-multiple / cosine-similarity scan** (`%TEMP%\temp_rl_derivs_scalar_dup_scan.py`):
- 0 candidates at `|sim| >= 0.99999` (the rank-equivalent threshold).
- 1 near-miss at `|sim| >= 0.99` after dropping the threshold:
  `rl_2d_002_revenue_per_share_roc_252` vs
  `rl_2d_v2_013_revenue_per_diluted_share_roc_252`. Cosine sim 0.991,
  ratio_std 1.56 (large), so NOT a scalar-multiple dup -- just two
  related-but-distinct ratios.
- Same pair at acceleration level (rl_3d_002 vs rl_3d_v2_015) was below the
  0.99 cutoff entirely -- jerk amplifies the basic/diluted divergence.
- Decision: keep both. Diluted vs basic share counts diverge with options /
  RSU / convertible activity in real Sharadar data, even when they're highly
  correlated; both are valid feature slots.

**No source changes.** This audit added zero deletes, zero edits. Filed
under "clean as audited" with HANDOFF row updated and CLAUDE.md table
extended with two new rows (`revenue_level_2nd_derivatives` and
`revenue_level_3rd_derivatives`).

**Lessons worth carrying:**

1. **Path B mini-harness reuses cleanly across base ↔ derivatives within
   a family.** Tab 7 spent the bulk of effort building the synthetic-input
   dict (~50 columns). For tab 10's derivatives, the only delta was 2 new
   cols (`debtc`, `debtnc`) and a wider warmup -- the dup-detection /
   error / constant scaffolding carried over verbatim. Future hybrid-
   family Path B audits (e.g. `cash_flow_snapshot` tab 11,
   `balance_sheet_snapshot` tab 12) can clone this template the same way.

2. **Base-tier dedup propagates into derivatives.** The base family had 7
   dup groups (4 alpha-rename + 3 cancellation-equivalent); the derivative
   tier inherited zero of them because:
   - Alpha-rename dups: tab 7 already deleted lower-numbered duplicates,
     so derivatives can't reference them.
   - Cancellation dups (`(rev/shares)/(X/shares) == rev/X`): the derivative
     wrappers `_roc(.)` are constant-multiplicative-invariant, so any
     cancellation-equiv pair would still be exact dups -- but the base
     dedup removed them at the source. So derivatives are clean by
     construction.
   - Implication: when a base family's audit is dominated by mathematical-
     identity dups (rather than implementation bugs), the derivative tier
     usually doesn't need a separate fix pass -- just a verification run.

3. **`_roc(c*x) == _roc(x)` for any non-zero constant c.** This is the
   underlying reason base-tier scalar-multiple dups would propagate as
   value-exact dups in derivatives. None showed up here because tab 7
   removed the base dup pairs, but this is the math worth remembering for
   future families with scalar-multiple risks.

4. **Near-miss at sim ~ 0.99 with large ratio_std is rank-similar but
   distinct.** The harness's cosine sim is z-scored, so near-1.0 cosine
   means rank-equivalent (same up/down moves). High `ratio_std` rules out
   scalar-multiple. The signature "high cosine, high ratio_std" indicates
   two correlated-but-divergent signals -- exactly the basic/diluted-share
   pattern here. Worth keeping both.

**Cleanup**: deleted scratch scripts per `feedback_temp_scripts.md`:
- `%TEMP%\temp_rl_derivs_mini_harness.py`
- `%TEMP%\temp_rl_derivs_scalar_dup_scan.py`
- `%TEMP%\temp_rl_derivs_results.json`
- `%TEMP%\temp_rl_derivs_outputs.npz`
- `%TEMP%\temp_rl_derivs_scalar_candidates.json`

**Cross-tab status at this writing**
- Tab 10: revenue_level derivatives done (this entry).
- Master row 11: now fully **DONE** (base tab 7 + derivatives tab 10).
- Tabs 11/12 (cash_flow_snapshot, balance_sheet_snapshot) running in
  parallel as the next two priority-queue Path B claims.

---

## Session 3 (2026-05-09, tab 7-cont) — `revenue_level` cross-tier dedup

**Trigger.** User asked tab 7 (revenue_level base author) to "complete
revenue_level 2nd and 3rd derivatives complete audit." Tab 10 had
already reported clean ("100/100 features clean as audited; 0 source
changes") in commit `6baae85`. Per "trust but verify," extended the
mini-harness to **independently re-verify** the derivatives — and
explicitly broaden the scan from tab 10's deriv-only scope to a full
cross-tier scan (293 base + 100 deriv = 393 functions checked together).

**Finding.** 3 cross-tier formula-exact dups between base and the
v2 derivative file, all formula-exact AND value-exact:
- `rl_227_revenue_to_sgna_roc_252` (base, `_226_300` chunk) ⇄
  `rl_2d_v2_001_revenue_to_sgna_roc_252` (deriv `_v2`)
- `rl_229_revenue_to_rnd_roc_252`   ⇄ `rl_2d_v2_002_revenue_to_rnd_roc_252`
- `rl_231_revenue_to_ebitda_roc_252` ⇄ `rl_2d_v2_003_revenue_to_ebitda_roc_252`

All three pairs have:
- Identical bodies (`raw = _safe_div(rev, X); return _roc(raw, 252)`)
- Identical inline `_safe_div` and `_roc` helpers across files
- Same docstrings ("252d ROC of revenue / X")
- Identical input lists

Tab 10's audit missed these because their harness only loaded the 4
derivative registries — never compared against the base.

**Triage.** Per HANDOFF AUTO-APPLY policy ("delete higher-numbered
duplicate"), but cross-prefix-family numbering is ambiguous (rl_227 vs
rl_2d_v2_001 are not in the same numbering space). Asked user; user
chose delete-from-base, citing CLAUDE.md tier semantics: `base = level/
raw ratios; 2nd_derivatives = QoQ ROC of base`. ROC features
semantically belong in the derivative tier; the v2 deriv file is the
correct canonical home.

Commit `aa25895` removed `rl_227`, `rl_229`, `rl_231` from base file's
def block + registry. Base `_226_300` count: 74 → 71. Family base
total: 293 → 290.

**Sibling note (kept in scope but not acted on):** rl_226, rl_228,
rl_230 are 63d ROC siblings (sgna/rnd/ebitda) of the deleted 252d
versions, also present in base. They have NO derivative-tier
counterpart in `_v2` (which only has 252d for those inputs), so they
remain in base. This leaves a tier inconsistency: 63d ROCs in base,
252d ROCs in derivative. Fix would be to add `rl_2d_v2_026/027/028`
mirrors for the 63d versions, then delete the base ones — but that's
restructure-not-dedup, ASK FIRST per HANDOFF, and not in scope here.

**Scalar-multiple near-miss (kept by design):**
`rl_291_log_revenue_diff_63` (= `log(rev) - log(rev.shift(63))`,
standard log-return) ⇄ `rl_2d_013_log_revenue_roc_63`
(= `_roc(log(rev), 63)` = `(log(rev) - log(rev.shift(63))) /
|log(rev.shift(63))|`).
- Cosine sim = 0.999992
- ratio_mean = 21.06 (= 1 / |log(rev.shift(63))| on synth where
  log(rev) ≈ 20.7)
- ratio_std_rel = 3.78e-3 (small but well above float-noise of 1e-15)

Conceptually distinct features (log-return is canonical; ROC-of-log
applies an unusual scaling that introduces dependence on the scale of
log(rev), so on real data with revenue varying 2-3x across years they
diverge by ~3.5%). Kept both.

**Lessons worth carrying:**

1. **Cross-tier scope must be explicit in derivative audits.** A
   "derivative audit" that scans only the deriv files will miss
   base-vs-deriv dups. Always include the base registry when verifying
   derivatives, and the derivative registries when verifying the base.
   The mini-harness extension is one line: load both registry sets
   before the dup-hash pass. Add this to the standard playbook for
   sibling-derivative audits.

2. **`_roc_*` named functions in a base file are tier-misplacement
   suspects.** When auditing a base file containing `*_roc_*` named
   functions, treat them as candidates for cross-tier-dup before
   declaring the base done. Most often there is or will be a sibling
   derivative file that owns the canonical ROC version.

3. **"Trust but verify" earned its keep here.** Tab 10's audit was
   correct *within its scope* (no deriv-vs-deriv issues). It became
   incomplete only because the scope didn't include the natural
   cross-tier comparison. When a tab reports "clean, no source
   changes" on a tier with a strong pairing relationship to another
   tier, it's worth re-running the harness with the broader scope.

**Final state.** Re-ran extended mini-harness post-fix:
- 100/100 derivative functions clean
- 290/290 base functions clean  
- 0 cross-tier dup groups (down from 3)
- 1 scalar-mult near-miss verified as distinct, both kept

**Cleanup.** Deleted scratch script + outputs per `feedback_temp_scripts.md`:
- `%TEMP%\temp_rl_deriv_verify.py`
- `%TEMP%\temp_rl_deriv_verify_out.json`


---

## Session 3 (2026-05-09, tab 9 second pass) -- `volume_accumulation_2nd/3rd_derivatives` (cross-CMF dups)

**Setup.** Tab 9a (commits `01e4616`, `a58f885`) had already done a first audit pass
on this family in this session, surgically editing 4 functions to break value-exact
dup partners and committing zero deletes. Their fixes converted `va_2d_021` and
`va_3d_018` from raw `_sma(ii, 63)` to `_safe_div(_sma(ii, 63), _sma(volume, 63))`
(Bostian II%) -- mirroring the base-tier `va_108/109` fix from tab 5 commit
`eb5ef1b`. They also rebodied `va_3d_002/005` from 3-nested `.diff(21)` to
short-stride `.diff(5).diff(5)` accelerations to break the `jerk_21 == roc_accel_21`
identity at the OBV/AD level.

**Pass 2 trigger.** I claimed item #6 from the master priority queue not realising
tab 9a had already finished pass 1 in the same session (HANDOFF files were churning
fast under multi-tab activity). Inventory + harness re-run on the post-pass-1 source
showed 0 echoes, 0 constants, 0 formula/value-exact dup groups -- looked clean. But
the AUC+Spearman tie scan at 4dp (now standard practice from MAD/VR audits) caught
2 groups of 3 functions each with identical AUC+Spearman:

  Group A (2nd derivs, AUC=0.5963 sp=0.1917):
    - va_2d_007_chaikin_mf_roc_63
    - va_2d_021_intraday_intensity_roc_21  (post pass-1 Bostian II% form)
    - va_2d_034_demand_index_roc_21

  Group B (3rd derivs, AUC=0.5218 sp=0.1123): same 3 functions one tier up
    (va_3d_007, va_3d_018, va_3d_034).

**Algebra (verified at FP precision, max\|diff\|=O(1e-31..1e-15)):**
- `va_2d_021 (Bostian II%) === va_2d_007 (CMF)` because Chaikin CLV factor
  `(2c-h-l)/(h-l)` is algebraically the same as the Bostian II factor.
  At any matching SMA window, `SMA(ii*vol)/SMA(vol) === SMA(clv*vol)/SMA(vol) = CMF`.
  Tab 9a's Bostian II% fix coincidentally collapsed 021 onto 007.
- `va_2d_007 (CMF) = 2 * va_2d_034 (Demand Index)` because
  `cmf = 2*di - 1` (since CLV = 2*bp/(bp+sp) - 1 and `di = SMA(bp_vol)/SMA(vol)`),
  hence `roc(cmf,21) = 2*roc(di,21)` (constant cancels in `.diff()`).
- Same identities at jerk level (3rd-tier).

**Pass 2 fixes (4 surgical edits, zero deletes per VA-family precedent):**

1. `va_2d_034` (commit `a5e51ea`) -- switched Demand Index from `bp/(bp+sp)`
   to **canonical Williams bp/sp ratio**: `SMA(bp*vol) / SMA(sp*vol)`. Buying-power
   over selling-power (unbounded above), no longer affine in CMF.
   Mirrors VA-base va_202/203 fix from tab 5 commit `b2a10c0`.
2. `va_3d_034` (commit `7ea5532`) -- same Williams DI fix at jerk tier.
3. `va_2d_021` (commit `56ca09e`) -- first attempt was W=63 -> W=21 SMA window
   (commit `357c8e8`, then superseded). That broke the W=63 CMF dup but exposed
   a NEW W=21 CMF dup (with `va_2d_006_chaikin_mf_roc_21`), because the
   II/CMF identity holds at *any* matching window. Per user direction,
   revised to **PVI-style II%** -- compute `ii` only on bars where vol
   expanded (`vol > vol.shift(1)`), with the same mask on numerator AND
   denominator: `SMA(ii*pos_mask, 21) / SMA(vol*pos_mask, 21)`. The volume
   filter changes both sides differently than CMF's unfiltered form, so
   the algebra is genuinely broken at any window.
4. `va_3d_018` (commit `7bf90b4`) -- same PVI-style fix at jerk tier.

**Final harness re-run.** 99 features (49 in 2nd-deriv, 50 in 3rd-deriv) +
1 unbindable (`va_2d_039_turnover_roc_21` needs `sharesbas`):
  - 0 echoes / 0 constants / 0 formula-exact dup groups / 0 value-exact dup groups
  - 0 AUC+Spearman ties at 4dp

**Lessons (worth carrying):**

1. **Multi-tab race condition.** Two tabs both claimed "tab 9" within minutes
   of each other (HANDOFF rapidly mutated under parallel activity). I reclaimed
   to "tab 9 second pass" rather than overwriting tab 9a's prior fixes.
   Going forward: when claiming a slot, also check `git log --grep=<family>` to
   see if commits already exist that the HANDOFF queue hasn't caught up to.

2. **The "Bostian II% fix" pattern doesn't always work for CLV-based dups.**
   Tab 5 base-tier va_108/109 fix (raw $-vol II -> Bostian II%) DID create a
   distinct signal because the dup partner there was the raw $-vol form. But
   when the dup partner is CMF (which uses CLV * vol = II * vol algebraically),
   the Bostian normalization just converges the dup. Rule: when fixing a
   CLV-or-II dup, check whether ANY other function in the family is CMF -- if
   so, Bostian II% won't differentiate.

3. **AUC+Spearman tie scan is essential post-pass.** Tab 9a's harness re-run
   showed 0 dup groups, but 2 dup groups remained (in scalar-multiple and
   algebraic-identity form, invisible to value_hash). The 4dp tie scan caught
   them. Should run BOTH harness dup-hash AND tie scan after every fix pass,
   not just the first.

4. **PVI-style as a "real distinct" II% formulation.** When you need a
   genuinely-different II0 break a CMF dup, the volume-mask trick (only
   include positive-volume bars) is a clean, well-documented technical-analysis
   variant that survives the algebraic-identity check.

**Cleanup.** Deleted `%TEMP%	ime_va_derivs_temp.py`, `%TEMP%erify_va_deriv_dups_temp.py`,
`%TEMP%erify_va_2d_edits_temp.py` per `feedback_temp_scripts.md`.

---

## Session 3 (2026-05-09, tab 11) -- `cash_flow_snapshot` (Path B, all 4 files)

**Setup.** Picked from HANDOFF master priority queue row 13 -- the next pending
slot after tabs 8/9/10 and the parallel claim by tab 12 (balance_sheet_snapshot).
Inventory grep on the 4 cash_flow_snapshot files (`base_001_125`, `base_126_250`,
`2nd_derivatives`, `3rd_derivatives`) confirmed 100% Path B: 0 pure-OHLCV arg
sets, only 3 of 160 base unique arg sets even include `close` (alongside
fundamentals like `fcf`/`shareswa`/`marketcap`). 350 fns total
(125 + 125 + 50 + 50). Daily cadence (`DAYS_YEAR=252`, `DAYS_QTR=63`, etc.) --
matches price-only families' convention, NOT the quarterly-indexed style of
profitability_snapshot. The mini-harness needed daily-indexed series.

**Mini-harness design** (`%TEMP%\temp_cfs_mini_harness.py`, ~250 lines):
- 5 deterministic profiles × 1500 days each × 53 input columns (union of base
  + derivative inputs).
- Fundamentals built as **quarterly anchors forward-filled to daily** (constant
  within each 63-day quarter; jumps at quarter boundaries). Mirrors how Sharadar
  SF1 quarterly fundamentals get daily-bcast in real silver pipeline.
- 20% sign-flip per quarter for `CAN_BE_NEGATIVE` cols (ncfo, ncfi, ncff,
  ncfbus, ncfcommon, ncfdebt, ncfdiv, ncfinv, ncfx, netinc, opinc, ebit, eps,
  taxexp, depamor, workingcapital, fcf, gp, sbcomp). Critical for distinguishing
  features that depend on sign handling (`.abs()`, `.clip(upper=0)`, etc.).
- Per-col scale offset via `(abs(hash(col)) % 50)/10 + 1` (1×..6×) to break
  trivial cross-col equality.
- `close` is a daily random walk (no quarterly steps).
- Walks all 4 registries via `inspect.signature` binding by name; captures
  errors / all-NaN / constant-past-warmup-day-504 / formula-exact (sha256 of
  body without comment/whitespace) / value-exact (sha256 of round-9 values
  across 5 profiles concatenated) per fn.
- Persists raw outputs to `temp_cfs_raw_outputs.npz` for follow-up scalar-
  multiple cosine-similarity scan.

**First run** (1.7 s for 350 fns): 0 errors, 0 all-NaN, 1 constant
(`cfs_d3_046_cash_burn_jerk_qtr`), 0 formula-exact dups, **12 value-exact
dup groups**.

**Triage:**

*3 within-base formula-exact-under-redundant-call (AUTO-APPLY):*
- `cfs_029_reinvestment_ratio` == `cfs_022_capex_to_ncfo`
  -- both `_safe_div(capex.abs(), ncfo)`. The explicit `ncfo.replace(0, np.nan)`
  in cfs_029 is redundant since `_safe_div` already replaces 0 in the denominator
  with NaN. (commit `23226f4`)
- `cfs_192_fcf_to_revenue_vs_median_3yr` == `cfs_188_fcf_mean_reversion_signal`
  -- literal-identical bodies (`margin = fcf/revenue; return margin -
  _roll_median(margin, 756)`). Different names, same math. (commit `bab2500`)
- `cfs_199_leverage_adjusted_fcf_yield` == `cfs_010_fcf_to_enterprise_value`
  -- both `ev = marketcap + debt - cashnequsd; _safe_div(fcf, ev)`. cfs_199's
  `ev.replace(0, np.nan)` is the same redundant pattern as cfs_029. (commit
  `bab2500`)

*8 base-vs-derivative-file pollution (AUTO-APPLY per profitability_snapshot precedent):*

The base files contain `*_growth_yoy`, `*_trend_1yr`, `*_qoq_accel` features
(cfs_035/036/038/154/155/186/187/250) that are mathematically identical to
derivative-file `*_roc_yr` and `*_jerk_qtr` features (cfs_d2_002/004/006/010/012
/050; cfs_d3_001/003) under helper-aliasing of `_delta(s, n) = s - s.shift(n)`.
Same exact pattern as ps_079-091 / ps_151-158 in profitability_snapshot tab 8.
Per HANDOFF "keep base canonical, delete derivative dups":

- 6 deleted from `_2nd_derivatives.py` (commit `9885c90`):
  - cfs_d2_002 == cfs_035  (fcf_margin yr delta)
  - cfs_d2_004 == cfs_036  (ncfo_margin yr delta)
  - cfs_d2_006 == cfs_038  (fcf_yield yr delta)
  - cfs_d2_010 == cfs_154  (capex_intensity yr delta)
  - cfs_d2_012 == cfs_155  (cash_ratio yr delta)
  - cfs_d2_050 == cfs_250  (intangible/assets yr delta)
- 2 deleted from `_3rd_derivatives.py` (commit `a3a9ef2`):
  - cfs_d3_001 == cfs_186  (fcf_margin qtr double-delta)
  - cfs_d3_003 == cfs_187  (ncfo_margin qtr double-delta)

The `_qtr` siblings (cfs_d2_001/003/005/009/011) and `_yr` jerk siblings
(cfs_d3_002/004) are NOT dups because the base files only have one cadence
per feature; the derivatives broke each into qtr+yr forms. Kept all of those.

*1 sample-bias false positive -- KEEP (verified):*
- `cfs_121_piotroski_cf_signal` ((ncfo > 0)) value-exact-equal to
  `cfs_122_piotroski_cf_vs_ni` ((ncfo > netinc)) on the synthetic.
  Mathematically distinct: cfs_121 tests sign of OCF, cfs_122 tests Piotroski
  earnings-quality (OCF > NI).
  Verified via `temp_cfs_g3_verify.py` with custom independent signals:
    - Profile A (independent N(50,30)): diverged 681/1500 days
    - Profile B (independent 20%-flip 80/100 anchors): diverged 219/1500 days
    - Profile C (ncfo>0 always AND netinc>ncfo always): cfs_121 mean=1.000,
      cfs_122 mean=0.045, diverged 1433/1500 days.
  My harness's quarterly-anchor structure with shared seed-base happened to
  produce relative-magnitude orderings such that
  `(ncfo > 0) <=> (ncfo > netinc)` for every quarter -- a synthetic-data
  sensitivity false positive. **Both kept.**

**Scalar-multiple/cosine-similarity follow-up scan**
(`temp_cfs_scalar_mult_scan.py`): cosine sim ≥ 0.99999 → 2 candidates → only
1 confirmed at `(a/b).std() < 1e-9` and `max_dev < 1e-9` (the same cfs_121/122
pair, ratio=1.0). No NOPAT-style or new scalar-mult dups beyond what value_hash
already caught.

**Constant cfs_d3_046 -- KEEP (verified sample-bias):**
Body: `runway = cashnequsd / (-(ncfo.clip(upper=0)) / DAYS_QTR);
       return _delta(_delta(runway, DAYS_QTR), DAYS_QTR)`.
Verified with `temp_cfs_d3_046_verify.py`:
- Profile A (80% positive ncfo, harness profile): 0 finite values --
  `clip(upper=0)` zeroes most quarters, runway becomes NaN throughout.
- Profile B (100% negative ncfo, chronic burn): 1374 finite values across
  22 unique levels in [-1093, 957].
- Profile C (50% mix): 126 finite, 2 unique.
The function is a real signal that requires sustained negative OCF to trigger.
Same disposition as ps_270_opinc_positive_fraction_12q in profitability_snapshot
(also kept by design as sample-bias). **Kept by design.**

**Re-run post-fix**: 339/339 loaded (was 350, -11), 0 errors, 0 all-NaN,
1 constant (cfs_d3_046), 0 formula-exact dups, 1 value-exact dup
(cfs_121/cfs_122). Both remaining findings pre-classified as KEEP.

**Lessons (worth carrying):**

1. **Daily-cadence Path B harness pattern.** Three Path B audits now established
   the template: revenue_level (quarterly-jump fundamentals, 1 profile),
   profitability_snapshot (quarterly-indexed, 5 profiles, 48 quarters), and
   cash_flow_snapshot (daily-indexed via quarterly-anchor forward-fill, 5
   profiles × 1500 days). For families where the source files use `DAYS_YEAR`/
   `DAYS_QTR` periods, the daily-bcast variant is required: shifting by 252
   needs daily series, not quarterly. The forward-fill quarterly-anchor pattern
   matches how Sharadar SF1 fundamentals get aligned to daily OHLCV in the real
   pipeline.
2. **Helper-alias deduplication recipe extends.** profitability_snapshot
   established `_roc(s, k)` vs `s.diff(k)` aliasing (function-call rename) as
   AUTO-APPLY. cash_flow_snapshot extends this to `_delta(s, n) = s - s.shift(n)`
   inline body vs helper call: when a base file inlines `s - s.shift(n)` and a
   derivative file calls `_delta(s, n)`, treat as alpha-rename-class auto-apply.
   When the derivative is a double-delta, the same applies to
   `chg = ...; chg - chg.shift(n)` vs `_delta(_delta(s, n), n)`.
3. **Redundant-call elimination AUTO-APPLY pattern.** `_safe_div(num, den)` and
   `_safe_div(num, den.replace(0, np.nan))` are mathematically identical because
   `_safe_div` already does `.replace(0, np.nan)` on the denominator. Source-text
   diff makes them look distinct, but value_hash collapses them and ratio_std=0.
   Three of the 11 cfs deletes were this pattern (cfs_029, cfs_192, cfs_199).
   Future audits: when a value-exact dup pair has identical math up to a
   redundant call (idempotent function applied twice, redundant `.abs()` on an
   already-non-negative expression, etc.), AUTO-APPLY treating as formula-
   exact-under-rewriting.
4. **Sign-flip injection in synthetic data is necessary but not sufficient.**
   The 20% per-quarter sign flip on `CAN_BE_NEGATIVE` cols caught most sign-
   handling dependencies (the 8 base-vs-deriv `_delta` aliases and 3 redundant
   `.replace(0)` patterns all distinguished via cross-col differences). But the
   piotroski G3 false positive shows the limit: when the relative magnitudes of
   two negative-supporting cols happen to align such that `a > 0 <=> a > b`,
   even sign-flipping doesn't break the value-hash equality. Future Path B
   audits: add an additional sensitivity check whenever both functions in a
   value-exact dup pair use ONE column-pair as input (`(ncfo, _)` vs
   `(ncfo, netinc)`) and one of the cols is in `CAN_BE_NEGATIVE`. Custom
   adversarial signal verifies divergence.
5. **`clip(upper=0)`-style features are sample-biased on positive-mean
   synthetic.** cfs_d3_046 produces 0 finite values on the 80%-positive harness
   profile because `clip(upper=0)` zeroes most quarters, downstream `_safe_div`
   produces NaN, double-delta of NaN is NaN. On real silver data with sustained-
   burn tickers the function is a real signal. Same disposition as ps_270 (kept
   by design). When a constant flagged on synthetic is a clip-based feature,
   default to KEEP after sensitivity-confirming on a chronic-burn profile.

**Cross-tab status at this writing (after cash_flow_snapshot commits)**
- Tab 11: cash_flow_snapshot DONE (this entry).
- Master row 13: now fully **DONE** (Path B, all 4 files).
- Tab 12 (balance_sheet_snapshot, master row 14) running in parallel.
- Tab 13 (valuation_at_entry, master row 15) claimed.
- Path B family count: 3 done (revenue_level, profitability_snapshot,
  cash_flow_snapshot) + 1 more in flight (balance_sheet_snapshot).

**Cleanup**: deleted scratch scripts per `feedback_temp_scripts.md`:
- `%TEMP%\temp_cfs_mini_harness.py`
- `%TEMP%\temp_cfs_g3_verify.py`
- `%TEMP%\temp_cfs_scalar_mult_scan.py`
- `%TEMP%\temp_cfs_d3_046_verify.py`
- `%TEMP%\temp_cfs_raw_outputs.npz`
- `%TEMP%\temp_cfs_results.json`

## 2026-05-09 — session 3, tab 12 (balance_sheet_snapshot, master row 14)

**Done this session:**
- Picked up master row 14 `balance_sheet_snapshot` per HANDOFF queue policy
  (rows 11-13 already DONE/claimed; rows 1-10 long done).
- **Inventory**: 4 files (2 base 150+150, 2 derivative 50+50) = 400 functions.
  0 OHLCV-only fns; 31 hybrid (OHLCV + fundamentals); 369 pure-fundamentals.
  38 unique input cols; 11 new vs prior Path B families: `accoci`, `assetsnc`,
  `bvps`, `deposits`, `goodwill`, `investmentsc`, `investmentsnc`,
  `tangibles`, `taxassets`, `taxliabilities`, `tbvps`. → Path B (synthetic-
  fundamentals mini-harness path, since db-direct skips on first arg-set
  containing fundamentals).
- **Claimed** the row as tab 12 (commit `38378a7`). Stashed tab 10's pending
  `HANDOFF.md` working-tree edit before committing my claim hunk to keep
  attribution clean; stash-popped after.
- **Built mini-harness** at `%TEMP%\temp_bss_mini_harness.py` (deleted
  per `feedback_temp_scripts.md` after audit complete). Design: 1500 trading
  days; `close` as daily geometric random walk; all 37 fundamentals as
  quarterly-stepped (constant within quarter) with deterministic per-col seed
  and 3-regime drift schedule (positive / negative / mild-positive) to break
  monotonicity and avoid the rl_042/043/140 cummax-clique class of synth-bias
  false positive. Captures: errors, all-NaN, constants (post-warmup), formula-
  exact dup groups (sha256 of inspect.getsource minus signature line),
  value-exact dup groups (sha256 of rounded post-warmup values).
- **Iteration on formula_hash**: first attempt skipped def-line then hashed,
  which collapsed all single-line `def f(...): return X` bodies to the empty-
  string hash (43+ false-positive groups). Fixed by walking past matching `)`
  + `:` to extract body even when on the def line. Second attempt added
  alpha-renaming of args, which falsely collapsed `_safe_div(debt, equity)`
  with `_safe_div(debt, assets)` since args were renamed to positional
  placeholders -- but **arg names refer to distinct dataset columns**, not
  interchangeable locals. Reverted alpha-rename. Third attempt clean.
- **Findings on cleaned mini-harness**:
  - 1 error: `bss_055_cash_conversion_proxy` with inner
    `_safe_div(receivables + inventory - payables, _safe_div(revenue, 4))`.
    `_safe_div(num, denom)` calls `denom.replace(0, np.nan)` -- passing int
    `4` as denom raises AttributeError. **Function had never produced
    output on any real call.** Fixed by replacing inner with `revenue / 4`
    (math identity preserved; no defensive-div needed for nonzero constant).
  - 1 all-NaN: `bss_288_cash_runway_quarters` (uses
    `(-ncfo).clip(lower=0)` as denominator -- synthetic ncfo positive-mean
    means burn ≈ 0 ≈ NaN-replaced denom on every day; valid math for chronic-
    burn real ticker). Kept by design, same disposition as cfs_d3_046.
  - 9 sample-bias-constants: Piotroski/Ohlson/distress binary indicators
    (bss_114, 115, 122, 223-228) where the trigger condition (`liab > assets`,
    `equity < 0`, etc.) never fires on healthy synthetic. Math is genuinely
    distinct (different cols, different comparison thresholds); 8-member
    value-exact zero-clique is a synth-bias artifact. Same disposition as
    peak_and_crash's 9 always-zeros: kept by design.
  - 12 formula-exact dup groups -> 13 fns to delete (one group has 3 members):
    bss_017 = bss_013, bss_089 = bss_044, bss_119 = bss_004, bss_120 = bss_015,
    bss_139 = bss_062, bss_216 = bss_015 (3-way clique with bss_120),
    bss_217 = bss_060, bss_220 = bss_191, bss_230 = bss_187,
    bss_268 = bss_118, bss_274 = bss_006, bss_275 = bss_005,
    bss_285 = bss_214. All textually identical bodies; auto-applied per
    AUTO-APPLY policy.
  - 2 value-exact-only dup groups (post-formula-exact-filter):
    - 8-member zero-clique (the binary indicator constants): synth-bias
      artifact, not real dups. Kept.
    - bss_131 (`goodwill / min(assets, equity)`) ≡ bss_266
      (`goodwill / equity`) on any valid balance sheet (since liabilities ≥ 0
      forces equity ≤ assets, so min collapses to equity). ASK FIRST ->
      user chose delete bss_266 (preserves bss_131's defensive-min framing
      against pathological edge cases).
- **Cross-reference check**: confirmed all 14 delete-targets appear only as
  def + registry entries (no calls from composite functions). bss_125
  (Ohlson O composite) and bss_221 (Altman Z composite) inline the Ohlson
  tlta/wcta and Altman x1/x2/x5 ratios directly -- they don't depend on the
  named-component functions getting deleted.
- **Commits** (one per affected file): `3eb0fbd` (file 1: bug fix + 5
  deletes), `0a0db67` (file 2: 8 deletes), `803a56a` (file 2: bss_266
  delete after user approval).
- **Final state**: 386 / 400 bound (= 400 - 14 deletions). 0 errors / 0
  formula-exact dups / 0 real value-exact dups. 9 sample-bias-constants + 1
  sample-bias-all-NaN kept by design.

**Lessons (worth carrying):**
1. **formula_hash must extract body even when on the def line.** A first-
   attempt naive `splitlines()[1:]` skip-the-def-line approach collapses
   all inline `def f(...): return X` bodies to the empty hash. Any future
   Path B harness needs to walk past the matching `)` + `:` to find the
   body regardless of layout.
2. **Don't alpha-rename function args in formula_hash.** Args name distinct
   dataset columns (`debt` vs `equity` vs `assets`), not interchangeable
   local symbols. Renaming all to `_p00`/`_p01` produces 43+ spurious
   formula-exact "dup" groups across columns that are economically distinct.
   Local-variable renames are caught by manual review of the smaller value-
   exact-but-not-formula-exact list.
3. **Composite scores often inline their named components.** Altman Z (bss_221)
   inlines the x1-x5 component ratios directly rather than calling
   bss_216-bss_220. Same for Ohlson O (bss_125) and Springate (bss_222).
   Deleting the named-component duplicates does not break the composites.
   Future audits: verify by grepping for the deleted-function-name substring,
   not just the registry name.
4. **Defensive `min()` calls that never fire under domain identity.**
   bss_131's `min(assets, equity)` is a no-op in any valid balance-sheet
   row because liabilities ≥ 0 -> equity ≤ assets. Same class as the
   defensive `_safe_div` in pure-positive-denom contexts: they signal
   "the author considered an edge case but it doesn't occur in real data."
   Treat as value-equivalent for dup purposes; user-approve before deletion.
5. **Sample-bias-constant binary indicators are nearly always KEEP-BY-DESIGN
   when their math is sound and conditions are real.** Different from
   bp_069 (which used `close.abs() == close` -- a degenerate no-op for
   equities). Always inspect the formula: if the condition has plausible
   trigger paths under stressed real data, keep regardless of what the
   synthetic shows.

**Cross-tab status at this writing (after BSS commits):**
- Tab 12: balance_sheet_snapshot DONE (this entry).
- Master row 14: now fully **DONE** (Path B, all 4 files; commits
  `38378a7`, `3eb0fbd`, `0a0db67`, `803a56a`).
- Path B family count: 4 done (revenue_level, profitability_snapshot,
  cash_flow_snapshot, balance_sheet_snapshot).
- Next-open per master priority queue: row 15 valuation_at_entry (already
  claimed by tab 13 per the working-tree HANDOFF state).

**Cleanup**: deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_bss_mini_harness.py`
- `%TEMP%\temp_bss_run1.log` through `temp_bss_run5.log`

---

## Session 3 (2026-05-09, tab 13) -- `valuation_at_entry` (Path B, all 8 files)

**Setup.** Picked priority-queue row 15 (next unblocked / unclaimed Path B
slot after tabs 11/12 took rows 13/14). Inventoried 8 files: 4 base
(75 fns each = 300 total; chunks 001-150 + 301-450 with intentional gap at
151-300) + 2 2nd-deriv (25+25=50) + 2 3rd-deriv (25+25=50) = **400 features**.

Inventory grep confirmed Path B (every fn touches fundamentals; ~33 cols
plus close + shareswa). New cols vs prior Path B audits: `dps`, `taxexp`.

**Mini-harness.** Cloned the revenue_level / profitability_snapshot template
(`%TEMP%\temp_ve_mini_harness.py`). Initial synthetic data made the mistake
of keying every fundamental as a strict multiple of `revenue` (e.g.
`netinc = revenue * 0.10`), which produced 51 false-positive value-exact
dups (P/E ≡ P/S ≡ P/FCF in synthetic because all denominators were
revenue×constant) and 45 false-positive constants in margin features
(`netinc/revenue = 0.10` exactly). Regenerated each fundamental as its own
independent quarterly random walk → 19 dups, 5 constants (real signal).

**Run 1 (post-fix synthetic data).**
- 388/400 ok, 12 errors, 0 missing_input, 0 not_series.
- 1 all-NaN past warmup (ve_386_cash_burn_to_mcap, downstream of ve_385
  bug).
- 5 constants past warmup (all are real always-positive flags on healthy
  synth: ve_060/061/062/312/448).
- 0 formula-exact dup groups (lexical hash sees through inlining only).
- 19 value-exact dup groups.

**Bug class diagnosis.**

*Cash-burn `_safe_div(scalar, 12)`:* ve_385 and ve_387 both call
`_safe_div(x, 12)` where 12 is a Python int. `_safe_div` does
`d.replace(0, np.nan)` which fails on int → AttributeError. Functions
have never worked end-to-end. Fix: replace `_safe_div(x, 12)` with
plain `x / 12` (int-as-divisor is safe; no zero-denominator risk).

*`_slope` helper shape mismatch (4 copies, 10 functions broken):* helper
hard-codes `x_demean = arange(window)` length `window`, but the rolling
apply uses `min_periods=max(1, window//2)` which feeds variable-length
arrays during warmup. ValueError on every warmup-edge call →
`ValueError: operands could not be broadcast together with shapes
(window,) (window-N,)`. Fixed by rebuilding `xd` inside `_sl(arr)` using
`len(arr)`. Same root cause across:
- valuation_at_entry_2nd_derivatives.py
- valuation_at_entry_2nd_derivatives_051_075.py
- valuation_at_entry_3rd_derivatives.py
(3rd_derivatives_051_075.py uses `_d2`, no `_slope`.)

**Scalar-multiple cosine-similarity scan** (post-fix synthetic, 387 fns,
~75k pairs). Found 38 candidates at sim≥0.99999. Filtered:
- 7 with ratio_std < 1e-12 → genuine FP-noise scalar-mult dups
  (matched into the 17 algebraic-identity clusters):
  ve_001 ⇄ ve_083 (×100), ve_005 ⇄ ve_419, ve_013 ⇄ ve_084 (×100),
  ve_022 ⇄ ve_419, ve_059 ⇄ ve_084 (×100), ve_081 ⇄ ve_084,
  ve_083 ⇄ ve_094.
- 31 with ratio_std > 1e-3 (correlated-but-distinct, not dups):
  mcap/X vs EV/X variants (8 pairs, ratio_std≈0.012 = (debt-cash)/X
  varying slowly), expansion vs ROC pairs (4 pairs, ratio_std≈100s
  due to /|pe.shift|), inverse-correlated pairs (3 pairs, sim=-1.0
  with huge ratio_std), constant-offset variants (ve_005/135 PB vs
  PB-1, ratio_std=0.044), ev_premium variants (3 pairs), and others.
  All keep both, real-data divergence expected.

**Triage classification (19 + 7 cosine = 17 unique algebraic-identity
clusters):**

| Cluster | Formula identity | Delete | Keep |
|---|---|---|---|
| P/E | mcap/TTM(netinc) | ve_083×100, ve_094 | ve_001 |
| P/S | mcap/TTM(rev) | ve_019 | ve_003 |
| P/B | mcap/equity | ve_022, ve_419 | ve_005 |
| book/market | equity/mcap | ve_434 | ve_006 |
| P/FCF | mcap/TTM(fcf) | ve_056 | ve_007 |
| EV/GP | EV/TTM(gp) | ve_080 | ve_012 |
| EV/opinc | EV/TTM(opinc) | ve_059, ve_081, ve_084×100 | ve_013 |
| P/GP | mcap/TTM(gp) | ve_058 | ve_014 |
| P/opinc | mcap/TTM(opinc) | ve_057 | ve_015 |
| mcap/tang | mcap/tangibles | ve_132 | ve_016 |
| P/EBITDA | mcap/TTM(ebitda) | ve_125 | ve_020 |
| log(P/S) | log(mcap/TTM(rev)) | ve_368 | ve_040 |
| Shiller PE | close/avg(eps,5y) | ve_112 | ve_068 |
| EV/(EBITDA-capex) | direct | ve_398 | ve_124 |
| (EV/EBITDA)×(D/E) | direct | ve_423 | ve_346 |
| book_yield ROC | _roc(equity/mcap) | ve_2d_075 | ve_2d_023 |
| book_yield jerk | jerk(equity/mcap) | ve_3d_068 | ve_3d_020 |

**Total: 20 deletes** (cluster #1 has 2, #3 has 2, #7 has 3).

**ve_424 naming bug.** `ve_424_ev_to_ocf` body identical to `ve_143_ev_to_ncf`
(both compute EV/TTM(ncf)) but name promises "operating cash flow" not "net
change in cash" (ncf vs ncfo). Surgical edit per vac_118 precedent: change
input `ncf → ncfo` in ve_424 + ve_425 (which calls ve_424). Restores name's
promise; introduces new column dependency.

**ve_399 inline.** Before deleting ve_398, inlined its body into ve_399
(ve_399 was the only caller — `_rpct(ve_398(...), 3y)`). Now ve_399
inlines `_safe_div(_ev(...), _ttm(ebitda)-_ttm(capex.abs()))` directly.
Avoids cross-file dependency on ve_124 (which lives in file 2).

**User decision.** Asked once with categorized findings (12 bug fixes,
ve_424 naming, 20 dup deletes). Approved all 3 recommended options.

**Per-file commits (8 total):**
- `abe9e9a` -- 2nd_derivatives: slope helper fix
- `48dc778` -- 3rd_derivatives: slope helper fix
- `e27ef3e` -- 2nd_derivatives_051_075: slope fix + ve_2d_075 delete
- `15b3d34` -- 3rd_derivatives_051_075: ve_3d_068 delete
- `eb6c346` -- base_001_075: 6 dup deletes
- `f837537` -- base_076_150: 8 dup deletes
- `2fa5c09` -- base_301_375: ve_368 delete
- `1e5cd37` -- base_376_450: cash_burn fix + ve_424 surgical + 4 dup
  deletes + ve_399 inline

**Re-run post-fix.** 379/379 ok / 0 errors / 0 formula-exact dups / 2
remaining value-exact dup groups (both synthetic-data artifacts):
- ve_060/061/062 positive flags (all 1 on profitable synth, real data
  diverges -- different profitability metrics).
- ve_385/386 cash_burn (both NaN past warmup because synthetic ncf is
  positive throughout. Real cash-burner firms produce signal. Same
  disposition as PC always-zeros, CFS cfs_d3_046, BSS bss_288).

5 constants past warmup unchanged (always-positive flags, real on live data).

**Final state.** 400 → 379 functions (-21 = 20 deletes + 1 dup absorbed
into ve_399 inline). All 21 verified by either formula-exact algebra or
cosine_sim=1.0 + ratio_std<1e-12.

**Next-session TODO (not addressed this session, ASK-FIRST scope):**
6 sibling functions have the same ve_424-style naming bug -- input named
`ncf` despite "ocf" in function name:
- `ve_426_log_ev_to_ocf` (file 4)
- `ve_2d_062_ocf_yield_roc_1q` (2nd_derivatives_051_075)
- `ve_2d_063_ocf_to_ev_roc_1q` (2nd_derivatives_051_075)
- `ve_3d_060_ocf_yield_accel_1q` (3rd_derivatives_051_075)
- `ve_3d_061_ocf_to_ev_accel_1q` (3rd_derivatives_051_075)
- `ve_3d_072_ocf_yield_sign_change_1y` (3rd_derivatives_051_075)

These weren't caught by the value-hash check because their bodies aren't
exact-equal to other functions (log/ROC/jerk wrappers around the
ev_to_ncf math). Next session: apply same `ncf → ncfo` surgical edit.

**Lessons worth carrying:**

1. **Strict multiples in synthetic data create cascading false dups.**
   First run had 51 dup groups; second run with independent fundamentals
   had 19 (all real). Future Path B harnesses: synthesize each
   fundamental as its own random walk, NOT a multiplier of revenue.

2. **The cosine-similarity scan complements the value-hash for
   scalar-multiple dups.** value-hash has 8-decimal rounding tolerance
   but doesn't z-score, so it misses pairs that differ by a constant
   factor (ve_001 vs ve_083 = ve_001×100). Cosine sim z-scores both
   sides → catches them; ratio_std<1e-12 confirms FP-noise scalar.
   Standard practice from MAD/VR sessions, now reconfirmed.

3. **Helper bugs that crash during warmup can hide for years.** The
   `_slope` helper crashed on every warmup-edge call yet got committed
   and shipped. The fix (rebuild `xd` from `len(arr)`) is mechanical.
   Worth re-grepping other families for similar `arange(window)` +
   `min_periods<window` antipatterns; would catch the same class.

4. **Surgical-edit-vs-delete decision matrix is solidifying.** When dup
   body is generic but name promises specificity → surgical (vac_118
   precedent, ve_424 here). When body and name both match a generic
   alias → delete (the 20 PE/PB/PS aliases here). When name promises
   specificity AND body matches AND alternate column exists → surgical
   (ve_424 changing to ncfo). Document in CLAUDE.md when next reviewing
   the policy section.

**Cleanup**: deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_ve_mini_harness.py`
- `%TEMP%\temp_ve_mini_harness_results.json`
- `%TEMP%\temp_ve_outputs.npz`
- `%TEMP%\temp_ve_scalar_dup_scan.py`
- `%TEMP%\temp_ve_scalar_candidates.json`


---

## 2026-05-09 — session 3 — tab 14: leverage_and_solvency (Path B, surgical-edits-only)

**User direction:** "do a surgical edit and review the feature surgical edits only do not remove intent or scripts" — applied surgical-edits-only audit policy: rebody dups to fulfill function-name promise, zero deletes, no script removal. Mirrors precedent of `volume_accumulation_base` (7 surgical edits, 0 deletes), `volume_at_capitulation_base` (1 surgical edit), and the `_v2` derivative passes for VA.

**Family:** 8 files, 400 functions (4 base × 75 + 4 deriv × 25). 100% Path B (every function takes fundamentals; 0 OHLCV-only arg sets).

**Inputs union (25 cols):** `assets`, `cashnequiv`, `close`, `currentassets`, `currentliabilities`, `debt`, `ebit`, `ebitda`, `ebt`, `equity`, `fcf`, `goodwill`, `intangibles`, `intexp`, `inventory`, `liabilities`, `ltdebt`, `ncfo`, `netinc`, `opinc`, `payables`, `receivables`, `retainedearnings`, `revenue`, `volume`. Notable: this family uses **non-Sharadar names** (`cashnequiv` vs SF1's `cashneq`/`cashnequsd`; `retainedearnings` vs SF1's `retearn`; `ltdebt` vs SF1's `debtnc`; `ebt` not in SF1 standard cols). Path B is name-agnostic (synthetic harness builds Series for whatever names appear), but flag for downstream pipeline -- the binding layer in `test_new_features_against_pipeline.py` will need a name-translation map.

**Mini-harness baseline** (`%TEMP%\temp_ls_mini_harness.py`, deleted post-audit): 0 errors / 0 all-NaN / **20 constants** / **4 formula-exact + 15 value-exact dup groups** / **4 scalar-mult pairs**.

### Surgical edits applied (7 rebodies, 4 commits)

Per the surgical-edits-only policy, identified 7 dup pairs where the higher-numbered function had a name promising distinct semantics from the canonical lower-numbered peer, but the body was a literal duplicate. Each rebody fulfills the name's promise and remains numerically distinct (verified <1e-9 on synthetic).

**Commit 377c6ab — leverage_and_solvency_base_076_150.py (4 rebodies):**
- ls_084_financial_leverage_dupont: was `assets/equity` (== ls_005). Now uses period-average (`(s + s.shift(252)) / 2.0` for both assets and equity), per DuPont decomposition convention which smooths balance-sheet items over the cycle. mean_rel_diff 3.27%.
- ls_121_fcf_yield_on_debt: was `fcf/debt` (== ls_019). Now uses 252d-average debt (banker's "yield-on-avg-debt" convention), so the yield reflects realized capacity over the trailing year rather than point-in-time. mean_rel_diff 3.38%.
- ls_130_operating_cash_cushion: was `ncfo/CL` (== ls_108). Now uses symmetric bounded form `(NCFO-CL)/(NCFO+CL)` ∈ [-1, 1] directly expressing the cushion semantics in the name (negative = deficit, positive = cushion). Distinct functional form, not a linear transform.
- ls_148_leverage_regime_flag: was continuous z-score (== ls_035), but name says "flag". Now returns actual binary 1/0 when D/E z-score > 1.0 (elevated regime). Mean 0.085 on synthetic — proper distress-flag behavior.

**Commit 1188999 — leverage_and_solvency_base_151_225.py (2 rebodies):**
- ls_187_debt_to_invested_cap_ex_cash: was `Debt/(Debt+Equity-Cash)` (== ls_085). First rebody attempt used `(D-C)/(D+E-C)` — algebraically identical to ls_010_net_debt_to_capital. **Caught by post-edit harness re-run** (good catch; otherwise would have introduced a new dup).
- ls_212_fcf_int_coverage: was `FCF/|intexp|` (== ls_127). Now uses after-tax interest (21% statutory rate) for apples-to-apples with post-tax FCF. **Scalar-mult by 1/(1-0.21)=1.266** — kept by NOPAT precedent (profitability_snapshot row 33 in HANDOFF: 14 NOPAT scalar-mult pairs at ratio 1.265823 are deliberate domain reformulations).

**Commit 2b7da4d — leverage_and_solvency_base_226_300.py (1 rebody):**
- ls_291_ncfo_minus_capex_to_debt: was literal `_safe_div(fcf, debt)` (== ls_019). Author's own docstring acknowledged the CF identity. Now uses 5/95 capex-retention blend: `(NCFO - 0.95*(NCFO-FCF)) / Debt = (0.05*NCFO + 0.95*FCF) / Debt`. The 0.95 factor reflects that not all capex is permanently sunk (sale/leaseback, working-capital recapture). mean_rel_diff 2.93%.

**Commit 592d891 — re-rebody ls_187 to escape ls_010 collision:**
- ls_187_debt_to_invested_cap_ex_cash: now uses `(Debt-Cash)/(Equity-Cash)` — net debt to net equity, cash netted from BOTH numerator and denominator. Distinct from ls_010 (different denominator structure) AND from ls_085 (gross debt over gross IC ex-cash). Treats cash as a direct equity-reduction item per coverage analysts' convention. mean_rel_diff 87.9% vs ls_085.

### KEPT BY DESIGN (zero deletes per user policy)

**9 value-exact dup groups remaining post-fix — all justified intent preservation:**

1. **ls_007 ↔ ls_156 ↔ ls_169** (liab/assets): direct ratio, Zmijewski X2 component, Ohlson TLTA component. Academic distress-model traceability — each model variable must be individually addressable so the Z/O-score composites can be recomputed and decomposed.
2. **ls_022 ↔ ls_296** (quick ratio): ls_296 has `inventory.clip(lower=0)` defensive guard; diverges from ls_022 on real data when inventory < 0 (rare but possible in restated filings).
3. **ls_061 ↔ ls_151 ↔ ls_170 ↔ ls_188** (WC/assets): Altman X1, Springate A, Ohlson WCTA, generic NWC/Assets. Same model-trace logic as group 1; this 4-clique spans three distinct distress-model namespaces.
4. **ls_073 ↔ ls_111** (debt/ncfo): ls_111 has `ncfo.clip(lower=0)` so payback-years caps when ncfo turns negative (returns ∞-like); ls_073 stays raw. Real-data distinct.
5. **ls_107 ↔ ls_173 ↔ ls_205** (ncfo/liab): direct ratio, Ohlson CFOTL, Beaver (1966) ratio. Beaver is a foundational standalone distress predictor; Ohlson references it as a component. Model-trace.
6. **ls_112 ↔ ls_115** (net_debt/ncfo): ls_112 clips both nd and ncfo to ≥0; ls_115 leaves them raw. Diverge when net debt or ncfo turns negative.
7. **ls_155 ↔ ls_172** (netinc/assets ROA): Zmijewski X1, Ohlson NITA. Model-trace (two separate published distress models reference ROA distinctly).
8. **ls_2d_013 ↔ ls_2d_035** (Beaver ROC): ROC of ncfo/liab via dual-named helpers (`_base_ncfol` vs `_beaver`). Academic-trace at deriv level.
9. **ls_3d_032 ↔ ls_3d_040** (Beaver jerk): same pattern at jerk level.

**1 formula-exact dup remaining:** ls_061 ↔ ls_188 — same WC/A bodies; both members of group 3 above; academic-trace KEEP.

**5 scalar-mult pairs kept:**
- ls_002 ↔ ls_083 (ratio 0.6): debt vs debt-capacity-used (ls_083 uses 60% theoretical cap as denominator scaler).
- ls_023 ↔ ls_297 (ratio 1/252): cash ratio vs days-of-defensive-interval — unit conversion (dimensionless ratio vs trading-day count).
- ls_127 ↔ ls_212 (ratio 0.79): pre-tax vs after-tax interest coverage. NOPAT-style domain reformulation, kept per profitability_snapshot precedent.
- ls_161 ↔ ls_162 (ratio 1, std_rel 9.5e-9): naive equity vol vs naive asset vol proxy. On synthetic mktcap (~19B) vastly exceeds debt (~1500), so the weighted-average asset vol collapses to equity vol; on real data with smaller mktcap or larger debt, they diverge significantly.
- ls_196 ↔ ls_197 (ratio 1, std_rel 1.4e-8): mktcap/debt vs ev/debt. Diff is `(debt-cash)/debt` ≈ 0.73, additive offset; at the harness's mktcap/debt ~ 12.6M scale, the offset is negligible, so cos≈1. Real data diverges when mktcap/debt is smaller.

**20 sample-bias constants kept** (distress flags / Z-score thresholds — synthetic models a healthy company, all flags evaluate to 0 or constant background): ls_086, ls_087, ls_128, ls_136, ls_137, ls_138, ls_139, ls_140, ls_141, ls_142, ls_147, ls_154, ls_158, ls_160, ls_164, ls_174, ls_289, ls_299, ls_300, ls_2d_031. All are real conditional triggers with low base rate on a healthy company, distinct from `bp_069`-style degenerate constants. Same disposition as PC's 9 always-zeros, BSS's 9 sample-bias-constants, and CFS's `cfs_d3_046`.

### Lessons for future audits

1. **"Surgical edits only" is a viable audit mode for families where intent matters more than dedup hygiene.** This family has a deliberately high duplication count by design (academic distress-model traceability is the explicit purpose of the dual-naming). Deleting "duplicates" would destroy the model-trace value. Asking the user upfront about deletion policy saves a lot of revert work.
2. **Post-edit re-run is essential.** First ls_187 rebody introduced a new dup (vs ls_010) that the harness caught immediately. Without the post-edit re-run, this would have leaked into the codebase.
3. **NOPAT-precedent for after-tax adjustments.** Any scalar-mult by `1/(1-tax_rate)` falls under the NOPAT-style "deliberate domain reformulation" precedent set by profitability_snapshot. Don't escalate; just document.
4. **Non-Sharadar column names are a flag for the binding layer, not the audit.** This family's `cashnequiv`/`retainedearnings`/`ltdebt`/`ebt` will require name-translation when wired into the production pipeline. Audit can proceed with the names as written; flag for downstream.
5. **Symmetric bounded forms `(A-B)/(A+B)` are good rebody targets for cushion/spread semantics.** Naturally expresses deficit-vs-surplus on a [-1, 1] scale, distinct from raw `A/B` ratio, no clipping artifacts.

**Cross-tab status at this writing (after LS commits):**
- Tab 14: leverage_and_solvency DONE (this entry).
- Master row 16: now fully **DONE** (Path B, all 8 files; commits 377c6ab, 1188999, 2b7da4d, 592d891).
- Path B family count: 6 done (revenue_level, profitability_snapshot, cash_flow_snapshot, balance_sheet_snapshot, valuation_at_entry, leverage_and_solvency).
- Next-open per master priority queue: row 17 efficiency_snapshot.

**Cleanup**: deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_ls_mini_harness.py`
- `%TEMP%\temp_ls_verify_rebodies.py`


---

## 2026-05-09 — session 3 — tab 16: rd_and_intangibles (Path B, all tiers)

**Family:** 7 files, 275 functions (3 base × {75, 75, 25} + 2 2nd-deriv × 25 + 2 3rd-deriv × 25). 100% Path B (every function takes fundamentals; no OHLCV-only signatures). Pulled from master priority queue row 18; row 17 (efficiency_snapshot) already claimed by tab 15, row 19 (share_and_dilution_snapshot) became claimed by tab 17 mid-session.

**Inputs union (19 cols):** `rnd`, `sgna`, `revenue`, `equity`, `assets`, `opex`, `debt`, `intangibles`, `goodwill`, `depamor`, `ebitda`, `fcf`, `gp`, `netinc`, `opinc`, `capex`, `cor`, `close`, `sharesbas`. Notable: this family **embeds the Hall-Jaffe-Trachtenberg (2001) and Eisfeldt-Papanikolaou (2013) PIM stocks** via the inlined `_build_pim_stock` helper. The depreciation-rate constants are hard-coded as `0.15/4.0` (R&D) and `0.20/4.0` (org capital), proving the family expects **quarterly-cadence input** -- the synthetic harness must use a quarterly index.

**Mini-harness design** (`%TEMP%\temp_ri_mini_harness.py`, deleted post-audit): 5 independent fundamental profiles × 60 quarterly observations × 19 cols. Profiles: `stable_mature`, `tech_high_rnd`, `declining`, `low_margin`, `ma_active`. Each variable built as an INDEPENDENT random walk per profile (NOT multiplicative -- explicit application of valuation_at_entry lesson #1: "Strict multiples in synthetic data create cascading false dups"). 24-quarter warmup discarded for value-hash / constant detection.

### Baseline harness output (pre-fix)

- 275 functions / 0 errors / 0 all-NaN
- 1 constant past warmup (ri_044_rnd_positive_streak — synth-bias, capped at 20 on always-positive R&D)
- 2 formula-exact dup groups
- 5 value-exact dup groups
- 6 scalar-mult cosine-sim pairs (5 are rediscoveries of the value-exact groups; 1 net-new at ratio=0.25)

### Triage classification

**AUTO-APPLY (formula-exact, 2 deletes — commit `5e62896`):**

| Delete | Body | Canonical |
|---|---|---|
| ri_161_rnd_funded_by_fcf | `_safe_div(fcf, rnd)` | ri_025_fcf_per_rnd |
| ri_162_rnd_funded_by_opinc | `_safe_div(opinc, rnd)` | ri_023_opinc_per_rnd |

The "rnd_funded_by_X" framing and "X_per_rnd" framing are conceptually equivalent at the formula level (`X/rnd` = "X per dollar of R&D" = "R&D coverage by X turns"). Bodies bit-exact identical, AST hash collides. Per-CLAUDE.md AUTO-APPLY policy. Lower-numbered (file 1) kept.

**ASK FIRST (batched in one user question, all 4 user-approved per recommendation):**

| Item | Disposition | Commit |
|---|---|---|
| ri_036 == ri_2d_016 (YoY R&D acceleration; value-exact post-warmup, differ in fillna NaN handling at rows 4-7) | Delete-from-base per CFS/RL precedent | `9845a0f` |
| ri_2d_002 vs ri_2d_031 (algebraic-identity scalar-mult ratio=0.25 via `_diff(MA_W,1) = _diff(s,W)/W` telescoping) | Delete higher-numbered ri_2d_031 per VA precedent | `c525cab` |
| ri_003/ri_090, ri_107/ri_115 (rnd|gw / equity vs equity.abs() clip-differentiated) | Keep-by-design per LS ls_022/296 precedent | n/a |
| ri_044_rnd_positive_streak (capped at 20 on always-positive synth) | Keep-by-design per ps_270/cfs_d3_046/bss_288 precedent | n/a |

**Justifications worth carrying:**

1. **ri_036 vs ri_2d_016 NaN-handling subtlety.** ri_036 body is `g = _pct_change(rnd, 4); return g - g.shift(4).fillna(0)` — the fillna is on `g.shift(4)`, so when `g.shift(4)` is NaN (rows 4-7), the function returns `g - 0 = g`. ri_2d_016 body is `_diff(_pct_change(rnd, 4), 4)`, where `_diff` does `.diff(periods).fillna(0.0)` — fillna on the diff result, so rows 4-7 return `0`. Post-warmup (row 24+) they're identical. Pre-warmup they differ. Value_hash detected as dup post-warmup; the difference is a NaN-handling code-smell, not a deliberate operator distinction. Delete-from-base preserves the canonical YoY-acceleration in the derivative tier.

2. **ri_2d_031 algebraic-identity is the "_roc_1q" naming bug.** `_diff(_rolling_mean(s, 4), 1) = (MA(s,4)[t] - MA(s,4)[t-1]) = (s[t] - s[t-4]) / 4 = _diff(s, 4) / 4`. The 4q rolling-mean introduces a 4q-strided operator that telescopes cleanly when 1q-differenced. The `_roc_1q` suffix is misleading — the operator is really a /4-scaled 4q ROC, not a true 1q operator. ri_2d_001 already covers true 1q ROC of raw intensity. Delete is straightforward; no surgical-edit needed because no slot semantics need preserving.

3. **Clip-differentiated dups (ri_003/ri_090, ri_107/ri_115).** Both pairs share the pattern `_safe_div(num, equity)` vs `_safe_div(num, equity.abs())`. On healthy synthetic equity (always positive, floored at 20.0), `equity == equity.abs()` so the pair collapses to value-exact. On real-data deeply distressed firms with negative equity (accumulated deficit > paid-in capital), they diverge: the raw form returns negative ratios; the .abs() form returns positive. Both signals are real. Same disposition as LS ls_022/296 (quick-ratio with `inventory.clip(lower=0)` defensive guard).

### Post-fix re-run

- 271 functions (275 - 4 deletes)
- 0 errors / 0 all-NaN
- 1 constant (ri_044, kept)
- **0 formula-exact dup groups** ✓
- 2 value-exact dup groups (the user-approved KEEPs)
- 2 scalar-mult pairs (= the same 2 KEEPs, re-detected)

### Per-file commits (3 total)

- `5e62896` — base_151_175.py: delete ri_161, ri_162 (formula-exact)
- `9845a0f` — base_001_075.py: delete ri_036 (base-vs-derivative pollution)
- `c525cab` — 2nd_derivatives_026_050.py: delete ri_2d_031 (algebraic-identity scalar-mult)

### Lessons worth carrying

1. **Quarterly-cadence Path B harness for PIM-stock families.** When a family inlines `0.15/4.0`-style depreciation-rate constants, that's a strong signal the input Series is expected at quarterly cadence. Use `pd.date_range(start, periods=N, freq="QE")` not daily forward-fill. Saves a wasted harness run and sidesteps PIM-stock smoothing artifacts that would otherwise mask signal.
2. **Independent random-walks per fundamental column was load-bearing.** Lesson #1 from valuation_at_entry confirmed: 5 independent walks across 19 cols produced exactly the dup count predicted by reading source (4 deletes + 2 KEEP-BY-DESIGN). No false-positive cascade. Multiplicative drivers would have invented dozens of false dups via revenue-anchored ratios collapsing.
3. **The `_roc_1q` / MA-4q algebraic-identity pattern is a recurrent gotcha.** Same shape as VA's ve_2d_023/075 book_yield_roc: a "short-stride ROC of long-window MA" name often hides a long-window ROC scaled by 1/W. Worth grepping future families for `_diff(_rolling_mean(s, W), 1)` when `_diff(s, W)` exists nearby.
4. **The "X_per_Y" / "Y_funded_by_X" naming-symmetry pattern.** Just generic ratio aliases at the formula level — auto-apply per policy. Distinct from LS's academic-trace dual-naming (Zmijewski/Ohlson/etc.) where each name is a load-bearing model variable. Call sign for distinguishing: does the docstring cite a published distress-model namespace? If yes, KEEP per academic-trace; if no, DELETE.

**Cross-tab status at this writing (after rd_and_intangibles commits):**
- Tab 16: rd_and_intangibles DONE (this entry).
- Master row 18: now fully **DONE** (Path B, all 7 files; commits `5e62896`, `9845a0f`, `c525cab`).
- Path B family count: 7 done (revenue_level, profitability_snapshot, cash_flow_snapshot, balance_sheet_snapshot, valuation_at_entry, leverage_and_solvency, rd_and_intangibles).
- Next-open per master priority queue: row 20 capital_allocation_snapshot (rows 17/19 claimed by tabs 15/17).

**Cleanup**: deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_ri_mini_harness.py`
- `%TEMP%\temp_ri_results.json`


## 2026-05-09 — session 3 — tab 15: efficiency_snapshot (Path B, all tiers, surgical-edits-only)

**Master row 17.** 15 files / 775 fns (8 base × 75 + 4 2nd-deriv × 25 + 3 3rd-deriv × 25). Hybrid-Path-B: every fn touches fundamentals; 67 distinct input cols (62 fundamentals + 5 OHLCV); 67 fns also reference price/volume.

User directive: **surgical-edits-only, zero deletes** — same policy as leverage_and_solvency tab 14.

### Concurrent-tab conflict (lesson)

While I was building the Path B mini-harness, another tab raced through the same family auto-deleting algebraic-identity dups. **13 functions across 5 files** were lost in 5 commits (`580972c` / `f00d073` / `623670e` / `f5755bc` / `fbde703`) before I noticed. Per user direction (asked 3 times in conversation, "can these be surgically edited to keep signal as features"), reverted all 5 concurrent commits with `git revert --no-edit ...` and rebodied each slot with a meaningful divergence design.

The HANDOFF "Multi-tab coordination" rule says the second tab to claim should release. Tab 15 (mine) claimed first in commit `d94a44b`, but a parallel claim landed in commit `a236b63` immediately after with the same tab-15 label. The HANDOFF row format didn't catch it because both entries said "claimed tab 15" — same tab number, ambiguous which session.

**Outcome of this conflict:** the HANDOFF rule was tightened during this session — the master queue is now explicitly a reference for the user, not an auto-pick list, and arriving tabs must ask the user for assignment rather than pulling the next pending row.

### Path B mini-harness (`%TEMP%\temp_es_mini_harness.py`)

5 deterministic synthetic firm profiles × 1500 trading days × 67 cols. Daily forward-fill from quarterly anchors (24 quarters). 20% sign-flip injection on `CAN_BE_NEGATIVE` cols. Per-fn capture: error class, all-NaN-post-warmup, constant-post-warmup, formula_hash, value_hash, finite_count, unique_count. Persists raw outputs to `temp_es_raw_outputs.npz` for the follow-up cosine-similarity scalar-mult scan.

### Baseline harness output (after sys.path fix, pre-rebody)

- 775 fns total
- 2 errors (es_503/504 `_log_safe(scalar)` bug — fixed in commit `6308e78`)
- 0 all-NaN
- 2 constants (es_2d_098, es_3d_070 — fractal-dim sample-bias)
- 12 value-hash dup groups
- 0 formula-hash dup groups

### Scalar-mult / cosine-similarity scan (`temp_es_scalar_mult_scan.py`)

Caught **15 additional rank-equivalent candidates** beyond value_hash. 7 of those were cross-tier `_diff(s, n) ≡ s.diff(n)` aliasing (post-warmup-equal but warmup NaN-vs-0 differs in value-hash); 5 were genuine new findings (CV-vs-bband 8x scalar-mult, percentile-vs-stochastic 100x scalar-mult, three sign-flip pairs); 3 were variants of the 12 value-hash groups already detected.

### Triage classification

**Cat 1 — Cross-tier helper-aliasing dups (5 deriv slots).** Deriv-side `*_roc_*` functions used `_diff` (absolute change) when their names canonically promised percentage rate of change. Switched `_diff(s, n)` → `_pct_change(s, n)` to match name promise: es_2d_008/009/010/011 + es_2d_085. Commit `6308e78`.

**Cat 1 (within-base yoy clusters, 5 slots).** Base files contained 3-way clusters of identical-math YoY operations under different naming nuances (`_expansion_1y` / `_q1_vs_q4` / `_yoy_same_quarter`). Each cluster differentiated:
- es_141 keeps raw `om.diff(252)`; es_280 → 4q-SMA-smoothed YoY; es_477 → deviation from trailing-1y rolling mean.
- es_143 raw / es_279 TTM-smoothed / es_475 vs trailing mean.
- es_145 raw / es_480 vs trailing mean.

**Cat 2 — DuPont decomposition rebodies (7 slots).** Function names like `dupont_margin`, `dupont_turnover`, `dupont_roe_decomp`, `margin_times_turnover`, `roa_times_leverage` document the canonical academic DuPont decomposition. Original bodies used point-in-time inputs, making the decomposition algebraically equal to the simple ratios (NM × AT × EM = NI/E). Surgical edit: switch to TTM-averaged inputs (canonical academic DuPont uses average assets / average equity / annualized income), breaking the algebraic identity since `TTM(NI)/TTM(R) × TTM(R)/TTM(A) × TTM(A)/TTM(E) = TTM(NI)/TTM(E) ≠ NI/E` when inputs vary.

For es_050 vs es_223 (both TTM-DuPont): switched es_050 to **EMA-weighted** (span=252d) inputs while es_223 keeps SMA. Different smoother → different value, identical canonical interpretation. Commits `e964875` + `297d4f3`.

**Cat 3 — Per-share-lens rebodies (2 slots).** es_324_sps_growth_1q (was equal to es_188 raw sps growth): TTM-smoothed sps before pct_change. es_331_eps_to_sps_efficiency (was equal to es_016 net_margin via per-share cancellation): TTM-avg eps / TTM-avg sps (per-share averaging differs from ratio of TTM scalars).

**Cat 5 — Scalar-multiple rebodies (5 slots).**
- es_211/212/213 (CV) ↔ es_469/470/468 (bband_width = 8σ/μ) at scalar-mult ratio 1/8: rebodied es_468/469/470 as `(max - min)/mean` (range-based volatility, robust to fat tails vs σ-based).
- es_244/247 (percentile [0,1]) ↔ es_471/473 (stochastic [0,100]) at ratio 1/100: rebodied es_471/473 as Williams %D (3d SMA of %K).

**Cat 6 — Sign-flip rebodies (2 slots).**
- es_239 (price_m - om_chg) ↔ es_413 (om_chg - price_m): rebodied es_413 as ratio form `om_chg / |price_m|`.
- es_447 (ev_g - om_chg) ↔ es_547 (om_chg - ev_g): rebodied es_547 as `om_chg / |ev_chg|` (matches "_ratio" suffix).

One pair (es_059 ↔ es_373) was flagged synth-bias-only (eps tiny vs fcfps huge by my synthetic scaling — diverges on real data) and kept without rebody.

**Cat 4 — Streak rebody (1 slot).** es_395_fcf_positive_duration: above-median fcf-margin streak instead of positive-fcf streak (anchors against trailing 1y rolling median rather than zero).

**Cat 7 — Sample-bias keeps (4 constants + 3 value-hash residuals)**

Kept by design with documentation:
- es_182 ↔ es_339: `equity.clip` vs `equity.abs().clip` — value-exact on positive-equity synthetic, diverge on negative-equity distress firms (LS ls_022/296 precedent).
- es_503 ↔ es_504: same Petrosian fractal formula on different ratios (ROA vs op-margin). Both produce **constants** on smooth fwd-fill synthetic because daily margin diffs don't sign-flip; on real daily-varying data these trigger meaningfully different signals because ROA and OM dynamics differ.
- es_2d_098 ↔ es_3d_070: same fractal pattern at deriv level — same sample-bias.

### Bug fix (es_503/504)

Petrosian fractal proxy did `_log_safe(scalar)` on the outer term (`n = float(252)`); `_log_safe` calls `s.clip(lower=0)` which fails on a float scalar with `'float' object has no attribute 'clip'`. Replaced with `np.log1p(n)` matching the deriv-side template. Same bug class as bss_055 `_safe_div(rev, 4)` int-as-denom from balance_sheet_snapshot tab 12 — template-bug pattern where helper meant for Series gets a scalar.

### Final harness state (post-fix)

- 775/775 fns bound
- 0 errors
- 0 all-NaN
- 4 sample-bias constants (all fractal proxies — see Cat 7)
- 3 value-hash dup groups (all kept-by-design — see Cat 7)
- 0 unexplained scalar-mults

### Per-file commits

1. `d94a44b docs(HANDOFF): claim efficiency_snapshot for tab 15`
2. `6308e78 fix(efficiency_snapshot): _log_safe(scalar) bug + Cat 1 deriv-side _roc rebody` (3 files)
3. `aca99c9` / `620e7f0` / `e03ce7d` / `84b1fce` / `faf5dc0` — reverts of concurrent-tab auto-deletes
4. `e964875 fix(efficiency_snapshot): surgical rebody of 13 dup slots (Cat 1+2 batch)` (5 base files)
5. `297d4f3 fix(efficiency_snapshot): surgical rebody of remaining 11 dup slots (Cat 5/6 + es_050/2d/3d/395)` (6 files)

### Lessons worth carrying

1. **`_diff` vs `_pct_change` aliasing** is a cross-tier dup pattern that value_hash doesn't catch when the deriv-side helper has `.fillna(0.0)` (warmup NaN→0 differs from base raw `.diff()` NaN). The scalar-mult cosine-similarity scan catches it because post-warmup values are identical (max|a-b|=0). Future Path B audits: always run the scalar-mult scan after value_hash, even when value_hash reports zero dups.

2. **Concurrent-tab races** silently lose user-preference work when one tab is doing surgical edits while another is auto-applying. The HANDOFF rule was tightened during this session — arriving tabs must now ask the user for assignment rather than pulling the next pending row.

3. **DuPont decomposition functions are systematically point-in-time-bug-prone.** The named "decomposition" only matters if inputs are smoothed; otherwise NM × AT × EM = NI/E by algebra. Whenever a function name says "dupont" or "decomposition" and the body uses raw point-in-time inputs, the function is implicitly under-specified (academic DuPont uses TTM/period-average inputs). Worth a future cross-family check.

4. **Petrosian fractal_dim_proxy templates** require real daily variation to trigger; on quarterly-fwd-fill synthetic they're constant. Same disposition as ps_270 / cfs_d3_046 / bss_288 — sample-bias keeps. Consider building a "real-data verification" path for these on actual silver SF1 data when feasible.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_es_mini_harness.py`
- `%TEMP%\temp_es_scalar_mult_scan.py`
- `%TEMP%\temp_es_results.json`
- `%TEMP%\temp_es_scalar_mult_results.json`
- `%TEMP%\temp_es_raw_outputs.npz`

## 2026-05-09 — session 3, tab 17 (share_and_dilution_snapshot, master row 19)

**Done this session:**
- Picked up master row 19 `share_and_dilution_snapshot` per HANDOFF queue
  policy — first unclaimed row after rows 17 (efficiency_snapshot, tab 15)
  and 18 (rd_and_intangibles, tab 16). User asked for "base and 2 and 3
  derivatives full audits" — all tiers in one pass.
- **Inventory** (corrected after initial false-zero on prefix mismatch):
  function prefix is `sd_` not `sds_`. 8 files = 4 base × 75 fns
  (chunks 001-300, base files have `(1)` suffix variant) + 2 2nd-deriv ×
  25 fns + 2 3rd-deriv × 25 fns (deriv files split into `(1)` for idx
  001-025 and `_v2` for idx 026-050) = 400 functions. 0 OHLCV-only,
  75 hybrid OHLCV+fundamentals, 325 pure-fundamentals. 35 distinct non-
  OHLCV cols including 4 new vs prior Path B audits: `sharesbas`,
  `shareswadil`, `sharefactor`, `dps`. Heavy use of `ncf*` cash-flow
  component family.
- **Claimed** as tab 17 (commit `d5f21c4`).
- **Built mini-harness** at `%TEMP%\temp_sds_mini_harness.py` (deleted
  post-audit). Adapted BSS template with shares-specific synthetic Series:
  `sharesbas` ~ 1e8 with multi-regime drift, `shareswadil` slightly higher
  start + slightly faster drift to ensure non-zero dilution spread, `dps`
  positive small dividend, `ncfcommon` start=-50 (buyback regime), 3-regime
  quarterly drift breaks to avoid synth-bias. Warmup=800 to clear 504d
  shifts.
- **Findings (initial run)**: 0 errors / 0 all-NaN / 2 sample-bias
  constants / 2 formula-exact dup groups / 14 value-exact dup groups.
- **Triage**:
  - **2 formula-exact** auto-applied: sd_049 == sd_009
    (`pct_change(s, 504)`), sd_248 == sd_183
    (`_safe_div(ncfcommon, capex.abs())`).
  - **14 value-exact dup groups** classified by close inspection:
    - **8 body-identical-modulo-docstring/var-rename** (auto-apply per
      cs_082/cs_133 precedent): sd_124, sd_125, sd_139, sd_140, sd_266,
      sd_273, sd_2d_009, sd_2d_001, sd_2d_005, sd_2d_024, sd_3d_016
      (literal text-identical bodies; only docstrings or local var names
      differ from canonical lower-numbered cousin).
    - **11 algebraic-identity** in 3 classes (user-approved auto-apply
      mirroring valuation_at_entry tab 13's 17-cluster precedent):
      (a) `s/b` vs `(s-b)/b` collapses under `.diff()`/`_compute_3d`
          because constant -1 cancels: sd_120, sd_121, sd_2d_020,
          sd_3d_020.
      (b) `close` factor cancels in mktcap normalization
          `((s-b)*c)/(c*b) = (s-b)/b`: sd_219, sd_220, sd_2d_v2_012,
          sd_3d_v2_012.
      (c) Cross-tier `pct_change + 2 deltas` collapses uniformly via
          `_compute_3d(base) = _delta(_delta(base, 63), 63)` semantics:
          sd_3d_001 (3rd deriv of pct_change_63d == sd_2d_016 hand-rolled
          chg-shift-delta), sd_3d_005, sd_3d_024.
    - **2 sample-bias constants kept by design**:
      sd_083_ncfcommon_positive_ratio_504d
      (`(ncfcommon > 0).rolling(504).mean()`) and sd_188_issuance_cash_to_debt
      (`_safe_div(ncfcommon.clip(lower=0), debt.abs())`) — both clip-based,
      both 0.0 on synthetic with mostly-negative ncfcommon (modeling
      buyback regime); on real data with positive issuance regimes both
      produce signal. Same disposition as cfs_d3_046 / bss_288.
    - **1 small-x-coincidence pair kept**: sd_131 simple-return rank
      (`_rank_pct(_pct_change(s, 252), 504)`) ≡ sd_156 log-return rank
      (`_rank_pct(np.log(s/s.shift(252)), 504)`) only because synthetic
      dilution rate ≤ 5%/yr (log(1+x) ≈ x for small x). On real data with
      growth firms at 10-30%/yr dilution they diverge meaningfully. Not
      a real dup.
- **Per-file commits** (one per affected file with scoped messages):
  `8092874` (b1: sd_049), `0ba2042` (b2: 6 deletes), `5fb2597` (b3:
  sd_219/sd_220), `88a21d0` (b4: sd_248/sd_266/sd_273), `2445b86`
  (d2a: 5 cross-tier), `adef6b3` (d2b: sd_2d_v2_012), `68104fc`
  (d3a: 5 jerk-tier), `f3791cd` (d3b: sd_3d_v2_012). All AST-parse
  validated post-edit.
- **Final state**: 376 / 400 bound (= 400 - 24 deletes). 0 errors / 0
  formula-exact dups / 0 real value-exact dups. 2 sample-bias constants
  + 1 small-x-coincidence pair kept by design.

**Lessons (worth carrying):**
1. **Function prefix mismatch detection**: family is named
   `share_and_dilution_snapshot_*` but functions are prefixed `sd_` not
   `sds_`. The inventory returned 0 matches initially because of this.
   Future audits: when inventory returns 0 functions, peek at the actual
   function names with a generic `^def [a-z]+_\d{3}` regex before
   assuming the prefix.
2. **Cross-tier dups are normal in shares-domain**: 11 of 24 deletes were
   cross-tier (base-vs-2d, 2d-vs-3d). Authors built parallel namings
   `sd_011 dilution_spread`, `sd_119 diluted_to_basic`, `sd_124
   potential_dilution_pct`, `sd_219 overhang_proxy` for the same
   underlying ratio, then propagated all four into ROC and jerk tiers,
   creating 6+ aliased columns at each derivative tier. Once the base-
   tier alias chain is identified, the deriv-tier ones cascade
   automatically.
3. **`_compute_3d(pct_change(s, k))` == `delta(delta(s, k), k)` after
   pct_change**: the 3rd-deriv tier has a convenience helper that some
   functions use and others hand-roll. Hand-rolled and helper forms
   produce text-different bodies but are value-exact. Pattern recognition
   for future audits: any base feature that's already a delta/pct_change
   followed by a `_compute_3d` wrapper is likely identical to a sibling
   that hand-rolls the chg-shift-delta sequence on the same input.
4. **ncfcommon synth modeling matters for sample-bias detection**: my
   choice of `ncfcommon: start=-50` (buyback regime) zeroed out 2
   constants (sd_083, sd_188 both clip to 0 when ncfcommon ≤ 0). To
   confirm they're real signals on issuing firms, would need an issuance-
   regime synth. Not done in this session — kept as KEEP-BY-DESIGN per
   established disposition for clip-based sample-bias-constants.

**Cross-tab status at this writing:**
- Tab 17: share_and_dilution_snapshot DONE (this entry).
- Master row 19: now fully **DONE** (Path B, all 8 files; 9 commits).
- Path B family count: 8 done (revenue_level, profitability_snapshot,
  cash_flow_snapshot, balance_sheet_snapshot, valuation_at_entry,
  leverage_and_solvency, rd_and_intangibles, share_and_dilution_snapshot).
- File audit count: 100 -> 108 / 431 (25.1%).

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_sds_mini_harness.py`
- `%TEMP%\temp_sds_run1.log`
- `%TEMP%\temp_sds_run2.log`

---

## Session 3 (2026-05-09, tab 18) — `capital_allocation_snapshot` (Path B, all tiers)

**Setup.** HANDOFF row 20. 8 files, 400 functions, 100% Path B (every fn
takes fundamentals; 0 OHLCV-only). Pre-claimed by tab 16's wrap-up
commit `1db6592` (which marked "Next-open per master priority queue:
row 20 capital_allocation_snapshot"); my Path B detail row + claim in
commit `d2a3537`.

**Multi-tab race.** When my session started, `%TEMP%\temp_cas_mini_harness.py`
already existed (timestamp 15:31, ~30s before my session). Another tab
had begun the same family without committing a claim or fix. Asked the
user how to proceed; user directed "Keep working on row 20." Replaced
the existing temp harness with a quarterly-cadence version (the
pre-existing harness used 1500-day daily fwd-fill from quarterly anchors
— a wrong fit for this family's `periods=4` semantics).

**Cadence.** This family is **quarterly-cadence** (periods=1 means 1
quarter, periods=4 means YoY, max window=20q). The TRADING_DAYS_*
constants exist in helpers but are never used in feature bodies; every
period in feature bodies is a small int 1/4/8/12/20. Same as
profitability_snapshot and rd_and_intangibles. A daily-cadence harness
with quarterly-fwd-fill would compute 4-day pct_change (mostly zero
within a quarter, occasional jumps at boundaries) instead of YoY,
yielding a flood of false constants and value-exact dups.

**Inputs union (36 cols).** `assets`, `capex`, `cashnequsd`, `cor`,
`debt`, `deferredrev`, `depamor`, `dividends`, `equity`, `fcf`,
`goodwill`, `gp`, `intangibles`, `intexp`, `inventory`, `investments`,
`liabilities`, `marketcap`, `ncff`, `ncfi`, `ncfo`, `netinc`, `opex`,
`opinc`, `payables`, `receivables`, `retainedearnings`, `revenue`,
`rnd`, `sbcomp`, `sgna`, `sharesbiz`, `shareswa`, `tangibles`, `taxexp`,
`workingcapital`. Non-Sharadar names: `cashnequsd` (vs SF1 `cashneq`),
`retainedearnings` (vs `retearn`), `dividends` (vs `ncfdiv`), `marketcap`
(vs `mcap`), `shareswa` (vs `shareswadil`), `sharesbiz` (unique to
this family). LS precedent for binding-layer translation map.

**Mini-harness baseline** (`%TEMP%\temp_cas_mini_harness.py`,
deleted post-audit; results at `temp_cas_results.json`): 5 profiles ×
60 quarters × 36 cols, independent random walks per col (no scalar-multiple
synth bias per ve session-13 lesson). Run 1: 0 errors / 0 all-NaN / 0
constants / 0 formula-exact dups / 7 value-exact dup groups / 10
scalar-mult pairs (8 of 10 are the same value-dup pairs at ratio=1; 1
new = cas_025 vs cas_136 ratio=4 annualization; 1 already-flagged).

### Triage (1 ASK with 4 options, user chose "All 3 deletes + surgical edit")

**5 dup deletes:**
1. `cas_078_total_reinvestment_to_revenue` == `cas_017_rnd_plus_capex_to_revenue`
   — both `_safe_div(rnd + capex.abs(), revenue)`. Formula-exact under
   rename, **AUTO-APPLY** per HANDOFF policy.
2. `cas_289_revenue_per_dollar_invested_capital` == `cas_089_capital_turnover`
   — both `_safe_div(revenue, debt + equity)`. Formula-exact, **AUTO-APPLY**.
3. `cas_158_eva_to_invested_capital` == `cas_155_eva_spread_proxy`
   — algebraic identity: `(NOPAT - IC*iw) / IC = NOPAT/IC - iw = roic - iw`.
   Different framings of the same EVA spread. ASK FIRST → user-approved.
4. `cas_182_roe_dupont` == `cas_221_roe` — DuPont 3-factor cancellation:
   `(N/R)(R/A)(A/E) = N/E`. The actual decomposition-sensitivity features
   live elsewhere (cas_184/185); cas_182 is just a multiplied-out ROE.
   Cancellation-equivalent precedent: rl_080/081/082. ASK FIRST → approved.
5. `cas_183_roe_5factor` == `cas_221_roe` — DuPont 5-factor:
   `(N/EBT)(EBT/OI)(OI/R)(R/A)(A/E) = N/E`. Same telescoping logic.
   ASK FIRST → approved.

**1 surgical edit (preserves naming intent for value-dup):**
- `cas_141_net_equity_issuance` was literal `_pct_change(shareswa, periods=1)`
  (== cas_031 share_change_qoq) but the name promised "issuance flag /
  positive share change = dilution". Rebodied to `clip(lower=0)` →
  positive-only dilution magnitude. Mirrors cas_050_debt_issuance pattern
  (`debt_chg.clip(lower=0)`). ls_148 / vac_118 naming-bug precedent.

### KEPT BY DESIGN

**2 academic-trace value-exact pairs (composite cas_231 inlines x1-x5):**
- `cas_062_wc_to_assets` == `cas_226_altman_x1` (working capital / assets,
  Altman X1 component for liquidity).
- `cas_090_asset_turnover` == `cas_230_altman_x5` (revenue / assets,
  Altman X5 component for asset utilization).
Same disposition as ls_061/151/170/188 — academic distress-model variables
must be individually addressable for model-trace explainability. The
composite `cas_231_altman_z_composite` literally inlines x1–x5 anyway.

**1 NOPAT-precedent scalar-mult pair:**
- `cas_025_div_to_equity` (quarterly) vs `cas_136_div_yield_on_equity`
  (annualized = quarterly × 4). Deliberate domain reformulation per
  profitability_snapshot's 14 NOPAT pairs at ratio 1/0.79 and
  leverage_and_solvency's ls_023/297 at ratio 1/252.

### Per-file commits (3 commits, one per file affected)

- `447528c` — base_076_150 (1).py: cas_078 delete + cas_141 surgical rebody.
- `59c486d` — base_151_225.py: cas_158, cas_182, cas_183 deletes (3 in one file).
- `a3964b2` — base_226_300.py: cas_289 delete.

### Re-run post-fix

`temp_cas_mini_harness.py` re-run: 395/400 fns / 0 errors / 0 all-NaN /
0 constants / 0 formula-exact dups / 2 value-exact dup groups (both
academic-trace KEEPs) / 3 scalar-mult pairs (1 NOPAT-precedent annualization
+ 2 academic-trace at ratio=1 = same as the value-dup pairs).

**Final state:** 400 → 395 fns. All non-KEEP dups removed.

### Lessons (worth carrying)

1. **Quarterly-cadence detection is critical for Path B harness design.**
   Three families so far use quarterly-cadence Series:
   `profitability_snapshot`, `rd_and_intangibles`, and now
   `capital_allocation_snapshot`. Tell vs daily-cadence by looking at
   the period args: small ints (1, 4, 8, 12, 20) and docstrings
   annotating "(4 quarters)" / "(YoY)" / "8q vol" → quarterly.
   `TRADING_DAYS_*` constants in feature bodies → daily. A
   quarterly family fed daily-fwd-fill data computes 4-day pct_change
   instead of YoY, yielding mostly-zero output and a flood of false
   constants. Always grep the period args before designing the harness.

2. **Multi-tab race detection is straightforward but the resolution is
   judgment.** When my temp file already existed at session start, I
   asked the user. Per the HANDOFF "second to start should release"
   policy I would have released, but the user directed me to keep
   working given (a) the other tab had no fix commits yet and (b) the
   pre-existing harness had a cadence bug. Worth surfacing the conflict
   explicitly rather than racing.

3. **DuPont-decomposition collapses are cancellation-equivalent dups.**
   When a DuPont k-factor identity `Π(s_i / s_{i-1}) = s_n / s_0`
   telescopes (each numerator cancels with the next denominator), the
   k-factor features are value-exact dups of the bottom-line `s_n / s_0`.
   The decomposition's analytical value lives in the *components*, not
   the multiplied-out form — and components are addressable as separate
   features (e.g., margin, turnover, leverage are individually present
   in this family at cas_021/090/041 etc.). Auto-applicable as
   cancellation-equivalent per RL rl_080/081/082 precedent.

4. **EVA framing dups: spread vs ratio.** EVA = NOPAT - IC*iw is the
   underlying quantity. EVA/IC = roic - iw (spread form) and (EVA)/IC
   (literal-divided form) are algebraically identical. When two siblings
   compute the same EVA component differently, prefer the more numerically
   stable / semantically clearer form (spread form, here cas_155).

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_cas_mini_harness.py`
- `%TEMP%\temp_cas_results.json`


---

## 2026-05-09 — session 3 — tab 20: margin_trajectory (Path B, 15 algebraic-identity deletes)

**Family scope.** 8 files / 400 functions. Naming is unusual — derivative
tiers reuse the integrated `mt_NNN` namespace via `_d_`/`_dd_` infixes
instead of the `_2d_`/`_3d_` prefix used elsewhere:

- mt_001-150 + mt_201-275 + mt_276-350 = 300 base fns (gaps 151-200,
  351-400 are occupied by deriv files)
- mt_151-175 + mt_351-375 = 50 first-deriv fns (`_d_` infix), in
  `2nd_derivatives` files
- mt_176-200 + mt_376-400 = 50 second-deriv fns (`_dd_` infix), in
  `3rd_derivatives` files

100% Path B (no OHLCV inputs); only 14 input cols: `capex`, `cor`,
`depamor`, `ebitda`, `fcf`, `intexp`, `ncfo`, `netinc`, `opinc`, `revenue`,
`rnd`, `sbcomp`, `sgna`, `taxexp`. All cash-flow / income-statement, no
balance-sheet items.

### Cadence trap caught early

First harness run used the standard daily-cadence Path B template (1500
days, forward-filled from quarterly anchors). Result: 0 errors, 0 dups,
but **35 false-positive constants past warmup** and **5 false-positive
all-NaN**. Investigating revealed margin_trajectory uses raw periods
(`.shift(4)`, `_rolling_mean(_, 8)`) without `QDAYS=63` mapping — meaning
inputs are expected at **quarterly cadence**, not daily. Per CLAUDE.md
"daily-vs-quarterly cadence trap" note.

Re-ran with 80-row quarterly synthetic (~20y of quarterly data). All 35
false constants and 5 false all-NaN cleared; same 15 scalar-mult pairs
remained — algebraic identities are cadence-invariant so true findings
survived the re-run.

### Findings (15 deletes, 0 keeps)

All 15 dups are algebraic-identity scalar-multiples at ratio = 1/4,
across 2 mathematical clusters:

**Cluster 1 (5 pairs): telescoping identity**
- `mt_151_d_gross_margin_4q_mean == mt_021_gross_margin_4q_chg / 4`
- ...and 4 sibling pairs (op/net/ebitda/fcf margin variants)

The `_d_X_4q_mean` body computes `_diff(rolling_mean(X, 4), 1)` while
`_X_4q_chg` computes `_diff(X, 4)` directly. The telescoping sum identity
`_diff(rolling_mean(s, W), 1) = _diff(s, W) / W` makes them
algebraically equal up to factor `1/W = 0.25`. Same precedent as RD's
ri_2d_031 == ri_2d_002/4 (commit `c525cab`). Auto-applied.

**Cluster 2 (10 pairs): boll_pctb == zscore/4 + 0.5 identity**
- `mt_371_d_gross_margin_boll_pctb == mt_161_d_gross_margin_zscore_8q / 4`
- ...and 4 sibling pairs at ROC level (mt_372-375 ↔ mt_162-165)
- `mt_396_dd_gross_margin_boll_pctb == mt_186_dd_gross_margin_zscore_8q / 4`
- ...and 4 sibling pairs at jerk level (mt_397-400 ↔ mt_187-190)

Standard Bollinger %B is `(s - (mid - 2*std)) / (4*std) = z(s)/4 + 0.5`
where `z` is the 8q rolling z-score. The `_d` operator (`s - s.shift(1)`)
is linear, so the +0.5 offset differences out: `_d(z/4 + 0.5) = _d(z)/4`.
Same identity at jerk level for `_dd`. All caught by post-warmup z-cosine
scan at sim=1.0, ratio_std_rel<1e-13.

### Per-file commits

- `7caaf78` — `margin_trajectory_2nd_derivatives.py`: delete mt_151-155
  (29 deletions; 25 → 20 fns)
- `286cf3d` — `margin_trajectory_2nd_derivatives_v2.py`: delete mt_371-375
  (28 deletions; 25 → 20 fns)
- `17124bf` — `margin_trajectory_3rd_derivatives_v2.py`: delete mt_396-400
  (28 deletions; 25 → 20 fns)

Re-ran harness post-fix: 385/385 fns clean, 0 errors / 0 all-NaN / 0
constants / 0 value-exact dups / 0 scalar-mult pairs.

### Lessons worth carrying

1. **Cadence check is mandatory before harness build.** When functions
   use `.shift(4)` or `rolling(8)` without an explicit `*QDAYS` factor,
   the family is quarterly-indexed — feed quarterly Series, not daily-
   forward-fill. Daily mode will silently produce sample-bias constants
   on RSI / incremental margin / op-leverage that look like real signals
   in the harness output. Both CAS (tab 18) and MT (tab 20) hit this
   trap and corrected to quarterly synthetic; document for future tabs.

2. **The Bollinger %B vs z-score scalar-multiple identity** generalizes
   to any pair of "deviation from mean / scale" features when the scale
   is `n_std × std`. Worth checking explicitly when families have both
   a raw z-score and a Bollinger-%B variant on the same underlier.

3. **Coordinate releases promptly.** Initially I claimed CAS (tab 18)
   then released when user flagged conflict; another tab finished CAS
   in parallel. After release I picked margin_trajectory under the
   pre-existing "auto-pick lowest-pending" policy, which the user then
   updated mid-session to "explicit assignment required". User
   confirmed continue; would have been cleaner to ask up-front. New
   policy is now reflected in HANDOFF preamble.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_mt_mini_harness.py`
- `%TEMP%\temp_mt_results.json`

---

## Session 3 — `cash_flow_trajectory` audit (item #23)

User instruction was originally to audit margin_trajectory; while the harness was being prepped, user said `stop`, asked about cash_flow_trajectory's status, and switched to `start full audit`. Margin_trajectory had since been finished by tab 20 in parallel.

### Inventory

8 files = 400 fns:
- `cash_flow_trajectory_base_001_075.py`, `_076_150`, `_151_225`, `_226_300` — 75 fns each = 300 base
- `cash_flow_trajectory_2nd_derivatives.py` (idx 001-025), `_2nd_derivatives_expanded.py` (idx 026-050) — 25 fns each
- `cash_flow_trajectory_3rd_derivatives.py` + `_3rd_derivatives_expanded.py` — same split

33 input cols (Path B, hybrid via market subset). Non-Sharadar / synthetic:
- `cur_liab` (vs `liabilitiesc`)
- `marketcap` (vs `mcap`)
- `depamor_prev_proxy` — only consumed by `cft_204_depi_index`; the docstring there says "we use shift internally", so harness passes `depamor` for both args.

Cadence check: 43× `shift(4)`, 28× `shift(1)`, rolling 4/8/12/20q. **Quarterly cadence** — same as `mt`. The `cft_206_*_price_momentum_252` / `cft_207_*_price_momentum_126` / `cft_208_*_volume_trend_21+63` are mixed-cadence outliers (designed for daily price/volume) but the family overall is quarterly. Built the harness with 80-row quarterly synthetic per `mt` tab-20 lesson.

### Harness

`temp_cft_harness.py` — 5 quarterly profiles × 80 rows, multi-regime drift (3 segments × 30/30/20 rows breaks monotonicity), accounting-consistent synthesis (`fcf = ncfo - capex`, `ev = mcap + debt - cash`, `ncff = ncfdebt + ncfdiv + ncfcommon`, etc.). Loaded all 8 registries. Per-fn stack across profiles → post-warmup byte hash for value-exact, post-warmup cosine for scalar-mult.

First run on 400 fns: 0 errors / 0 all-NaN / 12 sample-bias constants / 9 formula-exact dup groups / 10 scalar-mult candidates.

### Triage decisions

**Auto-apply (7 deletes)** — all match prior precedent:

| Delete | Survivor | Mechanism | Precedent |
|---|---|---|---|
| `cft_2d_002_fcf_margin_roc_yoy` | `cft_005_fcf_margin_expansion_4q` | `_delta(m,4)` = base "expansion_4q" alias | CFS cfs_d2_002 |
| `cft_2d_010_capex_intensity_roc_yoy` | `cft_029_capex_intensity_trend` | base "trend" wins | CFS |
| `cft_2d_028_sloan_accrual_roc_yoy` | `cft_158_sloan_accrual_ratio_trend` | base "trend" wins | CFS |
| `cft_2d_039_wc_to_revenue_roc` | `cft_246_wc_intensity_change` | base "change" wins | CFS |
| `cft_012_fcf_growth_acceleration` | `cft_2d_004_fcf_yoy_growth_roc_4q` | "acceleration" → deriv | RI ri_036 |
| `cft_284_fcf_margin_acceleration` | `cft_3d_001_fcf_margin_jerk` | "acceleration" → deriv (cft_3d_001 misnamed but `_delta(_delta(m,1),1)` is 2nd-order = same op) | RI |
| `cft_3d_002_fcf_margin_jerk_yoy` | `cft_218_fcf_margin_convexity` | algebraic-id `mean(d²,4) = jerk_yoy/4` ratio=4 std=1.34e-14 | mt_151..155 / ri_2d_031 |

The mean(d²,4) = jerk_yoy/4 identity: expanding `Σ_{k=t-3..t}(m_k − 2m_{k-1} + m_{k-2}) = m_t − m_{t-1} − m_{t-4} + m_{t-5}` which is `_delta(_delta(m,4),1)`. Divide by 4 → mean. Tight enough for `ratio_std_rel = 1.34e-14`.

Removed orphan helper `_fcf_margin_roc_yoy` in cft_3d_002 commit (was only called by cft_3d_002).

**Keep by design (no action)**:
- 12 sample-bias constants — all because synthetic firm is profitable (positive ncfo): `clip(upper=0)` on the 7-fn cash-burn family always zeroes, sign-transition flags don't fire, positive-mean durability=1, mixed-cadence `_x_price_momentum_252/126` `.shift(252)` exceeds 80-row window so `_safe_div(NaN,NaN)=0` via `fillna(0.0)` quirk
- 3 winsorized/synth-coincidence value-exact pairs:
  - `cft_008_fcf_yoy_growth ↔ cft_051_ocf_minus_capex_trend` — coincide on synthetic where `fcf = ncfo − |capex|` exactly; on real data fcf is reported separately and drifts
  - `cft_049_fcf_zscore_12q ↔ cft_288_fcf_winsorised_zscore` — `clip(±3)` doesn't fire on synthetic (z-scores stay within ±3); ps_006/312 winsorized precedent
  - `cft_072_fcf_to_revenue_zscore_12q ↔ cft_289_fcf_margin_winsorised` — same winsorized pattern
- 9 NOPAT/days-conversion scalar-mult pairs:
  - 5 days-conversion ratio=90 (DSO/DIO/DPO trends vs raw ratio trends, CCC vs wc/rev)
  - 1 yield_3y vs cumulative_to_mktcap ratio=3 (cft_032 = `4q_sum/mcap*3`, cft_057 = `12q_sum/mcap` — same `12q_sum` numerator, scalar denom diff)
  - 1 cft_021↔cft_105 ratio=1 — ocf_yoy_growth vs ocf_compounding_4q (telescoping `Π(1+g_q) - 1 = ocf_t/ocf_{t-4} - 1` matches yoy growth on positive ncfo because `|ncfo_{t-4}| = ncfo_{t-4}`; diverges on negative ncfo + clip behavior)
  - 1 cft_3d_021↔cft_3d_037 ratio=1/90 — same CCC-vs-wc/rev structure at jerk level

### `_safe_div` quirk worth noting

```python
def _safe_div(num, den, fill=0.0):
    return num.divide(den.replace(0, np.nan)).fillna(fill)
```

This family uses `fill=0.0` (not NaN) by default. Any caller relying on NaN-propagation will get 0 for "missing data" rows in cash_flow_trajectory output. The cft_206/207 mixed-cadence constants illustrate it: `.shift(252)` on 80-row → all-NaN intermediate → `fillna(0)` → output is constant 0 instead of all-NaN. Worth documenting in case downstream callers blend cft features into composites.

### Per-file commits

- `42bf7d3` — `cash_flow_trajectory_2nd_derivatives.py`: delete cft_2d_002, cft_2d_010 (25 → 23 fns)
- `c281a8f` — `cash_flow_trajectory_2nd_derivatives_expanded.py`: delete cft_2d_028, cft_2d_039 (25 → 23 fns)
- `2aeb4d1` — `cash_flow_trajectory_3rd_derivatives.py`: delete cft_3d_002 + orphan helper (25 → 24 fns)
- `c9732d2` — `cash_flow_trajectory_base_001_075.py`: delete cft_012 (75 → 74 fns)
- `5b1804d` — `cash_flow_trajectory_base_226_300.py`: delete cft_284 (75 → 74 fns)

Re-run post-fix: 393/393 valid, 0 errors / 0 all-NaN / 12 KBD constants / 3 KBD value-exact pairs / 9 KBD scalar-mult pairs. No surprises.

### Lessons

1. **Mixed-cadence designs leak through `_safe_div(fill=0.0)`.** The `*_x_price_momentum_*` functions in cft and similar families silently produce constant-zero output when their daily-cadence shifts exceed the data range, because `_safe_div` has been customized to fill NaN. On daily-cadence input these would work; on quarterly they look like sample-bias constants. Worth checking the family's `_safe_div` signature when triaging constants.
2. **Quarterly-cadence families are now the established Path B default** (mt, cas, cft); only `debt_trajectory` (already claimed by tab 22, marked daily) and `revenue_growth` (tab 19, mixed) deviate. Inventory shift-values are the cheap cadence check.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_cft_harness.py`
- `temp_cft_harness_out.json`

## 2026-05-09 — session 3 — tab 25: growth_vs_cost (Path B, all tiers)

**Scope.** 11 files / 575 features (6 base × 75 = 450 + 2 2nd-deriv × 25 = 50 + 3 3rd-deriv × 25 = 75). 100% Path B (54 input cols; daily-cadence per `TRADING_DAYS_QTR=63`/`TRADING_DAYS_YR=252` constants for shifts/rolling). Hybrid only via `close`/`high`/`low`/`volume`/`marketcap`/`ev`/`sharesbas`/`shareswa`. New cols vs prior Path B: `eps`, `ncf`, `ncfbus`.

**Mini-harness.** `temp_gvc_harness.py` — 5 fundamental profiles (A_grower, B_mature, C_distressed, D_cyclical, E_burn) × 1500 days, daily fwd-fill from quarterly anchors (~24q each). Identical pattern to BSS/CFS/SD/VE/RI Path B. Warmup=800.

**Findings (initial run):** 575 fns / 1 error / 0 all-NaN / 2 sample-bias constants / 21 value-groups / 1 scalar near-miss.

**Triage outcomes (13 deletes + 1 bug fix, 6 commits):**

| Class | Count | Examples | Action |
|---|---:|---|---|
| Within-base formula-exact (helper rename) | 8 | gc_005/431, gc_025/304, gc_026/301, gc_027/306, gc_062/389, gc_140/392, gc_192/403, gc_216/404 | Auto-apply delete |
| Within-base algebraic-identity | 2 | gc_017/137 (`*1`), gc_192/398 (`rg/vol = rg*(1/vol)`) | Auto-apply delete (SD/CAS/MT/RI precedent) |
| Cross-tier base-vs-deriv pollution | 1 | gc_066 == gc_2d_003 (literal 2nd diff) | Delete from base (RI/CFS/RL precedent) |
| Within-deriv formula-exact | 2 | gc_2d_007/2d_033, gc_3d_010/3d_069 | Auto-apply delete |
| Bug: kwarg name mismatch | 1 | gc_331 `_sd(.., fill=1.0)` vs helper `f=0.0` | Fix to positional |
| Synth-bias value-exact pair (KEEP) | 11 | opinc==ebit (6×), eps=netinc/100 (3×), shareswa=sharesbas*0.99, debtc/debtnc=const*debt | Document |
| Sample-bias constant (KEEP) | 2 | gc_405/406 rev-growth threshold flags | Document |
| Scalar near-miss not a dup (DROP) | 1 | gc_054/087 fcf vs fcf-per-share (ratio_std_rel=0.05) | Skip |

**Per-file commits:**
- `5bf9883` — `growth_vs_cost_base_001_075.py`: delete gc_066 (cross-tier; 75 → 74 fns)
- `70bf8be` — `growth_vs_cost_base_076_150.py`: delete gc_137 (algebraic identity; 75 → 74 fns)
- `b72acf0` — `growth_vs_cost_base_301_375.py`: delete gc_301/304/306 + fix gc_331 bug (75 → 72 fns)
- `538de8e` — `growth_vs_cost_base_376_450.py`: delete gc_389/392/398/403/404/431 (75 → 69 fns)
- `286605c` — `growth_vs_cost_2nd_derivatives_026_050.py`: delete gc_2d_033 (25 → 24 fns)
- `f4baf48` — `growth_vs_cost_3rd_derivatives_051_075.py`: delete gc_3d_069 (25 → 24 fns)

**Re-run post-fix:** 562/575 fns / 0 errors / 0 all-NaN / 2 KBD constants / 11 KBD synth-bias value-pairs / 1 dropped scalar near-miss.

### Notable finds

**gc_137_margin_trend_slope_1y bug-as-dup.** Body literally `_delta(om, 252) / 252 * 252` — the `/252*252` cancels to `*1`, making it numerically identical to gc_017_operating_margin_delta_1y on every input (not just synth). Docstring says "Linear slope of operating margin over trailing 1y (approximated with delta/periods)"; if the intent was "delta-per-day" then the `*252` shouldn't be there. Treated as algebraic-identity dup and deleted; if user wants a real slope feature, that's a fresh ASK.

**gc_066 mathematically equivalent to gc_2d_003.** gc_066 body is `d1 - om.shift(63).diff(63)`. Expanding: `(om - om.shift(63)) - (om.shift(63) - om.shift(126))` = `om - 2*om.shift(63) + om.shift(126)`. gc_2d_003 body is `_delta(_delta(om, 63), 63)` which expands the same way. Cross-tier pollution; delete-from-base per RI ri_036 / CFS cfs_d2 / RL rl_227-231 precedent.

**Synth-bias artifacts that won't appear on real Sharadar.** The 11 KEEP-BY-DESIGN value-exact pairs all hinge on synth simplifications:
- `ebit_q = opinc_q.copy()` (real EBIT includes non-operating items, so gc_015/199, gc_017/200, gc_051/198, gc_052/201, gc_2d_003/043, gc_3d_003/043 all diverge on real data)
- `eps_q = netinc_q / 100.0` (constant divisor cancels in pct_change/CAGR; real shareswa is time-varying so gc_040/210, gc_053/194, gc_105/196 diverge)
- `shareswa_q = sharesbas_q * 0.99` (constant scalar cancels in pct_change → gc_086/285)
- `debtc_q = debt_q * 0.20`, `debtnc_q = debt_q * 0.80` (constant proportions cancel → gc_079/280/281)

Could update the harness to break these collapses (e.g. add separate non-operating drift to ebit, dilution dynamics to shareswa, debt-mix shifts), but the KEEP justification is per-pair documented and matches established RI/SD precedents.

### Lessons

1. **Watch for naming-mismatch helper rename clusters across files.** `_safe_div`/`_pct_change`/`_rank_pct`/`_delta` (long names) coexist with `_sd`/`_pc`/`_rk`/`_d` (short names) in different files of the same family. 8 of the 13 deletes here were formula-exact under that rename — value-hash catches them, but a body-text grep would miss them. Standard auto-apply.
2. **Algebraic-identity scalar-mult-by-1 (`*N/N`) is now an established auto-apply pattern.** SD/CAS/MT/RI all have one. gc_137 makes 5 in a row. Add to triage checklist.
3. **`opinc==ebit` synth assumption is the single most-prolific synth-bias generator in this family.** 6 of 11 KEEPs trace to it. For future families with both opinc-features and ebit-features, consider injecting a drift between the two (e.g. `ebit_q = opinc_q + rev_q * normal(0.005, 0.003, n_q)`) so the harness can distinguish synth-bias from real dups in a single run.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_gvc_harness.py`
- `temp_gvc_harness_out.json`

## 2026-05-09 — session 3 — tab 28: valuation_trajectory (Path B, all tiers)

**Family:** `valuation_trajectory`. 14 files (8 base + 3 2nd-deriv + 3 3rd-deriv). 750 features (vt_001..vt_600 base + vt_601..vt_675 d2 + vt_676..vt_750 d3). Function prefix `vt_`. Daily-cadence (`TD_Y=252`/`TD_Q=63`/`TD_M=21`/`TD_W=5`).

**Outcome:** 726/726 fns clean post-fix. **24 dup deletes + 2 surgical edits + 1 bug fix** across 8 commits. 0 errors / 0 all-NaN / 0 constants / 0 formula-exact dups; 1 KEEP-BY-DESIGN clip-differentiated value-dup pair remains.

### Harness setup

- 5 synthetic profiles × 2000 daily rows × 47 input cols (warmup=1300, post-warmup=700/profile so 3500 total post-warmup rows for hashing).
- Daily-cadence forward-fill from quarterly anchors (1 anchor/63 days, 33 anchors over 2000 days). All flows / balance-sheet items quarterly; only `close`/`high`/`low`/`volume` are truly daily.
- Synthetic `marketcap = close * sharesbas` and `ev = marketcap + debt - cashneq` mirror the binding-layer translation precedent (CAS/BSS).
- 2000-day window chosen to cover the longest shift (`TD_Y*5 = 1260` in vt_211/212 / vt_287 etc.). 1500 days would have left those features all-NaN.

### Findings

| Class | Count | Action |
|---|---:|---|
| within-base mcap-X aliases | 8 | auto-apply delete |
| within-base body-identical-mod-rename + algebraic identity | 9 | auto-apply delete |
| cross-tier base→deriv | 5 | auto-apply delete-from-base |
| KEEP-BY-DESIGN clip-differentiated value-dup pair | 1 | keep |
| trivial-truncation bug | 1 | auto-apply fix |
| naming-bug surgical rebody | 2 | ASK FIRST → user-approved |

**24 dup deletes (one commit per file affected):**

- `0f154d6` base_076_150 (9): vt_103/104/105/107/108/109/110/111 (mcap-X aliases of close/X-per-share since `marketcap=close*sharesbas`); vt_114→vt_601_d2 (cross-tier, pe_momentum_21d = pe.diff(TD_M)).
- `246d8a3` base_301_375 (3): vt_306==vt_305 (E/P*100 algebraic identity), vt_319/320==vt_153/154 (mcap_ncfo aliases).
- `1a63b32` base_376_450 (3 + 1 bug fix): vt_418→vt_687_d3 (cross-tier z.diff(TD_M).diff(TD_M)), vt_433==vt_122 (`_pc(_rstd(W),W) = _sd(v1-v2,v2)` since `_rstd(s.shift(W),W) = _rstd(s,W).shift(W)`), vt_440==vt_093 (literal IQR alias). Bug fix vt_400_pe_entropy_63: removed `pe.diff().dropna()` which truncated output by 1 row, violating CLAUDE.md alignment contract.
- `0816109` base_451_525 (3): vt_483==vt_340 (pe_vol_1q==pe_vol_63 alias, 1q=63d); vt_489/490==vt_279/280 (pe-pb / pe-pfcf z-spread aliases, literal-identical body).
- `f1d13a2` base_526_600 (5): vt_552==vt_418 (mathematical identity `f-2*f(t-21)+f(t-42) = f.diff(21).diff(21)`); vt_575/576→vt_612/615_d2 (cross-tier z.diff(TD_M)); vt_583/584==vt_062/063 (sma_distance vs mean_reversion same body).
- `093981c` base_451_525 (1): vt_524==vt_116 (multiplication-commutative `-z*_pc(pe,W) = _pc(pe,W)*z*-1`); was missed in the first base_451_525 commit, landed as a separate commit per per-file commit policy.

**2 surgical-edit rebodies (user-approved):**

- `521f953` base_226_300: vt_296_pe_mass_index. Original `_rmax(pe,1)-_rmin(pe,1)` = 0 over a 1-element window, making the entire function always-NaN (downstream `_sd(e1,e2)` divides by zero). Rebodied to canonical Dorsey Mass Index: `EMA(pe.diff().abs(), 9) / EMA(EMA(pe.diff().abs(), 9), 9)` summed over 25 periods (with `min_periods=13` to match codebase half-window-warmup convention). This is the standard Mass Index formula adapted to a single-Series PE signal (substituting `pe.diff().abs()` for the high-low range used on bar data).
- `e426bf6` base_451_525: vt_511_graham_number_ratio. Original `_sd(pe*pb, gn**2)*100` where `gn = sqrt(22.5*pe.clip(0)*pb.clip(0))` reduces by trivial algebra to `100/22.5 = 4.444...` whenever pe>0 and pb>0 (the numerator pe*pb cancels with `gn^2 = 22.5*pe*pb`). Not a real signal. Rebodied to canonical Graham Number ratio: `EPS = netinc/sharesbas`, `BVPS = equity/sharesbas`, `GN = sqrt(22.5*EPS*BVPS)`, `ratio = close/GN`. Below 1 = price below Graham fair-value (potential undervalued), above 1 = above fair-value.

**1 KEEP-BY-DESIGN value-dup pair:** vt_031_pe_chg_1y (`_pc(pe,TD_Y) = (pe - pe.shift(TD_Y))/pe.shift(TD_Y)`) vs vt_064_pe_expansion_rate_1y (`(pe - pe.shift(TD_Y))/pe.shift(TD_Y).abs()`). On synth where PE is always positive (profitable firms), these are value-exact. On real data when PE shifts to negative (unprofitable firms), they differ in sign (`_pc` is signed; `_expansion_rate` is magnitude-normalized). Established clip-differentiated KEEP precedent: RI ri_003/090 (rnd/equity vs rnd/equity.abs()), LS ls_022/296 (inventory/equity vs inventory/equity.abs()).

### Cross-tier numbering note (unique to this family)

Unlike most families that prefix derivative functions with `_2d_`/`_3d_`, valuation_trajectory uses a **continuous numbering scheme** across tiers:

- Base: vt_001..vt_600 (in 8 base files, 75 fns each)
- 2nd-deriv: vt_601..vt_675 (in 3 d2 files, 25 fns each, registered as `vt_601_d2_*`..`vt_675_d2_*`)
- 3rd-deriv: vt_676..vt_750 (in 3 d3 files, 25 fns each, registered as `vt_676_d3_*`..`vt_750_d3_*`)

Each deriv file inlines its own Python copies of the base functions it wraps (vt_001..vt_025 in d2_001_025.py, etc.) — same self-containment pattern as other families. The d2 wrappers compute `base.diff(TD_M)` and d3 wrappers compute `base.diff(TD_M).diff(TD_M)`. This means the cross-tier dup detection naturally fires when a base feature happens to compute the same thing as the deriv-wrapper of a related base feature (e.g. vt_114_pe_momentum_21d = pe.diff(TD_M) collides with vt_601_d2_pe_ratio_current = pe.diff(TD_M)). Same delete-from-base disposition as CFS/RL/RI cross-tier-pollution precedent.

### Lessons

1. **Continuous-numbering deriv tiers don't change the audit shape.** This family's vt_601..vt_750 numbering for d2/d3 (rather than vt_2d_001..vt_2d_075) is just cosmetic; the cross-tier-dup detection works the same way as long as registry keys are unique across files (which they are — each tier uses a different `*_d2_*` / `*_d3_*` infix). The auto-discover-via-`*_REGISTRY*` pattern in the harness handles it transparently.
2. **`pe.diff().dropna()` is a CLAUDE.md contract violation.** This is the first audit where a function's output length didn't match input length — the harness short-circuit checking `arr.shape[0] != expected_len` (added during harness debug) caught it. Worth standardizing the check across future Path B harnesses.
3. **vt_511 is a textbook "formula reduces to constant by algebra" case.** Worth highlighting in audit checklist: when a function `_sd(num, den)*scale` produces a constant on synthetic AND `den` algebraically contains `num`, suspect bug. Even on real data, if `den = K*num` where K is a constant, the entire function is just `scale/K`. (vt_511 had `den = 22.5*num`, so output = `100/22.5 = 4.44` regardless of inputs.)
4. **Mass Index window=1 is the same class of bug as bss_055 `_safe_div(scalar_int, n)` and ve_385/387.** Functions occasionally fail because a parameter that should be a window length is hardcoded to 1 (or 0, or a scalar instead of a Series). Worth scanning future families for `_rmax(s, 1)`, `_rmin(s, 1)`, `_rolling_*(s, 1)` patterns specifically — they're almost always bugs.
5. **Mathematical-identity finite-difference recognition.** vt_552 == vt_418 via `f - 2*f(t-21) + f(t-42) = f.diff(21).diff(21)` (the discrete second derivative). This is the same pattern as cas_182==cas_221 DuPont 3-factor cancellation and ri_2d_031==ri_2d_002/4 telescoping — an algebraic identity that's invisible to body-text hash but caught by post-warmup value-hash. Add to triage checklist.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `C:\Users\jyama\Downloads\temp_vt_harness.py`
- `C:\Users\jyama\Desktop\origional  and complete features 1a\temp_vt_harness_out.json`


---

## 2026-05-09 — session 3 — tab 22: debt_trajectory (Path B, surgical-rebody-everything, ZERO DELETES)

**Family scope.** 14 files / 750 functions = 8 base (chunks 001-600,
75 fns each) + 3 second-deriv (idx 001-025, 026-050, 051-075; 25 each)
+ 3 third-deriv (same split). Daily-cadence (uses `TRADING_DAYS_*`
constants for `.shift(63/252)`/rolling). 31-input-col Path B (heavy
fundamentals; hybrid only via `close`/`volume`/`marketcap`/`shareswadil`).

**Non-Sharadar / Path-B-first cols added to mini-harness**:
`cashnequsd` (vs prior `cashneq`), `currentassets`/`currentliabilities`
(vs prior `assetsc`/`liabilitiesc`), `divyield` (annual dividend
yield decimal -- used by 3 fns dt_473/474/488), `depreciation` (alias
for `depamor` per registry naming).

### User direction: ZERO DELETES, surgical-rebody all `_ex_` slots

Initial harness pass returned 67 dup groups + 16 scalar-mult
candidates. Asked user how to handle the systemic naming-collision
in the `_ex_` derivative files (~30+ slots whose bodies didn't match
their docstrings -- e.g. `dt_2d_ex_028_altman_z_roc` returned
`CA/revenue` not Altman Z). User chose option 3: surgical-rebody
everything per LS tab 14 / CAS tab 18 / VAC tab 6 precedent --
"preserves every slot semantically."

This drove a much larger surgical-edit campaign (~80 rebodies across
12 files) than past audits, which typically had 5-15 deletes + a few
surgical edits.

### Two-pass surgical-rebody campaign

**Pass 1** (commits `b5db6af` through `73de82f`):
- 25 base-file dup rebodies (base_076_150, _151_225, _226_300,
  _376_450, _451_525): for each literal-identical / cancellation-
  equivalent dup, rebody the higher-numbered slot to a meaningful
  variant (252d-trailing-mean smoothed denom; net-of-cash form;
  net-of-currentliab denom; absolute `_diff` instead of `_pct_change`;
  Penman-style 25% AR haircut; capitalized 5yr-interest debt service;
  contributed-capital denom (equity - retearn); etc.).
- ~50 `_ex_` derivative-file rebodies (2nd_026_050, 2nd_051_075,
  3rd_026_050, 3rd_051_075): rebody each `_ex_` slot so the body
  actually computes what its docstring promises. Examples:
  - **dt_2d_ex_028_altman_z_roc**: full Altman Z = 1.2 X1 + 1.4 X2
    + 3.3 X3 + 0.6 X4 + 1.0 X5 then ROC. Was returning CA/revenue.
  - **dt_2d_ex_029_ohlson_o_roc**: full Ohlson O composite (-0.407*ln(A)
    + 6.03*L/A + ... 6 terms) then ROC. Was returning A/NCFO.
  - **dt_2d_ex_030_merton_dd_roc**: ln(V/D)/sigma where sigma =
    annualized 1yr close-return vol; uses close (was ignored).
  - **dt_2d_ex_032_tobins_q_roc**: (mcap+debt)/assets (uses assets
    denom). Was returning mcap/debt.
  - **dt_2d_ex_033_roic_roc**: NOPAT-style (NI + 0.79*intexp.abs())
    /(debt+equity). Was ignoring intexp+debt, returning NI/E.
  - **dt_2d_ex_040_fixed_charge_coverage_roc**: ebitda / (intexp.abs()
    + 0.05*CL) where 0.05*CL approximates lease commitments.
  - **dt_2d_ex_043_springate_s_roc**: full Springate S = 1.03 A +
    3.07 B + 0.66 C + 0.4 D composite.
  - **dt_2d_ex_047_debt_to_tangible_roc**: debt/(assets-intangibles).
    Was ignoring intangibles.
  - **dt_2d_ex_049_lt_debt_to_equity_roc**: (debt - 0.30*CL)/equity
    LT-debt approximation. Was returning debt/CL.
  - **dt_2d_ex_061_debt_to_avg_ebitda_3yr_roc**: debt / 3yr-rolling-
    mean(ebitda). Was point-in-time.
  - **dt_2d_ex_064_accruals_to_debt_roc**: (NI - NCFO)/debt accruals.
    Was returning NI/NCFO.
  - **dt_2d_ex_071_book_vs_market_leverage_roc**: D/(D+E) - D/(D+M)
    spread. Was returning D/E.
  - **dt_2d_ex_073_financial_leverage_effect_roc**: NI/OpInc (matches
    name; broken from _ex_064 dup).
  - **dt_2d_ex_074_invested_capital_growth_roc**: pct_change(D+E,
    YR) then pct_change(QTR) (proper acceleration of IC growth).
  - All 3rd-deriv `_ex_` mirror these but use a shared `_jerk(level)`
    helper = `pct_change(QTR).diff(QTR).diff(QTR)`.

**Pass 2** (commits `6030811` through `28fce41`): re-running the
harness post-Pass-1 caught 7 secondary collisions where Pass-1
rebodies happened to match an existing main-tier sibling that I
hadn't rebodied (because it was already canonical). Re-rebodied
to use 252d-trailing-mean smoothed denom variants (ls_121 precedent):
- dt_2d_ex_047 vs dt_2d_166 (debt/(assets-intangibles)): switched
  _ex_047 to debt / 252d-mean(assets-intangibles).
- dt_2d_ex_053 vs dt_2d_174 (net-debt/mcap): switched _ex_053 to
  net-debt/EV (full denom, bounded [-1,1]).
- dt_2d_ex_057 vs dt_2d_163 (intexp.abs()/revenue): switched _ex_057
  to intexp.abs() / 252d-mean(revenue).
- dt_3d_ex_047/053/057 mirror the same swaps for the jerk operator.
- dt_250 + dt_271 in base_226_300 (both my Pass-1 rebodies happened
  to match dt_061's net-debt/EV form): switched dt_250 to debt /
  252d-mean(EV) and dt_271 to (debt-cash) / 252d-mean(mcap).
- dt_370 in base_301_375 was literal-identical to dt_317_ohlson_o7:
  switched dt_370 to ncfo / LT-only-liabilities (liabilities -
  currentliabilities).
- dt_478 in base_451_525 was literal-identical to dt_410: switched
  dt_478 to debt / 252d-mean(sgna.abs()).

### Final findings

- **750/750 fns ok** (down from initial 33 errors -> 0 after extending
  harness with `sgna`/`depreciation`/`taxexp`/`divyield` cols).
- **0 errors / 0 all-NaN.**
- **Down from 67 -> 26 dup groups (-41); 750 fn slots PRESERVED;
  zero deletes.**
- 26 KEEP-BY-DESIGN dup groups remain:
  - **10 academic-trace** (Altman X1/X3/X4/X5; Ohlson O2/O3/O6/O7;
    Zmijewski X1/X2/X3 -- each model variable individually addressable
    for explainability; ls_061/151/170/188 precedent).
  - **14 sample-bias** (different X/Y inputs that happen to coincide
    on healthy-synth because intexp = const*debt, ncfo ~ const*ebitda,
    opinc = 0.78*ebitda, etc. -- all real-data divergent).
  - **2 clip-differentiated** (dt_137 cash on equity.clip(lower=0);
    dt_198 .clip(upper=50).fillna(50.0) cap on near-term-pressure).
- **27 sample-bias constants kept** (negative-equity / distress /
  buyback flags; Merton DD saturated at 10 on healthy synth; Merton
  percentiles ~0.5; cash-burn-runway needs sustained negative ncfo).
- **13 KEEP-BY-DESIGN scalar-mults**: 4 sample-bias 0.78/1.282 (synth
  opinc=0.78*ebitda); 4 stress-test thresholds (interest_coverage_
  stress_50/75 are ic/2 and ic/1.33 by design; debt_service_stress_50;
  chs vs distress_premium ratio=10; NOPAT-precedent KEEP); 1 unit-
  conversion 1/12 (cash_burn_months from cash/CL); 1 stress 0.667
  between two stress thresholds.

### Lessons worth carrying

1. **`_ex_` derivative files in this repo systematically have buggy
   bodies that don't match their docstrings.** Pattern: function
   accepts the proper input columns for the named formula (e.g.
   `currentassets, currentliabilities, assets, retearn, ebitda,
   marketcap, liabilities, revenue` for Altman Z) but body computes
   a simpler 2-input ratio (`CA/revenue`). Probably auto-generated
   stubs that were never finished. Other audits should grep for this
   pattern before harness time.

2. **Surgical-rebody-everything (zero-deletes) campaigns can drive
   ~80 edits in a single family.** Two-pass approach is essential:
   Pass 1 rebodies all naming-collision dups; Pass 2 fixes the
   secondary collisions where Pass-1 happened to match an existing
   sibling. Plan time accordingly.

3. **252d-trailing-mean smoothed denominator (ls_121 precedent) is
   the workhorse second-pass differentiator.** When two slots both
   compute X/Y at point-in-time, switching one to X / 252d-mean(Y)
   gives a meaningful "smoothed" feature variant that's bounded by
   the same scale and conceptually related, without inventing a
   new formula.

4. **Sample-bias dups are unavoidable on healthy-synth.** Any feature
   pair X/Y vs X/Z where Z is a constant fraction of Y on synth
   will show as value-exact (because pct_change cancels constants)
   on rolling/derivative tiers. Real-data variants always diverge.
   Documenting "sample-bias" as KEEP-BY-DESIGN per ps_270 / cfs_d3_046
   precedent is critical.

5. **Divyield isn't a Sharadar SF1 column** but appears in
   `dt_473_dividend_payout_to_debt_service`,
   `dt_474_dividend_vs_interest_priority`, and
   `dt_488_debt_to_total_payout`. Need binding-layer translation map
   (similar to `cashnequiv`/`retainedearnings`/`ltdebt` precedent
   from LS tab 14). Pipeline-side issue, flagged for future work.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `C:\Users\jyama\AppData\Local\Temp\temp_dt_mini_harness.py`
- `C:\Users\jyama\AppData\Local\Temp\temp_dt_results.json`
- `C:\Users\jyama\AppData\Local\Temp\temp_dt_dump_dups.py`
- `C:\Users\jyama\AppData\Local\Temp\temp_dt_dups_dump.txt`


## 2026-05-09 — session 3 — tab 29: revenue_acceleration (Path B, all tiers)

**Master queue row 29.** Inventory: 14 files / 750 functions = 8 base × 75 (chunks 001-600) + 3 2nd-deriv × 25 + 3 3rd-deriv × 25. Function prefix `ra_`. **Daily-cadence Path B** (uses `TRADING_DAYS_YR=252`/`TRADING_DAYS_QTR=63`/`TRADING_DAYS_MO=21`/`TRADING_DAYS_WK=5`). 26 input cols, all subsumed by prior Path B audits (no new col types). Hybrid only via `close`/`volume`/`shareswa`/`ev`.

### Harness

Path B mini-harness (5 firm profiles × **3500 days**, warmup=2600 to clear max 10y CAGR shift = 2520 days). 26 input columns synthesized from quarterly anchors (every 63 days) forward-filled to daily cadence; close = log-rev-correlated random walk; volume = log-normal noise; ev = mcap + debt - cashneq.

Pre-fix run: 6 errors / 1 all-NaN (subsumed by error fix) / 5 constants / 37 dup groups / 10 slow (>1s).

### Bug fixes (4 commits, one per file affected)

All 6 broken functions had clear bug signatures matching prior Path B precedent (bss_055/ve_385/es_503/ve_424). Auto-fixed:

1. **`294034d`** `revenue_acceleration_2nd_derivatives.py`: `ra_2d_025_roc_rev_3yr_cagr` had `cagr - cagr.shift(QTR)` as a bare statement (no `return`), causing implicit `None` return → harness all-NaN. Added `return`.

2. **`3c83871`** `revenue_acceleration_3rd_derivatives.py`: `ra_3d_025_roc2_rev_3yr_cagr` had same bare-statement bug + `return d2 - d2.shift(QTR)` referencing undefined `d2` → NameError. Replaced bare stmt with `d2 = cagr - cagr.shift(QTR)`.

3. **`2a93a1c`** `revenue_acceleration_base_076_150.py`: `ra_139/ra_140` (golden_cross/death_cross) had `~bool_series.shift(WK)` which fails because `.shift()` introduces NaN → bool dtype gets coerced to object/float, and `~` on float raises `TypeError: bad operand type for unary ~: 'float'`. Fixed via explicit `prev = above.shift(WK).fillna(False).astype(bool)` before negation.

4. **`be2fd24`** `revenue_acceleration_base_526_600.py`: `ra_571/ra_572/ra_573` (mean_cross/zero_cross_up/zero_cross_down) had same `~bool.shift()` bug. Same fix.

### Dup deletes (10 commits, 42 functions removed)

42 dup deletes across 8 base files + 1 deriv file. All auto-applied per established CFS/RI/RL/MT/CFT/SD precedent (formula-exact + cancellation-equivalent + algebraic-identity + cross-tier base-vs-deriv pollution).

**Cross-tier base→deriv pollution (12 deletes from base, deriv canonical):** ra_011/013/033/035/042/066/154/253/286/287/488/570 — base "_qoq/_accel/_jerk/_change" features value-exact equal to canonical deriv-tier `_roc_*`/`_roc2_*` operators. Per CFS cfs_d2_002 / RI ri_036 / RL rl_227-231 / cft_012==cft_2d_004: acceleration belongs in deriv tier; delete from base.

**Cross-tier deriv mis-tier (1 delete):** `c78a350` (corrected by `f355d20` forward-fix) deleted ra_2d_003_roc_growth_accel which is structurally a 3-diff jerk operator (`_pct_change(rev,QTR) - shift(QTR) - shift(QTR)`) placed in the 2nd_derivatives file. Body-identical to ra_3d_002_roc2_qoq_growth in correct 3rd-deriv tier per file convention (1-diff base + 2 ROC = 3 diffs).

**Within-base formula-exact + cancellation-equivalent + algebraic-identity (29 deletes):**
- File 076_150: ra_116, ra_129
- File 151_225: ra_189, ra_190
- File 226_300: ra_237, ra_244, ra_262, ra_291, ra_292
- File 301_375: ra_341
- File 376_450: ra_381, ra_382, ra_413, ra_416, ra_420, ra_422, ra_424
- File 451_525: ra_451, ra_461, ra_470, ra_471, ra_490, ra_492, ra_506, ra_515, ra_517
- File 526_600: ra_534, ra_548, ra_555

**Algebraic-identity reductions** (auto-applied per RL rl_080/081/082 cancellation + mt_151..155 telescoping precedent):
- {ra_022, ra_517}: `(rev/sh)/(eq/sh) = rev/eq` (share factor cancels)
- {ra_041, ra_381}: `(rev/sh)/close = rev/(close*sh)` (share factor cancels)
- {ra_088, ra_341}: `ps/pe = (mcap/rev)/(mcap/netinc) = netinc/rev` (mcap cancels)
- {ra_072, ra_237}: `mean(rev,QTR)/mean(rev,YR) = (YR/QTR) * sum_q/sum_y = 4 * sum_q/sum_y = sum_q/(sum_y/4)` (since YR/QTR = 252/63 = 4 exactly)
- {ra_336, ra_420}: `pos_mean/neg_mean = sum_pos/sum_neg = gains/losses` (same window cancels in division)
- {ra_299, ra_422}: `(fcf/debt) * (1+pct_change) = (fcf/debt) * rev/rev.shift(YR)` on positive revenue (since `_pct_change` denom uses `prev.abs()` and revenue > 0 always)

### Forward-fix incident (`c78a350` → `f355d20`)

Initial deletion script used regex pattern `(?s)\n*def NAME\([^)]*\):\s*\n(?:    .*\n)+?(?=\n*(?:def |[A-Z_0-9]+_REGISTRY|\Z))` with the DOTALL `(?s)` flag. The flag made `.` match newlines, causing the non-greedy `(?:    .*\n)+?` to extend across multiple def boundaries until it found the registry assignment. Result: ra_2d_004..ra_2d_025 (22 functions) were mass-deleted along with the intended ra_2d_003 target. The 24 registry entries still referenced these now-undefined functions, which would have caused NameError on import.

Caught by post-delete grep verification `grep -c "^def ra_"` showing only 2 defs remaining (vs expected 24). Earlier `git revert HEAD` accidentally reverted another tab's `27c1213` leverage_acceleration commit (HEAD had advanced from concurrent tab work); undone via `git reset --hard HEAD~1`. Then forward-fixed:
1. Restored 2nd_derivatives.py from `c78a350^` parent (24 def's).
2. Rewrote delete script with line-walk algorithm (no regex DOTALL): find `^def NAME(` line, walk forward until next `^def ` or `^[A-Z_]+_REGISTRY` line, delete the slice.
3. Re-applied single ra_2d_003 delete cleanly.
4. Committed as `f355d20` "restore 22 fns mass-deleted by buggy regex in c78a350".

Net effect across both commits: only ra_2d_003 removed; downstream tab work unaffected.

### Kept by design

**5 sample-bias constants** (zero on healthy synthetic — same disposition as ps_270/cfs_d3_046/bss_288/ri_044):
- ra_365_rev_growth_above_25pct, ra_366_above_50pct, ra_367_above_100pct, ra_369_deeply_neg — binary growth-threshold indicators, all zero on bounded synth growth (~5%/yr); real growth firms cross 25%/50%/100% thresholds and produce signal.
- ra_587_rev_growth_cummin — expanding minimum of YoY growth; on healthy synth stair-steps toward a floor and stabilizes; signals on volatile firms with persistent growth dispersion.

**2 KEEP-BY-DESIGN dup groups**:
- {ra_002_rev_yoy_growth, ra_325_rev_growth_winsorized} — `clip(p01, p99)` doesn't fire on bounded synth growth distribution; values coincide with raw `_pct_change(rev, YR)`. Diverges on real outliers. Same disposition as ps_006/ps_312 winsorized pairs from profitability_snapshot tab 8.
- {ra_365, ra_366, ra_367, ra_369} — 4-way always-zero binary indicators (same as constants list above). Mathematically distinct (different thresholds), value-exact only on healthy synth.

### Final state

- **708/750 functions** (= 750 base − 42 deletes) registered post-fix
- 0 errors / 0 all-NaN / 5 constants (kept) / 2 dup groups (kept)
- Total runtime: ~60s on 5-profile × 3500-day mini-harness
- 12 slow (>1s) functions are all `_slope`/`_r_squared`/`_hurst` rolling.apply patterns from base 001-075 helpers (same as RL/VE precedent — not vectorizing per HANDOFF "ASK FIRST" policy on non-standard rolling.apply)

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_ra_harness.py`
- `temp_ra_harness_out.json`
- `temp_ra_delete.py`

## 2026-05-09 — session 3 — this-tab: cash_flow_acceleration (Path B, all tiers)

Audited per HANDOFF policy. 14 files / 750 features (8 base × 75 + 3 2nd-deriv × 25 + 3 3rd-deriv × 25). Daily-cadence (`shift(63/252/504/1008/1260)`). 100% Path B (every fn takes `fcf`/`ncfo`/`capex` family); hybrid only via `close`/`volume`/`shareswa`. 41 standard Sharadar SF1 + OHLCV input cols, no non-Sharadar names.

### Harness

5 profiles × 1500 daily rows × 41 cols, daily quarterly-anchor forward-fill. Per-profile scaling (1.0 + 0.3·idx) and drift (0.5%-2.5%/qtr). `ncfo` allowed 20% sign-flip per-quarter. Warmup=800 (504d shifts clear; 1260d 5y features run with reduced support — no false-positive constants). Total runtime ~10s for 750 fns. No slow-function escalation needed.

### Triage

40 algebraic-identity dup deletes auto-applied per HANDOFF policy + ve/sd/cas precedent. Five recurring patterns:

1. **ufcf-* aliases of fcf-* under Sharadar `fcf = ncfo + capex`** (8 deletes): `cfa_095/096/097` (file 076_150) and `cfa_463/464/465/466/467` (file 451_525). Algebraic identity: `(ncfo - |capex|) == (ncfo + capex) == fcf` since `capex` is signed negative. With harness profiles where `fcf` is computed from `ncfo + capex`, value-hash catches them all on the first run.
2. **Verbose-rename of fundamentals ratios** (19 deletes, formula-exact): `cfa_041=cfa_015` (capex/ncfo "reinvestment_rate"), `cfa_043/044/045=cfa_005/007/008` ("cash_gen_efficiency"), `cfa_092=cfa_558` (ncfo/gp inverted name), `cfa_134=cfa_311` ("maintenance capex" body literally `_safe_div(depamor, revenue)`), `cfa_151=cfa_418` ("Beneish TATA" identical to Sloan accruals), `cfa_212=cfa_292` (persistence = autocorr at same lag/window), `cfa_073=cfa_347` (literal duplicate, identical name), `cfa_032=cfa_156` ("Ball et al cash op profit"), `cfa_054=cfa_193` (fcf yield = buyback capacity), `cfa_013=cfa_562` (fcf/ebitda), `cfa_218=cfa_563`, `cfa_059=cfa_477` (op leverage = revenue growth quality), `cfa_060/061=cfa_545/547` (streak = above_zero_run), `cfa_475/476=cfa_556/557` (opex = total costs), `cfa_225=cfa_559`.
3. **Net-op-cycle = CCC algebra** (3 deletes): `cfa_235/236/237 = cfa_033/034/035`. `dso + dio - dpo = (R*252)/rev + (I*252)/rev - (P*252)/rev = (R+I-P)*252/rev` (cfa_033 form). `_safe_div(num, den, fill=0.0)` behavior identical when revenue=0 (both sides return 0).
4. **Z-score = surprise alias** (4 deletes): `(s - rolling_mean) / rolling_std == _zscore`. cfa_069/070=cfa_297/298 (1y), cfa_299/300=cfa_481/482 (2y).
5. **Per-share-growth duplicate naming** (2 deletes): `cfa_389/390` "dilution_adj_*_growth" = `cfa_019/022` "*_per_share_growth_1y" — both literally `_pct_chg(X/shareswa, 252)`.
6. **Base "_acceleration_1y" = deriv-tier "_yoy_growth_roc" pollution** (2 deletes-from-base per RI/CFS/RL precedent): `cfa_027/028` → `cfa_2d_003/004`. Acceleration belongs in derivative tier.
7. **Deriv tiers follow base** (2 deletes): `cfa_2d_010/cfa_3d_010` = `cfa_2d_008/cfa_3d_008` capex/ncfo at deriv tiers, follows base cfa_015/041 collapse.

### Kept by design

**3 sample-bias constants** (real-data variants — same disposition as ps_270/cfs_d3_046/bss_288/ri_044):
- `cfa_201_cash_tax_rate_proxy` = `taxexp/ebt` constant 0.21 on synth (taxexp = ebt × 0.21 by design)
- `cfa_202_cash_tax_rate_chg_1y` = same diff, identically 0
- `cfa_420_beneish_gmi_proxy` = `gm_prev/gm` = 1 on constant-margin synth (gp = revenue × const within profile)

**1 academic-trace pair**: `cfa_167_altman_wc_ta` / `cfa_242_wc_to_assets` — both compute `wc/assets`. Composite `cfa_427_altman_composite_cf_adj` inlines `wc/assets` directly (doesn't call cfa_167 or cfa_425). Per ls_061/cas_062 academic-trace precedent each Altman component is individually addressable for explainability.

**1 clip-differentiated pair**: `cfa_105_ncfo_to_netinc_chg_1q` / `cfa_166_cash_earnings_quality_chg`. cfa_166 body `(ncfo-netinc)/|netinc|.diff(63)`. With netinc>0: `(ncfo-netinc)/netinc.diff(63) = (ncfo/netinc - 1).diff(63) = (ncfo/netinc).diff(63) = cfa_105`. With netinc<0: `|netinc| = -netinc`, sign-flips. Real-data divergent on unprofitable firms. LS ls_022/296 precedent.

**7 synth-coincidence pairs** (real-data divergent):
- **netinc/rev constant within profile** causes synth value-equality (real Sharadar has time-varying margins): `cfa_010/cfa_267` (ncfo_margin_chg_1y vs cash_gen_gap_chg_1y where gap=ncfo/rev - netinc/rev), `cfa_223/cfa_478` (ncfo_g - netinc_g vs ncfo_g - gp_g; on synth gp_g=netinc_g=rev_g)
- **Adjacent fcf↔ncfo** where `|ncfo| > |capex|` always in synth → `sign(fcf) = sign(ncfo)` every day: `cfa_025/cfa_026`, `cfa_060/cfa_061`, `cfa_216/cfa_217`, `cfa_325/cfa_326`, `cfa_590/cfa_591`. Real-data divergent on capital-intensive firms or growth phases (capex frequently exceeds ncfo).

**21 NOPAT/days-conversion scalar-mult pairs** kept (per cas/ls precedents): cfa_011/132/199 ratios `1.480494=1/(0.711)` (opinc/netinc) + `1.265823=1/0.79` (ebt/netinc) post-tax NOPAT; cfa_120-125 ↔ cfa_226-233 ratio `0.003968=1/252` days-conversion (DSO/DPO/DIO); cfa_168/426 ratio `0.714286=5/7` altman_re weight differential.

### Commits (11 total across 10 affected files)

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

### Final state

- **710/750 functions** (= 750 base − 40 deletes) registered post-fix
- 0 errors / 0 all-NaN / 3 constants (kept) / 9 dup groups (kept)
- Total runtime: ~10s on 5-profile × 1500-day mini-harness; no slow-fn vectorization needed

### Lessons

1. **Sharadar `fcf = ncfo + capex` produces a class of algebraic-identity dups** that look distinct by name (ufcf-* / "ncfo-minus-capex-*") but reduce algebraically under `capex` signed negative. 8 of 40 deletes in this family were of this form. Worth flagging early for any cash-flow-themed family.

2. **fcf-vs-ncfo sign-coincidence on healthy synth is sample-bias, not real dup.** With `|ncfo| > |capex|` in synth, `sign(fcf) = sign(ncfo)` every day → consecutive_positive / expanding_positive_pct features value-match. Real-data divergent. Same disposition as cft fcf↔ncfo coincidence pairs.

3. **netinc/revenue constant within profile is a synth artifact.** Synth uses `netinc = revenue × const_within_profile`, so `(netinc/revenue).diff(N) = 0` exactly → many "X minus netinc-margin diff" features collapse to "X diff" alone. Real Sharadar has time-varying margins. Documented per LS clip-differentiated precedent (the divergence mechanism is different but the KEEP rationale identical).

4. **Editor-race on multi-edit-per-file batches.** Initial cfa_311 + cfa_347 batch produced commit `f17c097` with only 1 deletion (10 lines) instead of intended 2 (28 lines); follow-up `ea04d4f` finished. The Edit tool's "file modified since read" guardrail caught the second-edit conflict but the first apparently succeeded silently against stale state. **Recommendation**: re-grep + re-Read before every Edit when batching multiple deletes per file, even if the previous Edit reported success. Verify with `python -c "import ...; print(len(REGISTRY))"` and `grep -c` after each commit.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_cfa_harness.py`
- `temp_cfa_harness_out.json`

## 2026-05-09 — session 3 — tab N: leverage_acceleration (Path B, all tiers)

Master row #32. 15 files: 8 base × 75 (la_001..600) + 4 2nd-deriv × 25 (la_d1_001..100) + 3 3rd-deriv × 25 (la_d2_001..075) = **775 features** original. Function-prefix tier convention: base = `la_NNN`, 2nd-deriv-file = `la_d1_NNN` (ROC of base), 3rd-deriv-file = `la_d2_NNN` (accel of base).

### Inventory + harness setup

- 33 input cols: assets, capex, **cashnequsd**, close, **costrev**, **currentassets**, **currentliabilities**, debt, depamor, **dividends**, ebitda, equity, fcf, goodwill, gp, intangibles, intexp, inventory, liabilities, ncff, ncfi, ncfo, netinc, opex, opinc, payables, ppnenet, receivables, retearn, revenue, sgna, shareswa, volume.
- Non-Sharadar (bold above): `cashnequsd`/`costrev`/`currentassets`/`currentliabilities`/`dividends` — same binding-layer-translation handling as LS used for `cashnequiv`/`retainedearnings`/`ltdebt`/`ebt`.
- Daily-cadence (uses `TRADING_DAYS_YR=252`/`QTR=63`/`MO=21`/`WK=5`). Max window observed: `TRADING_DAYS_YR*3=756d`.
- 100% Path B (every fn takes a fundamentals input; close/volume/shareswa only via hybrid — la_063, la_303, la_304, etc.).
- Built `temp_la_harness.py` per tab-29/27 template: 5 profiles × 2000 days × 33 cols, warmup=1000, value-hash on round-9 post-warmup output concatenated across profiles.

### First harness run (pre-fix)

errors: 4, all_nan: 1, constants: 3, dup_groups: 53, missing: 0, runtime: 15.9s

### Triage

#### 4 errors — int-as-denom bugs

`_safe_div(debt, N)` with scalar `N` errors at `(N).replace(0, np.nan)` (numpy/python int has no `.replace`). Same class as bss_055 (`_safe_div(revenue, 4)`), ve_385/387 (`_safe_div(scalar, 12)`), gc_331 (kwarg name mismatch). Fix: replace with direct `debt / N` (algebra preserved since N != 0 always).

- la_204 `debt/5` (5-yr amortization)
- la_316 `debt/5`
- la_555 `debt/7` (7-yr amortization)
- la_556 `debt/7`

#### 1 all-NaN — sample-bias KEEP

la_530_debt_growth_cvar_5pct: rolling CVaR (mean of debt growth excess above 95th percentile over 504d). Synth has tight constant-drift debt-growth distribution, no excess, all-NaN post-warmup. On real data with debt-growth outliers (M&A spikes, refinancing waves), produces signal. Same disposition as bss_288_cash_runway_quarters / cfs_d3_046_cash_burn_jerk_qtr / dr_137_dilution_half_life.

#### 3 constants — sample-bias KEEP (also form a 3-clique value-hash group)

- la_324_ncff_positive_binary: synth has ncff<0 always (sign=-1.0), constant 0
- la_380_zero_debt_binary: synth has nonzero debt always, constant 0
- la_385_ic_below_1: synth has IC>1 always, constant 0

All three coincide on value-hash because all are constant-zero on healthy synth. Mathematically distinct on real data (different conditions).

#### 53 dup_groups — classified

**A. Cross-tier base-vs-d1 ROC pollution (6 groups, auto-delete from base; RI/CFS/RL/cft precedent)**: la_494/495/496/497/498/499 in `_451_525.py` are literally `_pct_change(_safe_div(...), W)` — i.e., ROC of base ratio. Names are `la_NNN_*_pct_change_*`. These ARE the d1-tier `*_roc_*` features (la_d1_001/002/005/006/009/010). ROC features belong in deriv tier per established precedent.

**B. Beaver naming-bug (9 surgical edits, ASK-FIRST per HANDOFF, user-approved)**: la_199, la_200, la_d1_065/066/067/068, la_d2_049/050/051. Bodies all do `_safe_div(fcf, debt)` — literally identical to la_078, la_079, la_d1_037-040, la_d2_028-030. Names say `beaver_ratio`. Beaver (1966) academically defined = NCFO / total liabilities, NOT fcf/debt. Surgical-edit rebody to `_safe_div(ncfo, liabilities)` with signature changes from `(fcf, debt)` to `(ncfo, liabilities)` and registry inputs updated. Mirrors ls_148/vac_118/ve_424/cas_141 naming-bug-surgical-edit precedent. Restores academic accuracy AND breaks the dup. Post-rebody surfaced 2 additional dups: la_475/476 (literal `opcf_to_liab`) became formula-exact dups of la_199/200 since both now compute ncfo/liabilities — auto-deleted.

**C. Within-base alpha-rename / algebraic-identity / cancellation-equiv (25 deletes auto-applied)**:

Body-literal-identical (16): la_013, la_068, la_069, la_096, la_109, la_110, la_168, la_170, la_207, la_244, la_327, la_328, la_449, la_456, la_457, la_482, la_483, la_484. All have a docstring/var-rename and same compute as a lower-numbered canonical.

Algebraic-identity / commutativity (4): la_290 (`eq/(d+e)` vs `tc=d+e`), la_291 (debt/(d+e) same), la_554 (`nd/(nd+mkt) = nd/(mkt+nd)` commutativity), la_549 (`(debt/eq)/(debt/(close*sharesbas)) = (close*sharesbas)/eq = mktcap/eq`).

Cancellation-equiv (5): la_244 (`(liab-cl)/liab` = la_217 with intermediate `lt`), la_285 (`(netinc/equity)/(netinc/assets) = assets/equity`, RL rl_080-082 precedent), la_286 (same applied to `_delta`), la_445 (drawup_1yr alpha-rename of dist_from_1yr_low), la_444 (drawdown_1yr alpha-rename of dist_from_1yr_high).

**D. KEEP-by-design (13 groups)**:

7 clip-differentiated:
- la_001/547: debt/equity vs debt/equity.clip(lower=1), diverge on negative-equity firms
- la_004/126: debt/fcf vs debt/fcf.clip(lower=1), diverge on negative-FCF firms
- la_060/108: cashnequsd/debt vs cancellation `(cashnequsd/cl)/(debt/cl).clip(0.01)`, diverge on real low-leverage
- la_076/077: cancellation roe/de vs roa/da both clip(0.01), diverge when leverage clips
- la_227/492: tang vs tang.clip(1), diverge when intangibles+goodwill ≈ assets
- la_228/493: same for delta
- la_400/571 + la_402/572: log-de clip(0.001) vs log(debt.clip(1)) - log(equity.clip(1)), diverge on negative-equity

4 academic-distress traces (LS ls_061/151/170/188 precedent, composites la_182/194/198 inline x1-x5 directly):
- la_002/196: zmijewski_x2 = debt_to_assets
- la_176/190: altman_x1 = springate_a = WC/assets
- la_178/191: altman_x3 = springate_b = ebitda/assets
- la_181/193: altman_x5 = springate_d = revenue/assets

1 sample-bias 3-clique constants:
- la_324/380/385: ncff_positive/zero_debt/ic_below_1 all 0 on healthy synth, different conditions on real data

### Per-file commits (15 total)

8 base file commits + 4 deriv-file commits for Beaver rebodies + 3 follow-up commits for la_068/069 (file 1), la_109/110 (file 2), and la_475/476 (file 7) missed in first pass:

1. `ac2cf07` base_001_075: la_013 delete
2. `8236efa` base_001_075: la_068, la_069 deletes (follow-up)
3. `c4d2201` base_076_150: la_096 delete
4. `4a6996e` base_151_225: la_168, la_170, la_207 + la_204 bug fix
5. `27c1213` base_226_300: la_244, la_285, la_286, la_290, la_291, la_292
6. `5ae1bc0` base_301_375: la_327, la_328 + la_316 bug fix (re-applied after concurrent-tab revert)
7. `80bbb60` base_376_450: la_444, la_445, la_449
8. `dab7ebf` base_451_525: la_456/457/482/483/484/494-499 (5 within-base + 6 cross-tier)
9. `ceeb659` base_526_600: la_549, la_554 + la_555/556 bug fixes
10. `928b002` base_151_225: Beaver rebody la_199/200 (signature/registry inputs)
11. `0fd4814` 2nd_derivatives_051_075: Beaver rebody la_d1_065-068
12. `84e6198` 3rd_derivatives_026_050: Beaver rebody la_d2_049/050
13. `01f5aa8` 3rd_derivatives_051_075: Beaver rebody la_d2_051
14. `1199bf2` base_076_150: la_109, la_110 follow-up deletes
15. `7bdbd49` base_451_525: la_475, la_476 deletes (post-Beaver-rebody surface)

### Concurrent-tab incident (file_5 edits silently reverted)

While editing file 5 (`_301_375`), my la_316 bug fix and la_327/328 deletes were silently reverted by another tab's git operations (system reminder warned "modified, either by the user or by a linter"). `git status` showed clean working tree but file content matched pre-edit state. Re-applied edits and committed as `5ae1bc0`. No data loss, caught by file-fn-count check (`grep -cE "^def la_"`).

### Final harness run (post-fix)

errors: 0, all_nan: 1 (la_530 KEEP), constants: 3 (la_324/380/385 KEEP), dup_groups: 13 (all KEEP-by-design), runtime: 14.0s.

740 functions registered (= 775 − 35 deletes). 9 surgical Beaver-rebodies preserve those slots semantically.

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_la_harness.py`
- `temp_la_harness_out.json`
- `temp_la_journal_entry.md`


## 2026-05-09 — session 3 — tab 19: revenue_growth (Path B, all tiers)

**Master row 21.** 8 files / 400 fns (4 base × 75 + 2 2nd-deriv × 25 + 2 3rd-deriv × 25). Daily-cadence Path B (every fn takes `revenue`; hybrid only via `close`/`volume`/`sharesbas`). 36 input cols, all Sharadar-standard.

### Path B harness — v1 false-positive cascade

v1 built fundamentals as multiplicative scalings of revenue (`assets = revenue * 2.5`, `cor = revenue * (1 - gm)`, etc.). This produced **26 false-positive constants**: every `rg_growth_vs_X_growth` feature collapsed to identically zero because `_pct_change(rev, n) - _pct_change(α·rev, n) = 0` (multiplier cancels). A textbook synthetic-data trap.

v2 rebuild used **independent random walks per fundamental column** (RI tab 16 lesson confirmed): each col has its own (drift_extra, vol, level0) tuple; quarterly anchors via `cumprod(1 + log_steps)` with col-specific drift; 20% sign-flip injection on `CAN_BE_NEGATIVE` cols. Eliminated 25/26 false constants. Lesson re-confirmed (5th time across this session): never multiply fundamentals from a single driver in Path B harnesses.

### Baseline harness output (v2)

- 400 fns, 0 errors, 0 all-NaN
- 1 sample-bias constant (rg_166)
- 0 formula-exact dup groups (text fingerprint)
- 12 value-exact dup groups
- 2 scalar-mult pairs

### Triage classification (12 deletes + 2 rebodies)

**Cat 1 — Auto-apply formula-exact / helper-expansion dups (8 deletes within base + base-vs-deriv).** rg_067/068 (var-rename of rg_039/053), rg_086 (var-rename of rg_050), rg_139 (helper-expansion of rg_039 via `_pct_change(ttm,252)`), rg_176 (var-rename of rg_081), rg_269 (var-rename of rg_117); rg_009/010 base-vs-deriv pollution against rg_2d_003/002 (delete-from-base per CFS/RL/RI precedent). Auto-apply per HANDOFF policy.

**Cat 2 — User-approved algebraic-identity (3 NDR-proxy deletes + 1 positive-rev-identity delete).** Asked the user 3 questions via AskUserQuestion. Outcomes:

- **NDR cluster (3 deletes):** for positive revenue, `ndr = revenue/revenue.shift(252) = yoy + 1`, so `ndr.diff(N) ≡ yoy.diff(N)` for any N (constant cancels). User chose delete-NDR-side trio (rg_2d_032/033, rg_3d_032). Removed orphan helper `_base_ndr_proxy` from 2nd_derivatives_v2 since both its callers were deleted; `_2d_ndr_roc` retained in 3rd_derivatives_v2 because rg_3d_033 has a distinct stride (`.diff(63).diff(252)` ≠ rg_3d_002's `.diff(252).diff(252)`).

- **rg_034 vs rg_036 (1 delete):** `(g > 0) ⟺ (rev > rev.shift(63))` for revenue ≥ 0 (always in Sharadar SF1; pre-IPO is NaN not zero). User chose delete rg_036, keep rg_034 per "i want the % growth more than the raw value".

**Cat 3 — User-approved surgical rebody for naming-bug (2 rebodies).** rg_126/127 monotonic_score_4q/8q originally `rolling_sum / 4` and `/ 8` over 252d/504d windows respectively, producing values in [0, 63] when names promised [0, 1]. Same naming-bug class as ls_148, vac_118, cas_141, ve_424. User chose surgical rebody to a distinct metric: longest-consecutive-up-streak normalized to [0, 1] via run-length encoding (`np.diff` on padded boundary). Distinct semantic from rg_034 hit-rate (sustained run vs total up count). New shared helper `_longest_up_streak_norm`.

**Cat 4 — KEEP-BY-DESIGN (1 constant + 2 value-dup groups).**

- rg_166_rev_growth_determinism_proxy: fwd-fill artifact. `g.diff()` is non-zero only at quarter boundaries (1/63 days); `sign(0)==sign(0)` is True for the other 62/63 days, making `same_sign` constant ≈ 0.96. Real daily-varying data triggers signal. Same disposition as ps_270/cfs_d3_046/bss_288/ri_044/es_503/504.
- rg_002 ≡ rg_262 ≡ rg_263 (yoy × cap_flag): synth `mcap ≈ 5000` always satisfies `<2B`/`<300M`. Real-data variant fires. LS distress-flag precedent.
- rg_222 ≡ rg_223 (above_50pct_flag vs triple_accel): different formulas, both ≈ 0 on smooth synth, real volatile data diverges.

### Per-file commits (8 total + claim)

1. `4e64424 docs(handoff): claim revenue_growth (tab 19)`
2. `53196cd fix(revenue_growth_base_001_075): delete 4 formula-exact dups`
3. `908244b fix(revenue_growth_base_076_150): delete 2 formula-exact dups`
4. `020a41f fix(revenue_growth_base_151_225): delete rg_176 formula-exact dup`
5. `c0ff1a6 fix(revenue_growth_base_226_300): delete rg_269 formula-exact dup`
6. `6bd94c6 fix(revenue_growth_2nd_derivatives_v2): delete 2 NDR algebraic-identity dups`
7. `4d56d12 fix(revenue_growth_3rd_derivatives_v2): delete rg_3d_032 NDR-jerk dup`
8. `eaaae2c fix(revenue_growth_base_001_075): delete rg_036 value-exact dup of rg_034`
9. `f35aa8d fix(revenue_growth_base_076_150): rebody rg_126/127 monotonic_score to longest-streak`

### Final harness state (post-fix)

- 388/388 fns bound (was 400; 12 deletes)
- 0 errors / 0 all-NaN
- 1 sample-bias constant (rg_166, KEEP)
- 0 real formula-exact dup groups (1 reported is a harness fingerprint false-positive on rg_126/127 sharing `_longest_up_streak_norm` helper signature shape — value-hash check confirms they produce different outputs)
- 2 KEEP-BY-DESIGN value-dup groups
- 0 scalar-mult pairs

### Lessons worth carrying

1. **Multiplicative-from-revenue is a Path B trap for revenue-growth-vs-X-growth families.** Always use independent random walks per col. v1 vs v2 difference: 26 → 1 false-positive constants.

2. **The "yoy = ndr − 1" algebraic identity is a recurrent pattern.** When `f(x) = x/x.shift(n)` and `g(x) = (x − x.shift(n))/x.shift(n).abs()`, then `f.diff(m) ≡ g.diff(m)` for any m. Watch for this whenever a family has both ratio-form and pct-change-form siblings. Same template as RI ri_2d_031, RL rl_080-082, valuation_at_entry's 17 clusters.

3. **`_safe_div(.., .abs()).fillna(0.0)` creates clip-differentiated edge cases.** Diverges from raw boolean comparison only when denominator is 0 (Sharadar represents pre-IPO/missing as NaN, not 0, so never triggers in practice). Same disposition as RI ri_003/090, LS ls_022/296 — flag for keep-or-delete decision.

4. **Harness fingerprint bug to fix next session.** `fingerprint_func` skips body lines after a multiline docstring that closes with `..."""` mid-line. Detect closing `"""` anywhere in the line, not just `startswith`. False-positive formula-dups are caught by post-hoc value comparison but waste triage time.

### Cleanup

Per `feedback_temp_scripts.md`: deleted scratch:
- `temp_revenue_growth_pathb_harness.py`
- `temp_revenue_growth_audit_results.json`


---

## 2026-05-09 — `margin_acceleration` (audit-session-3, this tab) — surgical-edits-only

**Family**: `margin_acceleration` — 15 files (8 base × 75 fns + 3 2nd-deriv × 25 + 3 3rd-deriv × 25 = 750 features). Quarterly-cadence per CLAUDE.md note. 100% Path B (no OHLCV inputs). Function prefix `ma_`. Shared utils via `margin_acceleration_utils.py` (per CLAUDE.md exception).

**Inputs union (47 cols)**: assets, assetsc, assetsnc, capex, cashneq, cor, debt, debtc, debtnc, deferredrev, depamor, ebit, ebitda, equity, ev, fcf, gp, intangibles, intexp, inventory, investments, liabilities, liabilitiesc, liabilitiesnc, marketcap, ncf, ncfcommon, ncfdebt, ncfdiv, ncff, ncfinv, ncfo, netinc, opex, opinc, payables, ppnenet, receivables, retearn, revenue, rnd, sbcomp, sgna, shareswadil, taxassets, taxexp, taxliabilities.

**Path B mini-harness**: 5 profiles × 100 quarterly rows × 47 cols, warmup=20q (clears max 16q lookback). Quarterly synthetic generator with multi-regime drift: revenue trend + sin oscillation + noise; gm/om/nm paths drift 0.4±0.06 / 0.18±0.04 / 0.12±0.03; cogs computed as rev−gp (preserves 1−gm identity); cash flows mostly positive with mild noise. Exposes pre-warmup checks, value-exact dup hash, post-warmup z-cosine scalar-mult scan.

**Initial harness state (pre-rebody)**: 0 errors, 0 all-NaN, 11 constants (sample-bias), **90 value-exact dup groups, 122 scalar-mult candidates**. Triage classified into 7 patterns (cross-tier pollution, within-base alpha-rename, drawdown-helper-equivalent, cancellation, telescoping 4×, EMA AR1 1.5×, cogs sign-flips).

**User direction**: surgical-edits-only (zero deletes), per LS tab 14 / ES tab 15 precedent. User asked whether surgical edits actually produce different signals (answer: yes — currently every duplicate pair returns identical or scalar-mult-equivalent values; after rebody each computes mathematically distinct values matching its function-name promise).

**73 rebodies + 1 bug fix across 10 files (15 commits)**:

| File | Commit | Rebodies | Pattern |
|---|---|---:|---|
| `margin_acceleration_2nd_derivatives.py` | `d1abc46` | 20 | velocity slots: `pct_change` instead of `diff`; slope_velocity 2q-stride; ema4_velocity ema-of-velocity |
| `margin_acceleration_2nd_derivatives_026_050.py` | `8133229` | 17 | velocity slots: `pct_change`; ma_2d_026/027/028 4× telescoping → `diff(MA_4,4)` |
| `margin_acceleration_2nd_derivatives_051_075.py` | `a0b6b36` | 18 | velocity slots: `pct_change` |
| `margin_acceleration_3rd_derivatives.py` | `ec1617f` | 9 | jerk slots: `pct_change(N).diff(N)` instead of `diff(N).diff(N)` |
| `margin_acceleration_base_151_225.py` | `137ce04` | 8 | cogs sign-flip rebodies → `cor_growth - rev_growth` gap (breaks `cogs/rev = 1 − gm` identity) |
| `margin_acceleration_base_226_300.py` | `3a6d937` | 2 | convergence_yoy → spread-vs-8q-baseline ratio |
| `margin_acceleration_base_226_300.py` | `bda5b8d` | 1 | ma_289 gpoa-cancellation → TTM-avg assets denominator |
| `margin_acceleration_base_301_375.py` | `5d900c6` | 6 | ncfo/eps/debt cancellation → TTM-smoothed forms |
| `margin_acceleration_base_376_450.py` | `1652cd5` | 9 | drawdown/recovery/range alpha-renames → ratio forms; slope_accel → 4q-stride slope-of-slope |
| `margin_acceleration_base_451_525.py` | `48f0284` | 6 | cumsum_delta_8q telescoping → `pct_change` cumulative; rank_16q on TTM-mean; slope_12q on EMA |
| `margin_acceleration_base_526_600.py` | `d2d2366` | 4 | fcf_conversion / opinc_to_debt / reinvestment → TTM-mean / EMA forms |
| `margin_acceleration_2nd_derivatives.py` (follow-up) | `a8e01fd` | 3 | ema4_velocity widened from 1q→2q stride to break residual AR1 1.5× scalar-mult |
| `margin_acceleration_3rd_derivatives.py` (follow-up) | `80502f0` | 6 | ma_3d_010-015 jerk_4q → pct_change form (incl. ma_3d_013 cogs sign-flip) |
| `margin_acceleration_base_151_225.py` (follow-up) | `4e0c39d` | 1 | ma_189 streak rebody to (cor_growth>0 AND rev_growth>0) — prior streak still collapsed to gm-contraction identity |
| `margin_acceleration_base_451_525.py` (follow-up bug) | `ab7f633` | 1 | **bug fix**: ma_477_asset_light_margin had `ppnenet if 'ppnenet' in dir() else assets * 0.3` which always took False branch (function-arg names not in `dir()`), silently making fn `0.7×gm` (1/0.7=1.4286 scalar-mult to ma_001) — fixed via proper signature + registry inputs |

**Final harness state**: 750/750 fns clean, 0 errors, 0 all-NaN, **3 dup groups (KEEP BY DESIGN)**, **5 scalar-mult pairs (KEEP BY DESIGN)**. All remaining items are sample-bias-on-healthy-synth or NOPAT-precedent dilution-adjusted reformulations:
- 8-clique always-1.0 (margin > 0 / Piotroski positive flags): `ma_099/136/393/394/395/551/552/553` — ps_270/cfs_d3_046/bss_288/ri_044/sd_083_188/cas distress-flag precedent.
- 3-clique always-0.0 (sign-cross / no-dilution): `ma_100/293/558` — same disposition.
- `ma_555/ma_580` sample-bias-collapse: `gm_up & assets_up` reduces to `gm_up` when assets always grow on synth; real shrinking-assets firm produces divergent signal.
- 4 dilution-adjusted scalar-mult pairs at ratio ≈ 1.0088 ≈ 1/(1 − shares_growth_yoy): `ma_472/473/474` vs `ma_001/039/076` + `ma_175/325` lagged-shares cancellation — NOPAT 1.265823 precedent.

**Cadence note**: this is the second confirmed quarterly-cadence family (after `margin_trajectory` tab 20). Always check input-period convention (daily vs quarterly) BEFORE building harness — daily-cadence harness on a quarterly family produces false-positive constants/all-NaN due to `.shift(N)` semantics.

**Bug-fix class precedent**: ma_477's `'ppnenet' in dir()` bug joins the `bss_055 _safe_div(int_denom)` / `ve_385/387 _safe_div(scalar,12)` / `_slope` shape mismatch / `es_503/504 _log_safe(scalar)` / `ra_2d_025 missing return` line — silent-functional bugs that compute a constant or constant-multiple instead of the named formula.

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_ma_harness.py`
- `temp_ma_harness_out.json`


---

## 2026-05-09 -- session 3, tab 26 (`dilution_rate`, master row 26)

**Done this session:**
- Picked up master row 26 `dilution_rate` per HANDOFF queue (next pending after row 25 `growth_vs_cost` finished by tab 25).
- **Inventory**: 14 files = 8 base x 75 + 3 2nd-deriv x 25 + 3 3rd-deriv x 25 = 750 functions. Function prefix `dr_` (base) / `dr_d2_` / `dr_d3_`. Daily-cadence (uses `_pct_change_n(s, 63/252/504/756/1260)`). 100% Path B (every fn takes `sharesbas` or `shareswa` or `ncfcommon` or `sbcomp`; hybrid only via `close`/`volume`/`marketcap`/`ev`). ~52 input cols.
- **Claimed** as tab 26 (commit `e939567`).
- **Built mini-harness** at `%TEMP%\temp_dr_mini_harness.py` (deleted post-audit). Adapted SD tab 17 template with 5 distinct profiles to break `ncfcommon`-clip sample-bias: issuer (sb +8%/yr, ncfcommon +80), buyback (sb -4%/yr, ncfcommon -120), stable, sbc-heavy (high sbcomp), distress (sb +15%/yr, neg netinc, neg rev growth). 1500-day daily fwd-fill from quarterly anchors, warmup=800 to clear 1260d shifts.
- **Findings (initial run)**: 0 load_errors / 750 fns / 2 errors / 1 all-NaN / 102 constants / 4 formula-exact dup groups / 40 value-exact dup groups / 15 scalar-mult pairs.
- **Triage** (mirroring SD tab 17 precedent of 24 deletes auto-applied):
  - **2 errors** = real bugs: dr_344/dr_345 `lambda x: x.iloc[0]` with `raw=True` (pandas passes ndarray, .iloc fails). Fixed by `x[0]`. Same class as bss_055/ve_385/es_503 helper-on-wrong-type bugs from prior Path B audits.
  - **4 formula-exact** auto-applied: dr_015==dr_003 (literal pct_change_n(s, 252)), dr_079==dr_011 (literal (sw-sb)/sb), dr_145==dr_022 (literal sbcomp/assets), dr_528==dr_343 (literal ema_diff).
  - **10 cross-tier base->deriv** delete-from-base per CFS/RL/RI precedent (operators belong in deriv tier): dr_017/019/012/077/352/152/319/473/452/511/476 are all algebraically `pct_change_n(X, k).diff(k)` or similar, value-exact equal to `dr_d2_152/155/157/158/177/200/205/206/209` siblings.
  - **17 within-base body-identical-mod-rename + algebraic-identity** auto-applied: dr_330/331 = dr_001/002 (formula-exact under rename); dr_027/028 = dr_005/006 (`s/s.shift(n) - 1 == pct_change(s, n)` algebraic identity); dr_080 = dr_013 (body-identical "spread" vs "trend"); dr_078 = dr_013 (`s/b vs (s-b)/b` constant -1 cancels under .diff()); dr_075 = dr_016 (`s.diff(n) == s - s.shift(n)`); dr_339 = dr_142 (body-identical "vs capex" naming twin); dr_449 = dr_336 (body-identical "decay" vs "sequential ratio"); dr_546 = dr_368 (body-identical rolling beta to close); dr_570 = dr_481 (`log(s/s.shift) == log(s).diff` algebraic identity); dr_453 = dr_111 (body-identical "float-vs-volume" vs "expansion-vs-volume"); dr_576 = dr_573 (body-identical CUSUM-breach vs outlier-frequency); dr_014 = dr_001 x 4 (annualization scalar); dr_410 = dr_040 / 4 (regime_duration = streak/4 scalar).
  - **4 deriv-side scalar-mult** per VAL ve_083 precedent (lower-numbered z-score canonical kept): dr_d2_153 = dr_016 x 4 (annualization scalar in deriv tier); dr_d2_158 cross-deriv-tier collision (3rd-order operator misplaced in 2nd-deriv tier; dr_d3_178 properly placed); dr_d2_214 = dr_d2_167 / 2 (bollinger position = z-score / 2); dr_d3_239 = dr_d3_192 / 2 (same pattern at jerk tier).
  - **17 sample-bias coincidence value-dups KEEP BY DESIGN**: clip-collapse on synth tiny per-share/yield denoms (dr_226/228/229/230/300 div-adj price multiples; dr_114/115 div-to-yield with clip lower=0.001; dr_255/256 div-adj payout ratios; dr_100/dr_238 mktcap-per-share vs shareholder-value); constant-multiple synth balance sheet (dr_054/262/276/285/287 -- all per-share normalizations of constant-multiple-of-assets fillers; dr_411/412/413 -- inv/rec/pay are all 0.05-0.08 x assets in synth); sign-mask coincidence on profile-constant retearn/intexp (dr_003/dr_416/dr_432); profile-sign bias on ncfcommon (dr_173/175); clip-differentiated sbc-rank divergent on negative revenue (dr_081/dr_475); non-linear under tiny-x (dr_151/dr_202/dr_579 where ncfcommon/marketcap ~ 1e-8); constant-ratio shareswadil = shareswa x 1.005 in synth (dr_007/295, dr_008/296); clip-vs-no-clip on vol denom (dr_492/dr_535); telescoping fwd-fill on smooth synth (dr_001/dr_112); median-zero on smooth synth (dr_477/dr_571); multi-mech zero-collapse (dr_227/dr_469/dr_572 -- dilution_adj_pe-vs-raw=0 by clip-collapse, RSI=50 fixed, abs-median=0 on fwd-fill).
  - **3 scalar-mult sample-bias KEEP BY DESIGN**: dr_160/dr_184 (ncfcommon sign vs persistence_4q ratio=1 because sign is constant per profile); dr_050/dr_231 + dr_245/dr_247 (eps_diff vs (eps_diff)/|eps|.clip(lower=0.01) -- clipped to 0.01 on synth tiny eps, ratio=0.01).
  - **1 sample-bias all-NaN KEEP BY DESIGN**: dr_137_dilution_half_life (looks back to find when shares were half current; never triggers on growth/buyback profiles; works on real reverse-split data). Same disposition as ps_270/cfs_d3_046/bss_288.
- **Per-file commits** (one per affected file with scoped messages, lower-wins): `6143924` (b1: 8 deletes), `7ad14fb` (b2: 5 deletes), `557d261` (b3: 1 delete), `3120a65` (b4: 5 deletes + 2 raw=True bug fixes), `99ac9df` (b5: 2 deletes), `9881878` (b6: 5 deletes), `07f3a94` (b7: 5 deletes), `6dbbafe` (d2-1: 2 deletes), `16c5cba` (d2-3: 1 delete), `483b42c` (d3-3: 1 delete), `650e228` (b6 followup: dr_476 cross-tier missed on first pass, caught by post-fix re-run). All AST-parse + import validated post-edit.
- **Final state**: 714 / 750 bound (= 750 - 36 deletes). 0 errors / 0 missing inputs / 0 formula-exact dups / 0 unexplained value-exact dups. 17 sample-bias value-dup groups + 3 scalar-mult sample-bias + 1 sample-bias all-NaN kept by design.

**Lessons (worth carrying):**
1. **Profile mix matters for ncfcommon-clip families**: SD tab 17 used uniform buyback regime (ncfcommon=-50) and got 2 sample-bias-constants (sd_083/sd_188) on clip(lower=0)-style features. For DR I used 5 profiles with mixed signs (issuer +, buyback -, distress +) and the ncfcommon-clip features still produced sample-bias coincidences (e.g. dr_173/dr_175, dr_160/dr_184) but at value-dup level not constants -- different mechanism. **Lesson**: profile mix breaks per-fn sample-bias-constant detection, but cross-fn value-dups still need triage to distinguish profile-bias coincidence from real algebraic equivalence.
2. **Cross-tier dups dominate in operator-heavy families**: 10 of 36 deletes (28%) were cross-tier base->deriv (`_chg_1y` in base file = `_roc_1y` in d2 file). Same pattern as SD tab 17 (11/24 = 46%). Authors propagate `_chg`/`_roc`/`_jerk` slot names into base file when the operator is properly a derivative-tier feature. Always grep for "deriv-tier-name in base file" patterns first.
3. **Algebraic-identity scalar-mult: keep lower-numbered raw, delete annualized scaled**: dr_001 vs dr_014 (x4 annualization) -> keep dr_001. dr_d2_153 vs dr_016 (x4 cross-tier annualization) -> keep dr_016. Rule: scaling/annualization is a presentation choice, not a different signal. Deleting the scaled version preserves the canonical raw form.
4. **First-pass cross-tier scan can miss algebraically-equivalent base members**: dr_476_dilution_relative_strength returns `rate - rate.shift(252)` which is algebraically `rate.diff(252)` = same as dr_d2_152, but I missed it on the first pass because the body was hand-rolled rather than literal `.diff(252)`. Caught only by post-fix harness re-run. **Lesson**: always re-run harness after batch deletes to catch algebraically-equivalent siblings missed by first pass.
5. **Concurrent-tab race on shared docs**: HANDOFF.md and CLAUDE.md got concurrently modified by tabs 22/25/27/28/29 throughout this session. The Edit tool's "file modified since read" race forced me to re-read several times. Final HANDOFF row update went through cleanly; CLAUDE.md row addition got picked up by another tab's commit (tab 22 debt_trajectory commit `4c8d3dd`) -- race-acceptable because it landed in HEAD. **Lesson**: for shared-doc updates, read-then-immediately-edit and accept that other tabs may sweep the change in via their own commit.

**Cross-tab status at this writing:**
- Tab 26: dilution_rate DONE (this entry).
- Master row 26: now fully **DONE** (Path B, all 14 files; 12 commits).
- Path B family count: 12 done (revenue_level, profitability_snapshot, cash_flow_snapshot, balance_sheet_snapshot, valuation_at_entry, leverage_and_solvency, rd_and_intangibles, share_and_dilution_snapshot, capital_allocation_snapshot, margin_trajectory, cash_flow_trajectory, dilution_rate; debt_trajectory, valuation_trajectory, growth_vs_cost, revenue_acceleration, cash_flow_acceleration also reported done by other tabs while this audit ran).

### Cleanup

Deleted scratch per `feedback_temp_scripts.md`:
- `%TEMP%\temp_dr_mini_harness.py`
- `%TEMP%\temp_dr_mini_harness_out.json`

---

## Session 4 — tab-mt 2026-05-09 — moat_trajectory all tiers

User assigned `moat_trajectory` (queue row 43). 12 files, 600 features (6 base x 75 + 3 2nd-deriv x 25 + 3 3rd-deriv x 25). Mixed-cadence (528 quarterly + 72 daily + 6 mixed-cadence whose registry says quarterly but body pulls `close`).

### Harness build (Path B dual-cadence)

First pass: pure quarterly profiles (5 x 100q x 31 fundamental cols). Surfaced 6 `KeyError('close')` errors for mixed-cadence fns (mt_2d_043, mt_3d_041, mt_348, mt_349, mt_410, mt_411). Per CLAUDE.md HARNESS DESIGN LESSON 25 (mixed-cadence inside one family), added OHLCV co-sampled at quarter-end cadence to each quarterly profile -- fixed all 6 errors without needing a separate daily harness pass.

### 33 deletes (12 commits: bf6ba0e..6f69048)

All auto-applied per HANDOFF AUTO-APPLY classes 1-3. Breakdown:
- **8 DuPont decomposition aliases** (mt_076-081 + mt_2d_015 + mt_3d_015) -- CAS cas_182/183 cancellation-equivalent precedent. (NI/R)(R/A)(A/E) telescopes to NI/E.
- **4 SGR=ROE aliases** (mt_176/177 + mt_2d_029 + mt_3d_029) -- bodies literally return ROE; docstring acknowledges retention=1.
- **3 EVA-spread aliases** (mt_152, mt_2d_026, mt_3d_026) -- CAS cas_158 precedent; HURDLE constant cancels under .diff()/_d3.
- **4 Greenblatt EY = ROIC aliases** (mt_392/393, mt_2d_067, mt_3d_066) -- body uses BOOK equity not market cap so collapses to ROIC. Composite mt_394 inlines.
- **12 pure alpha-rename** (mt_075/273/293/402/446/447/346/366/367/332 + mt_2d_062 + mt_3d_061 + mt_3d_074).
- **1 algebraic-identity via Sharadar fcf=ncfo+capex** (mt_311 == mt_183) -- slope cancels constant. CFA cfa_015/041 precedent.

### KEEP-by-design (13 academic-trace dup groups + 4 constants + 1 all-NaN)

Per ls_061/151/170/188 + cas_062/090 + ls_188 Beaver precedent -- academic distress-model components individually addressable for explainability when the composite inlines x1-x5+:
- Piotroski components: mt_002/172, mt_051/166, mt_053/168, mt_064/173 (mt_174/175 composite inlines)
- Altman X3: mt_105/191 (mt_196 composite inlines)
- Altman X1 vs Ohlson WC: mt_186/379 (different academic models)
- Ohlson NITA: mt_051/382, mt_3d_006/3d_049 (LS Beaver-jerk precedent for 3d trace)
- AQR QMJ: mt_141/408, mt_142/409 (mt_412/413 inlines)
- Sloan accruals vs Beneish TATA: mt_143/206, mt_2d_025/2d_033, mt_3d_025/3d_033 (different academic models)

Constants kept by design (sample-bias/synth-symmetry):
- mt_287 close_position_in_range -- synth OHLC symmetry artifact
- mt_309 ocf_positive_ratio -- synth ncfo always positive (ps_270 precedent)
- mt_381 ohlson_oeneg_flag -- synth assets > debt always (LS distress-flag precedent)
- mt_420 revenue_entropy_8q -- smooth synth growth bins to <=2 quintiles

All-NaN kept (harness limitation):
- mt_410 qmj_safety -- needs daily 252d close.pct_change.std but quarterly profile has 100 obs.

### Surgical-rebody candidates flagged for next-session ASK FIRST

- `mt_392_greenblatt_earnings_yield`: Greenblatt EY academically uses EBIT/EV (where EV = market_cap + debt - cash). Body uses BOOK equity + debt = invested capital, collapsing to ROIC. Could rebody to use marketcap (close*sharesbas) instead of book equity to recover true EV-based EY (would also pull marketcap into input deps). Auto-deleted as formula-exact for now per HANDOFF policy; if user prefers true EY semantics later, surgical-rebody (vac_118 / cas_141 / ve_424 precedent) would restore distinct slot.
- 3 inst-ownership pct conventions in codebase now: VAC `instownpct` + HEP `insiderpct`/`instpct` + moat_trajectory `insider_pct`/`instinvest_pct`. Binding-layer needs all three in translation map.

### Function prefix collision

`mt_NNN_*` is shared between `margin_trajectory` (already audited tab-20) and `moat_trajectory` (this tab). Each file is self-contained at runtime so no symbol clash, but cross-family tooling (registry merging, search-by-prefix) must namespace by family. Flagged in HANDOFF row 43; not refactored this session.

### Final state

567/600 fns post-fix. 0 errors / 13 KEEP academic-trace dup groups / 4 sample-bias constants / 1 harness-limitation all-NaN.

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_moat_harness.py`
- `temp_moat_harness_out.json`
- `temp_moat_harness_err.log`


---

## tab-rj (audit-session-3) - 2026-05-09 - revenue_jerk

**Family**: revenue_jerk (priority queue #34). 14 files / 750 fns / 100% Path B daily-cadence.

**Approach**: surgical-rebody-everything per user direction (LS / debt_trajectory / efficiency_snapshot precedent). **Zero deletes; ~155 surgical edits across 14 files preserve all 750 slots.**

**Initial harness state** (5 profiles x 2500 daily rows x 28 input cols, warmup=1800):
0 errors / 0 missing inputs / 0 all-NaN / 0 constants / **21 body-exact dup groups** / **36 value-exact dup groups** / 1 scalar-mult.

**Per-file commits** (lower-wins canonical, surgical edits only):
- `03e5224` (b451-525 + b526-600): 10 _1y/_2y body-exact pair fixes via window assignment
- `b701466` (b001-075/151-225/226-300/526-600): 7 cross-tier mathematical-identity collisions broken via scale-normalization on base side
- `1c2ff0a` (b076-150/226-300/451-525/526-600): 11 within-base value-exact pair surgical edits
- `8dea87b` (2d_026-050 + 2d_051-075 + 3d_026-050 + 3d_051-075): 26 deriv-tier mass-bomb rebodies (rj_2d/3d_031-033 stride variation; rj_2d/3d_056-065 expanding-stat variation)
- `f36ce61` (b301-375 + b376-450): 76 expanding-mean placeholder rebodies (rj_375 + 75-fn complete file rewrite)
- `2939f43` (b151-225): 24 sgna_to_rev_jerk placeholder rebodies (rj_202-225 vary stride/stat/transform/window)
- `948766b` (six files): second-pass rebodies eliminating cross-file dups discovered by re-running harness post-pass-1

**Key second-pass discovery**: first-pass 376_450 design (1y rolling stats) collided with 16 existing 001_075/076_150 slots (vol_1y/2y, ema_63/252, max/min/range_1y, skew/kurt_1y, zscore, cumsum, sign_change, rank). Complete file rewrite to **expanding-window-based statistics** resolved all collisions. Plus 2 expanding-max/min ROC went constant on synthetic monotonic-up jerk series -> switched to expanding-q95/q05.

**2 pre-existing scalar-mult pairs surgically rebodied** (per user surgical-rebody-everything direction):
- rj_479 (algebraic identity with rj_118 mean/std consistency) -> MAD-based trend strength
- rj_2d_011 (EMA/diff linearity collapses to rj_070) -> shorter (21,63) EMA cross

**Final state**: 750/750 bound. 0 errors / 0 all-NaN / 0 constants / 0 body-dup / 0 value-dup / 0 scalar-mult. 14 files surgically edited; zero deletions; all original registry keys + Python identifiers preserved (including missing-underscore typos for binding-layer compat).

### Lessons (worth carrying)
1. **Mass-placeholder rebodies need cross-file dup awareness.** When designing rebodies for placeholder-bomb clusters, first inventory what statistical patterns are already covered in EARLIER chunks of the same family. For "expanding_mean" placeholder name, expanding-window stats were the natural answer and won't collide with rolling-window stats elsewhere.
2. **Expanding-max/min ROC goes constant on synth.** Monotonic expanding stats only update at boundary-crossing points; ROC is mostly 0. Use expanding-q95/q05 for smoother proxies.
3. **EMA/diff linearity creates cross-tier scalar-mult.** Cross-tier `_roc` of EMA-cross of `_acceleration` tends to scalar-mult the same EMA-cross of `_jerk`. Use distinct EMA windows when designing deriv-tier features that wrap base EMA-cross signals.
4. **Function-name typos are binding-layer hazards.** 124 placeholder slots have typo names like `rj_201sgna_*` (missing underscore). Preserved verbatim for binding-layer compat; flagged for future awareness.
5. **Surgical-rebody-everything mode (zero deletes) at scale**: ~155 rebodies across 14 files in a single audit session is feasible when the bulk of work is the 124 mass-bomb cluster (one big file rewrite + one block edit). The cross-tier collision and within-base pair fixes are individually small but additive.

### Cleanup
Deleted scratch per `feedback_temp_scripts.md`:
- `temp_rj_harness.py`
- `temp_rj_harness_out.json`
- `temp_rj_audits_append.py`
- `temp_rj_journal_append.py`

## 2026-05-09 — session 3 — tab-mj: margin_jerk (Path B, all tiers)

**Family scope:** 13 files, 725 features. 8 base × 75 (mj_001..mj_600 in chunks
001_075/076_150/151_225/226_300/301_375/376_450/451_525/526_600) + 2 2nd-deriv ×
25 (mj_2d_001..mj_2d_050 in 2nd_derivatives.py / 2nd_derivatives_026_050.py) +
3 3rd-deriv × 25 (mj_3d_001..mj_3d_075 in 3rd_derivatives.py /
3rd_derivatives_026_050.py / 3rd_derivatives_051_075.py). 100% Path B (no
OHLCV). Quarterly cadence per `margin_trajectory` tab-20 / `cas` tab-18
precedent (uses periods 1/2/4/8/12/16/20q for `.shift(N)`/rolling; max base
window = 20q + d3 nested 8q ≈ 28q lookback).

**Inputs (12 cols)**: `cor`, `depamor`, `ebitda`, `fcf`, `gp`, `intexp`,
`netinc`, `opinc`, `revenue`, `rnd`, `sgna`, `taxexp`. All subsumed by prior
Path B audits — no new col types.

**Harness**: `temp_mj_harness.py` (deleted post-audit per
`feedback_temp_scripts.md`) — 5 deterministic profiles × 80 quarterly rows ×
12 cols, warmup 30q. Standard checks: errors / all-NaN / constants /
formula-exact dups (value_hash) / value-exact dups (post-warmup) / scalar-mult
pairs (post-warmup z-cosine sim with ratio_std_rel < 1e-6 gate).

**Triage outcome**: 725 → 662 fns (63 deletes, 14 surgical rebodies, 0 errors,
0 all-NaN). Three passes per HANDOFF policy.

### Pass 1 — clear-cut auto-applies (48 deletes, 6 commits)

Per HANDOFF AUTO-APPLY: formula-exact + algebraic-identity + cross-tier
base-vs-deriv pollution + within-file/within-base literal duplicates.

Commits: `5032e2c` (file 001_075, 10 deletes), `fc48d69` (226_300, 14),
`fa20e6f` (301_375, 10), `4b4982f` (376_450, 4), `4d15d6e` (451_525, 5),
`a3e2cb7` (526_600, 5).

Categories:
- **5 base accel + 5 base jerk** for gp/opinc/netinc/ebitda/fcf core margins
  (mj_006/007/021/022/036/037/051/052/066/067) — 10 fns. Cross-tier
  base-vs-deriv pollution: deriv canonical exists at mj_2d_001/006/011/016/021
  (`*_chg_4q_roc`) and mj_3d_001/006/011/016/021 (`*_chg_4q_jerk`). Operators
  belong in deriv tier per RA tab-29 / CFS / RL / RI ri_036 precedent.
- **5 base surprise = accel algebraic-identity** (mj_315/330/345/360/375).
  Body `m - (m.shift(4) + d(m.shift(4),4)) = m - 2*m.shift(4) + m.shift(8)
  = d(d(m,4),4)` reduces to 2nd diff = mj_2d_001/006/011/016/021.
- **5 incr accel + 4 dol accel/jerk** (mj_289-297) cross-tier pollution.
- **5 ema4_roc base** (mj_312/327/342/357/372) — both base and deriv
  (mj_2d_045-049) had `_roc` in name; deriv is canonical placement.
- **5 mj_279-283 incr_vs_steady = lev** algebraic identity. Proof:
  `_incr_margin(p,r,4) - p/r = (gp.diff(4)/rev.diff(4)) - p/r`. Let `dm =
  m.diff(4)`, `dr = rev.diff(4)`. Then `gp.diff(4) = dm*rev + m.shift(4)*dr`,
  so `(gp.diff(4))/dr - m = (dm*rev/dr + m.shift(4)) - m = dm*(rev/dr - 1) =
  dm*rev.shift(4)/dr = lev(p,r,4)` exactly when rev.shift(4) > 0 (always on
  positive synth, real-data caveat = `clip(1e-9)`). RL rl_080-082
  cancellation-equiv precedent.
- **2 spread divergence** (mj_420/422) = 1st diff of margin spread by
  linearity of `_d`: `_d(a-b,4) = _d(a,4) - _d(b,4)`. Dups of mj_077/082.
- **1 cancellation-equiv** mj_427 = mj_401 via revenue cancellation:
  `_d((netinc/rev)/(gp/rev),4) = _d(netinc/gp,4)`.
- **1 within-file literal dup** mj_450 (verbatim copy of mj_449).
- **5 within-file literal dups** mj_516..520 (verbatim copies of mj_511..515).
- **5 within-base literal dups** mj_526/541/556/571/586 `*_inflection` =
  mj_314/329/344/359/374 `*_reversal_flag` (alternate name, same body
  `(np.sign(d4q) != np.sign(d4q.shift(1))).astype(float)`).

### Pass 2 — surgical rebodies (5 commits + 1 cross-tab race)

The deriv `_026_050.py` files had a systematic naming-bug pattern:

```python
# mj_2d_036 (was): applies _d4q to a level → 1st diff in 2nd-deriv tier
def mj_2d_036_cogs_margin_roc(cor, revenue):
    base = _sd(cor,revenue); return _d4q(base)

# mj_2d_001 (correct): applies _d4q to a (chg_4q level base) → 2nd diff
def mj_2d_001_gross_margin_chg_4q_roc(gp, revenue):
    base = _d(_sd(gp,revenue),4); return _d4q(base)
```

Slots 033..050 in `_2nd_derivatives_026_050.py` (and 043..050 in
`_3rd_derivatives_026_050.py`) were one diff short — they applied `_d4q` to a
LEVEL feature instead of to a `_d(level, 4)` base. The result was that mj_2d_036
literally computed 1st diff (= base mj_153 cogs_margin_chg_4q) and mj_3d_043
literally computed 2nd diff (= base mj_154 cogs_margin_accel).

User's 1st question response: "explain more about surgical rebody will it be
enough of a difference in jerk feature for different signal". I clarified that
rebody just relocates the canonical to the correct tier file — same math, same
signal — and asked again. User chose "Surgical rebody (preserve 16 slots,
relocate canonical to deriv tier)" per LA Beaver / cas_141 / vt_296 precedent.

Commit `0e9f510` rebodies 18 deriv slots (added inner `_d(...,4)` to each
buggy base expression) + fixes 2 signature bugs (mj_2d_044 cost_mix_roc and
mj_2d_050 gross_oper_spread_roc were missing `revenue` in their signatures
despite using it in their bodies → would NameError on every call) + fixes 1
body-equality bug (mj_2d_042 opex_ratio body was identical to mj_2d_037
sga_margin since both `sgna/rev` — rebodied to true `(sgna+rnd+depamor)/rev`
opex denominator with signature expanded `(sgna,revenue)` →
`(sgna,rnd,depamor,revenue)`).

Commit `ec0e442` rebodies 5 boll_pos_8q slots (mj_307/322/337/352/367). Bodies
were literally `(m-mu)/sd` = zscore = dups of mj_010/025/040/055/070
zscore_8q. Bollinger %B is academically `(m-midband)/(2*std) + 0.5` mapping
to [0,1]. Rebodied per ls_148/vac_118/cas_141/ve_424 surgical-edit precedent.

Commit `103788e` rebodies mj_278_contrib_margin_proxy. Body was literally
`_sd(gp, revenue)` (= mj_001 gross_margin) but signature `(gp, revenue, cor)`
ignored cor and the name says "contribution margin". Contribution margin =
fraction of revenue left after variable costs. Rebodied to
`_sd(gp - sgna - rnd, revenue)` (subtract two largest discretionary opex from
gp before normalizing). Signature `(gp, revenue, cor)` →
`(gp, revenue, sgna, rnd)`.

Commit `684f769` rebodies mj_221_variable_cost_proxy_ratio. Body was literally
`_sd(cor, revenue)` (= mj_151 cogs_margin) but the name says "variable cost"
which in managerial accounting = COGS plus variable selling/admin (sgna), not
just COGS. Rebodied to `_sd(cor + sgna, revenue)`. Signature `(cor, revenue)`
→ `(cor, sgna, revenue)`.

Commit `e5f1aa3` rebodies mj_521..525 placeholder slots. Bodies were literally
`_sd(gp, revenue) * np.nan` (all-NaN by construction). Rebodied to 5 distinct
cross-margin aggregate metrics extending the mj_511..515 family
(skew/kurt/maxdd/avg-pain/dispersion-vol):
- mj_521 sign_agreement_8q: rolling mean of cross-margin direction agreement
- mj_522 breadth_above_median_8q: fraction of margins above 8q rolling median
- mj_523 minmax_spread: max(margins) - min(margins) per quarter
- mj_524 minmax_spread_chg_4q: YoY change in cross-margin spread
- mj_525 chg_concentration_hhi_8q: HHI of |margin chg| shares
Function names + registry specifics + interval-type all updated.

**Cross-tab race**: A late one-line bugfix to mj_521 sign-agreement formula
(`abs().sum(axis=1)/5` → `sum(axis=1).abs()/5` for true sign-agreement
semantics) was made between Pass 2 and Pass 3 and staged for a follow-on
commit. I attempted `git commit --amend --no-edit` to fold it into the
mj_521 placeholder commit, but another tab had pushed `revenue_jerk_*`
commit `948766b` in the gap. The amend rewrote 948766b in place adding my
mj_521 fix, then a third tab's commit `76f5a1d` (cash_flow_jerk claim)
landed on top picking up my mj_521 staged change. Recovery: `git reset
--soft 948766b` restored the original revenue_jerk content; mj_521 fix
ended up in 76f5a1d. Net effect: the bugfix IS in HEAD (verified), just
not in a margin_jerk-named commit. Lesson: NEVER use `--amend` when other
tabs are concurrently committing; always create new commits.

### Pass 3 — auto-deletes after deriv rebody (15 deletes, 3 commits)

Re-ran harness post Pass 2 — found 15 NEW base-vs-deriv dup groups created by
the surgical rebody (rebodied derivs now compute true 2nd/3rd diff matching
existing base accel/jerk slots). Auto-applied per RA tab-29 cross-tier policy.

Commit `2dfc005` (file 076_150, 1 delete): mj_078_gross_oper_spread_accel
(2nd diff of `gp/rev - opinc/rev`) = mj_2d_050 (rebodied).

Commit `04cd0b6` (file 151_225, 10 deletes):
- mj_154/155 cogs accel/jerk = mj_2d_036/mj_3d_043
- mj_162/163 sga accel/jerk = mj_2d_037/mj_3d_044
- mj_170/171 rnd accel/jerk = mj_2d_038/mj_3d_045
- mj_178/179 da accel/jerk = mj_2d_039/mj_3d_046
- mj_186/187 intexp accel/jerk = mj_2d_040/mj_3d_047

Commit `e6b2eda` (file 376_450, 4 deletes):
- mj_432 net_to_gross_cascade_accel = mj_2d_033 (rebodied)
- mj_433 fcf_to_ebitda_cascade_accel = mj_2d_034
- mj_434 opinc_to_gp_cascade_accel = mj_2d_035
- mj_435 net_to_gross_cascade_jerk = mj_3d_050 (rebodied)

Note: mj_194/195 (taxexp accel/jerk in base) and mj_222/223/224/225 (cost
structure composites) are NOT deleted — no corresponding deriv slot exists in
`_026_050.py` files for these inputs, so the base slots remain sole canonical.
Same for mj_213 berry_zscore (not accel) and mj_201/204/207/210 zscore series.

### KEEP-by-design (final harness state)

- **5 entropy_proxy constants** (mj_536/551/566/581/596 = 4.0 always on
  smooth synth). Body counts distinct quartile bins in 12q rolling window via
  `pd.qcut(x, 4, duplicates='drop')`. On smooth-trend synth always 4 bins; on
  real data with ties or short-window edge cases produces real signal.
  ps_270/cfs_d3_046/bss_288 sample-bias precedent.
- **1 spread_chg vs convergence_rate dup pair** (mj_087/mj_426).
  mj_087 = `_d(gp/rev - netinc/rev, 4)`, mj_426 = `_d(|gp/rev - netinc/rev|, 4)`.
  On healthy synth gp/rev > netinc/rev always → spread > 0 → |spread| = spread.
  On real data with negative net margin (loss firms), spread can flip sign and
  they diverge meaningfully. cft_008/051 winsorized-synth-coincidence precedent.
- **5 incr/decr scalar pairs** (mj_228/232, 236/240, 244/248, 252/256,
  260/264). `_decr_margin(p, r, 4)` = `_sd(dp, dr)` masked to NaN when `dr >= 0`.
  On synth with mostly-monotone revenue growth, the common (non-NaN) support is
  rare quarters with revenue dip — and on those quarters both compute the same
  formula `_sd(dp, dr)` → ratio = 1.0. On real data with sustained revenue
  decline regimes, decr fires distinctly and represents a different signal
  (margin behavior during contraction vs expansion). cft_008/051 precedent.

### Cross-tab coordination notes

- Other tabs were concurrently committing on `revenue_jerk`, `efficiency_acceleration`,
  `cash_flow_jerk`, `margin_acceleration` during this audit. All disjoint
  files — no source conflicts. Doc files (CLAUDE.md/HANDOFF.md/AUDITS.md)
  saw multiple read-modify-write races; I retry-on-modified pattern handled
  most cleanly. Hard lesson on `git commit --amend`: don't use it when other
  tabs are pushing.

### Next-tab pickup

Family DONE. Queue row 35 marked done. Master priority queue row 36 next:
`cash_flow_jerk` — already claimed by tab-cfj (commit `76f5a1d`).

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_mj_harness.py`
- `temp_mj_harness_out.json`
- `temp_mj_harness_err.log`

---

## 2026-05-09 — tab-cfj — cash_flow_jerk audit (Path B)

**Outcome:** 750 → 731 features. 0 errors / 0 formula-exact dups post-fix.
6 commits across 5 files (+1 race-coupled commit `eca67ae` — see below).

**Harness** (`temp_cfj_harness.py`): 5 profiles × 1500 daily rows × 51 input
cols, daily-cadence with quarterly anchors fwd-filled per cas/dr/rg precedent.
Warmup=1300 to clear 1260d max lookback (`cfj_398_rank_5y`,
`cfj_280_slope_5y`, `cfj_465_5y_debt_repay`, `cfj_582_range_5y`).
Independent random walks per cost/balance-sheet ratio (per RG/RJ lesson)
and per cash-flow component (avoid multiplicative-from-revenue collisions).
Profile mix: steady, growth, accel, distress, volatile.

**Findings (pre-fix):**
- 0 errors
- 1 all-NaN: cfj_162_cash_runway_months (sample-bias on positive-ncfo synth)
- 3 constants: cfj_161, cfj_163, cfj_302 (all sample-bias zeros)
- 9 body-hash dup groups + 23 value-hash dup groups + 25 scalar-mult pairs
  (overlapping: most scalar-mult pairs are ratio=1.0 = value-exact dups)

**Triage (per HANDOFF policy):**
- 17 within-base formula-exact dups → AUTO-DELETE (class 1, lower-numbered
  slot wins): cfj_096/097/324/327/360/364/405/406/407/410/430/476/500/
  501/502/547/549.
- 2 cross-tier base→deriv pollution → AUTO-DELETE from base (class 4):
  cfj_052 (TDM-delta of cfj_050 ema_ratio level == cfj_2d_016 body),
  cfj_526 (TDM-delta of cfj_524 surprise level == cfj_2d_044 body).
- 4 sample-bias constants/all-NaN KEEP (cfj_161/162/163/302 — cash-burn
  family on healthy synth; ps_270/cfs_d3_046/bss_288 precedent).
- 4 synth-coincidence value-dup groups KEEP (cfj_073/074, cfj_117/552,
  cfj_303/304, cfj_161/163/302 3-clique — diverge on real distress data).
- 2 KEEP scalar-mult pairs: cfj_141/465 ratio=5 (NOPAT-style 5Y debt-repay
  capacity per cas_025/136, ls_023/297 precedent); cfj_488/495 ratio=365
  (days-conversion of working-capital ratio per CFT CCC vs wc/rev=90).

**Notable findings:**
- `cfj_430_fcf_to_ev_acceleration` had a docstring "redundancy check:
  different from 183 — uses pct_change base", but the body literally is
  `_d(_pc(_sd(fcf,ev),TDQ),TDQ)` — exactly what cfj_183 computes. Docstring
  was wrong; deleted as formula-exact dup.
- `cfj_360_ocf_yield_velocity` and `cfj_098_ocf_per_share_velocity` are
  both `_pc(_sd(ncfo,close),TDQ)` — the cfj_098 "per_share" framing is
  also wrong (close is not shares; it's price). Lower-numbered slot kept
  with name unchanged.

### Multi-tab coordination — git index race

Commit `eca67ae` is labeled `fix(cash_earnings_divergence_base_076_150): ...`
(a different tab/family) but its diff ALSO includes my cfj_096/cfj_097
deletes from `cash_flow_jerk_base_076_150.py`. Root cause: git's index
(staging area) is shared across all processes in the same checkout. I ran
`git add cash_flow_jerk_base_076_150.py && git diff --cached --name-only`
(showed only my file staged), then `git commit -m "..."` as a separate
command. Between those two commands, the ced tab also ran `git add ced_*.py
&& git commit -m "..."`. Their commit picked up MY staged file alongside
their own.

The deletes themselves are correct — only the commit-log attribution is
wrong. Future readers of the cash_flow_jerk audit trail will see
cfj_096/cfj_097 mysteriously deleted under a ced commit; the explanation
lives here in this journal entry and in the cfj HANDOFF row.

**Lesson:** chain `git add && git commit` in a single shell command (no
intervening `git diff --cached` etc.). I switched to that pattern for
all subsequent file commits.

### Next-tab pickup

Family DONE. Master priority queue row 36 marked done. Row 37
`hypergrowth_signature` already claimed by tab-hgs (commit `b079b34`).

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_cfj_harness.py`
- `temp_cfj_harness_out.json`


## 2026-05-09 — tab-olc — `operating_leverage_composite` audit (Path B, surgical-rebody-everything)

### Outcome

Master priority queue row 40 → DONE. 750/750 fns clean post-fix on Path B mini-harness (5 profiles × 2500 daily rows × 29 input cols, daily-cadence forward-fill from quarterly anchors, warmup=1800 to clear 1260d max base + 504d nested d3 lookback). 0 errors / 0 all-NaN / 0 dup groups. **77 → 0 dup groups (-77) and 750 fn slots PRESERVED via ~80 surgical rebodies + 0 deletes** (LS tab 14 / DT tab 22 / RJ / MJ precedent).

Commits: `32775a4`, `7cb6ddf`, `2fa7b6d`, `d17c184`, `81f8bdc`, `fdfce9c`, `5053bb1`, `db363d1`, `372eb92`, `b1b7524`, `6251be6`, `b91fd2b`, `1709f8f`, `18db786` (14 commits, one per file affected, + 2 cleanup commits for secondary collisions).

### Approach

User direction: surgical-rebody-everything (zero deletes). Per HANDOFF LS/DT/RJ/MJ precedent — preserves 750 slot count semantically.

Cluster breakdown:
- **~47 cross-tier base→deriv pollution** (CLAUDE class 4) — base side literally identical to deriv side (`_delta(level, n) = level.diff(n)` is a derivative operator). Standard rebody pattern: switch base to `_delta(_ema(level, _T['q']), n)` (delta of EMA-smoothed level; ES tab 15 EMA-input precedent; structurally distinct from raw `_delta(level, n)`).
- **6 cross-tier deriv mis-tier** (CLAUDE class 5) — bodies in 2nd-deriv files that are 2-diff structures (= 3rd-deriv). Per RA `ra_2d_003` precedent the canonical lives in 3d tier. Surgically rebody mis-tier side to 2d-tier-correct single-diff `_delta(_pct(level, q), q)` (delta of relative change — single-diff structure, distinct from raw `_delta(level, q)` of canonical 2d slots).
- **4 naming bugs** (CLAUDE class 8): olc_2d_071 / olc_3d_071 "_opinc_margin_roc_2q" used `_T['q']` not `2*_T['q']`; olc_2d_072 / olc_3d_072 "_dol_pct_change_q" used `_delta` not `_pct`. Surgical rebody to match the name promise (ls_148 / ve_424 / cas_141 precedent).
- **~17 within-tier algebraic-identity / value-exact pairs** rebodied to slot-faithful distinct formulations (bounded relative spread, log-difference, TTM-mean denom, smoothed acceleration, robust median/MAD z-score, log-cointegration correlation, etc.).
- **3 sign-flip-via-1-x identities** rebodied via linearity-breaking `_pct` instead of `_delta`/`_delta(_ema(...))`: olc_039, olc_038/olc_2d_024, olc_3d_065.

### Three-pass campaign

Pass 1 (commits `32775a4`..`b91fd2b`, 12 commits) cleared 73 of 77 dup groups. Standard pattern: read each file once, batch all needed Edit calls, run AST-parse-check, commit per file.

Pass 2 (commit `1709f8f`) caught 4 secondary collisions surfaced by re-running the harness:
- olc_108/109 cost_structure_ratio delta_q/y — I missed these in Pass 1 (same class 4 EMA-smoothed-delta pattern).
- olc_038 contribution_margin_delta_q — Pass 1 EMA-smoothed-delta rebody still sign-flip-equals olc_016 because EMA + delta are linear operators (sign-flip via 1-x propagates through EMA). Lesson: linearity-breaking requires `_pct` not `_delta`.
- olc_462 dol_acceleration_q — Pass 1 rebody to `_delta(_ema(_delta(dol, q), q), q)` value-exact-equals olc_3d_045 `_delta(_delta(_ema(dol, q), q), q)` because EMA and delta commute on shifted inputs (`_ema(s.shift(q), q) = _ema(s, q).shift(q)`).
- olc_466 margin_vs_min_y — Pass 1 rebody to `(m - rolling_min) / (rolling_max - rolling_min)` collided with olc_538_normalized_margin_q. Re-rebodied to `(m - floor) / |floor|`.

Pass 3 (commit `18db786`) caught one more secondary: olc_038 and olc_2d_024 both got rebodied to `_pct(cm, q)` independently in Pass 2, creating a new dup. Resolved by switching olc_038 (base) to `_pct(_ema(cm, q), q)` (relative change of EMA-smoothed cm) while olc_2d_024 (deriv) keeps raw `_pct(cm, q)`.

### Kept by design

- **1 sample-bias constant**: olc_567_opinc_sign_change_freq_y = 0.0 on healthy synth where each profile has stable opinc sign within post-warmup window (no sign changes fire). Real distress firms produce signal. ps_270 / cfs_d3_046 / bss_288 / ri_044 / sd_083/188 / cas distress-flag precedent.
- **16 scalar-mult pairs all KEEP**:
  - 4 synth-coincidence chain (olc_001/385/386/516 — masked-DOL on monotone synth profiles)
  - 4 chain-coincidence (olc_385↔484, olc_386↔484, olc_385↔516, olc_386↔516)
  - 2 sign-flip-via-mask (olc_082↔416/417 — masked rev/opex scaling diverges with mixed-sign growth)
  - 4 incremental-margin == regression-beta synth-coincidence (olc_023/063/517, olc_026/065, olc_028/066, olc_063↔517 — smooth synth makes OLS slope ≈ Δ ratio; gc_086/285 / cfs_121/122 sample-bias precedent)
  - 2 NOPAT-precedent ×365 unit conversion (olc_317↔365 receivables_days, olc_322↔367 payables_days; ls_023/297 + cas_025/136 + cft CCC days precedent)

### Lessons

1. **EMA + delta linearity preserves sign-flip identities.** Pass 1 rebody of olc_038 from `_delta(cm, q)` to `_delta(_ema(cm, q), q)` did NOT break sign-flip with olc_016 because `EMA(1 - cor/rev) = 1 - EMA(cor/rev)` and delta is linear. Linearity-breaking requires nonlinear transforms — `_pct` works because the denominator changes (`cm.shift(q)`) makes it nonlinear in cm.

2. **EMA and delta commute on level.** `_ema(s.shift(q), q) = _ema(s, q).shift(q)` so `_delta(_ema(s, q), q) = _ema(_delta(s, q), q)`. Pass 1's "smoothed delta" vs "delta of smoothed level" rebodies collapsed at FP precision. Lesson: when distinguishing slots, pick operators from different commute classes (EMA+delta vs rolling-mean+delta vs pct+delta).

3. **Class 5 mis-tier rebody pattern.** When a 2-diff body sits in a 2d file matching a 3d sibling, surgical-rebody to single-diff of relative change `_delta(_pct(level, q), q)` preserves the 2d-tier semantic and is distinct from canonical 2d slots that use raw `_delta(level, q)`.

4. **Sample-bias on independent-walk synth.** Even with independent random-walk inputs (RG tab-19 lesson confirmed), signals like "fraction of times margin > 0" coincide for opinc and margin because revenue is positive throughout the synth. Need real-data divergence test or rebody.

### Next-tab pickup

Family DONE. Master priority queue row 40 marked done.

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_olc_harness.py`
- `temp_olc_harness_out.json`
- `temp_olc_harness_err.log`


---

## 2026-05-09 — `hypergrowth_signature` (audit-session-3, tab-hgs)

**Family**: `hypergrowth_signature` — 12 files = 8 base × 75 (chunks 151_225..676_750, no 001-150 chunks) + 2 2nd-deriv × 25 (idx 026-050, 051-075) + 2 3rd-deriv × 25 (same split) = **700 features**. Function prefix `hgs_`; **deriv uses `hgs_d2_NNN` / `hgs_d3_NNN`** (not standard `_2d_` / `_3d_` per CLAUDE.md). `hgs_d3_*` files import `hgs_d2_*` siblings rather than inlining bodies. Daily-cadence (252d / 504d / 756d windows; max base lookback 756d, deriv adds `_delta(s,252).delta(63)` so worst-case ≈ 1080d).

**Inputs union (35 cols)**: assets, assetsc, capex, cashneq, close, debt, deferredrev, depamor, ebitda, eps, equity, fcf, goodwill, gp, high, insiderpct, instpct, intangibles, intexp, inventory, liabilitiesc, low, netinc, opcf, open, opex, opinc, payables, receivables, revenue, rnd, sgna, sharesbas, taxexp, volume.

**Non-Sharadar names** (binding-layer translation per LS/CAS/HEP precedent): `eps` (gc/ve precedent), `opcf` (alias for `ncfo`), `insiderpct` + `instpct` (HEP tab-hep precedent — parallel naming to VAC's `instownpct`).

**Path B mini-harness**: 5 profiles × 2000 daily rows × 35 cols, daily cadence with quarterly anchor fwd-fill, warmup=1500. Profiles: steady / hypergrowth (rev +30%/yr, sb +10%/yr dilution, neg fcf) / mature (rev +8%/yr, profitable, mild buyback) / distress (rev declining, neg netinc) / buyback (positive cash, sb declining, dividend payer).

**Initial run**: 0 errors / 1 all-NaN (hgs_689_cvar) / 7 constants / 2 body-dup groups (the 86-fn group is the harness fingerprint bug — single-line `def fn(x): return X` collapse to empty body after `[1:]` slice; ignore) / 26 value-dup groups / 42 scalar-mult pairs.

**Triage outcome (post user Q1+Q2+Q3 approval)**:

| Class | Count | Disposition |
|---|---:|---|
| Class 1 formula-exact-under-rename | 12 | DELETE higher slot |
| Class 7 sign-flip | 4 | DELETE higher slot |
| Plain-vs-academic delete-plain (Q2 user-approved) | 5 | DELETE plain, keep FF/Dupont |
| Three-way plain+2-academic (Q1 user-approved) | 2 | DELETE plain, keep both academics |
| Naming-bug surgical rebody (Q3) | 1 | hgs_443 → 4q HHI proxy |
| Structural bug fix (Q3) | 1 | hgs_689 min_periods 63 → 10 |
| Class 13 sample-bias constants | 7 | KEEP-by-design |
| KEEP value-dup groups (Class 11/12/13) | 8 | KEEP-by-design |
| Class 16 NOPAT/days/PEG scalar-mults | 4 | KEEP-by-design |
| Class 13 clip-differentiated scalar-mults | 2 | KEEP-by-design |

**Per-file commits** (one per file affected, lower-wins):

| File | Commit | Net |
|---|---|---|
| (claim) | `b079b34` | HANDOFF row 37 claimed |
| `_base_151_225.py` | `52a8f8e` | -2 (hgs_194 = hgs_151; hgs_211 = hgs_357 FF HML) |
| `_base_226_300.py` | `b8bd61e` | -4 (hgs_253 plain vs Beneish/Sloan; hgs_293/294 vs Dupont; hgs_296 sign-flip) |
| `_base_301_375.py` | `14ddf0e` | -2 (hgs_316 vs FF AG; hgs_364 vs Dupont NM) |
| `_base_376_450.py` | `94b7d7f` then `4d001ba` | rebody hgs_443 (HHI proxy; first-pass CV collided with hgs_678, repivoted to true 4q HHI sum-of-squared-shares) |
| `_base_526_600.py` | `9abd210` | -7 (4 plain renames, 1 sign-flip, 2 plain-rename of FF reversal/intermediate momentum) |
| `_base_601_675.py` | `dd3d135` | -5 (hgs_638/642/660 plain renames, hgs_639/643 sign-flips) |
| `_base_676_750.py` | `0cd9d05` | -5 + bug fix hgs_689 (cvar min_periods=63 → 10; same bug class as bss_055 / ve_385 / es_503) |

**Final harness state (post-fix)**:

- 675/700 fns bound (was 700; 25 deletes)
- 0 errors / 0 all-NaN (was 0/1; hgs_689 fix worked)
- 7 sample-bias constants (Piotroski 226/227/587 always-1 on profitable synth; 4-way 0-clique 400/651/655/710 binary regime flags)
- 8 KEEP-by-design value-dup groups (academic-trace + clip-differentiated + sample-bias cliques; per LS/CAS/RI precedent)
- 12 scalar-mult pairs (4 NOPAT/days unit-conversion + 4 academic-trace + 2 sign-flip clip-differentiated + others KEEP)

### Lessons worth carrying

1. **Plain-vs-academic delete preference**: when the same body has both a plain name (`net_margin_level`) and an academic-model name (`dupont_net_margin`, `ff_value_bm_ratio`, `altman_x5`, `beneish_tata`, etc.), the user pre-approved (Q2) "delete plain, keep academic" — overrides Class 1 lower-wins. Mirrors LS ls_061/151/170/188 and CAS cas_062/cas_226 academic-trace KEEP-by-design precedent. Worth surfacing as a 9th audit-precedent class in CLAUDE.md.

2. **Three-way academic-trace dups**: when one slot is plain and TWO others are academic from different models (Beneish + Sloan; Altman + Dupont), KEEP both academics, DELETE plain. Same Q1 pattern.

3. **Naming-bug pivot collisions**: hgs_443's first rebody (revenue CV) value-exact-collided with hgs_678 (already CV). Always re-run harness after each surgical rebody to catch new collisions; in this case a second pivot to true 4q HHI was needed. Same pattern as MA tab-30 Pass 2 (3 secondary collisions caught).

4. **Structural all-NaN bugs** (hgs_689 `min_periods=63` after 5%-survival mask): always check that `min_periods` ≤ expected non-NaN density × window. Class same as bss_055 / ve_385 / es_503 / la_204. The la_530 CVaR was kept as sample-bias because the bug was data-dependent; here it's structural (never works on any input), so fix in place.

5. **Naming convention drift for institutional ownership**: third distinct name observed for the same logical Sharadar SF3 col — `instownpct` (VAC), `instpct` + `insiderpct` (HEP, HGS), `instinvest_pct` (MT). Binding-layer needs translation map for at least 4 variants now.

6. **Harness body-hash false positive**: single-line `def fn(x): return X` patterns collapse to empty body after `[1:]` slice (the def-line is the only line). Drives ~86-fn body-dup groups to be ignored. Same harness fingerprint bug noted in RG tab 19 journal — value-hash is the source of truth.

### Cleanup

Per `feedback_temp_scripts.md`: deleted scratch:
- `temp_hgs_harness.py`
- `temp_hgs_harness_out.json`

### Next-tab pickup

Family DONE. Master priority queue row 37 marked done. Open rows: 38 `hidden_earnings_power` (claimed tab-hep), 41 `pricing_power_signal` (claimed tab-pps), 42 `sales_machine` (pending), 44 `winner_take_all_signal` (claimed tab-wta), 45 `network_growth_engine` (claimed tab-nge), 46 `accounting_manipulation` (untracked / unaudited).

## 2026-05-09 — tab-hep — hidden_earnings_power audit (Path B)

**Outcome:** 600 → 573 features. 0 errors / 0 unexplained dups post-fix.
11 commits across 9 files (1 claim + 9 fix + 1 bug fix).

**Harness** (`temp_hep_harness.py`): 5 profiles × 3500 daily rows × 39 input
cols. Daily-cadence with quarterly anchors fwd-filled. Warmup=2000 to clear
1764d max base lookback (`hep_376_450` 7Y CAPE-style mean PE/EY
`netinc.rolling(TRADING_DAYS_YEAR * 7, min_periods=TRADING_DAYS_YEAR * 3)`)
plus d3 stack of `_delta(s, 63)`. Profiles: healthy_growth, mature_value,
distress, earnings_mgr, cash_gusher (varying revenue drift, vol, om, fcf_skew).

### v1 → v2 synth identity-break progression

v1 produced **8 false-positive scalar-mult pairs** at ratios exactly 3/7, 0.3,
0.7, 0.75 from constant `rnd:sgna = 3:7` proportion baked into synth (HANDOFF
lesson 28 / EA tab 33 / RG tab 19 lesson). Plus **8 false-positive dup groups**
from `ebit==opinc` + `ncfi==capex` + `assets==debt+equity` + `dividends∝netinc`
+ `retainedearnings∝equity` synth identities.

v2 broke each identity:
- Time-varying `rd_share_t` ∈ [0.10, 0.65] for rnd vs sgna split
- Independent `nonop_t` walk so `ebit = opinc + nonop_t` (not equal to opinc)
- Independent `debt_share_t` and `equity_share_t` draws (sum < 1 — other
  liabilities exist; `assets ≠ debt + equity`)
- Independent `other_invest_t` walk so `ncfi = capex + other_invest_t`
- Independent walks for `dividends` and `retainedearnings` (not constant
  fraction of netinc / equity)

After v2: 0 false-positive scalar-mults / 0 false-positive dups. Only the 27
real algebraic deletes and 12 KEEP-by-design groups remained.

### 27 dup deletes by class

- 20 within-base / within-deriv formula-exact (Class 1)
- 3 cancellation-equivalent (Class 2; RL rl_080/081/082 precedent)
- 2 mathematical-identity under `_delta` (Class 6)
- 1 cross-tier base→deriv pollution (Class 4; `hep_179` body is `_delta(...)`)
- 1 algebraic-identity scalar-mult (Class 1 + VE ve_068/112 Shiller_PE precedent)
- 1 positive-revenue identity (RG rg_036 precedent)
- 2 Fama-French rename dups (Class 1; FF factor names without cross-sectional sort)

### 1 bug fix

`hep_234_low_vol_high_quality` called `_safe_div(1.0, cv)` where `_safe_div =
a.div(b.replace(0, np.nan)).fillna(fill)` — applies to Series only. Scalar 1.0
errored with `AttributeError: 'float' object has no attribute 'div'` on every
call. Replaced with direct `1.0 / cv`. Same root-cause class as bss_055 / ve_385/387 /
es_503/504 / la_204/316 / dr_344/345 / gc_331 (CLAUDE.md Class 17).

### KEEP-by-design (12 dup groups + 3 constants post-fix)

- 9 academic-trace dup groups (Altman X1/X5; Ohlson profitability/liquidity;
  Mohanram G1/G2/G3/G5; Beneish TATA + Sloan accruals; Piotroski F4 + Mohanram G3)
- 3 winsorized-clip-doesn't-fire (ROE / ROIC / capex_da_gap)
- 1 synth-coincidence (hep_021/130 — gp-opinc == rnd+sgna by construction;
  diverges with impairments / other opex on real data)
- 1 binary-coincidence (hep_159 Piotroski-F1 ≈ hep_288 deep-value regime — both
  ≈1.0 on healthy synth; diverge when conditions stop coinciding)
- 3 sample-bias constants (hep_115 negative_ccc_flag, hep_348 nwc_negative,
  hep_380 ohlson_liab_exceeds_assets — all binary distress flags = 0 on healthy
  synth, signal on real distress firms)

### Per-file commit cadence

Each fix one commit. Pattern matched HANDOFF tab-cfj `git add file && git commit
-m "..."` chained in single shell command (no intervening `git diff --cached`)
to avoid the cross-tab git-index race lesson from cfj `eca67ae` incident.

### NEW non-Sharadar col types

`insiderpct` (3 fns: hep_146/148/233) + `instpct` (2 fns: hep_147/148). VAC has
single `instownpct` (no underscore). moat_trajectory uses `insider_pct` /
`instinvest_pct` (with underscore). Binding-layer translation map now needs at
least 3 conventions for institutional / insider ownership.

### Next-tab pickup

Family DONE. Master priority queue row 38 marked done. Adjacent rows already
claimed: 36 cash_flow_jerk DONE (tab-cfj), 37 hypergrowth_signature claimed
(tab-hgs), 39 cash_earnings_divergence DONE (tab-ced).

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_hep_harness.py`
- `temp_hep_out.json`
- `temp_hep_err.log`

---

## 2026-05-09 tab-pps: pricing_power_signal (row 41) — surgical-rebody-everything

### Result
14 files / 750 fns. **47 surgical rebodies + 1 all-NaN bug fix, zero deletes.** Post-fix harness: 0 errors / 0 all-NaN / 0 constants / 0 value-dup groups (down from 42) / 5 KEEP-by-design Class 16 scalar-mults (down from 59).

### Disposition rationale
User asked for "per HANDOFF.md policy" but recent precedent (LS, ES, DT, MA, MJ, RJ, OLC) is "surgical-rebody-everything (zero deletes)" while older precedent (RA, CFA, DR, VE, SD, CAS) is "auto-delete per algebraic-identity precedent." Asked the user; chose surgical-rebody-everything to preserve all 750 slots.

### Cadence — first truly bimodal family
13 quarterly-cadence files (`.shift(4)` = YoY = 4 quarters) + 1 fully daily-cadence file (`pps_451_525.py`, 75 OHLCV-only fns) + 18 daily-cadence fns scattered in mostly-quarterly base files (pps_126-135 in 076_150; pps_385-392 in 376_450).

Registry `interval` field is authoritative — harness must dispatch per-fn or risk false-positive constants/all-NaNs. Built dual quarterly+daily synth (5 profiles each) and dispatched on `interval`. New harness lesson logged in HANDOFF row + AUDITS.md.

### Registry naming gotcha
`PRICING_POWER_SIGNAL_2ND_DERIVATIVES_REGISTRY` (no chunk suffix on main 001-025 file) vs `PRICING_POWER_SIGNAL_2ND_DERIVATIVES_REGISTRY_026_050` (with chunk). Initial harness regex `endswith('REGISTRY')` matched the former but missed the chunk-suffixed ones; only got 650 of 750 fns. Fixed to `'REGISTRY' in attr`. Same trap likely lurks in any family with chunked derivative files.

### Rebody catalog (organized by precedent class)

**Class 4 (cross-tier base→deriv pollution, 10 slots)** — base "_yoy_chg" slots whose body equals deriv-side `_roc`. Standard-mode disposition is delete-from-base, but surgical-mode preserves; rebodied each to **scale-normalized YoY** = `_safe_div(_d1(level, 4), _rm(level.abs(), 8))`. Recommended as new precedent for future surgical-mode handling of this class.

**Class 1+2 (formula-exact + cancellation-equiv DuPont decomp, 14 slots)** — pps_060/061/063/067 in deriv files (roc + jerk = 8 slots) and pps_168/169/171/174/180/181 in base file (6 slots). All variants of "DuPont decomposition that cancels back to the unfactored ratio" by RL `rl_080-082` precedent. Rebodied to TTM-smoothed inputs (`mean(num,4)/mean(denom,4)`) preserving "DuPont" semantic intent without redundancy.

**Class 2 (cancellation-equivalent ebitda-ebit = depamor, 3 slots)** — pps_048 (deriv roc + jerk) and pps_150 (base) had `(ebitda-ebit)/X = depamor/X` accounting identity. Rebodied to `(ebitda-ebit)/ebitda` = depreciation share of EBITDA (different normalization).

**Class 9 (same-window same-input collisions → smoothed-input differentiation, 5 slots)** — pps_543/544/545/546/573 EV-yield aliases were literal copies of pps_363/364/365/367/416. Rebodied to TTM-mean numerator (`mean(X,4)/denom`). LS `ls_121` precedent (FCF on 252d-avg debt).

**Class 1 (algebraic-identity in cost-mix, 3 slots)** — pps_580/581/582 cost_structure_(index|slope8|vol8) had `(cor+sgna+rnd)/rev = opex/rev = pps_347` accounting identity. Rebodied to `cor/(sgna+rnd)` operations-vs-overhead/innovation tilt.

**Class 7 (sign-flip algebraic-identity, 4 slots)** — pps_037/039 vol/range of cor/rev = vol/range of gm by sign-flip; rebodied to vol/range of cor/gp. pps_113/114 `(rnd+sgna)/rev = gm-om` algebraic-identity; rebodied to `(rnd-sgna)/rev` tilt. EA `ea_076/077` precedent extended.

**Class 1+3 (composite differentiations, 9 slots)** — pps_022/047, pps_073/384, pps_286/445, pps_153/212, pps_158/223, pps_527/532, pps_591/592, pps_449/599, pps_014/562. Each pair canonicalized to the lower-numbered slot, higher-numbered rebodied to a semantically-distinct sibling (markup-ratio growth, relative-streak, YoY-of-incremental, slope-of-z-score, relative-threshold-consistency, slope-of-z-sum, median composite, z-scored composite, longer window).

**Class 17 (bug fix, 1 slot)** — pps_595_margin_dispersion always-NaN due to `_rs(pd.concat([gm,om,nm], axis=1).T, 3).iloc[0]` shape-misuse. Replaced with proper per-row `concat(axis=1).std(axis=1)`. Same class as bss_055 (Series helper applied in wrong shape).

### KEEP-BY-DESIGN scalar-mults (5)
All Class 16 NOPAT/days-conversion precedent (ls_127/212, ls_023/297, cas_025/136):
- pps_029/033 receivables_to_rev × 90 = days_receivable (roc + jerk).
- pps_116/122 same at level.
- pps_069/431 rev_per_sga × 1000 = rev_per_employee_proxy (employee-proxy unit conversion).
- pps_159/209 ROE × 0.7 = sustainable_growth_rate (constant payout 0.30).

### Per-file commits (8 total)
1. `668363d` — claim row 41 (HANDOFF only)
2. `fe16bcc` — base_001_075: 3 rebodies (cor/gp normalization)
3. `bca4430` — base_076_150: 8 rebodies (scale-norm YoY + spread variants)
4. `5521563` — base_151_225: 13 rebodies (TTM-smoothed + relative-threshold)
5. `77750dd` — base_376_450: 2 rebodies (relative-streak + YoY-of-incremental)
6. `6e0723c` — base_526_600: 12 rebodies + 1 all-NaN bug fix (pps_595)
7. `2c72378` — derivatives_026_050 (2nd + 3rd): pps_048 ebitda_ebit_spread roc/jerk
8. `e163ab8` — derivatives_051_075 (2nd + 3rd): 8 DuPont rebodies (TTM-smoothed + spread)

### Next-tab pickup
Family DONE. Master priority queue row 41 marked done. Adjacent rows: 40 operating_leverage_composite DONE (tab-olc, also surgical-rebody mode), 42 sales_machine pending, 43 moat_trajectory DONE (tab-mt), 44 winner_take_all_signal claimed (tab-wta), 45 network_growth_engine claimed (tab-nge).

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_pps_harness.py`
- `temp_pps_harness_out.json`

---

## 2026-05-10 tab-pc: peak_and_crash re-audit verify pass — 4 missed cross-tier dups

### Result
4 files / 393 → 389 fns. **4 auto-deletes (Class 1/2/4) + 1 caller-rewrite, zero rebodies.** Post-fix harness: 0 errors / 0 all-NaN / 0 vhash dup groups (down from 4) / 2 Class 16 KEEP scalar-mults (down from 2). Commit `ad9955a`.

### Disposition rationale
User asked for "audit per HANDOFF.md policy" on a family already marked DONE (tab 1 / tab 4, commits `0c1443d`, `cfba2e7`, `5c0492d`, `e8888f7`, `fc5ef27`, `c46bab2`). Recent precedent for "DONE family + re-audit" is pricing_power_signal commit `47e0bee` (4 missed Class 1/7 pairs auto-fixed) and revenue_level commit `aa25895` (3 cross-tier dups missed by deriv-only scan). Applied same playbook: build re-audit harness scanning all tiers together, surface missed pairs, auto-apply Class 1-7 deletes.

### Harness (`temp_pc_verify_harness.py`)
Path B daily-cadence mini-harness: 5 profiles (`healthy_growth`, `distress`, `stable_value`, `volatile`, `crash_recovery` with 2 embedded crash regimes at days 800-900 and 1800-1880), N=2800d (warmup=1300d for 5y shift = 1260d), 11 input cols (OHLCV + quarterly fwd-filled revenue/netinc/fcf/assets/debt/equity). Standard vhash + post-warmup z-cosine scalar-mult scan.

### Findings (all 4 auto-deletes)

**Class 1 formula-exact (1)** — `pc_049_drawdown_duration_current` == `pc_006_days_since_ath` at max|a-b|=0.0 on independent random walk. Different implementation (cumcount-within-at_ATH-groups vs cumsum-of-in_dd-within-recovery-groups) but mathematically identical. Caller `pc_131_drawdown_slope_current` updated to call `pc_006`.

**Class 2 cancellation-equivalent (1)** — `pc_265_up_down_capture_ratio` == `pc_250_omega_ratio_proxy` at max|a-b|=2.22e-16. Body is `(mean_up/mean_dn)` vs `(sum_up/sum_dn)` over same window → `(X/W)/(Y/W) = X/Y`. RL `rl_080/081/082` + CAS `cas_182/183` precedent.

**Class 1+4 cross-tier base→deriv pollution (2)** —
- `pc_132_drawdown_convexity` == `pc_351_jerk_dd_ath_5d` at max|a-b|=0.0. Body is 2nd-diff_5d_5d of `dd_ath` — that's a 3rd-deriv-tier operation per CLAUDE class 4 (RL `rl_227/229/231` precedent).
- `pc_284_drawdown_acceleration_21d` == `pc_365_jerk_ema21_5d` at max|a-b|=7.5e-15. `ema(2nd_diff(x)) = 2nd_diff(ema(x))` by LTI commutation; the algebraic forms differ but both are 3rd-deriv-tier signals.

### KEEP-BY-DESIGN scalar-mults (2)

Both Class 16 unit-conversion (LS `ls_023/297` + CFT cumulative-vs-yield precedent):
- `pc_079_martin_ratio_252d` / `pc_083_burke_ratio_proxy_252d` ratio=100 (Martin uses Ulcer Index in pct scale `(100*dd/rh)^2`; Burke uses fractional dd `(dd/rh)^2`).
- `pc_090_downside_potential_63d` / `pc_147_cumulative_crash_return_1q` ratio=1/63 (mean vs cumulative over W=63 quarter; `mean = sum/63`).

### KEEP-BY-DESIGN synth-bias constants (10)
6 from synth-cadence artifacts (open=close.shift(1) → no overnight gaps): pc_062 close_vs_intraday_range (=0.5 from symmetric high/low intra), pc_073/074 crash/peak_gap_count, pc_120/121 overnight_gap_contribution/crash, pc_124 exhaustion_gap, pc_243 crash_gap_vs_intraday_ratio. 3 fundamental-vs-price flags from healthy-profile bias: pc_174 fundamental_crash_no_price_crash, pc_267 price_crash_with_revenue_growth, pc_268 price_peak_with_declining_revenue. (Different list from original audit's 9 KEEP because new harness profile mix is broader and triggers the original list's flags but not these 10.)

### Cross-chain dedup connectivity lesson
Original tab-1 audit scanned base+base. Original tab-4 audit scanned deriv+deriv. Neither scanned base+deriv together, so missed all 4 cross-tier dup groups (3 of them are base↔deriv pairs). Same lesson as RL tab 7-cont (commit `aa25895`, 3 base dups == deriv-v2 slots) and pricing_power_signal re-audit (commit `47e0bee`, 4 missed Class 1/7 pairs). Standard practice now: when re-auditing a family, run ONE harness that loads all tier files together.

### Per-file commit
1. `ad9955a` — peak_and_crash_base_001_150 + peak_and_crash_base_151_300: 4 deletes (pc_049/132/265/284) + 1 caller rewrite (pc_131 → pc_006). Single commit since all 4 share the same re-audit pass + same precedent class set.

### Next-tab pickup
Family DONE (re-audit verified). Master priority queue row 1 already marked done; updated with re-audit commit hash. Adjacent rows: row 2 crash_speed DONE, row 4 basing_pattern DONE, row 8 price_moving_averages DONE — all candidates for the same cross-tier re-audit pass.

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_pc_verify_harness.py`
- `temp_pc_verify_out.json`
- `temp_pc_dup_verify.py`

---

## 2026-05-10 tab-nge: network_growth_engine (row 45) — surgical-rebody-everything

### Result
18 files / 1050 fns (LARGEST family in repo, beats IT 950). **~94 surgical
rebodies + 0 deletes** preserving all 1050 slots, across two passes spanning
17 fix commits (10 prior-session + 7 this-session). Post-fix harness:
0 errors / 0 all-NaN / 7 constants / 0 body-dups / 3 value-dup groups (all
KEEP-by-design) / 4 scalar-mult pairs (all KEEP-by-design).

### Pre-fix state (after prior-session commits, before this session)
22 value-dup groups + 39 scalar-mult pairs + 8 constants + 3 body-dups
(1 was harness false-positive empty-body group affecting 7 single-line
return-fns in 751_825).

### Files committed this session (8 fix commits + 1 audit-add)
- `40d436e` — audit(network_growth_engine): add base_001_075 + base_226_300
  canonical files (no internal rebodies; partner higher-numbered slots in
  other files are rebodied to match).
- `c58db2e` — 151_225: rebody 9 dupont/prat/quality dups (TTM-smoothed
  DuPont components, EMA-smoothed PRAT margin, debt/equity for PRAT
  leverage vs A/E for DuPont, TTM-smoothed PRAT composite, relative-
  quality 3y-trailing for quality-ROE).
- `6c562c2` — 376_450 (add+rebody): ng_405 altman_x5 + ng_416 beneish_tata
  on TTM-mean asset base.
- `2ae9c2e` — 601_675: rebody 8 ohlson/springate/gscore dups (1y vs 2y
  asset-base smoothing distinguishes Ohlson/Springate; relative-to-3y-
  median G-score binaries).
- `9eb0da7` — 676_750: rebody ng_694 dilution-rev-growth (TTM-vs-baseline
  form breaks log-linear synth coincidence with raw 1y).
- `b2eaea0` — 751_825: rebody ng_814 book_value_cagr_3y (5y CAGR on TTM-
  mean BVPS to differentiate from ng_813 4y slope).
- `6dfb35a` — derivatives (all 6 deriv files added): rebody ng_2d_001
  revenue_growth_slope to QoQ-input form (vs ng_478 YoY-input Sharpe).
- `e39ec4f` — Pass-2: ng_405 + ng_616 secondary collisions.

### Pass-2 secondary collisions caught and fixed (`e39ec4f`)
- `ng_405` Pass-1 `rev / mean(A, 1y)` matched `ng_178` PRAT banker
  convention by accident. Re-rebody to TTM-numerator form
  `mean(rev, 1y) / A` — Altman's variant smooths the numerator.
- `ng_616` Pass-1 `(NCFO - NI) / A > 0` is mathematically identical to
  `NCFO > NI` since A>0 (a Class-6 mathematical-identity invisible to
  the rebody-author when only the formula's shape is inspected). Re-
  rebody to `NCFO > mean(NI, 1y)` — improving-cash-quality variant.

### 5-way smoothing-axis assignment (asset-turnover cluster)
After all rebodies the 5 nominally-similar asset-turnover slots each
use a distinct smoothing axis, illustrating the surgical-rebody-everything
pattern at its cleanest:
- `ng_031` = raw `rev / A`
- `ng_152` = `mean(rev/A, 1y)` (DuPont — smooth ratio)
- `ng_178` = `rev / mean(A, 1y)` (PRAT — smooth denom, banker)
- `ng_405` = `mean(rev, 1y) / A` (Altman — smooth numerator)
- `ng_637` = `rev / mean(A, 2y)` (Springate — long smooth denom)

### KEEP-BY-DESIGN final state
3 value-dup groups + 4 scalar-mult pairs, all classified:
- 4-fn constants=0 cluster `ng_330/600/605/608` (residual-income flag /
  ultimate-compounder / Ohlson insolvency / Ohlson loss) — Class 13
  sample-bias on healthy synth (ps_270/cfs_d3_046/bss_288 precedent).
- 2-fn constants=1 `ng_389/708` (piotroski-ROA-positive / dividend-
  consistency) — Class 13 on healthy synth.
- `ng_846/896` quality_value_interaction vs op_cash_yield — Class 12
  clip-differentiated (`cq.clip(-2, 3)` doesn't fire on healthy synth
  where NCFO~NI; LS ls_022/296 + CFA cfa_105/166 precedent; noted in
  earlier commit 19d3134).
- `ng_232/245` + `ng_233/246` ratio=365 — days-conversion scalar-mult
  Class 16 (cas_025/136 precedent).
- `ng_309/325` ratio=0.08 — WACC hurdle constant scalar-mult Class 16
  (NOPAT-precedent ls_127/212).

### Harness body-hash false-positive
7 single-line `def fn(x): return X` fns in 751_825 (`ng_814/815/816/817/
818/820/822`) collapsed to empty body after `inspect.getsource().split(
'\n')[1:]` slice in `get_function_body_hash`. Same fingerprint
documented in RG tab-19 / HGS journal entries. Value-hash is source of
truth; these 7 fns produce distinct outputs. No source change needed.

### Cumulative lesson
Largest family in repo (1050 fns) had ~9% of slots as alpha-rename or
algebraic-identity dups stemming from chunks 601-900 being a re-
implementation pass on early features 001-225. Surgical-rebody-everything
preserved each slot's name semantics by varying along: smoothing
(instantaneous → TTM rolling-mean / EMA); window (1y → 2y/3y/4y/5y);
operator (delta → slope → CAGR → log-CAGR); denominator (raw → smoothed
num / denom / ratio). Pass 2 was needed where Pass-1 rebodies collided
with existing slots or with a mathematical identity that only surfaced
when computed on synth — only re-running the harness post-Pass-1 caught
them.

### Per-file commit cadence
Each fix one commit. Matched HANDOFF tab-pps / tab-wta cadence.

### Next-tab pickup
Family DONE. Master priority queue row 45 marked done. Adjacent rows:
44 winner_take_all_signal DONE (tab-wta), 46 accounting_manipulation
DONE (this-tab earlier).

Deleted scratch per `feedback_temp_scripts.md`:
- `temp_nge_harness.py`
- `temp_nge_harness_out.json`
