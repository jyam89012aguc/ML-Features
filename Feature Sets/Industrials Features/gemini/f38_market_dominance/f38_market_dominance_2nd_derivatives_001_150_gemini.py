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

def f38_market_dominance_grossmargin_slope_pct_5d_v001_signal(grossmargin):
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_5d_v002_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_5d_v003_signal(roic):
    res = _slope_pct(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_5d_v004_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_10d_v005_signal(grossmargin):
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_10d_v006_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_10d_v007_signal(roic):
    res = _slope_pct(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_10d_v008_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_21d_v009_signal(grossmargin):
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_21d_v010_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_21d_v011_signal(roic):
    res = _slope_pct(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_21d_v012_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_42d_v013_signal(grossmargin):
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_42d_v014_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_42d_v015_signal(roic):
    res = _slope_pct(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_42d_v016_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_63d_v017_signal(grossmargin):
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_63d_v018_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_63d_v019_signal(roic):
    res = _slope_pct(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_63d_v020_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_126d_v021_signal(grossmargin):
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_126d_v022_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_126d_v023_signal(roic):
    res = _slope_pct(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_126d_v024_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_252d_v025_signal(grossmargin):
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_252d_v026_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_252d_v027_signal(roic):
    res = _slope_pct(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_252d_v028_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_504d_v029_signal(grossmargin):
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_504d_v030_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_504d_v031_signal(roic):
    res = _slope_pct(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_504d_v032_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_756d_v033_signal(grossmargin):
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_756d_v034_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_756d_v035_signal(roic):
    res = _slope_pct(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_756d_v036_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_1008d_v037_signal(grossmargin):
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_1008d_v038_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_1008d_v039_signal(roic):
    res = _slope_pct(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_1008d_v040_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_pct_1260d_v041_signal(grossmargin):
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_pct_1260d_v042_signal(ebitdamargin):
    res = _slope_pct(ebitdamargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_pct_1260d_v043_signal(roic):
    res = _slope_pct(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_pct_1260d_v044_signal(grossmargin, roic):
    res = _slope_pct(grossmargin * roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_5d_v045_signal(grossmargin):
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_5d_v046_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_5d_v047_signal(roic):
    res = _jerk(roic, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_5d_v048_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_10d_v049_signal(grossmargin):
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_10d_v050_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_10d_v051_signal(roic):
    res = _jerk(roic, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_10d_v052_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_21d_v053_signal(grossmargin):
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_21d_v054_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_21d_v055_signal(roic):
    res = _jerk(roic, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_21d_v056_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_42d_v057_signal(grossmargin):
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_42d_v058_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_42d_v059_signal(roic):
    res = _jerk(roic, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_42d_v060_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_63d_v061_signal(grossmargin):
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_63d_v062_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_63d_v063_signal(roic):
    res = _jerk(roic, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_63d_v064_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_126d_v065_signal(grossmargin):
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_126d_v066_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_126d_v067_signal(roic):
    res = _jerk(roic, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_126d_v068_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_252d_v069_signal(grossmargin):
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_252d_v070_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_252d_v071_signal(roic):
    res = _jerk(roic, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_252d_v072_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_504d_v073_signal(grossmargin):
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_504d_v074_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_504d_v075_signal(roic):
    res = _jerk(roic, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_504d_v076_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_756d_v077_signal(grossmargin):
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_756d_v078_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_756d_v079_signal(roic):
    res = _jerk(roic, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_756d_v080_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_1008d_v081_signal(grossmargin):
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_1008d_v082_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_1008d_v083_signal(roic):
    res = _jerk(roic, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_1008d_v084_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_jerk_1260d_v085_signal(grossmargin):
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_jerk_1260d_v086_signal(ebitdamargin):
    res = _jerk(ebitdamargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_jerk_1260d_v087_signal(roic):
    res = _jerk(roic, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_jerk_1260d_v088_signal(grossmargin, roic):
    res = _jerk(grossmargin * roic, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_5d_v089_signal(grossmargin):
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_5d_v090_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 5).diff(5) / _sma(ebitdamargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_5d_v091_signal(roic):
    res = (_slope_pct(roic, 5).diff(5) / _sma(roic.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_5d_v092_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 5).diff(5) / _sma(grossmargin * roic.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_10d_v093_signal(grossmargin):
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_10d_v094_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 10).diff(10) / _sma(ebitdamargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_10d_v095_signal(roic):
    res = (_slope_pct(roic, 10).diff(10) / _sma(roic.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_10d_v096_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 10).diff(10) / _sma(grossmargin * roic.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_21d_v097_signal(grossmargin):
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_21d_v098_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 21).diff(21) / _sma(ebitdamargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_21d_v099_signal(roic):
    res = (_slope_pct(roic, 21).diff(21) / _sma(roic.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_21d_v100_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 21).diff(21) / _sma(grossmargin * roic.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_42d_v101_signal(grossmargin):
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_42d_v102_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 42).diff(42) / _sma(ebitdamargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_42d_v103_signal(roic):
    res = (_slope_pct(roic, 42).diff(42) / _sma(roic.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_42d_v104_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 42).diff(42) / _sma(grossmargin * roic.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_63d_v105_signal(grossmargin):
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_63d_v106_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 63).diff(63) / _sma(ebitdamargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_63d_v107_signal(roic):
    res = (_slope_pct(roic, 63).diff(63) / _sma(roic.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_63d_v108_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 63).diff(63) / _sma(grossmargin * roic.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_126d_v109_signal(grossmargin):
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_126d_v110_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 126).diff(126) / _sma(ebitdamargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_126d_v111_signal(roic):
    res = (_slope_pct(roic, 126).diff(126) / _sma(roic.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_126d_v112_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 126).diff(126) / _sma(grossmargin * roic.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_252d_v113_signal(grossmargin):
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_252d_v114_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 252).diff(252) / _sma(ebitdamargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_252d_v115_signal(roic):
    res = (_slope_pct(roic, 252).diff(252) / _sma(roic.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_252d_v116_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 252).diff(252) / _sma(grossmargin * roic.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_504d_v117_signal(grossmargin):
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_504d_v118_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 504).diff(504) / _sma(ebitdamargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_504d_v119_signal(roic):
    res = (_slope_pct(roic, 504).diff(504) / _sma(roic.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_504d_v120_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 504).diff(504) / _sma(grossmargin * roic.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_756d_v121_signal(grossmargin):
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_756d_v122_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 756).diff(756) / _sma(ebitdamargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_756d_v123_signal(roic):
    res = (_slope_pct(roic, 756).diff(756) / _sma(roic.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_756d_v124_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 756).diff(756) / _sma(grossmargin * roic.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_1008d_v125_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_1008d_v126_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 1008).diff(1008) / _sma(ebitdamargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_1008d_v127_signal(roic):
    res = (_slope_pct(roic, 1008).diff(1008) / _sma(roic.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_1008d_v128_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 1008).diff(1008) / _sma(grossmargin * roic.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_slope_diff_norm_1260d_v129_signal(grossmargin):
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_slope_diff_norm_1260d_v130_signal(ebitdamargin):
    res = (_slope_pct(ebitdamargin, 1260).diff(1260) / _sma(ebitdamargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_slope_diff_norm_1260d_v131_signal(roic):
    res = (_slope_pct(roic, 1260).diff(1260) / _sma(roic.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_slope_diff_norm_1260d_v132_signal(grossmargin, roic):
    res = (_slope_pct(grossmargin * roic, 1260).diff(1260) / _sma(grossmargin * roic.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_mom_z_5d_v133_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_mom_z_5d_v134_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_mom_z_5d_v135_signal(roic):
    res = _z(_slope_pct(roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_mom_z_5d_v136_signal(grossmargin, roic):
    res = _z(_slope_pct(grossmargin * roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_mom_z_10d_v137_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_mom_z_10d_v138_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_mom_z_10d_v139_signal(roic):
    res = _z(_slope_pct(roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_mom_z_10d_v140_signal(grossmargin, roic):
    res = _z(_slope_pct(grossmargin * roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_mom_z_21d_v141_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_mom_z_21d_v142_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_mom_z_21d_v143_signal(roic):
    res = _z(_slope_pct(roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_mom_z_21d_v144_signal(grossmargin, roic):
    res = _z(_slope_pct(grossmargin * roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_mom_z_42d_v145_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_mom_z_42d_v146_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_roic_mom_z_42d_v147_signal(roic):
    res = _z(_slope_pct(roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_dominance_composite_mom_z_42d_v148_signal(grossmargin, roic):
    res = _z(_slope_pct(grossmargin * roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_grossmargin_mom_z_63d_v149_signal(grossmargin):
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f38_market_dominance_ebitdamargin_mom_z_63d_v150_signal(ebitdamargin):
    res = _z(_slope_pct(ebitdamargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 38...")
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
