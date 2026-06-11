import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
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

def f01_unit_economics_revenue_z_63d_v076_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_z_63d_v077_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 63d window."""
    res = _z(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_z_63d_v078_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 63d window."""
    res = _z(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_z_63d_v079_signal(revenue, capex):
    """Z-score for relative outlier detection of Revenue per unit of capital expenditure over 63d window."""
    res = _z(_ratio(revenue, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_z_63d_v080_signal(revenue, capex, assets):
    """Z-score for relative outlier detection of Net unit productivity relative to assets over 63d window."""
    res = _z(_ratio(revenue - capex, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_z_126d_v081_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_z_126d_v082_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 126d window."""
    res = _z(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_z_126d_v083_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 126d window."""
    res = _z(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_z_126d_v084_signal(revenue, capex):
    """Z-score for relative outlier detection of Revenue per unit of capital expenditure over 126d window."""
    res = _z(_ratio(revenue, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_z_126d_v085_signal(revenue, capex, assets):
    """Z-score for relative outlier detection of Net unit productivity relative to assets over 126d window."""
    res = _z(_ratio(revenue - capex, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_z_252d_v086_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_z_252d_v087_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 252d window."""
    res = _z(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_z_252d_v088_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 252d window."""
    res = _z(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_z_252d_v089_signal(revenue, capex):
    """Z-score for relative outlier detection of Revenue per unit of capital expenditure over 252d window."""
    res = _z(_ratio(revenue, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_z_252d_v090_signal(revenue, capex, assets):
    """Z-score for relative outlier detection of Net unit productivity relative to assets over 252d window."""
    res = _z(_ratio(revenue - capex, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_z_504d_v091_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_z_504d_v092_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 504d window."""
    res = _z(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_z_504d_v093_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 504d window."""
    res = _z(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_z_504d_v094_signal(revenue, capex):
    """Z-score for relative outlier detection of Revenue per unit of capital expenditure over 504d window."""
    res = _z(_ratio(revenue, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_z_504d_v095_signal(revenue, capex, assets):
    """Z-score for relative outlier detection of Net unit productivity relative to assets over 504d window."""
    res = _z(_ratio(revenue - capex, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_z_756d_v096_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_z_756d_v097_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 756d window."""
    res = _z(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_z_756d_v098_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 756d window."""
    res = _z(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_z_756d_v099_signal(revenue, capex):
    """Z-score for relative outlier detection of Revenue per unit of capital expenditure over 756d window."""
    res = _z(_ratio(revenue, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_z_756d_v100_signal(revenue, capex, assets):
    """Z-score for relative outlier detection of Net unit productivity relative to assets over 756d window."""
    res = _z(_ratio(revenue - capex, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_z_1008d_v101_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_z_1008d_v102_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 1008d window."""
    res = _z(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_z_1008d_v103_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 1008d window."""
    res = _z(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_z_1008d_v104_signal(revenue, capex):
    """Z-score for relative outlier detection of Revenue per unit of capital expenditure over 1008d window."""
    res = _z(_ratio(revenue, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_z_1008d_v105_signal(revenue, capex, assets):
    """Z-score for relative outlier detection of Net unit productivity relative to assets over 1008d window."""
    res = _z(_ratio(revenue - capex, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_z_1260d_v106_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_z_1260d_v107_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 1260d window."""
    res = _z(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_z_1260d_v108_signal(assets):
    """Z-score for relative outlier detection of Raw level of assets over 1260d window."""
    res = _z(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_z_1260d_v109_signal(revenue, capex):
    """Z-score for relative outlier detection of Revenue per unit of capital expenditure over 1260d window."""
    res = _z(_ratio(revenue, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_z_1260d_v110_signal(revenue, capex, assets):
    """Z-score for relative outlier detection of Net unit productivity relative to assets over 1260d window."""
    res = _z(_ratio(revenue - capex, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_dd_5d_v111_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_dd_5d_v112_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 5d window."""
    res = _drawdown(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_dd_5d_v113_signal(assets):
    """Drawdown from peak to identify cycle troughs of Raw level of assets over 5d window."""
    res = _drawdown(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_dd_5d_v114_signal(revenue, capex):
    """Drawdown from peak to identify cycle troughs of Revenue per unit of capital expenditure over 5d window."""
    res = _drawdown(_ratio(revenue, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_dd_5d_v115_signal(revenue, capex, assets):
    """Drawdown from peak to identify cycle troughs of Net unit productivity relative to assets over 5d window."""
    res = _drawdown(_ratio(revenue - capex, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_dd_10d_v116_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_dd_10d_v117_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 10d window."""
    res = _drawdown(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_dd_10d_v118_signal(assets):
    """Drawdown from peak to identify cycle troughs of Raw level of assets over 10d window."""
    res = _drawdown(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_dd_10d_v119_signal(revenue, capex):
    """Drawdown from peak to identify cycle troughs of Revenue per unit of capital expenditure over 10d window."""
    res = _drawdown(_ratio(revenue, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_dd_10d_v120_signal(revenue, capex, assets):
    """Drawdown from peak to identify cycle troughs of Net unit productivity relative to assets over 10d window."""
    res = _drawdown(_ratio(revenue - capex, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_dd_21d_v121_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_dd_21d_v122_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 21d window."""
    res = _drawdown(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_dd_21d_v123_signal(assets):
    """Drawdown from peak to identify cycle troughs of Raw level of assets over 21d window."""
    res = _drawdown(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_dd_21d_v124_signal(revenue, capex):
    """Drawdown from peak to identify cycle troughs of Revenue per unit of capital expenditure over 21d window."""
    res = _drawdown(_ratio(revenue, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_dd_21d_v125_signal(revenue, capex, assets):
    """Drawdown from peak to identify cycle troughs of Net unit productivity relative to assets over 21d window."""
    res = _drawdown(_ratio(revenue - capex, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_dd_42d_v126_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_dd_42d_v127_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 42d window."""
    res = _drawdown(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_dd_42d_v128_signal(assets):
    """Drawdown from peak to identify cycle troughs of Raw level of assets over 42d window."""
    res = _drawdown(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_dd_42d_v129_signal(revenue, capex):
    """Drawdown from peak to identify cycle troughs of Revenue per unit of capital expenditure over 42d window."""
    res = _drawdown(_ratio(revenue, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_dd_42d_v130_signal(revenue, capex, assets):
    """Drawdown from peak to identify cycle troughs of Net unit productivity relative to assets over 42d window."""
    res = _drawdown(_ratio(revenue - capex, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_dd_63d_v131_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_dd_63d_v132_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 63d window."""
    res = _drawdown(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_dd_63d_v133_signal(assets):
    """Drawdown from peak to identify cycle troughs of Raw level of assets over 63d window."""
    res = _drawdown(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_dd_63d_v134_signal(revenue, capex):
    """Drawdown from peak to identify cycle troughs of Revenue per unit of capital expenditure over 63d window."""
    res = _drawdown(_ratio(revenue, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_dd_63d_v135_signal(revenue, capex, assets):
    """Drawdown from peak to identify cycle troughs of Net unit productivity relative to assets over 63d window."""
    res = _drawdown(_ratio(revenue - capex, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_dd_126d_v136_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 126d window."""
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_dd_126d_v137_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 126d window."""
    res = _drawdown(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_dd_126d_v138_signal(assets):
    """Drawdown from peak to identify cycle troughs of Raw level of assets over 126d window."""
    res = _drawdown(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_dd_126d_v139_signal(revenue, capex):
    """Drawdown from peak to identify cycle troughs of Revenue per unit of capital expenditure over 126d window."""
    res = _drawdown(_ratio(revenue, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_dd_126d_v140_signal(revenue, capex, assets):
    """Drawdown from peak to identify cycle troughs of Net unit productivity relative to assets over 126d window."""
    res = _drawdown(_ratio(revenue - capex, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_dd_252d_v141_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 252d window."""
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_dd_252d_v142_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 252d window."""
    res = _drawdown(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_dd_252d_v143_signal(assets):
    """Drawdown from peak to identify cycle troughs of Raw level of assets over 252d window."""
    res = _drawdown(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_dd_252d_v144_signal(revenue, capex):
    """Drawdown from peak to identify cycle troughs of Revenue per unit of capital expenditure over 252d window."""
    res = _drawdown(_ratio(revenue, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_dd_252d_v145_signal(revenue, capex, assets):
    """Drawdown from peak to identify cycle troughs of Net unit productivity relative to assets over 252d window."""
    res = _drawdown(_ratio(revenue - capex, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_revenue_dd_504d_v146_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 504d window."""
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_capex_dd_504d_v147_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 504d window."""
    res = _drawdown(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_assets_dd_504d_v148_signal(assets):
    """Drawdown from peak to identify cycle troughs of Raw level of assets over 504d window."""
    res = _drawdown(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_rev_per_capex_dd_504d_v149_signal(revenue, capex):
    """Drawdown from peak to identify cycle troughs of Revenue per unit of capital expenditure over 504d window."""
    res = _drawdown(_ratio(revenue, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f01_unit_economics_asset_efficiency_dd_504d_v150_signal(revenue, capex, assets):
    """Drawdown from peak to identify cycle troughs of Net unit productivity relative to assets over 504d window."""
    res = _drawdown(_ratio(revenue - capex, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f01_unit_economics_revenue_z_63d_v076_signal": {"inputs": [], "func": f01_unit_economics_revenue_z_63d_v076_signal},    "f01_unit_economics_capex_z_63d_v077_signal": {"inputs": [], "func": f01_unit_economics_capex_z_63d_v077_signal},    "f01_unit_economics_assets_z_63d_v078_signal": {"inputs": [], "func": f01_unit_economics_assets_z_63d_v078_signal},    "f01_unit_economics_rev_per_capex_z_63d_v079_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_z_63d_v079_signal},    "f01_unit_economics_asset_efficiency_z_63d_v080_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_z_63d_v080_signal},    "f01_unit_economics_revenue_z_126d_v081_signal": {"inputs": [], "func": f01_unit_economics_revenue_z_126d_v081_signal},    "f01_unit_economics_capex_z_126d_v082_signal": {"inputs": [], "func": f01_unit_economics_capex_z_126d_v082_signal},    "f01_unit_economics_assets_z_126d_v083_signal": {"inputs": [], "func": f01_unit_economics_assets_z_126d_v083_signal},    "f01_unit_economics_rev_per_capex_z_126d_v084_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_z_126d_v084_signal},    "f01_unit_economics_asset_efficiency_z_126d_v085_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_z_126d_v085_signal},    "f01_unit_economics_revenue_z_252d_v086_signal": {"inputs": [], "func": f01_unit_economics_revenue_z_252d_v086_signal},    "f01_unit_economics_capex_z_252d_v087_signal": {"inputs": [], "func": f01_unit_economics_capex_z_252d_v087_signal},    "f01_unit_economics_assets_z_252d_v088_signal": {"inputs": [], "func": f01_unit_economics_assets_z_252d_v088_signal},    "f01_unit_economics_rev_per_capex_z_252d_v089_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_z_252d_v089_signal},    "f01_unit_economics_asset_efficiency_z_252d_v090_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_z_252d_v090_signal},    "f01_unit_economics_revenue_z_504d_v091_signal": {"inputs": [], "func": f01_unit_economics_revenue_z_504d_v091_signal},    "f01_unit_economics_capex_z_504d_v092_signal": {"inputs": [], "func": f01_unit_economics_capex_z_504d_v092_signal},    "f01_unit_economics_assets_z_504d_v093_signal": {"inputs": [], "func": f01_unit_economics_assets_z_504d_v093_signal},    "f01_unit_economics_rev_per_capex_z_504d_v094_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_z_504d_v094_signal},    "f01_unit_economics_asset_efficiency_z_504d_v095_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_z_504d_v095_signal},    "f01_unit_economics_revenue_z_756d_v096_signal": {"inputs": [], "func": f01_unit_economics_revenue_z_756d_v096_signal},    "f01_unit_economics_capex_z_756d_v097_signal": {"inputs": [], "func": f01_unit_economics_capex_z_756d_v097_signal},    "f01_unit_economics_assets_z_756d_v098_signal": {"inputs": [], "func": f01_unit_economics_assets_z_756d_v098_signal},    "f01_unit_economics_rev_per_capex_z_756d_v099_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_z_756d_v099_signal},    "f01_unit_economics_asset_efficiency_z_756d_v100_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_z_756d_v100_signal},    "f01_unit_economics_revenue_z_1008d_v101_signal": {"inputs": [], "func": f01_unit_economics_revenue_z_1008d_v101_signal},    "f01_unit_economics_capex_z_1008d_v102_signal": {"inputs": [], "func": f01_unit_economics_capex_z_1008d_v102_signal},    "f01_unit_economics_assets_z_1008d_v103_signal": {"inputs": [], "func": f01_unit_economics_assets_z_1008d_v103_signal},    "f01_unit_economics_rev_per_capex_z_1008d_v104_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_z_1008d_v104_signal},    "f01_unit_economics_asset_efficiency_z_1008d_v105_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_z_1008d_v105_signal},    "f01_unit_economics_revenue_z_1260d_v106_signal": {"inputs": [], "func": f01_unit_economics_revenue_z_1260d_v106_signal},    "f01_unit_economics_capex_z_1260d_v107_signal": {"inputs": [], "func": f01_unit_economics_capex_z_1260d_v107_signal},    "f01_unit_economics_assets_z_1260d_v108_signal": {"inputs": [], "func": f01_unit_economics_assets_z_1260d_v108_signal},    "f01_unit_economics_rev_per_capex_z_1260d_v109_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_z_1260d_v109_signal},    "f01_unit_economics_asset_efficiency_z_1260d_v110_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_z_1260d_v110_signal},    "f01_unit_economics_revenue_dd_5d_v111_signal": {"inputs": [], "func": f01_unit_economics_revenue_dd_5d_v111_signal},    "f01_unit_economics_capex_dd_5d_v112_signal": {"inputs": [], "func": f01_unit_economics_capex_dd_5d_v112_signal},    "f01_unit_economics_assets_dd_5d_v113_signal": {"inputs": [], "func": f01_unit_economics_assets_dd_5d_v113_signal},    "f01_unit_economics_rev_per_capex_dd_5d_v114_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_dd_5d_v114_signal},    "f01_unit_economics_asset_efficiency_dd_5d_v115_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_dd_5d_v115_signal},    "f01_unit_economics_revenue_dd_10d_v116_signal": {"inputs": [], "func": f01_unit_economics_revenue_dd_10d_v116_signal},    "f01_unit_economics_capex_dd_10d_v117_signal": {"inputs": [], "func": f01_unit_economics_capex_dd_10d_v117_signal},    "f01_unit_economics_assets_dd_10d_v118_signal": {"inputs": [], "func": f01_unit_economics_assets_dd_10d_v118_signal},    "f01_unit_economics_rev_per_capex_dd_10d_v119_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_dd_10d_v119_signal},    "f01_unit_economics_asset_efficiency_dd_10d_v120_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_dd_10d_v120_signal},    "f01_unit_economics_revenue_dd_21d_v121_signal": {"inputs": [], "func": f01_unit_economics_revenue_dd_21d_v121_signal},    "f01_unit_economics_capex_dd_21d_v122_signal": {"inputs": [], "func": f01_unit_economics_capex_dd_21d_v122_signal},    "f01_unit_economics_assets_dd_21d_v123_signal": {"inputs": [], "func": f01_unit_economics_assets_dd_21d_v123_signal},    "f01_unit_economics_rev_per_capex_dd_21d_v124_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_dd_21d_v124_signal},    "f01_unit_economics_asset_efficiency_dd_21d_v125_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_dd_21d_v125_signal},    "f01_unit_economics_revenue_dd_42d_v126_signal": {"inputs": [], "func": f01_unit_economics_revenue_dd_42d_v126_signal},    "f01_unit_economics_capex_dd_42d_v127_signal": {"inputs": [], "func": f01_unit_economics_capex_dd_42d_v127_signal},    "f01_unit_economics_assets_dd_42d_v128_signal": {"inputs": [], "func": f01_unit_economics_assets_dd_42d_v128_signal},    "f01_unit_economics_rev_per_capex_dd_42d_v129_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_dd_42d_v129_signal},    "f01_unit_economics_asset_efficiency_dd_42d_v130_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_dd_42d_v130_signal},    "f01_unit_economics_revenue_dd_63d_v131_signal": {"inputs": [], "func": f01_unit_economics_revenue_dd_63d_v131_signal},    "f01_unit_economics_capex_dd_63d_v132_signal": {"inputs": [], "func": f01_unit_economics_capex_dd_63d_v132_signal},    "f01_unit_economics_assets_dd_63d_v133_signal": {"inputs": [], "func": f01_unit_economics_assets_dd_63d_v133_signal},    "f01_unit_economics_rev_per_capex_dd_63d_v134_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_dd_63d_v134_signal},    "f01_unit_economics_asset_efficiency_dd_63d_v135_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_dd_63d_v135_signal},    "f01_unit_economics_revenue_dd_126d_v136_signal": {"inputs": [], "func": f01_unit_economics_revenue_dd_126d_v136_signal},    "f01_unit_economics_capex_dd_126d_v137_signal": {"inputs": [], "func": f01_unit_economics_capex_dd_126d_v137_signal},    "f01_unit_economics_assets_dd_126d_v138_signal": {"inputs": [], "func": f01_unit_economics_assets_dd_126d_v138_signal},    "f01_unit_economics_rev_per_capex_dd_126d_v139_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_dd_126d_v139_signal},    "f01_unit_economics_asset_efficiency_dd_126d_v140_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_dd_126d_v140_signal},    "f01_unit_economics_revenue_dd_252d_v141_signal": {"inputs": [], "func": f01_unit_economics_revenue_dd_252d_v141_signal},    "f01_unit_economics_capex_dd_252d_v142_signal": {"inputs": [], "func": f01_unit_economics_capex_dd_252d_v142_signal},    "f01_unit_economics_assets_dd_252d_v143_signal": {"inputs": [], "func": f01_unit_economics_assets_dd_252d_v143_signal},    "f01_unit_economics_rev_per_capex_dd_252d_v144_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_dd_252d_v144_signal},    "f01_unit_economics_asset_efficiency_dd_252d_v145_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_dd_252d_v145_signal},    "f01_unit_economics_revenue_dd_504d_v146_signal": {"inputs": [], "func": f01_unit_economics_revenue_dd_504d_v146_signal},    "f01_unit_economics_capex_dd_504d_v147_signal": {"inputs": [], "func": f01_unit_economics_capex_dd_504d_v147_signal},    "f01_unit_economics_assets_dd_504d_v148_signal": {"inputs": [], "func": f01_unit_economics_assets_dd_504d_v148_signal},    "f01_unit_economics_rev_per_capex_dd_504d_v149_signal": {"inputs": [], "func": f01_unit_economics_rev_per_capex_dd_504d_v149_signal},    "f01_unit_economics_asset_efficiency_dd_504d_v150_signal": {"inputs": [], "func": f01_unit_economics_asset_efficiency_dd_504d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
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
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
