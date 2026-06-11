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

def f13_electrification_expansion_ebitdamargin_slope_pct_5d_v001_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_5d_v002_signal(ebitda):
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_5d_v003_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_5d_v004_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_10d_v005_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_10d_v006_signal(ebitda):
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_10d_v007_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_10d_v008_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_21d_v009_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_21d_v010_signal(ebitda):
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_21d_v011_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_21d_v012_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_42d_v013_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_42d_v014_signal(ebitda):
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_42d_v015_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_42d_v016_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_63d_v017_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_63d_v018_signal(ebitda):
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_63d_v019_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_63d_v020_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_126d_v021_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_126d_v022_signal(ebitda):
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_126d_v023_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_126d_v024_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_252d_v025_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_252d_v026_signal(ebitda):
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_252d_v027_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_252d_v028_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_504d_v029_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_504d_v030_signal(ebitda):
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_504d_v031_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_504d_v032_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_756d_v033_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_756d_v034_signal(ebitda):
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_756d_v035_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_756d_v036_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_1008d_v037_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_1008d_v038_signal(ebitda):
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_1008d_v039_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_1008d_v040_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_pct_1260d_v041_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_pct_1260d_v042_signal(ebitda):
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_pct_1260d_v043_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_pct_1260d_v044_signal(ebitda, revenue):
    res = _slope_pct(ebitda / revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_5d_v045_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_5d_v046_signal(ebitda):
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_5d_v047_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_5d_v048_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_10d_v049_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_10d_v050_signal(ebitda):
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_10d_v051_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_10d_v052_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_21d_v053_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_21d_v054_signal(ebitda):
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_21d_v055_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_21d_v056_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_42d_v057_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_42d_v058_signal(ebitda):
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_42d_v059_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_42d_v060_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_63d_v061_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_63d_v062_signal(ebitda):
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_63d_v063_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_63d_v064_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_126d_v065_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_126d_v066_signal(ebitda):
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_126d_v067_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_126d_v068_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_252d_v069_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_252d_v070_signal(ebitda):
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_252d_v071_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_252d_v072_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_504d_v073_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_504d_v074_signal(ebitda):
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_504d_v075_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_504d_v076_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_756d_v077_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_756d_v078_signal(ebitda):
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_756d_v079_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_756d_v080_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_1008d_v081_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_1008d_v082_signal(ebitda):
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_1008d_v083_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_1008d_v084_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_jerk_1260d_v085_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_jerk_1260d_v086_signal(ebitda):
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_jerk_1260d_v087_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_jerk_1260d_v088_signal(ebitda, revenue):
    res = _jerk(ebitda / revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_5d_v089_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 5).diff(5) / _sma(ebitdamargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_5d_v090_signal(ebitda):
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_5d_v091_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_5d_v092_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 5).diff(5) / _sma(ebitda / revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_10d_v093_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 10).diff(10) / _sma(ebitdamargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_10d_v094_signal(ebitda):
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_10d_v095_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_10d_v096_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 10).diff(10) / _sma(ebitda / revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_21d_v097_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 21).diff(21) / _sma(ebitdamargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_21d_v098_signal(ebitda):
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_21d_v099_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_21d_v100_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 21).diff(21) / _sma(ebitda / revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_42d_v101_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 42).diff(42) / _sma(ebitdamargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_42d_v102_signal(ebitda):
    res = (_slope_pct(ebitda, 42).diff(42) / _sma(ebitda.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_42d_v103_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_42d_v104_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 42).diff(42) / _sma(ebitda / revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_63d_v105_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 63).diff(63) / _sma(ebitdamargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_63d_v106_signal(ebitda):
    res = (_slope_pct(ebitda, 63).diff(63) / _sma(ebitda.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_63d_v107_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_63d_v108_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 63).diff(63) / _sma(ebitda / revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_126d_v109_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 126).diff(126) / _sma(ebitdamargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_126d_v110_signal(ebitda):
    res = (_slope_pct(ebitda, 126).diff(126) / _sma(ebitda.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_126d_v111_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_126d_v112_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 126).diff(126) / _sma(ebitda / revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_252d_v113_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 252).diff(252) / _sma(ebitdamargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_252d_v114_signal(ebitda):
    res = (_slope_pct(ebitda, 252).diff(252) / _sma(ebitda.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_252d_v115_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_252d_v116_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 252).diff(252) / _sma(ebitda / revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_504d_v117_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 504).diff(504) / _sma(ebitdamargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_504d_v118_signal(ebitda):
    res = (_slope_pct(ebitda, 504).diff(504) / _sma(ebitda.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_504d_v119_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_504d_v120_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 504).diff(504) / _sma(ebitda / revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_756d_v121_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 756).diff(756) / _sma(ebitdamargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_756d_v122_signal(ebitda):
    res = (_slope_pct(ebitda, 756).diff(756) / _sma(ebitda.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_756d_v123_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_756d_v124_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 756).diff(756) / _sma(ebitda / revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_1008d_v125_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 1008).diff(1008) / _sma(ebitdamargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_1008d_v126_signal(ebitda):
    res = (_slope_pct(ebitda, 1008).diff(1008) / _sma(ebitda.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_1008d_v127_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_1008d_v128_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 1008).diff(1008) / _sma(ebitda / revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_slope_diff_norm_1260d_v129_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 1260).diff(1260) / _sma(ebitdamargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_slope_diff_norm_1260d_v130_signal(ebitda):
    res = (_slope_pct(ebitda, 1260).diff(1260) / _sma(ebitda.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_slope_diff_norm_1260d_v131_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_slope_diff_norm_1260d_v132_signal(ebitda, revenue):
    res = (_slope_pct(ebitda / revenue, 1260).diff(1260) / _sma(ebitda / revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_mom_z_5d_v133_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_mom_z_5d_v134_signal(ebitda):
    res = _z(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_mom_z_5d_v135_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_mom_z_5d_v136_signal(ebitda, revenue):
    res = _z(_slope_pct(ebitda / revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_mom_z_10d_v137_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_mom_z_10d_v138_signal(ebitda):
    res = _z(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_mom_z_10d_v139_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_mom_z_10d_v140_signal(ebitda, revenue):
    res = _z(_slope_pct(ebitda / revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_mom_z_21d_v141_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_mom_z_21d_v142_signal(ebitda):
    res = _z(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_mom_z_21d_v143_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_mom_z_21d_v144_signal(ebitda, revenue):
    res = _z(_slope_pct(ebitda / revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_mom_z_42d_v145_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_mom_z_42d_v146_signal(ebitda):
    res = _z(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_revenue_mom_z_42d_v147_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_margin_mom_z_42d_v148_signal(ebitda, revenue):
    res = _z(_slope_pct(ebitda / revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitdamargin_mom_z_63d_v149_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_electrification_expansion_ebitda_mom_z_63d_v150_signal(ebitda):
    res = _z(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 13...")
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
