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

def f02_tbvps_growth_tangibles_slope_pct_5d_v001_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 5d window."""
    res = _slope_pct(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_5d_v002_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 5d window."""
    res = _slope_pct(shareswa, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_5d_v003_signal(bvps):
    """Percentage slope for Raw level of bvps over 5d window."""
    res = _slope_pct(bvps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_5d_v004_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 5d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_5d_v005_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 5d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_5d_v006_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 5d window."""
    res = _slope_pct(_ratio(tangibles, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_10d_v007_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 10d window."""
    res = _slope_pct(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_10d_v008_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 10d window."""
    res = _slope_pct(shareswa, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_10d_v009_signal(bvps):
    """Percentage slope for Raw level of bvps over 10d window."""
    res = _slope_pct(bvps, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_10d_v010_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 10d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_10d_v011_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 10d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_10d_v012_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 10d window."""
    res = _slope_pct(_ratio(tangibles, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_21d_v013_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 21d window."""
    res = _slope_pct(tangibles, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_21d_v014_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 21d window."""
    res = _slope_pct(shareswa, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_21d_v015_signal(bvps):
    """Percentage slope for Raw level of bvps over 21d window."""
    res = _slope_pct(bvps, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_21d_v016_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 21d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_21d_v017_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 21d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_21d_v018_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 21d window."""
    res = _slope_pct(_ratio(tangibles, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_42d_v019_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 42d window."""
    res = _slope_pct(tangibles, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_42d_v020_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 42d window."""
    res = _slope_pct(shareswa, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_42d_v021_signal(bvps):
    """Percentage slope for Raw level of bvps over 42d window."""
    res = _slope_pct(bvps, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_42d_v022_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 42d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_42d_v023_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 42d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_42d_v024_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 42d window."""
    res = _slope_pct(_ratio(tangibles, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_63d_v025_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 63d window."""
    res = _slope_pct(tangibles, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_63d_v026_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 63d window."""
    res = _slope_pct(shareswa, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_63d_v027_signal(bvps):
    """Percentage slope for Raw level of bvps over 63d window."""
    res = _slope_pct(bvps, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_63d_v028_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 63d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_63d_v029_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 63d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_63d_v030_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 63d window."""
    res = _slope_pct(_ratio(tangibles, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_126d_v031_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 126d window."""
    res = _slope_pct(tangibles, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_126d_v032_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 126d window."""
    res = _slope_pct(shareswa, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_126d_v033_signal(bvps):
    """Percentage slope for Raw level of bvps over 126d window."""
    res = _slope_pct(bvps, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_126d_v034_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 126d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_126d_v035_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 126d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_126d_v036_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 126d window."""
    res = _slope_pct(_ratio(tangibles, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_252d_v037_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 252d window."""
    res = _slope_pct(tangibles, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_252d_v038_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 252d window."""
    res = _slope_pct(shareswa, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_252d_v039_signal(bvps):
    """Percentage slope for Raw level of bvps over 252d window."""
    res = _slope_pct(bvps, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_252d_v040_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 252d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_252d_v041_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 252d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_252d_v042_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 252d window."""
    res = _slope_pct(_ratio(tangibles, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_504d_v043_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 504d window."""
    res = _slope_pct(tangibles, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_504d_v044_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 504d window."""
    res = _slope_pct(shareswa, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_504d_v045_signal(bvps):
    """Percentage slope for Raw level of bvps over 504d window."""
    res = _slope_pct(bvps, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_504d_v046_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 504d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_504d_v047_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 504d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_504d_v048_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 504d window."""
    res = _slope_pct(_ratio(tangibles, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_756d_v049_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 756d window."""
    res = _slope_pct(tangibles, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_756d_v050_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 756d window."""
    res = _slope_pct(shareswa, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_756d_v051_signal(bvps):
    """Percentage slope for Raw level of bvps over 756d window."""
    res = _slope_pct(bvps, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_756d_v052_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 756d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_756d_v053_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 756d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_756d_v054_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 756d window."""
    res = _slope_pct(_ratio(tangibles, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_1008d_v055_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 1008d window."""
    res = _slope_pct(tangibles, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_1008d_v056_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 1008d window."""
    res = _slope_pct(shareswa, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_1008d_v057_signal(bvps):
    """Percentage slope for Raw level of bvps over 1008d window."""
    res = _slope_pct(bvps, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_1008d_v058_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 1008d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_1008d_v059_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 1008d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_1008d_v060_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 1008d window."""
    res = _slope_pct(_ratio(tangibles, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_pct_1260d_v061_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 1260d window."""
    res = _slope_pct(tangibles, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_pct_1260d_v062_signal(shareswa):
    """Percentage slope for Raw level of shareswa over 1260d window."""
    res = _slope_pct(shareswa, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_pct_1260d_v063_signal(bvps):
    """Percentage slope for Raw level of bvps over 1260d window."""
    res = _slope_pct(bvps, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_pct_1260d_v064_signal(tangibles, shareswa):
    """Percentage slope for Tangible book per share over 1260d window."""
    res = _slope_pct(_ratio(tangibles, shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_pct_1260d_v065_signal(tangibles, bvps, shareswa):
    """Percentage slope for Tangible concentration of book value over 1260d window."""
    res = _slope_pct(_ratio(tangibles, bvps * shareswa), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_pct_1260d_v066_signal(tangibles, assets):
    """Percentage slope for Tangible asset density over 1260d window."""
    res = _slope_pct(_ratio(tangibles, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_5d_v067_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 5d window."""
    res = _jerk(tangibles, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_5d_v068_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 5d window."""
    res = _jerk(shareswa, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_5d_v069_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 5d window."""
    res = _jerk(bvps, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_5d_v070_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 5d window."""
    res = _jerk(_ratio(tangibles, shareswa), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_5d_v071_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 5d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_5d_v072_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 5d window."""
    res = _jerk(_ratio(tangibles, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_10d_v073_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 10d window."""
    res = _jerk(tangibles, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_10d_v074_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 10d window."""
    res = _jerk(shareswa, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_10d_v075_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 10d window."""
    res = _jerk(bvps, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_10d_v076_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 10d window."""
    res = _jerk(_ratio(tangibles, shareswa), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_10d_v077_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 10d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_10d_v078_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 10d window."""
    res = _jerk(_ratio(tangibles, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_21d_v079_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 21d window."""
    res = _jerk(tangibles, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_21d_v080_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 21d window."""
    res = _jerk(shareswa, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_21d_v081_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 21d window."""
    res = _jerk(bvps, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_21d_v082_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 21d window."""
    res = _jerk(_ratio(tangibles, shareswa), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_21d_v083_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 21d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_21d_v084_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 21d window."""
    res = _jerk(_ratio(tangibles, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_42d_v085_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 42d window."""
    res = _jerk(tangibles, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_42d_v086_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 42d window."""
    res = _jerk(shareswa, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_42d_v087_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 42d window."""
    res = _jerk(bvps, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_42d_v088_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 42d window."""
    res = _jerk(_ratio(tangibles, shareswa), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_42d_v089_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 42d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_42d_v090_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 42d window."""
    res = _jerk(_ratio(tangibles, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_63d_v091_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 63d window."""
    res = _jerk(tangibles, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_63d_v092_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 63d window."""
    res = _jerk(shareswa, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_63d_v093_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 63d window."""
    res = _jerk(bvps, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_63d_v094_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 63d window."""
    res = _jerk(_ratio(tangibles, shareswa), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_63d_v095_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 63d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_63d_v096_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 63d window."""
    res = _jerk(_ratio(tangibles, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_126d_v097_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 126d window."""
    res = _jerk(tangibles, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_126d_v098_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 126d window."""
    res = _jerk(shareswa, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_126d_v099_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 126d window."""
    res = _jerk(bvps, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_126d_v100_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 126d window."""
    res = _jerk(_ratio(tangibles, shareswa), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_126d_v101_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 126d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_126d_v102_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 126d window."""
    res = _jerk(_ratio(tangibles, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_252d_v103_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 252d window."""
    res = _jerk(tangibles, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_252d_v104_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 252d window."""
    res = _jerk(shareswa, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_252d_v105_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 252d window."""
    res = _jerk(bvps, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_252d_v106_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 252d window."""
    res = _jerk(_ratio(tangibles, shareswa), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_252d_v107_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 252d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_252d_v108_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 252d window."""
    res = _jerk(_ratio(tangibles, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_504d_v109_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 504d window."""
    res = _jerk(tangibles, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_504d_v110_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 504d window."""
    res = _jerk(shareswa, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_504d_v111_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 504d window."""
    res = _jerk(bvps, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_504d_v112_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 504d window."""
    res = _jerk(_ratio(tangibles, shareswa), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_504d_v113_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 504d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_504d_v114_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 504d window."""
    res = _jerk(_ratio(tangibles, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_756d_v115_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 756d window."""
    res = _jerk(tangibles, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_756d_v116_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 756d window."""
    res = _jerk(shareswa, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_756d_v117_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 756d window."""
    res = _jerk(bvps, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_756d_v118_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 756d window."""
    res = _jerk(_ratio(tangibles, shareswa), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_756d_v119_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 756d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_756d_v120_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 756d window."""
    res = _jerk(_ratio(tangibles, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_1008d_v121_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 1008d window."""
    res = _jerk(tangibles, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_1008d_v122_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 1008d window."""
    res = _jerk(shareswa, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_1008d_v123_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 1008d window."""
    res = _jerk(bvps, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_1008d_v124_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 1008d window."""
    res = _jerk(_ratio(tangibles, shareswa), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_1008d_v125_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 1008d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_1008d_v126_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 1008d window."""
    res = _jerk(_ratio(tangibles, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_jerk_1260d_v127_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 1260d window."""
    res = _jerk(tangibles, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_jerk_1260d_v128_signal(shareswa):
    """Acceleration/Jerk for Raw level of shareswa over 1260d window."""
    res = _jerk(shareswa, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_jerk_1260d_v129_signal(bvps):
    """Acceleration/Jerk for Raw level of bvps over 1260d window."""
    res = _jerk(bvps, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_jerk_1260d_v130_signal(tangibles, shareswa):
    """Acceleration/Jerk for Tangible book per share over 1260d window."""
    res = _jerk(_ratio(tangibles, shareswa), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_jerk_1260d_v131_signal(tangibles, bvps, shareswa):
    """Acceleration/Jerk for Tangible concentration of book value over 1260d window."""
    res = _jerk(_ratio(tangibles, bvps * shareswa), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_jerk_1260d_v132_signal(tangibles, assets):
    """Acceleration/Jerk for Tangible asset density over 1260d window."""
    res = _jerk(_ratio(tangibles, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_5d_v133_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 5d window."""
    res = (_slope_pct(tangibles, 5).diff(5) / _sma(tangibles.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_5d_v134_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 5d window."""
    res = (_slope_pct(shareswa, 5).diff(5) / _sma(shareswa.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_5d_v135_signal(bvps):
    """Normalized slope change for Raw level of bvps over 5d window."""
    res = (_slope_pct(bvps, 5).diff(5) / _sma(bvps.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_5d_v136_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 5d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 5).diff(5) / _sma(_ratio(tangibles, shareswa).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_5d_v137_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 5d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 5).diff(5) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_5d_v138_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 5d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 5).diff(5) / _sma(_ratio(tangibles, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_10d_v139_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 10d window."""
    res = (_slope_pct(tangibles, 10).diff(10) / _sma(tangibles.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_10d_v140_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 10d window."""
    res = (_slope_pct(shareswa, 10).diff(10) / _sma(shareswa.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_10d_v141_signal(bvps):
    """Normalized slope change for Raw level of bvps over 10d window."""
    res = (_slope_pct(bvps, 10).diff(10) / _sma(bvps.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_10d_v142_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 10d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 10).diff(10) / _sma(_ratio(tangibles, shareswa).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_10d_v143_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 10d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 10).diff(10) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_10d_v144_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 10d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 10).diff(10) / _sma(_ratio(tangibles, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_21d_v145_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 21d window."""
    res = (_slope_pct(tangibles, 21).diff(21) / _sma(tangibles.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_21d_v146_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 21d window."""
    res = (_slope_pct(shareswa, 21).diff(21) / _sma(shareswa.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_21d_v147_signal(bvps):
    """Normalized slope change for Raw level of bvps over 21d window."""
    res = (_slope_pct(bvps, 21).diff(21) / _sma(bvps.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_21d_v148_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 21d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 21).diff(21) / _sma(_ratio(tangibles, shareswa).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_21d_v149_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 21d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 21).diff(21) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_21d_v150_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 21d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 21).diff(21) / _sma(_ratio(tangibles, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f02_tbvps_growth_tangibles_slope_pct_5d_v001_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_5d_v001_signal},
    "f02_tbvps_growth_shareswa_slope_pct_5d_v002_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_5d_v002_signal},
    "f02_tbvps_growth_bvps_slope_pct_5d_v003_signal": {"func": f02_tbvps_growth_bvps_slope_pct_5d_v003_signal},
    "f02_tbvps_growth_tbvps_slope_pct_5d_v004_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_5d_v004_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_5d_v005_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_5d_v005_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_5d_v006_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_5d_v006_signal},
    "f02_tbvps_growth_tangibles_slope_pct_10d_v007_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_10d_v007_signal},
    "f02_tbvps_growth_shareswa_slope_pct_10d_v008_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_10d_v008_signal},
    "f02_tbvps_growth_bvps_slope_pct_10d_v009_signal": {"func": f02_tbvps_growth_bvps_slope_pct_10d_v009_signal},
    "f02_tbvps_growth_tbvps_slope_pct_10d_v010_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_10d_v010_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_10d_v011_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_10d_v011_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_10d_v012_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_10d_v012_signal},
    "f02_tbvps_growth_tangibles_slope_pct_21d_v013_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_21d_v013_signal},
    "f02_tbvps_growth_shareswa_slope_pct_21d_v014_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_21d_v014_signal},
    "f02_tbvps_growth_bvps_slope_pct_21d_v015_signal": {"func": f02_tbvps_growth_bvps_slope_pct_21d_v015_signal},
    "f02_tbvps_growth_tbvps_slope_pct_21d_v016_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_21d_v016_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_21d_v017_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_21d_v017_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_21d_v018_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_21d_v018_signal},
    "f02_tbvps_growth_tangibles_slope_pct_42d_v019_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_42d_v019_signal},
    "f02_tbvps_growth_shareswa_slope_pct_42d_v020_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_42d_v020_signal},
    "f02_tbvps_growth_bvps_slope_pct_42d_v021_signal": {"func": f02_tbvps_growth_bvps_slope_pct_42d_v021_signal},
    "f02_tbvps_growth_tbvps_slope_pct_42d_v022_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_42d_v022_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_42d_v023_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_42d_v023_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_42d_v024_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_42d_v024_signal},
    "f02_tbvps_growth_tangibles_slope_pct_63d_v025_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_63d_v025_signal},
    "f02_tbvps_growth_shareswa_slope_pct_63d_v026_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_63d_v026_signal},
    "f02_tbvps_growth_bvps_slope_pct_63d_v027_signal": {"func": f02_tbvps_growth_bvps_slope_pct_63d_v027_signal},
    "f02_tbvps_growth_tbvps_slope_pct_63d_v028_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_63d_v028_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_63d_v029_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_63d_v029_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_63d_v030_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_63d_v030_signal},
    "f02_tbvps_growth_tangibles_slope_pct_126d_v031_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_126d_v031_signal},
    "f02_tbvps_growth_shareswa_slope_pct_126d_v032_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_126d_v032_signal},
    "f02_tbvps_growth_bvps_slope_pct_126d_v033_signal": {"func": f02_tbvps_growth_bvps_slope_pct_126d_v033_signal},
    "f02_tbvps_growth_tbvps_slope_pct_126d_v034_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_126d_v034_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_126d_v035_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_126d_v035_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_126d_v036_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_126d_v036_signal},
    "f02_tbvps_growth_tangibles_slope_pct_252d_v037_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_252d_v037_signal},
    "f02_tbvps_growth_shareswa_slope_pct_252d_v038_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_252d_v038_signal},
    "f02_tbvps_growth_bvps_slope_pct_252d_v039_signal": {"func": f02_tbvps_growth_bvps_slope_pct_252d_v039_signal},
    "f02_tbvps_growth_tbvps_slope_pct_252d_v040_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_252d_v040_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_252d_v041_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_252d_v041_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_252d_v042_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_252d_v042_signal},
    "f02_tbvps_growth_tangibles_slope_pct_504d_v043_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_504d_v043_signal},
    "f02_tbvps_growth_shareswa_slope_pct_504d_v044_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_504d_v044_signal},
    "f02_tbvps_growth_bvps_slope_pct_504d_v045_signal": {"func": f02_tbvps_growth_bvps_slope_pct_504d_v045_signal},
    "f02_tbvps_growth_tbvps_slope_pct_504d_v046_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_504d_v046_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_504d_v047_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_504d_v047_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_504d_v048_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_504d_v048_signal},
    "f02_tbvps_growth_tangibles_slope_pct_756d_v049_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_756d_v049_signal},
    "f02_tbvps_growth_shareswa_slope_pct_756d_v050_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_756d_v050_signal},
    "f02_tbvps_growth_bvps_slope_pct_756d_v051_signal": {"func": f02_tbvps_growth_bvps_slope_pct_756d_v051_signal},
    "f02_tbvps_growth_tbvps_slope_pct_756d_v052_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_756d_v052_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_756d_v053_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_756d_v053_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_756d_v054_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_756d_v054_signal},
    "f02_tbvps_growth_tangibles_slope_pct_1008d_v055_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_1008d_v055_signal},
    "f02_tbvps_growth_shareswa_slope_pct_1008d_v056_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_1008d_v056_signal},
    "f02_tbvps_growth_bvps_slope_pct_1008d_v057_signal": {"func": f02_tbvps_growth_bvps_slope_pct_1008d_v057_signal},
    "f02_tbvps_growth_tbvps_slope_pct_1008d_v058_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_1008d_v058_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_1008d_v059_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_1008d_v059_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_1008d_v060_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_1008d_v060_signal},
    "f02_tbvps_growth_tangibles_slope_pct_1260d_v061_signal": {"func": f02_tbvps_growth_tangibles_slope_pct_1260d_v061_signal},
    "f02_tbvps_growth_shareswa_slope_pct_1260d_v062_signal": {"func": f02_tbvps_growth_shareswa_slope_pct_1260d_v062_signal},
    "f02_tbvps_growth_bvps_slope_pct_1260d_v063_signal": {"func": f02_tbvps_growth_bvps_slope_pct_1260d_v063_signal},
    "f02_tbvps_growth_tbvps_slope_pct_1260d_v064_signal": {"func": f02_tbvps_growth_tbvps_slope_pct_1260d_v064_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_pct_1260d_v065_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_pct_1260d_v065_signal},
    "f02_tbvps_growth_growth_capacity_slope_pct_1260d_v066_signal": {"func": f02_tbvps_growth_growth_capacity_slope_pct_1260d_v066_signal},
    "f02_tbvps_growth_tangibles_jerk_5d_v067_signal": {"func": f02_tbvps_growth_tangibles_jerk_5d_v067_signal},
    "f02_tbvps_growth_shareswa_jerk_5d_v068_signal": {"func": f02_tbvps_growth_shareswa_jerk_5d_v068_signal},
    "f02_tbvps_growth_bvps_jerk_5d_v069_signal": {"func": f02_tbvps_growth_bvps_jerk_5d_v069_signal},
    "f02_tbvps_growth_tbvps_jerk_5d_v070_signal": {"func": f02_tbvps_growth_tbvps_jerk_5d_v070_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_5d_v071_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_5d_v071_signal},
    "f02_tbvps_growth_growth_capacity_jerk_5d_v072_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_5d_v072_signal},
    "f02_tbvps_growth_tangibles_jerk_10d_v073_signal": {"func": f02_tbvps_growth_tangibles_jerk_10d_v073_signal},
    "f02_tbvps_growth_shareswa_jerk_10d_v074_signal": {"func": f02_tbvps_growth_shareswa_jerk_10d_v074_signal},
    "f02_tbvps_growth_bvps_jerk_10d_v075_signal": {"func": f02_tbvps_growth_bvps_jerk_10d_v075_signal},
    "f02_tbvps_growth_tbvps_jerk_10d_v076_signal": {"func": f02_tbvps_growth_tbvps_jerk_10d_v076_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_10d_v077_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_10d_v077_signal},
    "f02_tbvps_growth_growth_capacity_jerk_10d_v078_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_10d_v078_signal},
    "f02_tbvps_growth_tangibles_jerk_21d_v079_signal": {"func": f02_tbvps_growth_tangibles_jerk_21d_v079_signal},
    "f02_tbvps_growth_shareswa_jerk_21d_v080_signal": {"func": f02_tbvps_growth_shareswa_jerk_21d_v080_signal},
    "f02_tbvps_growth_bvps_jerk_21d_v081_signal": {"func": f02_tbvps_growth_bvps_jerk_21d_v081_signal},
    "f02_tbvps_growth_tbvps_jerk_21d_v082_signal": {"func": f02_tbvps_growth_tbvps_jerk_21d_v082_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_21d_v083_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_21d_v083_signal},
    "f02_tbvps_growth_growth_capacity_jerk_21d_v084_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_21d_v084_signal},
    "f02_tbvps_growth_tangibles_jerk_42d_v085_signal": {"func": f02_tbvps_growth_tangibles_jerk_42d_v085_signal},
    "f02_tbvps_growth_shareswa_jerk_42d_v086_signal": {"func": f02_tbvps_growth_shareswa_jerk_42d_v086_signal},
    "f02_tbvps_growth_bvps_jerk_42d_v087_signal": {"func": f02_tbvps_growth_bvps_jerk_42d_v087_signal},
    "f02_tbvps_growth_tbvps_jerk_42d_v088_signal": {"func": f02_tbvps_growth_tbvps_jerk_42d_v088_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_42d_v089_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_42d_v089_signal},
    "f02_tbvps_growth_growth_capacity_jerk_42d_v090_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_42d_v090_signal},
    "f02_tbvps_growth_tangibles_jerk_63d_v091_signal": {"func": f02_tbvps_growth_tangibles_jerk_63d_v091_signal},
    "f02_tbvps_growth_shareswa_jerk_63d_v092_signal": {"func": f02_tbvps_growth_shareswa_jerk_63d_v092_signal},
    "f02_tbvps_growth_bvps_jerk_63d_v093_signal": {"func": f02_tbvps_growth_bvps_jerk_63d_v093_signal},
    "f02_tbvps_growth_tbvps_jerk_63d_v094_signal": {"func": f02_tbvps_growth_tbvps_jerk_63d_v094_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_63d_v095_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_63d_v095_signal},
    "f02_tbvps_growth_growth_capacity_jerk_63d_v096_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_63d_v096_signal},
    "f02_tbvps_growth_tangibles_jerk_126d_v097_signal": {"func": f02_tbvps_growth_tangibles_jerk_126d_v097_signal},
    "f02_tbvps_growth_shareswa_jerk_126d_v098_signal": {"func": f02_tbvps_growth_shareswa_jerk_126d_v098_signal},
    "f02_tbvps_growth_bvps_jerk_126d_v099_signal": {"func": f02_tbvps_growth_bvps_jerk_126d_v099_signal},
    "f02_tbvps_growth_tbvps_jerk_126d_v100_signal": {"func": f02_tbvps_growth_tbvps_jerk_126d_v100_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_126d_v101_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_126d_v101_signal},
    "f02_tbvps_growth_growth_capacity_jerk_126d_v102_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_126d_v102_signal},
    "f02_tbvps_growth_tangibles_jerk_252d_v103_signal": {"func": f02_tbvps_growth_tangibles_jerk_252d_v103_signal},
    "f02_tbvps_growth_shareswa_jerk_252d_v104_signal": {"func": f02_tbvps_growth_shareswa_jerk_252d_v104_signal},
    "f02_tbvps_growth_bvps_jerk_252d_v105_signal": {"func": f02_tbvps_growth_bvps_jerk_252d_v105_signal},
    "f02_tbvps_growth_tbvps_jerk_252d_v106_signal": {"func": f02_tbvps_growth_tbvps_jerk_252d_v106_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_252d_v107_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_252d_v107_signal},
    "f02_tbvps_growth_growth_capacity_jerk_252d_v108_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_252d_v108_signal},
    "f02_tbvps_growth_tangibles_jerk_504d_v109_signal": {"func": f02_tbvps_growth_tangibles_jerk_504d_v109_signal},
    "f02_tbvps_growth_shareswa_jerk_504d_v110_signal": {"func": f02_tbvps_growth_shareswa_jerk_504d_v110_signal},
    "f02_tbvps_growth_bvps_jerk_504d_v111_signal": {"func": f02_tbvps_growth_bvps_jerk_504d_v111_signal},
    "f02_tbvps_growth_tbvps_jerk_504d_v112_signal": {"func": f02_tbvps_growth_tbvps_jerk_504d_v112_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_504d_v113_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_504d_v113_signal},
    "f02_tbvps_growth_growth_capacity_jerk_504d_v114_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_504d_v114_signal},
    "f02_tbvps_growth_tangibles_jerk_756d_v115_signal": {"func": f02_tbvps_growth_tangibles_jerk_756d_v115_signal},
    "f02_tbvps_growth_shareswa_jerk_756d_v116_signal": {"func": f02_tbvps_growth_shareswa_jerk_756d_v116_signal},
    "f02_tbvps_growth_bvps_jerk_756d_v117_signal": {"func": f02_tbvps_growth_bvps_jerk_756d_v117_signal},
    "f02_tbvps_growth_tbvps_jerk_756d_v118_signal": {"func": f02_tbvps_growth_tbvps_jerk_756d_v118_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_756d_v119_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_756d_v119_signal},
    "f02_tbvps_growth_growth_capacity_jerk_756d_v120_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_756d_v120_signal},
    "f02_tbvps_growth_tangibles_jerk_1008d_v121_signal": {"func": f02_tbvps_growth_tangibles_jerk_1008d_v121_signal},
    "f02_tbvps_growth_shareswa_jerk_1008d_v122_signal": {"func": f02_tbvps_growth_shareswa_jerk_1008d_v122_signal},
    "f02_tbvps_growth_bvps_jerk_1008d_v123_signal": {"func": f02_tbvps_growth_bvps_jerk_1008d_v123_signal},
    "f02_tbvps_growth_tbvps_jerk_1008d_v124_signal": {"func": f02_tbvps_growth_tbvps_jerk_1008d_v124_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_1008d_v125_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_1008d_v125_signal},
    "f02_tbvps_growth_growth_capacity_jerk_1008d_v126_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_1008d_v126_signal},
    "f02_tbvps_growth_tangibles_jerk_1260d_v127_signal": {"func": f02_tbvps_growth_tangibles_jerk_1260d_v127_signal},
    "f02_tbvps_growth_shareswa_jerk_1260d_v128_signal": {"func": f02_tbvps_growth_shareswa_jerk_1260d_v128_signal},
    "f02_tbvps_growth_bvps_jerk_1260d_v129_signal": {"func": f02_tbvps_growth_bvps_jerk_1260d_v129_signal},
    "f02_tbvps_growth_tbvps_jerk_1260d_v130_signal": {"func": f02_tbvps_growth_tbvps_jerk_1260d_v130_signal},
    "f02_tbvps_growth_tbv_to_total_bv_jerk_1260d_v131_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_jerk_1260d_v131_signal},
    "f02_tbvps_growth_growth_capacity_jerk_1260d_v132_signal": {"func": f02_tbvps_growth_growth_capacity_jerk_1260d_v132_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_5d_v133_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_5d_v133_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_5d_v134_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_5d_v134_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_5d_v135_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_5d_v135_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_5d_v136_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_5d_v136_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_5d_v137_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_5d_v137_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_5d_v138_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_5d_v138_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_10d_v139_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_10d_v139_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_10d_v140_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_10d_v140_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_10d_v141_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_10d_v141_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_10d_v142_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_10d_v142_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_10d_v143_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_10d_v143_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_10d_v144_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_10d_v144_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_21d_v145_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_21d_v145_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_21d_v146_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_21d_v146_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_21d_v147_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_21d_v147_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_21d_v148_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_21d_v148_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_21d_v149_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_21d_v149_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_21d_v150_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_21d_v150_signal},
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
