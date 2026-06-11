"""Family f25 - Accumulated deficit / deficit funding  (D_Capital_Debt) | 2nd derivatives 001-150"""
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
def _accumulated_deficit_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _accumulated_deficit_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _accumulated_deficit_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw retearn
def ad_f25_accumulated_deficit_raw_21d_slope_v001_signal(retearn, closeadj):
    base = _mean(retearn, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw retearn
def ad_f25_accumulated_deficit_raw_21d_slope_v002_signal(retearn, closeadj):
    base = _mean(retearn, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw retearn
def ad_f25_accumulated_deficit_raw_21d_slope_v003_signal(retearn, closeadj):
    base = _mean(retearn, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw retearn
def ad_f25_accumulated_deficit_raw_63d_slope_v004_signal(retearn, closeadj):
    base = _mean(retearn, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw retearn
def ad_f25_accumulated_deficit_raw_63d_slope_v005_signal(retearn, closeadj):
    base = _mean(retearn, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw retearn
def ad_f25_accumulated_deficit_raw_63d_slope_v006_signal(retearn, closeadj):
    base = _mean(retearn, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw retearn
def ad_f25_accumulated_deficit_raw_126d_slope_v007_signal(retearn, closeadj):
    base = _mean(retearn, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw retearn
def ad_f25_accumulated_deficit_raw_126d_slope_v008_signal(retearn, closeadj):
    base = _mean(retearn, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw retearn
def ad_f25_accumulated_deficit_raw_126d_slope_v009_signal(retearn, closeadj):
    base = _mean(retearn, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw retearn
def ad_f25_accumulated_deficit_raw_252d_slope_v010_signal(retearn, closeadj):
    base = _mean(retearn, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw retearn
def ad_f25_accumulated_deficit_raw_252d_slope_v011_signal(retearn, closeadj):
    base = _mean(retearn, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw retearn
def ad_f25_accumulated_deficit_raw_252d_slope_v012_signal(retearn, closeadj):
    base = _mean(retearn, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw retearn
def ad_f25_accumulated_deficit_raw_504d_slope_v013_signal(retearn, closeadj):
    base = _mean(retearn, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw retearn
def ad_f25_accumulated_deficit_raw_504d_slope_v014_signal(retearn, closeadj):
    base = _mean(retearn, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw retearn
def ad_f25_accumulated_deficit_raw_504d_slope_v015_signal(retearn, closeadj):
    base = _mean(retearn, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log retearn
def ad_f25_accumulated_deficit_log_21d_slope_v016_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log retearn
def ad_f25_accumulated_deficit_log_21d_slope_v017_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log retearn
def ad_f25_accumulated_deficit_log_21d_slope_v018_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log retearn
def ad_f25_accumulated_deficit_log_63d_slope_v019_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log retearn
def ad_f25_accumulated_deficit_log_63d_slope_v020_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log retearn
def ad_f25_accumulated_deficit_log_63d_slope_v021_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log retearn
def ad_f25_accumulated_deficit_log_126d_slope_v022_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log retearn
def ad_f25_accumulated_deficit_log_126d_slope_v023_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log retearn
def ad_f25_accumulated_deficit_log_126d_slope_v024_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log retearn
def ad_f25_accumulated_deficit_log_252d_slope_v025_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log retearn
def ad_f25_accumulated_deficit_log_252d_slope_v026_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log retearn
def ad_f25_accumulated_deficit_log_252d_slope_v027_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log retearn
def ad_f25_accumulated_deficit_log_504d_slope_v028_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log retearn
def ad_f25_accumulated_deficit_log_504d_slope_v029_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log retearn
def ad_f25_accumulated_deficit_log_504d_slope_v030_signal(retearn, closeadj):
    base = _mean(_accumulated_deficit_log(retearn), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare retearn
def ad_f25_accumulated_deficit_pershare_21d_slope_v031_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare retearn
def ad_f25_accumulated_deficit_pershare_21d_slope_v032_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare retearn
def ad_f25_accumulated_deficit_pershare_21d_slope_v033_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare retearn
def ad_f25_accumulated_deficit_pershare_63d_slope_v034_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare retearn
def ad_f25_accumulated_deficit_pershare_63d_slope_v035_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare retearn
def ad_f25_accumulated_deficit_pershare_63d_slope_v036_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare retearn
def ad_f25_accumulated_deficit_pershare_126d_slope_v037_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare retearn
def ad_f25_accumulated_deficit_pershare_126d_slope_v038_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare retearn
def ad_f25_accumulated_deficit_pershare_126d_slope_v039_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare retearn
def ad_f25_accumulated_deficit_pershare_252d_slope_v040_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare retearn
def ad_f25_accumulated_deficit_pershare_252d_slope_v041_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare retearn
def ad_f25_accumulated_deficit_pershare_252d_slope_v042_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare retearn
def ad_f25_accumulated_deficit_pershare_504d_slope_v043_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare retearn
def ad_f25_accumulated_deficit_pershare_504d_slope_v044_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare retearn
def ad_f25_accumulated_deficit_pershare_504d_slope_v045_signal(retearn, sharesbas, closeadj):
    base = _mean(_accumulated_deficit_per_share(retearn, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_21d_slope_v046_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_21d_slope_v047_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_21d_slope_v048_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_63d_slope_v049_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_63d_slope_v050_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_63d_slope_v051_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_126d_slope_v052_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_126d_slope_v053_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_126d_slope_v054_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_252d_slope_v055_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_252d_slope_v056_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_252d_slope_v057_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_504d_slope_v058_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_504d_slope_v059_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets retearn
def ad_f25_accumulated_deficit_per_assets_504d_slope_v060_signal(retearn, assets):
    base = _mean(_accumulated_deficit_scaled(retearn, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_21d_slope_v061_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_21d_slope_v062_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_21d_slope_v063_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_63d_slope_v064_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_63d_slope_v065_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_63d_slope_v066_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_126d_slope_v067_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_126d_slope_v068_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_126d_slope_v069_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_252d_slope_v070_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_252d_slope_v071_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_252d_slope_v072_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_504d_slope_v073_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_504d_slope_v074_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap retearn
def ad_f25_accumulated_deficit_per_marketcap_504d_slope_v075_signal(retearn, marketcap):
    base = _mean(_accumulated_deficit_scaled(retearn, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_21d_slope_v076_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_21d_slope_v077_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_21d_slope_v078_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_63d_slope_v079_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_63d_slope_v080_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_63d_slope_v081_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_126d_slope_v082_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_126d_slope_v083_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_126d_slope_v084_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_252d_slope_v085_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_252d_slope_v086_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_252d_slope_v087_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_504d_slope_v088_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_504d_slope_v089_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity retearn
def ad_f25_accumulated_deficit_per_equity_504d_slope_v090_signal(retearn, equity):
    base = _mean(_accumulated_deficit_scaled(retearn, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std retearn
def ad_f25_accumulated_deficit_std_21d_slope_v091_signal(retearn, closeadj):
    base = _std(retearn, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std retearn
def ad_f25_accumulated_deficit_std_21d_slope_v092_signal(retearn, closeadj):
    base = _std(retearn, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std retearn
def ad_f25_accumulated_deficit_std_21d_slope_v093_signal(retearn, closeadj):
    base = _std(retearn, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std retearn
def ad_f25_accumulated_deficit_std_63d_slope_v094_signal(retearn, closeadj):
    base = _std(retearn, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std retearn
def ad_f25_accumulated_deficit_std_63d_slope_v095_signal(retearn, closeadj):
    base = _std(retearn, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std retearn
def ad_f25_accumulated_deficit_std_63d_slope_v096_signal(retearn, closeadj):
    base = _std(retearn, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std retearn
def ad_f25_accumulated_deficit_std_126d_slope_v097_signal(retearn, closeadj):
    base = _std(retearn, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std retearn
def ad_f25_accumulated_deficit_std_126d_slope_v098_signal(retearn, closeadj):
    base = _std(retearn, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std retearn
def ad_f25_accumulated_deficit_std_126d_slope_v099_signal(retearn, closeadj):
    base = _std(retearn, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std retearn
def ad_f25_accumulated_deficit_std_252d_slope_v100_signal(retearn, closeadj):
    base = _std(retearn, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std retearn
def ad_f25_accumulated_deficit_std_252d_slope_v101_signal(retearn, closeadj):
    base = _std(retearn, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std retearn
def ad_f25_accumulated_deficit_std_252d_slope_v102_signal(retearn, closeadj):
    base = _std(retearn, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std retearn
def ad_f25_accumulated_deficit_std_504d_slope_v103_signal(retearn, closeadj):
    base = _std(retearn, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std retearn
def ad_f25_accumulated_deficit_std_504d_slope_v104_signal(retearn, closeadj):
    base = _std(retearn, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std retearn
def ad_f25_accumulated_deficit_std_504d_slope_v105_signal(retearn, closeadj):
    base = _std(retearn, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm retearn
def ad_f25_accumulated_deficit_ewm_21d_slope_v106_signal(retearn, closeadj):
    base = retearn.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm retearn
def ad_f25_accumulated_deficit_ewm_21d_slope_v107_signal(retearn, closeadj):
    base = retearn.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm retearn
def ad_f25_accumulated_deficit_ewm_21d_slope_v108_signal(retearn, closeadj):
    base = retearn.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm retearn
def ad_f25_accumulated_deficit_ewm_63d_slope_v109_signal(retearn, closeadj):
    base = retearn.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm retearn
def ad_f25_accumulated_deficit_ewm_63d_slope_v110_signal(retearn, closeadj):
    base = retearn.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm retearn
def ad_f25_accumulated_deficit_ewm_63d_slope_v111_signal(retearn, closeadj):
    base = retearn.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm retearn
def ad_f25_accumulated_deficit_ewm_126d_slope_v112_signal(retearn, closeadj):
    base = retearn.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm retearn
def ad_f25_accumulated_deficit_ewm_126d_slope_v113_signal(retearn, closeadj):
    base = retearn.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm retearn
def ad_f25_accumulated_deficit_ewm_126d_slope_v114_signal(retearn, closeadj):
    base = retearn.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm retearn
def ad_f25_accumulated_deficit_ewm_252d_slope_v115_signal(retearn, closeadj):
    base = retearn.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm retearn
def ad_f25_accumulated_deficit_ewm_252d_slope_v116_signal(retearn, closeadj):
    base = retearn.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm retearn
def ad_f25_accumulated_deficit_ewm_252d_slope_v117_signal(retearn, closeadj):
    base = retearn.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm retearn
def ad_f25_accumulated_deficit_ewm_504d_slope_v118_signal(retearn, closeadj):
    base = retearn.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm retearn
def ad_f25_accumulated_deficit_ewm_504d_slope_v119_signal(retearn, closeadj):
    base = retearn.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm retearn
def ad_f25_accumulated_deficit_ewm_504d_slope_v120_signal(retearn, closeadj):
    base = retearn.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq retearn
def ad_f25_accumulated_deficit_sq_21d_slope_v121_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq retearn
def ad_f25_accumulated_deficit_sq_21d_slope_v122_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq retearn
def ad_f25_accumulated_deficit_sq_21d_slope_v123_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq retearn
def ad_f25_accumulated_deficit_sq_63d_slope_v124_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq retearn
def ad_f25_accumulated_deficit_sq_63d_slope_v125_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq retearn
def ad_f25_accumulated_deficit_sq_63d_slope_v126_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq retearn
def ad_f25_accumulated_deficit_sq_126d_slope_v127_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq retearn
def ad_f25_accumulated_deficit_sq_126d_slope_v128_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq retearn
def ad_f25_accumulated_deficit_sq_126d_slope_v129_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq retearn
def ad_f25_accumulated_deficit_sq_252d_slope_v130_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq retearn
def ad_f25_accumulated_deficit_sq_252d_slope_v131_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq retearn
def ad_f25_accumulated_deficit_sq_252d_slope_v132_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq retearn
def ad_f25_accumulated_deficit_sq_504d_slope_v133_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq retearn
def ad_f25_accumulated_deficit_sq_504d_slope_v134_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq retearn
def ad_f25_accumulated_deficit_sq_504d_slope_v135_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z retearn
def ad_f25_accumulated_deficit_z_21d_slope_v136_signal(retearn):
    base = _z(retearn, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z retearn
def ad_f25_accumulated_deficit_z_21d_slope_v137_signal(retearn):
    base = _z(retearn, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z retearn
def ad_f25_accumulated_deficit_z_21d_slope_v138_signal(retearn):
    base = _z(retearn, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z retearn
def ad_f25_accumulated_deficit_z_63d_slope_v139_signal(retearn):
    base = _z(retearn, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z retearn
def ad_f25_accumulated_deficit_z_63d_slope_v140_signal(retearn):
    base = _z(retearn, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z retearn
def ad_f25_accumulated_deficit_z_63d_slope_v141_signal(retearn):
    base = _z(retearn, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z retearn
def ad_f25_accumulated_deficit_z_126d_slope_v142_signal(retearn):
    base = _z(retearn, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z retearn
def ad_f25_accumulated_deficit_z_126d_slope_v143_signal(retearn):
    base = _z(retearn, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z retearn
def ad_f25_accumulated_deficit_z_126d_slope_v144_signal(retearn):
    base = _z(retearn, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z retearn
def ad_f25_accumulated_deficit_z_252d_slope_v145_signal(retearn):
    base = _z(retearn, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z retearn
def ad_f25_accumulated_deficit_z_252d_slope_v146_signal(retearn):
    base = _z(retearn, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z retearn
def ad_f25_accumulated_deficit_z_252d_slope_v147_signal(retearn):
    base = _z(retearn, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z retearn
def ad_f25_accumulated_deficit_z_504d_slope_v148_signal(retearn):
    base = _z(retearn, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z retearn
def ad_f25_accumulated_deficit_z_504d_slope_v149_signal(retearn):
    base = _z(retearn, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z retearn
def ad_f25_accumulated_deficit_z_504d_slope_v150_signal(retearn):
    base = _z(retearn, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
