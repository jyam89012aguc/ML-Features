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

def f07_insur_underwriting_cor_slope_diff_norm_42d_v151_signal(cor):
    """Normalized slope change for Raw level of cor over 42d window."""
    res = (_slope_pct(cor, 42).diff(42) / _sma(cor.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_42d_v152_signal(revenue):
    """Normalized slope change for Raw level of revenue over 42d window."""
    res = (_slope_pct(revenue, 42).diff(42) / _sma(revenue.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_42d_v153_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 42d window."""
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_42d_v154_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 42d window."""
    res = (_slope_pct(_ratio(cor, revenue), 42).diff(42) / _sma(_ratio(cor, revenue).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_42d_v155_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 42d window."""
    res = (_slope_pct(grossmargin, 42).diff(42) / _sma(grossmargin.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_42d_v156_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 42d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 42).diff(42) / _sma(_ratio(cor, grossmargin + cor).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_63d_v157_signal(cor):
    """Normalized slope change for Raw level of cor over 63d window."""
    res = (_slope_pct(cor, 63).diff(63) / _sma(cor.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_63d_v158_signal(revenue):
    """Normalized slope change for Raw level of revenue over 63d window."""
    res = (_slope_pct(revenue, 63).diff(63) / _sma(revenue.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_63d_v159_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 63d window."""
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_63d_v160_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 63d window."""
    res = (_slope_pct(_ratio(cor, revenue), 63).diff(63) / _sma(_ratio(cor, revenue).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_63d_v161_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 63d window."""
    res = (_slope_pct(grossmargin, 63).diff(63) / _sma(grossmargin.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_63d_v162_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 63d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 63).diff(63) / _sma(_ratio(cor, grossmargin + cor).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_126d_v163_signal(cor):
    """Normalized slope change for Raw level of cor over 126d window."""
    res = (_slope_pct(cor, 126).diff(126) / _sma(cor.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_126d_v164_signal(revenue):
    """Normalized slope change for Raw level of revenue over 126d window."""
    res = (_slope_pct(revenue, 126).diff(126) / _sma(revenue.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_126d_v165_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 126d window."""
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_126d_v166_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 126d window."""
    res = (_slope_pct(_ratio(cor, revenue), 126).diff(126) / _sma(_ratio(cor, revenue).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_126d_v167_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 126d window."""
    res = (_slope_pct(grossmargin, 126).diff(126) / _sma(grossmargin.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_126d_v168_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 126d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 126).diff(126) / _sma(_ratio(cor, grossmargin + cor).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_252d_v169_signal(cor):
    """Normalized slope change for Raw level of cor over 252d window."""
    res = (_slope_pct(cor, 252).diff(252) / _sma(cor.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_252d_v170_signal(revenue):
    """Normalized slope change for Raw level of revenue over 252d window."""
    res = (_slope_pct(revenue, 252).diff(252) / _sma(revenue.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_252d_v171_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 252d window."""
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_252d_v172_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 252d window."""
    res = (_slope_pct(_ratio(cor, revenue), 252).diff(252) / _sma(_ratio(cor, revenue).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_252d_v173_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 252d window."""
    res = (_slope_pct(grossmargin, 252).diff(252) / _sma(grossmargin.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_252d_v174_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 252d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 252).diff(252) / _sma(_ratio(cor, grossmargin + cor).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_504d_v175_signal(cor):
    """Normalized slope change for Raw level of cor over 504d window."""
    res = (_slope_pct(cor, 504).diff(504) / _sma(cor.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_504d_v176_signal(revenue):
    """Normalized slope change for Raw level of revenue over 504d window."""
    res = (_slope_pct(revenue, 504).diff(504) / _sma(revenue.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_504d_v177_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 504d window."""
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_504d_v178_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 504d window."""
    res = (_slope_pct(_ratio(cor, revenue), 504).diff(504) / _sma(_ratio(cor, revenue).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_504d_v179_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 504d window."""
    res = (_slope_pct(grossmargin, 504).diff(504) / _sma(grossmargin.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_504d_v180_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 504d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 504).diff(504) / _sma(_ratio(cor, grossmargin + cor).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_756d_v181_signal(cor):
    """Normalized slope change for Raw level of cor over 756d window."""
    res = (_slope_pct(cor, 756).diff(756) / _sma(cor.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_756d_v182_signal(revenue):
    """Normalized slope change for Raw level of revenue over 756d window."""
    res = (_slope_pct(revenue, 756).diff(756) / _sma(revenue.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_756d_v183_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 756d window."""
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_756d_v184_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 756d window."""
    res = (_slope_pct(_ratio(cor, revenue), 756).diff(756) / _sma(_ratio(cor, revenue).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_756d_v185_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 756d window."""
    res = (_slope_pct(grossmargin, 756).diff(756) / _sma(grossmargin.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_756d_v186_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 756d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 756).diff(756) / _sma(_ratio(cor, grossmargin + cor).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_1008d_v187_signal(cor):
    """Normalized slope change for Raw level of cor over 1008d window."""
    res = (_slope_pct(cor, 1008).diff(1008) / _sma(cor.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_1008d_v188_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1008d window."""
    res = (_slope_pct(revenue, 1008).diff(1008) / _sma(revenue.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_1008d_v189_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1008d window."""
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_1008d_v190_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 1008d window."""
    res = (_slope_pct(_ratio(cor, revenue), 1008).diff(1008) / _sma(_ratio(cor, revenue).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_1008d_v191_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 1008d window."""
    res = (_slope_pct(grossmargin, 1008).diff(1008) / _sma(grossmargin.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_1008d_v192_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 1008d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 1008).diff(1008) / _sma(_ratio(cor, grossmargin + cor).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_slope_diff_norm_1260d_v193_signal(cor):
    """Normalized slope change for Raw level of cor over 1260d window."""
    res = (_slope_pct(cor, 1260).diff(1260) / _sma(cor.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_slope_diff_norm_1260d_v194_signal(revenue):
    """Normalized slope change for Raw level of revenue over 1260d window."""
    res = (_slope_pct(revenue, 1260).diff(1260) / _sma(revenue.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_slope_diff_norm_1260d_v195_signal(grossmargin):
    """Normalized slope change for Raw level of grossmargin over 1260d window."""
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_slope_diff_norm_1260d_v196_signal(cor, revenue):
    """Normalized slope change for Insurance combined ratio proxy over 1260d window."""
    res = (_slope_pct(_ratio(cor, revenue), 1260).diff(1260) / _sma(_ratio(cor, revenue).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_slope_diff_norm_1260d_v197_signal(grossmargin):
    """Normalized slope change for Underwriting profitability over 1260d window."""
    res = (_slope_pct(grossmargin, 1260).diff(1260) / _sma(grossmargin.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_slope_diff_norm_1260d_v198_signal(cor, grossmargin):
    """Normalized slope change for Relative cost of premiums over 1260d window."""
    res = (_slope_pct(_ratio(cor, grossmargin + cor), 1260).diff(1260) / _sma(_ratio(cor, grossmargin + cor).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_5d_v199_signal(cor):
    """Relative momentum strength for Raw level of cor over 5d window."""
    res = _z(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_5d_v200_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 5d window."""
    res = _z(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_5d_v201_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 5d window."""
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_5d_v202_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 5d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_5d_v203_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 5d window."""
    res = _z(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_5d_v204_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 5d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_10d_v205_signal(cor):
    """Relative momentum strength for Raw level of cor over 10d window."""
    res = _z(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_10d_v206_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 10d window."""
    res = _z(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_10d_v207_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 10d window."""
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_10d_v208_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 10d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_10d_v209_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 10d window."""
    res = _z(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_10d_v210_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 10d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_21d_v211_signal(cor):
    """Relative momentum strength for Raw level of cor over 21d window."""
    res = _z(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_21d_v212_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 21d window."""
    res = _z(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_21d_v213_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 21d window."""
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_21d_v214_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 21d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_21d_v215_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 21d window."""
    res = _z(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_21d_v216_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 21d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_42d_v217_signal(cor):
    """Relative momentum strength for Raw level of cor over 42d window."""
    res = _z(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_42d_v218_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 42d window."""
    res = _z(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_42d_v219_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 42d window."""
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_42d_v220_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 42d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_42d_v221_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 42d window."""
    res = _z(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_42d_v222_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 42d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_63d_v223_signal(cor):
    """Relative momentum strength for Raw level of cor over 63d window."""
    res = _z(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_63d_v224_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 63d window."""
    res = _z(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_63d_v225_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 63d window."""
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_63d_v226_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 63d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_63d_v227_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 63d window."""
    res = _z(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_63d_v228_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 63d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_126d_v229_signal(cor):
    """Relative momentum strength for Raw level of cor over 126d window."""
    res = _z(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_126d_v230_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 126d window."""
    res = _z(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_126d_v231_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 126d window."""
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_126d_v232_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 126d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_126d_v233_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 126d window."""
    res = _z(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_126d_v234_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 126d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_252d_v235_signal(cor):
    """Relative momentum strength for Raw level of cor over 252d window."""
    res = _z(_slope_pct(cor, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_252d_v236_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 252d window."""
    res = _z(_slope_pct(revenue, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_252d_v237_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 252d window."""
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_252d_v238_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 252d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_252d_v239_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 252d window."""
    res = _z(_slope_pct(grossmargin, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_252d_v240_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 252d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_504d_v241_signal(cor):
    """Relative momentum strength for Raw level of cor over 504d window."""
    res = _z(_slope_pct(cor, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_504d_v242_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 504d window."""
    res = _z(_slope_pct(revenue, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_504d_v243_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 504d window."""
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_504d_v244_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 504d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_504d_v245_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 504d window."""
    res = _z(_slope_pct(grossmargin, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_504d_v246_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 504d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_756d_v247_signal(cor):
    """Relative momentum strength for Raw level of cor over 756d window."""
    res = _z(_slope_pct(cor, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_756d_v248_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 756d window."""
    res = _z(_slope_pct(revenue, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_756d_v249_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 756d window."""
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_756d_v250_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 756d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_756d_v251_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 756d window."""
    res = _z(_slope_pct(grossmargin, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_756d_v252_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 756d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_1008d_v253_signal(cor):
    """Relative momentum strength for Raw level of cor over 1008d window."""
    res = _z(_slope_pct(cor, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_1008d_v254_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1008d window."""
    res = _z(_slope_pct(revenue, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_1008d_v255_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 1008d window."""
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_1008d_v256_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 1008d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_1008d_v257_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 1008d window."""
    res = _z(_slope_pct(grossmargin, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_1008d_v258_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 1008d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_mom_z_1260d_v259_signal(cor):
    """Relative momentum strength for Raw level of cor over 1260d window."""
    res = _z(_slope_pct(cor, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_mom_z_1260d_v260_signal(revenue):
    """Relative momentum strength for Raw level of revenue over 1260d window."""
    res = _z(_slope_pct(revenue, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_mom_z_1260d_v261_signal(grossmargin):
    """Relative momentum strength for Raw level of grossmargin over 1260d window."""
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_mom_z_1260d_v262_signal(cor, revenue):
    """Relative momentum strength for Insurance combined ratio proxy over 1260d window."""
    res = _z(_slope_pct(_ratio(cor, revenue), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_mom_z_1260d_v263_signal(grossmargin):
    """Relative momentum strength for Underwriting profitability over 1260d window."""
    res = _z(_slope_pct(grossmargin, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_mom_z_1260d_v264_signal(cor, grossmargin):
    """Relative momentum strength for Relative cost of premiums over 1260d window."""
    res = _z(_slope_pct(_ratio(cor, grossmargin + cor), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_vol_slope_5d_v265_signal(cor):
    """Volatility of momentum for Raw level of cor over 5d window."""
    res = _std(_slope_pct(cor, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_vol_slope_5d_v266_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 5d window."""
    res = _std(_slope_pct(revenue, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_vol_slope_5d_v267_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 5d window."""
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_vol_slope_5d_v268_signal(cor, revenue):
    """Volatility of momentum for Insurance combined ratio proxy over 5d window."""
    res = _std(_slope_pct(_ratio(cor, revenue), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_vol_slope_5d_v269_signal(grossmargin):
    """Volatility of momentum for Underwriting profitability over 5d window."""
    res = _std(_slope_pct(grossmargin, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_vol_slope_5d_v270_signal(cor, grossmargin):
    """Volatility of momentum for Relative cost of premiums over 5d window."""
    res = _std(_slope_pct(_ratio(cor, grossmargin + cor), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_vol_slope_10d_v271_signal(cor):
    """Volatility of momentum for Raw level of cor over 10d window."""
    res = _std(_slope_pct(cor, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_vol_slope_10d_v272_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 10d window."""
    res = _std(_slope_pct(revenue, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_vol_slope_10d_v273_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 10d window."""
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_vol_slope_10d_v274_signal(cor, revenue):
    """Volatility of momentum for Insurance combined ratio proxy over 10d window."""
    res = _std(_slope_pct(_ratio(cor, revenue), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_vol_slope_10d_v275_signal(grossmargin):
    """Volatility of momentum for Underwriting profitability over 10d window."""
    res = _std(_slope_pct(grossmargin, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_vol_slope_10d_v276_signal(cor, grossmargin):
    """Volatility of momentum for Relative cost of premiums over 10d window."""
    res = _std(_slope_pct(_ratio(cor, grossmargin + cor), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_vol_slope_21d_v277_signal(cor):
    """Volatility of momentum for Raw level of cor over 21d window."""
    res = _std(_slope_pct(cor, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_vol_slope_21d_v278_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 21d window."""
    res = _std(_slope_pct(revenue, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_vol_slope_21d_v279_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 21d window."""
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_vol_slope_21d_v280_signal(cor, revenue):
    """Volatility of momentum for Insurance combined ratio proxy over 21d window."""
    res = _std(_slope_pct(_ratio(cor, revenue), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_vol_slope_21d_v281_signal(grossmargin):
    """Volatility of momentum for Underwriting profitability over 21d window."""
    res = _std(_slope_pct(grossmargin, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_vol_slope_21d_v282_signal(cor, grossmargin):
    """Volatility of momentum for Relative cost of premiums over 21d window."""
    res = _std(_slope_pct(_ratio(cor, grossmargin + cor), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_vol_slope_42d_v283_signal(cor):
    """Volatility of momentum for Raw level of cor over 42d window."""
    res = _std(_slope_pct(cor, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_vol_slope_42d_v284_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 42d window."""
    res = _std(_slope_pct(revenue, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_vol_slope_42d_v285_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 42d window."""
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_vol_slope_42d_v286_signal(cor, revenue):
    """Volatility of momentum for Insurance combined ratio proxy over 42d window."""
    res = _std(_slope_pct(_ratio(cor, revenue), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_vol_slope_42d_v287_signal(grossmargin):
    """Volatility of momentum for Underwriting profitability over 42d window."""
    res = _std(_slope_pct(grossmargin, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_vol_slope_42d_v288_signal(cor, grossmargin):
    """Volatility of momentum for Relative cost of premiums over 42d window."""
    res = _std(_slope_pct(_ratio(cor, grossmargin + cor), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_vol_slope_63d_v289_signal(cor):
    """Volatility of momentum for Raw level of cor over 63d window."""
    res = _std(_slope_pct(cor, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_vol_slope_63d_v290_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 63d window."""
    res = _std(_slope_pct(revenue, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_vol_slope_63d_v291_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 63d window."""
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_vol_slope_63d_v292_signal(cor, revenue):
    """Volatility of momentum for Insurance combined ratio proxy over 63d window."""
    res = _std(_slope_pct(_ratio(cor, revenue), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_vol_slope_63d_v293_signal(grossmargin):
    """Volatility of momentum for Underwriting profitability over 63d window."""
    res = _std(_slope_pct(grossmargin, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_vol_slope_63d_v294_signal(cor, grossmargin):
    """Volatility of momentum for Relative cost of premiums over 63d window."""
    res = _std(_slope_pct(_ratio(cor, grossmargin + cor), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_cor_vol_slope_126d_v295_signal(cor):
    """Volatility of momentum for Raw level of cor over 126d window."""
    res = _std(_slope_pct(cor, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_revenue_vol_slope_126d_v296_signal(revenue):
    """Volatility of momentum for Raw level of revenue over 126d window."""
    res = _std(_slope_pct(revenue, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_grossmargin_vol_slope_126d_v297_signal(grossmargin):
    """Volatility of momentum for Raw level of grossmargin over 126d window."""
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_combined_ratio_vol_slope_126d_v298_signal(cor, revenue):
    """Volatility of momentum for Insurance combined ratio proxy over 126d window."""
    res = _std(_slope_pct(_ratio(cor, revenue), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_uw_profitability_vol_slope_126d_v299_signal(grossmargin):
    """Volatility of momentum for Underwriting profitability over 126d window."""
    res = _std(_slope_pct(grossmargin, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f07_insur_underwriting_loss_load_vol_slope_126d_v300_signal(cor, grossmargin):
    """Volatility of momentum for Relative cost of premiums over 126d window."""
    res = _std(_slope_pct(_ratio(cor, grossmargin + cor), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f07_insur_underwriting_cor_slope_diff_norm_42d_v151_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_42d_v151_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_42d_v152_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_42d_v152_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_42d_v153_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_42d_v153_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_42d_v154_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_42d_v154_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_42d_v155_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_42d_v155_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_42d_v156_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_42d_v156_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_63d_v157_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_63d_v157_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_63d_v158_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_63d_v158_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_63d_v159_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_63d_v159_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_63d_v160_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_63d_v160_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_63d_v161_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_63d_v161_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_63d_v162_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_63d_v162_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_126d_v163_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_126d_v163_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_126d_v164_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_126d_v164_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_126d_v165_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_126d_v165_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_126d_v166_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_126d_v166_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_126d_v167_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_126d_v167_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_126d_v168_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_126d_v168_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_252d_v169_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_252d_v169_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_252d_v170_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_252d_v170_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_252d_v171_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_252d_v171_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_252d_v172_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_252d_v172_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_252d_v173_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_252d_v173_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_252d_v174_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_252d_v174_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_504d_v175_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_504d_v175_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_504d_v176_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_504d_v176_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_504d_v177_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_504d_v177_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_504d_v178_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_504d_v178_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_504d_v179_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_504d_v179_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_504d_v180_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_504d_v180_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_756d_v181_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_756d_v181_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_756d_v182_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_756d_v182_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_756d_v183_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_756d_v183_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_756d_v184_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_756d_v184_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_756d_v185_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_756d_v185_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_756d_v186_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_756d_v186_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_1008d_v187_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_1008d_v187_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_1008d_v188_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_1008d_v188_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_1008d_v189_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_1008d_v189_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_1008d_v190_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_1008d_v190_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_1008d_v191_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_1008d_v191_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_1008d_v192_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_1008d_v192_signal},
    "f07_insur_underwriting_cor_slope_diff_norm_1260d_v193_signal": {"func": f07_insur_underwriting_cor_slope_diff_norm_1260d_v193_signal},
    "f07_insur_underwriting_revenue_slope_diff_norm_1260d_v194_signal": {"func": f07_insur_underwriting_revenue_slope_diff_norm_1260d_v194_signal},
    "f07_insur_underwriting_grossmargin_slope_diff_norm_1260d_v195_signal": {"func": f07_insur_underwriting_grossmargin_slope_diff_norm_1260d_v195_signal},
    "f07_insur_underwriting_combined_ratio_slope_diff_norm_1260d_v196_signal": {"func": f07_insur_underwriting_combined_ratio_slope_diff_norm_1260d_v196_signal},
    "f07_insur_underwriting_uw_profitability_slope_diff_norm_1260d_v197_signal": {"func": f07_insur_underwriting_uw_profitability_slope_diff_norm_1260d_v197_signal},
    "f07_insur_underwriting_loss_load_slope_diff_norm_1260d_v198_signal": {"func": f07_insur_underwriting_loss_load_slope_diff_norm_1260d_v198_signal},
    "f07_insur_underwriting_cor_mom_z_5d_v199_signal": {"func": f07_insur_underwriting_cor_mom_z_5d_v199_signal},
    "f07_insur_underwriting_revenue_mom_z_5d_v200_signal": {"func": f07_insur_underwriting_revenue_mom_z_5d_v200_signal},
    "f07_insur_underwriting_grossmargin_mom_z_5d_v201_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_5d_v201_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_5d_v202_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_5d_v202_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_5d_v203_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_5d_v203_signal},
    "f07_insur_underwriting_loss_load_mom_z_5d_v204_signal": {"func": f07_insur_underwriting_loss_load_mom_z_5d_v204_signal},
    "f07_insur_underwriting_cor_mom_z_10d_v205_signal": {"func": f07_insur_underwriting_cor_mom_z_10d_v205_signal},
    "f07_insur_underwriting_revenue_mom_z_10d_v206_signal": {"func": f07_insur_underwriting_revenue_mom_z_10d_v206_signal},
    "f07_insur_underwriting_grossmargin_mom_z_10d_v207_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_10d_v207_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_10d_v208_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_10d_v208_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_10d_v209_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_10d_v209_signal},
    "f07_insur_underwriting_loss_load_mom_z_10d_v210_signal": {"func": f07_insur_underwriting_loss_load_mom_z_10d_v210_signal},
    "f07_insur_underwriting_cor_mom_z_21d_v211_signal": {"func": f07_insur_underwriting_cor_mom_z_21d_v211_signal},
    "f07_insur_underwriting_revenue_mom_z_21d_v212_signal": {"func": f07_insur_underwriting_revenue_mom_z_21d_v212_signal},
    "f07_insur_underwriting_grossmargin_mom_z_21d_v213_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_21d_v213_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_21d_v214_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_21d_v214_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_21d_v215_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_21d_v215_signal},
    "f07_insur_underwriting_loss_load_mom_z_21d_v216_signal": {"func": f07_insur_underwriting_loss_load_mom_z_21d_v216_signal},
    "f07_insur_underwriting_cor_mom_z_42d_v217_signal": {"func": f07_insur_underwriting_cor_mom_z_42d_v217_signal},
    "f07_insur_underwriting_revenue_mom_z_42d_v218_signal": {"func": f07_insur_underwriting_revenue_mom_z_42d_v218_signal},
    "f07_insur_underwriting_grossmargin_mom_z_42d_v219_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_42d_v219_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_42d_v220_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_42d_v220_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_42d_v221_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_42d_v221_signal},
    "f07_insur_underwriting_loss_load_mom_z_42d_v222_signal": {"func": f07_insur_underwriting_loss_load_mom_z_42d_v222_signal},
    "f07_insur_underwriting_cor_mom_z_63d_v223_signal": {"func": f07_insur_underwriting_cor_mom_z_63d_v223_signal},
    "f07_insur_underwriting_revenue_mom_z_63d_v224_signal": {"func": f07_insur_underwriting_revenue_mom_z_63d_v224_signal},
    "f07_insur_underwriting_grossmargin_mom_z_63d_v225_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_63d_v225_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_63d_v226_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_63d_v226_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_63d_v227_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_63d_v227_signal},
    "f07_insur_underwriting_loss_load_mom_z_63d_v228_signal": {"func": f07_insur_underwriting_loss_load_mom_z_63d_v228_signal},
    "f07_insur_underwriting_cor_mom_z_126d_v229_signal": {"func": f07_insur_underwriting_cor_mom_z_126d_v229_signal},
    "f07_insur_underwriting_revenue_mom_z_126d_v230_signal": {"func": f07_insur_underwriting_revenue_mom_z_126d_v230_signal},
    "f07_insur_underwriting_grossmargin_mom_z_126d_v231_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_126d_v231_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_126d_v232_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_126d_v232_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_126d_v233_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_126d_v233_signal},
    "f07_insur_underwriting_loss_load_mom_z_126d_v234_signal": {"func": f07_insur_underwriting_loss_load_mom_z_126d_v234_signal},
    "f07_insur_underwriting_cor_mom_z_252d_v235_signal": {"func": f07_insur_underwriting_cor_mom_z_252d_v235_signal},
    "f07_insur_underwriting_revenue_mom_z_252d_v236_signal": {"func": f07_insur_underwriting_revenue_mom_z_252d_v236_signal},
    "f07_insur_underwriting_grossmargin_mom_z_252d_v237_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_252d_v237_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_252d_v238_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_252d_v238_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_252d_v239_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_252d_v239_signal},
    "f07_insur_underwriting_loss_load_mom_z_252d_v240_signal": {"func": f07_insur_underwriting_loss_load_mom_z_252d_v240_signal},
    "f07_insur_underwriting_cor_mom_z_504d_v241_signal": {"func": f07_insur_underwriting_cor_mom_z_504d_v241_signal},
    "f07_insur_underwriting_revenue_mom_z_504d_v242_signal": {"func": f07_insur_underwriting_revenue_mom_z_504d_v242_signal},
    "f07_insur_underwriting_grossmargin_mom_z_504d_v243_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_504d_v243_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_504d_v244_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_504d_v244_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_504d_v245_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_504d_v245_signal},
    "f07_insur_underwriting_loss_load_mom_z_504d_v246_signal": {"func": f07_insur_underwriting_loss_load_mom_z_504d_v246_signal},
    "f07_insur_underwriting_cor_mom_z_756d_v247_signal": {"func": f07_insur_underwriting_cor_mom_z_756d_v247_signal},
    "f07_insur_underwriting_revenue_mom_z_756d_v248_signal": {"func": f07_insur_underwriting_revenue_mom_z_756d_v248_signal},
    "f07_insur_underwriting_grossmargin_mom_z_756d_v249_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_756d_v249_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_756d_v250_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_756d_v250_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_756d_v251_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_756d_v251_signal},
    "f07_insur_underwriting_loss_load_mom_z_756d_v252_signal": {"func": f07_insur_underwriting_loss_load_mom_z_756d_v252_signal},
    "f07_insur_underwriting_cor_mom_z_1008d_v253_signal": {"func": f07_insur_underwriting_cor_mom_z_1008d_v253_signal},
    "f07_insur_underwriting_revenue_mom_z_1008d_v254_signal": {"func": f07_insur_underwriting_revenue_mom_z_1008d_v254_signal},
    "f07_insur_underwriting_grossmargin_mom_z_1008d_v255_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_1008d_v255_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_1008d_v256_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_1008d_v256_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_1008d_v257_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_1008d_v257_signal},
    "f07_insur_underwriting_loss_load_mom_z_1008d_v258_signal": {"func": f07_insur_underwriting_loss_load_mom_z_1008d_v258_signal},
    "f07_insur_underwriting_cor_mom_z_1260d_v259_signal": {"func": f07_insur_underwriting_cor_mom_z_1260d_v259_signal},
    "f07_insur_underwriting_revenue_mom_z_1260d_v260_signal": {"func": f07_insur_underwriting_revenue_mom_z_1260d_v260_signal},
    "f07_insur_underwriting_grossmargin_mom_z_1260d_v261_signal": {"func": f07_insur_underwriting_grossmargin_mom_z_1260d_v261_signal},
    "f07_insur_underwriting_combined_ratio_mom_z_1260d_v262_signal": {"func": f07_insur_underwriting_combined_ratio_mom_z_1260d_v262_signal},
    "f07_insur_underwriting_uw_profitability_mom_z_1260d_v263_signal": {"func": f07_insur_underwriting_uw_profitability_mom_z_1260d_v263_signal},
    "f07_insur_underwriting_loss_load_mom_z_1260d_v264_signal": {"func": f07_insur_underwriting_loss_load_mom_z_1260d_v264_signal},
    "f07_insur_underwriting_cor_vol_slope_5d_v265_signal": {"func": f07_insur_underwriting_cor_vol_slope_5d_v265_signal},
    "f07_insur_underwriting_revenue_vol_slope_5d_v266_signal": {"func": f07_insur_underwriting_revenue_vol_slope_5d_v266_signal},
    "f07_insur_underwriting_grossmargin_vol_slope_5d_v267_signal": {"func": f07_insur_underwriting_grossmargin_vol_slope_5d_v267_signal},
    "f07_insur_underwriting_combined_ratio_vol_slope_5d_v268_signal": {"func": f07_insur_underwriting_combined_ratio_vol_slope_5d_v268_signal},
    "f07_insur_underwriting_uw_profitability_vol_slope_5d_v269_signal": {"func": f07_insur_underwriting_uw_profitability_vol_slope_5d_v269_signal},
    "f07_insur_underwriting_loss_load_vol_slope_5d_v270_signal": {"func": f07_insur_underwriting_loss_load_vol_slope_5d_v270_signal},
    "f07_insur_underwriting_cor_vol_slope_10d_v271_signal": {"func": f07_insur_underwriting_cor_vol_slope_10d_v271_signal},
    "f07_insur_underwriting_revenue_vol_slope_10d_v272_signal": {"func": f07_insur_underwriting_revenue_vol_slope_10d_v272_signal},
    "f07_insur_underwriting_grossmargin_vol_slope_10d_v273_signal": {"func": f07_insur_underwriting_grossmargin_vol_slope_10d_v273_signal},
    "f07_insur_underwriting_combined_ratio_vol_slope_10d_v274_signal": {"func": f07_insur_underwriting_combined_ratio_vol_slope_10d_v274_signal},
    "f07_insur_underwriting_uw_profitability_vol_slope_10d_v275_signal": {"func": f07_insur_underwriting_uw_profitability_vol_slope_10d_v275_signal},
    "f07_insur_underwriting_loss_load_vol_slope_10d_v276_signal": {"func": f07_insur_underwriting_loss_load_vol_slope_10d_v276_signal},
    "f07_insur_underwriting_cor_vol_slope_21d_v277_signal": {"func": f07_insur_underwriting_cor_vol_slope_21d_v277_signal},
    "f07_insur_underwriting_revenue_vol_slope_21d_v278_signal": {"func": f07_insur_underwriting_revenue_vol_slope_21d_v278_signal},
    "f07_insur_underwriting_grossmargin_vol_slope_21d_v279_signal": {"func": f07_insur_underwriting_grossmargin_vol_slope_21d_v279_signal},
    "f07_insur_underwriting_combined_ratio_vol_slope_21d_v280_signal": {"func": f07_insur_underwriting_combined_ratio_vol_slope_21d_v280_signal},
    "f07_insur_underwriting_uw_profitability_vol_slope_21d_v281_signal": {"func": f07_insur_underwriting_uw_profitability_vol_slope_21d_v281_signal},
    "f07_insur_underwriting_loss_load_vol_slope_21d_v282_signal": {"func": f07_insur_underwriting_loss_load_vol_slope_21d_v282_signal},
    "f07_insur_underwriting_cor_vol_slope_42d_v283_signal": {"func": f07_insur_underwriting_cor_vol_slope_42d_v283_signal},
    "f07_insur_underwriting_revenue_vol_slope_42d_v284_signal": {"func": f07_insur_underwriting_revenue_vol_slope_42d_v284_signal},
    "f07_insur_underwriting_grossmargin_vol_slope_42d_v285_signal": {"func": f07_insur_underwriting_grossmargin_vol_slope_42d_v285_signal},
    "f07_insur_underwriting_combined_ratio_vol_slope_42d_v286_signal": {"func": f07_insur_underwriting_combined_ratio_vol_slope_42d_v286_signal},
    "f07_insur_underwriting_uw_profitability_vol_slope_42d_v287_signal": {"func": f07_insur_underwriting_uw_profitability_vol_slope_42d_v287_signal},
    "f07_insur_underwriting_loss_load_vol_slope_42d_v288_signal": {"func": f07_insur_underwriting_loss_load_vol_slope_42d_v288_signal},
    "f07_insur_underwriting_cor_vol_slope_63d_v289_signal": {"func": f07_insur_underwriting_cor_vol_slope_63d_v289_signal},
    "f07_insur_underwriting_revenue_vol_slope_63d_v290_signal": {"func": f07_insur_underwriting_revenue_vol_slope_63d_v290_signal},
    "f07_insur_underwriting_grossmargin_vol_slope_63d_v291_signal": {"func": f07_insur_underwriting_grossmargin_vol_slope_63d_v291_signal},
    "f07_insur_underwriting_combined_ratio_vol_slope_63d_v292_signal": {"func": f07_insur_underwriting_combined_ratio_vol_slope_63d_v292_signal},
    "f07_insur_underwriting_uw_profitability_vol_slope_63d_v293_signal": {"func": f07_insur_underwriting_uw_profitability_vol_slope_63d_v293_signal},
    "f07_insur_underwriting_loss_load_vol_slope_63d_v294_signal": {"func": f07_insur_underwriting_loss_load_vol_slope_63d_v294_signal},
    "f07_insur_underwriting_cor_vol_slope_126d_v295_signal": {"func": f07_insur_underwriting_cor_vol_slope_126d_v295_signal},
    "f07_insur_underwriting_revenue_vol_slope_126d_v296_signal": {"func": f07_insur_underwriting_revenue_vol_slope_126d_v296_signal},
    "f07_insur_underwriting_grossmargin_vol_slope_126d_v297_signal": {"func": f07_insur_underwriting_grossmargin_vol_slope_126d_v297_signal},
    "f07_insur_underwriting_combined_ratio_vol_slope_126d_v298_signal": {"func": f07_insur_underwriting_combined_ratio_vol_slope_126d_v298_signal},
    "f07_insur_underwriting_uw_profitability_vol_slope_126d_v299_signal": {"func": f07_insur_underwriting_uw_profitability_vol_slope_126d_v299_signal},
    "f07_insur_underwriting_loss_load_vol_slope_126d_v300_signal": {"func": f07_insur_underwriting_loss_load_vol_slope_126d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "revenue": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 07...")
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
