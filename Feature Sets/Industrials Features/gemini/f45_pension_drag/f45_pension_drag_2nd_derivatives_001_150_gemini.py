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

def f45_pension_drag_netinc_slope_pct_5d_v001_signal(netinc):
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_5d_v002_signal(assets):
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_5d_v003_signal(debt):
    res = _slope_pct(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_5d_v004_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_10d_v005_signal(netinc):
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_10d_v006_signal(assets):
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_10d_v007_signal(debt):
    res = _slope_pct(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_10d_v008_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_21d_v009_signal(netinc):
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_21d_v010_signal(assets):
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_21d_v011_signal(debt):
    res = _slope_pct(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_21d_v012_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_42d_v013_signal(netinc):
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_42d_v014_signal(assets):
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_42d_v015_signal(debt):
    res = _slope_pct(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_42d_v016_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_63d_v017_signal(netinc):
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_63d_v018_signal(assets):
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_63d_v019_signal(debt):
    res = _slope_pct(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_63d_v020_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_126d_v021_signal(netinc):
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_126d_v022_signal(assets):
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_126d_v023_signal(debt):
    res = _slope_pct(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_126d_v024_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_252d_v025_signal(netinc):
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_252d_v026_signal(assets):
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_252d_v027_signal(debt):
    res = _slope_pct(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_252d_v028_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_504d_v029_signal(netinc):
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_504d_v030_signal(assets):
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_504d_v031_signal(debt):
    res = _slope_pct(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_504d_v032_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_756d_v033_signal(netinc):
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_756d_v034_signal(assets):
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_756d_v035_signal(debt):
    res = _slope_pct(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_756d_v036_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_1008d_v037_signal(netinc):
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_1008d_v038_signal(assets):
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_1008d_v039_signal(debt):
    res = _slope_pct(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_1008d_v040_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_pct_1260d_v041_signal(netinc):
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_pct_1260d_v042_signal(assets):
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_pct_1260d_v043_signal(debt):
    res = _slope_pct(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_pct_1260d_v044_signal(debt, assets):
    res = _slope_pct(_ratio(debt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_5d_v045_signal(netinc):
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_5d_v046_signal(assets):
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_5d_v047_signal(debt):
    res = _jerk(debt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_5d_v048_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_10d_v049_signal(netinc):
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_10d_v050_signal(assets):
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_10d_v051_signal(debt):
    res = _jerk(debt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_10d_v052_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_21d_v053_signal(netinc):
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_21d_v054_signal(assets):
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_21d_v055_signal(debt):
    res = _jerk(debt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_21d_v056_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_42d_v057_signal(netinc):
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_42d_v058_signal(assets):
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_42d_v059_signal(debt):
    res = _jerk(debt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_42d_v060_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_63d_v061_signal(netinc):
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_63d_v062_signal(assets):
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_63d_v063_signal(debt):
    res = _jerk(debt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_63d_v064_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_126d_v065_signal(netinc):
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_126d_v066_signal(assets):
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_126d_v067_signal(debt):
    res = _jerk(debt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_126d_v068_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_252d_v069_signal(netinc):
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_252d_v070_signal(assets):
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_252d_v071_signal(debt):
    res = _jerk(debt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_252d_v072_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_504d_v073_signal(netinc):
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_504d_v074_signal(assets):
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_504d_v075_signal(debt):
    res = _jerk(debt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_504d_v076_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_756d_v077_signal(netinc):
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_756d_v078_signal(assets):
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_756d_v079_signal(debt):
    res = _jerk(debt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_756d_v080_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_1008d_v081_signal(netinc):
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_1008d_v082_signal(assets):
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_1008d_v083_signal(debt):
    res = _jerk(debt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_1008d_v084_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_jerk_1260d_v085_signal(netinc):
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_jerk_1260d_v086_signal(assets):
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_jerk_1260d_v087_signal(debt):
    res = _jerk(debt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_jerk_1260d_v088_signal(debt, assets):
    res = _jerk(_ratio(debt, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_5d_v089_signal(netinc):
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_5d_v090_signal(assets):
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_5d_v091_signal(debt):
    res = (_slope_pct(debt, 5).diff(5) / _sma(debt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_5d_v092_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 5).diff(5) / _sma(_ratio(debt, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_10d_v093_signal(netinc):
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_10d_v094_signal(assets):
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_10d_v095_signal(debt):
    res = (_slope_pct(debt, 10).diff(10) / _sma(debt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_10d_v096_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 10).diff(10) / _sma(_ratio(debt, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_21d_v097_signal(netinc):
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_21d_v098_signal(assets):
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_21d_v099_signal(debt):
    res = (_slope_pct(debt, 21).diff(21) / _sma(debt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_21d_v100_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 21).diff(21) / _sma(_ratio(debt, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_42d_v101_signal(netinc):
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_42d_v102_signal(assets):
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_42d_v103_signal(debt):
    res = (_slope_pct(debt, 42).diff(42) / _sma(debt.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_42d_v104_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 42).diff(42) / _sma(_ratio(debt, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_63d_v105_signal(netinc):
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_63d_v106_signal(assets):
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_63d_v107_signal(debt):
    res = (_slope_pct(debt, 63).diff(63) / _sma(debt.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_63d_v108_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 63).diff(63) / _sma(_ratio(debt, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_126d_v109_signal(netinc):
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_126d_v110_signal(assets):
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_126d_v111_signal(debt):
    res = (_slope_pct(debt, 126).diff(126) / _sma(debt.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_126d_v112_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 126).diff(126) / _sma(_ratio(debt, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_252d_v113_signal(netinc):
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_252d_v114_signal(assets):
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_252d_v115_signal(debt):
    res = (_slope_pct(debt, 252).diff(252) / _sma(debt.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_252d_v116_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 252).diff(252) / _sma(_ratio(debt, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_504d_v117_signal(netinc):
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_504d_v118_signal(assets):
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_504d_v119_signal(debt):
    res = (_slope_pct(debt, 504).diff(504) / _sma(debt.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_504d_v120_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 504).diff(504) / _sma(_ratio(debt, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_756d_v121_signal(netinc):
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_756d_v122_signal(assets):
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_756d_v123_signal(debt):
    res = (_slope_pct(debt, 756).diff(756) / _sma(debt.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_756d_v124_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 756).diff(756) / _sma(_ratio(debt, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_1008d_v125_signal(netinc):
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_1008d_v126_signal(assets):
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_1008d_v127_signal(debt):
    res = (_slope_pct(debt, 1008).diff(1008) / _sma(debt.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_1008d_v128_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 1008).diff(1008) / _sma(_ratio(debt, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_slope_diff_norm_1260d_v129_signal(netinc):
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_slope_diff_norm_1260d_v130_signal(assets):
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_slope_diff_norm_1260d_v131_signal(debt):
    res = (_slope_pct(debt, 1260).diff(1260) / _sma(debt.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_slope_diff_norm_1260d_v132_signal(debt, assets):
    res = (_slope_pct(_ratio(debt, assets), 1260).diff(1260) / _sma(_ratio(debt, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_mom_z_5d_v133_signal(netinc):
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_mom_z_5d_v134_signal(assets):
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_mom_z_5d_v135_signal(debt):
    res = _z(_slope_pct(debt, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_mom_z_5d_v136_signal(debt, assets):
    res = _z(_slope_pct(_ratio(debt, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_mom_z_10d_v137_signal(netinc):
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_mom_z_10d_v138_signal(assets):
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_mom_z_10d_v139_signal(debt):
    res = _z(_slope_pct(debt, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_mom_z_10d_v140_signal(debt, assets):
    res = _z(_slope_pct(_ratio(debt, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_mom_z_21d_v141_signal(netinc):
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_mom_z_21d_v142_signal(assets):
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_mom_z_21d_v143_signal(debt):
    res = _z(_slope_pct(debt, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_mom_z_21d_v144_signal(debt, assets):
    res = _z(_slope_pct(_ratio(debt, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_mom_z_42d_v145_signal(netinc):
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_mom_z_42d_v146_signal(assets):
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_mom_z_42d_v147_signal(debt):
    res = _z(_slope_pct(debt, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_debt_to_assets_mom_z_42d_v148_signal(debt, assets):
    res = _z(_slope_pct(_ratio(debt, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_netinc_mom_z_63d_v149_signal(netinc):
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_pension_drag_assets_mom_z_63d_v150_signal(assets):
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 45...")
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
