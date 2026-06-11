"""Family f36 - Asset composition  (F_BalanceSheet) | 3rd derivatives 001-150"""
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
def _asset_composition_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _asset_composition_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _asset_composition_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw intangibles
def ac_f36_asset_composition_raw_21d_accel_v001_signal(intangibles, closeadj):
    base = _mean(intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw intangibles
def ac_f36_asset_composition_raw_21d_accel_v002_signal(intangibles, closeadj):
    base = _mean(intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw intangibles
def ac_f36_asset_composition_raw_21d_accel_v003_signal(intangibles, closeadj):
    base = _mean(intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw intangibles
def ac_f36_asset_composition_raw_63d_accel_v004_signal(intangibles, closeadj):
    base = _mean(intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw intangibles
def ac_f36_asset_composition_raw_63d_accel_v005_signal(intangibles, closeadj):
    base = _mean(intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw intangibles
def ac_f36_asset_composition_raw_63d_accel_v006_signal(intangibles, closeadj):
    base = _mean(intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw intangibles
def ac_f36_asset_composition_raw_126d_accel_v007_signal(intangibles, closeadj):
    base = _mean(intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw intangibles
def ac_f36_asset_composition_raw_126d_accel_v008_signal(intangibles, closeadj):
    base = _mean(intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw intangibles
def ac_f36_asset_composition_raw_126d_accel_v009_signal(intangibles, closeadj):
    base = _mean(intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw intangibles
def ac_f36_asset_composition_raw_252d_accel_v010_signal(intangibles, closeadj):
    base = _mean(intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw intangibles
def ac_f36_asset_composition_raw_252d_accel_v011_signal(intangibles, closeadj):
    base = _mean(intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw intangibles
def ac_f36_asset_composition_raw_252d_accel_v012_signal(intangibles, closeadj):
    base = _mean(intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw intangibles
def ac_f36_asset_composition_raw_504d_accel_v013_signal(intangibles, closeadj):
    base = _mean(intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw intangibles
def ac_f36_asset_composition_raw_504d_accel_v014_signal(intangibles, closeadj):
    base = _mean(intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw intangibles
def ac_f36_asset_composition_raw_504d_accel_v015_signal(intangibles, closeadj):
    base = _mean(intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log intangibles
def ac_f36_asset_composition_log_21d_accel_v016_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log intangibles
def ac_f36_asset_composition_log_21d_accel_v017_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log intangibles
def ac_f36_asset_composition_log_21d_accel_v018_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log intangibles
def ac_f36_asset_composition_log_63d_accel_v019_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log intangibles
def ac_f36_asset_composition_log_63d_accel_v020_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log intangibles
def ac_f36_asset_composition_log_63d_accel_v021_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log intangibles
def ac_f36_asset_composition_log_126d_accel_v022_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log intangibles
def ac_f36_asset_composition_log_126d_accel_v023_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log intangibles
def ac_f36_asset_composition_log_126d_accel_v024_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log intangibles
def ac_f36_asset_composition_log_252d_accel_v025_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log intangibles
def ac_f36_asset_composition_log_252d_accel_v026_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log intangibles
def ac_f36_asset_composition_log_252d_accel_v027_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log intangibles
def ac_f36_asset_composition_log_504d_accel_v028_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log intangibles
def ac_f36_asset_composition_log_504d_accel_v029_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log intangibles
def ac_f36_asset_composition_log_504d_accel_v030_signal(intangibles, closeadj):
    base = _mean(_asset_composition_log(intangibles), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare intangibles
def ac_f36_asset_composition_pershare_21d_accel_v031_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare intangibles
def ac_f36_asset_composition_pershare_21d_accel_v032_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare intangibles
def ac_f36_asset_composition_pershare_21d_accel_v033_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare intangibles
def ac_f36_asset_composition_pershare_63d_accel_v034_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare intangibles
def ac_f36_asset_composition_pershare_63d_accel_v035_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare intangibles
def ac_f36_asset_composition_pershare_63d_accel_v036_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare intangibles
def ac_f36_asset_composition_pershare_126d_accel_v037_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare intangibles
def ac_f36_asset_composition_pershare_126d_accel_v038_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare intangibles
def ac_f36_asset_composition_pershare_126d_accel_v039_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare intangibles
def ac_f36_asset_composition_pershare_252d_accel_v040_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare intangibles
def ac_f36_asset_composition_pershare_252d_accel_v041_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare intangibles
def ac_f36_asset_composition_pershare_252d_accel_v042_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare intangibles
def ac_f36_asset_composition_pershare_504d_accel_v043_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare intangibles
def ac_f36_asset_composition_pershare_504d_accel_v044_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare intangibles
def ac_f36_asset_composition_pershare_504d_accel_v045_signal(intangibles, sharesbas, closeadj):
    base = _mean(_asset_composition_per_share(intangibles, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets intangibles
def ac_f36_asset_composition_per_assets_21d_accel_v046_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets intangibles
def ac_f36_asset_composition_per_assets_21d_accel_v047_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets intangibles
def ac_f36_asset_composition_per_assets_21d_accel_v048_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets intangibles
def ac_f36_asset_composition_per_assets_63d_accel_v049_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets intangibles
def ac_f36_asset_composition_per_assets_63d_accel_v050_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets intangibles
def ac_f36_asset_composition_per_assets_63d_accel_v051_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets intangibles
def ac_f36_asset_composition_per_assets_126d_accel_v052_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets intangibles
def ac_f36_asset_composition_per_assets_126d_accel_v053_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets intangibles
def ac_f36_asset_composition_per_assets_126d_accel_v054_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets intangibles
def ac_f36_asset_composition_per_assets_252d_accel_v055_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets intangibles
def ac_f36_asset_composition_per_assets_252d_accel_v056_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets intangibles
def ac_f36_asset_composition_per_assets_252d_accel_v057_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets intangibles
def ac_f36_asset_composition_per_assets_504d_accel_v058_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets intangibles
def ac_f36_asset_composition_per_assets_504d_accel_v059_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets intangibles
def ac_f36_asset_composition_per_assets_504d_accel_v060_signal(intangibles, assets):
    base = _mean(_asset_composition_scaled(intangibles, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_21d_accel_v061_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_21d_accel_v062_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_21d_accel_v063_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_63d_accel_v064_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_63d_accel_v065_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_63d_accel_v066_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_126d_accel_v067_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_126d_accel_v068_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_126d_accel_v069_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_252d_accel_v070_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_252d_accel_v071_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_252d_accel_v072_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_504d_accel_v073_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_504d_accel_v074_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap intangibles
def ac_f36_asset_composition_per_marketcap_504d_accel_v075_signal(intangibles, marketcap):
    base = _mean(_asset_composition_scaled(intangibles, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity intangibles
def ac_f36_asset_composition_per_equity_21d_accel_v076_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity intangibles
def ac_f36_asset_composition_per_equity_21d_accel_v077_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity intangibles
def ac_f36_asset_composition_per_equity_21d_accel_v078_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity intangibles
def ac_f36_asset_composition_per_equity_63d_accel_v079_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity intangibles
def ac_f36_asset_composition_per_equity_63d_accel_v080_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity intangibles
def ac_f36_asset_composition_per_equity_63d_accel_v081_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity intangibles
def ac_f36_asset_composition_per_equity_126d_accel_v082_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity intangibles
def ac_f36_asset_composition_per_equity_126d_accel_v083_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity intangibles
def ac_f36_asset_composition_per_equity_126d_accel_v084_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity intangibles
def ac_f36_asset_composition_per_equity_252d_accel_v085_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity intangibles
def ac_f36_asset_composition_per_equity_252d_accel_v086_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity intangibles
def ac_f36_asset_composition_per_equity_252d_accel_v087_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity intangibles
def ac_f36_asset_composition_per_equity_504d_accel_v088_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity intangibles
def ac_f36_asset_composition_per_equity_504d_accel_v089_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity intangibles
def ac_f36_asset_composition_per_equity_504d_accel_v090_signal(intangibles, equity):
    base = _mean(_asset_composition_scaled(intangibles, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std intangibles
def ac_f36_asset_composition_std_21d_accel_v091_signal(intangibles, closeadj):
    base = _std(intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std intangibles
def ac_f36_asset_composition_std_21d_accel_v092_signal(intangibles, closeadj):
    base = _std(intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std intangibles
def ac_f36_asset_composition_std_21d_accel_v093_signal(intangibles, closeadj):
    base = _std(intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std intangibles
def ac_f36_asset_composition_std_63d_accel_v094_signal(intangibles, closeadj):
    base = _std(intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std intangibles
def ac_f36_asset_composition_std_63d_accel_v095_signal(intangibles, closeadj):
    base = _std(intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std intangibles
def ac_f36_asset_composition_std_63d_accel_v096_signal(intangibles, closeadj):
    base = _std(intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std intangibles
def ac_f36_asset_composition_std_126d_accel_v097_signal(intangibles, closeadj):
    base = _std(intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std intangibles
def ac_f36_asset_composition_std_126d_accel_v098_signal(intangibles, closeadj):
    base = _std(intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std intangibles
def ac_f36_asset_composition_std_126d_accel_v099_signal(intangibles, closeadj):
    base = _std(intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std intangibles
def ac_f36_asset_composition_std_252d_accel_v100_signal(intangibles, closeadj):
    base = _std(intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std intangibles
def ac_f36_asset_composition_std_252d_accel_v101_signal(intangibles, closeadj):
    base = _std(intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std intangibles
def ac_f36_asset_composition_std_252d_accel_v102_signal(intangibles, closeadj):
    base = _std(intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std intangibles
def ac_f36_asset_composition_std_504d_accel_v103_signal(intangibles, closeadj):
    base = _std(intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std intangibles
def ac_f36_asset_composition_std_504d_accel_v104_signal(intangibles, closeadj):
    base = _std(intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std intangibles
def ac_f36_asset_composition_std_504d_accel_v105_signal(intangibles, closeadj):
    base = _std(intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm intangibles
def ac_f36_asset_composition_ewm_21d_accel_v106_signal(intangibles, closeadj):
    base = intangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm intangibles
def ac_f36_asset_composition_ewm_21d_accel_v107_signal(intangibles, closeadj):
    base = intangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm intangibles
def ac_f36_asset_composition_ewm_21d_accel_v108_signal(intangibles, closeadj):
    base = intangibles.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm intangibles
def ac_f36_asset_composition_ewm_63d_accel_v109_signal(intangibles, closeadj):
    base = intangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm intangibles
def ac_f36_asset_composition_ewm_63d_accel_v110_signal(intangibles, closeadj):
    base = intangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm intangibles
def ac_f36_asset_composition_ewm_63d_accel_v111_signal(intangibles, closeadj):
    base = intangibles.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm intangibles
def ac_f36_asset_composition_ewm_126d_accel_v112_signal(intangibles, closeadj):
    base = intangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm intangibles
def ac_f36_asset_composition_ewm_126d_accel_v113_signal(intangibles, closeadj):
    base = intangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm intangibles
def ac_f36_asset_composition_ewm_126d_accel_v114_signal(intangibles, closeadj):
    base = intangibles.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm intangibles
def ac_f36_asset_composition_ewm_252d_accel_v115_signal(intangibles, closeadj):
    base = intangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm intangibles
def ac_f36_asset_composition_ewm_252d_accel_v116_signal(intangibles, closeadj):
    base = intangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm intangibles
def ac_f36_asset_composition_ewm_252d_accel_v117_signal(intangibles, closeadj):
    base = intangibles.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm intangibles
def ac_f36_asset_composition_ewm_504d_accel_v118_signal(intangibles, closeadj):
    base = intangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm intangibles
def ac_f36_asset_composition_ewm_504d_accel_v119_signal(intangibles, closeadj):
    base = intangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm intangibles
def ac_f36_asset_composition_ewm_504d_accel_v120_signal(intangibles, closeadj):
    base = intangibles.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq intangibles
def ac_f36_asset_composition_sq_21d_accel_v121_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq intangibles
def ac_f36_asset_composition_sq_21d_accel_v122_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq intangibles
def ac_f36_asset_composition_sq_21d_accel_v123_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq intangibles
def ac_f36_asset_composition_sq_63d_accel_v124_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq intangibles
def ac_f36_asset_composition_sq_63d_accel_v125_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq intangibles
def ac_f36_asset_composition_sq_63d_accel_v126_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq intangibles
def ac_f36_asset_composition_sq_126d_accel_v127_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq intangibles
def ac_f36_asset_composition_sq_126d_accel_v128_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq intangibles
def ac_f36_asset_composition_sq_126d_accel_v129_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq intangibles
def ac_f36_asset_composition_sq_252d_accel_v130_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq intangibles
def ac_f36_asset_composition_sq_252d_accel_v131_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq intangibles
def ac_f36_asset_composition_sq_252d_accel_v132_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq intangibles
def ac_f36_asset_composition_sq_504d_accel_v133_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq intangibles
def ac_f36_asset_composition_sq_504d_accel_v134_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq intangibles
def ac_f36_asset_composition_sq_504d_accel_v135_signal(intangibles, closeadj):
    base = _mean(intangibles * intangibles, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z intangibles
def ac_f36_asset_composition_z_21d_accel_v136_signal(intangibles):
    base = _z(intangibles, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z intangibles
def ac_f36_asset_composition_z_21d_accel_v137_signal(intangibles):
    base = _z(intangibles, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z intangibles
def ac_f36_asset_composition_z_21d_accel_v138_signal(intangibles):
    base = _z(intangibles, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z intangibles
def ac_f36_asset_composition_z_63d_accel_v139_signal(intangibles):
    base = _z(intangibles, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z intangibles
def ac_f36_asset_composition_z_63d_accel_v140_signal(intangibles):
    base = _z(intangibles, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z intangibles
def ac_f36_asset_composition_z_63d_accel_v141_signal(intangibles):
    base = _z(intangibles, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z intangibles
def ac_f36_asset_composition_z_126d_accel_v142_signal(intangibles):
    base = _z(intangibles, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z intangibles
def ac_f36_asset_composition_z_126d_accel_v143_signal(intangibles):
    base = _z(intangibles, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z intangibles
def ac_f36_asset_composition_z_126d_accel_v144_signal(intangibles):
    base = _z(intangibles, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z intangibles
def ac_f36_asset_composition_z_252d_accel_v145_signal(intangibles):
    base = _z(intangibles, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z intangibles
def ac_f36_asset_composition_z_252d_accel_v146_signal(intangibles):
    base = _z(intangibles, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z intangibles
def ac_f36_asset_composition_z_252d_accel_v147_signal(intangibles):
    base = _z(intangibles, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z intangibles
def ac_f36_asset_composition_z_504d_accel_v148_signal(intangibles):
    base = _z(intangibles, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z intangibles
def ac_f36_asset_composition_z_504d_accel_v149_signal(intangibles):
    base = _z(intangibles, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z intangibles
def ac_f36_asset_composition_z_504d_accel_v150_signal(intangibles):
    base = _z(intangibles, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
