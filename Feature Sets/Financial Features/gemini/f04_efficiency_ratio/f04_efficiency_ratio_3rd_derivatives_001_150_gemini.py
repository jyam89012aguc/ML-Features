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

def f04_efficiency_ratio_sgna_slope_diff_norm_42d_v151_signal(sgna):
    """Normalized slope change for Raw level of sgna over 42d window."""
    res = (_slope_pct(sgna, 42).diff(42) / _sma(sgna.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_42d_v152_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_42d_v153_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 42d window."""
    res = (_slope_pct(ebitda, 42).diff(42) / _sma(ebitda.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_42d_v154_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 42d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 42).diff(42) / _sma(_ratio(sgna, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_42d_v155_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 42d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 42).diff(42) / _sma(_ratio(ebitda, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_42d_v156_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 42d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 42).diff(42) / _sma(_ratio(ebitda, sgna).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_63d_v157_signal(sgna):
    """Normalized slope change for Raw level of sgna over 63d window."""
    res = (_slope_pct(sgna, 63).diff(63) / _sma(sgna.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_63d_v158_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_63d_v159_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 63d window."""
    res = (_slope_pct(ebitda, 63).diff(63) / _sma(ebitda.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_63d_v160_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 63d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 63).diff(63) / _sma(_ratio(sgna, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_63d_v161_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 63d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 63).diff(63) / _sma(_ratio(ebitda, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_63d_v162_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 63d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 63).diff(63) / _sma(_ratio(ebitda, sgna).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_126d_v163_signal(sgna):
    """Normalized slope change for Raw level of sgna over 126d window."""
    res = (_slope_pct(sgna, 126).diff(126) / _sma(sgna.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_126d_v164_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_126d_v165_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 126d window."""
    res = (_slope_pct(ebitda, 126).diff(126) / _sma(ebitda.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_126d_v166_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 126d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 126).diff(126) / _sma(_ratio(sgna, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_126d_v167_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 126d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 126).diff(126) / _sma(_ratio(ebitda, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_126d_v168_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 126d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 126).diff(126) / _sma(_ratio(ebitda, sgna).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_252d_v169_signal(sgna):
    """Normalized slope change for Raw level of sgna over 252d window."""
    res = (_slope_pct(sgna, 252).diff(252) / _sma(sgna.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_252d_v170_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_252d_v171_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 252d window."""
    res = (_slope_pct(ebitda, 252).diff(252) / _sma(ebitda.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_252d_v172_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 252d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 252).diff(252) / _sma(_ratio(sgna, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_252d_v173_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 252d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 252).diff(252) / _sma(_ratio(ebitda, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_252d_v174_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 252d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 252).diff(252) / _sma(_ratio(ebitda, sgna).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_504d_v175_signal(sgna):
    """Normalized slope change for Raw level of sgna over 504d window."""
    res = (_slope_pct(sgna, 504).diff(504) / _sma(sgna.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_504d_v176_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_504d_v177_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 504d window."""
    res = (_slope_pct(ebitda, 504).diff(504) / _sma(ebitda.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_504d_v178_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 504d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 504).diff(504) / _sma(_ratio(sgna, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_504d_v179_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 504d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 504).diff(504) / _sma(_ratio(ebitda, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_504d_v180_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 504d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 504).diff(504) / _sma(_ratio(ebitda, sgna).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_756d_v181_signal(sgna):
    """Normalized slope change for Raw level of sgna over 756d window."""
    res = (_slope_pct(sgna, 756).diff(756) / _sma(sgna.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_756d_v182_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_756d_v183_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 756d window."""
    res = (_slope_pct(ebitda, 756).diff(756) / _sma(ebitda.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_756d_v184_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 756d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 756).diff(756) / _sma(_ratio(sgna, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_756d_v185_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 756d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 756).diff(756) / _sma(_ratio(ebitda, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_756d_v186_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 756d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 756).diff(756) / _sma(_ratio(ebitda, sgna).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_1008d_v187_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1008d window."""
    res = (_slope_pct(sgna, 1008).diff(1008) / _sma(sgna.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_1008d_v188_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_1008d_v189_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 1008d window."""
    res = (_slope_pct(ebitda, 1008).diff(1008) / _sma(ebitda.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_1008d_v190_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 1008d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 1008).diff(1008) / _sma(_ratio(sgna, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_1008d_v191_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 1008d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 1008).diff(1008) / _sma(_ratio(ebitda, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_1008d_v192_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 1008d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 1008).diff(1008) / _sma(_ratio(ebitda, sgna).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_slope_diff_norm_1260d_v193_signal(sgna):
    """Normalized slope change for Raw level of sgna over 1260d window."""
    res = (_slope_pct(sgna, 1260).diff(1260) / _sma(sgna.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_slope_diff_norm_1260d_v194_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_slope_diff_norm_1260d_v195_signal(ebitda):
    """Normalized slope change for Raw level of ebitda over 1260d window."""
    res = (_slope_pct(ebitda, 1260).diff(1260) / _sma(ebitda.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_slope_diff_norm_1260d_v196_signal(sgna, revenue):
    """Normalized slope change for SG&A efficiency ratio over 1260d window."""
    res = (_slope_pct(_ratio(sgna, revenue), 1260).diff(1260) / _sma(_ratio(sgna, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_slope_diff_norm_1260d_v197_signal(ebitda, revenue):
    """Normalized slope change for EBITDA margin strength over 1260d window."""
    res = (_slope_pct(_ratio(ebitda, revenue), 1260).diff(1260) / _sma(_ratio(ebitda, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_slope_diff_norm_1260d_v198_signal(ebitda, sgna):
    """Normalized slope change for Operating income per unit of overhead over 1260d window."""
    res = (_slope_pct(_ratio(ebitda, sgna), 1260).diff(1260) / _sma(_ratio(ebitda, sgna).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_5d_v199_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 5d window."""
    res = _z(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_5d_v200_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_5d_v201_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 5d window."""
    res = _z(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_5d_v202_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 5d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_5d_v203_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 5d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_5d_v204_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 5d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_10d_v205_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 10d window."""
    res = _z(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_10d_v206_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_10d_v207_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 10d window."""
    res = _z(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_10d_v208_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 10d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_10d_v209_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 10d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_10d_v210_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 10d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_21d_v211_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 21d window."""
    res = _z(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_21d_v212_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_21d_v213_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 21d window."""
    res = _z(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_21d_v214_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 21d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_21d_v215_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 21d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_21d_v216_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 21d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_42d_v217_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 42d window."""
    res = _z(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_42d_v218_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_42d_v219_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 42d window."""
    res = _z(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_42d_v220_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 42d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_42d_v221_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 42d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_42d_v222_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 42d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_63d_v223_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 63d window."""
    res = _z(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_63d_v224_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_63d_v225_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 63d window."""
    res = _z(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_63d_v226_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 63d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_63d_v227_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 63d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_63d_v228_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 63d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_126d_v229_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 126d window."""
    res = _z(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_126d_v230_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_126d_v231_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 126d window."""
    res = _z(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_126d_v232_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 126d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_126d_v233_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 126d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_126d_v234_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 126d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_252d_v235_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 252d window."""
    res = _z(_slope_pct(sgna, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_252d_v236_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_252d_v237_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 252d window."""
    res = _z(_slope_pct(ebitda, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_252d_v238_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 252d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_252d_v239_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 252d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_252d_v240_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 252d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_504d_v241_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 504d window."""
    res = _z(_slope_pct(sgna, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_504d_v242_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_504d_v243_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 504d window."""
    res = _z(_slope_pct(ebitda, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_504d_v244_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 504d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_504d_v245_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 504d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_504d_v246_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 504d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_756d_v247_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 756d window."""
    res = _z(_slope_pct(sgna, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_756d_v248_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_756d_v249_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 756d window."""
    res = _z(_slope_pct(ebitda, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_756d_v250_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 756d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_756d_v251_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 756d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_756d_v252_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 756d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_1008d_v253_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 1008d window."""
    res = _z(_slope_pct(sgna, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_1008d_v254_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_1008d_v255_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 1008d window."""
    res = _z(_slope_pct(ebitda, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_1008d_v256_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 1008d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_1008d_v257_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 1008d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_1008d_v258_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 1008d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_mom_z_1260d_v259_signal(sgna):
    """Relative momentum strength for Raw level of sgna over 1260d window."""
    res = _z(_slope_pct(sgna, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_mom_z_1260d_v260_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_mom_z_1260d_v261_signal(ebitda):
    """Relative momentum strength for Raw level of ebitda over 1260d window."""
    res = _z(_slope_pct(ebitda, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_mom_z_1260d_v262_signal(sgna, revenue):
    """Relative momentum strength for SG&A efficiency ratio over 1260d window."""
    res = _z(_slope_pct(_ratio(sgna, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_mom_z_1260d_v263_signal(ebitda, revenue):
    """Relative momentum strength for EBITDA margin strength over 1260d window."""
    res = _z(_slope_pct(_ratio(ebitda, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_mom_z_1260d_v264_signal(ebitda, sgna):
    """Relative momentum strength for Operating income per unit of overhead over 1260d window."""
    res = _z(_slope_pct(_ratio(ebitda, sgna), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_vol_slope_5d_v265_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 5d window."""
    res = _std(_slope_pct(sgna, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_vol_slope_5d_v266_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_vol_slope_5d_v267_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 5d window."""
    res = _std(_slope_pct(ebitda, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_vol_slope_5d_v268_signal(sgna, revenue):
    """Volatility of momentum for SG&A efficiency ratio over 5d window."""
    res = _std(_slope_pct(_ratio(sgna, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_vol_slope_5d_v269_signal(ebitda, revenue):
    """Volatility of momentum for EBITDA margin strength over 5d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_vol_slope_5d_v270_signal(ebitda, sgna):
    """Volatility of momentum for Operating income per unit of overhead over 5d window."""
    res = _std(_slope_pct(_ratio(ebitda, sgna), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_vol_slope_10d_v271_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 10d window."""
    res = _std(_slope_pct(sgna, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_vol_slope_10d_v272_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_vol_slope_10d_v273_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 10d window."""
    res = _std(_slope_pct(ebitda, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_vol_slope_10d_v274_signal(sgna, revenue):
    """Volatility of momentum for SG&A efficiency ratio over 10d window."""
    res = _std(_slope_pct(_ratio(sgna, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_vol_slope_10d_v275_signal(ebitda, revenue):
    """Volatility of momentum for EBITDA margin strength over 10d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_vol_slope_10d_v276_signal(ebitda, sgna):
    """Volatility of momentum for Operating income per unit of overhead over 10d window."""
    res = _std(_slope_pct(_ratio(ebitda, sgna), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_vol_slope_21d_v277_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 21d window."""
    res = _std(_slope_pct(sgna, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_vol_slope_21d_v278_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_vol_slope_21d_v279_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 21d window."""
    res = _std(_slope_pct(ebitda, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_vol_slope_21d_v280_signal(sgna, revenue):
    """Volatility of momentum for SG&A efficiency ratio over 21d window."""
    res = _std(_slope_pct(_ratio(sgna, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_vol_slope_21d_v281_signal(ebitda, revenue):
    """Volatility of momentum for EBITDA margin strength over 21d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_vol_slope_21d_v282_signal(ebitda, sgna):
    """Volatility of momentum for Operating income per unit of overhead over 21d window."""
    res = _std(_slope_pct(_ratio(ebitda, sgna), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_vol_slope_42d_v283_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 42d window."""
    res = _std(_slope_pct(sgna, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_vol_slope_42d_v284_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_vol_slope_42d_v285_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 42d window."""
    res = _std(_slope_pct(ebitda, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_vol_slope_42d_v286_signal(sgna, revenue):
    """Volatility of momentum for SG&A efficiency ratio over 42d window."""
    res = _std(_slope_pct(_ratio(sgna, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_vol_slope_42d_v287_signal(ebitda, revenue):
    """Volatility of momentum for EBITDA margin strength over 42d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_vol_slope_42d_v288_signal(ebitda, sgna):
    """Volatility of momentum for Operating income per unit of overhead over 42d window."""
    res = _std(_slope_pct(_ratio(ebitda, sgna), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_vol_slope_63d_v289_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 63d window."""
    res = _std(_slope_pct(sgna, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_vol_slope_63d_v290_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_vol_slope_63d_v291_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 63d window."""
    res = _std(_slope_pct(ebitda, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_vol_slope_63d_v292_signal(sgna, revenue):
    """Volatility of momentum for SG&A efficiency ratio over 63d window."""
    res = _std(_slope_pct(_ratio(sgna, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_vol_slope_63d_v293_signal(ebitda, revenue):
    """Volatility of momentum for EBITDA margin strength over 63d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_vol_slope_63d_v294_signal(ebitda, sgna):
    """Volatility of momentum for Operating income per unit of overhead over 63d window."""
    res = _std(_slope_pct(_ratio(ebitda, sgna), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_sgna_vol_slope_126d_v295_signal(sgna):
    """Volatility of momentum for Raw level of sgna over 126d window."""
    res = _std(_slope_pct(sgna, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_revenue_vol_slope_126d_v296_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_vol_slope_126d_v297_signal(ebitda):
    """Volatility of momentum for Raw level of ebitda over 126d window."""
    res = _std(_slope_pct(ebitda, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_efficiency_score_vol_slope_126d_v298_signal(sgna, revenue):
    """Volatility of momentum for SG&A efficiency ratio over 126d window."""
    res = _std(_slope_pct(_ratio(sgna, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_ebitda_margin_vol_slope_126d_v299_signal(ebitda, revenue):
    """Volatility of momentum for EBITDA margin strength over 126d window."""
    res = _std(_slope_pct(_ratio(ebitda, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f04_efficiency_ratio_overhead_yield_vol_slope_126d_v300_signal(ebitda, sgna):
    """Volatility of momentum for Operating income per unit of overhead over 126d window."""
    res = _std(_slope_pct(_ratio(ebitda, sgna), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f04_efficiency_ratio_sgna_slope_diff_norm_42d_v151_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_42d_v151_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_42d_v152_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_42d_v152_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_42d_v153_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_42d_v153_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_42d_v154_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_42d_v154_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_42d_v155_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_42d_v155_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_42d_v156_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_42d_v156_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_63d_v157_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_63d_v157_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_63d_v158_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_63d_v158_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_63d_v159_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_63d_v159_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_63d_v160_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_63d_v160_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_63d_v161_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_63d_v161_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_63d_v162_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_63d_v162_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_126d_v163_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_126d_v163_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_126d_v164_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_126d_v164_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_126d_v165_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_126d_v165_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_126d_v166_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_126d_v166_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_126d_v167_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_126d_v167_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_126d_v168_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_126d_v168_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_252d_v169_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_252d_v169_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_252d_v170_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_252d_v170_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_252d_v171_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_252d_v171_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_252d_v172_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_252d_v172_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_252d_v173_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_252d_v173_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_252d_v174_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_252d_v174_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_504d_v175_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_504d_v175_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_504d_v176_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_504d_v176_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_504d_v177_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_504d_v177_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_504d_v178_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_504d_v178_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_504d_v179_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_504d_v179_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_504d_v180_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_504d_v180_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_756d_v181_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_756d_v181_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_756d_v182_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_756d_v182_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_756d_v183_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_756d_v183_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_756d_v184_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_756d_v184_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_756d_v185_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_756d_v185_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_756d_v186_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_756d_v186_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_1008d_v187_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_1008d_v187_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_1008d_v188_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_1008d_v188_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_1008d_v189_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_1008d_v189_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_1008d_v190_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_1008d_v190_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_1008d_v191_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_1008d_v191_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_1008d_v192_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_1008d_v192_signal},
    "f04_efficiency_ratio_sgna_slope_diff_norm_1260d_v193_signal": {"func": f04_efficiency_ratio_sgna_slope_diff_norm_1260d_v193_signal},
    "f04_efficiency_ratio_revenue_slope_diff_norm_1260d_v194_signal": {"func": f04_efficiency_ratio_revenue_slope_diff_norm_1260d_v194_signal},
    "f04_efficiency_ratio_ebitda_slope_diff_norm_1260d_v195_signal": {"func": f04_efficiency_ratio_ebitda_slope_diff_norm_1260d_v195_signal},
    "f04_efficiency_ratio_efficiency_score_slope_diff_norm_1260d_v196_signal": {"func": f04_efficiency_ratio_efficiency_score_slope_diff_norm_1260d_v196_signal},
    "f04_efficiency_ratio_ebitda_margin_slope_diff_norm_1260d_v197_signal": {"func": f04_efficiency_ratio_ebitda_margin_slope_diff_norm_1260d_v197_signal},
    "f04_efficiency_ratio_overhead_yield_slope_diff_norm_1260d_v198_signal": {"func": f04_efficiency_ratio_overhead_yield_slope_diff_norm_1260d_v198_signal},
    "f04_efficiency_ratio_sgna_mom_z_5d_v199_signal": {"func": f04_efficiency_ratio_sgna_mom_z_5d_v199_signal},
    "f04_efficiency_ratio_revenue_mom_z_5d_v200_signal": {"func": f04_efficiency_ratio_revenue_mom_z_5d_v200_signal},
    "f04_efficiency_ratio_ebitda_mom_z_5d_v201_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_5d_v201_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_5d_v202_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_5d_v202_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_5d_v203_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_5d_v203_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_5d_v204_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_5d_v204_signal},
    "f04_efficiency_ratio_sgna_mom_z_10d_v205_signal": {"func": f04_efficiency_ratio_sgna_mom_z_10d_v205_signal},
    "f04_efficiency_ratio_revenue_mom_z_10d_v206_signal": {"func": f04_efficiency_ratio_revenue_mom_z_10d_v206_signal},
    "f04_efficiency_ratio_ebitda_mom_z_10d_v207_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_10d_v207_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_10d_v208_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_10d_v208_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_10d_v209_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_10d_v209_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_10d_v210_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_10d_v210_signal},
    "f04_efficiency_ratio_sgna_mom_z_21d_v211_signal": {"func": f04_efficiency_ratio_sgna_mom_z_21d_v211_signal},
    "f04_efficiency_ratio_revenue_mom_z_21d_v212_signal": {"func": f04_efficiency_ratio_revenue_mom_z_21d_v212_signal},
    "f04_efficiency_ratio_ebitda_mom_z_21d_v213_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_21d_v213_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_21d_v214_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_21d_v214_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_21d_v215_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_21d_v215_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_21d_v216_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_21d_v216_signal},
    "f04_efficiency_ratio_sgna_mom_z_42d_v217_signal": {"func": f04_efficiency_ratio_sgna_mom_z_42d_v217_signal},
    "f04_efficiency_ratio_revenue_mom_z_42d_v218_signal": {"func": f04_efficiency_ratio_revenue_mom_z_42d_v218_signal},
    "f04_efficiency_ratio_ebitda_mom_z_42d_v219_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_42d_v219_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_42d_v220_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_42d_v220_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_42d_v221_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_42d_v221_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_42d_v222_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_42d_v222_signal},
    "f04_efficiency_ratio_sgna_mom_z_63d_v223_signal": {"func": f04_efficiency_ratio_sgna_mom_z_63d_v223_signal},
    "f04_efficiency_ratio_revenue_mom_z_63d_v224_signal": {"func": f04_efficiency_ratio_revenue_mom_z_63d_v224_signal},
    "f04_efficiency_ratio_ebitda_mom_z_63d_v225_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_63d_v225_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_63d_v226_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_63d_v226_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_63d_v227_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_63d_v227_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_63d_v228_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_63d_v228_signal},
    "f04_efficiency_ratio_sgna_mom_z_126d_v229_signal": {"func": f04_efficiency_ratio_sgna_mom_z_126d_v229_signal},
    "f04_efficiency_ratio_revenue_mom_z_126d_v230_signal": {"func": f04_efficiency_ratio_revenue_mom_z_126d_v230_signal},
    "f04_efficiency_ratio_ebitda_mom_z_126d_v231_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_126d_v231_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_126d_v232_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_126d_v232_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_126d_v233_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_126d_v233_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_126d_v234_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_126d_v234_signal},
    "f04_efficiency_ratio_sgna_mom_z_252d_v235_signal": {"func": f04_efficiency_ratio_sgna_mom_z_252d_v235_signal},
    "f04_efficiency_ratio_revenue_mom_z_252d_v236_signal": {"func": f04_efficiency_ratio_revenue_mom_z_252d_v236_signal},
    "f04_efficiency_ratio_ebitda_mom_z_252d_v237_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_252d_v237_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_252d_v238_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_252d_v238_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_252d_v239_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_252d_v239_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_252d_v240_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_252d_v240_signal},
    "f04_efficiency_ratio_sgna_mom_z_504d_v241_signal": {"func": f04_efficiency_ratio_sgna_mom_z_504d_v241_signal},
    "f04_efficiency_ratio_revenue_mom_z_504d_v242_signal": {"func": f04_efficiency_ratio_revenue_mom_z_504d_v242_signal},
    "f04_efficiency_ratio_ebitda_mom_z_504d_v243_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_504d_v243_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_504d_v244_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_504d_v244_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_504d_v245_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_504d_v245_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_504d_v246_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_504d_v246_signal},
    "f04_efficiency_ratio_sgna_mom_z_756d_v247_signal": {"func": f04_efficiency_ratio_sgna_mom_z_756d_v247_signal},
    "f04_efficiency_ratio_revenue_mom_z_756d_v248_signal": {"func": f04_efficiency_ratio_revenue_mom_z_756d_v248_signal},
    "f04_efficiency_ratio_ebitda_mom_z_756d_v249_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_756d_v249_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_756d_v250_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_756d_v250_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_756d_v251_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_756d_v251_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_756d_v252_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_756d_v252_signal},
    "f04_efficiency_ratio_sgna_mom_z_1008d_v253_signal": {"func": f04_efficiency_ratio_sgna_mom_z_1008d_v253_signal},
    "f04_efficiency_ratio_revenue_mom_z_1008d_v254_signal": {"func": f04_efficiency_ratio_revenue_mom_z_1008d_v254_signal},
    "f04_efficiency_ratio_ebitda_mom_z_1008d_v255_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_1008d_v255_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_1008d_v256_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_1008d_v256_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_1008d_v257_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_1008d_v257_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_1008d_v258_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_1008d_v258_signal},
    "f04_efficiency_ratio_sgna_mom_z_1260d_v259_signal": {"func": f04_efficiency_ratio_sgna_mom_z_1260d_v259_signal},
    "f04_efficiency_ratio_revenue_mom_z_1260d_v260_signal": {"func": f04_efficiency_ratio_revenue_mom_z_1260d_v260_signal},
    "f04_efficiency_ratio_ebitda_mom_z_1260d_v261_signal": {"func": f04_efficiency_ratio_ebitda_mom_z_1260d_v261_signal},
    "f04_efficiency_ratio_efficiency_score_mom_z_1260d_v262_signal": {"func": f04_efficiency_ratio_efficiency_score_mom_z_1260d_v262_signal},
    "f04_efficiency_ratio_ebitda_margin_mom_z_1260d_v263_signal": {"func": f04_efficiency_ratio_ebitda_margin_mom_z_1260d_v263_signal},
    "f04_efficiency_ratio_overhead_yield_mom_z_1260d_v264_signal": {"func": f04_efficiency_ratio_overhead_yield_mom_z_1260d_v264_signal},
    "f04_efficiency_ratio_sgna_vol_slope_5d_v265_signal": {"func": f04_efficiency_ratio_sgna_vol_slope_5d_v265_signal},
    "f04_efficiency_ratio_revenue_vol_slope_5d_v266_signal": {"func": f04_efficiency_ratio_revenue_vol_slope_5d_v266_signal},
    "f04_efficiency_ratio_ebitda_vol_slope_5d_v267_signal": {"func": f04_efficiency_ratio_ebitda_vol_slope_5d_v267_signal},
    "f04_efficiency_ratio_efficiency_score_vol_slope_5d_v268_signal": {"func": f04_efficiency_ratio_efficiency_score_vol_slope_5d_v268_signal},
    "f04_efficiency_ratio_ebitda_margin_vol_slope_5d_v269_signal": {"func": f04_efficiency_ratio_ebitda_margin_vol_slope_5d_v269_signal},
    "f04_efficiency_ratio_overhead_yield_vol_slope_5d_v270_signal": {"func": f04_efficiency_ratio_overhead_yield_vol_slope_5d_v270_signal},
    "f04_efficiency_ratio_sgna_vol_slope_10d_v271_signal": {"func": f04_efficiency_ratio_sgna_vol_slope_10d_v271_signal},
    "f04_efficiency_ratio_revenue_vol_slope_10d_v272_signal": {"func": f04_efficiency_ratio_revenue_vol_slope_10d_v272_signal},
    "f04_efficiency_ratio_ebitda_vol_slope_10d_v273_signal": {"func": f04_efficiency_ratio_ebitda_vol_slope_10d_v273_signal},
    "f04_efficiency_ratio_efficiency_score_vol_slope_10d_v274_signal": {"func": f04_efficiency_ratio_efficiency_score_vol_slope_10d_v274_signal},
    "f04_efficiency_ratio_ebitda_margin_vol_slope_10d_v275_signal": {"func": f04_efficiency_ratio_ebitda_margin_vol_slope_10d_v275_signal},
    "f04_efficiency_ratio_overhead_yield_vol_slope_10d_v276_signal": {"func": f04_efficiency_ratio_overhead_yield_vol_slope_10d_v276_signal},
    "f04_efficiency_ratio_sgna_vol_slope_21d_v277_signal": {"func": f04_efficiency_ratio_sgna_vol_slope_21d_v277_signal},
    "f04_efficiency_ratio_revenue_vol_slope_21d_v278_signal": {"func": f04_efficiency_ratio_revenue_vol_slope_21d_v278_signal},
    "f04_efficiency_ratio_ebitda_vol_slope_21d_v279_signal": {"func": f04_efficiency_ratio_ebitda_vol_slope_21d_v279_signal},
    "f04_efficiency_ratio_efficiency_score_vol_slope_21d_v280_signal": {"func": f04_efficiency_ratio_efficiency_score_vol_slope_21d_v280_signal},
    "f04_efficiency_ratio_ebitda_margin_vol_slope_21d_v281_signal": {"func": f04_efficiency_ratio_ebitda_margin_vol_slope_21d_v281_signal},
    "f04_efficiency_ratio_overhead_yield_vol_slope_21d_v282_signal": {"func": f04_efficiency_ratio_overhead_yield_vol_slope_21d_v282_signal},
    "f04_efficiency_ratio_sgna_vol_slope_42d_v283_signal": {"func": f04_efficiency_ratio_sgna_vol_slope_42d_v283_signal},
    "f04_efficiency_ratio_revenue_vol_slope_42d_v284_signal": {"func": f04_efficiency_ratio_revenue_vol_slope_42d_v284_signal},
    "f04_efficiency_ratio_ebitda_vol_slope_42d_v285_signal": {"func": f04_efficiency_ratio_ebitda_vol_slope_42d_v285_signal},
    "f04_efficiency_ratio_efficiency_score_vol_slope_42d_v286_signal": {"func": f04_efficiency_ratio_efficiency_score_vol_slope_42d_v286_signal},
    "f04_efficiency_ratio_ebitda_margin_vol_slope_42d_v287_signal": {"func": f04_efficiency_ratio_ebitda_margin_vol_slope_42d_v287_signal},
    "f04_efficiency_ratio_overhead_yield_vol_slope_42d_v288_signal": {"func": f04_efficiency_ratio_overhead_yield_vol_slope_42d_v288_signal},
    "f04_efficiency_ratio_sgna_vol_slope_63d_v289_signal": {"func": f04_efficiency_ratio_sgna_vol_slope_63d_v289_signal},
    "f04_efficiency_ratio_revenue_vol_slope_63d_v290_signal": {"func": f04_efficiency_ratio_revenue_vol_slope_63d_v290_signal},
    "f04_efficiency_ratio_ebitda_vol_slope_63d_v291_signal": {"func": f04_efficiency_ratio_ebitda_vol_slope_63d_v291_signal},
    "f04_efficiency_ratio_efficiency_score_vol_slope_63d_v292_signal": {"func": f04_efficiency_ratio_efficiency_score_vol_slope_63d_v292_signal},
    "f04_efficiency_ratio_ebitda_margin_vol_slope_63d_v293_signal": {"func": f04_efficiency_ratio_ebitda_margin_vol_slope_63d_v293_signal},
    "f04_efficiency_ratio_overhead_yield_vol_slope_63d_v294_signal": {"func": f04_efficiency_ratio_overhead_yield_vol_slope_63d_v294_signal},
    "f04_efficiency_ratio_sgna_vol_slope_126d_v295_signal": {"func": f04_efficiency_ratio_sgna_vol_slope_126d_v295_signal},
    "f04_efficiency_ratio_revenue_vol_slope_126d_v296_signal": {"func": f04_efficiency_ratio_revenue_vol_slope_126d_v296_signal},
    "f04_efficiency_ratio_ebitda_vol_slope_126d_v297_signal": {"func": f04_efficiency_ratio_ebitda_vol_slope_126d_v297_signal},
    "f04_efficiency_ratio_efficiency_score_vol_slope_126d_v298_signal": {"func": f04_efficiency_ratio_efficiency_score_vol_slope_126d_v298_signal},
    "f04_efficiency_ratio_ebitda_margin_vol_slope_126d_v299_signal": {"func": f04_efficiency_ratio_ebitda_margin_vol_slope_126d_v299_signal},
    "f04_efficiency_ratio_overhead_yield_vol_slope_126d_v300_signal": {"func": f04_efficiency_ratio_overhead_yield_vol_slope_126d_v300_signal},
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
