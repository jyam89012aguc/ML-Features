"""Family f058 - Comprehensive income versus net income (Earnings and Quality) | Sharadar tables: SF1 | fields: consolinc, netinc, equity | 2nd derivatives 001-150"""
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
def _comprehensive_income_gap_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _comprehensive_income_gap_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _comprehensive_income_gap_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw consolinc
def cig_f058_comprehensive_income_gap_raw_21d_slope_v001_signal(consolinc, closeadj):
    base = _mean(consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw consolinc
def cig_f058_comprehensive_income_gap_raw_21d_slope_v002_signal(consolinc, closeadj):
    base = _mean(consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw consolinc
def cig_f058_comprehensive_income_gap_raw_21d_slope_v003_signal(consolinc, closeadj):
    base = _mean(consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw consolinc
def cig_f058_comprehensive_income_gap_raw_63d_slope_v004_signal(consolinc, closeadj):
    base = _mean(consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw consolinc
def cig_f058_comprehensive_income_gap_raw_63d_slope_v005_signal(consolinc, closeadj):
    base = _mean(consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw consolinc
def cig_f058_comprehensive_income_gap_raw_63d_slope_v006_signal(consolinc, closeadj):
    base = _mean(consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw consolinc
def cig_f058_comprehensive_income_gap_raw_126d_slope_v007_signal(consolinc, closeadj):
    base = _mean(consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw consolinc
def cig_f058_comprehensive_income_gap_raw_126d_slope_v008_signal(consolinc, closeadj):
    base = _mean(consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw consolinc
def cig_f058_comprehensive_income_gap_raw_126d_slope_v009_signal(consolinc, closeadj):
    base = _mean(consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw consolinc
def cig_f058_comprehensive_income_gap_raw_252d_slope_v010_signal(consolinc, closeadj):
    base = _mean(consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw consolinc
def cig_f058_comprehensive_income_gap_raw_252d_slope_v011_signal(consolinc, closeadj):
    base = _mean(consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw consolinc
def cig_f058_comprehensive_income_gap_raw_252d_slope_v012_signal(consolinc, closeadj):
    base = _mean(consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw consolinc
def cig_f058_comprehensive_income_gap_raw_504d_slope_v013_signal(consolinc, closeadj):
    base = _mean(consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw consolinc
def cig_f058_comprehensive_income_gap_raw_504d_slope_v014_signal(consolinc, closeadj):
    base = _mean(consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw consolinc
def cig_f058_comprehensive_income_gap_raw_504d_slope_v015_signal(consolinc, closeadj):
    base = _mean(consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log consolinc
def cig_f058_comprehensive_income_gap_log_21d_slope_v016_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log consolinc
def cig_f058_comprehensive_income_gap_log_21d_slope_v017_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log consolinc
def cig_f058_comprehensive_income_gap_log_21d_slope_v018_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log consolinc
def cig_f058_comprehensive_income_gap_log_63d_slope_v019_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log consolinc
def cig_f058_comprehensive_income_gap_log_63d_slope_v020_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log consolinc
def cig_f058_comprehensive_income_gap_log_63d_slope_v021_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log consolinc
def cig_f058_comprehensive_income_gap_log_126d_slope_v022_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log consolinc
def cig_f058_comprehensive_income_gap_log_126d_slope_v023_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log consolinc
def cig_f058_comprehensive_income_gap_log_126d_slope_v024_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log consolinc
def cig_f058_comprehensive_income_gap_log_252d_slope_v025_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log consolinc
def cig_f058_comprehensive_income_gap_log_252d_slope_v026_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log consolinc
def cig_f058_comprehensive_income_gap_log_252d_slope_v027_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log consolinc
def cig_f058_comprehensive_income_gap_log_504d_slope_v028_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log consolinc
def cig_f058_comprehensive_income_gap_log_504d_slope_v029_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log consolinc
def cig_f058_comprehensive_income_gap_log_504d_slope_v030_signal(consolinc, closeadj):
    base = _mean(_comprehensive_income_gap_log(consolinc), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_21d_slope_v031_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_21d_slope_v032_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_21d_slope_v033_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_63d_slope_v034_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_63d_slope_v035_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_63d_slope_v036_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_126d_slope_v037_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_126d_slope_v038_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_126d_slope_v039_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_252d_slope_v040_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_252d_slope_v041_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_252d_slope_v042_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_504d_slope_v043_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_504d_slope_v044_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare consolinc
def cig_f058_comprehensive_income_gap_pershare_504d_slope_v045_signal(consolinc, sharesbas, closeadj):
    base = _mean(_comprehensive_income_gap_per_share(consolinc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_21d_slope_v046_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_21d_slope_v047_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_21d_slope_v048_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_63d_slope_v049_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_63d_slope_v050_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_63d_slope_v051_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_126d_slope_v052_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_126d_slope_v053_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_126d_slope_v054_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_252d_slope_v055_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_252d_slope_v056_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_252d_slope_v057_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_504d_slope_v058_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_504d_slope_v059_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_netinc consolinc
def cig_f058_comprehensive_income_gap_per_netinc_504d_slope_v060_signal(consolinc, netinc):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, netinc), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_21d_slope_v061_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_21d_slope_v062_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_21d_slope_v063_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_63d_slope_v064_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_63d_slope_v065_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_63d_slope_v066_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_126d_slope_v067_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_126d_slope_v068_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_126d_slope_v069_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_252d_slope_v070_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_252d_slope_v071_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_252d_slope_v072_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_504d_slope_v073_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_504d_slope_v074_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity consolinc
def cig_f058_comprehensive_income_gap_per_equity_504d_slope_v075_signal(consolinc, equity):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_21d_slope_v076_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_21d_slope_v077_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_21d_slope_v078_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_63d_slope_v079_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_63d_slope_v080_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_63d_slope_v081_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_126d_slope_v082_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_126d_slope_v083_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_126d_slope_v084_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_252d_slope_v085_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_252d_slope_v086_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_252d_slope_v087_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_504d_slope_v088_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_504d_slope_v089_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets consolinc
def cig_f058_comprehensive_income_gap_per_assets_504d_slope_v090_signal(consolinc, assets):
    base = _mean(_comprehensive_income_gap_scaled(consolinc, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std consolinc
def cig_f058_comprehensive_income_gap_std_21d_slope_v091_signal(consolinc, closeadj):
    base = _std(consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std consolinc
def cig_f058_comprehensive_income_gap_std_21d_slope_v092_signal(consolinc, closeadj):
    base = _std(consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std consolinc
def cig_f058_comprehensive_income_gap_std_21d_slope_v093_signal(consolinc, closeadj):
    base = _std(consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std consolinc
def cig_f058_comprehensive_income_gap_std_63d_slope_v094_signal(consolinc, closeadj):
    base = _std(consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std consolinc
def cig_f058_comprehensive_income_gap_std_63d_slope_v095_signal(consolinc, closeadj):
    base = _std(consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std consolinc
def cig_f058_comprehensive_income_gap_std_63d_slope_v096_signal(consolinc, closeadj):
    base = _std(consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std consolinc
def cig_f058_comprehensive_income_gap_std_126d_slope_v097_signal(consolinc, closeadj):
    base = _std(consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std consolinc
def cig_f058_comprehensive_income_gap_std_126d_slope_v098_signal(consolinc, closeadj):
    base = _std(consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std consolinc
def cig_f058_comprehensive_income_gap_std_126d_slope_v099_signal(consolinc, closeadj):
    base = _std(consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std consolinc
def cig_f058_comprehensive_income_gap_std_252d_slope_v100_signal(consolinc, closeadj):
    base = _std(consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std consolinc
def cig_f058_comprehensive_income_gap_std_252d_slope_v101_signal(consolinc, closeadj):
    base = _std(consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std consolinc
def cig_f058_comprehensive_income_gap_std_252d_slope_v102_signal(consolinc, closeadj):
    base = _std(consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std consolinc
def cig_f058_comprehensive_income_gap_std_504d_slope_v103_signal(consolinc, closeadj):
    base = _std(consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std consolinc
def cig_f058_comprehensive_income_gap_std_504d_slope_v104_signal(consolinc, closeadj):
    base = _std(consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std consolinc
def cig_f058_comprehensive_income_gap_std_504d_slope_v105_signal(consolinc, closeadj):
    base = _std(consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_21d_slope_v106_signal(consolinc, closeadj):
    base = consolinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_21d_slope_v107_signal(consolinc, closeadj):
    base = consolinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_21d_slope_v108_signal(consolinc, closeadj):
    base = consolinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_63d_slope_v109_signal(consolinc, closeadj):
    base = consolinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_63d_slope_v110_signal(consolinc, closeadj):
    base = consolinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_63d_slope_v111_signal(consolinc, closeadj):
    base = consolinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_126d_slope_v112_signal(consolinc, closeadj):
    base = consolinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_126d_slope_v113_signal(consolinc, closeadj):
    base = consolinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_126d_slope_v114_signal(consolinc, closeadj):
    base = consolinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_252d_slope_v115_signal(consolinc, closeadj):
    base = consolinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_252d_slope_v116_signal(consolinc, closeadj):
    base = consolinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_252d_slope_v117_signal(consolinc, closeadj):
    base = consolinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_504d_slope_v118_signal(consolinc, closeadj):
    base = consolinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_504d_slope_v119_signal(consolinc, closeadj):
    base = consolinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm consolinc
def cig_f058_comprehensive_income_gap_ewm_504d_slope_v120_signal(consolinc, closeadj):
    base = consolinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq consolinc
def cig_f058_comprehensive_income_gap_sq_21d_slope_v121_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq consolinc
def cig_f058_comprehensive_income_gap_sq_21d_slope_v122_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq consolinc
def cig_f058_comprehensive_income_gap_sq_21d_slope_v123_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq consolinc
def cig_f058_comprehensive_income_gap_sq_63d_slope_v124_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq consolinc
def cig_f058_comprehensive_income_gap_sq_63d_slope_v125_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq consolinc
def cig_f058_comprehensive_income_gap_sq_63d_slope_v126_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq consolinc
def cig_f058_comprehensive_income_gap_sq_126d_slope_v127_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq consolinc
def cig_f058_comprehensive_income_gap_sq_126d_slope_v128_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq consolinc
def cig_f058_comprehensive_income_gap_sq_126d_slope_v129_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq consolinc
def cig_f058_comprehensive_income_gap_sq_252d_slope_v130_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq consolinc
def cig_f058_comprehensive_income_gap_sq_252d_slope_v131_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq consolinc
def cig_f058_comprehensive_income_gap_sq_252d_slope_v132_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq consolinc
def cig_f058_comprehensive_income_gap_sq_504d_slope_v133_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq consolinc
def cig_f058_comprehensive_income_gap_sq_504d_slope_v134_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq consolinc
def cig_f058_comprehensive_income_gap_sq_504d_slope_v135_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z consolinc
def cig_f058_comprehensive_income_gap_z_21d_slope_v136_signal(consolinc):
    base = _z(consolinc, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z consolinc
def cig_f058_comprehensive_income_gap_z_21d_slope_v137_signal(consolinc):
    base = _z(consolinc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z consolinc
def cig_f058_comprehensive_income_gap_z_21d_slope_v138_signal(consolinc):
    base = _z(consolinc, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z consolinc
def cig_f058_comprehensive_income_gap_z_63d_slope_v139_signal(consolinc):
    base = _z(consolinc, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z consolinc
def cig_f058_comprehensive_income_gap_z_63d_slope_v140_signal(consolinc):
    base = _z(consolinc, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z consolinc
def cig_f058_comprehensive_income_gap_z_63d_slope_v141_signal(consolinc):
    base = _z(consolinc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z consolinc
def cig_f058_comprehensive_income_gap_z_126d_slope_v142_signal(consolinc):
    base = _z(consolinc, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z consolinc
def cig_f058_comprehensive_income_gap_z_126d_slope_v143_signal(consolinc):
    base = _z(consolinc, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z consolinc
def cig_f058_comprehensive_income_gap_z_126d_slope_v144_signal(consolinc):
    base = _z(consolinc, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z consolinc
def cig_f058_comprehensive_income_gap_z_252d_slope_v145_signal(consolinc):
    base = _z(consolinc, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z consolinc
def cig_f058_comprehensive_income_gap_z_252d_slope_v146_signal(consolinc):
    base = _z(consolinc, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z consolinc
def cig_f058_comprehensive_income_gap_z_252d_slope_v147_signal(consolinc):
    base = _z(consolinc, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z consolinc
def cig_f058_comprehensive_income_gap_z_504d_slope_v148_signal(consolinc):
    base = _z(consolinc, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z consolinc
def cig_f058_comprehensive_income_gap_z_504d_slope_v149_signal(consolinc):
    base = _z(consolinc, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z consolinc
def cig_f058_comprehensive_income_gap_z_504d_slope_v150_signal(consolinc):
    base = _z(consolinc, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
