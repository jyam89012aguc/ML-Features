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

def f39_working_cap_liquidity_liquidity_index_z_504d_v076_signal(cashneq, liabilitiesc):
    """Z-score for relative outlier detection of Current liquidity coverage of short-term liabilities over 504d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_z_756d_v077_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 756d window."""
    res = _z(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_z_756d_v078_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 756d window."""
    res = _z(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_z_756d_v079_signal(liabilitiesc):
    """Z-score for relative outlier detection of Raw level of liabilitiesc over 756d window."""
    res = _z(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_z_756d_v080_signal(cashneq, liabilitiesc):
    """Z-score for relative outlier detection of Current liquidity coverage of short-term liabilities over 756d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_z_1008d_v081_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 1008d window."""
    res = _z(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_z_1008d_v082_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 1008d window."""
    res = _z(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_z_1008d_v083_signal(liabilitiesc):
    """Z-score for relative outlier detection of Raw level of liabilitiesc over 1008d window."""
    res = _z(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_z_1008d_v084_signal(cashneq, liabilitiesc):
    """Z-score for relative outlier detection of Current liquidity coverage of short-term liabilities over 1008d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_z_1260d_v085_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 1260d window."""
    res = _z(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_z_1260d_v086_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 1260d window."""
    res = _z(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_z_1260d_v087_signal(liabilitiesc):
    """Z-score for relative outlier detection of Raw level of liabilitiesc over 1260d window."""
    res = _z(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_z_1260d_v088_signal(cashneq, liabilitiesc):
    """Z-score for relative outlier detection of Current liquidity coverage of short-term liabilities over 1260d window."""
    res = _z(_ratio(cashneq, liabilitiesc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_5d_v089_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 5d window."""
    res = _drawdown(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_5d_v090_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 5d window."""
    res = _drawdown(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_5d_v091_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 5d window."""
    res = _drawdown(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_5d_v092_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 5d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_10d_v093_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 10d window."""
    res = _drawdown(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_10d_v094_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 10d window."""
    res = _drawdown(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_10d_v095_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 10d window."""
    res = _drawdown(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_10d_v096_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 10d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_21d_v097_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 21d window."""
    res = _drawdown(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_21d_v098_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 21d window."""
    res = _drawdown(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_21d_v099_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 21d window."""
    res = _drawdown(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_21d_v100_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 21d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_42d_v101_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 42d window."""
    res = _drawdown(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_42d_v102_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 42d window."""
    res = _drawdown(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_42d_v103_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 42d window."""
    res = _drawdown(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_42d_v104_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 42d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_63d_v105_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 63d window."""
    res = _drawdown(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_63d_v106_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 63d window."""
    res = _drawdown(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_63d_v107_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 63d window."""
    res = _drawdown(liabilitiesc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_63d_v108_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 63d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_126d_v109_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 126d window."""
    res = _drawdown(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_126d_v110_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 126d window."""
    res = _drawdown(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_126d_v111_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 126d window."""
    res = _drawdown(liabilitiesc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_126d_v112_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 126d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_252d_v113_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 252d window."""
    res = _drawdown(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_252d_v114_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 252d window."""
    res = _drawdown(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_252d_v115_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 252d window."""
    res = _drawdown(liabilitiesc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_252d_v116_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 252d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_504d_v117_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 504d window."""
    res = _drawdown(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_504d_v118_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 504d window."""
    res = _drawdown(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_504d_v119_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 504d window."""
    res = _drawdown(liabilitiesc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_504d_v120_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 504d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_756d_v121_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 756d window."""
    res = _drawdown(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_756d_v122_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 756d window."""
    res = _drawdown(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_756d_v123_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 756d window."""
    res = _drawdown(liabilitiesc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_756d_v124_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 756d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_1008d_v125_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 1008d window."""
    res = _drawdown(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_1008d_v126_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 1008d window."""
    res = _drawdown(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_1008d_v127_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 1008d window."""
    res = _drawdown(liabilitiesc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_1008d_v128_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 1008d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_dd_1260d_v129_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 1260d window."""
    res = _drawdown(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_dd_1260d_v130_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 1260d window."""
    res = _drawdown(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_dd_1260d_v131_signal(liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Raw level of liabilitiesc over 1260d window."""
    res = _drawdown(liabilitiesc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_dd_1260d_v132_signal(cashneq, liabilitiesc):
    """Drawdown from peak to identify cycle troughs of Current liquidity coverage of short-term liabilities over 1260d window."""
    res = _drawdown(_ratio(cashneq, liabilitiesc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_rec_5d_v133_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 5d window."""
    res = _recovery(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_rec_5d_v134_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 5d window."""
    res = _recovery(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_rec_5d_v135_signal(liabilitiesc):
    """Recovery from trough for turnaround signals of Raw level of liabilitiesc over 5d window."""
    res = _recovery(liabilitiesc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_rec_5d_v136_signal(cashneq, liabilitiesc):
    """Recovery from trough for turnaround signals of Current liquidity coverage of short-term liabilities over 5d window."""
    res = _recovery(_ratio(cashneq, liabilitiesc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_rec_10d_v137_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 10d window."""
    res = _recovery(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_rec_10d_v138_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 10d window."""
    res = _recovery(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_rec_10d_v139_signal(liabilitiesc):
    """Recovery from trough for turnaround signals of Raw level of liabilitiesc over 10d window."""
    res = _recovery(liabilitiesc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_rec_10d_v140_signal(cashneq, liabilitiesc):
    """Recovery from trough for turnaround signals of Current liquidity coverage of short-term liabilities over 10d window."""
    res = _recovery(_ratio(cashneq, liabilitiesc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_rec_21d_v141_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 21d window."""
    res = _recovery(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_rec_21d_v142_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 21d window."""
    res = _recovery(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_rec_21d_v143_signal(liabilitiesc):
    """Recovery from trough for turnaround signals of Raw level of liabilitiesc over 21d window."""
    res = _recovery(liabilitiesc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_rec_21d_v144_signal(cashneq, liabilitiesc):
    """Recovery from trough for turnaround signals of Current liquidity coverage of short-term liabilities over 21d window."""
    res = _recovery(_ratio(cashneq, liabilitiesc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_rec_42d_v145_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 42d window."""
    res = _recovery(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_rec_42d_v146_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 42d window."""
    res = _recovery(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liabilitiesc_rec_42d_v147_signal(liabilitiesc):
    """Recovery from trough for turnaround signals of Raw level of liabilitiesc over 42d window."""
    res = _recovery(liabilitiesc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_liquidity_index_rec_42d_v148_signal(cashneq, liabilitiesc):
    """Recovery from trough for turnaround signals of Current liquidity coverage of short-term liabilities over 42d window."""
    res = _recovery(_ratio(cashneq, liabilitiesc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_inventory_rec_63d_v149_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 63d window."""
    res = _recovery(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f39_working_cap_liquidity_cashneq_rec_63d_v150_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 63d window."""
    res = _recovery(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f39_working_cap_liquidity_liquidity_index_z_504d_v076_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_z_504d_v076_signal},    "f39_working_cap_liquidity_inventory_z_756d_v077_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_z_756d_v077_signal},    "f39_working_cap_liquidity_cashneq_z_756d_v078_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_z_756d_v078_signal},    "f39_working_cap_liquidity_liabilitiesc_z_756d_v079_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_z_756d_v079_signal},    "f39_working_cap_liquidity_liquidity_index_z_756d_v080_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_z_756d_v080_signal},    "f39_working_cap_liquidity_inventory_z_1008d_v081_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_z_1008d_v081_signal},    "f39_working_cap_liquidity_cashneq_z_1008d_v082_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_z_1008d_v082_signal},    "f39_working_cap_liquidity_liabilitiesc_z_1008d_v083_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_z_1008d_v083_signal},    "f39_working_cap_liquidity_liquidity_index_z_1008d_v084_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_z_1008d_v084_signal},    "f39_working_cap_liquidity_inventory_z_1260d_v085_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_z_1260d_v085_signal},    "f39_working_cap_liquidity_cashneq_z_1260d_v086_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_z_1260d_v086_signal},    "f39_working_cap_liquidity_liabilitiesc_z_1260d_v087_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_z_1260d_v087_signal},    "f39_working_cap_liquidity_liquidity_index_z_1260d_v088_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_z_1260d_v088_signal},    "f39_working_cap_liquidity_inventory_dd_5d_v089_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_5d_v089_signal},    "f39_working_cap_liquidity_cashneq_dd_5d_v090_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_5d_v090_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_5d_v091_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_5d_v091_signal},    "f39_working_cap_liquidity_liquidity_index_dd_5d_v092_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_5d_v092_signal},    "f39_working_cap_liquidity_inventory_dd_10d_v093_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_10d_v093_signal},    "f39_working_cap_liquidity_cashneq_dd_10d_v094_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_10d_v094_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_10d_v095_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_10d_v095_signal},    "f39_working_cap_liquidity_liquidity_index_dd_10d_v096_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_10d_v096_signal},    "f39_working_cap_liquidity_inventory_dd_21d_v097_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_21d_v097_signal},    "f39_working_cap_liquidity_cashneq_dd_21d_v098_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_21d_v098_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_21d_v099_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_21d_v099_signal},    "f39_working_cap_liquidity_liquidity_index_dd_21d_v100_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_21d_v100_signal},    "f39_working_cap_liquidity_inventory_dd_42d_v101_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_42d_v101_signal},    "f39_working_cap_liquidity_cashneq_dd_42d_v102_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_42d_v102_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_42d_v103_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_42d_v103_signal},    "f39_working_cap_liquidity_liquidity_index_dd_42d_v104_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_42d_v104_signal},    "f39_working_cap_liquidity_inventory_dd_63d_v105_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_63d_v105_signal},    "f39_working_cap_liquidity_cashneq_dd_63d_v106_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_63d_v106_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_63d_v107_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_63d_v107_signal},    "f39_working_cap_liquidity_liquidity_index_dd_63d_v108_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_63d_v108_signal},    "f39_working_cap_liquidity_inventory_dd_126d_v109_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_126d_v109_signal},    "f39_working_cap_liquidity_cashneq_dd_126d_v110_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_126d_v110_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_126d_v111_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_126d_v111_signal},    "f39_working_cap_liquidity_liquidity_index_dd_126d_v112_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_126d_v112_signal},    "f39_working_cap_liquidity_inventory_dd_252d_v113_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_252d_v113_signal},    "f39_working_cap_liquidity_cashneq_dd_252d_v114_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_252d_v114_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_252d_v115_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_252d_v115_signal},    "f39_working_cap_liquidity_liquidity_index_dd_252d_v116_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_252d_v116_signal},    "f39_working_cap_liquidity_inventory_dd_504d_v117_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_504d_v117_signal},    "f39_working_cap_liquidity_cashneq_dd_504d_v118_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_504d_v118_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_504d_v119_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_504d_v119_signal},    "f39_working_cap_liquidity_liquidity_index_dd_504d_v120_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_504d_v120_signal},    "f39_working_cap_liquidity_inventory_dd_756d_v121_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_756d_v121_signal},    "f39_working_cap_liquidity_cashneq_dd_756d_v122_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_756d_v122_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_756d_v123_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_756d_v123_signal},    "f39_working_cap_liquidity_liquidity_index_dd_756d_v124_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_756d_v124_signal},    "f39_working_cap_liquidity_inventory_dd_1008d_v125_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_1008d_v125_signal},    "f39_working_cap_liquidity_cashneq_dd_1008d_v126_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_1008d_v126_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_1008d_v127_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_1008d_v127_signal},    "f39_working_cap_liquidity_liquidity_index_dd_1008d_v128_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_1008d_v128_signal},    "f39_working_cap_liquidity_inventory_dd_1260d_v129_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_dd_1260d_v129_signal},    "f39_working_cap_liquidity_cashneq_dd_1260d_v130_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_dd_1260d_v130_signal},    "f39_working_cap_liquidity_liabilitiesc_dd_1260d_v131_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_dd_1260d_v131_signal},    "f39_working_cap_liquidity_liquidity_index_dd_1260d_v132_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_dd_1260d_v132_signal},    "f39_working_cap_liquidity_inventory_rec_5d_v133_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_rec_5d_v133_signal},    "f39_working_cap_liquidity_cashneq_rec_5d_v134_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_rec_5d_v134_signal},    "f39_working_cap_liquidity_liabilitiesc_rec_5d_v135_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_rec_5d_v135_signal},    "f39_working_cap_liquidity_liquidity_index_rec_5d_v136_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_rec_5d_v136_signal},    "f39_working_cap_liquidity_inventory_rec_10d_v137_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_rec_10d_v137_signal},    "f39_working_cap_liquidity_cashneq_rec_10d_v138_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_rec_10d_v138_signal},    "f39_working_cap_liquidity_liabilitiesc_rec_10d_v139_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_rec_10d_v139_signal},    "f39_working_cap_liquidity_liquidity_index_rec_10d_v140_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_rec_10d_v140_signal},    "f39_working_cap_liquidity_inventory_rec_21d_v141_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_rec_21d_v141_signal},    "f39_working_cap_liquidity_cashneq_rec_21d_v142_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_rec_21d_v142_signal},    "f39_working_cap_liquidity_liabilitiesc_rec_21d_v143_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_rec_21d_v143_signal},    "f39_working_cap_liquidity_liquidity_index_rec_21d_v144_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_rec_21d_v144_signal},    "f39_working_cap_liquidity_inventory_rec_42d_v145_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_rec_42d_v145_signal},    "f39_working_cap_liquidity_cashneq_rec_42d_v146_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_rec_42d_v146_signal},    "f39_working_cap_liquidity_liabilitiesc_rec_42d_v147_signal": {"inputs": [], "func": f39_working_cap_liquidity_liabilitiesc_rec_42d_v147_signal},    "f39_working_cap_liquidity_liquidity_index_rec_42d_v148_signal": {"inputs": [], "func": f39_working_cap_liquidity_liquidity_index_rec_42d_v148_signal},    "f39_working_cap_liquidity_inventory_rec_63d_v149_signal": {"inputs": [], "func": f39_working_cap_liquidity_inventory_rec_63d_v149_signal},    "f39_working_cap_liquidity_cashneq_rec_63d_v150_signal": {"inputs": [], "func": f39_working_cap_liquidity_cashneq_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 39...")
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
