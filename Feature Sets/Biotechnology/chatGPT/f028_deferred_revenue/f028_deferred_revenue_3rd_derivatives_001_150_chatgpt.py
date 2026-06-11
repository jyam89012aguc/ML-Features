"""Family f028 - Deferred revenue and partner funding (Capital Structure) | Sharadar tables: SF1 | fields: deferredrev, revenue, liabilities | 3rd derivatives 001-150"""
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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _deferred_revenue_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _deferred_revenue_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _deferred_revenue_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw deferredrev
def dr_f028_deferred_revenue_raw_21d_accel_v001_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw deferredrev
def dr_f028_deferred_revenue_raw_21d_accel_v002_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw deferredrev
def dr_f028_deferred_revenue_raw_21d_accel_v003_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw deferredrev
def dr_f028_deferred_revenue_raw_63d_accel_v004_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw deferredrev
def dr_f028_deferred_revenue_raw_63d_accel_v005_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw deferredrev
def dr_f028_deferred_revenue_raw_63d_accel_v006_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw deferredrev
def dr_f028_deferred_revenue_raw_126d_accel_v007_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw deferredrev
def dr_f028_deferred_revenue_raw_126d_accel_v008_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw deferredrev
def dr_f028_deferred_revenue_raw_126d_accel_v009_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw deferredrev
def dr_f028_deferred_revenue_raw_252d_accel_v010_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw deferredrev
def dr_f028_deferred_revenue_raw_252d_accel_v011_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw deferredrev
def dr_f028_deferred_revenue_raw_252d_accel_v012_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw deferredrev
def dr_f028_deferred_revenue_raw_504d_accel_v013_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw deferredrev
def dr_f028_deferred_revenue_raw_504d_accel_v014_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw deferredrev
def dr_f028_deferred_revenue_raw_504d_accel_v015_signal(deferredrev, closeadj):
    base = _mean(deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log deferredrev
def dr_f028_deferred_revenue_log_21d_accel_v016_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log deferredrev
def dr_f028_deferred_revenue_log_21d_accel_v017_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log deferredrev
def dr_f028_deferred_revenue_log_21d_accel_v018_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log deferredrev
def dr_f028_deferred_revenue_log_63d_accel_v019_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log deferredrev
def dr_f028_deferred_revenue_log_63d_accel_v020_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log deferredrev
def dr_f028_deferred_revenue_log_63d_accel_v021_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log deferredrev
def dr_f028_deferred_revenue_log_126d_accel_v022_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log deferredrev
def dr_f028_deferred_revenue_log_126d_accel_v023_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log deferredrev
def dr_f028_deferred_revenue_log_126d_accel_v024_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log deferredrev
def dr_f028_deferred_revenue_log_252d_accel_v025_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log deferredrev
def dr_f028_deferred_revenue_log_252d_accel_v026_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log deferredrev
def dr_f028_deferred_revenue_log_252d_accel_v027_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log deferredrev
def dr_f028_deferred_revenue_log_504d_accel_v028_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log deferredrev
def dr_f028_deferred_revenue_log_504d_accel_v029_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log deferredrev
def dr_f028_deferred_revenue_log_504d_accel_v030_signal(deferredrev, closeadj):
    base = _mean(_deferred_revenue_log(deferredrev), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare deferredrev
def dr_f028_deferred_revenue_pershare_21d_accel_v031_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare deferredrev
def dr_f028_deferred_revenue_pershare_21d_accel_v032_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare deferredrev
def dr_f028_deferred_revenue_pershare_21d_accel_v033_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare deferredrev
def dr_f028_deferred_revenue_pershare_63d_accel_v034_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare deferredrev
def dr_f028_deferred_revenue_pershare_63d_accel_v035_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare deferredrev
def dr_f028_deferred_revenue_pershare_63d_accel_v036_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare deferredrev
def dr_f028_deferred_revenue_pershare_126d_accel_v037_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare deferredrev
def dr_f028_deferred_revenue_pershare_126d_accel_v038_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare deferredrev
def dr_f028_deferred_revenue_pershare_126d_accel_v039_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare deferredrev
def dr_f028_deferred_revenue_pershare_252d_accel_v040_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare deferredrev
def dr_f028_deferred_revenue_pershare_252d_accel_v041_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare deferredrev
def dr_f028_deferred_revenue_pershare_252d_accel_v042_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare deferredrev
def dr_f028_deferred_revenue_pershare_504d_accel_v043_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare deferredrev
def dr_f028_deferred_revenue_pershare_504d_accel_v044_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare deferredrev
def dr_f028_deferred_revenue_pershare_504d_accel_v045_signal(deferredrev, sharesbas, closeadj):
    base = _mean(_deferred_revenue_per_share(deferredrev, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_21d_accel_v046_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_21d_accel_v047_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_21d_accel_v048_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_63d_accel_v049_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_63d_accel_v050_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_63d_accel_v051_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_126d_accel_v052_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_126d_accel_v053_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_126d_accel_v054_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_252d_accel_v055_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_252d_accel_v056_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_252d_accel_v057_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_504d_accel_v058_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_504d_accel_v059_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_revenue deferredrev
def dr_f028_deferred_revenue_per_revenue_504d_accel_v060_signal(deferredrev, revenue):
    base = _mean(_deferred_revenue_scaled(deferredrev, revenue), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_21d_accel_v061_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_21d_accel_v062_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_21d_accel_v063_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_63d_accel_v064_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_63d_accel_v065_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_63d_accel_v066_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_126d_accel_v067_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_126d_accel_v068_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_126d_accel_v069_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_252d_accel_v070_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_252d_accel_v071_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_252d_accel_v072_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_504d_accel_v073_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_504d_accel_v074_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets deferredrev
def dr_f028_deferred_revenue_per_assets_504d_accel_v075_signal(deferredrev, assets):
    base = _mean(_deferred_revenue_scaled(deferredrev, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_21d_accel_v076_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_21d_accel_v077_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_21d_accel_v078_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_63d_accel_v079_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_63d_accel_v080_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_63d_accel_v081_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_126d_accel_v082_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_126d_accel_v083_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_126d_accel_v084_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_252d_accel_v085_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_252d_accel_v086_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_252d_accel_v087_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_504d_accel_v088_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_504d_accel_v089_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap deferredrev
def dr_f028_deferred_revenue_per_marketcap_504d_accel_v090_signal(deferredrev, marketcap):
    base = _mean(_deferred_revenue_scaled(deferredrev, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std deferredrev
def dr_f028_deferred_revenue_std_21d_accel_v091_signal(deferredrev, closeadj):
    base = _std(deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std deferredrev
def dr_f028_deferred_revenue_std_21d_accel_v092_signal(deferredrev, closeadj):
    base = _std(deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std deferredrev
def dr_f028_deferred_revenue_std_21d_accel_v093_signal(deferredrev, closeadj):
    base = _std(deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std deferredrev
def dr_f028_deferred_revenue_std_63d_accel_v094_signal(deferredrev, closeadj):
    base = _std(deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std deferredrev
def dr_f028_deferred_revenue_std_63d_accel_v095_signal(deferredrev, closeadj):
    base = _std(deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std deferredrev
def dr_f028_deferred_revenue_std_63d_accel_v096_signal(deferredrev, closeadj):
    base = _std(deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std deferredrev
def dr_f028_deferred_revenue_std_126d_accel_v097_signal(deferredrev, closeadj):
    base = _std(deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std deferredrev
def dr_f028_deferred_revenue_std_126d_accel_v098_signal(deferredrev, closeadj):
    base = _std(deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std deferredrev
def dr_f028_deferred_revenue_std_126d_accel_v099_signal(deferredrev, closeadj):
    base = _std(deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std deferredrev
def dr_f028_deferred_revenue_std_252d_accel_v100_signal(deferredrev, closeadj):
    base = _std(deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std deferredrev
def dr_f028_deferred_revenue_std_252d_accel_v101_signal(deferredrev, closeadj):
    base = _std(deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std deferredrev
def dr_f028_deferred_revenue_std_252d_accel_v102_signal(deferredrev, closeadj):
    base = _std(deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std deferredrev
def dr_f028_deferred_revenue_std_504d_accel_v103_signal(deferredrev, closeadj):
    base = _std(deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std deferredrev
def dr_f028_deferred_revenue_std_504d_accel_v104_signal(deferredrev, closeadj):
    base = _std(deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std deferredrev
def dr_f028_deferred_revenue_std_504d_accel_v105_signal(deferredrev, closeadj):
    base = _std(deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm deferredrev
def dr_f028_deferred_revenue_ewm_21d_accel_v106_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm deferredrev
def dr_f028_deferred_revenue_ewm_21d_accel_v107_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm deferredrev
def dr_f028_deferred_revenue_ewm_21d_accel_v108_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm deferredrev
def dr_f028_deferred_revenue_ewm_63d_accel_v109_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm deferredrev
def dr_f028_deferred_revenue_ewm_63d_accel_v110_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm deferredrev
def dr_f028_deferred_revenue_ewm_63d_accel_v111_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm deferredrev
def dr_f028_deferred_revenue_ewm_126d_accel_v112_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm deferredrev
def dr_f028_deferred_revenue_ewm_126d_accel_v113_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm deferredrev
def dr_f028_deferred_revenue_ewm_126d_accel_v114_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm deferredrev
def dr_f028_deferred_revenue_ewm_252d_accel_v115_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm deferredrev
def dr_f028_deferred_revenue_ewm_252d_accel_v116_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm deferredrev
def dr_f028_deferred_revenue_ewm_252d_accel_v117_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm deferredrev
def dr_f028_deferred_revenue_ewm_504d_accel_v118_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm deferredrev
def dr_f028_deferred_revenue_ewm_504d_accel_v119_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm deferredrev
def dr_f028_deferred_revenue_ewm_504d_accel_v120_signal(deferredrev, closeadj):
    base = deferredrev.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq deferredrev
def dr_f028_deferred_revenue_sq_21d_accel_v121_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq deferredrev
def dr_f028_deferred_revenue_sq_21d_accel_v122_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq deferredrev
def dr_f028_deferred_revenue_sq_21d_accel_v123_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq deferredrev
def dr_f028_deferred_revenue_sq_63d_accel_v124_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq deferredrev
def dr_f028_deferred_revenue_sq_63d_accel_v125_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq deferredrev
def dr_f028_deferred_revenue_sq_63d_accel_v126_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq deferredrev
def dr_f028_deferred_revenue_sq_126d_accel_v127_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq deferredrev
def dr_f028_deferred_revenue_sq_126d_accel_v128_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq deferredrev
def dr_f028_deferred_revenue_sq_126d_accel_v129_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq deferredrev
def dr_f028_deferred_revenue_sq_252d_accel_v130_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq deferredrev
def dr_f028_deferred_revenue_sq_252d_accel_v131_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq deferredrev
def dr_f028_deferred_revenue_sq_252d_accel_v132_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq deferredrev
def dr_f028_deferred_revenue_sq_504d_accel_v133_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq deferredrev
def dr_f028_deferred_revenue_sq_504d_accel_v134_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq deferredrev
def dr_f028_deferred_revenue_sq_504d_accel_v135_signal(deferredrev, closeadj):
    base = _mean(deferredrev * deferredrev, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z deferredrev
def dr_f028_deferred_revenue_z_21d_accel_v136_signal(deferredrev):
    base = _z(deferredrev, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z deferredrev
def dr_f028_deferred_revenue_z_21d_accel_v137_signal(deferredrev):
    base = _z(deferredrev, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z deferredrev
def dr_f028_deferred_revenue_z_21d_accel_v138_signal(deferredrev):
    base = _z(deferredrev, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z deferredrev
def dr_f028_deferred_revenue_z_63d_accel_v139_signal(deferredrev):
    base = _z(deferredrev, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z deferredrev
def dr_f028_deferred_revenue_z_63d_accel_v140_signal(deferredrev):
    base = _z(deferredrev, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z deferredrev
def dr_f028_deferred_revenue_z_63d_accel_v141_signal(deferredrev):
    base = _z(deferredrev, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z deferredrev
def dr_f028_deferred_revenue_z_126d_accel_v142_signal(deferredrev):
    base = _z(deferredrev, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z deferredrev
def dr_f028_deferred_revenue_z_126d_accel_v143_signal(deferredrev):
    base = _z(deferredrev, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z deferredrev
def dr_f028_deferred_revenue_z_126d_accel_v144_signal(deferredrev):
    base = _z(deferredrev, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z deferredrev
def dr_f028_deferred_revenue_z_252d_accel_v145_signal(deferredrev):
    base = _z(deferredrev, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z deferredrev
def dr_f028_deferred_revenue_z_252d_accel_v146_signal(deferredrev):
    base = _z(deferredrev, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z deferredrev
def dr_f028_deferred_revenue_z_252d_accel_v147_signal(deferredrev):
    base = _z(deferredrev, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z deferredrev
def dr_f028_deferred_revenue_z_504d_accel_v148_signal(deferredrev):
    base = _z(deferredrev, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z deferredrev
def dr_f028_deferred_revenue_z_504d_accel_v149_signal(deferredrev):
    base = _z(deferredrev, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z deferredrev
def dr_f028_deferred_revenue_z_504d_accel_v150_signal(deferredrev):
    base = _z(deferredrev, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
