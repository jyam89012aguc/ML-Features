import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
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

def f08_same_store_proxy_revenue_base_5d_v001_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_5d_v002_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 5d window."""
    res = _sma(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_5d_v003_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 5d window."""
    res = _sma(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_5d_v004_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 5d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_10d_v005_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_10d_v006_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 10d window."""
    res = _sma(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_10d_v007_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 10d window."""
    res = _sma(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_10d_v008_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 10d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_21d_v009_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_21d_v010_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 21d window."""
    res = _sma(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_21d_v011_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 21d window."""
    res = _sma(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_21d_v012_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 21d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_42d_v013_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_42d_v014_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 42d window."""
    res = _sma(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_42d_v015_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 42d window."""
    res = _sma(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_42d_v016_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 42d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_63d_v017_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_63d_v018_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 63d window."""
    res = _sma(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_63d_v019_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 63d window."""
    res = _sma(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_63d_v020_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 63d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_126d_v021_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_126d_v022_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 126d window."""
    res = _sma(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_126d_v023_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 126d window."""
    res = _sma(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_126d_v024_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 126d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_252d_v025_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_252d_v026_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 252d window."""
    res = _sma(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_252d_v027_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 252d window."""
    res = _sma(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_252d_v028_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 252d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_504d_v029_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_504d_v030_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 504d window."""
    res = _sma(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_504d_v031_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 504d window."""
    res = _sma(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_504d_v032_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 504d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_756d_v033_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_756d_v034_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 756d window."""
    res = _sma(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_756d_v035_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 756d window."""
    res = _sma(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_756d_v036_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 756d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_1008d_v037_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_1008d_v038_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 1008d window."""
    res = _sma(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_1008d_v039_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 1008d window."""
    res = _sma(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_1008d_v040_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 1008d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_base_1260d_v041_signal(revenue):
    """Moving average to smooth noise of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_base_1260d_v042_signal(receivables):
    """Moving average to smooth noise of Raw level of receivables over 1260d window."""
    res = _sma(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_base_1260d_v043_signal(deferredrev):
    """Moving average to smooth noise of Raw level of deferredrev over 1260d window."""
    res = _sma(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_base_1260d_v044_signal(revenue, receivables, deferredrev):
    """Moving average to smooth noise of Cash-realized organic growth proxy over 1260d window."""
    res = _sma(_ratio(revenue, receivables + deferredrev), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_z_5d_v045_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_z_5d_v046_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 5d window."""
    res = _z(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_z_5d_v047_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 5d window."""
    res = _z(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_z_5d_v048_signal(revenue, receivables, deferredrev):
    """Z-score for relative outlier detection of Cash-realized organic growth proxy over 5d window."""
    res = _z(_ratio(revenue, receivables + deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_z_10d_v049_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_z_10d_v050_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 10d window."""
    res = _z(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_z_10d_v051_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 10d window."""
    res = _z(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_z_10d_v052_signal(revenue, receivables, deferredrev):
    """Z-score for relative outlier detection of Cash-realized organic growth proxy over 10d window."""
    res = _z(_ratio(revenue, receivables + deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_z_21d_v053_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_z_21d_v054_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 21d window."""
    res = _z(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_z_21d_v055_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 21d window."""
    res = _z(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_z_21d_v056_signal(revenue, receivables, deferredrev):
    """Z-score for relative outlier detection of Cash-realized organic growth proxy over 21d window."""
    res = _z(_ratio(revenue, receivables + deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_z_42d_v057_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_z_42d_v058_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 42d window."""
    res = _z(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_z_42d_v059_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 42d window."""
    res = _z(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_z_42d_v060_signal(revenue, receivables, deferredrev):
    """Z-score for relative outlier detection of Cash-realized organic growth proxy over 42d window."""
    res = _z(_ratio(revenue, receivables + deferredrev), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_z_63d_v061_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_z_63d_v062_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 63d window."""
    res = _z(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_z_63d_v063_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 63d window."""
    res = _z(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_z_63d_v064_signal(revenue, receivables, deferredrev):
    """Z-score for relative outlier detection of Cash-realized organic growth proxy over 63d window."""
    res = _z(_ratio(revenue, receivables + deferredrev), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_z_126d_v065_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_z_126d_v066_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 126d window."""
    res = _z(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_z_126d_v067_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 126d window."""
    res = _z(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_z_126d_v068_signal(revenue, receivables, deferredrev):
    """Z-score for relative outlier detection of Cash-realized organic growth proxy over 126d window."""
    res = _z(_ratio(revenue, receivables + deferredrev), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_z_252d_v069_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_z_252d_v070_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 252d window."""
    res = _z(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_z_252d_v071_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 252d window."""
    res = _z(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_organic_momentum_z_252d_v072_signal(revenue, receivables, deferredrev):
    """Z-score for relative outlier detection of Cash-realized organic growth proxy over 252d window."""
    res = _z(_ratio(revenue, receivables + deferredrev), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_revenue_z_504d_v073_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_receivables_z_504d_v074_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 504d window."""
    res = _z(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_same_store_proxy_deferredrev_z_504d_v075_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 504d window."""
    res = _z(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f08_same_store_proxy_revenue_base_5d_v001_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_5d_v001_signal},    "f08_same_store_proxy_receivables_base_5d_v002_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_5d_v002_signal},    "f08_same_store_proxy_deferredrev_base_5d_v003_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_5d_v003_signal},    "f08_same_store_proxy_organic_momentum_base_5d_v004_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_5d_v004_signal},    "f08_same_store_proxy_revenue_base_10d_v005_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_10d_v005_signal},    "f08_same_store_proxy_receivables_base_10d_v006_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_10d_v006_signal},    "f08_same_store_proxy_deferredrev_base_10d_v007_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_10d_v007_signal},    "f08_same_store_proxy_organic_momentum_base_10d_v008_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_10d_v008_signal},    "f08_same_store_proxy_revenue_base_21d_v009_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_21d_v009_signal},    "f08_same_store_proxy_receivables_base_21d_v010_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_21d_v010_signal},    "f08_same_store_proxy_deferredrev_base_21d_v011_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_21d_v011_signal},    "f08_same_store_proxy_organic_momentum_base_21d_v012_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_21d_v012_signal},    "f08_same_store_proxy_revenue_base_42d_v013_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_42d_v013_signal},    "f08_same_store_proxy_receivables_base_42d_v014_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_42d_v014_signal},    "f08_same_store_proxy_deferredrev_base_42d_v015_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_42d_v015_signal},    "f08_same_store_proxy_organic_momentum_base_42d_v016_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_42d_v016_signal},    "f08_same_store_proxy_revenue_base_63d_v017_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_63d_v017_signal},    "f08_same_store_proxy_receivables_base_63d_v018_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_63d_v018_signal},    "f08_same_store_proxy_deferredrev_base_63d_v019_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_63d_v019_signal},    "f08_same_store_proxy_organic_momentum_base_63d_v020_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_63d_v020_signal},    "f08_same_store_proxy_revenue_base_126d_v021_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_126d_v021_signal},    "f08_same_store_proxy_receivables_base_126d_v022_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_126d_v022_signal},    "f08_same_store_proxy_deferredrev_base_126d_v023_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_126d_v023_signal},    "f08_same_store_proxy_organic_momentum_base_126d_v024_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_126d_v024_signal},    "f08_same_store_proxy_revenue_base_252d_v025_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_252d_v025_signal},    "f08_same_store_proxy_receivables_base_252d_v026_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_252d_v026_signal},    "f08_same_store_proxy_deferredrev_base_252d_v027_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_252d_v027_signal},    "f08_same_store_proxy_organic_momentum_base_252d_v028_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_252d_v028_signal},    "f08_same_store_proxy_revenue_base_504d_v029_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_504d_v029_signal},    "f08_same_store_proxy_receivables_base_504d_v030_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_504d_v030_signal},    "f08_same_store_proxy_deferredrev_base_504d_v031_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_504d_v031_signal},    "f08_same_store_proxy_organic_momentum_base_504d_v032_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_504d_v032_signal},    "f08_same_store_proxy_revenue_base_756d_v033_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_756d_v033_signal},    "f08_same_store_proxy_receivables_base_756d_v034_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_756d_v034_signal},    "f08_same_store_proxy_deferredrev_base_756d_v035_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_756d_v035_signal},    "f08_same_store_proxy_organic_momentum_base_756d_v036_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_756d_v036_signal},    "f08_same_store_proxy_revenue_base_1008d_v037_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_1008d_v037_signal},    "f08_same_store_proxy_receivables_base_1008d_v038_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_1008d_v038_signal},    "f08_same_store_proxy_deferredrev_base_1008d_v039_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_1008d_v039_signal},    "f08_same_store_proxy_organic_momentum_base_1008d_v040_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_1008d_v040_signal},    "f08_same_store_proxy_revenue_base_1260d_v041_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_base_1260d_v041_signal},    "f08_same_store_proxy_receivables_base_1260d_v042_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_base_1260d_v042_signal},    "f08_same_store_proxy_deferredrev_base_1260d_v043_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_base_1260d_v043_signal},    "f08_same_store_proxy_organic_momentum_base_1260d_v044_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_base_1260d_v044_signal},    "f08_same_store_proxy_revenue_z_5d_v045_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_z_5d_v045_signal},    "f08_same_store_proxy_receivables_z_5d_v046_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_z_5d_v046_signal},    "f08_same_store_proxy_deferredrev_z_5d_v047_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_z_5d_v047_signal},    "f08_same_store_proxy_organic_momentum_z_5d_v048_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_z_5d_v048_signal},    "f08_same_store_proxy_revenue_z_10d_v049_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_z_10d_v049_signal},    "f08_same_store_proxy_receivables_z_10d_v050_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_z_10d_v050_signal},    "f08_same_store_proxy_deferredrev_z_10d_v051_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_z_10d_v051_signal},    "f08_same_store_proxy_organic_momentum_z_10d_v052_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_z_10d_v052_signal},    "f08_same_store_proxy_revenue_z_21d_v053_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_z_21d_v053_signal},    "f08_same_store_proxy_receivables_z_21d_v054_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_z_21d_v054_signal},    "f08_same_store_proxy_deferredrev_z_21d_v055_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_z_21d_v055_signal},    "f08_same_store_proxy_organic_momentum_z_21d_v056_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_z_21d_v056_signal},    "f08_same_store_proxy_revenue_z_42d_v057_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_z_42d_v057_signal},    "f08_same_store_proxy_receivables_z_42d_v058_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_z_42d_v058_signal},    "f08_same_store_proxy_deferredrev_z_42d_v059_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_z_42d_v059_signal},    "f08_same_store_proxy_organic_momentum_z_42d_v060_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_z_42d_v060_signal},    "f08_same_store_proxy_revenue_z_63d_v061_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_z_63d_v061_signal},    "f08_same_store_proxy_receivables_z_63d_v062_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_z_63d_v062_signal},    "f08_same_store_proxy_deferredrev_z_63d_v063_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_z_63d_v063_signal},    "f08_same_store_proxy_organic_momentum_z_63d_v064_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_z_63d_v064_signal},    "f08_same_store_proxy_revenue_z_126d_v065_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_z_126d_v065_signal},    "f08_same_store_proxy_receivables_z_126d_v066_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_z_126d_v066_signal},    "f08_same_store_proxy_deferredrev_z_126d_v067_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_z_126d_v067_signal},    "f08_same_store_proxy_organic_momentum_z_126d_v068_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_z_126d_v068_signal},    "f08_same_store_proxy_revenue_z_252d_v069_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_z_252d_v069_signal},    "f08_same_store_proxy_receivables_z_252d_v070_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_z_252d_v070_signal},    "f08_same_store_proxy_deferredrev_z_252d_v071_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_z_252d_v071_signal},    "f08_same_store_proxy_organic_momentum_z_252d_v072_signal": {"inputs": [], "func": f08_same_store_proxy_organic_momentum_z_252d_v072_signal},    "f08_same_store_proxy_revenue_z_504d_v073_signal": {"inputs": [], "func": f08_same_store_proxy_revenue_z_504d_v073_signal},    "f08_same_store_proxy_receivables_z_504d_v074_signal": {"inputs": [], "func": f08_same_store_proxy_receivables_z_504d_v074_signal},    "f08_same_store_proxy_deferredrev_z_504d_v075_signal": {"inputs": [], "func": f08_same_store_proxy_deferredrev_z_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 08...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
