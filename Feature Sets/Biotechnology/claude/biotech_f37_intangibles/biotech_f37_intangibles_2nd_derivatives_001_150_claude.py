"""Family f37 - Intangibles & goodwill  (F_BalanceSheet) | 2nd derivatives 001-150"""
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
def _intangibles_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _intangibles_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _intangibles_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw intangibles
def intg_f37_intangibles_raw_21d_slope_v001_signal(intangibles, closeadj):
    base = _mean(intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw intangibles
def intg_f37_intangibles_raw_21d_slope_v002_signal(intangibles, closeadj):
    base = _mean(intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw intangibles
def intg_f37_intangibles_raw_21d_slope_v003_signal(intangibles, closeadj):
    base = _mean(intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw intangibles
def intg_f37_intangibles_raw_63d_slope_v004_signal(intangibles, closeadj):
    base = _mean(intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw intangibles
def intg_f37_intangibles_raw_63d_slope_v005_signal(intangibles, closeadj):
    base = _mean(intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw intangibles
def intg_f37_intangibles_raw_63d_slope_v006_signal(intangibles, closeadj):
    base = _mean(intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw intangibles
def intg_f37_intangibles_raw_126d_slope_v007_signal(intangibles, closeadj):
    base = _mean(intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw intangibles
def intg_f37_intangibles_raw_126d_slope_v008_signal(intangibles, closeadj):
    base = _mean(intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw intangibles
def intg_f37_intangibles_raw_126d_slope_v009_signal(intangibles, closeadj):
    base = _mean(intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw intangibles
def intg_f37_intangibles_raw_252d_slope_v010_signal(intangibles, closeadj):
    base = _mean(intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw intangibles
def intg_f37_intangibles_raw_252d_slope_v011_signal(intangibles, closeadj):
    base = _mean(intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw intangibles
def intg_f37_intangibles_raw_252d_slope_v012_signal(intangibles, closeadj):
    base = _mean(intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw intangibles
def intg_f37_intangibles_raw_504d_slope_v013_signal(intangibles, closeadj):
    base = _mean(intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw intangibles
def intg_f37_intangibles_raw_504d_slope_v014_signal(intangibles, closeadj):
    base = _mean(intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw intangibles
def intg_f37_intangibles_raw_504d_slope_v015_signal(intangibles, closeadj):
    base = _mean(intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log intangibles
def intg_f37_intangibles_log_21d_slope_v016_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log intangibles
def intg_f37_intangibles_log_21d_slope_v017_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log intangibles
def intg_f37_intangibles_log_21d_slope_v018_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log intangibles
def intg_f37_intangibles_log_63d_slope_v019_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log intangibles
def intg_f37_intangibles_log_63d_slope_v020_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log intangibles
def intg_f37_intangibles_log_63d_slope_v021_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log intangibles
def intg_f37_intangibles_log_126d_slope_v022_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log intangibles
def intg_f37_intangibles_log_126d_slope_v023_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log intangibles
def intg_f37_intangibles_log_126d_slope_v024_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log intangibles
def intg_f37_intangibles_log_252d_slope_v025_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log intangibles
def intg_f37_intangibles_log_252d_slope_v026_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log intangibles
def intg_f37_intangibles_log_252d_slope_v027_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log intangibles
def intg_f37_intangibles_log_504d_slope_v028_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log intangibles
def intg_f37_intangibles_log_504d_slope_v029_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log intangibles
def intg_f37_intangibles_log_504d_slope_v030_signal(intangibles, closeadj):
    base = _mean(_intangibles_log(intangibles), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare intangibles
def intg_f37_intangibles_pershare_21d_slope_v031_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare intangibles
def intg_f37_intangibles_pershare_21d_slope_v032_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare intangibles
def intg_f37_intangibles_pershare_21d_slope_v033_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare intangibles
def intg_f37_intangibles_pershare_63d_slope_v034_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare intangibles
def intg_f37_intangibles_pershare_63d_slope_v035_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare intangibles
def intg_f37_intangibles_pershare_63d_slope_v036_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare intangibles
def intg_f37_intangibles_pershare_126d_slope_v037_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare intangibles
def intg_f37_intangibles_pershare_126d_slope_v038_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare intangibles
def intg_f37_intangibles_pershare_126d_slope_v039_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare intangibles
def intg_f37_intangibles_pershare_252d_slope_v040_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare intangibles
def intg_f37_intangibles_pershare_252d_slope_v041_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare intangibles
def intg_f37_intangibles_pershare_252d_slope_v042_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare intangibles
def intg_f37_intangibles_pershare_504d_slope_v043_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare intangibles
def intg_f37_intangibles_pershare_504d_slope_v044_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare intangibles
def intg_f37_intangibles_pershare_504d_slope_v045_signal(intangibles, sharesbas, closeadj):
    base = _mean(_intangibles_per_share(intangibles, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets intangibles
def intg_f37_intangibles_per_assets_21d_slope_v046_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets intangibles
def intg_f37_intangibles_per_assets_21d_slope_v047_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets intangibles
def intg_f37_intangibles_per_assets_21d_slope_v048_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets intangibles
def intg_f37_intangibles_per_assets_63d_slope_v049_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets intangibles
def intg_f37_intangibles_per_assets_63d_slope_v050_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets intangibles
def intg_f37_intangibles_per_assets_63d_slope_v051_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets intangibles
def intg_f37_intangibles_per_assets_126d_slope_v052_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets intangibles
def intg_f37_intangibles_per_assets_126d_slope_v053_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets intangibles
def intg_f37_intangibles_per_assets_126d_slope_v054_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets intangibles
def intg_f37_intangibles_per_assets_252d_slope_v055_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets intangibles
def intg_f37_intangibles_per_assets_252d_slope_v056_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets intangibles
def intg_f37_intangibles_per_assets_252d_slope_v057_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets intangibles
def intg_f37_intangibles_per_assets_504d_slope_v058_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets intangibles
def intg_f37_intangibles_per_assets_504d_slope_v059_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets intangibles
def intg_f37_intangibles_per_assets_504d_slope_v060_signal(intangibles, assets):
    base = _mean(_intangibles_scaled(intangibles, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_21d_slope_v061_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_21d_slope_v062_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_21d_slope_v063_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_63d_slope_v064_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_63d_slope_v065_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_63d_slope_v066_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_126d_slope_v067_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_126d_slope_v068_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_126d_slope_v069_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_252d_slope_v070_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_252d_slope_v071_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_252d_slope_v072_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_504d_slope_v073_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_504d_slope_v074_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap intangibles
def intg_f37_intangibles_per_marketcap_504d_slope_v075_signal(intangibles, marketcap):
    base = _mean(_intangibles_scaled(intangibles, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity intangibles
def intg_f37_intangibles_per_equity_21d_slope_v076_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity intangibles
def intg_f37_intangibles_per_equity_21d_slope_v077_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity intangibles
def intg_f37_intangibles_per_equity_21d_slope_v078_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity intangibles
def intg_f37_intangibles_per_equity_63d_slope_v079_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity intangibles
def intg_f37_intangibles_per_equity_63d_slope_v080_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity intangibles
def intg_f37_intangibles_per_equity_63d_slope_v081_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity intangibles
def intg_f37_intangibles_per_equity_126d_slope_v082_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity intangibles
def intg_f37_intangibles_per_equity_126d_slope_v083_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity intangibles
def intg_f37_intangibles_per_equity_126d_slope_v084_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity intangibles
def intg_f37_intangibles_per_equity_252d_slope_v085_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity intangibles
def intg_f37_intangibles_per_equity_252d_slope_v086_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity intangibles
def intg_f37_intangibles_per_equity_252d_slope_v087_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity intangibles
def intg_f37_intangibles_per_equity_504d_slope_v088_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity intangibles
def intg_f37_intangibles_per_equity_504d_slope_v089_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity intangibles
def intg_f37_intangibles_per_equity_504d_slope_v090_signal(intangibles, equity):
    base = _mean(_intangibles_scaled(intangibles, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std intangibles
def intg_f37_intangibles_std_21d_slope_v091_signal(intangibles, closeadj):
    base = _std(intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std intangibles
def intg_f37_intangibles_std_21d_slope_v092_signal(intangibles, closeadj):
    base = _std(intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std intangibles
def intg_f37_intangibles_std_21d_slope_v093_signal(intangibles, closeadj):
    base = _std(intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std intangibles
def intg_f37_intangibles_std_63d_slope_v094_signal(intangibles, closeadj):
    base = _std(intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std intangibles
def intg_f37_intangibles_std_63d_slope_v095_signal(intangibles, closeadj):
    base = _std(intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std intangibles
def intg_f37_intangibles_std_63d_slope_v096_signal(intangibles, closeadj):
    base = _std(intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std intangibles
def intg_f37_intangibles_std_126d_slope_v097_signal(intangibles, closeadj):
    base = _std(intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std intangibles
def intg_f37_intangibles_std_126d_slope_v098_signal(intangibles, closeadj):
    base = _std(intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std intangibles
def intg_f37_intangibles_std_126d_slope_v099_signal(intangibles, closeadj):
    base = _std(intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std intangibles
def intg_f37_intangibles_std_252d_slope_v100_signal(intangibles, closeadj):
    base = _std(intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std intangibles
def intg_f37_intangibles_std_252d_slope_v101_signal(intangibles, closeadj):
    base = _std(intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std intangibles
def intg_f37_intangibles_std_252d_slope_v102_signal(intangibles, closeadj):
    base = _std(intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std intangibles
def intg_f37_intangibles_std_504d_slope_v103_signal(intangibles, closeadj):
    base = _std(intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std intangibles
def intg_f37_intangibles_std_504d_slope_v104_signal(intangibles, closeadj):
    base = _std(intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std intangibles
def intg_f37_intangibles_std_504d_slope_v105_signal(intangibles, closeadj):
    base = _std(intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm intangibles
def intg_f37_intangibles_ewm_21d_slope_v106_signal(intangibles, closeadj):
    base = intangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm intangibles
def intg_f37_intangibles_ewm_21d_slope_v107_signal(intangibles, closeadj):
    base = intangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm intangibles
def intg_f37_intangibles_ewm_21d_slope_v108_signal(intangibles, closeadj):
    base = intangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm intangibles
def intg_f37_intangibles_ewm_63d_slope_v109_signal(intangibles, closeadj):
    base = intangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm intangibles
def intg_f37_intangibles_ewm_63d_slope_v110_signal(intangibles, closeadj):
    base = intangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm intangibles
def intg_f37_intangibles_ewm_63d_slope_v111_signal(intangibles, closeadj):
    base = intangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm intangibles
def intg_f37_intangibles_ewm_126d_slope_v112_signal(intangibles, closeadj):
    base = intangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm intangibles
def intg_f37_intangibles_ewm_126d_slope_v113_signal(intangibles, closeadj):
    base = intangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm intangibles
def intg_f37_intangibles_ewm_126d_slope_v114_signal(intangibles, closeadj):
    base = intangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm intangibles
def intg_f37_intangibles_ewm_252d_slope_v115_signal(intangibles, closeadj):
    base = intangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm intangibles
def intg_f37_intangibles_ewm_252d_slope_v116_signal(intangibles, closeadj):
    base = intangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm intangibles
def intg_f37_intangibles_ewm_252d_slope_v117_signal(intangibles, closeadj):
    base = intangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm intangibles
def intg_f37_intangibles_ewm_504d_slope_v118_signal(intangibles, closeadj):
    base = intangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm intangibles
def intg_f37_intangibles_ewm_504d_slope_v119_signal(intangibles, closeadj):
    base = intangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm intangibles
def intg_f37_intangibles_ewm_504d_slope_v120_signal(intangibles, closeadj):
    base = intangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq intangibles
def intg_f37_intangibles_sq_21d_slope_v121_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq intangibles
def intg_f37_intangibles_sq_21d_slope_v122_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq intangibles
def intg_f37_intangibles_sq_21d_slope_v123_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq intangibles
def intg_f37_intangibles_sq_63d_slope_v124_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq intangibles
def intg_f37_intangibles_sq_63d_slope_v125_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq intangibles
def intg_f37_intangibles_sq_63d_slope_v126_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq intangibles
def intg_f37_intangibles_sq_126d_slope_v127_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq intangibles
def intg_f37_intangibles_sq_126d_slope_v128_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq intangibles
def intg_f37_intangibles_sq_126d_slope_v129_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq intangibles
def intg_f37_intangibles_sq_252d_slope_v130_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq intangibles
def intg_f37_intangibles_sq_252d_slope_v131_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq intangibles
def intg_f37_intangibles_sq_252d_slope_v132_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq intangibles
def intg_f37_intangibles_sq_504d_slope_v133_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq intangibles
def intg_f37_intangibles_sq_504d_slope_v134_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq intangibles
def intg_f37_intangibles_sq_504d_slope_v135_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z intangibles
def intg_f37_intangibles_z_21d_slope_v136_signal(intangibles):
    base = _z(intangibles, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z intangibles
def intg_f37_intangibles_z_21d_slope_v137_signal(intangibles):
    base = _z(intangibles, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z intangibles
def intg_f37_intangibles_z_21d_slope_v138_signal(intangibles):
    base = _z(intangibles, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z intangibles
def intg_f37_intangibles_z_63d_slope_v139_signal(intangibles):
    base = _z(intangibles, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z intangibles
def intg_f37_intangibles_z_63d_slope_v140_signal(intangibles):
    base = _z(intangibles, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z intangibles
def intg_f37_intangibles_z_63d_slope_v141_signal(intangibles):
    base = _z(intangibles, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z intangibles
def intg_f37_intangibles_z_126d_slope_v142_signal(intangibles):
    base = _z(intangibles, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z intangibles
def intg_f37_intangibles_z_126d_slope_v143_signal(intangibles):
    base = _z(intangibles, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z intangibles
def intg_f37_intangibles_z_126d_slope_v144_signal(intangibles):
    base = _z(intangibles, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z intangibles
def intg_f37_intangibles_z_252d_slope_v145_signal(intangibles):
    base = _z(intangibles, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z intangibles
def intg_f37_intangibles_z_252d_slope_v146_signal(intangibles):
    base = _z(intangibles, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z intangibles
def intg_f37_intangibles_z_252d_slope_v147_signal(intangibles):
    base = _z(intangibles, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z intangibles
def intg_f37_intangibles_z_504d_slope_v148_signal(intangibles):
    base = _z(intangibles, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z intangibles
def intg_f37_intangibles_z_504d_slope_v149_signal(intangibles):
    base = _z(intangibles, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z intangibles
def intg_f37_intangibles_z_504d_slope_v150_signal(intangibles):
    base = _z(intangibles, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
