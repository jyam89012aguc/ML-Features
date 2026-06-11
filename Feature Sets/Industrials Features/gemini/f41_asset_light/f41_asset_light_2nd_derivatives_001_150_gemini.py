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

def f41_asset_light_sgna_slope_pct_5d_v001_signal(sgna):
    res = _slope_pct(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_5d_v002_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_5d_v003_signal(assets):
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_5d_v004_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_5d_v005_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_10d_v006_signal(sgna):
    res = _slope_pct(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_10d_v007_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_10d_v008_signal(assets):
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_10d_v009_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_10d_v010_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_21d_v011_signal(sgna):
    res = _slope_pct(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_21d_v012_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_21d_v013_signal(assets):
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_21d_v014_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_21d_v015_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_42d_v016_signal(sgna):
    res = _slope_pct(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_42d_v017_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_42d_v018_signal(assets):
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_42d_v019_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_42d_v020_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_63d_v021_signal(sgna):
    res = _slope_pct(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_63d_v022_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_63d_v023_signal(assets):
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_63d_v024_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_63d_v025_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_126d_v026_signal(sgna):
    res = _slope_pct(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_126d_v027_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_126d_v028_signal(assets):
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_126d_v029_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_126d_v030_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_252d_v031_signal(sgna):
    res = _slope_pct(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_252d_v032_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_252d_v033_signal(assets):
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_252d_v034_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_252d_v035_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_504d_v036_signal(sgna):
    res = _slope_pct(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_504d_v037_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_504d_v038_signal(assets):
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_504d_v039_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_504d_v040_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_756d_v041_signal(sgna):
    res = _slope_pct(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_756d_v042_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_756d_v043_signal(assets):
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_756d_v044_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_756d_v045_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_1008d_v046_signal(sgna):
    res = _slope_pct(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_1008d_v047_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_1008d_v048_signal(assets):
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_1008d_v049_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_1008d_v050_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_pct_1260d_v051_signal(sgna):
    res = _slope_pct(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_pct_1260d_v052_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_pct_1260d_v053_signal(assets):
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_pct_1260d_v054_signal(revenue, assets):
    res = _slope_pct(_ratio(revenue, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_pct_1260d_v055_signal(sgna, revenue):
    res = _slope_pct(_ratio(sgna, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_5d_v056_signal(sgna):
    res = _jerk(sgna, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_5d_v057_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_5d_v058_signal(assets):
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_5d_v059_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_5d_v060_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_10d_v061_signal(sgna):
    res = _jerk(sgna, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_10d_v062_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_10d_v063_signal(assets):
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_10d_v064_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_10d_v065_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_21d_v066_signal(sgna):
    res = _jerk(sgna, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_21d_v067_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_21d_v068_signal(assets):
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_21d_v069_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_21d_v070_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_42d_v071_signal(sgna):
    res = _jerk(sgna, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_42d_v072_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_42d_v073_signal(assets):
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_42d_v074_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_42d_v075_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_63d_v076_signal(sgna):
    res = _jerk(sgna, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_63d_v077_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_63d_v078_signal(assets):
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_63d_v079_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_63d_v080_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_126d_v081_signal(sgna):
    res = _jerk(sgna, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_126d_v082_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_126d_v083_signal(assets):
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_126d_v084_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_126d_v085_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_252d_v086_signal(sgna):
    res = _jerk(sgna, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_252d_v087_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_252d_v088_signal(assets):
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_252d_v089_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_252d_v090_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_504d_v091_signal(sgna):
    res = _jerk(sgna, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_504d_v092_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_504d_v093_signal(assets):
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_504d_v094_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_504d_v095_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_756d_v096_signal(sgna):
    res = _jerk(sgna, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_756d_v097_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_756d_v098_signal(assets):
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_756d_v099_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_756d_v100_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_1008d_v101_signal(sgna):
    res = _jerk(sgna, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_1008d_v102_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_1008d_v103_signal(assets):
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_1008d_v104_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_1008d_v105_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_jerk_1260d_v106_signal(sgna):
    res = _jerk(sgna, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_jerk_1260d_v107_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_jerk_1260d_v108_signal(assets):
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_jerk_1260d_v109_signal(revenue, assets):
    res = _jerk(_ratio(revenue, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_jerk_1260d_v110_signal(sgna, revenue):
    res = _jerk(_ratio(sgna, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_diff_norm_5d_v111_signal(sgna):
    res = (_slope_pct(sgna, 5).diff(5) / _sma(sgna.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_diff_norm_5d_v112_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_diff_norm_5d_v113_signal(assets):
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_diff_norm_5d_v114_signal(revenue, assets):
    res = (_slope_pct(_ratio(revenue, assets), 5).diff(5) / _sma(_ratio(revenue, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_diff_norm_5d_v115_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 5).diff(5) / _sma(_ratio(sgna, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_diff_norm_10d_v116_signal(sgna):
    res = (_slope_pct(sgna, 10).diff(10) / _sma(sgna.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_diff_norm_10d_v117_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_diff_norm_10d_v118_signal(assets):
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_diff_norm_10d_v119_signal(revenue, assets):
    res = (_slope_pct(_ratio(revenue, assets), 10).diff(10) / _sma(_ratio(revenue, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_diff_norm_10d_v120_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 10).diff(10) / _sma(_ratio(sgna, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_diff_norm_21d_v121_signal(sgna):
    res = (_slope_pct(sgna, 21).diff(21) / _sma(sgna.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_diff_norm_21d_v122_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_diff_norm_21d_v123_signal(assets):
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_diff_norm_21d_v124_signal(revenue, assets):
    res = (_slope_pct(_ratio(revenue, assets), 21).diff(21) / _sma(_ratio(revenue, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_diff_norm_21d_v125_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 21).diff(21) / _sma(_ratio(sgna, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_diff_norm_42d_v126_signal(sgna):
    res = (_slope_pct(sgna, 42).diff(42) / _sma(sgna.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_diff_norm_42d_v127_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_diff_norm_42d_v128_signal(assets):
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_diff_norm_42d_v129_signal(revenue, assets):
    res = (_slope_pct(_ratio(revenue, assets), 42).diff(42) / _sma(_ratio(revenue, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_diff_norm_42d_v130_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 42).diff(42) / _sma(_ratio(sgna, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_diff_norm_63d_v131_signal(sgna):
    res = (_slope_pct(sgna, 63).diff(63) / _sma(sgna.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_diff_norm_63d_v132_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_diff_norm_63d_v133_signal(assets):
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_diff_norm_63d_v134_signal(revenue, assets):
    res = (_slope_pct(_ratio(revenue, assets), 63).diff(63) / _sma(_ratio(revenue, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_diff_norm_63d_v135_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 63).diff(63) / _sma(_ratio(sgna, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_diff_norm_126d_v136_signal(sgna):
    res = (_slope_pct(sgna, 126).diff(126) / _sma(sgna.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_diff_norm_126d_v137_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_diff_norm_126d_v138_signal(assets):
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_diff_norm_126d_v139_signal(revenue, assets):
    res = (_slope_pct(_ratio(revenue, assets), 126).diff(126) / _sma(_ratio(revenue, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_diff_norm_126d_v140_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 126).diff(126) / _sma(_ratio(sgna, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_diff_norm_252d_v141_signal(sgna):
    res = (_slope_pct(sgna, 252).diff(252) / _sma(sgna.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_diff_norm_252d_v142_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_diff_norm_252d_v143_signal(assets):
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_diff_norm_252d_v144_signal(revenue, assets):
    res = (_slope_pct(_ratio(revenue, assets), 252).diff(252) / _sma(_ratio(revenue, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_diff_norm_252d_v145_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 252).diff(252) / _sma(_ratio(sgna, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_sgna_slope_diff_norm_504d_v146_signal(sgna):
    res = (_slope_pct(sgna, 504).diff(504) / _sma(sgna.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_revenue_slope_diff_norm_504d_v147_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_assets_slope_diff_norm_504d_v148_signal(assets):
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_asset_turnover_slope_diff_norm_504d_v149_signal(revenue, assets):
    res = (_slope_pct(_ratio(revenue, assets), 504).diff(504) / _sma(_ratio(revenue, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f41_asset_light_fixed_cost_ratio_slope_diff_norm_504d_v150_signal(sgna, revenue):
    res = (_slope_pct(_ratio(sgna, revenue), 504).diff(504) / _sma(_ratio(sgna, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 41...")
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
