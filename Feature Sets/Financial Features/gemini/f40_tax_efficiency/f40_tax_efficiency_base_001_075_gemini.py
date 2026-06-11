import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return _slope_pct(s, w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()

def f40_tax_efficiency_taxexp_base_5d_v001_signal(taxexp):
    """Moving average of Raw level of taxexp over 5d window."""
    res = _sma(taxexp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_5d_v002_signal(ebt):
    """Moving average of Raw level of ebt over 5d window."""
    res = _sma(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_5d_v003_signal(netinc):
    """Moving average of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_5d_v004_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 5d window."""
    res = _sma(_ratio(taxexp, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_10d_v005_signal(taxexp):
    """Moving average of Raw level of taxexp over 10d window."""
    res = _sma(taxexp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_10d_v006_signal(ebt):
    """Moving average of Raw level of ebt over 10d window."""
    res = _sma(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_10d_v007_signal(netinc):
    """Moving average of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_10d_v008_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 10d window."""
    res = _sma(_ratio(taxexp, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_21d_v009_signal(taxexp):
    """Moving average of Raw level of taxexp over 21d window."""
    res = _sma(taxexp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_21d_v010_signal(ebt):
    """Moving average of Raw level of ebt over 21d window."""
    res = _sma(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_21d_v011_signal(netinc):
    """Moving average of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_21d_v012_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 21d window."""
    res = _sma(_ratio(taxexp, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_42d_v013_signal(taxexp):
    """Moving average of Raw level of taxexp over 42d window."""
    res = _sma(taxexp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_42d_v014_signal(ebt):
    """Moving average of Raw level of ebt over 42d window."""
    res = _sma(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_42d_v015_signal(netinc):
    """Moving average of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_42d_v016_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 42d window."""
    res = _sma(_ratio(taxexp, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_63d_v017_signal(taxexp):
    """Moving average of Raw level of taxexp over 63d window."""
    res = _sma(taxexp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_63d_v018_signal(ebt):
    """Moving average of Raw level of ebt over 63d window."""
    res = _sma(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_63d_v019_signal(netinc):
    """Moving average of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_63d_v020_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 63d window."""
    res = _sma(_ratio(taxexp, ebt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_126d_v021_signal(taxexp):
    """Moving average of Raw level of taxexp over 126d window."""
    res = _sma(taxexp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_126d_v022_signal(ebt):
    """Moving average of Raw level of ebt over 126d window."""
    res = _sma(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_126d_v023_signal(netinc):
    """Moving average of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_126d_v024_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 126d window."""
    res = _sma(_ratio(taxexp, ebt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_252d_v025_signal(taxexp):
    """Moving average of Raw level of taxexp over 252d window."""
    res = _sma(taxexp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_252d_v026_signal(ebt):
    """Moving average of Raw level of ebt over 252d window."""
    res = _sma(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_252d_v027_signal(netinc):
    """Moving average of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_252d_v028_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 252d window."""
    res = _sma(_ratio(taxexp, ebt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_504d_v029_signal(taxexp):
    """Moving average of Raw level of taxexp over 504d window."""
    res = _sma(taxexp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_504d_v030_signal(ebt):
    """Moving average of Raw level of ebt over 504d window."""
    res = _sma(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_504d_v031_signal(netinc):
    """Moving average of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_504d_v032_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 504d window."""
    res = _sma(_ratio(taxexp, ebt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_756d_v033_signal(taxexp):
    """Moving average of Raw level of taxexp over 756d window."""
    res = _sma(taxexp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_756d_v034_signal(ebt):
    """Moving average of Raw level of ebt over 756d window."""
    res = _sma(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_756d_v035_signal(netinc):
    """Moving average of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_756d_v036_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 756d window."""
    res = _sma(_ratio(taxexp, ebt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_1008d_v037_signal(taxexp):
    """Moving average of Raw level of taxexp over 1008d window."""
    res = _sma(taxexp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_1008d_v038_signal(ebt):
    """Moving average of Raw level of ebt over 1008d window."""
    res = _sma(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_1008d_v039_signal(netinc):
    """Moving average of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_1008d_v040_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 1008d window."""
    res = _sma(_ratio(taxexp, ebt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_base_1260d_v041_signal(taxexp):
    """Moving average of Raw level of taxexp over 1260d window."""
    res = _sma(taxexp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_base_1260d_v042_signal(ebt):
    """Moving average of Raw level of ebt over 1260d window."""
    res = _sma(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_base_1260d_v043_signal(netinc):
    """Moving average of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_base_1260d_v044_signal(taxexp, ebt):
    """Moving average of Tax load percentage over 1260d window."""
    res = _sma(_ratio(taxexp, ebt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_ewma_5d_v045_signal(taxexp):
    """Exponential moving average of Raw level of taxexp over 5d window."""
    res = _ewma(taxexp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_ewma_5d_v046_signal(ebt):
    """Exponential moving average of Raw level of ebt over 5d window."""
    res = _ewma(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_ewma_5d_v047_signal(netinc):
    """Exponential moving average of Raw level of netinc over 5d window."""
    res = _ewma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_ewma_5d_v048_signal(taxexp, ebt):
    """Exponential moving average of Tax load percentage over 5d window."""
    res = _ewma(_ratio(taxexp, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_ewma_10d_v049_signal(taxexp):
    """Exponential moving average of Raw level of taxexp over 10d window."""
    res = _ewma(taxexp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_ewma_10d_v050_signal(ebt):
    """Exponential moving average of Raw level of ebt over 10d window."""
    res = _ewma(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_ewma_10d_v051_signal(netinc):
    """Exponential moving average of Raw level of netinc over 10d window."""
    res = _ewma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_ewma_10d_v052_signal(taxexp, ebt):
    """Exponential moving average of Tax load percentage over 10d window."""
    res = _ewma(_ratio(taxexp, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_ewma_21d_v053_signal(taxexp):
    """Exponential moving average of Raw level of taxexp over 21d window."""
    res = _ewma(taxexp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_ewma_21d_v054_signal(ebt):
    """Exponential moving average of Raw level of ebt over 21d window."""
    res = _ewma(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_ewma_21d_v055_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_ewma_21d_v056_signal(taxexp, ebt):
    """Exponential moving average of Tax load percentage over 21d window."""
    res = _ewma(_ratio(taxexp, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_ewma_42d_v057_signal(taxexp):
    """Exponential moving average of Raw level of taxexp over 42d window."""
    res = _ewma(taxexp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_ewma_42d_v058_signal(ebt):
    """Exponential moving average of Raw level of ebt over 42d window."""
    res = _ewma(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_ewma_42d_v059_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_ewma_42d_v060_signal(taxexp, ebt):
    """Exponential moving average of Tax load percentage over 42d window."""
    res = _ewma(_ratio(taxexp, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_ewma_63d_v061_signal(taxexp):
    """Exponential moving average of Raw level of taxexp over 63d window."""
    res = _ewma(taxexp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_ewma_63d_v062_signal(ebt):
    """Exponential moving average of Raw level of ebt over 63d window."""
    res = _ewma(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_ewma_63d_v063_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_ewma_63d_v064_signal(taxexp, ebt):
    """Exponential moving average of Tax load percentage over 63d window."""
    res = _ewma(_ratio(taxexp, ebt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_ewma_126d_v065_signal(taxexp):
    """Exponential moving average of Raw level of taxexp over 126d window."""
    res = _ewma(taxexp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_ewma_126d_v066_signal(ebt):
    """Exponential moving average of Raw level of ebt over 126d window."""
    res = _ewma(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_ewma_126d_v067_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_ewma_126d_v068_signal(taxexp, ebt):
    """Exponential moving average of Tax load percentage over 126d window."""
    res = _ewma(_ratio(taxexp, ebt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_ewma_252d_v069_signal(taxexp):
    """Exponential moving average of Raw level of taxexp over 252d window."""
    res = _ewma(taxexp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_ewma_252d_v070_signal(ebt):
    """Exponential moving average of Raw level of ebt over 252d window."""
    res = _ewma(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_ewma_252d_v071_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_tax_load_ewma_252d_v072_signal(taxexp, ebt):
    """Exponential moving average of Tax load percentage over 252d window."""
    res = _ewma(_ratio(taxexp, ebt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_taxexp_ewma_504d_v073_signal(taxexp):
    """Exponential moving average of Raw level of taxexp over 504d window."""
    res = _ewma(taxexp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_ebt_ewma_504d_v074_signal(ebt):
    """Exponential moving average of Raw level of ebt over 504d window."""
    res = _ewma(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_tax_efficiency_netinc_ewma_504d_v075_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f40_tax_efficiency_taxexp_base_5d_v001_signal": {"func": f40_tax_efficiency_taxexp_base_5d_v001_signal},
    "f40_tax_efficiency_ebt_base_5d_v002_signal": {"func": f40_tax_efficiency_ebt_base_5d_v002_signal},
    "f40_tax_efficiency_netinc_base_5d_v003_signal": {"func": f40_tax_efficiency_netinc_base_5d_v003_signal},
    "f40_tax_efficiency_tax_load_base_5d_v004_signal": {"func": f40_tax_efficiency_tax_load_base_5d_v004_signal},
    "f40_tax_efficiency_taxexp_base_10d_v005_signal": {"func": f40_tax_efficiency_taxexp_base_10d_v005_signal},
    "f40_tax_efficiency_ebt_base_10d_v006_signal": {"func": f40_tax_efficiency_ebt_base_10d_v006_signal},
    "f40_tax_efficiency_netinc_base_10d_v007_signal": {"func": f40_tax_efficiency_netinc_base_10d_v007_signal},
    "f40_tax_efficiency_tax_load_base_10d_v008_signal": {"func": f40_tax_efficiency_tax_load_base_10d_v008_signal},
    "f40_tax_efficiency_taxexp_base_21d_v009_signal": {"func": f40_tax_efficiency_taxexp_base_21d_v009_signal},
    "f40_tax_efficiency_ebt_base_21d_v010_signal": {"func": f40_tax_efficiency_ebt_base_21d_v010_signal},
    "f40_tax_efficiency_netinc_base_21d_v011_signal": {"func": f40_tax_efficiency_netinc_base_21d_v011_signal},
    "f40_tax_efficiency_tax_load_base_21d_v012_signal": {"func": f40_tax_efficiency_tax_load_base_21d_v012_signal},
    "f40_tax_efficiency_taxexp_base_42d_v013_signal": {"func": f40_tax_efficiency_taxexp_base_42d_v013_signal},
    "f40_tax_efficiency_ebt_base_42d_v014_signal": {"func": f40_tax_efficiency_ebt_base_42d_v014_signal},
    "f40_tax_efficiency_netinc_base_42d_v015_signal": {"func": f40_tax_efficiency_netinc_base_42d_v015_signal},
    "f40_tax_efficiency_tax_load_base_42d_v016_signal": {"func": f40_tax_efficiency_tax_load_base_42d_v016_signal},
    "f40_tax_efficiency_taxexp_base_63d_v017_signal": {"func": f40_tax_efficiency_taxexp_base_63d_v017_signal},
    "f40_tax_efficiency_ebt_base_63d_v018_signal": {"func": f40_tax_efficiency_ebt_base_63d_v018_signal},
    "f40_tax_efficiency_netinc_base_63d_v019_signal": {"func": f40_tax_efficiency_netinc_base_63d_v019_signal},
    "f40_tax_efficiency_tax_load_base_63d_v020_signal": {"func": f40_tax_efficiency_tax_load_base_63d_v020_signal},
    "f40_tax_efficiency_taxexp_base_126d_v021_signal": {"func": f40_tax_efficiency_taxexp_base_126d_v021_signal},
    "f40_tax_efficiency_ebt_base_126d_v022_signal": {"func": f40_tax_efficiency_ebt_base_126d_v022_signal},
    "f40_tax_efficiency_netinc_base_126d_v023_signal": {"func": f40_tax_efficiency_netinc_base_126d_v023_signal},
    "f40_tax_efficiency_tax_load_base_126d_v024_signal": {"func": f40_tax_efficiency_tax_load_base_126d_v024_signal},
    "f40_tax_efficiency_taxexp_base_252d_v025_signal": {"func": f40_tax_efficiency_taxexp_base_252d_v025_signal},
    "f40_tax_efficiency_ebt_base_252d_v026_signal": {"func": f40_tax_efficiency_ebt_base_252d_v026_signal},
    "f40_tax_efficiency_netinc_base_252d_v027_signal": {"func": f40_tax_efficiency_netinc_base_252d_v027_signal},
    "f40_tax_efficiency_tax_load_base_252d_v028_signal": {"func": f40_tax_efficiency_tax_load_base_252d_v028_signal},
    "f40_tax_efficiency_taxexp_base_504d_v029_signal": {"func": f40_tax_efficiency_taxexp_base_504d_v029_signal},
    "f40_tax_efficiency_ebt_base_504d_v030_signal": {"func": f40_tax_efficiency_ebt_base_504d_v030_signal},
    "f40_tax_efficiency_netinc_base_504d_v031_signal": {"func": f40_tax_efficiency_netinc_base_504d_v031_signal},
    "f40_tax_efficiency_tax_load_base_504d_v032_signal": {"func": f40_tax_efficiency_tax_load_base_504d_v032_signal},
    "f40_tax_efficiency_taxexp_base_756d_v033_signal": {"func": f40_tax_efficiency_taxexp_base_756d_v033_signal},
    "f40_tax_efficiency_ebt_base_756d_v034_signal": {"func": f40_tax_efficiency_ebt_base_756d_v034_signal},
    "f40_tax_efficiency_netinc_base_756d_v035_signal": {"func": f40_tax_efficiency_netinc_base_756d_v035_signal},
    "f40_tax_efficiency_tax_load_base_756d_v036_signal": {"func": f40_tax_efficiency_tax_load_base_756d_v036_signal},
    "f40_tax_efficiency_taxexp_base_1008d_v037_signal": {"func": f40_tax_efficiency_taxexp_base_1008d_v037_signal},
    "f40_tax_efficiency_ebt_base_1008d_v038_signal": {"func": f40_tax_efficiency_ebt_base_1008d_v038_signal},
    "f40_tax_efficiency_netinc_base_1008d_v039_signal": {"func": f40_tax_efficiency_netinc_base_1008d_v039_signal},
    "f40_tax_efficiency_tax_load_base_1008d_v040_signal": {"func": f40_tax_efficiency_tax_load_base_1008d_v040_signal},
    "f40_tax_efficiency_taxexp_base_1260d_v041_signal": {"func": f40_tax_efficiency_taxexp_base_1260d_v041_signal},
    "f40_tax_efficiency_ebt_base_1260d_v042_signal": {"func": f40_tax_efficiency_ebt_base_1260d_v042_signal},
    "f40_tax_efficiency_netinc_base_1260d_v043_signal": {"func": f40_tax_efficiency_netinc_base_1260d_v043_signal},
    "f40_tax_efficiency_tax_load_base_1260d_v044_signal": {"func": f40_tax_efficiency_tax_load_base_1260d_v044_signal},
    "f40_tax_efficiency_taxexp_ewma_5d_v045_signal": {"func": f40_tax_efficiency_taxexp_ewma_5d_v045_signal},
    "f40_tax_efficiency_ebt_ewma_5d_v046_signal": {"func": f40_tax_efficiency_ebt_ewma_5d_v046_signal},
    "f40_tax_efficiency_netinc_ewma_5d_v047_signal": {"func": f40_tax_efficiency_netinc_ewma_5d_v047_signal},
    "f40_tax_efficiency_tax_load_ewma_5d_v048_signal": {"func": f40_tax_efficiency_tax_load_ewma_5d_v048_signal},
    "f40_tax_efficiency_taxexp_ewma_10d_v049_signal": {"func": f40_tax_efficiency_taxexp_ewma_10d_v049_signal},
    "f40_tax_efficiency_ebt_ewma_10d_v050_signal": {"func": f40_tax_efficiency_ebt_ewma_10d_v050_signal},
    "f40_tax_efficiency_netinc_ewma_10d_v051_signal": {"func": f40_tax_efficiency_netinc_ewma_10d_v051_signal},
    "f40_tax_efficiency_tax_load_ewma_10d_v052_signal": {"func": f40_tax_efficiency_tax_load_ewma_10d_v052_signal},
    "f40_tax_efficiency_taxexp_ewma_21d_v053_signal": {"func": f40_tax_efficiency_taxexp_ewma_21d_v053_signal},
    "f40_tax_efficiency_ebt_ewma_21d_v054_signal": {"func": f40_tax_efficiency_ebt_ewma_21d_v054_signal},
    "f40_tax_efficiency_netinc_ewma_21d_v055_signal": {"func": f40_tax_efficiency_netinc_ewma_21d_v055_signal},
    "f40_tax_efficiency_tax_load_ewma_21d_v056_signal": {"func": f40_tax_efficiency_tax_load_ewma_21d_v056_signal},
    "f40_tax_efficiency_taxexp_ewma_42d_v057_signal": {"func": f40_tax_efficiency_taxexp_ewma_42d_v057_signal},
    "f40_tax_efficiency_ebt_ewma_42d_v058_signal": {"func": f40_tax_efficiency_ebt_ewma_42d_v058_signal},
    "f40_tax_efficiency_netinc_ewma_42d_v059_signal": {"func": f40_tax_efficiency_netinc_ewma_42d_v059_signal},
    "f40_tax_efficiency_tax_load_ewma_42d_v060_signal": {"func": f40_tax_efficiency_tax_load_ewma_42d_v060_signal},
    "f40_tax_efficiency_taxexp_ewma_63d_v061_signal": {"func": f40_tax_efficiency_taxexp_ewma_63d_v061_signal},
    "f40_tax_efficiency_ebt_ewma_63d_v062_signal": {"func": f40_tax_efficiency_ebt_ewma_63d_v062_signal},
    "f40_tax_efficiency_netinc_ewma_63d_v063_signal": {"func": f40_tax_efficiency_netinc_ewma_63d_v063_signal},
    "f40_tax_efficiency_tax_load_ewma_63d_v064_signal": {"func": f40_tax_efficiency_tax_load_ewma_63d_v064_signal},
    "f40_tax_efficiency_taxexp_ewma_126d_v065_signal": {"func": f40_tax_efficiency_taxexp_ewma_126d_v065_signal},
    "f40_tax_efficiency_ebt_ewma_126d_v066_signal": {"func": f40_tax_efficiency_ebt_ewma_126d_v066_signal},
    "f40_tax_efficiency_netinc_ewma_126d_v067_signal": {"func": f40_tax_efficiency_netinc_ewma_126d_v067_signal},
    "f40_tax_efficiency_tax_load_ewma_126d_v068_signal": {"func": f40_tax_efficiency_tax_load_ewma_126d_v068_signal},
    "f40_tax_efficiency_taxexp_ewma_252d_v069_signal": {"func": f40_tax_efficiency_taxexp_ewma_252d_v069_signal},
    "f40_tax_efficiency_ebt_ewma_252d_v070_signal": {"func": f40_tax_efficiency_ebt_ewma_252d_v070_signal},
    "f40_tax_efficiency_netinc_ewma_252d_v071_signal": {"func": f40_tax_efficiency_netinc_ewma_252d_v071_signal},
    "f40_tax_efficiency_tax_load_ewma_252d_v072_signal": {"func": f40_tax_efficiency_tax_load_ewma_252d_v072_signal},
    "f40_tax_efficiency_taxexp_ewma_504d_v073_signal": {"func": f40_tax_efficiency_taxexp_ewma_504d_v073_signal},
    "f40_tax_efficiency_ebt_ewma_504d_v074_signal": {"func": f40_tax_efficiency_ebt_ewma_504d_v074_signal},
    "f40_tax_efficiency_netinc_ewma_504d_v075_signal": {"func": f40_tax_efficiency_netinc_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 40...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
