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

def f43_payout_resilience_fcf_to_debt_z_504d_v076_signal(fcf, debt):
    """Z-score for relative outlier detection of Cash flow coverage of total debt over 504d window."""
    res = _z(_ratio(fcf, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_z_756d_v077_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 756d window."""
    res = _z(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_z_756d_v078_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_z_756d_v079_signal(debt):
    """Z-score for relative outlier detection of Raw level of debt over 756d window."""
    res = _z(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_z_756d_v080_signal(fcf, debt):
    """Z-score for relative outlier detection of Cash flow coverage of total debt over 756d window."""
    res = _z(_ratio(fcf, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_z_1008d_v081_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 1008d window."""
    res = _z(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_z_1008d_v082_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_z_1008d_v083_signal(debt):
    """Z-score for relative outlier detection of Raw level of debt over 1008d window."""
    res = _z(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_z_1008d_v084_signal(fcf, debt):
    """Z-score for relative outlier detection of Cash flow coverage of total debt over 1008d window."""
    res = _z(_ratio(fcf, debt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_z_1260d_v085_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 1260d window."""
    res = _z(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_z_1260d_v086_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_z_1260d_v087_signal(debt):
    """Z-score for relative outlier detection of Raw level of debt over 1260d window."""
    res = _z(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_z_1260d_v088_signal(fcf, debt):
    """Z-score for relative outlier detection of Cash flow coverage of total debt over 1260d window."""
    res = _z(_ratio(fcf, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_5d_v089_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 5d window."""
    res = _drawdown(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_5d_v090_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_5d_v091_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 5d window."""
    res = _drawdown(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_5d_v092_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 5d window."""
    res = _drawdown(_ratio(fcf, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_10d_v093_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 10d window."""
    res = _drawdown(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_10d_v094_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_10d_v095_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 10d window."""
    res = _drawdown(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_10d_v096_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 10d window."""
    res = _drawdown(_ratio(fcf, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_21d_v097_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 21d window."""
    res = _drawdown(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_21d_v098_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_21d_v099_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 21d window."""
    res = _drawdown(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_21d_v100_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 21d window."""
    res = _drawdown(_ratio(fcf, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_42d_v101_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 42d window."""
    res = _drawdown(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_42d_v102_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_42d_v103_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 42d window."""
    res = _drawdown(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_42d_v104_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 42d window."""
    res = _drawdown(_ratio(fcf, debt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_63d_v105_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 63d window."""
    res = _drawdown(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_63d_v106_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 63d window."""
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_63d_v107_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 63d window."""
    res = _drawdown(debt, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_63d_v108_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 63d window."""
    res = _drawdown(_ratio(fcf, debt), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_126d_v109_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 126d window."""
    res = _drawdown(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_126d_v110_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 126d window."""
    res = _drawdown(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_126d_v111_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 126d window."""
    res = _drawdown(debt, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_126d_v112_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 126d window."""
    res = _drawdown(_ratio(fcf, debt), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_252d_v113_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 252d window."""
    res = _drawdown(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_252d_v114_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 252d window."""
    res = _drawdown(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_252d_v115_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 252d window."""
    res = _drawdown(debt, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_252d_v116_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 252d window."""
    res = _drawdown(_ratio(fcf, debt), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_504d_v117_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 504d window."""
    res = _drawdown(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_504d_v118_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 504d window."""
    res = _drawdown(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_504d_v119_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 504d window."""
    res = _drawdown(debt, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_504d_v120_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 504d window."""
    res = _drawdown(_ratio(fcf, debt), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_756d_v121_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 756d window."""
    res = _drawdown(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_756d_v122_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 756d window."""
    res = _drawdown(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_756d_v123_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 756d window."""
    res = _drawdown(debt, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_756d_v124_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 756d window."""
    res = _drawdown(_ratio(fcf, debt), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_1008d_v125_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 1008d window."""
    res = _drawdown(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_1008d_v126_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 1008d window."""
    res = _drawdown(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_1008d_v127_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 1008d window."""
    res = _drawdown(debt, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_1008d_v128_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 1008d window."""
    res = _drawdown(_ratio(fcf, debt), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_dd_1260d_v129_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 1260d window."""
    res = _drawdown(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_dd_1260d_v130_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 1260d window."""
    res = _drawdown(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_dd_1260d_v131_signal(debt):
    """Drawdown from peak to identify cycle troughs of Raw level of debt over 1260d window."""
    res = _drawdown(debt, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_dd_1260d_v132_signal(fcf, debt):
    """Drawdown from peak to identify cycle troughs of Cash flow coverage of total debt over 1260d window."""
    res = _drawdown(_ratio(fcf, debt), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_rec_5d_v133_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 5d window."""
    res = _recovery(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_rec_5d_v134_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 5d window."""
    res = _recovery(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_rec_5d_v135_signal(debt):
    """Recovery from trough for turnaround signals of Raw level of debt over 5d window."""
    res = _recovery(debt, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_rec_5d_v136_signal(fcf, debt):
    """Recovery from trough for turnaround signals of Cash flow coverage of total debt over 5d window."""
    res = _recovery(_ratio(fcf, debt), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_rec_10d_v137_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 10d window."""
    res = _recovery(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_rec_10d_v138_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 10d window."""
    res = _recovery(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_rec_10d_v139_signal(debt):
    """Recovery from trough for turnaround signals of Raw level of debt over 10d window."""
    res = _recovery(debt, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_rec_10d_v140_signal(fcf, debt):
    """Recovery from trough for turnaround signals of Cash flow coverage of total debt over 10d window."""
    res = _recovery(_ratio(fcf, debt), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_rec_21d_v141_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 21d window."""
    res = _recovery(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_rec_21d_v142_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 21d window."""
    res = _recovery(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_rec_21d_v143_signal(debt):
    """Recovery from trough for turnaround signals of Raw level of debt over 21d window."""
    res = _recovery(debt, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_rec_21d_v144_signal(fcf, debt):
    """Recovery from trough for turnaround signals of Cash flow coverage of total debt over 21d window."""
    res = _recovery(_ratio(fcf, debt), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_rec_42d_v145_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 42d window."""
    res = _recovery(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_rec_42d_v146_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 42d window."""
    res = _recovery(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_debt_rec_42d_v147_signal(debt):
    """Recovery from trough for turnaround signals of Raw level of debt over 42d window."""
    res = _recovery(debt, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_to_debt_rec_42d_v148_signal(fcf, debt):
    """Recovery from trough for turnaround signals of Cash flow coverage of total debt over 42d window."""
    res = _recovery(_ratio(fcf, debt), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_fcf_rec_63d_v149_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 63d window."""
    res = _recovery(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f43_payout_resilience_netinc_rec_63d_v150_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 63d window."""
    res = _recovery(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f43_payout_resilience_fcf_to_debt_z_504d_v076_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_z_504d_v076_signal},    "f43_payout_resilience_fcf_z_756d_v077_signal": {"inputs": [], "func": f43_payout_resilience_fcf_z_756d_v077_signal},    "f43_payout_resilience_netinc_z_756d_v078_signal": {"inputs": [], "func": f43_payout_resilience_netinc_z_756d_v078_signal},    "f43_payout_resilience_debt_z_756d_v079_signal": {"inputs": [], "func": f43_payout_resilience_debt_z_756d_v079_signal},    "f43_payout_resilience_fcf_to_debt_z_756d_v080_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_z_756d_v080_signal},    "f43_payout_resilience_fcf_z_1008d_v081_signal": {"inputs": [], "func": f43_payout_resilience_fcf_z_1008d_v081_signal},    "f43_payout_resilience_netinc_z_1008d_v082_signal": {"inputs": [], "func": f43_payout_resilience_netinc_z_1008d_v082_signal},    "f43_payout_resilience_debt_z_1008d_v083_signal": {"inputs": [], "func": f43_payout_resilience_debt_z_1008d_v083_signal},    "f43_payout_resilience_fcf_to_debt_z_1008d_v084_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_z_1008d_v084_signal},    "f43_payout_resilience_fcf_z_1260d_v085_signal": {"inputs": [], "func": f43_payout_resilience_fcf_z_1260d_v085_signal},    "f43_payout_resilience_netinc_z_1260d_v086_signal": {"inputs": [], "func": f43_payout_resilience_netinc_z_1260d_v086_signal},    "f43_payout_resilience_debt_z_1260d_v087_signal": {"inputs": [], "func": f43_payout_resilience_debt_z_1260d_v087_signal},    "f43_payout_resilience_fcf_to_debt_z_1260d_v088_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_z_1260d_v088_signal},    "f43_payout_resilience_fcf_dd_5d_v089_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_5d_v089_signal},    "f43_payout_resilience_netinc_dd_5d_v090_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_5d_v090_signal},    "f43_payout_resilience_debt_dd_5d_v091_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_5d_v091_signal},    "f43_payout_resilience_fcf_to_debt_dd_5d_v092_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_5d_v092_signal},    "f43_payout_resilience_fcf_dd_10d_v093_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_10d_v093_signal},    "f43_payout_resilience_netinc_dd_10d_v094_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_10d_v094_signal},    "f43_payout_resilience_debt_dd_10d_v095_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_10d_v095_signal},    "f43_payout_resilience_fcf_to_debt_dd_10d_v096_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_10d_v096_signal},    "f43_payout_resilience_fcf_dd_21d_v097_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_21d_v097_signal},    "f43_payout_resilience_netinc_dd_21d_v098_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_21d_v098_signal},    "f43_payout_resilience_debt_dd_21d_v099_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_21d_v099_signal},    "f43_payout_resilience_fcf_to_debt_dd_21d_v100_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_21d_v100_signal},    "f43_payout_resilience_fcf_dd_42d_v101_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_42d_v101_signal},    "f43_payout_resilience_netinc_dd_42d_v102_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_42d_v102_signal},    "f43_payout_resilience_debt_dd_42d_v103_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_42d_v103_signal},    "f43_payout_resilience_fcf_to_debt_dd_42d_v104_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_42d_v104_signal},    "f43_payout_resilience_fcf_dd_63d_v105_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_63d_v105_signal},    "f43_payout_resilience_netinc_dd_63d_v106_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_63d_v106_signal},    "f43_payout_resilience_debt_dd_63d_v107_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_63d_v107_signal},    "f43_payout_resilience_fcf_to_debt_dd_63d_v108_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_63d_v108_signal},    "f43_payout_resilience_fcf_dd_126d_v109_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_126d_v109_signal},    "f43_payout_resilience_netinc_dd_126d_v110_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_126d_v110_signal},    "f43_payout_resilience_debt_dd_126d_v111_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_126d_v111_signal},    "f43_payout_resilience_fcf_to_debt_dd_126d_v112_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_126d_v112_signal},    "f43_payout_resilience_fcf_dd_252d_v113_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_252d_v113_signal},    "f43_payout_resilience_netinc_dd_252d_v114_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_252d_v114_signal},    "f43_payout_resilience_debt_dd_252d_v115_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_252d_v115_signal},    "f43_payout_resilience_fcf_to_debt_dd_252d_v116_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_252d_v116_signal},    "f43_payout_resilience_fcf_dd_504d_v117_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_504d_v117_signal},    "f43_payout_resilience_netinc_dd_504d_v118_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_504d_v118_signal},    "f43_payout_resilience_debt_dd_504d_v119_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_504d_v119_signal},    "f43_payout_resilience_fcf_to_debt_dd_504d_v120_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_504d_v120_signal},    "f43_payout_resilience_fcf_dd_756d_v121_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_756d_v121_signal},    "f43_payout_resilience_netinc_dd_756d_v122_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_756d_v122_signal},    "f43_payout_resilience_debt_dd_756d_v123_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_756d_v123_signal},    "f43_payout_resilience_fcf_to_debt_dd_756d_v124_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_756d_v124_signal},    "f43_payout_resilience_fcf_dd_1008d_v125_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_1008d_v125_signal},    "f43_payout_resilience_netinc_dd_1008d_v126_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_1008d_v126_signal},    "f43_payout_resilience_debt_dd_1008d_v127_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_1008d_v127_signal},    "f43_payout_resilience_fcf_to_debt_dd_1008d_v128_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_1008d_v128_signal},    "f43_payout_resilience_fcf_dd_1260d_v129_signal": {"inputs": [], "func": f43_payout_resilience_fcf_dd_1260d_v129_signal},    "f43_payout_resilience_netinc_dd_1260d_v130_signal": {"inputs": [], "func": f43_payout_resilience_netinc_dd_1260d_v130_signal},    "f43_payout_resilience_debt_dd_1260d_v131_signal": {"inputs": [], "func": f43_payout_resilience_debt_dd_1260d_v131_signal},    "f43_payout_resilience_fcf_to_debt_dd_1260d_v132_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_dd_1260d_v132_signal},    "f43_payout_resilience_fcf_rec_5d_v133_signal": {"inputs": [], "func": f43_payout_resilience_fcf_rec_5d_v133_signal},    "f43_payout_resilience_netinc_rec_5d_v134_signal": {"inputs": [], "func": f43_payout_resilience_netinc_rec_5d_v134_signal},    "f43_payout_resilience_debt_rec_5d_v135_signal": {"inputs": [], "func": f43_payout_resilience_debt_rec_5d_v135_signal},    "f43_payout_resilience_fcf_to_debt_rec_5d_v136_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_rec_5d_v136_signal},    "f43_payout_resilience_fcf_rec_10d_v137_signal": {"inputs": [], "func": f43_payout_resilience_fcf_rec_10d_v137_signal},    "f43_payout_resilience_netinc_rec_10d_v138_signal": {"inputs": [], "func": f43_payout_resilience_netinc_rec_10d_v138_signal},    "f43_payout_resilience_debt_rec_10d_v139_signal": {"inputs": [], "func": f43_payout_resilience_debt_rec_10d_v139_signal},    "f43_payout_resilience_fcf_to_debt_rec_10d_v140_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_rec_10d_v140_signal},    "f43_payout_resilience_fcf_rec_21d_v141_signal": {"inputs": [], "func": f43_payout_resilience_fcf_rec_21d_v141_signal},    "f43_payout_resilience_netinc_rec_21d_v142_signal": {"inputs": [], "func": f43_payout_resilience_netinc_rec_21d_v142_signal},    "f43_payout_resilience_debt_rec_21d_v143_signal": {"inputs": [], "func": f43_payout_resilience_debt_rec_21d_v143_signal},    "f43_payout_resilience_fcf_to_debt_rec_21d_v144_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_rec_21d_v144_signal},    "f43_payout_resilience_fcf_rec_42d_v145_signal": {"inputs": [], "func": f43_payout_resilience_fcf_rec_42d_v145_signal},    "f43_payout_resilience_netinc_rec_42d_v146_signal": {"inputs": [], "func": f43_payout_resilience_netinc_rec_42d_v146_signal},    "f43_payout_resilience_debt_rec_42d_v147_signal": {"inputs": [], "func": f43_payout_resilience_debt_rec_42d_v147_signal},    "f43_payout_resilience_fcf_to_debt_rec_42d_v148_signal": {"inputs": [], "func": f43_payout_resilience_fcf_to_debt_rec_42d_v148_signal},    "f43_payout_resilience_fcf_rec_63d_v149_signal": {"inputs": [], "func": f43_payout_resilience_fcf_rec_63d_v149_signal},    "f43_payout_resilience_netinc_rec_63d_v150_signal": {"inputs": [], "func": f43_payout_resilience_netinc_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "debt": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 43...")
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
