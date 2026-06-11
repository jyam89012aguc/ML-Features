"""Family f58 - Comprehensive vs net income gap  (I_Earnings_EPS) | 3rd derivatives 001-150"""
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
def _compinc_gap_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _compinc_gap_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _compinc_gap_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw consolinc
def cig_f58_compinc_gap_raw_21d_accel_v001_signal(consolinc, closeadj):
    base = _mean(consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw consolinc
def cig_f58_compinc_gap_raw_21d_accel_v002_signal(consolinc, closeadj):
    base = _mean(consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw consolinc
def cig_f58_compinc_gap_raw_21d_accel_v003_signal(consolinc, closeadj):
    base = _mean(consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw consolinc
def cig_f58_compinc_gap_raw_63d_accel_v004_signal(consolinc, closeadj):
    base = _mean(consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw consolinc
def cig_f58_compinc_gap_raw_63d_accel_v005_signal(consolinc, closeadj):
    base = _mean(consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw consolinc
def cig_f58_compinc_gap_raw_63d_accel_v006_signal(consolinc, closeadj):
    base = _mean(consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw consolinc
def cig_f58_compinc_gap_raw_126d_accel_v007_signal(consolinc, closeadj):
    base = _mean(consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw consolinc
def cig_f58_compinc_gap_raw_126d_accel_v008_signal(consolinc, closeadj):
    base = _mean(consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw consolinc
def cig_f58_compinc_gap_raw_126d_accel_v009_signal(consolinc, closeadj):
    base = _mean(consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw consolinc
def cig_f58_compinc_gap_raw_252d_accel_v010_signal(consolinc, closeadj):
    base = _mean(consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw consolinc
def cig_f58_compinc_gap_raw_252d_accel_v011_signal(consolinc, closeadj):
    base = _mean(consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw consolinc
def cig_f58_compinc_gap_raw_252d_accel_v012_signal(consolinc, closeadj):
    base = _mean(consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw consolinc
def cig_f58_compinc_gap_raw_504d_accel_v013_signal(consolinc, closeadj):
    base = _mean(consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw consolinc
def cig_f58_compinc_gap_raw_504d_accel_v014_signal(consolinc, closeadj):
    base = _mean(consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw consolinc
def cig_f58_compinc_gap_raw_504d_accel_v015_signal(consolinc, closeadj):
    base = _mean(consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log consolinc
def cig_f58_compinc_gap_log_21d_accel_v016_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log consolinc
def cig_f58_compinc_gap_log_21d_accel_v017_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log consolinc
def cig_f58_compinc_gap_log_21d_accel_v018_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log consolinc
def cig_f58_compinc_gap_log_63d_accel_v019_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log consolinc
def cig_f58_compinc_gap_log_63d_accel_v020_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log consolinc
def cig_f58_compinc_gap_log_63d_accel_v021_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log consolinc
def cig_f58_compinc_gap_log_126d_accel_v022_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log consolinc
def cig_f58_compinc_gap_log_126d_accel_v023_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log consolinc
def cig_f58_compinc_gap_log_126d_accel_v024_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log consolinc
def cig_f58_compinc_gap_log_252d_accel_v025_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log consolinc
def cig_f58_compinc_gap_log_252d_accel_v026_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log consolinc
def cig_f58_compinc_gap_log_252d_accel_v027_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log consolinc
def cig_f58_compinc_gap_log_504d_accel_v028_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log consolinc
def cig_f58_compinc_gap_log_504d_accel_v029_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log consolinc
def cig_f58_compinc_gap_log_504d_accel_v030_signal(consolinc, closeadj):
    base = _mean(_compinc_gap_log(consolinc), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare consolinc
def cig_f58_compinc_gap_pershare_21d_accel_v031_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare consolinc
def cig_f58_compinc_gap_pershare_21d_accel_v032_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare consolinc
def cig_f58_compinc_gap_pershare_21d_accel_v033_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare consolinc
def cig_f58_compinc_gap_pershare_63d_accel_v034_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare consolinc
def cig_f58_compinc_gap_pershare_63d_accel_v035_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare consolinc
def cig_f58_compinc_gap_pershare_63d_accel_v036_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare consolinc
def cig_f58_compinc_gap_pershare_126d_accel_v037_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare consolinc
def cig_f58_compinc_gap_pershare_126d_accel_v038_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare consolinc
def cig_f58_compinc_gap_pershare_126d_accel_v039_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare consolinc
def cig_f58_compinc_gap_pershare_252d_accel_v040_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare consolinc
def cig_f58_compinc_gap_pershare_252d_accel_v041_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare consolinc
def cig_f58_compinc_gap_pershare_252d_accel_v042_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare consolinc
def cig_f58_compinc_gap_pershare_504d_accel_v043_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare consolinc
def cig_f58_compinc_gap_pershare_504d_accel_v044_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare consolinc
def cig_f58_compinc_gap_pershare_504d_accel_v045_signal(consolinc, sharesbas, closeadj):
    base = _mean(_compinc_gap_per_share(consolinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets consolinc
def cig_f58_compinc_gap_per_assets_21d_accel_v046_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets consolinc
def cig_f58_compinc_gap_per_assets_21d_accel_v047_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets consolinc
def cig_f58_compinc_gap_per_assets_21d_accel_v048_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets consolinc
def cig_f58_compinc_gap_per_assets_63d_accel_v049_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets consolinc
def cig_f58_compinc_gap_per_assets_63d_accel_v050_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets consolinc
def cig_f58_compinc_gap_per_assets_63d_accel_v051_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets consolinc
def cig_f58_compinc_gap_per_assets_126d_accel_v052_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets consolinc
def cig_f58_compinc_gap_per_assets_126d_accel_v053_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets consolinc
def cig_f58_compinc_gap_per_assets_126d_accel_v054_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets consolinc
def cig_f58_compinc_gap_per_assets_252d_accel_v055_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets consolinc
def cig_f58_compinc_gap_per_assets_252d_accel_v056_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets consolinc
def cig_f58_compinc_gap_per_assets_252d_accel_v057_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets consolinc
def cig_f58_compinc_gap_per_assets_504d_accel_v058_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets consolinc
def cig_f58_compinc_gap_per_assets_504d_accel_v059_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets consolinc
def cig_f58_compinc_gap_per_assets_504d_accel_v060_signal(consolinc, assets):
    base = _mean(_compinc_gap_scaled(consolinc, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_21d_accel_v061_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_21d_accel_v062_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_21d_accel_v063_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_63d_accel_v064_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_63d_accel_v065_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_63d_accel_v066_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_126d_accel_v067_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_126d_accel_v068_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_126d_accel_v069_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_252d_accel_v070_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_252d_accel_v071_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_252d_accel_v072_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_504d_accel_v073_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_504d_accel_v074_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap consolinc
def cig_f58_compinc_gap_per_marketcap_504d_accel_v075_signal(consolinc, marketcap):
    base = _mean(_compinc_gap_scaled(consolinc, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity consolinc
def cig_f58_compinc_gap_per_equity_21d_accel_v076_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity consolinc
def cig_f58_compinc_gap_per_equity_21d_accel_v077_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity consolinc
def cig_f58_compinc_gap_per_equity_21d_accel_v078_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity consolinc
def cig_f58_compinc_gap_per_equity_63d_accel_v079_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity consolinc
def cig_f58_compinc_gap_per_equity_63d_accel_v080_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity consolinc
def cig_f58_compinc_gap_per_equity_63d_accel_v081_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity consolinc
def cig_f58_compinc_gap_per_equity_126d_accel_v082_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity consolinc
def cig_f58_compinc_gap_per_equity_126d_accel_v083_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity consolinc
def cig_f58_compinc_gap_per_equity_126d_accel_v084_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity consolinc
def cig_f58_compinc_gap_per_equity_252d_accel_v085_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity consolinc
def cig_f58_compinc_gap_per_equity_252d_accel_v086_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity consolinc
def cig_f58_compinc_gap_per_equity_252d_accel_v087_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity consolinc
def cig_f58_compinc_gap_per_equity_504d_accel_v088_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity consolinc
def cig_f58_compinc_gap_per_equity_504d_accel_v089_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity consolinc
def cig_f58_compinc_gap_per_equity_504d_accel_v090_signal(consolinc, equity):
    base = _mean(_compinc_gap_scaled(consolinc, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std consolinc
def cig_f58_compinc_gap_std_21d_accel_v091_signal(consolinc, closeadj):
    base = _std(consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std consolinc
def cig_f58_compinc_gap_std_21d_accel_v092_signal(consolinc, closeadj):
    base = _std(consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std consolinc
def cig_f58_compinc_gap_std_21d_accel_v093_signal(consolinc, closeadj):
    base = _std(consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std consolinc
def cig_f58_compinc_gap_std_63d_accel_v094_signal(consolinc, closeadj):
    base = _std(consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std consolinc
def cig_f58_compinc_gap_std_63d_accel_v095_signal(consolinc, closeadj):
    base = _std(consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std consolinc
def cig_f58_compinc_gap_std_63d_accel_v096_signal(consolinc, closeadj):
    base = _std(consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std consolinc
def cig_f58_compinc_gap_std_126d_accel_v097_signal(consolinc, closeadj):
    base = _std(consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std consolinc
def cig_f58_compinc_gap_std_126d_accel_v098_signal(consolinc, closeadj):
    base = _std(consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std consolinc
def cig_f58_compinc_gap_std_126d_accel_v099_signal(consolinc, closeadj):
    base = _std(consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std consolinc
def cig_f58_compinc_gap_std_252d_accel_v100_signal(consolinc, closeadj):
    base = _std(consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std consolinc
def cig_f58_compinc_gap_std_252d_accel_v101_signal(consolinc, closeadj):
    base = _std(consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std consolinc
def cig_f58_compinc_gap_std_252d_accel_v102_signal(consolinc, closeadj):
    base = _std(consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std consolinc
def cig_f58_compinc_gap_std_504d_accel_v103_signal(consolinc, closeadj):
    base = _std(consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std consolinc
def cig_f58_compinc_gap_std_504d_accel_v104_signal(consolinc, closeadj):
    base = _std(consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std consolinc
def cig_f58_compinc_gap_std_504d_accel_v105_signal(consolinc, closeadj):
    base = _std(consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm consolinc
def cig_f58_compinc_gap_ewm_21d_accel_v106_signal(consolinc, closeadj):
    base = consolinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm consolinc
def cig_f58_compinc_gap_ewm_21d_accel_v107_signal(consolinc, closeadj):
    base = consolinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm consolinc
def cig_f58_compinc_gap_ewm_21d_accel_v108_signal(consolinc, closeadj):
    base = consolinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm consolinc
def cig_f58_compinc_gap_ewm_63d_accel_v109_signal(consolinc, closeadj):
    base = consolinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm consolinc
def cig_f58_compinc_gap_ewm_63d_accel_v110_signal(consolinc, closeadj):
    base = consolinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm consolinc
def cig_f58_compinc_gap_ewm_63d_accel_v111_signal(consolinc, closeadj):
    base = consolinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm consolinc
def cig_f58_compinc_gap_ewm_126d_accel_v112_signal(consolinc, closeadj):
    base = consolinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm consolinc
def cig_f58_compinc_gap_ewm_126d_accel_v113_signal(consolinc, closeadj):
    base = consolinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm consolinc
def cig_f58_compinc_gap_ewm_126d_accel_v114_signal(consolinc, closeadj):
    base = consolinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm consolinc
def cig_f58_compinc_gap_ewm_252d_accel_v115_signal(consolinc, closeadj):
    base = consolinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm consolinc
def cig_f58_compinc_gap_ewm_252d_accel_v116_signal(consolinc, closeadj):
    base = consolinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm consolinc
def cig_f58_compinc_gap_ewm_252d_accel_v117_signal(consolinc, closeadj):
    base = consolinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm consolinc
def cig_f58_compinc_gap_ewm_504d_accel_v118_signal(consolinc, closeadj):
    base = consolinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm consolinc
def cig_f58_compinc_gap_ewm_504d_accel_v119_signal(consolinc, closeadj):
    base = consolinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm consolinc
def cig_f58_compinc_gap_ewm_504d_accel_v120_signal(consolinc, closeadj):
    base = consolinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq consolinc
def cig_f58_compinc_gap_sq_21d_accel_v121_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq consolinc
def cig_f58_compinc_gap_sq_21d_accel_v122_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq consolinc
def cig_f58_compinc_gap_sq_21d_accel_v123_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq consolinc
def cig_f58_compinc_gap_sq_63d_accel_v124_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq consolinc
def cig_f58_compinc_gap_sq_63d_accel_v125_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq consolinc
def cig_f58_compinc_gap_sq_63d_accel_v126_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq consolinc
def cig_f58_compinc_gap_sq_126d_accel_v127_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq consolinc
def cig_f58_compinc_gap_sq_126d_accel_v128_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq consolinc
def cig_f58_compinc_gap_sq_126d_accel_v129_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq consolinc
def cig_f58_compinc_gap_sq_252d_accel_v130_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq consolinc
def cig_f58_compinc_gap_sq_252d_accel_v131_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq consolinc
def cig_f58_compinc_gap_sq_252d_accel_v132_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq consolinc
def cig_f58_compinc_gap_sq_504d_accel_v133_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq consolinc
def cig_f58_compinc_gap_sq_504d_accel_v134_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq consolinc
def cig_f58_compinc_gap_sq_504d_accel_v135_signal(consolinc, closeadj):
    base = _mean(consolinc * consolinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z consolinc
def cig_f58_compinc_gap_z_21d_accel_v136_signal(consolinc):
    base = _z(consolinc, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z consolinc
def cig_f58_compinc_gap_z_21d_accel_v137_signal(consolinc):
    base = _z(consolinc, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z consolinc
def cig_f58_compinc_gap_z_21d_accel_v138_signal(consolinc):
    base = _z(consolinc, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z consolinc
def cig_f58_compinc_gap_z_63d_accel_v139_signal(consolinc):
    base = _z(consolinc, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z consolinc
def cig_f58_compinc_gap_z_63d_accel_v140_signal(consolinc):
    base = _z(consolinc, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z consolinc
def cig_f58_compinc_gap_z_63d_accel_v141_signal(consolinc):
    base = _z(consolinc, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z consolinc
def cig_f58_compinc_gap_z_126d_accel_v142_signal(consolinc):
    base = _z(consolinc, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z consolinc
def cig_f58_compinc_gap_z_126d_accel_v143_signal(consolinc):
    base = _z(consolinc, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z consolinc
def cig_f58_compinc_gap_z_126d_accel_v144_signal(consolinc):
    base = _z(consolinc, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z consolinc
def cig_f58_compinc_gap_z_252d_accel_v145_signal(consolinc):
    base = _z(consolinc, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z consolinc
def cig_f58_compinc_gap_z_252d_accel_v146_signal(consolinc):
    base = _z(consolinc, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z consolinc
def cig_f58_compinc_gap_z_252d_accel_v147_signal(consolinc):
    base = _z(consolinc, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z consolinc
def cig_f58_compinc_gap_z_504d_accel_v148_signal(consolinc):
    base = _z(consolinc, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z consolinc
def cig_f58_compinc_gap_z_504d_accel_v149_signal(consolinc):
    base = _z(consolinc, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z consolinc
def cig_f58_compinc_gap_z_504d_accel_v150_signal(consolinc):
    base = _z(consolinc, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
