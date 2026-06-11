"""Family f59 - ROA / ROE / ROIC  (J_Returns_Efficiency) | 2nd derivatives 001-150"""
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
def _returns_family_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _returns_family_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _returns_family_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw roa
def rf_f59_returns_family_raw_21d_slope_v001_signal(roa, closeadj):
    base = _mean(roa, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw roa
def rf_f59_returns_family_raw_21d_slope_v002_signal(roa, closeadj):
    base = _mean(roa, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw roa
def rf_f59_returns_family_raw_21d_slope_v003_signal(roa, closeadj):
    base = _mean(roa, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw roa
def rf_f59_returns_family_raw_63d_slope_v004_signal(roa, closeadj):
    base = _mean(roa, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw roa
def rf_f59_returns_family_raw_63d_slope_v005_signal(roa, closeadj):
    base = _mean(roa, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw roa
def rf_f59_returns_family_raw_63d_slope_v006_signal(roa, closeadj):
    base = _mean(roa, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw roa
def rf_f59_returns_family_raw_126d_slope_v007_signal(roa, closeadj):
    base = _mean(roa, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw roa
def rf_f59_returns_family_raw_126d_slope_v008_signal(roa, closeadj):
    base = _mean(roa, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw roa
def rf_f59_returns_family_raw_126d_slope_v009_signal(roa, closeadj):
    base = _mean(roa, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw roa
def rf_f59_returns_family_raw_252d_slope_v010_signal(roa, closeadj):
    base = _mean(roa, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw roa
def rf_f59_returns_family_raw_252d_slope_v011_signal(roa, closeadj):
    base = _mean(roa, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw roa
def rf_f59_returns_family_raw_252d_slope_v012_signal(roa, closeadj):
    base = _mean(roa, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw roa
def rf_f59_returns_family_raw_504d_slope_v013_signal(roa, closeadj):
    base = _mean(roa, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw roa
def rf_f59_returns_family_raw_504d_slope_v014_signal(roa, closeadj):
    base = _mean(roa, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw roa
def rf_f59_returns_family_raw_504d_slope_v015_signal(roa, closeadj):
    base = _mean(roa, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log roa
def rf_f59_returns_family_log_21d_slope_v016_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log roa
def rf_f59_returns_family_log_21d_slope_v017_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log roa
def rf_f59_returns_family_log_21d_slope_v018_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log roa
def rf_f59_returns_family_log_63d_slope_v019_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log roa
def rf_f59_returns_family_log_63d_slope_v020_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log roa
def rf_f59_returns_family_log_63d_slope_v021_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log roa
def rf_f59_returns_family_log_126d_slope_v022_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log roa
def rf_f59_returns_family_log_126d_slope_v023_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log roa
def rf_f59_returns_family_log_126d_slope_v024_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log roa
def rf_f59_returns_family_log_252d_slope_v025_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log roa
def rf_f59_returns_family_log_252d_slope_v026_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log roa
def rf_f59_returns_family_log_252d_slope_v027_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log roa
def rf_f59_returns_family_log_504d_slope_v028_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log roa
def rf_f59_returns_family_log_504d_slope_v029_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log roa
def rf_f59_returns_family_log_504d_slope_v030_signal(roa, closeadj):
    base = _mean(_returns_family_log(roa), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare roa
def rf_f59_returns_family_pershare_21d_slope_v031_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare roa
def rf_f59_returns_family_pershare_21d_slope_v032_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare roa
def rf_f59_returns_family_pershare_21d_slope_v033_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare roa
def rf_f59_returns_family_pershare_63d_slope_v034_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare roa
def rf_f59_returns_family_pershare_63d_slope_v035_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare roa
def rf_f59_returns_family_pershare_63d_slope_v036_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare roa
def rf_f59_returns_family_pershare_126d_slope_v037_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare roa
def rf_f59_returns_family_pershare_126d_slope_v038_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare roa
def rf_f59_returns_family_pershare_126d_slope_v039_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare roa
def rf_f59_returns_family_pershare_252d_slope_v040_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare roa
def rf_f59_returns_family_pershare_252d_slope_v041_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare roa
def rf_f59_returns_family_pershare_252d_slope_v042_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare roa
def rf_f59_returns_family_pershare_504d_slope_v043_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare roa
def rf_f59_returns_family_pershare_504d_slope_v044_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare roa
def rf_f59_returns_family_pershare_504d_slope_v045_signal(roa, sharesbas, closeadj):
    base = _mean(_returns_family_per_share(roa, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets roa
def rf_f59_returns_family_per_assets_21d_slope_v046_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets roa
def rf_f59_returns_family_per_assets_21d_slope_v047_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets roa
def rf_f59_returns_family_per_assets_21d_slope_v048_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets roa
def rf_f59_returns_family_per_assets_63d_slope_v049_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets roa
def rf_f59_returns_family_per_assets_63d_slope_v050_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets roa
def rf_f59_returns_family_per_assets_63d_slope_v051_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets roa
def rf_f59_returns_family_per_assets_126d_slope_v052_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets roa
def rf_f59_returns_family_per_assets_126d_slope_v053_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets roa
def rf_f59_returns_family_per_assets_126d_slope_v054_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets roa
def rf_f59_returns_family_per_assets_252d_slope_v055_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets roa
def rf_f59_returns_family_per_assets_252d_slope_v056_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets roa
def rf_f59_returns_family_per_assets_252d_slope_v057_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets roa
def rf_f59_returns_family_per_assets_504d_slope_v058_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets roa
def rf_f59_returns_family_per_assets_504d_slope_v059_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets roa
def rf_f59_returns_family_per_assets_504d_slope_v060_signal(roa, assets):
    base = _mean(_returns_family_scaled(roa, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap roa
def rf_f59_returns_family_per_marketcap_21d_slope_v061_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap roa
def rf_f59_returns_family_per_marketcap_21d_slope_v062_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap roa
def rf_f59_returns_family_per_marketcap_21d_slope_v063_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap roa
def rf_f59_returns_family_per_marketcap_63d_slope_v064_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap roa
def rf_f59_returns_family_per_marketcap_63d_slope_v065_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap roa
def rf_f59_returns_family_per_marketcap_63d_slope_v066_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap roa
def rf_f59_returns_family_per_marketcap_126d_slope_v067_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap roa
def rf_f59_returns_family_per_marketcap_126d_slope_v068_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap roa
def rf_f59_returns_family_per_marketcap_126d_slope_v069_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap roa
def rf_f59_returns_family_per_marketcap_252d_slope_v070_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap roa
def rf_f59_returns_family_per_marketcap_252d_slope_v071_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap roa
def rf_f59_returns_family_per_marketcap_252d_slope_v072_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap roa
def rf_f59_returns_family_per_marketcap_504d_slope_v073_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap roa
def rf_f59_returns_family_per_marketcap_504d_slope_v074_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap roa
def rf_f59_returns_family_per_marketcap_504d_slope_v075_signal(roa, marketcap):
    base = _mean(_returns_family_scaled(roa, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity roa
def rf_f59_returns_family_per_equity_21d_slope_v076_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity roa
def rf_f59_returns_family_per_equity_21d_slope_v077_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity roa
def rf_f59_returns_family_per_equity_21d_slope_v078_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity roa
def rf_f59_returns_family_per_equity_63d_slope_v079_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity roa
def rf_f59_returns_family_per_equity_63d_slope_v080_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity roa
def rf_f59_returns_family_per_equity_63d_slope_v081_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity roa
def rf_f59_returns_family_per_equity_126d_slope_v082_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity roa
def rf_f59_returns_family_per_equity_126d_slope_v083_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity roa
def rf_f59_returns_family_per_equity_126d_slope_v084_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity roa
def rf_f59_returns_family_per_equity_252d_slope_v085_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity roa
def rf_f59_returns_family_per_equity_252d_slope_v086_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity roa
def rf_f59_returns_family_per_equity_252d_slope_v087_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity roa
def rf_f59_returns_family_per_equity_504d_slope_v088_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity roa
def rf_f59_returns_family_per_equity_504d_slope_v089_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity roa
def rf_f59_returns_family_per_equity_504d_slope_v090_signal(roa, equity):
    base = _mean(_returns_family_scaled(roa, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std roa
def rf_f59_returns_family_std_21d_slope_v091_signal(roa, closeadj):
    base = _std(roa, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std roa
def rf_f59_returns_family_std_21d_slope_v092_signal(roa, closeadj):
    base = _std(roa, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std roa
def rf_f59_returns_family_std_21d_slope_v093_signal(roa, closeadj):
    base = _std(roa, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std roa
def rf_f59_returns_family_std_63d_slope_v094_signal(roa, closeadj):
    base = _std(roa, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std roa
def rf_f59_returns_family_std_63d_slope_v095_signal(roa, closeadj):
    base = _std(roa, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std roa
def rf_f59_returns_family_std_63d_slope_v096_signal(roa, closeadj):
    base = _std(roa, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std roa
def rf_f59_returns_family_std_126d_slope_v097_signal(roa, closeadj):
    base = _std(roa, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std roa
def rf_f59_returns_family_std_126d_slope_v098_signal(roa, closeadj):
    base = _std(roa, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std roa
def rf_f59_returns_family_std_126d_slope_v099_signal(roa, closeadj):
    base = _std(roa, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std roa
def rf_f59_returns_family_std_252d_slope_v100_signal(roa, closeadj):
    base = _std(roa, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std roa
def rf_f59_returns_family_std_252d_slope_v101_signal(roa, closeadj):
    base = _std(roa, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std roa
def rf_f59_returns_family_std_252d_slope_v102_signal(roa, closeadj):
    base = _std(roa, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std roa
def rf_f59_returns_family_std_504d_slope_v103_signal(roa, closeadj):
    base = _std(roa, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std roa
def rf_f59_returns_family_std_504d_slope_v104_signal(roa, closeadj):
    base = _std(roa, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std roa
def rf_f59_returns_family_std_504d_slope_v105_signal(roa, closeadj):
    base = _std(roa, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm roa
def rf_f59_returns_family_ewm_21d_slope_v106_signal(roa, closeadj):
    base = roa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm roa
def rf_f59_returns_family_ewm_21d_slope_v107_signal(roa, closeadj):
    base = roa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm roa
def rf_f59_returns_family_ewm_21d_slope_v108_signal(roa, closeadj):
    base = roa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm roa
def rf_f59_returns_family_ewm_63d_slope_v109_signal(roa, closeadj):
    base = roa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm roa
def rf_f59_returns_family_ewm_63d_slope_v110_signal(roa, closeadj):
    base = roa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm roa
def rf_f59_returns_family_ewm_63d_slope_v111_signal(roa, closeadj):
    base = roa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm roa
def rf_f59_returns_family_ewm_126d_slope_v112_signal(roa, closeadj):
    base = roa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm roa
def rf_f59_returns_family_ewm_126d_slope_v113_signal(roa, closeadj):
    base = roa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm roa
def rf_f59_returns_family_ewm_126d_slope_v114_signal(roa, closeadj):
    base = roa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm roa
def rf_f59_returns_family_ewm_252d_slope_v115_signal(roa, closeadj):
    base = roa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm roa
def rf_f59_returns_family_ewm_252d_slope_v116_signal(roa, closeadj):
    base = roa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm roa
def rf_f59_returns_family_ewm_252d_slope_v117_signal(roa, closeadj):
    base = roa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm roa
def rf_f59_returns_family_ewm_504d_slope_v118_signal(roa, closeadj):
    base = roa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm roa
def rf_f59_returns_family_ewm_504d_slope_v119_signal(roa, closeadj):
    base = roa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm roa
def rf_f59_returns_family_ewm_504d_slope_v120_signal(roa, closeadj):
    base = roa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq roa
def rf_f59_returns_family_sq_21d_slope_v121_signal(roa, closeadj):
    base = _mean(roa * roa, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq roa
def rf_f59_returns_family_sq_21d_slope_v122_signal(roa, closeadj):
    base = _mean(roa * roa, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq roa
def rf_f59_returns_family_sq_21d_slope_v123_signal(roa, closeadj):
    base = _mean(roa * roa, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq roa
def rf_f59_returns_family_sq_63d_slope_v124_signal(roa, closeadj):
    base = _mean(roa * roa, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq roa
def rf_f59_returns_family_sq_63d_slope_v125_signal(roa, closeadj):
    base = _mean(roa * roa, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq roa
def rf_f59_returns_family_sq_63d_slope_v126_signal(roa, closeadj):
    base = _mean(roa * roa, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq roa
def rf_f59_returns_family_sq_126d_slope_v127_signal(roa, closeadj):
    base = _mean(roa * roa, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq roa
def rf_f59_returns_family_sq_126d_slope_v128_signal(roa, closeadj):
    base = _mean(roa * roa, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq roa
def rf_f59_returns_family_sq_126d_slope_v129_signal(roa, closeadj):
    base = _mean(roa * roa, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq roa
def rf_f59_returns_family_sq_252d_slope_v130_signal(roa, closeadj):
    base = _mean(roa * roa, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq roa
def rf_f59_returns_family_sq_252d_slope_v131_signal(roa, closeadj):
    base = _mean(roa * roa, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq roa
def rf_f59_returns_family_sq_252d_slope_v132_signal(roa, closeadj):
    base = _mean(roa * roa, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq roa
def rf_f59_returns_family_sq_504d_slope_v133_signal(roa, closeadj):
    base = _mean(roa * roa, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq roa
def rf_f59_returns_family_sq_504d_slope_v134_signal(roa, closeadj):
    base = _mean(roa * roa, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq roa
def rf_f59_returns_family_sq_504d_slope_v135_signal(roa, closeadj):
    base = _mean(roa * roa, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z roa
def rf_f59_returns_family_z_21d_slope_v136_signal(roa):
    base = _z(roa, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z roa
def rf_f59_returns_family_z_21d_slope_v137_signal(roa):
    base = _z(roa, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z roa
def rf_f59_returns_family_z_21d_slope_v138_signal(roa):
    base = _z(roa, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z roa
def rf_f59_returns_family_z_63d_slope_v139_signal(roa):
    base = _z(roa, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z roa
def rf_f59_returns_family_z_63d_slope_v140_signal(roa):
    base = _z(roa, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z roa
def rf_f59_returns_family_z_63d_slope_v141_signal(roa):
    base = _z(roa, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z roa
def rf_f59_returns_family_z_126d_slope_v142_signal(roa):
    base = _z(roa, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z roa
def rf_f59_returns_family_z_126d_slope_v143_signal(roa):
    base = _z(roa, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z roa
def rf_f59_returns_family_z_126d_slope_v144_signal(roa):
    base = _z(roa, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z roa
def rf_f59_returns_family_z_252d_slope_v145_signal(roa):
    base = _z(roa, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z roa
def rf_f59_returns_family_z_252d_slope_v146_signal(roa):
    base = _z(roa, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z roa
def rf_f59_returns_family_z_252d_slope_v147_signal(roa):
    base = _z(roa, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z roa
def rf_f59_returns_family_z_504d_slope_v148_signal(roa):
    base = _z(roa, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z roa
def rf_f59_returns_family_z_504d_slope_v149_signal(roa):
    base = _z(roa, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z roa
def rf_f59_returns_family_z_504d_slope_v150_signal(roa):
    base = _z(roa, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
