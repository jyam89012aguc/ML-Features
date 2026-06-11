"""Family f068 - Cash conversion cycle proxy (Returns and Efficiency) | Sharadar tables: SF1 | fields: receivables, inventory, payables, revenue, cor | 3rd derivatives 001-150"""
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
def _cash_conversion_cycle_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_conversion_cycle_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_conversion_cycle_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw receivables
def ccc_f068_cash_conversion_cycle_raw_21d_accel_v001_signal(receivables, closeadj):
    base = _mean(receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw receivables
def ccc_f068_cash_conversion_cycle_raw_21d_accel_v002_signal(receivables, closeadj):
    base = _mean(receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw receivables
def ccc_f068_cash_conversion_cycle_raw_21d_accel_v003_signal(receivables, closeadj):
    base = _mean(receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw receivables
def ccc_f068_cash_conversion_cycle_raw_63d_accel_v004_signal(receivables, closeadj):
    base = _mean(receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw receivables
def ccc_f068_cash_conversion_cycle_raw_63d_accel_v005_signal(receivables, closeadj):
    base = _mean(receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw receivables
def ccc_f068_cash_conversion_cycle_raw_63d_accel_v006_signal(receivables, closeadj):
    base = _mean(receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw receivables
def ccc_f068_cash_conversion_cycle_raw_126d_accel_v007_signal(receivables, closeadj):
    base = _mean(receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw receivables
def ccc_f068_cash_conversion_cycle_raw_126d_accel_v008_signal(receivables, closeadj):
    base = _mean(receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw receivables
def ccc_f068_cash_conversion_cycle_raw_126d_accel_v009_signal(receivables, closeadj):
    base = _mean(receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw receivables
def ccc_f068_cash_conversion_cycle_raw_252d_accel_v010_signal(receivables, closeadj):
    base = _mean(receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw receivables
def ccc_f068_cash_conversion_cycle_raw_252d_accel_v011_signal(receivables, closeadj):
    base = _mean(receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw receivables
def ccc_f068_cash_conversion_cycle_raw_252d_accel_v012_signal(receivables, closeadj):
    base = _mean(receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw receivables
def ccc_f068_cash_conversion_cycle_raw_504d_accel_v013_signal(receivables, closeadj):
    base = _mean(receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw receivables
def ccc_f068_cash_conversion_cycle_raw_504d_accel_v014_signal(receivables, closeadj):
    base = _mean(receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw receivables
def ccc_f068_cash_conversion_cycle_raw_504d_accel_v015_signal(receivables, closeadj):
    base = _mean(receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log receivables
def ccc_f068_cash_conversion_cycle_log_21d_accel_v016_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log receivables
def ccc_f068_cash_conversion_cycle_log_21d_accel_v017_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log receivables
def ccc_f068_cash_conversion_cycle_log_21d_accel_v018_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log receivables
def ccc_f068_cash_conversion_cycle_log_63d_accel_v019_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log receivables
def ccc_f068_cash_conversion_cycle_log_63d_accel_v020_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log receivables
def ccc_f068_cash_conversion_cycle_log_63d_accel_v021_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log receivables
def ccc_f068_cash_conversion_cycle_log_126d_accel_v022_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log receivables
def ccc_f068_cash_conversion_cycle_log_126d_accel_v023_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log receivables
def ccc_f068_cash_conversion_cycle_log_126d_accel_v024_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log receivables
def ccc_f068_cash_conversion_cycle_log_252d_accel_v025_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log receivables
def ccc_f068_cash_conversion_cycle_log_252d_accel_v026_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log receivables
def ccc_f068_cash_conversion_cycle_log_252d_accel_v027_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log receivables
def ccc_f068_cash_conversion_cycle_log_504d_accel_v028_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log receivables
def ccc_f068_cash_conversion_cycle_log_504d_accel_v029_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log receivables
def ccc_f068_cash_conversion_cycle_log_504d_accel_v030_signal(receivables, closeadj):
    base = _mean(_cash_conversion_cycle_log(receivables), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_21d_accel_v031_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_21d_accel_v032_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_21d_accel_v033_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_63d_accel_v034_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_63d_accel_v035_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_63d_accel_v036_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_126d_accel_v037_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_126d_accel_v038_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_126d_accel_v039_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_252d_accel_v040_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_252d_accel_v041_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_252d_accel_v042_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_504d_accel_v043_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_504d_accel_v044_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare receivables
def ccc_f068_cash_conversion_cycle_pershare_504d_accel_v045_signal(receivables, sharesbas, closeadj):
    base = _mean(_cash_conversion_cycle_per_share(receivables, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_21d_accel_v046_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_21d_accel_v047_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_21d_accel_v048_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_63d_accel_v049_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_63d_accel_v050_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_63d_accel_v051_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_126d_accel_v052_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_126d_accel_v053_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_126d_accel_v054_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_252d_accel_v055_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_252d_accel_v056_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_252d_accel_v057_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_504d_accel_v058_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_504d_accel_v059_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_inventory receivables
def ccc_f068_cash_conversion_cycle_per_inventory_504d_accel_v060_signal(receivables, inventory):
    base = _mean(_cash_conversion_cycle_scaled(receivables, inventory), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_21d_accel_v061_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_21d_accel_v062_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_21d_accel_v063_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_63d_accel_v064_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_63d_accel_v065_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_63d_accel_v066_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_126d_accel_v067_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_126d_accel_v068_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_126d_accel_v069_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_252d_accel_v070_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_252d_accel_v071_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_252d_accel_v072_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_504d_accel_v073_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_504d_accel_v074_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_payables receivables
def ccc_f068_cash_conversion_cycle_per_payables_504d_accel_v075_signal(receivables, payables):
    base = _mean(_cash_conversion_cycle_scaled(receivables, payables), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_21d_accel_v076_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_21d_accel_v077_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_21d_accel_v078_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_63d_accel_v079_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_63d_accel_v080_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_63d_accel_v081_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_126d_accel_v082_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_126d_accel_v083_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_126d_accel_v084_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_252d_accel_v085_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_252d_accel_v086_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_252d_accel_v087_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_504d_accel_v088_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_504d_accel_v089_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_revenue receivables
def ccc_f068_cash_conversion_cycle_per_revenue_504d_accel_v090_signal(receivables, revenue):
    base = _mean(_cash_conversion_cycle_scaled(receivables, revenue), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std receivables
def ccc_f068_cash_conversion_cycle_std_21d_accel_v091_signal(receivables, closeadj):
    base = _std(receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std receivables
def ccc_f068_cash_conversion_cycle_std_21d_accel_v092_signal(receivables, closeadj):
    base = _std(receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std receivables
def ccc_f068_cash_conversion_cycle_std_21d_accel_v093_signal(receivables, closeadj):
    base = _std(receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std receivables
def ccc_f068_cash_conversion_cycle_std_63d_accel_v094_signal(receivables, closeadj):
    base = _std(receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std receivables
def ccc_f068_cash_conversion_cycle_std_63d_accel_v095_signal(receivables, closeadj):
    base = _std(receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std receivables
def ccc_f068_cash_conversion_cycle_std_63d_accel_v096_signal(receivables, closeadj):
    base = _std(receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std receivables
def ccc_f068_cash_conversion_cycle_std_126d_accel_v097_signal(receivables, closeadj):
    base = _std(receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std receivables
def ccc_f068_cash_conversion_cycle_std_126d_accel_v098_signal(receivables, closeadj):
    base = _std(receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std receivables
def ccc_f068_cash_conversion_cycle_std_126d_accel_v099_signal(receivables, closeadj):
    base = _std(receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std receivables
def ccc_f068_cash_conversion_cycle_std_252d_accel_v100_signal(receivables, closeadj):
    base = _std(receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std receivables
def ccc_f068_cash_conversion_cycle_std_252d_accel_v101_signal(receivables, closeadj):
    base = _std(receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std receivables
def ccc_f068_cash_conversion_cycle_std_252d_accel_v102_signal(receivables, closeadj):
    base = _std(receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std receivables
def ccc_f068_cash_conversion_cycle_std_504d_accel_v103_signal(receivables, closeadj):
    base = _std(receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std receivables
def ccc_f068_cash_conversion_cycle_std_504d_accel_v104_signal(receivables, closeadj):
    base = _std(receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std receivables
def ccc_f068_cash_conversion_cycle_std_504d_accel_v105_signal(receivables, closeadj):
    base = _std(receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_21d_accel_v106_signal(receivables, closeadj):
    base = receivables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_21d_accel_v107_signal(receivables, closeadj):
    base = receivables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_21d_accel_v108_signal(receivables, closeadj):
    base = receivables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_63d_accel_v109_signal(receivables, closeadj):
    base = receivables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_63d_accel_v110_signal(receivables, closeadj):
    base = receivables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_63d_accel_v111_signal(receivables, closeadj):
    base = receivables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_126d_accel_v112_signal(receivables, closeadj):
    base = receivables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_126d_accel_v113_signal(receivables, closeadj):
    base = receivables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_126d_accel_v114_signal(receivables, closeadj):
    base = receivables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_252d_accel_v115_signal(receivables, closeadj):
    base = receivables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_252d_accel_v116_signal(receivables, closeadj):
    base = receivables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_252d_accel_v117_signal(receivables, closeadj):
    base = receivables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_504d_accel_v118_signal(receivables, closeadj):
    base = receivables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_504d_accel_v119_signal(receivables, closeadj):
    base = receivables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm receivables
def ccc_f068_cash_conversion_cycle_ewm_504d_accel_v120_signal(receivables, closeadj):
    base = receivables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq receivables
def ccc_f068_cash_conversion_cycle_sq_21d_accel_v121_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq receivables
def ccc_f068_cash_conversion_cycle_sq_21d_accel_v122_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq receivables
def ccc_f068_cash_conversion_cycle_sq_21d_accel_v123_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq receivables
def ccc_f068_cash_conversion_cycle_sq_63d_accel_v124_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq receivables
def ccc_f068_cash_conversion_cycle_sq_63d_accel_v125_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq receivables
def ccc_f068_cash_conversion_cycle_sq_63d_accel_v126_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq receivables
def ccc_f068_cash_conversion_cycle_sq_126d_accel_v127_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq receivables
def ccc_f068_cash_conversion_cycle_sq_126d_accel_v128_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq receivables
def ccc_f068_cash_conversion_cycle_sq_126d_accel_v129_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq receivables
def ccc_f068_cash_conversion_cycle_sq_252d_accel_v130_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq receivables
def ccc_f068_cash_conversion_cycle_sq_252d_accel_v131_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq receivables
def ccc_f068_cash_conversion_cycle_sq_252d_accel_v132_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq receivables
def ccc_f068_cash_conversion_cycle_sq_504d_accel_v133_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq receivables
def ccc_f068_cash_conversion_cycle_sq_504d_accel_v134_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq receivables
def ccc_f068_cash_conversion_cycle_sq_504d_accel_v135_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z receivables
def ccc_f068_cash_conversion_cycle_z_21d_accel_v136_signal(receivables):
    base = _z(receivables, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z receivables
def ccc_f068_cash_conversion_cycle_z_21d_accel_v137_signal(receivables):
    base = _z(receivables, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z receivables
def ccc_f068_cash_conversion_cycle_z_21d_accel_v138_signal(receivables):
    base = _z(receivables, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z receivables
def ccc_f068_cash_conversion_cycle_z_63d_accel_v139_signal(receivables):
    base = _z(receivables, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z receivables
def ccc_f068_cash_conversion_cycle_z_63d_accel_v140_signal(receivables):
    base = _z(receivables, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z receivables
def ccc_f068_cash_conversion_cycle_z_63d_accel_v141_signal(receivables):
    base = _z(receivables, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z receivables
def ccc_f068_cash_conversion_cycle_z_126d_accel_v142_signal(receivables):
    base = _z(receivables, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z receivables
def ccc_f068_cash_conversion_cycle_z_126d_accel_v143_signal(receivables):
    base = _z(receivables, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z receivables
def ccc_f068_cash_conversion_cycle_z_126d_accel_v144_signal(receivables):
    base = _z(receivables, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z receivables
def ccc_f068_cash_conversion_cycle_z_252d_accel_v145_signal(receivables):
    base = _z(receivables, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z receivables
def ccc_f068_cash_conversion_cycle_z_252d_accel_v146_signal(receivables):
    base = _z(receivables, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z receivables
def ccc_f068_cash_conversion_cycle_z_252d_accel_v147_signal(receivables):
    base = _z(receivables, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z receivables
def ccc_f068_cash_conversion_cycle_z_504d_accel_v148_signal(receivables):
    base = _z(receivables, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z receivables
def ccc_f068_cash_conversion_cycle_z_504d_accel_v149_signal(receivables):
    base = _z(receivables, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z receivables
def ccc_f068_cash_conversion_cycle_z_504d_accel_v150_signal(receivables):
    base = _z(receivables, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
