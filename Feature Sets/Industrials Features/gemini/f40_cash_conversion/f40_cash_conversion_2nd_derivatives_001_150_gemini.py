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

def f40_cash_conversion_fcf_slope_pct_5d_v001_signal(fcf):
    res = _slope_pct(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_5d_v002_signal(netinc):
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_5d_v003_signal(ebitda):
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_5d_v004_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_10d_v005_signal(fcf):
    res = _slope_pct(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_10d_v006_signal(netinc):
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_10d_v007_signal(ebitda):
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_10d_v008_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_21d_v009_signal(fcf):
    res = _slope_pct(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_21d_v010_signal(netinc):
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_21d_v011_signal(ebitda):
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_21d_v012_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_42d_v013_signal(fcf):
    res = _slope_pct(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_42d_v014_signal(netinc):
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_42d_v015_signal(ebitda):
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_42d_v016_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_63d_v017_signal(fcf):
    res = _slope_pct(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_63d_v018_signal(netinc):
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_63d_v019_signal(ebitda):
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_63d_v020_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_126d_v021_signal(fcf):
    res = _slope_pct(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_126d_v022_signal(netinc):
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_126d_v023_signal(ebitda):
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_126d_v024_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_252d_v025_signal(fcf):
    res = _slope_pct(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_252d_v026_signal(netinc):
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_252d_v027_signal(ebitda):
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_252d_v028_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_504d_v029_signal(fcf):
    res = _slope_pct(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_504d_v030_signal(netinc):
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_504d_v031_signal(ebitda):
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_504d_v032_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_756d_v033_signal(fcf):
    res = _slope_pct(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_756d_v034_signal(netinc):
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_756d_v035_signal(ebitda):
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_756d_v036_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_1008d_v037_signal(fcf):
    res = _slope_pct(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_1008d_v038_signal(netinc):
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_1008d_v039_signal(ebitda):
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_1008d_v040_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_pct_1260d_v041_signal(fcf):
    res = _slope_pct(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_pct_1260d_v042_signal(netinc):
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_pct_1260d_v043_signal(ebitda):
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_pct_1260d_v044_signal(fcf, netinc):
    res = _slope_pct(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_5d_v045_signal(fcf):
    res = _jerk(fcf, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_5d_v046_signal(netinc):
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_5d_v047_signal(ebitda):
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_5d_v048_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_10d_v049_signal(fcf):
    res = _jerk(fcf, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_10d_v050_signal(netinc):
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_10d_v051_signal(ebitda):
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_10d_v052_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_21d_v053_signal(fcf):
    res = _jerk(fcf, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_21d_v054_signal(netinc):
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_21d_v055_signal(ebitda):
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_21d_v056_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_42d_v057_signal(fcf):
    res = _jerk(fcf, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_42d_v058_signal(netinc):
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_42d_v059_signal(ebitda):
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_42d_v060_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_63d_v061_signal(fcf):
    res = _jerk(fcf, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_63d_v062_signal(netinc):
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_63d_v063_signal(ebitda):
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_63d_v064_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_126d_v065_signal(fcf):
    res = _jerk(fcf, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_126d_v066_signal(netinc):
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_126d_v067_signal(ebitda):
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_126d_v068_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_252d_v069_signal(fcf):
    res = _jerk(fcf, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_252d_v070_signal(netinc):
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_252d_v071_signal(ebitda):
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_252d_v072_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_504d_v073_signal(fcf):
    res = _jerk(fcf, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_504d_v074_signal(netinc):
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_504d_v075_signal(ebitda):
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_504d_v076_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_756d_v077_signal(fcf):
    res = _jerk(fcf, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_756d_v078_signal(netinc):
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_756d_v079_signal(ebitda):
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_756d_v080_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_1008d_v081_signal(fcf):
    res = _jerk(fcf, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_1008d_v082_signal(netinc):
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_1008d_v083_signal(ebitda):
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_1008d_v084_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_jerk_1260d_v085_signal(fcf):
    res = _jerk(fcf, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_jerk_1260d_v086_signal(netinc):
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_jerk_1260d_v087_signal(ebitda):
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_jerk_1260d_v088_signal(fcf, netinc):
    res = _jerk(_ratio(fcf, netinc), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_5d_v089_signal(fcf):
    res = (_slope_pct(fcf, 5).diff(5) / _sma(fcf.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_5d_v090_signal(netinc):
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_5d_v091_signal(ebitda):
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_5d_v092_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 5).diff(5) / _sma(_ratio(fcf, netinc).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_10d_v093_signal(fcf):
    res = (_slope_pct(fcf, 10).diff(10) / _sma(fcf.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_10d_v094_signal(netinc):
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_10d_v095_signal(ebitda):
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_10d_v096_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 10).diff(10) / _sma(_ratio(fcf, netinc).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_21d_v097_signal(fcf):
    res = (_slope_pct(fcf, 21).diff(21) / _sma(fcf.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_21d_v098_signal(netinc):
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_21d_v099_signal(ebitda):
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_21d_v100_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 21).diff(21) / _sma(_ratio(fcf, netinc).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_42d_v101_signal(fcf):
    res = (_slope_pct(fcf, 42).diff(42) / _sma(fcf.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_42d_v102_signal(netinc):
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_42d_v103_signal(ebitda):
    res = (_slope_pct(ebitda, 42).diff(42) / _sma(ebitda.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_42d_v104_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 42).diff(42) / _sma(_ratio(fcf, netinc).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_63d_v105_signal(fcf):
    res = (_slope_pct(fcf, 63).diff(63) / _sma(fcf.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_63d_v106_signal(netinc):
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_63d_v107_signal(ebitda):
    res = (_slope_pct(ebitda, 63).diff(63) / _sma(ebitda.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_63d_v108_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 63).diff(63) / _sma(_ratio(fcf, netinc).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_126d_v109_signal(fcf):
    res = (_slope_pct(fcf, 126).diff(126) / _sma(fcf.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_126d_v110_signal(netinc):
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_126d_v111_signal(ebitda):
    res = (_slope_pct(ebitda, 126).diff(126) / _sma(ebitda.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_126d_v112_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 126).diff(126) / _sma(_ratio(fcf, netinc).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_252d_v113_signal(fcf):
    res = (_slope_pct(fcf, 252).diff(252) / _sma(fcf.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_252d_v114_signal(netinc):
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_252d_v115_signal(ebitda):
    res = (_slope_pct(ebitda, 252).diff(252) / _sma(ebitda.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_252d_v116_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 252).diff(252) / _sma(_ratio(fcf, netinc).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_504d_v117_signal(fcf):
    res = (_slope_pct(fcf, 504).diff(504) / _sma(fcf.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_504d_v118_signal(netinc):
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_504d_v119_signal(ebitda):
    res = (_slope_pct(ebitda, 504).diff(504) / _sma(ebitda.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_504d_v120_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 504).diff(504) / _sma(_ratio(fcf, netinc).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_756d_v121_signal(fcf):
    res = (_slope_pct(fcf, 756).diff(756) / _sma(fcf.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_756d_v122_signal(netinc):
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_756d_v123_signal(ebitda):
    res = (_slope_pct(ebitda, 756).diff(756) / _sma(ebitda.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_756d_v124_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 756).diff(756) / _sma(_ratio(fcf, netinc).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_1008d_v125_signal(fcf):
    res = (_slope_pct(fcf, 1008).diff(1008) / _sma(fcf.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_1008d_v126_signal(netinc):
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_1008d_v127_signal(ebitda):
    res = (_slope_pct(ebitda, 1008).diff(1008) / _sma(ebitda.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_1008d_v128_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 1008).diff(1008) / _sma(_ratio(fcf, netinc).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_slope_diff_norm_1260d_v129_signal(fcf):
    res = (_slope_pct(fcf, 1260).diff(1260) / _sma(fcf.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_slope_diff_norm_1260d_v130_signal(netinc):
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_slope_diff_norm_1260d_v131_signal(ebitda):
    res = (_slope_pct(ebitda, 1260).diff(1260) / _sma(ebitda.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_slope_diff_norm_1260d_v132_signal(fcf, netinc):
    res = (_slope_pct(_ratio(fcf, netinc), 1260).diff(1260) / _sma(_ratio(fcf, netinc).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_mom_z_5d_v133_signal(fcf):
    res = _z(_slope_pct(fcf, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_mom_z_5d_v134_signal(netinc):
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_mom_z_5d_v135_signal(ebitda):
    res = _z(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_mom_z_5d_v136_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_mom_z_10d_v137_signal(fcf):
    res = _z(_slope_pct(fcf, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_mom_z_10d_v138_signal(netinc):
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_mom_z_10d_v139_signal(ebitda):
    res = _z(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_mom_z_10d_v140_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_mom_z_21d_v141_signal(fcf):
    res = _z(_slope_pct(fcf, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_mom_z_21d_v142_signal(netinc):
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_mom_z_21d_v143_signal(ebitda):
    res = _z(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_mom_z_21d_v144_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_mom_z_42d_v145_signal(fcf):
    res = _z(_slope_pct(fcf, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_mom_z_42d_v146_signal(netinc):
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_ebitda_mom_z_42d_v147_signal(ebitda):
    res = _z(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_cash_quality_mom_z_42d_v148_signal(fcf, netinc):
    res = _z(_slope_pct(_ratio(fcf, netinc), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_fcf_mom_z_63d_v149_signal(fcf):
    res = _z(_slope_pct(fcf, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_cash_conversion_netinc_mom_z_63d_v150_signal(netinc):
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 40...")
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
