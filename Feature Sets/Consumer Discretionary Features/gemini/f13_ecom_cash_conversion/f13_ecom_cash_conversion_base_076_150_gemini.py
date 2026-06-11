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

def f13_ecom_cash_conversion_ecom_liquidity_z_504d_v076_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 504d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_756d_v077_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_756d_v078_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 756d window."""
    res = _z(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_756d_v079_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 756d window."""
    res = _z(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_756d_v080_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 756d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_1008d_v081_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_1008d_v082_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 1008d window."""
    res = _z(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_1008d_v083_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 1008d window."""
    res = _z(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_1008d_v084_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 1008d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_z_1260d_v085_signal(revenue):
    """Z-score for relative outlier detection of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_z_1260d_v086_signal(deferredrev):
    """Z-score for relative outlier detection of Raw level of deferredrev over 1260d window."""
    res = _z(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_z_1260d_v087_signal(cashneq):
    """Z-score for relative outlier detection of Raw level of cashneq over 1260d window."""
    res = _z(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_z_1260d_v088_signal(cashneq, deferredrev, revenue):
    """Z-score for relative outlier detection of Digital liquidity and upfront payment strength over 1260d window."""
    res = _z(_ratio(cashneq + deferredrev, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_5d_v089_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_5d_v090_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 5d window."""
    res = _drawdown(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_5d_v091_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 5d window."""
    res = _drawdown(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_5d_v092_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 5d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_10d_v093_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_10d_v094_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 10d window."""
    res = _drawdown(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_10d_v095_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 10d window."""
    res = _drawdown(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_10d_v096_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 10d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_21d_v097_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_21d_v098_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 21d window."""
    res = _drawdown(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_21d_v099_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 21d window."""
    res = _drawdown(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_21d_v100_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 21d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_42d_v101_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_42d_v102_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 42d window."""
    res = _drawdown(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_42d_v103_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 42d window."""
    res = _drawdown(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_42d_v104_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 42d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_63d_v105_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_63d_v106_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 63d window."""
    res = _drawdown(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_63d_v107_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 63d window."""
    res = _drawdown(cashneq, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_63d_v108_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 63d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_126d_v109_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 126d window."""
    res = _drawdown(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_126d_v110_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 126d window."""
    res = _drawdown(deferredrev, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_126d_v111_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 126d window."""
    res = _drawdown(cashneq, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_126d_v112_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 126d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_252d_v113_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 252d window."""
    res = _drawdown(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_252d_v114_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 252d window."""
    res = _drawdown(deferredrev, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_252d_v115_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 252d window."""
    res = _drawdown(cashneq, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_252d_v116_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 252d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_504d_v117_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 504d window."""
    res = _drawdown(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_504d_v118_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 504d window."""
    res = _drawdown(deferredrev, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_504d_v119_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 504d window."""
    res = _drawdown(cashneq, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_504d_v120_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 504d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_756d_v121_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 756d window."""
    res = _drawdown(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_756d_v122_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 756d window."""
    res = _drawdown(deferredrev, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_756d_v123_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 756d window."""
    res = _drawdown(cashneq, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_756d_v124_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 756d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_1008d_v125_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1008d window."""
    res = _drawdown(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_1008d_v126_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 1008d window."""
    res = _drawdown(deferredrev, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_1008d_v127_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 1008d window."""
    res = _drawdown(cashneq, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_1008d_v128_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 1008d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_dd_1260d_v129_signal(revenue):
    """Drawdown from peak to identify cycle troughs of Raw level of revenue over 1260d window."""
    res = _drawdown(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_dd_1260d_v130_signal(deferredrev):
    """Drawdown from peak to identify cycle troughs of Raw level of deferredrev over 1260d window."""
    res = _drawdown(deferredrev, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_dd_1260d_v131_signal(cashneq):
    """Drawdown from peak to identify cycle troughs of Raw level of cashneq over 1260d window."""
    res = _drawdown(cashneq, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_dd_1260d_v132_signal(cashneq, deferredrev, revenue):
    """Drawdown from peak to identify cycle troughs of Digital liquidity and upfront payment strength over 1260d window."""
    res = _drawdown(_ratio(cashneq + deferredrev, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_rec_5d_v133_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 5d window."""
    res = _recovery(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_rec_5d_v134_signal(deferredrev):
    """Recovery from trough for turnaround signals of Raw level of deferredrev over 5d window."""
    res = _recovery(deferredrev, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_rec_5d_v135_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 5d window."""
    res = _recovery(cashneq, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_rec_5d_v136_signal(cashneq, deferredrev, revenue):
    """Recovery from trough for turnaround signals of Digital liquidity and upfront payment strength over 5d window."""
    res = _recovery(_ratio(cashneq + deferredrev, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_rec_10d_v137_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 10d window."""
    res = _recovery(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_rec_10d_v138_signal(deferredrev):
    """Recovery from trough for turnaround signals of Raw level of deferredrev over 10d window."""
    res = _recovery(deferredrev, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_rec_10d_v139_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 10d window."""
    res = _recovery(cashneq, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_rec_10d_v140_signal(cashneq, deferredrev, revenue):
    """Recovery from trough for turnaround signals of Digital liquidity and upfront payment strength over 10d window."""
    res = _recovery(_ratio(cashneq + deferredrev, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_rec_21d_v141_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 21d window."""
    res = _recovery(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_rec_21d_v142_signal(deferredrev):
    """Recovery from trough for turnaround signals of Raw level of deferredrev over 21d window."""
    res = _recovery(deferredrev, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_rec_21d_v143_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 21d window."""
    res = _recovery(cashneq, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_rec_21d_v144_signal(cashneq, deferredrev, revenue):
    """Recovery from trough for turnaround signals of Digital liquidity and upfront payment strength over 21d window."""
    res = _recovery(_ratio(cashneq + deferredrev, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_rec_42d_v145_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 42d window."""
    res = _recovery(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_rec_42d_v146_signal(deferredrev):
    """Recovery from trough for turnaround signals of Raw level of deferredrev over 42d window."""
    res = _recovery(deferredrev, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_cashneq_rec_42d_v147_signal(cashneq):
    """Recovery from trough for turnaround signals of Raw level of cashneq over 42d window."""
    res = _recovery(cashneq, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_ecom_liquidity_rec_42d_v148_signal(cashneq, deferredrev, revenue):
    """Recovery from trough for turnaround signals of Digital liquidity and upfront payment strength over 42d window."""
    res = _recovery(_ratio(cashneq + deferredrev, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_revenue_rec_63d_v149_signal(revenue):
    """Recovery from trough for turnaround signals of Raw level of revenue over 63d window."""
    res = _recovery(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f13_ecom_cash_conversion_deferredrev_rec_63d_v150_signal(deferredrev):
    """Recovery from trough for turnaround signals of Raw level of deferredrev over 63d window."""
    res = _recovery(deferredrev, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f13_ecom_cash_conversion_ecom_liquidity_z_504d_v076_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_504d_v076_signal},    "f13_ecom_cash_conversion_revenue_z_756d_v077_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_756d_v077_signal},    "f13_ecom_cash_conversion_deferredrev_z_756d_v078_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_756d_v078_signal},    "f13_ecom_cash_conversion_cashneq_z_756d_v079_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_756d_v079_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_756d_v080_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_756d_v080_signal},    "f13_ecom_cash_conversion_revenue_z_1008d_v081_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_1008d_v081_signal},    "f13_ecom_cash_conversion_deferredrev_z_1008d_v082_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_1008d_v082_signal},    "f13_ecom_cash_conversion_cashneq_z_1008d_v083_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_1008d_v083_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_1008d_v084_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_1008d_v084_signal},    "f13_ecom_cash_conversion_revenue_z_1260d_v085_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_z_1260d_v085_signal},    "f13_ecom_cash_conversion_deferredrev_z_1260d_v086_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_z_1260d_v086_signal},    "f13_ecom_cash_conversion_cashneq_z_1260d_v087_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_z_1260d_v087_signal},    "f13_ecom_cash_conversion_ecom_liquidity_z_1260d_v088_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_z_1260d_v088_signal},    "f13_ecom_cash_conversion_revenue_dd_5d_v089_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_5d_v089_signal},    "f13_ecom_cash_conversion_deferredrev_dd_5d_v090_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_5d_v090_signal},    "f13_ecom_cash_conversion_cashneq_dd_5d_v091_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_5d_v091_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_5d_v092_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_5d_v092_signal},    "f13_ecom_cash_conversion_revenue_dd_10d_v093_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_10d_v093_signal},    "f13_ecom_cash_conversion_deferredrev_dd_10d_v094_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_10d_v094_signal},    "f13_ecom_cash_conversion_cashneq_dd_10d_v095_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_10d_v095_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_10d_v096_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_10d_v096_signal},    "f13_ecom_cash_conversion_revenue_dd_21d_v097_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_21d_v097_signal},    "f13_ecom_cash_conversion_deferredrev_dd_21d_v098_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_21d_v098_signal},    "f13_ecom_cash_conversion_cashneq_dd_21d_v099_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_21d_v099_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_21d_v100_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_21d_v100_signal},    "f13_ecom_cash_conversion_revenue_dd_42d_v101_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_42d_v101_signal},    "f13_ecom_cash_conversion_deferredrev_dd_42d_v102_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_42d_v102_signal},    "f13_ecom_cash_conversion_cashneq_dd_42d_v103_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_42d_v103_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_42d_v104_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_42d_v104_signal},    "f13_ecom_cash_conversion_revenue_dd_63d_v105_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_63d_v105_signal},    "f13_ecom_cash_conversion_deferredrev_dd_63d_v106_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_63d_v106_signal},    "f13_ecom_cash_conversion_cashneq_dd_63d_v107_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_63d_v107_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_63d_v108_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_63d_v108_signal},    "f13_ecom_cash_conversion_revenue_dd_126d_v109_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_126d_v109_signal},    "f13_ecom_cash_conversion_deferredrev_dd_126d_v110_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_126d_v110_signal},    "f13_ecom_cash_conversion_cashneq_dd_126d_v111_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_126d_v111_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_126d_v112_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_126d_v112_signal},    "f13_ecom_cash_conversion_revenue_dd_252d_v113_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_252d_v113_signal},    "f13_ecom_cash_conversion_deferredrev_dd_252d_v114_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_252d_v114_signal},    "f13_ecom_cash_conversion_cashneq_dd_252d_v115_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_252d_v115_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_252d_v116_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_252d_v116_signal},    "f13_ecom_cash_conversion_revenue_dd_504d_v117_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_504d_v117_signal},    "f13_ecom_cash_conversion_deferredrev_dd_504d_v118_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_504d_v118_signal},    "f13_ecom_cash_conversion_cashneq_dd_504d_v119_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_504d_v119_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_504d_v120_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_504d_v120_signal},    "f13_ecom_cash_conversion_revenue_dd_756d_v121_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_756d_v121_signal},    "f13_ecom_cash_conversion_deferredrev_dd_756d_v122_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_756d_v122_signal},    "f13_ecom_cash_conversion_cashneq_dd_756d_v123_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_756d_v123_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_756d_v124_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_756d_v124_signal},    "f13_ecom_cash_conversion_revenue_dd_1008d_v125_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_1008d_v125_signal},    "f13_ecom_cash_conversion_deferredrev_dd_1008d_v126_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_1008d_v126_signal},    "f13_ecom_cash_conversion_cashneq_dd_1008d_v127_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_1008d_v127_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_1008d_v128_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_1008d_v128_signal},    "f13_ecom_cash_conversion_revenue_dd_1260d_v129_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_dd_1260d_v129_signal},    "f13_ecom_cash_conversion_deferredrev_dd_1260d_v130_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_dd_1260d_v130_signal},    "f13_ecom_cash_conversion_cashneq_dd_1260d_v131_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_dd_1260d_v131_signal},    "f13_ecom_cash_conversion_ecom_liquidity_dd_1260d_v132_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_dd_1260d_v132_signal},    "f13_ecom_cash_conversion_revenue_rec_5d_v133_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_rec_5d_v133_signal},    "f13_ecom_cash_conversion_deferredrev_rec_5d_v134_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_rec_5d_v134_signal},    "f13_ecom_cash_conversion_cashneq_rec_5d_v135_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_rec_5d_v135_signal},    "f13_ecom_cash_conversion_ecom_liquidity_rec_5d_v136_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_rec_5d_v136_signal},    "f13_ecom_cash_conversion_revenue_rec_10d_v137_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_rec_10d_v137_signal},    "f13_ecom_cash_conversion_deferredrev_rec_10d_v138_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_rec_10d_v138_signal},    "f13_ecom_cash_conversion_cashneq_rec_10d_v139_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_rec_10d_v139_signal},    "f13_ecom_cash_conversion_ecom_liquidity_rec_10d_v140_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_rec_10d_v140_signal},    "f13_ecom_cash_conversion_revenue_rec_21d_v141_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_rec_21d_v141_signal},    "f13_ecom_cash_conversion_deferredrev_rec_21d_v142_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_rec_21d_v142_signal},    "f13_ecom_cash_conversion_cashneq_rec_21d_v143_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_rec_21d_v143_signal},    "f13_ecom_cash_conversion_ecom_liquidity_rec_21d_v144_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_rec_21d_v144_signal},    "f13_ecom_cash_conversion_revenue_rec_42d_v145_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_rec_42d_v145_signal},    "f13_ecom_cash_conversion_deferredrev_rec_42d_v146_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_rec_42d_v146_signal},    "f13_ecom_cash_conversion_cashneq_rec_42d_v147_signal": {"inputs": [], "func": f13_ecom_cash_conversion_cashneq_rec_42d_v147_signal},    "f13_ecom_cash_conversion_ecom_liquidity_rec_42d_v148_signal": {"inputs": [], "func": f13_ecom_cash_conversion_ecom_liquidity_rec_42d_v148_signal},    "f13_ecom_cash_conversion_revenue_rec_63d_v149_signal": {"inputs": [], "func": f13_ecom_cash_conversion_revenue_rec_63d_v149_signal},    "f13_ecom_cash_conversion_deferredrev_rec_63d_v150_signal": {"inputs": [], "func": f13_ecom_cash_conversion_deferredrev_rec_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum()
    })
    
    print(f"Verifying {len(REGISTRY)} functions for family 13...")
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
