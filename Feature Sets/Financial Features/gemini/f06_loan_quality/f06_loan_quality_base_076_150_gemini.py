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

def f06_loan_quality_netinc_ewma_63d_v076_signal(netinc):
    """Exponential moving average of Raw level of netinc over 63d window."""
    res = _ewma(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_63d_v077_signal(ebt):
    """Exponential moving average of Raw level of ebt over 63d window."""
    res = _ewma(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_63d_v078_signal(revenue):
    """Exponential moving average of Raw level of revenue over 63d window."""
    res = _ewma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_63d_v079_signal(ebt, netinc, revenue):
    """Exponential moving average of Provisioning and load proxy over 63d window."""
    res = _ewma(_ratio(ebt - netinc, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_63d_v080_signal(netinc, revenue):
    """Exponential moving average of Revenue-to-net income efficiency over 63d window."""
    res = _ewma(_ratio(netinc, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_126d_v081_signal(netinc):
    """Exponential moving average of Raw level of netinc over 126d window."""
    res = _ewma(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_126d_v082_signal(ebt):
    """Exponential moving average of Raw level of ebt over 126d window."""
    res = _ewma(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_126d_v083_signal(revenue):
    """Exponential moving average of Raw level of revenue over 126d window."""
    res = _ewma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_126d_v084_signal(ebt, netinc, revenue):
    """Exponential moving average of Provisioning and load proxy over 126d window."""
    res = _ewma(_ratio(ebt - netinc, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_126d_v085_signal(netinc, revenue):
    """Exponential moving average of Revenue-to-net income efficiency over 126d window."""
    res = _ewma(_ratio(netinc, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_252d_v086_signal(netinc):
    """Exponential moving average of Raw level of netinc over 252d window."""
    res = _ewma(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_252d_v087_signal(ebt):
    """Exponential moving average of Raw level of ebt over 252d window."""
    res = _ewma(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_252d_v088_signal(revenue):
    """Exponential moving average of Raw level of revenue over 252d window."""
    res = _ewma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_252d_v089_signal(ebt, netinc, revenue):
    """Exponential moving average of Provisioning and load proxy over 252d window."""
    res = _ewma(_ratio(ebt - netinc, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_252d_v090_signal(netinc, revenue):
    """Exponential moving average of Revenue-to-net income efficiency over 252d window."""
    res = _ewma(_ratio(netinc, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_504d_v091_signal(netinc):
    """Exponential moving average of Raw level of netinc over 504d window."""
    res = _ewma(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_504d_v092_signal(ebt):
    """Exponential moving average of Raw level of ebt over 504d window."""
    res = _ewma(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_504d_v093_signal(revenue):
    """Exponential moving average of Raw level of revenue over 504d window."""
    res = _ewma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_504d_v094_signal(ebt, netinc, revenue):
    """Exponential moving average of Provisioning and load proxy over 504d window."""
    res = _ewma(_ratio(ebt - netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_504d_v095_signal(netinc, revenue):
    """Exponential moving average of Revenue-to-net income efficiency over 504d window."""
    res = _ewma(_ratio(netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_756d_v096_signal(netinc):
    """Exponential moving average of Raw level of netinc over 756d window."""
    res = _ewma(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_756d_v097_signal(ebt):
    """Exponential moving average of Raw level of ebt over 756d window."""
    res = _ewma(ebt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_756d_v098_signal(revenue):
    """Exponential moving average of Raw level of revenue over 756d window."""
    res = _ewma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_756d_v099_signal(ebt, netinc, revenue):
    """Exponential moving average of Provisioning and load proxy over 756d window."""
    res = _ewma(_ratio(ebt - netinc, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_756d_v100_signal(netinc, revenue):
    """Exponential moving average of Revenue-to-net income efficiency over 756d window."""
    res = _ewma(_ratio(netinc, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_1008d_v101_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1008d window."""
    res = _ewma(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_1008d_v102_signal(ebt):
    """Exponential moving average of Raw level of ebt over 1008d window."""
    res = _ewma(ebt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_1008d_v103_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1008d window."""
    res = _ewma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_1008d_v104_signal(ebt, netinc, revenue):
    """Exponential moving average of Provisioning and load proxy over 1008d window."""
    res = _ewma(_ratio(ebt - netinc, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_1008d_v105_signal(netinc, revenue):
    """Exponential moving average of Revenue-to-net income efficiency over 1008d window."""
    res = _ewma(_ratio(netinc, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_ewma_1260d_v106_signal(netinc):
    """Exponential moving average of Raw level of netinc over 1260d window."""
    res = _ewma(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_ewma_1260d_v107_signal(ebt):
    """Exponential moving average of Raw level of ebt over 1260d window."""
    res = _ewma(ebt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_ewma_1260d_v108_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1260d window."""
    res = _ewma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_ewma_1260d_v109_signal(ebt, netinc, revenue):
    """Exponential moving average of Provisioning and load proxy over 1260d window."""
    res = _ewma(_ratio(ebt - netinc, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_ewma_1260d_v110_signal(netinc, revenue):
    """Exponential moving average of Revenue-to-net income efficiency over 1260d window."""
    res = _ewma(_ratio(netinc, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_z_5d_v111_signal(netinc):
    """Z-score of Raw level of netinc over 5d window."""
    res = _z(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_z_5d_v112_signal(ebt):
    """Z-score of Raw level of ebt over 5d window."""
    res = _z(ebt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_z_5d_v113_signal(revenue):
    """Z-score of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_z_5d_v114_signal(ebt, netinc, revenue):
    """Z-score of Provisioning and load proxy over 5d window."""
    res = _z(_ratio(ebt - netinc, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_z_5d_v115_signal(netinc, revenue):
    """Z-score of Revenue-to-net income efficiency over 5d window."""
    res = _z(_ratio(netinc, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_z_10d_v116_signal(netinc):
    """Z-score of Raw level of netinc over 10d window."""
    res = _z(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_z_10d_v117_signal(ebt):
    """Z-score of Raw level of ebt over 10d window."""
    res = _z(ebt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_z_10d_v118_signal(revenue):
    """Z-score of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_z_10d_v119_signal(ebt, netinc, revenue):
    """Z-score of Provisioning and load proxy over 10d window."""
    res = _z(_ratio(ebt - netinc, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_z_10d_v120_signal(netinc, revenue):
    """Z-score of Revenue-to-net income efficiency over 10d window."""
    res = _z(_ratio(netinc, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_z_21d_v121_signal(netinc):
    """Z-score of Raw level of netinc over 21d window."""
    res = _z(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_z_21d_v122_signal(ebt):
    """Z-score of Raw level of ebt over 21d window."""
    res = _z(ebt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_z_21d_v123_signal(revenue):
    """Z-score of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_z_21d_v124_signal(ebt, netinc, revenue):
    """Z-score of Provisioning and load proxy over 21d window."""
    res = _z(_ratio(ebt - netinc, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_z_21d_v125_signal(netinc, revenue):
    """Z-score of Revenue-to-net income efficiency over 21d window."""
    res = _z(_ratio(netinc, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_z_42d_v126_signal(netinc):
    """Z-score of Raw level of netinc over 42d window."""
    res = _z(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_z_42d_v127_signal(ebt):
    """Z-score of Raw level of ebt over 42d window."""
    res = _z(ebt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_z_42d_v128_signal(revenue):
    """Z-score of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_z_42d_v129_signal(ebt, netinc, revenue):
    """Z-score of Provisioning and load proxy over 42d window."""
    res = _z(_ratio(ebt - netinc, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_z_42d_v130_signal(netinc, revenue):
    """Z-score of Revenue-to-net income efficiency over 42d window."""
    res = _z(_ratio(netinc, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_z_63d_v131_signal(netinc):
    """Z-score of Raw level of netinc over 63d window."""
    res = _z(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_z_63d_v132_signal(ebt):
    """Z-score of Raw level of ebt over 63d window."""
    res = _z(ebt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_z_63d_v133_signal(revenue):
    """Z-score of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_z_63d_v134_signal(ebt, netinc, revenue):
    """Z-score of Provisioning and load proxy over 63d window."""
    res = _z(_ratio(ebt - netinc, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_z_63d_v135_signal(netinc, revenue):
    """Z-score of Revenue-to-net income efficiency over 63d window."""
    res = _z(_ratio(netinc, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_z_126d_v136_signal(netinc):
    """Z-score of Raw level of netinc over 126d window."""
    res = _z(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_z_126d_v137_signal(ebt):
    """Z-score of Raw level of ebt over 126d window."""
    res = _z(ebt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_z_126d_v138_signal(revenue):
    """Z-score of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_z_126d_v139_signal(ebt, netinc, revenue):
    """Z-score of Provisioning and load proxy over 126d window."""
    res = _z(_ratio(ebt - netinc, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_z_126d_v140_signal(netinc, revenue):
    """Z-score of Revenue-to-net income efficiency over 126d window."""
    res = _z(_ratio(netinc, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_z_252d_v141_signal(netinc):
    """Z-score of Raw level of netinc over 252d window."""
    res = _z(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_z_252d_v142_signal(ebt):
    """Z-score of Raw level of ebt over 252d window."""
    res = _z(ebt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_z_252d_v143_signal(revenue):
    """Z-score of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_z_252d_v144_signal(ebt, netinc, revenue):
    """Z-score of Provisioning and load proxy over 252d window."""
    res = _z(_ratio(ebt - netinc, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_z_252d_v145_signal(netinc, revenue):
    """Z-score of Revenue-to-net income efficiency over 252d window."""
    res = _z(_ratio(netinc, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_netinc_z_504d_v146_signal(netinc):
    """Z-score of Raw level of netinc over 504d window."""
    res = _z(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_ebt_z_504d_v147_signal(ebt):
    """Z-score of Raw level of ebt over 504d window."""
    res = _z(ebt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_revenue_z_504d_v148_signal(revenue):
    """Z-score of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_provision_drag_z_504d_v149_signal(ebt, netinc, revenue):
    """Z-score of Provisioning and load proxy over 504d window."""
    res = _z(_ratio(ebt - netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f06_loan_quality_net_margin_z_504d_v150_signal(netinc, revenue):
    """Z-score of Revenue-to-net income efficiency over 504d window."""
    res = _z(_ratio(netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f06_loan_quality_netinc_ewma_63d_v076_signal": {"func": f06_loan_quality_netinc_ewma_63d_v076_signal},
    "f06_loan_quality_ebt_ewma_63d_v077_signal": {"func": f06_loan_quality_ebt_ewma_63d_v077_signal},
    "f06_loan_quality_revenue_ewma_63d_v078_signal": {"func": f06_loan_quality_revenue_ewma_63d_v078_signal},
    "f06_loan_quality_provision_drag_ewma_63d_v079_signal": {"func": f06_loan_quality_provision_drag_ewma_63d_v079_signal},
    "f06_loan_quality_net_margin_ewma_63d_v080_signal": {"func": f06_loan_quality_net_margin_ewma_63d_v080_signal},
    "f06_loan_quality_netinc_ewma_126d_v081_signal": {"func": f06_loan_quality_netinc_ewma_126d_v081_signal},
    "f06_loan_quality_ebt_ewma_126d_v082_signal": {"func": f06_loan_quality_ebt_ewma_126d_v082_signal},
    "f06_loan_quality_revenue_ewma_126d_v083_signal": {"func": f06_loan_quality_revenue_ewma_126d_v083_signal},
    "f06_loan_quality_provision_drag_ewma_126d_v084_signal": {"func": f06_loan_quality_provision_drag_ewma_126d_v084_signal},
    "f06_loan_quality_net_margin_ewma_126d_v085_signal": {"func": f06_loan_quality_net_margin_ewma_126d_v085_signal},
    "f06_loan_quality_netinc_ewma_252d_v086_signal": {"func": f06_loan_quality_netinc_ewma_252d_v086_signal},
    "f06_loan_quality_ebt_ewma_252d_v087_signal": {"func": f06_loan_quality_ebt_ewma_252d_v087_signal},
    "f06_loan_quality_revenue_ewma_252d_v088_signal": {"func": f06_loan_quality_revenue_ewma_252d_v088_signal},
    "f06_loan_quality_provision_drag_ewma_252d_v089_signal": {"func": f06_loan_quality_provision_drag_ewma_252d_v089_signal},
    "f06_loan_quality_net_margin_ewma_252d_v090_signal": {"func": f06_loan_quality_net_margin_ewma_252d_v090_signal},
    "f06_loan_quality_netinc_ewma_504d_v091_signal": {"func": f06_loan_quality_netinc_ewma_504d_v091_signal},
    "f06_loan_quality_ebt_ewma_504d_v092_signal": {"func": f06_loan_quality_ebt_ewma_504d_v092_signal},
    "f06_loan_quality_revenue_ewma_504d_v093_signal": {"func": f06_loan_quality_revenue_ewma_504d_v093_signal},
    "f06_loan_quality_provision_drag_ewma_504d_v094_signal": {"func": f06_loan_quality_provision_drag_ewma_504d_v094_signal},
    "f06_loan_quality_net_margin_ewma_504d_v095_signal": {"func": f06_loan_quality_net_margin_ewma_504d_v095_signal},
    "f06_loan_quality_netinc_ewma_756d_v096_signal": {"func": f06_loan_quality_netinc_ewma_756d_v096_signal},
    "f06_loan_quality_ebt_ewma_756d_v097_signal": {"func": f06_loan_quality_ebt_ewma_756d_v097_signal},
    "f06_loan_quality_revenue_ewma_756d_v098_signal": {"func": f06_loan_quality_revenue_ewma_756d_v098_signal},
    "f06_loan_quality_provision_drag_ewma_756d_v099_signal": {"func": f06_loan_quality_provision_drag_ewma_756d_v099_signal},
    "f06_loan_quality_net_margin_ewma_756d_v100_signal": {"func": f06_loan_quality_net_margin_ewma_756d_v100_signal},
    "f06_loan_quality_netinc_ewma_1008d_v101_signal": {"func": f06_loan_quality_netinc_ewma_1008d_v101_signal},
    "f06_loan_quality_ebt_ewma_1008d_v102_signal": {"func": f06_loan_quality_ebt_ewma_1008d_v102_signal},
    "f06_loan_quality_revenue_ewma_1008d_v103_signal": {"func": f06_loan_quality_revenue_ewma_1008d_v103_signal},
    "f06_loan_quality_provision_drag_ewma_1008d_v104_signal": {"func": f06_loan_quality_provision_drag_ewma_1008d_v104_signal},
    "f06_loan_quality_net_margin_ewma_1008d_v105_signal": {"func": f06_loan_quality_net_margin_ewma_1008d_v105_signal},
    "f06_loan_quality_netinc_ewma_1260d_v106_signal": {"func": f06_loan_quality_netinc_ewma_1260d_v106_signal},
    "f06_loan_quality_ebt_ewma_1260d_v107_signal": {"func": f06_loan_quality_ebt_ewma_1260d_v107_signal},
    "f06_loan_quality_revenue_ewma_1260d_v108_signal": {"func": f06_loan_quality_revenue_ewma_1260d_v108_signal},
    "f06_loan_quality_provision_drag_ewma_1260d_v109_signal": {"func": f06_loan_quality_provision_drag_ewma_1260d_v109_signal},
    "f06_loan_quality_net_margin_ewma_1260d_v110_signal": {"func": f06_loan_quality_net_margin_ewma_1260d_v110_signal},
    "f06_loan_quality_netinc_z_5d_v111_signal": {"func": f06_loan_quality_netinc_z_5d_v111_signal},
    "f06_loan_quality_ebt_z_5d_v112_signal": {"func": f06_loan_quality_ebt_z_5d_v112_signal},
    "f06_loan_quality_revenue_z_5d_v113_signal": {"func": f06_loan_quality_revenue_z_5d_v113_signal},
    "f06_loan_quality_provision_drag_z_5d_v114_signal": {"func": f06_loan_quality_provision_drag_z_5d_v114_signal},
    "f06_loan_quality_net_margin_z_5d_v115_signal": {"func": f06_loan_quality_net_margin_z_5d_v115_signal},
    "f06_loan_quality_netinc_z_10d_v116_signal": {"func": f06_loan_quality_netinc_z_10d_v116_signal},
    "f06_loan_quality_ebt_z_10d_v117_signal": {"func": f06_loan_quality_ebt_z_10d_v117_signal},
    "f06_loan_quality_revenue_z_10d_v118_signal": {"func": f06_loan_quality_revenue_z_10d_v118_signal},
    "f06_loan_quality_provision_drag_z_10d_v119_signal": {"func": f06_loan_quality_provision_drag_z_10d_v119_signal},
    "f06_loan_quality_net_margin_z_10d_v120_signal": {"func": f06_loan_quality_net_margin_z_10d_v120_signal},
    "f06_loan_quality_netinc_z_21d_v121_signal": {"func": f06_loan_quality_netinc_z_21d_v121_signal},
    "f06_loan_quality_ebt_z_21d_v122_signal": {"func": f06_loan_quality_ebt_z_21d_v122_signal},
    "f06_loan_quality_revenue_z_21d_v123_signal": {"func": f06_loan_quality_revenue_z_21d_v123_signal},
    "f06_loan_quality_provision_drag_z_21d_v124_signal": {"func": f06_loan_quality_provision_drag_z_21d_v124_signal},
    "f06_loan_quality_net_margin_z_21d_v125_signal": {"func": f06_loan_quality_net_margin_z_21d_v125_signal},
    "f06_loan_quality_netinc_z_42d_v126_signal": {"func": f06_loan_quality_netinc_z_42d_v126_signal},
    "f06_loan_quality_ebt_z_42d_v127_signal": {"func": f06_loan_quality_ebt_z_42d_v127_signal},
    "f06_loan_quality_revenue_z_42d_v128_signal": {"func": f06_loan_quality_revenue_z_42d_v128_signal},
    "f06_loan_quality_provision_drag_z_42d_v129_signal": {"func": f06_loan_quality_provision_drag_z_42d_v129_signal},
    "f06_loan_quality_net_margin_z_42d_v130_signal": {"func": f06_loan_quality_net_margin_z_42d_v130_signal},
    "f06_loan_quality_netinc_z_63d_v131_signal": {"func": f06_loan_quality_netinc_z_63d_v131_signal},
    "f06_loan_quality_ebt_z_63d_v132_signal": {"func": f06_loan_quality_ebt_z_63d_v132_signal},
    "f06_loan_quality_revenue_z_63d_v133_signal": {"func": f06_loan_quality_revenue_z_63d_v133_signal},
    "f06_loan_quality_provision_drag_z_63d_v134_signal": {"func": f06_loan_quality_provision_drag_z_63d_v134_signal},
    "f06_loan_quality_net_margin_z_63d_v135_signal": {"func": f06_loan_quality_net_margin_z_63d_v135_signal},
    "f06_loan_quality_netinc_z_126d_v136_signal": {"func": f06_loan_quality_netinc_z_126d_v136_signal},
    "f06_loan_quality_ebt_z_126d_v137_signal": {"func": f06_loan_quality_ebt_z_126d_v137_signal},
    "f06_loan_quality_revenue_z_126d_v138_signal": {"func": f06_loan_quality_revenue_z_126d_v138_signal},
    "f06_loan_quality_provision_drag_z_126d_v139_signal": {"func": f06_loan_quality_provision_drag_z_126d_v139_signal},
    "f06_loan_quality_net_margin_z_126d_v140_signal": {"func": f06_loan_quality_net_margin_z_126d_v140_signal},
    "f06_loan_quality_netinc_z_252d_v141_signal": {"func": f06_loan_quality_netinc_z_252d_v141_signal},
    "f06_loan_quality_ebt_z_252d_v142_signal": {"func": f06_loan_quality_ebt_z_252d_v142_signal},
    "f06_loan_quality_revenue_z_252d_v143_signal": {"func": f06_loan_quality_revenue_z_252d_v143_signal},
    "f06_loan_quality_provision_drag_z_252d_v144_signal": {"func": f06_loan_quality_provision_drag_z_252d_v144_signal},
    "f06_loan_quality_net_margin_z_252d_v145_signal": {"func": f06_loan_quality_net_margin_z_252d_v145_signal},
    "f06_loan_quality_netinc_z_504d_v146_signal": {"func": f06_loan_quality_netinc_z_504d_v146_signal},
    "f06_loan_quality_ebt_z_504d_v147_signal": {"func": f06_loan_quality_ebt_z_504d_v147_signal},
    "f06_loan_quality_revenue_z_504d_v148_signal": {"func": f06_loan_quality_revenue_z_504d_v148_signal},
    "f06_loan_quality_provision_drag_z_504d_v149_signal": {"func": f06_loan_quality_provision_drag_z_504d_v149_signal},
    "f06_loan_quality_net_margin_z_504d_v150_signal": {"func": f06_loan_quality_net_margin_z_504d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 06...")
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
