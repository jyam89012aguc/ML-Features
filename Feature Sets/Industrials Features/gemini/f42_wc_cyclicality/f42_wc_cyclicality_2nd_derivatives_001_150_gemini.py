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

def f42_wc_cyclicality_inventory_slope_pct_5d_v001_signal(inventory):
    res = _slope_pct(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_5d_v002_signal(receivables):
    res = _slope_pct(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_5d_v003_signal(payables):
    res = _slope_pct(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_5d_v004_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_5d_v005_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_10d_v006_signal(inventory):
    res = _slope_pct(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_10d_v007_signal(receivables):
    res = _slope_pct(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_10d_v008_signal(payables):
    res = _slope_pct(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_10d_v009_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_10d_v010_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_21d_v011_signal(inventory):
    res = _slope_pct(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_21d_v012_signal(receivables):
    res = _slope_pct(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_21d_v013_signal(payables):
    res = _slope_pct(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_21d_v014_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_21d_v015_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_42d_v016_signal(inventory):
    res = _slope_pct(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_42d_v017_signal(receivables):
    res = _slope_pct(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_42d_v018_signal(payables):
    res = _slope_pct(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_42d_v019_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_42d_v020_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_63d_v021_signal(inventory):
    res = _slope_pct(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_63d_v022_signal(receivables):
    res = _slope_pct(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_63d_v023_signal(payables):
    res = _slope_pct(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_63d_v024_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_63d_v025_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_126d_v026_signal(inventory):
    res = _slope_pct(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_126d_v027_signal(receivables):
    res = _slope_pct(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_126d_v028_signal(payables):
    res = _slope_pct(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_126d_v029_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_126d_v030_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_252d_v031_signal(inventory):
    res = _slope_pct(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_252d_v032_signal(receivables):
    res = _slope_pct(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_252d_v033_signal(payables):
    res = _slope_pct(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_252d_v034_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_252d_v035_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_504d_v036_signal(inventory):
    res = _slope_pct(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_504d_v037_signal(receivables):
    res = _slope_pct(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_504d_v038_signal(payables):
    res = _slope_pct(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_504d_v039_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_504d_v040_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_756d_v041_signal(inventory):
    res = _slope_pct(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_756d_v042_signal(receivables):
    res = _slope_pct(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_756d_v043_signal(payables):
    res = _slope_pct(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_756d_v044_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_756d_v045_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_1008d_v046_signal(inventory):
    res = _slope_pct(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_1008d_v047_signal(receivables):
    res = _slope_pct(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_1008d_v048_signal(payables):
    res = _slope_pct(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_1008d_v049_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_1008d_v050_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_pct_1260d_v051_signal(inventory):
    res = _slope_pct(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_pct_1260d_v052_signal(receivables):
    res = _slope_pct(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_pct_1260d_v053_signal(payables):
    res = _slope_pct(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_pct_1260d_v054_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_pct_1260d_v055_signal(inventory, receivables, payables, revenue):
    res = _slope_pct(_ratio(inventory + receivables - payables, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_5d_v056_signal(inventory):
    res = _jerk(inventory, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_5d_v057_signal(receivables):
    res = _jerk(receivables, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_5d_v058_signal(payables):
    res = _jerk(payables, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_5d_v059_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_5d_v060_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_10d_v061_signal(inventory):
    res = _jerk(inventory, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_10d_v062_signal(receivables):
    res = _jerk(receivables, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_10d_v063_signal(payables):
    res = _jerk(payables, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_10d_v064_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_10d_v065_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_21d_v066_signal(inventory):
    res = _jerk(inventory, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_21d_v067_signal(receivables):
    res = _jerk(receivables, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_21d_v068_signal(payables):
    res = _jerk(payables, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_21d_v069_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_21d_v070_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_42d_v071_signal(inventory):
    res = _jerk(inventory, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_42d_v072_signal(receivables):
    res = _jerk(receivables, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_42d_v073_signal(payables):
    res = _jerk(payables, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_42d_v074_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_42d_v075_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_63d_v076_signal(inventory):
    res = _jerk(inventory, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_63d_v077_signal(receivables):
    res = _jerk(receivables, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_63d_v078_signal(payables):
    res = _jerk(payables, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_63d_v079_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_63d_v080_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_126d_v081_signal(inventory):
    res = _jerk(inventory, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_126d_v082_signal(receivables):
    res = _jerk(receivables, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_126d_v083_signal(payables):
    res = _jerk(payables, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_126d_v084_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_126d_v085_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_252d_v086_signal(inventory):
    res = _jerk(inventory, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_252d_v087_signal(receivables):
    res = _jerk(receivables, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_252d_v088_signal(payables):
    res = _jerk(payables, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_252d_v089_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_252d_v090_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_504d_v091_signal(inventory):
    res = _jerk(inventory, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_504d_v092_signal(receivables):
    res = _jerk(receivables, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_504d_v093_signal(payables):
    res = _jerk(payables, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_504d_v094_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_504d_v095_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_756d_v096_signal(inventory):
    res = _jerk(inventory, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_756d_v097_signal(receivables):
    res = _jerk(receivables, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_756d_v098_signal(payables):
    res = _jerk(payables, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_756d_v099_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_756d_v100_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_1008d_v101_signal(inventory):
    res = _jerk(inventory, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_1008d_v102_signal(receivables):
    res = _jerk(receivables, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_1008d_v103_signal(payables):
    res = _jerk(payables, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_1008d_v104_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_1008d_v105_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_jerk_1260d_v106_signal(inventory):
    res = _jerk(inventory, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_jerk_1260d_v107_signal(receivables):
    res = _jerk(receivables, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_jerk_1260d_v108_signal(payables):
    res = _jerk(payables, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_jerk_1260d_v109_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_jerk_1260d_v110_signal(inventory, receivables, payables, revenue):
    res = _jerk(_ratio(inventory + receivables - payables, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_5d_v111_signal(inventory):
    res = (_slope_pct(inventory, 5).diff(5) / _sma(inventory.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_5d_v112_signal(receivables):
    res = (_slope_pct(receivables, 5).diff(5) / _sma(receivables.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_5d_v113_signal(payables):
    res = (_slope_pct(payables, 5).diff(5) / _sma(payables.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_5d_v114_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_5d_v115_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 5).diff(5) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_10d_v116_signal(inventory):
    res = (_slope_pct(inventory, 10).diff(10) / _sma(inventory.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_10d_v117_signal(receivables):
    res = (_slope_pct(receivables, 10).diff(10) / _sma(receivables.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_10d_v118_signal(payables):
    res = (_slope_pct(payables, 10).diff(10) / _sma(payables.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_10d_v119_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_10d_v120_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 10).diff(10) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_21d_v121_signal(inventory):
    res = (_slope_pct(inventory, 21).diff(21) / _sma(inventory.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_21d_v122_signal(receivables):
    res = (_slope_pct(receivables, 21).diff(21) / _sma(receivables.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_21d_v123_signal(payables):
    res = (_slope_pct(payables, 21).diff(21) / _sma(payables.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_21d_v124_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_21d_v125_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 21).diff(21) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_42d_v126_signal(inventory):
    res = (_slope_pct(inventory, 42).diff(42) / _sma(inventory.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_42d_v127_signal(receivables):
    res = (_slope_pct(receivables, 42).diff(42) / _sma(receivables.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_42d_v128_signal(payables):
    res = (_slope_pct(payables, 42).diff(42) / _sma(payables.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_42d_v129_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_42d_v130_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 42).diff(42) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_63d_v131_signal(inventory):
    res = (_slope_pct(inventory, 63).diff(63) / _sma(inventory.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_63d_v132_signal(receivables):
    res = (_slope_pct(receivables, 63).diff(63) / _sma(receivables.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_63d_v133_signal(payables):
    res = (_slope_pct(payables, 63).diff(63) / _sma(payables.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_63d_v134_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_63d_v135_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 63).diff(63) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_126d_v136_signal(inventory):
    res = (_slope_pct(inventory, 126).diff(126) / _sma(inventory.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_126d_v137_signal(receivables):
    res = (_slope_pct(receivables, 126).diff(126) / _sma(receivables.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_126d_v138_signal(payables):
    res = (_slope_pct(payables, 126).diff(126) / _sma(payables.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_126d_v139_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_126d_v140_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 126).diff(126) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_252d_v141_signal(inventory):
    res = (_slope_pct(inventory, 252).diff(252) / _sma(inventory.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_252d_v142_signal(receivables):
    res = (_slope_pct(receivables, 252).diff(252) / _sma(receivables.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_252d_v143_signal(payables):
    res = (_slope_pct(payables, 252).diff(252) / _sma(payables.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_252d_v144_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_252d_v145_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 252).diff(252) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_inventory_slope_diff_norm_504d_v146_signal(inventory):
    res = (_slope_pct(inventory, 504).diff(504) / _sma(inventory.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_receivables_slope_diff_norm_504d_v147_signal(receivables):
    res = (_slope_pct(receivables, 504).diff(504) / _sma(receivables.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_payables_slope_diff_norm_504d_v148_signal(payables):
    res = (_slope_pct(payables, 504).diff(504) / _sma(payables.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_revenue_slope_diff_norm_504d_v149_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f42_wc_cyclicality_wc_intensity_slope_diff_norm_504d_v150_signal(inventory, receivables, payables, revenue):
    res = (_slope_pct(_ratio(inventory + receivables - payables, revenue), 504).diff(504) / _sma(_ratio(inventory + receivables - payables, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 42...")
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
