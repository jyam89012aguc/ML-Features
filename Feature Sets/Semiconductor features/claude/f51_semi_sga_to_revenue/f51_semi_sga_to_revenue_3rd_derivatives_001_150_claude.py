import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)

def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives =====
def _f51_sga_rev(s, rev):
    return s / rev.replace(0, np.nan)


def _f51_sga_rev_log(s, rev):
    return np.log(s.replace(0, np.nan).abs() / rev.replace(0, np.nan).abs())


# 5d curvature of level of SG&A intensity (sga/rev) (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_21d_curv_v001_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of SG&A intensity (sga/rev) (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_21d_curv_v002_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of SG&A intensity (sga/rev) (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_21d_curv_v003_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of SG&A intensity (sga/rev) (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_21d_curv_v004_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of SG&A intensity (sga/rev) (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_21d_curv_v005_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of SG&A intensity (sga/rev) (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_63d_curv_v006_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of SG&A intensity (sga/rev) (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_63d_curv_v007_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of SG&A intensity (sga/rev) (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_63d_curv_v008_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of SG&A intensity (sga/rev) (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_63d_curv_v009_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of SG&A intensity (sga/rev) (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgar_level_63d_curv_v010_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_21d_curv_v011_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_21d_curv_v012_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_21d_curv_v013_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_21d_curv_v014_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_21d_curv_v015_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_63d_curv_v016_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_63d_curv_v017_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_63d_curv_v018_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_63d_curv_v019_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_63d_curv_v020_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_126d_curv_v021_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_126d_curv_v022_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_126d_curv_v023_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_126d_curv_v024_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_z_126d_curv_v025_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_rng_63d_curv_v026_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_rng_63d_curv_v027_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_rng_63d_curv_v028_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_rng_63d_curv_v029_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_rng_63d_curv_v030_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of SG&A intensity (sga/rev) in rolling range
def f51sga_semi_sga_to_revenue_sgar_pos_63d_curv_v031_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of SG&A intensity (sga/rev) in rolling range
def f51sga_semi_sga_to_revenue_sgar_pos_63d_curv_v032_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of SG&A intensity (sga/rev) in rolling range
def f51sga_semi_sga_to_revenue_sgar_pos_63d_curv_v033_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of SG&A intensity (sga/rev) in rolling range
def f51sga_semi_sga_to_revenue_sgar_pos_63d_curv_v034_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of SG&A intensity (sga/rev) in rolling range
def f51sga_semi_sga_to_revenue_sgar_pos_63d_curv_v035_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of SG&A intensity (sga/rev) from peak
def f51sga_semi_sga_to_revenue_sgar_dd_63d_curv_v036_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of SG&A intensity (sga/rev) from peak
def f51sga_semi_sga_to_revenue_sgar_dd_63d_curv_v037_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of SG&A intensity (sga/rev) from peak
def f51sga_semi_sga_to_revenue_sgar_dd_63d_curv_v038_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of SG&A intensity (sga/rev) from peak
def f51sga_semi_sga_to_revenue_sgar_dd_63d_curv_v039_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of SG&A intensity (sga/rev) from peak
def f51sga_semi_sga_to_revenue_sgar_dd_63d_curv_v040_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of SG&A intensity (sga/rev) above trough
def f51sga_semi_sga_to_revenue_sgar_up_63d_curv_v041_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of SG&A intensity (sga/rev) above trough
def f51sga_semi_sga_to_revenue_sgar_up_63d_curv_v042_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of SG&A intensity (sga/rev) above trough
def f51sga_semi_sga_to_revenue_sgar_up_63d_curv_v043_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of SG&A intensity (sga/rev) above trough
def f51sga_semi_sga_to_revenue_sgar_up_63d_curv_v044_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of SG&A intensity (sga/rev) above trough
def f51sga_semi_sga_to_revenue_sgar_up_63d_curv_v045_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_std_63d_curv_v046_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_std_63d_curv_v047_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_std_63d_curv_v048_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_std_63d_curv_v049_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_std_63d_curv_v050_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_ema_63d_curv_v051_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_ema_63d_curv_v052_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_ema_63d_curv_v053_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_ema_63d_curv_v054_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_ema_63d_curv_v055_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive SG&A intensity (sga/rev) changes
def f51sga_semi_sga_to_revenue_sgar_hit_63d_curv_v056_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive SG&A intensity (sga/rev) changes
def f51sga_semi_sga_to_revenue_sgar_hit_63d_curv_v057_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive SG&A intensity (sga/rev) changes
def f51sga_semi_sga_to_revenue_sgar_hit_63d_curv_v058_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive SG&A intensity (sga/rev) changes
def f51sga_semi_sga_to_revenue_sgar_hit_63d_curv_v059_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive SG&A intensity (sga/rev) changes
def f51sga_semi_sga_to_revenue_sgar_hit_63d_curv_v060_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_cumsign_63d_curv_v061_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_cumsign_63d_curv_v062_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_cumsign_63d_curv_v063_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_cumsign_63d_curv_v064_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_cumsign_63d_curv_v065_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_robustz_63d_curv_v066_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_robustz_63d_curv_v067_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_robustz_63d_curv_v068_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_robustz_63d_curv_v069_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_robustz_63d_curv_v070_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_skew_63d_curv_v071_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_skew_63d_curv_v072_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_skew_63d_curv_v073_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_skew_63d_curv_v074_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of SG&A intensity (sga/rev)
def f51sga_semi_sga_to_revenue_sgar_skew_63d_curv_v075_signal(sga, revenue, closeadj):
    m = _f51_sga_rev(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of log SG&A intensity (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_21d_curv_v076_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of log SG&A intensity (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_21d_curv_v077_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of log SG&A intensity (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_21d_curv_v078_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of log SG&A intensity (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_21d_curv_v079_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of log SG&A intensity (21d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_21d_curv_v080_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of level of log SG&A intensity (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_63d_curv_v081_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of level of log SG&A intensity (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_63d_curv_v082_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of level of log SG&A intensity (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_63d_curv_v083_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of level of log SG&A intensity (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_63d_curv_v084_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of level of log SG&A intensity (63d mean-centered)
def f51sga_semi_sga_to_revenue_sgarlog_level_63d_curv_v085_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m - _mean(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_21d_curv_v086_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_21d_curv_v087_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_21d_curv_v088_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_21d_curv_v089_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_21d_curv_v090_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_63d_curv_v091_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_63d_curv_v092_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_63d_curv_v093_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_63d_curv_v094_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_63d_curv_v095_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_126d_curv_v096_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_126d_curv_v097_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_126d_curv_v098_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_126d_curv_v099_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_z_126d_curv_v100_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _z(m, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d range of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_rng_63d_curv_v101_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d range of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_rng_63d_curv_v102_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d range of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_rng_63d_curv_v103_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d range of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_rng_63d_curv_v104_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d range of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_rng_63d_curv_v105_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _max(m, 63) - _min(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d position of log SG&A intensity in rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_63d_curv_v106_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d position of log SG&A intensity in rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_63d_curv_v107_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d position of log SG&A intensity in rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_63d_curv_v108_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d position of log SG&A intensity in rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_63d_curv_v109_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d position of log SG&A intensity in rolling range
def f51sga_semi_sga_to_revenue_sgarlog_pos_63d_curv_v110_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    lo = _min(m, 63)
    hi = _max(m, 63)
    base = (m - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d drawdown of log SG&A intensity from peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_63d_curv_v111_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d drawdown of log SG&A intensity from peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_63d_curv_v112_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d drawdown of log SG&A intensity from peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_63d_curv_v113_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d drawdown of log SG&A intensity from peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_63d_curv_v114_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d drawdown of log SG&A intensity from peak
def f51sga_semi_sga_to_revenue_sgarlog_dd_63d_curv_v115_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    peak = _max(m, 63)
    base = m - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d run-up of log SG&A intensity above trough
def f51sga_semi_sga_to_revenue_sgarlog_up_63d_curv_v116_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d run-up of log SG&A intensity above trough
def f51sga_semi_sga_to_revenue_sgarlog_up_63d_curv_v117_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d run-up of log SG&A intensity above trough
def f51sga_semi_sga_to_revenue_sgarlog_up_63d_curv_v118_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d run-up of log SG&A intensity above trough
def f51sga_semi_sga_to_revenue_sgarlog_up_63d_curv_v119_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d run-up of log SG&A intensity above trough
def f51sga_semi_sga_to_revenue_sgarlog_up_63d_curv_v120_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    trough = _min(m, 63)
    base = m - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_std_63d_curv_v121_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_std_63d_curv_v122_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_std_63d_curv_v123_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_std_63d_curv_v124_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_std_63d_curv_v125_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = _std(m, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d EMA-crossover of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_ema_63d_curv_v126_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d EMA-crossover of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_ema_63d_curv_v127_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d EMA-crossover of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_ema_63d_curv_v128_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d EMA-crossover of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_ema_63d_curv_v129_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d EMA-crossover of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_ema_63d_curv_v130_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.ewm(span=max(2, 63//4), adjust=False).mean() - m.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_63d_curv_v131_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_63d_curv_v132_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_63d_curv_v133_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_63d_curv_v134_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d hit-ratio of positive log SG&A intensity changes
def f51sga_semi_sga_to_revenue_sgarlog_hit_63d_curv_v135_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = (m.diff() > 0).astype(float).rolling(63, min_periods=32).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_63d_curv_v136_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_63d_curv_v137_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_63d_curv_v138_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_63d_curv_v139_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d signed cumulative changes of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_cumsign_63d_curv_v140_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = pd.Series(np.sign(m.diff()), index=m.index).rolling(63, min_periods=32).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d robust z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_robustz_63d_curv_v141_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d robust z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_robustz_63d_curv_v142_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d robust z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_robustz_63d_curv_v143_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d robust z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_robustz_63d_curv_v144_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d robust z-score of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_robustz_63d_curv_v145_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    med = m.rolling(63, min_periods=32).median()
    mad = (m - med).abs().rolling(63, min_periods=32).median()
    base = (m - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_63d_curv_v146_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_63d_curv_v147_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_63d_curv_v148_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_63d_curv_v149_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d skew of log SG&A intensity
def f51sga_semi_sga_to_revenue_sgarlog_skew_63d_curv_v150_signal(sga, revenue, closeadj):
    m = _f51_sga_rev_log(sga, revenue)
    base = m.rolling(63, min_periods=32).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)
