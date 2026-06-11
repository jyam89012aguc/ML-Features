"""Family f45 - Revenue per share  (G_Revenue_Growth) | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw sps
def rvp_f45_revenue_per_share_raw_21d_slope_v001_signal(sps, closeadj):
    base = _mean(sps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw sps
def rvp_f45_revenue_per_share_raw_21d_slope_v002_signal(sps, closeadj):
    base = _mean(sps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw sps
def rvp_f45_revenue_per_share_raw_21d_slope_v003_signal(sps, closeadj):
    base = _mean(sps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw sps
def rvp_f45_revenue_per_share_raw_63d_slope_v004_signal(sps, closeadj):
    base = _mean(sps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw sps
def rvp_f45_revenue_per_share_raw_63d_slope_v005_signal(sps, closeadj):
    base = _mean(sps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw sps
def rvp_f45_revenue_per_share_raw_63d_slope_v006_signal(sps, closeadj):
    base = _mean(sps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw sps
def rvp_f45_revenue_per_share_raw_126d_slope_v007_signal(sps, closeadj):
    base = _mean(sps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw sps
def rvp_f45_revenue_per_share_raw_126d_slope_v008_signal(sps, closeadj):
    base = _mean(sps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw sps
def rvp_f45_revenue_per_share_raw_126d_slope_v009_signal(sps, closeadj):
    base = _mean(sps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw sps
def rvp_f45_revenue_per_share_raw_252d_slope_v010_signal(sps, closeadj):
    base = _mean(sps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw sps
def rvp_f45_revenue_per_share_raw_252d_slope_v011_signal(sps, closeadj):
    base = _mean(sps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw sps
def rvp_f45_revenue_per_share_raw_252d_slope_v012_signal(sps, closeadj):
    base = _mean(sps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw sps
def rvp_f45_revenue_per_share_raw_504d_slope_v013_signal(sps, closeadj):
    base = _mean(sps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw sps
def rvp_f45_revenue_per_share_raw_504d_slope_v014_signal(sps, closeadj):
    base = _mean(sps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw sps
def rvp_f45_revenue_per_share_raw_504d_slope_v015_signal(sps, closeadj):
    base = _mean(sps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log sps
def rvp_f45_revenue_per_share_log_21d_slope_v016_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log sps
def rvp_f45_revenue_per_share_log_21d_slope_v017_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log sps
def rvp_f45_revenue_per_share_log_21d_slope_v018_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log sps
def rvp_f45_revenue_per_share_log_63d_slope_v019_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log sps
def rvp_f45_revenue_per_share_log_63d_slope_v020_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log sps
def rvp_f45_revenue_per_share_log_63d_slope_v021_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log sps
def rvp_f45_revenue_per_share_log_126d_slope_v022_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log sps
def rvp_f45_revenue_per_share_log_126d_slope_v023_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log sps
def rvp_f45_revenue_per_share_log_126d_slope_v024_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log sps
def rvp_f45_revenue_per_share_log_252d_slope_v025_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log sps
def rvp_f45_revenue_per_share_log_252d_slope_v026_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log sps
def rvp_f45_revenue_per_share_log_252d_slope_v027_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log sps
def rvp_f45_revenue_per_share_log_504d_slope_v028_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log sps
def rvp_f45_revenue_per_share_log_504d_slope_v029_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log sps
def rvp_f45_revenue_per_share_log_504d_slope_v030_signal(sps, closeadj):
    base = _mean(_revenue_per_share_log(sps), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare sps
def rvp_f45_revenue_per_share_pershare_21d_slope_v031_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare sps
def rvp_f45_revenue_per_share_pershare_21d_slope_v032_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare sps
def rvp_f45_revenue_per_share_pershare_21d_slope_v033_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare sps
def rvp_f45_revenue_per_share_pershare_63d_slope_v034_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare sps
def rvp_f45_revenue_per_share_pershare_63d_slope_v035_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare sps
def rvp_f45_revenue_per_share_pershare_63d_slope_v036_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare sps
def rvp_f45_revenue_per_share_pershare_126d_slope_v037_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare sps
def rvp_f45_revenue_per_share_pershare_126d_slope_v038_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare sps
def rvp_f45_revenue_per_share_pershare_126d_slope_v039_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare sps
def rvp_f45_revenue_per_share_pershare_252d_slope_v040_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare sps
def rvp_f45_revenue_per_share_pershare_252d_slope_v041_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare sps
def rvp_f45_revenue_per_share_pershare_252d_slope_v042_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare sps
def rvp_f45_revenue_per_share_pershare_504d_slope_v043_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare sps
def rvp_f45_revenue_per_share_pershare_504d_slope_v044_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare sps
def rvp_f45_revenue_per_share_pershare_504d_slope_v045_signal(sps, sharesbas, closeadj):
    base = _mean(_revenue_per_share_per_share(sps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets sps
def rvp_f45_revenue_per_share_per_assets_21d_slope_v046_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets sps
def rvp_f45_revenue_per_share_per_assets_21d_slope_v047_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets sps
def rvp_f45_revenue_per_share_per_assets_21d_slope_v048_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets sps
def rvp_f45_revenue_per_share_per_assets_63d_slope_v049_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets sps
def rvp_f45_revenue_per_share_per_assets_63d_slope_v050_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets sps
def rvp_f45_revenue_per_share_per_assets_63d_slope_v051_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets sps
def rvp_f45_revenue_per_share_per_assets_126d_slope_v052_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets sps
def rvp_f45_revenue_per_share_per_assets_126d_slope_v053_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets sps
def rvp_f45_revenue_per_share_per_assets_126d_slope_v054_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets sps
def rvp_f45_revenue_per_share_per_assets_252d_slope_v055_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets sps
def rvp_f45_revenue_per_share_per_assets_252d_slope_v056_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets sps
def rvp_f45_revenue_per_share_per_assets_252d_slope_v057_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets sps
def rvp_f45_revenue_per_share_per_assets_504d_slope_v058_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets sps
def rvp_f45_revenue_per_share_per_assets_504d_slope_v059_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets sps
def rvp_f45_revenue_per_share_per_assets_504d_slope_v060_signal(sps, assets):
    base = _mean(_revenue_per_share_scaled(sps, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_21d_slope_v061_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_21d_slope_v062_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_21d_slope_v063_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_63d_slope_v064_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_63d_slope_v065_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_63d_slope_v066_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_126d_slope_v067_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_126d_slope_v068_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_126d_slope_v069_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_252d_slope_v070_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_252d_slope_v071_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_252d_slope_v072_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_504d_slope_v073_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_504d_slope_v074_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap sps
def rvp_f45_revenue_per_share_per_marketcap_504d_slope_v075_signal(sps, marketcap):
    base = _mean(_revenue_per_share_scaled(sps, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity sps
def rvp_f45_revenue_per_share_per_equity_21d_slope_v076_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity sps
def rvp_f45_revenue_per_share_per_equity_21d_slope_v077_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity sps
def rvp_f45_revenue_per_share_per_equity_21d_slope_v078_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity sps
def rvp_f45_revenue_per_share_per_equity_63d_slope_v079_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity sps
def rvp_f45_revenue_per_share_per_equity_63d_slope_v080_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity sps
def rvp_f45_revenue_per_share_per_equity_63d_slope_v081_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity sps
def rvp_f45_revenue_per_share_per_equity_126d_slope_v082_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity sps
def rvp_f45_revenue_per_share_per_equity_126d_slope_v083_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity sps
def rvp_f45_revenue_per_share_per_equity_126d_slope_v084_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity sps
def rvp_f45_revenue_per_share_per_equity_252d_slope_v085_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity sps
def rvp_f45_revenue_per_share_per_equity_252d_slope_v086_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity sps
def rvp_f45_revenue_per_share_per_equity_252d_slope_v087_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity sps
def rvp_f45_revenue_per_share_per_equity_504d_slope_v088_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity sps
def rvp_f45_revenue_per_share_per_equity_504d_slope_v089_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity sps
def rvp_f45_revenue_per_share_per_equity_504d_slope_v090_signal(sps, equity):
    base = _mean(_revenue_per_share_scaled(sps, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std sps
def rvp_f45_revenue_per_share_std_21d_slope_v091_signal(sps, closeadj):
    base = _std(sps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std sps
def rvp_f45_revenue_per_share_std_21d_slope_v092_signal(sps, closeadj):
    base = _std(sps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std sps
def rvp_f45_revenue_per_share_std_21d_slope_v093_signal(sps, closeadj):
    base = _std(sps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std sps
def rvp_f45_revenue_per_share_std_63d_slope_v094_signal(sps, closeadj):
    base = _std(sps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std sps
def rvp_f45_revenue_per_share_std_63d_slope_v095_signal(sps, closeadj):
    base = _std(sps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std sps
def rvp_f45_revenue_per_share_std_63d_slope_v096_signal(sps, closeadj):
    base = _std(sps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std sps
def rvp_f45_revenue_per_share_std_126d_slope_v097_signal(sps, closeadj):
    base = _std(sps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std sps
def rvp_f45_revenue_per_share_std_126d_slope_v098_signal(sps, closeadj):
    base = _std(sps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std sps
def rvp_f45_revenue_per_share_std_126d_slope_v099_signal(sps, closeadj):
    base = _std(sps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std sps
def rvp_f45_revenue_per_share_std_252d_slope_v100_signal(sps, closeadj):
    base = _std(sps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std sps
def rvp_f45_revenue_per_share_std_252d_slope_v101_signal(sps, closeadj):
    base = _std(sps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std sps
def rvp_f45_revenue_per_share_std_252d_slope_v102_signal(sps, closeadj):
    base = _std(sps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std sps
def rvp_f45_revenue_per_share_std_504d_slope_v103_signal(sps, closeadj):
    base = _std(sps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std sps
def rvp_f45_revenue_per_share_std_504d_slope_v104_signal(sps, closeadj):
    base = _std(sps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std sps
def rvp_f45_revenue_per_share_std_504d_slope_v105_signal(sps, closeadj):
    base = _std(sps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm sps
def rvp_f45_revenue_per_share_ewm_21d_slope_v106_signal(sps, closeadj):
    base = sps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm sps
def rvp_f45_revenue_per_share_ewm_21d_slope_v107_signal(sps, closeadj):
    base = sps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm sps
def rvp_f45_revenue_per_share_ewm_21d_slope_v108_signal(sps, closeadj):
    base = sps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm sps
def rvp_f45_revenue_per_share_ewm_63d_slope_v109_signal(sps, closeadj):
    base = sps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm sps
def rvp_f45_revenue_per_share_ewm_63d_slope_v110_signal(sps, closeadj):
    base = sps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm sps
def rvp_f45_revenue_per_share_ewm_63d_slope_v111_signal(sps, closeadj):
    base = sps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm sps
def rvp_f45_revenue_per_share_ewm_126d_slope_v112_signal(sps, closeadj):
    base = sps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm sps
def rvp_f45_revenue_per_share_ewm_126d_slope_v113_signal(sps, closeadj):
    base = sps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm sps
def rvp_f45_revenue_per_share_ewm_126d_slope_v114_signal(sps, closeadj):
    base = sps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm sps
def rvp_f45_revenue_per_share_ewm_252d_slope_v115_signal(sps, closeadj):
    base = sps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm sps
def rvp_f45_revenue_per_share_ewm_252d_slope_v116_signal(sps, closeadj):
    base = sps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm sps
def rvp_f45_revenue_per_share_ewm_252d_slope_v117_signal(sps, closeadj):
    base = sps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm sps
def rvp_f45_revenue_per_share_ewm_504d_slope_v118_signal(sps, closeadj):
    base = sps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm sps
def rvp_f45_revenue_per_share_ewm_504d_slope_v119_signal(sps, closeadj):
    base = sps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm sps
def rvp_f45_revenue_per_share_ewm_504d_slope_v120_signal(sps, closeadj):
    base = sps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq sps
def rvp_f45_revenue_per_share_sq_21d_slope_v121_signal(sps, closeadj):
    base = _mean(sps * sps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq sps
def rvp_f45_revenue_per_share_sq_21d_slope_v122_signal(sps, closeadj):
    base = _mean(sps * sps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq sps
def rvp_f45_revenue_per_share_sq_21d_slope_v123_signal(sps, closeadj):
    base = _mean(sps * sps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq sps
def rvp_f45_revenue_per_share_sq_63d_slope_v124_signal(sps, closeadj):
    base = _mean(sps * sps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq sps
def rvp_f45_revenue_per_share_sq_63d_slope_v125_signal(sps, closeadj):
    base = _mean(sps * sps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq sps
def rvp_f45_revenue_per_share_sq_63d_slope_v126_signal(sps, closeadj):
    base = _mean(sps * sps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq sps
def rvp_f45_revenue_per_share_sq_126d_slope_v127_signal(sps, closeadj):
    base = _mean(sps * sps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq sps
def rvp_f45_revenue_per_share_sq_126d_slope_v128_signal(sps, closeadj):
    base = _mean(sps * sps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq sps
def rvp_f45_revenue_per_share_sq_126d_slope_v129_signal(sps, closeadj):
    base = _mean(sps * sps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq sps
def rvp_f45_revenue_per_share_sq_252d_slope_v130_signal(sps, closeadj):
    base = _mean(sps * sps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq sps
def rvp_f45_revenue_per_share_sq_252d_slope_v131_signal(sps, closeadj):
    base = _mean(sps * sps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq sps
def rvp_f45_revenue_per_share_sq_252d_slope_v132_signal(sps, closeadj):
    base = _mean(sps * sps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq sps
def rvp_f45_revenue_per_share_sq_504d_slope_v133_signal(sps, closeadj):
    base = _mean(sps * sps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq sps
def rvp_f45_revenue_per_share_sq_504d_slope_v134_signal(sps, closeadj):
    base = _mean(sps * sps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq sps
def rvp_f45_revenue_per_share_sq_504d_slope_v135_signal(sps, closeadj):
    base = _mean(sps * sps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z sps
def rvp_f45_revenue_per_share_z_21d_slope_v136_signal(sps):
    base = _z(sps, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z sps
def rvp_f45_revenue_per_share_z_21d_slope_v137_signal(sps):
    base = _z(sps, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z sps
def rvp_f45_revenue_per_share_z_21d_slope_v138_signal(sps):
    base = _z(sps, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z sps
def rvp_f45_revenue_per_share_z_63d_slope_v139_signal(sps):
    base = _z(sps, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z sps
def rvp_f45_revenue_per_share_z_63d_slope_v140_signal(sps):
    base = _z(sps, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z sps
def rvp_f45_revenue_per_share_z_63d_slope_v141_signal(sps):
    base = _z(sps, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z sps
def rvp_f45_revenue_per_share_z_126d_slope_v142_signal(sps):
    base = _z(sps, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z sps
def rvp_f45_revenue_per_share_z_126d_slope_v143_signal(sps):
    base = _z(sps, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z sps
def rvp_f45_revenue_per_share_z_126d_slope_v144_signal(sps):
    base = _z(sps, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z sps
def rvp_f45_revenue_per_share_z_252d_slope_v145_signal(sps):
    base = _z(sps, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z sps
def rvp_f45_revenue_per_share_z_252d_slope_v146_signal(sps):
    base = _z(sps, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z sps
def rvp_f45_revenue_per_share_z_252d_slope_v147_signal(sps):
    base = _z(sps, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z sps
def rvp_f45_revenue_per_share_z_504d_slope_v148_signal(sps):
    base = _z(sps, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z sps
def rvp_f45_revenue_per_share_z_504d_slope_v149_signal(sps):
    base = _z(sps, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z sps
def rvp_f45_revenue_per_share_z_504d_slope_v150_signal(sps):
    base = _z(sps, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
