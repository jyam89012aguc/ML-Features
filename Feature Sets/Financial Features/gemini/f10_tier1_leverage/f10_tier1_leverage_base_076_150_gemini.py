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

def f10_tier1_leverage_equity_ewma_63d_v076_signal(equity):
    """Exponential moving average of Raw level of equity over 63d window."""
    res = _ewma(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_63d_v077_signal(assets):
    """Exponential moving average of Raw level of assets over 63d window."""
    res = _ewma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_63d_v078_signal(debt):
    """Exponential moving average of Raw level of debt over 63d window."""
    res = _ewma(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_63d_v079_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 63d window."""
    res = _ewma(_ratio(equity, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_63d_v080_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 63d window."""
    res = _ewma(_ratio(debt, equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_126d_v081_signal(equity):
    """Exponential moving average of Raw level of equity over 126d window."""
    res = _ewma(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_126d_v082_signal(assets):
    """Exponential moving average of Raw level of assets over 126d window."""
    res = _ewma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_126d_v083_signal(debt):
    """Exponential moving average of Raw level of debt over 126d window."""
    res = _ewma(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_126d_v084_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 126d window."""
    res = _ewma(_ratio(equity, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_126d_v085_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 126d window."""
    res = _ewma(_ratio(debt, equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_252d_v086_signal(equity):
    """Exponential moving average of Raw level of equity over 252d window."""
    res = _ewma(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_252d_v087_signal(assets):
    """Exponential moving average of Raw level of assets over 252d window."""
    res = _ewma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_252d_v088_signal(debt):
    """Exponential moving average of Raw level of debt over 252d window."""
    res = _ewma(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_252d_v089_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 252d window."""
    res = _ewma(_ratio(equity, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_252d_v090_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 252d window."""
    res = _ewma(_ratio(debt, equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_504d_v091_signal(equity):
    """Exponential moving average of Raw level of equity over 504d window."""
    res = _ewma(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_504d_v092_signal(assets):
    """Exponential moving average of Raw level of assets over 504d window."""
    res = _ewma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_504d_v093_signal(debt):
    """Exponential moving average of Raw level of debt over 504d window."""
    res = _ewma(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_504d_v094_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 504d window."""
    res = _ewma(_ratio(equity, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_504d_v095_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 504d window."""
    res = _ewma(_ratio(debt, equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_756d_v096_signal(equity):
    """Exponential moving average of Raw level of equity over 756d window."""
    res = _ewma(equity, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_756d_v097_signal(assets):
    """Exponential moving average of Raw level of assets over 756d window."""
    res = _ewma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_756d_v098_signal(debt):
    """Exponential moving average of Raw level of debt over 756d window."""
    res = _ewma(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_756d_v099_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 756d window."""
    res = _ewma(_ratio(equity, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_756d_v100_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 756d window."""
    res = _ewma(_ratio(debt, equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_1008d_v101_signal(equity):
    """Exponential moving average of Raw level of equity over 1008d window."""
    res = _ewma(equity, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_1008d_v102_signal(assets):
    """Exponential moving average of Raw level of assets over 1008d window."""
    res = _ewma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_1008d_v103_signal(debt):
    """Exponential moving average of Raw level of debt over 1008d window."""
    res = _ewma(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_1008d_v104_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 1008d window."""
    res = _ewma(_ratio(equity, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_1008d_v105_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 1008d window."""
    res = _ewma(_ratio(debt, equity), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_ewma_1260d_v106_signal(equity):
    """Exponential moving average of Raw level of equity over 1260d window."""
    res = _ewma(equity, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_ewma_1260d_v107_signal(assets):
    """Exponential moving average of Raw level of assets over 1260d window."""
    res = _ewma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_ewma_1260d_v108_signal(debt):
    """Exponential moving average of Raw level of debt over 1260d window."""
    res = _ewma(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_ewma_1260d_v109_signal(equity, assets):
    """Exponential moving average of Capital adequacy proxy over 1260d window."""
    res = _ewma(_ratio(equity, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_ewma_1260d_v110_signal(debt, equity):
    """Exponential moving average of Total debt to equity ratio over 1260d window."""
    res = _ewma(_ratio(debt, equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_z_5d_v111_signal(equity):
    """Z-score of Raw level of equity over 5d window."""
    res = _z(equity, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_z_5d_v112_signal(assets):
    """Z-score of Raw level of assets over 5d window."""
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_z_5d_v113_signal(debt):
    """Z-score of Raw level of debt over 5d window."""
    res = _z(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_z_5d_v114_signal(equity, assets):
    """Z-score of Capital adequacy proxy over 5d window."""
    res = _z(_ratio(equity, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_z_5d_v115_signal(debt, equity):
    """Z-score of Total debt to equity ratio over 5d window."""
    res = _z(_ratio(debt, equity), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_z_10d_v116_signal(equity):
    """Z-score of Raw level of equity over 10d window."""
    res = _z(equity, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_z_10d_v117_signal(assets):
    """Z-score of Raw level of assets over 10d window."""
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_z_10d_v118_signal(debt):
    """Z-score of Raw level of debt over 10d window."""
    res = _z(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_z_10d_v119_signal(equity, assets):
    """Z-score of Capital adequacy proxy over 10d window."""
    res = _z(_ratio(equity, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_z_10d_v120_signal(debt, equity):
    """Z-score of Total debt to equity ratio over 10d window."""
    res = _z(_ratio(debt, equity), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_z_21d_v121_signal(equity):
    """Z-score of Raw level of equity over 21d window."""
    res = _z(equity, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_z_21d_v122_signal(assets):
    """Z-score of Raw level of assets over 21d window."""
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_z_21d_v123_signal(debt):
    """Z-score of Raw level of debt over 21d window."""
    res = _z(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_z_21d_v124_signal(equity, assets):
    """Z-score of Capital adequacy proxy over 21d window."""
    res = _z(_ratio(equity, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_z_21d_v125_signal(debt, equity):
    """Z-score of Total debt to equity ratio over 21d window."""
    res = _z(_ratio(debt, equity), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_z_42d_v126_signal(equity):
    """Z-score of Raw level of equity over 42d window."""
    res = _z(equity, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_z_42d_v127_signal(assets):
    """Z-score of Raw level of assets over 42d window."""
    res = _z(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_z_42d_v128_signal(debt):
    """Z-score of Raw level of debt over 42d window."""
    res = _z(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_z_42d_v129_signal(equity, assets):
    """Z-score of Capital adequacy proxy over 42d window."""
    res = _z(_ratio(equity, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_z_42d_v130_signal(debt, equity):
    """Z-score of Total debt to equity ratio over 42d window."""
    res = _z(_ratio(debt, equity), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_z_63d_v131_signal(equity):
    """Z-score of Raw level of equity over 63d window."""
    res = _z(equity, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_z_63d_v132_signal(assets):
    """Z-score of Raw level of assets over 63d window."""
    res = _z(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_z_63d_v133_signal(debt):
    """Z-score of Raw level of debt over 63d window."""
    res = _z(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_z_63d_v134_signal(equity, assets):
    """Z-score of Capital adequacy proxy over 63d window."""
    res = _z(_ratio(equity, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_z_63d_v135_signal(debt, equity):
    """Z-score of Total debt to equity ratio over 63d window."""
    res = _z(_ratio(debt, equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_z_126d_v136_signal(equity):
    """Z-score of Raw level of equity over 126d window."""
    res = _z(equity, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_z_126d_v137_signal(assets):
    """Z-score of Raw level of assets over 126d window."""
    res = _z(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_z_126d_v138_signal(debt):
    """Z-score of Raw level of debt over 126d window."""
    res = _z(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_z_126d_v139_signal(equity, assets):
    """Z-score of Capital adequacy proxy over 126d window."""
    res = _z(_ratio(equity, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_z_126d_v140_signal(debt, equity):
    """Z-score of Total debt to equity ratio over 126d window."""
    res = _z(_ratio(debt, equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_z_252d_v141_signal(equity):
    """Z-score of Raw level of equity over 252d window."""
    res = _z(equity, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_z_252d_v142_signal(assets):
    """Z-score of Raw level of assets over 252d window."""
    res = _z(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_z_252d_v143_signal(debt):
    """Z-score of Raw level of debt over 252d window."""
    res = _z(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_z_252d_v144_signal(equity, assets):
    """Z-score of Capital adequacy proxy over 252d window."""
    res = _z(_ratio(equity, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_z_252d_v145_signal(debt, equity):
    """Z-score of Total debt to equity ratio over 252d window."""
    res = _z(_ratio(debt, equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_equity_z_504d_v146_signal(equity):
    """Z-score of Raw level of equity over 504d window."""
    res = _z(equity, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_assets_z_504d_v147_signal(assets):
    """Z-score of Raw level of assets over 504d window."""
    res = _z(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_debt_z_504d_v148_signal(debt):
    """Z-score of Raw level of debt over 504d window."""
    res = _z(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_tier1_proxy_z_504d_v149_signal(equity, assets):
    """Z-score of Capital adequacy proxy over 504d window."""
    res = _z(_ratio(equity, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_tier1_leverage_total_leverage_z_504d_v150_signal(debt, equity):
    """Z-score of Total debt to equity ratio over 504d window."""
    res = _z(_ratio(debt, equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f10_tier1_leverage_equity_ewma_63d_v076_signal": {"func": f10_tier1_leverage_equity_ewma_63d_v076_signal},
    "f10_tier1_leverage_assets_ewma_63d_v077_signal": {"func": f10_tier1_leverage_assets_ewma_63d_v077_signal},
    "f10_tier1_leverage_debt_ewma_63d_v078_signal": {"func": f10_tier1_leverage_debt_ewma_63d_v078_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_63d_v079_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_63d_v079_signal},
    "f10_tier1_leverage_total_leverage_ewma_63d_v080_signal": {"func": f10_tier1_leverage_total_leverage_ewma_63d_v080_signal},
    "f10_tier1_leverage_equity_ewma_126d_v081_signal": {"func": f10_tier1_leverage_equity_ewma_126d_v081_signal},
    "f10_tier1_leverage_assets_ewma_126d_v082_signal": {"func": f10_tier1_leverage_assets_ewma_126d_v082_signal},
    "f10_tier1_leverage_debt_ewma_126d_v083_signal": {"func": f10_tier1_leverage_debt_ewma_126d_v083_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_126d_v084_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_126d_v084_signal},
    "f10_tier1_leverage_total_leverage_ewma_126d_v085_signal": {"func": f10_tier1_leverage_total_leverage_ewma_126d_v085_signal},
    "f10_tier1_leverage_equity_ewma_252d_v086_signal": {"func": f10_tier1_leverage_equity_ewma_252d_v086_signal},
    "f10_tier1_leverage_assets_ewma_252d_v087_signal": {"func": f10_tier1_leverage_assets_ewma_252d_v087_signal},
    "f10_tier1_leverage_debt_ewma_252d_v088_signal": {"func": f10_tier1_leverage_debt_ewma_252d_v088_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_252d_v089_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_252d_v089_signal},
    "f10_tier1_leverage_total_leverage_ewma_252d_v090_signal": {"func": f10_tier1_leverage_total_leverage_ewma_252d_v090_signal},
    "f10_tier1_leverage_equity_ewma_504d_v091_signal": {"func": f10_tier1_leverage_equity_ewma_504d_v091_signal},
    "f10_tier1_leverage_assets_ewma_504d_v092_signal": {"func": f10_tier1_leverage_assets_ewma_504d_v092_signal},
    "f10_tier1_leverage_debt_ewma_504d_v093_signal": {"func": f10_tier1_leverage_debt_ewma_504d_v093_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_504d_v094_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_504d_v094_signal},
    "f10_tier1_leverage_total_leverage_ewma_504d_v095_signal": {"func": f10_tier1_leverage_total_leverage_ewma_504d_v095_signal},
    "f10_tier1_leverage_equity_ewma_756d_v096_signal": {"func": f10_tier1_leverage_equity_ewma_756d_v096_signal},
    "f10_tier1_leverage_assets_ewma_756d_v097_signal": {"func": f10_tier1_leverage_assets_ewma_756d_v097_signal},
    "f10_tier1_leverage_debt_ewma_756d_v098_signal": {"func": f10_tier1_leverage_debt_ewma_756d_v098_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_756d_v099_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_756d_v099_signal},
    "f10_tier1_leverage_total_leverage_ewma_756d_v100_signal": {"func": f10_tier1_leverage_total_leverage_ewma_756d_v100_signal},
    "f10_tier1_leverage_equity_ewma_1008d_v101_signal": {"func": f10_tier1_leverage_equity_ewma_1008d_v101_signal},
    "f10_tier1_leverage_assets_ewma_1008d_v102_signal": {"func": f10_tier1_leverage_assets_ewma_1008d_v102_signal},
    "f10_tier1_leverage_debt_ewma_1008d_v103_signal": {"func": f10_tier1_leverage_debt_ewma_1008d_v103_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_1008d_v104_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_1008d_v104_signal},
    "f10_tier1_leverage_total_leverage_ewma_1008d_v105_signal": {"func": f10_tier1_leverage_total_leverage_ewma_1008d_v105_signal},
    "f10_tier1_leverage_equity_ewma_1260d_v106_signal": {"func": f10_tier1_leverage_equity_ewma_1260d_v106_signal},
    "f10_tier1_leverage_assets_ewma_1260d_v107_signal": {"func": f10_tier1_leverage_assets_ewma_1260d_v107_signal},
    "f10_tier1_leverage_debt_ewma_1260d_v108_signal": {"func": f10_tier1_leverage_debt_ewma_1260d_v108_signal},
    "f10_tier1_leverage_tier1_proxy_ewma_1260d_v109_signal": {"func": f10_tier1_leverage_tier1_proxy_ewma_1260d_v109_signal},
    "f10_tier1_leverage_total_leverage_ewma_1260d_v110_signal": {"func": f10_tier1_leverage_total_leverage_ewma_1260d_v110_signal},
    "f10_tier1_leverage_equity_z_5d_v111_signal": {"func": f10_tier1_leverage_equity_z_5d_v111_signal},
    "f10_tier1_leverage_assets_z_5d_v112_signal": {"func": f10_tier1_leverage_assets_z_5d_v112_signal},
    "f10_tier1_leverage_debt_z_5d_v113_signal": {"func": f10_tier1_leverage_debt_z_5d_v113_signal},
    "f10_tier1_leverage_tier1_proxy_z_5d_v114_signal": {"func": f10_tier1_leverage_tier1_proxy_z_5d_v114_signal},
    "f10_tier1_leverage_total_leverage_z_5d_v115_signal": {"func": f10_tier1_leverage_total_leverage_z_5d_v115_signal},
    "f10_tier1_leverage_equity_z_10d_v116_signal": {"func": f10_tier1_leverage_equity_z_10d_v116_signal},
    "f10_tier1_leverage_assets_z_10d_v117_signal": {"func": f10_tier1_leverage_assets_z_10d_v117_signal},
    "f10_tier1_leverage_debt_z_10d_v118_signal": {"func": f10_tier1_leverage_debt_z_10d_v118_signal},
    "f10_tier1_leverage_tier1_proxy_z_10d_v119_signal": {"func": f10_tier1_leverage_tier1_proxy_z_10d_v119_signal},
    "f10_tier1_leverage_total_leverage_z_10d_v120_signal": {"func": f10_tier1_leverage_total_leverage_z_10d_v120_signal},
    "f10_tier1_leverage_equity_z_21d_v121_signal": {"func": f10_tier1_leverage_equity_z_21d_v121_signal},
    "f10_tier1_leverage_assets_z_21d_v122_signal": {"func": f10_tier1_leverage_assets_z_21d_v122_signal},
    "f10_tier1_leverage_debt_z_21d_v123_signal": {"func": f10_tier1_leverage_debt_z_21d_v123_signal},
    "f10_tier1_leverage_tier1_proxy_z_21d_v124_signal": {"func": f10_tier1_leverage_tier1_proxy_z_21d_v124_signal},
    "f10_tier1_leverage_total_leverage_z_21d_v125_signal": {"func": f10_tier1_leverage_total_leverage_z_21d_v125_signal},
    "f10_tier1_leverage_equity_z_42d_v126_signal": {"func": f10_tier1_leverage_equity_z_42d_v126_signal},
    "f10_tier1_leverage_assets_z_42d_v127_signal": {"func": f10_tier1_leverage_assets_z_42d_v127_signal},
    "f10_tier1_leverage_debt_z_42d_v128_signal": {"func": f10_tier1_leverage_debt_z_42d_v128_signal},
    "f10_tier1_leverage_tier1_proxy_z_42d_v129_signal": {"func": f10_tier1_leverage_tier1_proxy_z_42d_v129_signal},
    "f10_tier1_leverage_total_leverage_z_42d_v130_signal": {"func": f10_tier1_leverage_total_leverage_z_42d_v130_signal},
    "f10_tier1_leverage_equity_z_63d_v131_signal": {"func": f10_tier1_leverage_equity_z_63d_v131_signal},
    "f10_tier1_leverage_assets_z_63d_v132_signal": {"func": f10_tier1_leverage_assets_z_63d_v132_signal},
    "f10_tier1_leverage_debt_z_63d_v133_signal": {"func": f10_tier1_leverage_debt_z_63d_v133_signal},
    "f10_tier1_leverage_tier1_proxy_z_63d_v134_signal": {"func": f10_tier1_leverage_tier1_proxy_z_63d_v134_signal},
    "f10_tier1_leverage_total_leverage_z_63d_v135_signal": {"func": f10_tier1_leverage_total_leverage_z_63d_v135_signal},
    "f10_tier1_leverage_equity_z_126d_v136_signal": {"func": f10_tier1_leverage_equity_z_126d_v136_signal},
    "f10_tier1_leverage_assets_z_126d_v137_signal": {"func": f10_tier1_leverage_assets_z_126d_v137_signal},
    "f10_tier1_leverage_debt_z_126d_v138_signal": {"func": f10_tier1_leverage_debt_z_126d_v138_signal},
    "f10_tier1_leverage_tier1_proxy_z_126d_v139_signal": {"func": f10_tier1_leverage_tier1_proxy_z_126d_v139_signal},
    "f10_tier1_leverage_total_leverage_z_126d_v140_signal": {"func": f10_tier1_leverage_total_leverage_z_126d_v140_signal},
    "f10_tier1_leverage_equity_z_252d_v141_signal": {"func": f10_tier1_leverage_equity_z_252d_v141_signal},
    "f10_tier1_leverage_assets_z_252d_v142_signal": {"func": f10_tier1_leverage_assets_z_252d_v142_signal},
    "f10_tier1_leverage_debt_z_252d_v143_signal": {"func": f10_tier1_leverage_debt_z_252d_v143_signal},
    "f10_tier1_leverage_tier1_proxy_z_252d_v144_signal": {"func": f10_tier1_leverage_tier1_proxy_z_252d_v144_signal},
    "f10_tier1_leverage_total_leverage_z_252d_v145_signal": {"func": f10_tier1_leverage_total_leverage_z_252d_v145_signal},
    "f10_tier1_leverage_equity_z_504d_v146_signal": {"func": f10_tier1_leverage_equity_z_504d_v146_signal},
    "f10_tier1_leverage_assets_z_504d_v147_signal": {"func": f10_tier1_leverage_assets_z_504d_v147_signal},
    "f10_tier1_leverage_debt_z_504d_v148_signal": {"func": f10_tier1_leverage_debt_z_504d_v148_signal},
    "f10_tier1_leverage_tier1_proxy_z_504d_v149_signal": {"func": f10_tier1_leverage_tier1_proxy_z_504d_v149_signal},
    "f10_tier1_leverage_total_leverage_z_504d_v150_signal": {"func": f10_tier1_leverage_total_leverage_z_504d_v150_signal},
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
