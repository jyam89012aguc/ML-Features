"""Family f31 - Stock-based compensation level  (E_Dilution_Shares) | 3rd derivatives 001-150"""
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
def _sbc_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sbc_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sbc_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw sbcomp
def sbl_f31_sbc_level_raw_21d_accel_v001_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw sbcomp
def sbl_f31_sbc_level_raw_21d_accel_v002_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw sbcomp
def sbl_f31_sbc_level_raw_21d_accel_v003_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw sbcomp
def sbl_f31_sbc_level_raw_63d_accel_v004_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw sbcomp
def sbl_f31_sbc_level_raw_63d_accel_v005_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw sbcomp
def sbl_f31_sbc_level_raw_63d_accel_v006_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw sbcomp
def sbl_f31_sbc_level_raw_126d_accel_v007_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw sbcomp
def sbl_f31_sbc_level_raw_126d_accel_v008_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw sbcomp
def sbl_f31_sbc_level_raw_126d_accel_v009_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw sbcomp
def sbl_f31_sbc_level_raw_252d_accel_v010_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw sbcomp
def sbl_f31_sbc_level_raw_252d_accel_v011_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw sbcomp
def sbl_f31_sbc_level_raw_252d_accel_v012_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw sbcomp
def sbl_f31_sbc_level_raw_504d_accel_v013_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw sbcomp
def sbl_f31_sbc_level_raw_504d_accel_v014_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw sbcomp
def sbl_f31_sbc_level_raw_504d_accel_v015_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log sbcomp
def sbl_f31_sbc_level_log_21d_accel_v016_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log sbcomp
def sbl_f31_sbc_level_log_21d_accel_v017_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log sbcomp
def sbl_f31_sbc_level_log_21d_accel_v018_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log sbcomp
def sbl_f31_sbc_level_log_63d_accel_v019_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log sbcomp
def sbl_f31_sbc_level_log_63d_accel_v020_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log sbcomp
def sbl_f31_sbc_level_log_63d_accel_v021_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log sbcomp
def sbl_f31_sbc_level_log_126d_accel_v022_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log sbcomp
def sbl_f31_sbc_level_log_126d_accel_v023_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log sbcomp
def sbl_f31_sbc_level_log_126d_accel_v024_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log sbcomp
def sbl_f31_sbc_level_log_252d_accel_v025_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log sbcomp
def sbl_f31_sbc_level_log_252d_accel_v026_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log sbcomp
def sbl_f31_sbc_level_log_252d_accel_v027_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log sbcomp
def sbl_f31_sbc_level_log_504d_accel_v028_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log sbcomp
def sbl_f31_sbc_level_log_504d_accel_v029_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log sbcomp
def sbl_f31_sbc_level_log_504d_accel_v030_signal(sbcomp, closeadj):
    base = _mean(_sbc_level_log(sbcomp), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare sbcomp
def sbl_f31_sbc_level_pershare_21d_accel_v031_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare sbcomp
def sbl_f31_sbc_level_pershare_21d_accel_v032_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare sbcomp
def sbl_f31_sbc_level_pershare_21d_accel_v033_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare sbcomp
def sbl_f31_sbc_level_pershare_63d_accel_v034_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare sbcomp
def sbl_f31_sbc_level_pershare_63d_accel_v035_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare sbcomp
def sbl_f31_sbc_level_pershare_63d_accel_v036_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare sbcomp
def sbl_f31_sbc_level_pershare_126d_accel_v037_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare sbcomp
def sbl_f31_sbc_level_pershare_126d_accel_v038_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare sbcomp
def sbl_f31_sbc_level_pershare_126d_accel_v039_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare sbcomp
def sbl_f31_sbc_level_pershare_252d_accel_v040_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare sbcomp
def sbl_f31_sbc_level_pershare_252d_accel_v041_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare sbcomp
def sbl_f31_sbc_level_pershare_252d_accel_v042_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare sbcomp
def sbl_f31_sbc_level_pershare_504d_accel_v043_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare sbcomp
def sbl_f31_sbc_level_pershare_504d_accel_v044_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare sbcomp
def sbl_f31_sbc_level_pershare_504d_accel_v045_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_level_per_share(sbcomp, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_21d_accel_v046_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_21d_accel_v047_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_21d_accel_v048_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_63d_accel_v049_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_63d_accel_v050_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_63d_accel_v051_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_126d_accel_v052_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_126d_accel_v053_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_126d_accel_v054_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_252d_accel_v055_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_252d_accel_v056_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_252d_accel_v057_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_504d_accel_v058_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_504d_accel_v059_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets sbcomp
def sbl_f31_sbc_level_per_assets_504d_accel_v060_signal(sbcomp, assets):
    base = _mean(_sbc_level_scaled(sbcomp, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_21d_accel_v061_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_21d_accel_v062_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_21d_accel_v063_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_63d_accel_v064_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_63d_accel_v065_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_63d_accel_v066_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_126d_accel_v067_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_126d_accel_v068_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_126d_accel_v069_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_252d_accel_v070_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_252d_accel_v071_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_252d_accel_v072_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_504d_accel_v073_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_504d_accel_v074_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap sbcomp
def sbl_f31_sbc_level_per_marketcap_504d_accel_v075_signal(sbcomp, marketcap):
    base = _mean(_sbc_level_scaled(sbcomp, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_21d_accel_v076_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_21d_accel_v077_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_21d_accel_v078_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_63d_accel_v079_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_63d_accel_v080_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_63d_accel_v081_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_126d_accel_v082_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_126d_accel_v083_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_126d_accel_v084_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_252d_accel_v085_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_252d_accel_v086_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_252d_accel_v087_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_504d_accel_v088_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_504d_accel_v089_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity sbcomp
def sbl_f31_sbc_level_per_equity_504d_accel_v090_signal(sbcomp, equity):
    base = _mean(_sbc_level_scaled(sbcomp, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std sbcomp
def sbl_f31_sbc_level_std_21d_accel_v091_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std sbcomp
def sbl_f31_sbc_level_std_21d_accel_v092_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std sbcomp
def sbl_f31_sbc_level_std_21d_accel_v093_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std sbcomp
def sbl_f31_sbc_level_std_63d_accel_v094_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std sbcomp
def sbl_f31_sbc_level_std_63d_accel_v095_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std sbcomp
def sbl_f31_sbc_level_std_63d_accel_v096_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std sbcomp
def sbl_f31_sbc_level_std_126d_accel_v097_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std sbcomp
def sbl_f31_sbc_level_std_126d_accel_v098_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std sbcomp
def sbl_f31_sbc_level_std_126d_accel_v099_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std sbcomp
def sbl_f31_sbc_level_std_252d_accel_v100_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std sbcomp
def sbl_f31_sbc_level_std_252d_accel_v101_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std sbcomp
def sbl_f31_sbc_level_std_252d_accel_v102_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std sbcomp
def sbl_f31_sbc_level_std_504d_accel_v103_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std sbcomp
def sbl_f31_sbc_level_std_504d_accel_v104_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std sbcomp
def sbl_f31_sbc_level_std_504d_accel_v105_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm sbcomp
def sbl_f31_sbc_level_ewm_21d_accel_v106_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm sbcomp
def sbl_f31_sbc_level_ewm_21d_accel_v107_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm sbcomp
def sbl_f31_sbc_level_ewm_21d_accel_v108_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm sbcomp
def sbl_f31_sbc_level_ewm_63d_accel_v109_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm sbcomp
def sbl_f31_sbc_level_ewm_63d_accel_v110_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm sbcomp
def sbl_f31_sbc_level_ewm_63d_accel_v111_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm sbcomp
def sbl_f31_sbc_level_ewm_126d_accel_v112_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm sbcomp
def sbl_f31_sbc_level_ewm_126d_accel_v113_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm sbcomp
def sbl_f31_sbc_level_ewm_126d_accel_v114_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm sbcomp
def sbl_f31_sbc_level_ewm_252d_accel_v115_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm sbcomp
def sbl_f31_sbc_level_ewm_252d_accel_v116_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm sbcomp
def sbl_f31_sbc_level_ewm_252d_accel_v117_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm sbcomp
def sbl_f31_sbc_level_ewm_504d_accel_v118_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm sbcomp
def sbl_f31_sbc_level_ewm_504d_accel_v119_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm sbcomp
def sbl_f31_sbc_level_ewm_504d_accel_v120_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq sbcomp
def sbl_f31_sbc_level_sq_21d_accel_v121_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq sbcomp
def sbl_f31_sbc_level_sq_21d_accel_v122_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq sbcomp
def sbl_f31_sbc_level_sq_21d_accel_v123_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq sbcomp
def sbl_f31_sbc_level_sq_63d_accel_v124_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq sbcomp
def sbl_f31_sbc_level_sq_63d_accel_v125_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq sbcomp
def sbl_f31_sbc_level_sq_63d_accel_v126_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq sbcomp
def sbl_f31_sbc_level_sq_126d_accel_v127_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq sbcomp
def sbl_f31_sbc_level_sq_126d_accel_v128_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq sbcomp
def sbl_f31_sbc_level_sq_126d_accel_v129_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq sbcomp
def sbl_f31_sbc_level_sq_252d_accel_v130_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq sbcomp
def sbl_f31_sbc_level_sq_252d_accel_v131_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq sbcomp
def sbl_f31_sbc_level_sq_252d_accel_v132_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq sbcomp
def sbl_f31_sbc_level_sq_504d_accel_v133_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq sbcomp
def sbl_f31_sbc_level_sq_504d_accel_v134_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq sbcomp
def sbl_f31_sbc_level_sq_504d_accel_v135_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z sbcomp
def sbl_f31_sbc_level_z_21d_accel_v136_signal(sbcomp):
    base = _z(sbcomp, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z sbcomp
def sbl_f31_sbc_level_z_21d_accel_v137_signal(sbcomp):
    base = _z(sbcomp, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z sbcomp
def sbl_f31_sbc_level_z_21d_accel_v138_signal(sbcomp):
    base = _z(sbcomp, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z sbcomp
def sbl_f31_sbc_level_z_63d_accel_v139_signal(sbcomp):
    base = _z(sbcomp, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z sbcomp
def sbl_f31_sbc_level_z_63d_accel_v140_signal(sbcomp):
    base = _z(sbcomp, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z sbcomp
def sbl_f31_sbc_level_z_63d_accel_v141_signal(sbcomp):
    base = _z(sbcomp, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z sbcomp
def sbl_f31_sbc_level_z_126d_accel_v142_signal(sbcomp):
    base = _z(sbcomp, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z sbcomp
def sbl_f31_sbc_level_z_126d_accel_v143_signal(sbcomp):
    base = _z(sbcomp, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z sbcomp
def sbl_f31_sbc_level_z_126d_accel_v144_signal(sbcomp):
    base = _z(sbcomp, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z sbcomp
def sbl_f31_sbc_level_z_252d_accel_v145_signal(sbcomp):
    base = _z(sbcomp, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z sbcomp
def sbl_f31_sbc_level_z_252d_accel_v146_signal(sbcomp):
    base = _z(sbcomp, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z sbcomp
def sbl_f31_sbc_level_z_252d_accel_v147_signal(sbcomp):
    base = _z(sbcomp, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z sbcomp
def sbl_f31_sbc_level_z_504d_accel_v148_signal(sbcomp):
    base = _z(sbcomp, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z sbcomp
def sbl_f31_sbc_level_z_504d_accel_v149_signal(sbcomp):
    base = _z(sbcomp, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z sbcomp
def sbl_f31_sbc_level_z_504d_accel_v150_signal(sbcomp):
    base = _z(sbcomp, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
