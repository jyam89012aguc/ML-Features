"""Family f066 - Asset turnover (Returns and Efficiency) | Sharadar tables: SF1 | fields: assetturnover, revenue, assetsavg | 2nd derivatives 001-150"""
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
def _asset_turnover_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _asset_turnover_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _asset_turnover_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw assetturnover
def at_f066_asset_turnover_raw_21d_slope_v001_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw assetturnover
def at_f066_asset_turnover_raw_21d_slope_v002_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw assetturnover
def at_f066_asset_turnover_raw_21d_slope_v003_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw assetturnover
def at_f066_asset_turnover_raw_63d_slope_v004_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw assetturnover
def at_f066_asset_turnover_raw_63d_slope_v005_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw assetturnover
def at_f066_asset_turnover_raw_63d_slope_v006_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw assetturnover
def at_f066_asset_turnover_raw_126d_slope_v007_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw assetturnover
def at_f066_asset_turnover_raw_126d_slope_v008_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw assetturnover
def at_f066_asset_turnover_raw_126d_slope_v009_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw assetturnover
def at_f066_asset_turnover_raw_252d_slope_v010_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw assetturnover
def at_f066_asset_turnover_raw_252d_slope_v011_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw assetturnover
def at_f066_asset_turnover_raw_252d_slope_v012_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw assetturnover
def at_f066_asset_turnover_raw_504d_slope_v013_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw assetturnover
def at_f066_asset_turnover_raw_504d_slope_v014_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw assetturnover
def at_f066_asset_turnover_raw_504d_slope_v015_signal(assetturnover, closeadj):
    base = _mean(assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log assetturnover
def at_f066_asset_turnover_log_21d_slope_v016_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log assetturnover
def at_f066_asset_turnover_log_21d_slope_v017_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log assetturnover
def at_f066_asset_turnover_log_21d_slope_v018_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log assetturnover
def at_f066_asset_turnover_log_63d_slope_v019_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log assetturnover
def at_f066_asset_turnover_log_63d_slope_v020_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log assetturnover
def at_f066_asset_turnover_log_63d_slope_v021_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log assetturnover
def at_f066_asset_turnover_log_126d_slope_v022_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log assetturnover
def at_f066_asset_turnover_log_126d_slope_v023_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log assetturnover
def at_f066_asset_turnover_log_126d_slope_v024_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log assetturnover
def at_f066_asset_turnover_log_252d_slope_v025_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log assetturnover
def at_f066_asset_turnover_log_252d_slope_v026_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log assetturnover
def at_f066_asset_turnover_log_252d_slope_v027_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log assetturnover
def at_f066_asset_turnover_log_504d_slope_v028_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log assetturnover
def at_f066_asset_turnover_log_504d_slope_v029_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log assetturnover
def at_f066_asset_turnover_log_504d_slope_v030_signal(assetturnover, closeadj):
    base = _mean(_asset_turnover_log(assetturnover), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare assetturnover
def at_f066_asset_turnover_pershare_21d_slope_v031_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare assetturnover
def at_f066_asset_turnover_pershare_21d_slope_v032_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare assetturnover
def at_f066_asset_turnover_pershare_21d_slope_v033_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare assetturnover
def at_f066_asset_turnover_pershare_63d_slope_v034_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare assetturnover
def at_f066_asset_turnover_pershare_63d_slope_v035_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare assetturnover
def at_f066_asset_turnover_pershare_63d_slope_v036_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare assetturnover
def at_f066_asset_turnover_pershare_126d_slope_v037_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare assetturnover
def at_f066_asset_turnover_pershare_126d_slope_v038_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare assetturnover
def at_f066_asset_turnover_pershare_126d_slope_v039_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare assetturnover
def at_f066_asset_turnover_pershare_252d_slope_v040_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare assetturnover
def at_f066_asset_turnover_pershare_252d_slope_v041_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare assetturnover
def at_f066_asset_turnover_pershare_252d_slope_v042_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare assetturnover
def at_f066_asset_turnover_pershare_504d_slope_v043_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare assetturnover
def at_f066_asset_turnover_pershare_504d_slope_v044_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare assetturnover
def at_f066_asset_turnover_pershare_504d_slope_v045_signal(assetturnover, sharesbas, closeadj):
    base = _mean(_asset_turnover_per_share(assetturnover, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_21d_slope_v046_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_21d_slope_v047_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_21d_slope_v048_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_63d_slope_v049_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_63d_slope_v050_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_63d_slope_v051_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_126d_slope_v052_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_126d_slope_v053_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_126d_slope_v054_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_252d_slope_v055_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_252d_slope_v056_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_252d_slope_v057_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_504d_slope_v058_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_504d_slope_v059_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_revenue assetturnover
def at_f066_asset_turnover_per_revenue_504d_slope_v060_signal(assetturnover, revenue):
    base = _mean(_asset_turnover_scaled(assetturnover, revenue), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_21d_slope_v061_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_21d_slope_v062_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_21d_slope_v063_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_63d_slope_v064_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_63d_slope_v065_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_63d_slope_v066_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_126d_slope_v067_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_126d_slope_v068_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_126d_slope_v069_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_252d_slope_v070_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_252d_slope_v071_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_252d_slope_v072_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_504d_slope_v073_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_504d_slope_v074_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assetsavg assetturnover
def at_f066_asset_turnover_per_assetsavg_504d_slope_v075_signal(assetturnover, assetsavg):
    base = _mean(_asset_turnover_scaled(assetturnover, assetsavg), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets assetturnover
def at_f066_asset_turnover_per_assets_21d_slope_v076_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets assetturnover
def at_f066_asset_turnover_per_assets_21d_slope_v077_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets assetturnover
def at_f066_asset_turnover_per_assets_21d_slope_v078_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets assetturnover
def at_f066_asset_turnover_per_assets_63d_slope_v079_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets assetturnover
def at_f066_asset_turnover_per_assets_63d_slope_v080_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets assetturnover
def at_f066_asset_turnover_per_assets_63d_slope_v081_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets assetturnover
def at_f066_asset_turnover_per_assets_126d_slope_v082_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets assetturnover
def at_f066_asset_turnover_per_assets_126d_slope_v083_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets assetturnover
def at_f066_asset_turnover_per_assets_126d_slope_v084_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets assetturnover
def at_f066_asset_turnover_per_assets_252d_slope_v085_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets assetturnover
def at_f066_asset_turnover_per_assets_252d_slope_v086_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets assetturnover
def at_f066_asset_turnover_per_assets_252d_slope_v087_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets assetturnover
def at_f066_asset_turnover_per_assets_504d_slope_v088_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets assetturnover
def at_f066_asset_turnover_per_assets_504d_slope_v089_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets assetturnover
def at_f066_asset_turnover_per_assets_504d_slope_v090_signal(assetturnover, assets):
    base = _mean(_asset_turnover_scaled(assetturnover, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std assetturnover
def at_f066_asset_turnover_std_21d_slope_v091_signal(assetturnover, closeadj):
    base = _std(assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std assetturnover
def at_f066_asset_turnover_std_21d_slope_v092_signal(assetturnover, closeadj):
    base = _std(assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std assetturnover
def at_f066_asset_turnover_std_21d_slope_v093_signal(assetturnover, closeadj):
    base = _std(assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std assetturnover
def at_f066_asset_turnover_std_63d_slope_v094_signal(assetturnover, closeadj):
    base = _std(assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std assetturnover
def at_f066_asset_turnover_std_63d_slope_v095_signal(assetturnover, closeadj):
    base = _std(assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std assetturnover
def at_f066_asset_turnover_std_63d_slope_v096_signal(assetturnover, closeadj):
    base = _std(assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std assetturnover
def at_f066_asset_turnover_std_126d_slope_v097_signal(assetturnover, closeadj):
    base = _std(assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std assetturnover
def at_f066_asset_turnover_std_126d_slope_v098_signal(assetturnover, closeadj):
    base = _std(assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std assetturnover
def at_f066_asset_turnover_std_126d_slope_v099_signal(assetturnover, closeadj):
    base = _std(assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std assetturnover
def at_f066_asset_turnover_std_252d_slope_v100_signal(assetturnover, closeadj):
    base = _std(assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std assetturnover
def at_f066_asset_turnover_std_252d_slope_v101_signal(assetturnover, closeadj):
    base = _std(assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std assetturnover
def at_f066_asset_turnover_std_252d_slope_v102_signal(assetturnover, closeadj):
    base = _std(assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std assetturnover
def at_f066_asset_turnover_std_504d_slope_v103_signal(assetturnover, closeadj):
    base = _std(assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std assetturnover
def at_f066_asset_turnover_std_504d_slope_v104_signal(assetturnover, closeadj):
    base = _std(assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std assetturnover
def at_f066_asset_turnover_std_504d_slope_v105_signal(assetturnover, closeadj):
    base = _std(assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm assetturnover
def at_f066_asset_turnover_ewm_21d_slope_v106_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm assetturnover
def at_f066_asset_turnover_ewm_21d_slope_v107_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm assetturnover
def at_f066_asset_turnover_ewm_21d_slope_v108_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm assetturnover
def at_f066_asset_turnover_ewm_63d_slope_v109_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm assetturnover
def at_f066_asset_turnover_ewm_63d_slope_v110_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm assetturnover
def at_f066_asset_turnover_ewm_63d_slope_v111_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm assetturnover
def at_f066_asset_turnover_ewm_126d_slope_v112_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm assetturnover
def at_f066_asset_turnover_ewm_126d_slope_v113_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm assetturnover
def at_f066_asset_turnover_ewm_126d_slope_v114_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm assetturnover
def at_f066_asset_turnover_ewm_252d_slope_v115_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm assetturnover
def at_f066_asset_turnover_ewm_252d_slope_v116_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm assetturnover
def at_f066_asset_turnover_ewm_252d_slope_v117_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm assetturnover
def at_f066_asset_turnover_ewm_504d_slope_v118_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm assetturnover
def at_f066_asset_turnover_ewm_504d_slope_v119_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm assetturnover
def at_f066_asset_turnover_ewm_504d_slope_v120_signal(assetturnover, closeadj):
    base = assetturnover.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq assetturnover
def at_f066_asset_turnover_sq_21d_slope_v121_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq assetturnover
def at_f066_asset_turnover_sq_21d_slope_v122_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq assetturnover
def at_f066_asset_turnover_sq_21d_slope_v123_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq assetturnover
def at_f066_asset_turnover_sq_63d_slope_v124_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq assetturnover
def at_f066_asset_turnover_sq_63d_slope_v125_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq assetturnover
def at_f066_asset_turnover_sq_63d_slope_v126_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq assetturnover
def at_f066_asset_turnover_sq_126d_slope_v127_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq assetturnover
def at_f066_asset_turnover_sq_126d_slope_v128_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq assetturnover
def at_f066_asset_turnover_sq_126d_slope_v129_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq assetturnover
def at_f066_asset_turnover_sq_252d_slope_v130_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq assetturnover
def at_f066_asset_turnover_sq_252d_slope_v131_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq assetturnover
def at_f066_asset_turnover_sq_252d_slope_v132_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq assetturnover
def at_f066_asset_turnover_sq_504d_slope_v133_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq assetturnover
def at_f066_asset_turnover_sq_504d_slope_v134_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq assetturnover
def at_f066_asset_turnover_sq_504d_slope_v135_signal(assetturnover, closeadj):
    base = _mean(assetturnover * assetturnover, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z assetturnover
def at_f066_asset_turnover_z_21d_slope_v136_signal(assetturnover):
    base = _z(assetturnover, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z assetturnover
def at_f066_asset_turnover_z_21d_slope_v137_signal(assetturnover):
    base = _z(assetturnover, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z assetturnover
def at_f066_asset_turnover_z_21d_slope_v138_signal(assetturnover):
    base = _z(assetturnover, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z assetturnover
def at_f066_asset_turnover_z_63d_slope_v139_signal(assetturnover):
    base = _z(assetturnover, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z assetturnover
def at_f066_asset_turnover_z_63d_slope_v140_signal(assetturnover):
    base = _z(assetturnover, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z assetturnover
def at_f066_asset_turnover_z_63d_slope_v141_signal(assetturnover):
    base = _z(assetturnover, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z assetturnover
def at_f066_asset_turnover_z_126d_slope_v142_signal(assetturnover):
    base = _z(assetturnover, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z assetturnover
def at_f066_asset_turnover_z_126d_slope_v143_signal(assetturnover):
    base = _z(assetturnover, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z assetturnover
def at_f066_asset_turnover_z_126d_slope_v144_signal(assetturnover):
    base = _z(assetturnover, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z assetturnover
def at_f066_asset_turnover_z_252d_slope_v145_signal(assetturnover):
    base = _z(assetturnover, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z assetturnover
def at_f066_asset_turnover_z_252d_slope_v146_signal(assetturnover):
    base = _z(assetturnover, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z assetturnover
def at_f066_asset_turnover_z_252d_slope_v147_signal(assetturnover):
    base = _z(assetturnover, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z assetturnover
def at_f066_asset_turnover_z_504d_slope_v148_signal(assetturnover):
    base = _z(assetturnover, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z assetturnover
def at_f066_asset_turnover_z_504d_slope_v149_signal(assetturnover):
    base = _z(assetturnover, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z assetturnover
def at_f066_asset_turnover_z_504d_slope_v150_signal(assetturnover):
    base = _z(assetturnover, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
