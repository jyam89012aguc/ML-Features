"""Family f043 - Inventory build and launch readiness (Balance Sheet Composition) | Sharadar tables: SF1 | fields: inventory, revenue, cor, assets | 2nd derivatives 001-150"""
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
def _inventory_build_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _inventory_build_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _inventory_build_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw inventory
def ib_f043_inventory_build_raw_21d_slope_v001_signal(inventory, closeadj):
    base = _mean(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw inventory
def ib_f043_inventory_build_raw_21d_slope_v002_signal(inventory, closeadj):
    base = _mean(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw inventory
def ib_f043_inventory_build_raw_21d_slope_v003_signal(inventory, closeadj):
    base = _mean(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw inventory
def ib_f043_inventory_build_raw_63d_slope_v004_signal(inventory, closeadj):
    base = _mean(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw inventory
def ib_f043_inventory_build_raw_63d_slope_v005_signal(inventory, closeadj):
    base = _mean(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw inventory
def ib_f043_inventory_build_raw_63d_slope_v006_signal(inventory, closeadj):
    base = _mean(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw inventory
def ib_f043_inventory_build_raw_126d_slope_v007_signal(inventory, closeadj):
    base = _mean(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw inventory
def ib_f043_inventory_build_raw_126d_slope_v008_signal(inventory, closeadj):
    base = _mean(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw inventory
def ib_f043_inventory_build_raw_126d_slope_v009_signal(inventory, closeadj):
    base = _mean(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw inventory
def ib_f043_inventory_build_raw_252d_slope_v010_signal(inventory, closeadj):
    base = _mean(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw inventory
def ib_f043_inventory_build_raw_252d_slope_v011_signal(inventory, closeadj):
    base = _mean(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw inventory
def ib_f043_inventory_build_raw_252d_slope_v012_signal(inventory, closeadj):
    base = _mean(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw inventory
def ib_f043_inventory_build_raw_504d_slope_v013_signal(inventory, closeadj):
    base = _mean(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw inventory
def ib_f043_inventory_build_raw_504d_slope_v014_signal(inventory, closeadj):
    base = _mean(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw inventory
def ib_f043_inventory_build_raw_504d_slope_v015_signal(inventory, closeadj):
    base = _mean(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log inventory
def ib_f043_inventory_build_log_21d_slope_v016_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log inventory
def ib_f043_inventory_build_log_21d_slope_v017_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log inventory
def ib_f043_inventory_build_log_21d_slope_v018_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log inventory
def ib_f043_inventory_build_log_63d_slope_v019_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log inventory
def ib_f043_inventory_build_log_63d_slope_v020_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log inventory
def ib_f043_inventory_build_log_63d_slope_v021_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log inventory
def ib_f043_inventory_build_log_126d_slope_v022_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log inventory
def ib_f043_inventory_build_log_126d_slope_v023_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log inventory
def ib_f043_inventory_build_log_126d_slope_v024_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log inventory
def ib_f043_inventory_build_log_252d_slope_v025_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log inventory
def ib_f043_inventory_build_log_252d_slope_v026_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log inventory
def ib_f043_inventory_build_log_252d_slope_v027_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log inventory
def ib_f043_inventory_build_log_504d_slope_v028_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log inventory
def ib_f043_inventory_build_log_504d_slope_v029_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log inventory
def ib_f043_inventory_build_log_504d_slope_v030_signal(inventory, closeadj):
    base = _mean(_inventory_build_log(inventory), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare inventory
def ib_f043_inventory_build_pershare_21d_slope_v031_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare inventory
def ib_f043_inventory_build_pershare_21d_slope_v032_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare inventory
def ib_f043_inventory_build_pershare_21d_slope_v033_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare inventory
def ib_f043_inventory_build_pershare_63d_slope_v034_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare inventory
def ib_f043_inventory_build_pershare_63d_slope_v035_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare inventory
def ib_f043_inventory_build_pershare_63d_slope_v036_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare inventory
def ib_f043_inventory_build_pershare_126d_slope_v037_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare inventory
def ib_f043_inventory_build_pershare_126d_slope_v038_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare inventory
def ib_f043_inventory_build_pershare_126d_slope_v039_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare inventory
def ib_f043_inventory_build_pershare_252d_slope_v040_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare inventory
def ib_f043_inventory_build_pershare_252d_slope_v041_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare inventory
def ib_f043_inventory_build_pershare_252d_slope_v042_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare inventory
def ib_f043_inventory_build_pershare_504d_slope_v043_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare inventory
def ib_f043_inventory_build_pershare_504d_slope_v044_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare inventory
def ib_f043_inventory_build_pershare_504d_slope_v045_signal(inventory, sharesbas, closeadj):
    base = _mean(_inventory_build_per_share(inventory, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_revenue inventory
def ib_f043_inventory_build_per_revenue_21d_slope_v046_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_revenue inventory
def ib_f043_inventory_build_per_revenue_21d_slope_v047_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_revenue inventory
def ib_f043_inventory_build_per_revenue_21d_slope_v048_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_revenue inventory
def ib_f043_inventory_build_per_revenue_63d_slope_v049_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_revenue inventory
def ib_f043_inventory_build_per_revenue_63d_slope_v050_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_revenue inventory
def ib_f043_inventory_build_per_revenue_63d_slope_v051_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_revenue inventory
def ib_f043_inventory_build_per_revenue_126d_slope_v052_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_revenue inventory
def ib_f043_inventory_build_per_revenue_126d_slope_v053_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_revenue inventory
def ib_f043_inventory_build_per_revenue_126d_slope_v054_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_revenue inventory
def ib_f043_inventory_build_per_revenue_252d_slope_v055_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_revenue inventory
def ib_f043_inventory_build_per_revenue_252d_slope_v056_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_revenue inventory
def ib_f043_inventory_build_per_revenue_252d_slope_v057_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_revenue inventory
def ib_f043_inventory_build_per_revenue_504d_slope_v058_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_revenue inventory
def ib_f043_inventory_build_per_revenue_504d_slope_v059_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_revenue inventory
def ib_f043_inventory_build_per_revenue_504d_slope_v060_signal(inventory, revenue):
    base = _mean(_inventory_build_scaled(inventory, revenue), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_cor inventory
def ib_f043_inventory_build_per_cor_21d_slope_v061_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_cor inventory
def ib_f043_inventory_build_per_cor_21d_slope_v062_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_cor inventory
def ib_f043_inventory_build_per_cor_21d_slope_v063_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_cor inventory
def ib_f043_inventory_build_per_cor_63d_slope_v064_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_cor inventory
def ib_f043_inventory_build_per_cor_63d_slope_v065_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_cor inventory
def ib_f043_inventory_build_per_cor_63d_slope_v066_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_cor inventory
def ib_f043_inventory_build_per_cor_126d_slope_v067_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_cor inventory
def ib_f043_inventory_build_per_cor_126d_slope_v068_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_cor inventory
def ib_f043_inventory_build_per_cor_126d_slope_v069_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_cor inventory
def ib_f043_inventory_build_per_cor_252d_slope_v070_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_cor inventory
def ib_f043_inventory_build_per_cor_252d_slope_v071_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_cor inventory
def ib_f043_inventory_build_per_cor_252d_slope_v072_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_cor inventory
def ib_f043_inventory_build_per_cor_504d_slope_v073_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_cor inventory
def ib_f043_inventory_build_per_cor_504d_slope_v074_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_cor inventory
def ib_f043_inventory_build_per_cor_504d_slope_v075_signal(inventory, cor):
    base = _mean(_inventory_build_scaled(inventory, cor), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets inventory
def ib_f043_inventory_build_per_assets_21d_slope_v076_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets inventory
def ib_f043_inventory_build_per_assets_21d_slope_v077_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets inventory
def ib_f043_inventory_build_per_assets_21d_slope_v078_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets inventory
def ib_f043_inventory_build_per_assets_63d_slope_v079_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets inventory
def ib_f043_inventory_build_per_assets_63d_slope_v080_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets inventory
def ib_f043_inventory_build_per_assets_63d_slope_v081_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets inventory
def ib_f043_inventory_build_per_assets_126d_slope_v082_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets inventory
def ib_f043_inventory_build_per_assets_126d_slope_v083_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets inventory
def ib_f043_inventory_build_per_assets_126d_slope_v084_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets inventory
def ib_f043_inventory_build_per_assets_252d_slope_v085_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets inventory
def ib_f043_inventory_build_per_assets_252d_slope_v086_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets inventory
def ib_f043_inventory_build_per_assets_252d_slope_v087_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets inventory
def ib_f043_inventory_build_per_assets_504d_slope_v088_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets inventory
def ib_f043_inventory_build_per_assets_504d_slope_v089_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets inventory
def ib_f043_inventory_build_per_assets_504d_slope_v090_signal(inventory, assets):
    base = _mean(_inventory_build_scaled(inventory, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std inventory
def ib_f043_inventory_build_std_21d_slope_v091_signal(inventory, closeadj):
    base = _std(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std inventory
def ib_f043_inventory_build_std_21d_slope_v092_signal(inventory, closeadj):
    base = _std(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std inventory
def ib_f043_inventory_build_std_21d_slope_v093_signal(inventory, closeadj):
    base = _std(inventory, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std inventory
def ib_f043_inventory_build_std_63d_slope_v094_signal(inventory, closeadj):
    base = _std(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std inventory
def ib_f043_inventory_build_std_63d_slope_v095_signal(inventory, closeadj):
    base = _std(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std inventory
def ib_f043_inventory_build_std_63d_slope_v096_signal(inventory, closeadj):
    base = _std(inventory, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std inventory
def ib_f043_inventory_build_std_126d_slope_v097_signal(inventory, closeadj):
    base = _std(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std inventory
def ib_f043_inventory_build_std_126d_slope_v098_signal(inventory, closeadj):
    base = _std(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std inventory
def ib_f043_inventory_build_std_126d_slope_v099_signal(inventory, closeadj):
    base = _std(inventory, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std inventory
def ib_f043_inventory_build_std_252d_slope_v100_signal(inventory, closeadj):
    base = _std(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std inventory
def ib_f043_inventory_build_std_252d_slope_v101_signal(inventory, closeadj):
    base = _std(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std inventory
def ib_f043_inventory_build_std_252d_slope_v102_signal(inventory, closeadj):
    base = _std(inventory, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std inventory
def ib_f043_inventory_build_std_504d_slope_v103_signal(inventory, closeadj):
    base = _std(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std inventory
def ib_f043_inventory_build_std_504d_slope_v104_signal(inventory, closeadj):
    base = _std(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std inventory
def ib_f043_inventory_build_std_504d_slope_v105_signal(inventory, closeadj):
    base = _std(inventory, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm inventory
def ib_f043_inventory_build_ewm_21d_slope_v106_signal(inventory, closeadj):
    base = inventory.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm inventory
def ib_f043_inventory_build_ewm_21d_slope_v107_signal(inventory, closeadj):
    base = inventory.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm inventory
def ib_f043_inventory_build_ewm_21d_slope_v108_signal(inventory, closeadj):
    base = inventory.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm inventory
def ib_f043_inventory_build_ewm_63d_slope_v109_signal(inventory, closeadj):
    base = inventory.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm inventory
def ib_f043_inventory_build_ewm_63d_slope_v110_signal(inventory, closeadj):
    base = inventory.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm inventory
def ib_f043_inventory_build_ewm_63d_slope_v111_signal(inventory, closeadj):
    base = inventory.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm inventory
def ib_f043_inventory_build_ewm_126d_slope_v112_signal(inventory, closeadj):
    base = inventory.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm inventory
def ib_f043_inventory_build_ewm_126d_slope_v113_signal(inventory, closeadj):
    base = inventory.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm inventory
def ib_f043_inventory_build_ewm_126d_slope_v114_signal(inventory, closeadj):
    base = inventory.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm inventory
def ib_f043_inventory_build_ewm_252d_slope_v115_signal(inventory, closeadj):
    base = inventory.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm inventory
def ib_f043_inventory_build_ewm_252d_slope_v116_signal(inventory, closeadj):
    base = inventory.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm inventory
def ib_f043_inventory_build_ewm_252d_slope_v117_signal(inventory, closeadj):
    base = inventory.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm inventory
def ib_f043_inventory_build_ewm_504d_slope_v118_signal(inventory, closeadj):
    base = inventory.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm inventory
def ib_f043_inventory_build_ewm_504d_slope_v119_signal(inventory, closeadj):
    base = inventory.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm inventory
def ib_f043_inventory_build_ewm_504d_slope_v120_signal(inventory, closeadj):
    base = inventory.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq inventory
def ib_f043_inventory_build_sq_21d_slope_v121_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq inventory
def ib_f043_inventory_build_sq_21d_slope_v122_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq inventory
def ib_f043_inventory_build_sq_21d_slope_v123_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq inventory
def ib_f043_inventory_build_sq_63d_slope_v124_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq inventory
def ib_f043_inventory_build_sq_63d_slope_v125_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq inventory
def ib_f043_inventory_build_sq_63d_slope_v126_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq inventory
def ib_f043_inventory_build_sq_126d_slope_v127_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq inventory
def ib_f043_inventory_build_sq_126d_slope_v128_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq inventory
def ib_f043_inventory_build_sq_126d_slope_v129_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq inventory
def ib_f043_inventory_build_sq_252d_slope_v130_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq inventory
def ib_f043_inventory_build_sq_252d_slope_v131_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq inventory
def ib_f043_inventory_build_sq_252d_slope_v132_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq inventory
def ib_f043_inventory_build_sq_504d_slope_v133_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq inventory
def ib_f043_inventory_build_sq_504d_slope_v134_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq inventory
def ib_f043_inventory_build_sq_504d_slope_v135_signal(inventory, closeadj):
    base = _mean(inventory * inventory, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z inventory
def ib_f043_inventory_build_z_21d_slope_v136_signal(inventory):
    base = _z(inventory, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z inventory
def ib_f043_inventory_build_z_21d_slope_v137_signal(inventory):
    base = _z(inventory, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z inventory
def ib_f043_inventory_build_z_21d_slope_v138_signal(inventory):
    base = _z(inventory, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z inventory
def ib_f043_inventory_build_z_63d_slope_v139_signal(inventory):
    base = _z(inventory, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z inventory
def ib_f043_inventory_build_z_63d_slope_v140_signal(inventory):
    base = _z(inventory, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z inventory
def ib_f043_inventory_build_z_63d_slope_v141_signal(inventory):
    base = _z(inventory, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z inventory
def ib_f043_inventory_build_z_126d_slope_v142_signal(inventory):
    base = _z(inventory, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z inventory
def ib_f043_inventory_build_z_126d_slope_v143_signal(inventory):
    base = _z(inventory, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z inventory
def ib_f043_inventory_build_z_126d_slope_v144_signal(inventory):
    base = _z(inventory, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z inventory
def ib_f043_inventory_build_z_252d_slope_v145_signal(inventory):
    base = _z(inventory, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z inventory
def ib_f043_inventory_build_z_252d_slope_v146_signal(inventory):
    base = _z(inventory, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z inventory
def ib_f043_inventory_build_z_252d_slope_v147_signal(inventory):
    base = _z(inventory, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z inventory
def ib_f043_inventory_build_z_504d_slope_v148_signal(inventory):
    base = _z(inventory, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z inventory
def ib_f043_inventory_build_z_504d_slope_v149_signal(inventory):
    base = _z(inventory, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z inventory
def ib_f043_inventory_build_z_504d_slope_v150_signal(inventory):
    base = _z(inventory, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
