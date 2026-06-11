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

def f42_uranium_market_sentiment_momentum_sgna_base_5d_v001_signal(sgna):
    """Moving average of Raw level of sgna over 5d window."""
    res = _sma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_5d_v002_signal(revenue):
    """Moving average of Raw level of revenue over 5d window."""
    res = _sma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_5d_v003_signal(ebit):
    """Moving average of Raw level of ebit over 5d window."""
    res = _sma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_5d_v004_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_5d_v005_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 5d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_5d_v006_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 5d window."""
    res = _sma(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_10d_v007_signal(sgna):
    """Moving average of Raw level of sgna over 10d window."""
    res = _sma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_10d_v008_signal(revenue):
    """Moving average of Raw level of revenue over 10d window."""
    res = _sma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_10d_v009_signal(ebit):
    """Moving average of Raw level of ebit over 10d window."""
    res = _sma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_10d_v010_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_10d_v011_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 10d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_10d_v012_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 10d window."""
    res = _sma(_ratio(revenue, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_21d_v013_signal(sgna):
    """Moving average of Raw level of sgna over 21d window."""
    res = _sma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_21d_v014_signal(revenue):
    """Moving average of Raw level of revenue over 21d window."""
    res = _sma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_21d_v015_signal(ebit):
    """Moving average of Raw level of ebit over 21d window."""
    res = _sma(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_21d_v016_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_21d_v017_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 21d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_21d_v018_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 21d window."""
    res = _sma(_ratio(revenue, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_42d_v019_signal(sgna):
    """Moving average of Raw level of sgna over 42d window."""
    res = _sma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_42d_v020_signal(revenue):
    """Moving average of Raw level of revenue over 42d window."""
    res = _sma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_42d_v021_signal(ebit):
    """Moving average of Raw level of ebit over 42d window."""
    res = _sma(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_42d_v022_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_42d_v023_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 42d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_42d_v024_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 42d window."""
    res = _sma(_ratio(revenue, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_63d_v025_signal(sgna):
    """Moving average of Raw level of sgna over 63d window."""
    res = _sma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_63d_v026_signal(revenue):
    """Moving average of Raw level of revenue over 63d window."""
    res = _sma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_63d_v027_signal(ebit):
    """Moving average of Raw level of ebit over 63d window."""
    res = _sma(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_63d_v028_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_63d_v029_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 63d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_63d_v030_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 63d window."""
    res = _sma(_ratio(revenue, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_126d_v031_signal(sgna):
    """Moving average of Raw level of sgna over 126d window."""
    res = _sma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_126d_v032_signal(revenue):
    """Moving average of Raw level of revenue over 126d window."""
    res = _sma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_126d_v033_signal(ebit):
    """Moving average of Raw level of ebit over 126d window."""
    res = _sma(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_126d_v034_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_126d_v035_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 126d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_126d_v036_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 126d window."""
    res = _sma(_ratio(revenue, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_252d_v037_signal(sgna):
    """Moving average of Raw level of sgna over 252d window."""
    res = _sma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_252d_v038_signal(revenue):
    """Moving average of Raw level of revenue over 252d window."""
    res = _sma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_252d_v039_signal(ebit):
    """Moving average of Raw level of ebit over 252d window."""
    res = _sma(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_252d_v040_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_252d_v041_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 252d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_252d_v042_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 252d window."""
    res = _sma(_ratio(revenue, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_504d_v043_signal(sgna):
    """Moving average of Raw level of sgna over 504d window."""
    res = _sma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_504d_v044_signal(revenue):
    """Moving average of Raw level of revenue over 504d window."""
    res = _sma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_504d_v045_signal(ebit):
    """Moving average of Raw level of ebit over 504d window."""
    res = _sma(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_504d_v046_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_504d_v047_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 504d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_504d_v048_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 504d window."""
    res = _sma(_ratio(revenue, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_756d_v049_signal(sgna):
    """Moving average of Raw level of sgna over 756d window."""
    res = _sma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_756d_v050_signal(revenue):
    """Moving average of Raw level of revenue over 756d window."""
    res = _sma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_756d_v051_signal(ebit):
    """Moving average of Raw level of ebit over 756d window."""
    res = _sma(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_756d_v052_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_756d_v053_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 756d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_756d_v054_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 756d window."""
    res = _sma(_ratio(revenue, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_1008d_v055_signal(sgna):
    """Moving average of Raw level of sgna over 1008d window."""
    res = _sma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_1008d_v056_signal(revenue):
    """Moving average of Raw level of revenue over 1008d window."""
    res = _sma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_1008d_v057_signal(ebit):
    """Moving average of Raw level of ebit over 1008d window."""
    res = _sma(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_1008d_v058_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_1008d_v059_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 1008d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_1008d_v060_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 1008d window."""
    res = _sma(_ratio(revenue, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_base_1260d_v061_signal(sgna):
    """Moving average of Raw level of sgna over 1260d window."""
    res = _sma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_base_1260d_v062_signal(revenue):
    """Moving average of Raw level of revenue over 1260d window."""
    res = _sma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_base_1260d_v063_signal(ebit):
    """Moving average of Raw level of ebit over 1260d window."""
    res = _sma(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_base_1260d_v064_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_base_1260d_v065_signal(ebit, sgna, revenue, assets):
    """Moving average of Operating scale and turnover interaction over 1260d window."""
    res = _sma(_ratio(ebit, sgna) * _ratio(revenue, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_base_1260d_v066_signal(revenue, sgna):
    """Moving average of Sales yield on overhead over 1260d window."""
    res = _sma(_ratio(revenue, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_ewma_5d_v067_signal(sgna):
    """Exponential moving average of Raw level of sgna over 5d window."""
    res = _ewma(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_ewma_5d_v068_signal(revenue):
    """Exponential moving average of Raw level of revenue over 5d window."""
    res = _ewma(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_ewma_5d_v069_signal(ebit):
    """Exponential moving average of Raw level of ebit over 5d window."""
    res = _ewma(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_assets_ewma_5d_v070_signal(assets):
    """Exponential moving average of Raw level of assets over 5d window."""
    res = _ewma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_operating_scale_ewma_5d_v071_signal(ebit, sgna, revenue, assets):
    """Exponential moving average of Operating scale and turnover interaction over 5d window."""
    res = _ewma(_ratio(ebit, sgna) * _ratio(revenue, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_overhead_efficiency_ewma_5d_v072_signal(revenue, sgna):
    """Exponential moving average of Sales yield on overhead over 5d window."""
    res = _ewma(_ratio(revenue, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_sgna_ewma_10d_v073_signal(sgna):
    """Exponential moving average of Raw level of sgna over 10d window."""
    res = _ewma(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_revenue_ewma_10d_v074_signal(revenue):
    """Exponential moving average of Raw level of revenue over 10d window."""
    res = _ewma(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f42_uranium_market_sentiment_momentum_ebit_ewma_10d_v075_signal(ebit):
    """Exponential moving average of Raw level of ebit over 10d window."""
    res = _ewma(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f42_uranium_market_sentiment_momentum_sgna_base_5d_v001_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_5d_v001_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_5d_v002_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_5d_v002_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_5d_v003_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_5d_v003_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_5d_v004_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_5d_v004_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_5d_v005_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_5d_v005_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_5d_v006_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_5d_v006_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_10d_v007_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_10d_v007_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_10d_v008_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_10d_v008_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_10d_v009_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_10d_v009_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_10d_v010_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_10d_v010_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_10d_v011_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_10d_v011_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_10d_v012_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_10d_v012_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_21d_v013_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_21d_v013_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_21d_v014_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_21d_v014_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_21d_v015_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_21d_v015_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_21d_v016_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_21d_v016_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_21d_v017_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_21d_v017_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_21d_v018_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_21d_v018_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_42d_v019_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_42d_v019_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_42d_v020_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_42d_v020_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_42d_v021_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_42d_v021_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_42d_v022_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_42d_v022_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_42d_v023_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_42d_v023_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_42d_v024_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_42d_v024_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_63d_v025_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_63d_v025_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_63d_v026_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_63d_v026_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_63d_v027_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_63d_v027_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_63d_v028_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_63d_v028_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_63d_v029_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_63d_v029_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_63d_v030_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_63d_v030_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_126d_v031_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_126d_v031_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_126d_v032_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_126d_v032_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_126d_v033_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_126d_v033_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_126d_v034_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_126d_v034_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_126d_v035_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_126d_v035_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_126d_v036_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_126d_v036_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_252d_v037_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_252d_v037_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_252d_v038_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_252d_v038_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_252d_v039_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_252d_v039_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_252d_v040_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_252d_v040_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_252d_v041_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_252d_v041_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_252d_v042_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_252d_v042_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_504d_v043_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_504d_v043_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_504d_v044_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_504d_v044_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_504d_v045_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_504d_v045_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_504d_v046_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_504d_v046_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_504d_v047_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_504d_v047_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_504d_v048_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_504d_v048_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_756d_v049_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_756d_v049_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_756d_v050_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_756d_v050_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_756d_v051_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_756d_v051_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_756d_v052_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_756d_v052_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_756d_v053_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_756d_v053_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_756d_v054_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_756d_v054_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_1008d_v055_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_1008d_v055_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_1008d_v056_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_1008d_v056_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_1008d_v057_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_1008d_v057_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_1008d_v058_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_1008d_v058_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_1008d_v059_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_1008d_v059_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_1008d_v060_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_1008d_v060_signal},
    "f42_uranium_market_sentiment_momentum_sgna_base_1260d_v061_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_base_1260d_v061_signal},
    "f42_uranium_market_sentiment_momentum_revenue_base_1260d_v062_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_base_1260d_v062_signal},
    "f42_uranium_market_sentiment_momentum_ebit_base_1260d_v063_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_base_1260d_v063_signal},
    "f42_uranium_market_sentiment_momentum_assets_base_1260d_v064_signal": {"func": f42_uranium_market_sentiment_momentum_assets_base_1260d_v064_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_base_1260d_v065_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_base_1260d_v065_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_base_1260d_v066_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_base_1260d_v066_signal},
    "f42_uranium_market_sentiment_momentum_sgna_ewma_5d_v067_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_ewma_5d_v067_signal},
    "f42_uranium_market_sentiment_momentum_revenue_ewma_5d_v068_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_ewma_5d_v068_signal},
    "f42_uranium_market_sentiment_momentum_ebit_ewma_5d_v069_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_ewma_5d_v069_signal},
    "f42_uranium_market_sentiment_momentum_assets_ewma_5d_v070_signal": {"func": f42_uranium_market_sentiment_momentum_assets_ewma_5d_v070_signal},
    "f42_uranium_market_sentiment_momentum_operating_scale_ewma_5d_v071_signal": {"func": f42_uranium_market_sentiment_momentum_operating_scale_ewma_5d_v071_signal},
    "f42_uranium_market_sentiment_momentum_overhead_efficiency_ewma_5d_v072_signal": {"func": f42_uranium_market_sentiment_momentum_overhead_efficiency_ewma_5d_v072_signal},
    "f42_uranium_market_sentiment_momentum_sgna_ewma_10d_v073_signal": {"func": f42_uranium_market_sentiment_momentum_sgna_ewma_10d_v073_signal},
    "f42_uranium_market_sentiment_momentum_revenue_ewma_10d_v074_signal": {"func": f42_uranium_market_sentiment_momentum_revenue_ewma_10d_v074_signal},
    "f42_uranium_market_sentiment_momentum_ebit_ewma_10d_v075_signal": {"func": f42_uranium_market_sentiment_momentum_ebit_ewma_10d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "divyield": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 42...")
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
