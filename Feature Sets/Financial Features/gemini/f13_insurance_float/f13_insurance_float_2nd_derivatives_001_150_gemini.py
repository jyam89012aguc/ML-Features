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

def f13_insurance_float_liabilitiesc_slope_pct_5d_v001_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 5d window."""
    res = _slope_pct(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_5d_v002_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_5d_v003_signal(netinc):
    """Percentage slope for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_5d_v004_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 5d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_10d_v005_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 10d window."""
    res = _slope_pct(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_10d_v006_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_10d_v007_signal(netinc):
    """Percentage slope for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_10d_v008_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 10d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_21d_v009_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 21d window."""
    res = _slope_pct(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_21d_v010_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_21d_v011_signal(netinc):
    """Percentage slope for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_21d_v012_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 21d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_42d_v013_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 42d window."""
    res = _slope_pct(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_42d_v014_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_42d_v015_signal(netinc):
    """Percentage slope for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_42d_v016_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 42d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_63d_v017_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 63d window."""
    res = _slope_pct(liabilitiesc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_63d_v018_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_63d_v019_signal(netinc):
    """Percentage slope for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_63d_v020_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 63d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_126d_v021_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 126d window."""
    res = _slope_pct(liabilitiesc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_126d_v022_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_126d_v023_signal(netinc):
    """Percentage slope for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_126d_v024_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 126d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_252d_v025_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 252d window."""
    res = _slope_pct(liabilitiesc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_252d_v026_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_252d_v027_signal(netinc):
    """Percentage slope for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_252d_v028_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 252d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_504d_v029_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 504d window."""
    res = _slope_pct(liabilitiesc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_504d_v030_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_504d_v031_signal(netinc):
    """Percentage slope for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_504d_v032_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 504d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_756d_v033_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 756d window."""
    res = _slope_pct(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_756d_v034_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_756d_v035_signal(netinc):
    """Percentage slope for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_756d_v036_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 756d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_1008d_v037_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 1008d window."""
    res = _slope_pct(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_1008d_v038_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_1008d_v039_signal(netinc):
    """Percentage slope for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_1008d_v040_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 1008d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_pct_1260d_v041_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 1260d window."""
    res = _slope_pct(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_pct_1260d_v042_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_pct_1260d_v043_signal(netinc):
    """Percentage slope for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_pct_1260d_v044_signal(liabilitiesc, assets):
    """Percentage slope for Float relative to total assets over 1260d window."""
    res = _slope_pct(_ratio(liabilitiesc, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_5d_v045_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 5d window."""
    res = _jerk(liabilitiesc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_5d_v046_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_5d_v047_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_5d_v048_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 5d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_10d_v049_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 10d window."""
    res = _jerk(liabilitiesc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_10d_v050_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_10d_v051_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_10d_v052_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 10d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_21d_v053_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 21d window."""
    res = _jerk(liabilitiesc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_21d_v054_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_21d_v055_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_21d_v056_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 21d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_42d_v057_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 42d window."""
    res = _jerk(liabilitiesc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_42d_v058_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_42d_v059_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_42d_v060_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 42d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_63d_v061_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 63d window."""
    res = _jerk(liabilitiesc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_63d_v062_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_63d_v063_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_63d_v064_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 63d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_126d_v065_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 126d window."""
    res = _jerk(liabilitiesc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_126d_v066_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_126d_v067_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_126d_v068_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 126d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_252d_v069_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 252d window."""
    res = _jerk(liabilitiesc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_252d_v070_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_252d_v071_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_252d_v072_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 252d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_504d_v073_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 504d window."""
    res = _jerk(liabilitiesc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_504d_v074_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_504d_v075_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_504d_v076_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 504d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_756d_v077_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 756d window."""
    res = _jerk(liabilitiesc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_756d_v078_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_756d_v079_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_756d_v080_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 756d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_1008d_v081_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 1008d window."""
    res = _jerk(liabilitiesc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_1008d_v082_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_1008d_v083_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_1008d_v084_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 1008d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_jerk_1260d_v085_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 1260d window."""
    res = _jerk(liabilitiesc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_jerk_1260d_v086_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_jerk_1260d_v087_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_jerk_1260d_v088_signal(liabilitiesc, assets):
    """Acceleration/Jerk for Float relative to total assets over 1260d window."""
    res = _jerk(_ratio(liabilitiesc, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_5d_v089_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 5d window."""
    res = (_slope_pct(liabilitiesc, 5).diff(5) / _sma(liabilitiesc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_5d_v090_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_5d_v091_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_5d_v092_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 5d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 5).diff(5) / _sma(_ratio(liabilitiesc, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_10d_v093_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 10d window."""
    res = (_slope_pct(liabilitiesc, 10).diff(10) / _sma(liabilitiesc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_10d_v094_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_10d_v095_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_10d_v096_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 10d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 10).diff(10) / _sma(_ratio(liabilitiesc, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_21d_v097_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 21d window."""
    res = (_slope_pct(liabilitiesc, 21).diff(21) / _sma(liabilitiesc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_21d_v098_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_21d_v099_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_21d_v100_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 21d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 21).diff(21) / _sma(_ratio(liabilitiesc, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_42d_v101_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 42d window."""
    res = (_slope_pct(liabilitiesc, 42).diff(42) / _sma(liabilitiesc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_42d_v102_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_42d_v103_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_42d_v104_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 42d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 42).diff(42) / _sma(_ratio(liabilitiesc, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_63d_v105_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 63d window."""
    res = (_slope_pct(liabilitiesc, 63).diff(63) / _sma(liabilitiesc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_63d_v106_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_63d_v107_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_63d_v108_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 63d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 63).diff(63) / _sma(_ratio(liabilitiesc, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_126d_v109_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 126d window."""
    res = (_slope_pct(liabilitiesc, 126).diff(126) / _sma(liabilitiesc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_126d_v110_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_126d_v111_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_126d_v112_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 126d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 126).diff(126) / _sma(_ratio(liabilitiesc, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_252d_v113_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 252d window."""
    res = (_slope_pct(liabilitiesc, 252).diff(252) / _sma(liabilitiesc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_252d_v114_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_252d_v115_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_252d_v116_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 252d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 252).diff(252) / _sma(_ratio(liabilitiesc, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_504d_v117_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 504d window."""
    res = (_slope_pct(liabilitiesc, 504).diff(504) / _sma(liabilitiesc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_504d_v118_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_504d_v119_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_504d_v120_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 504d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 504).diff(504) / _sma(_ratio(liabilitiesc, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_756d_v121_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 756d window."""
    res = (_slope_pct(liabilitiesc, 756).diff(756) / _sma(liabilitiesc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_756d_v122_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_756d_v123_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_756d_v124_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 756d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 756).diff(756) / _sma(_ratio(liabilitiesc, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_1008d_v125_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 1008d window."""
    res = (_slope_pct(liabilitiesc, 1008).diff(1008) / _sma(liabilitiesc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_1008d_v126_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_1008d_v127_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_1008d_v128_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 1008d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 1008).diff(1008) / _sma(_ratio(liabilitiesc, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_slope_diff_norm_1260d_v129_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 1260d window."""
    res = (_slope_pct(liabilitiesc, 1260).diff(1260) / _sma(liabilitiesc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_slope_diff_norm_1260d_v130_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_slope_diff_norm_1260d_v131_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_slope_diff_norm_1260d_v132_signal(liabilitiesc, assets):
    """Normalized slope change for Float relative to total assets over 1260d window."""
    res = (_slope_pct(_ratio(liabilitiesc, assets), 1260).diff(1260) / _sma(_ratio(liabilitiesc, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_mom_z_5d_v133_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 5d window."""
    res = _z(_slope_pct(liabilitiesc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_mom_z_5d_v134_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_mom_z_5d_v135_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_mom_z_5d_v136_signal(liabilitiesc, assets):
    """Relative momentum strength for Float relative to total assets over 5d window."""
    res = _z(_slope_pct(_ratio(liabilitiesc, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_mom_z_10d_v137_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 10d window."""
    res = _z(_slope_pct(liabilitiesc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_mom_z_10d_v138_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_mom_z_10d_v139_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_mom_z_10d_v140_signal(liabilitiesc, assets):
    """Relative momentum strength for Float relative to total assets over 10d window."""
    res = _z(_slope_pct(_ratio(liabilitiesc, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_mom_z_21d_v141_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 21d window."""
    res = _z(_slope_pct(liabilitiesc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_mom_z_21d_v142_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_mom_z_21d_v143_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_mom_z_21d_v144_signal(liabilitiesc, assets):
    """Relative momentum strength for Float relative to total assets over 21d window."""
    res = _z(_slope_pct(_ratio(liabilitiesc, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_mom_z_42d_v145_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 42d window."""
    res = _z(_slope_pct(liabilitiesc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_mom_z_42d_v146_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_netinc_mom_z_42d_v147_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_float_intensity_mom_z_42d_v148_signal(liabilitiesc, assets):
    """Relative momentum strength for Float relative to total assets over 42d window."""
    res = _z(_slope_pct(_ratio(liabilitiesc, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_liabilitiesc_mom_z_63d_v149_signal(liabilitiesc):
    """Relative momentum strength for Raw level of liabilitiesc over 63d window."""
    res = _z(_slope_pct(liabilitiesc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_insurance_float_assets_mom_z_63d_v150_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f13_insurance_float_liabilitiesc_slope_pct_5d_v001_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_5d_v001_signal},
    "f13_insurance_float_assets_slope_pct_5d_v002_signal": {"func": f13_insurance_float_assets_slope_pct_5d_v002_signal},
    "f13_insurance_float_netinc_slope_pct_5d_v003_signal": {"func": f13_insurance_float_netinc_slope_pct_5d_v003_signal},
    "f13_insurance_float_float_intensity_slope_pct_5d_v004_signal": {"func": f13_insurance_float_float_intensity_slope_pct_5d_v004_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_10d_v005_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_10d_v005_signal},
    "f13_insurance_float_assets_slope_pct_10d_v006_signal": {"func": f13_insurance_float_assets_slope_pct_10d_v006_signal},
    "f13_insurance_float_netinc_slope_pct_10d_v007_signal": {"func": f13_insurance_float_netinc_slope_pct_10d_v007_signal},
    "f13_insurance_float_float_intensity_slope_pct_10d_v008_signal": {"func": f13_insurance_float_float_intensity_slope_pct_10d_v008_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_21d_v009_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_21d_v009_signal},
    "f13_insurance_float_assets_slope_pct_21d_v010_signal": {"func": f13_insurance_float_assets_slope_pct_21d_v010_signal},
    "f13_insurance_float_netinc_slope_pct_21d_v011_signal": {"func": f13_insurance_float_netinc_slope_pct_21d_v011_signal},
    "f13_insurance_float_float_intensity_slope_pct_21d_v012_signal": {"func": f13_insurance_float_float_intensity_slope_pct_21d_v012_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_42d_v013_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_42d_v013_signal},
    "f13_insurance_float_assets_slope_pct_42d_v014_signal": {"func": f13_insurance_float_assets_slope_pct_42d_v014_signal},
    "f13_insurance_float_netinc_slope_pct_42d_v015_signal": {"func": f13_insurance_float_netinc_slope_pct_42d_v015_signal},
    "f13_insurance_float_float_intensity_slope_pct_42d_v016_signal": {"func": f13_insurance_float_float_intensity_slope_pct_42d_v016_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_63d_v017_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_63d_v017_signal},
    "f13_insurance_float_assets_slope_pct_63d_v018_signal": {"func": f13_insurance_float_assets_slope_pct_63d_v018_signal},
    "f13_insurance_float_netinc_slope_pct_63d_v019_signal": {"func": f13_insurance_float_netinc_slope_pct_63d_v019_signal},
    "f13_insurance_float_float_intensity_slope_pct_63d_v020_signal": {"func": f13_insurance_float_float_intensity_slope_pct_63d_v020_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_126d_v021_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_126d_v021_signal},
    "f13_insurance_float_assets_slope_pct_126d_v022_signal": {"func": f13_insurance_float_assets_slope_pct_126d_v022_signal},
    "f13_insurance_float_netinc_slope_pct_126d_v023_signal": {"func": f13_insurance_float_netinc_slope_pct_126d_v023_signal},
    "f13_insurance_float_float_intensity_slope_pct_126d_v024_signal": {"func": f13_insurance_float_float_intensity_slope_pct_126d_v024_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_252d_v025_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_252d_v025_signal},
    "f13_insurance_float_assets_slope_pct_252d_v026_signal": {"func": f13_insurance_float_assets_slope_pct_252d_v026_signal},
    "f13_insurance_float_netinc_slope_pct_252d_v027_signal": {"func": f13_insurance_float_netinc_slope_pct_252d_v027_signal},
    "f13_insurance_float_float_intensity_slope_pct_252d_v028_signal": {"func": f13_insurance_float_float_intensity_slope_pct_252d_v028_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_504d_v029_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_504d_v029_signal},
    "f13_insurance_float_assets_slope_pct_504d_v030_signal": {"func": f13_insurance_float_assets_slope_pct_504d_v030_signal},
    "f13_insurance_float_netinc_slope_pct_504d_v031_signal": {"func": f13_insurance_float_netinc_slope_pct_504d_v031_signal},
    "f13_insurance_float_float_intensity_slope_pct_504d_v032_signal": {"func": f13_insurance_float_float_intensity_slope_pct_504d_v032_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_756d_v033_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_756d_v033_signal},
    "f13_insurance_float_assets_slope_pct_756d_v034_signal": {"func": f13_insurance_float_assets_slope_pct_756d_v034_signal},
    "f13_insurance_float_netinc_slope_pct_756d_v035_signal": {"func": f13_insurance_float_netinc_slope_pct_756d_v035_signal},
    "f13_insurance_float_float_intensity_slope_pct_756d_v036_signal": {"func": f13_insurance_float_float_intensity_slope_pct_756d_v036_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_1008d_v037_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_1008d_v037_signal},
    "f13_insurance_float_assets_slope_pct_1008d_v038_signal": {"func": f13_insurance_float_assets_slope_pct_1008d_v038_signal},
    "f13_insurance_float_netinc_slope_pct_1008d_v039_signal": {"func": f13_insurance_float_netinc_slope_pct_1008d_v039_signal},
    "f13_insurance_float_float_intensity_slope_pct_1008d_v040_signal": {"func": f13_insurance_float_float_intensity_slope_pct_1008d_v040_signal},
    "f13_insurance_float_liabilitiesc_slope_pct_1260d_v041_signal": {"func": f13_insurance_float_liabilitiesc_slope_pct_1260d_v041_signal},
    "f13_insurance_float_assets_slope_pct_1260d_v042_signal": {"func": f13_insurance_float_assets_slope_pct_1260d_v042_signal},
    "f13_insurance_float_netinc_slope_pct_1260d_v043_signal": {"func": f13_insurance_float_netinc_slope_pct_1260d_v043_signal},
    "f13_insurance_float_float_intensity_slope_pct_1260d_v044_signal": {"func": f13_insurance_float_float_intensity_slope_pct_1260d_v044_signal},
    "f13_insurance_float_liabilitiesc_jerk_5d_v045_signal": {"func": f13_insurance_float_liabilitiesc_jerk_5d_v045_signal},
    "f13_insurance_float_assets_jerk_5d_v046_signal": {"func": f13_insurance_float_assets_jerk_5d_v046_signal},
    "f13_insurance_float_netinc_jerk_5d_v047_signal": {"func": f13_insurance_float_netinc_jerk_5d_v047_signal},
    "f13_insurance_float_float_intensity_jerk_5d_v048_signal": {"func": f13_insurance_float_float_intensity_jerk_5d_v048_signal},
    "f13_insurance_float_liabilitiesc_jerk_10d_v049_signal": {"func": f13_insurance_float_liabilitiesc_jerk_10d_v049_signal},
    "f13_insurance_float_assets_jerk_10d_v050_signal": {"func": f13_insurance_float_assets_jerk_10d_v050_signal},
    "f13_insurance_float_netinc_jerk_10d_v051_signal": {"func": f13_insurance_float_netinc_jerk_10d_v051_signal},
    "f13_insurance_float_float_intensity_jerk_10d_v052_signal": {"func": f13_insurance_float_float_intensity_jerk_10d_v052_signal},
    "f13_insurance_float_liabilitiesc_jerk_21d_v053_signal": {"func": f13_insurance_float_liabilitiesc_jerk_21d_v053_signal},
    "f13_insurance_float_assets_jerk_21d_v054_signal": {"func": f13_insurance_float_assets_jerk_21d_v054_signal},
    "f13_insurance_float_netinc_jerk_21d_v055_signal": {"func": f13_insurance_float_netinc_jerk_21d_v055_signal},
    "f13_insurance_float_float_intensity_jerk_21d_v056_signal": {"func": f13_insurance_float_float_intensity_jerk_21d_v056_signal},
    "f13_insurance_float_liabilitiesc_jerk_42d_v057_signal": {"func": f13_insurance_float_liabilitiesc_jerk_42d_v057_signal},
    "f13_insurance_float_assets_jerk_42d_v058_signal": {"func": f13_insurance_float_assets_jerk_42d_v058_signal},
    "f13_insurance_float_netinc_jerk_42d_v059_signal": {"func": f13_insurance_float_netinc_jerk_42d_v059_signal},
    "f13_insurance_float_float_intensity_jerk_42d_v060_signal": {"func": f13_insurance_float_float_intensity_jerk_42d_v060_signal},
    "f13_insurance_float_liabilitiesc_jerk_63d_v061_signal": {"func": f13_insurance_float_liabilitiesc_jerk_63d_v061_signal},
    "f13_insurance_float_assets_jerk_63d_v062_signal": {"func": f13_insurance_float_assets_jerk_63d_v062_signal},
    "f13_insurance_float_netinc_jerk_63d_v063_signal": {"func": f13_insurance_float_netinc_jerk_63d_v063_signal},
    "f13_insurance_float_float_intensity_jerk_63d_v064_signal": {"func": f13_insurance_float_float_intensity_jerk_63d_v064_signal},
    "f13_insurance_float_liabilitiesc_jerk_126d_v065_signal": {"func": f13_insurance_float_liabilitiesc_jerk_126d_v065_signal},
    "f13_insurance_float_assets_jerk_126d_v066_signal": {"func": f13_insurance_float_assets_jerk_126d_v066_signal},
    "f13_insurance_float_netinc_jerk_126d_v067_signal": {"func": f13_insurance_float_netinc_jerk_126d_v067_signal},
    "f13_insurance_float_float_intensity_jerk_126d_v068_signal": {"func": f13_insurance_float_float_intensity_jerk_126d_v068_signal},
    "f13_insurance_float_liabilitiesc_jerk_252d_v069_signal": {"func": f13_insurance_float_liabilitiesc_jerk_252d_v069_signal},
    "f13_insurance_float_assets_jerk_252d_v070_signal": {"func": f13_insurance_float_assets_jerk_252d_v070_signal},
    "f13_insurance_float_netinc_jerk_252d_v071_signal": {"func": f13_insurance_float_netinc_jerk_252d_v071_signal},
    "f13_insurance_float_float_intensity_jerk_252d_v072_signal": {"func": f13_insurance_float_float_intensity_jerk_252d_v072_signal},
    "f13_insurance_float_liabilitiesc_jerk_504d_v073_signal": {"func": f13_insurance_float_liabilitiesc_jerk_504d_v073_signal},
    "f13_insurance_float_assets_jerk_504d_v074_signal": {"func": f13_insurance_float_assets_jerk_504d_v074_signal},
    "f13_insurance_float_netinc_jerk_504d_v075_signal": {"func": f13_insurance_float_netinc_jerk_504d_v075_signal},
    "f13_insurance_float_float_intensity_jerk_504d_v076_signal": {"func": f13_insurance_float_float_intensity_jerk_504d_v076_signal},
    "f13_insurance_float_liabilitiesc_jerk_756d_v077_signal": {"func": f13_insurance_float_liabilitiesc_jerk_756d_v077_signal},
    "f13_insurance_float_assets_jerk_756d_v078_signal": {"func": f13_insurance_float_assets_jerk_756d_v078_signal},
    "f13_insurance_float_netinc_jerk_756d_v079_signal": {"func": f13_insurance_float_netinc_jerk_756d_v079_signal},
    "f13_insurance_float_float_intensity_jerk_756d_v080_signal": {"func": f13_insurance_float_float_intensity_jerk_756d_v080_signal},
    "f13_insurance_float_liabilitiesc_jerk_1008d_v081_signal": {"func": f13_insurance_float_liabilitiesc_jerk_1008d_v081_signal},
    "f13_insurance_float_assets_jerk_1008d_v082_signal": {"func": f13_insurance_float_assets_jerk_1008d_v082_signal},
    "f13_insurance_float_netinc_jerk_1008d_v083_signal": {"func": f13_insurance_float_netinc_jerk_1008d_v083_signal},
    "f13_insurance_float_float_intensity_jerk_1008d_v084_signal": {"func": f13_insurance_float_float_intensity_jerk_1008d_v084_signal},
    "f13_insurance_float_liabilitiesc_jerk_1260d_v085_signal": {"func": f13_insurance_float_liabilitiesc_jerk_1260d_v085_signal},
    "f13_insurance_float_assets_jerk_1260d_v086_signal": {"func": f13_insurance_float_assets_jerk_1260d_v086_signal},
    "f13_insurance_float_netinc_jerk_1260d_v087_signal": {"func": f13_insurance_float_netinc_jerk_1260d_v087_signal},
    "f13_insurance_float_float_intensity_jerk_1260d_v088_signal": {"func": f13_insurance_float_float_intensity_jerk_1260d_v088_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_5d_v089_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_5d_v089_signal},
    "f13_insurance_float_assets_slope_diff_norm_5d_v090_signal": {"func": f13_insurance_float_assets_slope_diff_norm_5d_v090_signal},
    "f13_insurance_float_netinc_slope_diff_norm_5d_v091_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_5d_v091_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_5d_v092_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_5d_v092_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_10d_v093_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_10d_v093_signal},
    "f13_insurance_float_assets_slope_diff_norm_10d_v094_signal": {"func": f13_insurance_float_assets_slope_diff_norm_10d_v094_signal},
    "f13_insurance_float_netinc_slope_diff_norm_10d_v095_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_10d_v095_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_10d_v096_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_10d_v096_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_21d_v097_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_21d_v097_signal},
    "f13_insurance_float_assets_slope_diff_norm_21d_v098_signal": {"func": f13_insurance_float_assets_slope_diff_norm_21d_v098_signal},
    "f13_insurance_float_netinc_slope_diff_norm_21d_v099_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_21d_v099_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_21d_v100_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_21d_v100_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_42d_v101_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_42d_v101_signal},
    "f13_insurance_float_assets_slope_diff_norm_42d_v102_signal": {"func": f13_insurance_float_assets_slope_diff_norm_42d_v102_signal},
    "f13_insurance_float_netinc_slope_diff_norm_42d_v103_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_42d_v103_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_42d_v104_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_42d_v104_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_63d_v105_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_63d_v105_signal},
    "f13_insurance_float_assets_slope_diff_norm_63d_v106_signal": {"func": f13_insurance_float_assets_slope_diff_norm_63d_v106_signal},
    "f13_insurance_float_netinc_slope_diff_norm_63d_v107_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_63d_v107_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_63d_v108_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_63d_v108_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_126d_v109_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_126d_v109_signal},
    "f13_insurance_float_assets_slope_diff_norm_126d_v110_signal": {"func": f13_insurance_float_assets_slope_diff_norm_126d_v110_signal},
    "f13_insurance_float_netinc_slope_diff_norm_126d_v111_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_126d_v111_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_126d_v112_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_126d_v112_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_252d_v113_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_252d_v113_signal},
    "f13_insurance_float_assets_slope_diff_norm_252d_v114_signal": {"func": f13_insurance_float_assets_slope_diff_norm_252d_v114_signal},
    "f13_insurance_float_netinc_slope_diff_norm_252d_v115_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_252d_v115_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_252d_v116_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_252d_v116_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_504d_v117_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_504d_v117_signal},
    "f13_insurance_float_assets_slope_diff_norm_504d_v118_signal": {"func": f13_insurance_float_assets_slope_diff_norm_504d_v118_signal},
    "f13_insurance_float_netinc_slope_diff_norm_504d_v119_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_504d_v119_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_504d_v120_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_504d_v120_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_756d_v121_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_756d_v121_signal},
    "f13_insurance_float_assets_slope_diff_norm_756d_v122_signal": {"func": f13_insurance_float_assets_slope_diff_norm_756d_v122_signal},
    "f13_insurance_float_netinc_slope_diff_norm_756d_v123_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_756d_v123_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_756d_v124_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_756d_v124_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_1008d_v125_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_1008d_v125_signal},
    "f13_insurance_float_assets_slope_diff_norm_1008d_v126_signal": {"func": f13_insurance_float_assets_slope_diff_norm_1008d_v126_signal},
    "f13_insurance_float_netinc_slope_diff_norm_1008d_v127_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_1008d_v127_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_1008d_v128_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_1008d_v128_signal},
    "f13_insurance_float_liabilitiesc_slope_diff_norm_1260d_v129_signal": {"func": f13_insurance_float_liabilitiesc_slope_diff_norm_1260d_v129_signal},
    "f13_insurance_float_assets_slope_diff_norm_1260d_v130_signal": {"func": f13_insurance_float_assets_slope_diff_norm_1260d_v130_signal},
    "f13_insurance_float_netinc_slope_diff_norm_1260d_v131_signal": {"func": f13_insurance_float_netinc_slope_diff_norm_1260d_v131_signal},
    "f13_insurance_float_float_intensity_slope_diff_norm_1260d_v132_signal": {"func": f13_insurance_float_float_intensity_slope_diff_norm_1260d_v132_signal},
    "f13_insurance_float_liabilitiesc_mom_z_5d_v133_signal": {"func": f13_insurance_float_liabilitiesc_mom_z_5d_v133_signal},
    "f13_insurance_float_assets_mom_z_5d_v134_signal": {"func": f13_insurance_float_assets_mom_z_5d_v134_signal},
    "f13_insurance_float_netinc_mom_z_5d_v135_signal": {"func": f13_insurance_float_netinc_mom_z_5d_v135_signal},
    "f13_insurance_float_float_intensity_mom_z_5d_v136_signal": {"func": f13_insurance_float_float_intensity_mom_z_5d_v136_signal},
    "f13_insurance_float_liabilitiesc_mom_z_10d_v137_signal": {"func": f13_insurance_float_liabilitiesc_mom_z_10d_v137_signal},
    "f13_insurance_float_assets_mom_z_10d_v138_signal": {"func": f13_insurance_float_assets_mom_z_10d_v138_signal},
    "f13_insurance_float_netinc_mom_z_10d_v139_signal": {"func": f13_insurance_float_netinc_mom_z_10d_v139_signal},
    "f13_insurance_float_float_intensity_mom_z_10d_v140_signal": {"func": f13_insurance_float_float_intensity_mom_z_10d_v140_signal},
    "f13_insurance_float_liabilitiesc_mom_z_21d_v141_signal": {"func": f13_insurance_float_liabilitiesc_mom_z_21d_v141_signal},
    "f13_insurance_float_assets_mom_z_21d_v142_signal": {"func": f13_insurance_float_assets_mom_z_21d_v142_signal},
    "f13_insurance_float_netinc_mom_z_21d_v143_signal": {"func": f13_insurance_float_netinc_mom_z_21d_v143_signal},
    "f13_insurance_float_float_intensity_mom_z_21d_v144_signal": {"func": f13_insurance_float_float_intensity_mom_z_21d_v144_signal},
    "f13_insurance_float_liabilitiesc_mom_z_42d_v145_signal": {"func": f13_insurance_float_liabilitiesc_mom_z_42d_v145_signal},
    "f13_insurance_float_assets_mom_z_42d_v146_signal": {"func": f13_insurance_float_assets_mom_z_42d_v146_signal},
    "f13_insurance_float_netinc_mom_z_42d_v147_signal": {"func": f13_insurance_float_netinc_mom_z_42d_v147_signal},
    "f13_insurance_float_float_intensity_mom_z_42d_v148_signal": {"func": f13_insurance_float_float_intensity_mom_z_42d_v148_signal},
    "f13_insurance_float_liabilitiesc_mom_z_63d_v149_signal": {"func": f13_insurance_float_liabilitiesc_mom_z_63d_v149_signal},
    "f13_insurance_float_assets_mom_z_63d_v150_signal": {"func": f13_insurance_float_assets_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 13...")
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
