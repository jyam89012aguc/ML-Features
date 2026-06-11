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

def f10_tier1_leverage_equity_base_5d_v001_signal(equity):
    """Moving average of Raw level of equity over 5d window."""
    res = _sma(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_5d_v002_signal(assets):
    """Moving average of Raw level of assets over 5d window."""
    res = _sma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_5d_v003_signal(debt):
    """Moving average of Raw level of debt over 5d window."""
    res = _sma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_5d_v004_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 5d window."""
    res = _sma(_ratio(equity, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_5d_v005_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 5d window."""
    res = _sma(_ratio(debt, equity), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_10d_v006_signal(equity):
    """Moving average of Raw level of equity over 10d window."""
    res = _sma(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_10d_v007_signal(assets):
    """Moving average of Raw level of assets over 10d window."""
    res = _sma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_10d_v008_signal(debt):
    """Moving average of Raw level of debt over 10d window."""
    res = _sma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_10d_v009_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 10d window."""
    res = _sma(_ratio(equity, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_10d_v010_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 10d window."""
    res = _sma(_ratio(debt, equity), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_21d_v011_signal(equity):
    """Moving average of Raw level of equity over 21d window."""
    res = _sma(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_21d_v012_signal(assets):
    """Moving average of Raw level of assets over 21d window."""
    res = _sma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_21d_v013_signal(debt):
    """Moving average of Raw level of debt over 21d window."""
    res = _sma(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_21d_v014_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 21d window."""
    res = _sma(_ratio(equity, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_21d_v015_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 21d window."""
    res = _sma(_ratio(debt, equity), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_42d_v016_signal(equity):
    """Moving average of Raw level of equity over 42d window."""
    res = _sma(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_42d_v017_signal(assets):
    """Moving average of Raw level of assets over 42d window."""
    res = _sma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_42d_v018_signal(debt):
    """Moving average of Raw level of debt over 42d window."""
    res = _sma(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_42d_v019_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 42d window."""
    res = _sma(_ratio(equity, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_42d_v020_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 42d window."""
    res = _sma(_ratio(debt, equity), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_63d_v021_signal(equity):
    """Moving average of Raw level of equity over 63d window."""
    res = _sma(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_63d_v022_signal(assets):
    """Moving average of Raw level of assets over 63d window."""
    res = _sma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_63d_v023_signal(debt):
    """Moving average of Raw level of debt over 63d window."""
    res = _sma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_63d_v024_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 63d window."""
    res = _sma(_ratio(equity, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_63d_v025_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 63d window."""
    res = _sma(_ratio(debt, equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_126d_v026_signal(equity):
    """Moving average of Raw level of equity over 126d window."""
    res = _sma(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_126d_v027_signal(assets):
    """Moving average of Raw level of assets over 126d window."""
    res = _sma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_126d_v028_signal(debt):
    """Moving average of Raw level of debt over 126d window."""
    res = _sma(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_126d_v029_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 126d window."""
    res = _sma(_ratio(equity, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_126d_v030_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 126d window."""
    res = _sma(_ratio(debt, equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_252d_v031_signal(equity):
    """Moving average of Raw level of equity over 252d window."""
    res = _sma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_252d_v032_signal(assets):
    """Moving average of Raw level of assets over 252d window."""
    res = _sma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_252d_v033_signal(debt):
    """Moving average of Raw level of debt over 252d window."""
    res = _sma(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_252d_v034_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 252d window."""
    res = _sma(_ratio(equity, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_252d_v035_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 252d window."""
    res = _sma(_ratio(debt, equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_504d_v036_signal(equity):
    """Moving average of Raw level of equity over 504d window."""
    res = _sma(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_504d_v037_signal(assets):
    """Moving average of Raw level of assets over 504d window."""
    res = _sma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_504d_v038_signal(debt):
    """Moving average of Raw level of debt over 504d window."""
    res = _sma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_504d_v039_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 504d window."""
    res = _sma(_ratio(equity, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_504d_v040_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 504d window."""
    res = _sma(_ratio(debt, equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_756d_v041_signal(equity):
    """Moving average of Raw level of equity over 756d window."""
    res = _sma(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_756d_v042_signal(assets):
    """Moving average of Raw level of assets over 756d window."""
    res = _sma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_756d_v043_signal(debt):
    """Moving average of Raw level of debt over 756d window."""
    res = _sma(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_756d_v044_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 756d window."""
    res = _sma(_ratio(equity, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_756d_v045_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 756d window."""
    res = _sma(_ratio(debt, equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_1008d_v046_signal(equity):
    """Moving average of Raw level of equity over 1008d window."""
    res = _sma(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_1008d_v047_signal(assets):
    """Moving average of Raw level of assets over 1008d window."""
    res = _sma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_1008d_v048_signal(debt):
    """Moving average of Raw level of debt over 1008d window."""
    res = _sma(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_1008d_v049_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 1008d window."""
    res = _sma(_ratio(equity, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_1008d_v050_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 1008d window."""
    res = _sma(_ratio(debt, equity), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_base_1260d_v051_signal(equity):
    """Moving average of Raw level of equity over 1260d window."""
    res = _sma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_base_1260d_v052_signal(assets):
    """Moving average of Raw level of assets over 1260d window."""
    res = _sma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_base_1260d_v053_signal(debt):
    """Moving average of Raw level of debt over 1260d window."""
    res = _sma(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_base_1260d_v054_signal(equity, assets):
    """Moving average of Capital adequacy proxy over 1260d window."""
    res = _sma(_ratio(equity, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_base_1260d_v055_signal(debt, equity):
    """Moving average of Total debt to equity ratio over 1260d window."""
    res = _sma(_ratio(debt, equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_5d_v056_signal(equity):
    """Exponential moving average of Raw level of equity over 5d window."""
    res = _ewma(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_5d_v057_signal(assets):
    """Exponential moving average of Raw level of assets over 5d window."""
    res = _ewma(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_5d_v058_signal(debt):
    """Exponential moving average of Raw level of debt over 5d window."""
    res = _ewma(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_5d_v059_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 5d window."""
    res = _ewma(_ratio(equity, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_5d_v060_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 5d window."""
    res = _ewma(_ratio(debt, equity), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_10d_v061_signal(equity):
    """Exponential moving average of Raw level of equity over 10d window."""
    res = _ewma(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_10d_v062_signal(assets):
    """Exponential moving average of Raw level of assets over 10d window."""
    res = _ewma(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_10d_v063_signal(debt):
    """Exponential moving average of Raw level of debt over 10d window."""
    res = _ewma(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_10d_v064_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 10d window."""
    res = _ewma(_ratio(equity, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_10d_v065_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 10d window."""
    res = _ewma(_ratio(debt, equity), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_21d_v066_signal(equity):
    """Exponential moving average of Raw level of equity over 21d window."""
    res = _ewma(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_21d_v067_signal(assets):
    """Exponential moving average of Raw level of assets over 21d window."""
    res = _ewma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_21d_v068_signal(debt):
    """Exponential moving average of Raw level of debt over 21d window."""
    res = _ewma(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_21d_v069_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 21d window."""
    res = _ewma(_ratio(equity, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_21d_v070_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 21d window."""
    res = _ewma(_ratio(debt, equity), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_42d_v071_signal(equity):
    """Exponential moving average of Raw level of equity over 42d window."""
    res = _ewma(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_42d_v072_signal(assets):
    """Exponential moving average of Raw level of assets over 42d window."""
    res = _ewma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_42d_v073_signal(debt):
    """Exponential moving average of Raw level of debt over 42d window."""
    res = _ewma(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_42d_v074_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 42d window."""
    res = _ewma(_ratio(equity, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_42d_v075_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 42d window."""
    res = _ewma(_ratio(debt, equity), 42)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f10_tier1_leverage_equity_base_5d_v001_signal": {"func": f10_tier1_leverage_equity_base_5d_v001_signal},
    "f10_tier1_leverage_assets_base_5d_v002_signal": {"func": f10_tier1_leverage_assets_base_5d_v002_signal},
    "f10_tier1_leverage_debt_base_5d_v003_signal": {"func": f10_tier1_leverage_debt_base_5d_v003_signal},
    "f10_tier1_leverage_tier1_proxy_base_5d_v004_signal": {"func": f10_tier1_leverage_tier1_proxy_base_5d_v004_signal},
    "f10_tier1_leverage_total_leverage_base_5d_v005_signal": {"func": f10_tier1_leverage_total_leverage_base_5d_v005_signal},
    "f10_tier1_leverage_equity_base_10d_v006_signal": {"func": f10_tier1_leverage_equity_base_10d_v006_signal},
    "f10_tier1_leverage_assets_base_10d_v007_signal": {"func": f10_tier1_leverage_assets_base_10d_v007_signal},
    "f10_tier1_leverage_debt_base_10d_v008_signal": {"func": f10_tier1_leverage_debt_base_10d_v008_signal},
    "f10_tier1_leverage_tier1_proxy_base_10d_v009_signal": {"func": f10_tier1_leverage_tier1_proxy_base_10d_v009_signal},
    "f10_tier1_leverage_total_leverage_base_10d_v010_signal": {"func": f10_tier1_leverage_total_leverage_base_10d_v010_signal},
    "f10_tier1_leverage_equity_base_21d_v011_signal": {"func": f10_tier1_leverage_equity_base_21d_v011_signal},
    "f10_tier1_leverage_assets_base_21d_v012_signal": {"func": f10_tier1_leverage_assets_base_21d_v012_signal},
    "f10_tier1_leverage_debt_base_21d_v013_signal": {"func": f10_tier1_leverage_debt_base_21d_v013_signal},
    "f10_tier1_leverage_tier1_proxy_base_21d_v014_signal": {"func": f10_tier1_leverage_tier1_proxy_base_21d_v014_signal},
    "f10_tier1_leverage_total_leverage_base_21d_v015_signal": {"func": f10_tier1_leverage_total_leverage_base_21d_v015_signal},
    "f10_tier1_leverage_equity_base_42d_v016_signal": {"func": f10_tier1_leverage_equity_base_42d_v016_signal},
    "f10_tier1_leverage_assets_base_42d_v017_signal": {"func": f10_tier1_leverage_assets_base_42d_v017_signal},
    "f10_tier1_leverage_debt_base_42d_v018_signal": {"func": f10_tier1_leverage_debt_base_42d_v018_signal},
    "f10_tier1_leverage_tier1_proxy_base_42d_v019_signal": {"func": f10_tier1_leverage_tier1_proxy_base_42d_v019_signal},
    "f10_tier1_leverage_total_leverage_base_42d_v020_signal": {"func": f10_tier1_leverage_total_leverage_base_42d_v020_signal},
    "f10_tier1_leverage_equity_base_63d_v021_signal": {"func": f10_tier1_leverage_equity_base_63d_v021_signal},
    "f10_tier1_leverage_assets_base_63d_v022_signal": {"func": f10_tier1_leverage_assets_base_63d_v022_signal},
    "f10_tier1_leverage_debt_base_63d_v023_signal": {"func": f10_tier1_leverage_debt_base_63d_v023_signal},
    "f10_tier1_leverage_tier1_proxy_base_63d_v024_signal": {"func": f10_tier1_leverage_tier1_proxy_base_63d_v024_signal},
    "f10_tier1_leverage_total_leverage_base_63d_v025_signal": {"func": f10_tier1_leverage_total_leverage_base_63d_v025_signal},
    "f10_tier1_leverage_equity_base_126d_v026_signal": {"func": f10_tier1_leverage_equity_base_126d_v026_signal},
    "f10_tier1_leverage_assets_base_126d_v027_signal": {"func": f10_tier1_leverage_assets_base_126d_v027_signal},
    "f10_tier1_leverage_debt_base_126d_v028_signal": {"func": f10_tier1_leverage_debt_base_126d_v028_signal},
    "f10_tier1_leverage_tier1_proxy_base_126d_v029_signal": {"func": f10_tier1_leverage_tier1_proxy_base_126d_v029_signal},
    "f10_tier1_leverage_total_leverage_base_126d_v030_signal": {"func": f10_tier1_leverage_total_leverage_base_126d_v030_signal},
    "f10_tier1_leverage_equity_base_252d_v031_signal": {"func": f10_tier1_leverage_equity_base_252d_v031_signal},
    "f10_tier1_leverage_assets_base_252d_v032_signal": {"func": f10_tier1_leverage_assets_base_252d_v032_signal},
    "f10_tier1_leverage_debt_base_252d_v033_signal": {"func": f10_tier1_leverage_debt_base_252d_v033_signal},
    "f10_tier1_leverage_tier1_proxy_base_252d_v034_signal": {"func": f10_tier1_leverage_tier1_proxy_base_252d_v034_signal},
    "f10_tier1_leverage_total_leverage_base_252d_v035_signal": {"func": f10_tier1_leverage_total_leverage_base_252d_v035_signal},
    "f10_tier1_leverage_equity_base_504d_v036_signal": {"func": f10_tier1_leverage_equity_base_504d_v036_signal},
    "f10_tier1_leverage_assets_base_504d_v037_signal": {"func": f10_tier1_leverage_assets_base_504d_v037_signal},
    "f10_tier1_leverage_debt_base_504d_v038_signal": {"func": f10_tier1_leverage_debt_base_504d_v038_signal},
    "f10_tier1_leverage_tier1_proxy_base_504d_v039_signal": {"func": f10_tier1_leverage_tier1_proxy_base_504d_v039_signal},
    "f10_tier1_leverage_total_leverage_base_504d_v040_signal": {"func": f10_tier1_leverage_total_leverage_base_504d_v040_signal},
    "f10_tier1_leverage_equity_base_756d_v041_signal": {"func": f10_tier1_leverage_equity_base_756d_v041_signal},
    "f10_tier1_leverage_assets_base_756d_v042_signal": {"func": f10_tier1_leverage_assets_base_756d_v042_signal},
    "f10_tier1_leverage_debt_base_756d_v043_signal": {"func": f10_tier1_leverage_debt_base_756d_v043_signal},
    "f10_tier1_leverage_tier1_proxy_base_756d_v044_signal": {"func": f10_tier1_leverage_tier1_proxy_base_756d_v044_signal},
    "f10_tier1_leverage_total_leverage_base_756d_v045_signal": {"func": f10_tier1_leverage_total_leverage_base_756d_v045_signal},
    "f10_tier1_leverage_equity_base_1008d_v046_signal": {"func": f10_tier1_leverage_equity_base_1008d_v046_signal},
    "f10_tier1_leverage_assets_base_1008d_v047_signal": {"func": f10_tier1_leverage_assets_base_1008d_v047_signal},
    "f10_tier1_leverage_debt_base_1008d_v048_signal": {"func": f10_tier1_leverage_debt_base_1008d_v048_signal},
    "f10_tier1_leverage_tier1_proxy_base_1008d_v049_signal": {"func": f10_tier1_leverage_tier1_proxy_base_1008d_v049_signal},
    "f10_tier1_leverage_total_leverage_base_1008d_v050_signal": {"func": f10_tier1_leverage_total_leverage_base_1008d_v050_signal},
    "f10_tier1_leverage_equity_base_1260d_v051_signal": {"func": f10_tier1_leverage_equity_base_1260d_v051_signal},
    "f10_tier1_leverage_assets_base_1260d_v052_signal": {"func": f10_tier1_leverage_assets_base_1260d_v052_signal},
    "f10_tier1_leverage_debt_base_1260d_v053_signal": {"func": f10_tier1_leverage_debt_base_1260d_v053_signal},
    "f10_tier1_leverage_tier1_proxy_base_1260d_v054_signal": {"func": f10_tier1_leverage_tier1_proxy_base_1260d_v054_signal},
    "f10_tier1_leverage_total_leverage_base_1260d_v055_signal": {"func": f10_tier1_leverage_total_leverage_base_1260d_v055_signal},
    "f10_tier1_leverage_equity_ewma_5d_v056_signal": {"func": f10_tier1_leverage_equity_ewma_5d_v056_signal},
    "f10_tier1_leverage_assets_ewma_5d_v057_signal": {"func": f10_tier1_leverage_assets_ewma_5d_v057_signal},
    "f10_tier1_leverage_debt_ewma_5d_v058_signal": {"func": f10_tier1_leverage_debt_ewma_5d_v058_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_5d_v059_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_5d_v059_signal},
    "f10_tier1_leverage_total_leverage_ewma_5d_v060_signal": {"func": f10_tier1_leverage_total_leverage_ewma_5d_v060_signal},
    "f10_tier1_leverage_equity_ewma_10d_v061_signal": {"func": f10_tier1_leverage_equity_ewma_10d_v061_signal},
    "f10_tier1_leverage_assets_ewma_10d_v062_signal": {"func": f10_tier1_leverage_assets_ewma_10d_v062_signal},
    "f10_tier1_leverage_debt_ewma_10d_v063_signal": {"func": f10_tier1_leverage_debt_ewma_10d_v063_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_10d_v064_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_10d_v064_signal},
    "f10_tier1_leverage_total_leverage_ewma_10d_v065_signal": {"func": f10_tier1_leverage_total_leverage_ewma_10d_v065_signal},
    "f10_tier1_leverage_equity_ewma_21d_v066_signal": {"func": f10_tier1_leverage_equity_ewma_21d_v066_signal},
    "f10_tier1_leverage_assets_ewma_21d_v067_signal": {"func": f10_tier1_leverage_assets_ewma_21d_v067_signal},
    "f10_tier1_leverage_debt_ewma_21d_v068_signal": {"func": f10_tier1_leverage_debt_ewma_21d_v068_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_21d_v069_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_21d_v069_signal},
    "f10_tier1_leverage_total_leverage_ewma_21d_v070_signal": {"func": f10_tier1_leverage_total_leverage_ewma_21d_v070_signal},
    "f10_tier1_leverage_equity_ewma_42d_v071_signal": {"func": f10_tier1_leverage_equity_ewma_42d_v071_signal},
    "f10_tier1_leverage_assets_ewma_42d_v072_signal": {"func": f10_tier1_leverage_assets_ewma_42d_v072_signal},
    "f10_tier1_leverage_debt_ewma_42d_v073_signal": {"func": f10_tier1_leverage_debt_ewma_42d_v073_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_42d_v074_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_42d_v074_signal},
    "f10_tier1_leverage_total_leverage_ewma_42d_v075_signal": {"func": f10_tier1_leverage_total_leverage_ewma_42d_v075_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "debt": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 10...")
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
