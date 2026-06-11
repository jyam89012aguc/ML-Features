import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f31cpe_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f31cpe_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f31cpe_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f31cpe_diff(a, b):
    return a - b


# 5d curvature of 21d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_21d_curv_v001_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_21d_curv_v002_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_21d_curv_v003_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_21d_curv_v004_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d level of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevel_21d_curv_v005_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d levelrel of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_63d_curv_v006_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d levelrel of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_63d_curv_v007_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d levelrel of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_63d_curv_v008_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d levelrel of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_63d_curv_v009_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d levelrel of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflevelrel_63d_curv_v010_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_126d_curv_v011_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_126d_curv_v012_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_126d_curv_v013_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_126d_curv_v014_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d mean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmean_126d_curv_v015_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d z of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_252d_curv_v016_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d z of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_252d_curv_v017_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d z of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_252d_curv_v018_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d z of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_252d_curv_v019_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d z of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffz_252d_curv_v020_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d robz of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_504d_curv_v021_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d robz of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_504d_curv_v022_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d robz of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_504d_curv_v023_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d robz of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_504d_curv_v024_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d robz of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrobz_504d_curv_v025_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_21d_curv_v026_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_21d_curv_v027_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_21d_curv_v028_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_21d_curv_v029_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d max of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmax_21d_curv_v030_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_63d_curv_v031_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _min(M, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_63d_curv_v032_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _min(M, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_63d_curv_v033_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _min(M, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_63d_curv_v034_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _min(M, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d min of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffmin_63d_curv_v035_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _min(M, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d rng of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_126d_curv_v036_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d rng of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_126d_curv_v037_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d rng of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_126d_curv_v038_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d rng of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_126d_curv_v039_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d rng of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffrng_126d_curv_v040_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d pos of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_252d_curv_v041_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d pos of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_252d_curv_v042_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d pos of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_252d_curv_v043_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d pos of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_252d_curv_v044_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d pos of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpos_252d_curv_v045_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d dd of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_504d_curv_v046_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d dd of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_504d_curv_v047_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d dd of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_504d_curv_v048_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d dd of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_504d_curv_v049_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d dd of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdd_504d_curv_v050_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d up of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_21d_curv_v051_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d up of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_21d_curv_v052_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d up of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_21d_curv_v053_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d up of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_21d_curv_v054_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d up of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffup_21d_curv_v055_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_63d_curv_v056_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_63d_curv_v057_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_63d_curv_v058_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_63d_curv_v059_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffstd_63d_curv_v060_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_126d_curv_v061_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_126d_curv_v062_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_126d_curv_v063_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_126d_curv_v064_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d skew of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffskew_126d_curv_v065_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d kurt of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_252d_curv_v066_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d kurt of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_252d_curv_v067_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d kurt of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_252d_curv_v068_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d kurt of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_252d_curv_v069_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d kurt of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffkurt_252d_curv_v070_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d hits of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_504d_curv_v071_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d hits of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_504d_curv_v072_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d hits of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_504d_curv_v073_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d hits of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_504d_curv_v074_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d hits of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhits_504d_curv_v075_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d signcum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_21d_curv_v076_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d signcum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_21d_curv_v077_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d signcum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_21d_curv_v078_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d signcum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_21d_curv_v079_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d signcum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffsigncum_21d_curv_v080_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d cum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_63d_curv_v081_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d cum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_63d_curv_v082_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d cum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_63d_curv_v083_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d cum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_63d_curv_v084_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d cum of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcum_63d_curv_v085_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d emafast of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_126d_curv_v086_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d emafast of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_126d_curv_v087_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d emafast of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_126d_curv_v088_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d emafast of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_126d_curv_v089_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d emafast of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemafast_126d_curv_v090_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d emaslow of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_252d_curv_v091_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d emaslow of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_252d_curv_v092_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d emaslow of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_252d_curv_v093_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d emaslow of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_252d_curv_v094_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d emaslow of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffemaslow_252d_curv_v095_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d zabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_504d_curv_v096_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504).abs()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d zabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_504d_curv_v097_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504).abs()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d zabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_504d_curv_v098_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504).abs()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d zabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_504d_curv_v099_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504).abs()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d zabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffzabs_504d_curv_v100_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504).abs()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d posmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_21d_curv_v101_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d posmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_21d_curv_v102_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d posmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_21d_curv_v103_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d posmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_21d_curv_v104_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d posmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffposmean_21d_curv_v105_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d negmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_63d_curv_v106_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d negmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_63d_curv_v107_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d negmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_63d_curv_v108_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d negmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_63d_curv_v109_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d negmean of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffnegmean_63d_curv_v110_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d cvar of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_126d_curv_v111_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d cvar of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_126d_curv_v112_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d cvar of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_126d_curv_v113_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d cvar of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_126d_curv_v114_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d cvar of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcvar_126d_curv_v115_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d logabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_252d_curv_v116_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d logabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_252d_curv_v117_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d logabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_252d_curv_v118_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d logabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_252d_curv_v119_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d logabs of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefflogabs_252d_curv_v120_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d diff of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_504d_curv_v121_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff(periods=504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d diff of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_504d_curv_v122_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff(periods=504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d diff of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_504d_curv_v123_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff(periods=504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d diff of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_504d_curv_v124_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff(periods=504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d diff of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffdiff_504d_curv_v125_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff(periods=504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d pctchg of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_21d_curv_v126_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.pct_change(periods=21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d pctchg of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_21d_curv_v127_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.pct_change(periods=21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d pctchg of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_21d_curv_v128_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.pct_change(periods=21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d pctchg of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_21d_curv_v129_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.pct_change(periods=21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d pctchg of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffpctchg_21d_curv_v130_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.pct_change(periods=21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d xover of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_63d_curv_v131_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d xover of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_63d_curv_v132_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d xover of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_63d_curv_v133_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d xover of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_63d_curv_v134_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d xover of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffxover_63d_curv_v135_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M - _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d trend of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_126d_curv_v136_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d trend of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_126d_curv_v137_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d trend of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_126d_curv_v138_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d trend of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_126d_curv_v139_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d trend of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpefftrend_126d_curv_v140_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d highmask of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_252d_curv_v141_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d highmask of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_252d_curv_v142_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d highmask of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_252d_curv_v143_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d highmask of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_252d_curv_v144_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d highmask of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffhighmask_252d_curv_v145_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d compositez of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_504d_curv_v146_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d compositez of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_504d_curv_v147_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d compositez of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_504d_curv_v148_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d compositez of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_504d_curv_v149_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d compositez of capex efficiency (capex/ppne)
def f31cpe_f31_semi_capex_ppe_efficiency_cpeffcompositez_504d_curv_v150_signal(capex, ppne, revenue, closeadj):
    M = _f31cpe_ratio(capex, ppne)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


