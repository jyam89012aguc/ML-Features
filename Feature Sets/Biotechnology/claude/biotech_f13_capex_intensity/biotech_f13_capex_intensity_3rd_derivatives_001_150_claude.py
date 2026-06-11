"""Family f13 - Capex intensity  (B_CashFlow_Burn) | 3rd derivatives 001-150"""
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
def _capex_intensity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capex_intensity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capex_intensity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw capex
def cxi_f13_capex_intensity_raw_21d_accel_v001_signal(capex, closeadj):
    base = _mean(capex, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw capex
def cxi_f13_capex_intensity_raw_21d_accel_v002_signal(capex, closeadj):
    base = _mean(capex, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw capex
def cxi_f13_capex_intensity_raw_21d_accel_v003_signal(capex, closeadj):
    base = _mean(capex, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw capex
def cxi_f13_capex_intensity_raw_63d_accel_v004_signal(capex, closeadj):
    base = _mean(capex, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw capex
def cxi_f13_capex_intensity_raw_63d_accel_v005_signal(capex, closeadj):
    base = _mean(capex, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw capex
def cxi_f13_capex_intensity_raw_63d_accel_v006_signal(capex, closeadj):
    base = _mean(capex, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw capex
def cxi_f13_capex_intensity_raw_126d_accel_v007_signal(capex, closeadj):
    base = _mean(capex, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw capex
def cxi_f13_capex_intensity_raw_126d_accel_v008_signal(capex, closeadj):
    base = _mean(capex, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw capex
def cxi_f13_capex_intensity_raw_126d_accel_v009_signal(capex, closeadj):
    base = _mean(capex, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw capex
def cxi_f13_capex_intensity_raw_252d_accel_v010_signal(capex, closeadj):
    base = _mean(capex, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw capex
def cxi_f13_capex_intensity_raw_252d_accel_v011_signal(capex, closeadj):
    base = _mean(capex, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw capex
def cxi_f13_capex_intensity_raw_252d_accel_v012_signal(capex, closeadj):
    base = _mean(capex, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw capex
def cxi_f13_capex_intensity_raw_504d_accel_v013_signal(capex, closeadj):
    base = _mean(capex, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw capex
def cxi_f13_capex_intensity_raw_504d_accel_v014_signal(capex, closeadj):
    base = _mean(capex, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw capex
def cxi_f13_capex_intensity_raw_504d_accel_v015_signal(capex, closeadj):
    base = _mean(capex, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log capex
def cxi_f13_capex_intensity_log_21d_accel_v016_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log capex
def cxi_f13_capex_intensity_log_21d_accel_v017_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log capex
def cxi_f13_capex_intensity_log_21d_accel_v018_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log capex
def cxi_f13_capex_intensity_log_63d_accel_v019_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log capex
def cxi_f13_capex_intensity_log_63d_accel_v020_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log capex
def cxi_f13_capex_intensity_log_63d_accel_v021_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log capex
def cxi_f13_capex_intensity_log_126d_accel_v022_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log capex
def cxi_f13_capex_intensity_log_126d_accel_v023_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log capex
def cxi_f13_capex_intensity_log_126d_accel_v024_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log capex
def cxi_f13_capex_intensity_log_252d_accel_v025_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log capex
def cxi_f13_capex_intensity_log_252d_accel_v026_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log capex
def cxi_f13_capex_intensity_log_252d_accel_v027_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log capex
def cxi_f13_capex_intensity_log_504d_accel_v028_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log capex
def cxi_f13_capex_intensity_log_504d_accel_v029_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log capex
def cxi_f13_capex_intensity_log_504d_accel_v030_signal(capex, closeadj):
    base = _mean(_capex_intensity_log(capex), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare capex
def cxi_f13_capex_intensity_pershare_21d_accel_v031_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare capex
def cxi_f13_capex_intensity_pershare_21d_accel_v032_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare capex
def cxi_f13_capex_intensity_pershare_21d_accel_v033_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare capex
def cxi_f13_capex_intensity_pershare_63d_accel_v034_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare capex
def cxi_f13_capex_intensity_pershare_63d_accel_v035_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare capex
def cxi_f13_capex_intensity_pershare_63d_accel_v036_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare capex
def cxi_f13_capex_intensity_pershare_126d_accel_v037_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare capex
def cxi_f13_capex_intensity_pershare_126d_accel_v038_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare capex
def cxi_f13_capex_intensity_pershare_126d_accel_v039_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare capex
def cxi_f13_capex_intensity_pershare_252d_accel_v040_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare capex
def cxi_f13_capex_intensity_pershare_252d_accel_v041_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare capex
def cxi_f13_capex_intensity_pershare_252d_accel_v042_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare capex
def cxi_f13_capex_intensity_pershare_504d_accel_v043_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare capex
def cxi_f13_capex_intensity_pershare_504d_accel_v044_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare capex
def cxi_f13_capex_intensity_pershare_504d_accel_v045_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_intensity_per_share(capex, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets capex
def cxi_f13_capex_intensity_per_assets_21d_accel_v046_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets capex
def cxi_f13_capex_intensity_per_assets_21d_accel_v047_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets capex
def cxi_f13_capex_intensity_per_assets_21d_accel_v048_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets capex
def cxi_f13_capex_intensity_per_assets_63d_accel_v049_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets capex
def cxi_f13_capex_intensity_per_assets_63d_accel_v050_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets capex
def cxi_f13_capex_intensity_per_assets_63d_accel_v051_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets capex
def cxi_f13_capex_intensity_per_assets_126d_accel_v052_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets capex
def cxi_f13_capex_intensity_per_assets_126d_accel_v053_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets capex
def cxi_f13_capex_intensity_per_assets_126d_accel_v054_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets capex
def cxi_f13_capex_intensity_per_assets_252d_accel_v055_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets capex
def cxi_f13_capex_intensity_per_assets_252d_accel_v056_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets capex
def cxi_f13_capex_intensity_per_assets_252d_accel_v057_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets capex
def cxi_f13_capex_intensity_per_assets_504d_accel_v058_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets capex
def cxi_f13_capex_intensity_per_assets_504d_accel_v059_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets capex
def cxi_f13_capex_intensity_per_assets_504d_accel_v060_signal(capex, assets):
    base = _mean(_capex_intensity_scaled(capex, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_21d_accel_v061_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_21d_accel_v062_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_21d_accel_v063_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_63d_accel_v064_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_63d_accel_v065_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_63d_accel_v066_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_126d_accel_v067_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_126d_accel_v068_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_126d_accel_v069_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_252d_accel_v070_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_252d_accel_v071_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_252d_accel_v072_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_504d_accel_v073_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_504d_accel_v074_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap capex
def cxi_f13_capex_intensity_per_marketcap_504d_accel_v075_signal(capex, marketcap):
    base = _mean(_capex_intensity_scaled(capex, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity capex
def cxi_f13_capex_intensity_per_equity_21d_accel_v076_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity capex
def cxi_f13_capex_intensity_per_equity_21d_accel_v077_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity capex
def cxi_f13_capex_intensity_per_equity_21d_accel_v078_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity capex
def cxi_f13_capex_intensity_per_equity_63d_accel_v079_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity capex
def cxi_f13_capex_intensity_per_equity_63d_accel_v080_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity capex
def cxi_f13_capex_intensity_per_equity_63d_accel_v081_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity capex
def cxi_f13_capex_intensity_per_equity_126d_accel_v082_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity capex
def cxi_f13_capex_intensity_per_equity_126d_accel_v083_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity capex
def cxi_f13_capex_intensity_per_equity_126d_accel_v084_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity capex
def cxi_f13_capex_intensity_per_equity_252d_accel_v085_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity capex
def cxi_f13_capex_intensity_per_equity_252d_accel_v086_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity capex
def cxi_f13_capex_intensity_per_equity_252d_accel_v087_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity capex
def cxi_f13_capex_intensity_per_equity_504d_accel_v088_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity capex
def cxi_f13_capex_intensity_per_equity_504d_accel_v089_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity capex
def cxi_f13_capex_intensity_per_equity_504d_accel_v090_signal(capex, equity):
    base = _mean(_capex_intensity_scaled(capex, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std capex
def cxi_f13_capex_intensity_std_21d_accel_v091_signal(capex, closeadj):
    base = _std(capex, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std capex
def cxi_f13_capex_intensity_std_21d_accel_v092_signal(capex, closeadj):
    base = _std(capex, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std capex
def cxi_f13_capex_intensity_std_21d_accel_v093_signal(capex, closeadj):
    base = _std(capex, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std capex
def cxi_f13_capex_intensity_std_63d_accel_v094_signal(capex, closeadj):
    base = _std(capex, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std capex
def cxi_f13_capex_intensity_std_63d_accel_v095_signal(capex, closeadj):
    base = _std(capex, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std capex
def cxi_f13_capex_intensity_std_63d_accel_v096_signal(capex, closeadj):
    base = _std(capex, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std capex
def cxi_f13_capex_intensity_std_126d_accel_v097_signal(capex, closeadj):
    base = _std(capex, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std capex
def cxi_f13_capex_intensity_std_126d_accel_v098_signal(capex, closeadj):
    base = _std(capex, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std capex
def cxi_f13_capex_intensity_std_126d_accel_v099_signal(capex, closeadj):
    base = _std(capex, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std capex
def cxi_f13_capex_intensity_std_252d_accel_v100_signal(capex, closeadj):
    base = _std(capex, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std capex
def cxi_f13_capex_intensity_std_252d_accel_v101_signal(capex, closeadj):
    base = _std(capex, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std capex
def cxi_f13_capex_intensity_std_252d_accel_v102_signal(capex, closeadj):
    base = _std(capex, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std capex
def cxi_f13_capex_intensity_std_504d_accel_v103_signal(capex, closeadj):
    base = _std(capex, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std capex
def cxi_f13_capex_intensity_std_504d_accel_v104_signal(capex, closeadj):
    base = _std(capex, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std capex
def cxi_f13_capex_intensity_std_504d_accel_v105_signal(capex, closeadj):
    base = _std(capex, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm capex
def cxi_f13_capex_intensity_ewm_21d_accel_v106_signal(capex, closeadj):
    base = capex.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm capex
def cxi_f13_capex_intensity_ewm_21d_accel_v107_signal(capex, closeadj):
    base = capex.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm capex
def cxi_f13_capex_intensity_ewm_21d_accel_v108_signal(capex, closeadj):
    base = capex.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm capex
def cxi_f13_capex_intensity_ewm_63d_accel_v109_signal(capex, closeadj):
    base = capex.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm capex
def cxi_f13_capex_intensity_ewm_63d_accel_v110_signal(capex, closeadj):
    base = capex.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm capex
def cxi_f13_capex_intensity_ewm_63d_accel_v111_signal(capex, closeadj):
    base = capex.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm capex
def cxi_f13_capex_intensity_ewm_126d_accel_v112_signal(capex, closeadj):
    base = capex.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm capex
def cxi_f13_capex_intensity_ewm_126d_accel_v113_signal(capex, closeadj):
    base = capex.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm capex
def cxi_f13_capex_intensity_ewm_126d_accel_v114_signal(capex, closeadj):
    base = capex.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm capex
def cxi_f13_capex_intensity_ewm_252d_accel_v115_signal(capex, closeadj):
    base = capex.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm capex
def cxi_f13_capex_intensity_ewm_252d_accel_v116_signal(capex, closeadj):
    base = capex.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm capex
def cxi_f13_capex_intensity_ewm_252d_accel_v117_signal(capex, closeadj):
    base = capex.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm capex
def cxi_f13_capex_intensity_ewm_504d_accel_v118_signal(capex, closeadj):
    base = capex.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm capex
def cxi_f13_capex_intensity_ewm_504d_accel_v119_signal(capex, closeadj):
    base = capex.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm capex
def cxi_f13_capex_intensity_ewm_504d_accel_v120_signal(capex, closeadj):
    base = capex.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq capex
def cxi_f13_capex_intensity_sq_21d_accel_v121_signal(capex, closeadj):
    base = _mean(capex * capex, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq capex
def cxi_f13_capex_intensity_sq_21d_accel_v122_signal(capex, closeadj):
    base = _mean(capex * capex, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq capex
def cxi_f13_capex_intensity_sq_21d_accel_v123_signal(capex, closeadj):
    base = _mean(capex * capex, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq capex
def cxi_f13_capex_intensity_sq_63d_accel_v124_signal(capex, closeadj):
    base = _mean(capex * capex, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq capex
def cxi_f13_capex_intensity_sq_63d_accel_v125_signal(capex, closeadj):
    base = _mean(capex * capex, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq capex
def cxi_f13_capex_intensity_sq_63d_accel_v126_signal(capex, closeadj):
    base = _mean(capex * capex, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq capex
def cxi_f13_capex_intensity_sq_126d_accel_v127_signal(capex, closeadj):
    base = _mean(capex * capex, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq capex
def cxi_f13_capex_intensity_sq_126d_accel_v128_signal(capex, closeadj):
    base = _mean(capex * capex, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq capex
def cxi_f13_capex_intensity_sq_126d_accel_v129_signal(capex, closeadj):
    base = _mean(capex * capex, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq capex
def cxi_f13_capex_intensity_sq_252d_accel_v130_signal(capex, closeadj):
    base = _mean(capex * capex, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq capex
def cxi_f13_capex_intensity_sq_252d_accel_v131_signal(capex, closeadj):
    base = _mean(capex * capex, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq capex
def cxi_f13_capex_intensity_sq_252d_accel_v132_signal(capex, closeadj):
    base = _mean(capex * capex, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq capex
def cxi_f13_capex_intensity_sq_504d_accel_v133_signal(capex, closeadj):
    base = _mean(capex * capex, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq capex
def cxi_f13_capex_intensity_sq_504d_accel_v134_signal(capex, closeadj):
    base = _mean(capex * capex, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq capex
def cxi_f13_capex_intensity_sq_504d_accel_v135_signal(capex, closeadj):
    base = _mean(capex * capex, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z capex
def cxi_f13_capex_intensity_z_21d_accel_v136_signal(capex):
    base = _z(capex, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z capex
def cxi_f13_capex_intensity_z_21d_accel_v137_signal(capex):
    base = _z(capex, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z capex
def cxi_f13_capex_intensity_z_21d_accel_v138_signal(capex):
    base = _z(capex, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z capex
def cxi_f13_capex_intensity_z_63d_accel_v139_signal(capex):
    base = _z(capex, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z capex
def cxi_f13_capex_intensity_z_63d_accel_v140_signal(capex):
    base = _z(capex, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z capex
def cxi_f13_capex_intensity_z_63d_accel_v141_signal(capex):
    base = _z(capex, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z capex
def cxi_f13_capex_intensity_z_126d_accel_v142_signal(capex):
    base = _z(capex, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z capex
def cxi_f13_capex_intensity_z_126d_accel_v143_signal(capex):
    base = _z(capex, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z capex
def cxi_f13_capex_intensity_z_126d_accel_v144_signal(capex):
    base = _z(capex, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z capex
def cxi_f13_capex_intensity_z_252d_accel_v145_signal(capex):
    base = _z(capex, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z capex
def cxi_f13_capex_intensity_z_252d_accel_v146_signal(capex):
    base = _z(capex, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z capex
def cxi_f13_capex_intensity_z_252d_accel_v147_signal(capex):
    base = _z(capex, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z capex
def cxi_f13_capex_intensity_z_504d_accel_v148_signal(capex):
    base = _z(capex, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z capex
def cxi_f13_capex_intensity_z_504d_accel_v149_signal(capex):
    base = _z(capex, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z capex
def cxi_f13_capex_intensity_z_504d_accel_v150_signal(capex):
    base = _z(capex, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
