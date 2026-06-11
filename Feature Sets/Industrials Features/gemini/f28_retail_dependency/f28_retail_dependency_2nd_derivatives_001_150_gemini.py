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

def f28_retail_dependency_receivables_slope_pct_5d_v001_signal(receivables):
    res = _slope_pct(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_5d_v002_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_5d_v003_signal(gp):
    res = _slope_pct(gp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_5d_v004_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_10d_v005_signal(receivables):
    res = _slope_pct(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_10d_v006_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_10d_v007_signal(gp):
    res = _slope_pct(gp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_10d_v008_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_21d_v009_signal(receivables):
    res = _slope_pct(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_21d_v010_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_21d_v011_signal(gp):
    res = _slope_pct(gp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_21d_v012_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_42d_v013_signal(receivables):
    res = _slope_pct(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_42d_v014_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_42d_v015_signal(gp):
    res = _slope_pct(gp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_42d_v016_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_63d_v017_signal(receivables):
    res = _slope_pct(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_63d_v018_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_63d_v019_signal(gp):
    res = _slope_pct(gp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_63d_v020_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_126d_v021_signal(receivables):
    res = _slope_pct(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_126d_v022_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_126d_v023_signal(gp):
    res = _slope_pct(gp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_126d_v024_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_252d_v025_signal(receivables):
    res = _slope_pct(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_252d_v026_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_252d_v027_signal(gp):
    res = _slope_pct(gp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_252d_v028_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_504d_v029_signal(receivables):
    res = _slope_pct(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_504d_v030_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_504d_v031_signal(gp):
    res = _slope_pct(gp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_504d_v032_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_756d_v033_signal(receivables):
    res = _slope_pct(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_756d_v034_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_756d_v035_signal(gp):
    res = _slope_pct(gp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_756d_v036_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_1008d_v037_signal(receivables):
    res = _slope_pct(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_1008d_v038_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_1008d_v039_signal(gp):
    res = _slope_pct(gp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_1008d_v040_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_pct_1260d_v041_signal(receivables):
    res = _slope_pct(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_pct_1260d_v042_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_pct_1260d_v043_signal(gp):
    res = _slope_pct(gp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_pct_1260d_v044_signal(receivables):
    res = _slope_pct(_slope_pct(receivables, 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_5d_v045_signal(receivables):
    res = _jerk(receivables, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_5d_v046_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_5d_v047_signal(gp):
    res = _jerk(gp, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_5d_v048_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_10d_v049_signal(receivables):
    res = _jerk(receivables, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_10d_v050_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_10d_v051_signal(gp):
    res = _jerk(gp, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_10d_v052_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_21d_v053_signal(receivables):
    res = _jerk(receivables, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_21d_v054_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_21d_v055_signal(gp):
    res = _jerk(gp, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_21d_v056_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_42d_v057_signal(receivables):
    res = _jerk(receivables, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_42d_v058_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_42d_v059_signal(gp):
    res = _jerk(gp, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_42d_v060_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_63d_v061_signal(receivables):
    res = _jerk(receivables, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_63d_v062_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_63d_v063_signal(gp):
    res = _jerk(gp, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_63d_v064_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_126d_v065_signal(receivables):
    res = _jerk(receivables, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_126d_v066_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_126d_v067_signal(gp):
    res = _jerk(gp, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_126d_v068_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_252d_v069_signal(receivables):
    res = _jerk(receivables, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_252d_v070_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_252d_v071_signal(gp):
    res = _jerk(gp, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_252d_v072_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_504d_v073_signal(receivables):
    res = _jerk(receivables, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_504d_v074_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_504d_v075_signal(gp):
    res = _jerk(gp, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_504d_v076_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_756d_v077_signal(receivables):
    res = _jerk(receivables, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_756d_v078_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_756d_v079_signal(gp):
    res = _jerk(gp, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_756d_v080_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_1008d_v081_signal(receivables):
    res = _jerk(receivables, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_1008d_v082_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_1008d_v083_signal(gp):
    res = _jerk(gp, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_1008d_v084_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_jerk_1260d_v085_signal(receivables):
    res = _jerk(receivables, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_jerk_1260d_v086_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_jerk_1260d_v087_signal(gp):
    res = _jerk(gp, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_jerk_1260d_v088_signal(receivables):
    res = _jerk(_slope_pct(receivables, 63), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_5d_v089_signal(receivables):
    res = (_slope_pct(receivables, 5).diff(5) / _sma(receivables.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_5d_v090_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_5d_v091_signal(gp):
    res = (_slope_pct(gp, 5).diff(5) / _sma(gp.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_5d_v092_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 5).diff(5) / _sma(_slope_pct(receivables, 63).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_10d_v093_signal(receivables):
    res = (_slope_pct(receivables, 10).diff(10) / _sma(receivables.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_10d_v094_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_10d_v095_signal(gp):
    res = (_slope_pct(gp, 10).diff(10) / _sma(gp.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_10d_v096_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 10).diff(10) / _sma(_slope_pct(receivables, 63).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_21d_v097_signal(receivables):
    res = (_slope_pct(receivables, 21).diff(21) / _sma(receivables.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_21d_v098_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_21d_v099_signal(gp):
    res = (_slope_pct(gp, 21).diff(21) / _sma(gp.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_21d_v100_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 21).diff(21) / _sma(_slope_pct(receivables, 63).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_42d_v101_signal(receivables):
    res = (_slope_pct(receivables, 42).diff(42) / _sma(receivables.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_42d_v102_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_42d_v103_signal(gp):
    res = (_slope_pct(gp, 42).diff(42) / _sma(gp.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_42d_v104_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 42).diff(42) / _sma(_slope_pct(receivables, 63).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_63d_v105_signal(receivables):
    res = (_slope_pct(receivables, 63).diff(63) / _sma(receivables.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_63d_v106_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_63d_v107_signal(gp):
    res = (_slope_pct(gp, 63).diff(63) / _sma(gp.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_63d_v108_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 63).diff(63) / _sma(_slope_pct(receivables, 63).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_126d_v109_signal(receivables):
    res = (_slope_pct(receivables, 126).diff(126) / _sma(receivables.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_126d_v110_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_126d_v111_signal(gp):
    res = (_slope_pct(gp, 126).diff(126) / _sma(gp.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_126d_v112_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 126).diff(126) / _sma(_slope_pct(receivables, 63).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_252d_v113_signal(receivables):
    res = (_slope_pct(receivables, 252).diff(252) / _sma(receivables.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_252d_v114_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_252d_v115_signal(gp):
    res = (_slope_pct(gp, 252).diff(252) / _sma(gp.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_252d_v116_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 252).diff(252) / _sma(_slope_pct(receivables, 63).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_504d_v117_signal(receivables):
    res = (_slope_pct(receivables, 504).diff(504) / _sma(receivables.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_504d_v118_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_504d_v119_signal(gp):
    res = (_slope_pct(gp, 504).diff(504) / _sma(gp.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_504d_v120_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 504).diff(504) / _sma(_slope_pct(receivables, 63).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_756d_v121_signal(receivables):
    res = (_slope_pct(receivables, 756).diff(756) / _sma(receivables.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_756d_v122_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_756d_v123_signal(gp):
    res = (_slope_pct(gp, 756).diff(756) / _sma(gp.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_756d_v124_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 756).diff(756) / _sma(_slope_pct(receivables, 63).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_1008d_v125_signal(receivables):
    res = (_slope_pct(receivables, 1008).diff(1008) / _sma(receivables.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_1008d_v126_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_1008d_v127_signal(gp):
    res = (_slope_pct(gp, 1008).diff(1008) / _sma(gp.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_1008d_v128_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 1008).diff(1008) / _sma(_slope_pct(receivables, 63).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_slope_diff_norm_1260d_v129_signal(receivables):
    res = (_slope_pct(receivables, 1260).diff(1260) / _sma(receivables.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_slope_diff_norm_1260d_v130_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_slope_diff_norm_1260d_v131_signal(gp):
    res = (_slope_pct(gp, 1260).diff(1260) / _sma(gp.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_slope_diff_norm_1260d_v132_signal(receivables):
    res = (_slope_pct(_slope_pct(receivables, 63), 1260).diff(1260) / _sma(_slope_pct(receivables, 63).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_mom_z_5d_v133_signal(receivables):
    res = _z(_slope_pct(receivables, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_mom_z_5d_v134_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_mom_z_5d_v135_signal(gp):
    res = _z(_slope_pct(gp, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_mom_z_5d_v136_signal(receivables):
    res = _z(_slope_pct(_slope_pct(receivables, 63), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_mom_z_10d_v137_signal(receivables):
    res = _z(_slope_pct(receivables, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_mom_z_10d_v138_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_mom_z_10d_v139_signal(gp):
    res = _z(_slope_pct(gp, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_mom_z_10d_v140_signal(receivables):
    res = _z(_slope_pct(_slope_pct(receivables, 63), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_mom_z_21d_v141_signal(receivables):
    res = _z(_slope_pct(receivables, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_mom_z_21d_v142_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_mom_z_21d_v143_signal(gp):
    res = _z(_slope_pct(gp, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_mom_z_21d_v144_signal(receivables):
    res = _z(_slope_pct(_slope_pct(receivables, 63), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_mom_z_42d_v145_signal(receivables):
    res = _z(_slope_pct(receivables, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_mom_z_42d_v146_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_gp_mom_z_42d_v147_signal(gp):
    res = _z(_slope_pct(gp, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_rec_momentum_mom_z_42d_v148_signal(receivables):
    res = _z(_slope_pct(_slope_pct(receivables, 63), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_receivables_mom_z_63d_v149_signal(receivables):
    res = _z(_slope_pct(receivables, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f28_retail_dependency_revenue_mom_z_63d_v150_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "gp": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 28...")
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
