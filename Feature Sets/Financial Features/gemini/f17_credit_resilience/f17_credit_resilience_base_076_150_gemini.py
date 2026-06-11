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

def f17_credit_resilience_pretax_margin_ewma_504d_v076_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 504d window."""
    res = _ewma(_ratio(ebt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_ewma_756d_v077_signal(netinc):
    """Exponential moving average of Raw level of netinc over 756d window."""
    res = _ewma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_ewma_756d_v078_signal(ebt):
    """Exponential moving average of Raw level of ebt over 756d window."""
    res = _ewma(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_ewma_756d_v079_signal(assets):
    """Exponential moving average of Raw level of assets over 756d window."""
    res = _ewma(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_ewma_756d_v080_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 756d window."""
    res = _ewma(_ratio(ebt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_ewma_1008d_v081_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1008d window."""
    res = _ewma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_ewma_1008d_v082_signal(ebt):
    """Exponential moving average of Raw level of ebt over 1008d window."""
    res = _ewma(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_ewma_1008d_v083_signal(assets):
    """Exponential moving average of Raw level of assets over 1008d window."""
    res = _ewma(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_ewma_1008d_v084_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 1008d window."""
    res = _ewma(_ratio(ebt, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_ewma_1260d_v085_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1260d window."""
    res = _ewma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_ewma_1260d_v086_signal(ebt):
    """Exponential moving average of Raw level of ebt over 1260d window."""
    res = _ewma(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_ewma_1260d_v087_signal(assets):
    """Exponential moving average of Raw level of assets over 1260d window."""
    res = _ewma(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_ewma_1260d_v088_signal(ebt, assets):
    """Exponential moving average of Pre-tax return on assets over 1260d window."""
    res = _ewma(_ratio(ebt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_5d_v089_signal(netinc):
    """Z-score of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_5d_v090_signal(ebt):
    """Z-score of Raw level of ebt over 5d window."""
    res = _z(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_5d_v091_signal(assets):
    """Z-score of Raw level of assets over 5d window."""
    res = _z(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_5d_v092_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 5d window."""
    res = _z(_ratio(ebt, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_10d_v093_signal(netinc):
    """Z-score of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_10d_v094_signal(ebt):
    """Z-score of Raw level of ebt over 10d window."""
    res = _z(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_10d_v095_signal(assets):
    """Z-score of Raw level of assets over 10d window."""
    res = _z(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_10d_v096_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 10d window."""
    res = _z(_ratio(ebt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_21d_v097_signal(netinc):
    """Z-score of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_21d_v098_signal(ebt):
    """Z-score of Raw level of ebt over 21d window."""
    res = _z(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_21d_v099_signal(assets):
    """Z-score of Raw level of assets over 21d window."""
    res = _z(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_21d_v100_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 21d window."""
    res = _z(_ratio(ebt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_42d_v101_signal(netinc):
    """Z-score of Raw level of netinc over 42d window."""
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_42d_v102_signal(ebt):
    """Z-score of Raw level of ebt over 42d window."""
    res = _z(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_42d_v103_signal(assets):
    """Z-score of Raw level of assets over 42d window."""
    res = _z(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_42d_v104_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 42d window."""
    res = _z(_ratio(ebt, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_63d_v105_signal(netinc):
    """Z-score of Raw level of netinc over 63d window."""
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_63d_v106_signal(ebt):
    """Z-score of Raw level of ebt over 63d window."""
    res = _z(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_63d_v107_signal(assets):
    """Z-score of Raw level of assets over 63d window."""
    res = _z(assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_63d_v108_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 63d window."""
    res = _z(_ratio(ebt, assets), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_126d_v109_signal(netinc):
    """Z-score of Raw level of netinc over 126d window."""
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_126d_v110_signal(ebt):
    """Z-score of Raw level of ebt over 126d window."""
    res = _z(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_126d_v111_signal(assets):
    """Z-score of Raw level of assets over 126d window."""
    res = _z(assets, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_126d_v112_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 126d window."""
    res = _z(_ratio(ebt, assets), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_252d_v113_signal(netinc):
    """Z-score of Raw level of netinc over 252d window."""
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_252d_v114_signal(ebt):
    """Z-score of Raw level of ebt over 252d window."""
    res = _z(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_252d_v115_signal(assets):
    """Z-score of Raw level of assets over 252d window."""
    res = _z(assets, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_252d_v116_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 252d window."""
    res = _z(_ratio(ebt, assets), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_504d_v117_signal(netinc):
    """Z-score of Raw level of netinc over 504d window."""
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_504d_v118_signal(ebt):
    """Z-score of Raw level of ebt over 504d window."""
    res = _z(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_504d_v119_signal(assets):
    """Z-score of Raw level of assets over 504d window."""
    res = _z(assets, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_504d_v120_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 504d window."""
    res = _z(_ratio(ebt, assets), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_756d_v121_signal(netinc):
    """Z-score of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_756d_v122_signal(ebt):
    """Z-score of Raw level of ebt over 756d window."""
    res = _z(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_756d_v123_signal(assets):
    """Z-score of Raw level of assets over 756d window."""
    res = _z(assets, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_756d_v124_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 756d window."""
    res = _z(_ratio(ebt, assets), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_1008d_v125_signal(netinc):
    """Z-score of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_1008d_v126_signal(ebt):
    """Z-score of Raw level of ebt over 1008d window."""
    res = _z(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_1008d_v127_signal(assets):
    """Z-score of Raw level of assets over 1008d window."""
    res = _z(assets, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_1008d_v128_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 1008d window."""
    res = _z(_ratio(ebt, assets), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_z_1260d_v129_signal(netinc):
    """Z-score of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_z_1260d_v130_signal(ebt):
    """Z-score of Raw level of ebt over 1260d window."""
    res = _z(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_z_1260d_v131_signal(assets):
    """Z-score of Raw level of assets over 1260d window."""
    res = _z(assets, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_z_1260d_v132_signal(ebt, assets):
    """Z-score of Pre-tax return on assets over 1260d window."""
    res = _z(_ratio(ebt, assets), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_dd_5d_v133_signal(netinc):
    """Drawdown of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_dd_5d_v134_signal(ebt):
    """Drawdown of Raw level of ebt over 5d window."""
    res = _drawdown(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_dd_5d_v135_signal(assets):
    """Drawdown of Raw level of assets over 5d window."""
    res = _drawdown(assets, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_dd_5d_v136_signal(ebt, assets):
    """Drawdown of Pre-tax return on assets over 5d window."""
    res = _drawdown(_ratio(ebt, assets), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_dd_10d_v137_signal(netinc):
    """Drawdown of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_dd_10d_v138_signal(ebt):
    """Drawdown of Raw level of ebt over 10d window."""
    res = _drawdown(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_dd_10d_v139_signal(assets):
    """Drawdown of Raw level of assets over 10d window."""
    res = _drawdown(assets, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_dd_10d_v140_signal(ebt, assets):
    """Drawdown of Pre-tax return on assets over 10d window."""
    res = _drawdown(_ratio(ebt, assets), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_dd_21d_v141_signal(netinc):
    """Drawdown of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_dd_21d_v142_signal(ebt):
    """Drawdown of Raw level of ebt over 21d window."""
    res = _drawdown(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_dd_21d_v143_signal(assets):
    """Drawdown of Raw level of assets over 21d window."""
    res = _drawdown(assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_dd_21d_v144_signal(ebt, assets):
    """Drawdown of Pre-tax return on assets over 21d window."""
    res = _drawdown(_ratio(ebt, assets), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_dd_42d_v145_signal(netinc):
    """Drawdown of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_dd_42d_v146_signal(ebt):
    """Drawdown of Raw level of ebt over 42d window."""
    res = _drawdown(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_assets_dd_42d_v147_signal(assets):
    """Drawdown of Raw level of assets over 42d window."""
    res = _drawdown(assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_pretax_margin_dd_42d_v148_signal(ebt, assets):
    """Drawdown of Pre-tax return on assets over 42d window."""
    res = _drawdown(_ratio(ebt, assets), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_netinc_dd_63d_v149_signal(netinc):
    """Drawdown of Raw level of netinc over 63d window."""
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f17_credit_resilience_ebt_dd_63d_v150_signal(ebt):
    """Drawdown of Raw level of ebt over 63d window."""
    res = _drawdown(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f17_credit_resilience_pretax_margin_ewma_504d_v076_signal": {"func": f17_credit_resilience_pretax_margin_ewma_504d_v076_signal},
    "f17_credit_resilience_netinc_ewma_756d_v077_signal": {"func": f17_credit_resilience_netinc_ewma_756d_v077_signal},
    "f17_credit_resilience_ebt_ewma_756d_v078_signal": {"func": f17_credit_resilience_ebt_ewma_756d_v078_signal},
    "f17_credit_resilience_assets_ewma_756d_v079_signal": {"func": f17_credit_resilience_assets_ewma_756d_v079_signal},
    "f17_credit_resilience_pretax_margin_ewma_756d_v080_signal": {"func": f17_credit_resilience_pretax_margin_ewma_756d_v080_signal},
    "f17_credit_resilience_netinc_ewma_1008d_v081_signal": {"func": f17_credit_resilience_netinc_ewma_1008d_v081_signal},
    "f17_credit_resilience_ebt_ewma_1008d_v082_signal": {"func": f17_credit_resilience_ebt_ewma_1008d_v082_signal},
    "f17_credit_resilience_assets_ewma_1008d_v083_signal": {"func": f17_credit_resilience_assets_ewma_1008d_v083_signal},
    "f17_credit_resilience_pretax_margin_ewma_1008d_v084_signal": {"func": f17_credit_resilience_pretax_margin_ewma_1008d_v084_signal},
    "f17_credit_resilience_netinc_ewma_1260d_v085_signal": {"func": f17_credit_resilience_netinc_ewma_1260d_v085_signal},
    "f17_credit_resilience_ebt_ewma_1260d_v086_signal": {"func": f17_credit_resilience_ebt_ewma_1260d_v086_signal},
    "f17_credit_resilience_assets_ewma_1260d_v087_signal": {"func": f17_credit_resilience_assets_ewma_1260d_v087_signal},
    "f17_credit_resilience_pretax_margin_ewma_1260d_v088_signal": {"func": f17_credit_resilience_pretax_margin_ewma_1260d_v088_signal},
    "f17_credit_resilience_netinc_z_5d_v089_signal": {"func": f17_credit_resilience_netinc_z_5d_v089_signal},
    "f17_credit_resilience_ebt_z_5d_v090_signal": {"func": f17_credit_resilience_ebt_z_5d_v090_signal},
    "f17_credit_resilience_assets_z_5d_v091_signal": {"func": f17_credit_resilience_assets_z_5d_v091_signal},
    "f17_credit_resilience_pretax_margin_z_5d_v092_signal": {"func": f17_credit_resilience_pretax_margin_z_5d_v092_signal},
    "f17_credit_resilience_netinc_z_10d_v093_signal": {"func": f17_credit_resilience_netinc_z_10d_v093_signal},
    "f17_credit_resilience_ebt_z_10d_v094_signal": {"func": f17_credit_resilience_ebt_z_10d_v094_signal},
    "f17_credit_resilience_assets_z_10d_v095_signal": {"func": f17_credit_resilience_assets_z_10d_v095_signal},
    "f17_credit_resilience_pretax_margin_z_10d_v096_signal": {"func": f17_credit_resilience_pretax_margin_z_10d_v096_signal},
    "f17_credit_resilience_netinc_z_21d_v097_signal": {"func": f17_credit_resilience_netinc_z_21d_v097_signal},
    "f17_credit_resilience_ebt_z_21d_v098_signal": {"func": f17_credit_resilience_ebt_z_21d_v098_signal},
    "f17_credit_resilience_assets_z_21d_v099_signal": {"func": f17_credit_resilience_assets_z_21d_v099_signal},
    "f17_credit_resilience_pretax_margin_z_21d_v100_signal": {"func": f17_credit_resilience_pretax_margin_z_21d_v100_signal},
    "f17_credit_resilience_netinc_z_42d_v101_signal": {"func": f17_credit_resilience_netinc_z_42d_v101_signal},
    "f17_credit_resilience_ebt_z_42d_v102_signal": {"func": f17_credit_resilience_ebt_z_42d_v102_signal},
    "f17_credit_resilience_assets_z_42d_v103_signal": {"func": f17_credit_resilience_assets_z_42d_v103_signal},
    "f17_credit_resilience_pretax_margin_z_42d_v104_signal": {"func": f17_credit_resilience_pretax_margin_z_42d_v104_signal},
    "f17_credit_resilience_netinc_z_63d_v105_signal": {"func": f17_credit_resilience_netinc_z_63d_v105_signal},
    "f17_credit_resilience_ebt_z_63d_v106_signal": {"func": f17_credit_resilience_ebt_z_63d_v106_signal},
    "f17_credit_resilience_assets_z_63d_v107_signal": {"func": f17_credit_resilience_assets_z_63d_v107_signal},
    "f17_credit_resilience_pretax_margin_z_63d_v108_signal": {"func": f17_credit_resilience_pretax_margin_z_63d_v108_signal},
    "f17_credit_resilience_netinc_z_126d_v109_signal": {"func": f17_credit_resilience_netinc_z_126d_v109_signal},
    "f17_credit_resilience_ebt_z_126d_v110_signal": {"func": f17_credit_resilience_ebt_z_126d_v110_signal},
    "f17_credit_resilience_assets_z_126d_v111_signal": {"func": f17_credit_resilience_assets_z_126d_v111_signal},
    "f17_credit_resilience_pretax_margin_z_126d_v112_signal": {"func": f17_credit_resilience_pretax_margin_z_126d_v112_signal},
    "f17_credit_resilience_netinc_z_252d_v113_signal": {"func": f17_credit_resilience_netinc_z_252d_v113_signal},
    "f17_credit_resilience_ebt_z_252d_v114_signal": {"func": f17_credit_resilience_ebt_z_252d_v114_signal},
    "f17_credit_resilience_assets_z_252d_v115_signal": {"func": f17_credit_resilience_assets_z_252d_v115_signal},
    "f17_credit_resilience_pretax_margin_z_252d_v116_signal": {"func": f17_credit_resilience_pretax_margin_z_252d_v116_signal},
    "f17_credit_resilience_netinc_z_504d_v117_signal": {"func": f17_credit_resilience_netinc_z_504d_v117_signal},
    "f17_credit_resilience_ebt_z_504d_v118_signal": {"func": f17_credit_resilience_ebt_z_504d_v118_signal},
    "f17_credit_resilience_assets_z_504d_v119_signal": {"func": f17_credit_resilience_assets_z_504d_v119_signal},
    "f17_credit_resilience_pretax_margin_z_504d_v120_signal": {"func": f17_credit_resilience_pretax_margin_z_504d_v120_signal},
    "f17_credit_resilience_netinc_z_756d_v121_signal": {"func": f17_credit_resilience_netinc_z_756d_v121_signal},
    "f17_credit_resilience_ebt_z_756d_v122_signal": {"func": f17_credit_resilience_ebt_z_756d_v122_signal},
    "f17_credit_resilience_assets_z_756d_v123_signal": {"func": f17_credit_resilience_assets_z_756d_v123_signal},
    "f17_credit_resilience_pretax_margin_z_756d_v124_signal": {"func": f17_credit_resilience_pretax_margin_z_756d_v124_signal},
    "f17_credit_resilience_netinc_z_1008d_v125_signal": {"func": f17_credit_resilience_netinc_z_1008d_v125_signal},
    "f17_credit_resilience_ebt_z_1008d_v126_signal": {"func": f17_credit_resilience_ebt_z_1008d_v126_signal},
    "f17_credit_resilience_assets_z_1008d_v127_signal": {"func": f17_credit_resilience_assets_z_1008d_v127_signal},
    "f17_credit_resilience_pretax_margin_z_1008d_v128_signal": {"func": f17_credit_resilience_pretax_margin_z_1008d_v128_signal},
    "f17_credit_resilience_netinc_z_1260d_v129_signal": {"func": f17_credit_resilience_netinc_z_1260d_v129_signal},
    "f17_credit_resilience_ebt_z_1260d_v130_signal": {"func": f17_credit_resilience_ebt_z_1260d_v130_signal},
    "f17_credit_resilience_assets_z_1260d_v131_signal": {"func": f17_credit_resilience_assets_z_1260d_v131_signal},
    "f17_credit_resilience_pretax_margin_z_1260d_v132_signal": {"func": f17_credit_resilience_pretax_margin_z_1260d_v132_signal},
    "f17_credit_resilience_netinc_dd_5d_v133_signal": {"func": f17_credit_resilience_netinc_dd_5d_v133_signal},
    "f17_credit_resilience_ebt_dd_5d_v134_signal": {"func": f17_credit_resilience_ebt_dd_5d_v134_signal},
    "f17_credit_resilience_assets_dd_5d_v135_signal": {"func": f17_credit_resilience_assets_dd_5d_v135_signal},
    "f17_credit_resilience_pretax_margin_dd_5d_v136_signal": {"func": f17_credit_resilience_pretax_margin_dd_5d_v136_signal},
    "f17_credit_resilience_netinc_dd_10d_v137_signal": {"func": f17_credit_resilience_netinc_dd_10d_v137_signal},
    "f17_credit_resilience_ebt_dd_10d_v138_signal": {"func": f17_credit_resilience_ebt_dd_10d_v138_signal},
    "f17_credit_resilience_assets_dd_10d_v139_signal": {"func": f17_credit_resilience_assets_dd_10d_v139_signal},
    "f17_credit_resilience_pretax_margin_dd_10d_v140_signal": {"func": f17_credit_resilience_pretax_margin_dd_10d_v140_signal},
    "f17_credit_resilience_netinc_dd_21d_v141_signal": {"func": f17_credit_resilience_netinc_dd_21d_v141_signal},
    "f17_credit_resilience_ebt_dd_21d_v142_signal": {"func": f17_credit_resilience_ebt_dd_21d_v142_signal},
    "f17_credit_resilience_assets_dd_21d_v143_signal": {"func": f17_credit_resilience_assets_dd_21d_v143_signal},
    "f17_credit_resilience_pretax_margin_dd_21d_v144_signal": {"func": f17_credit_resilience_pretax_margin_dd_21d_v144_signal},
    "f17_credit_resilience_netinc_dd_42d_v145_signal": {"func": f17_credit_resilience_netinc_dd_42d_v145_signal},
    "f17_credit_resilience_ebt_dd_42d_v146_signal": {"func": f17_credit_resilience_ebt_dd_42d_v146_signal},
    "f17_credit_resilience_assets_dd_42d_v147_signal": {"func": f17_credit_resilience_assets_dd_42d_v147_signal},
    "f17_credit_resilience_pretax_margin_dd_42d_v148_signal": {"func": f17_credit_resilience_pretax_margin_dd_42d_v148_signal},
    "f17_credit_resilience_netinc_dd_63d_v149_signal": {"func": f17_credit_resilience_netinc_dd_63d_v149_signal},
    "f17_credit_resilience_ebt_dd_63d_v150_signal": {"func": f17_credit_resilience_ebt_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 17...")
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
