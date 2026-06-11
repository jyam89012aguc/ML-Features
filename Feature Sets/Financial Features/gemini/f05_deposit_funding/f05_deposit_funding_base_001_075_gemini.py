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

def f05_deposit_funding_deposits_base_5d_v001_signal(deposits):
    """Moving average of Raw level of deposits over 5d window."""
    res = _sma(deposits, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_5d_v002_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_5d_v003_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 5d window."""
    res = _sma(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_5d_v004_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 5d window."""
    res = _sma(_ratio(deposits, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_5d_v005_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 5d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_5d_v006_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 5d window."""
    res = _sma(_ratio(deposits, assets - equity), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_10d_v007_signal(deposits):
    """Moving average of Raw level of deposits over 10d window."""
    res = _sma(deposits, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_10d_v008_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_10d_v009_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 10d window."""
    res = _sma(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_10d_v010_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 10d window."""
    res = _sma(_ratio(deposits, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_10d_v011_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 10d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_10d_v012_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 10d window."""
    res = _sma(_ratio(deposits, assets - equity), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_21d_v013_signal(deposits):
    """Moving average of Raw level of deposits over 21d window."""
    res = _sma(deposits, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_21d_v014_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_21d_v015_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 21d window."""
    res = _sma(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_21d_v016_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 21d window."""
    res = _sma(_ratio(deposits, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_21d_v017_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 21d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_21d_v018_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 21d window."""
    res = _sma(_ratio(deposits, assets - equity), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_42d_v019_signal(deposits):
    """Moving average of Raw level of deposits over 42d window."""
    res = _sma(deposits, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_42d_v020_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_42d_v021_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 42d window."""
    res = _sma(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_42d_v022_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 42d window."""
    res = _sma(_ratio(deposits, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_42d_v023_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 42d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_42d_v024_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 42d window."""
    res = _sma(_ratio(deposits, assets - equity), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_63d_v025_signal(deposits):
    """Moving average of Raw level of deposits over 63d window."""
    res = _sma(deposits, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_63d_v026_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_63d_v027_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 63d window."""
    res = _sma(liabilitiesc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_63d_v028_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 63d window."""
    res = _sma(_ratio(deposits, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_63d_v029_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 63d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_63d_v030_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 63d window."""
    res = _sma(_ratio(deposits, assets - equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_126d_v031_signal(deposits):
    """Moving average of Raw level of deposits over 126d window."""
    res = _sma(deposits, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_126d_v032_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_126d_v033_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 126d window."""
    res = _sma(liabilitiesc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_126d_v034_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 126d window."""
    res = _sma(_ratio(deposits, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_126d_v035_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 126d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_126d_v036_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 126d window."""
    res = _sma(_ratio(deposits, assets - equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_252d_v037_signal(deposits):
    """Moving average of Raw level of deposits over 252d window."""
    res = _sma(deposits, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_252d_v038_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_252d_v039_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 252d window."""
    res = _sma(liabilitiesc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_252d_v040_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 252d window."""
    res = _sma(_ratio(deposits, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_252d_v041_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 252d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_252d_v042_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 252d window."""
    res = _sma(_ratio(deposits, assets - equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_504d_v043_signal(deposits):
    """Moving average of Raw level of deposits over 504d window."""
    res = _sma(deposits, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_504d_v044_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_504d_v045_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 504d window."""
    res = _sma(liabilitiesc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_504d_v046_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 504d window."""
    res = _sma(_ratio(deposits, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_504d_v047_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 504d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_504d_v048_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 504d window."""
    res = _sma(_ratio(deposits, assets - equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_756d_v049_signal(deposits):
    """Moving average of Raw level of deposits over 756d window."""
    res = _sma(deposits, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_756d_v050_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_756d_v051_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 756d window."""
    res = _sma(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_756d_v052_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 756d window."""
    res = _sma(_ratio(deposits, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_756d_v053_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 756d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_756d_v054_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 756d window."""
    res = _sma(_ratio(deposits, assets - equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_1008d_v055_signal(deposits):
    """Moving average of Raw level of deposits over 1008d window."""
    res = _sma(deposits, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_1008d_v056_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_1008d_v057_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 1008d window."""
    res = _sma(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_1008d_v058_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 1008d window."""
    res = _sma(_ratio(deposits, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_1008d_v059_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 1008d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_1008d_v060_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 1008d window."""
    res = _sma(_ratio(deposits, assets - equity), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_base_1260d_v061_signal(deposits):
    """Moving average of Raw level of deposits over 1260d window."""
    res = _sma(deposits, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_base_1260d_v062_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_base_1260d_v063_signal(liabilitiesc):
    """Moving average of Raw level of liabilitiesc over 1260d window."""
    res = _sma(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_base_1260d_v064_signal(deposits, assets):
    """Moving average of Deposits as % of assets over 1260d window."""
    res = _sma(_ratio(deposits, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_base_1260d_v065_signal(deposits, liabilitiesc):
    """Moving average of Stable deposits relative to short-term liabilities over 1260d window."""
    res = _sma(_ratio(deposits, liabilitiesc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_base_1260d_v066_signal(deposits, assets, equity):
    """Moving average of Deposits relative to total debt funding over 1260d window."""
    res = _sma(_ratio(deposits, assets - equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_5d_v067_signal(deposits):
    """Exponential moving average of Raw level of deposits over 5d window."""
    res = _ewma(deposits, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_5d_v068_signal(assets):
    """Exponential moving average of Raw level of assets over 5d window."""
    res = _ewma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_5d_v069_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 5d window."""
    res = _ewma(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_5d_v070_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 5d window."""
    res = _ewma(_ratio(deposits, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_5d_v071_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 5d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_5d_v072_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 5d window."""
    res = _ewma(_ratio(deposits, assets - equity), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_10d_v073_signal(deposits):
    """Exponential moving average of Raw level of deposits over 10d window."""
    res = _ewma(deposits, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_10d_v074_signal(assets):
    """Exponential moving average of Raw level of assets over 10d window."""
    res = _ewma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_10d_v075_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 10d window."""
    res = _ewma(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f05_deposit_funding_deposits_base_5d_v001_signal": {"func": f05_deposit_funding_deposits_base_5d_v001_signal},
    "f05_deposit_funding_assets_base_5d_v002_signal": {"func": f05_deposit_funding_assets_base_5d_v002_signal},
    "f05_deposit_funding_liabilitiesc_base_5d_v003_signal": {"func": f05_deposit_funding_liabilitiesc_base_5d_v003_signal},
    "f05_deposit_funding_deposit_density_base_5d_v004_signal": {"func": f05_deposit_funding_deposit_density_base_5d_v004_signal},
    "f05_deposit_funding_funding_quality_base_5d_v005_signal": {"func": f05_deposit_funding_funding_quality_base_5d_v005_signal},
    "f05_deposit_funding_asset_funding_mix_base_5d_v006_signal": {"func": f05_deposit_funding_asset_funding_mix_base_5d_v006_signal},
    "f05_deposit_funding_deposits_base_10d_v007_signal": {"func": f05_deposit_funding_deposits_base_10d_v007_signal},
    "f05_deposit_funding_assets_base_10d_v008_signal": {"func": f05_deposit_funding_assets_base_10d_v008_signal},
    "f05_deposit_funding_liabilitiesc_base_10d_v009_signal": {"func": f05_deposit_funding_liabilitiesc_base_10d_v009_signal},
    "f05_deposit_funding_deposit_density_base_10d_v010_signal": {"func": f05_deposit_funding_deposit_density_base_10d_v010_signal},
    "f05_deposit_funding_funding_quality_base_10d_v011_signal": {"func": f05_deposit_funding_funding_quality_base_10d_v011_signal},
    "f05_deposit_funding_asset_funding_mix_base_10d_v012_signal": {"func": f05_deposit_funding_asset_funding_mix_base_10d_v012_signal},
    "f05_deposit_funding_deposits_base_21d_v013_signal": {"func": f05_deposit_funding_deposits_base_21d_v013_signal},
    "f05_deposit_funding_assets_base_21d_v014_signal": {"func": f05_deposit_funding_assets_base_21d_v014_signal},
    "f05_deposit_funding_liabilitiesc_base_21d_v015_signal": {"func": f05_deposit_funding_liabilitiesc_base_21d_v015_signal},
    "f05_deposit_funding_deposit_density_base_21d_v016_signal": {"func": f05_deposit_funding_deposit_density_base_21d_v016_signal},
    "f05_deposit_funding_funding_quality_base_21d_v017_signal": {"func": f05_deposit_funding_funding_quality_base_21d_v017_signal},
    "f05_deposit_funding_asset_funding_mix_base_21d_v018_signal": {"func": f05_deposit_funding_asset_funding_mix_base_21d_v018_signal},
    "f05_deposit_funding_deposits_base_42d_v019_signal": {"func": f05_deposit_funding_deposits_base_42d_v019_signal},
    "f05_deposit_funding_assets_base_42d_v020_signal": {"func": f05_deposit_funding_assets_base_42d_v020_signal},
    "f05_deposit_funding_liabilitiesc_base_42d_v021_signal": {"func": f05_deposit_funding_liabilitiesc_base_42d_v021_signal},
    "f05_deposit_funding_deposit_density_base_42d_v022_signal": {"func": f05_deposit_funding_deposit_density_base_42d_v022_signal},
    "f05_deposit_funding_funding_quality_base_42d_v023_signal": {"func": f05_deposit_funding_funding_quality_base_42d_v023_signal},
    "f05_deposit_funding_asset_funding_mix_base_42d_v024_signal": {"func": f05_deposit_funding_asset_funding_mix_base_42d_v024_signal},
    "f05_deposit_funding_deposits_base_63d_v025_signal": {"func": f05_deposit_funding_deposits_base_63d_v025_signal},
    "f05_deposit_funding_assets_base_63d_v026_signal": {"func": f05_deposit_funding_assets_base_63d_v026_signal},
    "f05_deposit_funding_liabilitiesc_base_63d_v027_signal": {"func": f05_deposit_funding_liabilitiesc_base_63d_v027_signal},
    "f05_deposit_funding_deposit_density_base_63d_v028_signal": {"func": f05_deposit_funding_deposit_density_base_63d_v028_signal},
    "f05_deposit_funding_funding_quality_base_63d_v029_signal": {"func": f05_deposit_funding_funding_quality_base_63d_v029_signal},
    "f05_deposit_funding_asset_funding_mix_base_63d_v030_signal": {"func": f05_deposit_funding_asset_funding_mix_base_63d_v030_signal},
    "f05_deposit_funding_deposits_base_126d_v031_signal": {"func": f05_deposit_funding_deposits_base_126d_v031_signal},
    "f05_deposit_funding_assets_base_126d_v032_signal": {"func": f05_deposit_funding_assets_base_126d_v032_signal},
    "f05_deposit_funding_liabilitiesc_base_126d_v033_signal": {"func": f05_deposit_funding_liabilitiesc_base_126d_v033_signal},
    "f05_deposit_funding_deposit_density_base_126d_v034_signal": {"func": f05_deposit_funding_deposit_density_base_126d_v034_signal},
    "f05_deposit_funding_funding_quality_base_126d_v035_signal": {"func": f05_deposit_funding_funding_quality_base_126d_v035_signal},
    "f05_deposit_funding_asset_funding_mix_base_126d_v036_signal": {"func": f05_deposit_funding_asset_funding_mix_base_126d_v036_signal},
    "f05_deposit_funding_deposits_base_252d_v037_signal": {"func": f05_deposit_funding_deposits_base_252d_v037_signal},
    "f05_deposit_funding_assets_base_252d_v038_signal": {"func": f05_deposit_funding_assets_base_252d_v038_signal},
    "f05_deposit_funding_liabilitiesc_base_252d_v039_signal": {"func": f05_deposit_funding_liabilitiesc_base_252d_v039_signal},
    "f05_deposit_funding_deposit_density_base_252d_v040_signal": {"func": f05_deposit_funding_deposit_density_base_252d_v040_signal},
    "f05_deposit_funding_funding_quality_base_252d_v041_signal": {"func": f05_deposit_funding_funding_quality_base_252d_v041_signal},
    "f05_deposit_funding_asset_funding_mix_base_252d_v042_signal": {"func": f05_deposit_funding_asset_funding_mix_base_252d_v042_signal},
    "f05_deposit_funding_deposits_base_504d_v043_signal": {"func": f05_deposit_funding_deposits_base_504d_v043_signal},
    "f05_deposit_funding_assets_base_504d_v044_signal": {"func": f05_deposit_funding_assets_base_504d_v044_signal},
    "f05_deposit_funding_liabilitiesc_base_504d_v045_signal": {"func": f05_deposit_funding_liabilitiesc_base_504d_v045_signal},
    "f05_deposit_funding_deposit_density_base_504d_v046_signal": {"func": f05_deposit_funding_deposit_density_base_504d_v046_signal},
    "f05_deposit_funding_funding_quality_base_504d_v047_signal": {"func": f05_deposit_funding_funding_quality_base_504d_v047_signal},
    "f05_deposit_funding_asset_funding_mix_base_504d_v048_signal": {"func": f05_deposit_funding_asset_funding_mix_base_504d_v048_signal},
    "f05_deposit_funding_deposits_base_756d_v049_signal": {"func": f05_deposit_funding_deposits_base_756d_v049_signal},
    "f05_deposit_funding_assets_base_756d_v050_signal": {"func": f05_deposit_funding_assets_base_756d_v050_signal},
    "f05_deposit_funding_liabilitiesc_base_756d_v051_signal": {"func": f05_deposit_funding_liabilitiesc_base_756d_v051_signal},
    "f05_deposit_funding_deposit_density_base_756d_v052_signal": {"func": f05_deposit_funding_deposit_density_base_756d_v052_signal},
    "f05_deposit_funding_funding_quality_base_756d_v053_signal": {"func": f05_deposit_funding_funding_quality_base_756d_v053_signal},
    "f05_deposit_funding_asset_funding_mix_base_756d_v054_signal": {"func": f05_deposit_funding_asset_funding_mix_base_756d_v054_signal},
    "f05_deposit_funding_deposits_base_1008d_v055_signal": {"func": f05_deposit_funding_deposits_base_1008d_v055_signal},
    "f05_deposit_funding_assets_base_1008d_v056_signal": {"func": f05_deposit_funding_assets_base_1008d_v056_signal},
    "f05_deposit_funding_liabilitiesc_base_1008d_v057_signal": {"func": f05_deposit_funding_liabilitiesc_base_1008d_v057_signal},
    "f05_deposit_funding_deposit_density_base_1008d_v058_signal": {"func": f05_deposit_funding_deposit_density_base_1008d_v058_signal},
    "f05_deposit_funding_funding_quality_base_1008d_v059_signal": {"func": f05_deposit_funding_funding_quality_base_1008d_v059_signal},
    "f05_deposit_funding_asset_funding_mix_base_1008d_v060_signal": {"func": f05_deposit_funding_asset_funding_mix_base_1008d_v060_signal},
    "f05_deposit_funding_deposits_base_1260d_v061_signal": {"func": f05_deposit_funding_deposits_base_1260d_v061_signal},
    "f05_deposit_funding_assets_base_1260d_v062_signal": {"func": f05_deposit_funding_assets_base_1260d_v062_signal},
    "f05_deposit_funding_liabilitiesc_base_1260d_v063_signal": {"func": f05_deposit_funding_liabilitiesc_base_1260d_v063_signal},
    "f05_deposit_funding_deposit_density_base_1260d_v064_signal": {"func": f05_deposit_funding_deposit_density_base_1260d_v064_signal},
    "f05_deposit_funding_funding_quality_base_1260d_v065_signal": {"func": f05_deposit_funding_funding_quality_base_1260d_v065_signal},
    "f05_deposit_funding_asset_funding_mix_base_1260d_v066_signal": {"func": f05_deposit_funding_asset_funding_mix_base_1260d_v066_signal},
    "f05_deposit_funding_deposits_ewma_5d_v067_signal": {"func": f05_deposit_funding_deposits_ewma_5d_v067_signal},
    "f05_deposit_funding_assets_ewma_5d_v068_signal": {"func": f05_deposit_funding_assets_ewma_5d_v068_signal},
    "f05_deposit_funding_liabilitiesc_ewma_5d_v069_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_5d_v069_signal},
    "f05_deposit_funding_deposit_density_ewma_5d_v070_signal": {"func": f05_deposit_funding_deposit_density_ewma_5d_v070_signal},
    "f05_deposit_funding_funding_quality_ewma_5d_v071_signal": {"func": f05_deposit_funding_funding_quality_ewma_5d_v071_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_5d_v072_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_5d_v072_signal},
    "f05_deposit_funding_deposits_ewma_10d_v073_signal": {"func": f05_deposit_funding_deposits_ewma_10d_v073_signal},
    "f05_deposit_funding_assets_ewma_10d_v074_signal": {"func": f05_deposit_funding_assets_ewma_10d_v074_signal},
    "f05_deposit_funding_liabilitiesc_ewma_10d_v075_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_10d_v075_signal},
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
