"""Family f033 - Equity issuance proceeds (Dilution and Share Count) | Sharadar tables: SF1 | fields: ncfcommon, ncff, sharesbas | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_21d_slope_v001_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_21d_slope_v002_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_21d_slope_v003_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_63d_slope_v004_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_63d_slope_v005_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_63d_slope_v006_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_126d_slope_v007_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_126d_slope_v008_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_126d_slope_v009_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_252d_slope_v010_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_252d_slope_v011_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_252d_slope_v012_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_504d_slope_v013_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_504d_slope_v014_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw ncfcommon
def eic_f033_equity_issuance_cash_raw_504d_slope_v015_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log ncfcommon
def eic_f033_equity_issuance_cash_log_21d_slope_v016_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log ncfcommon
def eic_f033_equity_issuance_cash_log_21d_slope_v017_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log ncfcommon
def eic_f033_equity_issuance_cash_log_21d_slope_v018_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log ncfcommon
def eic_f033_equity_issuance_cash_log_63d_slope_v019_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log ncfcommon
def eic_f033_equity_issuance_cash_log_63d_slope_v020_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log ncfcommon
def eic_f033_equity_issuance_cash_log_63d_slope_v021_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log ncfcommon
def eic_f033_equity_issuance_cash_log_126d_slope_v022_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log ncfcommon
def eic_f033_equity_issuance_cash_log_126d_slope_v023_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log ncfcommon
def eic_f033_equity_issuance_cash_log_126d_slope_v024_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log ncfcommon
def eic_f033_equity_issuance_cash_log_252d_slope_v025_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log ncfcommon
def eic_f033_equity_issuance_cash_log_252d_slope_v026_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log ncfcommon
def eic_f033_equity_issuance_cash_log_252d_slope_v027_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log ncfcommon
def eic_f033_equity_issuance_cash_log_504d_slope_v028_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log ncfcommon
def eic_f033_equity_issuance_cash_log_504d_slope_v029_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log ncfcommon
def eic_f033_equity_issuance_cash_log_504d_slope_v030_signal(ncfcommon, closeadj):
    base = _mean(_equity_issuance_cash_log(ncfcommon), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_21d_slope_v031_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_21d_slope_v032_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_21d_slope_v033_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_63d_slope_v034_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_63d_slope_v035_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_63d_slope_v036_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_126d_slope_v037_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_126d_slope_v038_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_126d_slope_v039_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_252d_slope_v040_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_252d_slope_v041_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_252d_slope_v042_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_504d_slope_v043_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_504d_slope_v044_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare ncfcommon
def eic_f033_equity_issuance_cash_pershare_504d_slope_v045_signal(ncfcommon, sharesbas, closeadj):
    base = _mean(_equity_issuance_cash_per_share(ncfcommon, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_21d_slope_v046_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_21d_slope_v047_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_21d_slope_v048_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_63d_slope_v049_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_63d_slope_v050_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_63d_slope_v051_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_126d_slope_v052_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_126d_slope_v053_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_126d_slope_v054_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_252d_slope_v055_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_252d_slope_v056_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_252d_slope_v057_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_504d_slope_v058_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_504d_slope_v059_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_ncff ncfcommon
def eic_f033_equity_issuance_cash_per_ncff_504d_slope_v060_signal(ncfcommon, ncff):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, ncff), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_21d_slope_v061_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_21d_slope_v062_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_21d_slope_v063_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_63d_slope_v064_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_63d_slope_v065_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_63d_slope_v066_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_126d_slope_v067_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_126d_slope_v068_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_126d_slope_v069_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_252d_slope_v070_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_252d_slope_v071_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_252d_slope_v072_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_504d_slope_v073_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_504d_slope_v074_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_sharesbas ncfcommon
def eic_f033_equity_issuance_cash_per_sharesbas_504d_slope_v075_signal(ncfcommon, sharesbas):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, sharesbas), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_21d_slope_v076_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_21d_slope_v077_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_21d_slope_v078_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_63d_slope_v079_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_63d_slope_v080_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_63d_slope_v081_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_126d_slope_v082_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_126d_slope_v083_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_126d_slope_v084_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_252d_slope_v085_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_252d_slope_v086_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_252d_slope_v087_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_504d_slope_v088_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_504d_slope_v089_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets ncfcommon
def eic_f033_equity_issuance_cash_per_assets_504d_slope_v090_signal(ncfcommon, assets):
    base = _mean(_equity_issuance_cash_scaled(ncfcommon, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std ncfcommon
def eic_f033_equity_issuance_cash_std_21d_slope_v091_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std ncfcommon
def eic_f033_equity_issuance_cash_std_21d_slope_v092_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std ncfcommon
def eic_f033_equity_issuance_cash_std_21d_slope_v093_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std ncfcommon
def eic_f033_equity_issuance_cash_std_63d_slope_v094_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std ncfcommon
def eic_f033_equity_issuance_cash_std_63d_slope_v095_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std ncfcommon
def eic_f033_equity_issuance_cash_std_63d_slope_v096_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std ncfcommon
def eic_f033_equity_issuance_cash_std_126d_slope_v097_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std ncfcommon
def eic_f033_equity_issuance_cash_std_126d_slope_v098_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std ncfcommon
def eic_f033_equity_issuance_cash_std_126d_slope_v099_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std ncfcommon
def eic_f033_equity_issuance_cash_std_252d_slope_v100_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std ncfcommon
def eic_f033_equity_issuance_cash_std_252d_slope_v101_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std ncfcommon
def eic_f033_equity_issuance_cash_std_252d_slope_v102_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std ncfcommon
def eic_f033_equity_issuance_cash_std_504d_slope_v103_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std ncfcommon
def eic_f033_equity_issuance_cash_std_504d_slope_v104_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std ncfcommon
def eic_f033_equity_issuance_cash_std_504d_slope_v105_signal(ncfcommon, closeadj):
    base = _std(ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_21d_slope_v106_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_21d_slope_v107_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_21d_slope_v108_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_63d_slope_v109_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_63d_slope_v110_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_63d_slope_v111_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_126d_slope_v112_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_126d_slope_v113_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_126d_slope_v114_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_252d_slope_v115_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_252d_slope_v116_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_252d_slope_v117_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_504d_slope_v118_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_504d_slope_v119_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm ncfcommon
def eic_f033_equity_issuance_cash_ewm_504d_slope_v120_signal(ncfcommon, closeadj):
    base = ncfcommon.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_21d_slope_v121_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_21d_slope_v122_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_21d_slope_v123_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_63d_slope_v124_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_63d_slope_v125_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_63d_slope_v126_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_126d_slope_v127_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_126d_slope_v128_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_126d_slope_v129_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_252d_slope_v130_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_252d_slope_v131_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_252d_slope_v132_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_504d_slope_v133_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_504d_slope_v134_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq ncfcommon
def eic_f033_equity_issuance_cash_sq_504d_slope_v135_signal(ncfcommon, closeadj):
    base = _mean(ncfcommon * ncfcommon, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z ncfcommon
def eic_f033_equity_issuance_cash_z_21d_slope_v136_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z ncfcommon
def eic_f033_equity_issuance_cash_z_21d_slope_v137_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z ncfcommon
def eic_f033_equity_issuance_cash_z_21d_slope_v138_signal(ncfcommon):
    base = _z(ncfcommon, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z ncfcommon
def eic_f033_equity_issuance_cash_z_63d_slope_v139_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z ncfcommon
def eic_f033_equity_issuance_cash_z_63d_slope_v140_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z ncfcommon
def eic_f033_equity_issuance_cash_z_63d_slope_v141_signal(ncfcommon):
    base = _z(ncfcommon, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z ncfcommon
def eic_f033_equity_issuance_cash_z_126d_slope_v142_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z ncfcommon
def eic_f033_equity_issuance_cash_z_126d_slope_v143_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z ncfcommon
def eic_f033_equity_issuance_cash_z_126d_slope_v144_signal(ncfcommon):
    base = _z(ncfcommon, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z ncfcommon
def eic_f033_equity_issuance_cash_z_252d_slope_v145_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z ncfcommon
def eic_f033_equity_issuance_cash_z_252d_slope_v146_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z ncfcommon
def eic_f033_equity_issuance_cash_z_252d_slope_v147_signal(ncfcommon):
    base = _z(ncfcommon, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z ncfcommon
def eic_f033_equity_issuance_cash_z_504d_slope_v148_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z ncfcommon
def eic_f033_equity_issuance_cash_z_504d_slope_v149_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z ncfcommon
def eic_f033_equity_issuance_cash_z_504d_slope_v150_signal(ncfcommon):
    base = _z(ncfcommon, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
