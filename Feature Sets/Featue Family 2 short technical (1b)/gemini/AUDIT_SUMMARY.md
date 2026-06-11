# Generated Feature Audit Summary

Audit date: 2026-05-18

Guide used: `C:\Users\jyama\Desktop\active_non audited features per AI\Audit Scripts`

## Scope

- Workspace audited: `C:\Users\jyama\Desktop\jahren new features\short_technical_features_1b_gemini`
- Directory inventory: 218 feature folders
- Folders containing Python files: 110
- Empty/non-code feature folders: 108
- Python files audited: 880
- Public feature functions discovered: 66,000

## Artifacts

- `audit_generated_features.py` - local audit harness adapted to this generated repo shape.
- `AUDIT_STATIC_REPORT.json` - parse/import/signature inventory.
- `AUDIT_DYNAMIC_REPORT.json` - full synthetic runtime audit, exact-output duplicate scan.
- `AUDIT_DUPLICATE_FOLDER_COUNTS.csv` - compact per-folder duplicate-group counts.
- `AUDIT_SCALAR_REPRESENTATIVE_01.json` and `AUDIT_SCALAR_REPRESENTATIVE_02.json` - representative scalar-multiple scans.
- `AUDIT_DYNAMIC_SPECTRAL_AFTER_FIX.json` - targeted post-fix spectral runtime audit.

## Method

The harness follows the audit-guide pattern, adjusted for this repo's generated files:

- AST parse every Python file.
- Import every Python file in isolation.
- Discover top-level public functions by signature instead of registry entries.
- Bind all parameters by name to synthetic daily OHLCV/fundamental Series.
- Run every feature on 1,500 business-day inputs.
- Check runtime errors, output length/alignment, all-NaN outputs, constants after warmup, exact value duplicates by rounded output hash.
- Run representative z-correlation/ratio scalar-multiple scans on folders `01_ath_proximity_extension_gemini` and `02_parabolic_blowoff_signature_gemini`.

## High-Level Results

| Check | Result |
|---|---:|
| Parse errors | 0 |
| Import errors | 0 |
| Runtime errors | 6,000 |
| Misaligned/shape-bad outputs | 0 |
| All-NaN outputs | 0 |
| Constant outputs | 0 |
| Exact-output duplicate groups | 11,960 |
| Representative scalar-multiple candidates | 0 |

## Finding 1 - Spectral Fragility Runtime Failure

Severity: High - fixed 2026-05-18

All 6,000 runtime errors come from these 10 folders:

- `101_spectral_fragility_101_gemini`
- `102_spectral_fragility_102_gemini`
- `103_spectral_fragility_103_gemini`
- `104_spectral_fragility_104_gemini`
- `105_spectral_fragility_105_gemini`
- `106_spectral_fragility_106_gemini`
- `107_spectral_fragility_107_gemini`
- `108_spectral_fragility_108_gemini`
- `109_spectral_fragility_109_gemini`
- `110_spectral_fragility_110_gemini`

Each folder has 600 feature functions, and every one fails with:

```text
LinAlgError('0-dimensional array given. Array must be at least two-dimensional')
```

Representative source:

- `101_spectral_fragility_101_gemini/101_spectral_fragility_101_gemini__base__001_075.py:62`
- `101_spectral_fragility_101_gemini/101_spectral_fragility_101_gemini__base__001_075.py:75`

Root cause: `_absorption_ratio_proxy()` builds a two-column DataFrame, then calls `data.rolling(21).apply(_ar, raw=True)`. Pandas applies the rolling function column-by-column, so `_ar()` receives a 1-D array, not a 2-D rolling matrix. `np.corrcoef(w.T)` then degenerates to a scalar, and `np.linalg.eigvalsh()` rejects it.

Resolution: fixed all 80 helper copies in folders `101_spectral_fragility_101_gemini` through `110_spectral_fragility_110_gemini`. `_absorption_ratio_proxy()` now manually walks 21-row multivariate windows, computes the cross-series correlation matrix with `rowvar=False`, sums the top `n_comp` eigenvalues, and returns an aligned Series.

Post-fix verification: `AUDIT_DYNAMIC_SPECTRAL_AFTER_FIX.json` audited 80 files / 6,000 functions with 0 parse errors, 0 import errors, 0 runtime errors, 0 shape issues, 0 all-NaN outputs, and 0 constants. Exact duplicate groups remain a separate generated-template issue.

## Finding 2 - Massive Exact Duplicate Output Groups

Severity: High

The dynamic harness found 11,960 exact-output duplicate groups. These are not scattered randomly; they are generated-template duplicates.

Pattern:

- 100 folders have duplicate groups.
- `01_ath_proximity_extension_gemini` has 80 duplicate groups.
- `02_parabolic_blowoff_signature_gemini` and `03_family_3_gemini` through `100_family_100_gemini` each have 120 duplicate groups.
- 118 folders have no Python files or no duplicate groups.

Group-size distribution:

| Duplicate group size | Count |
|---:|---:|
| 5 | 11,880 |
| 11 | 40 |
| 2 | 28 |
| 3 | 8 |
| 6 | 4 |

Representative duplicate cluster:

- `01_ath_proximity_extension_gemini/01_ath_proximity_extension_gemini__base__001_075.py:355`
- `01_ath_proximity_extension_gemini/01_ath_proximity_extension_gemini__base__001_075.py:415`

`f01_athx_gemini_041`, `051`, `061`, `071`, `081`, etc. repeat the same ATR-normalized distance logic for the same effective window and produce identical output.

Representative generated tier pattern:

- `02_parabolic_blowoff_signature_gemini/02_parabolic_blowoff_signature_gemini__base__001_075.py:75`
- `02_parabolic_blowoff_signature_gemini/02_parabolic_blowoff_signature_gemini__d1__001_075.py:75`

The base function returns a rolling curvature signal; derivative tiers wrap similar repeated generated formulas. Within each folder, many features collapse to identical outputs across repeated window/shift/name slots.

Disposition per guide: most of these appear to be Class 1 formula-exact/generated-template duplicates or value-exact duplicates needing body inspection before mass deletion. Lower-numbered feature slots should be treated as canonical if applying the existing auto-delete precedent.

## Finding 3 - Empty Named Feature Folders

Severity: Medium

108 feature folders are present but contain no Python files. Examples include:

- `03_topping_pattern_classical_gemini`
- `04_distribution_top_signature_gemini`
- `05_failed_breakout_dynamics_gemini`
- `101_absorption_ratio_standardized_shift_gemini`
- `110_spectral_regime_transition_composite_gemini`

The actual audited code lives in generated `NN_family_N_gemini` folders and the explicit `01_...`, `02_...`, `101_spectral...` through `110_spectral...` folders. This is a packaging/completeness issue if the named folders were intended to contain the final feature files.

## Finding 4 - No Basic Structural Failures Outside Spectral

Severity: Low

Outside the spectral helper failure:

- Every Python file parses.
- Every Python file imports.
- Every runnable feature returns a Series-like output with the expected 1,500-row alignment.
- No runnable feature was all-NaN on the synthetic data.
- No runnable feature was constant after warmup.

## Recommended Next Steps

1. Fix `_absorption_ratio_proxy()` across folders 101-110, then rerun `python audit_generated_features.py --folder <folder>` for each spectral folder.
2. Decide disposition for duplicate groups before source edits. The guide supports auto-deleting formula-exact generated duplicates, but the count is large enough that a scripted delete/re-registry pass should be reviewed carefully.
3. If source reduction is desired, start with one representative folder such as `02_parabolic_blowoff_signature_gemini`, delete higher-numbered exact duplicates, rerun its audit, then generalize.
4. Resolve whether the 108 empty named folders are expected staging folders or missed generation outputs.
