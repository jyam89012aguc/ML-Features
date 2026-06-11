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

def f04_efficiency_ratio_efficiency_score_ewma_10d_v076_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 10d window."""
    res = _ewma(_ratio(sgna, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_10d_v077_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 10d window."""
    res = _ewma(_ratio(ebitda, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_10d_v078_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 10d window."""
    res = _ewma(_ratio(ebitda, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_21d_v079_signal(sgna):
    """Exponential moving average of Raw level of sgna over 21d window."""
    res = _ewma(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_21d_v080_signal(revenue):
    """Exponential moving average of Raw level of revenue over 21d window."""
    res = _ewma(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_21d_v081_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 21d window."""
    res = _ewma(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_21d_v082_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 21d window."""
    res = _ewma(_ratio(sgna, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_21d_v083_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 21d window."""
    res = _ewma(_ratio(ebitda, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_21d_v084_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 21d window."""
    res = _ewma(_ratio(ebitda, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_42d_v085_signal(sgna):
    """Exponential moving average of Raw level of sgna over 42d window."""
    res = _ewma(sgna, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_42d_v086_signal(revenue):
    """Exponential moving average of Raw level of revenue over 42d window."""
    res = _ewma(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_42d_v087_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 42d window."""
    res = _ewma(ebitda, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_42d_v088_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 42d window."""
    res = _ewma(_ratio(sgna, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_42d_v089_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 42d window."""
    res = _ewma(_ratio(ebitda, revenue), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_42d_v090_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 42d window."""
    res = _ewma(_ratio(ebitda, sgna), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_63d_v091_signal(sgna):
    """Exponential moving average of Raw level of sgna over 63d window."""
    res = _ewma(sgna, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_63d_v092_signal(revenue):
    """Exponential moving average of Raw level of revenue over 63d window."""
    res = _ewma(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_63d_v093_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 63d window."""
    res = _ewma(ebitda, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_63d_v094_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 63d window."""
    res = _ewma(_ratio(sgna, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_63d_v095_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 63d window."""
    res = _ewma(_ratio(ebitda, revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_63d_v096_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 63d window."""
    res = _ewma(_ratio(ebitda, sgna), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_126d_v097_signal(sgna):
    """Exponential moving average of Raw level of sgna over 126d window."""
    res = _ewma(sgna, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_126d_v098_signal(revenue):
    """Exponential moving average of Raw level of revenue over 126d window."""
    res = _ewma(revenue, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_126d_v099_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 126d window."""
    res = _ewma(ebitda, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_126d_v100_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 126d window."""
    res = _ewma(_ratio(sgna, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_126d_v101_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 126d window."""
    res = _ewma(_ratio(ebitda, revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_126d_v102_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 126d window."""
    res = _ewma(_ratio(ebitda, sgna), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_252d_v103_signal(sgna):
    """Exponential moving average of Raw level of sgna over 252d window."""
    res = _ewma(sgna, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_252d_v104_signal(revenue):
    """Exponential moving average of Raw level of revenue over 252d window."""
    res = _ewma(revenue, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_252d_v105_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 252d window."""
    res = _ewma(ebitda, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_252d_v106_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 252d window."""
    res = _ewma(_ratio(sgna, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_252d_v107_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 252d window."""
    res = _ewma(_ratio(ebitda, revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_252d_v108_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 252d window."""
    res = _ewma(_ratio(ebitda, sgna), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_504d_v109_signal(sgna):
    """Exponential moving average of Raw level of sgna over 504d window."""
    res = _ewma(sgna, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_504d_v110_signal(revenue):
    """Exponential moving average of Raw level of revenue over 504d window."""
    res = _ewma(revenue, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_504d_v111_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 504d window."""
    res = _ewma(ebitda, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_504d_v112_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 504d window."""
    res = _ewma(_ratio(sgna, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_504d_v113_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 504d window."""
    res = _ewma(_ratio(ebitda, revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_504d_v114_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 504d window."""
    res = _ewma(_ratio(ebitda, sgna), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_756d_v115_signal(sgna):
    """Exponential moving average of Raw level of sgna over 756d window."""
    res = _ewma(sgna, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_756d_v116_signal(revenue):
    """Exponential moving average of Raw level of revenue over 756d window."""
    res = _ewma(revenue, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_756d_v117_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 756d window."""
    res = _ewma(ebitda, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_756d_v118_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 756d window."""
    res = _ewma(_ratio(sgna, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_756d_v119_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 756d window."""
    res = _ewma(_ratio(ebitda, revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_756d_v120_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 756d window."""
    res = _ewma(_ratio(ebitda, sgna), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_1008d_v121_signal(sgna):
    """Exponential moving average of Raw level of sgna over 1008d window."""
    res = _ewma(sgna, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_1008d_v122_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1008d window."""
    res = _ewma(revenue, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_1008d_v123_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 1008d window."""
    res = _ewma(ebitda, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_1008d_v124_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 1008d window."""
    res = _ewma(_ratio(sgna, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_1008d_v125_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 1008d window."""
    res = _ewma(_ratio(ebitda, revenue), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_1008d_v126_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 1008d window."""
    res = _ewma(_ratio(ebitda, sgna), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_ewma_1260d_v127_signal(sgna):
    """Exponential moving average of Raw level of sgna over 1260d window."""
    res = _ewma(sgna, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_ewma_1260d_v128_signal(revenue):
    """Exponential moving average of Raw level of revenue over 1260d window."""
    res = _ewma(revenue, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_ewma_1260d_v129_signal(ebitda):
    """Exponential moving average of Raw level of ebitda over 1260d window."""
    res = _ewma(ebitda, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_ewma_1260d_v130_signal(sgna, revenue):
    """Exponential moving average of SG&A efficiency ratio over 1260d window."""
    res = _ewma(_ratio(sgna, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_ewma_1260d_v131_signal(ebitda, revenue):
    """Exponential moving average of EBITDA margin strength over 1260d window."""
    res = _ewma(_ratio(ebitda, revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_ewma_1260d_v132_signal(ebitda, sgna):
    """Exponential moving average of Operating income per unit of overhead over 1260d window."""
    res = _ewma(_ratio(ebitda, sgna), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_z_5d_v133_signal(sgna):
    """Z-score of Raw level of sgna over 5d window."""
    res = _z(sgna, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_z_5d_v134_signal(revenue):
    """Z-score of Raw level of revenue over 5d window."""
    res = _z(revenue, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_z_5d_v135_signal(ebitda):
    """Z-score of Raw level of ebitda over 5d window."""
    res = _z(ebitda, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_z_5d_v136_signal(sgna, revenue):
    """Z-score of SG&A efficiency ratio over 5d window."""
    res = _z(_ratio(sgna, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_z_5d_v137_signal(ebitda, revenue):
    """Z-score of EBITDA margin strength over 5d window."""
    res = _z(_ratio(ebitda, revenue), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_z_5d_v138_signal(ebitda, sgna):
    """Z-score of Operating income per unit of overhead over 5d window."""
    res = _z(_ratio(ebitda, sgna), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_z_10d_v139_signal(sgna):
    """Z-score of Raw level of sgna over 10d window."""
    res = _z(sgna, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_z_10d_v140_signal(revenue):
    """Z-score of Raw level of revenue over 10d window."""
    res = _z(revenue, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_z_10d_v141_signal(ebitda):
    """Z-score of Raw level of ebitda over 10d window."""
    res = _z(ebitda, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_z_10d_v142_signal(sgna, revenue):
    """Z-score of SG&A efficiency ratio over 10d window."""
    res = _z(_ratio(sgna, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_z_10d_v143_signal(ebitda, revenue):
    """Z-score of EBITDA margin strength over 10d window."""
    res = _z(_ratio(ebitda, revenue), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_z_10d_v144_signal(ebitda, sgna):
    """Z-score of Operating income per unit of overhead over 10d window."""
    res = _z(_ratio(ebitda, sgna), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_z_21d_v145_signal(sgna):
    """Z-score of Raw level of sgna over 21d window."""
    res = _z(sgna, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_z_21d_v146_signal(revenue):
    """Z-score of Raw level of revenue over 21d window."""
    res = _z(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_z_21d_v147_signal(ebitda):
    """Z-score of Raw level of ebitda over 21d window."""
    res = _z(ebitda, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_z_21d_v148_signal(sgna, revenue):
    """Z-score of SG&A efficiency ratio over 21d window."""
    res = _z(_ratio(sgna, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_z_21d_v149_signal(ebitda, revenue):
    """Z-score of EBITDA margin strength over 21d window."""
    res = _z(_ratio(ebitda, revenue), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_z_21d_v150_signal(ebitda, sgna):
    """Z-score of Operating income per unit of overhead over 21d window."""
    res = _z(_ratio(ebitda, sgna), 21)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f04_efficiency_ratio_efficiency_score_ewma_10d_v076_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_10d_v076_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_10d_v077_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_10d_v077_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_10d_v078_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_10d_v078_signal},
    "f04_efficiency_ratio_sgna_ewma_21d_v079_signal": {"func": f04_efficiency_ratio_sgna_ewma_21d_v079_signal},
    "f04_efficiency_ratio_revenue_ewma_21d_v080_signal": {"func": f04_efficiency_ratio_revenue_ewma_21d_v080_signal},
    "f04_efficiency_ratio_ebitda_ewma_21d_v081_signal": {"func": f04_efficiency_ratio_ebitda_ewma_21d_v081_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_21d_v082_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_21d_v082_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_21d_v083_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_21d_v083_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_21d_v084_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_21d_v084_signal},
    "f04_efficiency_ratio_sgna_ewma_42d_v085_signal": {"func": f04_efficiency_ratio_sgna_ewma_42d_v085_signal},
    "f04_efficiency_ratio_revenue_ewma_42d_v086_signal": {"func": f04_efficiency_ratio_revenue_ewma_42d_v086_signal},
    "f04_efficiency_ratio_ebitda_ewma_42d_v087_signal": {"func": f04_efficiency_ratio_ebitda_ewma_42d_v087_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_42d_v088_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_42d_v088_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_42d_v089_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_42d_v089_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_42d_v090_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_42d_v090_signal},
    "f04_efficiency_ratio_sgna_ewma_63d_v091_signal": {"func": f04_efficiency_ratio_sgna_ewma_63d_v091_signal},
    "f04_efficiency_ratio_revenue_ewma_63d_v092_signal": {"func": f04_efficiency_ratio_revenue_ewma_63d_v092_signal},
    "f04_efficiency_ratio_ebitda_ewma_63d_v093_signal": {"func": f04_efficiency_ratio_ebitda_ewma_63d_v093_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_63d_v094_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_63d_v094_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_63d_v095_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_63d_v095_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_63d_v096_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_63d_v096_signal},
    "f04_efficiency_ratio_sgna_ewma_126d_v097_signal": {"func": f04_efficiency_ratio_sgna_ewma_126d_v097_signal},
    "f04_efficiency_ratio_revenue_ewma_126d_v098_signal": {"func": f04_efficiency_ratio_revenue_ewma_126d_v098_signal},
    "f04_efficiency_ratio_ebitda_ewma_126d_v099_signal": {"func": f04_efficiency_ratio_ebitda_ewma_126d_v099_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_126d_v100_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_126d_v100_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_126d_v101_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_126d_v101_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_126d_v102_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_126d_v102_signal},
    "f04_efficiency_ratio_sgna_ewma_252d_v103_signal": {"func": f04_efficiency_ratio_sgna_ewma_252d_v103_signal},
    "f04_efficiency_ratio_revenue_ewma_252d_v104_signal": {"func": f04_efficiency_ratio_revenue_ewma_252d_v104_signal},
    "f04_efficiency_ratio_ebitda_ewma_252d_v105_signal": {"func": f04_efficiency_ratio_ebitda_ewma_252d_v105_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_252d_v106_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_252d_v106_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_252d_v107_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_252d_v107_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_252d_v108_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_252d_v108_signal},
    "f04_efficiency_ratio_sgna_ewma_504d_v109_signal": {"func": f04_efficiency_ratio_sgna_ewma_504d_v109_signal},
    "f04_efficiency_ratio_revenue_ewma_504d_v110_signal": {"func": f04_efficiency_ratio_revenue_ewma_504d_v110_signal},
    "f04_efficiency_ratio_ebitda_ewma_504d_v111_signal": {"func": f04_efficiency_ratio_ebitda_ewma_504d_v111_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_504d_v112_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_504d_v112_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_504d_v113_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_504d_v113_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_504d_v114_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_504d_v114_signal},
    "f04_efficiency_ratio_sgna_ewma_756d_v115_signal": {"func": f04_efficiency_ratio_sgna_ewma_756d_v115_signal},
    "f04_efficiency_ratio_revenue_ewma_756d_v116_signal": {"func": f04_efficiency_ratio_revenue_ewma_756d_v116_signal},
    "f04_efficiency_ratio_ebitda_ewma_756d_v117_signal": {"func": f04_efficiency_ratio_ebitda_ewma_756d_v117_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_756d_v118_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_756d_v118_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_756d_v119_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_756d_v119_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_756d_v120_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_756d_v120_signal},
    "f04_efficiency_ratio_sgna_ewma_1008d_v121_signal": {"func": f04_efficiency_ratio_sgna_ewma_1008d_v121_signal},
    "f04_efficiency_ratio_revenue_ewma_1008d_v122_signal": {"func": f04_efficiency_ratio_revenue_ewma_1008d_v122_signal},
    "f04_efficiency_ratio_ebitda_ewma_1008d_v123_signal": {"func": f04_efficiency_ratio_ebitda_ewma_1008d_v123_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_1008d_v124_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_1008d_v124_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_1008d_v125_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_1008d_v125_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_1008d_v126_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_1008d_v126_signal},
    "f04_efficiency_ratio_sgna_ewma_1260d_v127_signal": {"func": f04_efficiency_ratio_sgna_ewma_1260d_v127_signal},
    "f04_efficiency_ratio_revenue_ewma_1260d_v128_signal": {"func": f04_efficiency_ratio_revenue_ewma_1260d_v128_signal},
    "f04_efficiency_ratio_ebitda_ewma_1260d_v129_signal": {"func": f04_efficiency_ratio_ebitda_ewma_1260d_v129_signal},
    "f04_efficiency_ratio_efficiency_score_ewma_1260d_v130_signal": {"func": f04_efficiency_ratio_efficiency_score_ewma_1260d_v130_signal},
    "f04_efficiency_ratio_ebitda_margin_ewma_1260d_v131_signal": {"func": f04_efficiency_ratio_ebitda_margin_ewma_1260d_v131_signal},
    "f04_efficiency_ratio_overhead_yield_ewma_1260d_v132_signal": {"func": f04_efficiency_ratio_overhead_yield_ewma_1260d_v132_signal},
    "f04_efficiency_ratio_sgna_z_5d_v133_signal": {"func": f04_efficiency_ratio_sgna_z_5d_v133_signal},
    "f04_efficiency_ratio_revenue_z_5d_v134_signal": {"func": f04_efficiency_ratio_revenue_z_5d_v134_signal},
    "f04_efficiency_ratio_ebitda_z_5d_v135_signal": {"func": f04_efficiency_ratio_ebitda_z_5d_v135_signal},
    "f04_efficiency_ratio_efficiency_score_z_5d_v136_signal": {"func": f04_efficiency_ratio_efficiency_score_z_5d_v136_signal},
    "f04_efficiency_ratio_ebitda_margin_z_5d_v137_signal": {"func": f04_efficiency_ratio_ebitda_margin_z_5d_v137_signal},
    "f04_efficiency_ratio_overhead_yield_z_5d_v138_signal": {"func": f04_efficiency_ratio_overhead_yield_z_5d_v138_signal},
    "f04_efficiency_ratio_sgna_z_10d_v139_signal": {"func": f04_efficiency_ratio_sgna_z_10d_v139_signal},
    "f04_efficiency_ratio_revenue_z_10d_v140_signal": {"func": f04_efficiency_ratio_revenue_z_10d_v140_signal},
    "f04_efficiency_ratio_ebitda_z_10d_v141_signal": {"func": f04_efficiency_ratio_ebitda_z_10d_v141_signal},
    "f04_efficiency_ratio_efficiency_score_z_10d_v142_signal": {"func": f04_efficiency_ratio_efficiency_score_z_10d_v142_signal},
    "f04_efficiency_ratio_ebitda_margin_z_10d_v143_signal": {"func": f04_efficiency_ratio_ebitda_margin_z_10d_v143_signal},
    "f04_efficiency_ratio_overhead_yield_z_10d_v144_signal": {"func": f04_efficiency_ratio_overhead_yield_z_10d_v144_signal},
    "f04_efficiency_ratio_sgna_z_21d_v145_signal": {"func": f04_efficiency_ratio_sgna_z_21d_v145_signal},
    "f04_efficiency_ratio_revenue_z_21d_v146_signal": {"func": f04_efficiency_ratio_revenue_z_21d_v146_signal},
    "f04_efficiency_ratio_ebitda_z_21d_v147_signal": {"func": f04_efficiency_ratio_ebitda_z_21d_v147_signal},
    "f04_efficiency_ratio_efficiency_score_z_21d_v148_signal": {"func": f04_efficiency_ratio_efficiency_score_z_21d_v148_signal},
    "f04_efficiency_ratio_ebitda_margin_z_21d_v149_signal": {"func": f04_efficiency_ratio_ebitda_margin_z_21d_v149_signal},
    "f04_efficiency_ratio_overhead_yield_z_21d_v150_signal": {"func": f04_efficiency_ratio_overhead_yield_z_21d_v150_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 04...")
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
