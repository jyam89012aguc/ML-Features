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

def f02_tbvps_growth_tangibles_slope_diff_norm_42d_v151_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 42d window."""
    res = (_slope_pct(tangibles, 42).diff(42) / _sma(tangibles.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_42d_v152_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 42d window."""
    res = (_slope_pct(shareswa, 42).diff(42) / _sma(shareswa.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_42d_v153_signal(bvps):
    """Normalized slope change for Raw level of bvps over 42d window."""
    res = (_slope_pct(bvps, 42).diff(42) / _sma(bvps.abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_42d_v154_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 42d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 42).diff(42) / _sma(_ratio(tangibles, shareswa).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_42d_v155_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 42d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 42).diff(42) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_42d_v156_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 42d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 42).diff(42) / _sma(_ratio(tangibles, assets).abs(), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_63d_v157_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 63d window."""
    res = (_slope_pct(tangibles, 63).diff(63) / _sma(tangibles.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_63d_v158_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 63d window."""
    res = (_slope_pct(shareswa, 63).diff(63) / _sma(shareswa.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_63d_v159_signal(bvps):
    """Normalized slope change for Raw level of bvps over 63d window."""
    res = (_slope_pct(bvps, 63).diff(63) / _sma(bvps.abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_63d_v160_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 63d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 63).diff(63) / _sma(_ratio(tangibles, shareswa).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_63d_v161_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 63d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 63).diff(63) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_63d_v162_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 63d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 63).diff(63) / _sma(_ratio(tangibles, assets).abs(), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_126d_v163_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 126d window."""
    res = (_slope_pct(tangibles, 126).diff(126) / _sma(tangibles.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_126d_v164_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 126d window."""
    res = (_slope_pct(shareswa, 126).diff(126) / _sma(shareswa.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_126d_v165_signal(bvps):
    """Normalized slope change for Raw level of bvps over 126d window."""
    res = (_slope_pct(bvps, 126).diff(126) / _sma(bvps.abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_126d_v166_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 126d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 126).diff(126) / _sma(_ratio(tangibles, shareswa).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_126d_v167_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 126d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 126).diff(126) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_126d_v168_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 126d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 126).diff(126) / _sma(_ratio(tangibles, assets).abs(), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_252d_v169_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 252d window."""
    res = (_slope_pct(tangibles, 252).diff(252) / _sma(tangibles.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_252d_v170_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 252d window."""
    res = (_slope_pct(shareswa, 252).diff(252) / _sma(shareswa.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_252d_v171_signal(bvps):
    """Normalized slope change for Raw level of bvps over 252d window."""
    res = (_slope_pct(bvps, 252).diff(252) / _sma(bvps.abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_252d_v172_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 252d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 252).diff(252) / _sma(_ratio(tangibles, shareswa).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_252d_v173_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 252d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 252).diff(252) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_252d_v174_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 252d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 252).diff(252) / _sma(_ratio(tangibles, assets).abs(), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_504d_v175_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 504d window."""
    res = (_slope_pct(tangibles, 504).diff(504) / _sma(tangibles.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_504d_v176_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 504d window."""
    res = (_slope_pct(shareswa, 504).diff(504) / _sma(shareswa.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_504d_v177_signal(bvps):
    """Normalized slope change for Raw level of bvps over 504d window."""
    res = (_slope_pct(bvps, 504).diff(504) / _sma(bvps.abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_504d_v178_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 504d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 504).diff(504) / _sma(_ratio(tangibles, shareswa).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_504d_v179_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 504d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 504).diff(504) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_504d_v180_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 504d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 504).diff(504) / _sma(_ratio(tangibles, assets).abs(), 504).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_756d_v181_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 756d window."""
    res = (_slope_pct(tangibles, 756).diff(756) / _sma(tangibles.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_756d_v182_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 756d window."""
    res = (_slope_pct(shareswa, 756).diff(756) / _sma(shareswa.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_756d_v183_signal(bvps):
    """Normalized slope change for Raw level of bvps over 756d window."""
    res = (_slope_pct(bvps, 756).diff(756) / _sma(bvps.abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_756d_v184_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 756d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 756).diff(756) / _sma(_ratio(tangibles, shareswa).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_756d_v185_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 756d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 756).diff(756) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_756d_v186_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 756d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 756).diff(756) / _sma(_ratio(tangibles, assets).abs(), 756).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_1008d_v187_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 1008d window."""
    res = (_slope_pct(tangibles, 1008).diff(1008) / _sma(tangibles.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_1008d_v188_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 1008d window."""
    res = (_slope_pct(shareswa, 1008).diff(1008) / _sma(shareswa.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_1008d_v189_signal(bvps):
    """Normalized slope change for Raw level of bvps over 1008d window."""
    res = (_slope_pct(bvps, 1008).diff(1008) / _sma(bvps.abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_1008d_v190_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 1008d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 1008).diff(1008) / _sma(_ratio(tangibles, shareswa).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_1008d_v191_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 1008d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 1008).diff(1008) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_1008d_v192_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 1008d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 1008).diff(1008) / _sma(_ratio(tangibles, assets).abs(), 1008).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_slope_diff_norm_1260d_v193_signal(tangibles):
    """Normalized slope change for Raw level of tangibles over 1260d window."""
    res = (_slope_pct(tangibles, 1260).diff(1260) / _sma(tangibles.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_slope_diff_norm_1260d_v194_signal(shareswa):
    """Normalized slope change for Raw level of shareswa over 1260d window."""
    res = (_slope_pct(shareswa, 1260).diff(1260) / _sma(shareswa.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_slope_diff_norm_1260d_v195_signal(bvps):
    """Normalized slope change for Raw level of bvps over 1260d window."""
    res = (_slope_pct(bvps, 1260).diff(1260) / _sma(bvps.abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_slope_diff_norm_1260d_v196_signal(tangibles, shareswa):
    """Normalized slope change for Tangible book per share over 1260d window."""
    res = (_slope_pct(_ratio(tangibles, shareswa), 1260).diff(1260) / _sma(_ratio(tangibles, shareswa).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_1260d_v197_signal(tangibles, bvps, shareswa):
    """Normalized slope change for Tangible concentration of book value over 1260d window."""
    res = (_slope_pct(_ratio(tangibles, bvps * shareswa), 1260).diff(1260) / _sma(_ratio(tangibles, bvps * shareswa).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_slope_diff_norm_1260d_v198_signal(tangibles, assets):
    """Normalized slope change for Tangible asset density over 1260d window."""
    res = (_slope_pct(_ratio(tangibles, assets), 1260).diff(1260) / _sma(_ratio(tangibles, assets).abs(), 1260).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_5d_v199_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 5d window."""
    res = _z(_slope_pct(tangibles, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_5d_v200_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 5d window."""
    res = _z(_slope_pct(shareswa, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_5d_v201_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 5d window."""
    res = _z(_slope_pct(bvps, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_5d_v202_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 5d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_5d_v203_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 5d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_5d_v204_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 5d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_10d_v205_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 10d window."""
    res = _z(_slope_pct(tangibles, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_10d_v206_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 10d window."""
    res = _z(_slope_pct(shareswa, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_10d_v207_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 10d window."""
    res = _z(_slope_pct(bvps, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_10d_v208_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 10d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_10d_v209_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 10d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_10d_v210_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 10d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_21d_v211_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 21d window."""
    res = _z(_slope_pct(tangibles, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_21d_v212_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 21d window."""
    res = _z(_slope_pct(shareswa, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_21d_v213_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 21d window."""
    res = _z(_slope_pct(bvps, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_21d_v214_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 21d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_21d_v215_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 21d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_21d_v216_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 21d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_42d_v217_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 42d window."""
    res = _z(_slope_pct(tangibles, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_42d_v218_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 42d window."""
    res = _z(_slope_pct(shareswa, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_42d_v219_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 42d window."""
    res = _z(_slope_pct(bvps, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_42d_v220_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 42d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_42d_v221_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 42d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_42d_v222_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 42d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_63d_v223_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 63d window."""
    res = _z(_slope_pct(tangibles, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_63d_v224_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 63d window."""
    res = _z(_slope_pct(shareswa, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_63d_v225_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 63d window."""
    res = _z(_slope_pct(bvps, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_63d_v226_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 63d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_63d_v227_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 63d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_63d_v228_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 63d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_126d_v229_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 126d window."""
    res = _z(_slope_pct(tangibles, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_126d_v230_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 126d window."""
    res = _z(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_126d_v231_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 126d window."""
    res = _z(_slope_pct(bvps, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_126d_v232_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 126d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_126d_v233_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 126d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_126d_v234_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 126d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_252d_v235_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 252d window."""
    res = _z(_slope_pct(tangibles, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_252d_v236_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 252d window."""
    res = _z(_slope_pct(shareswa, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_252d_v237_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 252d window."""
    res = _z(_slope_pct(bvps, 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_252d_v238_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 252d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_252d_v239_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 252d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_252d_v240_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 252d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 252), 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_504d_v241_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 504d window."""
    res = _z(_slope_pct(tangibles, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_504d_v242_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 504d window."""
    res = _z(_slope_pct(shareswa, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_504d_v243_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 504d window."""
    res = _z(_slope_pct(bvps, 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_504d_v244_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 504d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_504d_v245_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 504d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_504d_v246_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 504d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 504), 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_756d_v247_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 756d window."""
    res = _z(_slope_pct(tangibles, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_756d_v248_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 756d window."""
    res = _z(_slope_pct(shareswa, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_756d_v249_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 756d window."""
    res = _z(_slope_pct(bvps, 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_756d_v250_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 756d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_756d_v251_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 756d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_756d_v252_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 756d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 756), 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_1008d_v253_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 1008d window."""
    res = _z(_slope_pct(tangibles, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_1008d_v254_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 1008d window."""
    res = _z(_slope_pct(shareswa, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_1008d_v255_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 1008d window."""
    res = _z(_slope_pct(bvps, 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_1008d_v256_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 1008d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_1008d_v257_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 1008d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_1008d_v258_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 1008d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 1008), 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_mom_z_1260d_v259_signal(tangibles):
    """Relative momentum strength for Raw level of tangibles over 1260d window."""
    res = _z(_slope_pct(tangibles, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_mom_z_1260d_v260_signal(shareswa):
    """Relative momentum strength for Raw level of shareswa over 1260d window."""
    res = _z(_slope_pct(shareswa, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_mom_z_1260d_v261_signal(bvps):
    """Relative momentum strength for Raw level of bvps over 1260d window."""
    res = _z(_slope_pct(bvps, 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_mom_z_1260d_v262_signal(tangibles, shareswa):
    """Relative momentum strength for Tangible book per share over 1260d window."""
    res = _z(_slope_pct(_ratio(tangibles, shareswa), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_mom_z_1260d_v263_signal(tangibles, bvps, shareswa):
    """Relative momentum strength for Tangible concentration of book value over 1260d window."""
    res = _z(_slope_pct(_ratio(tangibles, bvps * shareswa), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_mom_z_1260d_v264_signal(tangibles, assets):
    """Relative momentum strength for Tangible asset density over 1260d window."""
    res = _z(_slope_pct(_ratio(tangibles, assets), 1260), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_vol_slope_5d_v265_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 5d window."""
    res = _std(_slope_pct(tangibles, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_vol_slope_5d_v266_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 5d window."""
    res = _std(_slope_pct(shareswa, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_vol_slope_5d_v267_signal(bvps):
    """Volatility of momentum for Raw level of bvps over 5d window."""
    res = _std(_slope_pct(bvps, 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_vol_slope_5d_v268_signal(tangibles, shareswa):
    """Volatility of momentum for Tangible book per share over 5d window."""
    res = _std(_slope_pct(_ratio(tangibles, shareswa), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_vol_slope_5d_v269_signal(tangibles, bvps, shareswa):
    """Volatility of momentum for Tangible concentration of book value over 5d window."""
    res = _std(_slope_pct(_ratio(tangibles, bvps * shareswa), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_vol_slope_5d_v270_signal(tangibles, assets):
    """Volatility of momentum for Tangible asset density over 5d window."""
    res = _std(_slope_pct(_ratio(tangibles, assets), 5), 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_vol_slope_10d_v271_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 10d window."""
    res = _std(_slope_pct(tangibles, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_vol_slope_10d_v272_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 10d window."""
    res = _std(_slope_pct(shareswa, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_vol_slope_10d_v273_signal(bvps):
    """Volatility of momentum for Raw level of bvps over 10d window."""
    res = _std(_slope_pct(bvps, 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_vol_slope_10d_v274_signal(tangibles, shareswa):
    """Volatility of momentum for Tangible book per share over 10d window."""
    res = _std(_slope_pct(_ratio(tangibles, shareswa), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_vol_slope_10d_v275_signal(tangibles, bvps, shareswa):
    """Volatility of momentum for Tangible concentration of book value over 10d window."""
    res = _std(_slope_pct(_ratio(tangibles, bvps * shareswa), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_vol_slope_10d_v276_signal(tangibles, assets):
    """Volatility of momentum for Tangible asset density over 10d window."""
    res = _std(_slope_pct(_ratio(tangibles, assets), 10), 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_vol_slope_21d_v277_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 21d window."""
    res = _std(_slope_pct(tangibles, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_vol_slope_21d_v278_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 21d window."""
    res = _std(_slope_pct(shareswa, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_vol_slope_21d_v279_signal(bvps):
    """Volatility of momentum for Raw level of bvps over 21d window."""
    res = _std(_slope_pct(bvps, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_vol_slope_21d_v280_signal(tangibles, shareswa):
    """Volatility of momentum for Tangible book per share over 21d window."""
    res = _std(_slope_pct(_ratio(tangibles, shareswa), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_vol_slope_21d_v281_signal(tangibles, bvps, shareswa):
    """Volatility of momentum for Tangible concentration of book value over 21d window."""
    res = _std(_slope_pct(_ratio(tangibles, bvps * shareswa), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_vol_slope_21d_v282_signal(tangibles, assets):
    """Volatility of momentum for Tangible asset density over 21d window."""
    res = _std(_slope_pct(_ratio(tangibles, assets), 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_vol_slope_42d_v283_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 42d window."""
    res = _std(_slope_pct(tangibles, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_vol_slope_42d_v284_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 42d window."""
    res = _std(_slope_pct(shareswa, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_vol_slope_42d_v285_signal(bvps):
    """Volatility of momentum for Raw level of bvps over 42d window."""
    res = _std(_slope_pct(bvps, 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_vol_slope_42d_v286_signal(tangibles, shareswa):
    """Volatility of momentum for Tangible book per share over 42d window."""
    res = _std(_slope_pct(_ratio(tangibles, shareswa), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_vol_slope_42d_v287_signal(tangibles, bvps, shareswa):
    """Volatility of momentum for Tangible concentration of book value over 42d window."""
    res = _std(_slope_pct(_ratio(tangibles, bvps * shareswa), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_vol_slope_42d_v288_signal(tangibles, assets):
    """Volatility of momentum for Tangible asset density over 42d window."""
    res = _std(_slope_pct(_ratio(tangibles, assets), 42), 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_vol_slope_63d_v289_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 63d window."""
    res = _std(_slope_pct(tangibles, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_vol_slope_63d_v290_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 63d window."""
    res = _std(_slope_pct(shareswa, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_vol_slope_63d_v291_signal(bvps):
    """Volatility of momentum for Raw level of bvps over 63d window."""
    res = _std(_slope_pct(bvps, 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_vol_slope_63d_v292_signal(tangibles, shareswa):
    """Volatility of momentum for Tangible book per share over 63d window."""
    res = _std(_slope_pct(_ratio(tangibles, shareswa), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_vol_slope_63d_v293_signal(tangibles, bvps, shareswa):
    """Volatility of momentum for Tangible concentration of book value over 63d window."""
    res = _std(_slope_pct(_ratio(tangibles, bvps * shareswa), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_vol_slope_63d_v294_signal(tangibles, assets):
    """Volatility of momentum for Tangible asset density over 63d window."""
    res = _std(_slope_pct(_ratio(tangibles, assets), 63), 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tangibles_vol_slope_126d_v295_signal(tangibles):
    """Volatility of momentum for Raw level of tangibles over 126d window."""
    res = _std(_slope_pct(tangibles, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_shareswa_vol_slope_126d_v296_signal(shareswa):
    """Volatility of momentum for Raw level of shareswa over 126d window."""
    res = _std(_slope_pct(shareswa, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_bvps_vol_slope_126d_v297_signal(bvps):
    """Volatility of momentum for Raw level of bvps over 126d window."""
    res = _std(_slope_pct(bvps, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbvps_vol_slope_126d_v298_signal(tangibles, shareswa):
    """Volatility of momentum for Tangible book per share over 126d window."""
    res = _std(_slope_pct(_ratio(tangibles, shareswa), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_tbv_to_total_bv_vol_slope_126d_v299_signal(tangibles, bvps, shareswa):
    """Volatility of momentum for Tangible concentration of book value over 126d window."""
    res = _std(_slope_pct(_ratio(tangibles, bvps * shareswa), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f02_tbvps_growth_growth_capacity_vol_slope_126d_v300_signal(tangibles, assets):
    """Volatility of momentum for Tangible asset density over 126d window."""
    res = _std(_slope_pct(_ratio(tangibles, assets), 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)


# ===== Feature Registry =====
REGISTRY = {
    "f02_tbvps_growth_tangibles_slope_diff_norm_42d_v151_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_42d_v151_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_42d_v152_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_42d_v152_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_42d_v153_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_42d_v153_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_42d_v154_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_42d_v154_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_42d_v155_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_42d_v155_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_42d_v156_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_42d_v156_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_63d_v157_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_63d_v157_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_63d_v158_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_63d_v158_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_63d_v159_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_63d_v159_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_63d_v160_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_63d_v160_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_63d_v161_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_63d_v161_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_63d_v162_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_63d_v162_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_126d_v163_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_126d_v163_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_126d_v164_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_126d_v164_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_126d_v165_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_126d_v165_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_126d_v166_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_126d_v166_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_126d_v167_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_126d_v167_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_126d_v168_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_126d_v168_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_252d_v169_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_252d_v169_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_252d_v170_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_252d_v170_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_252d_v171_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_252d_v171_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_252d_v172_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_252d_v172_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_252d_v173_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_252d_v173_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_252d_v174_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_252d_v174_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_504d_v175_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_504d_v175_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_504d_v176_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_504d_v176_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_504d_v177_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_504d_v177_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_504d_v178_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_504d_v178_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_504d_v179_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_504d_v179_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_504d_v180_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_504d_v180_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_756d_v181_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_756d_v181_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_756d_v182_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_756d_v182_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_756d_v183_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_756d_v183_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_756d_v184_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_756d_v184_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_756d_v185_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_756d_v185_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_756d_v186_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_756d_v186_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_1008d_v187_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_1008d_v187_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_1008d_v188_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_1008d_v188_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_1008d_v189_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_1008d_v189_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_1008d_v190_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_1008d_v190_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_1008d_v191_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_1008d_v191_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_1008d_v192_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_1008d_v192_signal},
    "f02_tbvps_growth_tangibles_slope_diff_norm_1260d_v193_signal": {"func": f02_tbvps_growth_tangibles_slope_diff_norm_1260d_v193_signal},
    "f02_tbvps_growth_shareswa_slope_diff_norm_1260d_v194_signal": {"func": f02_tbvps_growth_shareswa_slope_diff_norm_1260d_v194_signal},
    "f02_tbvps_growth_bvps_slope_diff_norm_1260d_v195_signal": {"func": f02_tbvps_growth_bvps_slope_diff_norm_1260d_v195_signal},
    "f02_tbvps_growth_tbvps_slope_diff_norm_1260d_v196_signal": {"func": f02_tbvps_growth_tbvps_slope_diff_norm_1260d_v196_signal},
    "f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_1260d_v197_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_slope_diff_norm_1260d_v197_signal},
    "f02_tbvps_growth_growth_capacity_slope_diff_norm_1260d_v198_signal": {"func": f02_tbvps_growth_growth_capacity_slope_diff_norm_1260d_v198_signal},
    "f02_tbvps_growth_tangibles_mom_z_5d_v199_signal": {"func": f02_tbvps_growth_tangibles_mom_z_5d_v199_signal},
    "f02_tbvps_growth_shareswa_mom_z_5d_v200_signal": {"func": f02_tbvps_growth_shareswa_mom_z_5d_v200_signal},
    "f02_tbvps_growth_bvps_mom_z_5d_v201_signal": {"func": f02_tbvps_growth_bvps_mom_z_5d_v201_signal},
    "f02_tbvps_growth_tbvps_mom_z_5d_v202_signal": {"func": f02_tbvps_growth_tbvps_mom_z_5d_v202_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_5d_v203_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_5d_v203_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_5d_v204_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_5d_v204_signal},
    "f02_tbvps_growth_tangibles_mom_z_10d_v205_signal": {"func": f02_tbvps_growth_tangibles_mom_z_10d_v205_signal},
    "f02_tbvps_growth_shareswa_mom_z_10d_v206_signal": {"func": f02_tbvps_growth_shareswa_mom_z_10d_v206_signal},
    "f02_tbvps_growth_bvps_mom_z_10d_v207_signal": {"func": f02_tbvps_growth_bvps_mom_z_10d_v207_signal},
    "f02_tbvps_growth_tbvps_mom_z_10d_v208_signal": {"func": f02_tbvps_growth_tbvps_mom_z_10d_v208_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_10d_v209_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_10d_v209_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_10d_v210_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_10d_v210_signal},
    "f02_tbvps_growth_tangibles_mom_z_21d_v211_signal": {"func": f02_tbvps_growth_tangibles_mom_z_21d_v211_signal},
    "f02_tbvps_growth_shareswa_mom_z_21d_v212_signal": {"func": f02_tbvps_growth_shareswa_mom_z_21d_v212_signal},
    "f02_tbvps_growth_bvps_mom_z_21d_v213_signal": {"func": f02_tbvps_growth_bvps_mom_z_21d_v213_signal},
    "f02_tbvps_growth_tbvps_mom_z_21d_v214_signal": {"func": f02_tbvps_growth_tbvps_mom_z_21d_v214_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_21d_v215_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_21d_v215_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_21d_v216_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_21d_v216_signal},
    "f02_tbvps_growth_tangibles_mom_z_42d_v217_signal": {"func": f02_tbvps_growth_tangibles_mom_z_42d_v217_signal},
    "f02_tbvps_growth_shareswa_mom_z_42d_v218_signal": {"func": f02_tbvps_growth_shareswa_mom_z_42d_v218_signal},
    "f02_tbvps_growth_bvps_mom_z_42d_v219_signal": {"func": f02_tbvps_growth_bvps_mom_z_42d_v219_signal},
    "f02_tbvps_growth_tbvps_mom_z_42d_v220_signal": {"func": f02_tbvps_growth_tbvps_mom_z_42d_v220_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_42d_v221_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_42d_v221_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_42d_v222_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_42d_v222_signal},
    "f02_tbvps_growth_tangibles_mom_z_63d_v223_signal": {"func": f02_tbvps_growth_tangibles_mom_z_63d_v223_signal},
    "f02_tbvps_growth_shareswa_mom_z_63d_v224_signal": {"func": f02_tbvps_growth_shareswa_mom_z_63d_v224_signal},
    "f02_tbvps_growth_bvps_mom_z_63d_v225_signal": {"func": f02_tbvps_growth_bvps_mom_z_63d_v225_signal},
    "f02_tbvps_growth_tbvps_mom_z_63d_v226_signal": {"func": f02_tbvps_growth_tbvps_mom_z_63d_v226_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_63d_v227_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_63d_v227_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_63d_v228_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_63d_v228_signal},
    "f02_tbvps_growth_tangibles_mom_z_126d_v229_signal": {"func": f02_tbvps_growth_tangibles_mom_z_126d_v229_signal},
    "f02_tbvps_growth_shareswa_mom_z_126d_v230_signal": {"func": f02_tbvps_growth_shareswa_mom_z_126d_v230_signal},
    "f02_tbvps_growth_bvps_mom_z_126d_v231_signal": {"func": f02_tbvps_growth_bvps_mom_z_126d_v231_signal},
    "f02_tbvps_growth_tbvps_mom_z_126d_v232_signal": {"func": f02_tbvps_growth_tbvps_mom_z_126d_v232_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_126d_v233_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_126d_v233_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_126d_v234_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_126d_v234_signal},
    "f02_tbvps_growth_tangibles_mom_z_252d_v235_signal": {"func": f02_tbvps_growth_tangibles_mom_z_252d_v235_signal},
    "f02_tbvps_growth_shareswa_mom_z_252d_v236_signal": {"func": f02_tbvps_growth_shareswa_mom_z_252d_v236_signal},
    "f02_tbvps_growth_bvps_mom_z_252d_v237_signal": {"func": f02_tbvps_growth_bvps_mom_z_252d_v237_signal},
    "f02_tbvps_growth_tbvps_mom_z_252d_v238_signal": {"func": f02_tbvps_growth_tbvps_mom_z_252d_v238_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_252d_v239_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_252d_v239_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_252d_v240_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_252d_v240_signal},
    "f02_tbvps_growth_tangibles_mom_z_504d_v241_signal": {"func": f02_tbvps_growth_tangibles_mom_z_504d_v241_signal},
    "f02_tbvps_growth_shareswa_mom_z_504d_v242_signal": {"func": f02_tbvps_growth_shareswa_mom_z_504d_v242_signal},
    "f02_tbvps_growth_bvps_mom_z_504d_v243_signal": {"func": f02_tbvps_growth_bvps_mom_z_504d_v243_signal},
    "f02_tbvps_growth_tbvps_mom_z_504d_v244_signal": {"func": f02_tbvps_growth_tbvps_mom_z_504d_v244_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_504d_v245_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_504d_v245_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_504d_v246_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_504d_v246_signal},
    "f02_tbvps_growth_tangibles_mom_z_756d_v247_signal": {"func": f02_tbvps_growth_tangibles_mom_z_756d_v247_signal},
    "f02_tbvps_growth_shareswa_mom_z_756d_v248_signal": {"func": f02_tbvps_growth_shareswa_mom_z_756d_v248_signal},
    "f02_tbvps_growth_bvps_mom_z_756d_v249_signal": {"func": f02_tbvps_growth_bvps_mom_z_756d_v249_signal},
    "f02_tbvps_growth_tbvps_mom_z_756d_v250_signal": {"func": f02_tbvps_growth_tbvps_mom_z_756d_v250_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_756d_v251_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_756d_v251_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_756d_v252_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_756d_v252_signal},
    "f02_tbvps_growth_tangibles_mom_z_1008d_v253_signal": {"func": f02_tbvps_growth_tangibles_mom_z_1008d_v253_signal},
    "f02_tbvps_growth_shareswa_mom_z_1008d_v254_signal": {"func": f02_tbvps_growth_shareswa_mom_z_1008d_v254_signal},
    "f02_tbvps_growth_bvps_mom_z_1008d_v255_signal": {"func": f02_tbvps_growth_bvps_mom_z_1008d_v255_signal},
    "f02_tbvps_growth_tbvps_mom_z_1008d_v256_signal": {"func": f02_tbvps_growth_tbvps_mom_z_1008d_v256_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_1008d_v257_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_1008d_v257_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_1008d_v258_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_1008d_v258_signal},
    "f02_tbvps_growth_tangibles_mom_z_1260d_v259_signal": {"func": f02_tbvps_growth_tangibles_mom_z_1260d_v259_signal},
    "f02_tbvps_growth_shareswa_mom_z_1260d_v260_signal": {"func": f02_tbvps_growth_shareswa_mom_z_1260d_v260_signal},
    "f02_tbvps_growth_bvps_mom_z_1260d_v261_signal": {"func": f02_tbvps_growth_bvps_mom_z_1260d_v261_signal},
    "f02_tbvps_growth_tbvps_mom_z_1260d_v262_signal": {"func": f02_tbvps_growth_tbvps_mom_z_1260d_v262_signal},
    "f02_tbvps_growth_tbv_to_total_bv_mom_z_1260d_v263_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_mom_z_1260d_v263_signal},
    "f02_tbvps_growth_growth_capacity_mom_z_1260d_v264_signal": {"func": f02_tbvps_growth_growth_capacity_mom_z_1260d_v264_signal},
    "f02_tbvps_growth_tangibles_vol_slope_5d_v265_signal": {"func": f02_tbvps_growth_tangibles_vol_slope_5d_v265_signal},
    "f02_tbvps_growth_shareswa_vol_slope_5d_v266_signal": {"func": f02_tbvps_growth_shareswa_vol_slope_5d_v266_signal},
    "f02_tbvps_growth_bvps_vol_slope_5d_v267_signal": {"func": f02_tbvps_growth_bvps_vol_slope_5d_v267_signal},
    "f02_tbvps_growth_tbvps_vol_slope_5d_v268_signal": {"func": f02_tbvps_growth_tbvps_vol_slope_5d_v268_signal},
    "f02_tbvps_growth_tbv_to_total_bv_vol_slope_5d_v269_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_vol_slope_5d_v269_signal},
    "f02_tbvps_growth_growth_capacity_vol_slope_5d_v270_signal": {"func": f02_tbvps_growth_growth_capacity_vol_slope_5d_v270_signal},
    "f02_tbvps_growth_tangibles_vol_slope_10d_v271_signal": {"func": f02_tbvps_growth_tangibles_vol_slope_10d_v271_signal},
    "f02_tbvps_growth_shareswa_vol_slope_10d_v272_signal": {"func": f02_tbvps_growth_shareswa_vol_slope_10d_v272_signal},
    "f02_tbvps_growth_bvps_vol_slope_10d_v273_signal": {"func": f02_tbvps_growth_bvps_vol_slope_10d_v273_signal},
    "f02_tbvps_growth_tbvps_vol_slope_10d_v274_signal": {"func": f02_tbvps_growth_tbvps_vol_slope_10d_v274_signal},
    "f02_tbvps_growth_tbv_to_total_bv_vol_slope_10d_v275_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_vol_slope_10d_v275_signal},
    "f02_tbvps_growth_growth_capacity_vol_slope_10d_v276_signal": {"func": f02_tbvps_growth_growth_capacity_vol_slope_10d_v276_signal},
    "f02_tbvps_growth_tangibles_vol_slope_21d_v277_signal": {"func": f02_tbvps_growth_tangibles_vol_slope_21d_v277_signal},
    "f02_tbvps_growth_shareswa_vol_slope_21d_v278_signal": {"func": f02_tbvps_growth_shareswa_vol_slope_21d_v278_signal},
    "f02_tbvps_growth_bvps_vol_slope_21d_v279_signal": {"func": f02_tbvps_growth_bvps_vol_slope_21d_v279_signal},
    "f02_tbvps_growth_tbvps_vol_slope_21d_v280_signal": {"func": f02_tbvps_growth_tbvps_vol_slope_21d_v280_signal},
    "f02_tbvps_growth_tbv_to_total_bv_vol_slope_21d_v281_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_vol_slope_21d_v281_signal},
    "f02_tbvps_growth_growth_capacity_vol_slope_21d_v282_signal": {"func": f02_tbvps_growth_growth_capacity_vol_slope_21d_v282_signal},
    "f02_tbvps_growth_tangibles_vol_slope_42d_v283_signal": {"func": f02_tbvps_growth_tangibles_vol_slope_42d_v283_signal},
    "f02_tbvps_growth_shareswa_vol_slope_42d_v284_signal": {"func": f02_tbvps_growth_shareswa_vol_slope_42d_v284_signal},
    "f02_tbvps_growth_bvps_vol_slope_42d_v285_signal": {"func": f02_tbvps_growth_bvps_vol_slope_42d_v285_signal},
    "f02_tbvps_growth_tbvps_vol_slope_42d_v286_signal": {"func": f02_tbvps_growth_tbvps_vol_slope_42d_v286_signal},
    "f02_tbvps_growth_tbv_to_total_bv_vol_slope_42d_v287_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_vol_slope_42d_v287_signal},
    "f02_tbvps_growth_growth_capacity_vol_slope_42d_v288_signal": {"func": f02_tbvps_growth_growth_capacity_vol_slope_42d_v288_signal},
    "f02_tbvps_growth_tangibles_vol_slope_63d_v289_signal": {"func": f02_tbvps_growth_tangibles_vol_slope_63d_v289_signal},
    "f02_tbvps_growth_shareswa_vol_slope_63d_v290_signal": {"func": f02_tbvps_growth_shareswa_vol_slope_63d_v290_signal},
    "f02_tbvps_growth_bvps_vol_slope_63d_v291_signal": {"func": f02_tbvps_growth_bvps_vol_slope_63d_v291_signal},
    "f02_tbvps_growth_tbvps_vol_slope_63d_v292_signal": {"func": f02_tbvps_growth_tbvps_vol_slope_63d_v292_signal},
    "f02_tbvps_growth_tbv_to_total_bv_vol_slope_63d_v293_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_vol_slope_63d_v293_signal},
    "f02_tbvps_growth_growth_capacity_vol_slope_63d_v294_signal": {"func": f02_tbvps_growth_growth_capacity_vol_slope_63d_v294_signal},
    "f02_tbvps_growth_tangibles_vol_slope_126d_v295_signal": {"func": f02_tbvps_growth_tangibles_vol_slope_126d_v295_signal},
    "f02_tbvps_growth_shareswa_vol_slope_126d_v296_signal": {"func": f02_tbvps_growth_shareswa_vol_slope_126d_v296_signal},
    "f02_tbvps_growth_bvps_vol_slope_126d_v297_signal": {"func": f02_tbvps_growth_bvps_vol_slope_126d_v297_signal},
    "f02_tbvps_growth_tbvps_vol_slope_126d_v298_signal": {"func": f02_tbvps_growth_tbvps_vol_slope_126d_v298_signal},
    "f02_tbvps_growth_tbv_to_total_bv_vol_slope_126d_v299_signal": {"func": f02_tbvps_growth_tbv_to_total_bv_vol_slope_126d_v299_signal},
    "f02_tbvps_growth_growth_capacity_vol_slope_126d_v300_signal": {"func": f02_tbvps_growth_growth_capacity_vol_slope_126d_v300_signal},
}

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "deferredrev": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "rnd": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 02...")
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
