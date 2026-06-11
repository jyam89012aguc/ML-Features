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

def f12_inventory_velocity_cor_slope_pct_5d_v001_signal(cor):
    res = _slope_pct(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_5d_v002_signal(inventory):
    res = _slope_pct(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_5d_v003_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_5d_v004_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_5d_v005_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_10d_v006_signal(cor):
    res = _slope_pct(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_10d_v007_signal(inventory):
    res = _slope_pct(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_10d_v008_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_10d_v009_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_10d_v010_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_21d_v011_signal(cor):
    res = _slope_pct(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_21d_v012_signal(inventory):
    res = _slope_pct(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_21d_v013_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_21d_v014_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_21d_v015_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_42d_v016_signal(cor):
    res = _slope_pct(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_42d_v017_signal(inventory):
    res = _slope_pct(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_42d_v018_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_42d_v019_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_42d_v020_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_63d_v021_signal(cor):
    res = _slope_pct(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_63d_v022_signal(inventory):
    res = _slope_pct(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_63d_v023_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_63d_v024_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_63d_v025_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_126d_v026_signal(cor):
    res = _slope_pct(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_126d_v027_signal(inventory):
    res = _slope_pct(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_126d_v028_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_126d_v029_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_126d_v030_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_252d_v031_signal(cor):
    res = _slope_pct(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_252d_v032_signal(inventory):
    res = _slope_pct(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_252d_v033_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_252d_v034_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_252d_v035_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_504d_v036_signal(cor):
    res = _slope_pct(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_504d_v037_signal(inventory):
    res = _slope_pct(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_504d_v038_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_504d_v039_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_504d_v040_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_756d_v041_signal(cor):
    res = _slope_pct(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_756d_v042_signal(inventory):
    res = _slope_pct(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_756d_v043_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_756d_v044_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_756d_v045_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_1008d_v046_signal(cor):
    res = _slope_pct(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_1008d_v047_signal(inventory):
    res = _slope_pct(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_1008d_v048_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_1008d_v049_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_1008d_v050_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_pct_1260d_v051_signal(cor):
    res = _slope_pct(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_pct_1260d_v052_signal(inventory):
    res = _slope_pct(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_pct_1260d_v053_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_pct_1260d_v054_signal(cor, inventory):
    res = _slope_pct(_ratio(cor, inventory), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_pct_1260d_v055_signal(inventory, cor):
    res = _slope_pct(_ratio(inventory, cor) * 365, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_5d_v056_signal(cor):
    res = _jerk(cor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_5d_v057_signal(inventory):
    res = _jerk(inventory, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_5d_v058_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_5d_v059_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_5d_v060_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_10d_v061_signal(cor):
    res = _jerk(cor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_10d_v062_signal(inventory):
    res = _jerk(inventory, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_10d_v063_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_10d_v064_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_10d_v065_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_21d_v066_signal(cor):
    res = _jerk(cor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_21d_v067_signal(inventory):
    res = _jerk(inventory, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_21d_v068_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_21d_v069_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_21d_v070_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_42d_v071_signal(cor):
    res = _jerk(cor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_42d_v072_signal(inventory):
    res = _jerk(inventory, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_42d_v073_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_42d_v074_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_42d_v075_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_63d_v076_signal(cor):
    res = _jerk(cor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_63d_v077_signal(inventory):
    res = _jerk(inventory, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_63d_v078_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_63d_v079_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_63d_v080_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_126d_v081_signal(cor):
    res = _jerk(cor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_126d_v082_signal(inventory):
    res = _jerk(inventory, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_126d_v083_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_126d_v084_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_126d_v085_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_252d_v086_signal(cor):
    res = _jerk(cor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_252d_v087_signal(inventory):
    res = _jerk(inventory, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_252d_v088_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_252d_v089_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_252d_v090_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_504d_v091_signal(cor):
    res = _jerk(cor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_504d_v092_signal(inventory):
    res = _jerk(inventory, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_504d_v093_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_504d_v094_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_504d_v095_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_756d_v096_signal(cor):
    res = _jerk(cor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_756d_v097_signal(inventory):
    res = _jerk(inventory, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_756d_v098_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_756d_v099_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_756d_v100_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_1008d_v101_signal(cor):
    res = _jerk(cor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_1008d_v102_signal(inventory):
    res = _jerk(inventory, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_1008d_v103_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_1008d_v104_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_1008d_v105_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_jerk_1260d_v106_signal(cor):
    res = _jerk(cor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_jerk_1260d_v107_signal(inventory):
    res = _jerk(inventory, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_jerk_1260d_v108_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_jerk_1260d_v109_signal(cor, inventory):
    res = _jerk(_ratio(cor, inventory), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_jerk_1260d_v110_signal(inventory, cor):
    res = _jerk(_ratio(inventory, cor) * 365, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_diff_norm_5d_v111_signal(cor):
    res = (_slope_pct(cor, 5).diff(5) / _sma(cor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_diff_norm_5d_v112_signal(inventory):
    res = (_slope_pct(inventory, 5).diff(5) / _sma(inventory.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_diff_norm_5d_v113_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_diff_norm_5d_v114_signal(cor, inventory):
    res = (_slope_pct(_ratio(cor, inventory), 5).diff(5) / _sma(_ratio(cor, inventory).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_diff_norm_5d_v115_signal(inventory, cor):
    res = (_slope_pct(_ratio(inventory, cor) * 365, 5).diff(5) / _sma(_ratio(inventory, cor) * 365.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_diff_norm_10d_v116_signal(cor):
    res = (_slope_pct(cor, 10).diff(10) / _sma(cor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_diff_norm_10d_v117_signal(inventory):
    res = (_slope_pct(inventory, 10).diff(10) / _sma(inventory.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_diff_norm_10d_v118_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_diff_norm_10d_v119_signal(cor, inventory):
    res = (_slope_pct(_ratio(cor, inventory), 10).diff(10) / _sma(_ratio(cor, inventory).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_diff_norm_10d_v120_signal(inventory, cor):
    res = (_slope_pct(_ratio(inventory, cor) * 365, 10).diff(10) / _sma(_ratio(inventory, cor) * 365.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_diff_norm_21d_v121_signal(cor):
    res = (_slope_pct(cor, 21).diff(21) / _sma(cor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_diff_norm_21d_v122_signal(inventory):
    res = (_slope_pct(inventory, 21).diff(21) / _sma(inventory.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_diff_norm_21d_v123_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_diff_norm_21d_v124_signal(cor, inventory):
    res = (_slope_pct(_ratio(cor, inventory), 21).diff(21) / _sma(_ratio(cor, inventory).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_diff_norm_21d_v125_signal(inventory, cor):
    res = (_slope_pct(_ratio(inventory, cor) * 365, 21).diff(21) / _sma(_ratio(inventory, cor) * 365.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_diff_norm_42d_v126_signal(cor):
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_diff_norm_42d_v127_signal(inventory):
    res = (_slope_pct(inventory, 42).diff(42) / _sma(inventory.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_diff_norm_42d_v128_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_diff_norm_42d_v129_signal(cor, inventory):
    res = (_slope_pct(_ratio(cor, inventory), 42).diff(42) / _sma(_ratio(cor, inventory).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_diff_norm_42d_v130_signal(inventory, cor):
    res = (_slope_pct(_ratio(inventory, cor) * 365, 42).diff(42) / _sma(_ratio(inventory, cor) * 365.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_diff_norm_63d_v131_signal(cor):
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_diff_norm_63d_v132_signal(inventory):
    res = (_slope_pct(inventory, 63).diff(63) / _sma(inventory.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_diff_norm_63d_v133_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_diff_norm_63d_v134_signal(cor, inventory):
    res = (_slope_pct(_ratio(cor, inventory), 63).diff(63) / _sma(_ratio(cor, inventory).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_diff_norm_63d_v135_signal(inventory, cor):
    res = (_slope_pct(_ratio(inventory, cor) * 365, 63).diff(63) / _sma(_ratio(inventory, cor) * 365.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_diff_norm_126d_v136_signal(cor):
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_diff_norm_126d_v137_signal(inventory):
    res = (_slope_pct(inventory, 126).diff(126) / _sma(inventory.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_diff_norm_126d_v138_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_diff_norm_126d_v139_signal(cor, inventory):
    res = (_slope_pct(_ratio(cor, inventory), 126).diff(126) / _sma(_ratio(cor, inventory).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_diff_norm_126d_v140_signal(inventory, cor):
    res = (_slope_pct(_ratio(inventory, cor) * 365, 126).diff(126) / _sma(_ratio(inventory, cor) * 365.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_diff_norm_252d_v141_signal(cor):
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_diff_norm_252d_v142_signal(inventory):
    res = (_slope_pct(inventory, 252).diff(252) / _sma(inventory.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_diff_norm_252d_v143_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_diff_norm_252d_v144_signal(cor, inventory):
    res = (_slope_pct(_ratio(cor, inventory), 252).diff(252) / _sma(_ratio(cor, inventory).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_diff_norm_252d_v145_signal(inventory, cor):
    res = (_slope_pct(_ratio(inventory, cor) * 365, 252).diff(252) / _sma(_ratio(inventory, cor) * 365.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_cor_slope_diff_norm_504d_v146_signal(cor):
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inventory_slope_diff_norm_504d_v147_signal(inventory):
    res = (_slope_pct(inventory, 504).diff(504) / _sma(inventory.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_revenue_slope_diff_norm_504d_v148_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_inv_turnover_slope_diff_norm_504d_v149_signal(cor, inventory):
    res = (_slope_pct(_ratio(cor, inventory), 504).diff(504) / _sma(_ratio(cor, inventory).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f12_inventory_velocity_days_inv_slope_diff_norm_504d_v150_signal(inventory, cor):
    res = (_slope_pct(_ratio(inventory, cor) * 365, 504).diff(504) / _sma(_ratio(inventory, cor) * 365.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 12...")
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
