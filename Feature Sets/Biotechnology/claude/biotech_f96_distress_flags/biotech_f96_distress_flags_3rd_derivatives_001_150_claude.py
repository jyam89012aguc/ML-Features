"""Family f96 - Distress & structural flags  (Q_Actions_Events) | 3rd derivatives 001-150"""
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
def _distress_flags_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _distress_flags_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _distress_flags_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw distressflag
def df_f96_distress_flags_raw_21d_accel_v001_signal(distressflag, closeadj):
    base = _mean(distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw distressflag
def df_f96_distress_flags_raw_21d_accel_v002_signal(distressflag, closeadj):
    base = _mean(distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw distressflag
def df_f96_distress_flags_raw_21d_accel_v003_signal(distressflag, closeadj):
    base = _mean(distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw distressflag
def df_f96_distress_flags_raw_63d_accel_v004_signal(distressflag, closeadj):
    base = _mean(distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw distressflag
def df_f96_distress_flags_raw_63d_accel_v005_signal(distressflag, closeadj):
    base = _mean(distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw distressflag
def df_f96_distress_flags_raw_63d_accel_v006_signal(distressflag, closeadj):
    base = _mean(distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw distressflag
def df_f96_distress_flags_raw_126d_accel_v007_signal(distressflag, closeadj):
    base = _mean(distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw distressflag
def df_f96_distress_flags_raw_126d_accel_v008_signal(distressflag, closeadj):
    base = _mean(distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw distressflag
def df_f96_distress_flags_raw_126d_accel_v009_signal(distressflag, closeadj):
    base = _mean(distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw distressflag
def df_f96_distress_flags_raw_252d_accel_v010_signal(distressflag, closeadj):
    base = _mean(distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw distressflag
def df_f96_distress_flags_raw_252d_accel_v011_signal(distressflag, closeadj):
    base = _mean(distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw distressflag
def df_f96_distress_flags_raw_252d_accel_v012_signal(distressflag, closeadj):
    base = _mean(distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw distressflag
def df_f96_distress_flags_raw_504d_accel_v013_signal(distressflag, closeadj):
    base = _mean(distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw distressflag
def df_f96_distress_flags_raw_504d_accel_v014_signal(distressflag, closeadj):
    base = _mean(distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw distressflag
def df_f96_distress_flags_raw_504d_accel_v015_signal(distressflag, closeadj):
    base = _mean(distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log distressflag
def df_f96_distress_flags_log_21d_accel_v016_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log distressflag
def df_f96_distress_flags_log_21d_accel_v017_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log distressflag
def df_f96_distress_flags_log_21d_accel_v018_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log distressflag
def df_f96_distress_flags_log_63d_accel_v019_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log distressflag
def df_f96_distress_flags_log_63d_accel_v020_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log distressflag
def df_f96_distress_flags_log_63d_accel_v021_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log distressflag
def df_f96_distress_flags_log_126d_accel_v022_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log distressflag
def df_f96_distress_flags_log_126d_accel_v023_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log distressflag
def df_f96_distress_flags_log_126d_accel_v024_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log distressflag
def df_f96_distress_flags_log_252d_accel_v025_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log distressflag
def df_f96_distress_flags_log_252d_accel_v026_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log distressflag
def df_f96_distress_flags_log_252d_accel_v027_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log distressflag
def df_f96_distress_flags_log_504d_accel_v028_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log distressflag
def df_f96_distress_flags_log_504d_accel_v029_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log distressflag
def df_f96_distress_flags_log_504d_accel_v030_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare distressflag
def df_f96_distress_flags_pershare_21d_accel_v031_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare distressflag
def df_f96_distress_flags_pershare_21d_accel_v032_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare distressflag
def df_f96_distress_flags_pershare_21d_accel_v033_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare distressflag
def df_f96_distress_flags_pershare_63d_accel_v034_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare distressflag
def df_f96_distress_flags_pershare_63d_accel_v035_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare distressflag
def df_f96_distress_flags_pershare_63d_accel_v036_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare distressflag
def df_f96_distress_flags_pershare_126d_accel_v037_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare distressflag
def df_f96_distress_flags_pershare_126d_accel_v038_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare distressflag
def df_f96_distress_flags_pershare_126d_accel_v039_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare distressflag
def df_f96_distress_flags_pershare_252d_accel_v040_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare distressflag
def df_f96_distress_flags_pershare_252d_accel_v041_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare distressflag
def df_f96_distress_flags_pershare_252d_accel_v042_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare distressflag
def df_f96_distress_flags_pershare_504d_accel_v043_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare distressflag
def df_f96_distress_flags_pershare_504d_accel_v044_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare distressflag
def df_f96_distress_flags_pershare_504d_accel_v045_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets distressflag
def df_f96_distress_flags_per_assets_21d_accel_v046_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets distressflag
def df_f96_distress_flags_per_assets_21d_accel_v047_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets distressflag
def df_f96_distress_flags_per_assets_21d_accel_v048_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets distressflag
def df_f96_distress_flags_per_assets_63d_accel_v049_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets distressflag
def df_f96_distress_flags_per_assets_63d_accel_v050_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets distressflag
def df_f96_distress_flags_per_assets_63d_accel_v051_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets distressflag
def df_f96_distress_flags_per_assets_126d_accel_v052_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets distressflag
def df_f96_distress_flags_per_assets_126d_accel_v053_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets distressflag
def df_f96_distress_flags_per_assets_126d_accel_v054_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets distressflag
def df_f96_distress_flags_per_assets_252d_accel_v055_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets distressflag
def df_f96_distress_flags_per_assets_252d_accel_v056_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets distressflag
def df_f96_distress_flags_per_assets_252d_accel_v057_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets distressflag
def df_f96_distress_flags_per_assets_504d_accel_v058_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets distressflag
def df_f96_distress_flags_per_assets_504d_accel_v059_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets distressflag
def df_f96_distress_flags_per_assets_504d_accel_v060_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_21d_accel_v061_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_21d_accel_v062_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_21d_accel_v063_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_63d_accel_v064_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_63d_accel_v065_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_63d_accel_v066_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_126d_accel_v067_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_126d_accel_v068_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_126d_accel_v069_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_252d_accel_v070_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_252d_accel_v071_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_252d_accel_v072_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_504d_accel_v073_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_504d_accel_v074_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_504d_accel_v075_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity distressflag
def df_f96_distress_flags_per_equity_21d_accel_v076_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity distressflag
def df_f96_distress_flags_per_equity_21d_accel_v077_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity distressflag
def df_f96_distress_flags_per_equity_21d_accel_v078_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity distressflag
def df_f96_distress_flags_per_equity_63d_accel_v079_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity distressflag
def df_f96_distress_flags_per_equity_63d_accel_v080_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity distressflag
def df_f96_distress_flags_per_equity_63d_accel_v081_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity distressflag
def df_f96_distress_flags_per_equity_126d_accel_v082_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity distressflag
def df_f96_distress_flags_per_equity_126d_accel_v083_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity distressflag
def df_f96_distress_flags_per_equity_126d_accel_v084_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity distressflag
def df_f96_distress_flags_per_equity_252d_accel_v085_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity distressflag
def df_f96_distress_flags_per_equity_252d_accel_v086_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity distressflag
def df_f96_distress_flags_per_equity_252d_accel_v087_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity distressflag
def df_f96_distress_flags_per_equity_504d_accel_v088_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity distressflag
def df_f96_distress_flags_per_equity_504d_accel_v089_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity distressflag
def df_f96_distress_flags_per_equity_504d_accel_v090_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std distressflag
def df_f96_distress_flags_std_21d_accel_v091_signal(distressflag, closeadj):
    base = _std(distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std distressflag
def df_f96_distress_flags_std_21d_accel_v092_signal(distressflag, closeadj):
    base = _std(distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std distressflag
def df_f96_distress_flags_std_21d_accel_v093_signal(distressflag, closeadj):
    base = _std(distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std distressflag
def df_f96_distress_flags_std_63d_accel_v094_signal(distressflag, closeadj):
    base = _std(distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std distressflag
def df_f96_distress_flags_std_63d_accel_v095_signal(distressflag, closeadj):
    base = _std(distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std distressflag
def df_f96_distress_flags_std_63d_accel_v096_signal(distressflag, closeadj):
    base = _std(distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std distressflag
def df_f96_distress_flags_std_126d_accel_v097_signal(distressflag, closeadj):
    base = _std(distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std distressflag
def df_f96_distress_flags_std_126d_accel_v098_signal(distressflag, closeadj):
    base = _std(distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std distressflag
def df_f96_distress_flags_std_126d_accel_v099_signal(distressflag, closeadj):
    base = _std(distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std distressflag
def df_f96_distress_flags_std_252d_accel_v100_signal(distressflag, closeadj):
    base = _std(distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std distressflag
def df_f96_distress_flags_std_252d_accel_v101_signal(distressflag, closeadj):
    base = _std(distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std distressflag
def df_f96_distress_flags_std_252d_accel_v102_signal(distressflag, closeadj):
    base = _std(distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std distressflag
def df_f96_distress_flags_std_504d_accel_v103_signal(distressflag, closeadj):
    base = _std(distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std distressflag
def df_f96_distress_flags_std_504d_accel_v104_signal(distressflag, closeadj):
    base = _std(distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std distressflag
def df_f96_distress_flags_std_504d_accel_v105_signal(distressflag, closeadj):
    base = _std(distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm distressflag
def df_f96_distress_flags_ewm_21d_accel_v106_signal(distressflag, closeadj):
    base = distressflag.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm distressflag
def df_f96_distress_flags_ewm_21d_accel_v107_signal(distressflag, closeadj):
    base = distressflag.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm distressflag
def df_f96_distress_flags_ewm_21d_accel_v108_signal(distressflag, closeadj):
    base = distressflag.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm distressflag
def df_f96_distress_flags_ewm_63d_accel_v109_signal(distressflag, closeadj):
    base = distressflag.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm distressflag
def df_f96_distress_flags_ewm_63d_accel_v110_signal(distressflag, closeadj):
    base = distressflag.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm distressflag
def df_f96_distress_flags_ewm_63d_accel_v111_signal(distressflag, closeadj):
    base = distressflag.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm distressflag
def df_f96_distress_flags_ewm_126d_accel_v112_signal(distressflag, closeadj):
    base = distressflag.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm distressflag
def df_f96_distress_flags_ewm_126d_accel_v113_signal(distressflag, closeadj):
    base = distressflag.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm distressflag
def df_f96_distress_flags_ewm_126d_accel_v114_signal(distressflag, closeadj):
    base = distressflag.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm distressflag
def df_f96_distress_flags_ewm_252d_accel_v115_signal(distressflag, closeadj):
    base = distressflag.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm distressflag
def df_f96_distress_flags_ewm_252d_accel_v116_signal(distressflag, closeadj):
    base = distressflag.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm distressflag
def df_f96_distress_flags_ewm_252d_accel_v117_signal(distressflag, closeadj):
    base = distressflag.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm distressflag
def df_f96_distress_flags_ewm_504d_accel_v118_signal(distressflag, closeadj):
    base = distressflag.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm distressflag
def df_f96_distress_flags_ewm_504d_accel_v119_signal(distressflag, closeadj):
    base = distressflag.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm distressflag
def df_f96_distress_flags_ewm_504d_accel_v120_signal(distressflag, closeadj):
    base = distressflag.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq distressflag
def df_f96_distress_flags_sq_21d_accel_v121_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq distressflag
def df_f96_distress_flags_sq_21d_accel_v122_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq distressflag
def df_f96_distress_flags_sq_21d_accel_v123_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq distressflag
def df_f96_distress_flags_sq_63d_accel_v124_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq distressflag
def df_f96_distress_flags_sq_63d_accel_v125_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq distressflag
def df_f96_distress_flags_sq_63d_accel_v126_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq distressflag
def df_f96_distress_flags_sq_126d_accel_v127_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq distressflag
def df_f96_distress_flags_sq_126d_accel_v128_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq distressflag
def df_f96_distress_flags_sq_126d_accel_v129_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq distressflag
def df_f96_distress_flags_sq_252d_accel_v130_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq distressflag
def df_f96_distress_flags_sq_252d_accel_v131_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq distressflag
def df_f96_distress_flags_sq_252d_accel_v132_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq distressflag
def df_f96_distress_flags_sq_504d_accel_v133_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq distressflag
def df_f96_distress_flags_sq_504d_accel_v134_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq distressflag
def df_f96_distress_flags_sq_504d_accel_v135_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z distressflag
def df_f96_distress_flags_z_21d_accel_v136_signal(distressflag):
    base = _z(distressflag, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z distressflag
def df_f96_distress_flags_z_21d_accel_v137_signal(distressflag):
    base = _z(distressflag, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z distressflag
def df_f96_distress_flags_z_21d_accel_v138_signal(distressflag):
    base = _z(distressflag, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z distressflag
def df_f96_distress_flags_z_63d_accel_v139_signal(distressflag):
    base = _z(distressflag, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z distressflag
def df_f96_distress_flags_z_63d_accel_v140_signal(distressflag):
    base = _z(distressflag, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z distressflag
def df_f96_distress_flags_z_63d_accel_v141_signal(distressflag):
    base = _z(distressflag, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z distressflag
def df_f96_distress_flags_z_126d_accel_v142_signal(distressflag):
    base = _z(distressflag, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z distressflag
def df_f96_distress_flags_z_126d_accel_v143_signal(distressflag):
    base = _z(distressflag, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z distressflag
def df_f96_distress_flags_z_126d_accel_v144_signal(distressflag):
    base = _z(distressflag, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z distressflag
def df_f96_distress_flags_z_252d_accel_v145_signal(distressflag):
    base = _z(distressflag, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z distressflag
def df_f96_distress_flags_z_252d_accel_v146_signal(distressflag):
    base = _z(distressflag, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z distressflag
def df_f96_distress_flags_z_252d_accel_v147_signal(distressflag):
    base = _z(distressflag, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z distressflag
def df_f96_distress_flags_z_504d_accel_v148_signal(distressflag):
    base = _z(distressflag, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z distressflag
def df_f96_distress_flags_z_504d_accel_v149_signal(distressflag):
    base = _z(distressflag, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z distressflag
def df_f96_distress_flags_z_504d_accel_v150_signal(distressflag):
    base = _z(distressflag, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
