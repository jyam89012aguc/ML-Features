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

def f18_mortgage_beta_revenue_slope_pct_5d_v001_signal(revenue):
    """Percentage slope for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_5d_v002_signal(cor):
    """Percentage slope for Raw level of cor over 5d window."""
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_5d_v003_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 5d window."""
    res = _slope_pct(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_5d_v004_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 5d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_10d_v005_signal(revenue):
    """Percentage slope for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_10d_v006_signal(cor):
    """Percentage slope for Raw level of cor over 10d window."""
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_10d_v007_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 10d window."""
    res = _slope_pct(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_10d_v008_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 10d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_21d_v009_signal(revenue):
    """Percentage slope for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_21d_v010_signal(cor):
    """Percentage slope for Raw level of cor over 21d window."""
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_21d_v011_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 21d window."""
    res = _slope_pct(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_21d_v012_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 21d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_42d_v013_signal(revenue):
    """Percentage slope for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_42d_v014_signal(cor):
    """Percentage slope for Raw level of cor over 42d window."""
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_42d_v015_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 42d window."""
    res = _slope_pct(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_42d_v016_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 42d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_63d_v017_signal(revenue):
    """Percentage slope for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_63d_v018_signal(cor):
    """Percentage slope for Raw level of cor over 63d window."""
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_63d_v019_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 63d window."""
    res = _slope_pct(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_63d_v020_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 63d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_126d_v021_signal(revenue):
    """Percentage slope for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_126d_v022_signal(cor):
    """Percentage slope for Raw level of cor over 126d window."""
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_126d_v023_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 126d window."""
    res = _slope_pct(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_126d_v024_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 126d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_252d_v025_signal(revenue):
    """Percentage slope for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_252d_v026_signal(cor):
    """Percentage slope for Raw level of cor over 252d window."""
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_252d_v027_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 252d window."""
    res = _slope_pct(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_252d_v028_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 252d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_504d_v029_signal(revenue):
    """Percentage slope for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_504d_v030_signal(cor):
    """Percentage slope for Raw level of cor over 504d window."""
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_504d_v031_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 504d window."""
    res = _slope_pct(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_504d_v032_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 504d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_756d_v033_signal(revenue):
    """Percentage slope for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_756d_v034_signal(cor):
    """Percentage slope for Raw level of cor over 756d window."""
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_756d_v035_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 756d window."""
    res = _slope_pct(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_756d_v036_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 756d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_1008d_v037_signal(revenue):
    """Percentage slope for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_1008d_v038_signal(cor):
    """Percentage slope for Raw level of cor over 1008d window."""
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_1008d_v039_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1008d window."""
    res = _slope_pct(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_1008d_v040_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 1008d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_pct_1260d_v041_signal(revenue):
    """Percentage slope for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_pct_1260d_v042_signal(cor):
    """Percentage slope for Raw level of cor over 1260d window."""
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_pct_1260d_v043_signal(marketcap):
    """Percentage slope for Raw level of marketcap over 1260d window."""
    res = _slope_pct(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_pct_1260d_v044_signal(revenue, marketcap):
    """Percentage slope for Revenue yield on market cap over 1260d window."""
    res = _slope_pct(_ratio(revenue, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_5d_v045_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_5d_v046_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 5d window."""
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_5d_v047_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 5d window."""
    res = _jerk(marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_5d_v048_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 5d window."""
    res = _jerk(_ratio(revenue, marketcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_10d_v049_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_10d_v050_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 10d window."""
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_10d_v051_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 10d window."""
    res = _jerk(marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_10d_v052_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 10d window."""
    res = _jerk(_ratio(revenue, marketcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_21d_v053_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_21d_v054_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 21d window."""
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_21d_v055_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 21d window."""
    res = _jerk(marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_21d_v056_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 21d window."""
    res = _jerk(_ratio(revenue, marketcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_42d_v057_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_42d_v058_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 42d window."""
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_42d_v059_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 42d window."""
    res = _jerk(marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_42d_v060_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 42d window."""
    res = _jerk(_ratio(revenue, marketcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_63d_v061_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_63d_v062_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 63d window."""
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_63d_v063_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 63d window."""
    res = _jerk(marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_63d_v064_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 63d window."""
    res = _jerk(_ratio(revenue, marketcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_126d_v065_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_126d_v066_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 126d window."""
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_126d_v067_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 126d window."""
    res = _jerk(marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_126d_v068_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 126d window."""
    res = _jerk(_ratio(revenue, marketcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_252d_v069_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_252d_v070_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 252d window."""
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_252d_v071_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 252d window."""
    res = _jerk(marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_252d_v072_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 252d window."""
    res = _jerk(_ratio(revenue, marketcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_504d_v073_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_504d_v074_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 504d window."""
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_504d_v075_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 504d window."""
    res = _jerk(marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_504d_v076_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 504d window."""
    res = _jerk(_ratio(revenue, marketcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_756d_v077_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_756d_v078_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 756d window."""
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_756d_v079_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 756d window."""
    res = _jerk(marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_756d_v080_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 756d window."""
    res = _jerk(_ratio(revenue, marketcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_1008d_v081_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_1008d_v082_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1008d window."""
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_1008d_v083_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1008d window."""
    res = _jerk(marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_1008d_v084_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 1008d window."""
    res = _jerk(_ratio(revenue, marketcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_jerk_1260d_v085_signal(revenue):
    """Acceleration/Jerk for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_jerk_1260d_v086_signal(cor):
    """Acceleration/Jerk for Raw level of cor over 1260d window."""
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_jerk_1260d_v087_signal(marketcap):
    """Acceleration/Jerk for Raw level of marketcap over 1260d window."""
    res = _jerk(marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_jerk_1260d_v088_signal(revenue, marketcap):
    """Acceleration/Jerk for Revenue yield on market cap over 1260d window."""
    res = _jerk(_ratio(revenue, marketcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_5d_v089_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_5d_v090_signal(cor):
    """Normalized slope change for Raw level of cor over 5d window."""
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_5d_v091_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 5d window."""
    res = (_slope_pct(marketcap, 5).diff(5) / _sma(marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_5d_v092_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 5d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 5).diff(5) / _sma(_ratio(revenue, marketcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_10d_v093_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_10d_v094_signal(cor):
    """Normalized slope change for Raw level of cor over 10d window."""
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_10d_v095_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 10d window."""
    res = (_slope_pct(marketcap, 10).diff(10) / _sma(marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_10d_v096_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 10d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 10).diff(10) / _sma(_ratio(revenue, marketcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_21d_v097_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_21d_v098_signal(cor):
    """Normalized slope change for Raw level of cor over 21d window."""
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_21d_v099_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 21d window."""
    res = (_slope_pct(marketcap, 21).diff(21) / _sma(marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_21d_v100_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 21d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 21).diff(21) / _sma(_ratio(revenue, marketcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_42d_v101_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_42d_v102_signal(cor):
    """Normalized slope change for Raw level of cor over 42d window."""
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_42d_v103_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 42d window."""
    res = (_slope_pct(marketcap, 42).diff(42) / _sma(marketcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_42d_v104_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 42d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 42).diff(42) / _sma(_ratio(revenue, marketcap).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_63d_v105_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_63d_v106_signal(cor):
    """Normalized slope change for Raw level of cor over 63d window."""
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_63d_v107_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 63d window."""
    res = (_slope_pct(marketcap, 63).diff(63) / _sma(marketcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_63d_v108_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 63d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 63).diff(63) / _sma(_ratio(revenue, marketcap).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_126d_v109_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_126d_v110_signal(cor):
    """Normalized slope change for Raw level of cor over 126d window."""
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_126d_v111_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 126d window."""
    res = (_slope_pct(marketcap, 126).diff(126) / _sma(marketcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_126d_v112_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 126d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 126).diff(126) / _sma(_ratio(revenue, marketcap).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_252d_v113_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_252d_v114_signal(cor):
    """Normalized slope change for Raw level of cor over 252d window."""
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_252d_v115_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 252d window."""
    res = (_slope_pct(marketcap, 252).diff(252) / _sma(marketcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_252d_v116_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 252d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 252).diff(252) / _sma(_ratio(revenue, marketcap).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_504d_v117_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_504d_v118_signal(cor):
    """Normalized slope change for Raw level of cor over 504d window."""
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_504d_v119_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 504d window."""
    res = (_slope_pct(marketcap, 504).diff(504) / _sma(marketcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_504d_v120_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 504d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 504).diff(504) / _sma(_ratio(revenue, marketcap).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_756d_v121_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_756d_v122_signal(cor):
    """Normalized slope change for Raw level of cor over 756d window."""
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_756d_v123_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 756d window."""
    res = (_slope_pct(marketcap, 756).diff(756) / _sma(marketcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_756d_v124_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 756d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 756).diff(756) / _sma(_ratio(revenue, marketcap).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_1008d_v125_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_1008d_v126_signal(cor):
    """Normalized slope change for Raw level of cor over 1008d window."""
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_1008d_v127_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1008d window."""
    res = (_slope_pct(marketcap, 1008).diff(1008) / _sma(marketcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_1008d_v128_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 1008d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 1008).diff(1008) / _sma(_ratio(revenue, marketcap).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_slope_diff_norm_1260d_v129_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_slope_diff_norm_1260d_v130_signal(cor):
    """Normalized slope change for Raw level of cor over 1260d window."""
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_slope_diff_norm_1260d_v131_signal(marketcap):
    """Normalized slope change for Raw level of marketcap over 1260d window."""
    res = (_slope_pct(marketcap, 1260).diff(1260) / _sma(marketcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_slope_diff_norm_1260d_v132_signal(revenue, marketcap):
    """Normalized slope change for Revenue yield on market cap over 1260d window."""
    res = (_slope_pct(_ratio(revenue, marketcap), 1260).diff(1260) / _sma(_ratio(revenue, marketcap).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_mom_z_5d_v133_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_mom_z_5d_v134_signal(cor):
    """Relative momentum strength for Raw level of cor over 5d window."""
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_mom_z_5d_v135_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 5d window."""
    res = _z(_slope_pct(marketcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_mom_z_5d_v136_signal(revenue, marketcap):
    """Relative momentum strength for Revenue yield on market cap over 5d window."""
    res = _z(_slope_pct(_ratio(revenue, marketcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_mom_z_10d_v137_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_mom_z_10d_v138_signal(cor):
    """Relative momentum strength for Raw level of cor over 10d window."""
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_mom_z_10d_v139_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 10d window."""
    res = _z(_slope_pct(marketcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_mom_z_10d_v140_signal(revenue, marketcap):
    """Relative momentum strength for Revenue yield on market cap over 10d window."""
    res = _z(_slope_pct(_ratio(revenue, marketcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_mom_z_21d_v141_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_mom_z_21d_v142_signal(cor):
    """Relative momentum strength for Raw level of cor over 21d window."""
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_mom_z_21d_v143_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 21d window."""
    res = _z(_slope_pct(marketcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_mom_z_21d_v144_signal(revenue, marketcap):
    """Relative momentum strength for Revenue yield on market cap over 21d window."""
    res = _z(_slope_pct(_ratio(revenue, marketcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_mom_z_42d_v145_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_mom_z_42d_v146_signal(cor):
    """Relative momentum strength for Raw level of cor over 42d window."""
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_marketcap_mom_z_42d_v147_signal(marketcap):
    """Relative momentum strength for Raw level of marketcap over 42d window."""
    res = _z(_slope_pct(marketcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_per_cap_mom_z_42d_v148_signal(revenue, marketcap):
    """Relative momentum strength for Revenue yield on market cap over 42d window."""
    res = _z(_slope_pct(_ratio(revenue, marketcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_revenue_mom_z_63d_v149_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_mortgage_beta_cor_mom_z_63d_v150_signal(cor):
    """Relative momentum strength for Raw level of cor over 63d window."""
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f18_mortgage_beta_revenue_slope_pct_5d_v001_signal": {"func": f18_mortgage_beta_revenue_slope_pct_5d_v001_signal},
    "f18_mortgage_beta_cor_slope_pct_5d_v002_signal": {"func": f18_mortgage_beta_cor_slope_pct_5d_v002_signal},
    "f18_mortgage_beta_marketcap_slope_pct_5d_v003_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_5d_v003_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_5d_v004_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_5d_v004_signal},
    "f18_mortgage_beta_revenue_slope_pct_10d_v005_signal": {"func": f18_mortgage_beta_revenue_slope_pct_10d_v005_signal},
    "f18_mortgage_beta_cor_slope_pct_10d_v006_signal": {"func": f18_mortgage_beta_cor_slope_pct_10d_v006_signal},
    "f18_mortgage_beta_marketcap_slope_pct_10d_v007_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_10d_v007_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_10d_v008_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_10d_v008_signal},
    "f18_mortgage_beta_revenue_slope_pct_21d_v009_signal": {"func": f18_mortgage_beta_revenue_slope_pct_21d_v009_signal},
    "f18_mortgage_beta_cor_slope_pct_21d_v010_signal": {"func": f18_mortgage_beta_cor_slope_pct_21d_v010_signal},
    "f18_mortgage_beta_marketcap_slope_pct_21d_v011_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_21d_v011_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_21d_v012_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_21d_v012_signal},
    "f18_mortgage_beta_revenue_slope_pct_42d_v013_signal": {"func": f18_mortgage_beta_revenue_slope_pct_42d_v013_signal},
    "f18_mortgage_beta_cor_slope_pct_42d_v014_signal": {"func": f18_mortgage_beta_cor_slope_pct_42d_v014_signal},
    "f18_mortgage_beta_marketcap_slope_pct_42d_v015_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_42d_v015_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_42d_v016_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_42d_v016_signal},
    "f18_mortgage_beta_revenue_slope_pct_63d_v017_signal": {"func": f18_mortgage_beta_revenue_slope_pct_63d_v017_signal},
    "f18_mortgage_beta_cor_slope_pct_63d_v018_signal": {"func": f18_mortgage_beta_cor_slope_pct_63d_v018_signal},
    "f18_mortgage_beta_marketcap_slope_pct_63d_v019_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_63d_v019_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_63d_v020_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_63d_v020_signal},
    "f18_mortgage_beta_revenue_slope_pct_126d_v021_signal": {"func": f18_mortgage_beta_revenue_slope_pct_126d_v021_signal},
    "f18_mortgage_beta_cor_slope_pct_126d_v022_signal": {"func": f18_mortgage_beta_cor_slope_pct_126d_v022_signal},
    "f18_mortgage_beta_marketcap_slope_pct_126d_v023_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_126d_v023_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_126d_v024_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_126d_v024_signal},
    "f18_mortgage_beta_revenue_slope_pct_252d_v025_signal": {"func": f18_mortgage_beta_revenue_slope_pct_252d_v025_signal},
    "f18_mortgage_beta_cor_slope_pct_252d_v026_signal": {"func": f18_mortgage_beta_cor_slope_pct_252d_v026_signal},
    "f18_mortgage_beta_marketcap_slope_pct_252d_v027_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_252d_v027_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_252d_v028_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_252d_v028_signal},
    "f18_mortgage_beta_revenue_slope_pct_504d_v029_signal": {"func": f18_mortgage_beta_revenue_slope_pct_504d_v029_signal},
    "f18_mortgage_beta_cor_slope_pct_504d_v030_signal": {"func": f18_mortgage_beta_cor_slope_pct_504d_v030_signal},
    "f18_mortgage_beta_marketcap_slope_pct_504d_v031_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_504d_v031_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_504d_v032_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_504d_v032_signal},
    "f18_mortgage_beta_revenue_slope_pct_756d_v033_signal": {"func": f18_mortgage_beta_revenue_slope_pct_756d_v033_signal},
    "f18_mortgage_beta_cor_slope_pct_756d_v034_signal": {"func": f18_mortgage_beta_cor_slope_pct_756d_v034_signal},
    "f18_mortgage_beta_marketcap_slope_pct_756d_v035_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_756d_v035_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_756d_v036_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_756d_v036_signal},
    "f18_mortgage_beta_revenue_slope_pct_1008d_v037_signal": {"func": f18_mortgage_beta_revenue_slope_pct_1008d_v037_signal},
    "f18_mortgage_beta_cor_slope_pct_1008d_v038_signal": {"func": f18_mortgage_beta_cor_slope_pct_1008d_v038_signal},
    "f18_mortgage_beta_marketcap_slope_pct_1008d_v039_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_1008d_v039_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_1008d_v040_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_1008d_v040_signal},
    "f18_mortgage_beta_revenue_slope_pct_1260d_v041_signal": {"func": f18_mortgage_beta_revenue_slope_pct_1260d_v041_signal},
    "f18_mortgage_beta_cor_slope_pct_1260d_v042_signal": {"func": f18_mortgage_beta_cor_slope_pct_1260d_v042_signal},
    "f18_mortgage_beta_marketcap_slope_pct_1260d_v043_signal": {"func": f18_mortgage_beta_marketcap_slope_pct_1260d_v043_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_pct_1260d_v044_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_pct_1260d_v044_signal},
    "f18_mortgage_beta_revenue_jerk_5d_v045_signal": {"func": f18_mortgage_beta_revenue_jerk_5d_v045_signal},
    "f18_mortgage_beta_cor_jerk_5d_v046_signal": {"func": f18_mortgage_beta_cor_jerk_5d_v046_signal},
    "f18_mortgage_beta_marketcap_jerk_5d_v047_signal": {"func": f18_mortgage_beta_marketcap_jerk_5d_v047_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_5d_v048_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_5d_v048_signal},
    "f18_mortgage_beta_revenue_jerk_10d_v049_signal": {"func": f18_mortgage_beta_revenue_jerk_10d_v049_signal},
    "f18_mortgage_beta_cor_jerk_10d_v050_signal": {"func": f18_mortgage_beta_cor_jerk_10d_v050_signal},
    "f18_mortgage_beta_marketcap_jerk_10d_v051_signal": {"func": f18_mortgage_beta_marketcap_jerk_10d_v051_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_10d_v052_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_10d_v052_signal},
    "f18_mortgage_beta_revenue_jerk_21d_v053_signal": {"func": f18_mortgage_beta_revenue_jerk_21d_v053_signal},
    "f18_mortgage_beta_cor_jerk_21d_v054_signal": {"func": f18_mortgage_beta_cor_jerk_21d_v054_signal},
    "f18_mortgage_beta_marketcap_jerk_21d_v055_signal": {"func": f18_mortgage_beta_marketcap_jerk_21d_v055_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_21d_v056_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_21d_v056_signal},
    "f18_mortgage_beta_revenue_jerk_42d_v057_signal": {"func": f18_mortgage_beta_revenue_jerk_42d_v057_signal},
    "f18_mortgage_beta_cor_jerk_42d_v058_signal": {"func": f18_mortgage_beta_cor_jerk_42d_v058_signal},
    "f18_mortgage_beta_marketcap_jerk_42d_v059_signal": {"func": f18_mortgage_beta_marketcap_jerk_42d_v059_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_42d_v060_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_42d_v060_signal},
    "f18_mortgage_beta_revenue_jerk_63d_v061_signal": {"func": f18_mortgage_beta_revenue_jerk_63d_v061_signal},
    "f18_mortgage_beta_cor_jerk_63d_v062_signal": {"func": f18_mortgage_beta_cor_jerk_63d_v062_signal},
    "f18_mortgage_beta_marketcap_jerk_63d_v063_signal": {"func": f18_mortgage_beta_marketcap_jerk_63d_v063_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_63d_v064_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_63d_v064_signal},
    "f18_mortgage_beta_revenue_jerk_126d_v065_signal": {"func": f18_mortgage_beta_revenue_jerk_126d_v065_signal},
    "f18_mortgage_beta_cor_jerk_126d_v066_signal": {"func": f18_mortgage_beta_cor_jerk_126d_v066_signal},
    "f18_mortgage_beta_marketcap_jerk_126d_v067_signal": {"func": f18_mortgage_beta_marketcap_jerk_126d_v067_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_126d_v068_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_126d_v068_signal},
    "f18_mortgage_beta_revenue_jerk_252d_v069_signal": {"func": f18_mortgage_beta_revenue_jerk_252d_v069_signal},
    "f18_mortgage_beta_cor_jerk_252d_v070_signal": {"func": f18_mortgage_beta_cor_jerk_252d_v070_signal},
    "f18_mortgage_beta_marketcap_jerk_252d_v071_signal": {"func": f18_mortgage_beta_marketcap_jerk_252d_v071_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_252d_v072_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_252d_v072_signal},
    "f18_mortgage_beta_revenue_jerk_504d_v073_signal": {"func": f18_mortgage_beta_revenue_jerk_504d_v073_signal},
    "f18_mortgage_beta_cor_jerk_504d_v074_signal": {"func": f18_mortgage_beta_cor_jerk_504d_v074_signal},
    "f18_mortgage_beta_marketcap_jerk_504d_v075_signal": {"func": f18_mortgage_beta_marketcap_jerk_504d_v075_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_504d_v076_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_504d_v076_signal},
    "f18_mortgage_beta_revenue_jerk_756d_v077_signal": {"func": f18_mortgage_beta_revenue_jerk_756d_v077_signal},
    "f18_mortgage_beta_cor_jerk_756d_v078_signal": {"func": f18_mortgage_beta_cor_jerk_756d_v078_signal},
    "f18_mortgage_beta_marketcap_jerk_756d_v079_signal": {"func": f18_mortgage_beta_marketcap_jerk_756d_v079_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_756d_v080_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_756d_v080_signal},
    "f18_mortgage_beta_revenue_jerk_1008d_v081_signal": {"func": f18_mortgage_beta_revenue_jerk_1008d_v081_signal},
    "f18_mortgage_beta_cor_jerk_1008d_v082_signal": {"func": f18_mortgage_beta_cor_jerk_1008d_v082_signal},
    "f18_mortgage_beta_marketcap_jerk_1008d_v083_signal": {"func": f18_mortgage_beta_marketcap_jerk_1008d_v083_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_1008d_v084_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_1008d_v084_signal},
    "f18_mortgage_beta_revenue_jerk_1260d_v085_signal": {"func": f18_mortgage_beta_revenue_jerk_1260d_v085_signal},
    "f18_mortgage_beta_cor_jerk_1260d_v086_signal": {"func": f18_mortgage_beta_cor_jerk_1260d_v086_signal},
    "f18_mortgage_beta_marketcap_jerk_1260d_v087_signal": {"func": f18_mortgage_beta_marketcap_jerk_1260d_v087_signal},
    "f18_mortgage_beta_revenue_per_cap_jerk_1260d_v088_signal": {"func": f18_mortgage_beta_revenue_per_cap_jerk_1260d_v088_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_5d_v089_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_5d_v089_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_5d_v090_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_5d_v090_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_5d_v091_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_5d_v091_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_5d_v092_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_5d_v092_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_10d_v093_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_10d_v093_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_10d_v094_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_10d_v094_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_10d_v095_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_10d_v095_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_10d_v096_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_10d_v096_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_21d_v097_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_21d_v097_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_21d_v098_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_21d_v098_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_21d_v099_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_21d_v099_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_21d_v100_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_21d_v100_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_42d_v101_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_42d_v101_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_42d_v102_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_42d_v102_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_42d_v103_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_42d_v103_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_42d_v104_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_42d_v104_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_63d_v105_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_63d_v105_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_63d_v106_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_63d_v106_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_63d_v107_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_63d_v107_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_63d_v108_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_63d_v108_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_126d_v109_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_126d_v109_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_126d_v110_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_126d_v110_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_126d_v111_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_126d_v111_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_126d_v112_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_126d_v112_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_252d_v113_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_252d_v113_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_252d_v114_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_252d_v114_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_252d_v115_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_252d_v115_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_252d_v116_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_252d_v116_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_504d_v117_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_504d_v117_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_504d_v118_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_504d_v118_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_504d_v119_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_504d_v119_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_504d_v120_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_504d_v120_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_756d_v121_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_756d_v121_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_756d_v122_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_756d_v122_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_756d_v123_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_756d_v123_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_756d_v124_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_756d_v124_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_1008d_v125_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_1008d_v125_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_1008d_v126_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_1008d_v126_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_1008d_v127_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_1008d_v127_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_1008d_v128_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_1008d_v128_signal},
    "f18_mortgage_beta_revenue_slope_diff_norm_1260d_v129_signal": {"func": f18_mortgage_beta_revenue_slope_diff_norm_1260d_v129_signal},
    "f18_mortgage_beta_cor_slope_diff_norm_1260d_v130_signal": {"func": f18_mortgage_beta_cor_slope_diff_norm_1260d_v130_signal},
    "f18_mortgage_beta_marketcap_slope_diff_norm_1260d_v131_signal": {"func": f18_mortgage_beta_marketcap_slope_diff_norm_1260d_v131_signal},
    "f18_mortgage_beta_revenue_per_cap_slope_diff_norm_1260d_v132_signal": {"func": f18_mortgage_beta_revenue_per_cap_slope_diff_norm_1260d_v132_signal},
    "f18_mortgage_beta_revenue_mom_z_5d_v133_signal": {"func": f18_mortgage_beta_revenue_mom_z_5d_v133_signal},
    "f18_mortgage_beta_cor_mom_z_5d_v134_signal": {"func": f18_mortgage_beta_cor_mom_z_5d_v134_signal},
    "f18_mortgage_beta_marketcap_mom_z_5d_v135_signal": {"func": f18_mortgage_beta_marketcap_mom_z_5d_v135_signal},
    "f18_mortgage_beta_revenue_per_cap_mom_z_5d_v136_signal": {"func": f18_mortgage_beta_revenue_per_cap_mom_z_5d_v136_signal},
    "f18_mortgage_beta_revenue_mom_z_10d_v137_signal": {"func": f18_mortgage_beta_revenue_mom_z_10d_v137_signal},
    "f18_mortgage_beta_cor_mom_z_10d_v138_signal": {"func": f18_mortgage_beta_cor_mom_z_10d_v138_signal},
    "f18_mortgage_beta_marketcap_mom_z_10d_v139_signal": {"func": f18_mortgage_beta_marketcap_mom_z_10d_v139_signal},
    "f18_mortgage_beta_revenue_per_cap_mom_z_10d_v140_signal": {"func": f18_mortgage_beta_revenue_per_cap_mom_z_10d_v140_signal},
    "f18_mortgage_beta_revenue_mom_z_21d_v141_signal": {"func": f18_mortgage_beta_revenue_mom_z_21d_v141_signal},
    "f18_mortgage_beta_cor_mom_z_21d_v142_signal": {"func": f18_mortgage_beta_cor_mom_z_21d_v142_signal},
    "f18_mortgage_beta_marketcap_mom_z_21d_v143_signal": {"func": f18_mortgage_beta_marketcap_mom_z_21d_v143_signal},
    "f18_mortgage_beta_revenue_per_cap_mom_z_21d_v144_signal": {"func": f18_mortgage_beta_revenue_per_cap_mom_z_21d_v144_signal},
    "f18_mortgage_beta_revenue_mom_z_42d_v145_signal": {"func": f18_mortgage_beta_revenue_mom_z_42d_v145_signal},
    "f18_mortgage_beta_cor_mom_z_42d_v146_signal": {"func": f18_mortgage_beta_cor_mom_z_42d_v146_signal},
    "f18_mortgage_beta_marketcap_mom_z_42d_v147_signal": {"func": f18_mortgage_beta_marketcap_mom_z_42d_v147_signal},
    "f18_mortgage_beta_revenue_per_cap_mom_z_42d_v148_signal": {"func": f18_mortgage_beta_revenue_per_cap_mom_z_42d_v148_signal},
    "f18_mortgage_beta_revenue_mom_z_63d_v149_signal": {"func": f18_mortgage_beta_revenue_mom_z_63d_v149_signal},
    "f18_mortgage_beta_cor_mom_z_63d_v150_signal": {"func": f18_mortgage_beta_cor_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 18...")
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
