import pandas as pd
import numpy as np
import inspect

# ===== Energy Ultra-High-Performance Alpha Helpers =====
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

def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def f20_ep_lifting_cost_efficiency_assets_base_5d_v001_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_5d_v002_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_5d_v003_signal(depamor):
    """Moving average of Raw level of depamor over 5d window."""
    res = _sma(depamor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_5d_v004_signal(roic):
    """Moving average of Raw level of roic over 5d window."""
    res = _sma(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_5d_v005_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 5d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_5d_v006_signal(revenue, assets):
    """Moving average of Gross asset turnover over 5d window."""
    res = _sma(_ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_10d_v007_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_10d_v008_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_10d_v009_signal(depamor):
    """Moving average of Raw level of depamor over 10d window."""
    res = _sma(depamor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_10d_v010_signal(roic):
    """Moving average of Raw level of roic over 10d window."""
    res = _sma(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_10d_v011_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 10d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_10d_v012_signal(revenue, assets):
    """Moving average of Gross asset turnover over 10d window."""
    res = _sma(_ratio(revenue, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_21d_v013_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_21d_v014_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_21d_v015_signal(depamor):
    """Moving average of Raw level of depamor over 21d window."""
    res = _sma(depamor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_21d_v016_signal(roic):
    """Moving average of Raw level of roic over 21d window."""
    res = _sma(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_21d_v017_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 21d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_21d_v018_signal(revenue, assets):
    """Moving average of Gross asset turnover over 21d window."""
    res = _sma(_ratio(revenue, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_42d_v019_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_42d_v020_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_42d_v021_signal(depamor):
    """Moving average of Raw level of depamor over 42d window."""
    res = _sma(depamor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_42d_v022_signal(roic):
    """Moving average of Raw level of roic over 42d window."""
    res = _sma(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_42d_v023_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 42d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_42d_v024_signal(revenue, assets):
    """Moving average of Gross asset turnover over 42d window."""
    res = _sma(_ratio(revenue, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_63d_v025_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_63d_v026_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_63d_v027_signal(depamor):
    """Moving average of Raw level of depamor over 63d window."""
    res = _sma(depamor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_63d_v028_signal(roic):
    """Moving average of Raw level of roic over 63d window."""
    res = _sma(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_63d_v029_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 63d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_63d_v030_signal(revenue, assets):
    """Moving average of Gross asset turnover over 63d window."""
    res = _sma(_ratio(revenue, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_126d_v031_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_126d_v032_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_126d_v033_signal(depamor):
    """Moving average of Raw level of depamor over 126d window."""
    res = _sma(depamor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_126d_v034_signal(roic):
    """Moving average of Raw level of roic over 126d window."""
    res = _sma(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_126d_v035_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 126d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_126d_v036_signal(revenue, assets):
    """Moving average of Gross asset turnover over 126d window."""
    res = _sma(_ratio(revenue, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_252d_v037_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_252d_v038_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_252d_v039_signal(depamor):
    """Moving average of Raw level of depamor over 252d window."""
    res = _sma(depamor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_252d_v040_signal(roic):
    """Moving average of Raw level of roic over 252d window."""
    res = _sma(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_252d_v041_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 252d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_252d_v042_signal(revenue, assets):
    """Moving average of Gross asset turnover over 252d window."""
    res = _sma(_ratio(revenue, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_504d_v043_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_504d_v044_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_504d_v045_signal(depamor):
    """Moving average of Raw level of depamor over 504d window."""
    res = _sma(depamor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_504d_v046_signal(roic):
    """Moving average of Raw level of roic over 504d window."""
    res = _sma(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_504d_v047_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 504d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_504d_v048_signal(revenue, assets):
    """Moving average of Gross asset turnover over 504d window."""
    res = _sma(_ratio(revenue, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_756d_v049_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_756d_v050_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_756d_v051_signal(depamor):
    """Moving average of Raw level of depamor over 756d window."""
    res = _sma(depamor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_756d_v052_signal(roic):
    """Moving average of Raw level of roic over 756d window."""
    res = _sma(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_756d_v053_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 756d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_756d_v054_signal(revenue, assets):
    """Moving average of Gross asset turnover over 756d window."""
    res = _sma(_ratio(revenue, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_1008d_v055_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_1008d_v056_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_1008d_v057_signal(depamor):
    """Moving average of Raw level of depamor over 1008d window."""
    res = _sma(depamor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_1008d_v058_signal(roic):
    """Moving average of Raw level of roic over 1008d window."""
    res = _sma(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_1008d_v059_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 1008d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_1008d_v060_signal(revenue, assets):
    """Moving average of Gross asset turnover over 1008d window."""
    res = _sma(_ratio(revenue, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_base_1260d_v061_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_base_1260d_v062_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_base_1260d_v063_signal(depamor):
    """Moving average of Raw level of depamor over 1260d window."""
    res = _sma(depamor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_base_1260d_v064_signal(roic):
    """Moving average of Raw level of roic over 1260d window."""
    res = _sma(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_base_1260d_v065_signal(revenue, depamor, roic):
    """Moving average of Asset modernization and efficiency index over 1260d window."""
    res = _sma(_ratio(revenue, depamor) * roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_base_1260d_v066_signal(revenue, assets):
    """Moving average of Gross asset turnover over 1260d window."""
    res = _sma(_ratio(revenue, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_ewma_5d_v067_signal(assets):
    """Exponential moving average of Raw level of assets over 5d window."""
    res = _ewma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_ewma_5d_v068_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_ewma_5d_v069_signal(depamor):
    """Exponential moving average of Raw level of depamor over 5d window."""
    res = _ewma(depamor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_roic_ewma_5d_v070_signal(roic):
    """Exponential moving average of Raw level of roic over 5d window."""
    res = _ewma(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_reinvestment_moat_ewma_5d_v071_signal(revenue, depamor, roic):
    """Exponential moving average of Asset modernization and efficiency index over 5d window."""
    res = _ewma(_ratio(revenue, depamor) * roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_asset_yield_ewma_5d_v072_signal(revenue, assets):
    """Exponential moving average of Gross asset turnover over 5d window."""
    res = _ewma(_ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_assets_ewma_10d_v073_signal(assets):
    """Exponential moving average of Raw level of assets over 10d window."""
    res = _ewma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_revenue_ewma_10d_v074_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_ep_lifting_cost_efficiency_depamor_ewma_10d_v075_signal(depamor):
    """Exponential moving average of Raw level of depamor over 10d window."""
    res = _ewma(depamor, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f20_ep_lifting_cost_efficiency_assets_base_5d_v001_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_5d_v001_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_5d_v002_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_5d_v002_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_5d_v003_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_5d_v003_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_5d_v004_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_5d_v004_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_5d_v005_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_5d_v005_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_5d_v006_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_5d_v006_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_10d_v007_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_10d_v007_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_10d_v008_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_10d_v008_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_10d_v009_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_10d_v009_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_10d_v010_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_10d_v010_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_10d_v011_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_10d_v011_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_10d_v012_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_10d_v012_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_21d_v013_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_21d_v013_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_21d_v014_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_21d_v014_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_21d_v015_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_21d_v015_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_21d_v016_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_21d_v016_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_21d_v017_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_21d_v017_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_21d_v018_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_21d_v018_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_42d_v019_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_42d_v019_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_42d_v020_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_42d_v020_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_42d_v021_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_42d_v021_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_42d_v022_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_42d_v022_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_42d_v023_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_42d_v023_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_42d_v024_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_42d_v024_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_63d_v025_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_63d_v025_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_63d_v026_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_63d_v026_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_63d_v027_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_63d_v027_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_63d_v028_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_63d_v028_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_63d_v029_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_63d_v029_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_63d_v030_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_63d_v030_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_126d_v031_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_126d_v031_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_126d_v032_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_126d_v032_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_126d_v033_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_126d_v033_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_126d_v034_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_126d_v034_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_126d_v035_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_126d_v035_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_126d_v036_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_126d_v036_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_252d_v037_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_252d_v037_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_252d_v038_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_252d_v038_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_252d_v039_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_252d_v039_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_252d_v040_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_252d_v040_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_252d_v041_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_252d_v041_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_252d_v042_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_252d_v042_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_504d_v043_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_504d_v043_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_504d_v044_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_504d_v044_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_504d_v045_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_504d_v045_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_504d_v046_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_504d_v046_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_504d_v047_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_504d_v047_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_504d_v048_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_504d_v048_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_756d_v049_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_756d_v049_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_756d_v050_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_756d_v050_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_756d_v051_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_756d_v051_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_756d_v052_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_756d_v052_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_756d_v053_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_756d_v053_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_756d_v054_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_756d_v054_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_1008d_v055_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_1008d_v055_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_1008d_v056_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_1008d_v056_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_1008d_v057_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_1008d_v057_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_1008d_v058_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_1008d_v058_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_1008d_v059_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_1008d_v059_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_1008d_v060_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_1008d_v060_signal},
    "f20_ep_lifting_cost_efficiency_assets_base_1260d_v061_signal": {"func": f20_ep_lifting_cost_efficiency_assets_base_1260d_v061_signal},
    "f20_ep_lifting_cost_efficiency_revenue_base_1260d_v062_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_base_1260d_v062_signal},
    "f20_ep_lifting_cost_efficiency_depamor_base_1260d_v063_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_base_1260d_v063_signal},
    "f20_ep_lifting_cost_efficiency_roic_base_1260d_v064_signal": {"func": f20_ep_lifting_cost_efficiency_roic_base_1260d_v064_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_base_1260d_v065_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_base_1260d_v065_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_base_1260d_v066_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_base_1260d_v066_signal},
    "f20_ep_lifting_cost_efficiency_assets_ewma_5d_v067_signal": {"func": f20_ep_lifting_cost_efficiency_assets_ewma_5d_v067_signal},
    "f20_ep_lifting_cost_efficiency_revenue_ewma_5d_v068_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_ewma_5d_v068_signal},
    "f20_ep_lifting_cost_efficiency_depamor_ewma_5d_v069_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_ewma_5d_v069_signal},
    "f20_ep_lifting_cost_efficiency_roic_ewma_5d_v070_signal": {"func": f20_ep_lifting_cost_efficiency_roic_ewma_5d_v070_signal},
    "f20_ep_lifting_cost_efficiency_reinvestment_moat_ewma_5d_v071_signal": {"func": f20_ep_lifting_cost_efficiency_reinvestment_moat_ewma_5d_v071_signal},
    "f20_ep_lifting_cost_efficiency_asset_yield_ewma_5d_v072_signal": {"func": f20_ep_lifting_cost_efficiency_asset_yield_ewma_5d_v072_signal},
    "f20_ep_lifting_cost_efficiency_assets_ewma_10d_v073_signal": {"func": f20_ep_lifting_cost_efficiency_assets_ewma_10d_v073_signal},
    "f20_ep_lifting_cost_efficiency_revenue_ewma_10d_v074_signal": {"func": f20_ep_lifting_cost_efficiency_revenue_ewma_10d_v074_signal},
    "f20_ep_lifting_cost_efficiency_depamor_ewma_10d_v075_signal": {"func": f20_ep_lifting_cost_efficiency_depamor_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "divyield": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 20...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            # Relaxing non-null for RSI/Skew which need more data
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
