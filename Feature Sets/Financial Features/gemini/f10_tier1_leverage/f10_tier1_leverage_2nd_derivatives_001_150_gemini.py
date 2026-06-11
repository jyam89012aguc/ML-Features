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

def f10_tier1_leverage_equity_slope_pct_5d_v001_signal(equity):
    """Percentage slope for Raw level of equity over 5d window."""
    res = _slope_pct(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_5d_v002_signal(assets):
    """Percentage slope for Raw level of assets over 5d window."""
    res = _slope_pct(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_5d_v003_signal(debt):
    """Percentage slope for Raw level of debt over 5d window."""
    res = _slope_pct(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_5d_v004_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 5d window."""
    res = _slope_pct(_ratio(equity, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_5d_v005_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 5d window."""
    res = _slope_pct(_ratio(debt, equity), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_10d_v006_signal(equity):
    """Percentage slope for Raw level of equity over 10d window."""
    res = _slope_pct(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_10d_v007_signal(assets):
    """Percentage slope for Raw level of assets over 10d window."""
    res = _slope_pct(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_10d_v008_signal(debt):
    """Percentage slope for Raw level of debt over 10d window."""
    res = _slope_pct(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_10d_v009_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 10d window."""
    res = _slope_pct(_ratio(equity, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_10d_v010_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 10d window."""
    res = _slope_pct(_ratio(debt, equity), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_21d_v011_signal(equity):
    """Percentage slope for Raw level of equity over 21d window."""
    res = _slope_pct(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_21d_v012_signal(assets):
    """Percentage slope for Raw level of assets over 21d window."""
    res = _slope_pct(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_21d_v013_signal(debt):
    """Percentage slope for Raw level of debt over 21d window."""
    res = _slope_pct(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_21d_v014_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 21d window."""
    res = _slope_pct(_ratio(equity, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_21d_v015_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 21d window."""
    res = _slope_pct(_ratio(debt, equity), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_42d_v016_signal(equity):
    """Percentage slope for Raw level of equity over 42d window."""
    res = _slope_pct(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_42d_v017_signal(assets):
    """Percentage slope for Raw level of assets over 42d window."""
    res = _slope_pct(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_42d_v018_signal(debt):
    """Percentage slope for Raw level of debt over 42d window."""
    res = _slope_pct(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_42d_v019_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 42d window."""
    res = _slope_pct(_ratio(equity, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_42d_v020_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 42d window."""
    res = _slope_pct(_ratio(debt, equity), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_63d_v021_signal(equity):
    """Percentage slope for Raw level of equity over 63d window."""
    res = _slope_pct(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_63d_v022_signal(assets):
    """Percentage slope for Raw level of assets over 63d window."""
    res = _slope_pct(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_63d_v023_signal(debt):
    """Percentage slope for Raw level of debt over 63d window."""
    res = _slope_pct(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_63d_v024_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 63d window."""
    res = _slope_pct(_ratio(equity, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_63d_v025_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 63d window."""
    res = _slope_pct(_ratio(debt, equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_126d_v026_signal(equity):
    """Percentage slope for Raw level of equity over 126d window."""
    res = _slope_pct(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_126d_v027_signal(assets):
    """Percentage slope for Raw level of assets over 126d window."""
    res = _slope_pct(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_126d_v028_signal(debt):
    """Percentage slope for Raw level of debt over 126d window."""
    res = _slope_pct(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_126d_v029_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 126d window."""
    res = _slope_pct(_ratio(equity, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_126d_v030_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 126d window."""
    res = _slope_pct(_ratio(debt, equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_252d_v031_signal(equity):
    """Percentage slope for Raw level of equity over 252d window."""
    res = _slope_pct(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_252d_v032_signal(assets):
    """Percentage slope for Raw level of assets over 252d window."""
    res = _slope_pct(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_252d_v033_signal(debt):
    """Percentage slope for Raw level of debt over 252d window."""
    res = _slope_pct(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_252d_v034_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 252d window."""
    res = _slope_pct(_ratio(equity, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_252d_v035_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 252d window."""
    res = _slope_pct(_ratio(debt, equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_504d_v036_signal(equity):
    """Percentage slope for Raw level of equity over 504d window."""
    res = _slope_pct(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_504d_v037_signal(assets):
    """Percentage slope for Raw level of assets over 504d window."""
    res = _slope_pct(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_504d_v038_signal(debt):
    """Percentage slope for Raw level of debt over 504d window."""
    res = _slope_pct(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_504d_v039_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 504d window."""
    res = _slope_pct(_ratio(equity, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_504d_v040_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 504d window."""
    res = _slope_pct(_ratio(debt, equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_756d_v041_signal(equity):
    """Percentage slope for Raw level of equity over 756d window."""
    res = _slope_pct(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_756d_v042_signal(assets):
    """Percentage slope for Raw level of assets over 756d window."""
    res = _slope_pct(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_756d_v043_signal(debt):
    """Percentage slope for Raw level of debt over 756d window."""
    res = _slope_pct(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_756d_v044_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 756d window."""
    res = _slope_pct(_ratio(equity, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_756d_v045_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 756d window."""
    res = _slope_pct(_ratio(debt, equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_1008d_v046_signal(equity):
    """Percentage slope for Raw level of equity over 1008d window."""
    res = _slope_pct(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_1008d_v047_signal(assets):
    """Percentage slope for Raw level of assets over 1008d window."""
    res = _slope_pct(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_1008d_v048_signal(debt):
    """Percentage slope for Raw level of debt over 1008d window."""
    res = _slope_pct(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_1008d_v049_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 1008d window."""
    res = _slope_pct(_ratio(equity, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_1008d_v050_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 1008d window."""
    res = _slope_pct(_ratio(debt, equity), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_pct_1260d_v051_signal(equity):
    """Percentage slope for Raw level of equity over 1260d window."""
    res = _slope_pct(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_pct_1260d_v052_signal(assets):
    """Percentage slope for Raw level of assets over 1260d window."""
    res = _slope_pct(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_pct_1260d_v053_signal(debt):
    """Percentage slope for Raw level of debt over 1260d window."""
    res = _slope_pct(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_pct_1260d_v054_signal(equity, assets):
    """Percentage slope for Capital adequacy proxy over 1260d window."""
    res = _slope_pct(_ratio(equity, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_pct_1260d_v055_signal(debt, equity):
    """Percentage slope for Total debt to equity ratio over 1260d window."""
    res = _slope_pct(_ratio(debt, equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_5d_v056_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 5d window."""
    res = _jerk(equity, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_5d_v057_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 5d window."""
    res = _jerk(assets, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_5d_v058_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 5d window."""
    res = _jerk(debt, 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_5d_v059_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 5d window."""
    res = _jerk(_ratio(equity, assets), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_5d_v060_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 5d window."""
    res = _jerk(_ratio(debt, equity), 5, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_10d_v061_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 10d window."""
    res = _jerk(equity, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_10d_v062_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 10d window."""
    res = _jerk(assets, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_10d_v063_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 10d window."""
    res = _jerk(debt, 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_10d_v064_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 10d window."""
    res = _jerk(_ratio(equity, assets), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_10d_v065_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 10d window."""
    res = _jerk(_ratio(debt, equity), 10, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_21d_v066_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 21d window."""
    res = _jerk(equity, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_21d_v067_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 21d window."""
    res = _jerk(assets, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_21d_v068_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 21d window."""
    res = _jerk(debt, 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_21d_v069_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 21d window."""
    res = _jerk(_ratio(equity, assets), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_21d_v070_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 21d window."""
    res = _jerk(_ratio(debt, equity), 21, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_42d_v071_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 42d window."""
    res = _jerk(equity, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_42d_v072_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 42d window."""
    res = _jerk(assets, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_42d_v073_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 42d window."""
    res = _jerk(debt, 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_42d_v074_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 42d window."""
    res = _jerk(_ratio(equity, assets), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_42d_v075_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 42d window."""
    res = _jerk(_ratio(debt, equity), 42, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_63d_v076_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 63d window."""
    res = _jerk(equity, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_63d_v077_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 63d window."""
    res = _jerk(assets, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_63d_v078_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 63d window."""
    res = _jerk(debt, 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_63d_v079_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 63d window."""
    res = _jerk(_ratio(equity, assets), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_63d_v080_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 63d window."""
    res = _jerk(_ratio(debt, equity), 63, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_126d_v081_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 126d window."""
    res = _jerk(equity, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_126d_v082_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 126d window."""
    res = _jerk(assets, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_126d_v083_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 126d window."""
    res = _jerk(debt, 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_126d_v084_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 126d window."""
    res = _jerk(_ratio(equity, assets), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_126d_v085_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 126d window."""
    res = _jerk(_ratio(debt, equity), 126, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_252d_v086_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 252d window."""
    res = _jerk(equity, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_252d_v087_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 252d window."""
    res = _jerk(assets, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_252d_v088_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 252d window."""
    res = _jerk(debt, 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_252d_v089_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 252d window."""
    res = _jerk(_ratio(equity, assets), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_252d_v090_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 252d window."""
    res = _jerk(_ratio(debt, equity), 252, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_504d_v091_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 504d window."""
    res = _jerk(equity, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_504d_v092_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 504d window."""
    res = _jerk(assets, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_504d_v093_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 504d window."""
    res = _jerk(debt, 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_504d_v094_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 504d window."""
    res = _jerk(_ratio(equity, assets), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_504d_v095_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 504d window."""
    res = _jerk(_ratio(debt, equity), 504, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_756d_v096_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 756d window."""
    res = _jerk(equity, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_756d_v097_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 756d window."""
    res = _jerk(assets, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_756d_v098_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 756d window."""
    res = _jerk(debt, 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_756d_v099_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 756d window."""
    res = _jerk(_ratio(equity, assets), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_756d_v100_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 756d window."""
    res = _jerk(_ratio(debt, equity), 756, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_1008d_v101_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 1008d window."""
    res = _jerk(equity, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_1008d_v102_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1008d window."""
    res = _jerk(assets, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_1008d_v103_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 1008d window."""
    res = _jerk(debt, 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_1008d_v104_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 1008d window."""
    res = _jerk(_ratio(equity, assets), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_1008d_v105_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 1008d window."""
    res = _jerk(_ratio(debt, equity), 1008, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_jerk_1260d_v106_signal(equity):
    """Acceleration/Jerk for Raw level of equity over 1260d window."""
    res = _jerk(equity, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_jerk_1260d_v107_signal(assets):
    """Acceleration/Jerk for Raw level of assets over 1260d window."""
    res = _jerk(assets, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_jerk_1260d_v108_signal(debt):
    """Acceleration/Jerk for Raw level of debt over 1260d window."""
    res = _jerk(debt, 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_jerk_1260d_v109_signal(equity, assets):
    """Acceleration/Jerk for Capital adequacy proxy over 1260d window."""
    res = _jerk(_ratio(equity, assets), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_jerk_1260d_v110_signal(debt, equity):
    """Acceleration/Jerk for Total debt to equity ratio over 1260d window."""
    res = _jerk(_ratio(debt, equity), 1260, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_5d_v111_signal(equity):
    """Normalized slope change for Raw level of equity over 5d window."""
    res = (_slope_pct(equity, 5).diff(5) / _sma(equity.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_5d_v112_signal(assets):
    """Normalized slope change for Raw level of assets over 5d window."""
    res = (_slope_pct(assets, 5).diff(5) / _sma(assets.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_5d_v113_signal(debt):
    """Normalized slope change for Raw level of debt over 5d window."""
    res = (_slope_pct(debt, 5).diff(5) / _sma(debt.abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_5d_v114_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 5d window."""
    res = (_slope_pct(_ratio(equity, assets), 5).diff(5) / _sma(_ratio(equity, assets).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_5d_v115_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 5d window."""
    res = (_slope_pct(_ratio(debt, equity), 5).diff(5) / _sma(_ratio(debt, equity).abs(), 5).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_10d_v116_signal(equity):
    """Normalized slope change for Raw level of equity over 10d window."""
    res = (_slope_pct(equity, 10).diff(10) / _sma(equity.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_10d_v117_signal(assets):
    """Normalized slope change for Raw level of assets over 10d window."""
    res = (_slope_pct(assets, 10).diff(10) / _sma(assets.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_10d_v118_signal(debt):
    """Normalized slope change for Raw level of debt over 10d window."""
    res = (_slope_pct(debt, 10).diff(10) / _sma(debt.abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_10d_v119_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 10d window."""
    res = (_slope_pct(_ratio(equity, assets), 10).diff(10) / _sma(_ratio(equity, assets).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_10d_v120_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 10d window."""
    res = (_slope_pct(_ratio(debt, equity), 10).diff(10) / _sma(_ratio(debt, equity).abs(), 10).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_21d_v121_signal(equity):
    """Normalized slope change for Raw level of equity over 21d window."""
    res = (_slope_pct(equity, 21).diff(21) / _sma(equity.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_21d_v122_signal(assets):
    """Normalized slope change for Raw level of assets over 21d window."""
    res = (_slope_pct(assets, 21).diff(21) / _sma(assets.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_21d_v123_signal(debt):
    """Normalized slope change for Raw level of debt over 21d window."""
    res = (_slope_pct(debt, 21).diff(21) / _sma(debt.abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_21d_v124_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 21d window."""
    res = (_slope_pct(_ratio(equity, assets), 21).diff(21) / _sma(_ratio(equity, assets).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_21d_v125_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 21d window."""
    res = (_slope_pct(_ratio(debt, equity), 21).diff(21) / _sma(_ratio(debt, equity).abs(), 21).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_42d_v126_signal(equity):
    """Normalized slope change for Raw level of equity over 42d window."""
    res = (_slope_pct(equity, 42).diff(42) / _sma(equity.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_42d_v127_signal(assets):
    """Normalized slope change for Raw level of assets over 42d window."""
    res = (_slope_pct(assets, 42).diff(42) / _sma(assets.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_42d_v128_signal(debt):
    """Normalized slope change for Raw level of debt over 42d window."""
    res = (_slope_pct(debt, 42).diff(42) / _sma(debt.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_42d_v129_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 42d window."""
    res = (_slope_pct(_ratio(equity, assets), 42).diff(42) / _sma(_ratio(equity, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_42d_v130_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 42d window."""
    res = (_slope_pct(_ratio(debt, equity), 42).diff(42) / _sma(_ratio(debt, equity).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_63d_v131_signal(equity):
    """Normalized slope change for Raw level of equity over 63d window."""
    res = (_slope_pct(equity, 63).diff(63) / _sma(equity.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_63d_v132_signal(assets):
    """Normalized slope change for Raw level of assets over 63d window."""
    res = (_slope_pct(assets, 63).diff(63) / _sma(assets.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_63d_v133_signal(debt):
    """Normalized slope change for Raw level of debt over 63d window."""
    res = (_slope_pct(debt, 63).diff(63) / _sma(debt.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_63d_v134_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 63d window."""
    res = (_slope_pct(_ratio(equity, assets), 63).diff(63) / _sma(_ratio(equity, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_63d_v135_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 63d window."""
    res = (_slope_pct(_ratio(debt, equity), 63).diff(63) / _sma(_ratio(debt, equity).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_126d_v136_signal(equity):
    """Normalized slope change for Raw level of equity over 126d window."""
    res = (_slope_pct(equity, 126).diff(126) / _sma(equity.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_126d_v137_signal(assets):
    """Normalized slope change for Raw level of assets over 126d window."""
    res = (_slope_pct(assets, 126).diff(126) / _sma(assets.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_126d_v138_signal(debt):
    """Normalized slope change for Raw level of debt over 126d window."""
    res = (_slope_pct(debt, 126).diff(126) / _sma(debt.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_126d_v139_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 126d window."""
    res = (_slope_pct(_ratio(equity, assets), 126).diff(126) / _sma(_ratio(equity, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_126d_v140_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 126d window."""
    res = (_slope_pct(_ratio(debt, equity), 126).diff(126) / _sma(_ratio(debt, equity).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_252d_v141_signal(equity):
    """Normalized slope change for Raw level of equity over 252d window."""
    res = (_slope_pct(equity, 252).diff(252) / _sma(equity.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_252d_v142_signal(assets):
    """Normalized slope change for Raw level of assets over 252d window."""
    res = (_slope_pct(assets, 252).diff(252) / _sma(assets.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_252d_v143_signal(debt):
    """Normalized slope change for Raw level of debt over 252d window."""
    res = (_slope_pct(debt, 252).diff(252) / _sma(debt.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_252d_v144_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 252d window."""
    res = (_slope_pct(_ratio(equity, assets), 252).diff(252) / _sma(_ratio(equity, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_252d_v145_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 252d window."""
    res = (_slope_pct(_ratio(debt, equity), 252).diff(252) / _sma(_ratio(debt, equity).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_slope_diff_norm_504d_v146_signal(equity):
    """Normalized slope change for Raw level of equity over 504d window."""
    res = (_slope_pct(equity, 504).diff(504) / _sma(equity.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_slope_diff_norm_504d_v147_signal(assets):
    """Normalized slope change for Raw level of assets over 504d window."""
    res = (_slope_pct(assets, 504).diff(504) / _sma(assets.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_slope_diff_norm_504d_v148_signal(debt):
    """Normalized slope change for Raw level of debt over 504d window."""
    res = (_slope_pct(debt, 504).diff(504) / _sma(debt.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_slope_diff_norm_504d_v149_signal(equity, assets):
    """Normalized slope change for Capital adequacy proxy over 504d window."""
    res = (_slope_pct(_ratio(equity, assets), 504).diff(504) / _sma(_ratio(equity, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_slope_diff_norm_504d_v150_signal(debt, equity):
    """Normalized slope change for Total debt to equity ratio over 504d window."""
    res = (_slope_pct(_ratio(debt, equity), 504).diff(504) / _sma(_ratio(debt, equity).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f10_tier1_leverage_equity_slope_pct_5d_v001_signal": {"func": f10_tier1_leverage_equity_slope_pct_5d_v001_signal},
    "f10_tier1_leverage_assets_slope_pct_5d_v002_signal": {"func": f10_tier1_leverage_assets_slope_pct_5d_v002_signal},
    "f10_tier1_leverage_debt_slope_pct_5d_v003_signal": {"func": f10_tier1_leverage_debt_slope_pct_5d_v003_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_5d_v004_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_5d_v004_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_5d_v005_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_5d_v005_signal},
    "f10_tier1_leverage_equity_slope_pct_10d_v006_signal": {"func": f10_tier1_leverage_equity_slope_pct_10d_v006_signal},
    "f10_tier1_leverage_assets_slope_pct_10d_v007_signal": {"func": f10_tier1_leverage_assets_slope_pct_10d_v007_signal},
    "f10_tier1_leverage_debt_slope_pct_10d_v008_signal": {"func": f10_tier1_leverage_debt_slope_pct_10d_v008_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_10d_v009_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_10d_v009_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_10d_v010_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_10d_v010_signal},
    "f10_tier1_leverage_equity_slope_pct_21d_v011_signal": {"func": f10_tier1_leverage_equity_slope_pct_21d_v011_signal},
    "f10_tier1_leverage_assets_slope_pct_21d_v012_signal": {"func": f10_tier1_leverage_assets_slope_pct_21d_v012_signal},
    "f10_tier1_leverage_debt_slope_pct_21d_v013_signal": {"func": f10_tier1_leverage_debt_slope_pct_21d_v013_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_21d_v014_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_21d_v014_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_21d_v015_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_21d_v015_signal},
    "f10_tier1_leverage_equity_slope_pct_42d_v016_signal": {"func": f10_tier1_leverage_equity_slope_pct_42d_v016_signal},
    "f10_tier1_leverage_assets_slope_pct_42d_v017_signal": {"func": f10_tier1_leverage_assets_slope_pct_42d_v017_signal},
    "f10_tier1_leverage_debt_slope_pct_42d_v018_signal": {"func": f10_tier1_leverage_debt_slope_pct_42d_v018_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_42d_v019_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_42d_v019_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_42d_v020_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_42d_v020_signal},
    "f10_tier1_leverage_equity_slope_pct_63d_v021_signal": {"func": f10_tier1_leverage_equity_slope_pct_63d_v021_signal},
    "f10_tier1_leverage_assets_slope_pct_63d_v022_signal": {"func": f10_tier1_leverage_assets_slope_pct_63d_v022_signal},
    "f10_tier1_leverage_debt_slope_pct_63d_v023_signal": {"func": f10_tier1_leverage_debt_slope_pct_63d_v023_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_63d_v024_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_63d_v024_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_63d_v025_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_63d_v025_signal},
    "f10_tier1_leverage_equity_slope_pct_126d_v026_signal": {"func": f10_tier1_leverage_equity_slope_pct_126d_v026_signal},
    "f10_tier1_leverage_assets_slope_pct_126d_v027_signal": {"func": f10_tier1_leverage_assets_slope_pct_126d_v027_signal},
    "f10_tier1_leverage_debt_slope_pct_126d_v028_signal": {"func": f10_tier1_leverage_debt_slope_pct_126d_v028_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_126d_v029_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_126d_v029_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_126d_v030_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_126d_v030_signal},
    "f10_tier1_leverage_equity_slope_pct_252d_v031_signal": {"func": f10_tier1_leverage_equity_slope_pct_252d_v031_signal},
    "f10_tier1_leverage_assets_slope_pct_252d_v032_signal": {"func": f10_tier1_leverage_assets_slope_pct_252d_v032_signal},
    "f10_tier1_leverage_debt_slope_pct_252d_v033_signal": {"func": f10_tier1_leverage_debt_slope_pct_252d_v033_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_252d_v034_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_252d_v034_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_252d_v035_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_252d_v035_signal},
    "f10_tier1_leverage_equity_slope_pct_504d_v036_signal": {"func": f10_tier1_leverage_equity_slope_pct_504d_v036_signal},
    "f10_tier1_leverage_assets_slope_pct_504d_v037_signal": {"func": f10_tier1_leverage_assets_slope_pct_504d_v037_signal},
    "f10_tier1_leverage_debt_slope_pct_504d_v038_signal": {"func": f10_tier1_leverage_debt_slope_pct_504d_v038_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_504d_v039_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_504d_v039_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_504d_v040_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_504d_v040_signal},
    "f10_tier1_leverage_equity_slope_pct_756d_v041_signal": {"func": f10_tier1_leverage_equity_slope_pct_756d_v041_signal},
    "f10_tier1_leverage_assets_slope_pct_756d_v042_signal": {"func": f10_tier1_leverage_assets_slope_pct_756d_v042_signal},
    "f10_tier1_leverage_debt_slope_pct_756d_v043_signal": {"func": f10_tier1_leverage_debt_slope_pct_756d_v043_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_756d_v044_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_756d_v044_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_756d_v045_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_756d_v045_signal},
    "f10_tier1_leverage_equity_slope_pct_1008d_v046_signal": {"func": f10_tier1_leverage_equity_slope_pct_1008d_v046_signal},
    "f10_tier1_leverage_assets_slope_pct_1008d_v047_signal": {"func": f10_tier1_leverage_assets_slope_pct_1008d_v047_signal},
    "f10_tier1_leverage_debt_slope_pct_1008d_v048_signal": {"func": f10_tier1_leverage_debt_slope_pct_1008d_v048_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_1008d_v049_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_1008d_v049_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_1008d_v050_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_1008d_v050_signal},
    "f10_tier1_leverage_equity_slope_pct_1260d_v051_signal": {"func": f10_tier1_leverage_equity_slope_pct_1260d_v051_signal},
    "f10_tier1_leverage_assets_slope_pct_1260d_v052_signal": {"func": f10_tier1_leverage_assets_slope_pct_1260d_v052_signal},
    "f10_tier1_leverage_debt_slope_pct_1260d_v053_signal": {"func": f10_tier1_leverage_debt_slope_pct_1260d_v053_signal},
    "f10_tier1_leverage_tier1_proxy_slope_pct_1260d_v054_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_pct_1260d_v054_signal},
    "f10_tier1_leverage_total_leverage_slope_pct_1260d_v055_signal": {"func": f10_tier1_leverage_total_leverage_slope_pct_1260d_v055_signal},
    "f10_tier1_leverage_equity_jerk_5d_v056_signal": {"func": f10_tier1_leverage_equity_jerk_5d_v056_signal},
    "f10_tier1_leverage_assets_jerk_5d_v057_signal": {"func": f10_tier1_leverage_assets_jerk_5d_v057_signal},
    "f10_tier1_leverage_debt_jerk_5d_v058_signal": {"func": f10_tier1_leverage_debt_jerk_5d_v058_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_5d_v059_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_5d_v059_signal},
    "f10_tier1_leverage_total_leverage_jerk_5d_v060_signal": {"func": f10_tier1_leverage_total_leverage_jerk_5d_v060_signal},
    "f10_tier1_leverage_equity_jerk_10d_v061_signal": {"func": f10_tier1_leverage_equity_jerk_10d_v061_signal},
    "f10_tier1_leverage_assets_jerk_10d_v062_signal": {"func": f10_tier1_leverage_assets_jerk_10d_v062_signal},
    "f10_tier1_leverage_debt_jerk_10d_v063_signal": {"func": f10_tier1_leverage_debt_jerk_10d_v063_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_10d_v064_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_10d_v064_signal},
    "f10_tier1_leverage_total_leverage_jerk_10d_v065_signal": {"func": f10_tier1_leverage_total_leverage_jerk_10d_v065_signal},
    "f10_tier1_leverage_equity_jerk_21d_v066_signal": {"func": f10_tier1_leverage_equity_jerk_21d_v066_signal},
    "f10_tier1_leverage_assets_jerk_21d_v067_signal": {"func": f10_tier1_leverage_assets_jerk_21d_v067_signal},
    "f10_tier1_leverage_debt_jerk_21d_v068_signal": {"func": f10_tier1_leverage_debt_jerk_21d_v068_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_21d_v069_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_21d_v069_signal},
    "f10_tier1_leverage_total_leverage_jerk_21d_v070_signal": {"func": f10_tier1_leverage_total_leverage_jerk_21d_v070_signal},
    "f10_tier1_leverage_equity_jerk_42d_v071_signal": {"func": f10_tier1_leverage_equity_jerk_42d_v071_signal},
    "f10_tier1_leverage_assets_jerk_42d_v072_signal": {"func": f10_tier1_leverage_assets_jerk_42d_v072_signal},
    "f10_tier1_leverage_debt_jerk_42d_v073_signal": {"func": f10_tier1_leverage_debt_jerk_42d_v073_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_42d_v074_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_42d_v074_signal},
    "f10_tier1_leverage_total_leverage_jerk_42d_v075_signal": {"func": f10_tier1_leverage_total_leverage_jerk_42d_v075_signal},
    "f10_tier1_leverage_equity_jerk_63d_v076_signal": {"func": f10_tier1_leverage_equity_jerk_63d_v076_signal},
    "f10_tier1_leverage_assets_jerk_63d_v077_signal": {"func": f10_tier1_leverage_assets_jerk_63d_v077_signal},
    "f10_tier1_leverage_debt_jerk_63d_v078_signal": {"func": f10_tier1_leverage_debt_jerk_63d_v078_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_63d_v079_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_63d_v079_signal},
    "f10_tier1_leverage_total_leverage_jerk_63d_v080_signal": {"func": f10_tier1_leverage_total_leverage_jerk_63d_v080_signal},
    "f10_tier1_leverage_equity_jerk_126d_v081_signal": {"func": f10_tier1_leverage_equity_jerk_126d_v081_signal},
    "f10_tier1_leverage_assets_jerk_126d_v082_signal": {"func": f10_tier1_leverage_assets_jerk_126d_v082_signal},
    "f10_tier1_leverage_debt_jerk_126d_v083_signal": {"func": f10_tier1_leverage_debt_jerk_126d_v083_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_126d_v084_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_126d_v084_signal},
    "f10_tier1_leverage_total_leverage_jerk_126d_v085_signal": {"func": f10_tier1_leverage_total_leverage_jerk_126d_v085_signal},
    "f10_tier1_leverage_equity_jerk_252d_v086_signal": {"func": f10_tier1_leverage_equity_jerk_252d_v086_signal},
    "f10_tier1_leverage_assets_jerk_252d_v087_signal": {"func": f10_tier1_leverage_assets_jerk_252d_v087_signal},
    "f10_tier1_leverage_debt_jerk_252d_v088_signal": {"func": f10_tier1_leverage_debt_jerk_252d_v088_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_252d_v089_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_252d_v089_signal},
    "f10_tier1_leverage_total_leverage_jerk_252d_v090_signal": {"func": f10_tier1_leverage_total_leverage_jerk_252d_v090_signal},
    "f10_tier1_leverage_equity_jerk_504d_v091_signal": {"func": f10_tier1_leverage_equity_jerk_504d_v091_signal},
    "f10_tier1_leverage_assets_jerk_504d_v092_signal": {"func": f10_tier1_leverage_assets_jerk_504d_v092_signal},
    "f10_tier1_leverage_debt_jerk_504d_v093_signal": {"func": f10_tier1_leverage_debt_jerk_504d_v093_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_504d_v094_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_504d_v094_signal},
    "f10_tier1_leverage_total_leverage_jerk_504d_v095_signal": {"func": f10_tier1_leverage_total_leverage_jerk_504d_v095_signal},
    "f10_tier1_leverage_equity_jerk_756d_v096_signal": {"func": f10_tier1_leverage_equity_jerk_756d_v096_signal},
    "f10_tier1_leverage_assets_jerk_756d_v097_signal": {"func": f10_tier1_leverage_assets_jerk_756d_v097_signal},
    "f10_tier1_leverage_debt_jerk_756d_v098_signal": {"func": f10_tier1_leverage_debt_jerk_756d_v098_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_756d_v099_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_756d_v099_signal},
    "f10_tier1_leverage_total_leverage_jerk_756d_v100_signal": {"func": f10_tier1_leverage_total_leverage_jerk_756d_v100_signal},
    "f10_tier1_leverage_equity_jerk_1008d_v101_signal": {"func": f10_tier1_leverage_equity_jerk_1008d_v101_signal},
    "f10_tier1_leverage_assets_jerk_1008d_v102_signal": {"func": f10_tier1_leverage_assets_jerk_1008d_v102_signal},
    "f10_tier1_leverage_debt_jerk_1008d_v103_signal": {"func": f10_tier1_leverage_debt_jerk_1008d_v103_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_1008d_v104_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_1008d_v104_signal},
    "f10_tier1_leverage_total_leverage_jerk_1008d_v105_signal": {"func": f10_tier1_leverage_total_leverage_jerk_1008d_v105_signal},
    "f10_tier1_leverage_equity_jerk_1260d_v106_signal": {"func": f10_tier1_leverage_equity_jerk_1260d_v106_signal},
    "f10_tier1_leverage_assets_jerk_1260d_v107_signal": {"func": f10_tier1_leverage_assets_jerk_1260d_v107_signal},
    "f10_tier1_leverage_debt_jerk_1260d_v108_signal": {"func": f10_tier1_leverage_debt_jerk_1260d_v108_signal},
    "f10_tier1_leverage_tier1_proxy_jerk_1260d_v109_signal": {"func": f10_tier1_leverage_tier1_proxy_jerk_1260d_v109_signal},
    "f10_tier1_leverage_total_leverage_jerk_1260d_v110_signal": {"func": f10_tier1_leverage_total_leverage_jerk_1260d_v110_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_5d_v111_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_5d_v111_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_5d_v112_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_5d_v112_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_5d_v113_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_5d_v113_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_5d_v114_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_5d_v114_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_5d_v115_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_5d_v115_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_10d_v116_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_10d_v116_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_10d_v117_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_10d_v117_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_10d_v118_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_10d_v118_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_10d_v119_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_10d_v119_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_10d_v120_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_10d_v120_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_21d_v121_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_21d_v121_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_21d_v122_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_21d_v122_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_21d_v123_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_21d_v123_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_21d_v124_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_21d_v124_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_21d_v125_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_21d_v125_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_42d_v126_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_42d_v126_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_42d_v127_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_42d_v127_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_42d_v128_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_42d_v128_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_42d_v129_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_42d_v129_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_42d_v130_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_42d_v130_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_63d_v131_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_63d_v131_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_63d_v132_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_63d_v132_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_63d_v133_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_63d_v133_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_63d_v134_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_63d_v134_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_63d_v135_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_63d_v135_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_126d_v136_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_126d_v136_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_126d_v137_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_126d_v137_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_126d_v138_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_126d_v138_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_126d_v139_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_126d_v139_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_126d_v140_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_126d_v140_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_252d_v141_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_252d_v141_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_252d_v142_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_252d_v142_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_252d_v143_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_252d_v143_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_252d_v144_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_252d_v144_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_252d_v145_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_252d_v145_signal},
    "f10_tier1_leverage_equity_slope_diff_norm_504d_v146_signal": {"func": f10_tier1_leverage_equity_slope_diff_norm_504d_v146_signal},
    "f10_tier1_leverage_assets_slope_diff_norm_504d_v147_signal": {"func": f10_tier1_leverage_assets_slope_diff_norm_504d_v147_signal},
    "f10_tier1_leverage_debt_slope_diff_norm_504d_v148_signal": {"func": f10_tier1_leverage_debt_slope_diff_norm_504d_v148_signal},
    "f10_tier1_leverage_tier1_proxy_slope_diff_norm_504d_v149_signal": {"func": f10_tier1_leverage_tier1_proxy_slope_diff_norm_504d_v149_signal},
    "f10_tier1_leverage_total_leverage_slope_diff_norm_504d_v150_signal": {"func": f10_tier1_leverage_total_leverage_slope_diff_norm_504d_v150_signal},
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
