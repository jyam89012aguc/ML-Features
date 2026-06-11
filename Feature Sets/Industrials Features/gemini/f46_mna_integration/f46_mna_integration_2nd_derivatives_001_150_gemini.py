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

def f46_mna_integration_ncfbus_slope_pct_5d_v001_signal(ncfbus):
    res = _slope_pct(ncfbus, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_5d_v002_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_5d_v003_signal(assets):
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_5d_v004_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_10d_v005_signal(ncfbus):
    res = _slope_pct(ncfbus, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_10d_v006_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_10d_v007_signal(assets):
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_10d_v008_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_21d_v009_signal(ncfbus):
    res = _slope_pct(ncfbus, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_21d_v010_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_21d_v011_signal(assets):
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_21d_v012_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_42d_v013_signal(ncfbus):
    res = _slope_pct(ncfbus, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_42d_v014_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_42d_v015_signal(assets):
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_42d_v016_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_63d_v017_signal(ncfbus):
    res = _slope_pct(ncfbus, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_63d_v018_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_63d_v019_signal(assets):
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_63d_v020_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_126d_v021_signal(ncfbus):
    res = _slope_pct(ncfbus, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_126d_v022_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_126d_v023_signal(assets):
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_126d_v024_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_252d_v025_signal(ncfbus):
    res = _slope_pct(ncfbus, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_252d_v026_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_252d_v027_signal(assets):
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_252d_v028_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_504d_v029_signal(ncfbus):
    res = _slope_pct(ncfbus, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_504d_v030_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_504d_v031_signal(assets):
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_504d_v032_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_756d_v033_signal(ncfbus):
    res = _slope_pct(ncfbus, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_756d_v034_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_756d_v035_signal(assets):
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_756d_v036_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_1008d_v037_signal(ncfbus):
    res = _slope_pct(ncfbus, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_1008d_v038_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_1008d_v039_signal(assets):
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_1008d_v040_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_pct_1260d_v041_signal(ncfbus):
    res = _slope_pct(ncfbus, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_pct_1260d_v042_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_pct_1260d_v043_signal(assets):
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_pct_1260d_v044_signal(ncfbus, assets):
    res = _slope_pct(_ratio(ncfbus, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_5d_v045_signal(ncfbus):
    res = _jerk(ncfbus, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_5d_v046_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_5d_v047_signal(assets):
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_5d_v048_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_10d_v049_signal(ncfbus):
    res = _jerk(ncfbus, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_10d_v050_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_10d_v051_signal(assets):
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_10d_v052_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_21d_v053_signal(ncfbus):
    res = _jerk(ncfbus, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_21d_v054_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_21d_v055_signal(assets):
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_21d_v056_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_42d_v057_signal(ncfbus):
    res = _jerk(ncfbus, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_42d_v058_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_42d_v059_signal(assets):
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_42d_v060_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_63d_v061_signal(ncfbus):
    res = _jerk(ncfbus, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_63d_v062_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_63d_v063_signal(assets):
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_63d_v064_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_126d_v065_signal(ncfbus):
    res = _jerk(ncfbus, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_126d_v066_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_126d_v067_signal(assets):
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_126d_v068_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_252d_v069_signal(ncfbus):
    res = _jerk(ncfbus, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_252d_v070_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_252d_v071_signal(assets):
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_252d_v072_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_504d_v073_signal(ncfbus):
    res = _jerk(ncfbus, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_504d_v074_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_504d_v075_signal(assets):
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_504d_v076_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_756d_v077_signal(ncfbus):
    res = _jerk(ncfbus, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_756d_v078_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_756d_v079_signal(assets):
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_756d_v080_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_1008d_v081_signal(ncfbus):
    res = _jerk(ncfbus, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_1008d_v082_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_1008d_v083_signal(assets):
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_1008d_v084_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_jerk_1260d_v085_signal(ncfbus):
    res = _jerk(ncfbus, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_jerk_1260d_v086_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_jerk_1260d_v087_signal(assets):
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_jerk_1260d_v088_signal(ncfbus, assets):
    res = _jerk(_ratio(ncfbus, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_5d_v089_signal(ncfbus):
    res = (_slope_pct(ncfbus, 5).diff(5) / _sma(ncfbus.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_5d_v090_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_5d_v091_signal(assets):
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_5d_v092_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 5).diff(5) / _sma(_ratio(ncfbus, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_10d_v093_signal(ncfbus):
    res = (_slope_pct(ncfbus, 10).diff(10) / _sma(ncfbus.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_10d_v094_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_10d_v095_signal(assets):
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_10d_v096_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 10).diff(10) / _sma(_ratio(ncfbus, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_21d_v097_signal(ncfbus):
    res = (_slope_pct(ncfbus, 21).diff(21) / _sma(ncfbus.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_21d_v098_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_21d_v099_signal(assets):
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_21d_v100_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 21).diff(21) / _sma(_ratio(ncfbus, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_42d_v101_signal(ncfbus):
    res = (_slope_pct(ncfbus, 42).diff(42) / _sma(ncfbus.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_42d_v102_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_42d_v103_signal(assets):
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_42d_v104_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 42).diff(42) / _sma(_ratio(ncfbus, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_63d_v105_signal(ncfbus):
    res = (_slope_pct(ncfbus, 63).diff(63) / _sma(ncfbus.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_63d_v106_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_63d_v107_signal(assets):
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_63d_v108_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 63).diff(63) / _sma(_ratio(ncfbus, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_126d_v109_signal(ncfbus):
    res = (_slope_pct(ncfbus, 126).diff(126) / _sma(ncfbus.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_126d_v110_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_126d_v111_signal(assets):
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_126d_v112_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 126).diff(126) / _sma(_ratio(ncfbus, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_252d_v113_signal(ncfbus):
    res = (_slope_pct(ncfbus, 252).diff(252) / _sma(ncfbus.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_252d_v114_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_252d_v115_signal(assets):
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_252d_v116_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 252).diff(252) / _sma(_ratio(ncfbus, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_504d_v117_signal(ncfbus):
    res = (_slope_pct(ncfbus, 504).diff(504) / _sma(ncfbus.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_504d_v118_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_504d_v119_signal(assets):
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_504d_v120_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 504).diff(504) / _sma(_ratio(ncfbus, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_756d_v121_signal(ncfbus):
    res = (_slope_pct(ncfbus, 756).diff(756) / _sma(ncfbus.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_756d_v122_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_756d_v123_signal(assets):
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_756d_v124_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 756).diff(756) / _sma(_ratio(ncfbus, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_1008d_v125_signal(ncfbus):
    res = (_slope_pct(ncfbus, 1008).diff(1008) / _sma(ncfbus.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_1008d_v126_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_1008d_v127_signal(assets):
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_1008d_v128_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 1008).diff(1008) / _sma(_ratio(ncfbus, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_slope_diff_norm_1260d_v129_signal(ncfbus):
    res = (_slope_pct(ncfbus, 1260).diff(1260) / _sma(ncfbus.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_slope_diff_norm_1260d_v130_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_slope_diff_norm_1260d_v131_signal(assets):
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_slope_diff_norm_1260d_v132_signal(ncfbus, assets):
    res = (_slope_pct(_ratio(ncfbus, assets), 1260).diff(1260) / _sma(_ratio(ncfbus, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_mom_z_5d_v133_signal(ncfbus):
    res = _z(_slope_pct(ncfbus, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_mom_z_5d_v134_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_mom_z_5d_v135_signal(assets):
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_mom_z_5d_v136_signal(ncfbus, assets):
    res = _z(_slope_pct(_ratio(ncfbus, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_mom_z_10d_v137_signal(ncfbus):
    res = _z(_slope_pct(ncfbus, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_mom_z_10d_v138_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_mom_z_10d_v139_signal(assets):
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_mom_z_10d_v140_signal(ncfbus, assets):
    res = _z(_slope_pct(_ratio(ncfbus, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_mom_z_21d_v141_signal(ncfbus):
    res = _z(_slope_pct(ncfbus, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_mom_z_21d_v142_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_mom_z_21d_v143_signal(assets):
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_mom_z_21d_v144_signal(ncfbus, assets):
    res = _z(_slope_pct(_ratio(ncfbus, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_mom_z_42d_v145_signal(ncfbus):
    res = _z(_slope_pct(ncfbus, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_mom_z_42d_v146_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_assets_mom_z_42d_v147_signal(assets):
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_mna_intensity_mom_z_42d_v148_signal(ncfbus, assets):
    res = _z(_slope_pct(_ratio(ncfbus, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_ncfbus_mom_z_63d_v149_signal(ncfbus):
    res = _z(_slope_pct(ncfbus, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_mna_integration_revenue_mom_z_63d_v150_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 46...")
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
