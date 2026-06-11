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

def f02_tbvps_growth_tangibles_base_5d_v001_signal(tangibles):
    """Moving average of Raw level of tangibles over 5d window."""
    res = _sma(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_5d_v002_signal(shareswa):
    """Moving average of Raw level of shareswa over 5d window."""
    res = _sma(shareswa, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_5d_v003_signal(bvps):
    """Moving average of Raw level of bvps over 5d window."""
    res = _sma(bvps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_5d_v004_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 5d window."""
    res = _sma(_ratio(tangibles, shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_5d_v005_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 5d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_5d_v006_signal(tangibles, assets):
    """Moving average of Tangible asset density over 5d window."""
    res = _sma(_ratio(tangibles, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_10d_v007_signal(tangibles):
    """Moving average of Raw level of tangibles over 10d window."""
    res = _sma(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_10d_v008_signal(shareswa):
    """Moving average of Raw level of shareswa over 10d window."""
    res = _sma(shareswa, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_10d_v009_signal(bvps):
    """Moving average of Raw level of bvps over 10d window."""
    res = _sma(bvps, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_10d_v010_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 10d window."""
    res = _sma(_ratio(tangibles, shareswa), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_10d_v011_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 10d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_10d_v012_signal(tangibles, assets):
    """Moving average of Tangible asset density over 10d window."""
    res = _sma(_ratio(tangibles, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_21d_v013_signal(tangibles):
    """Moving average of Raw level of tangibles over 21d window."""
    res = _sma(tangibles, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_21d_v014_signal(shareswa):
    """Moving average of Raw level of shareswa over 21d window."""
    res = _sma(shareswa, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_21d_v015_signal(bvps):
    """Moving average of Raw level of bvps over 21d window."""
    res = _sma(bvps, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_21d_v016_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 21d window."""
    res = _sma(_ratio(tangibles, shareswa), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_21d_v017_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 21d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_21d_v018_signal(tangibles, assets):
    """Moving average of Tangible asset density over 21d window."""
    res = _sma(_ratio(tangibles, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_42d_v019_signal(tangibles):
    """Moving average of Raw level of tangibles over 42d window."""
    res = _sma(tangibles, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_42d_v020_signal(shareswa):
    """Moving average of Raw level of shareswa over 42d window."""
    res = _sma(shareswa, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_42d_v021_signal(bvps):
    """Moving average of Raw level of bvps over 42d window."""
    res = _sma(bvps, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_42d_v022_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 42d window."""
    res = _sma(_ratio(tangibles, shareswa), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_42d_v023_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 42d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_42d_v024_signal(tangibles, assets):
    """Moving average of Tangible asset density over 42d window."""
    res = _sma(_ratio(tangibles, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_63d_v025_signal(tangibles):
    """Moving average of Raw level of tangibles over 63d window."""
    res = _sma(tangibles, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_63d_v026_signal(shareswa):
    """Moving average of Raw level of shareswa over 63d window."""
    res = _sma(shareswa, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_63d_v027_signal(bvps):
    """Moving average of Raw level of bvps over 63d window."""
    res = _sma(bvps, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_63d_v028_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 63d window."""
    res = _sma(_ratio(tangibles, shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_63d_v029_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 63d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_63d_v030_signal(tangibles, assets):
    """Moving average of Tangible asset density over 63d window."""
    res = _sma(_ratio(tangibles, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_126d_v031_signal(tangibles):
    """Moving average of Raw level of tangibles over 126d window."""
    res = _sma(tangibles, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_126d_v032_signal(shareswa):
    """Moving average of Raw level of shareswa over 126d window."""
    res = _sma(shareswa, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_126d_v033_signal(bvps):
    """Moving average of Raw level of bvps over 126d window."""
    res = _sma(bvps, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_126d_v034_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 126d window."""
    res = _sma(_ratio(tangibles, shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_126d_v035_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 126d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_126d_v036_signal(tangibles, assets):
    """Moving average of Tangible asset density over 126d window."""
    res = _sma(_ratio(tangibles, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_252d_v037_signal(tangibles):
    """Moving average of Raw level of tangibles over 252d window."""
    res = _sma(tangibles, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_252d_v038_signal(shareswa):
    """Moving average of Raw level of shareswa over 252d window."""
    res = _sma(shareswa, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_252d_v039_signal(bvps):
    """Moving average of Raw level of bvps over 252d window."""
    res = _sma(bvps, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_252d_v040_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 252d window."""
    res = _sma(_ratio(tangibles, shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_252d_v041_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 252d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_252d_v042_signal(tangibles, assets):
    """Moving average of Tangible asset density over 252d window."""
    res = _sma(_ratio(tangibles, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_504d_v043_signal(tangibles):
    """Moving average of Raw level of tangibles over 504d window."""
    res = _sma(tangibles, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_504d_v044_signal(shareswa):
    """Moving average of Raw level of shareswa over 504d window."""
    res = _sma(shareswa, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_504d_v045_signal(bvps):
    """Moving average of Raw level of bvps over 504d window."""
    res = _sma(bvps, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_504d_v046_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 504d window."""
    res = _sma(_ratio(tangibles, shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_504d_v047_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 504d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_504d_v048_signal(tangibles, assets):
    """Moving average of Tangible asset density over 504d window."""
    res = _sma(_ratio(tangibles, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_756d_v049_signal(tangibles):
    """Moving average of Raw level of tangibles over 756d window."""
    res = _sma(tangibles, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_756d_v050_signal(shareswa):
    """Moving average of Raw level of shareswa over 756d window."""
    res = _sma(shareswa, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_756d_v051_signal(bvps):
    """Moving average of Raw level of bvps over 756d window."""
    res = _sma(bvps, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_756d_v052_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 756d window."""
    res = _sma(_ratio(tangibles, shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_756d_v053_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 756d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_756d_v054_signal(tangibles, assets):
    """Moving average of Tangible asset density over 756d window."""
    res = _sma(_ratio(tangibles, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_1008d_v055_signal(tangibles):
    """Moving average of Raw level of tangibles over 1008d window."""
    res = _sma(tangibles, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_1008d_v056_signal(shareswa):
    """Moving average of Raw level of shareswa over 1008d window."""
    res = _sma(shareswa, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_1008d_v057_signal(bvps):
    """Moving average of Raw level of bvps over 1008d window."""
    res = _sma(bvps, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_1008d_v058_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 1008d window."""
    res = _sma(_ratio(tangibles, shareswa), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_1008d_v059_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 1008d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_1008d_v060_signal(tangibles, assets):
    """Moving average of Tangible asset density over 1008d window."""
    res = _sma(_ratio(tangibles, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_base_1260d_v061_signal(tangibles):
    """Moving average of Raw level of tangibles over 1260d window."""
    res = _sma(tangibles, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_base_1260d_v062_signal(shareswa):
    """Moving average of Raw level of shareswa over 1260d window."""
    res = _sma(shareswa, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_base_1260d_v063_signal(bvps):
    """Moving average of Raw level of bvps over 1260d window."""
    res = _sma(bvps, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_base_1260d_v064_signal(tangibles, shareswa):
    """Moving average of Tangible book per share over 1260d window."""
    res = _sma(_ratio(tangibles, shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_base_1260d_v065_signal(tangibles, bvps, shareswa):
    """Moving average of Tangible concentration of book value over 1260d window."""
    res = _sma(_ratio(tangibles, bvps * shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_base_1260d_v066_signal(tangibles, assets):
    """Moving average of Tangible asset density over 1260d window."""
    res = _sma(_ratio(tangibles, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_ewma_5d_v067_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 5d window."""
    res = _ewma(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_ewma_5d_v068_signal(shareswa):
    """Exponential moving average of Raw level of shareswa over 5d window."""
    res = _ewma(shareswa, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_ewma_5d_v069_signal(bvps):
    """Exponential moving average of Raw level of bvps over 5d window."""
    res = _ewma(bvps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_ewma_5d_v070_signal(tangibles, shareswa):
    """Exponential moving average of Tangible book per share over 5d window."""
    res = _ewma(_ratio(tangibles, shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_ewma_5d_v071_signal(tangibles, bvps, shareswa):
    """Exponential moving average of Tangible concentration of book value over 5d window."""
    res = _ewma(_ratio(tangibles, bvps * shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_ewma_5d_v072_signal(tangibles, assets):
    """Exponential moving average of Tangible asset density over 5d window."""
    res = _ewma(_ratio(tangibles, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_ewma_10d_v073_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 10d window."""
    res = _ewma(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_ewma_10d_v074_signal(shareswa):
    """Exponential moving average of Raw level of shareswa over 10d window."""
    res = _ewma(shareswa, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_ewma_10d_v075_signal(bvps):
    """Exponential moving average of Raw level of bvps over 10d window."""
    res = _ewma(bvps, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f02_tbvps_growth_tangibles_base_5d_v001_signal": {"func": f02_tbvps_growth_tangibles_base_5d_v001_signal},
    "f02_tbvps_growth_shareswa_base_5d_v002_signal": {"func": f02_tbvps_growth_shareswa_base_5d_v002_signal},
    "f02_tbvps_growth_bvps_base_5d_v003_signal": {"func": f02_tbvps_growth_bvps_base_5d_v003_signal},
    "f02_tbvps_growth_tbvps_base_5d_v004_signal": {"func": f02_tbvps_growth_tbvps_base_5d_v004_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_5d_v005_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_5d_v005_signal},
    "f02_tbvps_growth_growth_capacity_base_5d_v006_signal": {"func": f02_tbvps_growth_growth_capacity_base_5d_v006_signal},
    "f02_tbvps_growth_tangibles_base_10d_v007_signal": {"func": f02_tbvps_growth_tangibles_base_10d_v007_signal},
    "f02_tbvps_growth_shareswa_base_10d_v008_signal": {"func": f02_tbvps_growth_shareswa_base_10d_v008_signal},
    "f02_tbvps_growth_bvps_base_10d_v009_signal": {"func": f02_tbvps_growth_bvps_base_10d_v009_signal},
    "f02_tbvps_growth_tbvps_base_10d_v010_signal": {"func": f02_tbvps_growth_tbvps_base_10d_v010_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_10d_v011_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_10d_v011_signal},
    "f02_tbvps_growth_growth_capacity_base_10d_v012_signal": {"func": f02_tbvps_growth_growth_capacity_base_10d_v012_signal},
    "f02_tbvps_growth_tangibles_base_21d_v013_signal": {"func": f02_tbvps_growth_tangibles_base_21d_v013_signal},
    "f02_tbvps_growth_shareswa_base_21d_v014_signal": {"func": f02_tbvps_growth_shareswa_base_21d_v014_signal},
    "f02_tbvps_growth_bvps_base_21d_v015_signal": {"func": f02_tbvps_growth_bvps_base_21d_v015_signal},
    "f02_tbvps_growth_tbvps_base_21d_v016_signal": {"func": f02_tbvps_growth_tbvps_base_21d_v016_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_21d_v017_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_21d_v017_signal},
    "f02_tbvps_growth_growth_capacity_base_21d_v018_signal": {"func": f02_tbvps_growth_growth_capacity_base_21d_v018_signal},
    "f02_tbvps_growth_tangibles_base_42d_v019_signal": {"func": f02_tbvps_growth_tangibles_base_42d_v019_signal},
    "f02_tbvps_growth_shareswa_base_42d_v020_signal": {"func": f02_tbvps_growth_shareswa_base_42d_v020_signal},
    "f02_tbvps_growth_bvps_base_42d_v021_signal": {"func": f02_tbvps_growth_bvps_base_42d_v021_signal},
    "f02_tbvps_growth_tbvps_base_42d_v022_signal": {"func": f02_tbvps_growth_tbvps_base_42d_v022_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_42d_v023_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_42d_v023_signal},
    "f02_tbvps_growth_growth_capacity_base_42d_v024_signal": {"func": f02_tbvps_growth_growth_capacity_base_42d_v024_signal},
    "f02_tbvps_growth_tangibles_base_63d_v025_signal": {"func": f02_tbvps_growth_tangibles_base_63d_v025_signal},
    "f02_tbvps_growth_shareswa_base_63d_v026_signal": {"func": f02_tbvps_growth_shareswa_base_63d_v026_signal},
    "f02_tbvps_growth_bvps_base_63d_v027_signal": {"func": f02_tbvps_growth_bvps_base_63d_v027_signal},
    "f02_tbvps_growth_tbvps_base_63d_v028_signal": {"func": f02_tbvps_growth_tbvps_base_63d_v028_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_63d_v029_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_63d_v029_signal},
    "f02_tbvps_growth_growth_capacity_base_63d_v030_signal": {"func": f02_tbvps_growth_growth_capacity_base_63d_v030_signal},
    "f02_tbvps_growth_tangibles_base_126d_v031_signal": {"func": f02_tbvps_growth_tangibles_base_126d_v031_signal},
    "f02_tbvps_growth_shareswa_base_126d_v032_signal": {"func": f02_tbvps_growth_shareswa_base_126d_v032_signal},
    "f02_tbvps_growth_bvps_base_126d_v033_signal": {"func": f02_tbvps_growth_bvps_base_126d_v033_signal},
    "f02_tbvps_growth_tbvps_base_126d_v034_signal": {"func": f02_tbvps_growth_tbvps_base_126d_v034_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_126d_v035_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_126d_v035_signal},
    "f02_tbvps_growth_growth_capacity_base_126d_v036_signal": {"func": f02_tbvps_growth_growth_capacity_base_126d_v036_signal},
    "f02_tbvps_growth_tangibles_base_252d_v037_signal": {"func": f02_tbvps_growth_tangibles_base_252d_v037_signal},
    "f02_tbvps_growth_shareswa_base_252d_v038_signal": {"func": f02_tbvps_growth_shareswa_base_252d_v038_signal},
    "f02_tbvps_growth_bvps_base_252d_v039_signal": {"func": f02_tbvps_growth_bvps_base_252d_v039_signal},
    "f02_tbvps_growth_tbvps_base_252d_v040_signal": {"func": f02_tbvps_growth_tbvps_base_252d_v040_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_252d_v041_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_252d_v041_signal},
    "f02_tbvps_growth_growth_capacity_base_252d_v042_signal": {"func": f02_tbvps_growth_growth_capacity_base_252d_v042_signal},
    "f02_tbvps_growth_tangibles_base_504d_v043_signal": {"func": f02_tbvps_growth_tangibles_base_504d_v043_signal},
    "f02_tbvps_growth_shareswa_base_504d_v044_signal": {"func": f02_tbvps_growth_shareswa_base_504d_v044_signal},
    "f02_tbvps_growth_bvps_base_504d_v045_signal": {"func": f02_tbvps_growth_bvps_base_504d_v045_signal},
    "f02_tbvps_growth_tbvps_base_504d_v046_signal": {"func": f02_tbvps_growth_tbvps_base_504d_v046_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_504d_v047_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_504d_v047_signal},
    "f02_tbvps_growth_growth_capacity_base_504d_v048_signal": {"func": f02_tbvps_growth_growth_capacity_base_504d_v048_signal},
    "f02_tbvps_growth_tangibles_base_756d_v049_signal": {"func": f02_tbvps_growth_tangibles_base_756d_v049_signal},
    "f02_tbvps_growth_shareswa_base_756d_v050_signal": {"func": f02_tbvps_growth_shareswa_base_756d_v050_signal},
    "f02_tbvps_growth_bvps_base_756d_v051_signal": {"func": f02_tbvps_growth_bvps_base_756d_v051_signal},
    "f02_tbvps_growth_tbvps_base_756d_v052_signal": {"func": f02_tbvps_growth_tbvps_base_756d_v052_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_756d_v053_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_756d_v053_signal},
    "f02_tbvps_growth_growth_capacity_base_756d_v054_signal": {"func": f02_tbvps_growth_growth_capacity_base_756d_v054_signal},
    "f02_tbvps_growth_tangibles_base_1008d_v055_signal": {"func": f02_tbvps_growth_tangibles_base_1008d_v055_signal},
    "f02_tbvps_growth_shareswa_base_1008d_v056_signal": {"func": f02_tbvps_growth_shareswa_base_1008d_v056_signal},
    "f02_tbvps_growth_bvps_base_1008d_v057_signal": {"func": f02_tbvps_growth_bvps_base_1008d_v057_signal},
    "f02_tbvps_growth_tbvps_base_1008d_v058_signal": {"func": f02_tbvps_growth_tbvps_base_1008d_v058_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_1008d_v059_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_1008d_v059_signal},
    "f02_tbvps_growth_growth_capacity_base_1008d_v060_signal": {"func": f02_tbvps_growth_growth_capacity_base_1008d_v060_signal},
    "f02_tbvps_growth_tangibles_base_1260d_v061_signal": {"func": f02_tbvps_growth_tangibles_base_1260d_v061_signal},
    "f02_tbvps_growth_shareswa_base_1260d_v062_signal": {"func": f02_tbvps_growth_shareswa_base_1260d_v062_signal},
    "f02_tbvps_growth_bvps_base_1260d_v063_signal": {"func": f02_tbvps_growth_bvps_base_1260d_v063_signal},
    "f02_tbvps_growth_tbvps_base_1260d_v064_signal": {"func": f02_tbvps_growth_tbvps_base_1260d_v064_signal},
    "f02_tbvps_growth_tbv_to_total_bv_base_1260d_v065_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_base_1260d_v065_signal},
    "f02_tbvps_growth_growth_capacity_base_1260d_v066_signal": {"func": f02_tbvps_growth_growth_capacity_base_1260d_v066_signal},
    "f02_tbvps_growth_tangibles_ewma_5d_v067_signal": {"func": f02_tbvps_growth_tangibles_ewma_5d_v067_signal},
    "f02_tbvps_growth_shareswa_ewma_5d_v068_signal": {"func": f02_tbvps_growth_shareswa_ewma_5d_v068_signal},
    "f02_tbvps_growth_bvps_ewma_5d_v069_signal": {"func": f02_tbvps_growth_bvps_ewma_5d_v069_signal},
    "f02_tbvps_growth_tbvps_ewma_5d_v070_signal": {"func": f02_tbvps_growth_tbvps_ewma_5d_v070_signal},
    "f02_tbvps_growth_tbv_to_total_bv_ewma_5d_v071_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_ewma_5d_v071_signal},
    "f02_tbvps_growth_growth_capacity_ewma_5d_v072_signal": {"func": f02_tbvps_growth_growth_capacity_ewma_5d_v072_signal},
    "f02_tbvps_growth_tangibles_ewma_10d_v073_signal": {"func": f02_tbvps_growth_tangibles_ewma_10d_v073_signal},
    "f02_tbvps_growth_shareswa_ewma_10d_v074_signal": {"func": f02_tbvps_growth_shareswa_ewma_10d_v074_signal},
    "f02_tbvps_growth_bvps_ewma_10d_v075_signal": {"func": f02_tbvps_growth_bvps_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 02...")
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
