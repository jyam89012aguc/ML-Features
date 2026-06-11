"""Family f045 - Payables and accrued liabilities (Balance Sheet Composition) | Sharadar tables: SF1 | fields: payables, liabilitiesc, opex | 2nd derivatives 001-150"""
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
def _payables_and_accruals_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _payables_and_accruals_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _payables_and_accruals_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw payables
def paa_f045_payables_and_accruals_raw_21d_slope_v001_signal(payables, closeadj):
    base = _mean(payables, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw payables
def paa_f045_payables_and_accruals_raw_21d_slope_v002_signal(payables, closeadj):
    base = _mean(payables, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw payables
def paa_f045_payables_and_accruals_raw_21d_slope_v003_signal(payables, closeadj):
    base = _mean(payables, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw payables
def paa_f045_payables_and_accruals_raw_63d_slope_v004_signal(payables, closeadj):
    base = _mean(payables, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw payables
def paa_f045_payables_and_accruals_raw_63d_slope_v005_signal(payables, closeadj):
    base = _mean(payables, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw payables
def paa_f045_payables_and_accruals_raw_63d_slope_v006_signal(payables, closeadj):
    base = _mean(payables, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw payables
def paa_f045_payables_and_accruals_raw_126d_slope_v007_signal(payables, closeadj):
    base = _mean(payables, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw payables
def paa_f045_payables_and_accruals_raw_126d_slope_v008_signal(payables, closeadj):
    base = _mean(payables, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw payables
def paa_f045_payables_and_accruals_raw_126d_slope_v009_signal(payables, closeadj):
    base = _mean(payables, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw payables
def paa_f045_payables_and_accruals_raw_252d_slope_v010_signal(payables, closeadj):
    base = _mean(payables, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw payables
def paa_f045_payables_and_accruals_raw_252d_slope_v011_signal(payables, closeadj):
    base = _mean(payables, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw payables
def paa_f045_payables_and_accruals_raw_252d_slope_v012_signal(payables, closeadj):
    base = _mean(payables, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw payables
def paa_f045_payables_and_accruals_raw_504d_slope_v013_signal(payables, closeadj):
    base = _mean(payables, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw payables
def paa_f045_payables_and_accruals_raw_504d_slope_v014_signal(payables, closeadj):
    base = _mean(payables, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw payables
def paa_f045_payables_and_accruals_raw_504d_slope_v015_signal(payables, closeadj):
    base = _mean(payables, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log payables
def paa_f045_payables_and_accruals_log_21d_slope_v016_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log payables
def paa_f045_payables_and_accruals_log_21d_slope_v017_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log payables
def paa_f045_payables_and_accruals_log_21d_slope_v018_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log payables
def paa_f045_payables_and_accruals_log_63d_slope_v019_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log payables
def paa_f045_payables_and_accruals_log_63d_slope_v020_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log payables
def paa_f045_payables_and_accruals_log_63d_slope_v021_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log payables
def paa_f045_payables_and_accruals_log_126d_slope_v022_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log payables
def paa_f045_payables_and_accruals_log_126d_slope_v023_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log payables
def paa_f045_payables_and_accruals_log_126d_slope_v024_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log payables
def paa_f045_payables_and_accruals_log_252d_slope_v025_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log payables
def paa_f045_payables_and_accruals_log_252d_slope_v026_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log payables
def paa_f045_payables_and_accruals_log_252d_slope_v027_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log payables
def paa_f045_payables_and_accruals_log_504d_slope_v028_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log payables
def paa_f045_payables_and_accruals_log_504d_slope_v029_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log payables
def paa_f045_payables_and_accruals_log_504d_slope_v030_signal(payables, closeadj):
    base = _mean(_payables_and_accruals_log(payables), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare payables
def paa_f045_payables_and_accruals_pershare_21d_slope_v031_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare payables
def paa_f045_payables_and_accruals_pershare_21d_slope_v032_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare payables
def paa_f045_payables_and_accruals_pershare_21d_slope_v033_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare payables
def paa_f045_payables_and_accruals_pershare_63d_slope_v034_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare payables
def paa_f045_payables_and_accruals_pershare_63d_slope_v035_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare payables
def paa_f045_payables_and_accruals_pershare_63d_slope_v036_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare payables
def paa_f045_payables_and_accruals_pershare_126d_slope_v037_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare payables
def paa_f045_payables_and_accruals_pershare_126d_slope_v038_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare payables
def paa_f045_payables_and_accruals_pershare_126d_slope_v039_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare payables
def paa_f045_payables_and_accruals_pershare_252d_slope_v040_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare payables
def paa_f045_payables_and_accruals_pershare_252d_slope_v041_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare payables
def paa_f045_payables_and_accruals_pershare_252d_slope_v042_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare payables
def paa_f045_payables_and_accruals_pershare_504d_slope_v043_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare payables
def paa_f045_payables_and_accruals_pershare_504d_slope_v044_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare payables
def paa_f045_payables_and_accruals_pershare_504d_slope_v045_signal(payables, sharesbas, closeadj):
    base = _mean(_payables_and_accruals_per_share(payables, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_21d_slope_v046_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_21d_slope_v047_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_21d_slope_v048_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_63d_slope_v049_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_63d_slope_v050_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_63d_slope_v051_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_126d_slope_v052_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_126d_slope_v053_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_126d_slope_v054_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_252d_slope_v055_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_252d_slope_v056_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_252d_slope_v057_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_504d_slope_v058_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_504d_slope_v059_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_liabilitiesc payables
def paa_f045_payables_and_accruals_per_liabilitiesc_504d_slope_v060_signal(payables, liabilitiesc):
    base = _mean(_payables_and_accruals_scaled(payables, liabilitiesc), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets payables
def paa_f045_payables_and_accruals_per_assets_21d_slope_v061_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets payables
def paa_f045_payables_and_accruals_per_assets_21d_slope_v062_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets payables
def paa_f045_payables_and_accruals_per_assets_21d_slope_v063_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets payables
def paa_f045_payables_and_accruals_per_assets_63d_slope_v064_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets payables
def paa_f045_payables_and_accruals_per_assets_63d_slope_v065_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets payables
def paa_f045_payables_and_accruals_per_assets_63d_slope_v066_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets payables
def paa_f045_payables_and_accruals_per_assets_126d_slope_v067_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets payables
def paa_f045_payables_and_accruals_per_assets_126d_slope_v068_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets payables
def paa_f045_payables_and_accruals_per_assets_126d_slope_v069_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets payables
def paa_f045_payables_and_accruals_per_assets_252d_slope_v070_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets payables
def paa_f045_payables_and_accruals_per_assets_252d_slope_v071_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets payables
def paa_f045_payables_and_accruals_per_assets_252d_slope_v072_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets payables
def paa_f045_payables_and_accruals_per_assets_504d_slope_v073_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets payables
def paa_f045_payables_and_accruals_per_assets_504d_slope_v074_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets payables
def paa_f045_payables_and_accruals_per_assets_504d_slope_v075_signal(payables, assets):
    base = _mean(_payables_and_accruals_scaled(payables, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_21d_slope_v076_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_21d_slope_v077_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_21d_slope_v078_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_63d_slope_v079_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_63d_slope_v080_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_63d_slope_v081_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_126d_slope_v082_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_126d_slope_v083_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_126d_slope_v084_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_252d_slope_v085_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_252d_slope_v086_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_252d_slope_v087_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_504d_slope_v088_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_504d_slope_v089_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap payables
def paa_f045_payables_and_accruals_per_marketcap_504d_slope_v090_signal(payables, marketcap):
    base = _mean(_payables_and_accruals_scaled(payables, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std payables
def paa_f045_payables_and_accruals_std_21d_slope_v091_signal(payables, closeadj):
    base = _std(payables, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std payables
def paa_f045_payables_and_accruals_std_21d_slope_v092_signal(payables, closeadj):
    base = _std(payables, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std payables
def paa_f045_payables_and_accruals_std_21d_slope_v093_signal(payables, closeadj):
    base = _std(payables, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std payables
def paa_f045_payables_and_accruals_std_63d_slope_v094_signal(payables, closeadj):
    base = _std(payables, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std payables
def paa_f045_payables_and_accruals_std_63d_slope_v095_signal(payables, closeadj):
    base = _std(payables, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std payables
def paa_f045_payables_and_accruals_std_63d_slope_v096_signal(payables, closeadj):
    base = _std(payables, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std payables
def paa_f045_payables_and_accruals_std_126d_slope_v097_signal(payables, closeadj):
    base = _std(payables, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std payables
def paa_f045_payables_and_accruals_std_126d_slope_v098_signal(payables, closeadj):
    base = _std(payables, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std payables
def paa_f045_payables_and_accruals_std_126d_slope_v099_signal(payables, closeadj):
    base = _std(payables, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std payables
def paa_f045_payables_and_accruals_std_252d_slope_v100_signal(payables, closeadj):
    base = _std(payables, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std payables
def paa_f045_payables_and_accruals_std_252d_slope_v101_signal(payables, closeadj):
    base = _std(payables, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std payables
def paa_f045_payables_and_accruals_std_252d_slope_v102_signal(payables, closeadj):
    base = _std(payables, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std payables
def paa_f045_payables_and_accruals_std_504d_slope_v103_signal(payables, closeadj):
    base = _std(payables, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std payables
def paa_f045_payables_and_accruals_std_504d_slope_v104_signal(payables, closeadj):
    base = _std(payables, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std payables
def paa_f045_payables_and_accruals_std_504d_slope_v105_signal(payables, closeadj):
    base = _std(payables, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm payables
def paa_f045_payables_and_accruals_ewm_21d_slope_v106_signal(payables, closeadj):
    base = payables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm payables
def paa_f045_payables_and_accruals_ewm_21d_slope_v107_signal(payables, closeadj):
    base = payables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm payables
def paa_f045_payables_and_accruals_ewm_21d_slope_v108_signal(payables, closeadj):
    base = payables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm payables
def paa_f045_payables_and_accruals_ewm_63d_slope_v109_signal(payables, closeadj):
    base = payables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm payables
def paa_f045_payables_and_accruals_ewm_63d_slope_v110_signal(payables, closeadj):
    base = payables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm payables
def paa_f045_payables_and_accruals_ewm_63d_slope_v111_signal(payables, closeadj):
    base = payables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm payables
def paa_f045_payables_and_accruals_ewm_126d_slope_v112_signal(payables, closeadj):
    base = payables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm payables
def paa_f045_payables_and_accruals_ewm_126d_slope_v113_signal(payables, closeadj):
    base = payables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm payables
def paa_f045_payables_and_accruals_ewm_126d_slope_v114_signal(payables, closeadj):
    base = payables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm payables
def paa_f045_payables_and_accruals_ewm_252d_slope_v115_signal(payables, closeadj):
    base = payables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm payables
def paa_f045_payables_and_accruals_ewm_252d_slope_v116_signal(payables, closeadj):
    base = payables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm payables
def paa_f045_payables_and_accruals_ewm_252d_slope_v117_signal(payables, closeadj):
    base = payables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm payables
def paa_f045_payables_and_accruals_ewm_504d_slope_v118_signal(payables, closeadj):
    base = payables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm payables
def paa_f045_payables_and_accruals_ewm_504d_slope_v119_signal(payables, closeadj):
    base = payables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm payables
def paa_f045_payables_and_accruals_ewm_504d_slope_v120_signal(payables, closeadj):
    base = payables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq payables
def paa_f045_payables_and_accruals_sq_21d_slope_v121_signal(payables, closeadj):
    base = _mean(payables * payables, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq payables
def paa_f045_payables_and_accruals_sq_21d_slope_v122_signal(payables, closeadj):
    base = _mean(payables * payables, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq payables
def paa_f045_payables_and_accruals_sq_21d_slope_v123_signal(payables, closeadj):
    base = _mean(payables * payables, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq payables
def paa_f045_payables_and_accruals_sq_63d_slope_v124_signal(payables, closeadj):
    base = _mean(payables * payables, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq payables
def paa_f045_payables_and_accruals_sq_63d_slope_v125_signal(payables, closeadj):
    base = _mean(payables * payables, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq payables
def paa_f045_payables_and_accruals_sq_63d_slope_v126_signal(payables, closeadj):
    base = _mean(payables * payables, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq payables
def paa_f045_payables_and_accruals_sq_126d_slope_v127_signal(payables, closeadj):
    base = _mean(payables * payables, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq payables
def paa_f045_payables_and_accruals_sq_126d_slope_v128_signal(payables, closeadj):
    base = _mean(payables * payables, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq payables
def paa_f045_payables_and_accruals_sq_126d_slope_v129_signal(payables, closeadj):
    base = _mean(payables * payables, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq payables
def paa_f045_payables_and_accruals_sq_252d_slope_v130_signal(payables, closeadj):
    base = _mean(payables * payables, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq payables
def paa_f045_payables_and_accruals_sq_252d_slope_v131_signal(payables, closeadj):
    base = _mean(payables * payables, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq payables
def paa_f045_payables_and_accruals_sq_252d_slope_v132_signal(payables, closeadj):
    base = _mean(payables * payables, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq payables
def paa_f045_payables_and_accruals_sq_504d_slope_v133_signal(payables, closeadj):
    base = _mean(payables * payables, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq payables
def paa_f045_payables_and_accruals_sq_504d_slope_v134_signal(payables, closeadj):
    base = _mean(payables * payables, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq payables
def paa_f045_payables_and_accruals_sq_504d_slope_v135_signal(payables, closeadj):
    base = _mean(payables * payables, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z payables
def paa_f045_payables_and_accruals_z_21d_slope_v136_signal(payables):
    base = _z(payables, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z payables
def paa_f045_payables_and_accruals_z_21d_slope_v137_signal(payables):
    base = _z(payables, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z payables
def paa_f045_payables_and_accruals_z_21d_slope_v138_signal(payables):
    base = _z(payables, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z payables
def paa_f045_payables_and_accruals_z_63d_slope_v139_signal(payables):
    base = _z(payables, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z payables
def paa_f045_payables_and_accruals_z_63d_slope_v140_signal(payables):
    base = _z(payables, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z payables
def paa_f045_payables_and_accruals_z_63d_slope_v141_signal(payables):
    base = _z(payables, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z payables
def paa_f045_payables_and_accruals_z_126d_slope_v142_signal(payables):
    base = _z(payables, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z payables
def paa_f045_payables_and_accruals_z_126d_slope_v143_signal(payables):
    base = _z(payables, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z payables
def paa_f045_payables_and_accruals_z_126d_slope_v144_signal(payables):
    base = _z(payables, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z payables
def paa_f045_payables_and_accruals_z_252d_slope_v145_signal(payables):
    base = _z(payables, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z payables
def paa_f045_payables_and_accruals_z_252d_slope_v146_signal(payables):
    base = _z(payables, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z payables
def paa_f045_payables_and_accruals_z_252d_slope_v147_signal(payables):
    base = _z(payables, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z payables
def paa_f045_payables_and_accruals_z_504d_slope_v148_signal(payables):
    base = _z(payables, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z payables
def paa_f045_payables_and_accruals_z_504d_slope_v149_signal(payables):
    base = _z(payables, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z payables
def paa_f045_payables_and_accruals_z_504d_slope_v150_signal(payables):
    base = _z(payables, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
