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

def f34_earnings_quality_cash_quality_z_504d_v076_signal(fcf, netinc):
    """Z-score for relative outlier detection of Free cash flow conversion of net income over 504d window."""
    res = _z(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_z_756d_v077_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 756d window."""
    res = _z(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_z_756d_v078_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 756d window."""
    res = _z(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_z_756d_v079_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 756d window."""
    res = _z(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_z_756d_v080_signal(fcf, netinc):
    """Z-score for relative outlier detection of Free cash flow conversion of net income over 756d window."""
    res = _z(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_z_1008d_v081_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 1008d window."""
    res = _z(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_z_1008d_v082_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 1008d window."""
    res = _z(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_z_1008d_v083_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 1008d window."""
    res = _z(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_z_1008d_v084_signal(fcf, netinc):
    """Z-score for relative outlier detection of Free cash flow conversion of net income over 1008d window."""
    res = _z(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_z_1260d_v085_signal(fcf):
    """Z-score for relative outlier detection of Raw level of fcf over 1260d window."""
    res = _z(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_z_1260d_v086_signal(netinc):
    """Z-score for relative outlier detection of Raw level of netinc over 1260d window."""
    res = _z(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_z_1260d_v087_signal(receivables):
    """Z-score for relative outlier detection of Raw level of receivables over 1260d window."""
    res = _z(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_z_1260d_v088_signal(fcf, netinc):
    """Z-score for relative outlier detection of Free cash flow conversion of net income over 1260d window."""
    res = _z(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_5d_v089_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 5d window."""
    res = _drawdown(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_5d_v090_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 5d window."""
    res = _drawdown(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_5d_v091_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 5d window."""
    res = _drawdown(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_5d_v092_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 5d window."""
    res = _drawdown(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_10d_v093_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 10d window."""
    res = _drawdown(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_10d_v094_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 10d window."""
    res = _drawdown(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_10d_v095_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 10d window."""
    res = _drawdown(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_10d_v096_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 10d window."""
    res = _drawdown(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_21d_v097_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 21d window."""
    res = _drawdown(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_21d_v098_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 21d window."""
    res = _drawdown(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_21d_v099_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 21d window."""
    res = _drawdown(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_21d_v100_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 21d window."""
    res = _drawdown(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_42d_v101_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 42d window."""
    res = _drawdown(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_42d_v102_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 42d window."""
    res = _drawdown(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_42d_v103_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 42d window."""
    res = _drawdown(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_42d_v104_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 42d window."""
    res = _drawdown(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_63d_v105_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 63d window."""
    res = _drawdown(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_63d_v106_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 63d window."""
    res = _drawdown(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_63d_v107_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 63d window."""
    res = _drawdown(receivables, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_63d_v108_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 63d window."""
    res = _drawdown(_ratio(fcf, netinc), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_126d_v109_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 126d window."""
    res = _drawdown(fcf, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_126d_v110_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 126d window."""
    res = _drawdown(netinc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_126d_v111_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 126d window."""
    res = _drawdown(receivables, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_126d_v112_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 126d window."""
    res = _drawdown(_ratio(fcf, netinc), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_252d_v113_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 252d window."""
    res = _drawdown(fcf, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_252d_v114_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 252d window."""
    res = _drawdown(netinc, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_252d_v115_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 252d window."""
    res = _drawdown(receivables, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_252d_v116_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 252d window."""
    res = _drawdown(_ratio(fcf, netinc), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_504d_v117_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 504d window."""
    res = _drawdown(fcf, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_504d_v118_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 504d window."""
    res = _drawdown(netinc, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_504d_v119_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 504d window."""
    res = _drawdown(receivables, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_504d_v120_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 504d window."""
    res = _drawdown(_ratio(fcf, netinc), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_756d_v121_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 756d window."""
    res = _drawdown(fcf, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_756d_v122_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 756d window."""
    res = _drawdown(netinc, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_756d_v123_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 756d window."""
    res = _drawdown(receivables, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_756d_v124_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 756d window."""
    res = _drawdown(_ratio(fcf, netinc), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_1008d_v125_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 1008d window."""
    res = _drawdown(fcf, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_1008d_v126_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 1008d window."""
    res = _drawdown(netinc, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_1008d_v127_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 1008d window."""
    res = _drawdown(receivables, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_1008d_v128_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 1008d window."""
    res = _drawdown(_ratio(fcf, netinc), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_dd_1260d_v129_signal(fcf):
    """Drawdown from peak to identify cycle troughs of Raw level of fcf over 1260d window."""
    res = _drawdown(fcf, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_dd_1260d_v130_signal(netinc):
    """Drawdown from peak to identify cycle troughs of Raw level of netinc over 1260d window."""
    res = _drawdown(netinc, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_dd_1260d_v131_signal(receivables):
    """Drawdown from peak to identify cycle troughs of Raw level of receivables over 1260d window."""
    res = _drawdown(receivables, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_dd_1260d_v132_signal(fcf, netinc):
    """Drawdown from peak to identify cycle troughs of Free cash flow conversion of net income over 1260d window."""
    res = _drawdown(_ratio(fcf, netinc), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_rec_5d_v133_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 5d window."""
    res = _recovery(fcf, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_rec_5d_v134_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 5d window."""
    res = _recovery(netinc, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_rec_5d_v135_signal(receivables):
    """Recovery from trough for turnaround signals of Raw level of receivables over 5d window."""
    res = _recovery(receivables, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_rec_5d_v136_signal(fcf, netinc):
    """Recovery from trough for turnaround signals of Free cash flow conversion of net income over 5d window."""
    res = _recovery(_ratio(fcf, netinc), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_rec_10d_v137_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 10d window."""
    res = _recovery(fcf, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_rec_10d_v138_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 10d window."""
    res = _recovery(netinc, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_rec_10d_v139_signal(receivables):
    """Recovery from trough for turnaround signals of Raw level of receivables over 10d window."""
    res = _recovery(receivables, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_rec_10d_v140_signal(fcf, netinc):
    """Recovery from trough for turnaround signals of Free cash flow conversion of net income over 10d window."""
    res = _recovery(_ratio(fcf, netinc), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_rec_21d_v141_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 21d window."""
    res = _recovery(fcf, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_rec_21d_v142_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 21d window."""
    res = _recovery(netinc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_rec_21d_v143_signal(receivables):
    """Recovery from trough for turnaround signals of Raw level of receivables over 21d window."""
    res = _recovery(receivables, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_rec_21d_v144_signal(fcf, netinc):
    """Recovery from trough for turnaround signals of Free cash flow conversion of net income over 21d window."""
    res = _recovery(_ratio(fcf, netinc), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_rec_42d_v145_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 42d window."""
    res = _recovery(fcf, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_rec_42d_v146_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 42d window."""
    res = _recovery(netinc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_receivables_rec_42d_v147_signal(receivables):
    """Recovery from trough for turnaround signals of Raw level of receivables over 42d window."""
    res = _recovery(receivables, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_cash_quality_rec_42d_v148_signal(fcf, netinc):
    """Recovery from trough for turnaround signals of Free cash flow conversion of net income over 42d window."""
    res = _recovery(_ratio(fcf, netinc), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_fcf_rec_63d_v149_signal(fcf):
    """Recovery from trough for turnaround signals of Raw level of fcf over 63d window."""
    res = _recovery(fcf, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f34_earnings_quality_netinc_rec_63d_v150_signal(netinc):
    """Recovery from trough for turnaround signals of Raw level of netinc over 63d window."""
    res = _recovery(netinc, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f34_earnings_quality_cash_quality_z_504d_v076_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_z_504d_v076_signal},    "f34_earnings_quality_fcf_z_756d_v077_signal": {"inputs": [], "func": f34_earnings_quality_fcf_z_756d_v077_signal},    "f34_earnings_quality_netinc_z_756d_v078_signal": {"inputs": [], "func": f34_earnings_quality_netinc_z_756d_v078_signal},    "f34_earnings_quality_receivables_z_756d_v079_signal": {"inputs": [], "func": f34_earnings_quality_receivables_z_756d_v079_signal},    "f34_earnings_quality_cash_quality_z_756d_v080_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_z_756d_v080_signal},    "f34_earnings_quality_fcf_z_1008d_v081_signal": {"inputs": [], "func": f34_earnings_quality_fcf_z_1008d_v081_signal},    "f34_earnings_quality_netinc_z_1008d_v082_signal": {"inputs": [], "func": f34_earnings_quality_netinc_z_1008d_v082_signal},    "f34_earnings_quality_receivables_z_1008d_v083_signal": {"inputs": [], "func": f34_earnings_quality_receivables_z_1008d_v083_signal},    "f34_earnings_quality_cash_quality_z_1008d_v084_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_z_1008d_v084_signal},    "f34_earnings_quality_fcf_z_1260d_v085_signal": {"inputs": [], "func": f34_earnings_quality_fcf_z_1260d_v085_signal},    "f34_earnings_quality_netinc_z_1260d_v086_signal": {"inputs": [], "func": f34_earnings_quality_netinc_z_1260d_v086_signal},    "f34_earnings_quality_receivables_z_1260d_v087_signal": {"inputs": [], "func": f34_earnings_quality_receivables_z_1260d_v087_signal},    "f34_earnings_quality_cash_quality_z_1260d_v088_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_z_1260d_v088_signal},    "f34_earnings_quality_fcf_dd_5d_v089_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_5d_v089_signal},    "f34_earnings_quality_netinc_dd_5d_v090_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_5d_v090_signal},    "f34_earnings_quality_receivables_dd_5d_v091_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_5d_v091_signal},    "f34_earnings_quality_cash_quality_dd_5d_v092_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_5d_v092_signal},    "f34_earnings_quality_fcf_dd_10d_v093_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_10d_v093_signal},    "f34_earnings_quality_netinc_dd_10d_v094_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_10d_v094_signal},    "f34_earnings_quality_receivables_dd_10d_v095_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_10d_v095_signal},    "f34_earnings_quality_cash_quality_dd_10d_v096_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_10d_v096_signal},    "f34_earnings_quality_fcf_dd_21d_v097_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_21d_v097_signal},    "f34_earnings_quality_netinc_dd_21d_v098_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_21d_v098_signal},    "f34_earnings_quality_receivables_dd_21d_v099_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_21d_v099_signal},    "f34_earnings_quality_cash_quality_dd_21d_v100_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_21d_v100_signal},    "f34_earnings_quality_fcf_dd_42d_v101_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_42d_v101_signal},    "f34_earnings_quality_netinc_dd_42d_v102_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_42d_v102_signal},    "f34_earnings_quality_receivables_dd_42d_v103_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_42d_v103_signal},    "f34_earnings_quality_cash_quality_dd_42d_v104_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_42d_v104_signal},    "f34_earnings_quality_fcf_dd_63d_v105_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_63d_v105_signal},    "f34_earnings_quality_netinc_dd_63d_v106_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_63d_v106_signal},    "f34_earnings_quality_receivables_dd_63d_v107_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_63d_v107_signal},    "f34_earnings_quality_cash_quality_dd_63d_v108_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_63d_v108_signal},    "f34_earnings_quality_fcf_dd_126d_v109_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_126d_v109_signal},    "f34_earnings_quality_netinc_dd_126d_v110_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_126d_v110_signal},    "f34_earnings_quality_receivables_dd_126d_v111_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_126d_v111_signal},    "f34_earnings_quality_cash_quality_dd_126d_v112_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_126d_v112_signal},    "f34_earnings_quality_fcf_dd_252d_v113_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_252d_v113_signal},    "f34_earnings_quality_netinc_dd_252d_v114_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_252d_v114_signal},    "f34_earnings_quality_receivables_dd_252d_v115_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_252d_v115_signal},    "f34_earnings_quality_cash_quality_dd_252d_v116_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_252d_v116_signal},    "f34_earnings_quality_fcf_dd_504d_v117_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_504d_v117_signal},    "f34_earnings_quality_netinc_dd_504d_v118_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_504d_v118_signal},    "f34_earnings_quality_receivables_dd_504d_v119_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_504d_v119_signal},    "f34_earnings_quality_cash_quality_dd_504d_v120_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_504d_v120_signal},    "f34_earnings_quality_fcf_dd_756d_v121_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_756d_v121_signal},    "f34_earnings_quality_netinc_dd_756d_v122_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_756d_v122_signal},    "f34_earnings_quality_receivables_dd_756d_v123_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_756d_v123_signal},    "f34_earnings_quality_cash_quality_dd_756d_v124_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_756d_v124_signal},    "f34_earnings_quality_fcf_dd_1008d_v125_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_1008d_v125_signal},    "f34_earnings_quality_netinc_dd_1008d_v126_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_1008d_v126_signal},    "f34_earnings_quality_receivables_dd_1008d_v127_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_1008d_v127_signal},    "f34_earnings_quality_cash_quality_dd_1008d_v128_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_1008d_v128_signal},    "f34_earnings_quality_fcf_dd_1260d_v129_signal": {"inputs": [], "func": f34_earnings_quality_fcf_dd_1260d_v129_signal},    "f34_earnings_quality_netinc_dd_1260d_v130_signal": {"inputs": [], "func": f34_earnings_quality_netinc_dd_1260d_v130_signal},    "f34_earnings_quality_receivables_dd_1260d_v131_signal": {"inputs": [], "func": f34_earnings_quality_receivables_dd_1260d_v131_signal},    "f34_earnings_quality_cash_quality_dd_1260d_v132_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_dd_1260d_v132_signal},    "f34_earnings_quality_fcf_rec_5d_v133_signal": {"inputs": [], "func": f34_earnings_quality_fcf_rec_5d_v133_signal},    "f34_earnings_quality_netinc_rec_5d_v134_signal": {"inputs": [], "func": f34_earnings_quality_netinc_rec_5d_v134_signal},    "f34_earnings_quality_receivables_rec_5d_v135_signal": {"inputs": [], "func": f34_earnings_quality_receivables_rec_5d_v135_signal},    "f34_earnings_quality_cash_quality_rec_5d_v136_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_rec_5d_v136_signal},    "f34_earnings_quality_fcf_rec_10d_v137_signal": {"inputs": [], "func": f34_earnings_quality_fcf_rec_10d_v137_signal},    "f34_earnings_quality_netinc_rec_10d_v138_signal": {"inputs": [], "func": f34_earnings_quality_netinc_rec_10d_v138_signal},    "f34_earnings_quality_receivables_rec_10d_v139_signal": {"inputs": [], "func": f34_earnings_quality_receivables_rec_10d_v139_signal},    "f34_earnings_quality_cash_quality_rec_10d_v140_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_rec_10d_v140_signal},    "f34_earnings_quality_fcf_rec_21d_v141_signal": {"inputs": [], "func": f34_earnings_quality_fcf_rec_21d_v141_signal},    "f34_earnings_quality_netinc_rec_21d_v142_signal": {"inputs": [], "func": f34_earnings_quality_netinc_rec_21d_v142_signal},    "f34_earnings_quality_receivables_rec_21d_v143_signal": {"inputs": [], "func": f34_earnings_quality_receivables_rec_21d_v143_signal},    "f34_earnings_quality_cash_quality_rec_21d_v144_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_rec_21d_v144_signal},    "f34_earnings_quality_fcf_rec_42d_v145_signal": {"inputs": [], "func": f34_earnings_quality_fcf_rec_42d_v145_signal},    "f34_earnings_quality_netinc_rec_42d_v146_signal": {"inputs": [], "func": f34_earnings_quality_netinc_rec_42d_v146_signal},    "f34_earnings_quality_receivables_rec_42d_v147_signal": {"inputs": [], "func": f34_earnings_quality_receivables_rec_42d_v147_signal},    "f34_earnings_quality_cash_quality_rec_42d_v148_signal": {"inputs": [], "func": f34_earnings_quality_cash_quality_rec_42d_v148_signal},    "f34_earnings_quality_fcf_rec_63d_v149_signal": {"inputs": [], "func": f34_earnings_quality_fcf_rec_63d_v149_signal},    "f34_earnings_quality_netinc_rec_63d_v150_signal": {"inputs": [], "func": f34_earnings_quality_netinc_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 34...")
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
