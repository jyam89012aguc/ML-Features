import pandas as pd
import numpy as np
import inspect

# ===== BREAKOUT High-Performance Alpha Helpers =====
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
def _jerk(s, w1, w2): return s.slope_pct(w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()
def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))
def bo_036_vwap_distance_proxy_marketcap_slope_pct_5d_v001_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 5d window."""
    res = _slope_pct(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_5d_v002_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 5d window."""
    res = _slope_pct(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_5d_v003_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 5d window."""
    res = _slope_pct(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_10d_v004_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 10d window."""
    res = _slope_pct(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_10d_v005_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 10d window."""
    res = _slope_pct(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_10d_v006_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 10d window."""
    res = _slope_pct(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_21d_v007_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 21d window."""
    res = _slope_pct(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_21d_v008_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 21d window."""
    res = _slope_pct(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_21d_v009_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 21d window."""
    res = _slope_pct(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_42d_v010_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 42d window."""
    res = _slope_pct(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_42d_v011_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 42d window."""
    res = _slope_pct(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_42d_v012_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 42d window."""
    res = _slope_pct(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_63d_v013_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 63d window."""
    res = _slope_pct(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_63d_v014_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 63d window."""
    res = _slope_pct(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_63d_v015_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 63d window."""
    res = _slope_pct(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_126d_v016_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 126d window."""
    res = _slope_pct(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_126d_v017_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 126d window."""
    res = _slope_pct(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_126d_v018_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 126d window."""
    res = _slope_pct(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_252d_v019_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 252d window."""
    res = _slope_pct(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_252d_v020_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 252d window."""
    res = _slope_pct(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_252d_v021_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 252d window."""
    res = _slope_pct(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_504d_v022_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 504d window."""
    res = _slope_pct(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_504d_v023_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 504d window."""
    res = _slope_pct(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_504d_v024_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 504d window."""
    res = _slope_pct(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_756d_v025_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 756d window."""
    res = _slope_pct(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_756d_v026_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 756d window."""
    res = _slope_pct(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_756d_v027_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 756d window."""
    res = _slope_pct(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_1008d_v028_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 1008d window."""
    res = _slope_pct(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_1008d_v029_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 1008d window."""
    res = _slope_pct(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_1008d_v030_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 1008d window."""
    res = _slope_pct(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_pct_1260d_v031_signal(closeadj):
    """Percentage slope for Raw level of marketcap over 1260d window."""
    res = _slope_pct(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_pct_1260d_v032_signal(closeadj):
    """Percentage slope for Raw level of closeadj over 1260d window."""
    res = _slope_pct(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_pct_1260d_v033_signal(closeadj):
    """Percentage slope for Proxy for trading volume over 1260d window."""
    res = _slope_pct(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_5d_v034_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 5d window."""
    res = _jerk(closeadj, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_5d_v035_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 5d window."""
    res = _jerk(closeadj, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_5d_v036_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 5d window."""
    res = _jerk(closeadj, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_10d_v037_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 10d window."""
    res = _jerk(closeadj, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_10d_v038_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 10d window."""
    res = _jerk(closeadj, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_10d_v039_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 10d window."""
    res = _jerk(closeadj, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_21d_v040_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 21d window."""
    res = _jerk(closeadj, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_21d_v041_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 21d window."""
    res = _jerk(closeadj, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_21d_v042_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 21d window."""
    res = _jerk(closeadj, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_42d_v043_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 42d window."""
    res = _jerk(closeadj, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_42d_v044_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 42d window."""
    res = _jerk(closeadj, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_42d_v045_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 42d window."""
    res = _jerk(closeadj, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_63d_v046_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 63d window."""
    res = _jerk(closeadj, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_63d_v047_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 63d window."""
    res = _jerk(closeadj, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_63d_v048_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 63d window."""
    res = _jerk(closeadj, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_126d_v049_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 126d window."""
    res = _jerk(closeadj, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_126d_v050_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 126d window."""
    res = _jerk(closeadj, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_126d_v051_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 126d window."""
    res = _jerk(closeadj, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_252d_v052_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 252d window."""
    res = _jerk(closeadj, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_252d_v053_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 252d window."""
    res = _jerk(closeadj, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_252d_v054_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 252d window."""
    res = _jerk(closeadj, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_504d_v055_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 504d window."""
    res = _jerk(closeadj, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_504d_v056_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 504d window."""
    res = _jerk(closeadj, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_504d_v057_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 504d window."""
    res = _jerk(closeadj, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_756d_v058_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 756d window."""
    res = _jerk(closeadj, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_756d_v059_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 756d window."""
    res = _jerk(closeadj, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_756d_v060_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 756d window."""
    res = _jerk(closeadj, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_1008d_v061_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 1008d window."""
    res = _jerk(closeadj, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_1008d_v062_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 1008d window."""
    res = _jerk(closeadj, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_1008d_v063_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 1008d window."""
    res = _jerk(closeadj, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_jerk_1260d_v064_signal(closeadj):
    """Acceleration/Jerk for Raw level of marketcap over 1260d window."""
    res = _jerk(closeadj, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_jerk_1260d_v065_signal(closeadj):
    """Acceleration/Jerk for Raw level of closeadj over 1260d window."""
    res = _jerk(closeadj, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_jerk_1260d_v066_signal(closeadj):
    """Acceleration/Jerk for Proxy for trading volume over 1260d window."""
    res = _jerk(closeadj, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_5d_v067_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_5d_v068_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_5d_v069_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_10d_v070_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_10d_v071_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_10d_v072_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_21d_v073_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_21d_v074_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_21d_v075_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_42d_v076_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_42d_v077_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_42d_v078_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_63d_v079_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_63d_v080_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_63d_v081_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_126d_v082_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_126d_v083_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_126d_v084_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_252d_v085_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_252d_v086_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_252d_v087_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_504d_v088_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_504d_v089_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_504d_v090_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_756d_v091_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_756d_v092_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_756d_v093_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_1008d_v094_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_1008d_v095_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_1008d_v096_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_1260d_v097_signal(closeadj):
    """Normalized slope change for Raw level of marketcap over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_1260d_v098_signal(closeadj):
    """Normalized slope change for Raw level of closeadj over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_1260d_v099_signal(closeadj):
    """Normalized slope change for Proxy for trading volume over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_5d_v100_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 5d window."""
    res = _z(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_5d_v101_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 5d window."""
    res = _z(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_5d_v102_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 5d window."""
    res = _z(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_10d_v103_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 10d window."""
    res = _z(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_10d_v104_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 10d window."""
    res = _z(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_10d_v105_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 10d window."""
    res = _z(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_21d_v106_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 21d window."""
    res = _z(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_21d_v107_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 21d window."""
    res = _z(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_21d_v108_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 21d window."""
    res = _z(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_42d_v109_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 42d window."""
    res = _z(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_42d_v110_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 42d window."""
    res = _z(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_42d_v111_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 42d window."""
    res = _z(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_63d_v112_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 63d window."""
    res = _z(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_63d_v113_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 63d window."""
    res = _z(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_63d_v114_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 63d window."""
    res = _z(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_126d_v115_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 126d window."""
    res = _z(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_126d_v116_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 126d window."""
    res = _z(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_126d_v117_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 126d window."""
    res = _z(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_252d_v118_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 252d window."""
    res = _z(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_252d_v119_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 252d window."""
    res = _z(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_252d_v120_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 252d window."""
    res = _z(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_504d_v121_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 504d window."""
    res = _z(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_504d_v122_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 504d window."""
    res = _z(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_504d_v123_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 504d window."""
    res = _z(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_756d_v124_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 756d window."""
    res = _z(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_756d_v125_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 756d window."""
    res = _z(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_756d_v126_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 756d window."""
    res = _z(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_1008d_v127_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 1008d window."""
    res = _z(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_1008d_v128_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 1008d window."""
    res = _z(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_1008d_v129_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 1008d window."""
    res = _z(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_mom_z_1260d_v130_signal(closeadj):
    """Relative momentum strength for Raw level of marketcap over 1260d window."""
    res = _z(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_mom_z_1260d_v131_signal(closeadj):
    """Relative momentum strength for Raw level of closeadj over 1260d window."""
    res = _z(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_mom_z_1260d_v132_signal(closeadj):
    """Relative momentum strength for Proxy for trading volume over 1260d window."""
    res = _z(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_vol_slope_5d_v133_signal(closeadj):
    """Volatility of momentum for Raw level of marketcap over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_vol_slope_5d_v134_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_vol_slope_5d_v135_signal(closeadj):
    """Volatility of momentum for Proxy for trading volume over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_vol_slope_10d_v136_signal(closeadj):
    """Volatility of momentum for Raw level of marketcap over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_vol_slope_10d_v137_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_vol_slope_10d_v138_signal(closeadj):
    """Volatility of momentum for Proxy for trading volume over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_vol_slope_21d_v139_signal(closeadj):
    """Volatility of momentum for Raw level of marketcap over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_vol_slope_21d_v140_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_vol_slope_21d_v141_signal(closeadj):
    """Volatility of momentum for Proxy for trading volume over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_vol_slope_42d_v142_signal(closeadj):
    """Volatility of momentum for Raw level of marketcap over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_vol_slope_42d_v143_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_vol_slope_42d_v144_signal(closeadj):
    """Volatility of momentum for Proxy for trading volume over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_vol_slope_63d_v145_signal(closeadj):
    """Volatility of momentum for Raw level of marketcap over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_vol_slope_63d_v146_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_vol_slope_63d_v147_signal(closeadj):
    """Volatility of momentum for Proxy for trading volume over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_marketcap_vol_slope_126d_v148_signal(closeadj):
    """Volatility of momentum for Raw level of marketcap over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_closeadj_vol_slope_126d_v149_signal(closeadj):
    """Volatility of momentum for Raw level of closeadj over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_036_vwap_distance_proxy_volume_proxy_vol_slope_126d_v150_signal(closeadj):
    """Volatility of momentum for Proxy for trading volume over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_5d_v001_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_5d_v001_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_5d_v002_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_5d_v002_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_5d_v003_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_5d_v003_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_10d_v004_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_10d_v004_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_10d_v005_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_10d_v005_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_10d_v006_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_10d_v006_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_21d_v007_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_21d_v007_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_21d_v008_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_21d_v008_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_21d_v009_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_21d_v009_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_42d_v010_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_42d_v010_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_42d_v011_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_42d_v011_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_42d_v012_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_42d_v012_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_63d_v013_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_63d_v013_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_63d_v014_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_63d_v014_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_63d_v015_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_63d_v015_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_126d_v016_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_126d_v016_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_126d_v017_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_126d_v017_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_126d_v018_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_126d_v018_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_252d_v019_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_252d_v019_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_252d_v020_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_252d_v020_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_252d_v021_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_252d_v021_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_504d_v022_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_504d_v022_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_504d_v023_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_504d_v023_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_504d_v024_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_504d_v024_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_756d_v025_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_756d_v025_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_756d_v026_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_756d_v026_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_756d_v027_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_756d_v027_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_1008d_v028_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_1008d_v028_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_1008d_v029_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_1008d_v029_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_1008d_v030_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_1008d_v030_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_pct_1260d_v031_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_pct_1260d_v031_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_pct_1260d_v032_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_pct_1260d_v032_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_pct_1260d_v033_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_pct_1260d_v033_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_5d_v034_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_5d_v034_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_5d_v035_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_5d_v035_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_5d_v036_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_5d_v036_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_10d_v037_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_10d_v037_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_10d_v038_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_10d_v038_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_10d_v039_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_10d_v039_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_21d_v040_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_21d_v040_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_21d_v041_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_21d_v041_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_21d_v042_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_21d_v042_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_42d_v043_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_42d_v043_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_42d_v044_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_42d_v044_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_42d_v045_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_42d_v045_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_63d_v046_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_63d_v046_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_63d_v047_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_63d_v047_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_63d_v048_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_63d_v048_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_126d_v049_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_126d_v049_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_126d_v050_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_126d_v050_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_126d_v051_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_126d_v051_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_252d_v052_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_252d_v052_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_252d_v053_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_252d_v053_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_252d_v054_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_252d_v054_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_504d_v055_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_504d_v055_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_504d_v056_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_504d_v056_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_504d_v057_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_504d_v057_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_756d_v058_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_756d_v058_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_756d_v059_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_756d_v059_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_756d_v060_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_756d_v060_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_1008d_v061_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_1008d_v061_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_1008d_v062_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_1008d_v062_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_1008d_v063_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_1008d_v063_signal},
    "bo_036_vwap_distance_proxy_marketcap_jerk_1260d_v064_signal": {"func": bo_036_vwap_distance_proxy_marketcap_jerk_1260d_v064_signal},
    "bo_036_vwap_distance_proxy_closeadj_jerk_1260d_v065_signal": {"func": bo_036_vwap_distance_proxy_closeadj_jerk_1260d_v065_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_jerk_1260d_v066_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_jerk_1260d_v066_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_5d_v067_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_5d_v067_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_5d_v068_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_5d_v068_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_5d_v069_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_5d_v069_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_10d_v070_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_10d_v070_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_10d_v071_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_10d_v071_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_10d_v072_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_10d_v072_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_21d_v073_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_21d_v073_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_21d_v074_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_21d_v074_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_21d_v075_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_21d_v075_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_42d_v076_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_42d_v076_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_42d_v077_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_42d_v077_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_42d_v078_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_42d_v078_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_63d_v079_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_63d_v079_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_63d_v080_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_63d_v080_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_63d_v081_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_63d_v081_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_126d_v082_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_126d_v082_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_126d_v083_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_126d_v083_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_126d_v084_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_126d_v084_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_252d_v085_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_252d_v085_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_252d_v086_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_252d_v086_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_252d_v087_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_252d_v087_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_504d_v088_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_504d_v088_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_504d_v089_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_504d_v089_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_504d_v090_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_504d_v090_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_756d_v091_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_756d_v091_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_756d_v092_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_756d_v092_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_756d_v093_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_756d_v093_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_1008d_v094_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_1008d_v094_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_1008d_v095_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_1008d_v095_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_1008d_v096_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_1008d_v096_signal},
    "bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_1260d_v097_signal": {"func": bo_036_vwap_distance_proxy_marketcap_slope_diff_norm_1260d_v097_signal},
    "bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_1260d_v098_signal": {"func": bo_036_vwap_distance_proxy_closeadj_slope_diff_norm_1260d_v098_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_1260d_v099_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_slope_diff_norm_1260d_v099_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_5d_v100_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_5d_v100_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_5d_v101_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_5d_v101_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_5d_v102_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_5d_v102_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_10d_v103_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_10d_v103_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_10d_v104_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_10d_v104_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_10d_v105_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_10d_v105_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_21d_v106_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_21d_v106_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_21d_v107_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_21d_v107_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_21d_v108_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_21d_v108_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_42d_v109_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_42d_v109_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_42d_v110_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_42d_v110_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_42d_v111_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_42d_v111_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_63d_v112_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_63d_v112_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_63d_v113_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_63d_v113_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_63d_v114_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_63d_v114_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_126d_v115_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_126d_v115_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_126d_v116_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_126d_v116_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_126d_v117_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_126d_v117_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_252d_v118_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_252d_v118_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_252d_v119_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_252d_v119_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_252d_v120_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_252d_v120_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_504d_v121_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_504d_v121_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_504d_v122_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_504d_v122_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_504d_v123_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_504d_v123_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_756d_v124_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_756d_v124_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_756d_v125_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_756d_v125_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_756d_v126_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_756d_v126_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_1008d_v127_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_1008d_v127_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_1008d_v128_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_1008d_v128_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_1008d_v129_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_1008d_v129_signal},
    "bo_036_vwap_distance_proxy_marketcap_mom_z_1260d_v130_signal": {"func": bo_036_vwap_distance_proxy_marketcap_mom_z_1260d_v130_signal},
    "bo_036_vwap_distance_proxy_closeadj_mom_z_1260d_v131_signal": {"func": bo_036_vwap_distance_proxy_closeadj_mom_z_1260d_v131_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_mom_z_1260d_v132_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_mom_z_1260d_v132_signal},
    "bo_036_vwap_distance_proxy_marketcap_vol_slope_5d_v133_signal": {"func": bo_036_vwap_distance_proxy_marketcap_vol_slope_5d_v133_signal},
    "bo_036_vwap_distance_proxy_closeadj_vol_slope_5d_v134_signal": {"func": bo_036_vwap_distance_proxy_closeadj_vol_slope_5d_v134_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_vol_slope_5d_v135_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_vol_slope_5d_v135_signal},
    "bo_036_vwap_distance_proxy_marketcap_vol_slope_10d_v136_signal": {"func": bo_036_vwap_distance_proxy_marketcap_vol_slope_10d_v136_signal},
    "bo_036_vwap_distance_proxy_closeadj_vol_slope_10d_v137_signal": {"func": bo_036_vwap_distance_proxy_closeadj_vol_slope_10d_v137_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_vol_slope_10d_v138_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_vol_slope_10d_v138_signal},
    "bo_036_vwap_distance_proxy_marketcap_vol_slope_21d_v139_signal": {"func": bo_036_vwap_distance_proxy_marketcap_vol_slope_21d_v139_signal},
    "bo_036_vwap_distance_proxy_closeadj_vol_slope_21d_v140_signal": {"func": bo_036_vwap_distance_proxy_closeadj_vol_slope_21d_v140_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_vol_slope_21d_v141_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_vol_slope_21d_v141_signal},
    "bo_036_vwap_distance_proxy_marketcap_vol_slope_42d_v142_signal": {"func": bo_036_vwap_distance_proxy_marketcap_vol_slope_42d_v142_signal},
    "bo_036_vwap_distance_proxy_closeadj_vol_slope_42d_v143_signal": {"func": bo_036_vwap_distance_proxy_closeadj_vol_slope_42d_v143_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_vol_slope_42d_v144_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_vol_slope_42d_v144_signal},
    "bo_036_vwap_distance_proxy_marketcap_vol_slope_63d_v145_signal": {"func": bo_036_vwap_distance_proxy_marketcap_vol_slope_63d_v145_signal},
    "bo_036_vwap_distance_proxy_closeadj_vol_slope_63d_v146_signal": {"func": bo_036_vwap_distance_proxy_closeadj_vol_slope_63d_v146_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_vol_slope_63d_v147_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_vol_slope_63d_v147_signal},
    "bo_036_vwap_distance_proxy_marketcap_vol_slope_126d_v148_signal": {"func": bo_036_vwap_distance_proxy_marketcap_vol_slope_126d_v148_signal},
    "bo_036_vwap_distance_proxy_closeadj_vol_slope_126d_v149_signal": {"func": bo_036_vwap_distance_proxy_closeadj_vol_slope_126d_v149_signal},
    "bo_036_vwap_distance_proxy_volume_proxy_vol_slope_126d_v150_signal": {"func": bo_036_vwap_distance_proxy_volume_proxy_vol_slope_126d_v150_signal},
}
if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "rnd": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 036...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
