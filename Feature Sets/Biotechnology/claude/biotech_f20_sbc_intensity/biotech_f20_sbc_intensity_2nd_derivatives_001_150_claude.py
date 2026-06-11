"""Family f20 - Stock-based comp intensity  (C_RnD_Innovation) | 2nd derivatives 001-150"""
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
def _sbc_intensity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sbc_intensity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sbc_intensity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw sbcomp
def sbi_f20_sbc_intensity_raw_21d_slope_v001_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw sbcomp
def sbi_f20_sbc_intensity_raw_21d_slope_v002_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw sbcomp
def sbi_f20_sbc_intensity_raw_21d_slope_v003_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw sbcomp
def sbi_f20_sbc_intensity_raw_63d_slope_v004_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw sbcomp
def sbi_f20_sbc_intensity_raw_63d_slope_v005_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw sbcomp
def sbi_f20_sbc_intensity_raw_63d_slope_v006_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw sbcomp
def sbi_f20_sbc_intensity_raw_126d_slope_v007_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw sbcomp
def sbi_f20_sbc_intensity_raw_126d_slope_v008_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw sbcomp
def sbi_f20_sbc_intensity_raw_126d_slope_v009_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw sbcomp
def sbi_f20_sbc_intensity_raw_252d_slope_v010_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw sbcomp
def sbi_f20_sbc_intensity_raw_252d_slope_v011_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw sbcomp
def sbi_f20_sbc_intensity_raw_252d_slope_v012_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw sbcomp
def sbi_f20_sbc_intensity_raw_504d_slope_v013_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw sbcomp
def sbi_f20_sbc_intensity_raw_504d_slope_v014_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw sbcomp
def sbi_f20_sbc_intensity_raw_504d_slope_v015_signal(sbcomp, closeadj):
    base = _mean(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log sbcomp
def sbi_f20_sbc_intensity_log_21d_slope_v016_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log sbcomp
def sbi_f20_sbc_intensity_log_21d_slope_v017_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log sbcomp
def sbi_f20_sbc_intensity_log_21d_slope_v018_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log sbcomp
def sbi_f20_sbc_intensity_log_63d_slope_v019_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log sbcomp
def sbi_f20_sbc_intensity_log_63d_slope_v020_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log sbcomp
def sbi_f20_sbc_intensity_log_63d_slope_v021_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log sbcomp
def sbi_f20_sbc_intensity_log_126d_slope_v022_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log sbcomp
def sbi_f20_sbc_intensity_log_126d_slope_v023_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log sbcomp
def sbi_f20_sbc_intensity_log_126d_slope_v024_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log sbcomp
def sbi_f20_sbc_intensity_log_252d_slope_v025_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log sbcomp
def sbi_f20_sbc_intensity_log_252d_slope_v026_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log sbcomp
def sbi_f20_sbc_intensity_log_252d_slope_v027_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log sbcomp
def sbi_f20_sbc_intensity_log_504d_slope_v028_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log sbcomp
def sbi_f20_sbc_intensity_log_504d_slope_v029_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log sbcomp
def sbi_f20_sbc_intensity_log_504d_slope_v030_signal(sbcomp, closeadj):
    base = _mean(_sbc_intensity_log(sbcomp), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_21d_slope_v031_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_21d_slope_v032_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_21d_slope_v033_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_63d_slope_v034_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_63d_slope_v035_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_63d_slope_v036_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_126d_slope_v037_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_126d_slope_v038_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_126d_slope_v039_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_252d_slope_v040_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_252d_slope_v041_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_252d_slope_v042_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_504d_slope_v043_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_504d_slope_v044_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare sbcomp
def sbi_f20_sbc_intensity_pershare_504d_slope_v045_signal(sbcomp, sharesbas, closeadj):
    base = _mean(_sbc_intensity_per_share(sbcomp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_21d_slope_v046_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_21d_slope_v047_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_21d_slope_v048_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_63d_slope_v049_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_63d_slope_v050_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_63d_slope_v051_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_126d_slope_v052_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_126d_slope_v053_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_126d_slope_v054_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_252d_slope_v055_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_252d_slope_v056_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_252d_slope_v057_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_504d_slope_v058_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_504d_slope_v059_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets sbcomp
def sbi_f20_sbc_intensity_per_assets_504d_slope_v060_signal(sbcomp, assets):
    base = _mean(_sbc_intensity_scaled(sbcomp, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_21d_slope_v061_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_21d_slope_v062_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_21d_slope_v063_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_63d_slope_v064_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_63d_slope_v065_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_63d_slope_v066_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_126d_slope_v067_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_126d_slope_v068_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_126d_slope_v069_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_252d_slope_v070_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_252d_slope_v071_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_252d_slope_v072_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_504d_slope_v073_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_504d_slope_v074_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap sbcomp
def sbi_f20_sbc_intensity_per_marketcap_504d_slope_v075_signal(sbcomp, marketcap):
    base = _mean(_sbc_intensity_scaled(sbcomp, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_21d_slope_v076_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_21d_slope_v077_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_21d_slope_v078_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_63d_slope_v079_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_63d_slope_v080_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_63d_slope_v081_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_126d_slope_v082_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_126d_slope_v083_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_126d_slope_v084_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_252d_slope_v085_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_252d_slope_v086_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_252d_slope_v087_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_504d_slope_v088_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_504d_slope_v089_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity sbcomp
def sbi_f20_sbc_intensity_per_equity_504d_slope_v090_signal(sbcomp, equity):
    base = _mean(_sbc_intensity_scaled(sbcomp, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std sbcomp
def sbi_f20_sbc_intensity_std_21d_slope_v091_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std sbcomp
def sbi_f20_sbc_intensity_std_21d_slope_v092_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std sbcomp
def sbi_f20_sbc_intensity_std_21d_slope_v093_signal(sbcomp, closeadj):
    base = _std(sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std sbcomp
def sbi_f20_sbc_intensity_std_63d_slope_v094_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std sbcomp
def sbi_f20_sbc_intensity_std_63d_slope_v095_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std sbcomp
def sbi_f20_sbc_intensity_std_63d_slope_v096_signal(sbcomp, closeadj):
    base = _std(sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std sbcomp
def sbi_f20_sbc_intensity_std_126d_slope_v097_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std sbcomp
def sbi_f20_sbc_intensity_std_126d_slope_v098_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std sbcomp
def sbi_f20_sbc_intensity_std_126d_slope_v099_signal(sbcomp, closeadj):
    base = _std(sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std sbcomp
def sbi_f20_sbc_intensity_std_252d_slope_v100_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std sbcomp
def sbi_f20_sbc_intensity_std_252d_slope_v101_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std sbcomp
def sbi_f20_sbc_intensity_std_252d_slope_v102_signal(sbcomp, closeadj):
    base = _std(sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std sbcomp
def sbi_f20_sbc_intensity_std_504d_slope_v103_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std sbcomp
def sbi_f20_sbc_intensity_std_504d_slope_v104_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std sbcomp
def sbi_f20_sbc_intensity_std_504d_slope_v105_signal(sbcomp, closeadj):
    base = _std(sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_21d_slope_v106_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_21d_slope_v107_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_21d_slope_v108_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_63d_slope_v109_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_63d_slope_v110_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_63d_slope_v111_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_126d_slope_v112_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_126d_slope_v113_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_126d_slope_v114_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_252d_slope_v115_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_252d_slope_v116_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_252d_slope_v117_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_504d_slope_v118_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_504d_slope_v119_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm sbcomp
def sbi_f20_sbc_intensity_ewm_504d_slope_v120_signal(sbcomp, closeadj):
    base = sbcomp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq sbcomp
def sbi_f20_sbc_intensity_sq_21d_slope_v121_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq sbcomp
def sbi_f20_sbc_intensity_sq_21d_slope_v122_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq sbcomp
def sbi_f20_sbc_intensity_sq_21d_slope_v123_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq sbcomp
def sbi_f20_sbc_intensity_sq_63d_slope_v124_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq sbcomp
def sbi_f20_sbc_intensity_sq_63d_slope_v125_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq sbcomp
def sbi_f20_sbc_intensity_sq_63d_slope_v126_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq sbcomp
def sbi_f20_sbc_intensity_sq_126d_slope_v127_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq sbcomp
def sbi_f20_sbc_intensity_sq_126d_slope_v128_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq sbcomp
def sbi_f20_sbc_intensity_sq_126d_slope_v129_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq sbcomp
def sbi_f20_sbc_intensity_sq_252d_slope_v130_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq sbcomp
def sbi_f20_sbc_intensity_sq_252d_slope_v131_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq sbcomp
def sbi_f20_sbc_intensity_sq_252d_slope_v132_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq sbcomp
def sbi_f20_sbc_intensity_sq_504d_slope_v133_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq sbcomp
def sbi_f20_sbc_intensity_sq_504d_slope_v134_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq sbcomp
def sbi_f20_sbc_intensity_sq_504d_slope_v135_signal(sbcomp, closeadj):
    base = _mean(sbcomp * sbcomp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z sbcomp
def sbi_f20_sbc_intensity_z_21d_slope_v136_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z sbcomp
def sbi_f20_sbc_intensity_z_21d_slope_v137_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z sbcomp
def sbi_f20_sbc_intensity_z_21d_slope_v138_signal(sbcomp):
    base = _z(sbcomp, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z sbcomp
def sbi_f20_sbc_intensity_z_63d_slope_v139_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z sbcomp
def sbi_f20_sbc_intensity_z_63d_slope_v140_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z sbcomp
def sbi_f20_sbc_intensity_z_63d_slope_v141_signal(sbcomp):
    base = _z(sbcomp, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z sbcomp
def sbi_f20_sbc_intensity_z_126d_slope_v142_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z sbcomp
def sbi_f20_sbc_intensity_z_126d_slope_v143_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z sbcomp
def sbi_f20_sbc_intensity_z_126d_slope_v144_signal(sbcomp):
    base = _z(sbcomp, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z sbcomp
def sbi_f20_sbc_intensity_z_252d_slope_v145_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z sbcomp
def sbi_f20_sbc_intensity_z_252d_slope_v146_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z sbcomp
def sbi_f20_sbc_intensity_z_252d_slope_v147_signal(sbcomp):
    base = _z(sbcomp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z sbcomp
def sbi_f20_sbc_intensity_z_504d_slope_v148_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z sbcomp
def sbi_f20_sbc_intensity_z_504d_slope_v149_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z sbcomp
def sbi_f20_sbc_intensity_z_504d_slope_v150_signal(sbcomp):
    base = _z(sbcomp, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
