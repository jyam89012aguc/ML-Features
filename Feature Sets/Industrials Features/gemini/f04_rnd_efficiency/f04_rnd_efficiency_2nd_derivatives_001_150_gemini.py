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

def f04_rnd_efficiency_rnd_slope_pct_5d_v001_signal(rnd):
    res = _slope_pct(rnd, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_5d_v002_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_5d_v003_signal(ebit):
    res = _slope_pct(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_5d_v004_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_5d_v005_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_10d_v006_signal(rnd):
    res = _slope_pct(rnd, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_10d_v007_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_10d_v008_signal(ebit):
    res = _slope_pct(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_10d_v009_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_10d_v010_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_21d_v011_signal(rnd):
    res = _slope_pct(rnd, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_21d_v012_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_21d_v013_signal(ebit):
    res = _slope_pct(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_21d_v014_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_21d_v015_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_42d_v016_signal(rnd):
    res = _slope_pct(rnd, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_42d_v017_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_42d_v018_signal(ebit):
    res = _slope_pct(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_42d_v019_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_42d_v020_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_63d_v021_signal(rnd):
    res = _slope_pct(rnd, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_63d_v022_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_63d_v023_signal(ebit):
    res = _slope_pct(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_63d_v024_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_63d_v025_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_126d_v026_signal(rnd):
    res = _slope_pct(rnd, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_126d_v027_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_126d_v028_signal(ebit):
    res = _slope_pct(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_126d_v029_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_126d_v030_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_252d_v031_signal(rnd):
    res = _slope_pct(rnd, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_252d_v032_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_252d_v033_signal(ebit):
    res = _slope_pct(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_252d_v034_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_252d_v035_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_504d_v036_signal(rnd):
    res = _slope_pct(rnd, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_504d_v037_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_504d_v038_signal(ebit):
    res = _slope_pct(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_504d_v039_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_504d_v040_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_756d_v041_signal(rnd):
    res = _slope_pct(rnd, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_756d_v042_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_756d_v043_signal(ebit):
    res = _slope_pct(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_756d_v044_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_756d_v045_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_1008d_v046_signal(rnd):
    res = _slope_pct(rnd, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_1008d_v047_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_1008d_v048_signal(ebit):
    res = _slope_pct(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_1008d_v049_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_1008d_v050_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_pct_1260d_v051_signal(rnd):
    res = _slope_pct(rnd, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_pct_1260d_v052_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_pct_1260d_v053_signal(ebit):
    res = _slope_pct(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_pct_1260d_v054_signal(rnd, revenue):
    res = _slope_pct(_ratio(rnd, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_pct_1260d_v055_signal(rnd, ebit):
    res = _slope_pct(_ratio(rnd, ebit), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_5d_v056_signal(rnd):
    res = _jerk(rnd, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_5d_v057_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_5d_v058_signal(ebit):
    res = _jerk(ebit, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_5d_v059_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_5d_v060_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_10d_v061_signal(rnd):
    res = _jerk(rnd, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_10d_v062_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_10d_v063_signal(ebit):
    res = _jerk(ebit, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_10d_v064_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_10d_v065_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_21d_v066_signal(rnd):
    res = _jerk(rnd, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_21d_v067_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_21d_v068_signal(ebit):
    res = _jerk(ebit, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_21d_v069_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_21d_v070_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_42d_v071_signal(rnd):
    res = _jerk(rnd, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_42d_v072_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_42d_v073_signal(ebit):
    res = _jerk(ebit, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_42d_v074_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_42d_v075_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_63d_v076_signal(rnd):
    res = _jerk(rnd, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_63d_v077_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_63d_v078_signal(ebit):
    res = _jerk(ebit, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_63d_v079_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_63d_v080_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_126d_v081_signal(rnd):
    res = _jerk(rnd, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_126d_v082_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_126d_v083_signal(ebit):
    res = _jerk(ebit, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_126d_v084_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_126d_v085_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_252d_v086_signal(rnd):
    res = _jerk(rnd, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_252d_v087_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_252d_v088_signal(ebit):
    res = _jerk(ebit, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_252d_v089_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_252d_v090_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_504d_v091_signal(rnd):
    res = _jerk(rnd, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_504d_v092_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_504d_v093_signal(ebit):
    res = _jerk(ebit, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_504d_v094_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_504d_v095_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_756d_v096_signal(rnd):
    res = _jerk(rnd, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_756d_v097_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_756d_v098_signal(ebit):
    res = _jerk(ebit, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_756d_v099_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_756d_v100_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_1008d_v101_signal(rnd):
    res = _jerk(rnd, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_1008d_v102_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_1008d_v103_signal(ebit):
    res = _jerk(ebit, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_1008d_v104_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_1008d_v105_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_jerk_1260d_v106_signal(rnd):
    res = _jerk(rnd, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_jerk_1260d_v107_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_jerk_1260d_v108_signal(ebit):
    res = _jerk(ebit, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_jerk_1260d_v109_signal(rnd, revenue):
    res = _jerk(_ratio(rnd, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_jerk_1260d_v110_signal(rnd, ebit):
    res = _jerk(_ratio(rnd, ebit), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_diff_norm_5d_v111_signal(rnd):
    res = (_slope_pct(rnd, 5).diff(5) / _sma(rnd.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_diff_norm_5d_v112_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_diff_norm_5d_v113_signal(ebit):
    res = (_slope_pct(ebit, 5).diff(5) / _sma(ebit.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_diff_norm_5d_v114_signal(rnd, revenue):
    res = (_slope_pct(_ratio(rnd, revenue), 5).diff(5) / _sma(_ratio(rnd, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_diff_norm_5d_v115_signal(rnd, ebit):
    res = (_slope_pct(_ratio(rnd, ebit), 5).diff(5) / _sma(_ratio(rnd, ebit).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_diff_norm_10d_v116_signal(rnd):
    res = (_slope_pct(rnd, 10).diff(10) / _sma(rnd.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_diff_norm_10d_v117_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_diff_norm_10d_v118_signal(ebit):
    res = (_slope_pct(ebit, 10).diff(10) / _sma(ebit.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_diff_norm_10d_v119_signal(rnd, revenue):
    res = (_slope_pct(_ratio(rnd, revenue), 10).diff(10) / _sma(_ratio(rnd, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_diff_norm_10d_v120_signal(rnd, ebit):
    res = (_slope_pct(_ratio(rnd, ebit), 10).diff(10) / _sma(_ratio(rnd, ebit).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_diff_norm_21d_v121_signal(rnd):
    res = (_slope_pct(rnd, 21).diff(21) / _sma(rnd.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_diff_norm_21d_v122_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_diff_norm_21d_v123_signal(ebit):
    res = (_slope_pct(ebit, 21).diff(21) / _sma(ebit.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_diff_norm_21d_v124_signal(rnd, revenue):
    res = (_slope_pct(_ratio(rnd, revenue), 21).diff(21) / _sma(_ratio(rnd, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_diff_norm_21d_v125_signal(rnd, ebit):
    res = (_slope_pct(_ratio(rnd, ebit), 21).diff(21) / _sma(_ratio(rnd, ebit).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_diff_norm_42d_v126_signal(rnd):
    res = (_slope_pct(rnd, 42).diff(42) / _sma(rnd.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_diff_norm_42d_v127_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_diff_norm_42d_v128_signal(ebit):
    res = (_slope_pct(ebit, 42).diff(42) / _sma(ebit.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_diff_norm_42d_v129_signal(rnd, revenue):
    res = (_slope_pct(_ratio(rnd, revenue), 42).diff(42) / _sma(_ratio(rnd, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_diff_norm_42d_v130_signal(rnd, ebit):
    res = (_slope_pct(_ratio(rnd, ebit), 42).diff(42) / _sma(_ratio(rnd, ebit).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_diff_norm_63d_v131_signal(rnd):
    res = (_slope_pct(rnd, 63).diff(63) / _sma(rnd.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_diff_norm_63d_v132_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_diff_norm_63d_v133_signal(ebit):
    res = (_slope_pct(ebit, 63).diff(63) / _sma(ebit.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_diff_norm_63d_v134_signal(rnd, revenue):
    res = (_slope_pct(_ratio(rnd, revenue), 63).diff(63) / _sma(_ratio(rnd, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_diff_norm_63d_v135_signal(rnd, ebit):
    res = (_slope_pct(_ratio(rnd, ebit), 63).diff(63) / _sma(_ratio(rnd, ebit).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_diff_norm_126d_v136_signal(rnd):
    res = (_slope_pct(rnd, 126).diff(126) / _sma(rnd.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_diff_norm_126d_v137_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_diff_norm_126d_v138_signal(ebit):
    res = (_slope_pct(ebit, 126).diff(126) / _sma(ebit.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_diff_norm_126d_v139_signal(rnd, revenue):
    res = (_slope_pct(_ratio(rnd, revenue), 126).diff(126) / _sma(_ratio(rnd, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_diff_norm_126d_v140_signal(rnd, ebit):
    res = (_slope_pct(_ratio(rnd, ebit), 126).diff(126) / _sma(_ratio(rnd, ebit).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_diff_norm_252d_v141_signal(rnd):
    res = (_slope_pct(rnd, 252).diff(252) / _sma(rnd.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_diff_norm_252d_v142_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_diff_norm_252d_v143_signal(ebit):
    res = (_slope_pct(ebit, 252).diff(252) / _sma(ebit.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_diff_norm_252d_v144_signal(rnd, revenue):
    res = (_slope_pct(_ratio(rnd, revenue), 252).diff(252) / _sma(_ratio(rnd, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_diff_norm_252d_v145_signal(rnd, ebit):
    res = (_slope_pct(_ratio(rnd, ebit), 252).diff(252) / _sma(_ratio(rnd, ebit).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_slope_diff_norm_504d_v146_signal(rnd):
    res = (_slope_pct(rnd, 504).diff(504) / _sma(rnd.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_revenue_slope_diff_norm_504d_v147_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_ebit_slope_diff_norm_504d_v148_signal(ebit):
    res = (_slope_pct(ebit, 504).diff(504) / _sma(ebit.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_rev_slope_diff_norm_504d_v149_signal(rnd, revenue):
    res = (_slope_pct(_ratio(rnd, revenue), 504).diff(504) / _sma(_ratio(rnd, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_rnd_efficiency_rnd_to_ebit_slope_diff_norm_504d_v150_signal(rnd, ebit):
    res = (_slope_pct(_ratio(rnd, ebit), 504).diff(504) / _sma(_ratio(rnd, ebit).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 04...")
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
