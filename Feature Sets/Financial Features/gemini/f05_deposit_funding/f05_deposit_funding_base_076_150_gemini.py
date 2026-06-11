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

def f05_deposit_funding_deposit_density_ewma_10d_v076_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 10d window."""
    res = _ewma(_ratio(deposits, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_10d_v077_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 10d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_10d_v078_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 10d window."""
    res = _ewma(_ratio(deposits, assets - equity), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_21d_v079_signal(deposits):
    """Exponential moving average of Raw level of deposits over 21d window."""
    res = _ewma(deposits, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_21d_v080_signal(assets):
    """Exponential moving average of Raw level of assets over 21d window."""
    res = _ewma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_21d_v081_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 21d window."""
    res = _ewma(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_21d_v082_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 21d window."""
    res = _ewma(_ratio(deposits, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_21d_v083_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 21d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_21d_v084_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 21d window."""
    res = _ewma(_ratio(deposits, assets - equity), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_42d_v085_signal(deposits):
    """Exponential moving average of Raw level of deposits over 42d window."""
    res = _ewma(deposits, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_42d_v086_signal(assets):
    """Exponential moving average of Raw level of assets over 42d window."""
    res = _ewma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_42d_v087_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 42d window."""
    res = _ewma(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_42d_v088_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 42d window."""
    res = _ewma(_ratio(deposits, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_42d_v089_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 42d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_42d_v090_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 42d window."""
    res = _ewma(_ratio(deposits, assets - equity), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_63d_v091_signal(deposits):
    """Exponential moving average of Raw level of deposits over 63d window."""
    res = _ewma(deposits, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_63d_v092_signal(assets):
    """Exponential moving average of Raw level of assets over 63d window."""
    res = _ewma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_63d_v093_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 63d window."""
    res = _ewma(liabilitiesc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_63d_v094_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 63d window."""
    res = _ewma(_ratio(deposits, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_63d_v095_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 63d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_63d_v096_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 63d window."""
    res = _ewma(_ratio(deposits, assets - equity), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_126d_v097_signal(deposits):
    """Exponential moving average of Raw level of deposits over 126d window."""
    res = _ewma(deposits, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_126d_v098_signal(assets):
    """Exponential moving average of Raw level of assets over 126d window."""
    res = _ewma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_126d_v099_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 126d window."""
    res = _ewma(liabilitiesc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_126d_v100_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 126d window."""
    res = _ewma(_ratio(deposits, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_126d_v101_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 126d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_126d_v102_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 126d window."""
    res = _ewma(_ratio(deposits, assets - equity), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_252d_v103_signal(deposits):
    """Exponential moving average of Raw level of deposits over 252d window."""
    res = _ewma(deposits, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_252d_v104_signal(assets):
    """Exponential moving average of Raw level of assets over 252d window."""
    res = _ewma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_252d_v105_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 252d window."""
    res = _ewma(liabilitiesc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_252d_v106_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 252d window."""
    res = _ewma(_ratio(deposits, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_252d_v107_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 252d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_252d_v108_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 252d window."""
    res = _ewma(_ratio(deposits, assets - equity), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_504d_v109_signal(deposits):
    """Exponential moving average of Raw level of deposits over 504d window."""
    res = _ewma(deposits, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_504d_v110_signal(assets):
    """Exponential moving average of Raw level of assets over 504d window."""
    res = _ewma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_504d_v111_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 504d window."""
    res = _ewma(liabilitiesc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_504d_v112_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 504d window."""
    res = _ewma(_ratio(deposits, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_504d_v113_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 504d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_504d_v114_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 504d window."""
    res = _ewma(_ratio(deposits, assets - equity), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_756d_v115_signal(deposits):
    """Exponential moving average of Raw level of deposits over 756d window."""
    res = _ewma(deposits, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_756d_v116_signal(assets):
    """Exponential moving average of Raw level of assets over 756d window."""
    res = _ewma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_756d_v117_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 756d window."""
    res = _ewma(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_756d_v118_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 756d window."""
    res = _ewma(_ratio(deposits, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_756d_v119_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 756d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_756d_v120_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 756d window."""
    res = _ewma(_ratio(deposits, assets - equity), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_1008d_v121_signal(deposits):
    """Exponential moving average of Raw level of deposits over 1008d window."""
    res = _ewma(deposits, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_1008d_v122_signal(assets):
    """Exponential moving average of Raw level of assets over 1008d window."""
    res = _ewma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_1008d_v123_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 1008d window."""
    res = _ewma(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_1008d_v124_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 1008d window."""
    res = _ewma(_ratio(deposits, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_1008d_v125_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 1008d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_1008d_v126_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 1008d window."""
    res = _ewma(_ratio(deposits, assets - equity), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_ewma_1260d_v127_signal(deposits):
    """Exponential moving average of Raw level of deposits over 1260d window."""
    res = _ewma(deposits, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_ewma_1260d_v128_signal(assets):
    """Exponential moving average of Raw level of assets over 1260d window."""
    res = _ewma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_ewma_1260d_v129_signal(liabilitiesc):
    """Exponential moving average of Raw level of liabilitiesc over 1260d window."""
    res = _ewma(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_ewma_1260d_v130_signal(deposits, assets):
    """Exponential moving average of Deposits as % of assets over 1260d window."""
    res = _ewma(_ratio(deposits, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_ewma_1260d_v131_signal(deposits, liabilitiesc):
    """Exponential moving average of Stable deposits relative to short-term liabilities over 1260d window."""
    res = _ewma(_ratio(deposits, liabilitiesc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_ewma_1260d_v132_signal(deposits, assets, equity):
    """Exponential moving average of Deposits relative to total debt funding over 1260d window."""
    res = _ewma(_ratio(deposits, assets - equity), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_z_5d_v133_signal(deposits):
    """Z-score of Raw level of deposits over 5d window."""
    res = _z(deposits, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_z_5d_v134_signal(assets):
    """Z-score of Raw level of assets over 5d window."""
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_z_5d_v135_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 5d window."""
    res = _z(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_z_5d_v136_signal(deposits, assets):
    """Z-score of Deposits as % of assets over 5d window."""
    res = _z(_ratio(deposits, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_z_5d_v137_signal(deposits, liabilitiesc):
    """Z-score of Stable deposits relative to short-term liabilities over 5d window."""
    res = _z(_ratio(deposits, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_z_5d_v138_signal(deposits, assets, equity):
    """Z-score of Deposits relative to total debt funding over 5d window."""
    res = _z(_ratio(deposits, assets - equity), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_z_10d_v139_signal(deposits):
    """Z-score of Raw level of deposits over 10d window."""
    res = _z(deposits, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_z_10d_v140_signal(assets):
    """Z-score of Raw level of assets over 10d window."""
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_z_10d_v141_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 10d window."""
    res = _z(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_z_10d_v142_signal(deposits, assets):
    """Z-score of Deposits as % of assets over 10d window."""
    res = _z(_ratio(deposits, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_z_10d_v143_signal(deposits, liabilitiesc):
    """Z-score of Stable deposits relative to short-term liabilities over 10d window."""
    res = _z(_ratio(deposits, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_z_10d_v144_signal(deposits, assets, equity):
    """Z-score of Deposits relative to total debt funding over 10d window."""
    res = _z(_ratio(deposits, assets - equity), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposits_z_21d_v145_signal(deposits):
    """Z-score of Raw level of deposits over 21d window."""
    res = _z(deposits, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_assets_z_21d_v146_signal(assets):
    """Z-score of Raw level of assets over 21d window."""
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_liabilitiesc_z_21d_v147_signal(liabilitiesc):
    """Z-score of Raw level of liabilitiesc over 21d window."""
    res = _z(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_deposit_density_z_21d_v148_signal(deposits, assets):
    """Z-score of Deposits as % of assets over 21d window."""
    res = _z(_ratio(deposits, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_funding_quality_z_21d_v149_signal(deposits, liabilitiesc):
    """Z-score of Stable deposits relative to short-term liabilities over 21d window."""
    res = _z(_ratio(deposits, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_deposit_funding_asset_funding_mix_z_21d_v150_signal(deposits, assets, equity):
    """Z-score of Deposits relative to total debt funding over 21d window."""
    res = _z(_ratio(deposits, assets - equity), 21)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f05_deposit_funding_deposit_density_ewma_10d_v076_signal": {"func": f05_deposit_funding_deposit_density_ewma_10d_v076_signal},
    "f05_deposit_funding_funding_quality_ewma_10d_v077_signal": {"func": f05_deposit_funding_funding_quality_ewma_10d_v077_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_10d_v078_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_10d_v078_signal},
    "f05_deposit_funding_deposits_ewma_21d_v079_signal": {"func": f05_deposit_funding_deposits_ewma_21d_v079_signal},
    "f05_deposit_funding_assets_ewma_21d_v080_signal": {"func": f05_deposit_funding_assets_ewma_21d_v080_signal},
    "f05_deposit_funding_liabilitiesc_ewma_21d_v081_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_21d_v081_signal},
    "f05_deposit_funding_deposit_density_ewma_21d_v082_signal": {"func": f05_deposit_funding_deposit_density_ewma_21d_v082_signal},
    "f05_deposit_funding_funding_quality_ewma_21d_v083_signal": {"func": f05_deposit_funding_funding_quality_ewma_21d_v083_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_21d_v084_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_21d_v084_signal},
    "f05_deposit_funding_deposits_ewma_42d_v085_signal": {"func": f05_deposit_funding_deposits_ewma_42d_v085_signal},
    "f05_deposit_funding_assets_ewma_42d_v086_signal": {"func": f05_deposit_funding_assets_ewma_42d_v086_signal},
    "f05_deposit_funding_liabilitiesc_ewma_42d_v087_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_42d_v087_signal},
    "f05_deposit_funding_deposit_density_ewma_42d_v088_signal": {"func": f05_deposit_funding_deposit_density_ewma_42d_v088_signal},
    "f05_deposit_funding_funding_quality_ewma_42d_v089_signal": {"func": f05_deposit_funding_funding_quality_ewma_42d_v089_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_42d_v090_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_42d_v090_signal},
    "f05_deposit_funding_deposits_ewma_63d_v091_signal": {"func": f05_deposit_funding_deposits_ewma_63d_v091_signal},
    "f05_deposit_funding_assets_ewma_63d_v092_signal": {"func": f05_deposit_funding_assets_ewma_63d_v092_signal},
    "f05_deposit_funding_liabilitiesc_ewma_63d_v093_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_63d_v093_signal},
    "f05_deposit_funding_deposit_density_ewma_63d_v094_signal": {"func": f05_deposit_funding_deposit_density_ewma_63d_v094_signal},
    "f05_deposit_funding_funding_quality_ewma_63d_v095_signal": {"func": f05_deposit_funding_funding_quality_ewma_63d_v095_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_63d_v096_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_63d_v096_signal},
    "f05_deposit_funding_deposits_ewma_126d_v097_signal": {"func": f05_deposit_funding_deposits_ewma_126d_v097_signal},
    "f05_deposit_funding_assets_ewma_126d_v098_signal": {"func": f05_deposit_funding_assets_ewma_126d_v098_signal},
    "f05_deposit_funding_liabilitiesc_ewma_126d_v099_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_126d_v099_signal},
    "f05_deposit_funding_deposit_density_ewma_126d_v100_signal": {"func": f05_deposit_funding_deposit_density_ewma_126d_v100_signal},
    "f05_deposit_funding_funding_quality_ewma_126d_v101_signal": {"func": f05_deposit_funding_funding_quality_ewma_126d_v101_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_126d_v102_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_126d_v102_signal},
    "f05_deposit_funding_deposits_ewma_252d_v103_signal": {"func": f05_deposit_funding_deposits_ewma_252d_v103_signal},
    "f05_deposit_funding_assets_ewma_252d_v104_signal": {"func": f05_deposit_funding_assets_ewma_252d_v104_signal},
    "f05_deposit_funding_liabilitiesc_ewma_252d_v105_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_252d_v105_signal},
    "f05_deposit_funding_deposit_density_ewma_252d_v106_signal": {"func": f05_deposit_funding_deposit_density_ewma_252d_v106_signal},
    "f05_deposit_funding_funding_quality_ewma_252d_v107_signal": {"func": f05_deposit_funding_funding_quality_ewma_252d_v107_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_252d_v108_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_252d_v108_signal},
    "f05_deposit_funding_deposits_ewma_504d_v109_signal": {"func": f05_deposit_funding_deposits_ewma_504d_v109_signal},
    "f05_deposit_funding_assets_ewma_504d_v110_signal": {"func": f05_deposit_funding_assets_ewma_504d_v110_signal},
    "f05_deposit_funding_liabilitiesc_ewma_504d_v111_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_504d_v111_signal},
    "f05_deposit_funding_deposit_density_ewma_504d_v112_signal": {"func": f05_deposit_funding_deposit_density_ewma_504d_v112_signal},
    "f05_deposit_funding_funding_quality_ewma_504d_v113_signal": {"func": f05_deposit_funding_funding_quality_ewma_504d_v113_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_504d_v114_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_504d_v114_signal},
    "f05_deposit_funding_deposits_ewma_756d_v115_signal": {"func": f05_deposit_funding_deposits_ewma_756d_v115_signal},
    "f05_deposit_funding_assets_ewma_756d_v116_signal": {"func": f05_deposit_funding_assets_ewma_756d_v116_signal},
    "f05_deposit_funding_liabilitiesc_ewma_756d_v117_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_756d_v117_signal},
    "f05_deposit_funding_deposit_density_ewma_756d_v118_signal": {"func": f05_deposit_funding_deposit_density_ewma_756d_v118_signal},
    "f05_deposit_funding_funding_quality_ewma_756d_v119_signal": {"func": f05_deposit_funding_funding_quality_ewma_756d_v119_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_756d_v120_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_756d_v120_signal},
    "f05_deposit_funding_deposits_ewma_1008d_v121_signal": {"func": f05_deposit_funding_deposits_ewma_1008d_v121_signal},
    "f05_deposit_funding_assets_ewma_1008d_v122_signal": {"func": f05_deposit_funding_assets_ewma_1008d_v122_signal},
    "f05_deposit_funding_liabilitiesc_ewma_1008d_v123_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_1008d_v123_signal},
    "f05_deposit_funding_deposit_density_ewma_1008d_v124_signal": {"func": f05_deposit_funding_deposit_density_ewma_1008d_v124_signal},
    "f05_deposit_funding_funding_quality_ewma_1008d_v125_signal": {"func": f05_deposit_funding_funding_quality_ewma_1008d_v125_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_1008d_v126_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_1008d_v126_signal},
    "f05_deposit_funding_deposits_ewma_1260d_v127_signal": {"func": f05_deposit_funding_deposits_ewma_1260d_v127_signal},
    "f05_deposit_funding_assets_ewma_1260d_v128_signal": {"func": f05_deposit_funding_assets_ewma_1260d_v128_signal},
    "f05_deposit_funding_liabilitiesc_ewma_1260d_v129_signal": {"func": f05_deposit_funding_liabilitiesc_ewma_1260d_v129_signal},
    "f05_deposit_funding_deposit_density_ewma_1260d_v130_signal": {"func": f05_deposit_funding_deposit_density_ewma_1260d_v130_signal},
    "f05_deposit_funding_funding_quality_ewma_1260d_v131_signal": {"func": f05_deposit_funding_funding_quality_ewma_1260d_v131_signal},
    "f05_deposit_funding_asset_funding_mix_ewma_1260d_v132_signal": {"func": f05_deposit_funding_asset_funding_mix_ewma_1260d_v132_signal},
    "f05_deposit_funding_deposits_z_5d_v133_signal": {"func": f05_deposit_funding_deposits_z_5d_v133_signal},
    "f05_deposit_funding_assets_z_5d_v134_signal": {"func": f05_deposit_funding_assets_z_5d_v134_signal},
    "f05_deposit_funding_liabilitiesc_z_5d_v135_signal": {"func": f05_deposit_funding_liabilitiesc_z_5d_v135_signal},
    "f05_deposit_funding_deposit_density_z_5d_v136_signal": {"func": f05_deposit_funding_deposit_density_z_5d_v136_signal},
    "f05_deposit_funding_funding_quality_z_5d_v137_signal": {"func": f05_deposit_funding_funding_quality_z_5d_v137_signal},
    "f05_deposit_funding_asset_funding_mix_z_5d_v138_signal": {"func": f05_deposit_funding_asset_funding_mix_z_5d_v138_signal},
    "f05_deposit_funding_deposits_z_10d_v139_signal": {"func": f05_deposit_funding_deposits_z_10d_v139_signal},
    "f05_deposit_funding_assets_z_10d_v140_signal": {"func": f05_deposit_funding_assets_z_10d_v140_signal},
    "f05_deposit_funding_liabilitiesc_z_10d_v141_signal": {"func": f05_deposit_funding_liabilitiesc_z_10d_v141_signal},
    "f05_deposit_funding_deposit_density_z_10d_v142_signal": {"func": f05_deposit_funding_deposit_density_z_10d_v142_signal},
    "f05_deposit_funding_funding_quality_z_10d_v143_signal": {"func": f05_deposit_funding_funding_quality_z_10d_v143_signal},
    "f05_deposit_funding_asset_funding_mix_z_10d_v144_signal": {"func": f05_deposit_funding_asset_funding_mix_z_10d_v144_signal},
    "f05_deposit_funding_deposits_z_21d_v145_signal": {"func": f05_deposit_funding_deposits_z_21d_v145_signal},
    "f05_deposit_funding_assets_z_21d_v146_signal": {"func": f05_deposit_funding_assets_z_21d_v146_signal},
    "f05_deposit_funding_liabilitiesc_z_21d_v147_signal": {"func": f05_deposit_funding_liabilitiesc_z_21d_v147_signal},
    "f05_deposit_funding_deposit_density_z_21d_v148_signal": {"func": f05_deposit_funding_deposit_density_z_21d_v148_signal},
    "f05_deposit_funding_funding_quality_z_21d_v149_signal": {"func": f05_deposit_funding_funding_quality_z_21d_v149_signal},
    "f05_deposit_funding_asset_funding_mix_z_21d_v150_signal": {"func": f05_deposit_funding_asset_funding_mix_z_21d_v150_signal},
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
