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
def _f39dso_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f39dso_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f39dso_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f39dso_diff(a, b):
    return a - b


# 5d curvature of 21d level of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevel_21d_curv_v001_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d level of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevel_21d_curv_v002_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d level of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevel_21d_curv_v003_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d level of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevel_21d_curv_v004_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d level of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevel_21d_curv_v005_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d levelrel of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevelrel_63d_curv_v006_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d levelrel of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevelrel_63d_curv_v007_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d levelrel of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevelrel_63d_curv_v008_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d levelrel of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevelrel_63d_curv_v009_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d levelrel of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsolevelrel_63d_curv_v010_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d mean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomean_126d_curv_v011_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomean_126d_curv_v012_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d mean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomean_126d_curv_v013_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d mean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomean_126d_curv_v014_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d mean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomean_126d_curv_v015_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d z of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoz_252d_curv_v016_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d z of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoz_252d_curv_v017_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d z of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoz_252d_curv_v018_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d z of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoz_252d_curv_v019_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d z of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoz_252d_curv_v020_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d robz of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorobz_504d_curv_v021_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d robz of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorobz_504d_curv_v022_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d robz of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorobz_504d_curv_v023_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d robz of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorobz_504d_curv_v024_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d robz of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorobz_504d_curv_v025_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d max of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomax_21d_curv_v026_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d max of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomax_21d_curv_v027_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d max of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomax_21d_curv_v028_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d max of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomax_21d_curv_v029_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d max of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomax_21d_curv_v030_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d min of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomin_63d_curv_v031_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _min(M, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d min of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomin_63d_curv_v032_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _min(M, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d min of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomin_63d_curv_v033_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _min(M, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d min of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomin_63d_curv_v034_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _min(M, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d min of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsomin_63d_curv_v035_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _min(M, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d rng of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorng_126d_curv_v036_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d rng of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorng_126d_curv_v037_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d rng of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorng_126d_curv_v038_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d rng of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorng_126d_curv_v039_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d rng of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsorng_126d_curv_v040_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d pos of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopos_252d_curv_v041_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d pos of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopos_252d_curv_v042_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d pos of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopos_252d_curv_v043_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d pos of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopos_252d_curv_v044_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d pos of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopos_252d_curv_v045_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d dd of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodd_504d_curv_v046_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d dd of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodd_504d_curv_v047_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d dd of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodd_504d_curv_v048_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d dd of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodd_504d_curv_v049_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d dd of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodd_504d_curv_v050_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d up of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoup_21d_curv_v051_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d up of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoup_21d_curv_v052_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d up of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoup_21d_curv_v053_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d up of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoup_21d_curv_v054_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d up of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoup_21d_curv_v055_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsostd_63d_curv_v056_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsostd_63d_curv_v057_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsostd_63d_curv_v058_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsostd_63d_curv_v059_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsostd_63d_curv_v060_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d skew of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoskew_126d_curv_v061_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d skew of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoskew_126d_curv_v062_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d skew of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoskew_126d_curv_v063_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d skew of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoskew_126d_curv_v064_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d skew of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoskew_126d_curv_v065_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d kurt of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsokurt_252d_curv_v066_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d kurt of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsokurt_252d_curv_v067_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d kurt of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsokurt_252d_curv_v068_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d kurt of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsokurt_252d_curv_v069_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d kurt of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsokurt_252d_curv_v070_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d hits of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohits_504d_curv_v071_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d hits of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohits_504d_curv_v072_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d hits of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohits_504d_curv_v073_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d hits of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohits_504d_curv_v074_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d hits of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohits_504d_curv_v075_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d signcum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_21d_curv_v076_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d signcum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_21d_curv_v077_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d signcum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_21d_curv_v078_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d signcum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_21d_curv_v079_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d signcum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsosigncum_21d_curv_v080_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d cum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_63d_curv_v081_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d cum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_63d_curv_v082_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d cum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_63d_curv_v083_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d cum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_63d_curv_v084_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d cum of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocum_63d_curv_v085_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d emafast of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemafast_126d_curv_v086_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d emafast of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemafast_126d_curv_v087_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d emafast of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemafast_126d_curv_v088_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d emafast of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemafast_126d_curv_v089_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d emafast of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemafast_126d_curv_v090_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d emaslow of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_252d_curv_v091_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d emaslow of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_252d_curv_v092_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d emaslow of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_252d_curv_v093_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d emaslow of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_252d_curv_v094_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d emaslow of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoemaslow_252d_curv_v095_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d zabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_504d_curv_v096_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504).abs()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d zabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_504d_curv_v097_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504).abs()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d zabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_504d_curv_v098_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504).abs()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d zabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_504d_curv_v099_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504).abs()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d zabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsozabs_504d_curv_v100_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504).abs()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d posmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_21d_curv_v101_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d posmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_21d_curv_v102_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d posmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_21d_curv_v103_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d posmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_21d_curv_v104_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d posmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoposmean_21d_curv_v105_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d negmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_63d_curv_v106_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d negmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_63d_curv_v107_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d negmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_63d_curv_v108_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d negmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_63d_curv_v109_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d negmean of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsonegmean_63d_curv_v110_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d cvar of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_126d_curv_v111_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d cvar of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_126d_curv_v112_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d cvar of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_126d_curv_v113_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d cvar of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_126d_curv_v114_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d cvar of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocvar_126d_curv_v115_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d logabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsologabs_252d_curv_v116_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d logabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsologabs_252d_curv_v117_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d logabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsologabs_252d_curv_v118_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d logabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsologabs_252d_curv_v119_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d logabs of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsologabs_252d_curv_v120_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d diff of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_504d_curv_v121_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff(periods=504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d diff of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_504d_curv_v122_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff(periods=504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d diff of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_504d_curv_v123_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff(periods=504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d diff of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_504d_curv_v124_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff(periods=504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d diff of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsodiff_504d_curv_v125_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff(periods=504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d pctchg of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_21d_curv_v126_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.pct_change(periods=21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d pctchg of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_21d_curv_v127_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.pct_change(periods=21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d pctchg of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_21d_curv_v128_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.pct_change(periods=21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d pctchg of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_21d_curv_v129_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.pct_change(periods=21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d pctchg of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsopctchg_21d_curv_v130_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.pct_change(periods=21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d xover of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoxover_63d_curv_v131_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d xover of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoxover_63d_curv_v132_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d xover of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoxover_63d_curv_v133_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d xover of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoxover_63d_curv_v134_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d xover of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsoxover_63d_curv_v135_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M - _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d trend of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_126d_curv_v136_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d trend of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_126d_curv_v137_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d trend of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_126d_curv_v138_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d trend of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_126d_curv_v139_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d trend of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsotrend_126d_curv_v140_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d highmask of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohighmask_252d_curv_v141_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d highmask of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohighmask_252d_curv_v142_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d highmask of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohighmask_252d_curv_v143_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d highmask of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohighmask_252d_curv_v144_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d highmask of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsohighmask_252d_curv_v145_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d compositez of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocompositez_504d_curv_v146_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d compositez of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocompositez_504d_curv_v147_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d compositez of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocompositez_504d_curv_v148_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d compositez of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocompositez_504d_curv_v149_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d compositez of days sales outstanding (DSO)
def f39dso_f39_semi_dso_dynamics_dsocompositez_504d_curv_v150_signal(receivables, revenue, closeadj):
    M = _f39dso_ratio(receivables, revenue) * 365
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


