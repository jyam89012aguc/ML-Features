"""Family f70 - Non-cash share of earnings  (L_EarningsQuality) | 3rd derivatives 001-150"""
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
def _non_cash_earnings_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _non_cash_earnings_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _non_cash_earnings_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw depamor
def nce_f70_non_cash_earnings_raw_21d_accel_v001_signal(depamor, closeadj):
    base = _mean(depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw depamor
def nce_f70_non_cash_earnings_raw_21d_accel_v002_signal(depamor, closeadj):
    base = _mean(depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw depamor
def nce_f70_non_cash_earnings_raw_21d_accel_v003_signal(depamor, closeadj):
    base = _mean(depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw depamor
def nce_f70_non_cash_earnings_raw_63d_accel_v004_signal(depamor, closeadj):
    base = _mean(depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw depamor
def nce_f70_non_cash_earnings_raw_63d_accel_v005_signal(depamor, closeadj):
    base = _mean(depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw depamor
def nce_f70_non_cash_earnings_raw_63d_accel_v006_signal(depamor, closeadj):
    base = _mean(depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw depamor
def nce_f70_non_cash_earnings_raw_126d_accel_v007_signal(depamor, closeadj):
    base = _mean(depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw depamor
def nce_f70_non_cash_earnings_raw_126d_accel_v008_signal(depamor, closeadj):
    base = _mean(depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw depamor
def nce_f70_non_cash_earnings_raw_126d_accel_v009_signal(depamor, closeadj):
    base = _mean(depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw depamor
def nce_f70_non_cash_earnings_raw_252d_accel_v010_signal(depamor, closeadj):
    base = _mean(depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw depamor
def nce_f70_non_cash_earnings_raw_252d_accel_v011_signal(depamor, closeadj):
    base = _mean(depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw depamor
def nce_f70_non_cash_earnings_raw_252d_accel_v012_signal(depamor, closeadj):
    base = _mean(depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw depamor
def nce_f70_non_cash_earnings_raw_504d_accel_v013_signal(depamor, closeadj):
    base = _mean(depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw depamor
def nce_f70_non_cash_earnings_raw_504d_accel_v014_signal(depamor, closeadj):
    base = _mean(depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw depamor
def nce_f70_non_cash_earnings_raw_504d_accel_v015_signal(depamor, closeadj):
    base = _mean(depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log depamor
def nce_f70_non_cash_earnings_log_21d_accel_v016_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log depamor
def nce_f70_non_cash_earnings_log_21d_accel_v017_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log depamor
def nce_f70_non_cash_earnings_log_21d_accel_v018_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log depamor
def nce_f70_non_cash_earnings_log_63d_accel_v019_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log depamor
def nce_f70_non_cash_earnings_log_63d_accel_v020_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log depamor
def nce_f70_non_cash_earnings_log_63d_accel_v021_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log depamor
def nce_f70_non_cash_earnings_log_126d_accel_v022_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log depamor
def nce_f70_non_cash_earnings_log_126d_accel_v023_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log depamor
def nce_f70_non_cash_earnings_log_126d_accel_v024_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log depamor
def nce_f70_non_cash_earnings_log_252d_accel_v025_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log depamor
def nce_f70_non_cash_earnings_log_252d_accel_v026_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log depamor
def nce_f70_non_cash_earnings_log_252d_accel_v027_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log depamor
def nce_f70_non_cash_earnings_log_504d_accel_v028_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log depamor
def nce_f70_non_cash_earnings_log_504d_accel_v029_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log depamor
def nce_f70_non_cash_earnings_log_504d_accel_v030_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare depamor
def nce_f70_non_cash_earnings_pershare_21d_accel_v031_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare depamor
def nce_f70_non_cash_earnings_pershare_21d_accel_v032_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare depamor
def nce_f70_non_cash_earnings_pershare_21d_accel_v033_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare depamor
def nce_f70_non_cash_earnings_pershare_63d_accel_v034_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare depamor
def nce_f70_non_cash_earnings_pershare_63d_accel_v035_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare depamor
def nce_f70_non_cash_earnings_pershare_63d_accel_v036_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare depamor
def nce_f70_non_cash_earnings_pershare_126d_accel_v037_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare depamor
def nce_f70_non_cash_earnings_pershare_126d_accel_v038_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare depamor
def nce_f70_non_cash_earnings_pershare_126d_accel_v039_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare depamor
def nce_f70_non_cash_earnings_pershare_252d_accel_v040_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare depamor
def nce_f70_non_cash_earnings_pershare_252d_accel_v041_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare depamor
def nce_f70_non_cash_earnings_pershare_252d_accel_v042_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare depamor
def nce_f70_non_cash_earnings_pershare_504d_accel_v043_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare depamor
def nce_f70_non_cash_earnings_pershare_504d_accel_v044_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare depamor
def nce_f70_non_cash_earnings_pershare_504d_accel_v045_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_21d_accel_v046_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_21d_accel_v047_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_21d_accel_v048_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_63d_accel_v049_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_63d_accel_v050_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_63d_accel_v051_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_126d_accel_v052_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_126d_accel_v053_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_126d_accel_v054_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_252d_accel_v055_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_252d_accel_v056_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_252d_accel_v057_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_504d_accel_v058_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_504d_accel_v059_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_504d_accel_v060_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_21d_accel_v061_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_21d_accel_v062_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_21d_accel_v063_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_63d_accel_v064_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_63d_accel_v065_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_63d_accel_v066_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_126d_accel_v067_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_126d_accel_v068_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_126d_accel_v069_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_252d_accel_v070_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_252d_accel_v071_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_252d_accel_v072_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_504d_accel_v073_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_504d_accel_v074_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_504d_accel_v075_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_21d_accel_v076_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_21d_accel_v077_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_21d_accel_v078_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_63d_accel_v079_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_63d_accel_v080_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_63d_accel_v081_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_126d_accel_v082_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_126d_accel_v083_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_126d_accel_v084_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_252d_accel_v085_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_252d_accel_v086_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_252d_accel_v087_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_504d_accel_v088_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_504d_accel_v089_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_504d_accel_v090_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std depamor
def nce_f70_non_cash_earnings_std_21d_accel_v091_signal(depamor, closeadj):
    base = _std(depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std depamor
def nce_f70_non_cash_earnings_std_21d_accel_v092_signal(depamor, closeadj):
    base = _std(depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std depamor
def nce_f70_non_cash_earnings_std_21d_accel_v093_signal(depamor, closeadj):
    base = _std(depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std depamor
def nce_f70_non_cash_earnings_std_63d_accel_v094_signal(depamor, closeadj):
    base = _std(depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std depamor
def nce_f70_non_cash_earnings_std_63d_accel_v095_signal(depamor, closeadj):
    base = _std(depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std depamor
def nce_f70_non_cash_earnings_std_63d_accel_v096_signal(depamor, closeadj):
    base = _std(depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std depamor
def nce_f70_non_cash_earnings_std_126d_accel_v097_signal(depamor, closeadj):
    base = _std(depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std depamor
def nce_f70_non_cash_earnings_std_126d_accel_v098_signal(depamor, closeadj):
    base = _std(depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std depamor
def nce_f70_non_cash_earnings_std_126d_accel_v099_signal(depamor, closeadj):
    base = _std(depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std depamor
def nce_f70_non_cash_earnings_std_252d_accel_v100_signal(depamor, closeadj):
    base = _std(depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std depamor
def nce_f70_non_cash_earnings_std_252d_accel_v101_signal(depamor, closeadj):
    base = _std(depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std depamor
def nce_f70_non_cash_earnings_std_252d_accel_v102_signal(depamor, closeadj):
    base = _std(depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std depamor
def nce_f70_non_cash_earnings_std_504d_accel_v103_signal(depamor, closeadj):
    base = _std(depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std depamor
def nce_f70_non_cash_earnings_std_504d_accel_v104_signal(depamor, closeadj):
    base = _std(depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std depamor
def nce_f70_non_cash_earnings_std_504d_accel_v105_signal(depamor, closeadj):
    base = _std(depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm depamor
def nce_f70_non_cash_earnings_ewm_21d_accel_v106_signal(depamor, closeadj):
    base = depamor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm depamor
def nce_f70_non_cash_earnings_ewm_21d_accel_v107_signal(depamor, closeadj):
    base = depamor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm depamor
def nce_f70_non_cash_earnings_ewm_21d_accel_v108_signal(depamor, closeadj):
    base = depamor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm depamor
def nce_f70_non_cash_earnings_ewm_63d_accel_v109_signal(depamor, closeadj):
    base = depamor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm depamor
def nce_f70_non_cash_earnings_ewm_63d_accel_v110_signal(depamor, closeadj):
    base = depamor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm depamor
def nce_f70_non_cash_earnings_ewm_63d_accel_v111_signal(depamor, closeadj):
    base = depamor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm depamor
def nce_f70_non_cash_earnings_ewm_126d_accel_v112_signal(depamor, closeadj):
    base = depamor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm depamor
def nce_f70_non_cash_earnings_ewm_126d_accel_v113_signal(depamor, closeadj):
    base = depamor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm depamor
def nce_f70_non_cash_earnings_ewm_126d_accel_v114_signal(depamor, closeadj):
    base = depamor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm depamor
def nce_f70_non_cash_earnings_ewm_252d_accel_v115_signal(depamor, closeadj):
    base = depamor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm depamor
def nce_f70_non_cash_earnings_ewm_252d_accel_v116_signal(depamor, closeadj):
    base = depamor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm depamor
def nce_f70_non_cash_earnings_ewm_252d_accel_v117_signal(depamor, closeadj):
    base = depamor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm depamor
def nce_f70_non_cash_earnings_ewm_504d_accel_v118_signal(depamor, closeadj):
    base = depamor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm depamor
def nce_f70_non_cash_earnings_ewm_504d_accel_v119_signal(depamor, closeadj):
    base = depamor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm depamor
def nce_f70_non_cash_earnings_ewm_504d_accel_v120_signal(depamor, closeadj):
    base = depamor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq depamor
def nce_f70_non_cash_earnings_sq_21d_accel_v121_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq depamor
def nce_f70_non_cash_earnings_sq_21d_accel_v122_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq depamor
def nce_f70_non_cash_earnings_sq_21d_accel_v123_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq depamor
def nce_f70_non_cash_earnings_sq_63d_accel_v124_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq depamor
def nce_f70_non_cash_earnings_sq_63d_accel_v125_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq depamor
def nce_f70_non_cash_earnings_sq_63d_accel_v126_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq depamor
def nce_f70_non_cash_earnings_sq_126d_accel_v127_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq depamor
def nce_f70_non_cash_earnings_sq_126d_accel_v128_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq depamor
def nce_f70_non_cash_earnings_sq_126d_accel_v129_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq depamor
def nce_f70_non_cash_earnings_sq_252d_accel_v130_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq depamor
def nce_f70_non_cash_earnings_sq_252d_accel_v131_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq depamor
def nce_f70_non_cash_earnings_sq_252d_accel_v132_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq depamor
def nce_f70_non_cash_earnings_sq_504d_accel_v133_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq depamor
def nce_f70_non_cash_earnings_sq_504d_accel_v134_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq depamor
def nce_f70_non_cash_earnings_sq_504d_accel_v135_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z depamor
def nce_f70_non_cash_earnings_z_21d_accel_v136_signal(depamor):
    base = _z(depamor, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z depamor
def nce_f70_non_cash_earnings_z_21d_accel_v137_signal(depamor):
    base = _z(depamor, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z depamor
def nce_f70_non_cash_earnings_z_21d_accel_v138_signal(depamor):
    base = _z(depamor, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z depamor
def nce_f70_non_cash_earnings_z_63d_accel_v139_signal(depamor):
    base = _z(depamor, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z depamor
def nce_f70_non_cash_earnings_z_63d_accel_v140_signal(depamor):
    base = _z(depamor, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z depamor
def nce_f70_non_cash_earnings_z_63d_accel_v141_signal(depamor):
    base = _z(depamor, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z depamor
def nce_f70_non_cash_earnings_z_126d_accel_v142_signal(depamor):
    base = _z(depamor, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z depamor
def nce_f70_non_cash_earnings_z_126d_accel_v143_signal(depamor):
    base = _z(depamor, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z depamor
def nce_f70_non_cash_earnings_z_126d_accel_v144_signal(depamor):
    base = _z(depamor, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z depamor
def nce_f70_non_cash_earnings_z_252d_accel_v145_signal(depamor):
    base = _z(depamor, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z depamor
def nce_f70_non_cash_earnings_z_252d_accel_v146_signal(depamor):
    base = _z(depamor, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z depamor
def nce_f70_non_cash_earnings_z_252d_accel_v147_signal(depamor):
    base = _z(depamor, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z depamor
def nce_f70_non_cash_earnings_z_504d_accel_v148_signal(depamor):
    base = _z(depamor, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z depamor
def nce_f70_non_cash_earnings_z_504d_accel_v149_signal(depamor):
    base = _z(depamor, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z depamor
def nce_f70_non_cash_earnings_z_504d_accel_v150_signal(depamor):
    base = _z(depamor, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
