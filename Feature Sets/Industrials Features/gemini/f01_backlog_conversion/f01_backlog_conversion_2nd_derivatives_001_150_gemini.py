import pandas as pd
import numpy as np
import inspect

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

def f01_backlog_conversion_deferredrev_slope_pct_5d_v001_signal(deferredrev):
    res = _slope_pct(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_5d_v002_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_5d_v003_signal(marketcap):
    res = _slope_pct(marketcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_5d_v004_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_5d_v005_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_5d_v006_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_10d_v007_signal(deferredrev):
    res = _slope_pct(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_10d_v008_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_10d_v009_signal(marketcap):
    res = _slope_pct(marketcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_10d_v010_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_10d_v011_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_10d_v012_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_21d_v013_signal(deferredrev):
    res = _slope_pct(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_21d_v014_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_21d_v015_signal(marketcap):
    res = _slope_pct(marketcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_21d_v016_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_21d_v017_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_21d_v018_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_42d_v019_signal(deferredrev):
    res = _slope_pct(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_42d_v020_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_42d_v021_signal(marketcap):
    res = _slope_pct(marketcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_42d_v022_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_42d_v023_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_42d_v024_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_63d_v025_signal(deferredrev):
    res = _slope_pct(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_63d_v026_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_63d_v027_signal(marketcap):
    res = _slope_pct(marketcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_63d_v028_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_63d_v029_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_63d_v030_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_126d_v031_signal(deferredrev):
    res = _slope_pct(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_126d_v032_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_126d_v033_signal(marketcap):
    res = _slope_pct(marketcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_126d_v034_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_126d_v035_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_126d_v036_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_252d_v037_signal(deferredrev):
    res = _slope_pct(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_252d_v038_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_252d_v039_signal(marketcap):
    res = _slope_pct(marketcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_252d_v040_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_252d_v041_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_252d_v042_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_504d_v043_signal(deferredrev):
    res = _slope_pct(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_504d_v044_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_504d_v045_signal(marketcap):
    res = _slope_pct(marketcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_504d_v046_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_504d_v047_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_504d_v048_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_756d_v049_signal(deferredrev):
    res = _slope_pct(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_756d_v050_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_756d_v051_signal(marketcap):
    res = _slope_pct(marketcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_756d_v052_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_756d_v053_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_756d_v054_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_1008d_v055_signal(deferredrev):
    res = _slope_pct(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_1008d_v056_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_1008d_v057_signal(marketcap):
    res = _slope_pct(marketcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_1008d_v058_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_1008d_v059_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_1008d_v060_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_pct_1260d_v061_signal(deferredrev):
    res = _slope_pct(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_pct_1260d_v062_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_pct_1260d_v063_signal(marketcap):
    res = _slope_pct(marketcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_pct_1260d_v064_signal(deferredrev, revenue):
    res = _slope_pct(_ratio(deferredrev, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_pct_1260d_v065_signal(revenue, deferredrev):
    res = _slope_pct(_ratio(revenue, deferredrev), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_pct_1260d_v066_signal(deferredrev, marketcap):
    res = _slope_pct(_ratio(deferredrev, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_5d_v067_signal(deferredrev):
    res = _jerk(deferredrev, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_5d_v068_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_5d_v069_signal(marketcap):
    res = _jerk(marketcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_5d_v070_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_5d_v071_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_5d_v072_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_10d_v073_signal(deferredrev):
    res = _jerk(deferredrev, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_10d_v074_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_10d_v075_signal(marketcap):
    res = _jerk(marketcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_10d_v076_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_10d_v077_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_10d_v078_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_21d_v079_signal(deferredrev):
    res = _jerk(deferredrev, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_21d_v080_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_21d_v081_signal(marketcap):
    res = _jerk(marketcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_21d_v082_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_21d_v083_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_21d_v084_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_42d_v085_signal(deferredrev):
    res = _jerk(deferredrev, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_42d_v086_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_42d_v087_signal(marketcap):
    res = _jerk(marketcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_42d_v088_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_42d_v089_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_42d_v090_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_63d_v091_signal(deferredrev):
    res = _jerk(deferredrev, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_63d_v092_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_63d_v093_signal(marketcap):
    res = _jerk(marketcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_63d_v094_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_63d_v095_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_63d_v096_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_126d_v097_signal(deferredrev):
    res = _jerk(deferredrev, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_126d_v098_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_126d_v099_signal(marketcap):
    res = _jerk(marketcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_126d_v100_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_126d_v101_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_126d_v102_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_252d_v103_signal(deferredrev):
    res = _jerk(deferredrev, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_252d_v104_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_252d_v105_signal(marketcap):
    res = _jerk(marketcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_252d_v106_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_252d_v107_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_252d_v108_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_504d_v109_signal(deferredrev):
    res = _jerk(deferredrev, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_504d_v110_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_504d_v111_signal(marketcap):
    res = _jerk(marketcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_504d_v112_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_504d_v113_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_504d_v114_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_756d_v115_signal(deferredrev):
    res = _jerk(deferredrev, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_756d_v116_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_756d_v117_signal(marketcap):
    res = _jerk(marketcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_756d_v118_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_756d_v119_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_756d_v120_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_1008d_v121_signal(deferredrev):
    res = _jerk(deferredrev, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_1008d_v122_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_1008d_v123_signal(marketcap):
    res = _jerk(marketcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_1008d_v124_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_1008d_v125_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_1008d_v126_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_jerk_1260d_v127_signal(deferredrev):
    res = _jerk(deferredrev, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_jerk_1260d_v128_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_jerk_1260d_v129_signal(marketcap):
    res = _jerk(marketcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_jerk_1260d_v130_signal(deferredrev, revenue):
    res = _jerk(_ratio(deferredrev, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_jerk_1260d_v131_signal(revenue, deferredrev):
    res = _jerk(_ratio(revenue, deferredrev), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_jerk_1260d_v132_signal(deferredrev, marketcap):
    res = _jerk(_ratio(deferredrev, marketcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_5d_v133_signal(deferredrev):
    res = (_slope_pct(deferredrev, 5).diff(5) / _sma(deferredrev.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_5d_v134_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_5d_v135_signal(marketcap):
    res = (_slope_pct(marketcap, 5).diff(5) / _sma(marketcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_5d_v136_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 5).diff(5) / _sma(_ratio(deferredrev, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_5d_v137_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 5).diff(5) / _sma(_ratio(revenue, deferredrev).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_5d_v138_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 5).diff(5) / _sma(_ratio(deferredrev, marketcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_10d_v139_signal(deferredrev):
    res = (_slope_pct(deferredrev, 10).diff(10) / _sma(deferredrev.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_10d_v140_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_10d_v141_signal(marketcap):
    res = (_slope_pct(marketcap, 10).diff(10) / _sma(marketcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_10d_v142_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 10).diff(10) / _sma(_ratio(deferredrev, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_10d_v143_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 10).diff(10) / _sma(_ratio(revenue, deferredrev).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_10d_v144_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 10).diff(10) / _sma(_ratio(deferredrev, marketcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_deferredrev_slope_diff_norm_21d_v145_signal(deferredrev):
    res = (_slope_pct(deferredrev, 21).diff(21) / _sma(deferredrev.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_revenue_slope_diff_norm_21d_v146_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_marketcap_slope_diff_norm_21d_v147_signal(marketcap):
    res = (_slope_pct(marketcap, 21).diff(21) / _sma(marketcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_to_rev_slope_diff_norm_21d_v148_signal(deferredrev, revenue):
    res = (_slope_pct(_ratio(deferredrev, revenue), 21).diff(21) / _sma(_ratio(deferredrev, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_rev_to_backlog_slope_diff_norm_21d_v149_signal(revenue, deferredrev):
    res = (_slope_pct(_ratio(revenue, deferredrev), 21).diff(21) / _sma(_ratio(revenue, deferredrev).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f01_backlog_conversion_backlog_yield_slope_diff_norm_21d_v150_signal(deferredrev, marketcap):
    res = (_slope_pct(_ratio(deferredrev, marketcap), 21).diff(21) / _sma(_ratio(deferredrev, marketcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 01...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        try:
            res = func(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            break
    print("Success.")
