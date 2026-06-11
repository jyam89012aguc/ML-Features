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

def f05_operating_leverage_operating_alpha_z_504d_v076_signal(ebitda, revenue, sgna):
    """Z-score for relative outlier detection of Incremental margin expansion net of SG&A load over 504d window."""
    res = _z(ebitda / revenue - (sgna / revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_z_756d_v077_signal(ebitda):
    """Z-score for relative outlier detection of Raw level of ebitda over 756d window."""
    res = _z(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_z_756d_v078_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_z_756d_v079_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 756d window."""
    res = _z(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_z_756d_v080_signal(ebitda, revenue, sgna):
    """Z-score for relative outlier detection of Incremental margin expansion net of SG&A load over 756d window."""
    res = _z(ebitda / revenue - (sgna / revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_z_1008d_v081_signal(ebitda):
    """Z-score for relative outlier detection of Raw level of ebitda over 1008d window."""
    res = _z(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_z_1008d_v082_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_z_1008d_v083_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 1008d window."""
    res = _z(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_z_1008d_v084_signal(ebitda, revenue, sgna):
    """Z-score for relative outlier detection of Incremental margin expansion net of SG&A load over 1008d window."""
    res = _z(ebitda / revenue - (sgna / revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_z_1260d_v085_signal(ebitda):
    """Z-score for relative outlier detection of Raw level of ebitda over 1260d window."""
    res = _z(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_z_1260d_v086_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_z_1260d_v087_signal(sgna):
    """Z-score for relative outlier detection of Raw level of sgna over 1260d window."""
    res = _z(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_z_1260d_v088_signal(ebitda, revenue, sgna):
    """Z-score for relative outlier detection of Incremental margin expansion net of SG&A load over 1260d window."""
    res = _z(ebitda / revenue - (sgna / revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_5d_v089_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 5d window."""
    res = _drawdown(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_5d_v090_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_5d_v091_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 5d window."""
    res = _drawdown(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_5d_v092_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 5d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_10d_v093_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 10d window."""
    res = _drawdown(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_10d_v094_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_10d_v095_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 10d window."""
    res = _drawdown(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_10d_v096_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 10d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_21d_v097_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 21d window."""
    res = _drawdown(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_21d_v098_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_21d_v099_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 21d window."""
    res = _drawdown(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_21d_v100_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 21d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_42d_v101_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 42d window."""
    res = _drawdown(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_42d_v102_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_42d_v103_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 42d window."""
    res = _drawdown(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_42d_v104_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 42d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_63d_v105_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 63d window."""
    res = _drawdown(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_63d_v106_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_63d_v107_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 63d window."""
    res = _drawdown(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_63d_v108_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 63d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_126d_v109_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 126d window."""
    res = _drawdown(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_126d_v110_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 126d window."""
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_126d_v111_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 126d window."""
    res = _drawdown(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_126d_v112_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 126d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_252d_v113_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 252d window."""
    res = _drawdown(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_252d_v114_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 252d window."""
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_252d_v115_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 252d window."""
    res = _drawdown(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_252d_v116_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 252d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_504d_v117_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 504d window."""
    res = _drawdown(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_504d_v118_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 504d window."""
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_504d_v119_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 504d window."""
    res = _drawdown(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_504d_v120_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 504d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_756d_v121_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 756d window."""
    res = _drawdown(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_756d_v122_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 756d window."""
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_756d_v123_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 756d window."""
    res = _drawdown(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_756d_v124_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 756d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_1008d_v125_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 1008d window."""
    res = _drawdown(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_1008d_v126_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1008d window."""
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_1008d_v127_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 1008d window."""
    res = _drawdown(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_1008d_v128_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 1008d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_dd_1260d_v129_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 1260d window."""
    res = _drawdown(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_dd_1260d_v130_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1260d window."""
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_dd_1260d_v131_signal(sgna):
    """Drawdown from peak to identify cycle troughs of Raw level of sgna over 1260d window."""
    res = _drawdown(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_dd_1260d_v132_signal(ebitda, revenue, sgna):
    """Drawdown from peak to identify cycle troughs of Incremental margin expansion net of SG&A load over 1260d window."""
    res = _drawdown(ebitda / revenue - (sgna / revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_rec_5d_v133_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 5d window."""
    res = _recovery(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_rec_5d_v134_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 5d window."""
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_rec_5d_v135_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 5d window."""
    res = _recovery(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_rec_5d_v136_signal(ebitda, revenue, sgna):
    """Recovery from trough for turnaround signals of Incremental margin expansion net of SG&A load over 5d window."""
    res = _recovery(ebitda / revenue - (sgna / revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_rec_10d_v137_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 10d window."""
    res = _recovery(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_rec_10d_v138_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 10d window."""
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_rec_10d_v139_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 10d window."""
    res = _recovery(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_rec_10d_v140_signal(ebitda, revenue, sgna):
    """Recovery from trough for turnaround signals of Incremental margin expansion net of SG&A load over 10d window."""
    res = _recovery(ebitda / revenue - (sgna / revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_rec_21d_v141_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 21d window."""
    res = _recovery(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_rec_21d_v142_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 21d window."""
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_rec_21d_v143_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 21d window."""
    res = _recovery(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_rec_21d_v144_signal(ebitda, revenue, sgna):
    """Recovery from trough for turnaround signals of Incremental margin expansion net of SG&A load over 21d window."""
    res = _recovery(ebitda / revenue - (sgna / revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_rec_42d_v145_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 42d window."""
    res = _recovery(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_rec_42d_v146_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 42d window."""
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_sgna_rec_42d_v147_signal(sgna):
    """Recovery from trough for turnaround signals of Raw level of sgna over 42d window."""
    res = _recovery(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_operating_alpha_rec_42d_v148_signal(ebitda, revenue, sgna):
    """Recovery from trough for turnaround signals of Incremental margin expansion net of SG&A load over 42d window."""
    res = _recovery(ebitda / revenue - (sgna / revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_ebitda_rec_63d_v149_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 63d window."""
    res = _recovery(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05_operating_leverage_revenue_rec_63d_v150_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 63d window."""
    res = _recovery(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f05_operating_leverage_operating_alpha_z_504d_v076_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_z_504d_v076_signal},    "f05_operating_leverage_ebitda_z_756d_v077_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_z_756d_v077_signal},    "f05_operating_leverage_revenue_z_756d_v078_signal": {"inputs": [], "func": f05_operating_leverage_revenue_z_756d_v078_signal},    "f05_operating_leverage_sgna_z_756d_v079_signal": {"inputs": [], "func": f05_operating_leverage_sgna_z_756d_v079_signal},    "f05_operating_leverage_operating_alpha_z_756d_v080_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_z_756d_v080_signal},    "f05_operating_leverage_ebitda_z_1008d_v081_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_z_1008d_v081_signal},    "f05_operating_leverage_revenue_z_1008d_v082_signal": {"inputs": [], "func": f05_operating_leverage_revenue_z_1008d_v082_signal},    "f05_operating_leverage_sgna_z_1008d_v083_signal": {"inputs": [], "func": f05_operating_leverage_sgna_z_1008d_v083_signal},    "f05_operating_leverage_operating_alpha_z_1008d_v084_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_z_1008d_v084_signal},    "f05_operating_leverage_ebitda_z_1260d_v085_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_z_1260d_v085_signal},    "f05_operating_leverage_revenue_z_1260d_v086_signal": {"inputs": [], "func": f05_operating_leverage_revenue_z_1260d_v086_signal},    "f05_operating_leverage_sgna_z_1260d_v087_signal": {"inputs": [], "func": f05_operating_leverage_sgna_z_1260d_v087_signal},    "f05_operating_leverage_operating_alpha_z_1260d_v088_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_z_1260d_v088_signal},    "f05_operating_leverage_ebitda_dd_5d_v089_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_5d_v089_signal},    "f05_operating_leverage_revenue_dd_5d_v090_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_5d_v090_signal},    "f05_operating_leverage_sgna_dd_5d_v091_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_5d_v091_signal},    "f05_operating_leverage_operating_alpha_dd_5d_v092_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_5d_v092_signal},    "f05_operating_leverage_ebitda_dd_10d_v093_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_10d_v093_signal},    "f05_operating_leverage_revenue_dd_10d_v094_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_10d_v094_signal},    "f05_operating_leverage_sgna_dd_10d_v095_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_10d_v095_signal},    "f05_operating_leverage_operating_alpha_dd_10d_v096_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_10d_v096_signal},    "f05_operating_leverage_ebitda_dd_21d_v097_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_21d_v097_signal},    "f05_operating_leverage_revenue_dd_21d_v098_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_21d_v098_signal},    "f05_operating_leverage_sgna_dd_21d_v099_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_21d_v099_signal},    "f05_operating_leverage_operating_alpha_dd_21d_v100_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_21d_v100_signal},    "f05_operating_leverage_ebitda_dd_42d_v101_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_42d_v101_signal},    "f05_operating_leverage_revenue_dd_42d_v102_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_42d_v102_signal},    "f05_operating_leverage_sgna_dd_42d_v103_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_42d_v103_signal},    "f05_operating_leverage_operating_alpha_dd_42d_v104_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_42d_v104_signal},    "f05_operating_leverage_ebitda_dd_63d_v105_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_63d_v105_signal},    "f05_operating_leverage_revenue_dd_63d_v106_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_63d_v106_signal},    "f05_operating_leverage_sgna_dd_63d_v107_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_63d_v107_signal},    "f05_operating_leverage_operating_alpha_dd_63d_v108_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_63d_v108_signal},    "f05_operating_leverage_ebitda_dd_126d_v109_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_126d_v109_signal},    "f05_operating_leverage_revenue_dd_126d_v110_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_126d_v110_signal},    "f05_operating_leverage_sgna_dd_126d_v111_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_126d_v111_signal},    "f05_operating_leverage_operating_alpha_dd_126d_v112_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_126d_v112_signal},    "f05_operating_leverage_ebitda_dd_252d_v113_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_252d_v113_signal},    "f05_operating_leverage_revenue_dd_252d_v114_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_252d_v114_signal},    "f05_operating_leverage_sgna_dd_252d_v115_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_252d_v115_signal},    "f05_operating_leverage_operating_alpha_dd_252d_v116_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_252d_v116_signal},    "f05_operating_leverage_ebitda_dd_504d_v117_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_504d_v117_signal},    "f05_operating_leverage_revenue_dd_504d_v118_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_504d_v118_signal},    "f05_operating_leverage_sgna_dd_504d_v119_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_504d_v119_signal},    "f05_operating_leverage_operating_alpha_dd_504d_v120_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_504d_v120_signal},    "f05_operating_leverage_ebitda_dd_756d_v121_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_756d_v121_signal},    "f05_operating_leverage_revenue_dd_756d_v122_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_756d_v122_signal},    "f05_operating_leverage_sgna_dd_756d_v123_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_756d_v123_signal},    "f05_operating_leverage_operating_alpha_dd_756d_v124_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_756d_v124_signal},    "f05_operating_leverage_ebitda_dd_1008d_v125_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_1008d_v125_signal},    "f05_operating_leverage_revenue_dd_1008d_v126_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_1008d_v126_signal},    "f05_operating_leverage_sgna_dd_1008d_v127_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_1008d_v127_signal},    "f05_operating_leverage_operating_alpha_dd_1008d_v128_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_1008d_v128_signal},    "f05_operating_leverage_ebitda_dd_1260d_v129_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_dd_1260d_v129_signal},    "f05_operating_leverage_revenue_dd_1260d_v130_signal": {"inputs": [], "func": f05_operating_leverage_revenue_dd_1260d_v130_signal},    "f05_operating_leverage_sgna_dd_1260d_v131_signal": {"inputs": [], "func": f05_operating_leverage_sgna_dd_1260d_v131_signal},    "f05_operating_leverage_operating_alpha_dd_1260d_v132_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_dd_1260d_v132_signal},    "f05_operating_leverage_ebitda_rec_5d_v133_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_rec_5d_v133_signal},    "f05_operating_leverage_revenue_rec_5d_v134_signal": {"inputs": [], "func": f05_operating_leverage_revenue_rec_5d_v134_signal},    "f05_operating_leverage_sgna_rec_5d_v135_signal": {"inputs": [], "func": f05_operating_leverage_sgna_rec_5d_v135_signal},    "f05_operating_leverage_operating_alpha_rec_5d_v136_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_rec_5d_v136_signal},    "f05_operating_leverage_ebitda_rec_10d_v137_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_rec_10d_v137_signal},    "f05_operating_leverage_revenue_rec_10d_v138_signal": {"inputs": [], "func": f05_operating_leverage_revenue_rec_10d_v138_signal},    "f05_operating_leverage_sgna_rec_10d_v139_signal": {"inputs": [], "func": f05_operating_leverage_sgna_rec_10d_v139_signal},    "f05_operating_leverage_operating_alpha_rec_10d_v140_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_rec_10d_v140_signal},    "f05_operating_leverage_ebitda_rec_21d_v141_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_rec_21d_v141_signal},    "f05_operating_leverage_revenue_rec_21d_v142_signal": {"inputs": [], "func": f05_operating_leverage_revenue_rec_21d_v142_signal},    "f05_operating_leverage_sgna_rec_21d_v143_signal": {"inputs": [], "func": f05_operating_leverage_sgna_rec_21d_v143_signal},    "f05_operating_leverage_operating_alpha_rec_21d_v144_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_rec_21d_v144_signal},    "f05_operating_leverage_ebitda_rec_42d_v145_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_rec_42d_v145_signal},    "f05_operating_leverage_revenue_rec_42d_v146_signal": {"inputs": [], "func": f05_operating_leverage_revenue_rec_42d_v146_signal},    "f05_operating_leverage_sgna_rec_42d_v147_signal": {"inputs": [], "func": f05_operating_leverage_sgna_rec_42d_v147_signal},    "f05_operating_leverage_operating_alpha_rec_42d_v148_signal": {"inputs": [], "func": f05_operating_leverage_operating_alpha_rec_42d_v148_signal},    "f05_operating_leverage_ebitda_rec_63d_v149_signal": {"inputs": [], "func": f05_operating_leverage_ebitda_rec_63d_v149_signal},    "f05_operating_leverage_revenue_rec_63d_v150_signal": {"inputs": [], "func": f05_operating_leverage_revenue_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 05...")
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
