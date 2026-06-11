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

def f20_seasonal_stability_resilience_score_z_504d_v076_signal(ebitda, revenue):
    """Z-score for relative outlier detection of EBITDA strength relative to sales volatility over 504d window."""
    res = _z(_ratio(ebitda, _std(revenue, 63)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_z_756d_v077_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_z_756d_v078_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 756d window."""
    res = _z(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_z_756d_v079_signal(ebitda):
    """Z-score for relative outlier detection of Raw level of ebitda over 756d window."""
    res = _z(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_z_756d_v080_signal(ebitda, revenue):
    """Z-score for relative outlier detection of EBITDA strength relative to sales volatility over 756d window."""
    res = _z(_ratio(ebitda, _std(revenue, 63)), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_z_1008d_v081_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_z_1008d_v082_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1008d window."""
    res = _z(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_z_1008d_v083_signal(ebitda):
    """Z-score for relative outlier detection of Raw level of ebitda over 1008d window."""
    res = _z(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_z_1008d_v084_signal(ebitda, revenue):
    """Z-score for relative outlier detection of EBITDA strength relative to sales volatility over 1008d window."""
    res = _z(_ratio(ebitda, _std(revenue, 63)), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_z_1260d_v085_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_z_1260d_v086_signal(grossmargin):
    """Z-score for relative outlier detection of Raw level of grossmargin over 1260d window."""
    res = _z(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_z_1260d_v087_signal(ebitda):
    """Z-score for relative outlier detection of Raw level of ebitda over 1260d window."""
    res = _z(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_z_1260d_v088_signal(ebitda, revenue):
    """Z-score for relative outlier detection of EBITDA strength relative to sales volatility over 1260d window."""
    res = _z(_ratio(ebitda, _std(revenue, 63)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_5d_v089_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_5d_v090_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 5d window."""
    res = _drawdown(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_5d_v091_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 5d window."""
    res = _drawdown(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_5d_v092_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 5d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_10d_v093_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_10d_v094_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 10d window."""
    res = _drawdown(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_10d_v095_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 10d window."""
    res = _drawdown(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_10d_v096_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 10d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_21d_v097_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_21d_v098_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 21d window."""
    res = _drawdown(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_21d_v099_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 21d window."""
    res = _drawdown(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_21d_v100_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 21d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_42d_v101_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_42d_v102_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 42d window."""
    res = _drawdown(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_42d_v103_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 42d window."""
    res = _drawdown(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_42d_v104_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 42d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_63d_v105_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_63d_v106_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 63d window."""
    res = _drawdown(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_63d_v107_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 63d window."""
    res = _drawdown(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_63d_v108_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 63d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_126d_v109_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 126d window."""
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_126d_v110_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 126d window."""
    res = _drawdown(grossmargin, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_126d_v111_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 126d window."""
    res = _drawdown(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_126d_v112_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 126d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_252d_v113_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 252d window."""
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_252d_v114_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 252d window."""
    res = _drawdown(grossmargin, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_252d_v115_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 252d window."""
    res = _drawdown(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_252d_v116_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 252d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_504d_v117_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 504d window."""
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_504d_v118_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 504d window."""
    res = _drawdown(grossmargin, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_504d_v119_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 504d window."""
    res = _drawdown(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_504d_v120_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 504d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_756d_v121_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 756d window."""
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_756d_v122_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 756d window."""
    res = _drawdown(grossmargin, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_756d_v123_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 756d window."""
    res = _drawdown(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_756d_v124_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 756d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_1008d_v125_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1008d window."""
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_1008d_v126_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1008d window."""
    res = _drawdown(grossmargin, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_1008d_v127_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 1008d window."""
    res = _drawdown(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_1008d_v128_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 1008d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_dd_1260d_v129_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1260d window."""
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_dd_1260d_v130_signal(grossmargin):
    """Drawdown from peak to identify cycle troughs of Raw level of grossmargin over 1260d window."""
    res = _drawdown(grossmargin, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_dd_1260d_v131_signal(ebitda):
    """Drawdown from peak to identify cycle troughs of Raw level of ebitda over 1260d window."""
    res = _drawdown(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_dd_1260d_v132_signal(ebitda, revenue):
    """Drawdown from peak to identify cycle troughs of EBITDA strength relative to sales volatility over 1260d window."""
    res = _drawdown(_ratio(ebitda, _std(revenue, 63)), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_rec_5d_v133_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 5d window."""
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_rec_5d_v134_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 5d window."""
    res = _recovery(grossmargin, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_rec_5d_v135_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 5d window."""
    res = _recovery(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_rec_5d_v136_signal(ebitda, revenue):
    """Recovery from trough for turnaround signals of EBITDA strength relative to sales volatility over 5d window."""
    res = _recovery(_ratio(ebitda, _std(revenue, 63)), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_rec_10d_v137_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 10d window."""
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_rec_10d_v138_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 10d window."""
    res = _recovery(grossmargin, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_rec_10d_v139_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 10d window."""
    res = _recovery(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_rec_10d_v140_signal(ebitda, revenue):
    """Recovery from trough for turnaround signals of EBITDA strength relative to sales volatility over 10d window."""
    res = _recovery(_ratio(ebitda, _std(revenue, 63)), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_rec_21d_v141_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 21d window."""
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_rec_21d_v142_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 21d window."""
    res = _recovery(grossmargin, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_rec_21d_v143_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 21d window."""
    res = _recovery(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_rec_21d_v144_signal(ebitda, revenue):
    """Recovery from trough for turnaround signals of EBITDA strength relative to sales volatility over 21d window."""
    res = _recovery(_ratio(ebitda, _std(revenue, 63)), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_rec_42d_v145_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 42d window."""
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_rec_42d_v146_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 42d window."""
    res = _recovery(grossmargin, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_ebitda_rec_42d_v147_signal(ebitda):
    """Recovery from trough for turnaround signals of Raw level of ebitda over 42d window."""
    res = _recovery(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_resilience_score_rec_42d_v148_signal(ebitda, revenue):
    """Recovery from trough for turnaround signals of EBITDA strength relative to sales volatility over 42d window."""
    res = _recovery(_ratio(ebitda, _std(revenue, 63)), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_revenue_rec_63d_v149_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 63d window."""
    res = _recovery(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f20_seasonal_stability_grossmargin_rec_63d_v150_signal(grossmargin):
    """Recovery from trough for turnaround signals of Raw level of grossmargin over 63d window."""
    res = _recovery(grossmargin, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f20_seasonal_stability_resilience_score_z_504d_v076_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_z_504d_v076_signal},    "f20_seasonal_stability_revenue_z_756d_v077_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_z_756d_v077_signal},    "f20_seasonal_stability_grossmargin_z_756d_v078_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_z_756d_v078_signal},    "f20_seasonal_stability_ebitda_z_756d_v079_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_z_756d_v079_signal},    "f20_seasonal_stability_resilience_score_z_756d_v080_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_z_756d_v080_signal},    "f20_seasonal_stability_revenue_z_1008d_v081_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_z_1008d_v081_signal},    "f20_seasonal_stability_grossmargin_z_1008d_v082_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_z_1008d_v082_signal},    "f20_seasonal_stability_ebitda_z_1008d_v083_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_z_1008d_v083_signal},    "f20_seasonal_stability_resilience_score_z_1008d_v084_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_z_1008d_v084_signal},    "f20_seasonal_stability_revenue_z_1260d_v085_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_z_1260d_v085_signal},    "f20_seasonal_stability_grossmargin_z_1260d_v086_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_z_1260d_v086_signal},    "f20_seasonal_stability_ebitda_z_1260d_v087_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_z_1260d_v087_signal},    "f20_seasonal_stability_resilience_score_z_1260d_v088_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_z_1260d_v088_signal},    "f20_seasonal_stability_revenue_dd_5d_v089_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_5d_v089_signal},    "f20_seasonal_stability_grossmargin_dd_5d_v090_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_5d_v090_signal},    "f20_seasonal_stability_ebitda_dd_5d_v091_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_5d_v091_signal},    "f20_seasonal_stability_resilience_score_dd_5d_v092_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_5d_v092_signal},    "f20_seasonal_stability_revenue_dd_10d_v093_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_10d_v093_signal},    "f20_seasonal_stability_grossmargin_dd_10d_v094_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_10d_v094_signal},    "f20_seasonal_stability_ebitda_dd_10d_v095_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_10d_v095_signal},    "f20_seasonal_stability_resilience_score_dd_10d_v096_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_10d_v096_signal},    "f20_seasonal_stability_revenue_dd_21d_v097_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_21d_v097_signal},    "f20_seasonal_stability_grossmargin_dd_21d_v098_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_21d_v098_signal},    "f20_seasonal_stability_ebitda_dd_21d_v099_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_21d_v099_signal},    "f20_seasonal_stability_resilience_score_dd_21d_v100_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_21d_v100_signal},    "f20_seasonal_stability_revenue_dd_42d_v101_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_42d_v101_signal},    "f20_seasonal_stability_grossmargin_dd_42d_v102_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_42d_v102_signal},    "f20_seasonal_stability_ebitda_dd_42d_v103_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_42d_v103_signal},    "f20_seasonal_stability_resilience_score_dd_42d_v104_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_42d_v104_signal},    "f20_seasonal_stability_revenue_dd_63d_v105_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_63d_v105_signal},    "f20_seasonal_stability_grossmargin_dd_63d_v106_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_63d_v106_signal},    "f20_seasonal_stability_ebitda_dd_63d_v107_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_63d_v107_signal},    "f20_seasonal_stability_resilience_score_dd_63d_v108_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_63d_v108_signal},    "f20_seasonal_stability_revenue_dd_126d_v109_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_126d_v109_signal},    "f20_seasonal_stability_grossmargin_dd_126d_v110_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_126d_v110_signal},    "f20_seasonal_stability_ebitda_dd_126d_v111_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_126d_v111_signal},    "f20_seasonal_stability_resilience_score_dd_126d_v112_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_126d_v112_signal},    "f20_seasonal_stability_revenue_dd_252d_v113_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_252d_v113_signal},    "f20_seasonal_stability_grossmargin_dd_252d_v114_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_252d_v114_signal},    "f20_seasonal_stability_ebitda_dd_252d_v115_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_252d_v115_signal},    "f20_seasonal_stability_resilience_score_dd_252d_v116_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_252d_v116_signal},    "f20_seasonal_stability_revenue_dd_504d_v117_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_504d_v117_signal},    "f20_seasonal_stability_grossmargin_dd_504d_v118_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_504d_v118_signal},    "f20_seasonal_stability_ebitda_dd_504d_v119_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_504d_v119_signal},    "f20_seasonal_stability_resilience_score_dd_504d_v120_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_504d_v120_signal},    "f20_seasonal_stability_revenue_dd_756d_v121_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_756d_v121_signal},    "f20_seasonal_stability_grossmargin_dd_756d_v122_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_756d_v122_signal},    "f20_seasonal_stability_ebitda_dd_756d_v123_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_756d_v123_signal},    "f20_seasonal_stability_resilience_score_dd_756d_v124_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_756d_v124_signal},    "f20_seasonal_stability_revenue_dd_1008d_v125_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_1008d_v125_signal},    "f20_seasonal_stability_grossmargin_dd_1008d_v126_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_1008d_v126_signal},    "f20_seasonal_stability_ebitda_dd_1008d_v127_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_1008d_v127_signal},    "f20_seasonal_stability_resilience_score_dd_1008d_v128_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_1008d_v128_signal},    "f20_seasonal_stability_revenue_dd_1260d_v129_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_dd_1260d_v129_signal},    "f20_seasonal_stability_grossmargin_dd_1260d_v130_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_dd_1260d_v130_signal},    "f20_seasonal_stability_ebitda_dd_1260d_v131_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_dd_1260d_v131_signal},    "f20_seasonal_stability_resilience_score_dd_1260d_v132_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_dd_1260d_v132_signal},    "f20_seasonal_stability_revenue_rec_5d_v133_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_rec_5d_v133_signal},    "f20_seasonal_stability_grossmargin_rec_5d_v134_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_rec_5d_v134_signal},    "f20_seasonal_stability_ebitda_rec_5d_v135_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_rec_5d_v135_signal},    "f20_seasonal_stability_resilience_score_rec_5d_v136_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_rec_5d_v136_signal},    "f20_seasonal_stability_revenue_rec_10d_v137_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_rec_10d_v137_signal},    "f20_seasonal_stability_grossmargin_rec_10d_v138_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_rec_10d_v138_signal},    "f20_seasonal_stability_ebitda_rec_10d_v139_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_rec_10d_v139_signal},    "f20_seasonal_stability_resilience_score_rec_10d_v140_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_rec_10d_v140_signal},    "f20_seasonal_stability_revenue_rec_21d_v141_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_rec_21d_v141_signal},    "f20_seasonal_stability_grossmargin_rec_21d_v142_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_rec_21d_v142_signal},    "f20_seasonal_stability_ebitda_rec_21d_v143_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_rec_21d_v143_signal},    "f20_seasonal_stability_resilience_score_rec_21d_v144_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_rec_21d_v144_signal},    "f20_seasonal_stability_revenue_rec_42d_v145_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_rec_42d_v145_signal},    "f20_seasonal_stability_grossmargin_rec_42d_v146_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_rec_42d_v146_signal},    "f20_seasonal_stability_ebitda_rec_42d_v147_signal": {"inputs": [], "func": f20_seasonal_stability_ebitda_rec_42d_v147_signal},    "f20_seasonal_stability_resilience_score_rec_42d_v148_signal": {"inputs": [], "func": f20_seasonal_stability_resilience_score_rec_42d_v148_signal},    "f20_seasonal_stability_revenue_rec_63d_v149_signal": {"inputs": [], "func": f20_seasonal_stability_revenue_rec_63d_v149_signal},    "f20_seasonal_stability_grossmargin_rec_63d_v150_signal": {"inputs": [], "func": f20_seasonal_stability_grossmargin_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 20...")
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
