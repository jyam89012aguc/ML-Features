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

def f05_platform_lifecycle_ebitdamargin_slope_pct_5d_v001_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_5d_v002_signal(ebitda):
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_5d_v003_signal(ebit):
    res = _slope_pct(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_5d_v004_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_10d_v005_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_10d_v006_signal(ebitda):
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_10d_v007_signal(ebit):
    res = _slope_pct(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_10d_v008_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_21d_v009_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_21d_v010_signal(ebitda):
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_21d_v011_signal(ebit):
    res = _slope_pct(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_21d_v012_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_42d_v013_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_42d_v014_signal(ebitda):
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_42d_v015_signal(ebit):
    res = _slope_pct(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_42d_v016_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_63d_v017_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_63d_v018_signal(ebitda):
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_63d_v019_signal(ebit):
    res = _slope_pct(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_63d_v020_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_126d_v021_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_126d_v022_signal(ebitda):
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_126d_v023_signal(ebit):
    res = _slope_pct(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_126d_v024_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_252d_v025_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_252d_v026_signal(ebitda):
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_252d_v027_signal(ebit):
    res = _slope_pct(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_252d_v028_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_504d_v029_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_504d_v030_signal(ebitda):
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_504d_v031_signal(ebit):
    res = _slope_pct(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_504d_v032_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_756d_v033_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_756d_v034_signal(ebitda):
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_756d_v035_signal(ebit):
    res = _slope_pct(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_756d_v036_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_1008d_v037_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_1008d_v038_signal(ebitda):
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_1008d_v039_signal(ebit):
    res = _slope_pct(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_1008d_v040_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_pct_1260d_v041_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_pct_1260d_v042_signal(ebitda):
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_pct_1260d_v043_signal(ebit):
    res = _slope_pct(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_pct_1260d_v044_signal(ebit, ebitda):
    res = _slope_pct(_ratio(ebit, ebitda), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_5d_v045_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_5d_v046_signal(ebitda):
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_5d_v047_signal(ebit):
    res = _jerk(ebit, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_5d_v048_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_10d_v049_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_10d_v050_signal(ebitda):
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_10d_v051_signal(ebit):
    res = _jerk(ebit, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_10d_v052_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_21d_v053_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_21d_v054_signal(ebitda):
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_21d_v055_signal(ebit):
    res = _jerk(ebit, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_21d_v056_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_42d_v057_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_42d_v058_signal(ebitda):
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_42d_v059_signal(ebit):
    res = _jerk(ebit, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_42d_v060_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_63d_v061_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_63d_v062_signal(ebitda):
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_63d_v063_signal(ebit):
    res = _jerk(ebit, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_63d_v064_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_126d_v065_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_126d_v066_signal(ebitda):
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_126d_v067_signal(ebit):
    res = _jerk(ebit, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_126d_v068_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_252d_v069_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_252d_v070_signal(ebitda):
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_252d_v071_signal(ebit):
    res = _jerk(ebit, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_252d_v072_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_504d_v073_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_504d_v074_signal(ebitda):
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_504d_v075_signal(ebit):
    res = _jerk(ebit, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_504d_v076_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_756d_v077_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_756d_v078_signal(ebitda):
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_756d_v079_signal(ebit):
    res = _jerk(ebit, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_756d_v080_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_1008d_v081_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_1008d_v082_signal(ebitda):
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_1008d_v083_signal(ebit):
    res = _jerk(ebit, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_1008d_v084_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_jerk_1260d_v085_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_jerk_1260d_v086_signal(ebitda):
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_jerk_1260d_v087_signal(ebit):
    res = _jerk(ebit, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_jerk_1260d_v088_signal(ebit, ebitda):
    res = _jerk(_ratio(ebit, ebitda), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_5d_v089_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 5).diff(5) / _sma(ebitdamargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_5d_v090_signal(ebitda):
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_5d_v091_signal(ebit):
    res = (_slope_pct(ebit, 5).diff(5) / _sma(ebit.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_5d_v092_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 5).diff(5) / _sma(_ratio(ebit, ebitda).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_10d_v093_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 10).diff(10) / _sma(ebitdamargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_10d_v094_signal(ebitda):
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_10d_v095_signal(ebit):
    res = (_slope_pct(ebit, 10).diff(10) / _sma(ebit.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_10d_v096_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 10).diff(10) / _sma(_ratio(ebit, ebitda).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_21d_v097_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 21).diff(21) / _sma(ebitdamargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_21d_v098_signal(ebitda):
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_21d_v099_signal(ebit):
    res = (_slope_pct(ebit, 21).diff(21) / _sma(ebit.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_21d_v100_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 21).diff(21) / _sma(_ratio(ebit, ebitda).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_42d_v101_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 42).diff(42) / _sma(ebitdamargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_42d_v102_signal(ebitda):
    res = (_slope_pct(ebitda, 42).diff(42) / _sma(ebitda.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_42d_v103_signal(ebit):
    res = (_slope_pct(ebit, 42).diff(42) / _sma(ebit.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_42d_v104_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 42).diff(42) / _sma(_ratio(ebit, ebitda).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_63d_v105_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 63).diff(63) / _sma(ebitdamargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_63d_v106_signal(ebitda):
    res = (_slope_pct(ebitda, 63).diff(63) / _sma(ebitda.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_63d_v107_signal(ebit):
    res = (_slope_pct(ebit, 63).diff(63) / _sma(ebit.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_63d_v108_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 63).diff(63) / _sma(_ratio(ebit, ebitda).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_126d_v109_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 126).diff(126) / _sma(ebitdamargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_126d_v110_signal(ebitda):
    res = (_slope_pct(ebitda, 126).diff(126) / _sma(ebitda.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_126d_v111_signal(ebit):
    res = (_slope_pct(ebit, 126).diff(126) / _sma(ebit.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_126d_v112_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 126).diff(126) / _sma(_ratio(ebit, ebitda).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_252d_v113_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 252).diff(252) / _sma(ebitdamargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_252d_v114_signal(ebitda):
    res = (_slope_pct(ebitda, 252).diff(252) / _sma(ebitda.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_252d_v115_signal(ebit):
    res = (_slope_pct(ebit, 252).diff(252) / _sma(ebit.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_252d_v116_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 252).diff(252) / _sma(_ratio(ebit, ebitda).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_504d_v117_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 504).diff(504) / _sma(ebitdamargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_504d_v118_signal(ebitda):
    res = (_slope_pct(ebitda, 504).diff(504) / _sma(ebitda.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_504d_v119_signal(ebit):
    res = (_slope_pct(ebit, 504).diff(504) / _sma(ebit.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_504d_v120_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 504).diff(504) / _sma(_ratio(ebit, ebitda).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_756d_v121_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 756).diff(756) / _sma(ebitdamargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_756d_v122_signal(ebitda):
    res = (_slope_pct(ebitda, 756).diff(756) / _sma(ebitda.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_756d_v123_signal(ebit):
    res = (_slope_pct(ebit, 756).diff(756) / _sma(ebit.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_756d_v124_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 756).diff(756) / _sma(_ratio(ebit, ebitda).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_1008d_v125_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 1008).diff(1008) / _sma(ebitdamargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_1008d_v126_signal(ebitda):
    res = (_slope_pct(ebitda, 1008).diff(1008) / _sma(ebitda.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_1008d_v127_signal(ebit):
    res = (_slope_pct(ebit, 1008).diff(1008) / _sma(ebit.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_1008d_v128_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 1008).diff(1008) / _sma(_ratio(ebit, ebitda).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_slope_diff_norm_1260d_v129_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 1260).diff(1260) / _sma(ebitdamargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_slope_diff_norm_1260d_v130_signal(ebitda):
    res = (_slope_pct(ebitda, 1260).diff(1260) / _sma(ebitda.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_slope_diff_norm_1260d_v131_signal(ebit):
    res = (_slope_pct(ebit, 1260).diff(1260) / _sma(ebit.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_slope_diff_norm_1260d_v132_signal(ebit, ebitda):
    res = (_slope_pct(_ratio(ebit, ebitda), 1260).diff(1260) / _sma(_ratio(ebit, ebitda).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_mom_z_5d_v133_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_mom_z_5d_v134_signal(ebitda):
    res = _z(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_mom_z_5d_v135_signal(ebit):
    res = _z(_slope_pct(ebit, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_mom_z_5d_v136_signal(ebit, ebitda):
    res = _z(_slope_pct(_ratio(ebit, ebitda), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_mom_z_10d_v137_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_mom_z_10d_v138_signal(ebitda):
    res = _z(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_mom_z_10d_v139_signal(ebit):
    res = _z(_slope_pct(ebit, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_mom_z_10d_v140_signal(ebit, ebitda):
    res = _z(_slope_pct(_ratio(ebit, ebitda), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_mom_z_21d_v141_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_mom_z_21d_v142_signal(ebitda):
    res = _z(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_mom_z_21d_v143_signal(ebit):
    res = _z(_slope_pct(ebit, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_mom_z_21d_v144_signal(ebit, ebitda):
    res = _z(_slope_pct(_ratio(ebit, ebitda), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_mom_z_42d_v145_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_mom_z_42d_v146_signal(ebitda):
    res = _z(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebit_mom_z_42d_v147_signal(ebit):
    res = _z(_slope_pct(ebit, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_operating_leverage_mom_z_42d_v148_signal(ebit, ebitda):
    res = _z(_slope_pct(_ratio(ebit, ebitda), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitdamargin_mom_z_63d_v149_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_platform_lifecycle_ebitda_mom_z_63d_v150_signal(ebitda):
    res = _z(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 05...")
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
