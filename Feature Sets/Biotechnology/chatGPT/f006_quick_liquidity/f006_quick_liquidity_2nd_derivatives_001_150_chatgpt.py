"""Family f006 - Inventory-excluded liquidity (Liquidity and Runway) | Sharadar tables: SF1 | fields: assetsc, inventory, liabilitiesc, cashneq | 2nd derivatives 001-150"""
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
def _quick_liquidity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _quick_liquidity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _quick_liquidity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw assetsc
def ql_f006_quick_liquidity_raw_21d_slope_v001_signal(assetsc, closeadj):
    base = _mean(assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw assetsc
def ql_f006_quick_liquidity_raw_21d_slope_v002_signal(assetsc, closeadj):
    base = _mean(assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw assetsc
def ql_f006_quick_liquidity_raw_21d_slope_v003_signal(assetsc, closeadj):
    base = _mean(assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw assetsc
def ql_f006_quick_liquidity_raw_63d_slope_v004_signal(assetsc, closeadj):
    base = _mean(assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw assetsc
def ql_f006_quick_liquidity_raw_63d_slope_v005_signal(assetsc, closeadj):
    base = _mean(assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw assetsc
def ql_f006_quick_liquidity_raw_63d_slope_v006_signal(assetsc, closeadj):
    base = _mean(assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw assetsc
def ql_f006_quick_liquidity_raw_126d_slope_v007_signal(assetsc, closeadj):
    base = _mean(assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw assetsc
def ql_f006_quick_liquidity_raw_126d_slope_v008_signal(assetsc, closeadj):
    base = _mean(assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw assetsc
def ql_f006_quick_liquidity_raw_126d_slope_v009_signal(assetsc, closeadj):
    base = _mean(assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw assetsc
def ql_f006_quick_liquidity_raw_252d_slope_v010_signal(assetsc, closeadj):
    base = _mean(assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw assetsc
def ql_f006_quick_liquidity_raw_252d_slope_v011_signal(assetsc, closeadj):
    base = _mean(assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw assetsc
def ql_f006_quick_liquidity_raw_252d_slope_v012_signal(assetsc, closeadj):
    base = _mean(assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw assetsc
def ql_f006_quick_liquidity_raw_504d_slope_v013_signal(assetsc, closeadj):
    base = _mean(assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw assetsc
def ql_f006_quick_liquidity_raw_504d_slope_v014_signal(assetsc, closeadj):
    base = _mean(assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw assetsc
def ql_f006_quick_liquidity_raw_504d_slope_v015_signal(assetsc, closeadj):
    base = _mean(assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log assetsc
def ql_f006_quick_liquidity_log_21d_slope_v016_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log assetsc
def ql_f006_quick_liquidity_log_21d_slope_v017_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log assetsc
def ql_f006_quick_liquidity_log_21d_slope_v018_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log assetsc
def ql_f006_quick_liquidity_log_63d_slope_v019_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log assetsc
def ql_f006_quick_liquidity_log_63d_slope_v020_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log assetsc
def ql_f006_quick_liquidity_log_63d_slope_v021_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log assetsc
def ql_f006_quick_liquidity_log_126d_slope_v022_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log assetsc
def ql_f006_quick_liquidity_log_126d_slope_v023_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log assetsc
def ql_f006_quick_liquidity_log_126d_slope_v024_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log assetsc
def ql_f006_quick_liquidity_log_252d_slope_v025_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log assetsc
def ql_f006_quick_liquidity_log_252d_slope_v026_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log assetsc
def ql_f006_quick_liquidity_log_252d_slope_v027_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log assetsc
def ql_f006_quick_liquidity_log_504d_slope_v028_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log assetsc
def ql_f006_quick_liquidity_log_504d_slope_v029_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log assetsc
def ql_f006_quick_liquidity_log_504d_slope_v030_signal(assetsc, closeadj):
    base = _mean(_quick_liquidity_log(assetsc), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare assetsc
def ql_f006_quick_liquidity_pershare_21d_slope_v031_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare assetsc
def ql_f006_quick_liquidity_pershare_21d_slope_v032_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare assetsc
def ql_f006_quick_liquidity_pershare_21d_slope_v033_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare assetsc
def ql_f006_quick_liquidity_pershare_63d_slope_v034_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare assetsc
def ql_f006_quick_liquidity_pershare_63d_slope_v035_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare assetsc
def ql_f006_quick_liquidity_pershare_63d_slope_v036_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare assetsc
def ql_f006_quick_liquidity_pershare_126d_slope_v037_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare assetsc
def ql_f006_quick_liquidity_pershare_126d_slope_v038_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare assetsc
def ql_f006_quick_liquidity_pershare_126d_slope_v039_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare assetsc
def ql_f006_quick_liquidity_pershare_252d_slope_v040_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare assetsc
def ql_f006_quick_liquidity_pershare_252d_slope_v041_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare assetsc
def ql_f006_quick_liquidity_pershare_252d_slope_v042_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare assetsc
def ql_f006_quick_liquidity_pershare_504d_slope_v043_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare assetsc
def ql_f006_quick_liquidity_pershare_504d_slope_v044_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare assetsc
def ql_f006_quick_liquidity_pershare_504d_slope_v045_signal(assetsc, sharesbas, closeadj):
    base = _mean(_quick_liquidity_per_share(assetsc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_21d_slope_v046_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_21d_slope_v047_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_21d_slope_v048_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_63d_slope_v049_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_63d_slope_v050_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_63d_slope_v051_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_126d_slope_v052_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_126d_slope_v053_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_126d_slope_v054_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_252d_slope_v055_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_252d_slope_v056_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_252d_slope_v057_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_504d_slope_v058_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_504d_slope_v059_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_inventory assetsc
def ql_f006_quick_liquidity_per_inventory_504d_slope_v060_signal(assetsc, inventory):
    base = _mean(_quick_liquidity_scaled(assetsc, inventory), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_21d_slope_v061_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_21d_slope_v062_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_21d_slope_v063_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_63d_slope_v064_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_63d_slope_v065_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_63d_slope_v066_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_126d_slope_v067_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_126d_slope_v068_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_126d_slope_v069_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_252d_slope_v070_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_252d_slope_v071_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_252d_slope_v072_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_504d_slope_v073_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_504d_slope_v074_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_liabilitiesc assetsc
def ql_f006_quick_liquidity_per_liabilitiesc_504d_slope_v075_signal(assetsc, liabilitiesc):
    base = _mean(_quick_liquidity_scaled(assetsc, liabilitiesc), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_21d_slope_v076_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_21d_slope_v077_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_21d_slope_v078_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_63d_slope_v079_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_63d_slope_v080_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_63d_slope_v081_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_126d_slope_v082_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_126d_slope_v083_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_126d_slope_v084_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_252d_slope_v085_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_252d_slope_v086_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_252d_slope_v087_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_504d_slope_v088_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_504d_slope_v089_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_cashneq assetsc
def ql_f006_quick_liquidity_per_cashneq_504d_slope_v090_signal(assetsc, cashneq):
    base = _mean(_quick_liquidity_scaled(assetsc, cashneq), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std assetsc
def ql_f006_quick_liquidity_std_21d_slope_v091_signal(assetsc, closeadj):
    base = _std(assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std assetsc
def ql_f006_quick_liquidity_std_21d_slope_v092_signal(assetsc, closeadj):
    base = _std(assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std assetsc
def ql_f006_quick_liquidity_std_21d_slope_v093_signal(assetsc, closeadj):
    base = _std(assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std assetsc
def ql_f006_quick_liquidity_std_63d_slope_v094_signal(assetsc, closeadj):
    base = _std(assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std assetsc
def ql_f006_quick_liquidity_std_63d_slope_v095_signal(assetsc, closeadj):
    base = _std(assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std assetsc
def ql_f006_quick_liquidity_std_63d_slope_v096_signal(assetsc, closeadj):
    base = _std(assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std assetsc
def ql_f006_quick_liquidity_std_126d_slope_v097_signal(assetsc, closeadj):
    base = _std(assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std assetsc
def ql_f006_quick_liquidity_std_126d_slope_v098_signal(assetsc, closeadj):
    base = _std(assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std assetsc
def ql_f006_quick_liquidity_std_126d_slope_v099_signal(assetsc, closeadj):
    base = _std(assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std assetsc
def ql_f006_quick_liquidity_std_252d_slope_v100_signal(assetsc, closeadj):
    base = _std(assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std assetsc
def ql_f006_quick_liquidity_std_252d_slope_v101_signal(assetsc, closeadj):
    base = _std(assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std assetsc
def ql_f006_quick_liquidity_std_252d_slope_v102_signal(assetsc, closeadj):
    base = _std(assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std assetsc
def ql_f006_quick_liquidity_std_504d_slope_v103_signal(assetsc, closeadj):
    base = _std(assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std assetsc
def ql_f006_quick_liquidity_std_504d_slope_v104_signal(assetsc, closeadj):
    base = _std(assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std assetsc
def ql_f006_quick_liquidity_std_504d_slope_v105_signal(assetsc, closeadj):
    base = _std(assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm assetsc
def ql_f006_quick_liquidity_ewm_21d_slope_v106_signal(assetsc, closeadj):
    base = assetsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm assetsc
def ql_f006_quick_liquidity_ewm_21d_slope_v107_signal(assetsc, closeadj):
    base = assetsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm assetsc
def ql_f006_quick_liquidity_ewm_21d_slope_v108_signal(assetsc, closeadj):
    base = assetsc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm assetsc
def ql_f006_quick_liquidity_ewm_63d_slope_v109_signal(assetsc, closeadj):
    base = assetsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm assetsc
def ql_f006_quick_liquidity_ewm_63d_slope_v110_signal(assetsc, closeadj):
    base = assetsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm assetsc
def ql_f006_quick_liquidity_ewm_63d_slope_v111_signal(assetsc, closeadj):
    base = assetsc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm assetsc
def ql_f006_quick_liquidity_ewm_126d_slope_v112_signal(assetsc, closeadj):
    base = assetsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm assetsc
def ql_f006_quick_liquidity_ewm_126d_slope_v113_signal(assetsc, closeadj):
    base = assetsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm assetsc
def ql_f006_quick_liquidity_ewm_126d_slope_v114_signal(assetsc, closeadj):
    base = assetsc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm assetsc
def ql_f006_quick_liquidity_ewm_252d_slope_v115_signal(assetsc, closeadj):
    base = assetsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm assetsc
def ql_f006_quick_liquidity_ewm_252d_slope_v116_signal(assetsc, closeadj):
    base = assetsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm assetsc
def ql_f006_quick_liquidity_ewm_252d_slope_v117_signal(assetsc, closeadj):
    base = assetsc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm assetsc
def ql_f006_quick_liquidity_ewm_504d_slope_v118_signal(assetsc, closeadj):
    base = assetsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm assetsc
def ql_f006_quick_liquidity_ewm_504d_slope_v119_signal(assetsc, closeadj):
    base = assetsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm assetsc
def ql_f006_quick_liquidity_ewm_504d_slope_v120_signal(assetsc, closeadj):
    base = assetsc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq assetsc
def ql_f006_quick_liquidity_sq_21d_slope_v121_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq assetsc
def ql_f006_quick_liquidity_sq_21d_slope_v122_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq assetsc
def ql_f006_quick_liquidity_sq_21d_slope_v123_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq assetsc
def ql_f006_quick_liquidity_sq_63d_slope_v124_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq assetsc
def ql_f006_quick_liquidity_sq_63d_slope_v125_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq assetsc
def ql_f006_quick_liquidity_sq_63d_slope_v126_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq assetsc
def ql_f006_quick_liquidity_sq_126d_slope_v127_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq assetsc
def ql_f006_quick_liquidity_sq_126d_slope_v128_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq assetsc
def ql_f006_quick_liquidity_sq_126d_slope_v129_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq assetsc
def ql_f006_quick_liquidity_sq_252d_slope_v130_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq assetsc
def ql_f006_quick_liquidity_sq_252d_slope_v131_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq assetsc
def ql_f006_quick_liquidity_sq_252d_slope_v132_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq assetsc
def ql_f006_quick_liquidity_sq_504d_slope_v133_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq assetsc
def ql_f006_quick_liquidity_sq_504d_slope_v134_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq assetsc
def ql_f006_quick_liquidity_sq_504d_slope_v135_signal(assetsc, closeadj):
    base = _mean(assetsc * assetsc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z assetsc
def ql_f006_quick_liquidity_z_21d_slope_v136_signal(assetsc):
    base = _z(assetsc, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z assetsc
def ql_f006_quick_liquidity_z_21d_slope_v137_signal(assetsc):
    base = _z(assetsc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z assetsc
def ql_f006_quick_liquidity_z_21d_slope_v138_signal(assetsc):
    base = _z(assetsc, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z assetsc
def ql_f006_quick_liquidity_z_63d_slope_v139_signal(assetsc):
    base = _z(assetsc, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z assetsc
def ql_f006_quick_liquidity_z_63d_slope_v140_signal(assetsc):
    base = _z(assetsc, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z assetsc
def ql_f006_quick_liquidity_z_63d_slope_v141_signal(assetsc):
    base = _z(assetsc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z assetsc
def ql_f006_quick_liquidity_z_126d_slope_v142_signal(assetsc):
    base = _z(assetsc, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z assetsc
def ql_f006_quick_liquidity_z_126d_slope_v143_signal(assetsc):
    base = _z(assetsc, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z assetsc
def ql_f006_quick_liquidity_z_126d_slope_v144_signal(assetsc):
    base = _z(assetsc, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z assetsc
def ql_f006_quick_liquidity_z_252d_slope_v145_signal(assetsc):
    base = _z(assetsc, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z assetsc
def ql_f006_quick_liquidity_z_252d_slope_v146_signal(assetsc):
    base = _z(assetsc, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z assetsc
def ql_f006_quick_liquidity_z_252d_slope_v147_signal(assetsc):
    base = _z(assetsc, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z assetsc
def ql_f006_quick_liquidity_z_504d_slope_v148_signal(assetsc):
    base = _z(assetsc, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z assetsc
def ql_f006_quick_liquidity_z_504d_slope_v149_signal(assetsc):
    base = _z(assetsc, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z assetsc
def ql_f006_quick_liquidity_z_504d_slope_v150_signal(assetsc):
    base = _z(assetsc, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
