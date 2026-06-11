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

def f15_high_voltage_cycles_ebit_slope_pct_5d_v001_signal(ebit):
    res = _slope_pct(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_5d_v002_signal(capex):
    res = _slope_pct(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_5d_v003_signal(assets):
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_5d_v004_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_5d_v005_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_10d_v006_signal(ebit):
    res = _slope_pct(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_10d_v007_signal(capex):
    res = _slope_pct(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_10d_v008_signal(assets):
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_10d_v009_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_10d_v010_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_21d_v011_signal(ebit):
    res = _slope_pct(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_21d_v012_signal(capex):
    res = _slope_pct(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_21d_v013_signal(assets):
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_21d_v014_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_21d_v015_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_42d_v016_signal(ebit):
    res = _slope_pct(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_42d_v017_signal(capex):
    res = _slope_pct(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_42d_v018_signal(assets):
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_42d_v019_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_42d_v020_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_63d_v021_signal(ebit):
    res = _slope_pct(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_63d_v022_signal(capex):
    res = _slope_pct(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_63d_v023_signal(assets):
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_63d_v024_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_63d_v025_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_126d_v026_signal(ebit):
    res = _slope_pct(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_126d_v027_signal(capex):
    res = _slope_pct(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_126d_v028_signal(assets):
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_126d_v029_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_126d_v030_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_252d_v031_signal(ebit):
    res = _slope_pct(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_252d_v032_signal(capex):
    res = _slope_pct(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_252d_v033_signal(assets):
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_252d_v034_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_252d_v035_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_504d_v036_signal(ebit):
    res = _slope_pct(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_504d_v037_signal(capex):
    res = _slope_pct(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_504d_v038_signal(assets):
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_504d_v039_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_504d_v040_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_756d_v041_signal(ebit):
    res = _slope_pct(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_756d_v042_signal(capex):
    res = _slope_pct(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_756d_v043_signal(assets):
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_756d_v044_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_756d_v045_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_1008d_v046_signal(ebit):
    res = _slope_pct(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_1008d_v047_signal(capex):
    res = _slope_pct(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_1008d_v048_signal(assets):
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_1008d_v049_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_1008d_v050_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_pct_1260d_v051_signal(ebit):
    res = _slope_pct(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_pct_1260d_v052_signal(capex):
    res = _slope_pct(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_pct_1260d_v053_signal(assets):
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_pct_1260d_v054_signal(ebit, assets):
    res = _slope_pct(_ratio(ebit, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_pct_1260d_v055_signal(ebit, capex):
    res = _slope_pct(_ratio(ebit, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_5d_v056_signal(ebit):
    res = _jerk(ebit, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_5d_v057_signal(capex):
    res = _jerk(capex, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_5d_v058_signal(assets):
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_5d_v059_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_5d_v060_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_10d_v061_signal(ebit):
    res = _jerk(ebit, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_10d_v062_signal(capex):
    res = _jerk(capex, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_10d_v063_signal(assets):
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_10d_v064_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_10d_v065_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_21d_v066_signal(ebit):
    res = _jerk(ebit, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_21d_v067_signal(capex):
    res = _jerk(capex, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_21d_v068_signal(assets):
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_21d_v069_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_21d_v070_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_42d_v071_signal(ebit):
    res = _jerk(ebit, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_42d_v072_signal(capex):
    res = _jerk(capex, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_42d_v073_signal(assets):
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_42d_v074_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_42d_v075_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_63d_v076_signal(ebit):
    res = _jerk(ebit, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_63d_v077_signal(capex):
    res = _jerk(capex, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_63d_v078_signal(assets):
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_63d_v079_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_63d_v080_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_126d_v081_signal(ebit):
    res = _jerk(ebit, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_126d_v082_signal(capex):
    res = _jerk(capex, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_126d_v083_signal(assets):
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_126d_v084_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_126d_v085_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_252d_v086_signal(ebit):
    res = _jerk(ebit, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_252d_v087_signal(capex):
    res = _jerk(capex, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_252d_v088_signal(assets):
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_252d_v089_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_252d_v090_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_504d_v091_signal(ebit):
    res = _jerk(ebit, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_504d_v092_signal(capex):
    res = _jerk(capex, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_504d_v093_signal(assets):
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_504d_v094_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_504d_v095_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_756d_v096_signal(ebit):
    res = _jerk(ebit, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_756d_v097_signal(capex):
    res = _jerk(capex, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_756d_v098_signal(assets):
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_756d_v099_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_756d_v100_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_1008d_v101_signal(ebit):
    res = _jerk(ebit, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_1008d_v102_signal(capex):
    res = _jerk(capex, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_1008d_v103_signal(assets):
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_1008d_v104_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_1008d_v105_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_jerk_1260d_v106_signal(ebit):
    res = _jerk(ebit, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_jerk_1260d_v107_signal(capex):
    res = _jerk(capex, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_jerk_1260d_v108_signal(assets):
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_jerk_1260d_v109_signal(ebit, assets):
    res = _jerk(_ratio(ebit, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_jerk_1260d_v110_signal(ebit, capex):
    res = _jerk(_ratio(ebit, capex), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_diff_norm_5d_v111_signal(ebit):
    res = (_slope_pct(ebit, 5).diff(5) / _sma(ebit.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_diff_norm_5d_v112_signal(capex):
    res = (_slope_pct(capex, 5).diff(5) / _sma(capex.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_diff_norm_5d_v113_signal(assets):
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_diff_norm_5d_v114_signal(ebit, assets):
    res = (_slope_pct(_ratio(ebit, assets), 5).diff(5) / _sma(_ratio(ebit, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_diff_norm_5d_v115_signal(ebit, capex):
    res = (_slope_pct(_ratio(ebit, capex), 5).diff(5) / _sma(_ratio(ebit, capex).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_diff_norm_10d_v116_signal(ebit):
    res = (_slope_pct(ebit, 10).diff(10) / _sma(ebit.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_diff_norm_10d_v117_signal(capex):
    res = (_slope_pct(capex, 10).diff(10) / _sma(capex.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_diff_norm_10d_v118_signal(assets):
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_diff_norm_10d_v119_signal(ebit, assets):
    res = (_slope_pct(_ratio(ebit, assets), 10).diff(10) / _sma(_ratio(ebit, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_diff_norm_10d_v120_signal(ebit, capex):
    res = (_slope_pct(_ratio(ebit, capex), 10).diff(10) / _sma(_ratio(ebit, capex).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_diff_norm_21d_v121_signal(ebit):
    res = (_slope_pct(ebit, 21).diff(21) / _sma(ebit.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_diff_norm_21d_v122_signal(capex):
    res = (_slope_pct(capex, 21).diff(21) / _sma(capex.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_diff_norm_21d_v123_signal(assets):
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_diff_norm_21d_v124_signal(ebit, assets):
    res = (_slope_pct(_ratio(ebit, assets), 21).diff(21) / _sma(_ratio(ebit, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_diff_norm_21d_v125_signal(ebit, capex):
    res = (_slope_pct(_ratio(ebit, capex), 21).diff(21) / _sma(_ratio(ebit, capex).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_diff_norm_42d_v126_signal(ebit):
    res = (_slope_pct(ebit, 42).diff(42) / _sma(ebit.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_diff_norm_42d_v127_signal(capex):
    res = (_slope_pct(capex, 42).diff(42) / _sma(capex.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_diff_norm_42d_v128_signal(assets):
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_diff_norm_42d_v129_signal(ebit, assets):
    res = (_slope_pct(_ratio(ebit, assets), 42).diff(42) / _sma(_ratio(ebit, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_diff_norm_42d_v130_signal(ebit, capex):
    res = (_slope_pct(_ratio(ebit, capex), 42).diff(42) / _sma(_ratio(ebit, capex).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_diff_norm_63d_v131_signal(ebit):
    res = (_slope_pct(ebit, 63).diff(63) / _sma(ebit.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_diff_norm_63d_v132_signal(capex):
    res = (_slope_pct(capex, 63).diff(63) / _sma(capex.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_diff_norm_63d_v133_signal(assets):
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_diff_norm_63d_v134_signal(ebit, assets):
    res = (_slope_pct(_ratio(ebit, assets), 63).diff(63) / _sma(_ratio(ebit, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_diff_norm_63d_v135_signal(ebit, capex):
    res = (_slope_pct(_ratio(ebit, capex), 63).diff(63) / _sma(_ratio(ebit, capex).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_diff_norm_126d_v136_signal(ebit):
    res = (_slope_pct(ebit, 126).diff(126) / _sma(ebit.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_diff_norm_126d_v137_signal(capex):
    res = (_slope_pct(capex, 126).diff(126) / _sma(capex.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_diff_norm_126d_v138_signal(assets):
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_diff_norm_126d_v139_signal(ebit, assets):
    res = (_slope_pct(_ratio(ebit, assets), 126).diff(126) / _sma(_ratio(ebit, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_diff_norm_126d_v140_signal(ebit, capex):
    res = (_slope_pct(_ratio(ebit, capex), 126).diff(126) / _sma(_ratio(ebit, capex).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_diff_norm_252d_v141_signal(ebit):
    res = (_slope_pct(ebit, 252).diff(252) / _sma(ebit.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_diff_norm_252d_v142_signal(capex):
    res = (_slope_pct(capex, 252).diff(252) / _sma(capex.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_diff_norm_252d_v143_signal(assets):
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_diff_norm_252d_v144_signal(ebit, assets):
    res = (_slope_pct(_ratio(ebit, assets), 252).diff(252) / _sma(_ratio(ebit, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_diff_norm_252d_v145_signal(ebit, capex):
    res = (_slope_pct(_ratio(ebit, capex), 252).diff(252) / _sma(_ratio(ebit, capex).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_slope_diff_norm_504d_v146_signal(ebit):
    res = (_slope_pct(ebit, 504).diff(504) / _sma(ebit.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_capex_slope_diff_norm_504d_v147_signal(capex):
    res = (_slope_pct(capex, 504).diff(504) / _sma(capex.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_assets_slope_diff_norm_504d_v148_signal(assets):
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_assets_slope_diff_norm_504d_v149_signal(ebit, assets):
    res = (_slope_pct(_ratio(ebit, assets), 504).diff(504) / _sma(_ratio(ebit, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f15_high_voltage_cycles_ebit_to_capex_slope_diff_norm_504d_v150_signal(ebit, capex):
    res = (_slope_pct(_ratio(ebit, capex), 504).diff(504) / _sma(_ratio(ebit, capex).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 15...")
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
