"""Family f079 - Financial statement timeliness (Fundamental Dynamics) | Sharadar tables: SF1 | fields: calendardate, reportperiod, datekey, lastupdated | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw filingage
def rr_f079_reporting_recency_raw_21d_slope_v001_signal(filingage, closeadj):
    base = _mean(filingage, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw filingage
def rr_f079_reporting_recency_raw_21d_slope_v002_signal(filingage, closeadj):
    base = _mean(filingage, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw filingage
def rr_f079_reporting_recency_raw_21d_slope_v003_signal(filingage, closeadj):
    base = _mean(filingage, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw filingage
def rr_f079_reporting_recency_raw_63d_slope_v004_signal(filingage, closeadj):
    base = _mean(filingage, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw filingage
def rr_f079_reporting_recency_raw_63d_slope_v005_signal(filingage, closeadj):
    base = _mean(filingage, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw filingage
def rr_f079_reporting_recency_raw_63d_slope_v006_signal(filingage, closeadj):
    base = _mean(filingage, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw filingage
def rr_f079_reporting_recency_raw_126d_slope_v007_signal(filingage, closeadj):
    base = _mean(filingage, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw filingage
def rr_f079_reporting_recency_raw_126d_slope_v008_signal(filingage, closeadj):
    base = _mean(filingage, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw filingage
def rr_f079_reporting_recency_raw_126d_slope_v009_signal(filingage, closeadj):
    base = _mean(filingage, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw filingage
def rr_f079_reporting_recency_raw_252d_slope_v010_signal(filingage, closeadj):
    base = _mean(filingage, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw filingage
def rr_f079_reporting_recency_raw_252d_slope_v011_signal(filingage, closeadj):
    base = _mean(filingage, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw filingage
def rr_f079_reporting_recency_raw_252d_slope_v012_signal(filingage, closeadj):
    base = _mean(filingage, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw filingage
def rr_f079_reporting_recency_raw_504d_slope_v013_signal(filingage, closeadj):
    base = _mean(filingage, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw filingage
def rr_f079_reporting_recency_raw_504d_slope_v014_signal(filingage, closeadj):
    base = _mean(filingage, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw filingage
def rr_f079_reporting_recency_raw_504d_slope_v015_signal(filingage, closeadj):
    base = _mean(filingage, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log filingage
def rr_f079_reporting_recency_log_21d_slope_v016_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log filingage
def rr_f079_reporting_recency_log_21d_slope_v017_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log filingage
def rr_f079_reporting_recency_log_21d_slope_v018_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log filingage
def rr_f079_reporting_recency_log_63d_slope_v019_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log filingage
def rr_f079_reporting_recency_log_63d_slope_v020_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log filingage
def rr_f079_reporting_recency_log_63d_slope_v021_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log filingage
def rr_f079_reporting_recency_log_126d_slope_v022_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log filingage
def rr_f079_reporting_recency_log_126d_slope_v023_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log filingage
def rr_f079_reporting_recency_log_126d_slope_v024_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log filingage
def rr_f079_reporting_recency_log_252d_slope_v025_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log filingage
def rr_f079_reporting_recency_log_252d_slope_v026_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log filingage
def rr_f079_reporting_recency_log_252d_slope_v027_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log filingage
def rr_f079_reporting_recency_log_504d_slope_v028_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log filingage
def rr_f079_reporting_recency_log_504d_slope_v029_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log filingage
def rr_f079_reporting_recency_log_504d_slope_v030_signal(filingage, closeadj):
    base = _mean(_reporting_recency_log(filingage), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare filingage
def rr_f079_reporting_recency_pershare_21d_slope_v031_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare filingage
def rr_f079_reporting_recency_pershare_21d_slope_v032_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare filingage
def rr_f079_reporting_recency_pershare_21d_slope_v033_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare filingage
def rr_f079_reporting_recency_pershare_63d_slope_v034_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare filingage
def rr_f079_reporting_recency_pershare_63d_slope_v035_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare filingage
def rr_f079_reporting_recency_pershare_63d_slope_v036_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare filingage
def rr_f079_reporting_recency_pershare_126d_slope_v037_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare filingage
def rr_f079_reporting_recency_pershare_126d_slope_v038_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare filingage
def rr_f079_reporting_recency_pershare_126d_slope_v039_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare filingage
def rr_f079_reporting_recency_pershare_252d_slope_v040_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare filingage
def rr_f079_reporting_recency_pershare_252d_slope_v041_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare filingage
def rr_f079_reporting_recency_pershare_252d_slope_v042_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare filingage
def rr_f079_reporting_recency_pershare_504d_slope_v043_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare filingage
def rr_f079_reporting_recency_pershare_504d_slope_v044_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare filingage
def rr_f079_reporting_recency_pershare_504d_slope_v045_signal(filingage, sharesbas, closeadj):
    base = _mean(_reporting_recency_per_share(filingage, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_21d_slope_v046_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_21d_slope_v047_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_21d_slope_v048_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_63d_slope_v049_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_63d_slope_v050_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_63d_slope_v051_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_126d_slope_v052_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_126d_slope_v053_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_126d_slope_v054_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_252d_slope_v055_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_252d_slope_v056_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_252d_slope_v057_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_504d_slope_v058_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_504d_slope_v059_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_calendardate filingage
def rr_f079_reporting_recency_per_calendardate_504d_slope_v060_signal(filingage, calendardate):
    base = _mean(_reporting_recency_scaled(filingage, calendardate), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_21d_slope_v061_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_21d_slope_v062_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_21d_slope_v063_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_63d_slope_v064_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_63d_slope_v065_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_63d_slope_v066_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_126d_slope_v067_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_126d_slope_v068_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_126d_slope_v069_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_252d_slope_v070_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_252d_slope_v071_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_252d_slope_v072_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_504d_slope_v073_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_504d_slope_v074_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_datekey filingage
def rr_f079_reporting_recency_per_datekey_504d_slope_v075_signal(filingage, datekey):
    base = _mean(_reporting_recency_scaled(filingage, datekey), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets filingage
def rr_f079_reporting_recency_per_assets_21d_slope_v076_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets filingage
def rr_f079_reporting_recency_per_assets_21d_slope_v077_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets filingage
def rr_f079_reporting_recency_per_assets_21d_slope_v078_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets filingage
def rr_f079_reporting_recency_per_assets_63d_slope_v079_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets filingage
def rr_f079_reporting_recency_per_assets_63d_slope_v080_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets filingage
def rr_f079_reporting_recency_per_assets_63d_slope_v081_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets filingage
def rr_f079_reporting_recency_per_assets_126d_slope_v082_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets filingage
def rr_f079_reporting_recency_per_assets_126d_slope_v083_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets filingage
def rr_f079_reporting_recency_per_assets_126d_slope_v084_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets filingage
def rr_f079_reporting_recency_per_assets_252d_slope_v085_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets filingage
def rr_f079_reporting_recency_per_assets_252d_slope_v086_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets filingage
def rr_f079_reporting_recency_per_assets_252d_slope_v087_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets filingage
def rr_f079_reporting_recency_per_assets_504d_slope_v088_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets filingage
def rr_f079_reporting_recency_per_assets_504d_slope_v089_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets filingage
def rr_f079_reporting_recency_per_assets_504d_slope_v090_signal(filingage, assets):
    base = _mean(_reporting_recency_scaled(filingage, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std filingage
def rr_f079_reporting_recency_std_21d_slope_v091_signal(filingage, closeadj):
    base = _std(filingage, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std filingage
def rr_f079_reporting_recency_std_21d_slope_v092_signal(filingage, closeadj):
    base = _std(filingage, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std filingage
def rr_f079_reporting_recency_std_21d_slope_v093_signal(filingage, closeadj):
    base = _std(filingage, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std filingage
def rr_f079_reporting_recency_std_63d_slope_v094_signal(filingage, closeadj):
    base = _std(filingage, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std filingage
def rr_f079_reporting_recency_std_63d_slope_v095_signal(filingage, closeadj):
    base = _std(filingage, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std filingage
def rr_f079_reporting_recency_std_63d_slope_v096_signal(filingage, closeadj):
    base = _std(filingage, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std filingage
def rr_f079_reporting_recency_std_126d_slope_v097_signal(filingage, closeadj):
    base = _std(filingage, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std filingage
def rr_f079_reporting_recency_std_126d_slope_v098_signal(filingage, closeadj):
    base = _std(filingage, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std filingage
def rr_f079_reporting_recency_std_126d_slope_v099_signal(filingage, closeadj):
    base = _std(filingage, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std filingage
def rr_f079_reporting_recency_std_252d_slope_v100_signal(filingage, closeadj):
    base = _std(filingage, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std filingage
def rr_f079_reporting_recency_std_252d_slope_v101_signal(filingage, closeadj):
    base = _std(filingage, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std filingage
def rr_f079_reporting_recency_std_252d_slope_v102_signal(filingage, closeadj):
    base = _std(filingage, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std filingage
def rr_f079_reporting_recency_std_504d_slope_v103_signal(filingage, closeadj):
    base = _std(filingage, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std filingage
def rr_f079_reporting_recency_std_504d_slope_v104_signal(filingage, closeadj):
    base = _std(filingage, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std filingage
def rr_f079_reporting_recency_std_504d_slope_v105_signal(filingage, closeadj):
    base = _std(filingage, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm filingage
def rr_f079_reporting_recency_ewm_21d_slope_v106_signal(filingage, closeadj):
    base = filingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm filingage
def rr_f079_reporting_recency_ewm_21d_slope_v107_signal(filingage, closeadj):
    base = filingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm filingage
def rr_f079_reporting_recency_ewm_21d_slope_v108_signal(filingage, closeadj):
    base = filingage.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm filingage
def rr_f079_reporting_recency_ewm_63d_slope_v109_signal(filingage, closeadj):
    base = filingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm filingage
def rr_f079_reporting_recency_ewm_63d_slope_v110_signal(filingage, closeadj):
    base = filingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm filingage
def rr_f079_reporting_recency_ewm_63d_slope_v111_signal(filingage, closeadj):
    base = filingage.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm filingage
def rr_f079_reporting_recency_ewm_126d_slope_v112_signal(filingage, closeadj):
    base = filingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm filingage
def rr_f079_reporting_recency_ewm_126d_slope_v113_signal(filingage, closeadj):
    base = filingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm filingage
def rr_f079_reporting_recency_ewm_126d_slope_v114_signal(filingage, closeadj):
    base = filingage.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm filingage
def rr_f079_reporting_recency_ewm_252d_slope_v115_signal(filingage, closeadj):
    base = filingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm filingage
def rr_f079_reporting_recency_ewm_252d_slope_v116_signal(filingage, closeadj):
    base = filingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm filingage
def rr_f079_reporting_recency_ewm_252d_slope_v117_signal(filingage, closeadj):
    base = filingage.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm filingage
def rr_f079_reporting_recency_ewm_504d_slope_v118_signal(filingage, closeadj):
    base = filingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm filingage
def rr_f079_reporting_recency_ewm_504d_slope_v119_signal(filingage, closeadj):
    base = filingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm filingage
def rr_f079_reporting_recency_ewm_504d_slope_v120_signal(filingage, closeadj):
    base = filingage.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq filingage
def rr_f079_reporting_recency_sq_21d_slope_v121_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq filingage
def rr_f079_reporting_recency_sq_21d_slope_v122_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq filingage
def rr_f079_reporting_recency_sq_21d_slope_v123_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq filingage
def rr_f079_reporting_recency_sq_63d_slope_v124_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq filingage
def rr_f079_reporting_recency_sq_63d_slope_v125_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq filingage
def rr_f079_reporting_recency_sq_63d_slope_v126_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq filingage
def rr_f079_reporting_recency_sq_126d_slope_v127_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq filingage
def rr_f079_reporting_recency_sq_126d_slope_v128_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq filingage
def rr_f079_reporting_recency_sq_126d_slope_v129_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq filingage
def rr_f079_reporting_recency_sq_252d_slope_v130_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq filingage
def rr_f079_reporting_recency_sq_252d_slope_v131_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq filingage
def rr_f079_reporting_recency_sq_252d_slope_v132_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq filingage
def rr_f079_reporting_recency_sq_504d_slope_v133_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq filingage
def rr_f079_reporting_recency_sq_504d_slope_v134_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq filingage
def rr_f079_reporting_recency_sq_504d_slope_v135_signal(filingage, closeadj):
    base = _mean(filingage * filingage, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z filingage
def rr_f079_reporting_recency_z_21d_slope_v136_signal(filingage):
    base = _z(filingage, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z filingage
def rr_f079_reporting_recency_z_21d_slope_v137_signal(filingage):
    base = _z(filingage, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z filingage
def rr_f079_reporting_recency_z_21d_slope_v138_signal(filingage):
    base = _z(filingage, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z filingage
def rr_f079_reporting_recency_z_63d_slope_v139_signal(filingage):
    base = _z(filingage, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z filingage
def rr_f079_reporting_recency_z_63d_slope_v140_signal(filingage):
    base = _z(filingage, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z filingage
def rr_f079_reporting_recency_z_63d_slope_v141_signal(filingage):
    base = _z(filingage, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z filingage
def rr_f079_reporting_recency_z_126d_slope_v142_signal(filingage):
    base = _z(filingage, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z filingage
def rr_f079_reporting_recency_z_126d_slope_v143_signal(filingage):
    base = _z(filingage, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z filingage
def rr_f079_reporting_recency_z_126d_slope_v144_signal(filingage):
    base = _z(filingage, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z filingage
def rr_f079_reporting_recency_z_252d_slope_v145_signal(filingage):
    base = _z(filingage, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z filingage
def rr_f079_reporting_recency_z_252d_slope_v146_signal(filingage):
    base = _z(filingage, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z filingage
def rr_f079_reporting_recency_z_252d_slope_v147_signal(filingage):
    base = _z(filingage, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z filingage
def rr_f079_reporting_recency_z_504d_slope_v148_signal(filingage):
    base = _z(filingage, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z filingage
def rr_f079_reporting_recency_z_504d_slope_v149_signal(filingage):
    base = _z(filingage, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z filingage
def rr_f079_reporting_recency_z_504d_slope_v150_signal(filingage):
    base = _z(filingage, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
