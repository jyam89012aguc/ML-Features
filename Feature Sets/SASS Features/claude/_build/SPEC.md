# SASS Signal-Feature Build Spec (hedge fund) — canonical contract

You are generating ML **signal features** for ONE feature family. Every feature is a
standalone Python function that takes pandas Series (named exactly as source DB columns)
and returns a pandas Series of equal length, name ending in `_signal`.

Asset class: US equities. Target: 10x stocks over 5-year holds, all market caps.
Data: DuckDB `trading.duckdb`. The features below run inside a pipeline that feeds each
function the named pandas Series; your job is ONLY to author distinct, high-signal formulas.

## ISOLATION / SAFETY (HARD — read first)
- Write ONLY inside your own family folder: `C:\SASS-claude\{FOLDER}\`.
- NEVER delete, move, or overwrite anything OUTSIDE your own family folder.
- NEVER run a recursive/glob delete (`rm -rf`, `Remove-Item -Recurse`, delete of a parent dir,
  delete of `C:\SASS-claude\*`). If you create a build-helper script, put it INSIDE your own
  family folder and delete it by its exact single filename only.
- Do not touch `C:\Features\...` at all. Your entire output lives under `C:\SASS-claude\`.

## Output: exactly 4 files per family, written to `C:\SASS-claude\{FOLDER}\`

1. `{FOLDER}_base_001_075_claude.py`            — 75 base features
2. `{FOLDER}_base_076_150_claude.py`            — 75 base features
3. `{FOLDER}_2nd_derivatives_001_150_claude.py` — 150 features = **slope** (1st math derivative of a base feature)
4. `{FOLDER}_3rd_derivatives_001_150_claude.py` — 150 features = **jerk** (2nd math derivative of a base feature)

(Filenames use `_2nd_derivatives_` / `_3rd_derivatives_`. Internal function `{type}` token
is `base` / `slope` / `jerk` respectively.)

## Function-name format (REQUIRED)
`{short}_{FOLDER}_{calc_id}_{window}d_{type}_v{NNN}_signal`
- short: the family's 4-5 char code (given per family, e.g. `f01ts`)
- FOLDER: full folder name, e.g. `f01_trend_structure`
- calc_id: short descriptive calc id, e.g. `pxma`, `roc`, `accr`
- window: integer trading-day window, e.g. `21d`, `63d`, `252d`
- type: one of `base`, `slope`, `jerk`
- NNN: zero-padded 3-digit version
- always ends `_signal`
Example: `f01ts_f01_trend_structure_pxma_63d_base_v007_signal`

## Input-column rules (HARD)
- Price families: function inputs are a subset of `{open, high, low, close, closeadj, volume}`.
  - ANY rolling window > 21 trading days MUST use `closeadj` (splits corrupt `close` on 63d/126d/252d/504d).
  - Intraday range / gap features (window <= 5d) use unadjusted `open/high/low/close` from a single day.
  - Volume is raw `volume`; use `closeadj * volume` for dollar-volume on windows > 21d.
- Fundamental families: every feature's inputs include >= 1 fundamental column (see your family row).
- Valuation/ownership families: every feature's inputs include >= 1 metrics or ownership column.
- Function signatures vary per feature — accept exactly the pandas Series the formula needs,
  named exactly as the source column. Inputs are inferred from the signature.

## Derivative files (HARD)
- File 3 (slope) = 1st math derivative of a base feature; File 4 (jerk) = 2nd math derivative.
- Each function MUST be a fully expanded `def` computing its formula inline. NO dynamic generation.
- FORBIDDEN in files 3 & 4: importlib, exec, globals(), setattr on module, building functions in
  a loop, `_make()` factories, dict-comprehension over a base registry.
- Each slope/jerk uses a ROC window appropriate to its base window (5d base -> 5d ROC; 21d base
  -> 5d or 21d ROC; 252d base -> 21d or 63d ROC). Do NOT hardcode one ROC window everywhere.
- Each derivative file MUST be >= 30KB and <= 75KB. Files smaller than 30KB mean you used a
  generator — rewrite with expanded defs.

## Distinctness (HARD) — the user's #1 requirement is "no duplicates, high signal"
- NO shared parametric `_core()` feature function. Every feature contains its own inline formula.
- FORBIDDEN: `formulas=[...]; return formulas[variant % N]` or any index-into-list pattern.
- Within a file: no two features may share the same expression up to a window change. If A is
  `_mean(x,21)` and B is `_mean(x,63)`, that is a DUPLICATE pair — at most one may exist.
- Every feature must reflect THIS family's named domain (see your family row). Generic
  drawdown/range/zscore features that any family could claim are NOT acceptable here unless they
  are the family's own domain.
- You have a wide design space: combine the domain primitive with z-scoring, ratios, interactions
  (× volume / × dollar-vol / × range), differences across windows, rank/percentile, sign×magnitude,
  exponential weighting, regression slope, dispersion, hit-rate, asymmetry, etc. Use that variety
  so the in-file correlation test passes by design, not by luck.

## NaN policy (HARD)
- Do NOT call `fillna(0.0)` in helpers or rolling computations. Preserve NaN through warm-up.
- ONLY at the final return: `result.replace([np.inf, -np.inf], np.nan)`. Leave NaN as NaN.

## Registry + self-test (HARD) — each file ends with these
- A list `_FEATURES = [ ... all feature fns ... ]` then:
```
def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]
REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
{FOLDER_UPPER}_REGISTRY_{RANGE} = REGISTRY   # e.g. F01_TREND_STRUCTURE_REGISTRY_001_075
```
- `if __name__ == "__main__":` block that:
  (a) builds synthetic inputs with `np.random.seed(42)`, n=1500, including EVERY column the file
      consumes (use the synthetic harness below);
  (b) calls every feature; asserts result is reproducible (call twice, equal);
  (c) asserts (after warm-up index 504, dropna) `nunique() > 50`, `std() > 0`, not all-NaN;
  (d) asserts pairwise `abs(A.dropna().corr(B.dropna())) <= 0.97` for ALL feature pairs in the file
      (this is the duplicate guard — if a pair exceeds it, REPLACE one feature with a structurally
       different formula, do not just rewindow);
  (e) asserts >= 80% of features have < 50% NaN after warm-up (first 504 rows);
  (f) asserts feature count == expected (75 for base files, 150 for derivative files);
  (g) prints `OK {filename}: {n} features pass`.
- The file MUST run `python {file}.py` with no AssertionError. Iterate until green.

### Synthetic harness (use the subset your features consume)
```
import numpy as np, pandas as pd
np.random.seed(42)
n = 1500
rets = np.random.normal(0.0005, 0.02, n)
closeadj = pd.Series(100.0*np.exp(np.cumsum(rets)), name="closeadj")
close    = pd.Series(closeadj.values, name="close")
openp    = pd.Series(close.shift(1).fillna(close.iloc[0]).values*(1+np.random.normal(0,0.005,n)), name="open")
high     = pd.Series(np.maximum(close, openp)*(1+np.abs(np.random.normal(0,0.01,n))), name="high")
low      = pd.Series(np.minimum(close, openp)*(1-np.abs(np.random.normal(0,0.01,n))), name="low")
volume   = pd.Series(np.abs(np.random.normal(1e6,3e5,n))+1e5, name="volume")
# slowly-varying positive "fundamental"-like series (quarterly-step random walk), one per fundamental col used:
def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n//63 + 1), 63)[:n]
    s = base*np.exp(np.cumsum(steps/63))
    if allow_neg: s = s - base*0.3
    return pd.Series(s, name=None)
# build each fundamental/metrics/ownership column your features need via _fund(<distinct seed>), then .rename(col)
```
Name each synthesized fundamental/metrics/ownership Series exactly as its column. For ratios that
can be negative (netinc, fcf, opinc, retearn, workingcapital, ncf*), pass `allow_neg=True`.
The single `.fillna` inside this synthetic builder is allowed (test scaffold only); the BAN on
`fillna(0.0)` applies to feature/helper code, not the `__main__` synthetic harness.

## Other rules
- Helpers (`_z`, `_mean`, `_std`, `_safe_div`, family `_{short}_*` domain primitives) at top of file.
  Domain primitives are allowed and encouraged (they encode the family's economics) but must NOT be a
  generic `_core()` that takes a formula-id. Reuse a primitive across features only with DIFFERENT
  surrounding math so the pair stays uncorrelated.
- Every file passes `ast.parse()` and is <= 75KB. Base files target ~25-40KB.
- Trading days: 252/yr, 126/half, 63/qtr, 21/mo, 5/wk. Common windows: 5,21,63,126,252,504.
- Do NOT curate/rank features — generate the full count. ML decides significance.
- No README, no markdown, no prints other than the self-test OK line. Files only.

## Pre-return checklist (must all be PASS)
[ ] 4 files written with exact names to C:\SASS-claude\{FOLDER}\
[ ] wrote ONLY inside your own family folder; deleted nothing outside it; ran no recursive delete
[ ] no importlib/exec/globals/setattr-in-loop; no `_core()`; no `formulas[i%N]`
[ ] files 3 & 4 are each 30-75KB; base files <=75KB
[ ] window>21d uses closeadj (price families); fundamentals families use >=1 fundamental col/feature;
    valuation/ownership families use >=1 metrics/ownership col/feature
[ ] no fillna(0.0) in feature/helper code; only replace([inf,-inf],nan) at return
[ ] function names match the format spec; registry dict names include FOLDER
[ ] `python {file}.py` runs green for ALL 4 files (no AssertionError)
[ ] every base file computes distinct expressions (no parametric reuse)
