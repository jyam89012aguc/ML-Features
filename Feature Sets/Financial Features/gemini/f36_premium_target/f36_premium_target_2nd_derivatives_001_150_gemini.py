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

def f36_premium_target_pb_slope_pct_5d_v001_signal(pb):
    """Percentage slope for Raw level of pb over 5d window."""
    res = _slope_pct(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_5d_v002_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 5d window."""
    res = _slope_pct(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_5d_v003_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 5d window."""
    res = _slope_pct(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_5d_v004_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 5d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_10d_v005_signal(pb):
    """Percentage slope for Raw level of pb over 10d window."""
    res = _slope_pct(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_10d_v006_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 10d window."""
    res = _slope_pct(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_10d_v007_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 10d window."""
    res = _slope_pct(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_10d_v008_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 10d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_21d_v009_signal(pb):
    """Percentage slope for Raw level of pb over 21d window."""
    res = _slope_pct(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_21d_v010_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 21d window."""
    res = _slope_pct(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_21d_v011_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 21d window."""
    res = _slope_pct(tangibles, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_21d_v012_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 21d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_42d_v013_signal(pb):
    """Percentage slope for Raw level of pb over 42d window."""
    res = _slope_pct(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_42d_v014_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 42d window."""
    res = _slope_pct(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_42d_v015_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 42d window."""
    res = _slope_pct(tangibles, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_42d_v016_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 42d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_63d_v017_signal(pb):
    """Percentage slope for Raw level of pb over 63d window."""
    res = _slope_pct(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_63d_v018_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 63d window."""
    res = _slope_pct(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_63d_v019_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 63d window."""
    res = _slope_pct(tangibles, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_63d_v020_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 63d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_126d_v021_signal(pb):
    """Percentage slope for Raw level of pb over 126d window."""
    res = _slope_pct(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_126d_v022_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 126d window."""
    res = _slope_pct(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_126d_v023_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 126d window."""
    res = _slope_pct(tangibles, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_126d_v024_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 126d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_252d_v025_signal(pb):
    """Percentage slope for Raw level of pb over 252d window."""
    res = _slope_pct(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_252d_v026_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 252d window."""
    res = _slope_pct(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_252d_v027_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 252d window."""
    res = _slope_pct(tangibles, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_252d_v028_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 252d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_504d_v029_signal(pb):
    """Percentage slope for Raw level of pb over 504d window."""
    res = _slope_pct(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_504d_v030_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 504d window."""
    res = _slope_pct(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_504d_v031_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 504d window."""
    res = _slope_pct(tangibles, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_504d_v032_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 504d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_756d_v033_signal(pb):
    """Percentage slope for Raw level of pb over 756d window."""
    res = _slope_pct(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_756d_v034_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 756d window."""
    res = _slope_pct(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_756d_v035_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 756d window."""
    res = _slope_pct(tangibles, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_756d_v036_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 756d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_1008d_v037_signal(pb):
    """Percentage slope for Raw level of pb over 1008d window."""
    res = _slope_pct(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_1008d_v038_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1008d window."""
    res = _slope_pct(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_1008d_v039_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 1008d window."""
    res = _slope_pct(tangibles, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_1008d_v040_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 1008d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_pct_1260d_v041_signal(pb):
    """Percentage slope for Raw level of pb over 1260d window."""
    res = _slope_pct(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_pct_1260d_v042_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1260d window."""
    res = _slope_pct(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_pct_1260d_v043_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 1260d window."""
    res = _slope_pct(tangibles, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_pct_1260d_v044_signal(tangibles, marketcap):
    """Percentage slope for Tangible book relative to market cap over 1260d window."""
    res = _slope_pct(_ratio(tangibles, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_5d_v045_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 5d window."""
    res = _jerk(pb, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_5d_v046_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 5d window."""
    res = _jerk(marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_5d_v047_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 5d window."""
    res = _jerk(tangibles, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_5d_v048_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 5d window."""
    res = _jerk(_ratio(tangibles, marketcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_10d_v049_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 10d window."""
    res = _jerk(pb, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_10d_v050_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 10d window."""
    res = _jerk(marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_10d_v051_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 10d window."""
    res = _jerk(tangibles, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_10d_v052_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 10d window."""
    res = _jerk(_ratio(tangibles, marketcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_21d_v053_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 21d window."""
    res = _jerk(pb, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_21d_v054_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 21d window."""
    res = _jerk(marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_21d_v055_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 21d window."""
    res = _jerk(tangibles, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_21d_v056_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 21d window."""
    res = _jerk(_ratio(tangibles, marketcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_42d_v057_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 42d window."""
    res = _jerk(pb, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_42d_v058_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 42d window."""
    res = _jerk(marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_42d_v059_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 42d window."""
    res = _jerk(tangibles, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_42d_v060_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 42d window."""
    res = _jerk(_ratio(tangibles, marketcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_63d_v061_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 63d window."""
    res = _jerk(pb, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_63d_v062_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 63d window."""
    res = _jerk(marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_63d_v063_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 63d window."""
    res = _jerk(tangibles, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_63d_v064_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 63d window."""
    res = _jerk(_ratio(tangibles, marketcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_126d_v065_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 126d window."""
    res = _jerk(pb, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_126d_v066_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 126d window."""
    res = _jerk(marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_126d_v067_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 126d window."""
    res = _jerk(tangibles, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_126d_v068_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 126d window."""
    res = _jerk(_ratio(tangibles, marketcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_252d_v069_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 252d window."""
    res = _jerk(pb, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_252d_v070_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 252d window."""
    res = _jerk(marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_252d_v071_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 252d window."""
    res = _jerk(tangibles, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_252d_v072_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 252d window."""
    res = _jerk(_ratio(tangibles, marketcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_504d_v073_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 504d window."""
    res = _jerk(pb, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_504d_v074_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 504d window."""
    res = _jerk(marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_504d_v075_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 504d window."""
    res = _jerk(tangibles, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_504d_v076_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 504d window."""
    res = _jerk(_ratio(tangibles, marketcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_756d_v077_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 756d window."""
    res = _jerk(pb, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_756d_v078_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 756d window."""
    res = _jerk(marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_756d_v079_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 756d window."""
    res = _jerk(tangibles, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_756d_v080_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 756d window."""
    res = _jerk(_ratio(tangibles, marketcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_1008d_v081_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 1008d window."""
    res = _jerk(pb, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_1008d_v082_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1008d window."""
    res = _jerk(marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_1008d_v083_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 1008d window."""
    res = _jerk(tangibles, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_1008d_v084_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 1008d window."""
    res = _jerk(_ratio(tangibles, marketcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_jerk_1260d_v085_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 1260d window."""
    res = _jerk(pb, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_jerk_1260d_v086_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1260d window."""
    res = _jerk(marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_jerk_1260d_v087_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 1260d window."""
    res = _jerk(tangibles, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_jerk_1260d_v088_signal(tangibles, marketcap):
    """Acceleration/Jerk for Tangible book relative to market cap over 1260d window."""
    res = _jerk(_ratio(tangibles, marketcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_5d_v089_signal(pb):
    """Normalized slope change for Raw level of pb over 5d window."""
    res = (_slope_pct(pb, 5).diff(5) / _sma(pb.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_5d_v090_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 5d window."""
    res = (_slope_pct(marketcap, 5).diff(5) / _sma(marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_5d_v091_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 5d window."""
    res = (_slope_pct(tangibles, 5).diff(5) / _sma(tangibles.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_5d_v092_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 5d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 5).diff(5) / _sma(_ratio(tangibles, marketcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_10d_v093_signal(pb):
    """Normalized slope change for Raw level of pb over 10d window."""
    res = (_slope_pct(pb, 10).diff(10) / _sma(pb.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_10d_v094_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 10d window."""
    res = (_slope_pct(marketcap, 10).diff(10) / _sma(marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_10d_v095_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 10d window."""
    res = (_slope_pct(tangibles, 10).diff(10) / _sma(tangibles.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_10d_v096_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 10d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 10).diff(10) / _sma(_ratio(tangibles, marketcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_21d_v097_signal(pb):
    """Normalized slope change for Raw level of pb over 21d window."""
    res = (_slope_pct(pb, 21).diff(21) / _sma(pb.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_21d_v098_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 21d window."""
    res = (_slope_pct(marketcap, 21).diff(21) / _sma(marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_21d_v099_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 21d window."""
    res = (_slope_pct(tangibles, 21).diff(21) / _sma(tangibles.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_21d_v100_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 21d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 21).diff(21) / _sma(_ratio(tangibles, marketcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_42d_v101_signal(pb):
    """Normalized slope change for Raw level of pb over 42d window."""
    res = (_slope_pct(pb, 42).diff(42) / _sma(pb.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_42d_v102_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 42d window."""
    res = (_slope_pct(marketcap, 42).diff(42) / _sma(marketcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_42d_v103_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 42d window."""
    res = (_slope_pct(tangibles, 42).diff(42) / _sma(tangibles.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_42d_v104_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 42d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 42).diff(42) / _sma(_ratio(tangibles, marketcap).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_63d_v105_signal(pb):
    """Normalized slope change for Raw level of pb over 63d window."""
    res = (_slope_pct(pb, 63).diff(63) / _sma(pb.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_63d_v106_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 63d window."""
    res = (_slope_pct(marketcap, 63).diff(63) / _sma(marketcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_63d_v107_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 63d window."""
    res = (_slope_pct(tangibles, 63).diff(63) / _sma(tangibles.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_63d_v108_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 63d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 63).diff(63) / _sma(_ratio(tangibles, marketcap).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_126d_v109_signal(pb):
    """Normalized slope change for Raw level of pb over 126d window."""
    res = (_slope_pct(pb, 126).diff(126) / _sma(pb.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_126d_v110_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 126d window."""
    res = (_slope_pct(marketcap, 126).diff(126) / _sma(marketcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_126d_v111_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 126d window."""
    res = (_slope_pct(tangibles, 126).diff(126) / _sma(tangibles.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_126d_v112_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 126d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 126).diff(126) / _sma(_ratio(tangibles, marketcap).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_252d_v113_signal(pb):
    """Normalized slope change for Raw level of pb over 252d window."""
    res = (_slope_pct(pb, 252).diff(252) / _sma(pb.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_252d_v114_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 252d window."""
    res = (_slope_pct(marketcap, 252).diff(252) / _sma(marketcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_252d_v115_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 252d window."""
    res = (_slope_pct(tangibles, 252).diff(252) / _sma(tangibles.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_252d_v116_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 252d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 252).diff(252) / _sma(_ratio(tangibles, marketcap).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_504d_v117_signal(pb):
    """Normalized slope change for Raw level of pb over 504d window."""
    res = (_slope_pct(pb, 504).diff(504) / _sma(pb.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_504d_v118_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 504d window."""
    res = (_slope_pct(marketcap, 504).diff(504) / _sma(marketcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_504d_v119_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 504d window."""
    res = (_slope_pct(tangibles, 504).diff(504) / _sma(tangibles.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_504d_v120_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 504d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 504).diff(504) / _sma(_ratio(tangibles, marketcap).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_756d_v121_signal(pb):
    """Normalized slope change for Raw level of pb over 756d window."""
    res = (_slope_pct(pb, 756).diff(756) / _sma(pb.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_756d_v122_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 756d window."""
    res = (_slope_pct(marketcap, 756).diff(756) / _sma(marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_756d_v123_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 756d window."""
    res = (_slope_pct(tangibles, 756).diff(756) / _sma(tangibles.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_756d_v124_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 756d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 756).diff(756) / _sma(_ratio(tangibles, marketcap).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_1008d_v125_signal(pb):
    """Normalized slope change for Raw level of pb over 1008d window."""
    res = (_slope_pct(pb, 1008).diff(1008) / _sma(pb.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_1008d_v126_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1008d window."""
    res = (_slope_pct(marketcap, 1008).diff(1008) / _sma(marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_1008d_v127_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 1008d window."""
    res = (_slope_pct(tangibles, 1008).diff(1008) / _sma(tangibles.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_1008d_v128_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 1008d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 1008).diff(1008) / _sma(_ratio(tangibles, marketcap).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_slope_diff_norm_1260d_v129_signal(pb):
    """Normalized slope change for Raw level of pb over 1260d window."""
    res = (_slope_pct(pb, 1260).diff(1260) / _sma(pb.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_slope_diff_norm_1260d_v130_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1260d window."""
    res = (_slope_pct(marketcap, 1260).diff(1260) / _sma(marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_slope_diff_norm_1260d_v131_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 1260d window."""
    res = (_slope_pct(tangibles, 1260).diff(1260) / _sma(tangibles.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_slope_diff_norm_1260d_v132_signal(tangibles, marketcap):
    """Normalized slope change for Tangible book relative to market cap over 1260d window."""
    res = (_slope_pct(_ratio(tangibles, marketcap), 1260).diff(1260) / _sma(_ratio(tangibles, marketcap).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_mom_z_5d_v133_signal(pb):
    """Relative momentum strength for Raw level of pb over 5d window."""
    res = _z(_slope_pct(pb, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_mom_z_5d_v134_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 5d window."""
    res = _z(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_mom_z_5d_v135_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 5d window."""
    res = _z(_slope_pct(tangibles, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_mom_z_5d_v136_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible book relative to market cap over 5d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_mom_z_10d_v137_signal(pb):
    """Relative momentum strength for Raw level of pb over 10d window."""
    res = _z(_slope_pct(pb, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_mom_z_10d_v138_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 10d window."""
    res = _z(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_mom_z_10d_v139_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 10d window."""
    res = _z(_slope_pct(tangibles, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_mom_z_10d_v140_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible book relative to market cap over 10d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_mom_z_21d_v141_signal(pb):
    """Relative momentum strength for Raw level of pb over 21d window."""
    res = _z(_slope_pct(pb, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_mom_z_21d_v142_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 21d window."""
    res = _z(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_mom_z_21d_v143_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 21d window."""
    res = _z(_slope_pct(tangibles, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_mom_z_21d_v144_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible book relative to market cap over 21d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_mom_z_42d_v145_signal(pb):
    """Relative momentum strength for Raw level of pb over 42d window."""
    res = _z(_slope_pct(pb, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_mom_z_42d_v146_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 42d window."""
    res = _z(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangibles_mom_z_42d_v147_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 42d window."""
    res = _z(_slope_pct(tangibles, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_tangible_per_val_mom_z_42d_v148_signal(tangibles, marketcap):
    """Relative momentum strength for Tangible book relative to market cap over 42d window."""
    res = _z(_slope_pct(_ratio(tangibles, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_pb_mom_z_63d_v149_signal(pb):
    """Relative momentum strength for Raw level of pb over 63d window."""
    res = _z(_slope_pct(pb, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f36_premium_target_marketcap_mom_z_63d_v150_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 63d window."""
    res = _z(_slope_pct(marketcap, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f36_premium_target_pb_slope_pct_5d_v001_signal": {"func": f36_premium_target_pb_slope_pct_5d_v001_signal},
    "f36_premium_target_marketcap_slope_pct_5d_v002_signal": {"func": f36_premium_target_marketcap_slope_pct_5d_v002_signal},
    "f36_premium_target_tangibles_slope_pct_5d_v003_signal": {"func": f36_premium_target_tangibles_slope_pct_5d_v003_signal},
    "f36_premium_target_tangible_per_val_slope_pct_5d_v004_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_5d_v004_signal},
    "f36_premium_target_pb_slope_pct_10d_v005_signal": {"func": f36_premium_target_pb_slope_pct_10d_v005_signal},
    "f36_premium_target_marketcap_slope_pct_10d_v006_signal": {"func": f36_premium_target_marketcap_slope_pct_10d_v006_signal},
    "f36_premium_target_tangibles_slope_pct_10d_v007_signal": {"func": f36_premium_target_tangibles_slope_pct_10d_v007_signal},
    "f36_premium_target_tangible_per_val_slope_pct_10d_v008_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_10d_v008_signal},
    "f36_premium_target_pb_slope_pct_21d_v009_signal": {"func": f36_premium_target_pb_slope_pct_21d_v009_signal},
    "f36_premium_target_marketcap_slope_pct_21d_v010_signal": {"func": f36_premium_target_marketcap_slope_pct_21d_v010_signal},
    "f36_premium_target_tangibles_slope_pct_21d_v011_signal": {"func": f36_premium_target_tangibles_slope_pct_21d_v011_signal},
    "f36_premium_target_tangible_per_val_slope_pct_21d_v012_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_21d_v012_signal},
    "f36_premium_target_pb_slope_pct_42d_v013_signal": {"func": f36_premium_target_pb_slope_pct_42d_v013_signal},
    "f36_premium_target_marketcap_slope_pct_42d_v014_signal": {"func": f36_premium_target_marketcap_slope_pct_42d_v014_signal},
    "f36_premium_target_tangibles_slope_pct_42d_v015_signal": {"func": f36_premium_target_tangibles_slope_pct_42d_v015_signal},
    "f36_premium_target_tangible_per_val_slope_pct_42d_v016_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_42d_v016_signal},
    "f36_premium_target_pb_slope_pct_63d_v017_signal": {"func": f36_premium_target_pb_slope_pct_63d_v017_signal},
    "f36_premium_target_marketcap_slope_pct_63d_v018_signal": {"func": f36_premium_target_marketcap_slope_pct_63d_v018_signal},
    "f36_premium_target_tangibles_slope_pct_63d_v019_signal": {"func": f36_premium_target_tangibles_slope_pct_63d_v019_signal},
    "f36_premium_target_tangible_per_val_slope_pct_63d_v020_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_63d_v020_signal},
    "f36_premium_target_pb_slope_pct_126d_v021_signal": {"func": f36_premium_target_pb_slope_pct_126d_v021_signal},
    "f36_premium_target_marketcap_slope_pct_126d_v022_signal": {"func": f36_premium_target_marketcap_slope_pct_126d_v022_signal},
    "f36_premium_target_tangibles_slope_pct_126d_v023_signal": {"func": f36_premium_target_tangibles_slope_pct_126d_v023_signal},
    "f36_premium_target_tangible_per_val_slope_pct_126d_v024_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_126d_v024_signal},
    "f36_premium_target_pb_slope_pct_252d_v025_signal": {"func": f36_premium_target_pb_slope_pct_252d_v025_signal},
    "f36_premium_target_marketcap_slope_pct_252d_v026_signal": {"func": f36_premium_target_marketcap_slope_pct_252d_v026_signal},
    "f36_premium_target_tangibles_slope_pct_252d_v027_signal": {"func": f36_premium_target_tangibles_slope_pct_252d_v027_signal},
    "f36_premium_target_tangible_per_val_slope_pct_252d_v028_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_252d_v028_signal},
    "f36_premium_target_pb_slope_pct_504d_v029_signal": {"func": f36_premium_target_pb_slope_pct_504d_v029_signal},
    "f36_premium_target_marketcap_slope_pct_504d_v030_signal": {"func": f36_premium_target_marketcap_slope_pct_504d_v030_signal},
    "f36_premium_target_tangibles_slope_pct_504d_v031_signal": {"func": f36_premium_target_tangibles_slope_pct_504d_v031_signal},
    "f36_premium_target_tangible_per_val_slope_pct_504d_v032_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_504d_v032_signal},
    "f36_premium_target_pb_slope_pct_756d_v033_signal": {"func": f36_premium_target_pb_slope_pct_756d_v033_signal},
    "f36_premium_target_marketcap_slope_pct_756d_v034_signal": {"func": f36_premium_target_marketcap_slope_pct_756d_v034_signal},
    "f36_premium_target_tangibles_slope_pct_756d_v035_signal": {"func": f36_premium_target_tangibles_slope_pct_756d_v035_signal},
    "f36_premium_target_tangible_per_val_slope_pct_756d_v036_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_756d_v036_signal},
    "f36_premium_target_pb_slope_pct_1008d_v037_signal": {"func": f36_premium_target_pb_slope_pct_1008d_v037_signal},
    "f36_premium_target_marketcap_slope_pct_1008d_v038_signal": {"func": f36_premium_target_marketcap_slope_pct_1008d_v038_signal},
    "f36_premium_target_tangibles_slope_pct_1008d_v039_signal": {"func": f36_premium_target_tangibles_slope_pct_1008d_v039_signal},
    "f36_premium_target_tangible_per_val_slope_pct_1008d_v040_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_1008d_v040_signal},
    "f36_premium_target_pb_slope_pct_1260d_v041_signal": {"func": f36_premium_target_pb_slope_pct_1260d_v041_signal},
    "f36_premium_target_marketcap_slope_pct_1260d_v042_signal": {"func": f36_premium_target_marketcap_slope_pct_1260d_v042_signal},
    "f36_premium_target_tangibles_slope_pct_1260d_v043_signal": {"func": f36_premium_target_tangibles_slope_pct_1260d_v043_signal},
    "f36_premium_target_tangible_per_val_slope_pct_1260d_v044_signal": {"func": f36_premium_target_tangible_per_val_slope_pct_1260d_v044_signal},
    "f36_premium_target_pb_jerk_5d_v045_signal": {"func": f36_premium_target_pb_jerk_5d_v045_signal},
    "f36_premium_target_marketcap_jerk_5d_v046_signal": {"func": f36_premium_target_marketcap_jerk_5d_v046_signal},
    "f36_premium_target_tangibles_jerk_5d_v047_signal": {"func": f36_premium_target_tangibles_jerk_5d_v047_signal},
    "f36_premium_target_tangible_per_val_jerk_5d_v048_signal": {"func": f36_premium_target_tangible_per_val_jerk_5d_v048_signal},
    "f36_premium_target_pb_jerk_10d_v049_signal": {"func": f36_premium_target_pb_jerk_10d_v049_signal},
    "f36_premium_target_marketcap_jerk_10d_v050_signal": {"func": f36_premium_target_marketcap_jerk_10d_v050_signal},
    "f36_premium_target_tangibles_jerk_10d_v051_signal": {"func": f36_premium_target_tangibles_jerk_10d_v051_signal},
    "f36_premium_target_tangible_per_val_jerk_10d_v052_signal": {"func": f36_premium_target_tangible_per_val_jerk_10d_v052_signal},
    "f36_premium_target_pb_jerk_21d_v053_signal": {"func": f36_premium_target_pb_jerk_21d_v053_signal},
    "f36_premium_target_marketcap_jerk_21d_v054_signal": {"func": f36_premium_target_marketcap_jerk_21d_v054_signal},
    "f36_premium_target_tangibles_jerk_21d_v055_signal": {"func": f36_premium_target_tangibles_jerk_21d_v055_signal},
    "f36_premium_target_tangible_per_val_jerk_21d_v056_signal": {"func": f36_premium_target_tangible_per_val_jerk_21d_v056_signal},
    "f36_premium_target_pb_jerk_42d_v057_signal": {"func": f36_premium_target_pb_jerk_42d_v057_signal},
    "f36_premium_target_marketcap_jerk_42d_v058_signal": {"func": f36_premium_target_marketcap_jerk_42d_v058_signal},
    "f36_premium_target_tangibles_jerk_42d_v059_signal": {"func": f36_premium_target_tangibles_jerk_42d_v059_signal},
    "f36_premium_target_tangible_per_val_jerk_42d_v060_signal": {"func": f36_premium_target_tangible_per_val_jerk_42d_v060_signal},
    "f36_premium_target_pb_jerk_63d_v061_signal": {"func": f36_premium_target_pb_jerk_63d_v061_signal},
    "f36_premium_target_marketcap_jerk_63d_v062_signal": {"func": f36_premium_target_marketcap_jerk_63d_v062_signal},
    "f36_premium_target_tangibles_jerk_63d_v063_signal": {"func": f36_premium_target_tangibles_jerk_63d_v063_signal},
    "f36_premium_target_tangible_per_val_jerk_63d_v064_signal": {"func": f36_premium_target_tangible_per_val_jerk_63d_v064_signal},
    "f36_premium_target_pb_jerk_126d_v065_signal": {"func": f36_premium_target_pb_jerk_126d_v065_signal},
    "f36_premium_target_marketcap_jerk_126d_v066_signal": {"func": f36_premium_target_marketcap_jerk_126d_v066_signal},
    "f36_premium_target_tangibles_jerk_126d_v067_signal": {"func": f36_premium_target_tangibles_jerk_126d_v067_signal},
    "f36_premium_target_tangible_per_val_jerk_126d_v068_signal": {"func": f36_premium_target_tangible_per_val_jerk_126d_v068_signal},
    "f36_premium_target_pb_jerk_252d_v069_signal": {"func": f36_premium_target_pb_jerk_252d_v069_signal},
    "f36_premium_target_marketcap_jerk_252d_v070_signal": {"func": f36_premium_target_marketcap_jerk_252d_v070_signal},
    "f36_premium_target_tangibles_jerk_252d_v071_signal": {"func": f36_premium_target_tangibles_jerk_252d_v071_signal},
    "f36_premium_target_tangible_per_val_jerk_252d_v072_signal": {"func": f36_premium_target_tangible_per_val_jerk_252d_v072_signal},
    "f36_premium_target_pb_jerk_504d_v073_signal": {"func": f36_premium_target_pb_jerk_504d_v073_signal},
    "f36_premium_target_marketcap_jerk_504d_v074_signal": {"func": f36_premium_target_marketcap_jerk_504d_v074_signal},
    "f36_premium_target_tangibles_jerk_504d_v075_signal": {"func": f36_premium_target_tangibles_jerk_504d_v075_signal},
    "f36_premium_target_tangible_per_val_jerk_504d_v076_signal": {"func": f36_premium_target_tangible_per_val_jerk_504d_v076_signal},
    "f36_premium_target_pb_jerk_756d_v077_signal": {"func": f36_premium_target_pb_jerk_756d_v077_signal},
    "f36_premium_target_marketcap_jerk_756d_v078_signal": {"func": f36_premium_target_marketcap_jerk_756d_v078_signal},
    "f36_premium_target_tangibles_jerk_756d_v079_signal": {"func": f36_premium_target_tangibles_jerk_756d_v079_signal},
    "f36_premium_target_tangible_per_val_jerk_756d_v080_signal": {"func": f36_premium_target_tangible_per_val_jerk_756d_v080_signal},
    "f36_premium_target_pb_jerk_1008d_v081_signal": {"func": f36_premium_target_pb_jerk_1008d_v081_signal},
    "f36_premium_target_marketcap_jerk_1008d_v082_signal": {"func": f36_premium_target_marketcap_jerk_1008d_v082_signal},
    "f36_premium_target_tangibles_jerk_1008d_v083_signal": {"func": f36_premium_target_tangibles_jerk_1008d_v083_signal},
    "f36_premium_target_tangible_per_val_jerk_1008d_v084_signal": {"func": f36_premium_target_tangible_per_val_jerk_1008d_v084_signal},
    "f36_premium_target_pb_jerk_1260d_v085_signal": {"func": f36_premium_target_pb_jerk_1260d_v085_signal},
    "f36_premium_target_marketcap_jerk_1260d_v086_signal": {"func": f36_premium_target_marketcap_jerk_1260d_v086_signal},
    "f36_premium_target_tangibles_jerk_1260d_v087_signal": {"func": f36_premium_target_tangibles_jerk_1260d_v087_signal},
    "f36_premium_target_tangible_per_val_jerk_1260d_v088_signal": {"func": f36_premium_target_tangible_per_val_jerk_1260d_v088_signal},
    "f36_premium_target_pb_slope_diff_norm_5d_v089_signal": {"func": f36_premium_target_pb_slope_diff_norm_5d_v089_signal},
    "f36_premium_target_marketcap_slope_diff_norm_5d_v090_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_5d_v090_signal},
    "f36_premium_target_tangibles_slope_diff_norm_5d_v091_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_5d_v091_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_5d_v092_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_5d_v092_signal},
    "f36_premium_target_pb_slope_diff_norm_10d_v093_signal": {"func": f36_premium_target_pb_slope_diff_norm_10d_v093_signal},
    "f36_premium_target_marketcap_slope_diff_norm_10d_v094_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_10d_v094_signal},
    "f36_premium_target_tangibles_slope_diff_norm_10d_v095_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_10d_v095_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_10d_v096_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_10d_v096_signal},
    "f36_premium_target_pb_slope_diff_norm_21d_v097_signal": {"func": f36_premium_target_pb_slope_diff_norm_21d_v097_signal},
    "f36_premium_target_marketcap_slope_diff_norm_21d_v098_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_21d_v098_signal},
    "f36_premium_target_tangibles_slope_diff_norm_21d_v099_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_21d_v099_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_21d_v100_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_21d_v100_signal},
    "f36_premium_target_pb_slope_diff_norm_42d_v101_signal": {"func": f36_premium_target_pb_slope_diff_norm_42d_v101_signal},
    "f36_premium_target_marketcap_slope_diff_norm_42d_v102_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_42d_v102_signal},
    "f36_premium_target_tangibles_slope_diff_norm_42d_v103_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_42d_v103_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_42d_v104_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_42d_v104_signal},
    "f36_premium_target_pb_slope_diff_norm_63d_v105_signal": {"func": f36_premium_target_pb_slope_diff_norm_63d_v105_signal},
    "f36_premium_target_marketcap_slope_diff_norm_63d_v106_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_63d_v106_signal},
    "f36_premium_target_tangibles_slope_diff_norm_63d_v107_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_63d_v107_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_63d_v108_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_63d_v108_signal},
    "f36_premium_target_pb_slope_diff_norm_126d_v109_signal": {"func": f36_premium_target_pb_slope_diff_norm_126d_v109_signal},
    "f36_premium_target_marketcap_slope_diff_norm_126d_v110_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_126d_v110_signal},
    "f36_premium_target_tangibles_slope_diff_norm_126d_v111_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_126d_v111_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_126d_v112_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_126d_v112_signal},
    "f36_premium_target_pb_slope_diff_norm_252d_v113_signal": {"func": f36_premium_target_pb_slope_diff_norm_252d_v113_signal},
    "f36_premium_target_marketcap_slope_diff_norm_252d_v114_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_252d_v114_signal},
    "f36_premium_target_tangibles_slope_diff_norm_252d_v115_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_252d_v115_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_252d_v116_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_252d_v116_signal},
    "f36_premium_target_pb_slope_diff_norm_504d_v117_signal": {"func": f36_premium_target_pb_slope_diff_norm_504d_v117_signal},
    "f36_premium_target_marketcap_slope_diff_norm_504d_v118_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_504d_v118_signal},
    "f36_premium_target_tangibles_slope_diff_norm_504d_v119_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_504d_v119_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_504d_v120_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_504d_v120_signal},
    "f36_premium_target_pb_slope_diff_norm_756d_v121_signal": {"func": f36_premium_target_pb_slope_diff_norm_756d_v121_signal},
    "f36_premium_target_marketcap_slope_diff_norm_756d_v122_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_756d_v122_signal},
    "f36_premium_target_tangibles_slope_diff_norm_756d_v123_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_756d_v123_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_756d_v124_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_756d_v124_signal},
    "f36_premium_target_pb_slope_diff_norm_1008d_v125_signal": {"func": f36_premium_target_pb_slope_diff_norm_1008d_v125_signal},
    "f36_premium_target_marketcap_slope_diff_norm_1008d_v126_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_1008d_v126_signal},
    "f36_premium_target_tangibles_slope_diff_norm_1008d_v127_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_1008d_v127_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_1008d_v128_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_1008d_v128_signal},
    "f36_premium_target_pb_slope_diff_norm_1260d_v129_signal": {"func": f36_premium_target_pb_slope_diff_norm_1260d_v129_signal},
    "f36_premium_target_marketcap_slope_diff_norm_1260d_v130_signal": {"func": f36_premium_target_marketcap_slope_diff_norm_1260d_v130_signal},
    "f36_premium_target_tangibles_slope_diff_norm_1260d_v131_signal": {"func": f36_premium_target_tangibles_slope_diff_norm_1260d_v131_signal},
    "f36_premium_target_tangible_per_val_slope_diff_norm_1260d_v132_signal": {"func": f36_premium_target_tangible_per_val_slope_diff_norm_1260d_v132_signal},
    "f36_premium_target_pb_mom_z_5d_v133_signal": {"func": f36_premium_target_pb_mom_z_5d_v133_signal},
    "f36_premium_target_marketcap_mom_z_5d_v134_signal": {"func": f36_premium_target_marketcap_mom_z_5d_v134_signal},
    "f36_premium_target_tangibles_mom_z_5d_v135_signal": {"func": f36_premium_target_tangibles_mom_z_5d_v135_signal},
    "f36_premium_target_tangible_per_val_mom_z_5d_v136_signal": {"func": f36_premium_target_tangible_per_val_mom_z_5d_v136_signal},
    "f36_premium_target_pb_mom_z_10d_v137_signal": {"func": f36_premium_target_pb_mom_z_10d_v137_signal},
    "f36_premium_target_marketcap_mom_z_10d_v138_signal": {"func": f36_premium_target_marketcap_mom_z_10d_v138_signal},
    "f36_premium_target_tangibles_mom_z_10d_v139_signal": {"func": f36_premium_target_tangibles_mom_z_10d_v139_signal},
    "f36_premium_target_tangible_per_val_mom_z_10d_v140_signal": {"func": f36_premium_target_tangible_per_val_mom_z_10d_v140_signal},
    "f36_premium_target_pb_mom_z_21d_v141_signal": {"func": f36_premium_target_pb_mom_z_21d_v141_signal},
    "f36_premium_target_marketcap_mom_z_21d_v142_signal": {"func": f36_premium_target_marketcap_mom_z_21d_v142_signal},
    "f36_premium_target_tangibles_mom_z_21d_v143_signal": {"func": f36_premium_target_tangibles_mom_z_21d_v143_signal},
    "f36_premium_target_tangible_per_val_mom_z_21d_v144_signal": {"func": f36_premium_target_tangible_per_val_mom_z_21d_v144_signal},
    "f36_premium_target_pb_mom_z_42d_v145_signal": {"func": f36_premium_target_pb_mom_z_42d_v145_signal},
    "f36_premium_target_marketcap_mom_z_42d_v146_signal": {"func": f36_premium_target_marketcap_mom_z_42d_v146_signal},
    "f36_premium_target_tangibles_mom_z_42d_v147_signal": {"func": f36_premium_target_tangibles_mom_z_42d_v147_signal},
    "f36_premium_target_tangible_per_val_mom_z_42d_v148_signal": {"func": f36_premium_target_tangible_per_val_mom_z_42d_v148_signal},
    "f36_premium_target_pb_mom_z_63d_v149_signal": {"func": f36_premium_target_pb_mom_z_63d_v149_signal},
    "f36_premium_target_marketcap_mom_z_63d_v150_signal": {"func": f36_premium_target_marketcap_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 36...")
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
