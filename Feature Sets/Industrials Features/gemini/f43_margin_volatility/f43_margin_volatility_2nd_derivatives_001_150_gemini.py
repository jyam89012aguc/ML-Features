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

def f43_margin_volatility_grossmargin_slope_pct_5d_v001_signal(grossmargin):
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_5d_v002_signal(cor):
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_5d_v003_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_5d_v004_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_10d_v005_signal(grossmargin):
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_10d_v006_signal(cor):
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_10d_v007_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_10d_v008_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_21d_v009_signal(grossmargin):
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_21d_v010_signal(cor):
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_21d_v011_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_21d_v012_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_42d_v013_signal(grossmargin):
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_42d_v014_signal(cor):
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_42d_v015_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_42d_v016_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_63d_v017_signal(grossmargin):
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_63d_v018_signal(cor):
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_63d_v019_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_63d_v020_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_126d_v021_signal(grossmargin):
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_126d_v022_signal(cor):
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_126d_v023_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_126d_v024_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_252d_v025_signal(grossmargin):
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_252d_v026_signal(cor):
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_252d_v027_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_252d_v028_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_504d_v029_signal(grossmargin):
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_504d_v030_signal(cor):
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_504d_v031_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_504d_v032_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_756d_v033_signal(grossmargin):
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_756d_v034_signal(cor):
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_756d_v035_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_756d_v036_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_1008d_v037_signal(grossmargin):
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_1008d_v038_signal(cor):
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_1008d_v039_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_1008d_v040_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_pct_1260d_v041_signal(grossmargin):
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_pct_1260d_v042_signal(cor):
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_pct_1260d_v043_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_pct_1260d_v044_signal(grossmargin):
    res = _slope_pct(_std(grossmargin, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_5d_v045_signal(grossmargin):
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_5d_v046_signal(cor):
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_5d_v047_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_5d_v048_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_10d_v049_signal(grossmargin):
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_10d_v050_signal(cor):
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_10d_v051_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_10d_v052_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_21d_v053_signal(grossmargin):
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_21d_v054_signal(cor):
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_21d_v055_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_21d_v056_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_42d_v057_signal(grossmargin):
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_42d_v058_signal(cor):
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_42d_v059_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_42d_v060_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_63d_v061_signal(grossmargin):
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_63d_v062_signal(cor):
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_63d_v063_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_63d_v064_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_126d_v065_signal(grossmargin):
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_126d_v066_signal(cor):
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_126d_v067_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_126d_v068_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_252d_v069_signal(grossmargin):
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_252d_v070_signal(cor):
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_252d_v071_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_252d_v072_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_504d_v073_signal(grossmargin):
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_504d_v074_signal(cor):
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_504d_v075_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_504d_v076_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_756d_v077_signal(grossmargin):
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_756d_v078_signal(cor):
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_756d_v079_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_756d_v080_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_1008d_v081_signal(grossmargin):
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_1008d_v082_signal(cor):
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_1008d_v083_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_1008d_v084_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_jerk_1260d_v085_signal(grossmargin):
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_jerk_1260d_v086_signal(cor):
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_jerk_1260d_v087_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_jerk_1260d_v088_signal(grossmargin):
    res = _jerk(_std(grossmargin, 252), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_5d_v089_signal(grossmargin):
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_5d_v090_signal(cor):
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_5d_v091_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_5d_v092_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 5).diff(5) / _sma(_std(grossmargin, 252).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_10d_v093_signal(grossmargin):
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_10d_v094_signal(cor):
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_10d_v095_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_10d_v096_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 10).diff(10) / _sma(_std(grossmargin, 252).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_21d_v097_signal(grossmargin):
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_21d_v098_signal(cor):
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_21d_v099_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_21d_v100_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 21).diff(21) / _sma(_std(grossmargin, 252).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_42d_v101_signal(grossmargin):
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_42d_v102_signal(cor):
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_42d_v103_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_42d_v104_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 42).diff(42) / _sma(_std(grossmargin, 252).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_63d_v105_signal(grossmargin):
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_63d_v106_signal(cor):
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_63d_v107_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_63d_v108_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 63).diff(63) / _sma(_std(grossmargin, 252).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_126d_v109_signal(grossmargin):
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_126d_v110_signal(cor):
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_126d_v111_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_126d_v112_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 126).diff(126) / _sma(_std(grossmargin, 252).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_252d_v113_signal(grossmargin):
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_252d_v114_signal(cor):
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_252d_v115_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_252d_v116_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 252).diff(252) / _sma(_std(grossmargin, 252).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_504d_v117_signal(grossmargin):
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_504d_v118_signal(cor):
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_504d_v119_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_504d_v120_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 504).diff(504) / _sma(_std(grossmargin, 252).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_756d_v121_signal(grossmargin):
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_756d_v122_signal(cor):
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_756d_v123_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_756d_v124_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 756).diff(756) / _sma(_std(grossmargin, 252).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_1008d_v125_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_1008d_v126_signal(cor):
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_1008d_v127_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_1008d_v128_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 1008).diff(1008) / _sma(_std(grossmargin, 252).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_slope_diff_norm_1260d_v129_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_slope_diff_norm_1260d_v130_signal(cor):
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_slope_diff_norm_1260d_v131_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_slope_diff_norm_1260d_v132_signal(grossmargin):
    res = (_slope_pct(_std(grossmargin, 252), 1260).diff(1260) / _sma(_std(grossmargin, 252).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_5d_v133_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_5d_v134_signal(cor):
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_5d_v135_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_5d_v136_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_10d_v137_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_10d_v138_signal(cor):
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_10d_v139_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_10d_v140_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_21d_v141_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_21d_v142_signal(cor):
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_21d_v143_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_21d_v144_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_42d_v145_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_42d_v146_signal(cor):
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_revenue_mom_z_42d_v147_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_margin_vol_mom_z_42d_v148_signal(grossmargin):
    res = _z(_slope_pct(_std(grossmargin, 252), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_grossmargin_mom_z_63d_v149_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_margin_volatility_cor_mom_z_63d_v150_signal(cor):
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 43...")
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
