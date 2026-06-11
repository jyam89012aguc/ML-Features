"""Family f026 - preferred, convertible, and senior claim overhang (Capital Structure) | Sharadar tables: SF1 | fields: prefdivis, debtusd, assets, marketcap, equity, debt | 3rd derivatives 001-150"""
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
def _preferred_and_convertible_overhang_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _preferred_and_convertible_overhang_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _preferred_and_convertible_overhang_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_21d_accel_v001_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_21d_accel_v002_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_21d_accel_v003_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_63d_accel_v004_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_63d_accel_v005_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_63d_accel_v006_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_126d_accel_v007_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_126d_accel_v008_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_126d_accel_v009_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_252d_accel_v010_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_252d_accel_v011_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_252d_accel_v012_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_504d_accel_v013_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_504d_accel_v014_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw prefdivis
def paco_f026_preferred_and_convertible_overhang_raw_504d_accel_v015_signal(prefdivis, closeadj):
    base = _mean(prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_21d_accel_v016_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_21d_accel_v017_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_21d_accel_v018_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_63d_accel_v019_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_63d_accel_v020_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_63d_accel_v021_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_126d_accel_v022_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_126d_accel_v023_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_126d_accel_v024_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_252d_accel_v025_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_252d_accel_v026_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_252d_accel_v027_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_504d_accel_v028_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_504d_accel_v029_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log prefdivis
def paco_f026_preferred_and_convertible_overhang_log_504d_accel_v030_signal(prefdivis, closeadj):
    base = _mean(_preferred_and_convertible_overhang_log(prefdivis), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_21d_accel_v031_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_21d_accel_v032_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_21d_accel_v033_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_63d_accel_v034_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_63d_accel_v035_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_63d_accel_v036_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_126d_accel_v037_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_126d_accel_v038_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_126d_accel_v039_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_252d_accel_v040_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_252d_accel_v041_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_252d_accel_v042_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_504d_accel_v043_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_504d_accel_v044_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare prefdivis
def paco_f026_preferred_and_convertible_overhang_pershare_504d_accel_v045_signal(prefdivis, sharesbas, closeadj):
    base = _mean(_preferred_and_convertible_overhang_per_share(prefdivis, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_21d_accel_v046_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_21d_accel_v047_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_21d_accel_v048_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_63d_accel_v049_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_63d_accel_v050_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_63d_accel_v051_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_126d_accel_v052_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_126d_accel_v053_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_126d_accel_v054_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_252d_accel_v055_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_252d_accel_v056_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_252d_accel_v057_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_504d_accel_v058_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_504d_accel_v059_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_debtusd prefdivis
def paco_f026_preferred_and_convertible_overhang_per_debtusd_504d_accel_v060_signal(prefdivis, debtusd):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, debtusd), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_21d_accel_v061_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_21d_accel_v062_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_21d_accel_v063_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_63d_accel_v064_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_63d_accel_v065_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_63d_accel_v066_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_126d_accel_v067_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_126d_accel_v068_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_126d_accel_v069_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_252d_accel_v070_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_252d_accel_v071_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_252d_accel_v072_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_504d_accel_v073_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_504d_accel_v074_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets prefdivis
def paco_f026_preferred_and_convertible_overhang_per_assets_504d_accel_v075_signal(prefdivis, assets):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_21d_accel_v076_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_21d_accel_v077_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_21d_accel_v078_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_63d_accel_v079_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_63d_accel_v080_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_63d_accel_v081_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_126d_accel_v082_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_126d_accel_v083_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_126d_accel_v084_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_252d_accel_v085_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_252d_accel_v086_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_252d_accel_v087_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_504d_accel_v088_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_504d_accel_v089_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap prefdivis
def paco_f026_preferred_and_convertible_overhang_per_marketcap_504d_accel_v090_signal(prefdivis, marketcap):
    base = _mean(_preferred_and_convertible_overhang_scaled(prefdivis, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_21d_accel_v091_signal(prefdivis, closeadj):
    base = _std(prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_21d_accel_v092_signal(prefdivis, closeadj):
    base = _std(prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_21d_accel_v093_signal(prefdivis, closeadj):
    base = _std(prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_63d_accel_v094_signal(prefdivis, closeadj):
    base = _std(prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_63d_accel_v095_signal(prefdivis, closeadj):
    base = _std(prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_63d_accel_v096_signal(prefdivis, closeadj):
    base = _std(prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_126d_accel_v097_signal(prefdivis, closeadj):
    base = _std(prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_126d_accel_v098_signal(prefdivis, closeadj):
    base = _std(prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_126d_accel_v099_signal(prefdivis, closeadj):
    base = _std(prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_252d_accel_v100_signal(prefdivis, closeadj):
    base = _std(prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_252d_accel_v101_signal(prefdivis, closeadj):
    base = _std(prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_252d_accel_v102_signal(prefdivis, closeadj):
    base = _std(prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_504d_accel_v103_signal(prefdivis, closeadj):
    base = _std(prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_504d_accel_v104_signal(prefdivis, closeadj):
    base = _std(prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std prefdivis
def paco_f026_preferred_and_convertible_overhang_std_504d_accel_v105_signal(prefdivis, closeadj):
    base = _std(prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_21d_accel_v106_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_21d_accel_v107_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_21d_accel_v108_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_63d_accel_v109_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_63d_accel_v110_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_63d_accel_v111_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_126d_accel_v112_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_126d_accel_v113_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_126d_accel_v114_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_252d_accel_v115_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_252d_accel_v116_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_252d_accel_v117_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_504d_accel_v118_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_504d_accel_v119_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm prefdivis
def paco_f026_preferred_and_convertible_overhang_ewm_504d_accel_v120_signal(prefdivis, closeadj):
    base = prefdivis.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_21d_accel_v121_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_21d_accel_v122_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_21d_accel_v123_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_63d_accel_v124_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_63d_accel_v125_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_63d_accel_v126_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_126d_accel_v127_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_126d_accel_v128_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_126d_accel_v129_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_252d_accel_v130_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_252d_accel_v131_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_252d_accel_v132_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_504d_accel_v133_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_504d_accel_v134_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq prefdivis
def paco_f026_preferred_and_convertible_overhang_sq_504d_accel_v135_signal(prefdivis, closeadj):
    base = _mean(prefdivis * prefdivis, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_21d_accel_v136_signal(prefdivis):
    base = _z(prefdivis, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_21d_accel_v137_signal(prefdivis):
    base = _z(prefdivis, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_21d_accel_v138_signal(prefdivis):
    base = _z(prefdivis, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_63d_accel_v139_signal(prefdivis):
    base = _z(prefdivis, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_63d_accel_v140_signal(prefdivis):
    base = _z(prefdivis, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_63d_accel_v141_signal(prefdivis):
    base = _z(prefdivis, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_126d_accel_v142_signal(prefdivis):
    base = _z(prefdivis, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_126d_accel_v143_signal(prefdivis):
    base = _z(prefdivis, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_126d_accel_v144_signal(prefdivis):
    base = _z(prefdivis, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_252d_accel_v145_signal(prefdivis):
    base = _z(prefdivis, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_252d_accel_v146_signal(prefdivis):
    base = _z(prefdivis, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_252d_accel_v147_signal(prefdivis):
    base = _z(prefdivis, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_504d_accel_v148_signal(prefdivis):
    base = _z(prefdivis, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_504d_accel_v149_signal(prefdivis):
    base = _z(prefdivis, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z prefdivis
def paco_f026_preferred_and_convertible_overhang_z_504d_accel_v150_signal(prefdivis):
    base = _z(prefdivis, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
