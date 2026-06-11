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

def f22_warranty_risk_sgna_slope_pct_5d_v001_signal(sgna):
    res = _slope_pct(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_5d_v002_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_5d_v003_signal(netinc):
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_5d_v004_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_10d_v005_signal(sgna):
    res = _slope_pct(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_10d_v006_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_10d_v007_signal(netinc):
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_10d_v008_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_21d_v009_signal(sgna):
    res = _slope_pct(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_21d_v010_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_21d_v011_signal(netinc):
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_21d_v012_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_42d_v013_signal(sgna):
    res = _slope_pct(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_42d_v014_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_42d_v015_signal(netinc):
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_42d_v016_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_63d_v017_signal(sgna):
    res = _slope_pct(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_63d_v018_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_63d_v019_signal(netinc):
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_63d_v020_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_126d_v021_signal(sgna):
    res = _slope_pct(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_126d_v022_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_126d_v023_signal(netinc):
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_126d_v024_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_252d_v025_signal(sgna):
    res = _slope_pct(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_252d_v026_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_252d_v027_signal(netinc):
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_252d_v028_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_504d_v029_signal(sgna):
    res = _slope_pct(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_504d_v030_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_504d_v031_signal(netinc):
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_504d_v032_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_756d_v033_signal(sgna):
    res = _slope_pct(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_756d_v034_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_756d_v035_signal(netinc):
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_756d_v036_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_1008d_v037_signal(sgna):
    res = _slope_pct(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_1008d_v038_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_1008d_v039_signal(netinc):
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_1008d_v040_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_pct_1260d_v041_signal(sgna):
    res = _slope_pct(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_pct_1260d_v042_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_pct_1260d_v043_signal(netinc):
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_pct_1260d_v044_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_5d_v045_signal(sgna):
    res = _jerk(sgna, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_5d_v046_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_5d_v047_signal(netinc):
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_5d_v048_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_10d_v049_signal(sgna):
    res = _jerk(sgna, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_10d_v050_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_10d_v051_signal(netinc):
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_10d_v052_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_21d_v053_signal(sgna):
    res = _jerk(sgna, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_21d_v054_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_21d_v055_signal(netinc):
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_21d_v056_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_42d_v057_signal(sgna):
    res = _jerk(sgna, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_42d_v058_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_42d_v059_signal(netinc):
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_42d_v060_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_63d_v061_signal(sgna):
    res = _jerk(sgna, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_63d_v062_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_63d_v063_signal(netinc):
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_63d_v064_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_126d_v065_signal(sgna):
    res = _jerk(sgna, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_126d_v066_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_126d_v067_signal(netinc):
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_126d_v068_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_252d_v069_signal(sgna):
    res = _jerk(sgna, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_252d_v070_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_252d_v071_signal(netinc):
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_252d_v072_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_504d_v073_signal(sgna):
    res = _jerk(sgna, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_504d_v074_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_504d_v075_signal(netinc):
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_504d_v076_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_756d_v077_signal(sgna):
    res = _jerk(sgna, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_756d_v078_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_756d_v079_signal(netinc):
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_756d_v080_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_1008d_v081_signal(sgna):
    res = _jerk(sgna, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_1008d_v082_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_1008d_v083_signal(netinc):
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_1008d_v084_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_jerk_1260d_v085_signal(sgna):
    res = _jerk(sgna, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_jerk_1260d_v086_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_jerk_1260d_v087_signal(netinc):
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_jerk_1260d_v088_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_5d_v089_signal(sgna):
    res = (_slope_pct(sgna, 5).diff(5) / _sma(sgna.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_5d_v090_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_5d_v091_signal(netinc):
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_5d_v092_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 5).diff(5) / _sma(_ratio(sgna, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_10d_v093_signal(sgna):
    res = (_slope_pct(sgna, 10).diff(10) / _sma(sgna.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_10d_v094_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_10d_v095_signal(netinc):
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_10d_v096_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 10).diff(10) / _sma(_ratio(sgna, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_21d_v097_signal(sgna):
    res = (_slope_pct(sgna, 21).diff(21) / _sma(sgna.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_21d_v098_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_21d_v099_signal(netinc):
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_21d_v100_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 21).diff(21) / _sma(_ratio(sgna, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_42d_v101_signal(sgna):
    res = (_slope_pct(sgna, 42).diff(42) / _sma(sgna.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_42d_v102_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_42d_v103_signal(netinc):
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_42d_v104_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 42).diff(42) / _sma(_ratio(sgna, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_63d_v105_signal(sgna):
    res = (_slope_pct(sgna, 63).diff(63) / _sma(sgna.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_63d_v106_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_63d_v107_signal(netinc):
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_63d_v108_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 63).diff(63) / _sma(_ratio(sgna, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_126d_v109_signal(sgna):
    res = (_slope_pct(sgna, 126).diff(126) / _sma(sgna.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_126d_v110_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_126d_v111_signal(netinc):
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_126d_v112_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 126).diff(126) / _sma(_ratio(sgna, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_252d_v113_signal(sgna):
    res = (_slope_pct(sgna, 252).diff(252) / _sma(sgna.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_252d_v114_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_252d_v115_signal(netinc):
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_252d_v116_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 252).diff(252) / _sma(_ratio(sgna, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_504d_v117_signal(sgna):
    res = (_slope_pct(sgna, 504).diff(504) / _sma(sgna.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_504d_v118_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_504d_v119_signal(netinc):
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_504d_v120_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 504).diff(504) / _sma(_ratio(sgna, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_756d_v121_signal(sgna):
    res = (_slope_pct(sgna, 756).diff(756) / _sma(sgna.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_756d_v122_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_756d_v123_signal(netinc):
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_756d_v124_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 756).diff(756) / _sma(_ratio(sgna, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_1008d_v125_signal(sgna):
    res = (_slope_pct(sgna, 1008).diff(1008) / _sma(sgna.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_1008d_v126_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_1008d_v127_signal(netinc):
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_1008d_v128_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 1008).diff(1008) / _sma(_ratio(sgna, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_slope_diff_norm_1260d_v129_signal(sgna):
    res = (_slope_pct(sgna, 1260).diff(1260) / _sma(sgna.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_slope_diff_norm_1260d_v130_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_slope_diff_norm_1260d_v131_signal(netinc):
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_slope_diff_norm_1260d_v132_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 1260).diff(1260) / _sma(_ratio(sgna, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_mom_z_5d_v133_signal(sgna):
    res = _z(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_mom_z_5d_v134_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_mom_z_5d_v135_signal(netinc):
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_mom_z_5d_v136_signal(sgna, revenue):
    res = _z(_slope_pct(_ratio(sgna, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_mom_z_10d_v137_signal(sgna):
    res = _z(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_mom_z_10d_v138_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_mom_z_10d_v139_signal(netinc):
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_mom_z_10d_v140_signal(sgna, revenue):
    res = _z(_slope_pct(_ratio(sgna, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_mom_z_21d_v141_signal(sgna):
    res = _z(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_mom_z_21d_v142_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_mom_z_21d_v143_signal(netinc):
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_mom_z_21d_v144_signal(sgna, revenue):
    res = _z(_slope_pct(_ratio(sgna, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_mom_z_42d_v145_signal(sgna):
    res = _z(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_mom_z_42d_v146_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_netinc_mom_z_42d_v147_signal(netinc):
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_to_rev_mom_z_42d_v148_signal(sgna, revenue):
    res = _z(_slope_pct(_ratio(sgna, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_sgna_mom_z_63d_v149_signal(sgna):
    res = _z(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_warranty_risk_revenue_mom_z_63d_v150_signal(revenue):
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
    print(f"Testing {len(funcs)} functions for family 22...")
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
