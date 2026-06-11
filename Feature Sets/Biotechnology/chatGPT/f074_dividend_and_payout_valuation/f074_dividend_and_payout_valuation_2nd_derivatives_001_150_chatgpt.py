"""Family f074 - Dividend and payout valuation (Valuation Multiples) | Sharadar tables: SF1 | fields: dps, ncfdiv, payoutratio, value | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_21d_slope_v001_signal(dps, closeadj):
    base = _mean(dps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_21d_slope_v002_signal(dps, closeadj):
    base = _mean(dps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_21d_slope_v003_signal(dps, closeadj):
    base = _mean(dps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_63d_slope_v004_signal(dps, closeadj):
    base = _mean(dps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_63d_slope_v005_signal(dps, closeadj):
    base = _mean(dps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_63d_slope_v006_signal(dps, closeadj):
    base = _mean(dps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_126d_slope_v007_signal(dps, closeadj):
    base = _mean(dps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_126d_slope_v008_signal(dps, closeadj):
    base = _mean(dps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_126d_slope_v009_signal(dps, closeadj):
    base = _mean(dps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_252d_slope_v010_signal(dps, closeadj):
    base = _mean(dps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_252d_slope_v011_signal(dps, closeadj):
    base = _mean(dps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_252d_slope_v012_signal(dps, closeadj):
    base = _mean(dps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_504d_slope_v013_signal(dps, closeadj):
    base = _mean(dps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_504d_slope_v014_signal(dps, closeadj):
    base = _mean(dps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw dps
def dpv_f074_dividend_and_payout_valuation_raw_504d_slope_v015_signal(dps, closeadj):
    base = _mean(dps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log dps
def dpv_f074_dividend_and_payout_valuation_log_21d_slope_v016_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log dps
def dpv_f074_dividend_and_payout_valuation_log_21d_slope_v017_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log dps
def dpv_f074_dividend_and_payout_valuation_log_21d_slope_v018_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log dps
def dpv_f074_dividend_and_payout_valuation_log_63d_slope_v019_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log dps
def dpv_f074_dividend_and_payout_valuation_log_63d_slope_v020_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log dps
def dpv_f074_dividend_and_payout_valuation_log_63d_slope_v021_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log dps
def dpv_f074_dividend_and_payout_valuation_log_126d_slope_v022_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log dps
def dpv_f074_dividend_and_payout_valuation_log_126d_slope_v023_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log dps
def dpv_f074_dividend_and_payout_valuation_log_126d_slope_v024_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log dps
def dpv_f074_dividend_and_payout_valuation_log_252d_slope_v025_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log dps
def dpv_f074_dividend_and_payout_valuation_log_252d_slope_v026_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log dps
def dpv_f074_dividend_and_payout_valuation_log_252d_slope_v027_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log dps
def dpv_f074_dividend_and_payout_valuation_log_504d_slope_v028_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log dps
def dpv_f074_dividend_and_payout_valuation_log_504d_slope_v029_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log dps
def dpv_f074_dividend_and_payout_valuation_log_504d_slope_v030_signal(dps, closeadj):
    base = _mean(_dividend_and_payout_valuation_log(dps), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_21d_slope_v031_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_21d_slope_v032_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_21d_slope_v033_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_63d_slope_v034_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_63d_slope_v035_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_63d_slope_v036_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_126d_slope_v037_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_126d_slope_v038_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_126d_slope_v039_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_252d_slope_v040_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_252d_slope_v041_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_252d_slope_v042_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_504d_slope_v043_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_504d_slope_v044_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare dps
def dpv_f074_dividend_and_payout_valuation_pershare_504d_slope_v045_signal(dps, sharesbas, closeadj):
    base = _mean(_dividend_and_payout_valuation_per_share(dps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_21d_slope_v046_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_21d_slope_v047_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_21d_slope_v048_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_63d_slope_v049_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_63d_slope_v050_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_63d_slope_v051_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_126d_slope_v052_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_126d_slope_v053_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_126d_slope_v054_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_252d_slope_v055_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_252d_slope_v056_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_252d_slope_v057_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_504d_slope_v058_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_504d_slope_v059_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_ncfdiv dps
def dpv_f074_dividend_and_payout_valuation_per_ncfdiv_504d_slope_v060_signal(dps, ncfdiv):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, ncfdiv), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_21d_slope_v061_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_21d_slope_v062_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_21d_slope_v063_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_63d_slope_v064_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_63d_slope_v065_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_63d_slope_v066_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_126d_slope_v067_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_126d_slope_v068_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_126d_slope_v069_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_252d_slope_v070_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_252d_slope_v071_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_252d_slope_v072_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_504d_slope_v073_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_504d_slope_v074_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_payoutratio dps
def dpv_f074_dividend_and_payout_valuation_per_payoutratio_504d_slope_v075_signal(dps, payoutratio):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, payoutratio), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_21d_slope_v076_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_21d_slope_v077_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_21d_slope_v078_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_63d_slope_v079_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_63d_slope_v080_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_63d_slope_v081_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_126d_slope_v082_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_126d_slope_v083_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_126d_slope_v084_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_252d_slope_v085_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_252d_slope_v086_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_252d_slope_v087_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_504d_slope_v088_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_504d_slope_v089_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_value dps
def dpv_f074_dividend_and_payout_valuation_per_value_504d_slope_v090_signal(dps, value):
    base = _mean(_dividend_and_payout_valuation_scaled(dps, value), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std dps
def dpv_f074_dividend_and_payout_valuation_std_21d_slope_v091_signal(dps, closeadj):
    base = _std(dps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std dps
def dpv_f074_dividend_and_payout_valuation_std_21d_slope_v092_signal(dps, closeadj):
    base = _std(dps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std dps
def dpv_f074_dividend_and_payout_valuation_std_21d_slope_v093_signal(dps, closeadj):
    base = _std(dps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std dps
def dpv_f074_dividend_and_payout_valuation_std_63d_slope_v094_signal(dps, closeadj):
    base = _std(dps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std dps
def dpv_f074_dividend_and_payout_valuation_std_63d_slope_v095_signal(dps, closeadj):
    base = _std(dps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std dps
def dpv_f074_dividend_and_payout_valuation_std_63d_slope_v096_signal(dps, closeadj):
    base = _std(dps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std dps
def dpv_f074_dividend_and_payout_valuation_std_126d_slope_v097_signal(dps, closeadj):
    base = _std(dps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std dps
def dpv_f074_dividend_and_payout_valuation_std_126d_slope_v098_signal(dps, closeadj):
    base = _std(dps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std dps
def dpv_f074_dividend_and_payout_valuation_std_126d_slope_v099_signal(dps, closeadj):
    base = _std(dps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std dps
def dpv_f074_dividend_and_payout_valuation_std_252d_slope_v100_signal(dps, closeadj):
    base = _std(dps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std dps
def dpv_f074_dividend_and_payout_valuation_std_252d_slope_v101_signal(dps, closeadj):
    base = _std(dps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std dps
def dpv_f074_dividend_and_payout_valuation_std_252d_slope_v102_signal(dps, closeadj):
    base = _std(dps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std dps
def dpv_f074_dividend_and_payout_valuation_std_504d_slope_v103_signal(dps, closeadj):
    base = _std(dps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std dps
def dpv_f074_dividend_and_payout_valuation_std_504d_slope_v104_signal(dps, closeadj):
    base = _std(dps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std dps
def dpv_f074_dividend_and_payout_valuation_std_504d_slope_v105_signal(dps, closeadj):
    base = _std(dps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_21d_slope_v106_signal(dps, closeadj):
    base = dps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_21d_slope_v107_signal(dps, closeadj):
    base = dps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_21d_slope_v108_signal(dps, closeadj):
    base = dps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_63d_slope_v109_signal(dps, closeadj):
    base = dps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_63d_slope_v110_signal(dps, closeadj):
    base = dps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_63d_slope_v111_signal(dps, closeadj):
    base = dps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_126d_slope_v112_signal(dps, closeadj):
    base = dps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_126d_slope_v113_signal(dps, closeadj):
    base = dps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_126d_slope_v114_signal(dps, closeadj):
    base = dps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_252d_slope_v115_signal(dps, closeadj):
    base = dps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_252d_slope_v116_signal(dps, closeadj):
    base = dps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_252d_slope_v117_signal(dps, closeadj):
    base = dps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_504d_slope_v118_signal(dps, closeadj):
    base = dps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_504d_slope_v119_signal(dps, closeadj):
    base = dps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm dps
def dpv_f074_dividend_and_payout_valuation_ewm_504d_slope_v120_signal(dps, closeadj):
    base = dps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_21d_slope_v121_signal(dps, closeadj):
    base = _mean(dps * dps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_21d_slope_v122_signal(dps, closeadj):
    base = _mean(dps * dps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_21d_slope_v123_signal(dps, closeadj):
    base = _mean(dps * dps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_63d_slope_v124_signal(dps, closeadj):
    base = _mean(dps * dps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_63d_slope_v125_signal(dps, closeadj):
    base = _mean(dps * dps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_63d_slope_v126_signal(dps, closeadj):
    base = _mean(dps * dps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_126d_slope_v127_signal(dps, closeadj):
    base = _mean(dps * dps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_126d_slope_v128_signal(dps, closeadj):
    base = _mean(dps * dps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_126d_slope_v129_signal(dps, closeadj):
    base = _mean(dps * dps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_252d_slope_v130_signal(dps, closeadj):
    base = _mean(dps * dps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_252d_slope_v131_signal(dps, closeadj):
    base = _mean(dps * dps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_252d_slope_v132_signal(dps, closeadj):
    base = _mean(dps * dps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_504d_slope_v133_signal(dps, closeadj):
    base = _mean(dps * dps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_504d_slope_v134_signal(dps, closeadj):
    base = _mean(dps * dps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq dps
def dpv_f074_dividend_and_payout_valuation_sq_504d_slope_v135_signal(dps, closeadj):
    base = _mean(dps * dps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z dps
def dpv_f074_dividend_and_payout_valuation_z_21d_slope_v136_signal(dps):
    base = _z(dps, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z dps
def dpv_f074_dividend_and_payout_valuation_z_21d_slope_v137_signal(dps):
    base = _z(dps, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z dps
def dpv_f074_dividend_and_payout_valuation_z_21d_slope_v138_signal(dps):
    base = _z(dps, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z dps
def dpv_f074_dividend_and_payout_valuation_z_63d_slope_v139_signal(dps):
    base = _z(dps, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z dps
def dpv_f074_dividend_and_payout_valuation_z_63d_slope_v140_signal(dps):
    base = _z(dps, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z dps
def dpv_f074_dividend_and_payout_valuation_z_63d_slope_v141_signal(dps):
    base = _z(dps, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z dps
def dpv_f074_dividend_and_payout_valuation_z_126d_slope_v142_signal(dps):
    base = _z(dps, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z dps
def dpv_f074_dividend_and_payout_valuation_z_126d_slope_v143_signal(dps):
    base = _z(dps, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z dps
def dpv_f074_dividend_and_payout_valuation_z_126d_slope_v144_signal(dps):
    base = _z(dps, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z dps
def dpv_f074_dividend_and_payout_valuation_z_252d_slope_v145_signal(dps):
    base = _z(dps, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z dps
def dpv_f074_dividend_and_payout_valuation_z_252d_slope_v146_signal(dps):
    base = _z(dps, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z dps
def dpv_f074_dividend_and_payout_valuation_z_252d_slope_v147_signal(dps):
    base = _z(dps, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z dps
def dpv_f074_dividend_and_payout_valuation_z_504d_slope_v148_signal(dps):
    base = _z(dps, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z dps
def dpv_f074_dividend_and_payout_valuation_z_504d_slope_v149_signal(dps):
    base = _z(dps, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z dps
def dpv_f074_dividend_and_payout_valuation_z_504d_slope_v150_signal(dps):
    base = _z(dps, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
