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

def f24_liquidity_buffer_runway_proxy_z_504d_v076_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 504d window."""
    res = _z(_ratio(cashneq, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_756d_v077_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 756d window."""
    res = _z(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_756d_v078_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 756d window."""
    res = _z(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_756d_v079_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 756d window."""
    res = _z(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_756d_v080_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 756d window."""
    res = _z(_ratio(cashneq, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_1008d_v081_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 1008d window."""
    res = _z(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_1008d_v082_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 1008d window."""
    res = _z(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_1008d_v083_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 1008d window."""
    res = _z(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_1008d_v084_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 1008d window."""
    res = _z(_ratio(cashneq, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_z_1260d_v085_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 1260d window."""
    res = _z(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_z_1260d_v086_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 1260d window."""
    res = _z(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_z_1260d_v087_signal(cor):
    """Z-score for relative outlier detection of Raw level of cor over 1260d window."""
    res = _z(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_z_1260d_v088_signal(cashneq, sgna):
    """Z-score for relative outlier detection of Cash coverage of SG&A burn over 1260d window."""
    res = _z(_ratio(cashneq, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_5d_v089_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 5d window."""
    res = _drawdown(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_5d_v090_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 5d window."""
    res = _drawdown(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_5d_v091_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 5d window."""
    res = _drawdown(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_5d_v092_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 5d window."""
    res = _drawdown(_ratio(cashneq, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_10d_v093_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 10d window."""
    res = _drawdown(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_10d_v094_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 10d window."""
    res = _drawdown(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_10d_v095_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 10d window."""
    res = _drawdown(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_10d_v096_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 10d window."""
    res = _drawdown(_ratio(cashneq, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_21d_v097_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 21d window."""
    res = _drawdown(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_21d_v098_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 21d window."""
    res = _drawdown(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_21d_v099_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 21d window."""
    res = _drawdown(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_21d_v100_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 21d window."""
    res = _drawdown(_ratio(cashneq, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_42d_v101_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 42d window."""
    res = _drawdown(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_42d_v102_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 42d window."""
    res = _drawdown(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_42d_v103_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 42d window."""
    res = _drawdown(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_42d_v104_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 42d window."""
    res = _drawdown(_ratio(cashneq, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_63d_v105_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 63d window."""
    res = _drawdown(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_63d_v106_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 63d window."""
    res = _drawdown(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_63d_v107_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 63d window."""
    res = _drawdown(cor, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_63d_v108_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 63d window."""
    res = _drawdown(_ratio(cashneq, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_126d_v109_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 126d window."""
    res = _drawdown(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_126d_v110_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 126d window."""
    res = _drawdown(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_126d_v111_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 126d window."""
    res = _drawdown(cor, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_126d_v112_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 126d window."""
    res = _drawdown(_ratio(cashneq, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_252d_v113_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 252d window."""
    res = _drawdown(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_252d_v114_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 252d window."""
    res = _drawdown(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_252d_v115_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 252d window."""
    res = _drawdown(cor, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_252d_v116_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 252d window."""
    res = _drawdown(_ratio(cashneq, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_504d_v117_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 504d window."""
    res = _drawdown(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_504d_v118_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 504d window."""
    res = _drawdown(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_504d_v119_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 504d window."""
    res = _drawdown(cor, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_504d_v120_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 504d window."""
    res = _drawdown(_ratio(cashneq, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_756d_v121_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 756d window."""
    res = _drawdown(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_756d_v122_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 756d window."""
    res = _drawdown(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_756d_v123_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 756d window."""
    res = _drawdown(cor, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_756d_v124_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 756d window."""
    res = _drawdown(_ratio(cashneq, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_1008d_v125_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 1008d window."""
    res = _drawdown(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_1008d_v126_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 1008d window."""
    res = _drawdown(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_1008d_v127_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 1008d window."""
    res = _drawdown(cor, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_1008d_v128_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 1008d window."""
    res = _drawdown(_ratio(cashneq, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_dd_1260d_v129_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 1260d window."""
    res = _drawdown(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_dd_1260d_v130_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 1260d window."""
    res = _drawdown(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_dd_1260d_v131_signal(cor):
    """Drawdown from peak to identify cycle troughs of Raw level of cor over 1260d window."""
    res = _drawdown(cor, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_dd_1260d_v132_signal(cashneq, sgna):
    """Drawdown from peak to identify cycle troughs of Cash coverage of SG&A burn over 1260d window."""
    res = _drawdown(_ratio(cashneq, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_rec_5d_v133_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 5d window."""
    res = _recovery(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_rec_5d_v134_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 5d window."""
    res = _recovery(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_rec_5d_v135_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 5d window."""
    res = _recovery(cor, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_rec_5d_v136_signal(cashneq, sgna):
    """Recovery from trough for turnaround signals of Cash coverage of SG&A burn over 5d window."""
    res = _recovery(_ratio(cashneq, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_rec_10d_v137_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 10d window."""
    res = _recovery(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_rec_10d_v138_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 10d window."""
    res = _recovery(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_rec_10d_v139_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 10d window."""
    res = _recovery(cor, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_rec_10d_v140_signal(cashneq, sgna):
    """Recovery from trough for turnaround signals of Cash coverage of SG&A burn over 10d window."""
    res = _recovery(_ratio(cashneq, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_rec_21d_v141_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 21d window."""
    res = _recovery(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_rec_21d_v142_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 21d window."""
    res = _recovery(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_rec_21d_v143_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 21d window."""
    res = _recovery(cor, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_rec_21d_v144_signal(cashneq, sgna):
    """Recovery from trough for turnaround signals of Cash coverage of SG&A burn over 21d window."""
    res = _recovery(_ratio(cashneq, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_rec_42d_v145_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 42d window."""
    res = _recovery(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_rec_42d_v146_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 42d window."""
    res = _recovery(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cor_rec_42d_v147_signal(cor):
    """Recovery from trough for turnaround signals of Raw level of cor over 42d window."""
    res = _recovery(cor, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_runway_proxy_rec_42d_v148_signal(cashneq, sgna):
    """Recovery from trough for turnaround signals of Cash coverage of SG&A burn over 42d window."""
    res = _recovery(_ratio(cashneq, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_cashneq_rec_63d_v149_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 63d window."""
    res = _recovery(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f24_liquidity_buffer_sgna_rec_63d_v150_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 63d window."""
    res = _recovery(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f24_liquidity_buffer_runway_proxy_z_504d_v076_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_504d_v076_signal},    "f24_liquidity_buffer_cashneq_z_756d_v077_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_756d_v077_signal},    "f24_liquidity_buffer_sgna_z_756d_v078_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_756d_v078_signal},    "f24_liquidity_buffer_cor_z_756d_v079_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_756d_v079_signal},    "f24_liquidity_buffer_runway_proxy_z_756d_v080_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_756d_v080_signal},    "f24_liquidity_buffer_cashneq_z_1008d_v081_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_1008d_v081_signal},    "f24_liquidity_buffer_sgna_z_1008d_v082_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_1008d_v082_signal},    "f24_liquidity_buffer_cor_z_1008d_v083_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_1008d_v083_signal},    "f24_liquidity_buffer_runway_proxy_z_1008d_v084_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_1008d_v084_signal},    "f24_liquidity_buffer_cashneq_z_1260d_v085_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_z_1260d_v085_signal},    "f24_liquidity_buffer_sgna_z_1260d_v086_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_z_1260d_v086_signal},    "f24_liquidity_buffer_cor_z_1260d_v087_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_z_1260d_v087_signal},    "f24_liquidity_buffer_runway_proxy_z_1260d_v088_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_z_1260d_v088_signal},    "f24_liquidity_buffer_cashneq_dd_5d_v089_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_5d_v089_signal},    "f24_liquidity_buffer_sgna_dd_5d_v090_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_5d_v090_signal},    "f24_liquidity_buffer_cor_dd_5d_v091_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_5d_v091_signal},    "f24_liquidity_buffer_runway_proxy_dd_5d_v092_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_5d_v092_signal},    "f24_liquidity_buffer_cashneq_dd_10d_v093_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_10d_v093_signal},    "f24_liquidity_buffer_sgna_dd_10d_v094_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_10d_v094_signal},    "f24_liquidity_buffer_cor_dd_10d_v095_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_10d_v095_signal},    "f24_liquidity_buffer_runway_proxy_dd_10d_v096_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_10d_v096_signal},    "f24_liquidity_buffer_cashneq_dd_21d_v097_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_21d_v097_signal},    "f24_liquidity_buffer_sgna_dd_21d_v098_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_21d_v098_signal},    "f24_liquidity_buffer_cor_dd_21d_v099_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_21d_v099_signal},    "f24_liquidity_buffer_runway_proxy_dd_21d_v100_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_21d_v100_signal},    "f24_liquidity_buffer_cashneq_dd_42d_v101_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_42d_v101_signal},    "f24_liquidity_buffer_sgna_dd_42d_v102_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_42d_v102_signal},    "f24_liquidity_buffer_cor_dd_42d_v103_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_42d_v103_signal},    "f24_liquidity_buffer_runway_proxy_dd_42d_v104_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_42d_v104_signal},    "f24_liquidity_buffer_cashneq_dd_63d_v105_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_63d_v105_signal},    "f24_liquidity_buffer_sgna_dd_63d_v106_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_63d_v106_signal},    "f24_liquidity_buffer_cor_dd_63d_v107_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_63d_v107_signal},    "f24_liquidity_buffer_runway_proxy_dd_63d_v108_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_63d_v108_signal},    "f24_liquidity_buffer_cashneq_dd_126d_v109_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_126d_v109_signal},    "f24_liquidity_buffer_sgna_dd_126d_v110_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_126d_v110_signal},    "f24_liquidity_buffer_cor_dd_126d_v111_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_126d_v111_signal},    "f24_liquidity_buffer_runway_proxy_dd_126d_v112_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_126d_v112_signal},    "f24_liquidity_buffer_cashneq_dd_252d_v113_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_252d_v113_signal},    "f24_liquidity_buffer_sgna_dd_252d_v114_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_252d_v114_signal},    "f24_liquidity_buffer_cor_dd_252d_v115_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_252d_v115_signal},    "f24_liquidity_buffer_runway_proxy_dd_252d_v116_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_252d_v116_signal},    "f24_liquidity_buffer_cashneq_dd_504d_v117_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_504d_v117_signal},    "f24_liquidity_buffer_sgna_dd_504d_v118_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_504d_v118_signal},    "f24_liquidity_buffer_cor_dd_504d_v119_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_504d_v119_signal},    "f24_liquidity_buffer_runway_proxy_dd_504d_v120_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_504d_v120_signal},    "f24_liquidity_buffer_cashneq_dd_756d_v121_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_756d_v121_signal},    "f24_liquidity_buffer_sgna_dd_756d_v122_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_756d_v122_signal},    "f24_liquidity_buffer_cor_dd_756d_v123_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_756d_v123_signal},    "f24_liquidity_buffer_runway_proxy_dd_756d_v124_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_756d_v124_signal},    "f24_liquidity_buffer_cashneq_dd_1008d_v125_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_1008d_v125_signal},    "f24_liquidity_buffer_sgna_dd_1008d_v126_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_1008d_v126_signal},    "f24_liquidity_buffer_cor_dd_1008d_v127_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_1008d_v127_signal},    "f24_liquidity_buffer_runway_proxy_dd_1008d_v128_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_1008d_v128_signal},    "f24_liquidity_buffer_cashneq_dd_1260d_v129_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_dd_1260d_v129_signal},    "f24_liquidity_buffer_sgna_dd_1260d_v130_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_dd_1260d_v130_signal},    "f24_liquidity_buffer_cor_dd_1260d_v131_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_dd_1260d_v131_signal},    "f24_liquidity_buffer_runway_proxy_dd_1260d_v132_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_dd_1260d_v132_signal},    "f24_liquidity_buffer_cashneq_rec_5d_v133_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_rec_5d_v133_signal},    "f24_liquidity_buffer_sgna_rec_5d_v134_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_rec_5d_v134_signal},    "f24_liquidity_buffer_cor_rec_5d_v135_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_rec_5d_v135_signal},    "f24_liquidity_buffer_runway_proxy_rec_5d_v136_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_rec_5d_v136_signal},    "f24_liquidity_buffer_cashneq_rec_10d_v137_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_rec_10d_v137_signal},    "f24_liquidity_buffer_sgna_rec_10d_v138_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_rec_10d_v138_signal},    "f24_liquidity_buffer_cor_rec_10d_v139_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_rec_10d_v139_signal},    "f24_liquidity_buffer_runway_proxy_rec_10d_v140_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_rec_10d_v140_signal},    "f24_liquidity_buffer_cashneq_rec_21d_v141_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_rec_21d_v141_signal},    "f24_liquidity_buffer_sgna_rec_21d_v142_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_rec_21d_v142_signal},    "f24_liquidity_buffer_cor_rec_21d_v143_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_rec_21d_v143_signal},    "f24_liquidity_buffer_runway_proxy_rec_21d_v144_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_rec_21d_v144_signal},    "f24_liquidity_buffer_cashneq_rec_42d_v145_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_rec_42d_v145_signal},    "f24_liquidity_buffer_sgna_rec_42d_v146_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_rec_42d_v146_signal},    "f24_liquidity_buffer_cor_rec_42d_v147_signal": {"inputs": [], "func": f24_liquidity_buffer_cor_rec_42d_v147_signal},    "f24_liquidity_buffer_runway_proxy_rec_42d_v148_signal": {"inputs": [], "func": f24_liquidity_buffer_runway_proxy_rec_42d_v148_signal},    "f24_liquidity_buffer_cashneq_rec_63d_v149_signal": {"inputs": [], "func": f24_liquidity_buffer_cashneq_rec_63d_v149_signal},    "f24_liquidity_buffer_sgna_rec_63d_v150_signal": {"inputs": [], "func": f24_liquidity_buffer_sgna_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 24...")
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
