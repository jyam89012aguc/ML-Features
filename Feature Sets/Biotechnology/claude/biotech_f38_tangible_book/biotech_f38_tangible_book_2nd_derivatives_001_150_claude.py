"""Family f38 - Tangible book value  (F_BalanceSheet) | 2nd derivatives 001-150"""
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
def _tangible_book_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _tangible_book_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _tangible_book_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw tangibles
def tb_f38_tangible_book_raw_21d_slope_v001_signal(tangibles, closeadj):
    base = _mean(tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw tangibles
def tb_f38_tangible_book_raw_21d_slope_v002_signal(tangibles, closeadj):
    base = _mean(tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw tangibles
def tb_f38_tangible_book_raw_21d_slope_v003_signal(tangibles, closeadj):
    base = _mean(tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw tangibles
def tb_f38_tangible_book_raw_63d_slope_v004_signal(tangibles, closeadj):
    base = _mean(tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw tangibles
def tb_f38_tangible_book_raw_63d_slope_v005_signal(tangibles, closeadj):
    base = _mean(tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw tangibles
def tb_f38_tangible_book_raw_63d_slope_v006_signal(tangibles, closeadj):
    base = _mean(tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw tangibles
def tb_f38_tangible_book_raw_126d_slope_v007_signal(tangibles, closeadj):
    base = _mean(tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw tangibles
def tb_f38_tangible_book_raw_126d_slope_v008_signal(tangibles, closeadj):
    base = _mean(tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw tangibles
def tb_f38_tangible_book_raw_126d_slope_v009_signal(tangibles, closeadj):
    base = _mean(tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw tangibles
def tb_f38_tangible_book_raw_252d_slope_v010_signal(tangibles, closeadj):
    base = _mean(tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw tangibles
def tb_f38_tangible_book_raw_252d_slope_v011_signal(tangibles, closeadj):
    base = _mean(tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw tangibles
def tb_f38_tangible_book_raw_252d_slope_v012_signal(tangibles, closeadj):
    base = _mean(tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw tangibles
def tb_f38_tangible_book_raw_504d_slope_v013_signal(tangibles, closeadj):
    base = _mean(tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw tangibles
def tb_f38_tangible_book_raw_504d_slope_v014_signal(tangibles, closeadj):
    base = _mean(tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw tangibles
def tb_f38_tangible_book_raw_504d_slope_v015_signal(tangibles, closeadj):
    base = _mean(tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log tangibles
def tb_f38_tangible_book_log_21d_slope_v016_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log tangibles
def tb_f38_tangible_book_log_21d_slope_v017_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log tangibles
def tb_f38_tangible_book_log_21d_slope_v018_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log tangibles
def tb_f38_tangible_book_log_63d_slope_v019_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log tangibles
def tb_f38_tangible_book_log_63d_slope_v020_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log tangibles
def tb_f38_tangible_book_log_63d_slope_v021_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log tangibles
def tb_f38_tangible_book_log_126d_slope_v022_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log tangibles
def tb_f38_tangible_book_log_126d_slope_v023_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log tangibles
def tb_f38_tangible_book_log_126d_slope_v024_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log tangibles
def tb_f38_tangible_book_log_252d_slope_v025_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log tangibles
def tb_f38_tangible_book_log_252d_slope_v026_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log tangibles
def tb_f38_tangible_book_log_252d_slope_v027_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log tangibles
def tb_f38_tangible_book_log_504d_slope_v028_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log tangibles
def tb_f38_tangible_book_log_504d_slope_v029_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log tangibles
def tb_f38_tangible_book_log_504d_slope_v030_signal(tangibles, closeadj):
    base = _mean(_tangible_book_log(tangibles), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare tangibles
def tb_f38_tangible_book_pershare_21d_slope_v031_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare tangibles
def tb_f38_tangible_book_pershare_21d_slope_v032_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare tangibles
def tb_f38_tangible_book_pershare_21d_slope_v033_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare tangibles
def tb_f38_tangible_book_pershare_63d_slope_v034_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare tangibles
def tb_f38_tangible_book_pershare_63d_slope_v035_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare tangibles
def tb_f38_tangible_book_pershare_63d_slope_v036_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare tangibles
def tb_f38_tangible_book_pershare_126d_slope_v037_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare tangibles
def tb_f38_tangible_book_pershare_126d_slope_v038_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare tangibles
def tb_f38_tangible_book_pershare_126d_slope_v039_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare tangibles
def tb_f38_tangible_book_pershare_252d_slope_v040_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare tangibles
def tb_f38_tangible_book_pershare_252d_slope_v041_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare tangibles
def tb_f38_tangible_book_pershare_252d_slope_v042_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare tangibles
def tb_f38_tangible_book_pershare_504d_slope_v043_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare tangibles
def tb_f38_tangible_book_pershare_504d_slope_v044_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare tangibles
def tb_f38_tangible_book_pershare_504d_slope_v045_signal(tangibles, sharesbas, closeadj):
    base = _mean(_tangible_book_per_share(tangibles, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets tangibles
def tb_f38_tangible_book_per_assets_21d_slope_v046_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets tangibles
def tb_f38_tangible_book_per_assets_21d_slope_v047_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets tangibles
def tb_f38_tangible_book_per_assets_21d_slope_v048_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets tangibles
def tb_f38_tangible_book_per_assets_63d_slope_v049_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets tangibles
def tb_f38_tangible_book_per_assets_63d_slope_v050_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets tangibles
def tb_f38_tangible_book_per_assets_63d_slope_v051_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets tangibles
def tb_f38_tangible_book_per_assets_126d_slope_v052_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets tangibles
def tb_f38_tangible_book_per_assets_126d_slope_v053_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets tangibles
def tb_f38_tangible_book_per_assets_126d_slope_v054_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets tangibles
def tb_f38_tangible_book_per_assets_252d_slope_v055_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets tangibles
def tb_f38_tangible_book_per_assets_252d_slope_v056_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets tangibles
def tb_f38_tangible_book_per_assets_252d_slope_v057_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets tangibles
def tb_f38_tangible_book_per_assets_504d_slope_v058_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets tangibles
def tb_f38_tangible_book_per_assets_504d_slope_v059_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets tangibles
def tb_f38_tangible_book_per_assets_504d_slope_v060_signal(tangibles, assets):
    base = _mean(_tangible_book_scaled(tangibles, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_21d_slope_v061_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_21d_slope_v062_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_21d_slope_v063_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_63d_slope_v064_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_63d_slope_v065_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_63d_slope_v066_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_126d_slope_v067_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_126d_slope_v068_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_126d_slope_v069_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_252d_slope_v070_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_252d_slope_v071_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_252d_slope_v072_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_504d_slope_v073_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_504d_slope_v074_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap tangibles
def tb_f38_tangible_book_per_marketcap_504d_slope_v075_signal(tangibles, marketcap):
    base = _mean(_tangible_book_scaled(tangibles, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity tangibles
def tb_f38_tangible_book_per_equity_21d_slope_v076_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity tangibles
def tb_f38_tangible_book_per_equity_21d_slope_v077_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity tangibles
def tb_f38_tangible_book_per_equity_21d_slope_v078_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity tangibles
def tb_f38_tangible_book_per_equity_63d_slope_v079_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity tangibles
def tb_f38_tangible_book_per_equity_63d_slope_v080_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity tangibles
def tb_f38_tangible_book_per_equity_63d_slope_v081_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity tangibles
def tb_f38_tangible_book_per_equity_126d_slope_v082_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity tangibles
def tb_f38_tangible_book_per_equity_126d_slope_v083_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity tangibles
def tb_f38_tangible_book_per_equity_126d_slope_v084_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity tangibles
def tb_f38_tangible_book_per_equity_252d_slope_v085_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity tangibles
def tb_f38_tangible_book_per_equity_252d_slope_v086_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity tangibles
def tb_f38_tangible_book_per_equity_252d_slope_v087_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity tangibles
def tb_f38_tangible_book_per_equity_504d_slope_v088_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity tangibles
def tb_f38_tangible_book_per_equity_504d_slope_v089_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity tangibles
def tb_f38_tangible_book_per_equity_504d_slope_v090_signal(tangibles, equity):
    base = _mean(_tangible_book_scaled(tangibles, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std tangibles
def tb_f38_tangible_book_std_21d_slope_v091_signal(tangibles, closeadj):
    base = _std(tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std tangibles
def tb_f38_tangible_book_std_21d_slope_v092_signal(tangibles, closeadj):
    base = _std(tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std tangibles
def tb_f38_tangible_book_std_21d_slope_v093_signal(tangibles, closeadj):
    base = _std(tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std tangibles
def tb_f38_tangible_book_std_63d_slope_v094_signal(tangibles, closeadj):
    base = _std(tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std tangibles
def tb_f38_tangible_book_std_63d_slope_v095_signal(tangibles, closeadj):
    base = _std(tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std tangibles
def tb_f38_tangible_book_std_63d_slope_v096_signal(tangibles, closeadj):
    base = _std(tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std tangibles
def tb_f38_tangible_book_std_126d_slope_v097_signal(tangibles, closeadj):
    base = _std(tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std tangibles
def tb_f38_tangible_book_std_126d_slope_v098_signal(tangibles, closeadj):
    base = _std(tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std tangibles
def tb_f38_tangible_book_std_126d_slope_v099_signal(tangibles, closeadj):
    base = _std(tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std tangibles
def tb_f38_tangible_book_std_252d_slope_v100_signal(tangibles, closeadj):
    base = _std(tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std tangibles
def tb_f38_tangible_book_std_252d_slope_v101_signal(tangibles, closeadj):
    base = _std(tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std tangibles
def tb_f38_tangible_book_std_252d_slope_v102_signal(tangibles, closeadj):
    base = _std(tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std tangibles
def tb_f38_tangible_book_std_504d_slope_v103_signal(tangibles, closeadj):
    base = _std(tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std tangibles
def tb_f38_tangible_book_std_504d_slope_v104_signal(tangibles, closeadj):
    base = _std(tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std tangibles
def tb_f38_tangible_book_std_504d_slope_v105_signal(tangibles, closeadj):
    base = _std(tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm tangibles
def tb_f38_tangible_book_ewm_21d_slope_v106_signal(tangibles, closeadj):
    base = tangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm tangibles
def tb_f38_tangible_book_ewm_21d_slope_v107_signal(tangibles, closeadj):
    base = tangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm tangibles
def tb_f38_tangible_book_ewm_21d_slope_v108_signal(tangibles, closeadj):
    base = tangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm tangibles
def tb_f38_tangible_book_ewm_63d_slope_v109_signal(tangibles, closeadj):
    base = tangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm tangibles
def tb_f38_tangible_book_ewm_63d_slope_v110_signal(tangibles, closeadj):
    base = tangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm tangibles
def tb_f38_tangible_book_ewm_63d_slope_v111_signal(tangibles, closeadj):
    base = tangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm tangibles
def tb_f38_tangible_book_ewm_126d_slope_v112_signal(tangibles, closeadj):
    base = tangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm tangibles
def tb_f38_tangible_book_ewm_126d_slope_v113_signal(tangibles, closeadj):
    base = tangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm tangibles
def tb_f38_tangible_book_ewm_126d_slope_v114_signal(tangibles, closeadj):
    base = tangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm tangibles
def tb_f38_tangible_book_ewm_252d_slope_v115_signal(tangibles, closeadj):
    base = tangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm tangibles
def tb_f38_tangible_book_ewm_252d_slope_v116_signal(tangibles, closeadj):
    base = tangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm tangibles
def tb_f38_tangible_book_ewm_252d_slope_v117_signal(tangibles, closeadj):
    base = tangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm tangibles
def tb_f38_tangible_book_ewm_504d_slope_v118_signal(tangibles, closeadj):
    base = tangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm tangibles
def tb_f38_tangible_book_ewm_504d_slope_v119_signal(tangibles, closeadj):
    base = tangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm tangibles
def tb_f38_tangible_book_ewm_504d_slope_v120_signal(tangibles, closeadj):
    base = tangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq tangibles
def tb_f38_tangible_book_sq_21d_slope_v121_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq tangibles
def tb_f38_tangible_book_sq_21d_slope_v122_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq tangibles
def tb_f38_tangible_book_sq_21d_slope_v123_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq tangibles
def tb_f38_tangible_book_sq_63d_slope_v124_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq tangibles
def tb_f38_tangible_book_sq_63d_slope_v125_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq tangibles
def tb_f38_tangible_book_sq_63d_slope_v126_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq tangibles
def tb_f38_tangible_book_sq_126d_slope_v127_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq tangibles
def tb_f38_tangible_book_sq_126d_slope_v128_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq tangibles
def tb_f38_tangible_book_sq_126d_slope_v129_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq tangibles
def tb_f38_tangible_book_sq_252d_slope_v130_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq tangibles
def tb_f38_tangible_book_sq_252d_slope_v131_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq tangibles
def tb_f38_tangible_book_sq_252d_slope_v132_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq tangibles
def tb_f38_tangible_book_sq_504d_slope_v133_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq tangibles
def tb_f38_tangible_book_sq_504d_slope_v134_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq tangibles
def tb_f38_tangible_book_sq_504d_slope_v135_signal(tangibles, closeadj):
    base = _mean(tangibles * tangibles, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z tangibles
def tb_f38_tangible_book_z_21d_slope_v136_signal(tangibles):
    base = _z(tangibles, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z tangibles
def tb_f38_tangible_book_z_21d_slope_v137_signal(tangibles):
    base = _z(tangibles, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z tangibles
def tb_f38_tangible_book_z_21d_slope_v138_signal(tangibles):
    base = _z(tangibles, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z tangibles
def tb_f38_tangible_book_z_63d_slope_v139_signal(tangibles):
    base = _z(tangibles, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z tangibles
def tb_f38_tangible_book_z_63d_slope_v140_signal(tangibles):
    base = _z(tangibles, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z tangibles
def tb_f38_tangible_book_z_63d_slope_v141_signal(tangibles):
    base = _z(tangibles, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z tangibles
def tb_f38_tangible_book_z_126d_slope_v142_signal(tangibles):
    base = _z(tangibles, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z tangibles
def tb_f38_tangible_book_z_126d_slope_v143_signal(tangibles):
    base = _z(tangibles, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z tangibles
def tb_f38_tangible_book_z_126d_slope_v144_signal(tangibles):
    base = _z(tangibles, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z tangibles
def tb_f38_tangible_book_z_252d_slope_v145_signal(tangibles):
    base = _z(tangibles, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z tangibles
def tb_f38_tangible_book_z_252d_slope_v146_signal(tangibles):
    base = _z(tangibles, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z tangibles
def tb_f38_tangible_book_z_252d_slope_v147_signal(tangibles):
    base = _z(tangibles, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z tangibles
def tb_f38_tangible_book_z_504d_slope_v148_signal(tangibles):
    base = _z(tangibles, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z tangibles
def tb_f38_tangible_book_z_504d_slope_v149_signal(tangibles):
    base = _z(tangibles, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z tangibles
def tb_f38_tangible_book_z_504d_slope_v150_signal(tangibles):
    base = _z(tangibles, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
