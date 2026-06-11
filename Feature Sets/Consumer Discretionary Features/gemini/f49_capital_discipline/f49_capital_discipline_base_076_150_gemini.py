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

def f49_capital_discipline_fcf_yield_on_capex_z_504d_v076_signal(fcf, capex):
    """Z-score for relative outlier detection of Free cash flow generated per unit of capex over 504d window."""
    res = _z(_ratio(fcf, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_z_756d_v077_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 756d window."""
    res = _z(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_z_756d_v078_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_z_756d_v079_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 756d window."""
    res = _z(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_z_756d_v080_signal(fcf, capex):
    """Z-score for relative outlier detection of Free cash flow generated per unit of capex over 756d window."""
    res = _z(_ratio(fcf, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_z_1008d_v081_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 1008d window."""
    res = _z(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_z_1008d_v082_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_z_1008d_v083_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 1008d window."""
    res = _z(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_z_1008d_v084_signal(fcf, capex):
    """Z-score for relative outlier detection of Free cash flow generated per unit of capex over 1008d window."""
    res = _z(_ratio(fcf, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_z_1260d_v085_signal(capex):
    """Z-score for relative outlier detection of Raw level of capex over 1260d window."""
    res = _z(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_z_1260d_v086_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_z_1260d_v087_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 1260d window."""
    res = _z(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_z_1260d_v088_signal(fcf, capex):
    """Z-score for relative outlier detection of Free cash flow generated per unit of capex over 1260d window."""
    res = _z(_ratio(fcf, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_5d_v089_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 5d window."""
    res = _drawdown(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_5d_v090_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_5d_v091_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 5d window."""
    res = _drawdown(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_5d_v092_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 5d window."""
    res = _drawdown(_ratio(fcf, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_10d_v093_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 10d window."""
    res = _drawdown(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_10d_v094_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_10d_v095_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 10d window."""
    res = _drawdown(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_10d_v096_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 10d window."""
    res = _drawdown(_ratio(fcf, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_21d_v097_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 21d window."""
    res = _drawdown(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_21d_v098_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_21d_v099_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 21d window."""
    res = _drawdown(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_21d_v100_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 21d window."""
    res = _drawdown(_ratio(fcf, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_42d_v101_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 42d window."""
    res = _drawdown(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_42d_v102_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_42d_v103_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 42d window."""
    res = _drawdown(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_42d_v104_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 42d window."""
    res = _drawdown(_ratio(fcf, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_63d_v105_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 63d window."""
    res = _drawdown(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_63d_v106_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 63d window."""
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_63d_v107_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 63d window."""
    res = _drawdown(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_63d_v108_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 63d window."""
    res = _drawdown(_ratio(fcf, capex), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_126d_v109_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 126d window."""
    res = _drawdown(capex, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_126d_v110_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 126d window."""
    res = _drawdown(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_126d_v111_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 126d window."""
    res = _drawdown(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_126d_v112_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 126d window."""
    res = _drawdown(_ratio(fcf, capex), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_252d_v113_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 252d window."""
    res = _drawdown(capex, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_252d_v114_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 252d window."""
    res = _drawdown(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_252d_v115_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 252d window."""
    res = _drawdown(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_252d_v116_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 252d window."""
    res = _drawdown(_ratio(fcf, capex), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_504d_v117_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 504d window."""
    res = _drawdown(capex, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_504d_v118_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 504d window."""
    res = _drawdown(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_504d_v119_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 504d window."""
    res = _drawdown(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_504d_v120_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 504d window."""
    res = _drawdown(_ratio(fcf, capex), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_756d_v121_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 756d window."""
    res = _drawdown(capex, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_756d_v122_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 756d window."""
    res = _drawdown(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_756d_v123_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 756d window."""
    res = _drawdown(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_756d_v124_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 756d window."""
    res = _drawdown(_ratio(fcf, capex), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_1008d_v125_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 1008d window."""
    res = _drawdown(capex, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_1008d_v126_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 1008d window."""
    res = _drawdown(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_1008d_v127_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 1008d window."""
    res = _drawdown(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_1008d_v128_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 1008d window."""
    res = _drawdown(_ratio(fcf, capex), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_dd_1260d_v129_signal(capex):
    """Drawdown from peak to identify cycle troughs of Raw level of capex over 1260d window."""
    res = _drawdown(capex, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_dd_1260d_v130_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 1260d window."""
    res = _drawdown(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_dd_1260d_v131_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 1260d window."""
    res = _drawdown(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_dd_1260d_v132_signal(fcf, capex):
    """Drawdown from peak to identify cycle troughs of Free cash flow generated per unit of capex over 1260d window."""
    res = _drawdown(_ratio(fcf, capex), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_rec_5d_v133_signal(capex):
    """Recovery from trough for turnaround signals of Raw level of capex over 5d window."""
    res = _recovery(capex, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_rec_5d_v134_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 5d window."""
    res = _recovery(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_rec_5d_v135_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 5d window."""
    res = _recovery(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_rec_5d_v136_signal(fcf, capex):
    """Recovery from trough for turnaround signals of Free cash flow generated per unit of capex over 5d window."""
    res = _recovery(_ratio(fcf, capex), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_rec_10d_v137_signal(capex):
    """Recovery from trough for turnaround signals of Raw level of capex over 10d window."""
    res = _recovery(capex, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_rec_10d_v138_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 10d window."""
    res = _recovery(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_rec_10d_v139_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 10d window."""
    res = _recovery(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_rec_10d_v140_signal(fcf, capex):
    """Recovery from trough for turnaround signals of Free cash flow generated per unit of capex over 10d window."""
    res = _recovery(_ratio(fcf, capex), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_rec_21d_v141_signal(capex):
    """Recovery from trough for turnaround signals of Raw level of capex over 21d window."""
    res = _recovery(capex, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_rec_21d_v142_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 21d window."""
    res = _recovery(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_rec_21d_v143_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 21d window."""
    res = _recovery(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_rec_21d_v144_signal(fcf, capex):
    """Recovery from trough for turnaround signals of Free cash flow generated per unit of capex over 21d window."""
    res = _recovery(_ratio(fcf, capex), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_rec_42d_v145_signal(capex):
    """Recovery from trough for turnaround signals of Raw level of capex over 42d window."""
    res = _recovery(capex, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_rec_42d_v146_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 42d window."""
    res = _recovery(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_rec_42d_v147_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 42d window."""
    res = _recovery(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_fcf_yield_on_capex_rec_42d_v148_signal(fcf, capex):
    """Recovery from trough for turnaround signals of Free cash flow generated per unit of capex over 42d window."""
    res = _recovery(_ratio(fcf, capex), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_capex_rec_63d_v149_signal(capex):
    """Recovery from trough for turnaround signals of Raw level of capex over 63d window."""
    res = _recovery(capex, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f49_capital_discipline_netinc_rec_63d_v150_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 63d window."""
    res = _recovery(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f49_capital_discipline_fcf_yield_on_capex_z_504d_v076_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_z_504d_v076_signal},    "f49_capital_discipline_capex_z_756d_v077_signal": {"inputs": [], "func": f49_capital_discipline_capex_z_756d_v077_signal},    "f49_capital_discipline_netinc_z_756d_v078_signal": {"inputs": [], "func": f49_capital_discipline_netinc_z_756d_v078_signal},    "f49_capital_discipline_fcf_z_756d_v079_signal": {"inputs": [], "func": f49_capital_discipline_fcf_z_756d_v079_signal},    "f49_capital_discipline_fcf_yield_on_capex_z_756d_v080_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_z_756d_v080_signal},    "f49_capital_discipline_capex_z_1008d_v081_signal": {"inputs": [], "func": f49_capital_discipline_capex_z_1008d_v081_signal},    "f49_capital_discipline_netinc_z_1008d_v082_signal": {"inputs": [], "func": f49_capital_discipline_netinc_z_1008d_v082_signal},    "f49_capital_discipline_fcf_z_1008d_v083_signal": {"inputs": [], "func": f49_capital_discipline_fcf_z_1008d_v083_signal},    "f49_capital_discipline_fcf_yield_on_capex_z_1008d_v084_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_z_1008d_v084_signal},    "f49_capital_discipline_capex_z_1260d_v085_signal": {"inputs": [], "func": f49_capital_discipline_capex_z_1260d_v085_signal},    "f49_capital_discipline_netinc_z_1260d_v086_signal": {"inputs": [], "func": f49_capital_discipline_netinc_z_1260d_v086_signal},    "f49_capital_discipline_fcf_z_1260d_v087_signal": {"inputs": [], "func": f49_capital_discipline_fcf_z_1260d_v087_signal},    "f49_capital_discipline_fcf_yield_on_capex_z_1260d_v088_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_z_1260d_v088_signal},    "f49_capital_discipline_capex_dd_5d_v089_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_5d_v089_signal},    "f49_capital_discipline_netinc_dd_5d_v090_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_5d_v090_signal},    "f49_capital_discipline_fcf_dd_5d_v091_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_5d_v091_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_5d_v092_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_5d_v092_signal},    "f49_capital_discipline_capex_dd_10d_v093_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_10d_v093_signal},    "f49_capital_discipline_netinc_dd_10d_v094_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_10d_v094_signal},    "f49_capital_discipline_fcf_dd_10d_v095_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_10d_v095_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_10d_v096_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_10d_v096_signal},    "f49_capital_discipline_capex_dd_21d_v097_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_21d_v097_signal},    "f49_capital_discipline_netinc_dd_21d_v098_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_21d_v098_signal},    "f49_capital_discipline_fcf_dd_21d_v099_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_21d_v099_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_21d_v100_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_21d_v100_signal},    "f49_capital_discipline_capex_dd_42d_v101_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_42d_v101_signal},    "f49_capital_discipline_netinc_dd_42d_v102_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_42d_v102_signal},    "f49_capital_discipline_fcf_dd_42d_v103_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_42d_v103_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_42d_v104_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_42d_v104_signal},    "f49_capital_discipline_capex_dd_63d_v105_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_63d_v105_signal},    "f49_capital_discipline_netinc_dd_63d_v106_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_63d_v106_signal},    "f49_capital_discipline_fcf_dd_63d_v107_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_63d_v107_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_63d_v108_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_63d_v108_signal},    "f49_capital_discipline_capex_dd_126d_v109_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_126d_v109_signal},    "f49_capital_discipline_netinc_dd_126d_v110_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_126d_v110_signal},    "f49_capital_discipline_fcf_dd_126d_v111_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_126d_v111_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_126d_v112_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_126d_v112_signal},    "f49_capital_discipline_capex_dd_252d_v113_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_252d_v113_signal},    "f49_capital_discipline_netinc_dd_252d_v114_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_252d_v114_signal},    "f49_capital_discipline_fcf_dd_252d_v115_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_252d_v115_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_252d_v116_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_252d_v116_signal},    "f49_capital_discipline_capex_dd_504d_v117_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_504d_v117_signal},    "f49_capital_discipline_netinc_dd_504d_v118_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_504d_v118_signal},    "f49_capital_discipline_fcf_dd_504d_v119_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_504d_v119_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_504d_v120_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_504d_v120_signal},    "f49_capital_discipline_capex_dd_756d_v121_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_756d_v121_signal},    "f49_capital_discipline_netinc_dd_756d_v122_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_756d_v122_signal},    "f49_capital_discipline_fcf_dd_756d_v123_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_756d_v123_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_756d_v124_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_756d_v124_signal},    "f49_capital_discipline_capex_dd_1008d_v125_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_1008d_v125_signal},    "f49_capital_discipline_netinc_dd_1008d_v126_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_1008d_v126_signal},    "f49_capital_discipline_fcf_dd_1008d_v127_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_1008d_v127_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_1008d_v128_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_1008d_v128_signal},    "f49_capital_discipline_capex_dd_1260d_v129_signal": {"inputs": [], "func": f49_capital_discipline_capex_dd_1260d_v129_signal},    "f49_capital_discipline_netinc_dd_1260d_v130_signal": {"inputs": [], "func": f49_capital_discipline_netinc_dd_1260d_v130_signal},    "f49_capital_discipline_fcf_dd_1260d_v131_signal": {"inputs": [], "func": f49_capital_discipline_fcf_dd_1260d_v131_signal},    "f49_capital_discipline_fcf_yield_on_capex_dd_1260d_v132_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_dd_1260d_v132_signal},    "f49_capital_discipline_capex_rec_5d_v133_signal": {"inputs": [], "func": f49_capital_discipline_capex_rec_5d_v133_signal},    "f49_capital_discipline_netinc_rec_5d_v134_signal": {"inputs": [], "func": f49_capital_discipline_netinc_rec_5d_v134_signal},    "f49_capital_discipline_fcf_rec_5d_v135_signal": {"inputs": [], "func": f49_capital_discipline_fcf_rec_5d_v135_signal},    "f49_capital_discipline_fcf_yield_on_capex_rec_5d_v136_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_rec_5d_v136_signal},    "f49_capital_discipline_capex_rec_10d_v137_signal": {"inputs": [], "func": f49_capital_discipline_capex_rec_10d_v137_signal},    "f49_capital_discipline_netinc_rec_10d_v138_signal": {"inputs": [], "func": f49_capital_discipline_netinc_rec_10d_v138_signal},    "f49_capital_discipline_fcf_rec_10d_v139_signal": {"inputs": [], "func": f49_capital_discipline_fcf_rec_10d_v139_signal},    "f49_capital_discipline_fcf_yield_on_capex_rec_10d_v140_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_rec_10d_v140_signal},    "f49_capital_discipline_capex_rec_21d_v141_signal": {"inputs": [], "func": f49_capital_discipline_capex_rec_21d_v141_signal},    "f49_capital_discipline_netinc_rec_21d_v142_signal": {"inputs": [], "func": f49_capital_discipline_netinc_rec_21d_v142_signal},    "f49_capital_discipline_fcf_rec_21d_v143_signal": {"inputs": [], "func": f49_capital_discipline_fcf_rec_21d_v143_signal},    "f49_capital_discipline_fcf_yield_on_capex_rec_21d_v144_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_rec_21d_v144_signal},    "f49_capital_discipline_capex_rec_42d_v145_signal": {"inputs": [], "func": f49_capital_discipline_capex_rec_42d_v145_signal},    "f49_capital_discipline_netinc_rec_42d_v146_signal": {"inputs": [], "func": f49_capital_discipline_netinc_rec_42d_v146_signal},    "f49_capital_discipline_fcf_rec_42d_v147_signal": {"inputs": [], "func": f49_capital_discipline_fcf_rec_42d_v147_signal},    "f49_capital_discipline_fcf_yield_on_capex_rec_42d_v148_signal": {"inputs": [], "func": f49_capital_discipline_fcf_yield_on_capex_rec_42d_v148_signal},    "f49_capital_discipline_capex_rec_63d_v149_signal": {"inputs": [], "func": f49_capital_discipline_capex_rec_63d_v149_signal},    "f49_capital_discipline_netinc_rec_63d_v150_signal": {"inputs": [], "func": f49_capital_discipline_netinc_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 49...")
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
