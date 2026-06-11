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

def f21_equipment_age_capex_slope_pct_5d_v001_signal(capex):
    res = _slope_pct(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_5d_v002_signal(assets):
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_5d_v003_signal(depamor):
    res = _slope_pct(depamor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_5d_v004_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_5d_v005_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_10d_v006_signal(capex):
    res = _slope_pct(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_10d_v007_signal(assets):
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_10d_v008_signal(depamor):
    res = _slope_pct(depamor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_10d_v009_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_10d_v010_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_21d_v011_signal(capex):
    res = _slope_pct(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_21d_v012_signal(assets):
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_21d_v013_signal(depamor):
    res = _slope_pct(depamor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_21d_v014_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_21d_v015_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_42d_v016_signal(capex):
    res = _slope_pct(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_42d_v017_signal(assets):
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_42d_v018_signal(depamor):
    res = _slope_pct(depamor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_42d_v019_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_42d_v020_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_63d_v021_signal(capex):
    res = _slope_pct(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_63d_v022_signal(assets):
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_63d_v023_signal(depamor):
    res = _slope_pct(depamor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_63d_v024_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_63d_v025_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_126d_v026_signal(capex):
    res = _slope_pct(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_126d_v027_signal(assets):
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_126d_v028_signal(depamor):
    res = _slope_pct(depamor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_126d_v029_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_126d_v030_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_252d_v031_signal(capex):
    res = _slope_pct(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_252d_v032_signal(assets):
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_252d_v033_signal(depamor):
    res = _slope_pct(depamor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_252d_v034_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_252d_v035_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_504d_v036_signal(capex):
    res = _slope_pct(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_504d_v037_signal(assets):
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_504d_v038_signal(depamor):
    res = _slope_pct(depamor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_504d_v039_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_504d_v040_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_756d_v041_signal(capex):
    res = _slope_pct(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_756d_v042_signal(assets):
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_756d_v043_signal(depamor):
    res = _slope_pct(depamor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_756d_v044_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_756d_v045_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_1008d_v046_signal(capex):
    res = _slope_pct(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_1008d_v047_signal(assets):
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_1008d_v048_signal(depamor):
    res = _slope_pct(depamor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_1008d_v049_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_1008d_v050_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_pct_1260d_v051_signal(capex):
    res = _slope_pct(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_pct_1260d_v052_signal(assets):
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_pct_1260d_v053_signal(depamor):
    res = _slope_pct(depamor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_pct_1260d_v054_signal(capex, depamor):
    res = _slope_pct(_ratio(capex, depamor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_pct_1260d_v055_signal(assets, depamor):
    res = _slope_pct(_ratio(assets, depamor), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_5d_v056_signal(capex):
    res = _jerk(capex, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_5d_v057_signal(assets):
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_5d_v058_signal(depamor):
    res = _jerk(depamor, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_5d_v059_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_5d_v060_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_10d_v061_signal(capex):
    res = _jerk(capex, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_10d_v062_signal(assets):
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_10d_v063_signal(depamor):
    res = _jerk(depamor, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_10d_v064_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_10d_v065_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_21d_v066_signal(capex):
    res = _jerk(capex, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_21d_v067_signal(assets):
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_21d_v068_signal(depamor):
    res = _jerk(depamor, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_21d_v069_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_21d_v070_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_42d_v071_signal(capex):
    res = _jerk(capex, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_42d_v072_signal(assets):
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_42d_v073_signal(depamor):
    res = _jerk(depamor, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_42d_v074_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_42d_v075_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_63d_v076_signal(capex):
    res = _jerk(capex, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_63d_v077_signal(assets):
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_63d_v078_signal(depamor):
    res = _jerk(depamor, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_63d_v079_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_63d_v080_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_126d_v081_signal(capex):
    res = _jerk(capex, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_126d_v082_signal(assets):
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_126d_v083_signal(depamor):
    res = _jerk(depamor, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_126d_v084_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_126d_v085_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_252d_v086_signal(capex):
    res = _jerk(capex, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_252d_v087_signal(assets):
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_252d_v088_signal(depamor):
    res = _jerk(depamor, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_252d_v089_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_252d_v090_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_504d_v091_signal(capex):
    res = _jerk(capex, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_504d_v092_signal(assets):
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_504d_v093_signal(depamor):
    res = _jerk(depamor, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_504d_v094_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_504d_v095_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_756d_v096_signal(capex):
    res = _jerk(capex, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_756d_v097_signal(assets):
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_756d_v098_signal(depamor):
    res = _jerk(depamor, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_756d_v099_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_756d_v100_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_1008d_v101_signal(capex):
    res = _jerk(capex, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_1008d_v102_signal(assets):
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_1008d_v103_signal(depamor):
    res = _jerk(depamor, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_1008d_v104_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_1008d_v105_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_jerk_1260d_v106_signal(capex):
    res = _jerk(capex, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_jerk_1260d_v107_signal(assets):
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_jerk_1260d_v108_signal(depamor):
    res = _jerk(depamor, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_jerk_1260d_v109_signal(capex, depamor):
    res = _jerk(_ratio(capex, depamor), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_jerk_1260d_v110_signal(assets, depamor):
    res = _jerk(_ratio(assets, depamor), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_5d_v111_signal(capex):
    res = (_slope_pct(capex, 5).diff(5) / _sma(capex.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_5d_v112_signal(assets):
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_5d_v113_signal(depamor):
    res = (_slope_pct(depamor, 5).diff(5) / _sma(depamor.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_5d_v114_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 5).diff(5) / _sma(_ratio(capex, depamor).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_5d_v115_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 5).diff(5) / _sma(_ratio(assets, depamor).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_10d_v116_signal(capex):
    res = (_slope_pct(capex, 10).diff(10) / _sma(capex.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_10d_v117_signal(assets):
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_10d_v118_signal(depamor):
    res = (_slope_pct(depamor, 10).diff(10) / _sma(depamor.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_10d_v119_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 10).diff(10) / _sma(_ratio(capex, depamor).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_10d_v120_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 10).diff(10) / _sma(_ratio(assets, depamor).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_21d_v121_signal(capex):
    res = (_slope_pct(capex, 21).diff(21) / _sma(capex.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_21d_v122_signal(assets):
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_21d_v123_signal(depamor):
    res = (_slope_pct(depamor, 21).diff(21) / _sma(depamor.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_21d_v124_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 21).diff(21) / _sma(_ratio(capex, depamor).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_21d_v125_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 21).diff(21) / _sma(_ratio(assets, depamor).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_42d_v126_signal(capex):
    res = (_slope_pct(capex, 42).diff(42) / _sma(capex.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_42d_v127_signal(assets):
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_42d_v128_signal(depamor):
    res = (_slope_pct(depamor, 42).diff(42) / _sma(depamor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_42d_v129_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 42).diff(42) / _sma(_ratio(capex, depamor).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_42d_v130_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 42).diff(42) / _sma(_ratio(assets, depamor).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_63d_v131_signal(capex):
    res = (_slope_pct(capex, 63).diff(63) / _sma(capex.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_63d_v132_signal(assets):
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_63d_v133_signal(depamor):
    res = (_slope_pct(depamor, 63).diff(63) / _sma(depamor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_63d_v134_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 63).diff(63) / _sma(_ratio(capex, depamor).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_63d_v135_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 63).diff(63) / _sma(_ratio(assets, depamor).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_126d_v136_signal(capex):
    res = (_slope_pct(capex, 126).diff(126) / _sma(capex.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_126d_v137_signal(assets):
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_126d_v138_signal(depamor):
    res = (_slope_pct(depamor, 126).diff(126) / _sma(depamor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_126d_v139_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 126).diff(126) / _sma(_ratio(capex, depamor).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_126d_v140_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 126).diff(126) / _sma(_ratio(assets, depamor).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_252d_v141_signal(capex):
    res = (_slope_pct(capex, 252).diff(252) / _sma(capex.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_252d_v142_signal(assets):
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_252d_v143_signal(depamor):
    res = (_slope_pct(depamor, 252).diff(252) / _sma(depamor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_252d_v144_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 252).diff(252) / _sma(_ratio(capex, depamor).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_252d_v145_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 252).diff(252) / _sma(_ratio(assets, depamor).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_capex_slope_diff_norm_504d_v146_signal(capex):
    res = (_slope_pct(capex, 504).diff(504) / _sma(capex.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_assets_slope_diff_norm_504d_v147_signal(assets):
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_depamor_slope_diff_norm_504d_v148_signal(depamor):
    res = (_slope_pct(depamor, 504).diff(504) / _sma(depamor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_reinvestment_ratio_slope_diff_norm_504d_v149_signal(capex, depamor):
    res = (_slope_pct(_ratio(capex, depamor), 504).diff(504) / _sma(_ratio(capex, depamor).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f21_equipment_age_asset_age_proxy_slope_diff_norm_504d_v150_signal(assets, depamor):
    res = (_slope_pct(_ratio(assets, depamor), 504).diff(504) / _sma(_ratio(assets, depamor).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 21...")
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
