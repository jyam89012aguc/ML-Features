"""Family f08 - Operating cash flow level  (B_CashFlow_Burn) | 3rd derivatives 001-150"""
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
def _ocf_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ocf_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ocf_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw ncfo
def ocf_f08_ocf_level_raw_21d_accel_v001_signal(ncfo, closeadj):
    base = _mean(ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw ncfo
def ocf_f08_ocf_level_raw_21d_accel_v002_signal(ncfo, closeadj):
    base = _mean(ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw ncfo
def ocf_f08_ocf_level_raw_21d_accel_v003_signal(ncfo, closeadj):
    base = _mean(ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw ncfo
def ocf_f08_ocf_level_raw_63d_accel_v004_signal(ncfo, closeadj):
    base = _mean(ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw ncfo
def ocf_f08_ocf_level_raw_63d_accel_v005_signal(ncfo, closeadj):
    base = _mean(ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw ncfo
def ocf_f08_ocf_level_raw_63d_accel_v006_signal(ncfo, closeadj):
    base = _mean(ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw ncfo
def ocf_f08_ocf_level_raw_126d_accel_v007_signal(ncfo, closeadj):
    base = _mean(ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw ncfo
def ocf_f08_ocf_level_raw_126d_accel_v008_signal(ncfo, closeadj):
    base = _mean(ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw ncfo
def ocf_f08_ocf_level_raw_126d_accel_v009_signal(ncfo, closeadj):
    base = _mean(ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw ncfo
def ocf_f08_ocf_level_raw_252d_accel_v010_signal(ncfo, closeadj):
    base = _mean(ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw ncfo
def ocf_f08_ocf_level_raw_252d_accel_v011_signal(ncfo, closeadj):
    base = _mean(ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw ncfo
def ocf_f08_ocf_level_raw_252d_accel_v012_signal(ncfo, closeadj):
    base = _mean(ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw ncfo
def ocf_f08_ocf_level_raw_504d_accel_v013_signal(ncfo, closeadj):
    base = _mean(ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw ncfo
def ocf_f08_ocf_level_raw_504d_accel_v014_signal(ncfo, closeadj):
    base = _mean(ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw ncfo
def ocf_f08_ocf_level_raw_504d_accel_v015_signal(ncfo, closeadj):
    base = _mean(ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log ncfo
def ocf_f08_ocf_level_log_21d_accel_v016_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log ncfo
def ocf_f08_ocf_level_log_21d_accel_v017_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log ncfo
def ocf_f08_ocf_level_log_21d_accel_v018_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log ncfo
def ocf_f08_ocf_level_log_63d_accel_v019_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log ncfo
def ocf_f08_ocf_level_log_63d_accel_v020_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log ncfo
def ocf_f08_ocf_level_log_63d_accel_v021_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log ncfo
def ocf_f08_ocf_level_log_126d_accel_v022_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log ncfo
def ocf_f08_ocf_level_log_126d_accel_v023_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log ncfo
def ocf_f08_ocf_level_log_126d_accel_v024_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log ncfo
def ocf_f08_ocf_level_log_252d_accel_v025_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log ncfo
def ocf_f08_ocf_level_log_252d_accel_v026_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log ncfo
def ocf_f08_ocf_level_log_252d_accel_v027_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log ncfo
def ocf_f08_ocf_level_log_504d_accel_v028_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log ncfo
def ocf_f08_ocf_level_log_504d_accel_v029_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log ncfo
def ocf_f08_ocf_level_log_504d_accel_v030_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare ncfo
def ocf_f08_ocf_level_pershare_21d_accel_v031_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare ncfo
def ocf_f08_ocf_level_pershare_21d_accel_v032_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare ncfo
def ocf_f08_ocf_level_pershare_21d_accel_v033_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare ncfo
def ocf_f08_ocf_level_pershare_63d_accel_v034_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare ncfo
def ocf_f08_ocf_level_pershare_63d_accel_v035_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare ncfo
def ocf_f08_ocf_level_pershare_63d_accel_v036_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare ncfo
def ocf_f08_ocf_level_pershare_126d_accel_v037_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare ncfo
def ocf_f08_ocf_level_pershare_126d_accel_v038_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare ncfo
def ocf_f08_ocf_level_pershare_126d_accel_v039_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare ncfo
def ocf_f08_ocf_level_pershare_252d_accel_v040_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare ncfo
def ocf_f08_ocf_level_pershare_252d_accel_v041_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare ncfo
def ocf_f08_ocf_level_pershare_252d_accel_v042_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare ncfo
def ocf_f08_ocf_level_pershare_504d_accel_v043_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare ncfo
def ocf_f08_ocf_level_pershare_504d_accel_v044_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare ncfo
def ocf_f08_ocf_level_pershare_504d_accel_v045_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets ncfo
def ocf_f08_ocf_level_per_assets_21d_accel_v046_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets ncfo
def ocf_f08_ocf_level_per_assets_21d_accel_v047_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets ncfo
def ocf_f08_ocf_level_per_assets_21d_accel_v048_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets ncfo
def ocf_f08_ocf_level_per_assets_63d_accel_v049_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets ncfo
def ocf_f08_ocf_level_per_assets_63d_accel_v050_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets ncfo
def ocf_f08_ocf_level_per_assets_63d_accel_v051_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets ncfo
def ocf_f08_ocf_level_per_assets_126d_accel_v052_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets ncfo
def ocf_f08_ocf_level_per_assets_126d_accel_v053_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets ncfo
def ocf_f08_ocf_level_per_assets_126d_accel_v054_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets ncfo
def ocf_f08_ocf_level_per_assets_252d_accel_v055_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets ncfo
def ocf_f08_ocf_level_per_assets_252d_accel_v056_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets ncfo
def ocf_f08_ocf_level_per_assets_252d_accel_v057_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets ncfo
def ocf_f08_ocf_level_per_assets_504d_accel_v058_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets ncfo
def ocf_f08_ocf_level_per_assets_504d_accel_v059_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets ncfo
def ocf_f08_ocf_level_per_assets_504d_accel_v060_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_21d_accel_v061_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_21d_accel_v062_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_21d_accel_v063_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_63d_accel_v064_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_63d_accel_v065_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_63d_accel_v066_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_126d_accel_v067_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_126d_accel_v068_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_126d_accel_v069_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_252d_accel_v070_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_252d_accel_v071_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_252d_accel_v072_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_504d_accel_v073_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_504d_accel_v074_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_504d_accel_v075_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity ncfo
def ocf_f08_ocf_level_per_equity_21d_accel_v076_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity ncfo
def ocf_f08_ocf_level_per_equity_21d_accel_v077_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity ncfo
def ocf_f08_ocf_level_per_equity_21d_accel_v078_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity ncfo
def ocf_f08_ocf_level_per_equity_63d_accel_v079_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity ncfo
def ocf_f08_ocf_level_per_equity_63d_accel_v080_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity ncfo
def ocf_f08_ocf_level_per_equity_63d_accel_v081_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity ncfo
def ocf_f08_ocf_level_per_equity_126d_accel_v082_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity ncfo
def ocf_f08_ocf_level_per_equity_126d_accel_v083_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity ncfo
def ocf_f08_ocf_level_per_equity_126d_accel_v084_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity ncfo
def ocf_f08_ocf_level_per_equity_252d_accel_v085_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity ncfo
def ocf_f08_ocf_level_per_equity_252d_accel_v086_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity ncfo
def ocf_f08_ocf_level_per_equity_252d_accel_v087_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity ncfo
def ocf_f08_ocf_level_per_equity_504d_accel_v088_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity ncfo
def ocf_f08_ocf_level_per_equity_504d_accel_v089_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity ncfo
def ocf_f08_ocf_level_per_equity_504d_accel_v090_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std ncfo
def ocf_f08_ocf_level_std_21d_accel_v091_signal(ncfo, closeadj):
    base = _std(ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std ncfo
def ocf_f08_ocf_level_std_21d_accel_v092_signal(ncfo, closeadj):
    base = _std(ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std ncfo
def ocf_f08_ocf_level_std_21d_accel_v093_signal(ncfo, closeadj):
    base = _std(ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std ncfo
def ocf_f08_ocf_level_std_63d_accel_v094_signal(ncfo, closeadj):
    base = _std(ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std ncfo
def ocf_f08_ocf_level_std_63d_accel_v095_signal(ncfo, closeadj):
    base = _std(ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std ncfo
def ocf_f08_ocf_level_std_63d_accel_v096_signal(ncfo, closeadj):
    base = _std(ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std ncfo
def ocf_f08_ocf_level_std_126d_accel_v097_signal(ncfo, closeadj):
    base = _std(ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std ncfo
def ocf_f08_ocf_level_std_126d_accel_v098_signal(ncfo, closeadj):
    base = _std(ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std ncfo
def ocf_f08_ocf_level_std_126d_accel_v099_signal(ncfo, closeadj):
    base = _std(ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std ncfo
def ocf_f08_ocf_level_std_252d_accel_v100_signal(ncfo, closeadj):
    base = _std(ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std ncfo
def ocf_f08_ocf_level_std_252d_accel_v101_signal(ncfo, closeadj):
    base = _std(ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std ncfo
def ocf_f08_ocf_level_std_252d_accel_v102_signal(ncfo, closeadj):
    base = _std(ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std ncfo
def ocf_f08_ocf_level_std_504d_accel_v103_signal(ncfo, closeadj):
    base = _std(ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std ncfo
def ocf_f08_ocf_level_std_504d_accel_v104_signal(ncfo, closeadj):
    base = _std(ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std ncfo
def ocf_f08_ocf_level_std_504d_accel_v105_signal(ncfo, closeadj):
    base = _std(ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm ncfo
def ocf_f08_ocf_level_ewm_21d_accel_v106_signal(ncfo, closeadj):
    base = ncfo.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm ncfo
def ocf_f08_ocf_level_ewm_21d_accel_v107_signal(ncfo, closeadj):
    base = ncfo.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm ncfo
def ocf_f08_ocf_level_ewm_21d_accel_v108_signal(ncfo, closeadj):
    base = ncfo.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm ncfo
def ocf_f08_ocf_level_ewm_63d_accel_v109_signal(ncfo, closeadj):
    base = ncfo.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm ncfo
def ocf_f08_ocf_level_ewm_63d_accel_v110_signal(ncfo, closeadj):
    base = ncfo.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm ncfo
def ocf_f08_ocf_level_ewm_63d_accel_v111_signal(ncfo, closeadj):
    base = ncfo.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm ncfo
def ocf_f08_ocf_level_ewm_126d_accel_v112_signal(ncfo, closeadj):
    base = ncfo.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm ncfo
def ocf_f08_ocf_level_ewm_126d_accel_v113_signal(ncfo, closeadj):
    base = ncfo.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm ncfo
def ocf_f08_ocf_level_ewm_126d_accel_v114_signal(ncfo, closeadj):
    base = ncfo.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm ncfo
def ocf_f08_ocf_level_ewm_252d_accel_v115_signal(ncfo, closeadj):
    base = ncfo.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm ncfo
def ocf_f08_ocf_level_ewm_252d_accel_v116_signal(ncfo, closeadj):
    base = ncfo.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm ncfo
def ocf_f08_ocf_level_ewm_252d_accel_v117_signal(ncfo, closeadj):
    base = ncfo.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm ncfo
def ocf_f08_ocf_level_ewm_504d_accel_v118_signal(ncfo, closeadj):
    base = ncfo.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm ncfo
def ocf_f08_ocf_level_ewm_504d_accel_v119_signal(ncfo, closeadj):
    base = ncfo.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm ncfo
def ocf_f08_ocf_level_ewm_504d_accel_v120_signal(ncfo, closeadj):
    base = ncfo.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq ncfo
def ocf_f08_ocf_level_sq_21d_accel_v121_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq ncfo
def ocf_f08_ocf_level_sq_21d_accel_v122_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq ncfo
def ocf_f08_ocf_level_sq_21d_accel_v123_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq ncfo
def ocf_f08_ocf_level_sq_63d_accel_v124_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq ncfo
def ocf_f08_ocf_level_sq_63d_accel_v125_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq ncfo
def ocf_f08_ocf_level_sq_63d_accel_v126_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq ncfo
def ocf_f08_ocf_level_sq_126d_accel_v127_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq ncfo
def ocf_f08_ocf_level_sq_126d_accel_v128_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq ncfo
def ocf_f08_ocf_level_sq_126d_accel_v129_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq ncfo
def ocf_f08_ocf_level_sq_252d_accel_v130_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq ncfo
def ocf_f08_ocf_level_sq_252d_accel_v131_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq ncfo
def ocf_f08_ocf_level_sq_252d_accel_v132_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq ncfo
def ocf_f08_ocf_level_sq_504d_accel_v133_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq ncfo
def ocf_f08_ocf_level_sq_504d_accel_v134_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq ncfo
def ocf_f08_ocf_level_sq_504d_accel_v135_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z ncfo
def ocf_f08_ocf_level_z_21d_accel_v136_signal(ncfo):
    base = _z(ncfo, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z ncfo
def ocf_f08_ocf_level_z_21d_accel_v137_signal(ncfo):
    base = _z(ncfo, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z ncfo
def ocf_f08_ocf_level_z_21d_accel_v138_signal(ncfo):
    base = _z(ncfo, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z ncfo
def ocf_f08_ocf_level_z_63d_accel_v139_signal(ncfo):
    base = _z(ncfo, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z ncfo
def ocf_f08_ocf_level_z_63d_accel_v140_signal(ncfo):
    base = _z(ncfo, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z ncfo
def ocf_f08_ocf_level_z_63d_accel_v141_signal(ncfo):
    base = _z(ncfo, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z ncfo
def ocf_f08_ocf_level_z_126d_accel_v142_signal(ncfo):
    base = _z(ncfo, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z ncfo
def ocf_f08_ocf_level_z_126d_accel_v143_signal(ncfo):
    base = _z(ncfo, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z ncfo
def ocf_f08_ocf_level_z_126d_accel_v144_signal(ncfo):
    base = _z(ncfo, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z ncfo
def ocf_f08_ocf_level_z_252d_accel_v145_signal(ncfo):
    base = _z(ncfo, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z ncfo
def ocf_f08_ocf_level_z_252d_accel_v146_signal(ncfo):
    base = _z(ncfo, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z ncfo
def ocf_f08_ocf_level_z_252d_accel_v147_signal(ncfo):
    base = _z(ncfo, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z ncfo
def ocf_f08_ocf_level_z_504d_accel_v148_signal(ncfo):
    base = _z(ncfo, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z ncfo
def ocf_f08_ocf_level_z_504d_accel_v149_signal(ncfo):
    base = _z(ncfo, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z ncfo
def ocf_f08_ocf_level_z_504d_accel_v150_signal(ncfo):
    base = _z(ncfo, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
