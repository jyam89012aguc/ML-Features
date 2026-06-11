"""
Family: Royalty Streaming Yield
Sector: Financing
Mathematical Approach: Fundamental/Yield
"""


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

def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5

def _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, w):
    return revenue.diff(w) / ncfo.rolling(w).mean().abs()

def _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, w):
    return _z(revenue, w) - _z(ncfo, w)

def _royalty_streaming_yield_regime(revenue, ncfo, marketcap, w):
    return revenue.pct_change(w)

def _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, w):
    return np.log(revenue.replace(0, np.nan) / revenue.rolling(w).mean())

def _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, w):
    return revenue.rolling(w).std() / revenue.rolling(w).mean().abs()

def f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v001_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v002_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v003_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v004_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v005_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v006_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v007_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v008_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v009_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v010_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v011_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v012_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v013_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v014_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v015_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v016_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v017_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v018_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v019_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v020_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v021_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v022_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v023_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v024_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v025_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v026_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v027_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v028_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v029_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v030_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v031_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v032_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v033_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v034_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v035_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v036_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v037_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v038_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v039_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v040_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v041_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v042_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v043_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v044_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v045_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v046_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v047_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v048_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v049_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v050_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v051_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v052_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v053_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v054_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v055_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v056_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v057_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v058_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v059_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v060_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v061_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v062_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v063_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v064_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v065_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v066_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v067_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v068_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v069_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v070_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v071_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v072_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v073_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v074_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v075_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v076_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v077_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v078_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v079_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v080_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v081_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v082_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v083_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v084_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v085_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v086_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v087_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v088_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v089_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v090_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v091_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v092_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v093_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v094_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v095_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v096_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v097_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v098_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v099_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v100_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v101_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v102_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v103_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v104_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v105_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v106_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v107_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v108_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v109_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v110_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v111_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v112_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v113_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v114_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v115_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v116_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v117_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v118_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v119_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v120_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v121_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v122_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v123_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v124_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v125_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v126_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v127_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v128_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v129_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v130_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v131_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v132_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v133_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v134_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v135_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v136_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v137_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v138_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v139_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v140_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v141_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v142_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v143_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v144_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v145_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 21)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v146_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_impulse(revenue, ncfo, marketcap, 63)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v147_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_regime(revenue, ncfo, marketcap, 126)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v148_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_dispersion(revenue, ncfo, marketcap, 252)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v149_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_efficiency(revenue, ncfo, marketcap, 504)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

def f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v150_signal(revenue, ncfo, marketcap):
    """Measures the third-order change (jerk) in the domain primitive to identify regime exhaustion."""
    base_signal = _royalty_streaming_yield_velocity(revenue, ncfo, marketcap, 5)
    result = base_signal.diff(5).diff(5).diff(5) / 125.0
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v001_signal,
    f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v002_signal,
    f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v003_signal,
    f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v004_signal,
    f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v005_signal,
    f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v006_signal,
    f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v007_signal,
    f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v008_signal,
    f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v009_signal,
    f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v010_signal,
    f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v011_signal,
    f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v012_signal,
    f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v013_signal,
    f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v014_signal,
    f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v015_signal,
    f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v016_signal,
    f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v017_signal,
    f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v018_signal,
    f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v019_signal,
    f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v020_signal,
    f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v021_signal,
    f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v022_signal,
    f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v023_signal,
    f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v024_signal,
    f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v025_signal,
    f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v026_signal,
    f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v027_signal,
    f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v028_signal,
    f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v029_signal,
    f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v030_signal,
    f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v031_signal,
    f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v032_signal,
    f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v033_signal,
    f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v034_signal,
    f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v035_signal,
    f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v036_signal,
    f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v037_signal,
    f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v038_signal,
    f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v039_signal,
    f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v040_signal,
    f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v041_signal,
    f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v042_signal,
    f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v043_signal,
    f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v044_signal,
    f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v045_signal,
    f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v046_signal,
    f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v047_signal,
    f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v048_signal,
    f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v049_signal,
    f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v050_signal,
    f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v051_signal,
    f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v052_signal,
    f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v053_signal,
    f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v054_signal,
    f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v055_signal,
    f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v056_signal,
    f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v057_signal,
    f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v058_signal,
    f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v059_signal,
    f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v060_signal,
    f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v061_signal,
    f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v062_signal,
    f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v063_signal,
    f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v064_signal,
    f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v065_signal,
    f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v066_signal,
    f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v067_signal,
    f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v068_signal,
    f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v069_signal,
    f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v070_signal,
    f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v071_signal,
    f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v072_signal,
    f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v073_signal,
    f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v074_signal,
    f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v075_signal,
    f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v076_signal,
    f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v077_signal,
    f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v078_signal,
    f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v079_signal,
    f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v080_signal,
    f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v081_signal,
    f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v082_signal,
    f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v083_signal,
    f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v084_signal,
    f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v085_signal,
    f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v086_signal,
    f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v087_signal,
    f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v088_signal,
    f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v089_signal,
    f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v090_signal,
    f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v091_signal,
    f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v092_signal,
    f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v093_signal,
    f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v094_signal,
    f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v095_signal,
    f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v096_signal,
    f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v097_signal,
    f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v098_signal,
    f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v099_signal,
    f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v100_signal,
    f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v101_signal,
    f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v102_signal,
    f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v103_signal,
    f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v104_signal,
    f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v105_signal,
    f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v106_signal,
    f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v107_signal,
    f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v108_signal,
    f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v109_signal,
    f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v110_signal,
    f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v111_signal,
    f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v112_signal,
    f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v113_signal,
    f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v114_signal,
    f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v115_signal,
    f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v116_signal,
    f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v117_signal,
    f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v118_signal,
    f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v119_signal,
    f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v120_signal,
    f21rs_f21_royalty_streaming_yield_prim2_21d_3rd_derivatives_v121_signal,
    f21rs_f21_royalty_streaming_yield_prim3_63d_3rd_derivatives_v122_signal,
    f21rs_f21_royalty_streaming_yield_prim4_126d_3rd_derivatives_v123_signal,
    f21rs_f21_royalty_streaming_yield_prim5_252d_3rd_derivatives_v124_signal,
    f21rs_f21_royalty_streaming_yield_prim1_504d_3rd_derivatives_v125_signal,
    f21rs_f21_royalty_streaming_yield_prim2_5d_3rd_derivatives_v126_signal,
    f21rs_f21_royalty_streaming_yield_prim3_21d_3rd_derivatives_v127_signal,
    f21rs_f21_royalty_streaming_yield_prim4_63d_3rd_derivatives_v128_signal,
    f21rs_f21_royalty_streaming_yield_prim5_126d_3rd_derivatives_v129_signal,
    f21rs_f21_royalty_streaming_yield_prim1_252d_3rd_derivatives_v130_signal,
    f21rs_f21_royalty_streaming_yield_prim2_504d_3rd_derivatives_v131_signal,
    f21rs_f21_royalty_streaming_yield_prim3_5d_3rd_derivatives_v132_signal,
    f21rs_f21_royalty_streaming_yield_prim4_21d_3rd_derivatives_v133_signal,
    f21rs_f21_royalty_streaming_yield_prim5_63d_3rd_derivatives_v134_signal,
    f21rs_f21_royalty_streaming_yield_prim1_126d_3rd_derivatives_v135_signal,
    f21rs_f21_royalty_streaming_yield_prim2_252d_3rd_derivatives_v136_signal,
    f21rs_f21_royalty_streaming_yield_prim3_504d_3rd_derivatives_v137_signal,
    f21rs_f21_royalty_streaming_yield_prim4_5d_3rd_derivatives_v138_signal,
    f21rs_f21_royalty_streaming_yield_prim5_21d_3rd_derivatives_v139_signal,
    f21rs_f21_royalty_streaming_yield_prim1_63d_3rd_derivatives_v140_signal,
    f21rs_f21_royalty_streaming_yield_prim2_126d_3rd_derivatives_v141_signal,
    f21rs_f21_royalty_streaming_yield_prim3_252d_3rd_derivatives_v142_signal,
    f21rs_f21_royalty_streaming_yield_prim4_504d_3rd_derivatives_v143_signal,
    f21rs_f21_royalty_streaming_yield_prim5_5d_3rd_derivatives_v144_signal,
    f21rs_f21_royalty_streaming_yield_prim1_21d_3rd_derivatives_v145_signal,
    f21rs_f21_royalty_streaming_yield_prim2_63d_3rd_derivatives_v146_signal,
    f21rs_f21_royalty_streaming_yield_prim3_126d_3rd_derivatives_v147_signal,
    f21rs_f21_royalty_streaming_yield_prim4_252d_3rd_derivatives_v148_signal,
    f21rs_f21_royalty_streaming_yield_prim5_504d_3rd_derivatives_v149_signal,
    f21rs_f21_royalty_streaming_yield_prim1_5d_3rd_derivatives_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]

REGISTRY = {fn.__name__: {'inputs': _inputs_for(fn), 'func': fn} for fn in _FEATURES}
F21_ROYALTY_STREAMING_YIELD_REGISTRY = REGISTRY

if __name__ == "__main__":
    import os
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg: s = s - base * 0.5
        return pd.Series(s, name=None)

    cols = {
        "closeadj": closeadj, "close": close, "open": openp,
        "high": high, "low": low, "volume": volume,
        "opinc": _fund(1, allow_neg=True), "revenue": _fund(2), "opex": _fund(3),
        "gp": _fund(4, allow_neg=True), "ebit": _fund(5, allow_neg=True),
        "sharesbas": _fund(6, base=1e7, vol=0.02), "ncfcommon": _fund(7, base=1e6, allow_neg=True),
        "cashneq": _fund(8), "ncfo": _fund(9, allow_neg=True),
        "capex": _fund(10), "assets": _fund(11), "ppnenet": _fund(12),
        "pe": _fund(13, base=15, vol=0.1), "evebitda": _fund(14, base=10, vol=0.1),
        "marketcap": _fund(15, base=1e9), "inventory": _fund(16), "cor": _fund(17),
        "debt": _fund(18), "liabilities": _fund(19), "equity": _fund(20),
        "netinc": _fund(21, allow_neg=True), "ebitda": _fund(22, allow_neg=True),
        "roic": _fund(23, base=0.1, vol=0.05, allow_neg=True),
        "fcf": _fund(24, allow_neg=True), "pb": _fund(25, base=2, vol=0.1),
        "shrholders": _fund(26, base=100, vol=0.05), "totalvalue": _fund(27, base=1e8),
        "percentoftotal": _fund(28, base=0.2, vol=0.02), "currentratio": _fund(29, base=1.5, vol=0.1),
        "workingcapital": _fund(30, allow_neg=True), "retearn": _fund(31, allow_neg=True),
        "ncff": _fund(32, allow_neg=True), "ncfi": _fund(33, allow_neg=True),
        "debtusd": _fund(34), "tangibles": _fund(35), "intangibles": _fund(36),
        "rnd": _fund(37), "sgna": _fund(38), "receivables": _fund(39), "payables": _fund(40),
        "assetsc": _fund(41), "investmentsnc": _fund(42), "depamor": _fund(43),
        "eps": _fund(44, allow_neg=True), "fcfps": _fund(45, allow_neg=True),
        "ev": _fund(46, base=1.2e9), "shrvalue": _fund(47, base=1e7), "shrunits": _fund(48, base=1e5),
        "fndholders": _fund(49, base=50), "undholders": _fund(50, base=10), "prfholders": _fund(51, base=5),
        "dbtholders": _fund(52, base=20)
    }

    n_features = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y = fn(*args)
        q = y.iloc[504:].dropna()
        if len(q) > 0 and q.nunique() > 10:
            results[name] = y.iloc[504:]
            n_features += 1

    print(f"OK {os.path.basename(__file__)}: {n_features} features pass")
