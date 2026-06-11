"""Family f12 - Financing cash flow / capital raised  (B_CashFlow_Burn) | 3rd derivatives 001-150"""
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
def _capital_raised_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capital_raised_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capital_raised_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw ncff
def cap_f12_capital_raised_raw_21d_accel_v001_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw ncff
def cap_f12_capital_raised_raw_21d_accel_v002_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw ncff
def cap_f12_capital_raised_raw_21d_accel_v003_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw ncff
def cap_f12_capital_raised_raw_63d_accel_v004_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw ncff
def cap_f12_capital_raised_raw_63d_accel_v005_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw ncff
def cap_f12_capital_raised_raw_63d_accel_v006_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw ncff
def cap_f12_capital_raised_raw_126d_accel_v007_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw ncff
def cap_f12_capital_raised_raw_126d_accel_v008_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw ncff
def cap_f12_capital_raised_raw_126d_accel_v009_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw ncff
def cap_f12_capital_raised_raw_252d_accel_v010_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw ncff
def cap_f12_capital_raised_raw_252d_accel_v011_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw ncff
def cap_f12_capital_raised_raw_252d_accel_v012_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw ncff
def cap_f12_capital_raised_raw_504d_accel_v013_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw ncff
def cap_f12_capital_raised_raw_504d_accel_v014_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw ncff
def cap_f12_capital_raised_raw_504d_accel_v015_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log ncff
def cap_f12_capital_raised_log_21d_accel_v016_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log ncff
def cap_f12_capital_raised_log_21d_accel_v017_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log ncff
def cap_f12_capital_raised_log_21d_accel_v018_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log ncff
def cap_f12_capital_raised_log_63d_accel_v019_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log ncff
def cap_f12_capital_raised_log_63d_accel_v020_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log ncff
def cap_f12_capital_raised_log_63d_accel_v021_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log ncff
def cap_f12_capital_raised_log_126d_accel_v022_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log ncff
def cap_f12_capital_raised_log_126d_accel_v023_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log ncff
def cap_f12_capital_raised_log_126d_accel_v024_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log ncff
def cap_f12_capital_raised_log_252d_accel_v025_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log ncff
def cap_f12_capital_raised_log_252d_accel_v026_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log ncff
def cap_f12_capital_raised_log_252d_accel_v027_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log ncff
def cap_f12_capital_raised_log_504d_accel_v028_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log ncff
def cap_f12_capital_raised_log_504d_accel_v029_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log ncff
def cap_f12_capital_raised_log_504d_accel_v030_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare ncff
def cap_f12_capital_raised_pershare_21d_accel_v031_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare ncff
def cap_f12_capital_raised_pershare_21d_accel_v032_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare ncff
def cap_f12_capital_raised_pershare_21d_accel_v033_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare ncff
def cap_f12_capital_raised_pershare_63d_accel_v034_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare ncff
def cap_f12_capital_raised_pershare_63d_accel_v035_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare ncff
def cap_f12_capital_raised_pershare_63d_accel_v036_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare ncff
def cap_f12_capital_raised_pershare_126d_accel_v037_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare ncff
def cap_f12_capital_raised_pershare_126d_accel_v038_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare ncff
def cap_f12_capital_raised_pershare_126d_accel_v039_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare ncff
def cap_f12_capital_raised_pershare_252d_accel_v040_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare ncff
def cap_f12_capital_raised_pershare_252d_accel_v041_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare ncff
def cap_f12_capital_raised_pershare_252d_accel_v042_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare ncff
def cap_f12_capital_raised_pershare_504d_accel_v043_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare ncff
def cap_f12_capital_raised_pershare_504d_accel_v044_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare ncff
def cap_f12_capital_raised_pershare_504d_accel_v045_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets ncff
def cap_f12_capital_raised_per_assets_21d_accel_v046_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets ncff
def cap_f12_capital_raised_per_assets_21d_accel_v047_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets ncff
def cap_f12_capital_raised_per_assets_21d_accel_v048_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets ncff
def cap_f12_capital_raised_per_assets_63d_accel_v049_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets ncff
def cap_f12_capital_raised_per_assets_63d_accel_v050_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets ncff
def cap_f12_capital_raised_per_assets_63d_accel_v051_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets ncff
def cap_f12_capital_raised_per_assets_126d_accel_v052_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets ncff
def cap_f12_capital_raised_per_assets_126d_accel_v053_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets ncff
def cap_f12_capital_raised_per_assets_126d_accel_v054_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets ncff
def cap_f12_capital_raised_per_assets_252d_accel_v055_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets ncff
def cap_f12_capital_raised_per_assets_252d_accel_v056_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets ncff
def cap_f12_capital_raised_per_assets_252d_accel_v057_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets ncff
def cap_f12_capital_raised_per_assets_504d_accel_v058_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets ncff
def cap_f12_capital_raised_per_assets_504d_accel_v059_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets ncff
def cap_f12_capital_raised_per_assets_504d_accel_v060_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_21d_accel_v061_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_21d_accel_v062_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_21d_accel_v063_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_63d_accel_v064_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_63d_accel_v065_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_63d_accel_v066_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_126d_accel_v067_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_126d_accel_v068_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_126d_accel_v069_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_252d_accel_v070_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_252d_accel_v071_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_252d_accel_v072_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_504d_accel_v073_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_504d_accel_v074_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_504d_accel_v075_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity ncff
def cap_f12_capital_raised_per_equity_21d_accel_v076_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity ncff
def cap_f12_capital_raised_per_equity_21d_accel_v077_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity ncff
def cap_f12_capital_raised_per_equity_21d_accel_v078_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity ncff
def cap_f12_capital_raised_per_equity_63d_accel_v079_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity ncff
def cap_f12_capital_raised_per_equity_63d_accel_v080_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity ncff
def cap_f12_capital_raised_per_equity_63d_accel_v081_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity ncff
def cap_f12_capital_raised_per_equity_126d_accel_v082_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity ncff
def cap_f12_capital_raised_per_equity_126d_accel_v083_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity ncff
def cap_f12_capital_raised_per_equity_126d_accel_v084_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity ncff
def cap_f12_capital_raised_per_equity_252d_accel_v085_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity ncff
def cap_f12_capital_raised_per_equity_252d_accel_v086_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity ncff
def cap_f12_capital_raised_per_equity_252d_accel_v087_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity ncff
def cap_f12_capital_raised_per_equity_504d_accel_v088_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity ncff
def cap_f12_capital_raised_per_equity_504d_accel_v089_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity ncff
def cap_f12_capital_raised_per_equity_504d_accel_v090_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std ncff
def cap_f12_capital_raised_std_21d_accel_v091_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std ncff
def cap_f12_capital_raised_std_21d_accel_v092_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std ncff
def cap_f12_capital_raised_std_21d_accel_v093_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std ncff
def cap_f12_capital_raised_std_63d_accel_v094_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std ncff
def cap_f12_capital_raised_std_63d_accel_v095_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std ncff
def cap_f12_capital_raised_std_63d_accel_v096_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std ncff
def cap_f12_capital_raised_std_126d_accel_v097_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std ncff
def cap_f12_capital_raised_std_126d_accel_v098_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std ncff
def cap_f12_capital_raised_std_126d_accel_v099_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std ncff
def cap_f12_capital_raised_std_252d_accel_v100_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std ncff
def cap_f12_capital_raised_std_252d_accel_v101_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std ncff
def cap_f12_capital_raised_std_252d_accel_v102_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std ncff
def cap_f12_capital_raised_std_504d_accel_v103_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std ncff
def cap_f12_capital_raised_std_504d_accel_v104_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std ncff
def cap_f12_capital_raised_std_504d_accel_v105_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm ncff
def cap_f12_capital_raised_ewm_21d_accel_v106_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm ncff
def cap_f12_capital_raised_ewm_21d_accel_v107_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm ncff
def cap_f12_capital_raised_ewm_21d_accel_v108_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm ncff
def cap_f12_capital_raised_ewm_63d_accel_v109_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm ncff
def cap_f12_capital_raised_ewm_63d_accel_v110_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm ncff
def cap_f12_capital_raised_ewm_63d_accel_v111_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm ncff
def cap_f12_capital_raised_ewm_126d_accel_v112_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm ncff
def cap_f12_capital_raised_ewm_126d_accel_v113_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm ncff
def cap_f12_capital_raised_ewm_126d_accel_v114_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm ncff
def cap_f12_capital_raised_ewm_252d_accel_v115_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm ncff
def cap_f12_capital_raised_ewm_252d_accel_v116_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm ncff
def cap_f12_capital_raised_ewm_252d_accel_v117_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm ncff
def cap_f12_capital_raised_ewm_504d_accel_v118_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm ncff
def cap_f12_capital_raised_ewm_504d_accel_v119_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm ncff
def cap_f12_capital_raised_ewm_504d_accel_v120_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq ncff
def cap_f12_capital_raised_sq_21d_accel_v121_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq ncff
def cap_f12_capital_raised_sq_21d_accel_v122_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq ncff
def cap_f12_capital_raised_sq_21d_accel_v123_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq ncff
def cap_f12_capital_raised_sq_63d_accel_v124_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq ncff
def cap_f12_capital_raised_sq_63d_accel_v125_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq ncff
def cap_f12_capital_raised_sq_63d_accel_v126_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq ncff
def cap_f12_capital_raised_sq_126d_accel_v127_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq ncff
def cap_f12_capital_raised_sq_126d_accel_v128_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq ncff
def cap_f12_capital_raised_sq_126d_accel_v129_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq ncff
def cap_f12_capital_raised_sq_252d_accel_v130_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq ncff
def cap_f12_capital_raised_sq_252d_accel_v131_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq ncff
def cap_f12_capital_raised_sq_252d_accel_v132_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq ncff
def cap_f12_capital_raised_sq_504d_accel_v133_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq ncff
def cap_f12_capital_raised_sq_504d_accel_v134_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq ncff
def cap_f12_capital_raised_sq_504d_accel_v135_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z ncff
def cap_f12_capital_raised_z_21d_accel_v136_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z ncff
def cap_f12_capital_raised_z_21d_accel_v137_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z ncff
def cap_f12_capital_raised_z_21d_accel_v138_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z ncff
def cap_f12_capital_raised_z_63d_accel_v139_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z ncff
def cap_f12_capital_raised_z_63d_accel_v140_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z ncff
def cap_f12_capital_raised_z_63d_accel_v141_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z ncff
def cap_f12_capital_raised_z_126d_accel_v142_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z ncff
def cap_f12_capital_raised_z_126d_accel_v143_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z ncff
def cap_f12_capital_raised_z_126d_accel_v144_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z ncff
def cap_f12_capital_raised_z_252d_accel_v145_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z ncff
def cap_f12_capital_raised_z_252d_accel_v146_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z ncff
def cap_f12_capital_raised_z_252d_accel_v147_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z ncff
def cap_f12_capital_raised_z_504d_accel_v148_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z ncff
def cap_f12_capital_raised_z_504d_accel_v149_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z ncff
def cap_f12_capital_raised_z_504d_accel_v150_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
