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

def f50_luxury_moat_index_luxury_score_z_504d_v076_signal(grossmargin, netinc, revenue):
    """Z-score for relative outlier detection of Combined manufacturing and net profitability index over 504d window."""
    res = _z(grossmargin * _ratio(netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_z_756d_v077_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 756d window."""
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_z_756d_v078_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_z_756d_v079_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_z_756d_v080_signal(grossmargin, netinc, revenue):
    """Z-score for relative outlier detection of Combined manufacturing and net profitability index over 756d window."""
    res = _z(grossmargin * _ratio(netinc, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_z_1008d_v081_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1008d window."""
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_z_1008d_v082_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_z_1008d_v083_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_z_1008d_v084_signal(grossmargin, netinc, revenue):
    """Z-score for relative outlier detection of Combined manufacturing and net profitability index over 1008d window."""
    res = _z(grossmargin * _ratio(netinc, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_z_1260d_v085_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1260d window."""
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_z_1260d_v086_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_z_1260d_v087_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_z_1260d_v088_signal(grossmargin, netinc, revenue):
    """Z-score for relative outlier detection of Combined manufacturing and net profitability index over 1260d window."""
    res = _z(grossmargin * _ratio(netinc, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_5d_v089_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 5d window."""
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_5d_v090_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_5d_v091_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_5d_v092_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 5d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_10d_v093_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 10d window."""
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_10d_v094_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_10d_v095_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_10d_v096_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 10d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_21d_v097_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 21d window."""
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_21d_v098_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_21d_v099_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_21d_v100_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 21d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_42d_v101_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 42d window."""
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_42d_v102_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_42d_v103_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_42d_v104_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 42d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_63d_v105_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 63d window."""
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_63d_v106_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_63d_v107_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 63d window."""
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_63d_v108_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 63d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_126d_v109_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 126d window."""
    res = _drawdown(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_126d_v110_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 126d window."""
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_126d_v111_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 126d window."""
    res = _drawdown(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_126d_v112_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 126d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_252d_v113_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 252d window."""
    res = _drawdown(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_252d_v114_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 252d window."""
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_252d_v115_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 252d window."""
    res = _drawdown(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_252d_v116_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 252d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_504d_v117_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 504d window."""
    res = _drawdown(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_504d_v118_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 504d window."""
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_504d_v119_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 504d window."""
    res = _drawdown(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_504d_v120_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 504d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_756d_v121_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 756d window."""
    res = _drawdown(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_756d_v122_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 756d window."""
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_756d_v123_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 756d window."""
    res = _drawdown(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_756d_v124_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 756d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_1008d_v125_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1008d window."""
    res = _drawdown(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_1008d_v126_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1008d window."""
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_1008d_v127_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 1008d window."""
    res = _drawdown(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_1008d_v128_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 1008d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_dd_1260d_v129_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1260d window."""
    res = _drawdown(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_dd_1260d_v130_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1260d window."""
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_dd_1260d_v131_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 1260d window."""
    res = _drawdown(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_dd_1260d_v132_signal(grossmargin, netinc, revenue):
    """Drawdown from peak to identify cycle troughs of Combined manufacturing and net profitability index over 1260d window."""
    res = _drawdown(grossmargin * _ratio(netinc, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_rec_5d_v133_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 5d window."""
    res = _recovery(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_rec_5d_v134_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 5d window."""
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_rec_5d_v135_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 5d window."""
    res = _recovery(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_rec_5d_v136_signal(grossmargin, netinc, revenue):
    """Recovery from trough for turnaround signals of Combined manufacturing and net profitability index over 5d window."""
    res = _recovery(grossmargin * _ratio(netinc, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_rec_10d_v137_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 10d window."""
    res = _recovery(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_rec_10d_v138_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 10d window."""
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_rec_10d_v139_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 10d window."""
    res = _recovery(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_rec_10d_v140_signal(grossmargin, netinc, revenue):
    """Recovery from trough for turnaround signals of Combined manufacturing and net profitability index over 10d window."""
    res = _recovery(grossmargin * _ratio(netinc, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_rec_21d_v141_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 21d window."""
    res = _recovery(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_rec_21d_v142_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 21d window."""
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_rec_21d_v143_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 21d window."""
    res = _recovery(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_rec_21d_v144_signal(grossmargin, netinc, revenue):
    """Recovery from trough for turnaround signals of Combined manufacturing and net profitability index over 21d window."""
    res = _recovery(grossmargin * _ratio(netinc, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_rec_42d_v145_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 42d window."""
    res = _recovery(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_rec_42d_v146_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 42d window."""
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_netinc_rec_42d_v147_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 42d window."""
    res = _recovery(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_luxury_score_rec_42d_v148_signal(grossmargin, netinc, revenue):
    """Recovery from trough for turnaround signals of Combined manufacturing and net profitability index over 42d window."""
    res = _recovery(grossmargin * _ratio(netinc, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_grossmargin_rec_63d_v149_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 63d window."""
    res = _recovery(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f50_luxury_moat_index_revenue_rec_63d_v150_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 63d window."""
    res = _recovery(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f50_luxury_moat_index_luxury_score_z_504d_v076_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_z_504d_v076_signal},    "f50_luxury_moat_index_grossmargin_z_756d_v077_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_z_756d_v077_signal},    "f50_luxury_moat_index_revenue_z_756d_v078_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_z_756d_v078_signal},    "f50_luxury_moat_index_netinc_z_756d_v079_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_z_756d_v079_signal},    "f50_luxury_moat_index_luxury_score_z_756d_v080_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_z_756d_v080_signal},    "f50_luxury_moat_index_grossmargin_z_1008d_v081_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_z_1008d_v081_signal},    "f50_luxury_moat_index_revenue_z_1008d_v082_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_z_1008d_v082_signal},    "f50_luxury_moat_index_netinc_z_1008d_v083_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_z_1008d_v083_signal},    "f50_luxury_moat_index_luxury_score_z_1008d_v084_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_z_1008d_v084_signal},    "f50_luxury_moat_index_grossmargin_z_1260d_v085_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_z_1260d_v085_signal},    "f50_luxury_moat_index_revenue_z_1260d_v086_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_z_1260d_v086_signal},    "f50_luxury_moat_index_netinc_z_1260d_v087_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_z_1260d_v087_signal},    "f50_luxury_moat_index_luxury_score_z_1260d_v088_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_z_1260d_v088_signal},    "f50_luxury_moat_index_grossmargin_dd_5d_v089_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_5d_v089_signal},    "f50_luxury_moat_index_revenue_dd_5d_v090_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_5d_v090_signal},    "f50_luxury_moat_index_netinc_dd_5d_v091_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_5d_v091_signal},    "f50_luxury_moat_index_luxury_score_dd_5d_v092_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_5d_v092_signal},    "f50_luxury_moat_index_grossmargin_dd_10d_v093_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_10d_v093_signal},    "f50_luxury_moat_index_revenue_dd_10d_v094_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_10d_v094_signal},    "f50_luxury_moat_index_netinc_dd_10d_v095_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_10d_v095_signal},    "f50_luxury_moat_index_luxury_score_dd_10d_v096_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_10d_v096_signal},    "f50_luxury_moat_index_grossmargin_dd_21d_v097_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_21d_v097_signal},    "f50_luxury_moat_index_revenue_dd_21d_v098_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_21d_v098_signal},    "f50_luxury_moat_index_netinc_dd_21d_v099_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_21d_v099_signal},    "f50_luxury_moat_index_luxury_score_dd_21d_v100_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_21d_v100_signal},    "f50_luxury_moat_index_grossmargin_dd_42d_v101_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_42d_v101_signal},    "f50_luxury_moat_index_revenue_dd_42d_v102_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_42d_v102_signal},    "f50_luxury_moat_index_netinc_dd_42d_v103_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_42d_v103_signal},    "f50_luxury_moat_index_luxury_score_dd_42d_v104_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_42d_v104_signal},    "f50_luxury_moat_index_grossmargin_dd_63d_v105_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_63d_v105_signal},    "f50_luxury_moat_index_revenue_dd_63d_v106_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_63d_v106_signal},    "f50_luxury_moat_index_netinc_dd_63d_v107_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_63d_v107_signal},    "f50_luxury_moat_index_luxury_score_dd_63d_v108_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_63d_v108_signal},    "f50_luxury_moat_index_grossmargin_dd_126d_v109_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_126d_v109_signal},    "f50_luxury_moat_index_revenue_dd_126d_v110_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_126d_v110_signal},    "f50_luxury_moat_index_netinc_dd_126d_v111_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_126d_v111_signal},    "f50_luxury_moat_index_luxury_score_dd_126d_v112_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_126d_v112_signal},    "f50_luxury_moat_index_grossmargin_dd_252d_v113_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_252d_v113_signal},    "f50_luxury_moat_index_revenue_dd_252d_v114_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_252d_v114_signal},    "f50_luxury_moat_index_netinc_dd_252d_v115_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_252d_v115_signal},    "f50_luxury_moat_index_luxury_score_dd_252d_v116_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_252d_v116_signal},    "f50_luxury_moat_index_grossmargin_dd_504d_v117_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_504d_v117_signal},    "f50_luxury_moat_index_revenue_dd_504d_v118_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_504d_v118_signal},    "f50_luxury_moat_index_netinc_dd_504d_v119_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_504d_v119_signal},    "f50_luxury_moat_index_luxury_score_dd_504d_v120_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_504d_v120_signal},    "f50_luxury_moat_index_grossmargin_dd_756d_v121_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_756d_v121_signal},    "f50_luxury_moat_index_revenue_dd_756d_v122_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_756d_v122_signal},    "f50_luxury_moat_index_netinc_dd_756d_v123_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_756d_v123_signal},    "f50_luxury_moat_index_luxury_score_dd_756d_v124_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_756d_v124_signal},    "f50_luxury_moat_index_grossmargin_dd_1008d_v125_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_1008d_v125_signal},    "f50_luxury_moat_index_revenue_dd_1008d_v126_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_1008d_v126_signal},    "f50_luxury_moat_index_netinc_dd_1008d_v127_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_1008d_v127_signal},    "f50_luxury_moat_index_luxury_score_dd_1008d_v128_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_1008d_v128_signal},    "f50_luxury_moat_index_grossmargin_dd_1260d_v129_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_dd_1260d_v129_signal},    "f50_luxury_moat_index_revenue_dd_1260d_v130_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_dd_1260d_v130_signal},    "f50_luxury_moat_index_netinc_dd_1260d_v131_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_dd_1260d_v131_signal},    "f50_luxury_moat_index_luxury_score_dd_1260d_v132_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_dd_1260d_v132_signal},    "f50_luxury_moat_index_grossmargin_rec_5d_v133_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_rec_5d_v133_signal},    "f50_luxury_moat_index_revenue_rec_5d_v134_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_rec_5d_v134_signal},    "f50_luxury_moat_index_netinc_rec_5d_v135_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_rec_5d_v135_signal},    "f50_luxury_moat_index_luxury_score_rec_5d_v136_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_rec_5d_v136_signal},    "f50_luxury_moat_index_grossmargin_rec_10d_v137_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_rec_10d_v137_signal},    "f50_luxury_moat_index_revenue_rec_10d_v138_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_rec_10d_v138_signal},    "f50_luxury_moat_index_netinc_rec_10d_v139_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_rec_10d_v139_signal},    "f50_luxury_moat_index_luxury_score_rec_10d_v140_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_rec_10d_v140_signal},    "f50_luxury_moat_index_grossmargin_rec_21d_v141_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_rec_21d_v141_signal},    "f50_luxury_moat_index_revenue_rec_21d_v142_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_rec_21d_v142_signal},    "f50_luxury_moat_index_netinc_rec_21d_v143_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_rec_21d_v143_signal},    "f50_luxury_moat_index_luxury_score_rec_21d_v144_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_rec_21d_v144_signal},    "f50_luxury_moat_index_grossmargin_rec_42d_v145_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_rec_42d_v145_signal},    "f50_luxury_moat_index_revenue_rec_42d_v146_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_rec_42d_v146_signal},    "f50_luxury_moat_index_netinc_rec_42d_v147_signal": {"inputs": [], "func": f50_luxury_moat_index_netinc_rec_42d_v147_signal},    "f50_luxury_moat_index_luxury_score_rec_42d_v148_signal": {"inputs": [], "func": f50_luxury_moat_index_luxury_score_rec_42d_v148_signal},    "f50_luxury_moat_index_grossmargin_rec_63d_v149_signal": {"inputs": [], "func": f50_luxury_moat_index_grossmargin_rec_63d_v149_signal},    "f50_luxury_moat_index_revenue_rec_63d_v150_signal": {"inputs": [], "func": f50_luxury_moat_index_revenue_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 50...")
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
