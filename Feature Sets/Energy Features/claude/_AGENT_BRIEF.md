# Agent brief — Energy feature family generator

You will produce **5 feature-family folders** for the Energy sector, each with
**exactly 4 files**, modeled after the existing folder
`D:\active_non audited features per AI\Feature Family 1 long (50 Features)\claude\f01_peak_and_crash\`.

## Output location
`D:\active_non audited features per AI\Energy Features\claude\f##_<slug>\`

## Energy-sector input notes
- `revenue` is commodity-linked: oil/gas/uranium volumes × prices for producers; throughput
  fees for midstream; service fees for OFS / drillers.
- `cor` = lifting / operating / drilling cost — gross margin reflects cycle position.
- `capex` is CYCLICAL and lumpy: drilling, well completion, LNG/midstream long-cycle projects.
- `ppnenet` = capitalized reserves / midstream pipeline / rig assets.
- `inventory` = crude oil + refined products inventory (refiners + integrated names).
- `deferredrev` = backlog for OFS / drillers / midstream contracted volumes.
- `debt` and `de` matter a lot — energy cycles produce distress and recovery.
- `intangibles` is small except for M&A targets; useful for consolidation signals.
- Margins (`grossmargin`, `ebitdamargin`, `netmargin`) are highly cyclical — durability is rare
  and is itself the signal.

## Naming
For family number `NN` (two digits) and slug `<slug>`:
- two-letter abbreviation `ab` (first letter of slug words, lowercase) used inside function names
- folder: `fNN_<slug>`
- files (exactly these names):
  - `fNN_<slug>_base_001_075_claude.py`
  - `fNN_<slug>_base_076_150_claude.py`
  - `fNN_<slug>_2nd_derivatives_001_150_claude.py`
  - `fNN_<slug>_3rd_derivatives_001_150_claude.py`

## Each file MUST follow this skeleton
```python
import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5

# ===== shared helpers =====
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

# In 2nd/3rd derivative files also add:
def _diff(s, n):
    return s.diff(periods=n)

def _slope_pct(s, w):
    return s.pct_change(periods=w)

def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

# In 3rd derivative files add:
def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)

def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)

# ===== folder domain primitives =====
def _fNN_<concept_1>(...): ...
def _fNN_<concept_2>(...): ...
def _fNN_<concept_3>(...): ...

# ===== features =====
def fNNab_fNN_<slug>_<concept>_<window>_<type>_v###_signal(<inputs>):
    result = ...   # MUST reference at least one of the _fNN_* domain primitives
    return result.replace([np.inf, -np.inf], np.nan)

# ... repeat for each feature ...

_FEATURES = [
    fNNab_..._v001_signal,
    fNNab_..._v002_signal,
    ...
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
FNN_<SLUG_UPPER>_REGISTRY_<FILE_SUFFIX> = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    # Synthetic fundamentals (positive, evolving) for any fundamental inputs your features use.
    # Pick values that yield non-degenerate distributions when smoothed/diffed.
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_fNN_<concept_1>", "_fNN_<concept_2>", "_fNN_<concept_3>")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == <EXPECTED>, n_features  # 75 for base files, 150 for derivative files
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK fNN_<slug>_<suffix>_claude: {n_features} features pass")
```

## Mandatory rules
1. **Function name pattern**: `fNNab_fNN_<slug>_<concept>_<window>_<type>_v###_signal` where:
   - `ab` is the family's two-letter abbreviation (e.g. f01 industrial_cycle_phase → `icp`).
   - `<type>` ∈ {`base`, `slope`, `jerk`}.
   - `<window>` is the rolling window (e.g. `21d`, `63d`, `252d`).
   - `v###` is a zero-padded 3-digit version: `v001`…`v075` (base 1), `v076`…`v150` (base 2),
     `v001`…`v150` (slope), `v001`…`v150` (jerk).
2. **EVERY feature body must reference at least one folder-specific primitive `_fNN_<concept>`**.
   The test asserts this; if missing, test fails.
3. **Every feature returns `series.replace([np.inf, -np.inf], np.nan)`** — never raw inf.
4. **Inputs must be a subset of the `cols` dict keys above** (closeadj, high, low, volume,
   revenue, ebitda, ebit, netinc, fcf, ncfo, capex, depamor, sgna, opex, gp, cor, rnd,
   assets, assetsc, assetsnc, liabilities, liabilitiesc, liabilitiesnc, equity, equityusd,
   debt, debtc, debtnc, cashneq, inventory, receivables, payables, deferredrev, workingcapital,
   ppnenet, intangibles, tangibles, invcap, retearn, sbcomp, sharesbas, shareswa, shareswadil,
   eps, epsdil, bvps, fcfps, sps, dps, marketcap, ev, pe, pb, ps, evebit, evebitda,
   grossmargin, ebitdamargin, netmargin, roa, roe, roic, ros, currentratio, de,
   payoutratio, divyield, assetturnover). Do NOT invent column names.
5. **No duplicate function names** within or across files. Each feature should differ from
   siblings by either concept, window, scaling, multiplier, EMA vs SMA, etc.
6. **Distribution requirements** (each feature must satisfy these on `y[504:]`):
   - `nunique() > 50` (i.e. the output must vary meaningfully — multiply by `closeadj` or another
     evolving series when the underlying ratio is too piecewise constant).
   - `std() > 0`.
   - `<50%` NaN fraction (for ≥80% of features).
7. **2nd derivative file**: each feature is a slope of a base concept over a window.
   The test domain_primitives list still contains the folder-level `_fNN_*` primitives — so each
   slope feature MUST call one of those primitives inside it (typically: `base = _fNN_concept(...)`;
   `result = _slope_pct(base, w)` or `_slope_diff_norm(base, w)`).
8. **3rd derivative file**: each feature is a jerk (second-derivative of a base concept) over a
   window — `result = _jerk(base, w)`. Same primitive-reference rule.
9. **Aliases at bottom of each file** following the model:
   - base_001_075: `FNN_<SLUG_UPPER>_REGISTRY_001_075 = REGISTRY`
   - base_076_150: `FNN_<SLUG_UPPER>_REGISTRY_076_150 = REGISTRY`
   - 2nd_derivatives:  `FNN_<SLUG_UPPER>_REGISTRY_SLOPE_001_150 = REGISTRY`
   - 3rd_derivatives:  `FNN_<SLUG_UPPER>_REGISTRY_JERK_001_150 = REGISTRY`
10. **Test n_features assertion**: `assert n_features == 75` for base files, `== 150` for
    derivative files.
11. **NAMING DISCRIMINATOR (CRITICAL — fixes a bug from prior runs)**: jerk-file function names
    MUST contain `_jerk` (e.g. `..._jerk_v###_signal`); slope-file function names MUST contain
    `_slope` (e.g. `..._slope_v###_signal`). Bare `_v###_signal` without `_slope_`/`_jerk_` in
    derivative files causes cross-file name collisions.
12. **NO WITHIN-FILE DUPLICATE BODIES**. Before declaring done, verify via:
    ```python
    import hashlib, inspect
    seen = set()
    for name, meta in mod.REGISTRY.items():
        body = "\n".join(l.strip() for l in inspect.getsource(meta["func"]).splitlines()
                        if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("def "))
        h = hashlib.sha1(body.encode()).hexdigest()
        assert h not in seen, f"DUP body in {name}"
        seen.add(h)
    ```
    Widen variation axes (primitive × window × transform × scaling × slope/jerk window) if any
    collisions appear.

## Authoring tips
- Vary windows: 5d, 10d, 21d, 42d, 63d, 126d, 189d, 252d, 378d, 504d.
- Vary transforms: rolling mean, rolling std, EMA, z-score, log, sign, quantile rank, ratio.
- Vary scaling: × closeadj, × volume, × dollar volume, ÷ marketcap, ÷ assets, ÷ revenue.
- Vary multipliers: cross another fundamental (e.g. capex × revenue growth).
- If your base ratio is bounded/discrete (e.g. a 0/1 indicator), MULTIPLY by an evolving series
  like `closeadj` or `_mean(closeadj * volume, 21)` to ensure `nunique() > 50`.
- Domain primitives should encode the family's core economic intuition (3 are typical).

## When in doubt
Mirror the structure of:
`D:\active_non audited features per AI\Feature Family 1 long (50 Features)\claude\f01_peak_and_crash\`
which has exactly this skeleton with 3 primitives `_f01_peak_level`, `_f01_drawdown_from_peak`,
`_f01_crash_intensity` and 75/75/150/150 features.
