import pandas as pd
import numpy as np
import inspect

# ===== High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
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

def f45_overhead_rational_sgna_momentum_ewma_504d_v076_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 504d window."""
    res = _ewma(_slope_pct(sgna, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_756d_v077_signal(sgna):
    """Exponential moving average of Raw level of sgna over 756d window."""
    res = _ewma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_756d_v078_signal(revenue):
    """Exponential moving average of Raw level of revenue over 756d window."""
    res = _ewma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_756d_v079_signal(ebit):
    """Exponential moving average of Raw level of ebit over 756d window."""
    res = _ewma(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_756d_v080_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 756d window."""
    res = _ewma(_slope_pct(sgna, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_1008d_v081_signal(sgna):
    """Exponential moving average of Raw level of sgna over 1008d window."""
    res = _ewma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_1008d_v082_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1008d window."""
    res = _ewma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_1008d_v083_signal(ebit):
    """Exponential moving average of Raw level of ebit over 1008d window."""
    res = _ewma(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_1008d_v084_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 1008d window."""
    res = _ewma(_slope_pct(sgna, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_ewma_1260d_v085_signal(sgna):
    """Exponential moving average of Raw level of sgna over 1260d window."""
    res = _ewma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_ewma_1260d_v086_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1260d window."""
    res = _ewma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_ewma_1260d_v087_signal(ebit):
    """Exponential moving average of Raw level of ebit over 1260d window."""
    res = _ewma(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_ewma_1260d_v088_signal(sgna):
    """Exponential moving average of Annual SG&A change momentum over 1260d window."""
    res = _ewma(_slope_pct(sgna, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_5d_v089_signal(sgna):
    """Z-score of Raw level of sgna over 5d window."""
    res = _z(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_5d_v090_signal(revenue):
    """Z-score of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_5d_v091_signal(ebit):
    """Z-score of Raw level of ebit over 5d window."""
    res = _z(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_5d_v092_signal(sgna):
    """Z-score of Annual SG&A change momentum over 5d window."""
    res = _z(_slope_pct(sgna, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_10d_v093_signal(sgna):
    """Z-score of Raw level of sgna over 10d window."""
    res = _z(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_10d_v094_signal(revenue):
    """Z-score of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_10d_v095_signal(ebit):
    """Z-score of Raw level of ebit over 10d window."""
    res = _z(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_10d_v096_signal(sgna):
    """Z-score of Annual SG&A change momentum over 10d window."""
    res = _z(_slope_pct(sgna, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_21d_v097_signal(sgna):
    """Z-score of Raw level of sgna over 21d window."""
    res = _z(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_21d_v098_signal(revenue):
    """Z-score of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_21d_v099_signal(ebit):
    """Z-score of Raw level of ebit over 21d window."""
    res = _z(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_21d_v100_signal(sgna):
    """Z-score of Annual SG&A change momentum over 21d window."""
    res = _z(_slope_pct(sgna, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_42d_v101_signal(sgna):
    """Z-score of Raw level of sgna over 42d window."""
    res = _z(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_42d_v102_signal(revenue):
    """Z-score of Raw level of revenue over 42d window."""
    res = _z(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_42d_v103_signal(ebit):
    """Z-score of Raw level of ebit over 42d window."""
    res = _z(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_42d_v104_signal(sgna):
    """Z-score of Annual SG&A change momentum over 42d window."""
    res = _z(_slope_pct(sgna, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_63d_v105_signal(sgna):
    """Z-score of Raw level of sgna over 63d window."""
    res = _z(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_63d_v106_signal(revenue):
    """Z-score of Raw level of revenue over 63d window."""
    res = _z(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_63d_v107_signal(ebit):
    """Z-score of Raw level of ebit over 63d window."""
    res = _z(ebit, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_63d_v108_signal(sgna):
    """Z-score of Annual SG&A change momentum over 63d window."""
    res = _z(_slope_pct(sgna, 252), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_126d_v109_signal(sgna):
    """Z-score of Raw level of sgna over 126d window."""
    res = _z(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_126d_v110_signal(revenue):
    """Z-score of Raw level of revenue over 126d window."""
    res = _z(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_126d_v111_signal(ebit):
    """Z-score of Raw level of ebit over 126d window."""
    res = _z(ebit, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_126d_v112_signal(sgna):
    """Z-score of Annual SG&A change momentum over 126d window."""
    res = _z(_slope_pct(sgna, 252), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_252d_v113_signal(sgna):
    """Z-score of Raw level of sgna over 252d window."""
    res = _z(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_252d_v114_signal(revenue):
    """Z-score of Raw level of revenue over 252d window."""
    res = _z(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_252d_v115_signal(ebit):
    """Z-score of Raw level of ebit over 252d window."""
    res = _z(ebit, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_252d_v116_signal(sgna):
    """Z-score of Annual SG&A change momentum over 252d window."""
    res = _z(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_504d_v117_signal(sgna):
    """Z-score of Raw level of sgna over 504d window."""
    res = _z(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_504d_v118_signal(revenue):
    """Z-score of Raw level of revenue over 504d window."""
    res = _z(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_504d_v119_signal(ebit):
    """Z-score of Raw level of ebit over 504d window."""
    res = _z(ebit, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_504d_v120_signal(sgna):
    """Z-score of Annual SG&A change momentum over 504d window."""
    res = _z(_slope_pct(sgna, 252), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_756d_v121_signal(sgna):
    """Z-score of Raw level of sgna over 756d window."""
    res = _z(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_756d_v122_signal(revenue):
    """Z-score of Raw level of revenue over 756d window."""
    res = _z(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_756d_v123_signal(ebit):
    """Z-score of Raw level of ebit over 756d window."""
    res = _z(ebit, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_756d_v124_signal(sgna):
    """Z-score of Annual SG&A change momentum over 756d window."""
    res = _z(_slope_pct(sgna, 252), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_1008d_v125_signal(sgna):
    """Z-score of Raw level of sgna over 1008d window."""
    res = _z(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_1008d_v126_signal(revenue):
    """Z-score of Raw level of revenue over 1008d window."""
    res = _z(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_1008d_v127_signal(ebit):
    """Z-score of Raw level of ebit over 1008d window."""
    res = _z(ebit, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_1008d_v128_signal(sgna):
    """Z-score of Annual SG&A change momentum over 1008d window."""
    res = _z(_slope_pct(sgna, 252), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_z_1260d_v129_signal(sgna):
    """Z-score of Raw level of sgna over 1260d window."""
    res = _z(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_z_1260d_v130_signal(revenue):
    """Z-score of Raw level of revenue over 1260d window."""
    res = _z(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_z_1260d_v131_signal(ebit):
    """Z-score of Raw level of ebit over 1260d window."""
    res = _z(ebit, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_z_1260d_v132_signal(sgna):
    """Z-score of Annual SG&A change momentum over 1260d window."""
    res = _z(_slope_pct(sgna, 252), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_dd_5d_v133_signal(sgna):
    """Drawdown of Raw level of sgna over 5d window."""
    res = _drawdown(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_dd_5d_v134_signal(revenue):
    """Drawdown of Raw level of revenue over 5d window."""
    res = _drawdown(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_dd_5d_v135_signal(ebit):
    """Drawdown of Raw level of ebit over 5d window."""
    res = _drawdown(ebit, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_dd_5d_v136_signal(sgna):
    """Drawdown of Annual SG&A change momentum over 5d window."""
    res = _drawdown(_slope_pct(sgna, 252), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_dd_10d_v137_signal(sgna):
    """Drawdown of Raw level of sgna over 10d window."""
    res = _drawdown(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_dd_10d_v138_signal(revenue):
    """Drawdown of Raw level of revenue over 10d window."""
    res = _drawdown(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_dd_10d_v139_signal(ebit):
    """Drawdown of Raw level of ebit over 10d window."""
    res = _drawdown(ebit, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_dd_10d_v140_signal(sgna):
    """Drawdown of Annual SG&A change momentum over 10d window."""
    res = _drawdown(_slope_pct(sgna, 252), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_dd_21d_v141_signal(sgna):
    """Drawdown of Raw level of sgna over 21d window."""
    res = _drawdown(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_dd_21d_v142_signal(revenue):
    """Drawdown of Raw level of revenue over 21d window."""
    res = _drawdown(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_dd_21d_v143_signal(ebit):
    """Drawdown of Raw level of ebit over 21d window."""
    res = _drawdown(ebit, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_dd_21d_v144_signal(sgna):
    """Drawdown of Annual SG&A change momentum over 21d window."""
    res = _drawdown(_slope_pct(sgna, 252), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_dd_42d_v145_signal(sgna):
    """Drawdown of Raw level of sgna over 42d window."""
    res = _drawdown(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_dd_42d_v146_signal(revenue):
    """Drawdown of Raw level of revenue over 42d window."""
    res = _drawdown(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_ebit_dd_42d_v147_signal(ebit):
    """Drawdown of Raw level of ebit over 42d window."""
    res = _drawdown(ebit, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_momentum_dd_42d_v148_signal(sgna):
    """Drawdown of Annual SG&A change momentum over 42d window."""
    res = _drawdown(_slope_pct(sgna, 252), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_sgna_dd_63d_v149_signal(sgna):
    """Drawdown of Raw level of sgna over 63d window."""
    res = _drawdown(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f45_overhead_rational_revenue_dd_63d_v150_signal(revenue):
    """Drawdown of Raw level of revenue over 63d window."""
    res = _drawdown(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f45_overhead_rational_sgna_momentum_ewma_504d_v076_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_504d_v076_signal},
    "f45_overhead_rational_sgna_ewma_756d_v077_signal": {"func": f45_overhead_rational_sgna_ewma_756d_v077_signal},
    "f45_overhead_rational_revenue_ewma_756d_v078_signal": {"func": f45_overhead_rational_revenue_ewma_756d_v078_signal},
    "f45_overhead_rational_ebit_ewma_756d_v079_signal": {"func": f45_overhead_rational_ebit_ewma_756d_v079_signal},
    "f45_overhead_rational_sgna_momentum_ewma_756d_v080_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_756d_v080_signal},
    "f45_overhead_rational_sgna_ewma_1008d_v081_signal": {"func": f45_overhead_rational_sgna_ewma_1008d_v081_signal},
    "f45_overhead_rational_revenue_ewma_1008d_v082_signal": {"func": f45_overhead_rational_revenue_ewma_1008d_v082_signal},
    "f45_overhead_rational_ebit_ewma_1008d_v083_signal": {"func": f45_overhead_rational_ebit_ewma_1008d_v083_signal},
    "f45_overhead_rational_sgna_momentum_ewma_1008d_v084_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_1008d_v084_signal},
    "f45_overhead_rational_sgna_ewma_1260d_v085_signal": {"func": f45_overhead_rational_sgna_ewma_1260d_v085_signal},
    "f45_overhead_rational_revenue_ewma_1260d_v086_signal": {"func": f45_overhead_rational_revenue_ewma_1260d_v086_signal},
    "f45_overhead_rational_ebit_ewma_1260d_v087_signal": {"func": f45_overhead_rational_ebit_ewma_1260d_v087_signal},
    "f45_overhead_rational_sgna_momentum_ewma_1260d_v088_signal": {"func": f45_overhead_rational_sgna_momentum_ewma_1260d_v088_signal},
    "f45_overhead_rational_sgna_z_5d_v089_signal": {"func": f45_overhead_rational_sgna_z_5d_v089_signal},
    "f45_overhead_rational_revenue_z_5d_v090_signal": {"func": f45_overhead_rational_revenue_z_5d_v090_signal},
    "f45_overhead_rational_ebit_z_5d_v091_signal": {"func": f45_overhead_rational_ebit_z_5d_v091_signal},
    "f45_overhead_rational_sgna_momentum_z_5d_v092_signal": {"func": f45_overhead_rational_sgna_momentum_z_5d_v092_signal},
    "f45_overhead_rational_sgna_z_10d_v093_signal": {"func": f45_overhead_rational_sgna_z_10d_v093_signal},
    "f45_overhead_rational_revenue_z_10d_v094_signal": {"func": f45_overhead_rational_revenue_z_10d_v094_signal},
    "f45_overhead_rational_ebit_z_10d_v095_signal": {"func": f45_overhead_rational_ebit_z_10d_v095_signal},
    "f45_overhead_rational_sgna_momentum_z_10d_v096_signal": {"func": f45_overhead_rational_sgna_momentum_z_10d_v096_signal},
    "f45_overhead_rational_sgna_z_21d_v097_signal": {"func": f45_overhead_rational_sgna_z_21d_v097_signal},
    "f45_overhead_rational_revenue_z_21d_v098_signal": {"func": f45_overhead_rational_revenue_z_21d_v098_signal},
    "f45_overhead_rational_ebit_z_21d_v099_signal": {"func": f45_overhead_rational_ebit_z_21d_v099_signal},
    "f45_overhead_rational_sgna_momentum_z_21d_v100_signal": {"func": f45_overhead_rational_sgna_momentum_z_21d_v100_signal},
    "f45_overhead_rational_sgna_z_42d_v101_signal": {"func": f45_overhead_rational_sgna_z_42d_v101_signal},
    "f45_overhead_rational_revenue_z_42d_v102_signal": {"func": f45_overhead_rational_revenue_z_42d_v102_signal},
    "f45_overhead_rational_ebit_z_42d_v103_signal": {"func": f45_overhead_rational_ebit_z_42d_v103_signal},
    "f45_overhead_rational_sgna_momentum_z_42d_v104_signal": {"func": f45_overhead_rational_sgna_momentum_z_42d_v104_signal},
    "f45_overhead_rational_sgna_z_63d_v105_signal": {"func": f45_overhead_rational_sgna_z_63d_v105_signal},
    "f45_overhead_rational_revenue_z_63d_v106_signal": {"func": f45_overhead_rational_revenue_z_63d_v106_signal},
    "f45_overhead_rational_ebit_z_63d_v107_signal": {"func": f45_overhead_rational_ebit_z_63d_v107_signal},
    "f45_overhead_rational_sgna_momentum_z_63d_v108_signal": {"func": f45_overhead_rational_sgna_momentum_z_63d_v108_signal},
    "f45_overhead_rational_sgna_z_126d_v109_signal": {"func": f45_overhead_rational_sgna_z_126d_v109_signal},
    "f45_overhead_rational_revenue_z_126d_v110_signal": {"func": f45_overhead_rational_revenue_z_126d_v110_signal},
    "f45_overhead_rational_ebit_z_126d_v111_signal": {"func": f45_overhead_rational_ebit_z_126d_v111_signal},
    "f45_overhead_rational_sgna_momentum_z_126d_v112_signal": {"func": f45_overhead_rational_sgna_momentum_z_126d_v112_signal},
    "f45_overhead_rational_sgna_z_252d_v113_signal": {"func": f45_overhead_rational_sgna_z_252d_v113_signal},
    "f45_overhead_rational_revenue_z_252d_v114_signal": {"func": f45_overhead_rational_revenue_z_252d_v114_signal},
    "f45_overhead_rational_ebit_z_252d_v115_signal": {"func": f45_overhead_rational_ebit_z_252d_v115_signal},
    "f45_overhead_rational_sgna_momentum_z_252d_v116_signal": {"func": f45_overhead_rational_sgna_momentum_z_252d_v116_signal},
    "f45_overhead_rational_sgna_z_504d_v117_signal": {"func": f45_overhead_rational_sgna_z_504d_v117_signal},
    "f45_overhead_rational_revenue_z_504d_v118_signal": {"func": f45_overhead_rational_revenue_z_504d_v118_signal},
    "f45_overhead_rational_ebit_z_504d_v119_signal": {"func": f45_overhead_rational_ebit_z_504d_v119_signal},
    "f45_overhead_rational_sgna_momentum_z_504d_v120_signal": {"func": f45_overhead_rational_sgna_momentum_z_504d_v120_signal},
    "f45_overhead_rational_sgna_z_756d_v121_signal": {"func": f45_overhead_rational_sgna_z_756d_v121_signal},
    "f45_overhead_rational_revenue_z_756d_v122_signal": {"func": f45_overhead_rational_revenue_z_756d_v122_signal},
    "f45_overhead_rational_ebit_z_756d_v123_signal": {"func": f45_overhead_rational_ebit_z_756d_v123_signal},
    "f45_overhead_rational_sgna_momentum_z_756d_v124_signal": {"func": f45_overhead_rational_sgna_momentum_z_756d_v124_signal},
    "f45_overhead_rational_sgna_z_1008d_v125_signal": {"func": f45_overhead_rational_sgna_z_1008d_v125_signal},
    "f45_overhead_rational_revenue_z_1008d_v126_signal": {"func": f45_overhead_rational_revenue_z_1008d_v126_signal},
    "f45_overhead_rational_ebit_z_1008d_v127_signal": {"func": f45_overhead_rational_ebit_z_1008d_v127_signal},
    "f45_overhead_rational_sgna_momentum_z_1008d_v128_signal": {"func": f45_overhead_rational_sgna_momentum_z_1008d_v128_signal},
    "f45_overhead_rational_sgna_z_1260d_v129_signal": {"func": f45_overhead_rational_sgna_z_1260d_v129_signal},
    "f45_overhead_rational_revenue_z_1260d_v130_signal": {"func": f45_overhead_rational_revenue_z_1260d_v130_signal},
    "f45_overhead_rational_ebit_z_1260d_v131_signal": {"func": f45_overhead_rational_ebit_z_1260d_v131_signal},
    "f45_overhead_rational_sgna_momentum_z_1260d_v132_signal": {"func": f45_overhead_rational_sgna_momentum_z_1260d_v132_signal},
    "f45_overhead_rational_sgna_dd_5d_v133_signal": {"func": f45_overhead_rational_sgna_dd_5d_v133_signal},
    "f45_overhead_rational_revenue_dd_5d_v134_signal": {"func": f45_overhead_rational_revenue_dd_5d_v134_signal},
    "f45_overhead_rational_ebit_dd_5d_v135_signal": {"func": f45_overhead_rational_ebit_dd_5d_v135_signal},
    "f45_overhead_rational_sgna_momentum_dd_5d_v136_signal": {"func": f45_overhead_rational_sgna_momentum_dd_5d_v136_signal},
    "f45_overhead_rational_sgna_dd_10d_v137_signal": {"func": f45_overhead_rational_sgna_dd_10d_v137_signal},
    "f45_overhead_rational_revenue_dd_10d_v138_signal": {"func": f45_overhead_rational_revenue_dd_10d_v138_signal},
    "f45_overhead_rational_ebit_dd_10d_v139_signal": {"func": f45_overhead_rational_ebit_dd_10d_v139_signal},
    "f45_overhead_rational_sgna_momentum_dd_10d_v140_signal": {"func": f45_overhead_rational_sgna_momentum_dd_10d_v140_signal},
    "f45_overhead_rational_sgna_dd_21d_v141_signal": {"func": f45_overhead_rational_sgna_dd_21d_v141_signal},
    "f45_overhead_rational_revenue_dd_21d_v142_signal": {"func": f45_overhead_rational_revenue_dd_21d_v142_signal},
    "f45_overhead_rational_ebit_dd_21d_v143_signal": {"func": f45_overhead_rational_ebit_dd_21d_v143_signal},
    "f45_overhead_rational_sgna_momentum_dd_21d_v144_signal": {"func": f45_overhead_rational_sgna_momentum_dd_21d_v144_signal},
    "f45_overhead_rational_sgna_dd_42d_v145_signal": {"func": f45_overhead_rational_sgna_dd_42d_v145_signal},
    "f45_overhead_rational_revenue_dd_42d_v146_signal": {"func": f45_overhead_rational_revenue_dd_42d_v146_signal},
    "f45_overhead_rational_ebit_dd_42d_v147_signal": {"func": f45_overhead_rational_ebit_dd_42d_v147_signal},
    "f45_overhead_rational_sgna_momentum_dd_42d_v148_signal": {"func": f45_overhead_rational_sgna_momentum_dd_42d_v148_signal},
    "f45_overhead_rational_sgna_dd_63d_v149_signal": {"func": f45_overhead_rational_sgna_dd_63d_v149_signal},
    "f45_overhead_rational_revenue_dd_63d_v150_signal": {"func": f45_overhead_rational_revenue_dd_63d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 45...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
