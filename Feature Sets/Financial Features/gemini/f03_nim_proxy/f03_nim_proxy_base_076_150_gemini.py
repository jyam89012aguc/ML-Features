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

def f03_nim_proxy_roa_net_ewma_10d_v076_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 10d window."""
    res = _ewma(_ratio(netinc, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_10d_v077_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 10d window."""
    res = _ewma(_ratio(ebt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_10d_v078_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 10d window."""
    res = _ewma(_ratio(netinc, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_21d_v079_signal(netinc):
    """Exponential moving average of Raw level of netinc over 21d window."""
    res = _ewma(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_21d_v080_signal(assets):
    """Exponential moving average of Raw level of assets over 21d window."""
    res = _ewma(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_21d_v081_signal(ebt):
    """Exponential moving average of Raw level of ebt over 21d window."""
    res = _ewma(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_21d_v082_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 21d window."""
    res = _ewma(_ratio(netinc, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_21d_v083_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 21d window."""
    res = _ewma(_ratio(ebt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_21d_v084_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 21d window."""
    res = _ewma(_ratio(netinc, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_42d_v085_signal(netinc):
    """Exponential moving average of Raw level of netinc over 42d window."""
    res = _ewma(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_42d_v086_signal(assets):
    """Exponential moving average of Raw level of assets over 42d window."""
    res = _ewma(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_42d_v087_signal(ebt):
    """Exponential moving average of Raw level of ebt over 42d window."""
    res = _ewma(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_42d_v088_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 42d window."""
    res = _ewma(_ratio(netinc, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_42d_v089_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 42d window."""
    res = _ewma(_ratio(ebt, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_42d_v090_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 42d window."""
    res = _ewma(_ratio(netinc, ebt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_63d_v091_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_63d_v092_signal(assets):
    """Exponential moving average of Raw level of assets over 63d window."""
    res = _ewma(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_63d_v093_signal(ebt):
    """Exponential moving average of Raw level of ebt over 63d window."""
    res = _ewma(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_63d_v094_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 63d window."""
    res = _ewma(_ratio(netinc, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_63d_v095_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 63d window."""
    res = _ewma(_ratio(ebt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_63d_v096_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 63d window."""
    res = _ewma(_ratio(netinc, ebt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_126d_v097_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_126d_v098_signal(assets):
    """Exponential moving average of Raw level of assets over 126d window."""
    res = _ewma(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_126d_v099_signal(ebt):
    """Exponential moving average of Raw level of ebt over 126d window."""
    res = _ewma(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_126d_v100_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 126d window."""
    res = _ewma(_ratio(netinc, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_126d_v101_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 126d window."""
    res = _ewma(_ratio(ebt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_126d_v102_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 126d window."""
    res = _ewma(_ratio(netinc, ebt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_252d_v103_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_252d_v104_signal(assets):
    """Exponential moving average of Raw level of assets over 252d window."""
    res = _ewma(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_252d_v105_signal(ebt):
    """Exponential moving average of Raw level of ebt over 252d window."""
    res = _ewma(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_252d_v106_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 252d window."""
    res = _ewma(_ratio(netinc, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_252d_v107_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 252d window."""
    res = _ewma(_ratio(ebt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_252d_v108_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 252d window."""
    res = _ewma(_ratio(netinc, ebt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_504d_v109_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_504d_v110_signal(assets):
    """Exponential moving average of Raw level of assets over 504d window."""
    res = _ewma(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_504d_v111_signal(ebt):
    """Exponential moving average of Raw level of ebt over 504d window."""
    res = _ewma(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_504d_v112_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 504d window."""
    res = _ewma(_ratio(netinc, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_504d_v113_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 504d window."""
    res = _ewma(_ratio(ebt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_504d_v114_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 504d window."""
    res = _ewma(_ratio(netinc, ebt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_756d_v115_signal(netinc):
    """Exponential moving average of Raw level of netinc over 756d window."""
    res = _ewma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_756d_v116_signal(assets):
    """Exponential moving average of Raw level of assets over 756d window."""
    res = _ewma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_756d_v117_signal(ebt):
    """Exponential moving average of Raw level of ebt over 756d window."""
    res = _ewma(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_756d_v118_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 756d window."""
    res = _ewma(_ratio(netinc, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_756d_v119_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 756d window."""
    res = _ewma(_ratio(ebt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_756d_v120_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 756d window."""
    res = _ewma(_ratio(netinc, ebt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_1008d_v121_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1008d window."""
    res = _ewma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_1008d_v122_signal(assets):
    """Exponential moving average of Raw level of assets over 1008d window."""
    res = _ewma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_1008d_v123_signal(ebt):
    """Exponential moving average of Raw level of ebt over 1008d window."""
    res = _ewma(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_1008d_v124_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 1008d window."""
    res = _ewma(_ratio(netinc, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_1008d_v125_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 1008d window."""
    res = _ewma(_ratio(ebt, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_1008d_v126_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 1008d window."""
    res = _ewma(_ratio(netinc, ebt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_ewma_1260d_v127_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1260d window."""
    res = _ewma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_ewma_1260d_v128_signal(assets):
    """Exponential moving average of Raw level of assets over 1260d window."""
    res = _ewma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_ewma_1260d_v129_signal(ebt):
    """Exponential moving average of Raw level of ebt over 1260d window."""
    res = _ewma(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_ewma_1260d_v130_signal(netinc, assets):
    """Exponential moving average of Net return on assets over 1260d window."""
    res = _ewma(_ratio(netinc, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_ewma_1260d_v131_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 1260d window."""
    res = _ewma(_ratio(ebt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_ewma_1260d_v132_signal(netinc, ebt):
    """Exponential moving average of Tax efficiency proxy over 1260d window."""
    res = _ewma(_ratio(netinc, ebt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_z_5d_v133_signal(netinc):
    """Z-score of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_z_5d_v134_signal(assets):
    """Z-score of Raw level of assets over 5d window."""
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_z_5d_v135_signal(ebt):
    """Z-score of Raw level of ebt over 5d window."""
    res = _z(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_z_5d_v136_signal(netinc, assets):
    """Z-score of Net return on assets over 5d window."""
    res = _z(_ratio(netinc, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_z_5d_v137_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 5d window."""
    res = _z(_ratio(ebt, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_z_5d_v138_signal(netinc, ebt):
    """Z-score of Tax efficiency proxy over 5d window."""
    res = _z(_ratio(netinc, ebt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_z_10d_v139_signal(netinc):
    """Z-score of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_z_10d_v140_signal(assets):
    """Z-score of Raw level of assets over 10d window."""
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_z_10d_v141_signal(ebt):
    """Z-score of Raw level of ebt over 10d window."""
    res = _z(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_z_10d_v142_signal(netinc, assets):
    """Z-score of Net return on assets over 10d window."""
    res = _z(_ratio(netinc, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_z_10d_v143_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 10d window."""
    res = _z(_ratio(ebt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_z_10d_v144_signal(netinc, ebt):
    """Z-score of Tax efficiency proxy over 10d window."""
    res = _z(_ratio(netinc, ebt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_netinc_z_21d_v145_signal(netinc):
    """Z-score of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_assets_z_21d_v146_signal(assets):
    """Z-score of Raw level of assets over 21d window."""
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_ebt_z_21d_v147_signal(ebt):
    """Z-score of Raw level of ebt over 21d window."""
    res = _z(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_net_z_21d_v148_signal(netinc, assets):
    """Z-score of Net return on assets over 21d window."""
    res = _z(_ratio(netinc, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_roa_pretax_z_21d_v149_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 21d window."""
    res = _z(_ratio(ebt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f03_nim_proxy_tax_shield_z_21d_v150_signal(netinc, ebt):
    """Z-score of Tax efficiency proxy over 21d window."""
    res = _z(_ratio(netinc, ebt), 21)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f03_nim_proxy_roa_net_ewma_10d_v076_signal": {"func": f03_nim_proxy_roa_net_ewma_10d_v076_signal},
    "f03_nim_proxy_roa_pretax_ewma_10d_v077_signal": {"func": f03_nim_proxy_roa_pretax_ewma_10d_v077_signal},
    "f03_nim_proxy_tax_shield_ewma_10d_v078_signal": {"func": f03_nim_proxy_tax_shield_ewma_10d_v078_signal},
    "f03_nim_proxy_netinc_ewma_21d_v079_signal": {"func": f03_nim_proxy_netinc_ewma_21d_v079_signal},
    "f03_nim_proxy_assets_ewma_21d_v080_signal": {"func": f03_nim_proxy_assets_ewma_21d_v080_signal},
    "f03_nim_proxy_ebt_ewma_21d_v081_signal": {"func": f03_nim_proxy_ebt_ewma_21d_v081_signal},
    "f03_nim_proxy_roa_net_ewma_21d_v082_signal": {"func": f03_nim_proxy_roa_net_ewma_21d_v082_signal},
    "f03_nim_proxy_roa_pretax_ewma_21d_v083_signal": {"func": f03_nim_proxy_roa_pretax_ewma_21d_v083_signal},
    "f03_nim_proxy_tax_shield_ewma_21d_v084_signal": {"func": f03_nim_proxy_tax_shield_ewma_21d_v084_signal},
    "f03_nim_proxy_netinc_ewma_42d_v085_signal": {"func": f03_nim_proxy_netinc_ewma_42d_v085_signal},
    "f03_nim_proxy_assets_ewma_42d_v086_signal": {"func": f03_nim_proxy_assets_ewma_42d_v086_signal},
    "f03_nim_proxy_ebt_ewma_42d_v087_signal": {"func": f03_nim_proxy_ebt_ewma_42d_v087_signal},
    "f03_nim_proxy_roa_net_ewma_42d_v088_signal": {"func": f03_nim_proxy_roa_net_ewma_42d_v088_signal},
    "f03_nim_proxy_roa_pretax_ewma_42d_v089_signal": {"func": f03_nim_proxy_roa_pretax_ewma_42d_v089_signal},
    "f03_nim_proxy_tax_shield_ewma_42d_v090_signal": {"func": f03_nim_proxy_tax_shield_ewma_42d_v090_signal},
    "f03_nim_proxy_netinc_ewma_63d_v091_signal": {"func": f03_nim_proxy_netinc_ewma_63d_v091_signal},
    "f03_nim_proxy_assets_ewma_63d_v092_signal": {"func": f03_nim_proxy_assets_ewma_63d_v092_signal},
    "f03_nim_proxy_ebt_ewma_63d_v093_signal": {"func": f03_nim_proxy_ebt_ewma_63d_v093_signal},
    "f03_nim_proxy_roa_net_ewma_63d_v094_signal": {"func": f03_nim_proxy_roa_net_ewma_63d_v094_signal},
    "f03_nim_proxy_roa_pretax_ewma_63d_v095_signal": {"func": f03_nim_proxy_roa_pretax_ewma_63d_v095_signal},
    "f03_nim_proxy_tax_shield_ewma_63d_v096_signal": {"func": f03_nim_proxy_tax_shield_ewma_63d_v096_signal},
    "f03_nim_proxy_netinc_ewma_126d_v097_signal": {"func": f03_nim_proxy_netinc_ewma_126d_v097_signal},
    "f03_nim_proxy_assets_ewma_126d_v098_signal": {"func": f03_nim_proxy_assets_ewma_126d_v098_signal},
    "f03_nim_proxy_ebt_ewma_126d_v099_signal": {"func": f03_nim_proxy_ebt_ewma_126d_v099_signal},
    "f03_nim_proxy_roa_net_ewma_126d_v100_signal": {"func": f03_nim_proxy_roa_net_ewma_126d_v100_signal},
    "f03_nim_proxy_roa_pretax_ewma_126d_v101_signal": {"func": f03_nim_proxy_roa_pretax_ewma_126d_v101_signal},
    "f03_nim_proxy_tax_shield_ewma_126d_v102_signal": {"func": f03_nim_proxy_tax_shield_ewma_126d_v102_signal},
    "f03_nim_proxy_netinc_ewma_252d_v103_signal": {"func": f03_nim_proxy_netinc_ewma_252d_v103_signal},
    "f03_nim_proxy_assets_ewma_252d_v104_signal": {"func": f03_nim_proxy_assets_ewma_252d_v104_signal},
    "f03_nim_proxy_ebt_ewma_252d_v105_signal": {"func": f03_nim_proxy_ebt_ewma_252d_v105_signal},
    "f03_nim_proxy_roa_net_ewma_252d_v106_signal": {"func": f03_nim_proxy_roa_net_ewma_252d_v106_signal},
    "f03_nim_proxy_roa_pretax_ewma_252d_v107_signal": {"func": f03_nim_proxy_roa_pretax_ewma_252d_v107_signal},
    "f03_nim_proxy_tax_shield_ewma_252d_v108_signal": {"func": f03_nim_proxy_tax_shield_ewma_252d_v108_signal},
    "f03_nim_proxy_netinc_ewma_504d_v109_signal": {"func": f03_nim_proxy_netinc_ewma_504d_v109_signal},
    "f03_nim_proxy_assets_ewma_504d_v110_signal": {"func": f03_nim_proxy_assets_ewma_504d_v110_signal},
    "f03_nim_proxy_ebt_ewma_504d_v111_signal": {"func": f03_nim_proxy_ebt_ewma_504d_v111_signal},
    "f03_nim_proxy_roa_net_ewma_504d_v112_signal": {"func": f03_nim_proxy_roa_net_ewma_504d_v112_signal},
    "f03_nim_proxy_roa_pretax_ewma_504d_v113_signal": {"func": f03_nim_proxy_roa_pretax_ewma_504d_v113_signal},
    "f03_nim_proxy_tax_shield_ewma_504d_v114_signal": {"func": f03_nim_proxy_tax_shield_ewma_504d_v114_signal},
    "f03_nim_proxy_netinc_ewma_756d_v115_signal": {"func": f03_nim_proxy_netinc_ewma_756d_v115_signal},
    "f03_nim_proxy_assets_ewma_756d_v116_signal": {"func": f03_nim_proxy_assets_ewma_756d_v116_signal},
    "f03_nim_proxy_ebt_ewma_756d_v117_signal": {"func": f03_nim_proxy_ebt_ewma_756d_v117_signal},
    "f03_nim_proxy_roa_net_ewma_756d_v118_signal": {"func": f03_nim_proxy_roa_net_ewma_756d_v118_signal},
    "f03_nim_proxy_roa_pretax_ewma_756d_v119_signal": {"func": f03_nim_proxy_roa_pretax_ewma_756d_v119_signal},
    "f03_nim_proxy_tax_shield_ewma_756d_v120_signal": {"func": f03_nim_proxy_tax_shield_ewma_756d_v120_signal},
    "f03_nim_proxy_netinc_ewma_1008d_v121_signal": {"func": f03_nim_proxy_netinc_ewma_1008d_v121_signal},
    "f03_nim_proxy_assets_ewma_1008d_v122_signal": {"func": f03_nim_proxy_assets_ewma_1008d_v122_signal},
    "f03_nim_proxy_ebt_ewma_1008d_v123_signal": {"func": f03_nim_proxy_ebt_ewma_1008d_v123_signal},
    "f03_nim_proxy_roa_net_ewma_1008d_v124_signal": {"func": f03_nim_proxy_roa_net_ewma_1008d_v124_signal},
    "f03_nim_proxy_roa_pretax_ewma_1008d_v125_signal": {"func": f03_nim_proxy_roa_pretax_ewma_1008d_v125_signal},
    "f03_nim_proxy_tax_shield_ewma_1008d_v126_signal": {"func": f03_nim_proxy_tax_shield_ewma_1008d_v126_signal},
    "f03_nim_proxy_netinc_ewma_1260d_v127_signal": {"func": f03_nim_proxy_netinc_ewma_1260d_v127_signal},
    "f03_nim_proxy_assets_ewma_1260d_v128_signal": {"func": f03_nim_proxy_assets_ewma_1260d_v128_signal},
    "f03_nim_proxy_ebt_ewma_1260d_v129_signal": {"func": f03_nim_proxy_ebt_ewma_1260d_v129_signal},
    "f03_nim_proxy_roa_net_ewma_1260d_v130_signal": {"func": f03_nim_proxy_roa_net_ewma_1260d_v130_signal},
    "f03_nim_proxy_roa_pretax_ewma_1260d_v131_signal": {"func": f03_nim_proxy_roa_pretax_ewma_1260d_v131_signal},
    "f03_nim_proxy_tax_shield_ewma_1260d_v132_signal": {"func": f03_nim_proxy_tax_shield_ewma_1260d_v132_signal},
    "f03_nim_proxy_netinc_z_5d_v133_signal": {"func": f03_nim_proxy_netinc_z_5d_v133_signal},
    "f03_nim_proxy_assets_z_5d_v134_signal": {"func": f03_nim_proxy_assets_z_5d_v134_signal},
    "f03_nim_proxy_ebt_z_5d_v135_signal": {"func": f03_nim_proxy_ebt_z_5d_v135_signal},
    "f03_nim_proxy_roa_net_z_5d_v136_signal": {"func": f03_nim_proxy_roa_net_z_5d_v136_signal},
    "f03_nim_proxy_roa_pretax_z_5d_v137_signal": {"func": f03_nim_proxy_roa_pretax_z_5d_v137_signal},
    "f03_nim_proxy_tax_shield_z_5d_v138_signal": {"func": f03_nim_proxy_tax_shield_z_5d_v138_signal},
    "f03_nim_proxy_netinc_z_10d_v139_signal": {"func": f03_nim_proxy_netinc_z_10d_v139_signal},
    "f03_nim_proxy_assets_z_10d_v140_signal": {"func": f03_nim_proxy_assets_z_10d_v140_signal},
    "f03_nim_proxy_ebt_z_10d_v141_signal": {"func": f03_nim_proxy_ebt_z_10d_v141_signal},
    "f03_nim_proxy_roa_net_z_10d_v142_signal": {"func": f03_nim_proxy_roa_net_z_10d_v142_signal},
    "f03_nim_proxy_roa_pretax_z_10d_v143_signal": {"func": f03_nim_proxy_roa_pretax_z_10d_v143_signal},
    "f03_nim_proxy_tax_shield_z_10d_v144_signal": {"func": f03_nim_proxy_tax_shield_z_10d_v144_signal},
    "f03_nim_proxy_netinc_z_21d_v145_signal": {"func": f03_nim_proxy_netinc_z_21d_v145_signal},
    "f03_nim_proxy_assets_z_21d_v146_signal": {"func": f03_nim_proxy_assets_z_21d_v146_signal},
    "f03_nim_proxy_ebt_z_21d_v147_signal": {"func": f03_nim_proxy_ebt_z_21d_v147_signal},
    "f03_nim_proxy_roa_net_z_21d_v148_signal": {"func": f03_nim_proxy_roa_net_z_21d_v148_signal},
    "f03_nim_proxy_roa_pretax_z_21d_v149_signal": {"func": f03_nim_proxy_roa_pretax_z_21d_v149_signal},
    "f03_nim_proxy_tax_shield_z_21d_v150_signal": {"func": f03_nim_proxy_tax_shield_z_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 03...")
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
