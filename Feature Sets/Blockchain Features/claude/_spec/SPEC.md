# Blockchain feature family build spec (claude)

You build ONE feature family = a folder `fNN_<name>` under `D:\Features\claude\`
containing exactly 4 Python files:

1. `fNN_<name>_base_001_075_claude.py`        (75 base features, v001-v075)
2. `fNN_<name>_base_076_150_claude.py`        (75 base features, v076-v150)
3. `fNN_<name>_2nd_derivatives_001_150_claude.py`  (150 slope features — GENERATED)
4. `fNN_<name>_3rd_derivatives_001_150_claude.py`  (150 jerk features — GENERATED)

You hand-author ONLY files 1 and 2. Files 3 and 4 are produced by running
`python D:/Features/claude/_spec/build_derivatives.py "<folder>"`.

## CANONICAL EXAMPLE — read these first and mirror their structure exactly:
- D:/Features/claude/f01_crypto_beta_momentum/f01_crypto_beta_momentum_base_001_075_claude.py
- D:/Features/claude/f01_crypto_beta_momentum/f01_crypto_beta_momentum_base_076_150_claude.py

## HARD rules
- Each feature = standalone `def` taking pandas Series named EXACTLY as source columns,
  returning a pandas Series of equal length, ending with `.replace([np.inf, -np.inf], np.nan)`.
- NO `fillna(0)` anywhere. Preserve NaN warm-up. Only inf->nan at the return.
- Every feature body MUST reference >=1 of the family's domain primitives `_fNN_*`.
  If a feature doesn't naturally use one, anchor it: `+ _fNN_prim(<col>, w) * 0.0`.
- NO shared `_core()` generator. NO `formulas[i % N]` indexing. NO importlib/exec/
  globals()/setattr loops. Every function is a literal, fully-expanded def.
- Function name format (REQUIRED):
  `{short}_{fNN_full}_{calc}_{w}d_base_v{NNN}_signal`
  - short = 5-char code (e.g. f02 -> "f02cw"), fNN_full = full folder name,
  - calc = short descriptive id, w = integer window in days, NNN = 3-digit zero-padded.
  - file 1 uses v001..v075, file 2 uses v076..v150. No duplicate names.
- FEATURES MUST BE CONTINUOUS (the self-test asserts nunique > 50 on the warm-up tail).
  AVOID: rolling max/min of returns (sticky), sign rolling-means, 0/1 day-fraction means,
  integer event counts on short windows. PREFER: ratios, z-scores, normalized diffs,
  rolling std/skew/kurt, percentile ranks, ewm, vol-scaled values, smoothed series.
- Windows to use: mix of 5,10,21,42,63,84,126,189,252,315,378,504. For any rolling
  window > 21 use `closeadj` (never `close`) for price. Use raw `volume`; dollar-volume
  = `closeadj * volume`.
- Distinctness: no two features identical up to a window change is the spirit; vary the
  TRANSFORM, not just the window. Aim for genuinely different formulas — high signal, no dups.

## Input-column assignment (HARD, by family number)
- f01-f15 (OHLCV): inputs subset of {open, high, low, close, closeadj, volume}.
- f16-f25 (fundamentals): EVERY feature consumes >=1 of {revenue, netinc, fcf, equity,
  debt, assets, ebitda, capex, eps, sharesbas, shareswa, ncfo, ncfi, ncff, opinc, gp,
  grossmargin, cor, opex, ppnenet, cashneq, currentratio, de, sbcomp, workingcapital,
  retearn, intangibles, rnd}. (May ALSO use closeadj/volume as secondary, but a
  fundamental column must be present.)
- f26-f30 (metrics/ownership): EVERY feature consumes >=1 of {marketcap, ev, evebit,
  evebitda, pe, pb, ps, shrvalue, shrunits, totalvalue, percentoftotal, sf3a_shares,
  sf3a_value, sf3b_shares, sf3b_value, beta1y, beta5y}.

NOTE: feature INPUTS are pandas Series passed positionally; the self-test synthesizes
them. Fundamental/ownership series are quarterly in reality but the feature functions
operate on whatever Series they are given (daily synthetic in self-test) — that is fine.

## HEADER TEMPLATE (top of BOTH base files — copy, then add your domain primitives)
```python
import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (define 3-4, named _fNN_*) =====
def _fNN_<prim1>(...):
    ...
# ============ FEATURES 001-075 ============   <-- this exact marker line is REQUIRED
```
The literal marker line `# ============ FEATURES` MUST appear once, right before the
first feature def, in BOTH base files (the derivative builder splits on it).

## FOOTER TEMPLATE (bottom of BOTH base files — copy verbatim, fill the 3 <...> slots)
```python
_FEATURES = [
    # ... list all 75 functions in order ...
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
<FAM_UPPER>_REGISTRY_<001_075 or 076_150> = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = (<tuple of your _fNN_* primitive name strings>)
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK <filename without .py>: {n_features} features pass")
```

## BUILD & VERIFY checklist (you must complete ALL before finishing)
1. Write both base files. Run each: `python <basefile>.py` -> must print `OK ...: 75 features pass`.
2. Run: `python D:/Features/claude/_spec/build_derivatives.py "<your folder>"`
3. Run both generated derivative files -> each must print `OK ...: 150 features pass`.
4. Confirm derivative files are between 30KB and 75KB and base files <= 75KB.
5. Report PASS/counts. If any self-test fails, FIX the offending feature (usually make it
   continuous) and re-run until green. Do not leave failing files.
