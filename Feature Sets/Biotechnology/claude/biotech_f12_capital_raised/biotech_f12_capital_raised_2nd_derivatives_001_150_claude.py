"""Family f12 - Financing cash flow / capital raised  (B_CashFlow_Burn) | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw ncff
def cap_f12_capital_raised_raw_21d_slope_v001_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw ncff
def cap_f12_capital_raised_raw_21d_slope_v002_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw ncff
def cap_f12_capital_raised_raw_21d_slope_v003_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw ncff
def cap_f12_capital_raised_raw_63d_slope_v004_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw ncff
def cap_f12_capital_raised_raw_63d_slope_v005_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw ncff
def cap_f12_capital_raised_raw_63d_slope_v006_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw ncff
def cap_f12_capital_raised_raw_126d_slope_v007_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw ncff
def cap_f12_capital_raised_raw_126d_slope_v008_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw ncff
def cap_f12_capital_raised_raw_126d_slope_v009_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw ncff
def cap_f12_capital_raised_raw_252d_slope_v010_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw ncff
def cap_f12_capital_raised_raw_252d_slope_v011_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw ncff
def cap_f12_capital_raised_raw_252d_slope_v012_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw ncff
def cap_f12_capital_raised_raw_504d_slope_v013_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw ncff
def cap_f12_capital_raised_raw_504d_slope_v014_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw ncff
def cap_f12_capital_raised_raw_504d_slope_v015_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log ncff
def cap_f12_capital_raised_log_21d_slope_v016_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log ncff
def cap_f12_capital_raised_log_21d_slope_v017_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log ncff
def cap_f12_capital_raised_log_21d_slope_v018_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log ncff
def cap_f12_capital_raised_log_63d_slope_v019_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log ncff
def cap_f12_capital_raised_log_63d_slope_v020_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log ncff
def cap_f12_capital_raised_log_63d_slope_v021_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log ncff
def cap_f12_capital_raised_log_126d_slope_v022_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log ncff
def cap_f12_capital_raised_log_126d_slope_v023_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log ncff
def cap_f12_capital_raised_log_126d_slope_v024_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log ncff
def cap_f12_capital_raised_log_252d_slope_v025_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log ncff
def cap_f12_capital_raised_log_252d_slope_v026_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log ncff
def cap_f12_capital_raised_log_252d_slope_v027_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log ncff
def cap_f12_capital_raised_log_504d_slope_v028_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log ncff
def cap_f12_capital_raised_log_504d_slope_v029_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log ncff
def cap_f12_capital_raised_log_504d_slope_v030_signal(ncff, closeadj):
    base = _mean(_capital_raised_log(ncff), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare ncff
def cap_f12_capital_raised_pershare_21d_slope_v031_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare ncff
def cap_f12_capital_raised_pershare_21d_slope_v032_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare ncff
def cap_f12_capital_raised_pershare_21d_slope_v033_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare ncff
def cap_f12_capital_raised_pershare_63d_slope_v034_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare ncff
def cap_f12_capital_raised_pershare_63d_slope_v035_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare ncff
def cap_f12_capital_raised_pershare_63d_slope_v036_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare ncff
def cap_f12_capital_raised_pershare_126d_slope_v037_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare ncff
def cap_f12_capital_raised_pershare_126d_slope_v038_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare ncff
def cap_f12_capital_raised_pershare_126d_slope_v039_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare ncff
def cap_f12_capital_raised_pershare_252d_slope_v040_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare ncff
def cap_f12_capital_raised_pershare_252d_slope_v041_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare ncff
def cap_f12_capital_raised_pershare_252d_slope_v042_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare ncff
def cap_f12_capital_raised_pershare_504d_slope_v043_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare ncff
def cap_f12_capital_raised_pershare_504d_slope_v044_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare ncff
def cap_f12_capital_raised_pershare_504d_slope_v045_signal(ncff, sharesbas, closeadj):
    base = _mean(_capital_raised_per_share(ncff, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets ncff
def cap_f12_capital_raised_per_assets_21d_slope_v046_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets ncff
def cap_f12_capital_raised_per_assets_21d_slope_v047_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets ncff
def cap_f12_capital_raised_per_assets_21d_slope_v048_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets ncff
def cap_f12_capital_raised_per_assets_63d_slope_v049_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets ncff
def cap_f12_capital_raised_per_assets_63d_slope_v050_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets ncff
def cap_f12_capital_raised_per_assets_63d_slope_v051_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets ncff
def cap_f12_capital_raised_per_assets_126d_slope_v052_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets ncff
def cap_f12_capital_raised_per_assets_126d_slope_v053_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets ncff
def cap_f12_capital_raised_per_assets_126d_slope_v054_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets ncff
def cap_f12_capital_raised_per_assets_252d_slope_v055_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets ncff
def cap_f12_capital_raised_per_assets_252d_slope_v056_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets ncff
def cap_f12_capital_raised_per_assets_252d_slope_v057_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets ncff
def cap_f12_capital_raised_per_assets_504d_slope_v058_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets ncff
def cap_f12_capital_raised_per_assets_504d_slope_v059_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets ncff
def cap_f12_capital_raised_per_assets_504d_slope_v060_signal(ncff, assets):
    base = _mean(_capital_raised_scaled(ncff, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_21d_slope_v061_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_21d_slope_v062_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_21d_slope_v063_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_63d_slope_v064_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_63d_slope_v065_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_63d_slope_v066_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_126d_slope_v067_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_126d_slope_v068_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_126d_slope_v069_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_252d_slope_v070_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_252d_slope_v071_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_252d_slope_v072_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_504d_slope_v073_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_504d_slope_v074_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap ncff
def cap_f12_capital_raised_per_marketcap_504d_slope_v075_signal(ncff, marketcap):
    base = _mean(_capital_raised_scaled(ncff, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity ncff
def cap_f12_capital_raised_per_equity_21d_slope_v076_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity ncff
def cap_f12_capital_raised_per_equity_21d_slope_v077_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity ncff
def cap_f12_capital_raised_per_equity_21d_slope_v078_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity ncff
def cap_f12_capital_raised_per_equity_63d_slope_v079_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity ncff
def cap_f12_capital_raised_per_equity_63d_slope_v080_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity ncff
def cap_f12_capital_raised_per_equity_63d_slope_v081_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity ncff
def cap_f12_capital_raised_per_equity_126d_slope_v082_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity ncff
def cap_f12_capital_raised_per_equity_126d_slope_v083_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity ncff
def cap_f12_capital_raised_per_equity_126d_slope_v084_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity ncff
def cap_f12_capital_raised_per_equity_252d_slope_v085_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity ncff
def cap_f12_capital_raised_per_equity_252d_slope_v086_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity ncff
def cap_f12_capital_raised_per_equity_252d_slope_v087_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity ncff
def cap_f12_capital_raised_per_equity_504d_slope_v088_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity ncff
def cap_f12_capital_raised_per_equity_504d_slope_v089_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity ncff
def cap_f12_capital_raised_per_equity_504d_slope_v090_signal(ncff, equity):
    base = _mean(_capital_raised_scaled(ncff, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std ncff
def cap_f12_capital_raised_std_21d_slope_v091_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std ncff
def cap_f12_capital_raised_std_21d_slope_v092_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std ncff
def cap_f12_capital_raised_std_21d_slope_v093_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std ncff
def cap_f12_capital_raised_std_63d_slope_v094_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std ncff
def cap_f12_capital_raised_std_63d_slope_v095_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std ncff
def cap_f12_capital_raised_std_63d_slope_v096_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std ncff
def cap_f12_capital_raised_std_126d_slope_v097_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std ncff
def cap_f12_capital_raised_std_126d_slope_v098_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std ncff
def cap_f12_capital_raised_std_126d_slope_v099_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std ncff
def cap_f12_capital_raised_std_252d_slope_v100_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std ncff
def cap_f12_capital_raised_std_252d_slope_v101_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std ncff
def cap_f12_capital_raised_std_252d_slope_v102_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std ncff
def cap_f12_capital_raised_std_504d_slope_v103_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std ncff
def cap_f12_capital_raised_std_504d_slope_v104_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std ncff
def cap_f12_capital_raised_std_504d_slope_v105_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm ncff
def cap_f12_capital_raised_ewm_21d_slope_v106_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm ncff
def cap_f12_capital_raised_ewm_21d_slope_v107_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm ncff
def cap_f12_capital_raised_ewm_21d_slope_v108_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm ncff
def cap_f12_capital_raised_ewm_63d_slope_v109_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm ncff
def cap_f12_capital_raised_ewm_63d_slope_v110_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm ncff
def cap_f12_capital_raised_ewm_63d_slope_v111_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm ncff
def cap_f12_capital_raised_ewm_126d_slope_v112_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm ncff
def cap_f12_capital_raised_ewm_126d_slope_v113_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm ncff
def cap_f12_capital_raised_ewm_126d_slope_v114_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm ncff
def cap_f12_capital_raised_ewm_252d_slope_v115_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm ncff
def cap_f12_capital_raised_ewm_252d_slope_v116_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm ncff
def cap_f12_capital_raised_ewm_252d_slope_v117_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm ncff
def cap_f12_capital_raised_ewm_504d_slope_v118_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm ncff
def cap_f12_capital_raised_ewm_504d_slope_v119_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm ncff
def cap_f12_capital_raised_ewm_504d_slope_v120_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq ncff
def cap_f12_capital_raised_sq_21d_slope_v121_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq ncff
def cap_f12_capital_raised_sq_21d_slope_v122_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq ncff
def cap_f12_capital_raised_sq_21d_slope_v123_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq ncff
def cap_f12_capital_raised_sq_63d_slope_v124_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq ncff
def cap_f12_capital_raised_sq_63d_slope_v125_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq ncff
def cap_f12_capital_raised_sq_63d_slope_v126_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq ncff
def cap_f12_capital_raised_sq_126d_slope_v127_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq ncff
def cap_f12_capital_raised_sq_126d_slope_v128_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq ncff
def cap_f12_capital_raised_sq_126d_slope_v129_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq ncff
def cap_f12_capital_raised_sq_252d_slope_v130_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq ncff
def cap_f12_capital_raised_sq_252d_slope_v131_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq ncff
def cap_f12_capital_raised_sq_252d_slope_v132_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq ncff
def cap_f12_capital_raised_sq_504d_slope_v133_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq ncff
def cap_f12_capital_raised_sq_504d_slope_v134_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq ncff
def cap_f12_capital_raised_sq_504d_slope_v135_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z ncff
def cap_f12_capital_raised_z_21d_slope_v136_signal(ncff):
    base = _z(ncff, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z ncff
def cap_f12_capital_raised_z_21d_slope_v137_signal(ncff):
    base = _z(ncff, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z ncff
def cap_f12_capital_raised_z_21d_slope_v138_signal(ncff):
    base = _z(ncff, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z ncff
def cap_f12_capital_raised_z_63d_slope_v139_signal(ncff):
    base = _z(ncff, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z ncff
def cap_f12_capital_raised_z_63d_slope_v140_signal(ncff):
    base = _z(ncff, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z ncff
def cap_f12_capital_raised_z_63d_slope_v141_signal(ncff):
    base = _z(ncff, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z ncff
def cap_f12_capital_raised_z_126d_slope_v142_signal(ncff):
    base = _z(ncff, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z ncff
def cap_f12_capital_raised_z_126d_slope_v143_signal(ncff):
    base = _z(ncff, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z ncff
def cap_f12_capital_raised_z_126d_slope_v144_signal(ncff):
    base = _z(ncff, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z ncff
def cap_f12_capital_raised_z_252d_slope_v145_signal(ncff):
    base = _z(ncff, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z ncff
def cap_f12_capital_raised_z_252d_slope_v146_signal(ncff):
    base = _z(ncff, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z ncff
def cap_f12_capital_raised_z_252d_slope_v147_signal(ncff):
    base = _z(ncff, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z ncff
def cap_f12_capital_raised_z_504d_slope_v148_signal(ncff):
    base = _z(ncff, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z ncff
def cap_f12_capital_raised_z_504d_slope_v149_signal(ncff):
    base = _z(ncff, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z ncff
def cap_f12_capital_raised_z_504d_slope_v150_signal(ncff):
    base = _z(ncff, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
