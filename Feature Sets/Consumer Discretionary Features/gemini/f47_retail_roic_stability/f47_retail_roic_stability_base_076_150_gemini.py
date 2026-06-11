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

def f47_retail_roic_stability_roic_z_z_504d_v076_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 504d window."""
    res = _z(_z(roic, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_756d_v077_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 756d window."""
    res = _z(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_756d_v078_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 756d window."""
    res = _z(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_756d_v079_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 756d window."""
    res = _z(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_756d_v080_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 756d window."""
    res = _z(_z(roic, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_1008d_v081_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 1008d window."""
    res = _z(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_1008d_v082_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 1008d window."""
    res = _z(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_1008d_v083_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 1008d window."""
    res = _z(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_1008d_v084_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 1008d window."""
    res = _z(_z(roic, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_1260d_v085_signal(roic):
    """Z-score for relative outlier detection of Raw level of roic over 1260d window."""
    res = _z(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_z_1260d_v086_signal(ebit):
    """Z-score for relative outlier detection of Raw level of ebit over 1260d window."""
    res = _z(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_z_1260d_v087_signal(invcap):
    """Z-score for relative outlier detection of Raw level of invcap over 1260d window."""
    res = _z(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_z_1260d_v088_signal(roic):
    """Z-score for relative outlier detection of Z-score of ROIC relative to 1y history over 1260d window."""
    res = _z(_z(roic, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_5d_v089_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 5d window."""
    res = _drawdown(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_5d_v090_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 5d window."""
    res = _drawdown(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_5d_v091_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 5d window."""
    res = _drawdown(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_5d_v092_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 5d window."""
    res = _drawdown(_z(roic, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_10d_v093_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 10d window."""
    res = _drawdown(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_10d_v094_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 10d window."""
    res = _drawdown(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_10d_v095_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 10d window."""
    res = _drawdown(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_10d_v096_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 10d window."""
    res = _drawdown(_z(roic, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_21d_v097_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 21d window."""
    res = _drawdown(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_21d_v098_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 21d window."""
    res = _drawdown(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_21d_v099_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 21d window."""
    res = _drawdown(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_21d_v100_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 21d window."""
    res = _drawdown(_z(roic, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_42d_v101_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 42d window."""
    res = _drawdown(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_42d_v102_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 42d window."""
    res = _drawdown(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_42d_v103_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 42d window."""
    res = _drawdown(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_42d_v104_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 42d window."""
    res = _drawdown(_z(roic, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_63d_v105_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 63d window."""
    res = _drawdown(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_63d_v106_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 63d window."""
    res = _drawdown(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_63d_v107_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 63d window."""
    res = _drawdown(invcap, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_63d_v108_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 63d window."""
    res = _drawdown(_z(roic, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_126d_v109_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 126d window."""
    res = _drawdown(roic, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_126d_v110_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 126d window."""
    res = _drawdown(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_126d_v111_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 126d window."""
    res = _drawdown(invcap, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_126d_v112_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 126d window."""
    res = _drawdown(_z(roic, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_252d_v113_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 252d window."""
    res = _drawdown(roic, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_252d_v114_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 252d window."""
    res = _drawdown(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_252d_v115_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 252d window."""
    res = _drawdown(invcap, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_252d_v116_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 252d window."""
    res = _drawdown(_z(roic, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_504d_v117_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 504d window."""
    res = _drawdown(roic, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_504d_v118_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 504d window."""
    res = _drawdown(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_504d_v119_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 504d window."""
    res = _drawdown(invcap, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_504d_v120_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 504d window."""
    res = _drawdown(_z(roic, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_756d_v121_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 756d window."""
    res = _drawdown(roic, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_756d_v122_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 756d window."""
    res = _drawdown(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_756d_v123_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 756d window."""
    res = _drawdown(invcap, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_756d_v124_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 756d window."""
    res = _drawdown(_z(roic, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_1008d_v125_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 1008d window."""
    res = _drawdown(roic, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_1008d_v126_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 1008d window."""
    res = _drawdown(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_1008d_v127_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 1008d window."""
    res = _drawdown(invcap, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_1008d_v128_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 1008d window."""
    res = _drawdown(_z(roic, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_dd_1260d_v129_signal(roic):
    """Drawdown from peak to identify cycle troughs of Raw level of roic over 1260d window."""
    res = _drawdown(roic, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_dd_1260d_v130_signal(ebit):
    """Drawdown from peak to identify cycle troughs of Raw level of ebit over 1260d window."""
    res = _drawdown(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_dd_1260d_v131_signal(invcap):
    """Drawdown from peak to identify cycle troughs of Raw level of invcap over 1260d window."""
    res = _drawdown(invcap, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_dd_1260d_v132_signal(roic):
    """Drawdown from peak to identify cycle troughs of Z-score of ROIC relative to 1y history over 1260d window."""
    res = _drawdown(_z(roic, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_rec_5d_v133_signal(roic):
    """Recovery from trough for turnaround signals of Raw level of roic over 5d window."""
    res = _recovery(roic, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_rec_5d_v134_signal(ebit):
    """Recovery from trough for turnaround signals of Raw level of ebit over 5d window."""
    res = _recovery(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_rec_5d_v135_signal(invcap):
    """Recovery from trough for turnaround signals of Raw level of invcap over 5d window."""
    res = _recovery(invcap, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_rec_5d_v136_signal(roic):
    """Recovery from trough for turnaround signals of Z-score of ROIC relative to 1y history over 5d window."""
    res = _recovery(_z(roic, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_rec_10d_v137_signal(roic):
    """Recovery from trough for turnaround signals of Raw level of roic over 10d window."""
    res = _recovery(roic, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_rec_10d_v138_signal(ebit):
    """Recovery from trough for turnaround signals of Raw level of ebit over 10d window."""
    res = _recovery(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_rec_10d_v139_signal(invcap):
    """Recovery from trough for turnaround signals of Raw level of invcap over 10d window."""
    res = _recovery(invcap, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_rec_10d_v140_signal(roic):
    """Recovery from trough for turnaround signals of Z-score of ROIC relative to 1y history over 10d window."""
    res = _recovery(_z(roic, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_rec_21d_v141_signal(roic):
    """Recovery from trough for turnaround signals of Raw level of roic over 21d window."""
    res = _recovery(roic, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_rec_21d_v142_signal(ebit):
    """Recovery from trough for turnaround signals of Raw level of ebit over 21d window."""
    res = _recovery(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_rec_21d_v143_signal(invcap):
    """Recovery from trough for turnaround signals of Raw level of invcap over 21d window."""
    res = _recovery(invcap, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_rec_21d_v144_signal(roic):
    """Recovery from trough for turnaround signals of Z-score of ROIC relative to 1y history over 21d window."""
    res = _recovery(_z(roic, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_rec_42d_v145_signal(roic):
    """Recovery from trough for turnaround signals of Raw level of roic over 42d window."""
    res = _recovery(roic, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_rec_42d_v146_signal(ebit):
    """Recovery from trough for turnaround signals of Raw level of ebit over 42d window."""
    res = _recovery(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_invcap_rec_42d_v147_signal(invcap):
    """Recovery from trough for turnaround signals of Raw level of invcap over 42d window."""
    res = _recovery(invcap, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_z_rec_42d_v148_signal(roic):
    """Recovery from trough for turnaround signals of Z-score of ROIC relative to 1y history over 42d window."""
    res = _recovery(_z(roic, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_roic_rec_63d_v149_signal(roic):
    """Recovery from trough for turnaround signals of Raw level of roic over 63d window."""
    res = _recovery(roic, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f47_retail_roic_stability_ebit_rec_63d_v150_signal(ebit):
    """Recovery from trough for turnaround signals of Raw level of ebit over 63d window."""
    res = _recovery(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f47_retail_roic_stability_roic_z_z_504d_v076_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_504d_v076_signal},    "f47_retail_roic_stability_roic_z_756d_v077_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_756d_v077_signal},    "f47_retail_roic_stability_ebit_z_756d_v078_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_756d_v078_signal},    "f47_retail_roic_stability_invcap_z_756d_v079_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_756d_v079_signal},    "f47_retail_roic_stability_roic_z_z_756d_v080_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_756d_v080_signal},    "f47_retail_roic_stability_roic_z_1008d_v081_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_1008d_v081_signal},    "f47_retail_roic_stability_ebit_z_1008d_v082_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_1008d_v082_signal},    "f47_retail_roic_stability_invcap_z_1008d_v083_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_1008d_v083_signal},    "f47_retail_roic_stability_roic_z_z_1008d_v084_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_1008d_v084_signal},    "f47_retail_roic_stability_roic_z_1260d_v085_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_1260d_v085_signal},    "f47_retail_roic_stability_ebit_z_1260d_v086_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_z_1260d_v086_signal},    "f47_retail_roic_stability_invcap_z_1260d_v087_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_z_1260d_v087_signal},    "f47_retail_roic_stability_roic_z_z_1260d_v088_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_z_1260d_v088_signal},    "f47_retail_roic_stability_roic_dd_5d_v089_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_5d_v089_signal},    "f47_retail_roic_stability_ebit_dd_5d_v090_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_5d_v090_signal},    "f47_retail_roic_stability_invcap_dd_5d_v091_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_5d_v091_signal},    "f47_retail_roic_stability_roic_z_dd_5d_v092_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_5d_v092_signal},    "f47_retail_roic_stability_roic_dd_10d_v093_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_10d_v093_signal},    "f47_retail_roic_stability_ebit_dd_10d_v094_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_10d_v094_signal},    "f47_retail_roic_stability_invcap_dd_10d_v095_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_10d_v095_signal},    "f47_retail_roic_stability_roic_z_dd_10d_v096_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_10d_v096_signal},    "f47_retail_roic_stability_roic_dd_21d_v097_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_21d_v097_signal},    "f47_retail_roic_stability_ebit_dd_21d_v098_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_21d_v098_signal},    "f47_retail_roic_stability_invcap_dd_21d_v099_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_21d_v099_signal},    "f47_retail_roic_stability_roic_z_dd_21d_v100_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_21d_v100_signal},    "f47_retail_roic_stability_roic_dd_42d_v101_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_42d_v101_signal},    "f47_retail_roic_stability_ebit_dd_42d_v102_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_42d_v102_signal},    "f47_retail_roic_stability_invcap_dd_42d_v103_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_42d_v103_signal},    "f47_retail_roic_stability_roic_z_dd_42d_v104_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_42d_v104_signal},    "f47_retail_roic_stability_roic_dd_63d_v105_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_63d_v105_signal},    "f47_retail_roic_stability_ebit_dd_63d_v106_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_63d_v106_signal},    "f47_retail_roic_stability_invcap_dd_63d_v107_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_63d_v107_signal},    "f47_retail_roic_stability_roic_z_dd_63d_v108_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_63d_v108_signal},    "f47_retail_roic_stability_roic_dd_126d_v109_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_126d_v109_signal},    "f47_retail_roic_stability_ebit_dd_126d_v110_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_126d_v110_signal},    "f47_retail_roic_stability_invcap_dd_126d_v111_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_126d_v111_signal},    "f47_retail_roic_stability_roic_z_dd_126d_v112_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_126d_v112_signal},    "f47_retail_roic_stability_roic_dd_252d_v113_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_252d_v113_signal},    "f47_retail_roic_stability_ebit_dd_252d_v114_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_252d_v114_signal},    "f47_retail_roic_stability_invcap_dd_252d_v115_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_252d_v115_signal},    "f47_retail_roic_stability_roic_z_dd_252d_v116_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_252d_v116_signal},    "f47_retail_roic_stability_roic_dd_504d_v117_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_504d_v117_signal},    "f47_retail_roic_stability_ebit_dd_504d_v118_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_504d_v118_signal},    "f47_retail_roic_stability_invcap_dd_504d_v119_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_504d_v119_signal},    "f47_retail_roic_stability_roic_z_dd_504d_v120_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_504d_v120_signal},    "f47_retail_roic_stability_roic_dd_756d_v121_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_756d_v121_signal},    "f47_retail_roic_stability_ebit_dd_756d_v122_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_756d_v122_signal},    "f47_retail_roic_stability_invcap_dd_756d_v123_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_756d_v123_signal},    "f47_retail_roic_stability_roic_z_dd_756d_v124_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_756d_v124_signal},    "f47_retail_roic_stability_roic_dd_1008d_v125_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_1008d_v125_signal},    "f47_retail_roic_stability_ebit_dd_1008d_v126_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_1008d_v126_signal},    "f47_retail_roic_stability_invcap_dd_1008d_v127_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_1008d_v127_signal},    "f47_retail_roic_stability_roic_z_dd_1008d_v128_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_1008d_v128_signal},    "f47_retail_roic_stability_roic_dd_1260d_v129_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_dd_1260d_v129_signal},    "f47_retail_roic_stability_ebit_dd_1260d_v130_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_dd_1260d_v130_signal},    "f47_retail_roic_stability_invcap_dd_1260d_v131_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_dd_1260d_v131_signal},    "f47_retail_roic_stability_roic_z_dd_1260d_v132_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_dd_1260d_v132_signal},    "f47_retail_roic_stability_roic_rec_5d_v133_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_rec_5d_v133_signal},    "f47_retail_roic_stability_ebit_rec_5d_v134_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_rec_5d_v134_signal},    "f47_retail_roic_stability_invcap_rec_5d_v135_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_rec_5d_v135_signal},    "f47_retail_roic_stability_roic_z_rec_5d_v136_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_rec_5d_v136_signal},    "f47_retail_roic_stability_roic_rec_10d_v137_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_rec_10d_v137_signal},    "f47_retail_roic_stability_ebit_rec_10d_v138_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_rec_10d_v138_signal},    "f47_retail_roic_stability_invcap_rec_10d_v139_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_rec_10d_v139_signal},    "f47_retail_roic_stability_roic_z_rec_10d_v140_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_rec_10d_v140_signal},    "f47_retail_roic_stability_roic_rec_21d_v141_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_rec_21d_v141_signal},    "f47_retail_roic_stability_ebit_rec_21d_v142_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_rec_21d_v142_signal},    "f47_retail_roic_stability_invcap_rec_21d_v143_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_rec_21d_v143_signal},    "f47_retail_roic_stability_roic_z_rec_21d_v144_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_rec_21d_v144_signal},    "f47_retail_roic_stability_roic_rec_42d_v145_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_rec_42d_v145_signal},    "f47_retail_roic_stability_ebit_rec_42d_v146_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_rec_42d_v146_signal},    "f47_retail_roic_stability_invcap_rec_42d_v147_signal": {"inputs": [], "func": f47_retail_roic_stability_invcap_rec_42d_v147_signal},    "f47_retail_roic_stability_roic_z_rec_42d_v148_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_z_rec_42d_v148_signal},    "f47_retail_roic_stability_roic_rec_63d_v149_signal": {"inputs": [], "func": f47_retail_roic_stability_roic_rec_63d_v149_signal},    "f47_retail_roic_stability_ebit_rec_63d_v150_signal": {"inputs": [], "func": f47_retail_roic_stability_ebit_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 47...")
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
