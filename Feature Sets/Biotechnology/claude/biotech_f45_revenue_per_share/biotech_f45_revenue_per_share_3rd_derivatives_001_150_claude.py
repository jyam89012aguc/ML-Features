"""Family f45 - Revenue per share  (G_Revenue_Growth) | 3rd derivatives 001-150"""
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
def _revenue_per_share_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _revenue_per_share_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _revenue_per_share_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw sps
def rvp_f45_revenue_per_share_raw_21d_accel_v001_signal(sps, closeadj):
    base = _mean(sps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw sps
def rvp_f45_revenue_per_share_raw_21d_accel_v002_signal(sps, closeadj):
    base = _mean(sps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw sps
def rvp_f45_revenue_per_share_raw_21d_accel_v003_signal(sps, closeadj):
    base = _mean(sps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw sps
def rvp_f45_revenue_per_share_raw_63d_accel_v004_signal(sps, closeadj):
    base = _mean(sps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw sps
def rvp_f45_revenue_per_share_raw_63d_accel_v005_signal(sps, closeadj):
    base = _mean(sps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw sps
def rvp_f45_revenue_per_share_raw_63d_accel_v006_signal(sps, closeadj):
    base = _mean(sps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw sps
def rvp_f45_revenue_per_share_raw_126d_accel_v007_signal(sps, closeadj):
    base = _mean(sps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw sps
def rvp_f45_revenue_per_share_raw_126d_accel_v008_signal(sps, closeadj):
    base = _mean(sps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw sps
def rvp_f45_revenue_per_share_raw_126d_accel_v009_signal(sps, closeadj):
    base = _mean(sps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw sps
def rvp_f45_revenue_per_share_raw_252d_accel_v010_signal(sps, closeadj):
    base = _mean(sps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw sps
def rvp_f45_revenue_per_share_raw_252d_accel_v011_signal(sps, closeadj):
    base = _mean(sps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw sps
def rvp_f45_revenue_per_share_raw_252d_accel_v012_signal(sps, closeadj):
    base = _mean(sps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw sps
def rvp_f45_revenue_per_share_raw_504d_accel_v013_signal(sps, closeadj):
    base = _mean(sps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw sps
def rvp_f45_revenue_per_share_raw_504d_accel_v014_signal(sps, closeadj):
    base = _mean(sps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw sps
def rvp_f45_revenue_per_share_raw_504d_accel_v015_signal(sps, closeadj):
    base = _mean(sps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log sps
def rvp_f45_revenue_per_share_log_21d_accel_v016_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log sps
def rvp_f45_revenue_per_share_log_21d_accel_v017_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log sps
def rvp_f45_revenue_per_share_log_21d_accel_v018_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log sps
def rvp_f45_revenue_per_share_log_63d_accel_v019_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log sps
def rvp_f45_revenue_per_share_log_63d_accel_v020_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log sps
def rvp_f45_revenue_per_share_log_63d_accel_v021_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log sps
def rvp_f45_revenue_per_share_log_126d_accel_v022_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log sps
def rvp_f45_revenue_per_share_log_126d_accel_v023_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log sps
def rvp_f45_revenue_per_share_log_126d_accel_v024_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log sps
def rvp_f45_revenue_per_share_log_252d_accel_v025_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log sps
def rvp_f45_revenue_per_share_log_252d_accel_v026_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log sps
def rvp_f45_revenue_per_share_log_252d_accel_v027_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log sps
def rvp_f45_revenue_per_share_log_504d_accel_v028_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log sps
def rvp_f45_revenue_per_share_log_504d_accel_v029_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log sps
def rvp_f45_revenue_per_share_log_504d_accel_v030_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare sps
def rvp_f45_revenue_per_share_pershare_21d_accel_v031_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare sps
def rvp_f45_revenue_per_share_pershare_21d_accel_v032_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare sps
def rvp_f45_revenue_per_share_pershare_21d_accel_v033_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare sps
def rvp_f45_revenue_per_share_pershare_63d_accel_v034_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare sps
def rvp_f45_revenue_per_share_pershare_63d_accel_v035_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare sps
def rvp_f45_revenue_per_share_pershare_63d_accel_v036_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare sps
def rvp_f45_revenue_per_share_pershare_126d_accel_v037_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare sps
def rvp_f45_revenue_per_share_pershare_126d_accel_v038_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare sps
def rvp_f45_revenue_per_share_pershare_126d_accel_v039_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare sps
def rvp_f45_revenue_per_share_pershare_252d_accel_v040_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare sps
def rvp_f45_revenue_per_share_pershare_252d_accel_v041_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare sps
def rvp_f45_revenue_per_share_pershare_252d_accel_v042_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare sps
def rvp_f45_revenue_per_share_pershare_504d_accel_v043_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare sps
def rvp_f45_revenue_per_share_pershare_504d_accel_v044_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare sps
def rvp_f45_revenue_per_share_pershare_504d_accel_v045_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets sps
def rvp_f45_revenue_per_share_per_assets_21d_accel_v046_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets sps
def rvp_f45_revenue_per_share_per_assets_21d_accel_v047_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets sps
def rvp_f45_revenue_per_share_per_assets_21d_accel_v048_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets sps
def rvp_f45_revenue_per_share_per_assets_63d_accel_v049_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets sps
def rvp_f45_revenue_per_share_per_assets_63d_accel_v050_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets sps
def rvp_f45_revenue_per_share_per_assets_63d_accel_v051_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets sps
def rvp_f45_revenue_per_share_per_assets_126d_accel_v052_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets sps
def rvp_f45_revenue_per_share_per_assets_126d_accel_v053_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets sps
def rvp_f45_revenue_per_share_per_assets_126d_accel_v054_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets sps
def rvp_f45_revenue_per_share_per_assets_252d_accel_v055_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets sps
def rvp_f45_revenue_per_share_per_assets_252d_accel_v056_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets sps
def rvp_f45_revenue_per_share_per_assets_252d_accel_v057_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets sps
def rvp_f45_revenue_per_share_per_assets_504d_accel_v058_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets sps
def rvp_f45_revenue_per_share_per_assets_504d_accel_v059_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets sps
def rvp_f45_revenue_per_share_per_assets_504d_accel_v060_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_21d_accel_v061_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_21d_accel_v062_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_21d_accel_v063_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_63d_accel_v064_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_63d_accel_v065_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_63d_accel_v066_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_126d_accel_v067_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_126d_accel_v068_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_126d_accel_v069_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_252d_accel_v070_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_252d_accel_v071_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_252d_accel_v072_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_504d_accel_v073_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_504d_accel_v074_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_504d_accel_v075_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity sps
def rvp_f45_revenue_per_share_per_equity_21d_accel_v076_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity sps
def rvp_f45_revenue_per_share_per_equity_21d_accel_v077_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity sps
def rvp_f45_revenue_per_share_per_equity_21d_accel_v078_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity sps
def rvp_f45_revenue_per_share_per_equity_63d_accel_v079_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity sps
def rvp_f45_revenue_per_share_per_equity_63d_accel_v080_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity sps
def rvp_f45_revenue_per_share_per_equity_63d_accel_v081_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity sps
def rvp_f45_revenue_per_share_per_equity_126d_accel_v082_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity sps
def rvp_f45_revenue_per_share_per_equity_126d_accel_v083_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity sps
def rvp_f45_revenue_per_share_per_equity_126d_accel_v084_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity sps
def rvp_f45_revenue_per_share_per_equity_252d_accel_v085_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity sps
def rvp_f45_revenue_per_share_per_equity_252d_accel_v086_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity sps
def rvp_f45_revenue_per_share_per_equity_252d_accel_v087_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity sps
def rvp_f45_revenue_per_share_per_equity_504d_accel_v088_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity sps
def rvp_f45_revenue_per_share_per_equity_504d_accel_v089_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity sps
def rvp_f45_revenue_per_share_per_equity_504d_accel_v090_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std sps
def rvp_f45_revenue_per_share_std_21d_accel_v091_signal(sps, closeadj):
    base = _std(sps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std sps
def rvp_f45_revenue_per_share_std_21d_accel_v092_signal(sps, closeadj):
    base = _std(sps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std sps
def rvp_f45_revenue_per_share_std_21d_accel_v093_signal(sps, closeadj):
    base = _std(sps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std sps
def rvp_f45_revenue_per_share_std_63d_accel_v094_signal(sps, closeadj):
    base = _std(sps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std sps
def rvp_f45_revenue_per_share_std_63d_accel_v095_signal(sps, closeadj):
    base = _std(sps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std sps
def rvp_f45_revenue_per_share_std_63d_accel_v096_signal(sps, closeadj):
    base = _std(sps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std sps
def rvp_f45_revenue_per_share_std_126d_accel_v097_signal(sps, closeadj):
    base = _std(sps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std sps
def rvp_f45_revenue_per_share_std_126d_accel_v098_signal(sps, closeadj):
    base = _std(sps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std sps
def rvp_f45_revenue_per_share_std_126d_accel_v099_signal(sps, closeadj):
    base = _std(sps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std sps
def rvp_f45_revenue_per_share_std_252d_accel_v100_signal(sps, closeadj):
    base = _std(sps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std sps
def rvp_f45_revenue_per_share_std_252d_accel_v101_signal(sps, closeadj):
    base = _std(sps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std sps
def rvp_f45_revenue_per_share_std_252d_accel_v102_signal(sps, closeadj):
    base = _std(sps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std sps
def rvp_f45_revenue_per_share_std_504d_accel_v103_signal(sps, closeadj):
    base = _std(sps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std sps
def rvp_f45_revenue_per_share_std_504d_accel_v104_signal(sps, closeadj):
    base = _std(sps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std sps
def rvp_f45_revenue_per_share_std_504d_accel_v105_signal(sps, closeadj):
    base = _std(sps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm sps
def rvp_f45_revenue_per_share_ewm_21d_accel_v106_signal(sps, closeadj):
    base = sps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm sps
def rvp_f45_revenue_per_share_ewm_21d_accel_v107_signal(sps, closeadj):
    base = sps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm sps
def rvp_f45_revenue_per_share_ewm_21d_accel_v108_signal(sps, closeadj):
    base = sps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm sps
def rvp_f45_revenue_per_share_ewm_63d_accel_v109_signal(sps, closeadj):
    base = sps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm sps
def rvp_f45_revenue_per_share_ewm_63d_accel_v110_signal(sps, closeadj):
    base = sps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm sps
def rvp_f45_revenue_per_share_ewm_63d_accel_v111_signal(sps, closeadj):
    base = sps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm sps
def rvp_f45_revenue_per_share_ewm_126d_accel_v112_signal(sps, closeadj):
    base = sps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm sps
def rvp_f45_revenue_per_share_ewm_126d_accel_v113_signal(sps, closeadj):
    base = sps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm sps
def rvp_f45_revenue_per_share_ewm_126d_accel_v114_signal(sps, closeadj):
    base = sps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm sps
def rvp_f45_revenue_per_share_ewm_252d_accel_v115_signal(sps, closeadj):
    base = sps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm sps
def rvp_f45_revenue_per_share_ewm_252d_accel_v116_signal(sps, closeadj):
    base = sps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm sps
def rvp_f45_revenue_per_share_ewm_252d_accel_v117_signal(sps, closeadj):
    base = sps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm sps
def rvp_f45_revenue_per_share_ewm_504d_accel_v118_signal(sps, closeadj):
    base = sps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm sps
def rvp_f45_revenue_per_share_ewm_504d_accel_v119_signal(sps, closeadj):
    base = sps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm sps
def rvp_f45_revenue_per_share_ewm_504d_accel_v120_signal(sps, closeadj):
    base = sps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq sps
def rvp_f45_revenue_per_share_sq_21d_accel_v121_signal(sps, closeadj):
    base = _mean(sps * sps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq sps
def rvp_f45_revenue_per_share_sq_21d_accel_v122_signal(sps, closeadj):
    base = _mean(sps * sps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq sps
def rvp_f45_revenue_per_share_sq_21d_accel_v123_signal(sps, closeadj):
    base = _mean(sps * sps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq sps
def rvp_f45_revenue_per_share_sq_63d_accel_v124_signal(sps, closeadj):
    base = _mean(sps * sps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq sps
def rvp_f45_revenue_per_share_sq_63d_accel_v125_signal(sps, closeadj):
    base = _mean(sps * sps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq sps
def rvp_f45_revenue_per_share_sq_63d_accel_v126_signal(sps, closeadj):
    base = _mean(sps * sps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq sps
def rvp_f45_revenue_per_share_sq_126d_accel_v127_signal(sps, closeadj):
    base = _mean(sps * sps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq sps
def rvp_f45_revenue_per_share_sq_126d_accel_v128_signal(sps, closeadj):
    base = _mean(sps * sps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq sps
def rvp_f45_revenue_per_share_sq_126d_accel_v129_signal(sps, closeadj):
    base = _mean(sps * sps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq sps
def rvp_f45_revenue_per_share_sq_252d_accel_v130_signal(sps, closeadj):
    base = _mean(sps * sps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq sps
def rvp_f45_revenue_per_share_sq_252d_accel_v131_signal(sps, closeadj):
    base = _mean(sps * sps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq sps
def rvp_f45_revenue_per_share_sq_252d_accel_v132_signal(sps, closeadj):
    base = _mean(sps * sps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq sps
def rvp_f45_revenue_per_share_sq_504d_accel_v133_signal(sps, closeadj):
    base = _mean(sps * sps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq sps
def rvp_f45_revenue_per_share_sq_504d_accel_v134_signal(sps, closeadj):
    base = _mean(sps * sps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq sps
def rvp_f45_revenue_per_share_sq_504d_accel_v135_signal(sps, closeadj):
    base = _mean(sps * sps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z sps
def rvp_f45_revenue_per_share_z_21d_accel_v136_signal(sps):
    base = _z(sps, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z sps
def rvp_f45_revenue_per_share_z_21d_accel_v137_signal(sps):
    base = _z(sps, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z sps
def rvp_f45_revenue_per_share_z_21d_accel_v138_signal(sps):
    base = _z(sps, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z sps
def rvp_f45_revenue_per_share_z_63d_accel_v139_signal(sps):
    base = _z(sps, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z sps
def rvp_f45_revenue_per_share_z_63d_accel_v140_signal(sps):
    base = _z(sps, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z sps
def rvp_f45_revenue_per_share_z_63d_accel_v141_signal(sps):
    base = _z(sps, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z sps
def rvp_f45_revenue_per_share_z_126d_accel_v142_signal(sps):
    base = _z(sps, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z sps
def rvp_f45_revenue_per_share_z_126d_accel_v143_signal(sps):
    base = _z(sps, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z sps
def rvp_f45_revenue_per_share_z_126d_accel_v144_signal(sps):
    base = _z(sps, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z sps
def rvp_f45_revenue_per_share_z_252d_accel_v145_signal(sps):
    base = _z(sps, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z sps
def rvp_f45_revenue_per_share_z_252d_accel_v146_signal(sps):
    base = _z(sps, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z sps
def rvp_f45_revenue_per_share_z_252d_accel_v147_signal(sps):
    base = _z(sps, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z sps
def rvp_f45_revenue_per_share_z_504d_accel_v148_signal(sps):
    base = _z(sps, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z sps
def rvp_f45_revenue_per_share_z_504d_accel_v149_signal(sps):
    base = _z(sps, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z sps
def rvp_f45_revenue_per_share_z_504d_accel_v150_signal(sps):
    base = _z(sps, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
