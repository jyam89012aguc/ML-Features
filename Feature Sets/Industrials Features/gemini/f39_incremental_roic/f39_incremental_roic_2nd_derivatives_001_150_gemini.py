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

def f39_incremental_roic_roic_slope_pct_5d_v001_signal(roic):
    res = _slope_pct(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_5d_v002_signal(ebit):
    res = _slope_pct(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_5d_v003_signal(invcap):
    res = _slope_pct(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_5d_v004_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_10d_v005_signal(roic):
    res = _slope_pct(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_10d_v006_signal(ebit):
    res = _slope_pct(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_10d_v007_signal(invcap):
    res = _slope_pct(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_10d_v008_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_21d_v009_signal(roic):
    res = _slope_pct(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_21d_v010_signal(ebit):
    res = _slope_pct(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_21d_v011_signal(invcap):
    res = _slope_pct(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_21d_v012_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_42d_v013_signal(roic):
    res = _slope_pct(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_42d_v014_signal(ebit):
    res = _slope_pct(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_42d_v015_signal(invcap):
    res = _slope_pct(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_42d_v016_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_63d_v017_signal(roic):
    res = _slope_pct(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_63d_v018_signal(ebit):
    res = _slope_pct(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_63d_v019_signal(invcap):
    res = _slope_pct(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_63d_v020_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_126d_v021_signal(roic):
    res = _slope_pct(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_126d_v022_signal(ebit):
    res = _slope_pct(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_126d_v023_signal(invcap):
    res = _slope_pct(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_126d_v024_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_252d_v025_signal(roic):
    res = _slope_pct(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_252d_v026_signal(ebit):
    res = _slope_pct(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_252d_v027_signal(invcap):
    res = _slope_pct(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_252d_v028_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_504d_v029_signal(roic):
    res = _slope_pct(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_504d_v030_signal(ebit):
    res = _slope_pct(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_504d_v031_signal(invcap):
    res = _slope_pct(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_504d_v032_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_756d_v033_signal(roic):
    res = _slope_pct(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_756d_v034_signal(ebit):
    res = _slope_pct(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_756d_v035_signal(invcap):
    res = _slope_pct(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_756d_v036_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_1008d_v037_signal(roic):
    res = _slope_pct(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_1008d_v038_signal(ebit):
    res = _slope_pct(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_1008d_v039_signal(invcap):
    res = _slope_pct(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_1008d_v040_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_pct_1260d_v041_signal(roic):
    res = _slope_pct(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_pct_1260d_v042_signal(ebit):
    res = _slope_pct(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_pct_1260d_v043_signal(invcap):
    res = _slope_pct(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_pct_1260d_v044_signal(ebit, invcap):
    res = _slope_pct(_ratio(ebit, invcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_5d_v045_signal(roic):
    res = _jerk(roic, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_5d_v046_signal(ebit):
    res = _jerk(ebit, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_5d_v047_signal(invcap):
    res = _jerk(invcap, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_5d_v048_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_10d_v049_signal(roic):
    res = _jerk(roic, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_10d_v050_signal(ebit):
    res = _jerk(ebit, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_10d_v051_signal(invcap):
    res = _jerk(invcap, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_10d_v052_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_21d_v053_signal(roic):
    res = _jerk(roic, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_21d_v054_signal(ebit):
    res = _jerk(ebit, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_21d_v055_signal(invcap):
    res = _jerk(invcap, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_21d_v056_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_42d_v057_signal(roic):
    res = _jerk(roic, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_42d_v058_signal(ebit):
    res = _jerk(ebit, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_42d_v059_signal(invcap):
    res = _jerk(invcap, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_42d_v060_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_63d_v061_signal(roic):
    res = _jerk(roic, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_63d_v062_signal(ebit):
    res = _jerk(ebit, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_63d_v063_signal(invcap):
    res = _jerk(invcap, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_63d_v064_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_126d_v065_signal(roic):
    res = _jerk(roic, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_126d_v066_signal(ebit):
    res = _jerk(ebit, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_126d_v067_signal(invcap):
    res = _jerk(invcap, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_126d_v068_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_252d_v069_signal(roic):
    res = _jerk(roic, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_252d_v070_signal(ebit):
    res = _jerk(ebit, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_252d_v071_signal(invcap):
    res = _jerk(invcap, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_252d_v072_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_504d_v073_signal(roic):
    res = _jerk(roic, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_504d_v074_signal(ebit):
    res = _jerk(ebit, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_504d_v075_signal(invcap):
    res = _jerk(invcap, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_504d_v076_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_756d_v077_signal(roic):
    res = _jerk(roic, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_756d_v078_signal(ebit):
    res = _jerk(ebit, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_756d_v079_signal(invcap):
    res = _jerk(invcap, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_756d_v080_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_1008d_v081_signal(roic):
    res = _jerk(roic, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_1008d_v082_signal(ebit):
    res = _jerk(ebit, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_1008d_v083_signal(invcap):
    res = _jerk(invcap, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_1008d_v084_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_jerk_1260d_v085_signal(roic):
    res = _jerk(roic, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_jerk_1260d_v086_signal(ebit):
    res = _jerk(ebit, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_jerk_1260d_v087_signal(invcap):
    res = _jerk(invcap, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_jerk_1260d_v088_signal(ebit, invcap):
    res = _jerk(_ratio(ebit, invcap), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_5d_v089_signal(roic):
    res = (_slope_pct(roic, 5).diff(5) / _sma(roic.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_5d_v090_signal(ebit):
    res = (_slope_pct(ebit, 5).diff(5) / _sma(ebit.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_5d_v091_signal(invcap):
    res = (_slope_pct(invcap, 5).diff(5) / _sma(invcap.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_5d_v092_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 5).diff(5) / _sma(_ratio(ebit, invcap).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_10d_v093_signal(roic):
    res = (_slope_pct(roic, 10).diff(10) / _sma(roic.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_10d_v094_signal(ebit):
    res = (_slope_pct(ebit, 10).diff(10) / _sma(ebit.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_10d_v095_signal(invcap):
    res = (_slope_pct(invcap, 10).diff(10) / _sma(invcap.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_10d_v096_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 10).diff(10) / _sma(_ratio(ebit, invcap).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_21d_v097_signal(roic):
    res = (_slope_pct(roic, 21).diff(21) / _sma(roic.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_21d_v098_signal(ebit):
    res = (_slope_pct(ebit, 21).diff(21) / _sma(ebit.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_21d_v099_signal(invcap):
    res = (_slope_pct(invcap, 21).diff(21) / _sma(invcap.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_21d_v100_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 21).diff(21) / _sma(_ratio(ebit, invcap).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_42d_v101_signal(roic):
    res = (_slope_pct(roic, 42).diff(42) / _sma(roic.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_42d_v102_signal(ebit):
    res = (_slope_pct(ebit, 42).diff(42) / _sma(ebit.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_42d_v103_signal(invcap):
    res = (_slope_pct(invcap, 42).diff(42) / _sma(invcap.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_42d_v104_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 42).diff(42) / _sma(_ratio(ebit, invcap).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_63d_v105_signal(roic):
    res = (_slope_pct(roic, 63).diff(63) / _sma(roic.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_63d_v106_signal(ebit):
    res = (_slope_pct(ebit, 63).diff(63) / _sma(ebit.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_63d_v107_signal(invcap):
    res = (_slope_pct(invcap, 63).diff(63) / _sma(invcap.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_63d_v108_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 63).diff(63) / _sma(_ratio(ebit, invcap).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_126d_v109_signal(roic):
    res = (_slope_pct(roic, 126).diff(126) / _sma(roic.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_126d_v110_signal(ebit):
    res = (_slope_pct(ebit, 126).diff(126) / _sma(ebit.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_126d_v111_signal(invcap):
    res = (_slope_pct(invcap, 126).diff(126) / _sma(invcap.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_126d_v112_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 126).diff(126) / _sma(_ratio(ebit, invcap).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_252d_v113_signal(roic):
    res = (_slope_pct(roic, 252).diff(252) / _sma(roic.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_252d_v114_signal(ebit):
    res = (_slope_pct(ebit, 252).diff(252) / _sma(ebit.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_252d_v115_signal(invcap):
    res = (_slope_pct(invcap, 252).diff(252) / _sma(invcap.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_252d_v116_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 252).diff(252) / _sma(_ratio(ebit, invcap).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_504d_v117_signal(roic):
    res = (_slope_pct(roic, 504).diff(504) / _sma(roic.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_504d_v118_signal(ebit):
    res = (_slope_pct(ebit, 504).diff(504) / _sma(ebit.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_504d_v119_signal(invcap):
    res = (_slope_pct(invcap, 504).diff(504) / _sma(invcap.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_504d_v120_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 504).diff(504) / _sma(_ratio(ebit, invcap).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_756d_v121_signal(roic):
    res = (_slope_pct(roic, 756).diff(756) / _sma(roic.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_756d_v122_signal(ebit):
    res = (_slope_pct(ebit, 756).diff(756) / _sma(ebit.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_756d_v123_signal(invcap):
    res = (_slope_pct(invcap, 756).diff(756) / _sma(invcap.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_756d_v124_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 756).diff(756) / _sma(_ratio(ebit, invcap).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_1008d_v125_signal(roic):
    res = (_slope_pct(roic, 1008).diff(1008) / _sma(roic.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_1008d_v126_signal(ebit):
    res = (_slope_pct(ebit, 1008).diff(1008) / _sma(ebit.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_1008d_v127_signal(invcap):
    res = (_slope_pct(invcap, 1008).diff(1008) / _sma(invcap.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_1008d_v128_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 1008).diff(1008) / _sma(_ratio(ebit, invcap).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_slope_diff_norm_1260d_v129_signal(roic):
    res = (_slope_pct(roic, 1260).diff(1260) / _sma(roic.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_slope_diff_norm_1260d_v130_signal(ebit):
    res = (_slope_pct(ebit, 1260).diff(1260) / _sma(ebit.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_slope_diff_norm_1260d_v131_signal(invcap):
    res = (_slope_pct(invcap, 1260).diff(1260) / _sma(invcap.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_slope_diff_norm_1260d_v132_signal(ebit, invcap):
    res = (_slope_pct(_ratio(ebit, invcap), 1260).diff(1260) / _sma(_ratio(ebit, invcap).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_mom_z_5d_v133_signal(roic):
    res = _z(_slope_pct(roic, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_mom_z_5d_v134_signal(ebit):
    res = _z(_slope_pct(ebit, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_mom_z_5d_v135_signal(invcap):
    res = _z(_slope_pct(invcap, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_mom_z_5d_v136_signal(ebit, invcap):
    res = _z(_slope_pct(_ratio(ebit, invcap), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_mom_z_10d_v137_signal(roic):
    res = _z(_slope_pct(roic, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_mom_z_10d_v138_signal(ebit):
    res = _z(_slope_pct(ebit, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_mom_z_10d_v139_signal(invcap):
    res = _z(_slope_pct(invcap, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_mom_z_10d_v140_signal(ebit, invcap):
    res = _z(_slope_pct(_ratio(ebit, invcap), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_mom_z_21d_v141_signal(roic):
    res = _z(_slope_pct(roic, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_mom_z_21d_v142_signal(ebit):
    res = _z(_slope_pct(ebit, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_mom_z_21d_v143_signal(invcap):
    res = _z(_slope_pct(invcap, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_mom_z_21d_v144_signal(ebit, invcap):
    res = _z(_slope_pct(_ratio(ebit, invcap), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_mom_z_42d_v145_signal(roic):
    res = _z(_slope_pct(roic, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_mom_z_42d_v146_signal(ebit):
    res = _z(_slope_pct(ebit, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_invcap_mom_z_42d_v147_signal(invcap):
    res = _z(_slope_pct(invcap, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_to_invcap_mom_z_42d_v148_signal(ebit, invcap):
    res = _z(_slope_pct(_ratio(ebit, invcap), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_roic_mom_z_63d_v149_signal(roic):
    res = _z(_slope_pct(roic, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_incremental_roic_ebit_mom_z_63d_v150_signal(ebit):
    res = _z(_slope_pct(ebit, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 39...")
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
