"""Family f91 - Holder count & concentration  (P_Institutional_SF3) | 2nd derivatives 001-150"""
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
def _holder_concentration_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _holder_concentration_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _holder_concentration_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw units
def hc_f91_holder_concentration_raw_21d_slope_v001_signal(units, closeadj):
    base = _mean(units, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw units
def hc_f91_holder_concentration_raw_21d_slope_v002_signal(units, closeadj):
    base = _mean(units, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw units
def hc_f91_holder_concentration_raw_21d_slope_v003_signal(units, closeadj):
    base = _mean(units, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw units
def hc_f91_holder_concentration_raw_63d_slope_v004_signal(units, closeadj):
    base = _mean(units, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw units
def hc_f91_holder_concentration_raw_63d_slope_v005_signal(units, closeadj):
    base = _mean(units, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw units
def hc_f91_holder_concentration_raw_63d_slope_v006_signal(units, closeadj):
    base = _mean(units, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw units
def hc_f91_holder_concentration_raw_126d_slope_v007_signal(units, closeadj):
    base = _mean(units, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw units
def hc_f91_holder_concentration_raw_126d_slope_v008_signal(units, closeadj):
    base = _mean(units, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw units
def hc_f91_holder_concentration_raw_126d_slope_v009_signal(units, closeadj):
    base = _mean(units, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw units
def hc_f91_holder_concentration_raw_252d_slope_v010_signal(units, closeadj):
    base = _mean(units, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw units
def hc_f91_holder_concentration_raw_252d_slope_v011_signal(units, closeadj):
    base = _mean(units, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw units
def hc_f91_holder_concentration_raw_252d_slope_v012_signal(units, closeadj):
    base = _mean(units, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw units
def hc_f91_holder_concentration_raw_504d_slope_v013_signal(units, closeadj):
    base = _mean(units, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw units
def hc_f91_holder_concentration_raw_504d_slope_v014_signal(units, closeadj):
    base = _mean(units, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw units
def hc_f91_holder_concentration_raw_504d_slope_v015_signal(units, closeadj):
    base = _mean(units, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log units
def hc_f91_holder_concentration_log_21d_slope_v016_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log units
def hc_f91_holder_concentration_log_21d_slope_v017_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log units
def hc_f91_holder_concentration_log_21d_slope_v018_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log units
def hc_f91_holder_concentration_log_63d_slope_v019_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log units
def hc_f91_holder_concentration_log_63d_slope_v020_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log units
def hc_f91_holder_concentration_log_63d_slope_v021_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log units
def hc_f91_holder_concentration_log_126d_slope_v022_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log units
def hc_f91_holder_concentration_log_126d_slope_v023_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log units
def hc_f91_holder_concentration_log_126d_slope_v024_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log units
def hc_f91_holder_concentration_log_252d_slope_v025_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log units
def hc_f91_holder_concentration_log_252d_slope_v026_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log units
def hc_f91_holder_concentration_log_252d_slope_v027_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log units
def hc_f91_holder_concentration_log_504d_slope_v028_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log units
def hc_f91_holder_concentration_log_504d_slope_v029_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log units
def hc_f91_holder_concentration_log_504d_slope_v030_signal(units, closeadj):
    base = _mean(_holder_concentration_log(units), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare units
def hc_f91_holder_concentration_pershare_21d_slope_v031_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare units
def hc_f91_holder_concentration_pershare_21d_slope_v032_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare units
def hc_f91_holder_concentration_pershare_21d_slope_v033_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare units
def hc_f91_holder_concentration_pershare_63d_slope_v034_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare units
def hc_f91_holder_concentration_pershare_63d_slope_v035_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare units
def hc_f91_holder_concentration_pershare_63d_slope_v036_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare units
def hc_f91_holder_concentration_pershare_126d_slope_v037_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare units
def hc_f91_holder_concentration_pershare_126d_slope_v038_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare units
def hc_f91_holder_concentration_pershare_126d_slope_v039_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare units
def hc_f91_holder_concentration_pershare_252d_slope_v040_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare units
def hc_f91_holder_concentration_pershare_252d_slope_v041_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare units
def hc_f91_holder_concentration_pershare_252d_slope_v042_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare units
def hc_f91_holder_concentration_pershare_504d_slope_v043_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare units
def hc_f91_holder_concentration_pershare_504d_slope_v044_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare units
def hc_f91_holder_concentration_pershare_504d_slope_v045_signal(units, sharesbas, closeadj):
    base = _mean(_holder_concentration_per_share(units, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets units
def hc_f91_holder_concentration_per_assets_21d_slope_v046_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets units
def hc_f91_holder_concentration_per_assets_21d_slope_v047_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets units
def hc_f91_holder_concentration_per_assets_21d_slope_v048_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets units
def hc_f91_holder_concentration_per_assets_63d_slope_v049_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets units
def hc_f91_holder_concentration_per_assets_63d_slope_v050_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets units
def hc_f91_holder_concentration_per_assets_63d_slope_v051_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets units
def hc_f91_holder_concentration_per_assets_126d_slope_v052_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets units
def hc_f91_holder_concentration_per_assets_126d_slope_v053_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets units
def hc_f91_holder_concentration_per_assets_126d_slope_v054_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets units
def hc_f91_holder_concentration_per_assets_252d_slope_v055_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets units
def hc_f91_holder_concentration_per_assets_252d_slope_v056_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets units
def hc_f91_holder_concentration_per_assets_252d_slope_v057_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets units
def hc_f91_holder_concentration_per_assets_504d_slope_v058_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets units
def hc_f91_holder_concentration_per_assets_504d_slope_v059_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets units
def hc_f91_holder_concentration_per_assets_504d_slope_v060_signal(units, assets):
    base = _mean(_holder_concentration_scaled(units, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_21d_slope_v061_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_21d_slope_v062_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_21d_slope_v063_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_63d_slope_v064_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_63d_slope_v065_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_63d_slope_v066_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_126d_slope_v067_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_126d_slope_v068_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_126d_slope_v069_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_252d_slope_v070_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_252d_slope_v071_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_252d_slope_v072_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_504d_slope_v073_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_504d_slope_v074_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap units
def hc_f91_holder_concentration_per_marketcap_504d_slope_v075_signal(units, marketcap):
    base = _mean(_holder_concentration_scaled(units, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity units
def hc_f91_holder_concentration_per_equity_21d_slope_v076_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity units
def hc_f91_holder_concentration_per_equity_21d_slope_v077_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity units
def hc_f91_holder_concentration_per_equity_21d_slope_v078_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity units
def hc_f91_holder_concentration_per_equity_63d_slope_v079_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity units
def hc_f91_holder_concentration_per_equity_63d_slope_v080_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity units
def hc_f91_holder_concentration_per_equity_63d_slope_v081_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity units
def hc_f91_holder_concentration_per_equity_126d_slope_v082_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity units
def hc_f91_holder_concentration_per_equity_126d_slope_v083_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity units
def hc_f91_holder_concentration_per_equity_126d_slope_v084_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity units
def hc_f91_holder_concentration_per_equity_252d_slope_v085_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity units
def hc_f91_holder_concentration_per_equity_252d_slope_v086_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity units
def hc_f91_holder_concentration_per_equity_252d_slope_v087_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity units
def hc_f91_holder_concentration_per_equity_504d_slope_v088_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity units
def hc_f91_holder_concentration_per_equity_504d_slope_v089_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity units
def hc_f91_holder_concentration_per_equity_504d_slope_v090_signal(units, equity):
    base = _mean(_holder_concentration_scaled(units, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std units
def hc_f91_holder_concentration_std_21d_slope_v091_signal(units, closeadj):
    base = _std(units, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std units
def hc_f91_holder_concentration_std_21d_slope_v092_signal(units, closeadj):
    base = _std(units, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std units
def hc_f91_holder_concentration_std_21d_slope_v093_signal(units, closeadj):
    base = _std(units, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std units
def hc_f91_holder_concentration_std_63d_slope_v094_signal(units, closeadj):
    base = _std(units, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std units
def hc_f91_holder_concentration_std_63d_slope_v095_signal(units, closeadj):
    base = _std(units, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std units
def hc_f91_holder_concentration_std_63d_slope_v096_signal(units, closeadj):
    base = _std(units, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std units
def hc_f91_holder_concentration_std_126d_slope_v097_signal(units, closeadj):
    base = _std(units, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std units
def hc_f91_holder_concentration_std_126d_slope_v098_signal(units, closeadj):
    base = _std(units, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std units
def hc_f91_holder_concentration_std_126d_slope_v099_signal(units, closeadj):
    base = _std(units, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std units
def hc_f91_holder_concentration_std_252d_slope_v100_signal(units, closeadj):
    base = _std(units, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std units
def hc_f91_holder_concentration_std_252d_slope_v101_signal(units, closeadj):
    base = _std(units, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std units
def hc_f91_holder_concentration_std_252d_slope_v102_signal(units, closeadj):
    base = _std(units, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std units
def hc_f91_holder_concentration_std_504d_slope_v103_signal(units, closeadj):
    base = _std(units, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std units
def hc_f91_holder_concentration_std_504d_slope_v104_signal(units, closeadj):
    base = _std(units, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std units
def hc_f91_holder_concentration_std_504d_slope_v105_signal(units, closeadj):
    base = _std(units, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm units
def hc_f91_holder_concentration_ewm_21d_slope_v106_signal(units, closeadj):
    base = units.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm units
def hc_f91_holder_concentration_ewm_21d_slope_v107_signal(units, closeadj):
    base = units.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm units
def hc_f91_holder_concentration_ewm_21d_slope_v108_signal(units, closeadj):
    base = units.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm units
def hc_f91_holder_concentration_ewm_63d_slope_v109_signal(units, closeadj):
    base = units.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm units
def hc_f91_holder_concentration_ewm_63d_slope_v110_signal(units, closeadj):
    base = units.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm units
def hc_f91_holder_concentration_ewm_63d_slope_v111_signal(units, closeadj):
    base = units.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm units
def hc_f91_holder_concentration_ewm_126d_slope_v112_signal(units, closeadj):
    base = units.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm units
def hc_f91_holder_concentration_ewm_126d_slope_v113_signal(units, closeadj):
    base = units.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm units
def hc_f91_holder_concentration_ewm_126d_slope_v114_signal(units, closeadj):
    base = units.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm units
def hc_f91_holder_concentration_ewm_252d_slope_v115_signal(units, closeadj):
    base = units.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm units
def hc_f91_holder_concentration_ewm_252d_slope_v116_signal(units, closeadj):
    base = units.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm units
def hc_f91_holder_concentration_ewm_252d_slope_v117_signal(units, closeadj):
    base = units.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm units
def hc_f91_holder_concentration_ewm_504d_slope_v118_signal(units, closeadj):
    base = units.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm units
def hc_f91_holder_concentration_ewm_504d_slope_v119_signal(units, closeadj):
    base = units.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm units
def hc_f91_holder_concentration_ewm_504d_slope_v120_signal(units, closeadj):
    base = units.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq units
def hc_f91_holder_concentration_sq_21d_slope_v121_signal(units, closeadj):
    base = _mean(units * units, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq units
def hc_f91_holder_concentration_sq_21d_slope_v122_signal(units, closeadj):
    base = _mean(units * units, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq units
def hc_f91_holder_concentration_sq_21d_slope_v123_signal(units, closeadj):
    base = _mean(units * units, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq units
def hc_f91_holder_concentration_sq_63d_slope_v124_signal(units, closeadj):
    base = _mean(units * units, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq units
def hc_f91_holder_concentration_sq_63d_slope_v125_signal(units, closeadj):
    base = _mean(units * units, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq units
def hc_f91_holder_concentration_sq_63d_slope_v126_signal(units, closeadj):
    base = _mean(units * units, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq units
def hc_f91_holder_concentration_sq_126d_slope_v127_signal(units, closeadj):
    base = _mean(units * units, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq units
def hc_f91_holder_concentration_sq_126d_slope_v128_signal(units, closeadj):
    base = _mean(units * units, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq units
def hc_f91_holder_concentration_sq_126d_slope_v129_signal(units, closeadj):
    base = _mean(units * units, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq units
def hc_f91_holder_concentration_sq_252d_slope_v130_signal(units, closeadj):
    base = _mean(units * units, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq units
def hc_f91_holder_concentration_sq_252d_slope_v131_signal(units, closeadj):
    base = _mean(units * units, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq units
def hc_f91_holder_concentration_sq_252d_slope_v132_signal(units, closeadj):
    base = _mean(units * units, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq units
def hc_f91_holder_concentration_sq_504d_slope_v133_signal(units, closeadj):
    base = _mean(units * units, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq units
def hc_f91_holder_concentration_sq_504d_slope_v134_signal(units, closeadj):
    base = _mean(units * units, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq units
def hc_f91_holder_concentration_sq_504d_slope_v135_signal(units, closeadj):
    base = _mean(units * units, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z units
def hc_f91_holder_concentration_z_21d_slope_v136_signal(units):
    base = _z(units, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z units
def hc_f91_holder_concentration_z_21d_slope_v137_signal(units):
    base = _z(units, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z units
def hc_f91_holder_concentration_z_21d_slope_v138_signal(units):
    base = _z(units, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z units
def hc_f91_holder_concentration_z_63d_slope_v139_signal(units):
    base = _z(units, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z units
def hc_f91_holder_concentration_z_63d_slope_v140_signal(units):
    base = _z(units, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z units
def hc_f91_holder_concentration_z_63d_slope_v141_signal(units):
    base = _z(units, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z units
def hc_f91_holder_concentration_z_126d_slope_v142_signal(units):
    base = _z(units, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z units
def hc_f91_holder_concentration_z_126d_slope_v143_signal(units):
    base = _z(units, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z units
def hc_f91_holder_concentration_z_126d_slope_v144_signal(units):
    base = _z(units, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z units
def hc_f91_holder_concentration_z_252d_slope_v145_signal(units):
    base = _z(units, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z units
def hc_f91_holder_concentration_z_252d_slope_v146_signal(units):
    base = _z(units, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z units
def hc_f91_holder_concentration_z_252d_slope_v147_signal(units):
    base = _z(units, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z units
def hc_f91_holder_concentration_z_504d_slope_v148_signal(units):
    base = _z(units, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z units
def hc_f91_holder_concentration_z_504d_slope_v149_signal(units):
    base = _z(units, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z units
def hc_f91_holder_concentration_z_504d_slope_v150_signal(units):
    base = _z(units, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
