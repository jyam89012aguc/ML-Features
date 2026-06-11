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

def f22_cost_pass_through_inflation_shield_z_504d_v076_signal(grossmargin, cor):
    """Z-score for relative outlier detection of Gross margin relative to input cost load over 504d window."""
    res = _z(grossmargin / cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_z_756d_v077_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 756d window."""
    res = _z(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_z_756d_v078_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 756d window."""
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_z_756d_v079_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_z_756d_v080_signal(grossmargin, cor):
    """Z-score for relative outlier detection of Gross margin relative to input cost load over 756d window."""
    res = _z(grossmargin / cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_z_1008d_v081_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 1008d window."""
    res = _z(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_z_1008d_v082_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1008d window."""
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_z_1008d_v083_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_z_1008d_v084_signal(grossmargin, cor):
    """Z-score for relative outlier detection of Gross margin relative to input cost load over 1008d window."""
    res = _z(grossmargin / cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_z_1260d_v085_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 1260d window."""
    res = _z(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_z_1260d_v086_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1260d window."""
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_z_1260d_v087_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_z_1260d_v088_signal(grossmargin, cor):
    """Z-score for relative outlier detection of Gross margin relative to input cost load over 1260d window."""
    res = _z(grossmargin / cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_5d_v089_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 5d window."""
    res = _drawdown(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_5d_v090_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 5d window."""
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_5d_v091_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_5d_v092_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 5d window."""
    res = _drawdown(grossmargin / cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_10d_v093_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 10d window."""
    res = _drawdown(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_10d_v094_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 10d window."""
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_10d_v095_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_10d_v096_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 10d window."""
    res = _drawdown(grossmargin / cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_21d_v097_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 21d window."""
    res = _drawdown(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_21d_v098_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 21d window."""
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_21d_v099_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_21d_v100_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 21d window."""
    res = _drawdown(grossmargin / cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_42d_v101_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 42d window."""
    res = _drawdown(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_42d_v102_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 42d window."""
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_42d_v103_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_42d_v104_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 42d window."""
    res = _drawdown(grossmargin / cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_63d_v105_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 63d window."""
    res = _drawdown(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_63d_v106_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 63d window."""
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_63d_v107_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_63d_v108_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 63d window."""
    res = _drawdown(grossmargin / cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_126d_v109_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 126d window."""
    res = _drawdown(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_126d_v110_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 126d window."""
    res = _drawdown(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_126d_v111_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 126d window."""
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_126d_v112_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 126d window."""
    res = _drawdown(grossmargin / cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_252d_v113_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 252d window."""
    res = _drawdown(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_252d_v114_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 252d window."""
    res = _drawdown(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_252d_v115_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 252d window."""
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_252d_v116_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 252d window."""
    res = _drawdown(grossmargin / cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_504d_v117_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 504d window."""
    res = _drawdown(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_504d_v118_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 504d window."""
    res = _drawdown(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_504d_v119_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 504d window."""
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_504d_v120_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 504d window."""
    res = _drawdown(grossmargin / cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_756d_v121_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 756d window."""
    res = _drawdown(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_756d_v122_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 756d window."""
    res = _drawdown(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_756d_v123_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 756d window."""
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_756d_v124_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 756d window."""
    res = _drawdown(grossmargin / cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_1008d_v125_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 1008d window."""
    res = _drawdown(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_1008d_v126_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1008d window."""
    res = _drawdown(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_1008d_v127_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1008d window."""
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_1008d_v128_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 1008d window."""
    res = _drawdown(grossmargin / cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_dd_1260d_v129_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 1260d window."""
    res = _drawdown(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_dd_1260d_v130_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1260d window."""
    res = _drawdown(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_dd_1260d_v131_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1260d window."""
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_dd_1260d_v132_signal(grossmargin, cor):
    """Drawdown from peak to identify cycle troughs of Gross margin relative to input cost load over 1260d window."""
    res = _drawdown(grossmargin / cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_rec_5d_v133_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 5d window."""
    res = _recovery(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_rec_5d_v134_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 5d window."""
    res = _recovery(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_rec_5d_v135_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 5d window."""
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_rec_5d_v136_signal(grossmargin, cor):
    """Recovery from trough for turnaround signals of Gross margin relative to input cost load over 5d window."""
    res = _recovery(grossmargin / cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_rec_10d_v137_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 10d window."""
    res = _recovery(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_rec_10d_v138_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 10d window."""
    res = _recovery(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_rec_10d_v139_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 10d window."""
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_rec_10d_v140_signal(grossmargin, cor):
    """Recovery from trough for turnaround signals of Gross margin relative to input cost load over 10d window."""
    res = _recovery(grossmargin / cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_rec_21d_v141_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 21d window."""
    res = _recovery(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_rec_21d_v142_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 21d window."""
    res = _recovery(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_rec_21d_v143_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 21d window."""
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_rec_21d_v144_signal(grossmargin, cor):
    """Recovery from trough for turnaround signals of Gross margin relative to input cost load over 21d window."""
    res = _recovery(grossmargin / cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_rec_42d_v145_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 42d window."""
    res = _recovery(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_rec_42d_v146_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 42d window."""
    res = _recovery(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_revenue_rec_42d_v147_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 42d window."""
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_inflation_shield_rec_42d_v148_signal(grossmargin, cor):
    """Recovery from trough for turnaround signals of Gross margin relative to input cost load over 42d window."""
    res = _recovery(grossmargin / cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_cor_rec_63d_v149_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 63d window."""
    res = _recovery(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22_cost_pass_through_grossmargin_rec_63d_v150_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 63d window."""
    res = _recovery(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f22_cost_pass_through_inflation_shield_z_504d_v076_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_z_504d_v076_signal},    "f22_cost_pass_through_cor_z_756d_v077_signal": {"inputs": [], "func": f22_cost_pass_through_cor_z_756d_v077_signal},    "f22_cost_pass_through_grossmargin_z_756d_v078_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_z_756d_v078_signal},    "f22_cost_pass_through_revenue_z_756d_v079_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_z_756d_v079_signal},    "f22_cost_pass_through_inflation_shield_z_756d_v080_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_z_756d_v080_signal},    "f22_cost_pass_through_cor_z_1008d_v081_signal": {"inputs": [], "func": f22_cost_pass_through_cor_z_1008d_v081_signal},    "f22_cost_pass_through_grossmargin_z_1008d_v082_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_z_1008d_v082_signal},    "f22_cost_pass_through_revenue_z_1008d_v083_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_z_1008d_v083_signal},    "f22_cost_pass_through_inflation_shield_z_1008d_v084_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_z_1008d_v084_signal},    "f22_cost_pass_through_cor_z_1260d_v085_signal": {"inputs": [], "func": f22_cost_pass_through_cor_z_1260d_v085_signal},    "f22_cost_pass_through_grossmargin_z_1260d_v086_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_z_1260d_v086_signal},    "f22_cost_pass_through_revenue_z_1260d_v087_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_z_1260d_v087_signal},    "f22_cost_pass_through_inflation_shield_z_1260d_v088_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_z_1260d_v088_signal},    "f22_cost_pass_through_cor_dd_5d_v089_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_5d_v089_signal},    "f22_cost_pass_through_grossmargin_dd_5d_v090_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_5d_v090_signal},    "f22_cost_pass_through_revenue_dd_5d_v091_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_5d_v091_signal},    "f22_cost_pass_through_inflation_shield_dd_5d_v092_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_5d_v092_signal},    "f22_cost_pass_through_cor_dd_10d_v093_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_10d_v093_signal},    "f22_cost_pass_through_grossmargin_dd_10d_v094_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_10d_v094_signal},    "f22_cost_pass_through_revenue_dd_10d_v095_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_10d_v095_signal},    "f22_cost_pass_through_inflation_shield_dd_10d_v096_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_10d_v096_signal},    "f22_cost_pass_through_cor_dd_21d_v097_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_21d_v097_signal},    "f22_cost_pass_through_grossmargin_dd_21d_v098_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_21d_v098_signal},    "f22_cost_pass_through_revenue_dd_21d_v099_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_21d_v099_signal},    "f22_cost_pass_through_inflation_shield_dd_21d_v100_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_21d_v100_signal},    "f22_cost_pass_through_cor_dd_42d_v101_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_42d_v101_signal},    "f22_cost_pass_through_grossmargin_dd_42d_v102_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_42d_v102_signal},    "f22_cost_pass_through_revenue_dd_42d_v103_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_42d_v103_signal},    "f22_cost_pass_through_inflation_shield_dd_42d_v104_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_42d_v104_signal},    "f22_cost_pass_through_cor_dd_63d_v105_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_63d_v105_signal},    "f22_cost_pass_through_grossmargin_dd_63d_v106_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_63d_v106_signal},    "f22_cost_pass_through_revenue_dd_63d_v107_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_63d_v107_signal},    "f22_cost_pass_through_inflation_shield_dd_63d_v108_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_63d_v108_signal},    "f22_cost_pass_through_cor_dd_126d_v109_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_126d_v109_signal},    "f22_cost_pass_through_grossmargin_dd_126d_v110_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_126d_v110_signal},    "f22_cost_pass_through_revenue_dd_126d_v111_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_126d_v111_signal},    "f22_cost_pass_through_inflation_shield_dd_126d_v112_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_126d_v112_signal},    "f22_cost_pass_through_cor_dd_252d_v113_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_252d_v113_signal},    "f22_cost_pass_through_grossmargin_dd_252d_v114_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_252d_v114_signal},    "f22_cost_pass_through_revenue_dd_252d_v115_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_252d_v115_signal},    "f22_cost_pass_through_inflation_shield_dd_252d_v116_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_252d_v116_signal},    "f22_cost_pass_through_cor_dd_504d_v117_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_504d_v117_signal},    "f22_cost_pass_through_grossmargin_dd_504d_v118_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_504d_v118_signal},    "f22_cost_pass_through_revenue_dd_504d_v119_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_504d_v119_signal},    "f22_cost_pass_through_inflation_shield_dd_504d_v120_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_504d_v120_signal},    "f22_cost_pass_through_cor_dd_756d_v121_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_756d_v121_signal},    "f22_cost_pass_through_grossmargin_dd_756d_v122_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_756d_v122_signal},    "f22_cost_pass_through_revenue_dd_756d_v123_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_756d_v123_signal},    "f22_cost_pass_through_inflation_shield_dd_756d_v124_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_756d_v124_signal},    "f22_cost_pass_through_cor_dd_1008d_v125_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_1008d_v125_signal},    "f22_cost_pass_through_grossmargin_dd_1008d_v126_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_1008d_v126_signal},    "f22_cost_pass_through_revenue_dd_1008d_v127_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_1008d_v127_signal},    "f22_cost_pass_through_inflation_shield_dd_1008d_v128_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_1008d_v128_signal},    "f22_cost_pass_through_cor_dd_1260d_v129_signal": {"inputs": [], "func": f22_cost_pass_through_cor_dd_1260d_v129_signal},    "f22_cost_pass_through_grossmargin_dd_1260d_v130_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_dd_1260d_v130_signal},    "f22_cost_pass_through_revenue_dd_1260d_v131_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_dd_1260d_v131_signal},    "f22_cost_pass_through_inflation_shield_dd_1260d_v132_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_dd_1260d_v132_signal},    "f22_cost_pass_through_cor_rec_5d_v133_signal": {"inputs": [], "func": f22_cost_pass_through_cor_rec_5d_v133_signal},    "f22_cost_pass_through_grossmargin_rec_5d_v134_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_rec_5d_v134_signal},    "f22_cost_pass_through_revenue_rec_5d_v135_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_rec_5d_v135_signal},    "f22_cost_pass_through_inflation_shield_rec_5d_v136_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_rec_5d_v136_signal},    "f22_cost_pass_through_cor_rec_10d_v137_signal": {"inputs": [], "func": f22_cost_pass_through_cor_rec_10d_v137_signal},    "f22_cost_pass_through_grossmargin_rec_10d_v138_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_rec_10d_v138_signal},    "f22_cost_pass_through_revenue_rec_10d_v139_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_rec_10d_v139_signal},    "f22_cost_pass_through_inflation_shield_rec_10d_v140_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_rec_10d_v140_signal},    "f22_cost_pass_through_cor_rec_21d_v141_signal": {"inputs": [], "func": f22_cost_pass_through_cor_rec_21d_v141_signal},    "f22_cost_pass_through_grossmargin_rec_21d_v142_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_rec_21d_v142_signal},    "f22_cost_pass_through_revenue_rec_21d_v143_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_rec_21d_v143_signal},    "f22_cost_pass_through_inflation_shield_rec_21d_v144_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_rec_21d_v144_signal},    "f22_cost_pass_through_cor_rec_42d_v145_signal": {"inputs": [], "func": f22_cost_pass_through_cor_rec_42d_v145_signal},    "f22_cost_pass_through_grossmargin_rec_42d_v146_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_rec_42d_v146_signal},    "f22_cost_pass_through_revenue_rec_42d_v147_signal": {"inputs": [], "func": f22_cost_pass_through_revenue_rec_42d_v147_signal},    "f22_cost_pass_through_inflation_shield_rec_42d_v148_signal": {"inputs": [], "func": f22_cost_pass_through_inflation_shield_rec_42d_v148_signal},    "f22_cost_pass_through_cor_rec_63d_v149_signal": {"inputs": [], "func": f22_cost_pass_through_cor_rec_63d_v149_signal},    "f22_cost_pass_through_grossmargin_rec_63d_v150_signal": {"inputs": [], "func": f22_cost_pass_through_grossmargin_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 22...")
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
