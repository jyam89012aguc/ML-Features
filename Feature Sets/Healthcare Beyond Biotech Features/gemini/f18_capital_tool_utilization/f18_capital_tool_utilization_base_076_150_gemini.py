import pandas as pd
import numpy as np
import inspect

# ===== Healthcare High-Performance Alpha Helpers =====
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

def f18_capital_tool_utilization_capex_roi_ewma_504d_v076_signal(ebitda, capex):
    """Exponential moving average of Operating return on capex over 504d window."""
    res = _ewma(_ratio(ebitda, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_ewma_756d_v077_signal(capex):
    """Exponential moving average of Raw level of capex over 756d window."""
    res = _ewma(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_ewma_756d_v078_signal(revenue):
    """Exponential moving average of Raw level of revenue over 756d window."""
    res = _ewma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_ewma_756d_v079_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 756d window."""
    res = _ewma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_ewma_756d_v080_signal(ebitda, capex):
    """Exponential moving average of Operating return on capex over 756d window."""
    res = _ewma(_ratio(ebitda, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_ewma_1008d_v081_signal(capex):
    """Exponential moving average of Raw level of capex over 1008d window."""
    res = _ewma(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_ewma_1008d_v082_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1008d window."""
    res = _ewma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_ewma_1008d_v083_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 1008d window."""
    res = _ewma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_ewma_1008d_v084_signal(ebitda, capex):
    """Exponential moving average of Operating return on capex over 1008d window."""
    res = _ewma(_ratio(ebitda, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_ewma_1260d_v085_signal(capex):
    """Exponential moving average of Raw level of capex over 1260d window."""
    res = _ewma(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_ewma_1260d_v086_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1260d window."""
    res = _ewma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_ewma_1260d_v087_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 1260d window."""
    res = _ewma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_ewma_1260d_v088_signal(ebitda, capex):
    """Exponential moving average of Operating return on capex over 1260d window."""
    res = _ewma(_ratio(ebitda, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_5d_v089_signal(capex):
    """Z-score of Raw level of capex over 5d window."""
    res = _z(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_5d_v090_signal(revenue):
    """Z-score of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_5d_v091_signal(ebitda):
    """Z-score of Raw level of ebitda over 5d window."""
    res = _z(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_5d_v092_signal(ebitda, capex):
    """Z-score of Operating return on capex over 5d window."""
    res = _z(_ratio(ebitda, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_10d_v093_signal(capex):
    """Z-score of Raw level of capex over 10d window."""
    res = _z(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_10d_v094_signal(revenue):
    """Z-score of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_10d_v095_signal(ebitda):
    """Z-score of Raw level of ebitda over 10d window."""
    res = _z(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_10d_v096_signal(ebitda, capex):
    """Z-score of Operating return on capex over 10d window."""
    res = _z(_ratio(ebitda, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_21d_v097_signal(capex):
    """Z-score of Raw level of capex over 21d window."""
    res = _z(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_21d_v098_signal(revenue):
    """Z-score of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_21d_v099_signal(ebitda):
    """Z-score of Raw level of ebitda over 21d window."""
    res = _z(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_21d_v100_signal(ebitda, capex):
    """Z-score of Operating return on capex over 21d window."""
    res = _z(_ratio(ebitda, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_42d_v101_signal(capex):
    """Z-score of Raw level of capex over 42d window."""
    res = _z(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_42d_v102_signal(revenue):
    """Z-score of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_42d_v103_signal(ebitda):
    """Z-score of Raw level of ebitda over 42d window."""
    res = _z(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_42d_v104_signal(ebitda, capex):
    """Z-score of Operating return on capex over 42d window."""
    res = _z(_ratio(ebitda, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_63d_v105_signal(capex):
    """Z-score of Raw level of capex over 63d window."""
    res = _z(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_63d_v106_signal(revenue):
    """Z-score of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_63d_v107_signal(ebitda):
    """Z-score of Raw level of ebitda over 63d window."""
    res = _z(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_63d_v108_signal(ebitda, capex):
    """Z-score of Operating return on capex over 63d window."""
    res = _z(_ratio(ebitda, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_126d_v109_signal(capex):
    """Z-score of Raw level of capex over 126d window."""
    res = _z(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_126d_v110_signal(revenue):
    """Z-score of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_126d_v111_signal(ebitda):
    """Z-score of Raw level of ebitda over 126d window."""
    res = _z(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_126d_v112_signal(ebitda, capex):
    """Z-score of Operating return on capex over 126d window."""
    res = _z(_ratio(ebitda, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_252d_v113_signal(capex):
    """Z-score of Raw level of capex over 252d window."""
    res = _z(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_252d_v114_signal(revenue):
    """Z-score of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_252d_v115_signal(ebitda):
    """Z-score of Raw level of ebitda over 252d window."""
    res = _z(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_252d_v116_signal(ebitda, capex):
    """Z-score of Operating return on capex over 252d window."""
    res = _z(_ratio(ebitda, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_504d_v117_signal(capex):
    """Z-score of Raw level of capex over 504d window."""
    res = _z(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_504d_v118_signal(revenue):
    """Z-score of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_504d_v119_signal(ebitda):
    """Z-score of Raw level of ebitda over 504d window."""
    res = _z(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_504d_v120_signal(ebitda, capex):
    """Z-score of Operating return on capex over 504d window."""
    res = _z(_ratio(ebitda, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_756d_v121_signal(capex):
    """Z-score of Raw level of capex over 756d window."""
    res = _z(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_756d_v122_signal(revenue):
    """Z-score of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_756d_v123_signal(ebitda):
    """Z-score of Raw level of ebitda over 756d window."""
    res = _z(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_756d_v124_signal(ebitda, capex):
    """Z-score of Operating return on capex over 756d window."""
    res = _z(_ratio(ebitda, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_1008d_v125_signal(capex):
    """Z-score of Raw level of capex over 1008d window."""
    res = _z(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_1008d_v126_signal(revenue):
    """Z-score of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_1008d_v127_signal(ebitda):
    """Z-score of Raw level of ebitda over 1008d window."""
    res = _z(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_1008d_v128_signal(ebitda, capex):
    """Z-score of Operating return on capex over 1008d window."""
    res = _z(_ratio(ebitda, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_z_1260d_v129_signal(capex):
    """Z-score of Raw level of capex over 1260d window."""
    res = _z(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_z_1260d_v130_signal(revenue):
    """Z-score of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_z_1260d_v131_signal(ebitda):
    """Z-score of Raw level of ebitda over 1260d window."""
    res = _z(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_z_1260d_v132_signal(ebitda, capex):
    """Z-score of Operating return on capex over 1260d window."""
    res = _z(_ratio(ebitda, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_dd_5d_v133_signal(capex):
    """Drawdown of Raw level of capex over 5d window."""
    res = _drawdown(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_dd_5d_v134_signal(revenue):
    """Drawdown of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_dd_5d_v135_signal(ebitda):
    """Drawdown of Raw level of ebitda over 5d window."""
    res = _drawdown(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_dd_5d_v136_signal(ebitda, capex):
    """Drawdown of Operating return on capex over 5d window."""
    res = _drawdown(_ratio(ebitda, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_dd_10d_v137_signal(capex):
    """Drawdown of Raw level of capex over 10d window."""
    res = _drawdown(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_dd_10d_v138_signal(revenue):
    """Drawdown of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_dd_10d_v139_signal(ebitda):
    """Drawdown of Raw level of ebitda over 10d window."""
    res = _drawdown(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_dd_10d_v140_signal(ebitda, capex):
    """Drawdown of Operating return on capex over 10d window."""
    res = _drawdown(_ratio(ebitda, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_dd_21d_v141_signal(capex):
    """Drawdown of Raw level of capex over 21d window."""
    res = _drawdown(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_dd_21d_v142_signal(revenue):
    """Drawdown of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_dd_21d_v143_signal(ebitda):
    """Drawdown of Raw level of ebitda over 21d window."""
    res = _drawdown(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_dd_21d_v144_signal(ebitda, capex):
    """Drawdown of Operating return on capex over 21d window."""
    res = _drawdown(_ratio(ebitda, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_dd_42d_v145_signal(capex):
    """Drawdown of Raw level of capex over 42d window."""
    res = _drawdown(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_dd_42d_v146_signal(revenue):
    """Drawdown of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_ebitda_dd_42d_v147_signal(ebitda):
    """Drawdown of Raw level of ebitda over 42d window."""
    res = _drawdown(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_roi_dd_42d_v148_signal(ebitda, capex):
    """Drawdown of Operating return on capex over 42d window."""
    res = _drawdown(_ratio(ebitda, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_capex_dd_63d_v149_signal(capex):
    """Drawdown of Raw level of capex over 63d window."""
    res = _drawdown(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f18_capital_tool_utilization_revenue_dd_63d_v150_signal(revenue):
    """Drawdown of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f18_capital_tool_utilization_capex_roi_ewma_504d_v076_signal": {"func": f18_capital_tool_utilization_capex_roi_ewma_504d_v076_signal},
    "f18_capital_tool_utilization_capex_ewma_756d_v077_signal": {"func": f18_capital_tool_utilization_capex_ewma_756d_v077_signal},
    "f18_capital_tool_utilization_revenue_ewma_756d_v078_signal": {"func": f18_capital_tool_utilization_revenue_ewma_756d_v078_signal},
    "f18_capital_tool_utilization_ebitda_ewma_756d_v079_signal": {"func": f18_capital_tool_utilization_ebitda_ewma_756d_v079_signal},
    "f18_capital_tool_utilization_capex_roi_ewma_756d_v080_signal": {"func": f18_capital_tool_utilization_capex_roi_ewma_756d_v080_signal},
    "f18_capital_tool_utilization_capex_ewma_1008d_v081_signal": {"func": f18_capital_tool_utilization_capex_ewma_1008d_v081_signal},
    "f18_capital_tool_utilization_revenue_ewma_1008d_v082_signal": {"func": f18_capital_tool_utilization_revenue_ewma_1008d_v082_signal},
    "f18_capital_tool_utilization_ebitda_ewma_1008d_v083_signal": {"func": f18_capital_tool_utilization_ebitda_ewma_1008d_v083_signal},
    "f18_capital_tool_utilization_capex_roi_ewma_1008d_v084_signal": {"func": f18_capital_tool_utilization_capex_roi_ewma_1008d_v084_signal},
    "f18_capital_tool_utilization_capex_ewma_1260d_v085_signal": {"func": f18_capital_tool_utilization_capex_ewma_1260d_v085_signal},
    "f18_capital_tool_utilization_revenue_ewma_1260d_v086_signal": {"func": f18_capital_tool_utilization_revenue_ewma_1260d_v086_signal},
    "f18_capital_tool_utilization_ebitda_ewma_1260d_v087_signal": {"func": f18_capital_tool_utilization_ebitda_ewma_1260d_v087_signal},
    "f18_capital_tool_utilization_capex_roi_ewma_1260d_v088_signal": {"func": f18_capital_tool_utilization_capex_roi_ewma_1260d_v088_signal},
    "f18_capital_tool_utilization_capex_z_5d_v089_signal": {"func": f18_capital_tool_utilization_capex_z_5d_v089_signal},
    "f18_capital_tool_utilization_revenue_z_5d_v090_signal": {"func": f18_capital_tool_utilization_revenue_z_5d_v090_signal},
    "f18_capital_tool_utilization_ebitda_z_5d_v091_signal": {"func": f18_capital_tool_utilization_ebitda_z_5d_v091_signal},
    "f18_capital_tool_utilization_capex_roi_z_5d_v092_signal": {"func": f18_capital_tool_utilization_capex_roi_z_5d_v092_signal},
    "f18_capital_tool_utilization_capex_z_10d_v093_signal": {"func": f18_capital_tool_utilization_capex_z_10d_v093_signal},
    "f18_capital_tool_utilization_revenue_z_10d_v094_signal": {"func": f18_capital_tool_utilization_revenue_z_10d_v094_signal},
    "f18_capital_tool_utilization_ebitda_z_10d_v095_signal": {"func": f18_capital_tool_utilization_ebitda_z_10d_v095_signal},
    "f18_capital_tool_utilization_capex_roi_z_10d_v096_signal": {"func": f18_capital_tool_utilization_capex_roi_z_10d_v096_signal},
    "f18_capital_tool_utilization_capex_z_21d_v097_signal": {"func": f18_capital_tool_utilization_capex_z_21d_v097_signal},
    "f18_capital_tool_utilization_revenue_z_21d_v098_signal": {"func": f18_capital_tool_utilization_revenue_z_21d_v098_signal},
    "f18_capital_tool_utilization_ebitda_z_21d_v099_signal": {"func": f18_capital_tool_utilization_ebitda_z_21d_v099_signal},
    "f18_capital_tool_utilization_capex_roi_z_21d_v100_signal": {"func": f18_capital_tool_utilization_capex_roi_z_21d_v100_signal},
    "f18_capital_tool_utilization_capex_z_42d_v101_signal": {"func": f18_capital_tool_utilization_capex_z_42d_v101_signal},
    "f18_capital_tool_utilization_revenue_z_42d_v102_signal": {"func": f18_capital_tool_utilization_revenue_z_42d_v102_signal},
    "f18_capital_tool_utilization_ebitda_z_42d_v103_signal": {"func": f18_capital_tool_utilization_ebitda_z_42d_v103_signal},
    "f18_capital_tool_utilization_capex_roi_z_42d_v104_signal": {"func": f18_capital_tool_utilization_capex_roi_z_42d_v104_signal},
    "f18_capital_tool_utilization_capex_z_63d_v105_signal": {"func": f18_capital_tool_utilization_capex_z_63d_v105_signal},
    "f18_capital_tool_utilization_revenue_z_63d_v106_signal": {"func": f18_capital_tool_utilization_revenue_z_63d_v106_signal},
    "f18_capital_tool_utilization_ebitda_z_63d_v107_signal": {"func": f18_capital_tool_utilization_ebitda_z_63d_v107_signal},
    "f18_capital_tool_utilization_capex_roi_z_63d_v108_signal": {"func": f18_capital_tool_utilization_capex_roi_z_63d_v108_signal},
    "f18_capital_tool_utilization_capex_z_126d_v109_signal": {"func": f18_capital_tool_utilization_capex_z_126d_v109_signal},
    "f18_capital_tool_utilization_revenue_z_126d_v110_signal": {"func": f18_capital_tool_utilization_revenue_z_126d_v110_signal},
    "f18_capital_tool_utilization_ebitda_z_126d_v111_signal": {"func": f18_capital_tool_utilization_ebitda_z_126d_v111_signal},
    "f18_capital_tool_utilization_capex_roi_z_126d_v112_signal": {"func": f18_capital_tool_utilization_capex_roi_z_126d_v112_signal},
    "f18_capital_tool_utilization_capex_z_252d_v113_signal": {"func": f18_capital_tool_utilization_capex_z_252d_v113_signal},
    "f18_capital_tool_utilization_revenue_z_252d_v114_signal": {"func": f18_capital_tool_utilization_revenue_z_252d_v114_signal},
    "f18_capital_tool_utilization_ebitda_z_252d_v115_signal": {"func": f18_capital_tool_utilization_ebitda_z_252d_v115_signal},
    "f18_capital_tool_utilization_capex_roi_z_252d_v116_signal": {"func": f18_capital_tool_utilization_capex_roi_z_252d_v116_signal},
    "f18_capital_tool_utilization_capex_z_504d_v117_signal": {"func": f18_capital_tool_utilization_capex_z_504d_v117_signal},
    "f18_capital_tool_utilization_revenue_z_504d_v118_signal": {"func": f18_capital_tool_utilization_revenue_z_504d_v118_signal},
    "f18_capital_tool_utilization_ebitda_z_504d_v119_signal": {"func": f18_capital_tool_utilization_ebitda_z_504d_v119_signal},
    "f18_capital_tool_utilization_capex_roi_z_504d_v120_signal": {"func": f18_capital_tool_utilization_capex_roi_z_504d_v120_signal},
    "f18_capital_tool_utilization_capex_z_756d_v121_signal": {"func": f18_capital_tool_utilization_capex_z_756d_v121_signal},
    "f18_capital_tool_utilization_revenue_z_756d_v122_signal": {"func": f18_capital_tool_utilization_revenue_z_756d_v122_signal},
    "f18_capital_tool_utilization_ebitda_z_756d_v123_signal": {"func": f18_capital_tool_utilization_ebitda_z_756d_v123_signal},
    "f18_capital_tool_utilization_capex_roi_z_756d_v124_signal": {"func": f18_capital_tool_utilization_capex_roi_z_756d_v124_signal},
    "f18_capital_tool_utilization_capex_z_1008d_v125_signal": {"func": f18_capital_tool_utilization_capex_z_1008d_v125_signal},
    "f18_capital_tool_utilization_revenue_z_1008d_v126_signal": {"func": f18_capital_tool_utilization_revenue_z_1008d_v126_signal},
    "f18_capital_tool_utilization_ebitda_z_1008d_v127_signal": {"func": f18_capital_tool_utilization_ebitda_z_1008d_v127_signal},
    "f18_capital_tool_utilization_capex_roi_z_1008d_v128_signal": {"func": f18_capital_tool_utilization_capex_roi_z_1008d_v128_signal},
    "f18_capital_tool_utilization_capex_z_1260d_v129_signal": {"func": f18_capital_tool_utilization_capex_z_1260d_v129_signal},
    "f18_capital_tool_utilization_revenue_z_1260d_v130_signal": {"func": f18_capital_tool_utilization_revenue_z_1260d_v130_signal},
    "f18_capital_tool_utilization_ebitda_z_1260d_v131_signal": {"func": f18_capital_tool_utilization_ebitda_z_1260d_v131_signal},
    "f18_capital_tool_utilization_capex_roi_z_1260d_v132_signal": {"func": f18_capital_tool_utilization_capex_roi_z_1260d_v132_signal},
    "f18_capital_tool_utilization_capex_dd_5d_v133_signal": {"func": f18_capital_tool_utilization_capex_dd_5d_v133_signal},
    "f18_capital_tool_utilization_revenue_dd_5d_v134_signal": {"func": f18_capital_tool_utilization_revenue_dd_5d_v134_signal},
    "f18_capital_tool_utilization_ebitda_dd_5d_v135_signal": {"func": f18_capital_tool_utilization_ebitda_dd_5d_v135_signal},
    "f18_capital_tool_utilization_capex_roi_dd_5d_v136_signal": {"func": f18_capital_tool_utilization_capex_roi_dd_5d_v136_signal},
    "f18_capital_tool_utilization_capex_dd_10d_v137_signal": {"func": f18_capital_tool_utilization_capex_dd_10d_v137_signal},
    "f18_capital_tool_utilization_revenue_dd_10d_v138_signal": {"func": f18_capital_tool_utilization_revenue_dd_10d_v138_signal},
    "f18_capital_tool_utilization_ebitda_dd_10d_v139_signal": {"func": f18_capital_tool_utilization_ebitda_dd_10d_v139_signal},
    "f18_capital_tool_utilization_capex_roi_dd_10d_v140_signal": {"func": f18_capital_tool_utilization_capex_roi_dd_10d_v140_signal},
    "f18_capital_tool_utilization_capex_dd_21d_v141_signal": {"func": f18_capital_tool_utilization_capex_dd_21d_v141_signal},
    "f18_capital_tool_utilization_revenue_dd_21d_v142_signal": {"func": f18_capital_tool_utilization_revenue_dd_21d_v142_signal},
    "f18_capital_tool_utilization_ebitda_dd_21d_v143_signal": {"func": f18_capital_tool_utilization_ebitda_dd_21d_v143_signal},
    "f18_capital_tool_utilization_capex_roi_dd_21d_v144_signal": {"func": f18_capital_tool_utilization_capex_roi_dd_21d_v144_signal},
    "f18_capital_tool_utilization_capex_dd_42d_v145_signal": {"func": f18_capital_tool_utilization_capex_dd_42d_v145_signal},
    "f18_capital_tool_utilization_revenue_dd_42d_v146_signal": {"func": f18_capital_tool_utilization_revenue_dd_42d_v146_signal},
    "f18_capital_tool_utilization_ebitda_dd_42d_v147_signal": {"func": f18_capital_tool_utilization_ebitda_dd_42d_v147_signal},
    "f18_capital_tool_utilization_capex_roi_dd_42d_v148_signal": {"func": f18_capital_tool_utilization_capex_roi_dd_42d_v148_signal},
    "f18_capital_tool_utilization_capex_dd_63d_v149_signal": {"func": f18_capital_tool_utilization_capex_dd_63d_v149_signal},
    "f18_capital_tool_utilization_revenue_dd_63d_v150_signal": {"func": f18_capital_tool_utilization_revenue_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "sbcomp": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 18...")
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
