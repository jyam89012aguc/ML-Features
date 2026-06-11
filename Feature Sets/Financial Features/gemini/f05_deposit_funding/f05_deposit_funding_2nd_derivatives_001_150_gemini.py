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

def f05_deposit_funding_deposits_slope_pct_5d_v001_signal(deposits):
    """Percentage slope for Raw level of deposits over 5d window."""
    res = _slope_pct(deposits, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_5d_v002_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_5d_v003_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 5d window."""
    res = _slope_pct(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_5d_v004_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 5d window."""
    res = _slope_pct(_ratio(deposits, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_5d_v005_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 5d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_5d_v006_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 5d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_10d_v007_signal(deposits):
    """Percentage slope for Raw level of deposits over 10d window."""
    res = _slope_pct(deposits, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_10d_v008_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_10d_v009_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 10d window."""
    res = _slope_pct(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_10d_v010_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 10d window."""
    res = _slope_pct(_ratio(deposits, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_10d_v011_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 10d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_10d_v012_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 10d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_21d_v013_signal(deposits):
    """Percentage slope for Raw level of deposits over 21d window."""
    res = _slope_pct(deposits, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_21d_v014_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_21d_v015_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 21d window."""
    res = _slope_pct(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_21d_v016_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 21d window."""
    res = _slope_pct(_ratio(deposits, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_21d_v017_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 21d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_21d_v018_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 21d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_42d_v019_signal(deposits):
    """Percentage slope for Raw level of deposits over 42d window."""
    res = _slope_pct(deposits, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_42d_v020_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_42d_v021_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 42d window."""
    res = _slope_pct(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_42d_v022_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 42d window."""
    res = _slope_pct(_ratio(deposits, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_42d_v023_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 42d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_42d_v024_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 42d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_63d_v025_signal(deposits):
    """Percentage slope for Raw level of deposits over 63d window."""
    res = _slope_pct(deposits, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_63d_v026_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_63d_v027_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 63d window."""
    res = _slope_pct(liabilitiesc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_63d_v028_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 63d window."""
    res = _slope_pct(_ratio(deposits, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_63d_v029_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 63d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_63d_v030_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 63d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_126d_v031_signal(deposits):
    """Percentage slope for Raw level of deposits over 126d window."""
    res = _slope_pct(deposits, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_126d_v032_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_126d_v033_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 126d window."""
    res = _slope_pct(liabilitiesc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_126d_v034_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 126d window."""
    res = _slope_pct(_ratio(deposits, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_126d_v035_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 126d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_126d_v036_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 126d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_252d_v037_signal(deposits):
    """Percentage slope for Raw level of deposits over 252d window."""
    res = _slope_pct(deposits, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_252d_v038_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_252d_v039_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 252d window."""
    res = _slope_pct(liabilitiesc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_252d_v040_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 252d window."""
    res = _slope_pct(_ratio(deposits, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_252d_v041_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 252d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_252d_v042_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 252d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_504d_v043_signal(deposits):
    """Percentage slope for Raw level of deposits over 504d window."""
    res = _slope_pct(deposits, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_504d_v044_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_504d_v045_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 504d window."""
    res = _slope_pct(liabilitiesc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_504d_v046_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 504d window."""
    res = _slope_pct(_ratio(deposits, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_504d_v047_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 504d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_504d_v048_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 504d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_756d_v049_signal(deposits):
    """Percentage slope for Raw level of deposits over 756d window."""
    res = _slope_pct(deposits, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_756d_v050_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_756d_v051_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 756d window."""
    res = _slope_pct(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_756d_v052_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 756d window."""
    res = _slope_pct(_ratio(deposits, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_756d_v053_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 756d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_756d_v054_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 756d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_1008d_v055_signal(deposits):
    """Percentage slope for Raw level of deposits over 1008d window."""
    res = _slope_pct(deposits, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_1008d_v056_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_1008d_v057_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 1008d window."""
    res = _slope_pct(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_1008d_v058_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 1008d window."""
    res = _slope_pct(_ratio(deposits, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_1008d_v059_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 1008d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_1008d_v060_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 1008d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_pct_1260d_v061_signal(deposits):
    """Percentage slope for Raw level of deposits over 1260d window."""
    res = _slope_pct(deposits, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_pct_1260d_v062_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_pct_1260d_v063_signal(liabilitiesc):
    """Percentage slope for Raw level of liabilitiesc over 1260d window."""
    res = _slope_pct(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_pct_1260d_v064_signal(deposits, assets):
    """Percentage slope for Deposits as % of assets over 1260d window."""
    res = _slope_pct(_ratio(deposits, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_pct_1260d_v065_signal(deposits, liabilitiesc):
    """Percentage slope for Stable deposits relative to short-term liabilities over 1260d window."""
    res = _slope_pct(_ratio(deposits, liabilitiesc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_pct_1260d_v066_signal(deposits, assets, equity):
    """Percentage slope for Deposits relative to total debt funding over 1260d window."""
    res = _slope_pct(_ratio(deposits, assets - equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_5d_v067_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 5d window."""
    res = _jerk(deposits, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_5d_v068_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_5d_v069_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 5d window."""
    res = _jerk(liabilitiesc, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_5d_v070_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 5d window."""
    res = _jerk(_ratio(deposits, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_5d_v071_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 5d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_5d_v072_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 5d window."""
    res = _jerk(_ratio(deposits, assets - equity), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_10d_v073_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 10d window."""
    res = _jerk(deposits, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_10d_v074_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_10d_v075_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 10d window."""
    res = _jerk(liabilitiesc, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_10d_v076_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 10d window."""
    res = _jerk(_ratio(deposits, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_10d_v077_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 10d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_10d_v078_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 10d window."""
    res = _jerk(_ratio(deposits, assets - equity), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_21d_v079_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 21d window."""
    res = _jerk(deposits, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_21d_v080_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_21d_v081_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 21d window."""
    res = _jerk(liabilitiesc, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_21d_v082_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 21d window."""
    res = _jerk(_ratio(deposits, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_21d_v083_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 21d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_21d_v084_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 21d window."""
    res = _jerk(_ratio(deposits, assets - equity), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_42d_v085_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 42d window."""
    res = _jerk(deposits, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_42d_v086_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_42d_v087_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 42d window."""
    res = _jerk(liabilitiesc, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_42d_v088_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 42d window."""
    res = _jerk(_ratio(deposits, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_42d_v089_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 42d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_42d_v090_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 42d window."""
    res = _jerk(_ratio(deposits, assets - equity), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_63d_v091_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 63d window."""
    res = _jerk(deposits, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_63d_v092_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_63d_v093_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 63d window."""
    res = _jerk(liabilitiesc, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_63d_v094_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 63d window."""
    res = _jerk(_ratio(deposits, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_63d_v095_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 63d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_63d_v096_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 63d window."""
    res = _jerk(_ratio(deposits, assets - equity), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_126d_v097_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 126d window."""
    res = _jerk(deposits, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_126d_v098_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_126d_v099_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 126d window."""
    res = _jerk(liabilitiesc, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_126d_v100_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 126d window."""
    res = _jerk(_ratio(deposits, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_126d_v101_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 126d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_126d_v102_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 126d window."""
    res = _jerk(_ratio(deposits, assets - equity), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_252d_v103_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 252d window."""
    res = _jerk(deposits, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_252d_v104_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_252d_v105_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 252d window."""
    res = _jerk(liabilitiesc, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_252d_v106_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 252d window."""
    res = _jerk(_ratio(deposits, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_252d_v107_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 252d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_252d_v108_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 252d window."""
    res = _jerk(_ratio(deposits, assets - equity), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_504d_v109_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 504d window."""
    res = _jerk(deposits, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_504d_v110_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_504d_v111_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 504d window."""
    res = _jerk(liabilitiesc, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_504d_v112_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 504d window."""
    res = _jerk(_ratio(deposits, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_504d_v113_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 504d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_504d_v114_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 504d window."""
    res = _jerk(_ratio(deposits, assets - equity), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_756d_v115_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 756d window."""
    res = _jerk(deposits, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_756d_v116_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_756d_v117_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 756d window."""
    res = _jerk(liabilitiesc, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_756d_v118_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 756d window."""
    res = _jerk(_ratio(deposits, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_756d_v119_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 756d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_756d_v120_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 756d window."""
    res = _jerk(_ratio(deposits, assets - equity), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_1008d_v121_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 1008d window."""
    res = _jerk(deposits, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_1008d_v122_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_1008d_v123_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 1008d window."""
    res = _jerk(liabilitiesc, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_1008d_v124_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 1008d window."""
    res = _jerk(_ratio(deposits, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_1008d_v125_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 1008d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_1008d_v126_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 1008d window."""
    res = _jerk(_ratio(deposits, assets - equity), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_jerk_1260d_v127_signal(deposits):
    """Acceleration/Jerk for Raw level of deposits over 1260d window."""
    res = _jerk(deposits, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_jerk_1260d_v128_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_jerk_1260d_v129_signal(liabilitiesc):
    """Acceleration/Jerk for Raw level of liabilitiesc over 1260d window."""
    res = _jerk(liabilitiesc, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_jerk_1260d_v130_signal(deposits, assets):
    """Acceleration/Jerk for Deposits as % of assets over 1260d window."""
    res = _jerk(_ratio(deposits, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_jerk_1260d_v131_signal(deposits, liabilitiesc):
    """Acceleration/Jerk for Stable deposits relative to short-term liabilities over 1260d window."""
    res = _jerk(_ratio(deposits, liabilitiesc), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_jerk_1260d_v132_signal(deposits, assets, equity):
    """Acceleration/Jerk for Deposits relative to total debt funding over 1260d window."""
    res = _jerk(_ratio(deposits, assets - equity), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_5d_v133_signal(deposits):
    """Normalized slope change for Raw level of deposits over 5d window."""
    res = (_slope_pct(deposits, 5).diff(5) / _sma(deposits.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_5d_v134_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_5d_v135_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 5d window."""
    res = (_slope_pct(liabilitiesc, 5).diff(5) / _sma(liabilitiesc.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_5d_v136_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 5d window."""
    res = (_slope_pct(_ratio(deposits, assets), 5).diff(5) / _sma(_ratio(deposits, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_5d_v137_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 5d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 5).diff(5) / _sma(_ratio(deposits, liabilitiesc).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_5d_v138_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 5d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 5).diff(5) / _sma(_ratio(deposits, assets - equity).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_10d_v139_signal(deposits):
    """Normalized slope change for Raw level of deposits over 10d window."""
    res = (_slope_pct(deposits, 10).diff(10) / _sma(deposits.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_10d_v140_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_10d_v141_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 10d window."""
    res = (_slope_pct(liabilitiesc, 10).diff(10) / _sma(liabilitiesc.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_10d_v142_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 10d window."""
    res = (_slope_pct(_ratio(deposits, assets), 10).diff(10) / _sma(_ratio(deposits, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_10d_v143_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 10d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 10).diff(10) / _sma(_ratio(deposits, liabilitiesc).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_10d_v144_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 10d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 10).diff(10) / _sma(_ratio(deposits, assets - equity).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_slope_diff_norm_21d_v145_signal(deposits):
    """Normalized slope change for Raw level of deposits over 21d window."""
    res = (_slope_pct(deposits, 21).diff(21) / _sma(deposits.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_slope_diff_norm_21d_v146_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_slope_diff_norm_21d_v147_signal(liabilitiesc):
    """Normalized slope change for Raw level of liabilitiesc over 21d window."""
    res = (_slope_pct(liabilitiesc, 21).diff(21) / _sma(liabilitiesc.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_slope_diff_norm_21d_v148_signal(deposits, assets):
    """Normalized slope change for Deposits as % of assets over 21d window."""
    res = (_slope_pct(_ratio(deposits, assets), 21).diff(21) / _sma(_ratio(deposits, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_slope_diff_norm_21d_v149_signal(deposits, liabilitiesc):
    """Normalized slope change for Stable deposits relative to short-term liabilities over 21d window."""
    res = (_slope_pct(_ratio(deposits, liabilitiesc), 21).diff(21) / _sma(_ratio(deposits, liabilitiesc).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_slope_diff_norm_21d_v150_signal(deposits, assets, equity):
    """Normalized slope change for Deposits relative to total debt funding over 21d window."""
    res = (_slope_pct(_ratio(deposits, assets - equity), 21).diff(21) / _sma(_ratio(deposits, assets - equity).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f05_deposit_funding_deposits_slope_pct_5d_v001_signal": {"func": f05_deposit_funding_deposits_slope_pct_5d_v001_signal},
    "f05_deposit_funding_assets_slope_pct_5d_v002_signal": {"func": f05_deposit_funding_assets_slope_pct_5d_v002_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_5d_v003_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_5d_v003_signal},
    "f05_deposit_funding_deposit_density_slope_pct_5d_v004_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_5d_v004_signal},
    "f05_deposit_funding_funding_quality_slope_pct_5d_v005_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_5d_v005_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_5d_v006_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_5d_v006_signal},
    "f05_deposit_funding_deposits_slope_pct_10d_v007_signal": {"func": f05_deposit_funding_deposits_slope_pct_10d_v007_signal},
    "f05_deposit_funding_assets_slope_pct_10d_v008_signal": {"func": f05_deposit_funding_assets_slope_pct_10d_v008_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_10d_v009_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_10d_v009_signal},
    "f05_deposit_funding_deposit_density_slope_pct_10d_v010_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_10d_v010_signal},
    "f05_deposit_funding_funding_quality_slope_pct_10d_v011_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_10d_v011_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_10d_v012_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_10d_v012_signal},
    "f05_deposit_funding_deposits_slope_pct_21d_v013_signal": {"func": f05_deposit_funding_deposits_slope_pct_21d_v013_signal},
    "f05_deposit_funding_assets_slope_pct_21d_v014_signal": {"func": f05_deposit_funding_assets_slope_pct_21d_v014_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_21d_v015_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_21d_v015_signal},
    "f05_deposit_funding_deposit_density_slope_pct_21d_v016_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_21d_v016_signal},
    "f05_deposit_funding_funding_quality_slope_pct_21d_v017_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_21d_v017_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_21d_v018_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_21d_v018_signal},
    "f05_deposit_funding_deposits_slope_pct_42d_v019_signal": {"func": f05_deposit_funding_deposits_slope_pct_42d_v019_signal},
    "f05_deposit_funding_assets_slope_pct_42d_v020_signal": {"func": f05_deposit_funding_assets_slope_pct_42d_v020_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_42d_v021_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_42d_v021_signal},
    "f05_deposit_funding_deposit_density_slope_pct_42d_v022_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_42d_v022_signal},
    "f05_deposit_funding_funding_quality_slope_pct_42d_v023_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_42d_v023_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_42d_v024_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_42d_v024_signal},
    "f05_deposit_funding_deposits_slope_pct_63d_v025_signal": {"func": f05_deposit_funding_deposits_slope_pct_63d_v025_signal},
    "f05_deposit_funding_assets_slope_pct_63d_v026_signal": {"func": f05_deposit_funding_assets_slope_pct_63d_v026_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_63d_v027_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_63d_v027_signal},
    "f05_deposit_funding_deposit_density_slope_pct_63d_v028_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_63d_v028_signal},
    "f05_deposit_funding_funding_quality_slope_pct_63d_v029_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_63d_v029_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_63d_v030_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_63d_v030_signal},
    "f05_deposit_funding_deposits_slope_pct_126d_v031_signal": {"func": f05_deposit_funding_deposits_slope_pct_126d_v031_signal},
    "f05_deposit_funding_assets_slope_pct_126d_v032_signal": {"func": f05_deposit_funding_assets_slope_pct_126d_v032_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_126d_v033_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_126d_v033_signal},
    "f05_deposit_funding_deposit_density_slope_pct_126d_v034_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_126d_v034_signal},
    "f05_deposit_funding_funding_quality_slope_pct_126d_v035_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_126d_v035_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_126d_v036_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_126d_v036_signal},
    "f05_deposit_funding_deposits_slope_pct_252d_v037_signal": {"func": f05_deposit_funding_deposits_slope_pct_252d_v037_signal},
    "f05_deposit_funding_assets_slope_pct_252d_v038_signal": {"func": f05_deposit_funding_assets_slope_pct_252d_v038_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_252d_v039_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_252d_v039_signal},
    "f05_deposit_funding_deposit_density_slope_pct_252d_v040_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_252d_v040_signal},
    "f05_deposit_funding_funding_quality_slope_pct_252d_v041_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_252d_v041_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_252d_v042_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_252d_v042_signal},
    "f05_deposit_funding_deposits_slope_pct_504d_v043_signal": {"func": f05_deposit_funding_deposits_slope_pct_504d_v043_signal},
    "f05_deposit_funding_assets_slope_pct_504d_v044_signal": {"func": f05_deposit_funding_assets_slope_pct_504d_v044_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_504d_v045_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_504d_v045_signal},
    "f05_deposit_funding_deposit_density_slope_pct_504d_v046_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_504d_v046_signal},
    "f05_deposit_funding_funding_quality_slope_pct_504d_v047_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_504d_v047_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_504d_v048_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_504d_v048_signal},
    "f05_deposit_funding_deposits_slope_pct_756d_v049_signal": {"func": f05_deposit_funding_deposits_slope_pct_756d_v049_signal},
    "f05_deposit_funding_assets_slope_pct_756d_v050_signal": {"func": f05_deposit_funding_assets_slope_pct_756d_v050_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_756d_v051_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_756d_v051_signal},
    "f05_deposit_funding_deposit_density_slope_pct_756d_v052_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_756d_v052_signal},
    "f05_deposit_funding_funding_quality_slope_pct_756d_v053_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_756d_v053_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_756d_v054_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_756d_v054_signal},
    "f05_deposit_funding_deposits_slope_pct_1008d_v055_signal": {"func": f05_deposit_funding_deposits_slope_pct_1008d_v055_signal},
    "f05_deposit_funding_assets_slope_pct_1008d_v056_signal": {"func": f05_deposit_funding_assets_slope_pct_1008d_v056_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_1008d_v057_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_1008d_v057_signal},
    "f05_deposit_funding_deposit_density_slope_pct_1008d_v058_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_1008d_v058_signal},
    "f05_deposit_funding_funding_quality_slope_pct_1008d_v059_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_1008d_v059_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_1008d_v060_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_1008d_v060_signal},
    "f05_deposit_funding_deposits_slope_pct_1260d_v061_signal": {"func": f05_deposit_funding_deposits_slope_pct_1260d_v061_signal},
    "f05_deposit_funding_assets_slope_pct_1260d_v062_signal": {"func": f05_deposit_funding_assets_slope_pct_1260d_v062_signal},
    "f05_deposit_funding_liabilitiesc_slope_pct_1260d_v063_signal": {"func": f05_deposit_funding_liabilitiesc_slope_pct_1260d_v063_signal},
    "f05_deposit_funding_deposit_density_slope_pct_1260d_v064_signal": {"func": f05_deposit_funding_deposit_density_slope_pct_1260d_v064_signal},
    "f05_deposit_funding_funding_quality_slope_pct_1260d_v065_signal": {"func": f05_deposit_funding_funding_quality_slope_pct_1260d_v065_signal},
    "f05_deposit_funding_asset_funding_mix_slope_pct_1260d_v066_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_pct_1260d_v066_signal},
    "f05_deposit_funding_deposits_jerk_5d_v067_signal": {"func": f05_deposit_funding_deposits_jerk_5d_v067_signal},
    "f05_deposit_funding_assets_jerk_5d_v068_signal": {"func": f05_deposit_funding_assets_jerk_5d_v068_signal},
    "f05_deposit_funding_liabilitiesc_jerk_5d_v069_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_5d_v069_signal},
    "f05_deposit_funding_deposit_density_jerk_5d_v070_signal": {"func": f05_deposit_funding_deposit_density_jerk_5d_v070_signal},
    "f05_deposit_funding_funding_quality_jerk_5d_v071_signal": {"func": f05_deposit_funding_funding_quality_jerk_5d_v071_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_5d_v072_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_5d_v072_signal},
    "f05_deposit_funding_deposits_jerk_10d_v073_signal": {"func": f05_deposit_funding_deposits_jerk_10d_v073_signal},
    "f05_deposit_funding_assets_jerk_10d_v074_signal": {"func": f05_deposit_funding_assets_jerk_10d_v074_signal},
    "f05_deposit_funding_liabilitiesc_jerk_10d_v075_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_10d_v075_signal},
    "f05_deposit_funding_deposit_density_jerk_10d_v076_signal": {"func": f05_deposit_funding_deposit_density_jerk_10d_v076_signal},
    "f05_deposit_funding_funding_quality_jerk_10d_v077_signal": {"func": f05_deposit_funding_funding_quality_jerk_10d_v077_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_10d_v078_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_10d_v078_signal},
    "f05_deposit_funding_deposits_jerk_21d_v079_signal": {"func": f05_deposit_funding_deposits_jerk_21d_v079_signal},
    "f05_deposit_funding_assets_jerk_21d_v080_signal": {"func": f05_deposit_funding_assets_jerk_21d_v080_signal},
    "f05_deposit_funding_liabilitiesc_jerk_21d_v081_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_21d_v081_signal},
    "f05_deposit_funding_deposit_density_jerk_21d_v082_signal": {"func": f05_deposit_funding_deposit_density_jerk_21d_v082_signal},
    "f05_deposit_funding_funding_quality_jerk_21d_v083_signal": {"func": f05_deposit_funding_funding_quality_jerk_21d_v083_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_21d_v084_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_21d_v084_signal},
    "f05_deposit_funding_deposits_jerk_42d_v085_signal": {"func": f05_deposit_funding_deposits_jerk_42d_v085_signal},
    "f05_deposit_funding_assets_jerk_42d_v086_signal": {"func": f05_deposit_funding_assets_jerk_42d_v086_signal},
    "f05_deposit_funding_liabilitiesc_jerk_42d_v087_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_42d_v087_signal},
    "f05_deposit_funding_deposit_density_jerk_42d_v088_signal": {"func": f05_deposit_funding_deposit_density_jerk_42d_v088_signal},
    "f05_deposit_funding_funding_quality_jerk_42d_v089_signal": {"func": f05_deposit_funding_funding_quality_jerk_42d_v089_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_42d_v090_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_42d_v090_signal},
    "f05_deposit_funding_deposits_jerk_63d_v091_signal": {"func": f05_deposit_funding_deposits_jerk_63d_v091_signal},
    "f05_deposit_funding_assets_jerk_63d_v092_signal": {"func": f05_deposit_funding_assets_jerk_63d_v092_signal},
    "f05_deposit_funding_liabilitiesc_jerk_63d_v093_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_63d_v093_signal},
    "f05_deposit_funding_deposit_density_jerk_63d_v094_signal": {"func": f05_deposit_funding_deposit_density_jerk_63d_v094_signal},
    "f05_deposit_funding_funding_quality_jerk_63d_v095_signal": {"func": f05_deposit_funding_funding_quality_jerk_63d_v095_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_63d_v096_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_63d_v096_signal},
    "f05_deposit_funding_deposits_jerk_126d_v097_signal": {"func": f05_deposit_funding_deposits_jerk_126d_v097_signal},
    "f05_deposit_funding_assets_jerk_126d_v098_signal": {"func": f05_deposit_funding_assets_jerk_126d_v098_signal},
    "f05_deposit_funding_liabilitiesc_jerk_126d_v099_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_126d_v099_signal},
    "f05_deposit_funding_deposit_density_jerk_126d_v100_signal": {"func": f05_deposit_funding_deposit_density_jerk_126d_v100_signal},
    "f05_deposit_funding_funding_quality_jerk_126d_v101_signal": {"func": f05_deposit_funding_funding_quality_jerk_126d_v101_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_126d_v102_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_126d_v102_signal},
    "f05_deposit_funding_deposits_jerk_252d_v103_signal": {"func": f05_deposit_funding_deposits_jerk_252d_v103_signal},
    "f05_deposit_funding_assets_jerk_252d_v104_signal": {"func": f05_deposit_funding_assets_jerk_252d_v104_signal},
    "f05_deposit_funding_liabilitiesc_jerk_252d_v105_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_252d_v105_signal},
    "f05_deposit_funding_deposit_density_jerk_252d_v106_signal": {"func": f05_deposit_funding_deposit_density_jerk_252d_v106_signal},
    "f05_deposit_funding_funding_quality_jerk_252d_v107_signal": {"func": f05_deposit_funding_funding_quality_jerk_252d_v107_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_252d_v108_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_252d_v108_signal},
    "f05_deposit_funding_deposits_jerk_504d_v109_signal": {"func": f05_deposit_funding_deposits_jerk_504d_v109_signal},
    "f05_deposit_funding_assets_jerk_504d_v110_signal": {"func": f05_deposit_funding_assets_jerk_504d_v110_signal},
    "f05_deposit_funding_liabilitiesc_jerk_504d_v111_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_504d_v111_signal},
    "f05_deposit_funding_deposit_density_jerk_504d_v112_signal": {"func": f05_deposit_funding_deposit_density_jerk_504d_v112_signal},
    "f05_deposit_funding_funding_quality_jerk_504d_v113_signal": {"func": f05_deposit_funding_funding_quality_jerk_504d_v113_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_504d_v114_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_504d_v114_signal},
    "f05_deposit_funding_deposits_jerk_756d_v115_signal": {"func": f05_deposit_funding_deposits_jerk_756d_v115_signal},
    "f05_deposit_funding_assets_jerk_756d_v116_signal": {"func": f05_deposit_funding_assets_jerk_756d_v116_signal},
    "f05_deposit_funding_liabilitiesc_jerk_756d_v117_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_756d_v117_signal},
    "f05_deposit_funding_deposit_density_jerk_756d_v118_signal": {"func": f05_deposit_funding_deposit_density_jerk_756d_v118_signal},
    "f05_deposit_funding_funding_quality_jerk_756d_v119_signal": {"func": f05_deposit_funding_funding_quality_jerk_756d_v119_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_756d_v120_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_756d_v120_signal},
    "f05_deposit_funding_deposits_jerk_1008d_v121_signal": {"func": f05_deposit_funding_deposits_jerk_1008d_v121_signal},
    "f05_deposit_funding_assets_jerk_1008d_v122_signal": {"func": f05_deposit_funding_assets_jerk_1008d_v122_signal},
    "f05_deposit_funding_liabilitiesc_jerk_1008d_v123_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_1008d_v123_signal},
    "f05_deposit_funding_deposit_density_jerk_1008d_v124_signal": {"func": f05_deposit_funding_deposit_density_jerk_1008d_v124_signal},
    "f05_deposit_funding_funding_quality_jerk_1008d_v125_signal": {"func": f05_deposit_funding_funding_quality_jerk_1008d_v125_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_1008d_v126_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_1008d_v126_signal},
    "f05_deposit_funding_deposits_jerk_1260d_v127_signal": {"func": f05_deposit_funding_deposits_jerk_1260d_v127_signal},
    "f05_deposit_funding_assets_jerk_1260d_v128_signal": {"func": f05_deposit_funding_assets_jerk_1260d_v128_signal},
    "f05_deposit_funding_liabilitiesc_jerk_1260d_v129_signal": {"func": f05_deposit_funding_liabilitiesc_jerk_1260d_v129_signal},
    "f05_deposit_funding_deposit_density_jerk_1260d_v130_signal": {"func": f05_deposit_funding_deposit_density_jerk_1260d_v130_signal},
    "f05_deposit_funding_funding_quality_jerk_1260d_v131_signal": {"func": f05_deposit_funding_funding_quality_jerk_1260d_v131_signal},
    "f05_deposit_funding_asset_funding_mix_jerk_1260d_v132_signal": {"func": f05_deposit_funding_asset_funding_mix_jerk_1260d_v132_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_5d_v133_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_5d_v133_signal},
    "f05_deposit_funding_assets_slope_diff_norm_5d_v134_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_5d_v134_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_5d_v135_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_5d_v135_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_5d_v136_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_5d_v136_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_5d_v137_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_5d_v137_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_5d_v138_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_5d_v138_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_10d_v139_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_10d_v139_signal},
    "f05_deposit_funding_assets_slope_diff_norm_10d_v140_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_10d_v140_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_10d_v141_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_10d_v141_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_10d_v142_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_10d_v142_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_10d_v143_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_10d_v143_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_10d_v144_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_10d_v144_signal},
    "f05_deposit_funding_deposits_slope_diff_norm_21d_v145_signal": {"func": f05_deposit_funding_deposits_slope_diff_norm_21d_v145_signal},
    "f05_deposit_funding_assets_slope_diff_norm_21d_v146_signal": {"func": f05_deposit_funding_assets_slope_diff_norm_21d_v146_signal},
    "f05_deposit_funding_liabilitiesc_slope_diff_norm_21d_v147_signal": {"func": f05_deposit_funding_liabilitiesc_slope_diff_norm_21d_v147_signal},
    "f05_deposit_funding_deposit_density_slope_diff_norm_21d_v148_signal": {"func": f05_deposit_funding_deposit_density_slope_diff_norm_21d_v148_signal},
    "f05_deposit_funding_funding_quality_slope_diff_norm_21d_v149_signal": {"func": f05_deposit_funding_funding_quality_slope_diff_norm_21d_v149_signal},
    "f05_deposit_funding_asset_funding_mix_slope_diff_norm_21d_v150_signal": {"func": f05_deposit_funding_asset_funding_mix_slope_diff_norm_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 05...")
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
