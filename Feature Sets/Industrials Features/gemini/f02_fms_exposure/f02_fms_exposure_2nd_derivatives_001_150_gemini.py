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

def f02_fms_exposure_revenue_slope_pct_5d_v001_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_5d_v002_signal(netinc):
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_5d_v003_signal(ebitda):
    res = _slope_pct(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_5d_v004_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_5d_v005_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_10d_v006_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_10d_v007_signal(netinc):
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_10d_v008_signal(ebitda):
    res = _slope_pct(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_10d_v009_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_10d_v010_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_21d_v011_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_21d_v012_signal(netinc):
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_21d_v013_signal(ebitda):
    res = _slope_pct(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_21d_v014_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_21d_v015_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_42d_v016_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_42d_v017_signal(netinc):
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_42d_v018_signal(ebitda):
    res = _slope_pct(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_42d_v019_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_42d_v020_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_63d_v021_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_63d_v022_signal(netinc):
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_63d_v023_signal(ebitda):
    res = _slope_pct(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_63d_v024_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_63d_v025_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_126d_v026_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_126d_v027_signal(netinc):
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_126d_v028_signal(ebitda):
    res = _slope_pct(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_126d_v029_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_126d_v030_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_252d_v031_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_252d_v032_signal(netinc):
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_252d_v033_signal(ebitda):
    res = _slope_pct(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_252d_v034_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_252d_v035_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_504d_v036_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_504d_v037_signal(netinc):
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_504d_v038_signal(ebitda):
    res = _slope_pct(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_504d_v039_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_504d_v040_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_756d_v041_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_756d_v042_signal(netinc):
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_756d_v043_signal(ebitda):
    res = _slope_pct(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_756d_v044_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_756d_v045_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_1008d_v046_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_1008d_v047_signal(netinc):
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_1008d_v048_signal(ebitda):
    res = _slope_pct(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_1008d_v049_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_1008d_v050_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_pct_1260d_v051_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_pct_1260d_v052_signal(netinc):
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_pct_1260d_v053_signal(ebitda):
    res = _slope_pct(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_pct_1260d_v054_signal(netinc, revenue):
    res = _slope_pct(_ratio(netinc, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_pct_1260d_v055_signal(ebitda, revenue):
    res = _slope_pct(_ratio(ebitda, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_5d_v056_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_5d_v057_signal(netinc):
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_5d_v058_signal(ebitda):
    res = _jerk(ebitda, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_5d_v059_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_5d_v060_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_10d_v061_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_10d_v062_signal(netinc):
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_10d_v063_signal(ebitda):
    res = _jerk(ebitda, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_10d_v064_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_10d_v065_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_21d_v066_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_21d_v067_signal(netinc):
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_21d_v068_signal(ebitda):
    res = _jerk(ebitda, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_21d_v069_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_21d_v070_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_42d_v071_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_42d_v072_signal(netinc):
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_42d_v073_signal(ebitda):
    res = _jerk(ebitda, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_42d_v074_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_42d_v075_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_63d_v076_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_63d_v077_signal(netinc):
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_63d_v078_signal(ebitda):
    res = _jerk(ebitda, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_63d_v079_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_63d_v080_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_126d_v081_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_126d_v082_signal(netinc):
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_126d_v083_signal(ebitda):
    res = _jerk(ebitda, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_126d_v084_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_126d_v085_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_252d_v086_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_252d_v087_signal(netinc):
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_252d_v088_signal(ebitda):
    res = _jerk(ebitda, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_252d_v089_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_252d_v090_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_504d_v091_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_504d_v092_signal(netinc):
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_504d_v093_signal(ebitda):
    res = _jerk(ebitda, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_504d_v094_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_504d_v095_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_756d_v096_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_756d_v097_signal(netinc):
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_756d_v098_signal(ebitda):
    res = _jerk(ebitda, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_756d_v099_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_756d_v100_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_1008d_v101_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_1008d_v102_signal(netinc):
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_1008d_v103_signal(ebitda):
    res = _jerk(ebitda, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_1008d_v104_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_1008d_v105_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_jerk_1260d_v106_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_jerk_1260d_v107_signal(netinc):
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_jerk_1260d_v108_signal(ebitda):
    res = _jerk(ebitda, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_jerk_1260d_v109_signal(netinc, revenue):
    res = _jerk(_ratio(netinc, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_jerk_1260d_v110_signal(ebitda, revenue):
    res = _jerk(_ratio(ebitda, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_diff_norm_5d_v111_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_diff_norm_5d_v112_signal(netinc):
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_diff_norm_5d_v113_signal(ebitda):
    res = (_slope_pct(ebitda, 5).diff(5) / _sma(ebitda.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_diff_norm_5d_v114_signal(netinc, revenue):
    res = (_slope_pct(_ratio(netinc, revenue), 5).diff(5) / _sma(_ratio(netinc, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_diff_norm_5d_v115_signal(ebitda, revenue):
    res = (_slope_pct(_ratio(ebitda, revenue), 5).diff(5) / _sma(_ratio(ebitda, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_diff_norm_10d_v116_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_diff_norm_10d_v117_signal(netinc):
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_diff_norm_10d_v118_signal(ebitda):
    res = (_slope_pct(ebitda, 10).diff(10) / _sma(ebitda.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_diff_norm_10d_v119_signal(netinc, revenue):
    res = (_slope_pct(_ratio(netinc, revenue), 10).diff(10) / _sma(_ratio(netinc, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_diff_norm_10d_v120_signal(ebitda, revenue):
    res = (_slope_pct(_ratio(ebitda, revenue), 10).diff(10) / _sma(_ratio(ebitda, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_diff_norm_21d_v121_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_diff_norm_21d_v122_signal(netinc):
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_diff_norm_21d_v123_signal(ebitda):
    res = (_slope_pct(ebitda, 21).diff(21) / _sma(ebitda.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_diff_norm_21d_v124_signal(netinc, revenue):
    res = (_slope_pct(_ratio(netinc, revenue), 21).diff(21) / _sma(_ratio(netinc, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_diff_norm_21d_v125_signal(ebitda, revenue):
    res = (_slope_pct(_ratio(ebitda, revenue), 21).diff(21) / _sma(_ratio(ebitda, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_diff_norm_42d_v126_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_diff_norm_42d_v127_signal(netinc):
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_diff_norm_42d_v128_signal(ebitda):
    res = (_slope_pct(ebitda, 42).diff(42) / _sma(ebitda.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_diff_norm_42d_v129_signal(netinc, revenue):
    res = (_slope_pct(_ratio(netinc, revenue), 42).diff(42) / _sma(_ratio(netinc, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_diff_norm_42d_v130_signal(ebitda, revenue):
    res = (_slope_pct(_ratio(ebitda, revenue), 42).diff(42) / _sma(_ratio(ebitda, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_diff_norm_63d_v131_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_diff_norm_63d_v132_signal(netinc):
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_diff_norm_63d_v133_signal(ebitda):
    res = (_slope_pct(ebitda, 63).diff(63) / _sma(ebitda.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_diff_norm_63d_v134_signal(netinc, revenue):
    res = (_slope_pct(_ratio(netinc, revenue), 63).diff(63) / _sma(_ratio(netinc, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_diff_norm_63d_v135_signal(ebitda, revenue):
    res = (_slope_pct(_ratio(ebitda, revenue), 63).diff(63) / _sma(_ratio(ebitda, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_diff_norm_126d_v136_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_diff_norm_126d_v137_signal(netinc):
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_diff_norm_126d_v138_signal(ebitda):
    res = (_slope_pct(ebitda, 126).diff(126) / _sma(ebitda.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_diff_norm_126d_v139_signal(netinc, revenue):
    res = (_slope_pct(_ratio(netinc, revenue), 126).diff(126) / _sma(_ratio(netinc, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_diff_norm_126d_v140_signal(ebitda, revenue):
    res = (_slope_pct(_ratio(ebitda, revenue), 126).diff(126) / _sma(_ratio(ebitda, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_diff_norm_252d_v141_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_diff_norm_252d_v142_signal(netinc):
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_diff_norm_252d_v143_signal(ebitda):
    res = (_slope_pct(ebitda, 252).diff(252) / _sma(ebitda.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_diff_norm_252d_v144_signal(netinc, revenue):
    res = (_slope_pct(_ratio(netinc, revenue), 252).diff(252) / _sma(_ratio(netinc, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_diff_norm_252d_v145_signal(ebitda, revenue):
    res = (_slope_pct(_ratio(ebitda, revenue), 252).diff(252) / _sma(_ratio(ebitda, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_revenue_slope_diff_norm_504d_v146_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_netinc_slope_diff_norm_504d_v147_signal(netinc):
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_slope_diff_norm_504d_v148_signal(ebitda):
    res = (_slope_pct(ebitda, 504).diff(504) / _sma(ebitda.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_profit_margin_slope_diff_norm_504d_v149_signal(netinc, revenue):
    res = (_slope_pct(_ratio(netinc, revenue), 504).diff(504) / _sma(_ratio(netinc, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_fms_exposure_ebitda_margin_slope_diff_norm_504d_v150_signal(ebitda, revenue):
    res = (_slope_pct(_ratio(ebitda, revenue), 504).diff(504) / _sma(_ratio(ebitda, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 02...")
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
