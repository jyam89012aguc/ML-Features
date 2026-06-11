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
def _f35ib_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f35ib_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f35ib_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f35ib_diff(a, b):
    return a - b


# 5d curvature of 21d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_21d_curv_v001_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_21d_curv_v002_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_21d_curv_v003_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_21d_curv_v004_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d level of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevel_21d_curv_v005_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d levelrel of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_63d_curv_v006_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d levelrel of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_63d_curv_v007_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d levelrel of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_63d_curv_v008_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d levelrel of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_63d_curv_v009_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d levelrel of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlevelrel_63d_curv_v010_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_126d_curv_v011_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_126d_curv_v012_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_126d_curv_v013_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_126d_curv_v014_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d mean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmean_126d_curv_v015_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d z of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_252d_curv_v016_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d z of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_252d_curv_v017_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d z of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_252d_curv_v018_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d z of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_252d_curv_v019_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d z of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnz_252d_curv_v020_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d robz of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrobz_504d_curv_v021_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d robz of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrobz_504d_curv_v022_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d robz of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrobz_504d_curv_v023_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d robz of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrobz_504d_curv_v024_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d robz of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrobz_504d_curv_v025_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_21d_curv_v026_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_21d_curv_v027_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_21d_curv_v028_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_21d_curv_v029_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d max of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmax_21d_curv_v030_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_63d_curv_v031_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _min(M, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_63d_curv_v032_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _min(M, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_63d_curv_v033_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _min(M, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_63d_curv_v034_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _min(M, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d min of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnmin_63d_curv_v035_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _min(M, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d rng of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_126d_curv_v036_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d rng of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_126d_curv_v037_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d rng of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_126d_curv_v038_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d rng of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_126d_curv_v039_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d rng of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnrng_126d_curv_v040_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d pos of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpos_252d_curv_v041_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d pos of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpos_252d_curv_v042_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d pos of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpos_252d_curv_v043_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d pos of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpos_252d_curv_v044_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d pos of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpos_252d_curv_v045_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d dd of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndd_504d_curv_v046_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d dd of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndd_504d_curv_v047_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d dd of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndd_504d_curv_v048_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d dd of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndd_504d_curv_v049_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d dd of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndd_504d_curv_v050_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d up of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnup_21d_curv_v051_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d up of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnup_21d_curv_v052_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d up of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnup_21d_curv_v053_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d up of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnup_21d_curv_v054_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d up of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnup_21d_curv_v055_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_63d_curv_v056_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_63d_curv_v057_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_63d_curv_v058_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_63d_curv_v059_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnstd_63d_curv_v060_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_126d_curv_v061_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_126d_curv_v062_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_126d_curv_v063_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_126d_curv_v064_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d skew of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnskew_126d_curv_v065_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d kurt of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_252d_curv_v066_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d kurt of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_252d_curv_v067_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d kurt of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_252d_curv_v068_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d kurt of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_252d_curv_v069_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d kurt of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnkurt_252d_curv_v070_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d hits of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_504d_curv_v071_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d hits of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_504d_curv_v072_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d hits of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_504d_curv_v073_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d hits of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_504d_curv_v074_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d hits of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhits_504d_curv_v075_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d signcum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnsigncum_21d_curv_v076_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d signcum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnsigncum_21d_curv_v077_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d signcum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnsigncum_21d_curv_v078_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d signcum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnsigncum_21d_curv_v079_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d signcum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnsigncum_21d_curv_v080_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d cum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncum_63d_curv_v081_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d cum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncum_63d_curv_v082_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d cum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncum_63d_curv_v083_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d cum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncum_63d_curv_v084_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d cum of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncum_63d_curv_v085_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d emafast of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemafast_126d_curv_v086_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d emafast of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemafast_126d_curv_v087_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d emafast of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemafast_126d_curv_v088_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d emafast of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemafast_126d_curv_v089_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d emafast of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemafast_126d_curv_v090_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d emaslow of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemaslow_252d_curv_v091_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d emaslow of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemaslow_252d_curv_v092_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d emaslow of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemaslow_252d_curv_v093_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d emaslow of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemaslow_252d_curv_v094_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d emaslow of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnemaslow_252d_curv_v095_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d zabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnzabs_504d_curv_v096_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504).abs()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d zabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnzabs_504d_curv_v097_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504).abs()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d zabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnzabs_504d_curv_v098_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504).abs()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d zabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnzabs_504d_curv_v099_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504).abs()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d zabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnzabs_504d_curv_v100_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504).abs()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d posmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnposmean_21d_curv_v101_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d posmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnposmean_21d_curv_v102_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d posmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnposmean_21d_curv_v103_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d posmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnposmean_21d_curv_v104_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d posmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnposmean_21d_curv_v105_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d negmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnnegmean_63d_curv_v106_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d negmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnnegmean_63d_curv_v107_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d negmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnnegmean_63d_curv_v108_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d negmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnnegmean_63d_curv_v109_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d negmean of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnnegmean_63d_curv_v110_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d cvar of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncvar_126d_curv_v111_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d cvar of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncvar_126d_curv_v112_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d cvar of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncvar_126d_curv_v113_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d cvar of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncvar_126d_curv_v114_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d cvar of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncvar_126d_curv_v115_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d logabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlogabs_252d_curv_v116_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d logabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlogabs_252d_curv_v117_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d logabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlogabs_252d_curv_v118_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d logabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlogabs_252d_curv_v119_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d logabs of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnlogabs_252d_curv_v120_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d diff of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndiff_504d_curv_v121_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff(periods=504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d diff of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndiff_504d_curv_v122_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff(periods=504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d diff of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndiff_504d_curv_v123_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff(periods=504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d diff of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndiff_504d_curv_v124_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff(periods=504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d diff of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburndiff_504d_curv_v125_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff(periods=504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d pctchg of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpctchg_21d_curv_v126_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.pct_change(periods=21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d pctchg of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpctchg_21d_curv_v127_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.pct_change(periods=21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d pctchg of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpctchg_21d_curv_v128_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.pct_change(periods=21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d pctchg of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpctchg_21d_curv_v129_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.pct_change(periods=21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d pctchg of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnpctchg_21d_curv_v130_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.pct_change(periods=21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d xover of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnxover_63d_curv_v131_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d xover of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnxover_63d_curv_v132_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d xover of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnxover_63d_curv_v133_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d xover of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnxover_63d_curv_v134_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d xover of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnxover_63d_curv_v135_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M - _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d trend of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburntrend_126d_curv_v136_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d trend of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburntrend_126d_curv_v137_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d trend of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburntrend_126d_curv_v138_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d trend of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburntrend_126d_curv_v139_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d trend of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburntrend_126d_curv_v140_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d highmask of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhighmask_252d_curv_v141_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d highmask of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhighmask_252d_curv_v142_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d highmask of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhighmask_252d_curv_v143_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d highmask of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhighmask_252d_curv_v144_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d highmask of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburnhighmask_252d_curv_v145_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d compositez of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncompositez_504d_curv_v146_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d compositez of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncompositez_504d_curv_v147_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d compositez of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncompositez_504d_curv_v148_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d compositez of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncompositez_504d_curv_v149_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d compositez of sequential inventory burn (negative log change)
def f35ib_f35_semi_inventory_burn_invburncompositez_504d_curv_v150_signal(inventory, closeadj):
    M = -_f35ib_log_change(inventory, 63)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


