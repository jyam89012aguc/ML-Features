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

def f29_energy_mandates_revenue_slope_pct_5d_v001_signal(revenue):
    res = _slope_pct(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_5d_v002_signal(capex):
    res = _slope_pct(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_5d_v003_signal(rnd):
    res = _slope_pct(rnd, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_5d_v004_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_10d_v005_signal(revenue):
    res = _slope_pct(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_10d_v006_signal(capex):
    res = _slope_pct(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_10d_v007_signal(rnd):
    res = _slope_pct(rnd, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_10d_v008_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_21d_v009_signal(revenue):
    res = _slope_pct(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_21d_v010_signal(capex):
    res = _slope_pct(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_21d_v011_signal(rnd):
    res = _slope_pct(rnd, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_21d_v012_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_42d_v013_signal(revenue):
    res = _slope_pct(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_42d_v014_signal(capex):
    res = _slope_pct(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_42d_v015_signal(rnd):
    res = _slope_pct(rnd, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_42d_v016_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_63d_v017_signal(revenue):
    res = _slope_pct(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_63d_v018_signal(capex):
    res = _slope_pct(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_63d_v019_signal(rnd):
    res = _slope_pct(rnd, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_63d_v020_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_126d_v021_signal(revenue):
    res = _slope_pct(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_126d_v022_signal(capex):
    res = _slope_pct(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_126d_v023_signal(rnd):
    res = _slope_pct(rnd, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_126d_v024_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_252d_v025_signal(revenue):
    res = _slope_pct(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_252d_v026_signal(capex):
    res = _slope_pct(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_252d_v027_signal(rnd):
    res = _slope_pct(rnd, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_252d_v028_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_504d_v029_signal(revenue):
    res = _slope_pct(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_504d_v030_signal(capex):
    res = _slope_pct(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_504d_v031_signal(rnd):
    res = _slope_pct(rnd, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_504d_v032_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_756d_v033_signal(revenue):
    res = _slope_pct(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_756d_v034_signal(capex):
    res = _slope_pct(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_756d_v035_signal(rnd):
    res = _slope_pct(rnd, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_756d_v036_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_1008d_v037_signal(revenue):
    res = _slope_pct(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_1008d_v038_signal(capex):
    res = _slope_pct(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_1008d_v039_signal(rnd):
    res = _slope_pct(rnd, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_1008d_v040_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_pct_1260d_v041_signal(revenue):
    res = _slope_pct(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_pct_1260d_v042_signal(capex):
    res = _slope_pct(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_pct_1260d_v043_signal(rnd):
    res = _slope_pct(rnd, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_pct_1260d_v044_signal(capex, rnd, revenue):
    res = _slope_pct(_ratio(capex + rnd, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_5d_v045_signal(revenue):
    res = _jerk(revenue, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_5d_v046_signal(capex):
    res = _jerk(capex, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_5d_v047_signal(rnd):
    res = _jerk(rnd, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_5d_v048_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_10d_v049_signal(revenue):
    res = _jerk(revenue, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_10d_v050_signal(capex):
    res = _jerk(capex, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_10d_v051_signal(rnd):
    res = _jerk(rnd, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_10d_v052_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_21d_v053_signal(revenue):
    res = _jerk(revenue, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_21d_v054_signal(capex):
    res = _jerk(capex, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_21d_v055_signal(rnd):
    res = _jerk(rnd, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_21d_v056_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_42d_v057_signal(revenue):
    res = _jerk(revenue, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_42d_v058_signal(capex):
    res = _jerk(capex, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_42d_v059_signal(rnd):
    res = _jerk(rnd, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_42d_v060_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_63d_v061_signal(revenue):
    res = _jerk(revenue, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_63d_v062_signal(capex):
    res = _jerk(capex, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_63d_v063_signal(rnd):
    res = _jerk(rnd, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_63d_v064_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_126d_v065_signal(revenue):
    res = _jerk(revenue, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_126d_v066_signal(capex):
    res = _jerk(capex, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_126d_v067_signal(rnd):
    res = _jerk(rnd, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_126d_v068_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_252d_v069_signal(revenue):
    res = _jerk(revenue, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_252d_v070_signal(capex):
    res = _jerk(capex, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_252d_v071_signal(rnd):
    res = _jerk(rnd, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_252d_v072_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_504d_v073_signal(revenue):
    res = _jerk(revenue, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_504d_v074_signal(capex):
    res = _jerk(capex, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_504d_v075_signal(rnd):
    res = _jerk(rnd, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_504d_v076_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_756d_v077_signal(revenue):
    res = _jerk(revenue, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_756d_v078_signal(capex):
    res = _jerk(capex, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_756d_v079_signal(rnd):
    res = _jerk(rnd, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_756d_v080_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_1008d_v081_signal(revenue):
    res = _jerk(revenue, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_1008d_v082_signal(capex):
    res = _jerk(capex, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_1008d_v083_signal(rnd):
    res = _jerk(rnd, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_1008d_v084_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_jerk_1260d_v085_signal(revenue):
    res = _jerk(revenue, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_jerk_1260d_v086_signal(capex):
    res = _jerk(capex, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_jerk_1260d_v087_signal(rnd):
    res = _jerk(rnd, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_jerk_1260d_v088_signal(capex, rnd, revenue):
    res = _jerk(_ratio(capex + rnd, revenue), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_5d_v089_signal(revenue):
    res = (_slope_pct(revenue, 5).diff(5) / _sma(revenue.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_5d_v090_signal(capex):
    res = (_slope_pct(capex, 5).diff(5) / _sma(capex.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_5d_v091_signal(rnd):
    res = (_slope_pct(rnd, 5).diff(5) / _sma(rnd.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_5d_v092_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 5).diff(5) / _sma(_ratio(capex + rnd, revenue).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_10d_v093_signal(revenue):
    res = (_slope_pct(revenue, 10).diff(10) / _sma(revenue.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_10d_v094_signal(capex):
    res = (_slope_pct(capex, 10).diff(10) / _sma(capex.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_10d_v095_signal(rnd):
    res = (_slope_pct(rnd, 10).diff(10) / _sma(rnd.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_10d_v096_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 10).diff(10) / _sma(_ratio(capex + rnd, revenue).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_21d_v097_signal(revenue):
    res = (_slope_pct(revenue, 21).diff(21) / _sma(revenue.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_21d_v098_signal(capex):
    res = (_slope_pct(capex, 21).diff(21) / _sma(capex.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_21d_v099_signal(rnd):
    res = (_slope_pct(rnd, 21).diff(21) / _sma(rnd.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_21d_v100_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 21).diff(21) / _sma(_ratio(capex + rnd, revenue).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_42d_v101_signal(revenue):
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_42d_v102_signal(capex):
    res = (_slope_pct(capex, 42).diff(42) / _sma(capex.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_42d_v103_signal(rnd):
    res = (_slope_pct(rnd, 42).diff(42) / _sma(rnd.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_42d_v104_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 42).diff(42) / _sma(_ratio(capex + rnd, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_63d_v105_signal(revenue):
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_63d_v106_signal(capex):
    res = (_slope_pct(capex, 63).diff(63) / _sma(capex.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_63d_v107_signal(rnd):
    res = (_slope_pct(rnd, 63).diff(63) / _sma(rnd.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_63d_v108_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 63).diff(63) / _sma(_ratio(capex + rnd, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_126d_v109_signal(revenue):
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_126d_v110_signal(capex):
    res = (_slope_pct(capex, 126).diff(126) / _sma(capex.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_126d_v111_signal(rnd):
    res = (_slope_pct(rnd, 126).diff(126) / _sma(rnd.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_126d_v112_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 126).diff(126) / _sma(_ratio(capex + rnd, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_252d_v113_signal(revenue):
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_252d_v114_signal(capex):
    res = (_slope_pct(capex, 252).diff(252) / _sma(capex.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_252d_v115_signal(rnd):
    res = (_slope_pct(rnd, 252).diff(252) / _sma(rnd.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_252d_v116_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 252).diff(252) / _sma(_ratio(capex + rnd, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_504d_v117_signal(revenue):
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_504d_v118_signal(capex):
    res = (_slope_pct(capex, 504).diff(504) / _sma(capex.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_504d_v119_signal(rnd):
    res = (_slope_pct(rnd, 504).diff(504) / _sma(rnd.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_504d_v120_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 504).diff(504) / _sma(_ratio(capex + rnd, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_756d_v121_signal(revenue):
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_756d_v122_signal(capex):
    res = (_slope_pct(capex, 756).diff(756) / _sma(capex.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_756d_v123_signal(rnd):
    res = (_slope_pct(rnd, 756).diff(756) / _sma(rnd.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_756d_v124_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 756).diff(756) / _sma(_ratio(capex + rnd, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_1008d_v125_signal(revenue):
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_1008d_v126_signal(capex):
    res = (_slope_pct(capex, 1008).diff(1008) / _sma(capex.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_1008d_v127_signal(rnd):
    res = (_slope_pct(rnd, 1008).diff(1008) / _sma(rnd.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_1008d_v128_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 1008).diff(1008) / _sma(_ratio(capex + rnd, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_slope_diff_norm_1260d_v129_signal(revenue):
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_slope_diff_norm_1260d_v130_signal(capex):
    res = (_slope_pct(capex, 1260).diff(1260) / _sma(capex.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_slope_diff_norm_1260d_v131_signal(rnd):
    res = (_slope_pct(rnd, 1260).diff(1260) / _sma(rnd.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_slope_diff_norm_1260d_v132_signal(capex, rnd, revenue):
    res = (_slope_pct(_ratio(capex + rnd, revenue), 1260).diff(1260) / _sma(_ratio(capex + rnd, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_mom_z_5d_v133_signal(revenue):
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_mom_z_5d_v134_signal(capex):
    res = _z(_slope_pct(capex, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_mom_z_5d_v135_signal(rnd):
    res = _z(_slope_pct(rnd, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_mom_z_5d_v136_signal(capex, rnd, revenue):
    res = _z(_slope_pct(_ratio(capex + rnd, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_mom_z_10d_v137_signal(revenue):
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_mom_z_10d_v138_signal(capex):
    res = _z(_slope_pct(capex, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_mom_z_10d_v139_signal(rnd):
    res = _z(_slope_pct(rnd, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_mom_z_10d_v140_signal(capex, rnd, revenue):
    res = _z(_slope_pct(_ratio(capex + rnd, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_mom_z_21d_v141_signal(revenue):
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_mom_z_21d_v142_signal(capex):
    res = _z(_slope_pct(capex, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_mom_z_21d_v143_signal(rnd):
    res = _z(_slope_pct(rnd, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_mom_z_21d_v144_signal(capex, rnd, revenue):
    res = _z(_slope_pct(_ratio(capex + rnd, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_mom_z_42d_v145_signal(revenue):
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_mom_z_42d_v146_signal(capex):
    res = _z(_slope_pct(capex, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_rnd_mom_z_42d_v147_signal(rnd):
    res = _z(_slope_pct(rnd, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_green_capex_proxy_mom_z_42d_v148_signal(capex, rnd, revenue):
    res = _z(_slope_pct(_ratio(capex + rnd, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_revenue_mom_z_63d_v149_signal(revenue):
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f29_energy_mandates_capex_mom_z_63d_v150_signal(capex):
    res = _z(_slope_pct(capex, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum()
    })
    
    module = inspect.getmodule(inspect.currentframe())
    funcs = [obj for name, obj in inspect.getmembers(module) if (inspect.isfunction(obj) and name.startswith("f"))]
    print(f"Testing {len(funcs)} functions for family 29...")
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
