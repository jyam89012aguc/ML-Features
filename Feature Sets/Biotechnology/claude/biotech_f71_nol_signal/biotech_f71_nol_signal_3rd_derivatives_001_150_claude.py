"""Family f71 - Tax position / NOL signal  (L_EarningsQuality) | 3rd derivatives 001-150"""
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
def _nol_signal_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _nol_signal_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _nol_signal_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw taxexp
def nol_f71_nol_signal_raw_21d_accel_v001_signal(taxexp, closeadj):
    base = _mean(taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw taxexp
def nol_f71_nol_signal_raw_21d_accel_v002_signal(taxexp, closeadj):
    base = _mean(taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw taxexp
def nol_f71_nol_signal_raw_21d_accel_v003_signal(taxexp, closeadj):
    base = _mean(taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw taxexp
def nol_f71_nol_signal_raw_63d_accel_v004_signal(taxexp, closeadj):
    base = _mean(taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw taxexp
def nol_f71_nol_signal_raw_63d_accel_v005_signal(taxexp, closeadj):
    base = _mean(taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw taxexp
def nol_f71_nol_signal_raw_63d_accel_v006_signal(taxexp, closeadj):
    base = _mean(taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw taxexp
def nol_f71_nol_signal_raw_126d_accel_v007_signal(taxexp, closeadj):
    base = _mean(taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw taxexp
def nol_f71_nol_signal_raw_126d_accel_v008_signal(taxexp, closeadj):
    base = _mean(taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw taxexp
def nol_f71_nol_signal_raw_126d_accel_v009_signal(taxexp, closeadj):
    base = _mean(taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw taxexp
def nol_f71_nol_signal_raw_252d_accel_v010_signal(taxexp, closeadj):
    base = _mean(taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw taxexp
def nol_f71_nol_signal_raw_252d_accel_v011_signal(taxexp, closeadj):
    base = _mean(taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw taxexp
def nol_f71_nol_signal_raw_252d_accel_v012_signal(taxexp, closeadj):
    base = _mean(taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw taxexp
def nol_f71_nol_signal_raw_504d_accel_v013_signal(taxexp, closeadj):
    base = _mean(taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw taxexp
def nol_f71_nol_signal_raw_504d_accel_v014_signal(taxexp, closeadj):
    base = _mean(taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw taxexp
def nol_f71_nol_signal_raw_504d_accel_v015_signal(taxexp, closeadj):
    base = _mean(taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log taxexp
def nol_f71_nol_signal_log_21d_accel_v016_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log taxexp
def nol_f71_nol_signal_log_21d_accel_v017_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log taxexp
def nol_f71_nol_signal_log_21d_accel_v018_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log taxexp
def nol_f71_nol_signal_log_63d_accel_v019_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log taxexp
def nol_f71_nol_signal_log_63d_accel_v020_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log taxexp
def nol_f71_nol_signal_log_63d_accel_v021_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log taxexp
def nol_f71_nol_signal_log_126d_accel_v022_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log taxexp
def nol_f71_nol_signal_log_126d_accel_v023_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log taxexp
def nol_f71_nol_signal_log_126d_accel_v024_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log taxexp
def nol_f71_nol_signal_log_252d_accel_v025_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log taxexp
def nol_f71_nol_signal_log_252d_accel_v026_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log taxexp
def nol_f71_nol_signal_log_252d_accel_v027_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log taxexp
def nol_f71_nol_signal_log_504d_accel_v028_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log taxexp
def nol_f71_nol_signal_log_504d_accel_v029_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log taxexp
def nol_f71_nol_signal_log_504d_accel_v030_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare taxexp
def nol_f71_nol_signal_pershare_21d_accel_v031_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare taxexp
def nol_f71_nol_signal_pershare_21d_accel_v032_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare taxexp
def nol_f71_nol_signal_pershare_21d_accel_v033_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare taxexp
def nol_f71_nol_signal_pershare_63d_accel_v034_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare taxexp
def nol_f71_nol_signal_pershare_63d_accel_v035_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare taxexp
def nol_f71_nol_signal_pershare_63d_accel_v036_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare taxexp
def nol_f71_nol_signal_pershare_126d_accel_v037_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare taxexp
def nol_f71_nol_signal_pershare_126d_accel_v038_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare taxexp
def nol_f71_nol_signal_pershare_126d_accel_v039_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare taxexp
def nol_f71_nol_signal_pershare_252d_accel_v040_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare taxexp
def nol_f71_nol_signal_pershare_252d_accel_v041_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare taxexp
def nol_f71_nol_signal_pershare_252d_accel_v042_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare taxexp
def nol_f71_nol_signal_pershare_504d_accel_v043_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare taxexp
def nol_f71_nol_signal_pershare_504d_accel_v044_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare taxexp
def nol_f71_nol_signal_pershare_504d_accel_v045_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets taxexp
def nol_f71_nol_signal_per_assets_21d_accel_v046_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets taxexp
def nol_f71_nol_signal_per_assets_21d_accel_v047_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets taxexp
def nol_f71_nol_signal_per_assets_21d_accel_v048_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets taxexp
def nol_f71_nol_signal_per_assets_63d_accel_v049_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets taxexp
def nol_f71_nol_signal_per_assets_63d_accel_v050_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets taxexp
def nol_f71_nol_signal_per_assets_63d_accel_v051_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets taxexp
def nol_f71_nol_signal_per_assets_126d_accel_v052_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets taxexp
def nol_f71_nol_signal_per_assets_126d_accel_v053_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets taxexp
def nol_f71_nol_signal_per_assets_126d_accel_v054_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets taxexp
def nol_f71_nol_signal_per_assets_252d_accel_v055_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets taxexp
def nol_f71_nol_signal_per_assets_252d_accel_v056_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets taxexp
def nol_f71_nol_signal_per_assets_252d_accel_v057_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets taxexp
def nol_f71_nol_signal_per_assets_504d_accel_v058_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets taxexp
def nol_f71_nol_signal_per_assets_504d_accel_v059_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets taxexp
def nol_f71_nol_signal_per_assets_504d_accel_v060_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_21d_accel_v061_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_21d_accel_v062_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_21d_accel_v063_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_63d_accel_v064_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_63d_accel_v065_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_63d_accel_v066_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_126d_accel_v067_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_126d_accel_v068_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_126d_accel_v069_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_252d_accel_v070_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_252d_accel_v071_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_252d_accel_v072_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_504d_accel_v073_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_504d_accel_v074_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_504d_accel_v075_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity taxexp
def nol_f71_nol_signal_per_equity_21d_accel_v076_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity taxexp
def nol_f71_nol_signal_per_equity_21d_accel_v077_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity taxexp
def nol_f71_nol_signal_per_equity_21d_accel_v078_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity taxexp
def nol_f71_nol_signal_per_equity_63d_accel_v079_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity taxexp
def nol_f71_nol_signal_per_equity_63d_accel_v080_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity taxexp
def nol_f71_nol_signal_per_equity_63d_accel_v081_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity taxexp
def nol_f71_nol_signal_per_equity_126d_accel_v082_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity taxexp
def nol_f71_nol_signal_per_equity_126d_accel_v083_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity taxexp
def nol_f71_nol_signal_per_equity_126d_accel_v084_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity taxexp
def nol_f71_nol_signal_per_equity_252d_accel_v085_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity taxexp
def nol_f71_nol_signal_per_equity_252d_accel_v086_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity taxexp
def nol_f71_nol_signal_per_equity_252d_accel_v087_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity taxexp
def nol_f71_nol_signal_per_equity_504d_accel_v088_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity taxexp
def nol_f71_nol_signal_per_equity_504d_accel_v089_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity taxexp
def nol_f71_nol_signal_per_equity_504d_accel_v090_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std taxexp
def nol_f71_nol_signal_std_21d_accel_v091_signal(taxexp, closeadj):
    base = _std(taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std taxexp
def nol_f71_nol_signal_std_21d_accel_v092_signal(taxexp, closeadj):
    base = _std(taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std taxexp
def nol_f71_nol_signal_std_21d_accel_v093_signal(taxexp, closeadj):
    base = _std(taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std taxexp
def nol_f71_nol_signal_std_63d_accel_v094_signal(taxexp, closeadj):
    base = _std(taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std taxexp
def nol_f71_nol_signal_std_63d_accel_v095_signal(taxexp, closeadj):
    base = _std(taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std taxexp
def nol_f71_nol_signal_std_63d_accel_v096_signal(taxexp, closeadj):
    base = _std(taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std taxexp
def nol_f71_nol_signal_std_126d_accel_v097_signal(taxexp, closeadj):
    base = _std(taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std taxexp
def nol_f71_nol_signal_std_126d_accel_v098_signal(taxexp, closeadj):
    base = _std(taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std taxexp
def nol_f71_nol_signal_std_126d_accel_v099_signal(taxexp, closeadj):
    base = _std(taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std taxexp
def nol_f71_nol_signal_std_252d_accel_v100_signal(taxexp, closeadj):
    base = _std(taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std taxexp
def nol_f71_nol_signal_std_252d_accel_v101_signal(taxexp, closeadj):
    base = _std(taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std taxexp
def nol_f71_nol_signal_std_252d_accel_v102_signal(taxexp, closeadj):
    base = _std(taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std taxexp
def nol_f71_nol_signal_std_504d_accel_v103_signal(taxexp, closeadj):
    base = _std(taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std taxexp
def nol_f71_nol_signal_std_504d_accel_v104_signal(taxexp, closeadj):
    base = _std(taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std taxexp
def nol_f71_nol_signal_std_504d_accel_v105_signal(taxexp, closeadj):
    base = _std(taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm taxexp
def nol_f71_nol_signal_ewm_21d_accel_v106_signal(taxexp, closeadj):
    base = taxexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm taxexp
def nol_f71_nol_signal_ewm_21d_accel_v107_signal(taxexp, closeadj):
    base = taxexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm taxexp
def nol_f71_nol_signal_ewm_21d_accel_v108_signal(taxexp, closeadj):
    base = taxexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm taxexp
def nol_f71_nol_signal_ewm_63d_accel_v109_signal(taxexp, closeadj):
    base = taxexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm taxexp
def nol_f71_nol_signal_ewm_63d_accel_v110_signal(taxexp, closeadj):
    base = taxexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm taxexp
def nol_f71_nol_signal_ewm_63d_accel_v111_signal(taxexp, closeadj):
    base = taxexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm taxexp
def nol_f71_nol_signal_ewm_126d_accel_v112_signal(taxexp, closeadj):
    base = taxexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm taxexp
def nol_f71_nol_signal_ewm_126d_accel_v113_signal(taxexp, closeadj):
    base = taxexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm taxexp
def nol_f71_nol_signal_ewm_126d_accel_v114_signal(taxexp, closeadj):
    base = taxexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm taxexp
def nol_f71_nol_signal_ewm_252d_accel_v115_signal(taxexp, closeadj):
    base = taxexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm taxexp
def nol_f71_nol_signal_ewm_252d_accel_v116_signal(taxexp, closeadj):
    base = taxexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm taxexp
def nol_f71_nol_signal_ewm_252d_accel_v117_signal(taxexp, closeadj):
    base = taxexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm taxexp
def nol_f71_nol_signal_ewm_504d_accel_v118_signal(taxexp, closeadj):
    base = taxexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm taxexp
def nol_f71_nol_signal_ewm_504d_accel_v119_signal(taxexp, closeadj):
    base = taxexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm taxexp
def nol_f71_nol_signal_ewm_504d_accel_v120_signal(taxexp, closeadj):
    base = taxexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq taxexp
def nol_f71_nol_signal_sq_21d_accel_v121_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq taxexp
def nol_f71_nol_signal_sq_21d_accel_v122_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq taxexp
def nol_f71_nol_signal_sq_21d_accel_v123_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq taxexp
def nol_f71_nol_signal_sq_63d_accel_v124_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq taxexp
def nol_f71_nol_signal_sq_63d_accel_v125_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq taxexp
def nol_f71_nol_signal_sq_63d_accel_v126_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq taxexp
def nol_f71_nol_signal_sq_126d_accel_v127_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq taxexp
def nol_f71_nol_signal_sq_126d_accel_v128_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq taxexp
def nol_f71_nol_signal_sq_126d_accel_v129_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq taxexp
def nol_f71_nol_signal_sq_252d_accel_v130_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq taxexp
def nol_f71_nol_signal_sq_252d_accel_v131_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq taxexp
def nol_f71_nol_signal_sq_252d_accel_v132_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq taxexp
def nol_f71_nol_signal_sq_504d_accel_v133_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq taxexp
def nol_f71_nol_signal_sq_504d_accel_v134_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq taxexp
def nol_f71_nol_signal_sq_504d_accel_v135_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z taxexp
def nol_f71_nol_signal_z_21d_accel_v136_signal(taxexp):
    base = _z(taxexp, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z taxexp
def nol_f71_nol_signal_z_21d_accel_v137_signal(taxexp):
    base = _z(taxexp, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z taxexp
def nol_f71_nol_signal_z_21d_accel_v138_signal(taxexp):
    base = _z(taxexp, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z taxexp
def nol_f71_nol_signal_z_63d_accel_v139_signal(taxexp):
    base = _z(taxexp, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z taxexp
def nol_f71_nol_signal_z_63d_accel_v140_signal(taxexp):
    base = _z(taxexp, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z taxexp
def nol_f71_nol_signal_z_63d_accel_v141_signal(taxexp):
    base = _z(taxexp, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z taxexp
def nol_f71_nol_signal_z_126d_accel_v142_signal(taxexp):
    base = _z(taxexp, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z taxexp
def nol_f71_nol_signal_z_126d_accel_v143_signal(taxexp):
    base = _z(taxexp, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z taxexp
def nol_f71_nol_signal_z_126d_accel_v144_signal(taxexp):
    base = _z(taxexp, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z taxexp
def nol_f71_nol_signal_z_252d_accel_v145_signal(taxexp):
    base = _z(taxexp, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z taxexp
def nol_f71_nol_signal_z_252d_accel_v146_signal(taxexp):
    base = _z(taxexp, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z taxexp
def nol_f71_nol_signal_z_252d_accel_v147_signal(taxexp):
    base = _z(taxexp, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z taxexp
def nol_f71_nol_signal_z_504d_accel_v148_signal(taxexp):
    base = _z(taxexp, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z taxexp
def nol_f71_nol_signal_z_504d_accel_v149_signal(taxexp):
    base = _z(taxexp, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z taxexp
def nol_f71_nol_signal_z_504d_accel_v150_signal(taxexp):
    base = _z(taxexp, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
