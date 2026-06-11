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

def f11_thrift_alpha_tangibles_base_5d_v001_signal(tangibles):
    """Moving average of Raw level of tangibles over 5d window."""
    res = _sma(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_5d_v002_signal(marketcap):
    """Moving average of Raw level of marketcap over 5d window."""
    res = _sma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_5d_v003_signal(pb):
    """Moving average of Raw level of pb over 5d window."""
    res = _sma(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_5d_v004_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 5d window."""
    res = _sma(_ratio(tangibles, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_10d_v005_signal(tangibles):
    """Moving average of Raw level of tangibles over 10d window."""
    res = _sma(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_10d_v006_signal(marketcap):
    """Moving average of Raw level of marketcap over 10d window."""
    res = _sma(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_10d_v007_signal(pb):
    """Moving average of Raw level of pb over 10d window."""
    res = _sma(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_10d_v008_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 10d window."""
    res = _sma(_ratio(tangibles, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_21d_v009_signal(tangibles):
    """Moving average of Raw level of tangibles over 21d window."""
    res = _sma(tangibles, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_21d_v010_signal(marketcap):
    """Moving average of Raw level of marketcap over 21d window."""
    res = _sma(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_21d_v011_signal(pb):
    """Moving average of Raw level of pb over 21d window."""
    res = _sma(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_21d_v012_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 21d window."""
    res = _sma(_ratio(tangibles, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_42d_v013_signal(tangibles):
    """Moving average of Raw level of tangibles over 42d window."""
    res = _sma(tangibles, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_42d_v014_signal(marketcap):
    """Moving average of Raw level of marketcap over 42d window."""
    res = _sma(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_42d_v015_signal(pb):
    """Moving average of Raw level of pb over 42d window."""
    res = _sma(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_42d_v016_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 42d window."""
    res = _sma(_ratio(tangibles, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_63d_v017_signal(tangibles):
    """Moving average of Raw level of tangibles over 63d window."""
    res = _sma(tangibles, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_63d_v018_signal(marketcap):
    """Moving average of Raw level of marketcap over 63d window."""
    res = _sma(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_63d_v019_signal(pb):
    """Moving average of Raw level of pb over 63d window."""
    res = _sma(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_63d_v020_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 63d window."""
    res = _sma(_ratio(tangibles, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_126d_v021_signal(tangibles):
    """Moving average of Raw level of tangibles over 126d window."""
    res = _sma(tangibles, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_126d_v022_signal(marketcap):
    """Moving average of Raw level of marketcap over 126d window."""
    res = _sma(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_126d_v023_signal(pb):
    """Moving average of Raw level of pb over 126d window."""
    res = _sma(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_126d_v024_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 126d window."""
    res = _sma(_ratio(tangibles, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_252d_v025_signal(tangibles):
    """Moving average of Raw level of tangibles over 252d window."""
    res = _sma(tangibles, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_252d_v026_signal(marketcap):
    """Moving average of Raw level of marketcap over 252d window."""
    res = _sma(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_252d_v027_signal(pb):
    """Moving average of Raw level of pb over 252d window."""
    res = _sma(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_252d_v028_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 252d window."""
    res = _sma(_ratio(tangibles, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_504d_v029_signal(tangibles):
    """Moving average of Raw level of tangibles over 504d window."""
    res = _sma(tangibles, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_504d_v030_signal(marketcap):
    """Moving average of Raw level of marketcap over 504d window."""
    res = _sma(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_504d_v031_signal(pb):
    """Moving average of Raw level of pb over 504d window."""
    res = _sma(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_504d_v032_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 504d window."""
    res = _sma(_ratio(tangibles, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_756d_v033_signal(tangibles):
    """Moving average of Raw level of tangibles over 756d window."""
    res = _sma(tangibles, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_756d_v034_signal(marketcap):
    """Moving average of Raw level of marketcap over 756d window."""
    res = _sma(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_756d_v035_signal(pb):
    """Moving average of Raw level of pb over 756d window."""
    res = _sma(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_756d_v036_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 756d window."""
    res = _sma(_ratio(tangibles, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_1008d_v037_signal(tangibles):
    """Moving average of Raw level of tangibles over 1008d window."""
    res = _sma(tangibles, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_1008d_v038_signal(marketcap):
    """Moving average of Raw level of marketcap over 1008d window."""
    res = _sma(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_1008d_v039_signal(pb):
    """Moving average of Raw level of pb over 1008d window."""
    res = _sma(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_1008d_v040_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 1008d window."""
    res = _sma(_ratio(tangibles, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_base_1260d_v041_signal(tangibles):
    """Moving average of Raw level of tangibles over 1260d window."""
    res = _sma(tangibles, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_base_1260d_v042_signal(marketcap):
    """Moving average of Raw level of marketcap over 1260d window."""
    res = _sma(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_base_1260d_v043_signal(pb):
    """Moving average of Raw level of pb over 1260d window."""
    res = _sma(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_base_1260d_v044_signal(tangibles, marketcap):
    """Moving average of Tangible assets per market dollar over 1260d window."""
    res = _sma(_ratio(tangibles, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_5d_v045_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 5d window."""
    res = _ewma(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_5d_v046_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 5d window."""
    res = _ewma(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_5d_v047_signal(pb):
    """Exponential moving average of Raw level of pb over 5d window."""
    res = _ewma(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_5d_v048_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 5d window."""
    res = _ewma(_ratio(tangibles, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_10d_v049_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 10d window."""
    res = _ewma(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_10d_v050_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 10d window."""
    res = _ewma(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_10d_v051_signal(pb):
    """Exponential moving average of Raw level of pb over 10d window."""
    res = _ewma(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_10d_v052_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 10d window."""
    res = _ewma(_ratio(tangibles, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_21d_v053_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 21d window."""
    res = _ewma(tangibles, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_21d_v054_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 21d window."""
    res = _ewma(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_21d_v055_signal(pb):
    """Exponential moving average of Raw level of pb over 21d window."""
    res = _ewma(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_21d_v056_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 21d window."""
    res = _ewma(_ratio(tangibles, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_42d_v057_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 42d window."""
    res = _ewma(tangibles, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_42d_v058_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 42d window."""
    res = _ewma(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_42d_v059_signal(pb):
    """Exponential moving average of Raw level of pb over 42d window."""
    res = _ewma(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_42d_v060_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 42d window."""
    res = _ewma(_ratio(tangibles, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_63d_v061_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 63d window."""
    res = _ewma(tangibles, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_63d_v062_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 63d window."""
    res = _ewma(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_63d_v063_signal(pb):
    """Exponential moving average of Raw level of pb over 63d window."""
    res = _ewma(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_63d_v064_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 63d window."""
    res = _ewma(_ratio(tangibles, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_126d_v065_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 126d window."""
    res = _ewma(tangibles, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_126d_v066_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 126d window."""
    res = _ewma(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_126d_v067_signal(pb):
    """Exponential moving average of Raw level of pb over 126d window."""
    res = _ewma(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_126d_v068_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 126d window."""
    res = _ewma(_ratio(tangibles, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_252d_v069_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 252d window."""
    res = _ewma(tangibles, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_252d_v070_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 252d window."""
    res = _ewma(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_252d_v071_signal(pb):
    """Exponential moving average of Raw level of pb over 252d window."""
    res = _ewma(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangible_yield_ewma_252d_v072_signal(tangibles, marketcap):
    """Exponential moving average of Tangible assets per market dollar over 252d window."""
    res = _ewma(_ratio(tangibles, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_tangibles_ewma_504d_v073_signal(tangibles):
    """Exponential moving average of Raw level of tangibles over 504d window."""
    res = _ewma(tangibles, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_marketcap_ewma_504d_v074_signal(marketcap):
    """Exponential moving average of Raw level of marketcap over 504d window."""
    res = _ewma(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f11_thrift_alpha_pb_ewma_504d_v075_signal(pb):
    """Exponential moving average of Raw level of pb over 504d window."""
    res = _ewma(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f11_thrift_alpha_tangibles_base_5d_v001_signal": {"func": f11_thrift_alpha_tangibles_base_5d_v001_signal},
    "f11_thrift_alpha_marketcap_base_5d_v002_signal": {"func": f11_thrift_alpha_marketcap_base_5d_v002_signal},
    "f11_thrift_alpha_pb_base_5d_v003_signal": {"func": f11_thrift_alpha_pb_base_5d_v003_signal},
    "f11_thrift_alpha_tangible_yield_base_5d_v004_signal": {"func": f11_thrift_alpha_tangible_yield_base_5d_v004_signal},
    "f11_thrift_alpha_tangibles_base_10d_v005_signal": {"func": f11_thrift_alpha_tangibles_base_10d_v005_signal},
    "f11_thrift_alpha_marketcap_base_10d_v006_signal": {"func": f11_thrift_alpha_marketcap_base_10d_v006_signal},
    "f11_thrift_alpha_pb_base_10d_v007_signal": {"func": f11_thrift_alpha_pb_base_10d_v007_signal},
    "f11_thrift_alpha_tangible_yield_base_10d_v008_signal": {"func": f11_thrift_alpha_tangible_yield_base_10d_v008_signal},
    "f11_thrift_alpha_tangibles_base_21d_v009_signal": {"func": f11_thrift_alpha_tangibles_base_21d_v009_signal},
    "f11_thrift_alpha_marketcap_base_21d_v010_signal": {"func": f11_thrift_alpha_marketcap_base_21d_v010_signal},
    "f11_thrift_alpha_pb_base_21d_v011_signal": {"func": f11_thrift_alpha_pb_base_21d_v011_signal},
    "f11_thrift_alpha_tangible_yield_base_21d_v012_signal": {"func": f11_thrift_alpha_tangible_yield_base_21d_v012_signal},
    "f11_thrift_alpha_tangibles_base_42d_v013_signal": {"func": f11_thrift_alpha_tangibles_base_42d_v013_signal},
    "f11_thrift_alpha_marketcap_base_42d_v014_signal": {"func": f11_thrift_alpha_marketcap_base_42d_v014_signal},
    "f11_thrift_alpha_pb_base_42d_v015_signal": {"func": f11_thrift_alpha_pb_base_42d_v015_signal},
    "f11_thrift_alpha_tangible_yield_base_42d_v016_signal": {"func": f11_thrift_alpha_tangible_yield_base_42d_v016_signal},
    "f11_thrift_alpha_tangibles_base_63d_v017_signal": {"func": f11_thrift_alpha_tangibles_base_63d_v017_signal},
    "f11_thrift_alpha_marketcap_base_63d_v018_signal": {"func": f11_thrift_alpha_marketcap_base_63d_v018_signal},
    "f11_thrift_alpha_pb_base_63d_v019_signal": {"func": f11_thrift_alpha_pb_base_63d_v019_signal},
    "f11_thrift_alpha_tangible_yield_base_63d_v020_signal": {"func": f11_thrift_alpha_tangible_yield_base_63d_v020_signal},
    "f11_thrift_alpha_tangibles_base_126d_v021_signal": {"func": f11_thrift_alpha_tangibles_base_126d_v021_signal},
    "f11_thrift_alpha_marketcap_base_126d_v022_signal": {"func": f11_thrift_alpha_marketcap_base_126d_v022_signal},
    "f11_thrift_alpha_pb_base_126d_v023_signal": {"func": f11_thrift_alpha_pb_base_126d_v023_signal},
    "f11_thrift_alpha_tangible_yield_base_126d_v024_signal": {"func": f11_thrift_alpha_tangible_yield_base_126d_v024_signal},
    "f11_thrift_alpha_tangibles_base_252d_v025_signal": {"func": f11_thrift_alpha_tangibles_base_252d_v025_signal},
    "f11_thrift_alpha_marketcap_base_252d_v026_signal": {"func": f11_thrift_alpha_marketcap_base_252d_v026_signal},
    "f11_thrift_alpha_pb_base_252d_v027_signal": {"func": f11_thrift_alpha_pb_base_252d_v027_signal},
    "f11_thrift_alpha_tangible_yield_base_252d_v028_signal": {"func": f11_thrift_alpha_tangible_yield_base_252d_v028_signal},
    "f11_thrift_alpha_tangibles_base_504d_v029_signal": {"func": f11_thrift_alpha_tangibles_base_504d_v029_signal},
    "f11_thrift_alpha_marketcap_base_504d_v030_signal": {"func": f11_thrift_alpha_marketcap_base_504d_v030_signal},
    "f11_thrift_alpha_pb_base_504d_v031_signal": {"func": f11_thrift_alpha_pb_base_504d_v031_signal},
    "f11_thrift_alpha_tangible_yield_base_504d_v032_signal": {"func": f11_thrift_alpha_tangible_yield_base_504d_v032_signal},
    "f11_thrift_alpha_tangibles_base_756d_v033_signal": {"func": f11_thrift_alpha_tangibles_base_756d_v033_signal},
    "f11_thrift_alpha_marketcap_base_756d_v034_signal": {"func": f11_thrift_alpha_marketcap_base_756d_v034_signal},
    "f11_thrift_alpha_pb_base_756d_v035_signal": {"func": f11_thrift_alpha_pb_base_756d_v035_signal},
    "f11_thrift_alpha_tangible_yield_base_756d_v036_signal": {"func": f11_thrift_alpha_tangible_yield_base_756d_v036_signal},
    "f11_thrift_alpha_tangibles_base_1008d_v037_signal": {"func": f11_thrift_alpha_tangibles_base_1008d_v037_signal},
    "f11_thrift_alpha_marketcap_base_1008d_v038_signal": {"func": f11_thrift_alpha_marketcap_base_1008d_v038_signal},
    "f11_thrift_alpha_pb_base_1008d_v039_signal": {"func": f11_thrift_alpha_pb_base_1008d_v039_signal},
    "f11_thrift_alpha_tangible_yield_base_1008d_v040_signal": {"func": f11_thrift_alpha_tangible_yield_base_1008d_v040_signal},
    "f11_thrift_alpha_tangibles_base_1260d_v041_signal": {"func": f11_thrift_alpha_tangibles_base_1260d_v041_signal},
    "f11_thrift_alpha_marketcap_base_1260d_v042_signal": {"func": f11_thrift_alpha_marketcap_base_1260d_v042_signal},
    "f11_thrift_alpha_pb_base_1260d_v043_signal": {"func": f11_thrift_alpha_pb_base_1260d_v043_signal},
    "f11_thrift_alpha_tangible_yield_base_1260d_v044_signal": {"func": f11_thrift_alpha_tangible_yield_base_1260d_v044_signal},
    "f11_thrift_alpha_tangibles_ewma_5d_v045_signal": {"func": f11_thrift_alpha_tangibles_ewma_5d_v045_signal},
    "f11_thrift_alpha_marketcap_ewma_5d_v046_signal": {"func": f11_thrift_alpha_marketcap_ewma_5d_v046_signal},
    "f11_thrift_alpha_pb_ewma_5d_v047_signal": {"func": f11_thrift_alpha_pb_ewma_5d_v047_signal},
    "f11_thrift_alpha_tangible_yield_ewma_5d_v048_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_5d_v048_signal},
    "f11_thrift_alpha_tangibles_ewma_10d_v049_signal": {"func": f11_thrift_alpha_tangibles_ewma_10d_v049_signal},
    "f11_thrift_alpha_marketcap_ewma_10d_v050_signal": {"func": f11_thrift_alpha_marketcap_ewma_10d_v050_signal},
    "f11_thrift_alpha_pb_ewma_10d_v051_signal": {"func": f11_thrift_alpha_pb_ewma_10d_v051_signal},
    "f11_thrift_alpha_tangible_yield_ewma_10d_v052_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_10d_v052_signal},
    "f11_thrift_alpha_tangibles_ewma_21d_v053_signal": {"func": f11_thrift_alpha_tangibles_ewma_21d_v053_signal},
    "f11_thrift_alpha_marketcap_ewma_21d_v054_signal": {"func": f11_thrift_alpha_marketcap_ewma_21d_v054_signal},
    "f11_thrift_alpha_pb_ewma_21d_v055_signal": {"func": f11_thrift_alpha_pb_ewma_21d_v055_signal},
    "f11_thrift_alpha_tangible_yield_ewma_21d_v056_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_21d_v056_signal},
    "f11_thrift_alpha_tangibles_ewma_42d_v057_signal": {"func": f11_thrift_alpha_tangibles_ewma_42d_v057_signal},
    "f11_thrift_alpha_marketcap_ewma_42d_v058_signal": {"func": f11_thrift_alpha_marketcap_ewma_42d_v058_signal},
    "f11_thrift_alpha_pb_ewma_42d_v059_signal": {"func": f11_thrift_alpha_pb_ewma_42d_v059_signal},
    "f11_thrift_alpha_tangible_yield_ewma_42d_v060_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_42d_v060_signal},
    "f11_thrift_alpha_tangibles_ewma_63d_v061_signal": {"func": f11_thrift_alpha_tangibles_ewma_63d_v061_signal},
    "f11_thrift_alpha_marketcap_ewma_63d_v062_signal": {"func": f11_thrift_alpha_marketcap_ewma_63d_v062_signal},
    "f11_thrift_alpha_pb_ewma_63d_v063_signal": {"func": f11_thrift_alpha_pb_ewma_63d_v063_signal},
    "f11_thrift_alpha_tangible_yield_ewma_63d_v064_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_63d_v064_signal},
    "f11_thrift_alpha_tangibles_ewma_126d_v065_signal": {"func": f11_thrift_alpha_tangibles_ewma_126d_v065_signal},
    "f11_thrift_alpha_marketcap_ewma_126d_v066_signal": {"func": f11_thrift_alpha_marketcap_ewma_126d_v066_signal},
    "f11_thrift_alpha_pb_ewma_126d_v067_signal": {"func": f11_thrift_alpha_pb_ewma_126d_v067_signal},
    "f11_thrift_alpha_tangible_yield_ewma_126d_v068_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_126d_v068_signal},
    "f11_thrift_alpha_tangibles_ewma_252d_v069_signal": {"func": f11_thrift_alpha_tangibles_ewma_252d_v069_signal},
    "f11_thrift_alpha_marketcap_ewma_252d_v070_signal": {"func": f11_thrift_alpha_marketcap_ewma_252d_v070_signal},
    "f11_thrift_alpha_pb_ewma_252d_v071_signal": {"func": f11_thrift_alpha_pb_ewma_252d_v071_signal},
    "f11_thrift_alpha_tangible_yield_ewma_252d_v072_signal": {"func": f11_thrift_alpha_tangible_yield_ewma_252d_v072_signal},
    "f11_thrift_alpha_tangibles_ewma_504d_v073_signal": {"func": f11_thrift_alpha_tangibles_ewma_504d_v073_signal},
    "f11_thrift_alpha_marketcap_ewma_504d_v074_signal": {"func": f11_thrift_alpha_marketcap_ewma_504d_v074_signal},
    "f11_thrift_alpha_pb_ewma_504d_v075_signal": {"func": f11_thrift_alpha_pb_ewma_504d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 11...")
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
