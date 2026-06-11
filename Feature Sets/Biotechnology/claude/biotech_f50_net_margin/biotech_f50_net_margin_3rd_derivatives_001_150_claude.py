"""Family f50 - Net margin  (H_Margins) | 3rd derivatives 001-150"""
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
def _net_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _net_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _net_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw netmargin
def nm_f50_net_margin_raw_21d_accel_v001_signal(netmargin, closeadj):
    base = _mean(netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw netmargin
def nm_f50_net_margin_raw_21d_accel_v002_signal(netmargin, closeadj):
    base = _mean(netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw netmargin
def nm_f50_net_margin_raw_21d_accel_v003_signal(netmargin, closeadj):
    base = _mean(netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw netmargin
def nm_f50_net_margin_raw_63d_accel_v004_signal(netmargin, closeadj):
    base = _mean(netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw netmargin
def nm_f50_net_margin_raw_63d_accel_v005_signal(netmargin, closeadj):
    base = _mean(netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw netmargin
def nm_f50_net_margin_raw_63d_accel_v006_signal(netmargin, closeadj):
    base = _mean(netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw netmargin
def nm_f50_net_margin_raw_126d_accel_v007_signal(netmargin, closeadj):
    base = _mean(netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw netmargin
def nm_f50_net_margin_raw_126d_accel_v008_signal(netmargin, closeadj):
    base = _mean(netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw netmargin
def nm_f50_net_margin_raw_126d_accel_v009_signal(netmargin, closeadj):
    base = _mean(netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw netmargin
def nm_f50_net_margin_raw_252d_accel_v010_signal(netmargin, closeadj):
    base = _mean(netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw netmargin
def nm_f50_net_margin_raw_252d_accel_v011_signal(netmargin, closeadj):
    base = _mean(netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw netmargin
def nm_f50_net_margin_raw_252d_accel_v012_signal(netmargin, closeadj):
    base = _mean(netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw netmargin
def nm_f50_net_margin_raw_504d_accel_v013_signal(netmargin, closeadj):
    base = _mean(netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw netmargin
def nm_f50_net_margin_raw_504d_accel_v014_signal(netmargin, closeadj):
    base = _mean(netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw netmargin
def nm_f50_net_margin_raw_504d_accel_v015_signal(netmargin, closeadj):
    base = _mean(netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log netmargin
def nm_f50_net_margin_log_21d_accel_v016_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log netmargin
def nm_f50_net_margin_log_21d_accel_v017_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log netmargin
def nm_f50_net_margin_log_21d_accel_v018_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log netmargin
def nm_f50_net_margin_log_63d_accel_v019_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log netmargin
def nm_f50_net_margin_log_63d_accel_v020_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log netmargin
def nm_f50_net_margin_log_63d_accel_v021_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log netmargin
def nm_f50_net_margin_log_126d_accel_v022_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log netmargin
def nm_f50_net_margin_log_126d_accel_v023_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log netmargin
def nm_f50_net_margin_log_126d_accel_v024_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log netmargin
def nm_f50_net_margin_log_252d_accel_v025_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log netmargin
def nm_f50_net_margin_log_252d_accel_v026_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log netmargin
def nm_f50_net_margin_log_252d_accel_v027_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log netmargin
def nm_f50_net_margin_log_504d_accel_v028_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log netmargin
def nm_f50_net_margin_log_504d_accel_v029_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log netmargin
def nm_f50_net_margin_log_504d_accel_v030_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare netmargin
def nm_f50_net_margin_pershare_21d_accel_v031_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare netmargin
def nm_f50_net_margin_pershare_21d_accel_v032_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare netmargin
def nm_f50_net_margin_pershare_21d_accel_v033_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare netmargin
def nm_f50_net_margin_pershare_63d_accel_v034_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare netmargin
def nm_f50_net_margin_pershare_63d_accel_v035_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare netmargin
def nm_f50_net_margin_pershare_63d_accel_v036_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare netmargin
def nm_f50_net_margin_pershare_126d_accel_v037_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare netmargin
def nm_f50_net_margin_pershare_126d_accel_v038_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare netmargin
def nm_f50_net_margin_pershare_126d_accel_v039_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare netmargin
def nm_f50_net_margin_pershare_252d_accel_v040_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare netmargin
def nm_f50_net_margin_pershare_252d_accel_v041_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare netmargin
def nm_f50_net_margin_pershare_252d_accel_v042_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare netmargin
def nm_f50_net_margin_pershare_504d_accel_v043_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare netmargin
def nm_f50_net_margin_pershare_504d_accel_v044_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare netmargin
def nm_f50_net_margin_pershare_504d_accel_v045_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets netmargin
def nm_f50_net_margin_per_assets_21d_accel_v046_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets netmargin
def nm_f50_net_margin_per_assets_21d_accel_v047_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets netmargin
def nm_f50_net_margin_per_assets_21d_accel_v048_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets netmargin
def nm_f50_net_margin_per_assets_63d_accel_v049_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets netmargin
def nm_f50_net_margin_per_assets_63d_accel_v050_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets netmargin
def nm_f50_net_margin_per_assets_63d_accel_v051_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets netmargin
def nm_f50_net_margin_per_assets_126d_accel_v052_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets netmargin
def nm_f50_net_margin_per_assets_126d_accel_v053_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets netmargin
def nm_f50_net_margin_per_assets_126d_accel_v054_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets netmargin
def nm_f50_net_margin_per_assets_252d_accel_v055_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets netmargin
def nm_f50_net_margin_per_assets_252d_accel_v056_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets netmargin
def nm_f50_net_margin_per_assets_252d_accel_v057_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets netmargin
def nm_f50_net_margin_per_assets_504d_accel_v058_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets netmargin
def nm_f50_net_margin_per_assets_504d_accel_v059_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets netmargin
def nm_f50_net_margin_per_assets_504d_accel_v060_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_21d_accel_v061_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_21d_accel_v062_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_21d_accel_v063_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_63d_accel_v064_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_63d_accel_v065_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_63d_accel_v066_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_126d_accel_v067_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_126d_accel_v068_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_126d_accel_v069_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_252d_accel_v070_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_252d_accel_v071_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_252d_accel_v072_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_504d_accel_v073_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_504d_accel_v074_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_504d_accel_v075_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity netmargin
def nm_f50_net_margin_per_equity_21d_accel_v076_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity netmargin
def nm_f50_net_margin_per_equity_21d_accel_v077_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity netmargin
def nm_f50_net_margin_per_equity_21d_accel_v078_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity netmargin
def nm_f50_net_margin_per_equity_63d_accel_v079_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity netmargin
def nm_f50_net_margin_per_equity_63d_accel_v080_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity netmargin
def nm_f50_net_margin_per_equity_63d_accel_v081_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity netmargin
def nm_f50_net_margin_per_equity_126d_accel_v082_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity netmargin
def nm_f50_net_margin_per_equity_126d_accel_v083_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity netmargin
def nm_f50_net_margin_per_equity_126d_accel_v084_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity netmargin
def nm_f50_net_margin_per_equity_252d_accel_v085_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity netmargin
def nm_f50_net_margin_per_equity_252d_accel_v086_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity netmargin
def nm_f50_net_margin_per_equity_252d_accel_v087_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity netmargin
def nm_f50_net_margin_per_equity_504d_accel_v088_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity netmargin
def nm_f50_net_margin_per_equity_504d_accel_v089_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity netmargin
def nm_f50_net_margin_per_equity_504d_accel_v090_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std netmargin
def nm_f50_net_margin_std_21d_accel_v091_signal(netmargin, closeadj):
    base = _std(netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std netmargin
def nm_f50_net_margin_std_21d_accel_v092_signal(netmargin, closeadj):
    base = _std(netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std netmargin
def nm_f50_net_margin_std_21d_accel_v093_signal(netmargin, closeadj):
    base = _std(netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std netmargin
def nm_f50_net_margin_std_63d_accel_v094_signal(netmargin, closeadj):
    base = _std(netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std netmargin
def nm_f50_net_margin_std_63d_accel_v095_signal(netmargin, closeadj):
    base = _std(netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std netmargin
def nm_f50_net_margin_std_63d_accel_v096_signal(netmargin, closeadj):
    base = _std(netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std netmargin
def nm_f50_net_margin_std_126d_accel_v097_signal(netmargin, closeadj):
    base = _std(netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std netmargin
def nm_f50_net_margin_std_126d_accel_v098_signal(netmargin, closeadj):
    base = _std(netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std netmargin
def nm_f50_net_margin_std_126d_accel_v099_signal(netmargin, closeadj):
    base = _std(netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std netmargin
def nm_f50_net_margin_std_252d_accel_v100_signal(netmargin, closeadj):
    base = _std(netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std netmargin
def nm_f50_net_margin_std_252d_accel_v101_signal(netmargin, closeadj):
    base = _std(netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std netmargin
def nm_f50_net_margin_std_252d_accel_v102_signal(netmargin, closeadj):
    base = _std(netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std netmargin
def nm_f50_net_margin_std_504d_accel_v103_signal(netmargin, closeadj):
    base = _std(netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std netmargin
def nm_f50_net_margin_std_504d_accel_v104_signal(netmargin, closeadj):
    base = _std(netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std netmargin
def nm_f50_net_margin_std_504d_accel_v105_signal(netmargin, closeadj):
    base = _std(netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm netmargin
def nm_f50_net_margin_ewm_21d_accel_v106_signal(netmargin, closeadj):
    base = netmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm netmargin
def nm_f50_net_margin_ewm_21d_accel_v107_signal(netmargin, closeadj):
    base = netmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm netmargin
def nm_f50_net_margin_ewm_21d_accel_v108_signal(netmargin, closeadj):
    base = netmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm netmargin
def nm_f50_net_margin_ewm_63d_accel_v109_signal(netmargin, closeadj):
    base = netmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm netmargin
def nm_f50_net_margin_ewm_63d_accel_v110_signal(netmargin, closeadj):
    base = netmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm netmargin
def nm_f50_net_margin_ewm_63d_accel_v111_signal(netmargin, closeadj):
    base = netmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm netmargin
def nm_f50_net_margin_ewm_126d_accel_v112_signal(netmargin, closeadj):
    base = netmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm netmargin
def nm_f50_net_margin_ewm_126d_accel_v113_signal(netmargin, closeadj):
    base = netmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm netmargin
def nm_f50_net_margin_ewm_126d_accel_v114_signal(netmargin, closeadj):
    base = netmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm netmargin
def nm_f50_net_margin_ewm_252d_accel_v115_signal(netmargin, closeadj):
    base = netmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm netmargin
def nm_f50_net_margin_ewm_252d_accel_v116_signal(netmargin, closeadj):
    base = netmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm netmargin
def nm_f50_net_margin_ewm_252d_accel_v117_signal(netmargin, closeadj):
    base = netmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm netmargin
def nm_f50_net_margin_ewm_504d_accel_v118_signal(netmargin, closeadj):
    base = netmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm netmargin
def nm_f50_net_margin_ewm_504d_accel_v119_signal(netmargin, closeadj):
    base = netmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm netmargin
def nm_f50_net_margin_ewm_504d_accel_v120_signal(netmargin, closeadj):
    base = netmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq netmargin
def nm_f50_net_margin_sq_21d_accel_v121_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq netmargin
def nm_f50_net_margin_sq_21d_accel_v122_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq netmargin
def nm_f50_net_margin_sq_21d_accel_v123_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq netmargin
def nm_f50_net_margin_sq_63d_accel_v124_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq netmargin
def nm_f50_net_margin_sq_63d_accel_v125_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq netmargin
def nm_f50_net_margin_sq_63d_accel_v126_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq netmargin
def nm_f50_net_margin_sq_126d_accel_v127_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq netmargin
def nm_f50_net_margin_sq_126d_accel_v128_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq netmargin
def nm_f50_net_margin_sq_126d_accel_v129_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq netmargin
def nm_f50_net_margin_sq_252d_accel_v130_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq netmargin
def nm_f50_net_margin_sq_252d_accel_v131_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq netmargin
def nm_f50_net_margin_sq_252d_accel_v132_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq netmargin
def nm_f50_net_margin_sq_504d_accel_v133_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq netmargin
def nm_f50_net_margin_sq_504d_accel_v134_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq netmargin
def nm_f50_net_margin_sq_504d_accel_v135_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z netmargin
def nm_f50_net_margin_z_21d_accel_v136_signal(netmargin):
    base = _z(netmargin, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z netmargin
def nm_f50_net_margin_z_21d_accel_v137_signal(netmargin):
    base = _z(netmargin, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z netmargin
def nm_f50_net_margin_z_21d_accel_v138_signal(netmargin):
    base = _z(netmargin, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z netmargin
def nm_f50_net_margin_z_63d_accel_v139_signal(netmargin):
    base = _z(netmargin, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z netmargin
def nm_f50_net_margin_z_63d_accel_v140_signal(netmargin):
    base = _z(netmargin, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z netmargin
def nm_f50_net_margin_z_63d_accel_v141_signal(netmargin):
    base = _z(netmargin, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z netmargin
def nm_f50_net_margin_z_126d_accel_v142_signal(netmargin):
    base = _z(netmargin, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z netmargin
def nm_f50_net_margin_z_126d_accel_v143_signal(netmargin):
    base = _z(netmargin, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z netmargin
def nm_f50_net_margin_z_126d_accel_v144_signal(netmargin):
    base = _z(netmargin, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z netmargin
def nm_f50_net_margin_z_252d_accel_v145_signal(netmargin):
    base = _z(netmargin, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z netmargin
def nm_f50_net_margin_z_252d_accel_v146_signal(netmargin):
    base = _z(netmargin, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z netmargin
def nm_f50_net_margin_z_252d_accel_v147_signal(netmargin):
    base = _z(netmargin, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z netmargin
def nm_f50_net_margin_z_504d_accel_v148_signal(netmargin):
    base = _z(netmargin, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z netmargin
def nm_f50_net_margin_z_504d_accel_v149_signal(netmargin):
    base = _z(netmargin, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z netmargin
def nm_f50_net_margin_z_504d_accel_v150_signal(netmargin):
    base = _z(netmargin, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
