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

def f07_supplier_pricing_grossmargin_slope_pct_5d_v001_signal(grossmargin):
    res = _slope_pct(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_5d_v002_signal(cor):
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_5d_v003_signal(gp):
    res = _slope_pct(gp, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_5d_v004_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_5d_v005_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_10d_v006_signal(grossmargin):
    res = _slope_pct(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_10d_v007_signal(cor):
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_10d_v008_signal(gp):
    res = _slope_pct(gp, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_10d_v009_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_10d_v010_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_21d_v011_signal(grossmargin):
    res = _slope_pct(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_21d_v012_signal(cor):
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_21d_v013_signal(gp):
    res = _slope_pct(gp, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_21d_v014_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_21d_v015_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_42d_v016_signal(grossmargin):
    res = _slope_pct(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_42d_v017_signal(cor):
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_42d_v018_signal(gp):
    res = _slope_pct(gp, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_42d_v019_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_42d_v020_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_63d_v021_signal(grossmargin):
    res = _slope_pct(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_63d_v022_signal(cor):
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_63d_v023_signal(gp):
    res = _slope_pct(gp, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_63d_v024_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_63d_v025_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_126d_v026_signal(grossmargin):
    res = _slope_pct(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_126d_v027_signal(cor):
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_126d_v028_signal(gp):
    res = _slope_pct(gp, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_126d_v029_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_126d_v030_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_252d_v031_signal(grossmargin):
    res = _slope_pct(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_252d_v032_signal(cor):
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_252d_v033_signal(gp):
    res = _slope_pct(gp, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_252d_v034_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_252d_v035_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_504d_v036_signal(grossmargin):
    res = _slope_pct(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_504d_v037_signal(cor):
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_504d_v038_signal(gp):
    res = _slope_pct(gp, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_504d_v039_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_504d_v040_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_756d_v041_signal(grossmargin):
    res = _slope_pct(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_756d_v042_signal(cor):
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_756d_v043_signal(gp):
    res = _slope_pct(gp, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_756d_v044_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_756d_v045_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_1008d_v046_signal(grossmargin):
    res = _slope_pct(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_1008d_v047_signal(cor):
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_1008d_v048_signal(gp):
    res = _slope_pct(gp, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_1008d_v049_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_1008d_v050_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_pct_1260d_v051_signal(grossmargin):
    res = _slope_pct(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_pct_1260d_v052_signal(cor):
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_pct_1260d_v053_signal(gp):
    res = _slope_pct(gp, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_pct_1260d_v054_signal(cor, gp):
    res = _slope_pct(_ratio(cor, gp + cor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_pct_1260d_v055_signal(gp, cor):
    res = _slope_pct(_ratio(gp, cor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_5d_v056_signal(grossmargin):
    res = _jerk(grossmargin, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_5d_v057_signal(cor):
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_5d_v058_signal(gp):
    res = _jerk(gp, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_5d_v059_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_5d_v060_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_10d_v061_signal(grossmargin):
    res = _jerk(grossmargin, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_10d_v062_signal(cor):
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_10d_v063_signal(gp):
    res = _jerk(gp, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_10d_v064_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_10d_v065_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_21d_v066_signal(grossmargin):
    res = _jerk(grossmargin, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_21d_v067_signal(cor):
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_21d_v068_signal(gp):
    res = _jerk(gp, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_21d_v069_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_21d_v070_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_42d_v071_signal(grossmargin):
    res = _jerk(grossmargin, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_42d_v072_signal(cor):
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_42d_v073_signal(gp):
    res = _jerk(gp, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_42d_v074_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_42d_v075_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_63d_v076_signal(grossmargin):
    res = _jerk(grossmargin, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_63d_v077_signal(cor):
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_63d_v078_signal(gp):
    res = _jerk(gp, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_63d_v079_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_63d_v080_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_126d_v081_signal(grossmargin):
    res = _jerk(grossmargin, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_126d_v082_signal(cor):
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_126d_v083_signal(gp):
    res = _jerk(gp, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_126d_v084_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_126d_v085_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_252d_v086_signal(grossmargin):
    res = _jerk(grossmargin, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_252d_v087_signal(cor):
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_252d_v088_signal(gp):
    res = _jerk(gp, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_252d_v089_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_252d_v090_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_504d_v091_signal(grossmargin):
    res = _jerk(grossmargin, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_504d_v092_signal(cor):
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_504d_v093_signal(gp):
    res = _jerk(gp, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_504d_v094_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_504d_v095_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_756d_v096_signal(grossmargin):
    res = _jerk(grossmargin, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_756d_v097_signal(cor):
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_756d_v098_signal(gp):
    res = _jerk(gp, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_756d_v099_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_756d_v100_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_1008d_v101_signal(grossmargin):
    res = _jerk(grossmargin, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_1008d_v102_signal(cor):
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_1008d_v103_signal(gp):
    res = _jerk(gp, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_1008d_v104_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_1008d_v105_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_jerk_1260d_v106_signal(grossmargin):
    res = _jerk(grossmargin, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_jerk_1260d_v107_signal(cor):
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_jerk_1260d_v108_signal(gp):
    res = _jerk(gp, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_jerk_1260d_v109_signal(cor, gp):
    res = _jerk(_ratio(cor, gp + cor), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_jerk_1260d_v110_signal(gp, cor):
    res = _jerk(_ratio(gp, cor), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_5d_v111_signal(grossmargin):
    res = (_slope_pct(grossmargin, 5).diff(5) / _sma(grossmargin.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_5d_v112_signal(cor):
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_5d_v113_signal(gp):
    res = (_slope_pct(gp, 5).diff(5) / _sma(gp.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_5d_v114_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 5).diff(5) / _sma(_ratio(cor, gp + cor).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_5d_v115_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 5).diff(5) / _sma(_ratio(gp, cor).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_10d_v116_signal(grossmargin):
    res = (_slope_pct(grossmargin, 10).diff(10) / _sma(grossmargin.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_10d_v117_signal(cor):
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_10d_v118_signal(gp):
    res = (_slope_pct(gp, 10).diff(10) / _sma(gp.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_10d_v119_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 10).diff(10) / _sma(_ratio(cor, gp + cor).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_10d_v120_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 10).diff(10) / _sma(_ratio(gp, cor).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_21d_v121_signal(grossmargin):
    res = (_slope_pct(grossmargin, 21).diff(21) / _sma(grossmargin.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_21d_v122_signal(cor):
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_21d_v123_signal(gp):
    res = (_slope_pct(gp, 21).diff(21) / _sma(gp.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_21d_v124_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 21).diff(21) / _sma(_ratio(cor, gp + cor).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_21d_v125_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 21).diff(21) / _sma(_ratio(gp, cor).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_42d_v126_signal(grossmargin):
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_42d_v127_signal(cor):
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_42d_v128_signal(gp):
    res = (_slope_pct(gp, 42).diff(42) / _sma(gp.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_42d_v129_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 42).diff(42) / _sma(_ratio(cor, gp + cor).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_42d_v130_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 42).diff(42) / _sma(_ratio(gp, cor).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_63d_v131_signal(grossmargin):
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_63d_v132_signal(cor):
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_63d_v133_signal(gp):
    res = (_slope_pct(gp, 63).diff(63) / _sma(gp.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_63d_v134_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 63).diff(63) / _sma(_ratio(cor, gp + cor).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_63d_v135_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 63).diff(63) / _sma(_ratio(gp, cor).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_126d_v136_signal(grossmargin):
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_126d_v137_signal(cor):
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_126d_v138_signal(gp):
    res = (_slope_pct(gp, 126).diff(126) / _sma(gp.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_126d_v139_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 126).diff(126) / _sma(_ratio(cor, gp + cor).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_126d_v140_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 126).diff(126) / _sma(_ratio(gp, cor).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_252d_v141_signal(grossmargin):
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_252d_v142_signal(cor):
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_252d_v143_signal(gp):
    res = (_slope_pct(gp, 252).diff(252) / _sma(gp.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_252d_v144_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 252).diff(252) / _sma(_ratio(cor, gp + cor).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_252d_v145_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 252).diff(252) / _sma(_ratio(gp, cor).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_grossmargin_slope_diff_norm_504d_v146_signal(grossmargin):
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_slope_diff_norm_504d_v147_signal(cor):
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_gp_slope_diff_norm_504d_v148_signal(gp):
    res = (_slope_pct(gp, 504).diff(504) / _sma(gp.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_cor_to_rev_slope_diff_norm_504d_v149_signal(cor, gp):
    res = (_slope_pct(_ratio(cor, gp + cor), 504).diff(504) / _sma(_ratio(cor, gp + cor).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_supplier_pricing_markup_slope_diff_norm_504d_v150_signal(gp, cor):
    res = (_slope_pct(_ratio(gp, cor), 504).diff(504) / _sma(_ratio(gp, cor).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "gp": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 07...")
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
