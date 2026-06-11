"""Family f079 - Financial statement timeliness (Fundamental Dynamics) | Sharadar tables: SF1 | fields: calendardate, reportperiod, datekey, lastupdated | 3rd derivatives 001-150"""
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
def _reporting_recency_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _reporting_recency_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _reporting_recency_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw filingage
def rr_f079_reporting_recency_raw_21d_accel_v001_signal(filingage, closeadj):
    base = _mean(filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw filingage
def rr_f079_reporting_recency_raw_21d_accel_v002_signal(filingage, closeadj):
    base = _mean(filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw filingage
def rr_f079_reporting_recency_raw_21d_accel_v003_signal(filingage, closeadj):
    base = _mean(filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw filingage
def rr_f079_reporting_recency_raw_63d_accel_v004_signal(filingage, closeadj):
    base = _mean(filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw filingage
def rr_f079_reporting_recency_raw_63d_accel_v005_signal(filingage, closeadj):
    base = _mean(filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw filingage
def rr_f079_reporting_recency_raw_63d_accel_v006_signal(filingage, closeadj):
    base = _mean(filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw filingage
def rr_f079_reporting_recency_raw_126d_accel_v007_signal(filingage, closeadj):
    base = _mean(filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw filingage
def rr_f079_reporting_recency_raw_126d_accel_v008_signal(filingage, closeadj):
    base = _mean(filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw filingage
def rr_f079_reporting_recency_raw_126d_accel_v009_signal(filingage, closeadj):
    base = _mean(filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw filingage
def rr_f079_reporting_recency_raw_252d_accel_v010_signal(filingage, closeadj):
    base = _mean(filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw filingage
def rr_f079_reporting_recency_raw_252d_accel_v011_signal(filingage, closeadj):
    base = _mean(filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw filingage
def rr_f079_reporting_recency_raw_252d_accel_v012_signal(filingage, closeadj):
    base = _mean(filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw filingage
def rr_f079_reporting_recency_raw_504d_accel_v013_signal(filingage, closeadj):
    base = _mean(filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw filingage
def rr_f079_reporting_recency_raw_504d_accel_v014_signal(filingage, closeadj):
    base = _mean(filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw filingage
def rr_f079_reporting_recency_raw_504d_accel_v015_signal(filingage, closeadj):
    base = _mean(filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log filingage
def rr_f079_reporting_recency_log_21d_accel_v016_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log filingage
def rr_f079_reporting_recency_log_21d_accel_v017_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log filingage
def rr_f079_reporting_recency_log_21d_accel_v018_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log filingage
def rr_f079_reporting_recency_log_63d_accel_v019_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log filingage
def rr_f079_reporting_recency_log_63d_accel_v020_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log filingage
def rr_f079_reporting_recency_log_63d_accel_v021_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log filingage
def rr_f079_reporting_recency_log_126d_accel_v022_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log filingage
def rr_f079_reporting_recency_log_126d_accel_v023_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log filingage
def rr_f079_reporting_recency_log_126d_accel_v024_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log filingage
def rr_f079_reporting_recency_log_252d_accel_v025_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log filingage
def rr_f079_reporting_recency_log_252d_accel_v026_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log filingage
def rr_f079_reporting_recency_log_252d_accel_v027_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log filingage
def rr_f079_reporting_recency_log_504d_accel_v028_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log filingage
def rr_f079_reporting_recency_log_504d_accel_v029_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log filingage
def rr_f079_reporting_recency_log_504d_accel_v030_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare filingage
def rr_f079_reporting_recency_pershare_21d_accel_v031_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare filingage
def rr_f079_reporting_recency_pershare_21d_accel_v032_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare filingage
def rr_f079_reporting_recency_pershare_21d_accel_v033_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare filingage
def rr_f079_reporting_recency_pershare_63d_accel_v034_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare filingage
def rr_f079_reporting_recency_pershare_63d_accel_v035_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare filingage
def rr_f079_reporting_recency_pershare_63d_accel_v036_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare filingage
def rr_f079_reporting_recency_pershare_126d_accel_v037_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare filingage
def rr_f079_reporting_recency_pershare_126d_accel_v038_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare filingage
def rr_f079_reporting_recency_pershare_126d_accel_v039_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare filingage
def rr_f079_reporting_recency_pershare_252d_accel_v040_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare filingage
def rr_f079_reporting_recency_pershare_252d_accel_v041_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare filingage
def rr_f079_reporting_recency_pershare_252d_accel_v042_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare filingage
def rr_f079_reporting_recency_pershare_504d_accel_v043_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare filingage
def rr_f079_reporting_recency_pershare_504d_accel_v044_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare filingage
def rr_f079_reporting_recency_pershare_504d_accel_v045_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_21d_accel_v046_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_21d_accel_v047_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_21d_accel_v048_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_63d_accel_v049_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_63d_accel_v050_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_63d_accel_v051_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_126d_accel_v052_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_126d_accel_v053_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_126d_accel_v054_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_252d_accel_v055_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_252d_accel_v056_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_252d_accel_v057_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_504d_accel_v058_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_504d_accel_v059_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_504d_accel_v060_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_21d_accel_v061_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_21d_accel_v062_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_21d_accel_v063_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_63d_accel_v064_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_63d_accel_v065_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_63d_accel_v066_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_126d_accel_v067_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_126d_accel_v068_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_126d_accel_v069_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_252d_accel_v070_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_252d_accel_v071_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_252d_accel_v072_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_504d_accel_v073_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_504d_accel_v074_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_504d_accel_v075_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets filingage
def rr_f079_reporting_recency_per_assets_21d_accel_v076_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets filingage
def rr_f079_reporting_recency_per_assets_21d_accel_v077_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets filingage
def rr_f079_reporting_recency_per_assets_21d_accel_v078_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets filingage
def rr_f079_reporting_recency_per_assets_63d_accel_v079_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets filingage
def rr_f079_reporting_recency_per_assets_63d_accel_v080_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets filingage
def rr_f079_reporting_recency_per_assets_63d_accel_v081_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets filingage
def rr_f079_reporting_recency_per_assets_126d_accel_v082_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets filingage
def rr_f079_reporting_recency_per_assets_126d_accel_v083_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets filingage
def rr_f079_reporting_recency_per_assets_126d_accel_v084_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets filingage
def rr_f079_reporting_recency_per_assets_252d_accel_v085_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets filingage
def rr_f079_reporting_recency_per_assets_252d_accel_v086_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets filingage
def rr_f079_reporting_recency_per_assets_252d_accel_v087_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets filingage
def rr_f079_reporting_recency_per_assets_504d_accel_v088_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets filingage
def rr_f079_reporting_recency_per_assets_504d_accel_v089_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets filingage
def rr_f079_reporting_recency_per_assets_504d_accel_v090_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std filingage
def rr_f079_reporting_recency_std_21d_accel_v091_signal(filingage, closeadj):
    base = _std(filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std filingage
def rr_f079_reporting_recency_std_21d_accel_v092_signal(filingage, closeadj):
    base = _std(filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std filingage
def rr_f079_reporting_recency_std_21d_accel_v093_signal(filingage, closeadj):
    base = _std(filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std filingage
def rr_f079_reporting_recency_std_63d_accel_v094_signal(filingage, closeadj):
    base = _std(filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std filingage
def rr_f079_reporting_recency_std_63d_accel_v095_signal(filingage, closeadj):
    base = _std(filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std filingage
def rr_f079_reporting_recency_std_63d_accel_v096_signal(filingage, closeadj):
    base = _std(filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std filingage
def rr_f079_reporting_recency_std_126d_accel_v097_signal(filingage, closeadj):
    base = _std(filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std filingage
def rr_f079_reporting_recency_std_126d_accel_v098_signal(filingage, closeadj):
    base = _std(filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std filingage
def rr_f079_reporting_recency_std_126d_accel_v099_signal(filingage, closeadj):
    base = _std(filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std filingage
def rr_f079_reporting_recency_std_252d_accel_v100_signal(filingage, closeadj):
    base = _std(filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std filingage
def rr_f079_reporting_recency_std_252d_accel_v101_signal(filingage, closeadj):
    base = _std(filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std filingage
def rr_f079_reporting_recency_std_252d_accel_v102_signal(filingage, closeadj):
    base = _std(filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std filingage
def rr_f079_reporting_recency_std_504d_accel_v103_signal(filingage, closeadj):
    base = _std(filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std filingage
def rr_f079_reporting_recency_std_504d_accel_v104_signal(filingage, closeadj):
    base = _std(filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std filingage
def rr_f079_reporting_recency_std_504d_accel_v105_signal(filingage, closeadj):
    base = _std(filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm filingage
def rr_f079_reporting_recency_ewm_21d_accel_v106_signal(filingage, closeadj):
    base = filingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm filingage
def rr_f079_reporting_recency_ewm_21d_accel_v107_signal(filingage, closeadj):
    base = filingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm filingage
def rr_f079_reporting_recency_ewm_21d_accel_v108_signal(filingage, closeadj):
    base = filingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm filingage
def rr_f079_reporting_recency_ewm_63d_accel_v109_signal(filingage, closeadj):
    base = filingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm filingage
def rr_f079_reporting_recency_ewm_63d_accel_v110_signal(filingage, closeadj):
    base = filingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm filingage
def rr_f079_reporting_recency_ewm_63d_accel_v111_signal(filingage, closeadj):
    base = filingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm filingage
def rr_f079_reporting_recency_ewm_126d_accel_v112_signal(filingage, closeadj):
    base = filingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm filingage
def rr_f079_reporting_recency_ewm_126d_accel_v113_signal(filingage, closeadj):
    base = filingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm filingage
def rr_f079_reporting_recency_ewm_126d_accel_v114_signal(filingage, closeadj):
    base = filingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm filingage
def rr_f079_reporting_recency_ewm_252d_accel_v115_signal(filingage, closeadj):
    base = filingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm filingage
def rr_f079_reporting_recency_ewm_252d_accel_v116_signal(filingage, closeadj):
    base = filingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm filingage
def rr_f079_reporting_recency_ewm_252d_accel_v117_signal(filingage, closeadj):
    base = filingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm filingage
def rr_f079_reporting_recency_ewm_504d_accel_v118_signal(filingage, closeadj):
    base = filingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm filingage
def rr_f079_reporting_recency_ewm_504d_accel_v119_signal(filingage, closeadj):
    base = filingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm filingage
def rr_f079_reporting_recency_ewm_504d_accel_v120_signal(filingage, closeadj):
    base = filingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq filingage
def rr_f079_reporting_recency_sq_21d_accel_v121_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq filingage
def rr_f079_reporting_recency_sq_21d_accel_v122_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq filingage
def rr_f079_reporting_recency_sq_21d_accel_v123_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq filingage
def rr_f079_reporting_recency_sq_63d_accel_v124_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq filingage
def rr_f079_reporting_recency_sq_63d_accel_v125_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq filingage
def rr_f079_reporting_recency_sq_63d_accel_v126_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq filingage
def rr_f079_reporting_recency_sq_126d_accel_v127_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq filingage
def rr_f079_reporting_recency_sq_126d_accel_v128_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq filingage
def rr_f079_reporting_recency_sq_126d_accel_v129_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq filingage
def rr_f079_reporting_recency_sq_252d_accel_v130_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq filingage
def rr_f079_reporting_recency_sq_252d_accel_v131_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq filingage
def rr_f079_reporting_recency_sq_252d_accel_v132_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq filingage
def rr_f079_reporting_recency_sq_504d_accel_v133_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq filingage
def rr_f079_reporting_recency_sq_504d_accel_v134_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq filingage
def rr_f079_reporting_recency_sq_504d_accel_v135_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z filingage
def rr_f079_reporting_recency_z_21d_accel_v136_signal(filingage):
    base = _z(filingage, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z filingage
def rr_f079_reporting_recency_z_21d_accel_v137_signal(filingage):
    base = _z(filingage, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z filingage
def rr_f079_reporting_recency_z_21d_accel_v138_signal(filingage):
    base = _z(filingage, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z filingage
def rr_f079_reporting_recency_z_63d_accel_v139_signal(filingage):
    base = _z(filingage, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z filingage
def rr_f079_reporting_recency_z_63d_accel_v140_signal(filingage):
    base = _z(filingage, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z filingage
def rr_f079_reporting_recency_z_63d_accel_v141_signal(filingage):
    base = _z(filingage, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z filingage
def rr_f079_reporting_recency_z_126d_accel_v142_signal(filingage):
    base = _z(filingage, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z filingage
def rr_f079_reporting_recency_z_126d_accel_v143_signal(filingage):
    base = _z(filingage, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z filingage
def rr_f079_reporting_recency_z_126d_accel_v144_signal(filingage):
    base = _z(filingage, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z filingage
def rr_f079_reporting_recency_z_252d_accel_v145_signal(filingage):
    base = _z(filingage, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z filingage
def rr_f079_reporting_recency_z_252d_accel_v146_signal(filingage):
    base = _z(filingage, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z filingage
def rr_f079_reporting_recency_z_252d_accel_v147_signal(filingage):
    base = _z(filingage, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z filingage
def rr_f079_reporting_recency_z_504d_accel_v148_signal(filingage):
    base = _z(filingage, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z filingage
def rr_f079_reporting_recency_z_504d_accel_v149_signal(filingage):
    base = _z(filingage, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z filingage
def rr_f079_reporting_recency_z_504d_accel_v150_signal(filingage):
    base = _z(filingage, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
