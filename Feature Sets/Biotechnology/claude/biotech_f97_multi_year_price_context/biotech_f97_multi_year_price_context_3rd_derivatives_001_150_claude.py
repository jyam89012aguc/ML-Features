"""Family f97 - Multi-year price context  (R_Price_Context) | 3rd derivatives 001-150"""
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
def _multi_year_price_context_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _multi_year_price_context_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _multi_year_price_context_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw close
def mpc_f97_multi_year_price_context_raw_21d_accel_v001_signal(close, closeadj):
    base = _mean(close, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw close
def mpc_f97_multi_year_price_context_raw_21d_accel_v002_signal(close, closeadj):
    base = _mean(close, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw close
def mpc_f97_multi_year_price_context_raw_21d_accel_v003_signal(close, closeadj):
    base = _mean(close, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw close
def mpc_f97_multi_year_price_context_raw_63d_accel_v004_signal(close, closeadj):
    base = _mean(close, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw close
def mpc_f97_multi_year_price_context_raw_63d_accel_v005_signal(close, closeadj):
    base = _mean(close, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw close
def mpc_f97_multi_year_price_context_raw_63d_accel_v006_signal(close, closeadj):
    base = _mean(close, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw close
def mpc_f97_multi_year_price_context_raw_126d_accel_v007_signal(close, closeadj):
    base = _mean(close, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw close
def mpc_f97_multi_year_price_context_raw_126d_accel_v008_signal(close, closeadj):
    base = _mean(close, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw close
def mpc_f97_multi_year_price_context_raw_126d_accel_v009_signal(close, closeadj):
    base = _mean(close, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw close
def mpc_f97_multi_year_price_context_raw_252d_accel_v010_signal(close, closeadj):
    base = _mean(close, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw close
def mpc_f97_multi_year_price_context_raw_252d_accel_v011_signal(close, closeadj):
    base = _mean(close, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw close
def mpc_f97_multi_year_price_context_raw_252d_accel_v012_signal(close, closeadj):
    base = _mean(close, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw close
def mpc_f97_multi_year_price_context_raw_504d_accel_v013_signal(close, closeadj):
    base = _mean(close, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw close
def mpc_f97_multi_year_price_context_raw_504d_accel_v014_signal(close, closeadj):
    base = _mean(close, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw close
def mpc_f97_multi_year_price_context_raw_504d_accel_v015_signal(close, closeadj):
    base = _mean(close, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log close
def mpc_f97_multi_year_price_context_log_21d_accel_v016_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log close
def mpc_f97_multi_year_price_context_log_21d_accel_v017_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log close
def mpc_f97_multi_year_price_context_log_21d_accel_v018_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log close
def mpc_f97_multi_year_price_context_log_63d_accel_v019_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log close
def mpc_f97_multi_year_price_context_log_63d_accel_v020_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log close
def mpc_f97_multi_year_price_context_log_63d_accel_v021_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log close
def mpc_f97_multi_year_price_context_log_126d_accel_v022_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log close
def mpc_f97_multi_year_price_context_log_126d_accel_v023_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log close
def mpc_f97_multi_year_price_context_log_126d_accel_v024_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log close
def mpc_f97_multi_year_price_context_log_252d_accel_v025_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log close
def mpc_f97_multi_year_price_context_log_252d_accel_v026_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log close
def mpc_f97_multi_year_price_context_log_252d_accel_v027_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log close
def mpc_f97_multi_year_price_context_log_504d_accel_v028_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log close
def mpc_f97_multi_year_price_context_log_504d_accel_v029_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log close
def mpc_f97_multi_year_price_context_log_504d_accel_v030_signal(close, closeadj):
    base = _mean(_multi_year_price_context_log(close), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare close
def mpc_f97_multi_year_price_context_pershare_21d_accel_v031_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare close
def mpc_f97_multi_year_price_context_pershare_21d_accel_v032_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare close
def mpc_f97_multi_year_price_context_pershare_21d_accel_v033_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare close
def mpc_f97_multi_year_price_context_pershare_63d_accel_v034_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare close
def mpc_f97_multi_year_price_context_pershare_63d_accel_v035_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare close
def mpc_f97_multi_year_price_context_pershare_63d_accel_v036_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare close
def mpc_f97_multi_year_price_context_pershare_126d_accel_v037_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare close
def mpc_f97_multi_year_price_context_pershare_126d_accel_v038_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare close
def mpc_f97_multi_year_price_context_pershare_126d_accel_v039_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare close
def mpc_f97_multi_year_price_context_pershare_252d_accel_v040_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare close
def mpc_f97_multi_year_price_context_pershare_252d_accel_v041_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare close
def mpc_f97_multi_year_price_context_pershare_252d_accel_v042_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare close
def mpc_f97_multi_year_price_context_pershare_504d_accel_v043_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare close
def mpc_f97_multi_year_price_context_pershare_504d_accel_v044_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare close
def mpc_f97_multi_year_price_context_pershare_504d_accel_v045_signal(close, sharesbas, closeadj):
    base = _mean(_multi_year_price_context_per_share(close, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets close
def mpc_f97_multi_year_price_context_per_assets_21d_accel_v046_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets close
def mpc_f97_multi_year_price_context_per_assets_21d_accel_v047_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets close
def mpc_f97_multi_year_price_context_per_assets_21d_accel_v048_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets close
def mpc_f97_multi_year_price_context_per_assets_63d_accel_v049_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets close
def mpc_f97_multi_year_price_context_per_assets_63d_accel_v050_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets close
def mpc_f97_multi_year_price_context_per_assets_63d_accel_v051_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets close
def mpc_f97_multi_year_price_context_per_assets_126d_accel_v052_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets close
def mpc_f97_multi_year_price_context_per_assets_126d_accel_v053_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets close
def mpc_f97_multi_year_price_context_per_assets_126d_accel_v054_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets close
def mpc_f97_multi_year_price_context_per_assets_252d_accel_v055_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets close
def mpc_f97_multi_year_price_context_per_assets_252d_accel_v056_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets close
def mpc_f97_multi_year_price_context_per_assets_252d_accel_v057_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets close
def mpc_f97_multi_year_price_context_per_assets_504d_accel_v058_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets close
def mpc_f97_multi_year_price_context_per_assets_504d_accel_v059_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets close
def mpc_f97_multi_year_price_context_per_assets_504d_accel_v060_signal(close, assets):
    base = _mean(_multi_year_price_context_scaled(close, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_21d_accel_v061_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_21d_accel_v062_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_21d_accel_v063_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_63d_accel_v064_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_63d_accel_v065_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_63d_accel_v066_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_126d_accel_v067_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_126d_accel_v068_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_126d_accel_v069_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_252d_accel_v070_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_252d_accel_v071_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_252d_accel_v072_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_504d_accel_v073_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_504d_accel_v074_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap close
def mpc_f97_multi_year_price_context_per_marketcap_504d_accel_v075_signal(close, marketcap):
    base = _mean(_multi_year_price_context_scaled(close, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity close
def mpc_f97_multi_year_price_context_per_equity_21d_accel_v076_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity close
def mpc_f97_multi_year_price_context_per_equity_21d_accel_v077_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity close
def mpc_f97_multi_year_price_context_per_equity_21d_accel_v078_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity close
def mpc_f97_multi_year_price_context_per_equity_63d_accel_v079_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity close
def mpc_f97_multi_year_price_context_per_equity_63d_accel_v080_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity close
def mpc_f97_multi_year_price_context_per_equity_63d_accel_v081_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity close
def mpc_f97_multi_year_price_context_per_equity_126d_accel_v082_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity close
def mpc_f97_multi_year_price_context_per_equity_126d_accel_v083_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity close
def mpc_f97_multi_year_price_context_per_equity_126d_accel_v084_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity close
def mpc_f97_multi_year_price_context_per_equity_252d_accel_v085_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity close
def mpc_f97_multi_year_price_context_per_equity_252d_accel_v086_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity close
def mpc_f97_multi_year_price_context_per_equity_252d_accel_v087_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity close
def mpc_f97_multi_year_price_context_per_equity_504d_accel_v088_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity close
def mpc_f97_multi_year_price_context_per_equity_504d_accel_v089_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity close
def mpc_f97_multi_year_price_context_per_equity_504d_accel_v090_signal(close, equity):
    base = _mean(_multi_year_price_context_scaled(close, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std close
def mpc_f97_multi_year_price_context_std_21d_accel_v091_signal(close, closeadj):
    base = _std(close, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std close
def mpc_f97_multi_year_price_context_std_21d_accel_v092_signal(close, closeadj):
    base = _std(close, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std close
def mpc_f97_multi_year_price_context_std_21d_accel_v093_signal(close, closeadj):
    base = _std(close, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std close
def mpc_f97_multi_year_price_context_std_63d_accel_v094_signal(close, closeadj):
    base = _std(close, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std close
def mpc_f97_multi_year_price_context_std_63d_accel_v095_signal(close, closeadj):
    base = _std(close, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std close
def mpc_f97_multi_year_price_context_std_63d_accel_v096_signal(close, closeadj):
    base = _std(close, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std close
def mpc_f97_multi_year_price_context_std_126d_accel_v097_signal(close, closeadj):
    base = _std(close, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std close
def mpc_f97_multi_year_price_context_std_126d_accel_v098_signal(close, closeadj):
    base = _std(close, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std close
def mpc_f97_multi_year_price_context_std_126d_accel_v099_signal(close, closeadj):
    base = _std(close, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std close
def mpc_f97_multi_year_price_context_std_252d_accel_v100_signal(close, closeadj):
    base = _std(close, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std close
def mpc_f97_multi_year_price_context_std_252d_accel_v101_signal(close, closeadj):
    base = _std(close, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std close
def mpc_f97_multi_year_price_context_std_252d_accel_v102_signal(close, closeadj):
    base = _std(close, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std close
def mpc_f97_multi_year_price_context_std_504d_accel_v103_signal(close, closeadj):
    base = _std(close, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std close
def mpc_f97_multi_year_price_context_std_504d_accel_v104_signal(close, closeadj):
    base = _std(close, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std close
def mpc_f97_multi_year_price_context_std_504d_accel_v105_signal(close, closeadj):
    base = _std(close, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm close
def mpc_f97_multi_year_price_context_ewm_21d_accel_v106_signal(close, closeadj):
    base = close.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm close
def mpc_f97_multi_year_price_context_ewm_21d_accel_v107_signal(close, closeadj):
    base = close.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm close
def mpc_f97_multi_year_price_context_ewm_21d_accel_v108_signal(close, closeadj):
    base = close.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm close
def mpc_f97_multi_year_price_context_ewm_63d_accel_v109_signal(close, closeadj):
    base = close.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm close
def mpc_f97_multi_year_price_context_ewm_63d_accel_v110_signal(close, closeadj):
    base = close.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm close
def mpc_f97_multi_year_price_context_ewm_63d_accel_v111_signal(close, closeadj):
    base = close.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm close
def mpc_f97_multi_year_price_context_ewm_126d_accel_v112_signal(close, closeadj):
    base = close.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm close
def mpc_f97_multi_year_price_context_ewm_126d_accel_v113_signal(close, closeadj):
    base = close.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm close
def mpc_f97_multi_year_price_context_ewm_126d_accel_v114_signal(close, closeadj):
    base = close.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm close
def mpc_f97_multi_year_price_context_ewm_252d_accel_v115_signal(close, closeadj):
    base = close.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm close
def mpc_f97_multi_year_price_context_ewm_252d_accel_v116_signal(close, closeadj):
    base = close.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm close
def mpc_f97_multi_year_price_context_ewm_252d_accel_v117_signal(close, closeadj):
    base = close.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm close
def mpc_f97_multi_year_price_context_ewm_504d_accel_v118_signal(close, closeadj):
    base = close.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm close
def mpc_f97_multi_year_price_context_ewm_504d_accel_v119_signal(close, closeadj):
    base = close.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm close
def mpc_f97_multi_year_price_context_ewm_504d_accel_v120_signal(close, closeadj):
    base = close.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq close
def mpc_f97_multi_year_price_context_sq_21d_accel_v121_signal(close, closeadj):
    base = _mean(close * close, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq close
def mpc_f97_multi_year_price_context_sq_21d_accel_v122_signal(close, closeadj):
    base = _mean(close * close, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq close
def mpc_f97_multi_year_price_context_sq_21d_accel_v123_signal(close, closeadj):
    base = _mean(close * close, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq close
def mpc_f97_multi_year_price_context_sq_63d_accel_v124_signal(close, closeadj):
    base = _mean(close * close, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq close
def mpc_f97_multi_year_price_context_sq_63d_accel_v125_signal(close, closeadj):
    base = _mean(close * close, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq close
def mpc_f97_multi_year_price_context_sq_63d_accel_v126_signal(close, closeadj):
    base = _mean(close * close, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq close
def mpc_f97_multi_year_price_context_sq_126d_accel_v127_signal(close, closeadj):
    base = _mean(close * close, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq close
def mpc_f97_multi_year_price_context_sq_126d_accel_v128_signal(close, closeadj):
    base = _mean(close * close, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq close
def mpc_f97_multi_year_price_context_sq_126d_accel_v129_signal(close, closeadj):
    base = _mean(close * close, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq close
def mpc_f97_multi_year_price_context_sq_252d_accel_v130_signal(close, closeadj):
    base = _mean(close * close, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq close
def mpc_f97_multi_year_price_context_sq_252d_accel_v131_signal(close, closeadj):
    base = _mean(close * close, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq close
def mpc_f97_multi_year_price_context_sq_252d_accel_v132_signal(close, closeadj):
    base = _mean(close * close, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq close
def mpc_f97_multi_year_price_context_sq_504d_accel_v133_signal(close, closeadj):
    base = _mean(close * close, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq close
def mpc_f97_multi_year_price_context_sq_504d_accel_v134_signal(close, closeadj):
    base = _mean(close * close, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq close
def mpc_f97_multi_year_price_context_sq_504d_accel_v135_signal(close, closeadj):
    base = _mean(close * close, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z close
def mpc_f97_multi_year_price_context_z_21d_accel_v136_signal(close):
    base = _z(close, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z close
def mpc_f97_multi_year_price_context_z_21d_accel_v137_signal(close):
    base = _z(close, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z close
def mpc_f97_multi_year_price_context_z_21d_accel_v138_signal(close):
    base = _z(close, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z close
def mpc_f97_multi_year_price_context_z_63d_accel_v139_signal(close):
    base = _z(close, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z close
def mpc_f97_multi_year_price_context_z_63d_accel_v140_signal(close):
    base = _z(close, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z close
def mpc_f97_multi_year_price_context_z_63d_accel_v141_signal(close):
    base = _z(close, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z close
def mpc_f97_multi_year_price_context_z_126d_accel_v142_signal(close):
    base = _z(close, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z close
def mpc_f97_multi_year_price_context_z_126d_accel_v143_signal(close):
    base = _z(close, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z close
def mpc_f97_multi_year_price_context_z_126d_accel_v144_signal(close):
    base = _z(close, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z close
def mpc_f97_multi_year_price_context_z_252d_accel_v145_signal(close):
    base = _z(close, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z close
def mpc_f97_multi_year_price_context_z_252d_accel_v146_signal(close):
    base = _z(close, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z close
def mpc_f97_multi_year_price_context_z_252d_accel_v147_signal(close):
    base = _z(close, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z close
def mpc_f97_multi_year_price_context_z_504d_accel_v148_signal(close):
    base = _z(close, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z close
def mpc_f97_multi_year_price_context_z_504d_accel_v149_signal(close):
    base = _z(close, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z close
def mpc_f97_multi_year_price_context_z_504d_accel_v150_signal(close):
    base = _z(close, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
