import pandas as pd
import numpy as np
import inspect

# ===== Healthcare High-Performance Alpha Helpers =====
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

def f30_long_term_trend_momentum_capex_slope_pct_5d_v001_signal(capex):
    """Percentage slope for Raw level of capex over 5d window."""
    res = _slope_pct(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_5d_v002_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_5d_v003_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 5d window."""
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_5d_v004_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 5d window."""
    res = _slope_pct(_ratio(ebitda, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_10d_v005_signal(capex):
    """Percentage slope for Raw level of capex over 10d window."""
    res = _slope_pct(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_10d_v006_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_10d_v007_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 10d window."""
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_10d_v008_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 10d window."""
    res = _slope_pct(_ratio(ebitda, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_21d_v009_signal(capex):
    """Percentage slope for Raw level of capex over 21d window."""
    res = _slope_pct(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_21d_v010_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_21d_v011_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 21d window."""
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_21d_v012_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 21d window."""
    res = _slope_pct(_ratio(ebitda, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_42d_v013_signal(capex):
    """Percentage slope for Raw level of capex over 42d window."""
    res = _slope_pct(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_42d_v014_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_42d_v015_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 42d window."""
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_42d_v016_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 42d window."""
    res = _slope_pct(_ratio(ebitda, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_63d_v017_signal(capex):
    """Percentage slope for Raw level of capex over 63d window."""
    res = _slope_pct(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_63d_v018_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_63d_v019_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 63d window."""
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_63d_v020_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 63d window."""
    res = _slope_pct(_ratio(ebitda, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_126d_v021_signal(capex):
    """Percentage slope for Raw level of capex over 126d window."""
    res = _slope_pct(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_126d_v022_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_126d_v023_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 126d window."""
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_126d_v024_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 126d window."""
    res = _slope_pct(_ratio(ebitda, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_252d_v025_signal(capex):
    """Percentage slope for Raw level of capex over 252d window."""
    res = _slope_pct(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_252d_v026_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_252d_v027_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 252d window."""
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_252d_v028_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 252d window."""
    res = _slope_pct(_ratio(ebitda, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_504d_v029_signal(capex):
    """Percentage slope for Raw level of capex over 504d window."""
    res = _slope_pct(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_504d_v030_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_504d_v031_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 504d window."""
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_504d_v032_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 504d window."""
    res = _slope_pct(_ratio(ebitda, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_756d_v033_signal(capex):
    """Percentage slope for Raw level of capex over 756d window."""
    res = _slope_pct(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_756d_v034_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_756d_v035_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 756d window."""
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_756d_v036_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 756d window."""
    res = _slope_pct(_ratio(ebitda, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_1008d_v037_signal(capex):
    """Percentage slope for Raw level of capex over 1008d window."""
    res = _slope_pct(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_1008d_v038_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_1008d_v039_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1008d window."""
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_1008d_v040_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 1008d window."""
    res = _slope_pct(_ratio(ebitda, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_pct_1260d_v041_signal(capex):
    """Percentage slope for Raw level of capex over 1260d window."""
    res = _slope_pct(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_pct_1260d_v042_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_pct_1260d_v043_signal(ebitda):
    """Percentage slope for Raw level of ebitda over 1260d window."""
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_pct_1260d_v044_signal(ebitda, capex):
    """Percentage slope for Operating return on capex over 1260d window."""
    res = _slope_pct(_ratio(ebitda, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_5d_v045_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 5d window."""
    res = _jerk(capex, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_5d_v046_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_5d_v047_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 5d window."""
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_5d_v048_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 5d window."""
    res = _jerk(_ratio(ebitda, capex), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_10d_v049_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 10d window."""
    res = _jerk(capex, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_10d_v050_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_10d_v051_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 10d window."""
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_10d_v052_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 10d window."""
    res = _jerk(_ratio(ebitda, capex), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_21d_v053_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 21d window."""
    res = _jerk(capex, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_21d_v054_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_21d_v055_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 21d window."""
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_21d_v056_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 21d window."""
    res = _jerk(_ratio(ebitda, capex), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_42d_v057_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 42d window."""
    res = _jerk(capex, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_42d_v058_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_42d_v059_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 42d window."""
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_42d_v060_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 42d window."""
    res = _jerk(_ratio(ebitda, capex), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_63d_v061_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 63d window."""
    res = _jerk(capex, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_63d_v062_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_63d_v063_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 63d window."""
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_63d_v064_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 63d window."""
    res = _jerk(_ratio(ebitda, capex), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_126d_v065_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 126d window."""
    res = _jerk(capex, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_126d_v066_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_126d_v067_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 126d window."""
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_126d_v068_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 126d window."""
    res = _jerk(_ratio(ebitda, capex), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_252d_v069_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 252d window."""
    res = _jerk(capex, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_252d_v070_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_252d_v071_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 252d window."""
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_252d_v072_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 252d window."""
    res = _jerk(_ratio(ebitda, capex), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_504d_v073_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 504d window."""
    res = _jerk(capex, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_504d_v074_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_504d_v075_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 504d window."""
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_504d_v076_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 504d window."""
    res = _jerk(_ratio(ebitda, capex), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_756d_v077_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 756d window."""
    res = _jerk(capex, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_756d_v078_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_756d_v079_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 756d window."""
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_756d_v080_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 756d window."""
    res = _jerk(_ratio(ebitda, capex), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_1008d_v081_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 1008d window."""
    res = _jerk(capex, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_1008d_v082_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_1008d_v083_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1008d window."""
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_1008d_v084_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 1008d window."""
    res = _jerk(_ratio(ebitda, capex), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_jerk_1260d_v085_signal(capex):
    """Acceleration/Jerk for Raw level of capex over 1260d window."""
    res = _jerk(capex, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_jerk_1260d_v086_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_jerk_1260d_v087_signal(ebitda):
    """Acceleration/Jerk for Raw level of ebitda over 1260d window."""
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_jerk_1260d_v088_signal(ebitda, capex):
    """Acceleration/Jerk for Operating return on capex over 1260d window."""
    res = _jerk(_ratio(ebitda, capex), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_5d_v089_signal(capex):
    """Normalized slope change for Raw level of capex over 5d window."""
    res = (_slope_pct(capex, 5).diff(5) / _sma(capex.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_5d_v090_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_5d_v091_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 5d window."""
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_5d_v092_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 5d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 5).diff(5) / _sma(_ratio(ebitda, capex).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_10d_v093_signal(capex):
    """Normalized slope change for Raw level of capex over 10d window."""
    res = (_slope_pct(capex, 10).diff(10) / _sma(capex.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_10d_v094_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_10d_v095_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 10d window."""
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_10d_v096_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 10d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 10).diff(10) / _sma(_ratio(ebitda, capex).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_21d_v097_signal(capex):
    """Normalized slope change for Raw level of capex over 21d window."""
    res = (_slope_pct(capex, 21).diff(21) / _sma(capex.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_21d_v098_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_21d_v099_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 21d window."""
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_21d_v100_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 21d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 21).diff(21) / _sma(_ratio(ebitda, capex).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_42d_v101_signal(capex):
    """Normalized slope change for Raw level of capex over 42d window."""
    res = (_slope_pct(capex, 42).diff(42) / _sma(capex.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_42d_v102_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_42d_v103_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 42d window."""
    res = (_slope_pct(ebitda, 42).diff(42) / _sma(ebitda.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_42d_v104_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 42d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 42).diff(42) / _sma(_ratio(ebitda, capex).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_63d_v105_signal(capex):
    """Normalized slope change for Raw level of capex over 63d window."""
    res = (_slope_pct(capex, 63).diff(63) / _sma(capex.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_63d_v106_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_63d_v107_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 63d window."""
    res = (_slope_pct(ebitda, 63).diff(63) / _sma(ebitda.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_63d_v108_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 63d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 63).diff(63) / _sma(_ratio(ebitda, capex).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_126d_v109_signal(capex):
    """Normalized slope change for Raw level of capex over 126d window."""
    res = (_slope_pct(capex, 126).diff(126) / _sma(capex.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_126d_v110_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_126d_v111_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 126d window."""
    res = (_slope_pct(ebitda, 126).diff(126) / _sma(ebitda.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_126d_v112_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 126d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 126).diff(126) / _sma(_ratio(ebitda, capex).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_252d_v113_signal(capex):
    """Normalized slope change for Raw level of capex over 252d window."""
    res = (_slope_pct(capex, 252).diff(252) / _sma(capex.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_252d_v114_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_252d_v115_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 252d window."""
    res = (_slope_pct(ebitda, 252).diff(252) / _sma(ebitda.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_252d_v116_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 252d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 252).diff(252) / _sma(_ratio(ebitda, capex).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_504d_v117_signal(capex):
    """Normalized slope change for Raw level of capex over 504d window."""
    res = (_slope_pct(capex, 504).diff(504) / _sma(capex.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_504d_v118_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_504d_v119_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 504d window."""
    res = (_slope_pct(ebitda, 504).diff(504) / _sma(ebitda.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_504d_v120_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 504d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 504).diff(504) / _sma(_ratio(ebitda, capex).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_756d_v121_signal(capex):
    """Normalized slope change for Raw level of capex over 756d window."""
    res = (_slope_pct(capex, 756).diff(756) / _sma(capex.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_756d_v122_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_756d_v123_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 756d window."""
    res = (_slope_pct(ebitda, 756).diff(756) / _sma(ebitda.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_756d_v124_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 756d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 756).diff(756) / _sma(_ratio(ebitda, capex).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_1008d_v125_signal(capex):
    """Normalized slope change for Raw level of capex over 1008d window."""
    res = (_slope_pct(capex, 1008).diff(1008) / _sma(capex.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_1008d_v126_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_1008d_v127_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 1008d window."""
    res = (_slope_pct(ebitda, 1008).diff(1008) / _sma(ebitda.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_1008d_v128_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 1008d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 1008).diff(1008) / _sma(_ratio(ebitda, capex).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_slope_diff_norm_1260d_v129_signal(capex):
    """Normalized slope change for Raw level of capex over 1260d window."""
    res = (_slope_pct(capex, 1260).diff(1260) / _sma(capex.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_slope_diff_norm_1260d_v130_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_slope_diff_norm_1260d_v131_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 1260d window."""
    res = (_slope_pct(ebitda, 1260).diff(1260) / _sma(ebitda.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_slope_diff_norm_1260d_v132_signal(ebitda, capex):
    """Normalized slope change for Operating return on capex over 1260d window."""
    res = (_slope_pct(_ratio(ebitda, capex), 1260).diff(1260) / _sma(_ratio(ebitda, capex).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_mom_z_5d_v133_signal(capex):
    """Relative momentum strength for Raw level of capex over 5d window."""
    res = _z(_slope_pct(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_mom_z_5d_v134_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_mom_z_5d_v135_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 5d window."""
    res = _z(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_mom_z_5d_v136_signal(ebitda, capex):
    """Relative momentum strength for Operating return on capex over 5d window."""
    res = _z(_slope_pct(_ratio(ebitda, capex), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_mom_z_10d_v137_signal(capex):
    """Relative momentum strength for Raw level of capex over 10d window."""
    res = _z(_slope_pct(capex, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_mom_z_10d_v138_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_mom_z_10d_v139_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 10d window."""
    res = _z(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_mom_z_10d_v140_signal(ebitda, capex):
    """Relative momentum strength for Operating return on capex over 10d window."""
    res = _z(_slope_pct(_ratio(ebitda, capex), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_mom_z_21d_v141_signal(capex):
    """Relative momentum strength for Raw level of capex over 21d window."""
    res = _z(_slope_pct(capex, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_mom_z_21d_v142_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_mom_z_21d_v143_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 21d window."""
    res = _z(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_mom_z_21d_v144_signal(ebitda, capex):
    """Relative momentum strength for Operating return on capex over 21d window."""
    res = _z(_slope_pct(_ratio(ebitda, capex), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_mom_z_42d_v145_signal(capex):
    """Relative momentum strength for Raw level of capex over 42d window."""
    res = _z(_slope_pct(capex, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_mom_z_42d_v146_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_ebitda_mom_z_42d_v147_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 42d window."""
    res = _z(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_roi_mom_z_42d_v148_signal(ebitda, capex):
    """Relative momentum strength for Operating return on capex over 42d window."""
    res = _z(_slope_pct(_ratio(ebitda, capex), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_capex_mom_z_63d_v149_signal(capex):
    """Relative momentum strength for Raw level of capex over 63d window."""
    res = _z(_slope_pct(capex, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_long_term_trend_momentum_revenue_mom_z_63d_v150_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f30_long_term_trend_momentum_capex_slope_pct_5d_v001_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_5d_v001_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_5d_v002_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_5d_v002_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_5d_v003_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_5d_v003_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_5d_v004_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_5d_v004_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_10d_v005_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_10d_v005_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_10d_v006_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_10d_v006_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_10d_v007_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_10d_v007_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_10d_v008_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_10d_v008_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_21d_v009_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_21d_v009_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_21d_v010_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_21d_v010_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_21d_v011_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_21d_v011_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_21d_v012_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_21d_v012_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_42d_v013_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_42d_v013_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_42d_v014_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_42d_v014_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_42d_v015_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_42d_v015_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_42d_v016_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_42d_v016_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_63d_v017_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_63d_v017_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_63d_v018_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_63d_v018_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_63d_v019_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_63d_v019_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_63d_v020_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_63d_v020_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_126d_v021_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_126d_v021_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_126d_v022_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_126d_v022_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_126d_v023_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_126d_v023_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_126d_v024_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_126d_v024_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_252d_v025_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_252d_v025_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_252d_v026_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_252d_v026_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_252d_v027_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_252d_v027_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_252d_v028_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_252d_v028_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_504d_v029_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_504d_v029_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_504d_v030_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_504d_v030_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_504d_v031_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_504d_v031_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_504d_v032_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_504d_v032_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_756d_v033_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_756d_v033_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_756d_v034_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_756d_v034_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_756d_v035_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_756d_v035_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_756d_v036_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_756d_v036_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_1008d_v037_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_1008d_v037_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_1008d_v038_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_1008d_v038_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_1008d_v039_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_1008d_v039_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_1008d_v040_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_1008d_v040_signal},
    "f30_long_term_trend_momentum_capex_slope_pct_1260d_v041_signal": {"func": f30_long_term_trend_momentum_capex_slope_pct_1260d_v041_signal},
    "f30_long_term_trend_momentum_revenue_slope_pct_1260d_v042_signal": {"func": f30_long_term_trend_momentum_revenue_slope_pct_1260d_v042_signal},
    "f30_long_term_trend_momentum_ebitda_slope_pct_1260d_v043_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_pct_1260d_v043_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_pct_1260d_v044_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_pct_1260d_v044_signal},
    "f30_long_term_trend_momentum_capex_jerk_5d_v045_signal": {"func": f30_long_term_trend_momentum_capex_jerk_5d_v045_signal},
    "f30_long_term_trend_momentum_revenue_jerk_5d_v046_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_5d_v046_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_5d_v047_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_5d_v047_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_5d_v048_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_5d_v048_signal},
    "f30_long_term_trend_momentum_capex_jerk_10d_v049_signal": {"func": f30_long_term_trend_momentum_capex_jerk_10d_v049_signal},
    "f30_long_term_trend_momentum_revenue_jerk_10d_v050_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_10d_v050_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_10d_v051_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_10d_v051_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_10d_v052_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_10d_v052_signal},
    "f30_long_term_trend_momentum_capex_jerk_21d_v053_signal": {"func": f30_long_term_trend_momentum_capex_jerk_21d_v053_signal},
    "f30_long_term_trend_momentum_revenue_jerk_21d_v054_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_21d_v054_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_21d_v055_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_21d_v055_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_21d_v056_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_21d_v056_signal},
    "f30_long_term_trend_momentum_capex_jerk_42d_v057_signal": {"func": f30_long_term_trend_momentum_capex_jerk_42d_v057_signal},
    "f30_long_term_trend_momentum_revenue_jerk_42d_v058_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_42d_v058_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_42d_v059_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_42d_v059_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_42d_v060_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_42d_v060_signal},
    "f30_long_term_trend_momentum_capex_jerk_63d_v061_signal": {"func": f30_long_term_trend_momentum_capex_jerk_63d_v061_signal},
    "f30_long_term_trend_momentum_revenue_jerk_63d_v062_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_63d_v062_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_63d_v063_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_63d_v063_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_63d_v064_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_63d_v064_signal},
    "f30_long_term_trend_momentum_capex_jerk_126d_v065_signal": {"func": f30_long_term_trend_momentum_capex_jerk_126d_v065_signal},
    "f30_long_term_trend_momentum_revenue_jerk_126d_v066_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_126d_v066_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_126d_v067_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_126d_v067_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_126d_v068_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_126d_v068_signal},
    "f30_long_term_trend_momentum_capex_jerk_252d_v069_signal": {"func": f30_long_term_trend_momentum_capex_jerk_252d_v069_signal},
    "f30_long_term_trend_momentum_revenue_jerk_252d_v070_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_252d_v070_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_252d_v071_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_252d_v071_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_252d_v072_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_252d_v072_signal},
    "f30_long_term_trend_momentum_capex_jerk_504d_v073_signal": {"func": f30_long_term_trend_momentum_capex_jerk_504d_v073_signal},
    "f30_long_term_trend_momentum_revenue_jerk_504d_v074_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_504d_v074_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_504d_v075_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_504d_v075_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_504d_v076_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_504d_v076_signal},
    "f30_long_term_trend_momentum_capex_jerk_756d_v077_signal": {"func": f30_long_term_trend_momentum_capex_jerk_756d_v077_signal},
    "f30_long_term_trend_momentum_revenue_jerk_756d_v078_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_756d_v078_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_756d_v079_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_756d_v079_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_756d_v080_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_756d_v080_signal},
    "f30_long_term_trend_momentum_capex_jerk_1008d_v081_signal": {"func": f30_long_term_trend_momentum_capex_jerk_1008d_v081_signal},
    "f30_long_term_trend_momentum_revenue_jerk_1008d_v082_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_1008d_v082_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_1008d_v083_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_1008d_v083_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_1008d_v084_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_1008d_v084_signal},
    "f30_long_term_trend_momentum_capex_jerk_1260d_v085_signal": {"func": f30_long_term_trend_momentum_capex_jerk_1260d_v085_signal},
    "f30_long_term_trend_momentum_revenue_jerk_1260d_v086_signal": {"func": f30_long_term_trend_momentum_revenue_jerk_1260d_v086_signal},
    "f30_long_term_trend_momentum_ebitda_jerk_1260d_v087_signal": {"func": f30_long_term_trend_momentum_ebitda_jerk_1260d_v087_signal},
    "f30_long_term_trend_momentum_capex_roi_jerk_1260d_v088_signal": {"func": f30_long_term_trend_momentum_capex_roi_jerk_1260d_v088_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_5d_v089_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_5d_v089_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_5d_v090_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_5d_v090_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_5d_v091_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_5d_v091_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_5d_v092_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_5d_v092_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_10d_v093_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_10d_v093_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_10d_v094_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_10d_v094_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_10d_v095_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_10d_v095_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_10d_v096_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_10d_v096_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_21d_v097_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_21d_v097_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_21d_v098_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_21d_v098_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_21d_v099_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_21d_v099_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_21d_v100_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_21d_v100_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_42d_v101_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_42d_v101_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_42d_v102_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_42d_v102_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_42d_v103_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_42d_v103_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_42d_v104_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_42d_v104_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_63d_v105_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_63d_v105_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_63d_v106_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_63d_v106_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_63d_v107_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_63d_v107_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_63d_v108_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_63d_v108_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_126d_v109_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_126d_v109_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_126d_v110_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_126d_v110_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_126d_v111_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_126d_v111_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_126d_v112_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_126d_v112_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_252d_v113_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_252d_v113_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_252d_v114_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_252d_v114_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_252d_v115_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_252d_v115_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_252d_v116_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_252d_v116_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_504d_v117_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_504d_v117_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_504d_v118_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_504d_v118_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_504d_v119_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_504d_v119_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_504d_v120_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_504d_v120_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_756d_v121_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_756d_v121_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_756d_v122_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_756d_v122_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_756d_v123_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_756d_v123_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_756d_v124_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_756d_v124_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_1008d_v125_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_1008d_v125_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_1008d_v126_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_1008d_v126_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_1008d_v127_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_1008d_v127_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_1008d_v128_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_1008d_v128_signal},
    "f30_long_term_trend_momentum_capex_slope_diff_norm_1260d_v129_signal": {"func": f30_long_term_trend_momentum_capex_slope_diff_norm_1260d_v129_signal},
    "f30_long_term_trend_momentum_revenue_slope_diff_norm_1260d_v130_signal": {"func": f30_long_term_trend_momentum_revenue_slope_diff_norm_1260d_v130_signal},
    "f30_long_term_trend_momentum_ebitda_slope_diff_norm_1260d_v131_signal": {"func": f30_long_term_trend_momentum_ebitda_slope_diff_norm_1260d_v131_signal},
    "f30_long_term_trend_momentum_capex_roi_slope_diff_norm_1260d_v132_signal": {"func": f30_long_term_trend_momentum_capex_roi_slope_diff_norm_1260d_v132_signal},
    "f30_long_term_trend_momentum_capex_mom_z_5d_v133_signal": {"func": f30_long_term_trend_momentum_capex_mom_z_5d_v133_signal},
    "f30_long_term_trend_momentum_revenue_mom_z_5d_v134_signal": {"func": f30_long_term_trend_momentum_revenue_mom_z_5d_v134_signal},
    "f30_long_term_trend_momentum_ebitda_mom_z_5d_v135_signal": {"func": f30_long_term_trend_momentum_ebitda_mom_z_5d_v135_signal},
    "f30_long_term_trend_momentum_capex_roi_mom_z_5d_v136_signal": {"func": f30_long_term_trend_momentum_capex_roi_mom_z_5d_v136_signal},
    "f30_long_term_trend_momentum_capex_mom_z_10d_v137_signal": {"func": f30_long_term_trend_momentum_capex_mom_z_10d_v137_signal},
    "f30_long_term_trend_momentum_revenue_mom_z_10d_v138_signal": {"func": f30_long_term_trend_momentum_revenue_mom_z_10d_v138_signal},
    "f30_long_term_trend_momentum_ebitda_mom_z_10d_v139_signal": {"func": f30_long_term_trend_momentum_ebitda_mom_z_10d_v139_signal},
    "f30_long_term_trend_momentum_capex_roi_mom_z_10d_v140_signal": {"func": f30_long_term_trend_momentum_capex_roi_mom_z_10d_v140_signal},
    "f30_long_term_trend_momentum_capex_mom_z_21d_v141_signal": {"func": f30_long_term_trend_momentum_capex_mom_z_21d_v141_signal},
    "f30_long_term_trend_momentum_revenue_mom_z_21d_v142_signal": {"func": f30_long_term_trend_momentum_revenue_mom_z_21d_v142_signal},
    "f30_long_term_trend_momentum_ebitda_mom_z_21d_v143_signal": {"func": f30_long_term_trend_momentum_ebitda_mom_z_21d_v143_signal},
    "f30_long_term_trend_momentum_capex_roi_mom_z_21d_v144_signal": {"func": f30_long_term_trend_momentum_capex_roi_mom_z_21d_v144_signal},
    "f30_long_term_trend_momentum_capex_mom_z_42d_v145_signal": {"func": f30_long_term_trend_momentum_capex_mom_z_42d_v145_signal},
    "f30_long_term_trend_momentum_revenue_mom_z_42d_v146_signal": {"func": f30_long_term_trend_momentum_revenue_mom_z_42d_v146_signal},
    "f30_long_term_trend_momentum_ebitda_mom_z_42d_v147_signal": {"func": f30_long_term_trend_momentum_ebitda_mom_z_42d_v147_signal},
    "f30_long_term_trend_momentum_capex_roi_mom_z_42d_v148_signal": {"func": f30_long_term_trend_momentum_capex_roi_mom_z_42d_v148_signal},
    "f30_long_term_trend_momentum_capex_mom_z_63d_v149_signal": {"func": f30_long_term_trend_momentum_capex_mom_z_63d_v149_signal},
    "f30_long_term_trend_momentum_revenue_mom_z_63d_v150_signal": {"func": f30_long_term_trend_momentum_revenue_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "sbcomp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 30...")
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
