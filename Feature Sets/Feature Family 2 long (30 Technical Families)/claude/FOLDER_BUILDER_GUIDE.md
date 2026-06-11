# Folder-builder shared guide

You are building one folder of ML features in this directory:
`C:\Users\jyama\Desktop\active_non audited features per AI\claude\20260510_223738\`

A reference folder already exists at `f01_moving_average_systems/`. Skim its 4 files BEFORE starting to learn the working pattern:
- `f01_moving_average_systems_base_001_075_claude.py` (75 features, 55 KB)
- `f01_moving_average_systems_base_076_150_claude.py` (75 features, 63 KB)
- `f01_moving_average_systems_slope_001_150_claude.py` (150 features, 73 KB)
- `f01_moving_average_systems_jerk_001_150_claude.py` (150 features, 75 KB)

## Per-folder deliverables (always 4 files)

For your folder `{FOLDER}` (e.g., `f02_price_channel_position`) with 5-char short code `{SHORT}` (e.g., `f02pc`):

1. `{FOLDER}/{FOLDER}_base_001_075_claude.py` — 75 features v001-v075
2. `{FOLDER}/{FOLDER}_base_076_150_claude.py` — 75 features v076-v150
3. `{FOLDER}/{FOLDER}_slope_001_150_claude.py` — 150 features = 1st derivative of corresponding base feature
4. `{FOLDER}/{FOLDER}_jerk_001_150_claude.py` — 150 features = 2nd derivative of corresponding base feature

Create the `{FOLDER}/` subdirectory if missing.

## Function naming (REQUIRED format)

`{SHORT}_{FOLDER}_{calc_id}_{window}d_{type}_v{NNN}_signal`

- `SHORT` is the 5-char folder code (e.g., `f02pc`)
- `FOLDER` is the full folder name (e.g., `f02_price_channel_position`)
- `calc_id` is a short calc identifier (e.g., `chpos`, `dist20`)
- `window` is integer trading days (e.g., `21d`, `63d`)
- `type` is `base`, `slope`, or `jerk`
- `NNN` is 3-digit version, zero-padded
- Always ends with `_signal`

Example: `f02pc_f02_price_channel_position_chpos_20d_base_v001_signal`

## HARD constraints

1. **Each function fully expanded `def` block**. No `_core()` factory, no `formulas[i]` indexing, no factory loops, no `importlib`/`exec`/`globals()`/`setattr` patterns. Utility helpers (e.g., for an MA construction) are allowed but each feature function must spell its formula inline.

2. **NaN policy**: NEVER call `fillna(0.0)` (or any `fillna(<value>)`) inside helpers or rolling computations. Preserve NaN through warm-up. Only `result.replace([np.inf, -np.inf], np.nan)` at the function's final return. Filling NaN with 0 creates fake clusters at zero in trained models and is forbidden.

3. **Window > 21 trading days → use `closeadj`** (not `close`). Windows ≤ 21 use `close`. This applies to any rolling window on close-based inputs. For OHLC features within a single bar (window ≤ 5), use unadjusted `open/high/low/close`.

4. **Domain integrity**: every feature must reference your folder's named domain. Generic features that any folder could claim are NOT acceptable. For example, a feature in `f04_support_resistance_proximity` must reference prior support/resistance levels; one in `f07_gap_behavior` must reference open-vs-prior-close gaps. If a feature would be at home in `f01_moving_average_systems`, it doesn't belong here.

5. **No structural duplicates** within a file or across the 2 base files in your folder: "no two features may share the same expression up to a window-size change. If feature A is `_mean(close, 21)` and feature B is `_mean(close, 63)`, that is a DUPLICATE pair — at most one may exist."

6. **Registry dict at end of each file**: `{FOLDER}_base_001_075_REGISTRY = {name: {"inputs": [...], "func": fn}}` (or `_base_076_150_`, `_slope_001_150_`, `_jerk_001_150_`). Inputs list must include exactly the source column names the function consumes (subset of `{open, high, low, close, closeadj, volume}`).

7. **Self-test at file bottom**. Copy the `_synthetic_inputs` and `_self_test` block exactly as written in `f01_moving_average_systems_base_001_075_claude.py` (regime-switching 4-segment GBM, n=800, seed=42, warm-up=252). The test must assert:
   - All features produce non-NaN, non-constant outputs
   - Pairwise `|corr| ≤ 0.95` on the post-warmup window (use `corr(min_periods=50).abs()`)
   - ≥ 80% of features have < 50% NaN after warm-up

8. **File size**: each file 30,000 ≤ bytes ≤ 75,000 (HARD limits). Base files have no minimum but cap at 75 KB. Slope/jerk MUST be ≥ 30 KB (proves 150 functions are fully expanded, not generator output). Helpers, blank lines, docstrings can be trimmed if needed to fit 75 KB cap.

9. **`ast.parse()` must succeed** on every file.

10. **Each file must run** `python <file>.py` and print the expected OK line:
    - `OK base_001_075: 75 features, max |corr|=X.XXXX, coverage_ok=YY.YY%`
    - `OK base_076_150: 75 features, ...`
    - `OK slope_001_150: 150 features, ...`
    - `OK jerk_001_150: 150 features, ...`

## ROC window rule for slope/jerk files

For each slope/jerk feature, the inner derivative window depends on the base window:
- Base window ≤ 5 → k = 5
- 6 ≤ base window ≤ 21 → k = 5 or 10
- 22 ≤ base window ≤ 63 → k = 10 or 21
- 64 ≤ base window ≤ 200 → k = 21 or 63
- base window > 200 → k = 63

Vary k across features within a bracket. DO NOT hardcode the same k for all features. This variation also breaks correlations between similar-shape features.

- Slope = `base.diff(k)` (or `base.diff(k) / base.abs().rolling(k).mean()` if normalization needed for corr-decorrelation)
- Jerk = `base - 2*base.shift(k) + base.shift(2k)` (or normalized variant)

For sign/discrete base features, slope = `base.diff(k)` is still meaningful (values in `{-2,-1,0,1,2}` for sign-based, integer for counts).

## Recipe to pass the pairwise-corr ≤ 0.95 test

This is the hardest constraint. Lessons from f01:

- **AT MOST 3-5 raw "level-distance" features** per file, spaced VERY widely in window (e.g., 8d, 50d, 200d). Many similar level-distance features at nearby windows correlate > 0.95.
- **Mix structural classes aggressively**: binary signs, discrete counts, streak/days-since signals, percentile ranks, stochastics, bounded transforms (arctan, tanh, sigmoid, %B), slopes, curvatures, jerks, kernel-comparison differentials, statistical (Hurst, skew, kurt, MAD/std, autocorr).
- **Cross-window differentials null absolute drift** (e.g., short_slope − long_slope, log(MA20) − log(MA50)). Use these instead of more level-distance features.
- **Use OHLC inputs** where the domain allows: features using high/low/open differ structurally from close-only features.
- **If a pair > 0.95 emerges**: identify the offending features (see diagnostic snippet below) and REPLACE one with a structurally different feature class (e.g., swap a level-distance for a kurtosis or a streak count). Do NOT just tweak the window — that's still a duplicate per the rule.

Diagnostic snippet to find offenders:
```python
import sys; sys.path.insert(0, '.')
from <module> import REGISTRY, _synthetic_inputs
import pandas as pd, numpy as np
df = _synthetic_inputs(800, 42)
res = {n: e['func'](*[df[c] for c in e['inputs']]) for n, e in REGISTRY.items()}
A = pd.concat(res, axis=1).iloc[252:].replace([np.inf, -np.inf], np.nan)
C = A.corr(min_periods=50).abs(); np.fill_diagonal(C.values, 0.0)
for i, a in enumerate(C.columns):
    for j, b in enumerate(C.columns):
        if j > i and C.iloc[i,j] > 0.94:
            print(f'{C.iloc[i,j]:.4f}  {a}  vs  {b}')
```

## Self-test boilerplate (copy verbatim into each file)

```python
def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in REGISTRY.items():  # rename to the right registry constant
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK <NAME>: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
```

## Process per folder

1. Read this guide. Read `f01_moving_average_systems` files for template reference.
2. Design ≥ 75 distinct features for the domain. Use heavy structural diversity per the lessons.
3. Write base file 1. Run python on it. Iterate until self-test passes.
4. Write base file 2. Iterate.
5. Write slope file. Iterate.
6. Write jerk file. Iterate.
7. Final verification: all 4 self-tests pass, all files 30–75 KB, ast.parse OK, no `fillna(0.0)` outside docstrings, no `_core()`/`importlib`/`exec`/`globals()`/`setattr` patterns.

Run `python <file>` via the `Bash` tool. Iterate on corr failures by replacing offending features with structurally different ones (NOT just window changes).

Use the Edit/Write/Read tools — do not modify any file outside your assigned folder.

## Final report

Report back with: folder path, 4 file sizes, max |corr| per file, NaN coverage % per file, ast.parse status, and any constraint waivers you had to apply.
