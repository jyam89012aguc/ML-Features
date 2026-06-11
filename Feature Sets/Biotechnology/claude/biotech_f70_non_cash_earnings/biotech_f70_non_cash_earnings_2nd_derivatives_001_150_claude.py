"""Family f70 - Non-cash share of earnings  (L_EarningsQuality) | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw depamor
def nce_f70_non_cash_earnings_raw_21d_slope_v001_signal(depamor, closeadj):
    base = _mean(depamor, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw depamor
def nce_f70_non_cash_earnings_raw_21d_slope_v002_signal(depamor, closeadj):
    base = _mean(depamor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw depamor
def nce_f70_non_cash_earnings_raw_21d_slope_v003_signal(depamor, closeadj):
    base = _mean(depamor, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw depamor
def nce_f70_non_cash_earnings_raw_63d_slope_v004_signal(depamor, closeadj):
    base = _mean(depamor, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw depamor
def nce_f70_non_cash_earnings_raw_63d_slope_v005_signal(depamor, closeadj):
    base = _mean(depamor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw depamor
def nce_f70_non_cash_earnings_raw_63d_slope_v006_signal(depamor, closeadj):
    base = _mean(depamor, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw depamor
def nce_f70_non_cash_earnings_raw_126d_slope_v007_signal(depamor, closeadj):
    base = _mean(depamor, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw depamor
def nce_f70_non_cash_earnings_raw_126d_slope_v008_signal(depamor, closeadj):
    base = _mean(depamor, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw depamor
def nce_f70_non_cash_earnings_raw_126d_slope_v009_signal(depamor, closeadj):
    base = _mean(depamor, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw depamor
def nce_f70_non_cash_earnings_raw_252d_slope_v010_signal(depamor, closeadj):
    base = _mean(depamor, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw depamor
def nce_f70_non_cash_earnings_raw_252d_slope_v011_signal(depamor, closeadj):
    base = _mean(depamor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw depamor
def nce_f70_non_cash_earnings_raw_252d_slope_v012_signal(depamor, closeadj):
    base = _mean(depamor, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw depamor
def nce_f70_non_cash_earnings_raw_504d_slope_v013_signal(depamor, closeadj):
    base = _mean(depamor, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw depamor
def nce_f70_non_cash_earnings_raw_504d_slope_v014_signal(depamor, closeadj):
    base = _mean(depamor, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw depamor
def nce_f70_non_cash_earnings_raw_504d_slope_v015_signal(depamor, closeadj):
    base = _mean(depamor, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log depamor
def nce_f70_non_cash_earnings_log_21d_slope_v016_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log depamor
def nce_f70_non_cash_earnings_log_21d_slope_v017_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log depamor
def nce_f70_non_cash_earnings_log_21d_slope_v018_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log depamor
def nce_f70_non_cash_earnings_log_63d_slope_v019_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log depamor
def nce_f70_non_cash_earnings_log_63d_slope_v020_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log depamor
def nce_f70_non_cash_earnings_log_63d_slope_v021_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log depamor
def nce_f70_non_cash_earnings_log_126d_slope_v022_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log depamor
def nce_f70_non_cash_earnings_log_126d_slope_v023_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log depamor
def nce_f70_non_cash_earnings_log_126d_slope_v024_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log depamor
def nce_f70_non_cash_earnings_log_252d_slope_v025_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log depamor
def nce_f70_non_cash_earnings_log_252d_slope_v026_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log depamor
def nce_f70_non_cash_earnings_log_252d_slope_v027_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log depamor
def nce_f70_non_cash_earnings_log_504d_slope_v028_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log depamor
def nce_f70_non_cash_earnings_log_504d_slope_v029_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log depamor
def nce_f70_non_cash_earnings_log_504d_slope_v030_signal(depamor, closeadj):
    base = _mean(_non_cash_earnings_log(depamor), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare depamor
def nce_f70_non_cash_earnings_pershare_21d_slope_v031_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare depamor
def nce_f70_non_cash_earnings_pershare_21d_slope_v032_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare depamor
def nce_f70_non_cash_earnings_pershare_21d_slope_v033_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare depamor
def nce_f70_non_cash_earnings_pershare_63d_slope_v034_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare depamor
def nce_f70_non_cash_earnings_pershare_63d_slope_v035_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare depamor
def nce_f70_non_cash_earnings_pershare_63d_slope_v036_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare depamor
def nce_f70_non_cash_earnings_pershare_126d_slope_v037_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare depamor
def nce_f70_non_cash_earnings_pershare_126d_slope_v038_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare depamor
def nce_f70_non_cash_earnings_pershare_126d_slope_v039_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare depamor
def nce_f70_non_cash_earnings_pershare_252d_slope_v040_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare depamor
def nce_f70_non_cash_earnings_pershare_252d_slope_v041_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare depamor
def nce_f70_non_cash_earnings_pershare_252d_slope_v042_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare depamor
def nce_f70_non_cash_earnings_pershare_504d_slope_v043_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare depamor
def nce_f70_non_cash_earnings_pershare_504d_slope_v044_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare depamor
def nce_f70_non_cash_earnings_pershare_504d_slope_v045_signal(depamor, sharesbas, closeadj):
    base = _mean(_non_cash_earnings_per_share(depamor, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_21d_slope_v046_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_21d_slope_v047_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_21d_slope_v048_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_63d_slope_v049_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_63d_slope_v050_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_63d_slope_v051_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_126d_slope_v052_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_126d_slope_v053_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_126d_slope_v054_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_252d_slope_v055_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_252d_slope_v056_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_252d_slope_v057_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_504d_slope_v058_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_504d_slope_v059_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets depamor
def nce_f70_non_cash_earnings_per_assets_504d_slope_v060_signal(depamor, assets):
    base = _mean(_non_cash_earnings_scaled(depamor, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_21d_slope_v061_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_21d_slope_v062_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_21d_slope_v063_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_63d_slope_v064_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_63d_slope_v065_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_63d_slope_v066_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_126d_slope_v067_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_126d_slope_v068_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_126d_slope_v069_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_252d_slope_v070_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_252d_slope_v071_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_252d_slope_v072_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_504d_slope_v073_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_504d_slope_v074_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap depamor
def nce_f70_non_cash_earnings_per_marketcap_504d_slope_v075_signal(depamor, marketcap):
    base = _mean(_non_cash_earnings_scaled(depamor, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_21d_slope_v076_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_21d_slope_v077_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_21d_slope_v078_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_63d_slope_v079_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_63d_slope_v080_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_63d_slope_v081_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_126d_slope_v082_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_126d_slope_v083_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_126d_slope_v084_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_252d_slope_v085_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_252d_slope_v086_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_252d_slope_v087_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_504d_slope_v088_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_504d_slope_v089_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity depamor
def nce_f70_non_cash_earnings_per_equity_504d_slope_v090_signal(depamor, equity):
    base = _mean(_non_cash_earnings_scaled(depamor, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std depamor
def nce_f70_non_cash_earnings_std_21d_slope_v091_signal(depamor, closeadj):
    base = _std(depamor, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std depamor
def nce_f70_non_cash_earnings_std_21d_slope_v092_signal(depamor, closeadj):
    base = _std(depamor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std depamor
def nce_f70_non_cash_earnings_std_21d_slope_v093_signal(depamor, closeadj):
    base = _std(depamor, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std depamor
def nce_f70_non_cash_earnings_std_63d_slope_v094_signal(depamor, closeadj):
    base = _std(depamor, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std depamor
def nce_f70_non_cash_earnings_std_63d_slope_v095_signal(depamor, closeadj):
    base = _std(depamor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std depamor
def nce_f70_non_cash_earnings_std_63d_slope_v096_signal(depamor, closeadj):
    base = _std(depamor, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std depamor
def nce_f70_non_cash_earnings_std_126d_slope_v097_signal(depamor, closeadj):
    base = _std(depamor, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std depamor
def nce_f70_non_cash_earnings_std_126d_slope_v098_signal(depamor, closeadj):
    base = _std(depamor, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std depamor
def nce_f70_non_cash_earnings_std_126d_slope_v099_signal(depamor, closeadj):
    base = _std(depamor, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std depamor
def nce_f70_non_cash_earnings_std_252d_slope_v100_signal(depamor, closeadj):
    base = _std(depamor, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std depamor
def nce_f70_non_cash_earnings_std_252d_slope_v101_signal(depamor, closeadj):
    base = _std(depamor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std depamor
def nce_f70_non_cash_earnings_std_252d_slope_v102_signal(depamor, closeadj):
    base = _std(depamor, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std depamor
def nce_f70_non_cash_earnings_std_504d_slope_v103_signal(depamor, closeadj):
    base = _std(depamor, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std depamor
def nce_f70_non_cash_earnings_std_504d_slope_v104_signal(depamor, closeadj):
    base = _std(depamor, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std depamor
def nce_f70_non_cash_earnings_std_504d_slope_v105_signal(depamor, closeadj):
    base = _std(depamor, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm depamor
def nce_f70_non_cash_earnings_ewm_21d_slope_v106_signal(depamor, closeadj):
    base = depamor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm depamor
def nce_f70_non_cash_earnings_ewm_21d_slope_v107_signal(depamor, closeadj):
    base = depamor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm depamor
def nce_f70_non_cash_earnings_ewm_21d_slope_v108_signal(depamor, closeadj):
    base = depamor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm depamor
def nce_f70_non_cash_earnings_ewm_63d_slope_v109_signal(depamor, closeadj):
    base = depamor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm depamor
def nce_f70_non_cash_earnings_ewm_63d_slope_v110_signal(depamor, closeadj):
    base = depamor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm depamor
def nce_f70_non_cash_earnings_ewm_63d_slope_v111_signal(depamor, closeadj):
    base = depamor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm depamor
def nce_f70_non_cash_earnings_ewm_126d_slope_v112_signal(depamor, closeadj):
    base = depamor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm depamor
def nce_f70_non_cash_earnings_ewm_126d_slope_v113_signal(depamor, closeadj):
    base = depamor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm depamor
def nce_f70_non_cash_earnings_ewm_126d_slope_v114_signal(depamor, closeadj):
    base = depamor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm depamor
def nce_f70_non_cash_earnings_ewm_252d_slope_v115_signal(depamor, closeadj):
    base = depamor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm depamor
def nce_f70_non_cash_earnings_ewm_252d_slope_v116_signal(depamor, closeadj):
    base = depamor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm depamor
def nce_f70_non_cash_earnings_ewm_252d_slope_v117_signal(depamor, closeadj):
    base = depamor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm depamor
def nce_f70_non_cash_earnings_ewm_504d_slope_v118_signal(depamor, closeadj):
    base = depamor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm depamor
def nce_f70_non_cash_earnings_ewm_504d_slope_v119_signal(depamor, closeadj):
    base = depamor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm depamor
def nce_f70_non_cash_earnings_ewm_504d_slope_v120_signal(depamor, closeadj):
    base = depamor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq depamor
def nce_f70_non_cash_earnings_sq_21d_slope_v121_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq depamor
def nce_f70_non_cash_earnings_sq_21d_slope_v122_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq depamor
def nce_f70_non_cash_earnings_sq_21d_slope_v123_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq depamor
def nce_f70_non_cash_earnings_sq_63d_slope_v124_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq depamor
def nce_f70_non_cash_earnings_sq_63d_slope_v125_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq depamor
def nce_f70_non_cash_earnings_sq_63d_slope_v126_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq depamor
def nce_f70_non_cash_earnings_sq_126d_slope_v127_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq depamor
def nce_f70_non_cash_earnings_sq_126d_slope_v128_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq depamor
def nce_f70_non_cash_earnings_sq_126d_slope_v129_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq depamor
def nce_f70_non_cash_earnings_sq_252d_slope_v130_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq depamor
def nce_f70_non_cash_earnings_sq_252d_slope_v131_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq depamor
def nce_f70_non_cash_earnings_sq_252d_slope_v132_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq depamor
def nce_f70_non_cash_earnings_sq_504d_slope_v133_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq depamor
def nce_f70_non_cash_earnings_sq_504d_slope_v134_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq depamor
def nce_f70_non_cash_earnings_sq_504d_slope_v135_signal(depamor, closeadj):
    base = _mean(depamor * depamor, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z depamor
def nce_f70_non_cash_earnings_z_21d_slope_v136_signal(depamor):
    base = _z(depamor, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z depamor
def nce_f70_non_cash_earnings_z_21d_slope_v137_signal(depamor):
    base = _z(depamor, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z depamor
def nce_f70_non_cash_earnings_z_21d_slope_v138_signal(depamor):
    base = _z(depamor, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z depamor
def nce_f70_non_cash_earnings_z_63d_slope_v139_signal(depamor):
    base = _z(depamor, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z depamor
def nce_f70_non_cash_earnings_z_63d_slope_v140_signal(depamor):
    base = _z(depamor, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z depamor
def nce_f70_non_cash_earnings_z_63d_slope_v141_signal(depamor):
    base = _z(depamor, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z depamor
def nce_f70_non_cash_earnings_z_126d_slope_v142_signal(depamor):
    base = _z(depamor, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z depamor
def nce_f70_non_cash_earnings_z_126d_slope_v143_signal(depamor):
    base = _z(depamor, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z depamor
def nce_f70_non_cash_earnings_z_126d_slope_v144_signal(depamor):
    base = _z(depamor, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z depamor
def nce_f70_non_cash_earnings_z_252d_slope_v145_signal(depamor):
    base = _z(depamor, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z depamor
def nce_f70_non_cash_earnings_z_252d_slope_v146_signal(depamor):
    base = _z(depamor, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z depamor
def nce_f70_non_cash_earnings_z_252d_slope_v147_signal(depamor):
    base = _z(depamor, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z depamor
def nce_f70_non_cash_earnings_z_504d_slope_v148_signal(depamor):
    base = _z(depamor, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z depamor
def nce_f70_non_cash_earnings_z_504d_slope_v149_signal(depamor):
    base = _z(depamor, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z depamor
def nce_f70_non_cash_earnings_z_504d_slope_v150_signal(depamor):
    base = _z(depamor, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
