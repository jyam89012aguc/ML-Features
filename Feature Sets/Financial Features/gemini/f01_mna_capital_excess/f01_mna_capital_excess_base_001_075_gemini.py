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

def f01_mna_capital_excess_equity_base_5d_v001_signal(equity):
    """Moving average of Raw level of equity over 5d window."""
    res = _sma(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_5d_v002_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_5d_v003_signal(pb):
    """Moving average of Raw level of pb over 5d window."""
    res = _sma(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_5d_v004_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 5d window."""
    res = _sma(_ratio(equity, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_5d_v005_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 5d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_5d_v006_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 5d window."""
    res = _sma(_ratio(marketcap, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_5d_v007_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 5d window."""
    res = _sma(_ratio(assets - equity, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_10d_v008_signal(equity):
    """Moving average of Raw level of equity over 10d window."""
    res = _sma(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_10d_v009_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_10d_v010_signal(pb):
    """Moving average of Raw level of pb over 10d window."""
    res = _sma(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_10d_v011_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 10d window."""
    res = _sma(_ratio(equity, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_10d_v012_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 10d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_10d_v013_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 10d window."""
    res = _sma(_ratio(marketcap, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_10d_v014_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 10d window."""
    res = _sma(_ratio(assets - equity, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_21d_v015_signal(equity):
    """Moving average of Raw level of equity over 21d window."""
    res = _sma(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_21d_v016_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_21d_v017_signal(pb):
    """Moving average of Raw level of pb over 21d window."""
    res = _sma(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_21d_v018_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 21d window."""
    res = _sma(_ratio(equity, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_21d_v019_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 21d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_21d_v020_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 21d window."""
    res = _sma(_ratio(marketcap, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_21d_v021_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 21d window."""
    res = _sma(_ratio(assets - equity, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_42d_v022_signal(equity):
    """Moving average of Raw level of equity over 42d window."""
    res = _sma(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_42d_v023_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_42d_v024_signal(pb):
    """Moving average of Raw level of pb over 42d window."""
    res = _sma(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_42d_v025_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 42d window."""
    res = _sma(_ratio(equity, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_42d_v026_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 42d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_42d_v027_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 42d window."""
    res = _sma(_ratio(marketcap, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_42d_v028_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 42d window."""
    res = _sma(_ratio(assets - equity, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_63d_v029_signal(equity):
    """Moving average of Raw level of equity over 63d window."""
    res = _sma(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_63d_v030_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_63d_v031_signal(pb):
    """Moving average of Raw level of pb over 63d window."""
    res = _sma(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_63d_v032_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 63d window."""
    res = _sma(_ratio(equity, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_63d_v033_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 63d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_63d_v034_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 63d window."""
    res = _sma(_ratio(marketcap, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_63d_v035_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 63d window."""
    res = _sma(_ratio(assets - equity, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_126d_v036_signal(equity):
    """Moving average of Raw level of equity over 126d window."""
    res = _sma(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_126d_v037_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_126d_v038_signal(pb):
    """Moving average of Raw level of pb over 126d window."""
    res = _sma(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_126d_v039_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 126d window."""
    res = _sma(_ratio(equity, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_126d_v040_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 126d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_126d_v041_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 126d window."""
    res = _sma(_ratio(marketcap, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_126d_v042_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 126d window."""
    res = _sma(_ratio(assets - equity, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_252d_v043_signal(equity):
    """Moving average of Raw level of equity over 252d window."""
    res = _sma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_252d_v044_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_252d_v045_signal(pb):
    """Moving average of Raw level of pb over 252d window."""
    res = _sma(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_252d_v046_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 252d window."""
    res = _sma(_ratio(equity, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_252d_v047_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 252d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_252d_v048_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 252d window."""
    res = _sma(_ratio(marketcap, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_252d_v049_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 252d window."""
    res = _sma(_ratio(assets - equity, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_504d_v050_signal(equity):
    """Moving average of Raw level of equity over 504d window."""
    res = _sma(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_504d_v051_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_504d_v052_signal(pb):
    """Moving average of Raw level of pb over 504d window."""
    res = _sma(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_504d_v053_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 504d window."""
    res = _sma(_ratio(equity, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_504d_v054_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 504d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_504d_v055_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 504d window."""
    res = _sma(_ratio(marketcap, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_504d_v056_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 504d window."""
    res = _sma(_ratio(assets - equity, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_756d_v057_signal(equity):
    """Moving average of Raw level of equity over 756d window."""
    res = _sma(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_756d_v058_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_756d_v059_signal(pb):
    """Moving average of Raw level of pb over 756d window."""
    res = _sma(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_756d_v060_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 756d window."""
    res = _sma(_ratio(equity, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_756d_v061_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 756d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_756d_v062_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 756d window."""
    res = _sma(_ratio(marketcap, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_756d_v063_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 756d window."""
    res = _sma(_ratio(assets - equity, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_1008d_v064_signal(equity):
    """Moving average of Raw level of equity over 1008d window."""
    res = _sma(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_1008d_v065_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_1008d_v066_signal(pb):
    """Moving average of Raw level of pb over 1008d window."""
    res = _sma(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_1008d_v067_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 1008d window."""
    res = _sma(_ratio(equity, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_1008d_v068_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 1008d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_base_1008d_v069_signal(marketcap, assets):
    """Moving average of Market valuation per unit of asset over 1008d window."""
    res = _sma(_ratio(marketcap, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_base_1008d_v070_signal(assets, equity, marketcap):
    """Moving average of Non-equity funding relative to valuation over 1008d window."""
    res = _sma(_ratio(assets - equity, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_base_1260d_v071_signal(equity):
    """Moving average of Raw level of equity over 1260d window."""
    res = _sma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_base_1260d_v072_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_base_1260d_v073_signal(pb):
    """Moving average of Raw level of pb over 1260d window."""
    res = _sma(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_base_1260d_v074_signal(equity, assets):
    """Moving average of Equity-to-assets buffer over 1260d window."""
    res = _sma(_ratio(equity, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_base_1260d_v075_signal(equity, assets, marketcap):
    """Moving average of True excess capital relative to valuation over 1260d window."""
    res = _sma(_ratio(equity - (0.08 * assets), marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f01_mna_capital_excess_equity_base_5d_v001_signal": {"func": f01_mna_capital_excess_equity_base_5d_v001_signal},
    "f01_mna_capital_excess_assets_base_5d_v002_signal": {"func": f01_mna_capital_excess_assets_base_5d_v002_signal},
    "f01_mna_capital_excess_pb_base_5d_v003_signal": {"func": f01_mna_capital_excess_pb_base_5d_v003_signal},
    "f01_mna_capital_excess_capital_buffer_base_5d_v004_signal": {"func": f01_mna_capital_excess_capital_buffer_base_5d_v004_signal},
    "f01_mna_capital_excess_excess_capital_base_5d_v005_signal": {"func": f01_mna_capital_excess_excess_capital_base_5d_v005_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_5d_v006_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_5d_v006_signal},
    "f01_mna_capital_excess_leverage_moat_base_5d_v007_signal": {"func": f01_mna_capital_excess_leverage_moat_base_5d_v007_signal},
    "f01_mna_capital_excess_equity_base_10d_v008_signal": {"func": f01_mna_capital_excess_equity_base_10d_v008_signal},
    "f01_mna_capital_excess_assets_base_10d_v009_signal": {"func": f01_mna_capital_excess_assets_base_10d_v009_signal},
    "f01_mna_capital_excess_pb_base_10d_v010_signal": {"func": f01_mna_capital_excess_pb_base_10d_v010_signal},
    "f01_mna_capital_excess_capital_buffer_base_10d_v011_signal": {"func": f01_mna_capital_excess_capital_buffer_base_10d_v011_signal},
    "f01_mna_capital_excess_excess_capital_base_10d_v012_signal": {"func": f01_mna_capital_excess_excess_capital_base_10d_v012_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_10d_v013_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_10d_v013_signal},
    "f01_mna_capital_excess_leverage_moat_base_10d_v014_signal": {"func": f01_mna_capital_excess_leverage_moat_base_10d_v014_signal},
    "f01_mna_capital_excess_equity_base_21d_v015_signal": {"func": f01_mna_capital_excess_equity_base_21d_v015_signal},
    "f01_mna_capital_excess_assets_base_21d_v016_signal": {"func": f01_mna_capital_excess_assets_base_21d_v016_signal},
    "f01_mna_capital_excess_pb_base_21d_v017_signal": {"func": f01_mna_capital_excess_pb_base_21d_v017_signal},
    "f01_mna_capital_excess_capital_buffer_base_21d_v018_signal": {"func": f01_mna_capital_excess_capital_buffer_base_21d_v018_signal},
    "f01_mna_capital_excess_excess_capital_base_21d_v019_signal": {"func": f01_mna_capital_excess_excess_capital_base_21d_v019_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_21d_v020_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_21d_v020_signal},
    "f01_mna_capital_excess_leverage_moat_base_21d_v021_signal": {"func": f01_mna_capital_excess_leverage_moat_base_21d_v021_signal},
    "f01_mna_capital_excess_equity_base_42d_v022_signal": {"func": f01_mna_capital_excess_equity_base_42d_v022_signal},
    "f01_mna_capital_excess_assets_base_42d_v023_signal": {"func": f01_mna_capital_excess_assets_base_42d_v023_signal},
    "f01_mna_capital_excess_pb_base_42d_v024_signal": {"func": f01_mna_capital_excess_pb_base_42d_v024_signal},
    "f01_mna_capital_excess_capital_buffer_base_42d_v025_signal": {"func": f01_mna_capital_excess_capital_buffer_base_42d_v025_signal},
    "f01_mna_capital_excess_excess_capital_base_42d_v026_signal": {"func": f01_mna_capital_excess_excess_capital_base_42d_v026_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_42d_v027_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_42d_v027_signal},
    "f01_mna_capital_excess_leverage_moat_base_42d_v028_signal": {"func": f01_mna_capital_excess_leverage_moat_base_42d_v028_signal},
    "f01_mna_capital_excess_equity_base_63d_v029_signal": {"func": f01_mna_capital_excess_equity_base_63d_v029_signal},
    "f01_mna_capital_excess_assets_base_63d_v030_signal": {"func": f01_mna_capital_excess_assets_base_63d_v030_signal},
    "f01_mna_capital_excess_pb_base_63d_v031_signal": {"func": f01_mna_capital_excess_pb_base_63d_v031_signal},
    "f01_mna_capital_excess_capital_buffer_base_63d_v032_signal": {"func": f01_mna_capital_excess_capital_buffer_base_63d_v032_signal},
    "f01_mna_capital_excess_excess_capital_base_63d_v033_signal": {"func": f01_mna_capital_excess_excess_capital_base_63d_v033_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_63d_v034_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_63d_v034_signal},
    "f01_mna_capital_excess_leverage_moat_base_63d_v035_signal": {"func": f01_mna_capital_excess_leverage_moat_base_63d_v035_signal},
    "f01_mna_capital_excess_equity_base_126d_v036_signal": {"func": f01_mna_capital_excess_equity_base_126d_v036_signal},
    "f01_mna_capital_excess_assets_base_126d_v037_signal": {"func": f01_mna_capital_excess_assets_base_126d_v037_signal},
    "f01_mna_capital_excess_pb_base_126d_v038_signal": {"func": f01_mna_capital_excess_pb_base_126d_v038_signal},
    "f01_mna_capital_excess_capital_buffer_base_126d_v039_signal": {"func": f01_mna_capital_excess_capital_buffer_base_126d_v039_signal},
    "f01_mna_capital_excess_excess_capital_base_126d_v040_signal": {"func": f01_mna_capital_excess_excess_capital_base_126d_v040_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_126d_v041_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_126d_v041_signal},
    "f01_mna_capital_excess_leverage_moat_base_126d_v042_signal": {"func": f01_mna_capital_excess_leverage_moat_base_126d_v042_signal},
    "f01_mna_capital_excess_equity_base_252d_v043_signal": {"func": f01_mna_capital_excess_equity_base_252d_v043_signal},
    "f01_mna_capital_excess_assets_base_252d_v044_signal": {"func": f01_mna_capital_excess_assets_base_252d_v044_signal},
    "f01_mna_capital_excess_pb_base_252d_v045_signal": {"func": f01_mna_capital_excess_pb_base_252d_v045_signal},
    "f01_mna_capital_excess_capital_buffer_base_252d_v046_signal": {"func": f01_mna_capital_excess_capital_buffer_base_252d_v046_signal},
    "f01_mna_capital_excess_excess_capital_base_252d_v047_signal": {"func": f01_mna_capital_excess_excess_capital_base_252d_v047_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_252d_v048_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_252d_v048_signal},
    "f01_mna_capital_excess_leverage_moat_base_252d_v049_signal": {"func": f01_mna_capital_excess_leverage_moat_base_252d_v049_signal},
    "f01_mna_capital_excess_equity_base_504d_v050_signal": {"func": f01_mna_capital_excess_equity_base_504d_v050_signal},
    "f01_mna_capital_excess_assets_base_504d_v051_signal": {"func": f01_mna_capital_excess_assets_base_504d_v051_signal},
    "f01_mna_capital_excess_pb_base_504d_v052_signal": {"func": f01_mna_capital_excess_pb_base_504d_v052_signal},
    "f01_mna_capital_excess_capital_buffer_base_504d_v053_signal": {"func": f01_mna_capital_excess_capital_buffer_base_504d_v053_signal},
    "f01_mna_capital_excess_excess_capital_base_504d_v054_signal": {"func": f01_mna_capital_excess_excess_capital_base_504d_v054_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_504d_v055_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_504d_v055_signal},
    "f01_mna_capital_excess_leverage_moat_base_504d_v056_signal": {"func": f01_mna_capital_excess_leverage_moat_base_504d_v056_signal},
    "f01_mna_capital_excess_equity_base_756d_v057_signal": {"func": f01_mna_capital_excess_equity_base_756d_v057_signal},
    "f01_mna_capital_excess_assets_base_756d_v058_signal": {"func": f01_mna_capital_excess_assets_base_756d_v058_signal},
    "f01_mna_capital_excess_pb_base_756d_v059_signal": {"func": f01_mna_capital_excess_pb_base_756d_v059_signal},
    "f01_mna_capital_excess_capital_buffer_base_756d_v060_signal": {"func": f01_mna_capital_excess_capital_buffer_base_756d_v060_signal},
    "f01_mna_capital_excess_excess_capital_base_756d_v061_signal": {"func": f01_mna_capital_excess_excess_capital_base_756d_v061_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_756d_v062_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_756d_v062_signal},
    "f01_mna_capital_excess_leverage_moat_base_756d_v063_signal": {"func": f01_mna_capital_excess_leverage_moat_base_756d_v063_signal},
    "f01_mna_capital_excess_equity_base_1008d_v064_signal": {"func": f01_mna_capital_excess_equity_base_1008d_v064_signal},
    "f01_mna_capital_excess_assets_base_1008d_v065_signal": {"func": f01_mna_capital_excess_assets_base_1008d_v065_signal},
    "f01_mna_capital_excess_pb_base_1008d_v066_signal": {"func": f01_mna_capital_excess_pb_base_1008d_v066_signal},
    "f01_mna_capital_excess_capital_buffer_base_1008d_v067_signal": {"func": f01_mna_capital_excess_capital_buffer_base_1008d_v067_signal},
    "f01_mna_capital_excess_excess_capital_base_1008d_v068_signal": {"func": f01_mna_capital_excess_excess_capital_base_1008d_v068_signal},
    "f01_mna_capital_excess_valuation_per_asset_base_1008d_v069_signal": {"func": f01_mna_capital_excess_valuation_per_asset_base_1008d_v069_signal},
    "f01_mna_capital_excess_leverage_moat_base_1008d_v070_signal": {"func": f01_mna_capital_excess_leverage_moat_base_1008d_v070_signal},
    "f01_mna_capital_excess_equity_base_1260d_v071_signal": {"func": f01_mna_capital_excess_equity_base_1260d_v071_signal},
    "f01_mna_capital_excess_assets_base_1260d_v072_signal": {"func": f01_mna_capital_excess_assets_base_1260d_v072_signal},
    "f01_mna_capital_excess_pb_base_1260d_v073_signal": {"func": f01_mna_capital_excess_pb_base_1260d_v073_signal},
    "f01_mna_capital_excess_capital_buffer_base_1260d_v074_signal": {"func": f01_mna_capital_excess_capital_buffer_base_1260d_v074_signal},
    "f01_mna_capital_excess_excess_capital_base_1260d_v075_signal": {"func": f01_mna_capital_excess_excess_capital_base_1260d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 01...")
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
