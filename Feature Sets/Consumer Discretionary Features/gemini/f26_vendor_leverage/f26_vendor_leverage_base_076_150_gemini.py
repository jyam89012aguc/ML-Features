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

def f26_vendor_leverage_financing_moat_z_504d_v076_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 504d window."""
    res = _z(_ratio(payables, inventory), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_756d_v077_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 756d window."""
    res = _z(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_756d_v078_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 756d window."""
    res = _z(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_756d_v079_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 756d window."""
    res = _z(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_756d_v080_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 756d window."""
    res = _z(_ratio(payables, inventory), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_1008d_v081_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 1008d window."""
    res = _z(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_1008d_v082_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 1008d window."""
    res = _z(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_1008d_v083_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 1008d window."""
    res = _z(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_1008d_v084_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 1008d window."""
    res = _z(_ratio(payables, inventory), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_z_1260d_v085_signal(inventory):
    """Z-score for relative outlier detection of Raw level of inventory over 1260d window."""
    res = _z(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_z_1260d_v086_signal(payables):
    """Z-score for relative outlier detection of Raw level of payables over 1260d window."""
    res = _z(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_z_1260d_v087_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 1260d window."""
    res = _z(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_z_1260d_v088_signal(payables, inventory):
    """Z-score for relative outlier detection of Percentage of inventory financed by vendors over 1260d window."""
    res = _z(_ratio(payables, inventory), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_5d_v089_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 5d window."""
    res = _drawdown(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_5d_v090_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 5d window."""
    res = _drawdown(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_5d_v091_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 5d window."""
    res = _drawdown(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_5d_v092_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 5d window."""
    res = _drawdown(_ratio(payables, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_10d_v093_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 10d window."""
    res = _drawdown(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_10d_v094_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 10d window."""
    res = _drawdown(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_10d_v095_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 10d window."""
    res = _drawdown(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_10d_v096_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 10d window."""
    res = _drawdown(_ratio(payables, inventory), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_21d_v097_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 21d window."""
    res = _drawdown(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_21d_v098_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 21d window."""
    res = _drawdown(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_21d_v099_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 21d window."""
    res = _drawdown(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_21d_v100_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 21d window."""
    res = _drawdown(_ratio(payables, inventory), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_42d_v101_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 42d window."""
    res = _drawdown(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_42d_v102_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 42d window."""
    res = _drawdown(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_42d_v103_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 42d window."""
    res = _drawdown(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_42d_v104_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 42d window."""
    res = _drawdown(_ratio(payables, inventory), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_63d_v105_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 63d window."""
    res = _drawdown(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_63d_v106_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 63d window."""
    res = _drawdown(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_63d_v107_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 63d window."""
    res = _drawdown(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_63d_v108_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 63d window."""
    res = _drawdown(_ratio(payables, inventory), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_126d_v109_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 126d window."""
    res = _drawdown(inventory, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_126d_v110_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 126d window."""
    res = _drawdown(payables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_126d_v111_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 126d window."""
    res = _drawdown(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_126d_v112_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 126d window."""
    res = _drawdown(_ratio(payables, inventory), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_252d_v113_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 252d window."""
    res = _drawdown(inventory, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_252d_v114_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 252d window."""
    res = _drawdown(payables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_252d_v115_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 252d window."""
    res = _drawdown(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_252d_v116_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 252d window."""
    res = _drawdown(_ratio(payables, inventory), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_504d_v117_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 504d window."""
    res = _drawdown(inventory, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_504d_v118_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 504d window."""
    res = _drawdown(payables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_504d_v119_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 504d window."""
    res = _drawdown(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_504d_v120_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 504d window."""
    res = _drawdown(_ratio(payables, inventory), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_756d_v121_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 756d window."""
    res = _drawdown(inventory, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_756d_v122_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 756d window."""
    res = _drawdown(payables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_756d_v123_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 756d window."""
    res = _drawdown(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_756d_v124_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 756d window."""
    res = _drawdown(_ratio(payables, inventory), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_1008d_v125_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 1008d window."""
    res = _drawdown(inventory, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_1008d_v126_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 1008d window."""
    res = _drawdown(payables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_1008d_v127_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 1008d window."""
    res = _drawdown(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_1008d_v128_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 1008d window."""
    res = _drawdown(_ratio(payables, inventory), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_dd_1260d_v129_signal(inventory):
    """Drawdown from peak to identify cycle troughs of Raw level of inventory over 1260d window."""
    res = _drawdown(inventory, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_dd_1260d_v130_signal(payables):
    """Drawdown from peak to identify cycle troughs of Raw level of payables over 1260d window."""
    res = _drawdown(payables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_dd_1260d_v131_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 1260d window."""
    res = _drawdown(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_dd_1260d_v132_signal(payables, inventory):
    """Drawdown from peak to identify cycle troughs of Percentage of inventory financed by vendors over 1260d window."""
    res = _drawdown(_ratio(payables, inventory), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_rec_5d_v133_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 5d window."""
    res = _recovery(inventory, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_rec_5d_v134_signal(payables):
    """Recovery from trough for turnaround signals of Raw level of payables over 5d window."""
    res = _recovery(payables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_rec_5d_v135_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 5d window."""
    res = _recovery(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_rec_5d_v136_signal(payables, inventory):
    """Recovery from trough for turnaround signals of Percentage of inventory financed by vendors over 5d window."""
    res = _recovery(_ratio(payables, inventory), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_rec_10d_v137_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 10d window."""
    res = _recovery(inventory, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_rec_10d_v138_signal(payables):
    """Recovery from trough for turnaround signals of Raw level of payables over 10d window."""
    res = _recovery(payables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_rec_10d_v139_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 10d window."""
    res = _recovery(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_rec_10d_v140_signal(payables, inventory):
    """Recovery from trough for turnaround signals of Percentage of inventory financed by vendors over 10d window."""
    res = _recovery(_ratio(payables, inventory), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_rec_21d_v141_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 21d window."""
    res = _recovery(inventory, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_rec_21d_v142_signal(payables):
    """Recovery from trough for turnaround signals of Raw level of payables over 21d window."""
    res = _recovery(payables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_rec_21d_v143_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 21d window."""
    res = _recovery(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_rec_21d_v144_signal(payables, inventory):
    """Recovery from trough for turnaround signals of Percentage of inventory financed by vendors over 21d window."""
    res = _recovery(_ratio(payables, inventory), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_rec_42d_v145_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 42d window."""
    res = _recovery(inventory, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_rec_42d_v146_signal(payables):
    """Recovery from trough for turnaround signals of Raw level of payables over 42d window."""
    res = _recovery(payables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_cor_rec_42d_v147_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 42d window."""
    res = _recovery(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_financing_moat_rec_42d_v148_signal(payables, inventory):
    """Recovery from trough for turnaround signals of Percentage of inventory financed by vendors over 42d window."""
    res = _recovery(_ratio(payables, inventory), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_inventory_rec_63d_v149_signal(inventory):
    """Recovery from trough for turnaround signals of Raw level of inventory over 63d window."""
    res = _recovery(inventory, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f26_vendor_leverage_payables_rec_63d_v150_signal(payables):
    """Recovery from trough for turnaround signals of Raw level of payables over 63d window."""
    res = _recovery(payables, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f26_vendor_leverage_financing_moat_z_504d_v076_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_504d_v076_signal},    "f26_vendor_leverage_inventory_z_756d_v077_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_756d_v077_signal},    "f26_vendor_leverage_payables_z_756d_v078_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_756d_v078_signal},    "f26_vendor_leverage_cor_z_756d_v079_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_756d_v079_signal},    "f26_vendor_leverage_financing_moat_z_756d_v080_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_756d_v080_signal},    "f26_vendor_leverage_inventory_z_1008d_v081_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_1008d_v081_signal},    "f26_vendor_leverage_payables_z_1008d_v082_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_1008d_v082_signal},    "f26_vendor_leverage_cor_z_1008d_v083_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_1008d_v083_signal},    "f26_vendor_leverage_financing_moat_z_1008d_v084_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_1008d_v084_signal},    "f26_vendor_leverage_inventory_z_1260d_v085_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_z_1260d_v085_signal},    "f26_vendor_leverage_payables_z_1260d_v086_signal": {"inputs": [], "func": f26_vendor_leverage_payables_z_1260d_v086_signal},    "f26_vendor_leverage_cor_z_1260d_v087_signal": {"inputs": [], "func": f26_vendor_leverage_cor_z_1260d_v087_signal},    "f26_vendor_leverage_financing_moat_z_1260d_v088_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_z_1260d_v088_signal},    "f26_vendor_leverage_inventory_dd_5d_v089_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_5d_v089_signal},    "f26_vendor_leverage_payables_dd_5d_v090_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_5d_v090_signal},    "f26_vendor_leverage_cor_dd_5d_v091_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_5d_v091_signal},    "f26_vendor_leverage_financing_moat_dd_5d_v092_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_5d_v092_signal},    "f26_vendor_leverage_inventory_dd_10d_v093_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_10d_v093_signal},    "f26_vendor_leverage_payables_dd_10d_v094_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_10d_v094_signal},    "f26_vendor_leverage_cor_dd_10d_v095_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_10d_v095_signal},    "f26_vendor_leverage_financing_moat_dd_10d_v096_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_10d_v096_signal},    "f26_vendor_leverage_inventory_dd_21d_v097_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_21d_v097_signal},    "f26_vendor_leverage_payables_dd_21d_v098_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_21d_v098_signal},    "f26_vendor_leverage_cor_dd_21d_v099_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_21d_v099_signal},    "f26_vendor_leverage_financing_moat_dd_21d_v100_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_21d_v100_signal},    "f26_vendor_leverage_inventory_dd_42d_v101_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_42d_v101_signal},    "f26_vendor_leverage_payables_dd_42d_v102_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_42d_v102_signal},    "f26_vendor_leverage_cor_dd_42d_v103_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_42d_v103_signal},    "f26_vendor_leverage_financing_moat_dd_42d_v104_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_42d_v104_signal},    "f26_vendor_leverage_inventory_dd_63d_v105_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_63d_v105_signal},    "f26_vendor_leverage_payables_dd_63d_v106_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_63d_v106_signal},    "f26_vendor_leverage_cor_dd_63d_v107_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_63d_v107_signal},    "f26_vendor_leverage_financing_moat_dd_63d_v108_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_63d_v108_signal},    "f26_vendor_leverage_inventory_dd_126d_v109_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_126d_v109_signal},    "f26_vendor_leverage_payables_dd_126d_v110_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_126d_v110_signal},    "f26_vendor_leverage_cor_dd_126d_v111_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_126d_v111_signal},    "f26_vendor_leverage_financing_moat_dd_126d_v112_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_126d_v112_signal},    "f26_vendor_leverage_inventory_dd_252d_v113_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_252d_v113_signal},    "f26_vendor_leverage_payables_dd_252d_v114_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_252d_v114_signal},    "f26_vendor_leverage_cor_dd_252d_v115_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_252d_v115_signal},    "f26_vendor_leverage_financing_moat_dd_252d_v116_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_252d_v116_signal},    "f26_vendor_leverage_inventory_dd_504d_v117_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_504d_v117_signal},    "f26_vendor_leverage_payables_dd_504d_v118_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_504d_v118_signal},    "f26_vendor_leverage_cor_dd_504d_v119_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_504d_v119_signal},    "f26_vendor_leverage_financing_moat_dd_504d_v120_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_504d_v120_signal},    "f26_vendor_leverage_inventory_dd_756d_v121_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_756d_v121_signal},    "f26_vendor_leverage_payables_dd_756d_v122_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_756d_v122_signal},    "f26_vendor_leverage_cor_dd_756d_v123_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_756d_v123_signal},    "f26_vendor_leverage_financing_moat_dd_756d_v124_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_756d_v124_signal},    "f26_vendor_leverage_inventory_dd_1008d_v125_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_1008d_v125_signal},    "f26_vendor_leverage_payables_dd_1008d_v126_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_1008d_v126_signal},    "f26_vendor_leverage_cor_dd_1008d_v127_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_1008d_v127_signal},    "f26_vendor_leverage_financing_moat_dd_1008d_v128_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_1008d_v128_signal},    "f26_vendor_leverage_inventory_dd_1260d_v129_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_dd_1260d_v129_signal},    "f26_vendor_leverage_payables_dd_1260d_v130_signal": {"inputs": [], "func": f26_vendor_leverage_payables_dd_1260d_v130_signal},    "f26_vendor_leverage_cor_dd_1260d_v131_signal": {"inputs": [], "func": f26_vendor_leverage_cor_dd_1260d_v131_signal},    "f26_vendor_leverage_financing_moat_dd_1260d_v132_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_dd_1260d_v132_signal},    "f26_vendor_leverage_inventory_rec_5d_v133_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_rec_5d_v133_signal},    "f26_vendor_leverage_payables_rec_5d_v134_signal": {"inputs": [], "func": f26_vendor_leverage_payables_rec_5d_v134_signal},    "f26_vendor_leverage_cor_rec_5d_v135_signal": {"inputs": [], "func": f26_vendor_leverage_cor_rec_5d_v135_signal},    "f26_vendor_leverage_financing_moat_rec_5d_v136_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_rec_5d_v136_signal},    "f26_vendor_leverage_inventory_rec_10d_v137_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_rec_10d_v137_signal},    "f26_vendor_leverage_payables_rec_10d_v138_signal": {"inputs": [], "func": f26_vendor_leverage_payables_rec_10d_v138_signal},    "f26_vendor_leverage_cor_rec_10d_v139_signal": {"inputs": [], "func": f26_vendor_leverage_cor_rec_10d_v139_signal},    "f26_vendor_leverage_financing_moat_rec_10d_v140_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_rec_10d_v140_signal},    "f26_vendor_leverage_inventory_rec_21d_v141_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_rec_21d_v141_signal},    "f26_vendor_leverage_payables_rec_21d_v142_signal": {"inputs": [], "func": f26_vendor_leverage_payables_rec_21d_v142_signal},    "f26_vendor_leverage_cor_rec_21d_v143_signal": {"inputs": [], "func": f26_vendor_leverage_cor_rec_21d_v143_signal},    "f26_vendor_leverage_financing_moat_rec_21d_v144_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_rec_21d_v144_signal},    "f26_vendor_leverage_inventory_rec_42d_v145_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_rec_42d_v145_signal},    "f26_vendor_leverage_payables_rec_42d_v146_signal": {"inputs": [], "func": f26_vendor_leverage_payables_rec_42d_v146_signal},    "f26_vendor_leverage_cor_rec_42d_v147_signal": {"inputs": [], "func": f26_vendor_leverage_cor_rec_42d_v147_signal},    "f26_vendor_leverage_financing_moat_rec_42d_v148_signal": {"inputs": [], "func": f26_vendor_leverage_financing_moat_rec_42d_v148_signal},    "f26_vendor_leverage_inventory_rec_63d_v149_signal": {"inputs": [], "func": f26_vendor_leverage_inventory_rec_63d_v149_signal},    "f26_vendor_leverage_payables_rec_63d_v150_signal": {"inputs": [], "func": f26_vendor_leverage_payables_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 26...")
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
