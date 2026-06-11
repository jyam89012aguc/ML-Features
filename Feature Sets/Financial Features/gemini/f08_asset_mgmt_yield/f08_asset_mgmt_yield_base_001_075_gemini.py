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

def f08_asset_mgmt_yield_netinc_base_5d_v001_signal(netinc):
    """Moving average of Raw level of netinc over 5d window."""
    res = _sma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_5d_v002_signal(invcap):
    """Moving average of Raw level of invcap over 5d window."""
    res = _sma(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_5d_v003_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_5d_v004_signal(netinc, invcap):
    """Moving average of Return on invested capital over 5d window."""
    res = _sma(_ratio(netinc, invcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_5d_v005_signal(revenue, assets):
    """Moving average of Total asset utilization over 5d window."""
    res = _sma(_ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_10d_v006_signal(netinc):
    """Moving average of Raw level of netinc over 10d window."""
    res = _sma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_10d_v007_signal(invcap):
    """Moving average of Raw level of invcap over 10d window."""
    res = _sma(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_10d_v008_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_10d_v009_signal(netinc, invcap):
    """Moving average of Return on invested capital over 10d window."""
    res = _sma(_ratio(netinc, invcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_10d_v010_signal(revenue, assets):
    """Moving average of Total asset utilization over 10d window."""
    res = _sma(_ratio(revenue, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_21d_v011_signal(netinc):
    """Moving average of Raw level of netinc over 21d window."""
    res = _sma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_21d_v012_signal(invcap):
    """Moving average of Raw level of invcap over 21d window."""
    res = _sma(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_21d_v013_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_21d_v014_signal(netinc, invcap):
    """Moving average of Return on invested capital over 21d window."""
    res = _sma(_ratio(netinc, invcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_21d_v015_signal(revenue, assets):
    """Moving average of Total asset utilization over 21d window."""
    res = _sma(_ratio(revenue, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_42d_v016_signal(netinc):
    """Moving average of Raw level of netinc over 42d window."""
    res = _sma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_42d_v017_signal(invcap):
    """Moving average of Raw level of invcap over 42d window."""
    res = _sma(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_42d_v018_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_42d_v019_signal(netinc, invcap):
    """Moving average of Return on invested capital over 42d window."""
    res = _sma(_ratio(netinc, invcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_42d_v020_signal(revenue, assets):
    """Moving average of Total asset utilization over 42d window."""
    res = _sma(_ratio(revenue, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_63d_v021_signal(netinc):
    """Moving average of Raw level of netinc over 63d window."""
    res = _sma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_63d_v022_signal(invcap):
    """Moving average of Raw level of invcap over 63d window."""
    res = _sma(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_63d_v023_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_63d_v024_signal(netinc, invcap):
    """Moving average of Return on invested capital over 63d window."""
    res = _sma(_ratio(netinc, invcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_63d_v025_signal(revenue, assets):
    """Moving average of Total asset utilization over 63d window."""
    res = _sma(_ratio(revenue, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_126d_v026_signal(netinc):
    """Moving average of Raw level of netinc over 126d window."""
    res = _sma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_126d_v027_signal(invcap):
    """Moving average of Raw level of invcap over 126d window."""
    res = _sma(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_126d_v028_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_126d_v029_signal(netinc, invcap):
    """Moving average of Return on invested capital over 126d window."""
    res = _sma(_ratio(netinc, invcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_126d_v030_signal(revenue, assets):
    """Moving average of Total asset utilization over 126d window."""
    res = _sma(_ratio(revenue, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_252d_v031_signal(netinc):
    """Moving average of Raw level of netinc over 252d window."""
    res = _sma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_252d_v032_signal(invcap):
    """Moving average of Raw level of invcap over 252d window."""
    res = _sma(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_252d_v033_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_252d_v034_signal(netinc, invcap):
    """Moving average of Return on invested capital over 252d window."""
    res = _sma(_ratio(netinc, invcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_252d_v035_signal(revenue, assets):
    """Moving average of Total asset utilization over 252d window."""
    res = _sma(_ratio(revenue, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_504d_v036_signal(netinc):
    """Moving average of Raw level of netinc over 504d window."""
    res = _sma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_504d_v037_signal(invcap):
    """Moving average of Raw level of invcap over 504d window."""
    res = _sma(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_504d_v038_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_504d_v039_signal(netinc, invcap):
    """Moving average of Return on invested capital over 504d window."""
    res = _sma(_ratio(netinc, invcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_504d_v040_signal(revenue, assets):
    """Moving average of Total asset utilization over 504d window."""
    res = _sma(_ratio(revenue, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_756d_v041_signal(netinc):
    """Moving average of Raw level of netinc over 756d window."""
    res = _sma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_756d_v042_signal(invcap):
    """Moving average of Raw level of invcap over 756d window."""
    res = _sma(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_756d_v043_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_756d_v044_signal(netinc, invcap):
    """Moving average of Return on invested capital over 756d window."""
    res = _sma(_ratio(netinc, invcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_756d_v045_signal(revenue, assets):
    """Moving average of Total asset utilization over 756d window."""
    res = _sma(_ratio(revenue, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_1008d_v046_signal(netinc):
    """Moving average of Raw level of netinc over 1008d window."""
    res = _sma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_1008d_v047_signal(invcap):
    """Moving average of Raw level of invcap over 1008d window."""
    res = _sma(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_1008d_v048_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_1008d_v049_signal(netinc, invcap):
    """Moving average of Return on invested capital over 1008d window."""
    res = _sma(_ratio(netinc, invcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_1008d_v050_signal(revenue, assets):
    """Moving average of Total asset utilization over 1008d window."""
    res = _sma(_ratio(revenue, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_base_1260d_v051_signal(netinc):
    """Moving average of Raw level of netinc over 1260d window."""
    res = _sma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_base_1260d_v052_signal(invcap):
    """Moving average of Raw level of invcap over 1260d window."""
    res = _sma(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_base_1260d_v053_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_base_1260d_v054_signal(netinc, invcap):
    """Moving average of Return on invested capital over 1260d window."""
    res = _sma(_ratio(netinc, invcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_base_1260d_v055_signal(revenue, assets):
    """Moving average of Total asset utilization over 1260d window."""
    res = _sma(_ratio(revenue, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_5d_v056_signal(netinc):
    """Exponential moving average of Raw level of netinc over 5d window."""
    res = _ewma(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_5d_v057_signal(invcap):
    """Exponential moving average of Raw level of invcap over 5d window."""
    res = _ewma(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_5d_v058_signal(assets):
    """Exponential moving average of Raw level of assets over 5d window."""
    res = _ewma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_5d_v059_signal(netinc, invcap):
    """Exponential moving average of Return on invested capital over 5d window."""
    res = _ewma(_ratio(netinc, invcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_5d_v060_signal(revenue, assets):
    """Exponential moving average of Total asset utilization over 5d window."""
    res = _ewma(_ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_10d_v061_signal(netinc):
    """Exponential moving average of Raw level of netinc over 10d window."""
    res = _ewma(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_10d_v062_signal(invcap):
    """Exponential moving average of Raw level of invcap over 10d window."""
    res = _ewma(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_10d_v063_signal(assets):
    """Exponential moving average of Raw level of assets over 10d window."""
    res = _ewma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_10d_v064_signal(netinc, invcap):
    """Exponential moving average of Return on invested capital over 10d window."""
    res = _ewma(_ratio(netinc, invcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_10d_v065_signal(revenue, assets):
    """Exponential moving average of Total asset utilization over 10d window."""
    res = _ewma(_ratio(revenue, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_21d_v066_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_21d_v067_signal(invcap):
    """Exponential moving average of Raw level of invcap over 21d window."""
    res = _ewma(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_21d_v068_signal(assets):
    """Exponential moving average of Raw level of assets over 21d window."""
    res = _ewma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_21d_v069_signal(netinc, invcap):
    """Exponential moving average of Return on invested capital over 21d window."""
    res = _ewma(_ratio(netinc, invcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_21d_v070_signal(revenue, assets):
    """Exponential moving average of Total asset utilization over 21d window."""
    res = _ewma(_ratio(revenue, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_netinc_ewma_42d_v071_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_invcap_ewma_42d_v072_signal(invcap):
    """Exponential moving average of Raw level of invcap over 42d window."""
    res = _ewma(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_assets_ewma_42d_v073_signal(assets):
    """Exponential moving average of Raw level of assets over 42d window."""
    res = _ewma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_roic_ewma_42d_v074_signal(netinc, invcap):
    """Exponential moving average of Return on invested capital over 42d window."""
    res = _ewma(_ratio(netinc, invcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f08_asset_mgmt_yield_asset_turnover_ewma_42d_v075_signal(revenue, assets):
    """Exponential moving average of Total asset utilization over 42d window."""
    res = _ewma(_ratio(revenue, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f08_asset_mgmt_yield_netinc_base_5d_v001_signal": {"func": f08_asset_mgmt_yield_netinc_base_5d_v001_signal},
    "f08_asset_mgmt_yield_invcap_base_5d_v002_signal": {"func": f08_asset_mgmt_yield_invcap_base_5d_v002_signal},
    "f08_asset_mgmt_yield_assets_base_5d_v003_signal": {"func": f08_asset_mgmt_yield_assets_base_5d_v003_signal},
    "f08_asset_mgmt_yield_roic_base_5d_v004_signal": {"func": f08_asset_mgmt_yield_roic_base_5d_v004_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_5d_v005_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_5d_v005_signal},
    "f08_asset_mgmt_yield_netinc_base_10d_v006_signal": {"func": f08_asset_mgmt_yield_netinc_base_10d_v006_signal},
    "f08_asset_mgmt_yield_invcap_base_10d_v007_signal": {"func": f08_asset_mgmt_yield_invcap_base_10d_v007_signal},
    "f08_asset_mgmt_yield_assets_base_10d_v008_signal": {"func": f08_asset_mgmt_yield_assets_base_10d_v008_signal},
    "f08_asset_mgmt_yield_roic_base_10d_v009_signal": {"func": f08_asset_mgmt_yield_roic_base_10d_v009_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_10d_v010_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_10d_v010_signal},
    "f08_asset_mgmt_yield_netinc_base_21d_v011_signal": {"func": f08_asset_mgmt_yield_netinc_base_21d_v011_signal},
    "f08_asset_mgmt_yield_invcap_base_21d_v012_signal": {"func": f08_asset_mgmt_yield_invcap_base_21d_v012_signal},
    "f08_asset_mgmt_yield_assets_base_21d_v013_signal": {"func": f08_asset_mgmt_yield_assets_base_21d_v013_signal},
    "f08_asset_mgmt_yield_roic_base_21d_v014_signal": {"func": f08_asset_mgmt_yield_roic_base_21d_v014_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_21d_v015_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_21d_v015_signal},
    "f08_asset_mgmt_yield_netinc_base_42d_v016_signal": {"func": f08_asset_mgmt_yield_netinc_base_42d_v016_signal},
    "f08_asset_mgmt_yield_invcap_base_42d_v017_signal": {"func": f08_asset_mgmt_yield_invcap_base_42d_v017_signal},
    "f08_asset_mgmt_yield_assets_base_42d_v018_signal": {"func": f08_asset_mgmt_yield_assets_base_42d_v018_signal},
    "f08_asset_mgmt_yield_roic_base_42d_v019_signal": {"func": f08_asset_mgmt_yield_roic_base_42d_v019_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_42d_v020_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_42d_v020_signal},
    "f08_asset_mgmt_yield_netinc_base_63d_v021_signal": {"func": f08_asset_mgmt_yield_netinc_base_63d_v021_signal},
    "f08_asset_mgmt_yield_invcap_base_63d_v022_signal": {"func": f08_asset_mgmt_yield_invcap_base_63d_v022_signal},
    "f08_asset_mgmt_yield_assets_base_63d_v023_signal": {"func": f08_asset_mgmt_yield_assets_base_63d_v023_signal},
    "f08_asset_mgmt_yield_roic_base_63d_v024_signal": {"func": f08_asset_mgmt_yield_roic_base_63d_v024_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_63d_v025_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_63d_v025_signal},
    "f08_asset_mgmt_yield_netinc_base_126d_v026_signal": {"func": f08_asset_mgmt_yield_netinc_base_126d_v026_signal},
    "f08_asset_mgmt_yield_invcap_base_126d_v027_signal": {"func": f08_asset_mgmt_yield_invcap_base_126d_v027_signal},
    "f08_asset_mgmt_yield_assets_base_126d_v028_signal": {"func": f08_asset_mgmt_yield_assets_base_126d_v028_signal},
    "f08_asset_mgmt_yield_roic_base_126d_v029_signal": {"func": f08_asset_mgmt_yield_roic_base_126d_v029_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_126d_v030_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_126d_v030_signal},
    "f08_asset_mgmt_yield_netinc_base_252d_v031_signal": {"func": f08_asset_mgmt_yield_netinc_base_252d_v031_signal},
    "f08_asset_mgmt_yield_invcap_base_252d_v032_signal": {"func": f08_asset_mgmt_yield_invcap_base_252d_v032_signal},
    "f08_asset_mgmt_yield_assets_base_252d_v033_signal": {"func": f08_asset_mgmt_yield_assets_base_252d_v033_signal},
    "f08_asset_mgmt_yield_roic_base_252d_v034_signal": {"func": f08_asset_mgmt_yield_roic_base_252d_v034_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_252d_v035_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_252d_v035_signal},
    "f08_asset_mgmt_yield_netinc_base_504d_v036_signal": {"func": f08_asset_mgmt_yield_netinc_base_504d_v036_signal},
    "f08_asset_mgmt_yield_invcap_base_504d_v037_signal": {"func": f08_asset_mgmt_yield_invcap_base_504d_v037_signal},
    "f08_asset_mgmt_yield_assets_base_504d_v038_signal": {"func": f08_asset_mgmt_yield_assets_base_504d_v038_signal},
    "f08_asset_mgmt_yield_roic_base_504d_v039_signal": {"func": f08_asset_mgmt_yield_roic_base_504d_v039_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_504d_v040_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_504d_v040_signal},
    "f08_asset_mgmt_yield_netinc_base_756d_v041_signal": {"func": f08_asset_mgmt_yield_netinc_base_756d_v041_signal},
    "f08_asset_mgmt_yield_invcap_base_756d_v042_signal": {"func": f08_asset_mgmt_yield_invcap_base_756d_v042_signal},
    "f08_asset_mgmt_yield_assets_base_756d_v043_signal": {"func": f08_asset_mgmt_yield_assets_base_756d_v043_signal},
    "f08_asset_mgmt_yield_roic_base_756d_v044_signal": {"func": f08_asset_mgmt_yield_roic_base_756d_v044_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_756d_v045_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_756d_v045_signal},
    "f08_asset_mgmt_yield_netinc_base_1008d_v046_signal": {"func": f08_asset_mgmt_yield_netinc_base_1008d_v046_signal},
    "f08_asset_mgmt_yield_invcap_base_1008d_v047_signal": {"func": f08_asset_mgmt_yield_invcap_base_1008d_v047_signal},
    "f08_asset_mgmt_yield_assets_base_1008d_v048_signal": {"func": f08_asset_mgmt_yield_assets_base_1008d_v048_signal},
    "f08_asset_mgmt_yield_roic_base_1008d_v049_signal": {"func": f08_asset_mgmt_yield_roic_base_1008d_v049_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_1008d_v050_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_1008d_v050_signal},
    "f08_asset_mgmt_yield_netinc_base_1260d_v051_signal": {"func": f08_asset_mgmt_yield_netinc_base_1260d_v051_signal},
    "f08_asset_mgmt_yield_invcap_base_1260d_v052_signal": {"func": f08_asset_mgmt_yield_invcap_base_1260d_v052_signal},
    "f08_asset_mgmt_yield_assets_base_1260d_v053_signal": {"func": f08_asset_mgmt_yield_assets_base_1260d_v053_signal},
    "f08_asset_mgmt_yield_roic_base_1260d_v054_signal": {"func": f08_asset_mgmt_yield_roic_base_1260d_v054_signal},
    "f08_asset_mgmt_yield_asset_turnover_base_1260d_v055_signal": {"func": f08_asset_mgmt_yield_asset_turnover_base_1260d_v055_signal},
    "f08_asset_mgmt_yield_netinc_ewma_5d_v056_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_5d_v056_signal},
    "f08_asset_mgmt_yield_invcap_ewma_5d_v057_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_5d_v057_signal},
    "f08_asset_mgmt_yield_assets_ewma_5d_v058_signal": {"func": f08_asset_mgmt_yield_assets_ewma_5d_v058_signal},
    "f08_asset_mgmt_yield_roic_ewma_5d_v059_signal": {"func": f08_asset_mgmt_yield_roic_ewma_5d_v059_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_5d_v060_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_5d_v060_signal},
    "f08_asset_mgmt_yield_netinc_ewma_10d_v061_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_10d_v061_signal},
    "f08_asset_mgmt_yield_invcap_ewma_10d_v062_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_10d_v062_signal},
    "f08_asset_mgmt_yield_assets_ewma_10d_v063_signal": {"func": f08_asset_mgmt_yield_assets_ewma_10d_v063_signal},
    "f08_asset_mgmt_yield_roic_ewma_10d_v064_signal": {"func": f08_asset_mgmt_yield_roic_ewma_10d_v064_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_10d_v065_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_10d_v065_signal},
    "f08_asset_mgmt_yield_netinc_ewma_21d_v066_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_21d_v066_signal},
    "f08_asset_mgmt_yield_invcap_ewma_21d_v067_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_21d_v067_signal},
    "f08_asset_mgmt_yield_assets_ewma_21d_v068_signal": {"func": f08_asset_mgmt_yield_assets_ewma_21d_v068_signal},
    "f08_asset_mgmt_yield_roic_ewma_21d_v069_signal": {"func": f08_asset_mgmt_yield_roic_ewma_21d_v069_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_21d_v070_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_21d_v070_signal},
    "f08_asset_mgmt_yield_netinc_ewma_42d_v071_signal": {"func": f08_asset_mgmt_yield_netinc_ewma_42d_v071_signal},
    "f08_asset_mgmt_yield_invcap_ewma_42d_v072_signal": {"func": f08_asset_mgmt_yield_invcap_ewma_42d_v072_signal},
    "f08_asset_mgmt_yield_assets_ewma_42d_v073_signal": {"func": f08_asset_mgmt_yield_assets_ewma_42d_v073_signal},
    "f08_asset_mgmt_yield_roic_ewma_42d_v074_signal": {"func": f08_asset_mgmt_yield_roic_ewma_42d_v074_signal},
    "f08_asset_mgmt_yield_asset_turnover_ewma_42d_v075_signal": {"func": f08_asset_mgmt_yield_asset_turnover_ewma_42d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 08...")
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
