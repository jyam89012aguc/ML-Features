"""Family f64 - Inventory turnover / days  (K_WorkingCapital) | 3rd derivatives 001-150"""
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
def _inventory_turnover_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _inventory_turnover_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _inventory_turnover_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw inventory
def it_f64_inventory_turnover_raw_21d_accel_v001_signal(inventory, closeadj):
    base = _mean(inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw inventory
def it_f64_inventory_turnover_raw_21d_accel_v002_signal(inventory, closeadj):
    base = _mean(inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw inventory
def it_f64_inventory_turnover_raw_21d_accel_v003_signal(inventory, closeadj):
    base = _mean(inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw inventory
def it_f64_inventory_turnover_raw_63d_accel_v004_signal(inventory, closeadj):
    base = _mean(inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw inventory
def it_f64_inventory_turnover_raw_63d_accel_v005_signal(inventory, closeadj):
    base = _mean(inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw inventory
def it_f64_inventory_turnover_raw_63d_accel_v006_signal(inventory, closeadj):
    base = _mean(inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw inventory
def it_f64_inventory_turnover_raw_126d_accel_v007_signal(inventory, closeadj):
    base = _mean(inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw inventory
def it_f64_inventory_turnover_raw_126d_accel_v008_signal(inventory, closeadj):
    base = _mean(inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw inventory
def it_f64_inventory_turnover_raw_126d_accel_v009_signal(inventory, closeadj):
    base = _mean(inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw inventory
def it_f64_inventory_turnover_raw_252d_accel_v010_signal(inventory, closeadj):
    base = _mean(inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw inventory
def it_f64_inventory_turnover_raw_252d_accel_v011_signal(inventory, closeadj):
    base = _mean(inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw inventory
def it_f64_inventory_turnover_raw_252d_accel_v012_signal(inventory, closeadj):
    base = _mean(inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw inventory
def it_f64_inventory_turnover_raw_504d_accel_v013_signal(inventory, closeadj):
    base = _mean(inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw inventory
def it_f64_inventory_turnover_raw_504d_accel_v014_signal(inventory, closeadj):
    base = _mean(inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw inventory
def it_f64_inventory_turnover_raw_504d_accel_v015_signal(inventory, closeadj):
    base = _mean(inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log inventory
def it_f64_inventory_turnover_log_21d_accel_v016_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log inventory
def it_f64_inventory_turnover_log_21d_accel_v017_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log inventory
def it_f64_inventory_turnover_log_21d_accel_v018_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log inventory
def it_f64_inventory_turnover_log_63d_accel_v019_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log inventory
def it_f64_inventory_turnover_log_63d_accel_v020_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log inventory
def it_f64_inventory_turnover_log_63d_accel_v021_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log inventory
def it_f64_inventory_turnover_log_126d_accel_v022_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log inventory
def it_f64_inventory_turnover_log_126d_accel_v023_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log inventory
def it_f64_inventory_turnover_log_126d_accel_v024_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log inventory
def it_f64_inventory_turnover_log_252d_accel_v025_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log inventory
def it_f64_inventory_turnover_log_252d_accel_v026_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log inventory
def it_f64_inventory_turnover_log_252d_accel_v027_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log inventory
def it_f64_inventory_turnover_log_504d_accel_v028_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log inventory
def it_f64_inventory_turnover_log_504d_accel_v029_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log inventory
def it_f64_inventory_turnover_log_504d_accel_v030_signal(inventory, closeadj):
    base = _mean(_inventory_turnover_log(inventory), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare inventory
def it_f64_inventory_turnover_pershare_21d_accel_v031_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare inventory
def it_f64_inventory_turnover_pershare_21d_accel_v032_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare inventory
def it_f64_inventory_turnover_pershare_21d_accel_v033_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare inventory
def it_f64_inventory_turnover_pershare_63d_accel_v034_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare inventory
def it_f64_inventory_turnover_pershare_63d_accel_v035_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare inventory
def it_f64_inventory_turnover_pershare_63d_accel_v036_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare inventory
def it_f64_inventory_turnover_pershare_126d_accel_v037_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare inventory
def it_f64_inventory_turnover_pershare_126d_accel_v038_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare inventory
def it_f64_inventory_turnover_pershare_126d_accel_v039_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare inventory
def it_f64_inventory_turnover_pershare_252d_accel_v040_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare inventory
def it_f64_inventory_turnover_pershare_252d_accel_v041_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare inventory
def it_f64_inventory_turnover_pershare_252d_accel_v042_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare inventory
def it_f64_inventory_turnover_pershare_504d_accel_v043_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare inventory
def it_f64_inventory_turnover_pershare_504d_accel_v044_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare inventory
def it_f64_inventory_turnover_pershare_504d_accel_v045_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_turnover_per_share(inventory, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets inventory
def it_f64_inventory_turnover_per_assets_21d_accel_v046_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets inventory
def it_f64_inventory_turnover_per_assets_21d_accel_v047_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets inventory
def it_f64_inventory_turnover_per_assets_21d_accel_v048_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets inventory
def it_f64_inventory_turnover_per_assets_63d_accel_v049_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets inventory
def it_f64_inventory_turnover_per_assets_63d_accel_v050_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets inventory
def it_f64_inventory_turnover_per_assets_63d_accel_v051_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets inventory
def it_f64_inventory_turnover_per_assets_126d_accel_v052_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets inventory
def it_f64_inventory_turnover_per_assets_126d_accel_v053_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets inventory
def it_f64_inventory_turnover_per_assets_126d_accel_v054_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets inventory
def it_f64_inventory_turnover_per_assets_252d_accel_v055_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets inventory
def it_f64_inventory_turnover_per_assets_252d_accel_v056_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets inventory
def it_f64_inventory_turnover_per_assets_252d_accel_v057_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets inventory
def it_f64_inventory_turnover_per_assets_504d_accel_v058_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets inventory
def it_f64_inventory_turnover_per_assets_504d_accel_v059_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets inventory
def it_f64_inventory_turnover_per_assets_504d_accel_v060_signal(inventory, assets):
    base = _mean(_inventory_turnover_scaled(inventory, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_21d_accel_v061_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_21d_accel_v062_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_21d_accel_v063_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_63d_accel_v064_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_63d_accel_v065_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_63d_accel_v066_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_126d_accel_v067_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_126d_accel_v068_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_126d_accel_v069_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_252d_accel_v070_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_252d_accel_v071_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_252d_accel_v072_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_504d_accel_v073_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_504d_accel_v074_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap inventory
def it_f64_inventory_turnover_per_marketcap_504d_accel_v075_signal(inventory, marketcap):
    base = _mean(_inventory_turnover_scaled(inventory, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity inventory
def it_f64_inventory_turnover_per_equity_21d_accel_v076_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity inventory
def it_f64_inventory_turnover_per_equity_21d_accel_v077_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity inventory
def it_f64_inventory_turnover_per_equity_21d_accel_v078_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity inventory
def it_f64_inventory_turnover_per_equity_63d_accel_v079_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity inventory
def it_f64_inventory_turnover_per_equity_63d_accel_v080_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity inventory
def it_f64_inventory_turnover_per_equity_63d_accel_v081_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity inventory
def it_f64_inventory_turnover_per_equity_126d_accel_v082_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity inventory
def it_f64_inventory_turnover_per_equity_126d_accel_v083_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity inventory
def it_f64_inventory_turnover_per_equity_126d_accel_v084_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity inventory
def it_f64_inventory_turnover_per_equity_252d_accel_v085_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity inventory
def it_f64_inventory_turnover_per_equity_252d_accel_v086_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity inventory
def it_f64_inventory_turnover_per_equity_252d_accel_v087_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity inventory
def it_f64_inventory_turnover_per_equity_504d_accel_v088_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity inventory
def it_f64_inventory_turnover_per_equity_504d_accel_v089_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity inventory
def it_f64_inventory_turnover_per_equity_504d_accel_v090_signal(inventory, equity):
    base = _mean(_inventory_turnover_scaled(inventory, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std inventory
def it_f64_inventory_turnover_std_21d_accel_v091_signal(inventory, closeadj):
    base = _std(inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std inventory
def it_f64_inventory_turnover_std_21d_accel_v092_signal(inventory, closeadj):
    base = _std(inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std inventory
def it_f64_inventory_turnover_std_21d_accel_v093_signal(inventory, closeadj):
    base = _std(inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std inventory
def it_f64_inventory_turnover_std_63d_accel_v094_signal(inventory, closeadj):
    base = _std(inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std inventory
def it_f64_inventory_turnover_std_63d_accel_v095_signal(inventory, closeadj):
    base = _std(inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std inventory
def it_f64_inventory_turnover_std_63d_accel_v096_signal(inventory, closeadj):
    base = _std(inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std inventory
def it_f64_inventory_turnover_std_126d_accel_v097_signal(inventory, closeadj):
    base = _std(inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std inventory
def it_f64_inventory_turnover_std_126d_accel_v098_signal(inventory, closeadj):
    base = _std(inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std inventory
def it_f64_inventory_turnover_std_126d_accel_v099_signal(inventory, closeadj):
    base = _std(inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std inventory
def it_f64_inventory_turnover_std_252d_accel_v100_signal(inventory, closeadj):
    base = _std(inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std inventory
def it_f64_inventory_turnover_std_252d_accel_v101_signal(inventory, closeadj):
    base = _std(inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std inventory
def it_f64_inventory_turnover_std_252d_accel_v102_signal(inventory, closeadj):
    base = _std(inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std inventory
def it_f64_inventory_turnover_std_504d_accel_v103_signal(inventory, closeadj):
    base = _std(inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std inventory
def it_f64_inventory_turnover_std_504d_accel_v104_signal(inventory, closeadj):
    base = _std(inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std inventory
def it_f64_inventory_turnover_std_504d_accel_v105_signal(inventory, closeadj):
    base = _std(inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm inventory
def it_f64_inventory_turnover_ewm_21d_accel_v106_signal(inventory, closeadj):
    base = inventory.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm inventory
def it_f64_inventory_turnover_ewm_21d_accel_v107_signal(inventory, closeadj):
    base = inventory.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm inventory
def it_f64_inventory_turnover_ewm_21d_accel_v108_signal(inventory, closeadj):
    base = inventory.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm inventory
def it_f64_inventory_turnover_ewm_63d_accel_v109_signal(inventory, closeadj):
    base = inventory.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm inventory
def it_f64_inventory_turnover_ewm_63d_accel_v110_signal(inventory, closeadj):
    base = inventory.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm inventory
def it_f64_inventory_turnover_ewm_63d_accel_v111_signal(inventory, closeadj):
    base = inventory.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm inventory
def it_f64_inventory_turnover_ewm_126d_accel_v112_signal(inventory, closeadj):
    base = inventory.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm inventory
def it_f64_inventory_turnover_ewm_126d_accel_v113_signal(inventory, closeadj):
    base = inventory.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm inventory
def it_f64_inventory_turnover_ewm_126d_accel_v114_signal(inventory, closeadj):
    base = inventory.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm inventory
def it_f64_inventory_turnover_ewm_252d_accel_v115_signal(inventory, closeadj):
    base = inventory.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm inventory
def it_f64_inventory_turnover_ewm_252d_accel_v116_signal(inventory, closeadj):
    base = inventory.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm inventory
def it_f64_inventory_turnover_ewm_252d_accel_v117_signal(inventory, closeadj):
    base = inventory.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm inventory
def it_f64_inventory_turnover_ewm_504d_accel_v118_signal(inventory, closeadj):
    base = inventory.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm inventory
def it_f64_inventory_turnover_ewm_504d_accel_v119_signal(inventory, closeadj):
    base = inventory.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm inventory
def it_f64_inventory_turnover_ewm_504d_accel_v120_signal(inventory, closeadj):
    base = inventory.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq inventory
def it_f64_inventory_turnover_sq_21d_accel_v121_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq inventory
def it_f64_inventory_turnover_sq_21d_accel_v122_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq inventory
def it_f64_inventory_turnover_sq_21d_accel_v123_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq inventory
def it_f64_inventory_turnover_sq_63d_accel_v124_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq inventory
def it_f64_inventory_turnover_sq_63d_accel_v125_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq inventory
def it_f64_inventory_turnover_sq_63d_accel_v126_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq inventory
def it_f64_inventory_turnover_sq_126d_accel_v127_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq inventory
def it_f64_inventory_turnover_sq_126d_accel_v128_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq inventory
def it_f64_inventory_turnover_sq_126d_accel_v129_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq inventory
def it_f64_inventory_turnover_sq_252d_accel_v130_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq inventory
def it_f64_inventory_turnover_sq_252d_accel_v131_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq inventory
def it_f64_inventory_turnover_sq_252d_accel_v132_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq inventory
def it_f64_inventory_turnover_sq_504d_accel_v133_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq inventory
def it_f64_inventory_turnover_sq_504d_accel_v134_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq inventory
def it_f64_inventory_turnover_sq_504d_accel_v135_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z inventory
def it_f64_inventory_turnover_z_21d_accel_v136_signal(inventory):
    base = _z(inventory, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z inventory
def it_f64_inventory_turnover_z_21d_accel_v137_signal(inventory):
    base = _z(inventory, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z inventory
def it_f64_inventory_turnover_z_21d_accel_v138_signal(inventory):
    base = _z(inventory, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z inventory
def it_f64_inventory_turnover_z_63d_accel_v139_signal(inventory):
    base = _z(inventory, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z inventory
def it_f64_inventory_turnover_z_63d_accel_v140_signal(inventory):
    base = _z(inventory, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z inventory
def it_f64_inventory_turnover_z_63d_accel_v141_signal(inventory):
    base = _z(inventory, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z inventory
def it_f64_inventory_turnover_z_126d_accel_v142_signal(inventory):
    base = _z(inventory, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z inventory
def it_f64_inventory_turnover_z_126d_accel_v143_signal(inventory):
    base = _z(inventory, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z inventory
def it_f64_inventory_turnover_z_126d_accel_v144_signal(inventory):
    base = _z(inventory, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z inventory
def it_f64_inventory_turnover_z_252d_accel_v145_signal(inventory):
    base = _z(inventory, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z inventory
def it_f64_inventory_turnover_z_252d_accel_v146_signal(inventory):
    base = _z(inventory, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z inventory
def it_f64_inventory_turnover_z_252d_accel_v147_signal(inventory):
    base = _z(inventory, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z inventory
def it_f64_inventory_turnover_z_504d_accel_v148_signal(inventory):
    base = _z(inventory, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z inventory
def it_f64_inventory_turnover_z_504d_accel_v149_signal(inventory):
    base = _z(inventory, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z inventory
def it_f64_inventory_turnover_z_504d_accel_v150_signal(inventory):
    base = _z(inventory, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
