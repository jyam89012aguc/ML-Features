"""Family f033 - Equity issuance proceeds (Dilution and Share Count) | Sharadar tables: SF1 | fields: ncfcommon, ncff, sharesbas | 3rd derivatives 001-150"""
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
def _equity_issuance_cash_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _equity_issuance_cash_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _equity_issuance_cash_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_21d_accel_v001_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_21d_accel_v002_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_21d_accel_v003_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_63d_accel_v004_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_63d_accel_v005_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_63d_accel_v006_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_126d_accel_v007_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_126d_accel_v008_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_126d_accel_v009_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_252d_accel_v010_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_252d_accel_v011_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_252d_accel_v012_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_504d_accel_v013_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_504d_accel_v014_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_504d_accel_v015_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log ncfcommon
def eic_f033_equity_issuance_cash_log_21d_accel_v016_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log ncfcommon
def eic_f033_equity_issuance_cash_log_21d_accel_v017_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log ncfcommon
def eic_f033_equity_issuance_cash_log_21d_accel_v018_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log ncfcommon
def eic_f033_equity_issuance_cash_log_63d_accel_v019_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log ncfcommon
def eic_f033_equity_issuance_cash_log_63d_accel_v020_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log ncfcommon
def eic_f033_equity_issuance_cash_log_63d_accel_v021_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log ncfcommon
def eic_f033_equity_issuance_cash_log_126d_accel_v022_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log ncfcommon
def eic_f033_equity_issuance_cash_log_126d_accel_v023_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log ncfcommon
def eic_f033_equity_issuance_cash_log_126d_accel_v024_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log ncfcommon
def eic_f033_equity_issuance_cash_log_252d_accel_v025_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log ncfcommon
def eic_f033_equity_issuance_cash_log_252d_accel_v026_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log ncfcommon
def eic_f033_equity_issuance_cash_log_252d_accel_v027_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log ncfcommon
def eic_f033_equity_issuance_cash_log_504d_accel_v028_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log ncfcommon
def eic_f033_equity_issuance_cash_log_504d_accel_v029_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log ncfcommon
def eic_f033_equity_issuance_cash_log_504d_accel_v030_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_21d_accel_v031_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_21d_accel_v032_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_21d_accel_v033_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_63d_accel_v034_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_63d_accel_v035_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_63d_accel_v036_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_126d_accel_v037_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_126d_accel_v038_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_126d_accel_v039_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_252d_accel_v040_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_252d_accel_v041_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_252d_accel_v042_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_504d_accel_v043_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_504d_accel_v044_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_504d_accel_v045_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_21d_accel_v046_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_21d_accel_v047_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_21d_accel_v048_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_63d_accel_v049_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_63d_accel_v050_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_63d_accel_v051_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_126d_accel_v052_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_126d_accel_v053_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_126d_accel_v054_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_252d_accel_v055_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_252d_accel_v056_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_252d_accel_v057_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_504d_accel_v058_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_504d_accel_v059_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_504d_accel_v060_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_21d_accel_v061_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_21d_accel_v062_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_21d_accel_v063_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_63d_accel_v064_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_63d_accel_v065_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_63d_accel_v066_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_126d_accel_v067_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_126d_accel_v068_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_126d_accel_v069_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_252d_accel_v070_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_252d_accel_v071_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_252d_accel_v072_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_504d_accel_v073_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_504d_accel_v074_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_504d_accel_v075_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_21d_accel_v076_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_21d_accel_v077_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_21d_accel_v078_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_63d_accel_v079_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_63d_accel_v080_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_63d_accel_v081_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_126d_accel_v082_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_126d_accel_v083_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_126d_accel_v084_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_252d_accel_v085_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_252d_accel_v086_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_252d_accel_v087_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_504d_accel_v088_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_504d_accel_v089_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_504d_accel_v090_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std ncfcommon
def eic_f033_equity_issuance_cash_std_21d_accel_v091_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std ncfcommon
def eic_f033_equity_issuance_cash_std_21d_accel_v092_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std ncfcommon
def eic_f033_equity_issuance_cash_std_21d_accel_v093_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std ncfcommon
def eic_f033_equity_issuance_cash_std_63d_accel_v094_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std ncfcommon
def eic_f033_equity_issuance_cash_std_63d_accel_v095_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std ncfcommon
def eic_f033_equity_issuance_cash_std_63d_accel_v096_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std ncfcommon
def eic_f033_equity_issuance_cash_std_126d_accel_v097_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std ncfcommon
def eic_f033_equity_issuance_cash_std_126d_accel_v098_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std ncfcommon
def eic_f033_equity_issuance_cash_std_126d_accel_v099_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std ncfcommon
def eic_f033_equity_issuance_cash_std_252d_accel_v100_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std ncfcommon
def eic_f033_equity_issuance_cash_std_252d_accel_v101_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std ncfcommon
def eic_f033_equity_issuance_cash_std_252d_accel_v102_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std ncfcommon
def eic_f033_equity_issuance_cash_std_504d_accel_v103_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std ncfcommon
def eic_f033_equity_issuance_cash_std_504d_accel_v104_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std ncfcommon
def eic_f033_equity_issuance_cash_std_504d_accel_v105_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_21d_accel_v106_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_21d_accel_v107_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_21d_accel_v108_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_63d_accel_v109_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_63d_accel_v110_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_63d_accel_v111_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_126d_accel_v112_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_126d_accel_v113_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_126d_accel_v114_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_252d_accel_v115_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_252d_accel_v116_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_252d_accel_v117_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_504d_accel_v118_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_504d_accel_v119_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_504d_accel_v120_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_21d_accel_v121_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_21d_accel_v122_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_21d_accel_v123_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_63d_accel_v124_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_63d_accel_v125_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_63d_accel_v126_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_126d_accel_v127_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_126d_accel_v128_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_126d_accel_v129_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_252d_accel_v130_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_252d_accel_v131_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_252d_accel_v132_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_504d_accel_v133_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_504d_accel_v134_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_504d_accel_v135_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z ncfcommon
def eic_f033_equity_issuance_cash_z_21d_accel_v136_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z ncfcommon
def eic_f033_equity_issuance_cash_z_21d_accel_v137_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z ncfcommon
def eic_f033_equity_issuance_cash_z_21d_accel_v138_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z ncfcommon
def eic_f033_equity_issuance_cash_z_63d_accel_v139_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z ncfcommon
def eic_f033_equity_issuance_cash_z_63d_accel_v140_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z ncfcommon
def eic_f033_equity_issuance_cash_z_63d_accel_v141_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z ncfcommon
def eic_f033_equity_issuance_cash_z_126d_accel_v142_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z ncfcommon
def eic_f033_equity_issuance_cash_z_126d_accel_v143_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z ncfcommon
def eic_f033_equity_issuance_cash_z_126d_accel_v144_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z ncfcommon
def eic_f033_equity_issuance_cash_z_252d_accel_v145_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z ncfcommon
def eic_f033_equity_issuance_cash_z_252d_accel_v146_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z ncfcommon
def eic_f033_equity_issuance_cash_z_252d_accel_v147_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z ncfcommon
def eic_f033_equity_issuance_cash_z_504d_accel_v148_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z ncfcommon
def eic_f033_equity_issuance_cash_z_504d_accel_v149_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z ncfcommon
def eic_f033_equity_issuance_cash_z_504d_accel_v150_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
