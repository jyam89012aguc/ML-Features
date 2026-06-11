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

def f49_asset_light_moat_fin_netinc_slope_pct_5d_v001_signal(netinc):
    """Percentage slope for Raw level of netinc over 5d window."""
    res = _slope_pct(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_5d_v002_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_5d_v003_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 5d window."""
    res = _slope_pct(tangibles, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_5d_v004_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 5d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_10d_v005_signal(netinc):
    """Percentage slope for Raw level of netinc over 10d window."""
    res = _slope_pct(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_10d_v006_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_10d_v007_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 10d window."""
    res = _slope_pct(tangibles, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_10d_v008_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 10d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_21d_v009_signal(netinc):
    """Percentage slope for Raw level of netinc over 21d window."""
    res = _slope_pct(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_21d_v010_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_21d_v011_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 21d window."""
    res = _slope_pct(tangibles, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_21d_v012_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 21d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_42d_v013_signal(netinc):
    """Percentage slope for Raw level of netinc over 42d window."""
    res = _slope_pct(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_42d_v014_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_42d_v015_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 42d window."""
    res = _slope_pct(tangibles, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_42d_v016_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 42d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_63d_v017_signal(netinc):
    """Percentage slope for Raw level of netinc over 63d window."""
    res = _slope_pct(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_63d_v018_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_63d_v019_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 63d window."""
    res = _slope_pct(tangibles, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_63d_v020_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 63d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_126d_v021_signal(netinc):
    """Percentage slope for Raw level of netinc over 126d window."""
    res = _slope_pct(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_126d_v022_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_126d_v023_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 126d window."""
    res = _slope_pct(tangibles, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_126d_v024_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 126d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_252d_v025_signal(netinc):
    """Percentage slope for Raw level of netinc over 252d window."""
    res = _slope_pct(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_252d_v026_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_252d_v027_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 252d window."""
    res = _slope_pct(tangibles, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_252d_v028_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 252d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_504d_v029_signal(netinc):
    """Percentage slope for Raw level of netinc over 504d window."""
    res = _slope_pct(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_504d_v030_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_504d_v031_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 504d window."""
    res = _slope_pct(tangibles, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_504d_v032_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 504d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_756d_v033_signal(netinc):
    """Percentage slope for Raw level of netinc over 756d window."""
    res = _slope_pct(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_756d_v034_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_756d_v035_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 756d window."""
    res = _slope_pct(tangibles, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_756d_v036_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 756d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_1008d_v037_signal(netinc):
    """Percentage slope for Raw level of netinc over 1008d window."""
    res = _slope_pct(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_1008d_v038_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_1008d_v039_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 1008d window."""
    res = _slope_pct(tangibles, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_1008d_v040_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 1008d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_pct_1260d_v041_signal(netinc):
    """Percentage slope for Raw level of netinc over 1260d window."""
    res = _slope_pct(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_pct_1260d_v042_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_pct_1260d_v043_signal(tangibles):
    """Percentage slope for Raw level of tangibles over 1260d window."""
    res = _slope_pct(tangibles, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_pct_1260d_v044_signal(netinc, tangibles):
    """Percentage slope for Return on tangible assets over 1260d window."""
    res = _slope_pct(_ratio(netinc, tangibles), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_5d_v045_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 5d window."""
    res = _jerk(netinc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_5d_v046_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_5d_v047_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 5d window."""
    res = _jerk(tangibles, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_5d_v048_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 5d window."""
    res = _jerk(_ratio(netinc, tangibles), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_10d_v049_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 10d window."""
    res = _jerk(netinc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_10d_v050_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_10d_v051_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 10d window."""
    res = _jerk(tangibles, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_10d_v052_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 10d window."""
    res = _jerk(_ratio(netinc, tangibles), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_21d_v053_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 21d window."""
    res = _jerk(netinc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_21d_v054_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_21d_v055_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 21d window."""
    res = _jerk(tangibles, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_21d_v056_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 21d window."""
    res = _jerk(_ratio(netinc, tangibles), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_42d_v057_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 42d window."""
    res = _jerk(netinc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_42d_v058_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_42d_v059_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 42d window."""
    res = _jerk(tangibles, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_42d_v060_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 42d window."""
    res = _jerk(_ratio(netinc, tangibles), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_63d_v061_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 63d window."""
    res = _jerk(netinc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_63d_v062_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_63d_v063_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 63d window."""
    res = _jerk(tangibles, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_63d_v064_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 63d window."""
    res = _jerk(_ratio(netinc, tangibles), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_126d_v065_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 126d window."""
    res = _jerk(netinc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_126d_v066_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_126d_v067_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 126d window."""
    res = _jerk(tangibles, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_126d_v068_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 126d window."""
    res = _jerk(_ratio(netinc, tangibles), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_252d_v069_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 252d window."""
    res = _jerk(netinc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_252d_v070_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_252d_v071_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 252d window."""
    res = _jerk(tangibles, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_252d_v072_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 252d window."""
    res = _jerk(_ratio(netinc, tangibles), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_504d_v073_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 504d window."""
    res = _jerk(netinc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_504d_v074_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_504d_v075_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 504d window."""
    res = _jerk(tangibles, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_504d_v076_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 504d window."""
    res = _jerk(_ratio(netinc, tangibles), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_756d_v077_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 756d window."""
    res = _jerk(netinc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_756d_v078_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_756d_v079_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 756d window."""
    res = _jerk(tangibles, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_756d_v080_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 756d window."""
    res = _jerk(_ratio(netinc, tangibles), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_1008d_v081_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1008d window."""
    res = _jerk(netinc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_1008d_v082_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_1008d_v083_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 1008d window."""
    res = _jerk(tangibles, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_1008d_v084_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 1008d window."""
    res = _jerk(_ratio(netinc, tangibles), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_jerk_1260d_v085_signal(netinc):
    """Acceleration/Jerk for Raw level of netinc over 1260d window."""
    res = _jerk(netinc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_jerk_1260d_v086_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_jerk_1260d_v087_signal(tangibles):
    """Acceleration/Jerk for Raw level of tangibles over 1260d window."""
    res = _jerk(tangibles, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_jerk_1260d_v088_signal(netinc, tangibles):
    """Acceleration/Jerk for Return on tangible assets over 1260d window."""
    res = _jerk(_ratio(netinc, tangibles), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_5d_v089_signal(netinc):
    """Normalized slope change for Raw level of netinc over 5d window."""
    res = (_slope_pct(netinc, 5).diff(5) / _sma(netinc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_5d_v090_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_5d_v091_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 5d window."""
    res = (_slope_pct(tangibles, 5).diff(5) / _sma(tangibles.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_5d_v092_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 5d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 5).diff(5) / _sma(_ratio(netinc, tangibles).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_10d_v093_signal(netinc):
    """Normalized slope change for Raw level of netinc over 10d window."""
    res = (_slope_pct(netinc, 10).diff(10) / _sma(netinc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_10d_v094_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_10d_v095_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 10d window."""
    res = (_slope_pct(tangibles, 10).diff(10) / _sma(tangibles.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_10d_v096_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 10d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 10).diff(10) / _sma(_ratio(netinc, tangibles).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_21d_v097_signal(netinc):
    """Normalized slope change for Raw level of netinc over 21d window."""
    res = (_slope_pct(netinc, 21).diff(21) / _sma(netinc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_21d_v098_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_21d_v099_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 21d window."""
    res = (_slope_pct(tangibles, 21).diff(21) / _sma(tangibles.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_21d_v100_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 21d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 21).diff(21) / _sma(_ratio(netinc, tangibles).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_42d_v101_signal(netinc):
    """Normalized slope change for Raw level of netinc over 42d window."""
    res = (_slope_pct(netinc, 42).diff(42) / _sma(netinc.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_42d_v102_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_42d_v103_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 42d window."""
    res = (_slope_pct(tangibles, 42).diff(42) / _sma(tangibles.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_42d_v104_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 42d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 42).diff(42) / _sma(_ratio(netinc, tangibles).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_63d_v105_signal(netinc):
    """Normalized slope change for Raw level of netinc over 63d window."""
    res = (_slope_pct(netinc, 63).diff(63) / _sma(netinc.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_63d_v106_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_63d_v107_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 63d window."""
    res = (_slope_pct(tangibles, 63).diff(63) / _sma(tangibles.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_63d_v108_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 63d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 63).diff(63) / _sma(_ratio(netinc, tangibles).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_126d_v109_signal(netinc):
    """Normalized slope change for Raw level of netinc over 126d window."""
    res = (_slope_pct(netinc, 126).diff(126) / _sma(netinc.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_126d_v110_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_126d_v111_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 126d window."""
    res = (_slope_pct(tangibles, 126).diff(126) / _sma(tangibles.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_126d_v112_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 126d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 126).diff(126) / _sma(_ratio(netinc, tangibles).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_252d_v113_signal(netinc):
    """Normalized slope change for Raw level of netinc over 252d window."""
    res = (_slope_pct(netinc, 252).diff(252) / _sma(netinc.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_252d_v114_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_252d_v115_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 252d window."""
    res = (_slope_pct(tangibles, 252).diff(252) / _sma(tangibles.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_252d_v116_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 252d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 252).diff(252) / _sma(_ratio(netinc, tangibles).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_504d_v117_signal(netinc):
    """Normalized slope change for Raw level of netinc over 504d window."""
    res = (_slope_pct(netinc, 504).diff(504) / _sma(netinc.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_504d_v118_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_504d_v119_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 504d window."""
    res = (_slope_pct(tangibles, 504).diff(504) / _sma(tangibles.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_504d_v120_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 504d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 504).diff(504) / _sma(_ratio(netinc, tangibles).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_756d_v121_signal(netinc):
    """Normalized slope change for Raw level of netinc over 756d window."""
    res = (_slope_pct(netinc, 756).diff(756) / _sma(netinc.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_756d_v122_signal(assets):
    """Normalized slope change for Raw level of assets over 756d window."""
    res = (_slope_pct(assets, 756).diff(756) / _sma(assets.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_756d_v123_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 756d window."""
    res = (_slope_pct(tangibles, 756).diff(756) / _sma(tangibles.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_756d_v124_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 756d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 756).diff(756) / _sma(_ratio(netinc, tangibles).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_1008d_v125_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1008d window."""
    res = (_slope_pct(netinc, 1008).diff(1008) / _sma(netinc.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_1008d_v126_signal(assets):
    """Normalized slope change for Raw level of assets over 1008d window."""
    res = (_slope_pct(assets, 1008).diff(1008) / _sma(assets.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_1008d_v127_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 1008d window."""
    res = (_slope_pct(tangibles, 1008).diff(1008) / _sma(tangibles.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_1008d_v128_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 1008d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 1008).diff(1008) / _sma(_ratio(netinc, tangibles).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_slope_diff_norm_1260d_v129_signal(netinc):
    """Normalized slope change for Raw level of netinc over 1260d window."""
    res = (_slope_pct(netinc, 1260).diff(1260) / _sma(netinc.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_slope_diff_norm_1260d_v130_signal(assets):
    """Normalized slope change for Raw level of assets over 1260d window."""
    res = (_slope_pct(assets, 1260).diff(1260) / _sma(assets.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_slope_diff_norm_1260d_v131_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 1260d window."""
    res = (_slope_pct(tangibles, 1260).diff(1260) / _sma(tangibles.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_1260d_v132_signal(netinc, tangibles):
    """Normalized slope change for Return on tangible assets over 1260d window."""
    res = (_slope_pct(_ratio(netinc, tangibles), 1260).diff(1260) / _sma(_ratio(netinc, tangibles).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_mom_z_5d_v133_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 5d window."""
    res = _z(_slope_pct(netinc, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_mom_z_5d_v134_signal(assets):
    """Relative momentum strength for Raw level of assets over 5d window."""
    res = _z(_slope_pct(assets, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_mom_z_5d_v135_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 5d window."""
    res = _z(_slope_pct(tangibles, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_mom_z_5d_v136_signal(netinc, tangibles):
    """Relative momentum strength for Return on tangible assets over 5d window."""
    res = _z(_slope_pct(_ratio(netinc, tangibles), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_mom_z_10d_v137_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 10d window."""
    res = _z(_slope_pct(netinc, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_mom_z_10d_v138_signal(assets):
    """Relative momentum strength for Raw level of assets over 10d window."""
    res = _z(_slope_pct(assets, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_mom_z_10d_v139_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 10d window."""
    res = _z(_slope_pct(tangibles, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_mom_z_10d_v140_signal(netinc, tangibles):
    """Relative momentum strength for Return on tangible assets over 10d window."""
    res = _z(_slope_pct(_ratio(netinc, tangibles), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_mom_z_21d_v141_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 21d window."""
    res = _z(_slope_pct(netinc, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_mom_z_21d_v142_signal(assets):
    """Relative momentum strength for Raw level of assets over 21d window."""
    res = _z(_slope_pct(assets, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_mom_z_21d_v143_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 21d window."""
    res = _z(_slope_pct(tangibles, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_mom_z_21d_v144_signal(netinc, tangibles):
    """Relative momentum strength for Return on tangible assets over 21d window."""
    res = _z(_slope_pct(_ratio(netinc, tangibles), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_mom_z_42d_v145_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 42d window."""
    res = _z(_slope_pct(netinc, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_mom_z_42d_v146_signal(assets):
    """Relative momentum strength for Raw level of assets over 42d window."""
    res = _z(_slope_pct(assets, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_tangibles_mom_z_42d_v147_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 42d window."""
    res = _z(_slope_pct(tangibles, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_net_tangible_return_mom_z_42d_v148_signal(netinc, tangibles):
    """Relative momentum strength for Return on tangible assets over 42d window."""
    res = _z(_slope_pct(_ratio(netinc, tangibles), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_netinc_mom_z_63d_v149_signal(netinc):
    """Relative momentum strength for Raw level of netinc over 63d window."""
    res = _z(_slope_pct(netinc, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_asset_light_moat_fin_assets_mom_z_63d_v150_signal(assets):
    """Relative momentum strength for Raw level of assets over 63d window."""
    res = _z(_slope_pct(assets, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f49_asset_light_moat_fin_netinc_slope_pct_5d_v001_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_5d_v001_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_5d_v002_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_5d_v002_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_5d_v003_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_5d_v003_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_5d_v004_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_5d_v004_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_10d_v005_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_10d_v005_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_10d_v006_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_10d_v006_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_10d_v007_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_10d_v007_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_10d_v008_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_10d_v008_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_21d_v009_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_21d_v009_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_21d_v010_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_21d_v010_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_21d_v011_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_21d_v011_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_21d_v012_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_21d_v012_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_42d_v013_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_42d_v013_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_42d_v014_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_42d_v014_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_42d_v015_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_42d_v015_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_42d_v016_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_42d_v016_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_63d_v017_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_63d_v017_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_63d_v018_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_63d_v018_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_63d_v019_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_63d_v019_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_63d_v020_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_63d_v020_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_126d_v021_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_126d_v021_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_126d_v022_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_126d_v022_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_126d_v023_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_126d_v023_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_126d_v024_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_126d_v024_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_252d_v025_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_252d_v025_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_252d_v026_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_252d_v026_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_252d_v027_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_252d_v027_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_252d_v028_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_252d_v028_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_504d_v029_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_504d_v029_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_504d_v030_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_504d_v030_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_504d_v031_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_504d_v031_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_504d_v032_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_504d_v032_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_756d_v033_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_756d_v033_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_756d_v034_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_756d_v034_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_756d_v035_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_756d_v035_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_756d_v036_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_756d_v036_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_1008d_v037_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_1008d_v037_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_1008d_v038_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_1008d_v038_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_1008d_v039_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_1008d_v039_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_1008d_v040_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_1008d_v040_signal},
    "f49_asset_light_moat_fin_netinc_slope_pct_1260d_v041_signal": {"func": f49_asset_light_moat_fin_netinc_slope_pct_1260d_v041_signal},
    "f49_asset_light_moat_fin_assets_slope_pct_1260d_v042_signal": {"func": f49_asset_light_moat_fin_assets_slope_pct_1260d_v042_signal},
    "f49_asset_light_moat_fin_tangibles_slope_pct_1260d_v043_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_pct_1260d_v043_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_pct_1260d_v044_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_pct_1260d_v044_signal},
    "f49_asset_light_moat_fin_netinc_jerk_5d_v045_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_5d_v045_signal},
    "f49_asset_light_moat_fin_assets_jerk_5d_v046_signal": {"func": f49_asset_light_moat_fin_assets_jerk_5d_v046_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_5d_v047_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_5d_v047_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_5d_v048_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_5d_v048_signal},
    "f49_asset_light_moat_fin_netinc_jerk_10d_v049_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_10d_v049_signal},
    "f49_asset_light_moat_fin_assets_jerk_10d_v050_signal": {"func": f49_asset_light_moat_fin_assets_jerk_10d_v050_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_10d_v051_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_10d_v051_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_10d_v052_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_10d_v052_signal},
    "f49_asset_light_moat_fin_netinc_jerk_21d_v053_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_21d_v053_signal},
    "f49_asset_light_moat_fin_assets_jerk_21d_v054_signal": {"func": f49_asset_light_moat_fin_assets_jerk_21d_v054_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_21d_v055_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_21d_v055_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_21d_v056_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_21d_v056_signal},
    "f49_asset_light_moat_fin_netinc_jerk_42d_v057_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_42d_v057_signal},
    "f49_asset_light_moat_fin_assets_jerk_42d_v058_signal": {"func": f49_asset_light_moat_fin_assets_jerk_42d_v058_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_42d_v059_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_42d_v059_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_42d_v060_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_42d_v060_signal},
    "f49_asset_light_moat_fin_netinc_jerk_63d_v061_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_63d_v061_signal},
    "f49_asset_light_moat_fin_assets_jerk_63d_v062_signal": {"func": f49_asset_light_moat_fin_assets_jerk_63d_v062_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_63d_v063_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_63d_v063_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_63d_v064_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_63d_v064_signal},
    "f49_asset_light_moat_fin_netinc_jerk_126d_v065_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_126d_v065_signal},
    "f49_asset_light_moat_fin_assets_jerk_126d_v066_signal": {"func": f49_asset_light_moat_fin_assets_jerk_126d_v066_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_126d_v067_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_126d_v067_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_126d_v068_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_126d_v068_signal},
    "f49_asset_light_moat_fin_netinc_jerk_252d_v069_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_252d_v069_signal},
    "f49_asset_light_moat_fin_assets_jerk_252d_v070_signal": {"func": f49_asset_light_moat_fin_assets_jerk_252d_v070_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_252d_v071_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_252d_v071_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_252d_v072_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_252d_v072_signal},
    "f49_asset_light_moat_fin_netinc_jerk_504d_v073_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_504d_v073_signal},
    "f49_asset_light_moat_fin_assets_jerk_504d_v074_signal": {"func": f49_asset_light_moat_fin_assets_jerk_504d_v074_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_504d_v075_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_504d_v075_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_504d_v076_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_504d_v076_signal},
    "f49_asset_light_moat_fin_netinc_jerk_756d_v077_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_756d_v077_signal},
    "f49_asset_light_moat_fin_assets_jerk_756d_v078_signal": {"func": f49_asset_light_moat_fin_assets_jerk_756d_v078_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_756d_v079_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_756d_v079_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_756d_v080_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_756d_v080_signal},
    "f49_asset_light_moat_fin_netinc_jerk_1008d_v081_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_1008d_v081_signal},
    "f49_asset_light_moat_fin_assets_jerk_1008d_v082_signal": {"func": f49_asset_light_moat_fin_assets_jerk_1008d_v082_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_1008d_v083_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_1008d_v083_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_1008d_v084_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_1008d_v084_signal},
    "f49_asset_light_moat_fin_netinc_jerk_1260d_v085_signal": {"func": f49_asset_light_moat_fin_netinc_jerk_1260d_v085_signal},
    "f49_asset_light_moat_fin_assets_jerk_1260d_v086_signal": {"func": f49_asset_light_moat_fin_assets_jerk_1260d_v086_signal},
    "f49_asset_light_moat_fin_tangibles_jerk_1260d_v087_signal": {"func": f49_asset_light_moat_fin_tangibles_jerk_1260d_v087_signal},
    "f49_asset_light_moat_fin_net_tangible_return_jerk_1260d_v088_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_jerk_1260d_v088_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_5d_v089_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_5d_v089_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_5d_v090_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_5d_v090_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_5d_v091_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_5d_v091_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_5d_v092_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_5d_v092_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_10d_v093_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_10d_v093_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_10d_v094_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_10d_v094_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_10d_v095_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_10d_v095_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_10d_v096_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_10d_v096_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_21d_v097_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_21d_v097_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_21d_v098_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_21d_v098_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_21d_v099_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_21d_v099_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_21d_v100_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_21d_v100_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_42d_v101_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_42d_v101_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_42d_v102_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_42d_v102_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_42d_v103_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_42d_v103_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_42d_v104_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_42d_v104_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_63d_v105_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_63d_v105_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_63d_v106_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_63d_v106_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_63d_v107_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_63d_v107_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_63d_v108_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_63d_v108_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_126d_v109_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_126d_v109_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_126d_v110_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_126d_v110_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_126d_v111_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_126d_v111_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_126d_v112_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_126d_v112_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_252d_v113_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_252d_v113_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_252d_v114_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_252d_v114_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_252d_v115_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_252d_v115_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_252d_v116_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_252d_v116_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_504d_v117_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_504d_v117_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_504d_v118_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_504d_v118_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_504d_v119_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_504d_v119_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_504d_v120_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_504d_v120_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_756d_v121_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_756d_v121_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_756d_v122_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_756d_v122_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_756d_v123_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_756d_v123_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_756d_v124_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_756d_v124_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_1008d_v125_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_1008d_v125_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_1008d_v126_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_1008d_v126_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_1008d_v127_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_1008d_v127_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_1008d_v128_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_1008d_v128_signal},
    "f49_asset_light_moat_fin_netinc_slope_diff_norm_1260d_v129_signal": {"func": f49_asset_light_moat_fin_netinc_slope_diff_norm_1260d_v129_signal},
    "f49_asset_light_moat_fin_assets_slope_diff_norm_1260d_v130_signal": {"func": f49_asset_light_moat_fin_assets_slope_diff_norm_1260d_v130_signal},
    "f49_asset_light_moat_fin_tangibles_slope_diff_norm_1260d_v131_signal": {"func": f49_asset_light_moat_fin_tangibles_slope_diff_norm_1260d_v131_signal},
    "f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_1260d_v132_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_slope_diff_norm_1260d_v132_signal},
    "f49_asset_light_moat_fin_netinc_mom_z_5d_v133_signal": {"func": f49_asset_light_moat_fin_netinc_mom_z_5d_v133_signal},
    "f49_asset_light_moat_fin_assets_mom_z_5d_v134_signal": {"func": f49_asset_light_moat_fin_assets_mom_z_5d_v134_signal},
    "f49_asset_light_moat_fin_tangibles_mom_z_5d_v135_signal": {"func": f49_asset_light_moat_fin_tangibles_mom_z_5d_v135_signal},
    "f49_asset_light_moat_fin_net_tangible_return_mom_z_5d_v136_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_mom_z_5d_v136_signal},
    "f49_asset_light_moat_fin_netinc_mom_z_10d_v137_signal": {"func": f49_asset_light_moat_fin_netinc_mom_z_10d_v137_signal},
    "f49_asset_light_moat_fin_assets_mom_z_10d_v138_signal": {"func": f49_asset_light_moat_fin_assets_mom_z_10d_v138_signal},
    "f49_asset_light_moat_fin_tangibles_mom_z_10d_v139_signal": {"func": f49_asset_light_moat_fin_tangibles_mom_z_10d_v139_signal},
    "f49_asset_light_moat_fin_net_tangible_return_mom_z_10d_v140_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_mom_z_10d_v140_signal},
    "f49_asset_light_moat_fin_netinc_mom_z_21d_v141_signal": {"func": f49_asset_light_moat_fin_netinc_mom_z_21d_v141_signal},
    "f49_asset_light_moat_fin_assets_mom_z_21d_v142_signal": {"func": f49_asset_light_moat_fin_assets_mom_z_21d_v142_signal},
    "f49_asset_light_moat_fin_tangibles_mom_z_21d_v143_signal": {"func": f49_asset_light_moat_fin_tangibles_mom_z_21d_v143_signal},
    "f49_asset_light_moat_fin_net_tangible_return_mom_z_21d_v144_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_mom_z_21d_v144_signal},
    "f49_asset_light_moat_fin_netinc_mom_z_42d_v145_signal": {"func": f49_asset_light_moat_fin_netinc_mom_z_42d_v145_signal},
    "f49_asset_light_moat_fin_assets_mom_z_42d_v146_signal": {"func": f49_asset_light_moat_fin_assets_mom_z_42d_v146_signal},
    "f49_asset_light_moat_fin_tangibles_mom_z_42d_v147_signal": {"func": f49_asset_light_moat_fin_tangibles_mom_z_42d_v147_signal},
    "f49_asset_light_moat_fin_net_tangible_return_mom_z_42d_v148_signal": {"func": f49_asset_light_moat_fin_net_tangible_return_mom_z_42d_v148_signal},
    "f49_asset_light_moat_fin_netinc_mom_z_63d_v149_signal": {"func": f49_asset_light_moat_fin_netinc_mom_z_63d_v149_signal},
    "f49_asset_light_moat_fin_assets_mom_z_63d_v150_signal": {"func": f49_asset_light_moat_fin_assets_mom_z_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 49...")
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
