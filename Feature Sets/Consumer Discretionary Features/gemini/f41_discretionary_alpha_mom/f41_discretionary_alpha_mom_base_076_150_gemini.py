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

def f41_discretionary_alpha_mom_price_velocity_z_504d_v076_signal(closeadj):
    """Z-score for relative outlier detection of Short-term price momentum over 504d window."""
    res = _z(_slope_pct(closeadj, 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_z_756d_v077_signal(closeadj):
    """Z-score for relative outlier detection of Raw level of closeadj over 756d window."""
    res = _z(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_z_756d_v078_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 756d window."""
    res = _z(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_z_756d_v079_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 756d window."""
    res = _z(ps, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_z_756d_v080_signal(closeadj):
    """Z-score for relative outlier detection of Short-term price momentum over 756d window."""
    res = _z(_slope_pct(closeadj, 63), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_z_1008d_v081_signal(closeadj):
    """Z-score for relative outlier detection of Raw level of closeadj over 1008d window."""
    res = _z(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_z_1008d_v082_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 1008d window."""
    res = _z(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_z_1008d_v083_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 1008d window."""
    res = _z(ps, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_z_1008d_v084_signal(closeadj):
    """Z-score for relative outlier detection of Short-term price momentum over 1008d window."""
    res = _z(_slope_pct(closeadj, 63), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_z_1260d_v085_signal(closeadj):
    """Z-score for relative outlier detection of Raw level of closeadj over 1260d window."""
    res = _z(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_z_1260d_v086_signal(pe):
    """Z-score for relative outlier detection of Raw level of pe over 1260d window."""
    res = _z(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_z_1260d_v087_signal(ps):
    """Z-score for relative outlier detection of Raw level of ps over 1260d window."""
    res = _z(ps, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_z_1260d_v088_signal(closeadj):
    """Z-score for relative outlier detection of Short-term price momentum over 1260d window."""
    res = _z(_slope_pct(closeadj, 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_5d_v089_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 5d window."""
    res = _drawdown(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_5d_v090_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 5d window."""
    res = _drawdown(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_5d_v091_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 5d window."""
    res = _drawdown(ps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_5d_v092_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 5d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_10d_v093_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 10d window."""
    res = _drawdown(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_10d_v094_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 10d window."""
    res = _drawdown(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_10d_v095_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 10d window."""
    res = _drawdown(ps, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_10d_v096_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 10d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_21d_v097_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 21d window."""
    res = _drawdown(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_21d_v098_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 21d window."""
    res = _drawdown(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_21d_v099_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 21d window."""
    res = _drawdown(ps, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_21d_v100_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 21d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_42d_v101_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 42d window."""
    res = _drawdown(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_42d_v102_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 42d window."""
    res = _drawdown(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_42d_v103_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 42d window."""
    res = _drawdown(ps, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_42d_v104_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 42d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_63d_v105_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 63d window."""
    res = _drawdown(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_63d_v106_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 63d window."""
    res = _drawdown(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_63d_v107_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 63d window."""
    res = _drawdown(ps, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_63d_v108_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 63d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_126d_v109_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 126d window."""
    res = _drawdown(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_126d_v110_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 126d window."""
    res = _drawdown(pe, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_126d_v111_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 126d window."""
    res = _drawdown(ps, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_126d_v112_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 126d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_252d_v113_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 252d window."""
    res = _drawdown(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_252d_v114_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 252d window."""
    res = _drawdown(pe, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_252d_v115_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 252d window."""
    res = _drawdown(ps, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_252d_v116_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 252d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_504d_v117_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 504d window."""
    res = _drawdown(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_504d_v118_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 504d window."""
    res = _drawdown(pe, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_504d_v119_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 504d window."""
    res = _drawdown(ps, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_504d_v120_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 504d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_756d_v121_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 756d window."""
    res = _drawdown(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_756d_v122_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 756d window."""
    res = _drawdown(pe, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_756d_v123_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 756d window."""
    res = _drawdown(ps, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_756d_v124_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 756d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_1008d_v125_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 1008d window."""
    res = _drawdown(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_1008d_v126_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 1008d window."""
    res = _drawdown(pe, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_1008d_v127_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 1008d window."""
    res = _drawdown(ps, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_1008d_v128_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 1008d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_dd_1260d_v129_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Raw level of closeadj over 1260d window."""
    res = _drawdown(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_dd_1260d_v130_signal(pe):
    """Drawdown from peak to identify cycle troughs of Raw level of pe over 1260d window."""
    res = _drawdown(pe, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_dd_1260d_v131_signal(ps):
    """Drawdown from peak to identify cycle troughs of Raw level of ps over 1260d window."""
    res = _drawdown(ps, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_dd_1260d_v132_signal(closeadj):
    """Drawdown from peak to identify cycle troughs of Short-term price momentum over 1260d window."""
    res = _drawdown(_slope_pct(closeadj, 63), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_rec_5d_v133_signal(closeadj):
    """Recovery from trough for turnaround signals of Raw level of closeadj over 5d window."""
    res = _recovery(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_rec_5d_v134_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 5d window."""
    res = _recovery(pe, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_rec_5d_v135_signal(ps):
    """Recovery from trough for turnaround signals of Raw level of ps over 5d window."""
    res = _recovery(ps, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_rec_5d_v136_signal(closeadj):
    """Recovery from trough for turnaround signals of Short-term price momentum over 5d window."""
    res = _recovery(_slope_pct(closeadj, 63), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_rec_10d_v137_signal(closeadj):
    """Recovery from trough for turnaround signals of Raw level of closeadj over 10d window."""
    res = _recovery(closeadj, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_rec_10d_v138_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 10d window."""
    res = _recovery(pe, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_rec_10d_v139_signal(ps):
    """Recovery from trough for turnaround signals of Raw level of ps over 10d window."""
    res = _recovery(ps, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_rec_10d_v140_signal(closeadj):
    """Recovery from trough for turnaround signals of Short-term price momentum over 10d window."""
    res = _recovery(_slope_pct(closeadj, 63), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_rec_21d_v141_signal(closeadj):
    """Recovery from trough for turnaround signals of Raw level of closeadj over 21d window."""
    res = _recovery(closeadj, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_rec_21d_v142_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 21d window."""
    res = _recovery(pe, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_rec_21d_v143_signal(ps):
    """Recovery from trough for turnaround signals of Raw level of ps over 21d window."""
    res = _recovery(ps, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_rec_21d_v144_signal(closeadj):
    """Recovery from trough for turnaround signals of Short-term price momentum over 21d window."""
    res = _recovery(_slope_pct(closeadj, 63), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_rec_42d_v145_signal(closeadj):
    """Recovery from trough for turnaround signals of Raw level of closeadj over 42d window."""
    res = _recovery(closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_rec_42d_v146_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 42d window."""
    res = _recovery(pe, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_ps_rec_42d_v147_signal(ps):
    """Recovery from trough for turnaround signals of Raw level of ps over 42d window."""
    res = _recovery(ps, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_price_velocity_rec_42d_v148_signal(closeadj):
    """Recovery from trough for turnaround signals of Short-term price momentum over 42d window."""
    res = _recovery(_slope_pct(closeadj, 63), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_closeadj_rec_63d_v149_signal(closeadj):
    """Recovery from trough for turnaround signals of Raw level of closeadj over 63d window."""
    res = _recovery(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f41_discretionary_alpha_mom_pe_rec_63d_v150_signal(pe):
    """Recovery from trough for turnaround signals of Raw level of pe over 63d window."""
    res = _recovery(pe, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f41_discretionary_alpha_mom_price_velocity_z_504d_v076_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_z_504d_v076_signal},    "f41_discretionary_alpha_mom_closeadj_z_756d_v077_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_z_756d_v077_signal},    "f41_discretionary_alpha_mom_pe_z_756d_v078_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_z_756d_v078_signal},    "f41_discretionary_alpha_mom_ps_z_756d_v079_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_z_756d_v079_signal},    "f41_discretionary_alpha_mom_price_velocity_z_756d_v080_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_z_756d_v080_signal},    "f41_discretionary_alpha_mom_closeadj_z_1008d_v081_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_z_1008d_v081_signal},    "f41_discretionary_alpha_mom_pe_z_1008d_v082_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_z_1008d_v082_signal},    "f41_discretionary_alpha_mom_ps_z_1008d_v083_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_z_1008d_v083_signal},    "f41_discretionary_alpha_mom_price_velocity_z_1008d_v084_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_z_1008d_v084_signal},    "f41_discretionary_alpha_mom_closeadj_z_1260d_v085_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_z_1260d_v085_signal},    "f41_discretionary_alpha_mom_pe_z_1260d_v086_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_z_1260d_v086_signal},    "f41_discretionary_alpha_mom_ps_z_1260d_v087_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_z_1260d_v087_signal},    "f41_discretionary_alpha_mom_price_velocity_z_1260d_v088_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_z_1260d_v088_signal},    "f41_discretionary_alpha_mom_closeadj_dd_5d_v089_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_5d_v089_signal},    "f41_discretionary_alpha_mom_pe_dd_5d_v090_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_5d_v090_signal},    "f41_discretionary_alpha_mom_ps_dd_5d_v091_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_5d_v091_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_5d_v092_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_5d_v092_signal},    "f41_discretionary_alpha_mom_closeadj_dd_10d_v093_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_10d_v093_signal},    "f41_discretionary_alpha_mom_pe_dd_10d_v094_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_10d_v094_signal},    "f41_discretionary_alpha_mom_ps_dd_10d_v095_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_10d_v095_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_10d_v096_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_10d_v096_signal},    "f41_discretionary_alpha_mom_closeadj_dd_21d_v097_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_21d_v097_signal},    "f41_discretionary_alpha_mom_pe_dd_21d_v098_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_21d_v098_signal},    "f41_discretionary_alpha_mom_ps_dd_21d_v099_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_21d_v099_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_21d_v100_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_21d_v100_signal},    "f41_discretionary_alpha_mom_closeadj_dd_42d_v101_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_42d_v101_signal},    "f41_discretionary_alpha_mom_pe_dd_42d_v102_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_42d_v102_signal},    "f41_discretionary_alpha_mom_ps_dd_42d_v103_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_42d_v103_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_42d_v104_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_42d_v104_signal},    "f41_discretionary_alpha_mom_closeadj_dd_63d_v105_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_63d_v105_signal},    "f41_discretionary_alpha_mom_pe_dd_63d_v106_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_63d_v106_signal},    "f41_discretionary_alpha_mom_ps_dd_63d_v107_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_63d_v107_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_63d_v108_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_63d_v108_signal},    "f41_discretionary_alpha_mom_closeadj_dd_126d_v109_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_126d_v109_signal},    "f41_discretionary_alpha_mom_pe_dd_126d_v110_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_126d_v110_signal},    "f41_discretionary_alpha_mom_ps_dd_126d_v111_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_126d_v111_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_126d_v112_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_126d_v112_signal},    "f41_discretionary_alpha_mom_closeadj_dd_252d_v113_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_252d_v113_signal},    "f41_discretionary_alpha_mom_pe_dd_252d_v114_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_252d_v114_signal},    "f41_discretionary_alpha_mom_ps_dd_252d_v115_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_252d_v115_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_252d_v116_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_252d_v116_signal},    "f41_discretionary_alpha_mom_closeadj_dd_504d_v117_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_504d_v117_signal},    "f41_discretionary_alpha_mom_pe_dd_504d_v118_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_504d_v118_signal},    "f41_discretionary_alpha_mom_ps_dd_504d_v119_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_504d_v119_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_504d_v120_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_504d_v120_signal},    "f41_discretionary_alpha_mom_closeadj_dd_756d_v121_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_756d_v121_signal},    "f41_discretionary_alpha_mom_pe_dd_756d_v122_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_756d_v122_signal},    "f41_discretionary_alpha_mom_ps_dd_756d_v123_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_756d_v123_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_756d_v124_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_756d_v124_signal},    "f41_discretionary_alpha_mom_closeadj_dd_1008d_v125_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_1008d_v125_signal},    "f41_discretionary_alpha_mom_pe_dd_1008d_v126_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_1008d_v126_signal},    "f41_discretionary_alpha_mom_ps_dd_1008d_v127_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_1008d_v127_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_1008d_v128_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_1008d_v128_signal},    "f41_discretionary_alpha_mom_closeadj_dd_1260d_v129_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_dd_1260d_v129_signal},    "f41_discretionary_alpha_mom_pe_dd_1260d_v130_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_dd_1260d_v130_signal},    "f41_discretionary_alpha_mom_ps_dd_1260d_v131_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_dd_1260d_v131_signal},    "f41_discretionary_alpha_mom_price_velocity_dd_1260d_v132_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_dd_1260d_v132_signal},    "f41_discretionary_alpha_mom_closeadj_rec_5d_v133_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_rec_5d_v133_signal},    "f41_discretionary_alpha_mom_pe_rec_5d_v134_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_rec_5d_v134_signal},    "f41_discretionary_alpha_mom_ps_rec_5d_v135_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_rec_5d_v135_signal},    "f41_discretionary_alpha_mom_price_velocity_rec_5d_v136_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_rec_5d_v136_signal},    "f41_discretionary_alpha_mom_closeadj_rec_10d_v137_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_rec_10d_v137_signal},    "f41_discretionary_alpha_mom_pe_rec_10d_v138_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_rec_10d_v138_signal},    "f41_discretionary_alpha_mom_ps_rec_10d_v139_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_rec_10d_v139_signal},    "f41_discretionary_alpha_mom_price_velocity_rec_10d_v140_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_rec_10d_v140_signal},    "f41_discretionary_alpha_mom_closeadj_rec_21d_v141_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_rec_21d_v141_signal},    "f41_discretionary_alpha_mom_pe_rec_21d_v142_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_rec_21d_v142_signal},    "f41_discretionary_alpha_mom_ps_rec_21d_v143_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_rec_21d_v143_signal},    "f41_discretionary_alpha_mom_price_velocity_rec_21d_v144_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_rec_21d_v144_signal},    "f41_discretionary_alpha_mom_closeadj_rec_42d_v145_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_rec_42d_v145_signal},    "f41_discretionary_alpha_mom_pe_rec_42d_v146_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_rec_42d_v146_signal},    "f41_discretionary_alpha_mom_ps_rec_42d_v147_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_ps_rec_42d_v147_signal},    "f41_discretionary_alpha_mom_price_velocity_rec_42d_v148_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_price_velocity_rec_42d_v148_signal},    "f41_discretionary_alpha_mom_closeadj_rec_63d_v149_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_closeadj_rec_63d_v149_signal},    "f41_discretionary_alpha_mom_pe_rec_63d_v150_signal": {"inputs": [], "func": f41_discretionary_alpha_mom_pe_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 41...")
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
