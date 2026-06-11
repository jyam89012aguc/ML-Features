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

def f35_route_density_cor_slope_pct_5d_v001_signal(cor):
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_5d_v002_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_5d_v003_signal(ebit):
    res = _slope_pct(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_5d_v004_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_10d_v005_signal(cor):
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_10d_v006_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_10d_v007_signal(ebit):
    res = _slope_pct(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_10d_v008_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_21d_v009_signal(cor):
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_21d_v010_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_21d_v011_signal(ebit):
    res = _slope_pct(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_21d_v012_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_42d_v013_signal(cor):
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_42d_v014_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_42d_v015_signal(ebit):
    res = _slope_pct(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_42d_v016_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_63d_v017_signal(cor):
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_63d_v018_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_63d_v019_signal(ebit):
    res = _slope_pct(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_63d_v020_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_126d_v021_signal(cor):
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_126d_v022_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_126d_v023_signal(ebit):
    res = _slope_pct(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_126d_v024_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_252d_v025_signal(cor):
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_252d_v026_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_252d_v027_signal(ebit):
    res = _slope_pct(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_252d_v028_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_504d_v029_signal(cor):
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_504d_v030_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_504d_v031_signal(ebit):
    res = _slope_pct(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_504d_v032_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_756d_v033_signal(cor):
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_756d_v034_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_756d_v035_signal(ebit):
    res = _slope_pct(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_756d_v036_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_1008d_v037_signal(cor):
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_1008d_v038_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_1008d_v039_signal(ebit):
    res = _slope_pct(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_1008d_v040_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_pct_1260d_v041_signal(cor):
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_pct_1260d_v042_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_pct_1260d_v043_signal(ebit):
    res = _slope_pct(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_pct_1260d_v044_signal(revenue, cor):
    res = _slope_pct(_ratio(revenue, cor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_5d_v045_signal(cor):
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_5d_v046_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_5d_v047_signal(ebit):
    res = _jerk(ebit, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_5d_v048_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_10d_v049_signal(cor):
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_10d_v050_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_10d_v051_signal(ebit):
    res = _jerk(ebit, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_10d_v052_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_21d_v053_signal(cor):
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_21d_v054_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_21d_v055_signal(ebit):
    res = _jerk(ebit, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_21d_v056_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_42d_v057_signal(cor):
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_42d_v058_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_42d_v059_signal(ebit):
    res = _jerk(ebit, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_42d_v060_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_63d_v061_signal(cor):
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_63d_v062_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_63d_v063_signal(ebit):
    res = _jerk(ebit, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_63d_v064_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_126d_v065_signal(cor):
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_126d_v066_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_126d_v067_signal(ebit):
    res = _jerk(ebit, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_126d_v068_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_252d_v069_signal(cor):
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_252d_v070_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_252d_v071_signal(ebit):
    res = _jerk(ebit, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_252d_v072_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_504d_v073_signal(cor):
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_504d_v074_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_504d_v075_signal(ebit):
    res = _jerk(ebit, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_504d_v076_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_756d_v077_signal(cor):
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_756d_v078_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_756d_v079_signal(ebit):
    res = _jerk(ebit, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_756d_v080_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_1008d_v081_signal(cor):
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_1008d_v082_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_1008d_v083_signal(ebit):
    res = _jerk(ebit, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_1008d_v084_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_jerk_1260d_v085_signal(cor):
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_jerk_1260d_v086_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_jerk_1260d_v087_signal(ebit):
    res = _jerk(ebit, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_jerk_1260d_v088_signal(revenue, cor):
    res = _jerk(_ratio(revenue, cor), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_5d_v089_signal(cor):
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_5d_v090_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_5d_v091_signal(ebit):
    res = (_slope_pct(ebit, 5).diff(5) / _sma(ebit.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_5d_v092_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 5).diff(5) / _sma(_ratio(revenue, cor).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_10d_v093_signal(cor):
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_10d_v094_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_10d_v095_signal(ebit):
    res = (_slope_pct(ebit, 10).diff(10) / _sma(ebit.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_10d_v096_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 10).diff(10) / _sma(_ratio(revenue, cor).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_21d_v097_signal(cor):
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_21d_v098_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_21d_v099_signal(ebit):
    res = (_slope_pct(ebit, 21).diff(21) / _sma(ebit.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_21d_v100_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 21).diff(21) / _sma(_ratio(revenue, cor).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_42d_v101_signal(cor):
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_42d_v102_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_42d_v103_signal(ebit):
    res = (_slope_pct(ebit, 42).diff(42) / _sma(ebit.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_42d_v104_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 42).diff(42) / _sma(_ratio(revenue, cor).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_63d_v105_signal(cor):
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_63d_v106_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_63d_v107_signal(ebit):
    res = (_slope_pct(ebit, 63).diff(63) / _sma(ebit.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_63d_v108_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 63).diff(63) / _sma(_ratio(revenue, cor).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_126d_v109_signal(cor):
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_126d_v110_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_126d_v111_signal(ebit):
    res = (_slope_pct(ebit, 126).diff(126) / _sma(ebit.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_126d_v112_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 126).diff(126) / _sma(_ratio(revenue, cor).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_252d_v113_signal(cor):
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_252d_v114_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_252d_v115_signal(ebit):
    res = (_slope_pct(ebit, 252).diff(252) / _sma(ebit.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_252d_v116_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 252).diff(252) / _sma(_ratio(revenue, cor).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_504d_v117_signal(cor):
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_504d_v118_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_504d_v119_signal(ebit):
    res = (_slope_pct(ebit, 504).diff(504) / _sma(ebit.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_504d_v120_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 504).diff(504) / _sma(_ratio(revenue, cor).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_756d_v121_signal(cor):
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_756d_v122_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_756d_v123_signal(ebit):
    res = (_slope_pct(ebit, 756).diff(756) / _sma(ebit.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_756d_v124_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 756).diff(756) / _sma(_ratio(revenue, cor).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_1008d_v125_signal(cor):
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_1008d_v126_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_1008d_v127_signal(ebit):
    res = (_slope_pct(ebit, 1008).diff(1008) / _sma(ebit.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_1008d_v128_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 1008).diff(1008) / _sma(_ratio(revenue, cor).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_slope_diff_norm_1260d_v129_signal(cor):
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_slope_diff_norm_1260d_v130_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_slope_diff_norm_1260d_v131_signal(ebit):
    res = (_slope_pct(ebit, 1260).diff(1260) / _sma(ebit.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_slope_diff_norm_1260d_v132_signal(revenue, cor):
    res = (_slope_pct(_ratio(revenue, cor), 1260).diff(1260) / _sma(_ratio(revenue, cor).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_mom_z_5d_v133_signal(cor):
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_mom_z_5d_v134_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_mom_z_5d_v135_signal(ebit):
    res = _z(_slope_pct(ebit, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_mom_z_5d_v136_signal(revenue, cor):
    res = _z(_slope_pct(_ratio(revenue, cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_mom_z_10d_v137_signal(cor):
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_mom_z_10d_v138_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_mom_z_10d_v139_signal(ebit):
    res = _z(_slope_pct(ebit, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_mom_z_10d_v140_signal(revenue, cor):
    res = _z(_slope_pct(_ratio(revenue, cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_mom_z_21d_v141_signal(cor):
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_mom_z_21d_v142_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_mom_z_21d_v143_signal(ebit):
    res = _z(_slope_pct(ebit, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_mom_z_21d_v144_signal(revenue, cor):
    res = _z(_slope_pct(_ratio(revenue, cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_mom_z_42d_v145_signal(cor):
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_mom_z_42d_v146_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_ebit_mom_z_42d_v147_signal(ebit):
    res = _z(_slope_pct(ebit, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_efficiency_mom_z_42d_v148_signal(revenue, cor):
    res = _z(_slope_pct(_ratio(revenue, cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_cor_mom_z_63d_v149_signal(cor):
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_route_density_revenue_mom_z_63d_v150_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 35...")
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
