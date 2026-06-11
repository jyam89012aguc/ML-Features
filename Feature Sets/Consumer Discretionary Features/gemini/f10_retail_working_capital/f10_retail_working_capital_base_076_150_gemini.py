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

def f10_retail_working_capital_inventory_z_63d_v076_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 63d window."""
    res = _z(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_63d_v077_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 63d window."""
    res = _z(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_63d_v078_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 63d window."""
    res = _z(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_63d_v079_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_63d_v080_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 63d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_126d_v081_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 126d window."""
    res = _z(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_126d_v082_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 126d window."""
    res = _z(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_126d_v083_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 126d window."""
    res = _z(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_126d_v084_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_126d_v085_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 126d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_252d_v086_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 252d window."""
    res = _z(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_252d_v087_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 252d window."""
    res = _z(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_252d_v088_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 252d window."""
    res = _z(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_252d_v089_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_252d_v090_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 252d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_504d_v091_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 504d window."""
    res = _z(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_504d_v092_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 504d window."""
    res = _z(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_504d_v093_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 504d window."""
    res = _z(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_504d_v094_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_504d_v095_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 504d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_756d_v096_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 756d window."""
    res = _z(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_756d_v097_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 756d window."""
    res = _z(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_756d_v098_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 756d window."""
    res = _z(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_756d_v099_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_756d_v100_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 756d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_1008d_v101_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 1008d window."""
    res = _z(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_1008d_v102_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 1008d window."""
    res = _z(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_1008d_v103_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 1008d window."""
    res = _z(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_1008d_v104_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_1008d_v105_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 1008d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_z_1260d_v106_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 1260d window."""
    res = _z(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_z_1260d_v107_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 1260d window."""
    res = _z(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_z_1260d_v108_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 1260d window."""
    res = _z(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_z_1260d_v109_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_z_1260d_v110_signal(inventory, receivables, payables, revenue):
    """Z-score for relative outlier detection of Working capital load per dollar of sales over 1260d window."""
    res = _z(_ratio(inventory + receivables - payables, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_dd_5d_v111_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 5d window."""
    res = _drawdown(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_dd_5d_v112_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 5d window."""
    res = _drawdown(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_dd_5d_v113_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 5d window."""
    res = _drawdown(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_dd_5d_v114_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_dd_5d_v115_signal(inventory, receivables, payables, revenue):
    """Drawdown from peak to identify cycle troughs of Working capital load per dollar of sales over 5d window."""
    res = _drawdown(_ratio(inventory + receivables - payables, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_dd_10d_v116_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 10d window."""
    res = _drawdown(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_dd_10d_v117_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 10d window."""
    res = _drawdown(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_dd_10d_v118_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 10d window."""
    res = _drawdown(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_dd_10d_v119_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_dd_10d_v120_signal(inventory, receivables, payables, revenue):
    """Drawdown from peak to identify cycle troughs of Working capital load per dollar of sales over 10d window."""
    res = _drawdown(_ratio(inventory + receivables - payables, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_dd_21d_v121_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 21d window."""
    res = _drawdown(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_dd_21d_v122_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 21d window."""
    res = _drawdown(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_dd_21d_v123_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 21d window."""
    res = _drawdown(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_dd_21d_v124_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_dd_21d_v125_signal(inventory, receivables, payables, revenue):
    """Drawdown from peak to identify cycle troughs of Working capital load per dollar of sales over 21d window."""
    res = _drawdown(_ratio(inventory + receivables - payables, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_dd_42d_v126_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 42d window."""
    res = _drawdown(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_dd_42d_v127_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 42d window."""
    res = _drawdown(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_dd_42d_v128_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 42d window."""
    res = _drawdown(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_dd_42d_v129_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_dd_42d_v130_signal(inventory, receivables, payables, revenue):
    """Drawdown from peak to identify cycle troughs of Working capital load per dollar of sales over 42d window."""
    res = _drawdown(_ratio(inventory + receivables - payables, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_dd_63d_v131_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 63d window."""
    res = _drawdown(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_dd_63d_v132_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 63d window."""
    res = _drawdown(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_dd_63d_v133_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 63d window."""
    res = _drawdown(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_dd_63d_v134_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_dd_63d_v135_signal(inventory, receivables, payables, revenue):
    """Drawdown from peak to identify cycle troughs of Working capital load per dollar of sales over 63d window."""
    res = _drawdown(_ratio(inventory + receivables - payables, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_dd_126d_v136_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 126d window."""
    res = _drawdown(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_dd_126d_v137_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 126d window."""
    res = _drawdown(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_dd_126d_v138_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 126d window."""
    res = _drawdown(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_dd_126d_v139_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 126d window."""
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_dd_126d_v140_signal(inventory, receivables, payables, revenue):
    """Drawdown from peak to identify cycle troughs of Working capital load per dollar of sales over 126d window."""
    res = _drawdown(_ratio(inventory + receivables - payables, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_dd_252d_v141_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 252d window."""
    res = _drawdown(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_dd_252d_v142_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 252d window."""
    res = _drawdown(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_dd_252d_v143_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 252d window."""
    res = _drawdown(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_dd_252d_v144_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 252d window."""
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_dd_252d_v145_signal(inventory, receivables, payables, revenue):
    """Drawdown from peak to identify cycle troughs of Working capital load per dollar of sales over 252d window."""
    res = _drawdown(_ratio(inventory + receivables - payables, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_inventory_dd_504d_v146_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 504d window."""
    res = _drawdown(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_receivables_dd_504d_v147_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 504d window."""
    res = _drawdown(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_payables_dd_504d_v148_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 504d window."""
    res = _drawdown(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_revenue_dd_504d_v149_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 504d window."""
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_retail_working_capital_wc_drag_dd_504d_v150_signal(inventory, receivables, payables, revenue):
    """Drawdown from peak to identify cycle troughs of Working capital load per dollar of sales over 504d window."""
    res = _drawdown(_ratio(inventory + receivables - payables, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f10_retail_working_capital_inventory_z_63d_v076_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_63d_v076_signal},    "f10_retail_working_capital_receivables_z_63d_v077_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_63d_v077_signal},    "f10_retail_working_capital_payables_z_63d_v078_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_63d_v078_signal},    "f10_retail_working_capital_revenue_z_63d_v079_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_63d_v079_signal},    "f10_retail_working_capital_wc_drag_z_63d_v080_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_63d_v080_signal},    "f10_retail_working_capital_inventory_z_126d_v081_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_126d_v081_signal},    "f10_retail_working_capital_receivables_z_126d_v082_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_126d_v082_signal},    "f10_retail_working_capital_payables_z_126d_v083_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_126d_v083_signal},    "f10_retail_working_capital_revenue_z_126d_v084_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_126d_v084_signal},    "f10_retail_working_capital_wc_drag_z_126d_v085_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_126d_v085_signal},    "f10_retail_working_capital_inventory_z_252d_v086_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_252d_v086_signal},    "f10_retail_working_capital_receivables_z_252d_v087_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_252d_v087_signal},    "f10_retail_working_capital_payables_z_252d_v088_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_252d_v088_signal},    "f10_retail_working_capital_revenue_z_252d_v089_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_252d_v089_signal},    "f10_retail_working_capital_wc_drag_z_252d_v090_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_252d_v090_signal},    "f10_retail_working_capital_inventory_z_504d_v091_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_504d_v091_signal},    "f10_retail_working_capital_receivables_z_504d_v092_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_504d_v092_signal},    "f10_retail_working_capital_payables_z_504d_v093_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_504d_v093_signal},    "f10_retail_working_capital_revenue_z_504d_v094_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_504d_v094_signal},    "f10_retail_working_capital_wc_drag_z_504d_v095_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_504d_v095_signal},    "f10_retail_working_capital_inventory_z_756d_v096_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_756d_v096_signal},    "f10_retail_working_capital_receivables_z_756d_v097_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_756d_v097_signal},    "f10_retail_working_capital_payables_z_756d_v098_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_756d_v098_signal},    "f10_retail_working_capital_revenue_z_756d_v099_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_756d_v099_signal},    "f10_retail_working_capital_wc_drag_z_756d_v100_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_756d_v100_signal},    "f10_retail_working_capital_inventory_z_1008d_v101_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_1008d_v101_signal},    "f10_retail_working_capital_receivables_z_1008d_v102_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_1008d_v102_signal},    "f10_retail_working_capital_payables_z_1008d_v103_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_1008d_v103_signal},    "f10_retail_working_capital_revenue_z_1008d_v104_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_1008d_v104_signal},    "f10_retail_working_capital_wc_drag_z_1008d_v105_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_1008d_v105_signal},    "f10_retail_working_capital_inventory_z_1260d_v106_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_z_1260d_v106_signal},    "f10_retail_working_capital_receivables_z_1260d_v107_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_z_1260d_v107_signal},    "f10_retail_working_capital_payables_z_1260d_v108_signal": {"inputs": [], "func": f10_retail_working_capital_payables_z_1260d_v108_signal},    "f10_retail_working_capital_revenue_z_1260d_v109_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_z_1260d_v109_signal},    "f10_retail_working_capital_wc_drag_z_1260d_v110_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_z_1260d_v110_signal},    "f10_retail_working_capital_inventory_dd_5d_v111_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_dd_5d_v111_signal},    "f10_retail_working_capital_receivables_dd_5d_v112_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_dd_5d_v112_signal},    "f10_retail_working_capital_payables_dd_5d_v113_signal": {"inputs": [], "func": f10_retail_working_capital_payables_dd_5d_v113_signal},    "f10_retail_working_capital_revenue_dd_5d_v114_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_dd_5d_v114_signal},    "f10_retail_working_capital_wc_drag_dd_5d_v115_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_dd_5d_v115_signal},    "f10_retail_working_capital_inventory_dd_10d_v116_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_dd_10d_v116_signal},    "f10_retail_working_capital_receivables_dd_10d_v117_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_dd_10d_v117_signal},    "f10_retail_working_capital_payables_dd_10d_v118_signal": {"inputs": [], "func": f10_retail_working_capital_payables_dd_10d_v118_signal},    "f10_retail_working_capital_revenue_dd_10d_v119_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_dd_10d_v119_signal},    "f10_retail_working_capital_wc_drag_dd_10d_v120_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_dd_10d_v120_signal},    "f10_retail_working_capital_inventory_dd_21d_v121_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_dd_21d_v121_signal},    "f10_retail_working_capital_receivables_dd_21d_v122_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_dd_21d_v122_signal},    "f10_retail_working_capital_payables_dd_21d_v123_signal": {"inputs": [], "func": f10_retail_working_capital_payables_dd_21d_v123_signal},    "f10_retail_working_capital_revenue_dd_21d_v124_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_dd_21d_v124_signal},    "f10_retail_working_capital_wc_drag_dd_21d_v125_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_dd_21d_v125_signal},    "f10_retail_working_capital_inventory_dd_42d_v126_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_dd_42d_v126_signal},    "f10_retail_working_capital_receivables_dd_42d_v127_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_dd_42d_v127_signal},    "f10_retail_working_capital_payables_dd_42d_v128_signal": {"inputs": [], "func": f10_retail_working_capital_payables_dd_42d_v128_signal},    "f10_retail_working_capital_revenue_dd_42d_v129_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_dd_42d_v129_signal},    "f10_retail_working_capital_wc_drag_dd_42d_v130_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_dd_42d_v130_signal},    "f10_retail_working_capital_inventory_dd_63d_v131_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_dd_63d_v131_signal},    "f10_retail_working_capital_receivables_dd_63d_v132_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_dd_63d_v132_signal},    "f10_retail_working_capital_payables_dd_63d_v133_signal": {"inputs": [], "func": f10_retail_working_capital_payables_dd_63d_v133_signal},    "f10_retail_working_capital_revenue_dd_63d_v134_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_dd_63d_v134_signal},    "f10_retail_working_capital_wc_drag_dd_63d_v135_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_dd_63d_v135_signal},    "f10_retail_working_capital_inventory_dd_126d_v136_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_dd_126d_v136_signal},    "f10_retail_working_capital_receivables_dd_126d_v137_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_dd_126d_v137_signal},    "f10_retail_working_capital_payables_dd_126d_v138_signal": {"inputs": [], "func": f10_retail_working_capital_payables_dd_126d_v138_signal},    "f10_retail_working_capital_revenue_dd_126d_v139_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_dd_126d_v139_signal},    "f10_retail_working_capital_wc_drag_dd_126d_v140_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_dd_126d_v140_signal},    "f10_retail_working_capital_inventory_dd_252d_v141_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_dd_252d_v141_signal},    "f10_retail_working_capital_receivables_dd_252d_v142_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_dd_252d_v142_signal},    "f10_retail_working_capital_payables_dd_252d_v143_signal": {"inputs": [], "func": f10_retail_working_capital_payables_dd_252d_v143_signal},    "f10_retail_working_capital_revenue_dd_252d_v144_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_dd_252d_v144_signal},    "f10_retail_working_capital_wc_drag_dd_252d_v145_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_dd_252d_v145_signal},    "f10_retail_working_capital_inventory_dd_504d_v146_signal": {"inputs": [], "func": f10_retail_working_capital_inventory_dd_504d_v146_signal},    "f10_retail_working_capital_receivables_dd_504d_v147_signal": {"inputs": [], "func": f10_retail_working_capital_receivables_dd_504d_v147_signal},    "f10_retail_working_capital_payables_dd_504d_v148_signal": {"inputs": [], "func": f10_retail_working_capital_payables_dd_504d_v148_signal},    "f10_retail_working_capital_revenue_dd_504d_v149_signal": {"inputs": [], "func": f10_retail_working_capital_revenue_dd_504d_v149_signal},    "f10_retail_working_capital_wc_drag_dd_504d_v150_signal": {"inputs": [], "func": f10_retail_working_capital_wc_drag_dd_504d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
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
            if res.dropna().empty: raise ValueError("All NaNs produced")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
