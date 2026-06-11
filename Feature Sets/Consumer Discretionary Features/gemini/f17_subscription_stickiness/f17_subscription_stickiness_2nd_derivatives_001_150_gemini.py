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

def f17_subscription_stickiness_deferredrev_slope_pct_5d_v001_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 5d window."""
    res = _slope_pct(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_5d_v002_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 5d window."""
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_5d_v003_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 5d window."""
    res = _slope_pct(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_5d_v004_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 5d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_10d_v005_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 10d window."""
    res = _slope_pct(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_10d_v006_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 10d window."""
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_10d_v007_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 10d window."""
    res = _slope_pct(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_10d_v008_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 10d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_21d_v009_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 21d window."""
    res = _slope_pct(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_21d_v010_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 21d window."""
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_21d_v011_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 21d window."""
    res = _slope_pct(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_21d_v012_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 21d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_42d_v013_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 42d window."""
    res = _slope_pct(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_42d_v014_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 42d window."""
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_42d_v015_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 42d window."""
    res = _slope_pct(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_42d_v016_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 42d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_63d_v017_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 63d window."""
    res = _slope_pct(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_63d_v018_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 63d window."""
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_63d_v019_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 63d window."""
    res = _slope_pct(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_63d_v020_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 63d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_126d_v021_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 126d window."""
    res = _slope_pct(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_126d_v022_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 126d window."""
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_126d_v023_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 126d window."""
    res = _slope_pct(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_126d_v024_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 126d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_252d_v025_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 252d window."""
    res = _slope_pct(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_252d_v026_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 252d window."""
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_252d_v027_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 252d window."""
    res = _slope_pct(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_252d_v028_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 252d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_504d_v029_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 504d window."""
    res = _slope_pct(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_504d_v030_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 504d window."""
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_504d_v031_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 504d window."""
    res = _slope_pct(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_504d_v032_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 504d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_756d_v033_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 756d window."""
    res = _slope_pct(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_756d_v034_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 756d window."""
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_756d_v035_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 756d window."""
    res = _slope_pct(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_756d_v036_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 756d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_1008d_v037_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 1008d window."""
    res = _slope_pct(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_1008d_v038_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1008d window."""
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_1008d_v039_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 1008d window."""
    res = _slope_pct(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_1008d_v040_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 1008d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_pct_1260d_v041_signal(deferredrev):
    """Percentage slope for momentum for Raw level of deferredrev over 1260d window."""
    res = _slope_pct(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_pct_1260d_v042_signal(revenue):
    """Percentage slope for momentum for Raw level of revenue over 1260d window."""
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_pct_1260d_v043_signal(fcf):
    """Percentage slope for momentum for Raw level of fcf over 1260d window."""
    res = _slope_pct(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_1260d_v044_signal(deferredrev, revenue):
    """Percentage slope for momentum for Percentage of revenue captured as deferred over 1260d window."""
    res = _slope_pct(_ratio(deferredrev, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_5d_v045_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 5d window."""
    res = _jerk(deferredrev, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_5d_v046_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 5d window."""
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_5d_v047_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 5d window."""
    res = _jerk(fcf, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_5d_v048_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 5d window."""
    res = _jerk(_ratio(deferredrev, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_10d_v049_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 10d window."""
    res = _jerk(deferredrev, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_10d_v050_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 10d window."""
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_10d_v051_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 10d window."""
    res = _jerk(fcf, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_10d_v052_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 10d window."""
    res = _jerk(_ratio(deferredrev, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_21d_v053_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 21d window."""
    res = _jerk(deferredrev, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_21d_v054_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 21d window."""
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_21d_v055_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 21d window."""
    res = _jerk(fcf, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_21d_v056_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 21d window."""
    res = _jerk(_ratio(deferredrev, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_42d_v057_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 42d window."""
    res = _jerk(deferredrev, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_42d_v058_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 42d window."""
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_42d_v059_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 42d window."""
    res = _jerk(fcf, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_42d_v060_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 42d window."""
    res = _jerk(_ratio(deferredrev, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_63d_v061_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 63d window."""
    res = _jerk(deferredrev, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_63d_v062_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 63d window."""
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_63d_v063_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 63d window."""
    res = _jerk(fcf, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_63d_v064_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 63d window."""
    res = _jerk(_ratio(deferredrev, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_126d_v065_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 126d window."""
    res = _jerk(deferredrev, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_126d_v066_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 126d window."""
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_126d_v067_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 126d window."""
    res = _jerk(fcf, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_126d_v068_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 126d window."""
    res = _jerk(_ratio(deferredrev, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_252d_v069_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 252d window."""
    res = _jerk(deferredrev, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_252d_v070_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 252d window."""
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_252d_v071_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 252d window."""
    res = _jerk(fcf, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_252d_v072_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 252d window."""
    res = _jerk(_ratio(deferredrev, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_504d_v073_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 504d window."""
    res = _jerk(deferredrev, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_504d_v074_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 504d window."""
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_504d_v075_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 504d window."""
    res = _jerk(fcf, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_504d_v076_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 504d window."""
    res = _jerk(_ratio(deferredrev, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_756d_v077_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 756d window."""
    res = _jerk(deferredrev, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_756d_v078_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 756d window."""
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_756d_v079_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 756d window."""
    res = _jerk(fcf, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_756d_v080_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 756d window."""
    res = _jerk(_ratio(deferredrev, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_1008d_v081_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 1008d window."""
    res = _jerk(deferredrev, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_1008d_v082_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1008d window."""
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_1008d_v083_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 1008d window."""
    res = _jerk(fcf, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_1008d_v084_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 1008d window."""
    res = _jerk(_ratio(deferredrev, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_jerk_1260d_v085_signal(deferredrev):
    """Acceleration/Jerk for structural shifts for Raw level of deferredrev over 1260d window."""
    res = _jerk(deferredrev, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_jerk_1260d_v086_signal(revenue):
    """Acceleration/Jerk for structural shifts for Raw level of revenue over 1260d window."""
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_jerk_1260d_v087_signal(fcf):
    """Acceleration/Jerk for structural shifts for Raw level of fcf over 1260d window."""
    res = _jerk(fcf, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_jerk_1260d_v088_signal(deferredrev, revenue):
    """Acceleration/Jerk for structural shifts for Percentage of revenue captured as deferred over 1260d window."""
    res = _jerk(_ratio(deferredrev, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_5d_v089_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 5d window."""
    res = (_slope_pct(deferredrev, 5).diff(5) / _sma(deferredrev.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_5d_v090_signal(revenue):
    """Normalized slope change for Raw level of revenue over 5d window."""
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_5d_v091_signal(fcf):
    """Normalized slope change for Raw level of fcf over 5d window."""
    res = (_slope_pct(fcf, 5).diff(5) / _sma(fcf.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_5d_v092_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 5d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 5).diff(5) / _sma(_ratio(deferredrev, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_10d_v093_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 10d window."""
    res = (_slope_pct(deferredrev, 10).diff(10) / _sma(deferredrev.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_10d_v094_signal(revenue):
    """Normalized slope change for Raw level of revenue over 10d window."""
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_10d_v095_signal(fcf):
    """Normalized slope change for Raw level of fcf over 10d window."""
    res = (_slope_pct(fcf, 10).diff(10) / _sma(fcf.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_10d_v096_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 10d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 10).diff(10) / _sma(_ratio(deferredrev, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_21d_v097_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 21d window."""
    res = (_slope_pct(deferredrev, 21).diff(21) / _sma(deferredrev.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_21d_v098_signal(revenue):
    """Normalized slope change for Raw level of revenue over 21d window."""
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_21d_v099_signal(fcf):
    """Normalized slope change for Raw level of fcf over 21d window."""
    res = (_slope_pct(fcf, 21).diff(21) / _sma(fcf.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_21d_v100_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 21d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 21).diff(21) / _sma(_ratio(deferredrev, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_42d_v101_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 42d window."""
    res = (_slope_pct(deferredrev, 42).diff(42) / _sma(deferredrev.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_42d_v102_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_42d_v103_signal(fcf):
    """Normalized slope change for Raw level of fcf over 42d window."""
    res = (_slope_pct(fcf, 42).diff(42) / _sma(fcf.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_42d_v104_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 42d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 42).diff(42) / _sma(_ratio(deferredrev, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_63d_v105_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 63d window."""
    res = (_slope_pct(deferredrev, 63).diff(63) / _sma(deferredrev.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_63d_v106_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_63d_v107_signal(fcf):
    """Normalized slope change for Raw level of fcf over 63d window."""
    res = (_slope_pct(fcf, 63).diff(63) / _sma(fcf.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_63d_v108_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 63d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 63).diff(63) / _sma(_ratio(deferredrev, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_126d_v109_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 126d window."""
    res = (_slope_pct(deferredrev, 126).diff(126) / _sma(deferredrev.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_126d_v110_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_126d_v111_signal(fcf):
    """Normalized slope change for Raw level of fcf over 126d window."""
    res = (_slope_pct(fcf, 126).diff(126) / _sma(fcf.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_126d_v112_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 126d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 126).diff(126) / _sma(_ratio(deferredrev, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_252d_v113_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 252d window."""
    res = (_slope_pct(deferredrev, 252).diff(252) / _sma(deferredrev.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_252d_v114_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_252d_v115_signal(fcf):
    """Normalized slope change for Raw level of fcf over 252d window."""
    res = (_slope_pct(fcf, 252).diff(252) / _sma(fcf.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_252d_v116_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 252d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 252).diff(252) / _sma(_ratio(deferredrev, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_504d_v117_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 504d window."""
    res = (_slope_pct(deferredrev, 504).diff(504) / _sma(deferredrev.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_504d_v118_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_504d_v119_signal(fcf):
    """Normalized slope change for Raw level of fcf over 504d window."""
    res = (_slope_pct(fcf, 504).diff(504) / _sma(fcf.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_504d_v120_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 504d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 504).diff(504) / _sma(_ratio(deferredrev, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_756d_v121_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 756d window."""
    res = (_slope_pct(deferredrev, 756).diff(756) / _sma(deferredrev.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_756d_v122_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_756d_v123_signal(fcf):
    """Normalized slope change for Raw level of fcf over 756d window."""
    res = (_slope_pct(fcf, 756).diff(756) / _sma(fcf.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_756d_v124_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 756d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 756).diff(756) / _sma(_ratio(deferredrev, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_1008d_v125_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 1008d window."""
    res = (_slope_pct(deferredrev, 1008).diff(1008) / _sma(deferredrev.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_1008d_v126_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_1008d_v127_signal(fcf):
    """Normalized slope change for Raw level of fcf over 1008d window."""
    res = (_slope_pct(fcf, 1008).diff(1008) / _sma(fcf.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_1008d_v128_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 1008d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 1008).diff(1008) / _sma(_ratio(deferredrev, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_slope_diff_norm_1260d_v129_signal(deferredrev):
    """Normalized slope change for Raw level of deferredrev over 1260d window."""
    res = (_slope_pct(deferredrev, 1260).diff(1260) / _sma(deferredrev.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_slope_diff_norm_1260d_v130_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_slope_diff_norm_1260d_v131_signal(fcf):
    """Normalized slope change for Raw level of fcf over 1260d window."""
    res = (_slope_pct(fcf, 1260).diff(1260) / _sma(fcf.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_1260d_v132_signal(deferredrev, revenue):
    """Normalized slope change for Percentage of revenue captured as deferred over 1260d window."""
    res = (_slope_pct(_ratio(deferredrev, revenue), 1260).diff(1260) / _sma(_ratio(deferredrev, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_mom_z_5d_v133_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 5d window."""
    res = _z(_slope_pct(deferredrev, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_mom_z_5d_v134_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_mom_z_5d_v135_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 5d window."""
    res = _z(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_mom_z_5d_v136_signal(deferredrev, revenue):
    """Relative momentum strength for Percentage of revenue captured as deferred over 5d window."""
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_mom_z_10d_v137_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 10d window."""
    res = _z(_slope_pct(deferredrev, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_mom_z_10d_v138_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_mom_z_10d_v139_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 10d window."""
    res = _z(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_mom_z_10d_v140_signal(deferredrev, revenue):
    """Relative momentum strength for Percentage of revenue captured as deferred over 10d window."""
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_mom_z_21d_v141_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 21d window."""
    res = _z(_slope_pct(deferredrev, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_mom_z_21d_v142_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_mom_z_21d_v143_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 21d window."""
    res = _z(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_mom_z_21d_v144_signal(deferredrev, revenue):
    """Relative momentum strength for Percentage of revenue captured as deferred over 21d window."""
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_mom_z_42d_v145_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 42d window."""
    res = _z(_slope_pct(deferredrev, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_mom_z_42d_v146_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_fcf_mom_z_42d_v147_signal(fcf):
    """Relative momentum strength for Raw level of fcf over 42d window."""
    res = _z(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_recurring_revenue_proxy_mom_z_42d_v148_signal(deferredrev, revenue):
    """Relative momentum strength for Percentage of revenue captured as deferred over 42d window."""
    res = _z(_slope_pct(_ratio(deferredrev, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_deferredrev_mom_z_63d_v149_signal(deferredrev):
    """Relative momentum strength for Raw level of deferredrev over 63d window."""
    res = _z(_slope_pct(deferredrev, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_subscription_stickiness_revenue_mom_z_63d_v150_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f17_subscription_stickiness_deferredrev_slope_pct_5d_v001_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_5d_v001_signal},    "f17_subscription_stickiness_revenue_slope_pct_5d_v002_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_5d_v002_signal},    "f17_subscription_stickiness_fcf_slope_pct_5d_v003_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_5d_v003_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_5d_v004_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_5d_v004_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_10d_v005_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_10d_v005_signal},    "f17_subscription_stickiness_revenue_slope_pct_10d_v006_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_10d_v006_signal},    "f17_subscription_stickiness_fcf_slope_pct_10d_v007_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_10d_v007_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_10d_v008_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_10d_v008_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_21d_v009_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_21d_v009_signal},    "f17_subscription_stickiness_revenue_slope_pct_21d_v010_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_21d_v010_signal},    "f17_subscription_stickiness_fcf_slope_pct_21d_v011_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_21d_v011_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_21d_v012_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_21d_v012_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_42d_v013_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_42d_v013_signal},    "f17_subscription_stickiness_revenue_slope_pct_42d_v014_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_42d_v014_signal},    "f17_subscription_stickiness_fcf_slope_pct_42d_v015_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_42d_v015_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_42d_v016_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_42d_v016_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_63d_v017_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_63d_v017_signal},    "f17_subscription_stickiness_revenue_slope_pct_63d_v018_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_63d_v018_signal},    "f17_subscription_stickiness_fcf_slope_pct_63d_v019_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_63d_v019_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_63d_v020_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_63d_v020_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_126d_v021_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_126d_v021_signal},    "f17_subscription_stickiness_revenue_slope_pct_126d_v022_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_126d_v022_signal},    "f17_subscription_stickiness_fcf_slope_pct_126d_v023_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_126d_v023_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_126d_v024_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_126d_v024_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_252d_v025_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_252d_v025_signal},    "f17_subscription_stickiness_revenue_slope_pct_252d_v026_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_252d_v026_signal},    "f17_subscription_stickiness_fcf_slope_pct_252d_v027_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_252d_v027_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_252d_v028_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_252d_v028_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_504d_v029_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_504d_v029_signal},    "f17_subscription_stickiness_revenue_slope_pct_504d_v030_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_504d_v030_signal},    "f17_subscription_stickiness_fcf_slope_pct_504d_v031_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_504d_v031_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_504d_v032_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_504d_v032_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_756d_v033_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_756d_v033_signal},    "f17_subscription_stickiness_revenue_slope_pct_756d_v034_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_756d_v034_signal},    "f17_subscription_stickiness_fcf_slope_pct_756d_v035_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_756d_v035_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_756d_v036_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_756d_v036_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_1008d_v037_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_1008d_v037_signal},    "f17_subscription_stickiness_revenue_slope_pct_1008d_v038_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_1008d_v038_signal},    "f17_subscription_stickiness_fcf_slope_pct_1008d_v039_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_1008d_v039_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_1008d_v040_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_1008d_v040_signal},    "f17_subscription_stickiness_deferredrev_slope_pct_1260d_v041_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_pct_1260d_v041_signal},    "f17_subscription_stickiness_revenue_slope_pct_1260d_v042_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_pct_1260d_v042_signal},    "f17_subscription_stickiness_fcf_slope_pct_1260d_v043_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_pct_1260d_v043_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_1260d_v044_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_pct_1260d_v044_signal},    "f17_subscription_stickiness_deferredrev_jerk_5d_v045_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_5d_v045_signal},    "f17_subscription_stickiness_revenue_jerk_5d_v046_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_5d_v046_signal},    "f17_subscription_stickiness_fcf_jerk_5d_v047_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_5d_v047_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_5d_v048_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_5d_v048_signal},    "f17_subscription_stickiness_deferredrev_jerk_10d_v049_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_10d_v049_signal},    "f17_subscription_stickiness_revenue_jerk_10d_v050_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_10d_v050_signal},    "f17_subscription_stickiness_fcf_jerk_10d_v051_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_10d_v051_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_10d_v052_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_10d_v052_signal},    "f17_subscription_stickiness_deferredrev_jerk_21d_v053_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_21d_v053_signal},    "f17_subscription_stickiness_revenue_jerk_21d_v054_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_21d_v054_signal},    "f17_subscription_stickiness_fcf_jerk_21d_v055_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_21d_v055_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_21d_v056_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_21d_v056_signal},    "f17_subscription_stickiness_deferredrev_jerk_42d_v057_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_42d_v057_signal},    "f17_subscription_stickiness_revenue_jerk_42d_v058_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_42d_v058_signal},    "f17_subscription_stickiness_fcf_jerk_42d_v059_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_42d_v059_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_42d_v060_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_42d_v060_signal},    "f17_subscription_stickiness_deferredrev_jerk_63d_v061_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_63d_v061_signal},    "f17_subscription_stickiness_revenue_jerk_63d_v062_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_63d_v062_signal},    "f17_subscription_stickiness_fcf_jerk_63d_v063_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_63d_v063_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_63d_v064_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_63d_v064_signal},    "f17_subscription_stickiness_deferredrev_jerk_126d_v065_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_126d_v065_signal},    "f17_subscription_stickiness_revenue_jerk_126d_v066_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_126d_v066_signal},    "f17_subscription_stickiness_fcf_jerk_126d_v067_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_126d_v067_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_126d_v068_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_126d_v068_signal},    "f17_subscription_stickiness_deferredrev_jerk_252d_v069_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_252d_v069_signal},    "f17_subscription_stickiness_revenue_jerk_252d_v070_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_252d_v070_signal},    "f17_subscription_stickiness_fcf_jerk_252d_v071_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_252d_v071_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_252d_v072_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_252d_v072_signal},    "f17_subscription_stickiness_deferredrev_jerk_504d_v073_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_504d_v073_signal},    "f17_subscription_stickiness_revenue_jerk_504d_v074_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_504d_v074_signal},    "f17_subscription_stickiness_fcf_jerk_504d_v075_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_504d_v075_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_504d_v076_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_504d_v076_signal},    "f17_subscription_stickiness_deferredrev_jerk_756d_v077_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_756d_v077_signal},    "f17_subscription_stickiness_revenue_jerk_756d_v078_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_756d_v078_signal},    "f17_subscription_stickiness_fcf_jerk_756d_v079_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_756d_v079_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_756d_v080_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_756d_v080_signal},    "f17_subscription_stickiness_deferredrev_jerk_1008d_v081_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_1008d_v081_signal},    "f17_subscription_stickiness_revenue_jerk_1008d_v082_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_1008d_v082_signal},    "f17_subscription_stickiness_fcf_jerk_1008d_v083_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_1008d_v083_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_1008d_v084_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_1008d_v084_signal},    "f17_subscription_stickiness_deferredrev_jerk_1260d_v085_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_jerk_1260d_v085_signal},    "f17_subscription_stickiness_revenue_jerk_1260d_v086_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_jerk_1260d_v086_signal},    "f17_subscription_stickiness_fcf_jerk_1260d_v087_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_jerk_1260d_v087_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_jerk_1260d_v088_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_jerk_1260d_v088_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_5d_v089_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_5d_v089_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_5d_v090_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_5d_v090_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_5d_v091_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_5d_v091_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_5d_v092_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_5d_v092_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_10d_v093_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_10d_v093_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_10d_v094_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_10d_v094_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_10d_v095_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_10d_v095_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_10d_v096_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_10d_v096_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_21d_v097_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_21d_v097_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_21d_v098_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_21d_v098_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_21d_v099_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_21d_v099_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_21d_v100_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_21d_v100_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_42d_v101_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_42d_v101_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_42d_v102_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_42d_v102_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_42d_v103_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_42d_v103_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_42d_v104_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_42d_v104_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_63d_v105_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_63d_v105_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_63d_v106_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_63d_v106_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_63d_v107_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_63d_v107_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_63d_v108_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_63d_v108_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_126d_v109_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_126d_v109_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_126d_v110_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_126d_v110_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_126d_v111_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_126d_v111_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_126d_v112_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_126d_v112_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_252d_v113_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_252d_v113_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_252d_v114_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_252d_v114_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_252d_v115_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_252d_v115_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_252d_v116_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_252d_v116_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_504d_v117_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_504d_v117_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_504d_v118_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_504d_v118_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_504d_v119_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_504d_v119_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_504d_v120_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_504d_v120_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_756d_v121_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_756d_v121_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_756d_v122_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_756d_v122_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_756d_v123_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_756d_v123_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_756d_v124_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_756d_v124_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_1008d_v125_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_1008d_v125_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_1008d_v126_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_1008d_v126_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_1008d_v127_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_1008d_v127_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_1008d_v128_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_1008d_v128_signal},    "f17_subscription_stickiness_deferredrev_slope_diff_norm_1260d_v129_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_slope_diff_norm_1260d_v129_signal},    "f17_subscription_stickiness_revenue_slope_diff_norm_1260d_v130_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_slope_diff_norm_1260d_v130_signal},    "f17_subscription_stickiness_fcf_slope_diff_norm_1260d_v131_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_slope_diff_norm_1260d_v131_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_1260d_v132_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_slope_diff_norm_1260d_v132_signal},    "f17_subscription_stickiness_deferredrev_mom_z_5d_v133_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_mom_z_5d_v133_signal},    "f17_subscription_stickiness_revenue_mom_z_5d_v134_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_mom_z_5d_v134_signal},    "f17_subscription_stickiness_fcf_mom_z_5d_v135_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_mom_z_5d_v135_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_mom_z_5d_v136_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_mom_z_5d_v136_signal},    "f17_subscription_stickiness_deferredrev_mom_z_10d_v137_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_mom_z_10d_v137_signal},    "f17_subscription_stickiness_revenue_mom_z_10d_v138_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_mom_z_10d_v138_signal},    "f17_subscription_stickiness_fcf_mom_z_10d_v139_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_mom_z_10d_v139_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_mom_z_10d_v140_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_mom_z_10d_v140_signal},    "f17_subscription_stickiness_deferredrev_mom_z_21d_v141_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_mom_z_21d_v141_signal},    "f17_subscription_stickiness_revenue_mom_z_21d_v142_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_mom_z_21d_v142_signal},    "f17_subscription_stickiness_fcf_mom_z_21d_v143_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_mom_z_21d_v143_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_mom_z_21d_v144_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_mom_z_21d_v144_signal},    "f17_subscription_stickiness_deferredrev_mom_z_42d_v145_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_mom_z_42d_v145_signal},    "f17_subscription_stickiness_revenue_mom_z_42d_v146_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_mom_z_42d_v146_signal},    "f17_subscription_stickiness_fcf_mom_z_42d_v147_signal": {"inputs": [], "func": f17_subscription_stickiness_fcf_mom_z_42d_v147_signal},    "f17_subscription_stickiness_recurring_revenue_proxy_mom_z_42d_v148_signal": {"inputs": [], "func": f17_subscription_stickiness_recurring_revenue_proxy_mom_z_42d_v148_signal},    "f17_subscription_stickiness_deferredrev_mom_z_63d_v149_signal": {"inputs": [], "func": f17_subscription_stickiness_deferredrev_mom_z_63d_v149_signal},    "f17_subscription_stickiness_revenue_mom_z_63d_v150_signal": {"inputs": [], "func": f17_subscription_stickiness_revenue_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 17...")
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
