import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
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

def f30_curve_sensitivity_ebit_slope_pct_5d_v001_signal(ebit):
    """Percentage slope for Raw level of ebit over 5d window."""
    res = _slope_pct(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_5d_v002_signal(netinc):
    """Percentage slope for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_5d_v003_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_5d_v004_signal(ebit, assets):
    """Percentage slope for Operating ROA over 5d window."""
    res = _slope_pct(_ratio(ebit, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_10d_v005_signal(ebit):
    """Percentage slope for Raw level of ebit over 10d window."""
    res = _slope_pct(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_10d_v006_signal(netinc):
    """Percentage slope for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_10d_v007_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_10d_v008_signal(ebit, assets):
    """Percentage slope for Operating ROA over 10d window."""
    res = _slope_pct(_ratio(ebit, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_21d_v009_signal(ebit):
    """Percentage slope for Raw level of ebit over 21d window."""
    res = _slope_pct(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_21d_v010_signal(netinc):
    """Percentage slope for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_21d_v011_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_21d_v012_signal(ebit, assets):
    """Percentage slope for Operating ROA over 21d window."""
    res = _slope_pct(_ratio(ebit, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_42d_v013_signal(ebit):
    """Percentage slope for Raw level of ebit over 42d window."""
    res = _slope_pct(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_42d_v014_signal(netinc):
    """Percentage slope for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_42d_v015_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_42d_v016_signal(ebit, assets):
    """Percentage slope for Operating ROA over 42d window."""
    res = _slope_pct(_ratio(ebit, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_63d_v017_signal(ebit):
    """Percentage slope for Raw level of ebit over 63d window."""
    res = _slope_pct(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_63d_v018_signal(netinc):
    """Percentage slope for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_63d_v019_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_63d_v020_signal(ebit, assets):
    """Percentage slope for Operating ROA over 63d window."""
    res = _slope_pct(_ratio(ebit, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_126d_v021_signal(ebit):
    """Percentage slope for Raw level of ebit over 126d window."""
    res = _slope_pct(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_126d_v022_signal(netinc):
    """Percentage slope for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_126d_v023_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_126d_v024_signal(ebit, assets):
    """Percentage slope for Operating ROA over 126d window."""
    res = _slope_pct(_ratio(ebit, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_252d_v025_signal(ebit):
    """Percentage slope for Raw level of ebit over 252d window."""
    res = _slope_pct(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_252d_v026_signal(netinc):
    """Percentage slope for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_252d_v027_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_252d_v028_signal(ebit, assets):
    """Percentage slope for Operating ROA over 252d window."""
    res = _slope_pct(_ratio(ebit, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_504d_v029_signal(ebit):
    """Percentage slope for Raw level of ebit over 504d window."""
    res = _slope_pct(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_504d_v030_signal(netinc):
    """Percentage slope for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_504d_v031_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_504d_v032_signal(ebit, assets):
    """Percentage slope for Operating ROA over 504d window."""
    res = _slope_pct(_ratio(ebit, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_756d_v033_signal(ebit):
    """Percentage slope for Raw level of ebit over 756d window."""
    res = _slope_pct(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_756d_v034_signal(netinc):
    """Percentage slope for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_756d_v035_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_756d_v036_signal(ebit, assets):
    """Percentage slope for Operating ROA over 756d window."""
    res = _slope_pct(_ratio(ebit, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_1008d_v037_signal(ebit):
    """Percentage slope for Raw level of ebit over 1008d window."""
    res = _slope_pct(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_1008d_v038_signal(netinc):
    """Percentage slope for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_1008d_v039_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_1008d_v040_signal(ebit, assets):
    """Percentage slope for Operating ROA over 1008d window."""
    res = _slope_pct(_ratio(ebit, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_pct_1260d_v041_signal(ebit):
    """Percentage slope for Raw level of ebit over 1260d window."""
    res = _slope_pct(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_pct_1260d_v042_signal(netinc):
    """Percentage slope for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_pct_1260d_v043_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_pct_1260d_v044_signal(ebit, assets):
    """Percentage slope for Operating ROA over 1260d window."""
    res = _slope_pct(_ratio(ebit, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_5d_v045_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 5d window."""
    res = _jerk(ebit, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_5d_v046_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_5d_v047_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_5d_v048_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 5d window."""
    res = _jerk(_ratio(ebit, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_10d_v049_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 10d window."""
    res = _jerk(ebit, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_10d_v050_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_10d_v051_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_10d_v052_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 10d window."""
    res = _jerk(_ratio(ebit, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_21d_v053_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 21d window."""
    res = _jerk(ebit, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_21d_v054_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_21d_v055_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_21d_v056_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 21d window."""
    res = _jerk(_ratio(ebit, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_42d_v057_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 42d window."""
    res = _jerk(ebit, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_42d_v058_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_42d_v059_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_42d_v060_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 42d window."""
    res = _jerk(_ratio(ebit, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_63d_v061_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 63d window."""
    res = _jerk(ebit, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_63d_v062_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_63d_v063_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_63d_v064_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 63d window."""
    res = _jerk(_ratio(ebit, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_126d_v065_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 126d window."""
    res = _jerk(ebit, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_126d_v066_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_126d_v067_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_126d_v068_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 126d window."""
    res = _jerk(_ratio(ebit, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_252d_v069_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 252d window."""
    res = _jerk(ebit, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_252d_v070_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_252d_v071_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_252d_v072_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 252d window."""
    res = _jerk(_ratio(ebit, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_504d_v073_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 504d window."""
    res = _jerk(ebit, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_504d_v074_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_504d_v075_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_504d_v076_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 504d window."""
    res = _jerk(_ratio(ebit, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_756d_v077_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 756d window."""
    res = _jerk(ebit, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_756d_v078_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_756d_v079_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_756d_v080_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 756d window."""
    res = _jerk(_ratio(ebit, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_1008d_v081_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 1008d window."""
    res = _jerk(ebit, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_1008d_v082_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_1008d_v083_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_1008d_v084_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 1008d window."""
    res = _jerk(_ratio(ebit, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_jerk_1260d_v085_signal(ebit):
    """Acceleration/Jerk for Raw level of ebit over 1260d window."""
    res = _jerk(ebit, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_jerk_1260d_v086_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_jerk_1260d_v087_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_jerk_1260d_v088_signal(ebit, assets):
    """Acceleration/Jerk for Operating ROA over 1260d window."""
    res = _jerk(_ratio(ebit, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_5d_v089_signal(ebit):
    """Normalized slope change for Raw level of ebit over 5d window."""
    res = (_slope_pct(ebit, 5).diff(5) / _sma(ebit.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_5d_v090_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_5d_v091_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_5d_v092_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 5d window."""
    res = (_slope_pct(_ratio(ebit, assets), 5).diff(5) / _sma(_ratio(ebit, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_10d_v093_signal(ebit):
    """Normalized slope change for Raw level of ebit over 10d window."""
    res = (_slope_pct(ebit, 10).diff(10) / _sma(ebit.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_10d_v094_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_10d_v095_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_10d_v096_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 10d window."""
    res = (_slope_pct(_ratio(ebit, assets), 10).diff(10) / _sma(_ratio(ebit, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_21d_v097_signal(ebit):
    """Normalized slope change for Raw level of ebit over 21d window."""
    res = (_slope_pct(ebit, 21).diff(21) / _sma(ebit.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_21d_v098_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_21d_v099_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_21d_v100_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 21d window."""
    res = (_slope_pct(_ratio(ebit, assets), 21).diff(21) / _sma(_ratio(ebit, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_42d_v101_signal(ebit):
    """Normalized slope change for Raw level of ebit over 42d window."""
    res = (_slope_pct(ebit, 42).diff(42) / _sma(ebit.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_42d_v102_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_42d_v103_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_42d_v104_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 42d window."""
    res = (_slope_pct(_ratio(ebit, assets), 42).diff(42) / _sma(_ratio(ebit, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_63d_v105_signal(ebit):
    """Normalized slope change for Raw level of ebit over 63d window."""
    res = (_slope_pct(ebit, 63).diff(63) / _sma(ebit.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_63d_v106_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_63d_v107_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_63d_v108_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 63d window."""
    res = (_slope_pct(_ratio(ebit, assets), 63).diff(63) / _sma(_ratio(ebit, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_126d_v109_signal(ebit):
    """Normalized slope change for Raw level of ebit over 126d window."""
    res = (_slope_pct(ebit, 126).diff(126) / _sma(ebit.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_126d_v110_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_126d_v111_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_126d_v112_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 126d window."""
    res = (_slope_pct(_ratio(ebit, assets), 126).diff(126) / _sma(_ratio(ebit, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_252d_v113_signal(ebit):
    """Normalized slope change for Raw level of ebit over 252d window."""
    res = (_slope_pct(ebit, 252).diff(252) / _sma(ebit.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_252d_v114_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_252d_v115_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_252d_v116_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 252d window."""
    res = (_slope_pct(_ratio(ebit, assets), 252).diff(252) / _sma(_ratio(ebit, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_504d_v117_signal(ebit):
    """Normalized slope change for Raw level of ebit over 504d window."""
    res = (_slope_pct(ebit, 504).diff(504) / _sma(ebit.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_504d_v118_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_504d_v119_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_504d_v120_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 504d window."""
    res = (_slope_pct(_ratio(ebit, assets), 504).diff(504) / _sma(_ratio(ebit, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_756d_v121_signal(ebit):
    """Normalized slope change for Raw level of ebit over 756d window."""
    res = (_slope_pct(ebit, 756).diff(756) / _sma(ebit.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_756d_v122_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_756d_v123_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_756d_v124_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 756d window."""
    res = (_slope_pct(_ratio(ebit, assets), 756).diff(756) / _sma(_ratio(ebit, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_1008d_v125_signal(ebit):
    """Normalized slope change for Raw level of ebit over 1008d window."""
    res = (_slope_pct(ebit, 1008).diff(1008) / _sma(ebit.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_1008d_v126_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_1008d_v127_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_1008d_v128_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 1008d window."""
    res = (_slope_pct(_ratio(ebit, assets), 1008).diff(1008) / _sma(_ratio(ebit, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_slope_diff_norm_1260d_v129_signal(ebit):
    """Normalized slope change for Raw level of ebit over 1260d window."""
    res = (_slope_pct(ebit, 1260).diff(1260) / _sma(ebit.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_slope_diff_norm_1260d_v130_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_slope_diff_norm_1260d_v131_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_slope_diff_norm_1260d_v132_signal(ebit, assets):
    """Normalized slope change for Operating ROA over 1260d window."""
    res = (_slope_pct(_ratio(ebit, assets), 1260).diff(1260) / _sma(_ratio(ebit, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_mom_z_5d_v133_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 5d window."""
    res = _z(_slope_pct(ebit, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_mom_z_5d_v134_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_mom_z_5d_v135_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_mom_z_5d_v136_signal(ebit, assets):
    """Relative momentum strength for Operating ROA over 5d window."""
    res = _z(_slope_pct(_ratio(ebit, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_mom_z_10d_v137_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 10d window."""
    res = _z(_slope_pct(ebit, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_mom_z_10d_v138_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_mom_z_10d_v139_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_mom_z_10d_v140_signal(ebit, assets):
    """Relative momentum strength for Operating ROA over 10d window."""
    res = _z(_slope_pct(_ratio(ebit, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_mom_z_21d_v141_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 21d window."""
    res = _z(_slope_pct(ebit, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_mom_z_21d_v142_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_mom_z_21d_v143_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_mom_z_21d_v144_signal(ebit, assets):
    """Relative momentum strength for Operating ROA over 21d window."""
    res = _z(_slope_pct(_ratio(ebit, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_mom_z_42d_v145_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 42d window."""
    res = _z(_slope_pct(ebit, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_mom_z_42d_v146_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_assets_mom_z_42d_v147_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_conversion_roa_mom_z_42d_v148_signal(ebit, assets):
    """Relative momentum strength for Operating ROA over 42d window."""
    res = _z(_slope_pct(_ratio(ebit, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_ebit_mom_z_63d_v149_signal(ebit):
    """Relative momentum strength for Raw level of ebit over 63d window."""
    res = _z(_slope_pct(ebit, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f30_curve_sensitivity_netinc_mom_z_63d_v150_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f30_curve_sensitivity_ebit_slope_pct_5d_v001_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_5d_v001_signal},
    "f30_curve_sensitivity_netinc_slope_pct_5d_v002_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_5d_v002_signal},
    "f30_curve_sensitivity_assets_slope_pct_5d_v003_signal": {"func": f30_curve_sensitivity_assets_slope_pct_5d_v003_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_5d_v004_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_5d_v004_signal},
    "f30_curve_sensitivity_ebit_slope_pct_10d_v005_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_10d_v005_signal},
    "f30_curve_sensitivity_netinc_slope_pct_10d_v006_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_10d_v006_signal},
    "f30_curve_sensitivity_assets_slope_pct_10d_v007_signal": {"func": f30_curve_sensitivity_assets_slope_pct_10d_v007_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_10d_v008_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_10d_v008_signal},
    "f30_curve_sensitivity_ebit_slope_pct_21d_v009_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_21d_v009_signal},
    "f30_curve_sensitivity_netinc_slope_pct_21d_v010_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_21d_v010_signal},
    "f30_curve_sensitivity_assets_slope_pct_21d_v011_signal": {"func": f30_curve_sensitivity_assets_slope_pct_21d_v011_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_21d_v012_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_21d_v012_signal},
    "f30_curve_sensitivity_ebit_slope_pct_42d_v013_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_42d_v013_signal},
    "f30_curve_sensitivity_netinc_slope_pct_42d_v014_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_42d_v014_signal},
    "f30_curve_sensitivity_assets_slope_pct_42d_v015_signal": {"func": f30_curve_sensitivity_assets_slope_pct_42d_v015_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_42d_v016_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_42d_v016_signal},
    "f30_curve_sensitivity_ebit_slope_pct_63d_v017_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_63d_v017_signal},
    "f30_curve_sensitivity_netinc_slope_pct_63d_v018_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_63d_v018_signal},
    "f30_curve_sensitivity_assets_slope_pct_63d_v019_signal": {"func": f30_curve_sensitivity_assets_slope_pct_63d_v019_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_63d_v020_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_63d_v020_signal},
    "f30_curve_sensitivity_ebit_slope_pct_126d_v021_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_126d_v021_signal},
    "f30_curve_sensitivity_netinc_slope_pct_126d_v022_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_126d_v022_signal},
    "f30_curve_sensitivity_assets_slope_pct_126d_v023_signal": {"func": f30_curve_sensitivity_assets_slope_pct_126d_v023_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_126d_v024_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_126d_v024_signal},
    "f30_curve_sensitivity_ebit_slope_pct_252d_v025_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_252d_v025_signal},
    "f30_curve_sensitivity_netinc_slope_pct_252d_v026_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_252d_v026_signal},
    "f30_curve_sensitivity_assets_slope_pct_252d_v027_signal": {"func": f30_curve_sensitivity_assets_slope_pct_252d_v027_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_252d_v028_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_252d_v028_signal},
    "f30_curve_sensitivity_ebit_slope_pct_504d_v029_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_504d_v029_signal},
    "f30_curve_sensitivity_netinc_slope_pct_504d_v030_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_504d_v030_signal},
    "f30_curve_sensitivity_assets_slope_pct_504d_v031_signal": {"func": f30_curve_sensitivity_assets_slope_pct_504d_v031_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_504d_v032_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_504d_v032_signal},
    "f30_curve_sensitivity_ebit_slope_pct_756d_v033_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_756d_v033_signal},
    "f30_curve_sensitivity_netinc_slope_pct_756d_v034_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_756d_v034_signal},
    "f30_curve_sensitivity_assets_slope_pct_756d_v035_signal": {"func": f30_curve_sensitivity_assets_slope_pct_756d_v035_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_756d_v036_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_756d_v036_signal},
    "f30_curve_sensitivity_ebit_slope_pct_1008d_v037_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_1008d_v037_signal},
    "f30_curve_sensitivity_netinc_slope_pct_1008d_v038_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_1008d_v038_signal},
    "f30_curve_sensitivity_assets_slope_pct_1008d_v039_signal": {"func": f30_curve_sensitivity_assets_slope_pct_1008d_v039_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_1008d_v040_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_1008d_v040_signal},
    "f30_curve_sensitivity_ebit_slope_pct_1260d_v041_signal": {"func": f30_curve_sensitivity_ebit_slope_pct_1260d_v041_signal},
    "f30_curve_sensitivity_netinc_slope_pct_1260d_v042_signal": {"func": f30_curve_sensitivity_netinc_slope_pct_1260d_v042_signal},
    "f30_curve_sensitivity_assets_slope_pct_1260d_v043_signal": {"func": f30_curve_sensitivity_assets_slope_pct_1260d_v043_signal},
    "f30_curve_sensitivity_conversion_roa_slope_pct_1260d_v044_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_pct_1260d_v044_signal},
    "f30_curve_sensitivity_ebit_jerk_5d_v045_signal": {"func": f30_curve_sensitivity_ebit_jerk_5d_v045_signal},
    "f30_curve_sensitivity_netinc_jerk_5d_v046_signal": {"func": f30_curve_sensitivity_netinc_jerk_5d_v046_signal},
    "f30_curve_sensitivity_assets_jerk_5d_v047_signal": {"func": f30_curve_sensitivity_assets_jerk_5d_v047_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_5d_v048_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_5d_v048_signal},
    "f30_curve_sensitivity_ebit_jerk_10d_v049_signal": {"func": f30_curve_sensitivity_ebit_jerk_10d_v049_signal},
    "f30_curve_sensitivity_netinc_jerk_10d_v050_signal": {"func": f30_curve_sensitivity_netinc_jerk_10d_v050_signal},
    "f30_curve_sensitivity_assets_jerk_10d_v051_signal": {"func": f30_curve_sensitivity_assets_jerk_10d_v051_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_10d_v052_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_10d_v052_signal},
    "f30_curve_sensitivity_ebit_jerk_21d_v053_signal": {"func": f30_curve_sensitivity_ebit_jerk_21d_v053_signal},
    "f30_curve_sensitivity_netinc_jerk_21d_v054_signal": {"func": f30_curve_sensitivity_netinc_jerk_21d_v054_signal},
    "f30_curve_sensitivity_assets_jerk_21d_v055_signal": {"func": f30_curve_sensitivity_assets_jerk_21d_v055_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_21d_v056_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_21d_v056_signal},
    "f30_curve_sensitivity_ebit_jerk_42d_v057_signal": {"func": f30_curve_sensitivity_ebit_jerk_42d_v057_signal},
    "f30_curve_sensitivity_netinc_jerk_42d_v058_signal": {"func": f30_curve_sensitivity_netinc_jerk_42d_v058_signal},
    "f30_curve_sensitivity_assets_jerk_42d_v059_signal": {"func": f30_curve_sensitivity_assets_jerk_42d_v059_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_42d_v060_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_42d_v060_signal},
    "f30_curve_sensitivity_ebit_jerk_63d_v061_signal": {"func": f30_curve_sensitivity_ebit_jerk_63d_v061_signal},
    "f30_curve_sensitivity_netinc_jerk_63d_v062_signal": {"func": f30_curve_sensitivity_netinc_jerk_63d_v062_signal},
    "f30_curve_sensitivity_assets_jerk_63d_v063_signal": {"func": f30_curve_sensitivity_assets_jerk_63d_v063_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_63d_v064_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_63d_v064_signal},
    "f30_curve_sensitivity_ebit_jerk_126d_v065_signal": {"func": f30_curve_sensitivity_ebit_jerk_126d_v065_signal},
    "f30_curve_sensitivity_netinc_jerk_126d_v066_signal": {"func": f30_curve_sensitivity_netinc_jerk_126d_v066_signal},
    "f30_curve_sensitivity_assets_jerk_126d_v067_signal": {"func": f30_curve_sensitivity_assets_jerk_126d_v067_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_126d_v068_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_126d_v068_signal},
    "f30_curve_sensitivity_ebit_jerk_252d_v069_signal": {"func": f30_curve_sensitivity_ebit_jerk_252d_v069_signal},
    "f30_curve_sensitivity_netinc_jerk_252d_v070_signal": {"func": f30_curve_sensitivity_netinc_jerk_252d_v070_signal},
    "f30_curve_sensitivity_assets_jerk_252d_v071_signal": {"func": f30_curve_sensitivity_assets_jerk_252d_v071_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_252d_v072_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_252d_v072_signal},
    "f30_curve_sensitivity_ebit_jerk_504d_v073_signal": {"func": f30_curve_sensitivity_ebit_jerk_504d_v073_signal},
    "f30_curve_sensitivity_netinc_jerk_504d_v074_signal": {"func": f30_curve_sensitivity_netinc_jerk_504d_v074_signal},
    "f30_curve_sensitivity_assets_jerk_504d_v075_signal": {"func": f30_curve_sensitivity_assets_jerk_504d_v075_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_504d_v076_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_504d_v076_signal},
    "f30_curve_sensitivity_ebit_jerk_756d_v077_signal": {"func": f30_curve_sensitivity_ebit_jerk_756d_v077_signal},
    "f30_curve_sensitivity_netinc_jerk_756d_v078_signal": {"func": f30_curve_sensitivity_netinc_jerk_756d_v078_signal},
    "f30_curve_sensitivity_assets_jerk_756d_v079_signal": {"func": f30_curve_sensitivity_assets_jerk_756d_v079_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_756d_v080_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_756d_v080_signal},
    "f30_curve_sensitivity_ebit_jerk_1008d_v081_signal": {"func": f30_curve_sensitivity_ebit_jerk_1008d_v081_signal},
    "f30_curve_sensitivity_netinc_jerk_1008d_v082_signal": {"func": f30_curve_sensitivity_netinc_jerk_1008d_v082_signal},
    "f30_curve_sensitivity_assets_jerk_1008d_v083_signal": {"func": f30_curve_sensitivity_assets_jerk_1008d_v083_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_1008d_v084_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_1008d_v084_signal},
    "f30_curve_sensitivity_ebit_jerk_1260d_v085_signal": {"func": f30_curve_sensitivity_ebit_jerk_1260d_v085_signal},
    "f30_curve_sensitivity_netinc_jerk_1260d_v086_signal": {"func": f30_curve_sensitivity_netinc_jerk_1260d_v086_signal},
    "f30_curve_sensitivity_assets_jerk_1260d_v087_signal": {"func": f30_curve_sensitivity_assets_jerk_1260d_v087_signal},
    "f30_curve_sensitivity_conversion_roa_jerk_1260d_v088_signal": {"func": f30_curve_sensitivity_conversion_roa_jerk_1260d_v088_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_5d_v089_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_5d_v089_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_5d_v090_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_5d_v090_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_5d_v091_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_5d_v091_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_5d_v092_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_5d_v092_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_10d_v093_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_10d_v093_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_10d_v094_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_10d_v094_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_10d_v095_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_10d_v095_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_10d_v096_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_10d_v096_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_21d_v097_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_21d_v097_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_21d_v098_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_21d_v098_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_21d_v099_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_21d_v099_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_21d_v100_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_21d_v100_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_42d_v101_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_42d_v101_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_42d_v102_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_42d_v102_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_42d_v103_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_42d_v103_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_42d_v104_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_42d_v104_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_63d_v105_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_63d_v105_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_63d_v106_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_63d_v106_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_63d_v107_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_63d_v107_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_63d_v108_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_63d_v108_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_126d_v109_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_126d_v109_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_126d_v110_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_126d_v110_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_126d_v111_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_126d_v111_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_126d_v112_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_126d_v112_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_252d_v113_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_252d_v113_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_252d_v114_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_252d_v114_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_252d_v115_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_252d_v115_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_252d_v116_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_252d_v116_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_504d_v117_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_504d_v117_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_504d_v118_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_504d_v118_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_504d_v119_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_504d_v119_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_504d_v120_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_504d_v120_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_756d_v121_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_756d_v121_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_756d_v122_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_756d_v122_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_756d_v123_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_756d_v123_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_756d_v124_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_756d_v124_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_1008d_v125_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_1008d_v125_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_1008d_v126_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_1008d_v126_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_1008d_v127_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_1008d_v127_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_1008d_v128_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_1008d_v128_signal},
    "f30_curve_sensitivity_ebit_slope_diff_norm_1260d_v129_signal": {"func": f30_curve_sensitivity_ebit_slope_diff_norm_1260d_v129_signal},
    "f30_curve_sensitivity_netinc_slope_diff_norm_1260d_v130_signal": {"func": f30_curve_sensitivity_netinc_slope_diff_norm_1260d_v130_signal},
    "f30_curve_sensitivity_assets_slope_diff_norm_1260d_v131_signal": {"func": f30_curve_sensitivity_assets_slope_diff_norm_1260d_v131_signal},
    "f30_curve_sensitivity_conversion_roa_slope_diff_norm_1260d_v132_signal": {"func": f30_curve_sensitivity_conversion_roa_slope_diff_norm_1260d_v132_signal},
    "f30_curve_sensitivity_ebit_mom_z_5d_v133_signal": {"func": f30_curve_sensitivity_ebit_mom_z_5d_v133_signal},
    "f30_curve_sensitivity_netinc_mom_z_5d_v134_signal": {"func": f30_curve_sensitivity_netinc_mom_z_5d_v134_signal},
    "f30_curve_sensitivity_assets_mom_z_5d_v135_signal": {"func": f30_curve_sensitivity_assets_mom_z_5d_v135_signal},
    "f30_curve_sensitivity_conversion_roa_mom_z_5d_v136_signal": {"func": f30_curve_sensitivity_conversion_roa_mom_z_5d_v136_signal},
    "f30_curve_sensitivity_ebit_mom_z_10d_v137_signal": {"func": f30_curve_sensitivity_ebit_mom_z_10d_v137_signal},
    "f30_curve_sensitivity_netinc_mom_z_10d_v138_signal": {"func": f30_curve_sensitivity_netinc_mom_z_10d_v138_signal},
    "f30_curve_sensitivity_assets_mom_z_10d_v139_signal": {"func": f30_curve_sensitivity_assets_mom_z_10d_v139_signal},
    "f30_curve_sensitivity_conversion_roa_mom_z_10d_v140_signal": {"func": f30_curve_sensitivity_conversion_roa_mom_z_10d_v140_signal},
    "f30_curve_sensitivity_ebit_mom_z_21d_v141_signal": {"func": f30_curve_sensitivity_ebit_mom_z_21d_v141_signal},
    "f30_curve_sensitivity_netinc_mom_z_21d_v142_signal": {"func": f30_curve_sensitivity_netinc_mom_z_21d_v142_signal},
    "f30_curve_sensitivity_assets_mom_z_21d_v143_signal": {"func": f30_curve_sensitivity_assets_mom_z_21d_v143_signal},
    "f30_curve_sensitivity_conversion_roa_mom_z_21d_v144_signal": {"func": f30_curve_sensitivity_conversion_roa_mom_z_21d_v144_signal},
    "f30_curve_sensitivity_ebit_mom_z_42d_v145_signal": {"func": f30_curve_sensitivity_ebit_mom_z_42d_v145_signal},
    "f30_curve_sensitivity_netinc_mom_z_42d_v146_signal": {"func": f30_curve_sensitivity_netinc_mom_z_42d_v146_signal},
    "f30_curve_sensitivity_assets_mom_z_42d_v147_signal": {"func": f30_curve_sensitivity_assets_mom_z_42d_v147_signal},
    "f30_curve_sensitivity_conversion_roa_mom_z_42d_v148_signal": {"func": f30_curve_sensitivity_conversion_roa_mom_z_42d_v148_signal},
    "f30_curve_sensitivity_ebit_mom_z_63d_v149_signal": {"func": f30_curve_sensitivity_ebit_mom_z_63d_v149_signal},
    "f30_curve_sensitivity_netinc_mom_z_63d_v150_signal": {"func": f30_curve_sensitivity_netinc_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 30...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
