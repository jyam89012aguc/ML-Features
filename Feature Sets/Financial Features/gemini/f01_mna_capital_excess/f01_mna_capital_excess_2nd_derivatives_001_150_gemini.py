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

def f01_mna_capital_excess_equity_slope_pct_5d_v001_signal(equity):
    """Percentage slope for Raw level of equity over 5d window."""
    res = _slope_pct(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_5d_v002_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_5d_v003_signal(pb):
    """Percentage slope for Raw level of pb over 5d window."""
    res = _slope_pct(pb, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_5d_v004_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 5d window."""
    res = _slope_pct(_ratio(equity, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_5d_v005_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 5d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_5d_v006_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 5d window."""
    res = _slope_pct(_ratio(marketcap, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_5d_v007_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 5d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_10d_v008_signal(equity):
    """Percentage slope for Raw level of equity over 10d window."""
    res = _slope_pct(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_10d_v009_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_10d_v010_signal(pb):
    """Percentage slope for Raw level of pb over 10d window."""
    res = _slope_pct(pb, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_10d_v011_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 10d window."""
    res = _slope_pct(_ratio(equity, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_10d_v012_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 10d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_10d_v013_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 10d window."""
    res = _slope_pct(_ratio(marketcap, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_10d_v014_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 10d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_21d_v015_signal(equity):
    """Percentage slope for Raw level of equity over 21d window."""
    res = _slope_pct(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_21d_v016_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_21d_v017_signal(pb):
    """Percentage slope for Raw level of pb over 21d window."""
    res = _slope_pct(pb, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_21d_v018_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 21d window."""
    res = _slope_pct(_ratio(equity, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_21d_v019_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 21d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_21d_v020_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 21d window."""
    res = _slope_pct(_ratio(marketcap, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_21d_v021_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 21d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_42d_v022_signal(equity):
    """Percentage slope for Raw level of equity over 42d window."""
    res = _slope_pct(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_42d_v023_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_42d_v024_signal(pb):
    """Percentage slope for Raw level of pb over 42d window."""
    res = _slope_pct(pb, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_42d_v025_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 42d window."""
    res = _slope_pct(_ratio(equity, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_42d_v026_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 42d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_42d_v027_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 42d window."""
    res = _slope_pct(_ratio(marketcap, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_42d_v028_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 42d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_63d_v029_signal(equity):
    """Percentage slope for Raw level of equity over 63d window."""
    res = _slope_pct(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_63d_v030_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_63d_v031_signal(pb):
    """Percentage slope for Raw level of pb over 63d window."""
    res = _slope_pct(pb, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_63d_v032_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 63d window."""
    res = _slope_pct(_ratio(equity, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_63d_v033_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 63d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_63d_v034_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 63d window."""
    res = _slope_pct(_ratio(marketcap, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_63d_v035_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 63d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_126d_v036_signal(equity):
    """Percentage slope for Raw level of equity over 126d window."""
    res = _slope_pct(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_126d_v037_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_126d_v038_signal(pb):
    """Percentage slope for Raw level of pb over 126d window."""
    res = _slope_pct(pb, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_126d_v039_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 126d window."""
    res = _slope_pct(_ratio(equity, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_126d_v040_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 126d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_126d_v041_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 126d window."""
    res = _slope_pct(_ratio(marketcap, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_126d_v042_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 126d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_252d_v043_signal(equity):
    """Percentage slope for Raw level of equity over 252d window."""
    res = _slope_pct(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_252d_v044_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_252d_v045_signal(pb):
    """Percentage slope for Raw level of pb over 252d window."""
    res = _slope_pct(pb, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_252d_v046_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 252d window."""
    res = _slope_pct(_ratio(equity, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_252d_v047_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 252d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_252d_v048_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 252d window."""
    res = _slope_pct(_ratio(marketcap, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_252d_v049_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 252d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_504d_v050_signal(equity):
    """Percentage slope for Raw level of equity over 504d window."""
    res = _slope_pct(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_504d_v051_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_504d_v052_signal(pb):
    """Percentage slope for Raw level of pb over 504d window."""
    res = _slope_pct(pb, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_504d_v053_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 504d window."""
    res = _slope_pct(_ratio(equity, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_504d_v054_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 504d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_504d_v055_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 504d window."""
    res = _slope_pct(_ratio(marketcap, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_504d_v056_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 504d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_756d_v057_signal(equity):
    """Percentage slope for Raw level of equity over 756d window."""
    res = _slope_pct(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_756d_v058_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_756d_v059_signal(pb):
    """Percentage slope for Raw level of pb over 756d window."""
    res = _slope_pct(pb, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_756d_v060_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 756d window."""
    res = _slope_pct(_ratio(equity, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_756d_v061_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 756d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_756d_v062_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 756d window."""
    res = _slope_pct(_ratio(marketcap, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_756d_v063_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 756d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_1008d_v064_signal(equity):
    """Percentage slope for Raw level of equity over 1008d window."""
    res = _slope_pct(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_1008d_v065_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_1008d_v066_signal(pb):
    """Percentage slope for Raw level of pb over 1008d window."""
    res = _slope_pct(pb, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_1008d_v067_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 1008d window."""
    res = _slope_pct(_ratio(equity, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_1008d_v068_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 1008d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_1008d_v069_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 1008d window."""
    res = _slope_pct(_ratio(marketcap, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_1008d_v070_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 1008d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_slope_pct_1260d_v071_signal(equity):
    """Percentage slope for Raw level of equity over 1260d window."""
    res = _slope_pct(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_slope_pct_1260d_v072_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_slope_pct_1260d_v073_signal(pb):
    """Percentage slope for Raw level of pb over 1260d window."""
    res = _slope_pct(pb, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_slope_pct_1260d_v074_signal(equity, assets):
    """Percentage slope for Equity-to-assets buffer over 1260d window."""
    res = _slope_pct(_ratio(equity, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_slope_pct_1260d_v075_signal(equity, assets, marketcap):
    """Percentage slope for True excess capital relative to valuation over 1260d window."""
    res = _slope_pct(_ratio(equity - (0.08 * assets), marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_slope_pct_1260d_v076_signal(marketcap, assets):
    """Percentage slope for Market valuation per unit of asset over 1260d window."""
    res = _slope_pct(_ratio(marketcap, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_slope_pct_1260d_v077_signal(assets, equity, marketcap):
    """Percentage slope for Non-equity funding relative to valuation over 1260d window."""
    res = _slope_pct(_ratio(assets - equity, marketcap), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_5d_v078_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 5d window."""
    res = _jerk(equity, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_5d_v079_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_5d_v080_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 5d window."""
    res = _jerk(pb, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_5d_v081_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 5d window."""
    res = _jerk(_ratio(equity, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_5d_v082_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 5d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_5d_v083_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 5d window."""
    res = _jerk(_ratio(marketcap, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_5d_v084_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 5d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_10d_v085_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 10d window."""
    res = _jerk(equity, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_10d_v086_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_10d_v087_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 10d window."""
    res = _jerk(pb, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_10d_v088_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 10d window."""
    res = _jerk(_ratio(equity, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_10d_v089_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 10d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_10d_v090_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 10d window."""
    res = _jerk(_ratio(marketcap, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_10d_v091_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 10d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_21d_v092_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 21d window."""
    res = _jerk(equity, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_21d_v093_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_21d_v094_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 21d window."""
    res = _jerk(pb, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_21d_v095_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 21d window."""
    res = _jerk(_ratio(equity, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_21d_v096_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 21d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_21d_v097_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 21d window."""
    res = _jerk(_ratio(marketcap, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_21d_v098_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 21d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_42d_v099_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 42d window."""
    res = _jerk(equity, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_42d_v100_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_42d_v101_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 42d window."""
    res = _jerk(pb, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_42d_v102_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 42d window."""
    res = _jerk(_ratio(equity, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_42d_v103_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 42d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_42d_v104_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 42d window."""
    res = _jerk(_ratio(marketcap, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_42d_v105_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 42d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_63d_v106_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 63d window."""
    res = _jerk(equity, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_63d_v107_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_63d_v108_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 63d window."""
    res = _jerk(pb, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_63d_v109_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 63d window."""
    res = _jerk(_ratio(equity, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_63d_v110_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 63d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_63d_v111_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 63d window."""
    res = _jerk(_ratio(marketcap, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_63d_v112_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 63d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_126d_v113_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 126d window."""
    res = _jerk(equity, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_126d_v114_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_126d_v115_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 126d window."""
    res = _jerk(pb, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_126d_v116_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 126d window."""
    res = _jerk(_ratio(equity, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_126d_v117_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 126d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_126d_v118_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 126d window."""
    res = _jerk(_ratio(marketcap, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_126d_v119_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 126d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_252d_v120_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 252d window."""
    res = _jerk(equity, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_252d_v121_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_252d_v122_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 252d window."""
    res = _jerk(pb, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_252d_v123_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 252d window."""
    res = _jerk(_ratio(equity, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_252d_v124_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 252d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_252d_v125_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 252d window."""
    res = _jerk(_ratio(marketcap, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_252d_v126_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 252d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_504d_v127_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 504d window."""
    res = _jerk(equity, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_504d_v128_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_504d_v129_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 504d window."""
    res = _jerk(pb, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_504d_v130_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 504d window."""
    res = _jerk(_ratio(equity, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_504d_v131_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 504d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_504d_v132_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 504d window."""
    res = _jerk(_ratio(marketcap, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_504d_v133_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 504d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_756d_v134_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 756d window."""
    res = _jerk(equity, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_756d_v135_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_756d_v136_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 756d window."""
    res = _jerk(pb, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_756d_v137_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 756d window."""
    res = _jerk(_ratio(equity, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_756d_v138_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 756d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_756d_v139_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 756d window."""
    res = _jerk(_ratio(marketcap, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_756d_v140_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 756d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_1008d_v141_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 1008d window."""
    res = _jerk(equity, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_1008d_v142_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_1008d_v143_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 1008d window."""
    res = _jerk(pb, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_capital_buffer_jerk_1008d_v144_signal(equity, assets):
    """Acceleration/Jerk for Equity-to-assets buffer over 1008d window."""
    res = _jerk(_ratio(equity, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_excess_capital_jerk_1008d_v145_signal(equity, assets, marketcap):
    """Acceleration/Jerk for True excess capital relative to valuation over 1008d window."""
    res = _jerk(_ratio(equity - (0.08 * assets), marketcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_valuation_per_asset_jerk_1008d_v146_signal(marketcap, assets):
    """Acceleration/Jerk for Market valuation per unit of asset over 1008d window."""
    res = _jerk(_ratio(marketcap, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_leverage_moat_jerk_1008d_v147_signal(assets, equity, marketcap):
    """Acceleration/Jerk for Non-equity funding relative to valuation over 1008d window."""
    res = _jerk(_ratio(assets - equity, marketcap), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_equity_jerk_1260d_v148_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 1260d window."""
    res = _jerk(equity, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_assets_jerk_1260d_v149_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_mna_capital_excess_pb_jerk_1260d_v150_signal(pb):
    """Acceleration/Jerk for Raw level of pb over 1260d window."""
    res = _jerk(pb, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f01_mna_capital_excess_equity_slope_pct_5d_v001_signal": {"func": f01_mna_capital_excess_equity_slope_pct_5d_v001_signal},
    "f01_mna_capital_excess_assets_slope_pct_5d_v002_signal": {"func": f01_mna_capital_excess_assets_slope_pct_5d_v002_signal},
    "f01_mna_capital_excess_pb_slope_pct_5d_v003_signal": {"func": f01_mna_capital_excess_pb_slope_pct_5d_v003_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_5d_v004_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_5d_v004_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_5d_v005_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_5d_v005_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_5d_v006_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_5d_v006_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_5d_v007_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_5d_v007_signal},
    "f01_mna_capital_excess_equity_slope_pct_10d_v008_signal": {"func": f01_mna_capital_excess_equity_slope_pct_10d_v008_signal},
    "f01_mna_capital_excess_assets_slope_pct_10d_v009_signal": {"func": f01_mna_capital_excess_assets_slope_pct_10d_v009_signal},
    "f01_mna_capital_excess_pb_slope_pct_10d_v010_signal": {"func": f01_mna_capital_excess_pb_slope_pct_10d_v010_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_10d_v011_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_10d_v011_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_10d_v012_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_10d_v012_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_10d_v013_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_10d_v013_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_10d_v014_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_10d_v014_signal},
    "f01_mna_capital_excess_equity_slope_pct_21d_v015_signal": {"func": f01_mna_capital_excess_equity_slope_pct_21d_v015_signal},
    "f01_mna_capital_excess_assets_slope_pct_21d_v016_signal": {"func": f01_mna_capital_excess_assets_slope_pct_21d_v016_signal},
    "f01_mna_capital_excess_pb_slope_pct_21d_v017_signal": {"func": f01_mna_capital_excess_pb_slope_pct_21d_v017_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_21d_v018_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_21d_v018_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_21d_v019_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_21d_v019_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_21d_v020_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_21d_v020_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_21d_v021_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_21d_v021_signal},
    "f01_mna_capital_excess_equity_slope_pct_42d_v022_signal": {"func": f01_mna_capital_excess_equity_slope_pct_42d_v022_signal},
    "f01_mna_capital_excess_assets_slope_pct_42d_v023_signal": {"func": f01_mna_capital_excess_assets_slope_pct_42d_v023_signal},
    "f01_mna_capital_excess_pb_slope_pct_42d_v024_signal": {"func": f01_mna_capital_excess_pb_slope_pct_42d_v024_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_42d_v025_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_42d_v025_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_42d_v026_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_42d_v026_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_42d_v027_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_42d_v027_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_42d_v028_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_42d_v028_signal},
    "f01_mna_capital_excess_equity_slope_pct_63d_v029_signal": {"func": f01_mna_capital_excess_equity_slope_pct_63d_v029_signal},
    "f01_mna_capital_excess_assets_slope_pct_63d_v030_signal": {"func": f01_mna_capital_excess_assets_slope_pct_63d_v030_signal},
    "f01_mna_capital_excess_pb_slope_pct_63d_v031_signal": {"func": f01_mna_capital_excess_pb_slope_pct_63d_v031_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_63d_v032_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_63d_v032_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_63d_v033_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_63d_v033_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_63d_v034_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_63d_v034_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_63d_v035_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_63d_v035_signal},
    "f01_mna_capital_excess_equity_slope_pct_126d_v036_signal": {"func": f01_mna_capital_excess_equity_slope_pct_126d_v036_signal},
    "f01_mna_capital_excess_assets_slope_pct_126d_v037_signal": {"func": f01_mna_capital_excess_assets_slope_pct_126d_v037_signal},
    "f01_mna_capital_excess_pb_slope_pct_126d_v038_signal": {"func": f01_mna_capital_excess_pb_slope_pct_126d_v038_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_126d_v039_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_126d_v039_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_126d_v040_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_126d_v040_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_126d_v041_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_126d_v041_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_126d_v042_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_126d_v042_signal},
    "f01_mna_capital_excess_equity_slope_pct_252d_v043_signal": {"func": f01_mna_capital_excess_equity_slope_pct_252d_v043_signal},
    "f01_mna_capital_excess_assets_slope_pct_252d_v044_signal": {"func": f01_mna_capital_excess_assets_slope_pct_252d_v044_signal},
    "f01_mna_capital_excess_pb_slope_pct_252d_v045_signal": {"func": f01_mna_capital_excess_pb_slope_pct_252d_v045_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_252d_v046_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_252d_v046_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_252d_v047_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_252d_v047_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_252d_v048_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_252d_v048_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_252d_v049_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_252d_v049_signal},
    "f01_mna_capital_excess_equity_slope_pct_504d_v050_signal": {"func": f01_mna_capital_excess_equity_slope_pct_504d_v050_signal},
    "f01_mna_capital_excess_assets_slope_pct_504d_v051_signal": {"func": f01_mna_capital_excess_assets_slope_pct_504d_v051_signal},
    "f01_mna_capital_excess_pb_slope_pct_504d_v052_signal": {"func": f01_mna_capital_excess_pb_slope_pct_504d_v052_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_504d_v053_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_504d_v053_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_504d_v054_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_504d_v054_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_504d_v055_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_504d_v055_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_504d_v056_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_504d_v056_signal},
    "f01_mna_capital_excess_equity_slope_pct_756d_v057_signal": {"func": f01_mna_capital_excess_equity_slope_pct_756d_v057_signal},
    "f01_mna_capital_excess_assets_slope_pct_756d_v058_signal": {"func": f01_mna_capital_excess_assets_slope_pct_756d_v058_signal},
    "f01_mna_capital_excess_pb_slope_pct_756d_v059_signal": {"func": f01_mna_capital_excess_pb_slope_pct_756d_v059_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_756d_v060_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_756d_v060_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_756d_v061_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_756d_v061_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_756d_v062_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_756d_v062_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_756d_v063_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_756d_v063_signal},
    "f01_mna_capital_excess_equity_slope_pct_1008d_v064_signal": {"func": f01_mna_capital_excess_equity_slope_pct_1008d_v064_signal},
    "f01_mna_capital_excess_assets_slope_pct_1008d_v065_signal": {"func": f01_mna_capital_excess_assets_slope_pct_1008d_v065_signal},
    "f01_mna_capital_excess_pb_slope_pct_1008d_v066_signal": {"func": f01_mna_capital_excess_pb_slope_pct_1008d_v066_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_1008d_v067_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_1008d_v067_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_1008d_v068_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_1008d_v068_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_1008d_v069_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_1008d_v069_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_1008d_v070_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_1008d_v070_signal},
    "f01_mna_capital_excess_equity_slope_pct_1260d_v071_signal": {"func": f01_mna_capital_excess_equity_slope_pct_1260d_v071_signal},
    "f01_mna_capital_excess_assets_slope_pct_1260d_v072_signal": {"func": f01_mna_capital_excess_assets_slope_pct_1260d_v072_signal},
    "f01_mna_capital_excess_pb_slope_pct_1260d_v073_signal": {"func": f01_mna_capital_excess_pb_slope_pct_1260d_v073_signal},
    "f01_mna_capital_excess_capital_buffer_slope_pct_1260d_v074_signal": {"func": f01_mna_capital_excess_capital_buffer_slope_pct_1260d_v074_signal},
    "f01_mna_capital_excess_excess_capital_slope_pct_1260d_v075_signal": {"func": f01_mna_capital_excess_excess_capital_slope_pct_1260d_v075_signal},
    "f01_mna_capital_excess_valuation_per_asset_slope_pct_1260d_v076_signal": {"func": f01_mna_capital_excess_valuation_per_asset_slope_pct_1260d_v076_signal},
    "f01_mna_capital_excess_leverage_moat_slope_pct_1260d_v077_signal": {"func": f01_mna_capital_excess_leverage_moat_slope_pct_1260d_v077_signal},
    "f01_mna_capital_excess_equity_jerk_5d_v078_signal": {"func": f01_mna_capital_excess_equity_jerk_5d_v078_signal},
    "f01_mna_capital_excess_assets_jerk_5d_v079_signal": {"func": f01_mna_capital_excess_assets_jerk_5d_v079_signal},
    "f01_mna_capital_excess_pb_jerk_5d_v080_signal": {"func": f01_mna_capital_excess_pb_jerk_5d_v080_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_5d_v081_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_5d_v081_signal},
    "f01_mna_capital_excess_excess_capital_jerk_5d_v082_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_5d_v082_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_5d_v083_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_5d_v083_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_5d_v084_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_5d_v084_signal},
    "f01_mna_capital_excess_equity_jerk_10d_v085_signal": {"func": f01_mna_capital_excess_equity_jerk_10d_v085_signal},
    "f01_mna_capital_excess_assets_jerk_10d_v086_signal": {"func": f01_mna_capital_excess_assets_jerk_10d_v086_signal},
    "f01_mna_capital_excess_pb_jerk_10d_v087_signal": {"func": f01_mna_capital_excess_pb_jerk_10d_v087_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_10d_v088_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_10d_v088_signal},
    "f01_mna_capital_excess_excess_capital_jerk_10d_v089_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_10d_v089_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_10d_v090_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_10d_v090_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_10d_v091_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_10d_v091_signal},
    "f01_mna_capital_excess_equity_jerk_21d_v092_signal": {"func": f01_mna_capital_excess_equity_jerk_21d_v092_signal},
    "f01_mna_capital_excess_assets_jerk_21d_v093_signal": {"func": f01_mna_capital_excess_assets_jerk_21d_v093_signal},
    "f01_mna_capital_excess_pb_jerk_21d_v094_signal": {"func": f01_mna_capital_excess_pb_jerk_21d_v094_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_21d_v095_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_21d_v095_signal},
    "f01_mna_capital_excess_excess_capital_jerk_21d_v096_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_21d_v096_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_21d_v097_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_21d_v097_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_21d_v098_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_21d_v098_signal},
    "f01_mna_capital_excess_equity_jerk_42d_v099_signal": {"func": f01_mna_capital_excess_equity_jerk_42d_v099_signal},
    "f01_mna_capital_excess_assets_jerk_42d_v100_signal": {"func": f01_mna_capital_excess_assets_jerk_42d_v100_signal},
    "f01_mna_capital_excess_pb_jerk_42d_v101_signal": {"func": f01_mna_capital_excess_pb_jerk_42d_v101_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_42d_v102_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_42d_v102_signal},
    "f01_mna_capital_excess_excess_capital_jerk_42d_v103_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_42d_v103_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_42d_v104_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_42d_v104_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_42d_v105_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_42d_v105_signal},
    "f01_mna_capital_excess_equity_jerk_63d_v106_signal": {"func": f01_mna_capital_excess_equity_jerk_63d_v106_signal},
    "f01_mna_capital_excess_assets_jerk_63d_v107_signal": {"func": f01_mna_capital_excess_assets_jerk_63d_v107_signal},
    "f01_mna_capital_excess_pb_jerk_63d_v108_signal": {"func": f01_mna_capital_excess_pb_jerk_63d_v108_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_63d_v109_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_63d_v109_signal},
    "f01_mna_capital_excess_excess_capital_jerk_63d_v110_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_63d_v110_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_63d_v111_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_63d_v111_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_63d_v112_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_63d_v112_signal},
    "f01_mna_capital_excess_equity_jerk_126d_v113_signal": {"func": f01_mna_capital_excess_equity_jerk_126d_v113_signal},
    "f01_mna_capital_excess_assets_jerk_126d_v114_signal": {"func": f01_mna_capital_excess_assets_jerk_126d_v114_signal},
    "f01_mna_capital_excess_pb_jerk_126d_v115_signal": {"func": f01_mna_capital_excess_pb_jerk_126d_v115_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_126d_v116_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_126d_v116_signal},
    "f01_mna_capital_excess_excess_capital_jerk_126d_v117_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_126d_v117_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_126d_v118_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_126d_v118_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_126d_v119_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_126d_v119_signal},
    "f01_mna_capital_excess_equity_jerk_252d_v120_signal": {"func": f01_mna_capital_excess_equity_jerk_252d_v120_signal},
    "f01_mna_capital_excess_assets_jerk_252d_v121_signal": {"func": f01_mna_capital_excess_assets_jerk_252d_v121_signal},
    "f01_mna_capital_excess_pb_jerk_252d_v122_signal": {"func": f01_mna_capital_excess_pb_jerk_252d_v122_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_252d_v123_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_252d_v123_signal},
    "f01_mna_capital_excess_excess_capital_jerk_252d_v124_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_252d_v124_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_252d_v125_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_252d_v125_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_252d_v126_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_252d_v126_signal},
    "f01_mna_capital_excess_equity_jerk_504d_v127_signal": {"func": f01_mna_capital_excess_equity_jerk_504d_v127_signal},
    "f01_mna_capital_excess_assets_jerk_504d_v128_signal": {"func": f01_mna_capital_excess_assets_jerk_504d_v128_signal},
    "f01_mna_capital_excess_pb_jerk_504d_v129_signal": {"func": f01_mna_capital_excess_pb_jerk_504d_v129_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_504d_v130_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_504d_v130_signal},
    "f01_mna_capital_excess_excess_capital_jerk_504d_v131_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_504d_v131_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_504d_v132_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_504d_v132_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_504d_v133_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_504d_v133_signal},
    "f01_mna_capital_excess_equity_jerk_756d_v134_signal": {"func": f01_mna_capital_excess_equity_jerk_756d_v134_signal},
    "f01_mna_capital_excess_assets_jerk_756d_v135_signal": {"func": f01_mna_capital_excess_assets_jerk_756d_v135_signal},
    "f01_mna_capital_excess_pb_jerk_756d_v136_signal": {"func": f01_mna_capital_excess_pb_jerk_756d_v136_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_756d_v137_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_756d_v137_signal},
    "f01_mna_capital_excess_excess_capital_jerk_756d_v138_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_756d_v138_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_756d_v139_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_756d_v139_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_756d_v140_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_756d_v140_signal},
    "f01_mna_capital_excess_equity_jerk_1008d_v141_signal": {"func": f01_mna_capital_excess_equity_jerk_1008d_v141_signal},
    "f01_mna_capital_excess_assets_jerk_1008d_v142_signal": {"func": f01_mna_capital_excess_assets_jerk_1008d_v142_signal},
    "f01_mna_capital_excess_pb_jerk_1008d_v143_signal": {"func": f01_mna_capital_excess_pb_jerk_1008d_v143_signal},
    "f01_mna_capital_excess_capital_buffer_jerk_1008d_v144_signal": {"func": f01_mna_capital_excess_capital_buffer_jerk_1008d_v144_signal},
    "f01_mna_capital_excess_excess_capital_jerk_1008d_v145_signal": {"func": f01_mna_capital_excess_excess_capital_jerk_1008d_v145_signal},
    "f01_mna_capital_excess_valuation_per_asset_jerk_1008d_v146_signal": {"func": f01_mna_capital_excess_valuation_per_asset_jerk_1008d_v146_signal},
    "f01_mna_capital_excess_leverage_moat_jerk_1008d_v147_signal": {"func": f01_mna_capital_excess_leverage_moat_jerk_1008d_v147_signal},
    "f01_mna_capital_excess_equity_jerk_1260d_v148_signal": {"func": f01_mna_capital_excess_equity_jerk_1260d_v148_signal},
    "f01_mna_capital_excess_assets_jerk_1260d_v149_signal": {"func": f01_mna_capital_excess_assets_jerk_1260d_v149_signal},
    "f01_mna_capital_excess_pb_jerk_1260d_v150_signal": {"func": f01_mna_capital_excess_pb_jerk_1260d_v150_signal},
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
