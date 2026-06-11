"""Family f074 - Dividend and payout valuation (Valuation Multiples) | Sharadar tables: SF1 | fields: dps, ncfdiv, payoutratio, value | 3rd derivatives 001-150"""
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
def _dividend_and_payout_valuation_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _dividend_and_payout_valuation_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _dividend_and_payout_valuation_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_21d_accel_v001_signal(dps, closeadj):
    base = _mean(dps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_21d_accel_v002_signal(dps, closeadj):
    base = _mean(dps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_21d_accel_v003_signal(dps, closeadj):
    base = _mean(dps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_63d_accel_v004_signal(dps, closeadj):
    base = _mean(dps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_63d_accel_v005_signal(dps, closeadj):
    base = _mean(dps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_63d_accel_v006_signal(dps, closeadj):
    base = _mean(dps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_126d_accel_v007_signal(dps, closeadj):
    base = _mean(dps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_126d_accel_v008_signal(dps, closeadj):
    base = _mean(dps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_126d_accel_v009_signal(dps, closeadj):
    base = _mean(dps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_252d_accel_v010_signal(dps, closeadj):
    base = _mean(dps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_252d_accel_v011_signal(dps, closeadj):
    base = _mean(dps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_252d_accel_v012_signal(dps, closeadj):
    base = _mean(dps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_504d_accel_v013_signal(dps, closeadj):
    base = _mean(dps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_504d_accel_v014_signal(dps, closeadj):
    base = _mean(dps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_504d_accel_v015_signal(dps, closeadj):
    base = _mean(dps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log dps
def dpv_f074_dividend_and_payout_valuation_log_21d_accel_v016_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log dps
def dpv_f074_dividend_and_payout_valuation_log_21d_accel_v017_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log dps
def dpv_f074_dividend_and_payout_valuation_log_21d_accel_v018_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log dps
def dpv_f074_dividend_and_payout_valuation_log_63d_accel_v019_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log dps
def dpv_f074_dividend_and_payout_valuation_log_63d_accel_v020_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log dps
def dpv_f074_dividend_and_payout_valuation_log_63d_accel_v021_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log dps
def dpv_f074_dividend_and_payout_valuation_log_126d_accel_v022_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log dps
def dpv_f074_dividend_and_payout_valuation_log_126d_accel_v023_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log dps
def dpv_f074_dividend_and_payout_valuation_log_126d_accel_v024_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log dps
def dpv_f074_dividend_and_payout_valuation_log_252d_accel_v025_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log dps
def dpv_f074_dividend_and_payout_valuation_log_252d_accel_v026_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log dps
def dpv_f074_dividend_and_payout_valuation_log_252d_accel_v027_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log dps
def dpv_f074_dividend_and_payout_valuation_log_504d_accel_v028_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log dps
def dpv_f074_dividend_and_payout_valuation_log_504d_accel_v029_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log dps
def dpv_f074_dividend_and_payout_valuation_log_504d_accel_v030_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_21d_accel_v031_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_21d_accel_v032_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_21d_accel_v033_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_63d_accel_v034_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_63d_accel_v035_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_63d_accel_v036_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_126d_accel_v037_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_126d_accel_v038_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_126d_accel_v039_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_252d_accel_v040_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_252d_accel_v041_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_252d_accel_v042_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_504d_accel_v043_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_504d_accel_v044_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_504d_accel_v045_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_21d_accel_v046_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_21d_accel_v047_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_21d_accel_v048_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_63d_accel_v049_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_63d_accel_v050_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_63d_accel_v051_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_126d_accel_v052_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_126d_accel_v053_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_126d_accel_v054_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_252d_accel_v055_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_252d_accel_v056_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_252d_accel_v057_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_504d_accel_v058_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_504d_accel_v059_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_504d_accel_v060_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_21d_accel_v061_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_21d_accel_v062_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_21d_accel_v063_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_63d_accel_v064_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_63d_accel_v065_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_63d_accel_v066_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_126d_accel_v067_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_126d_accel_v068_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_126d_accel_v069_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_252d_accel_v070_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_252d_accel_v071_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_252d_accel_v072_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_504d_accel_v073_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_504d_accel_v074_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_504d_accel_v075_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_21d_accel_v076_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_21d_accel_v077_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_21d_accel_v078_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_63d_accel_v079_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_63d_accel_v080_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_63d_accel_v081_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_126d_accel_v082_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_126d_accel_v083_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_126d_accel_v084_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_252d_accel_v085_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_252d_accel_v086_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_252d_accel_v087_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_504d_accel_v088_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_504d_accel_v089_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_504d_accel_v090_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std dps
def dpv_f074_dividend_and_payout_valuation_std_21d_accel_v091_signal(dps, closeadj):
    base = _std(dps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std dps
def dpv_f074_dividend_and_payout_valuation_std_21d_accel_v092_signal(dps, closeadj):
    base = _std(dps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std dps
def dpv_f074_dividend_and_payout_valuation_std_21d_accel_v093_signal(dps, closeadj):
    base = _std(dps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std dps
def dpv_f074_dividend_and_payout_valuation_std_63d_accel_v094_signal(dps, closeadj):
    base = _std(dps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std dps
def dpv_f074_dividend_and_payout_valuation_std_63d_accel_v095_signal(dps, closeadj):
    base = _std(dps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std dps
def dpv_f074_dividend_and_payout_valuation_std_63d_accel_v096_signal(dps, closeadj):
    base = _std(dps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std dps
def dpv_f074_dividend_and_payout_valuation_std_126d_accel_v097_signal(dps, closeadj):
    base = _std(dps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std dps
def dpv_f074_dividend_and_payout_valuation_std_126d_accel_v098_signal(dps, closeadj):
    base = _std(dps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std dps
def dpv_f074_dividend_and_payout_valuation_std_126d_accel_v099_signal(dps, closeadj):
    base = _std(dps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std dps
def dpv_f074_dividend_and_payout_valuation_std_252d_accel_v100_signal(dps, closeadj):
    base = _std(dps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std dps
def dpv_f074_dividend_and_payout_valuation_std_252d_accel_v101_signal(dps, closeadj):
    base = _std(dps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std dps
def dpv_f074_dividend_and_payout_valuation_std_252d_accel_v102_signal(dps, closeadj):
    base = _std(dps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std dps
def dpv_f074_dividend_and_payout_valuation_std_504d_accel_v103_signal(dps, closeadj):
    base = _std(dps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std dps
def dpv_f074_dividend_and_payout_valuation_std_504d_accel_v104_signal(dps, closeadj):
    base = _std(dps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std dps
def dpv_f074_dividend_and_payout_valuation_std_504d_accel_v105_signal(dps, closeadj):
    base = _std(dps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_21d_accel_v106_signal(dps, closeadj):
    base = dps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_21d_accel_v107_signal(dps, closeadj):
    base = dps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_21d_accel_v108_signal(dps, closeadj):
    base = dps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_63d_accel_v109_signal(dps, closeadj):
    base = dps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_63d_accel_v110_signal(dps, closeadj):
    base = dps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_63d_accel_v111_signal(dps, closeadj):
    base = dps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_126d_accel_v112_signal(dps, closeadj):
    base = dps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_126d_accel_v113_signal(dps, closeadj):
    base = dps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_126d_accel_v114_signal(dps, closeadj):
    base = dps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_252d_accel_v115_signal(dps, closeadj):
    base = dps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_252d_accel_v116_signal(dps, closeadj):
    base = dps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_252d_accel_v117_signal(dps, closeadj):
    base = dps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_504d_accel_v118_signal(dps, closeadj):
    base = dps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_504d_accel_v119_signal(dps, closeadj):
    base = dps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_504d_accel_v120_signal(dps, closeadj):
    base = dps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_21d_accel_v121_signal(dps, closeadj):
    base = _mean(dps * dps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_21d_accel_v122_signal(dps, closeadj):
    base = _mean(dps * dps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_21d_accel_v123_signal(dps, closeadj):
    base = _mean(dps * dps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_63d_accel_v124_signal(dps, closeadj):
    base = _mean(dps * dps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_63d_accel_v125_signal(dps, closeadj):
    base = _mean(dps * dps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_63d_accel_v126_signal(dps, closeadj):
    base = _mean(dps * dps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_126d_accel_v127_signal(dps, closeadj):
    base = _mean(dps * dps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_126d_accel_v128_signal(dps, closeadj):
    base = _mean(dps * dps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_126d_accel_v129_signal(dps, closeadj):
    base = _mean(dps * dps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_252d_accel_v130_signal(dps, closeadj):
    base = _mean(dps * dps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_252d_accel_v131_signal(dps, closeadj):
    base = _mean(dps * dps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_252d_accel_v132_signal(dps, closeadj):
    base = _mean(dps * dps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_504d_accel_v133_signal(dps, closeadj):
    base = _mean(dps * dps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_504d_accel_v134_signal(dps, closeadj):
    base = _mean(dps * dps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_504d_accel_v135_signal(dps, closeadj):
    base = _mean(dps * dps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z dps
def dpv_f074_dividend_and_payout_valuation_z_21d_accel_v136_signal(dps):
    base = _z(dps, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z dps
def dpv_f074_dividend_and_payout_valuation_z_21d_accel_v137_signal(dps):
    base = _z(dps, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z dps
def dpv_f074_dividend_and_payout_valuation_z_21d_accel_v138_signal(dps):
    base = _z(dps, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z dps
def dpv_f074_dividend_and_payout_valuation_z_63d_accel_v139_signal(dps):
    base = _z(dps, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z dps
def dpv_f074_dividend_and_payout_valuation_z_63d_accel_v140_signal(dps):
    base = _z(dps, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z dps
def dpv_f074_dividend_and_payout_valuation_z_63d_accel_v141_signal(dps):
    base = _z(dps, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z dps
def dpv_f074_dividend_and_payout_valuation_z_126d_accel_v142_signal(dps):
    base = _z(dps, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z dps
def dpv_f074_dividend_and_payout_valuation_z_126d_accel_v143_signal(dps):
    base = _z(dps, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z dps
def dpv_f074_dividend_and_payout_valuation_z_126d_accel_v144_signal(dps):
    base = _z(dps, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z dps
def dpv_f074_dividend_and_payout_valuation_z_252d_accel_v145_signal(dps):
    base = _z(dps, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z dps
def dpv_f074_dividend_and_payout_valuation_z_252d_accel_v146_signal(dps):
    base = _z(dps, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z dps
def dpv_f074_dividend_and_payout_valuation_z_252d_accel_v147_signal(dps):
    base = _z(dps, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z dps
def dpv_f074_dividend_and_payout_valuation_z_504d_accel_v148_signal(dps):
    base = _z(dps, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z dps
def dpv_f074_dividend_and_payout_valuation_z_504d_accel_v149_signal(dps):
    base = _z(dps, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z dps
def dpv_f074_dividend_and_payout_valuation_z_504d_accel_v150_signal(dps):
    base = _z(dps, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
