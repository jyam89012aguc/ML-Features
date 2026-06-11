"""Family f022 - Total debt burden (Capital Structure) | Sharadar tables: SF1 | fields: debt, debtusd, assets, equity, marketcap | 3rd derivatives 001-150"""
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
def _debt_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _debt_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _debt_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw debt
def dl_f022_debt_level_raw_21d_accel_v001_signal(debt, closeadj):
    base = _mean(debt, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw debt
def dl_f022_debt_level_raw_21d_accel_v002_signal(debt, closeadj):
    base = _mean(debt, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw debt
def dl_f022_debt_level_raw_21d_accel_v003_signal(debt, closeadj):
    base = _mean(debt, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw debt
def dl_f022_debt_level_raw_63d_accel_v004_signal(debt, closeadj):
    base = _mean(debt, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw debt
def dl_f022_debt_level_raw_63d_accel_v005_signal(debt, closeadj):
    base = _mean(debt, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw debt
def dl_f022_debt_level_raw_63d_accel_v006_signal(debt, closeadj):
    base = _mean(debt, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw debt
def dl_f022_debt_level_raw_126d_accel_v007_signal(debt, closeadj):
    base = _mean(debt, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw debt
def dl_f022_debt_level_raw_126d_accel_v008_signal(debt, closeadj):
    base = _mean(debt, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw debt
def dl_f022_debt_level_raw_126d_accel_v009_signal(debt, closeadj):
    base = _mean(debt, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw debt
def dl_f022_debt_level_raw_252d_accel_v010_signal(debt, closeadj):
    base = _mean(debt, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw debt
def dl_f022_debt_level_raw_252d_accel_v011_signal(debt, closeadj):
    base = _mean(debt, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw debt
def dl_f022_debt_level_raw_252d_accel_v012_signal(debt, closeadj):
    base = _mean(debt, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw debt
def dl_f022_debt_level_raw_504d_accel_v013_signal(debt, closeadj):
    base = _mean(debt, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw debt
def dl_f022_debt_level_raw_504d_accel_v014_signal(debt, closeadj):
    base = _mean(debt, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw debt
def dl_f022_debt_level_raw_504d_accel_v015_signal(debt, closeadj):
    base = _mean(debt, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log debt
def dl_f022_debt_level_log_21d_accel_v016_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log debt
def dl_f022_debt_level_log_21d_accel_v017_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log debt
def dl_f022_debt_level_log_21d_accel_v018_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log debt
def dl_f022_debt_level_log_63d_accel_v019_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log debt
def dl_f022_debt_level_log_63d_accel_v020_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log debt
def dl_f022_debt_level_log_63d_accel_v021_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log debt
def dl_f022_debt_level_log_126d_accel_v022_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log debt
def dl_f022_debt_level_log_126d_accel_v023_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log debt
def dl_f022_debt_level_log_126d_accel_v024_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log debt
def dl_f022_debt_level_log_252d_accel_v025_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log debt
def dl_f022_debt_level_log_252d_accel_v026_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log debt
def dl_f022_debt_level_log_252d_accel_v027_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log debt
def dl_f022_debt_level_log_504d_accel_v028_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log debt
def dl_f022_debt_level_log_504d_accel_v029_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log debt
def dl_f022_debt_level_log_504d_accel_v030_signal(debt, closeadj):
    base = _mean(_debt_level_log(debt), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare debt
def dl_f022_debt_level_pershare_21d_accel_v031_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare debt
def dl_f022_debt_level_pershare_21d_accel_v032_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare debt
def dl_f022_debt_level_pershare_21d_accel_v033_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare debt
def dl_f022_debt_level_pershare_63d_accel_v034_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare debt
def dl_f022_debt_level_pershare_63d_accel_v035_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare debt
def dl_f022_debt_level_pershare_63d_accel_v036_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare debt
def dl_f022_debt_level_pershare_126d_accel_v037_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare debt
def dl_f022_debt_level_pershare_126d_accel_v038_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare debt
def dl_f022_debt_level_pershare_126d_accel_v039_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare debt
def dl_f022_debt_level_pershare_252d_accel_v040_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare debt
def dl_f022_debt_level_pershare_252d_accel_v041_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare debt
def dl_f022_debt_level_pershare_252d_accel_v042_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare debt
def dl_f022_debt_level_pershare_504d_accel_v043_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare debt
def dl_f022_debt_level_pershare_504d_accel_v044_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare debt
def dl_f022_debt_level_pershare_504d_accel_v045_signal(debt, sharesbas, closeadj):
    base = _mean(_debt_level_per_share(debt, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_debtusd debt
def dl_f022_debt_level_per_debtusd_21d_accel_v046_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_debtusd debt
def dl_f022_debt_level_per_debtusd_21d_accel_v047_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_debtusd debt
def dl_f022_debt_level_per_debtusd_21d_accel_v048_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_debtusd debt
def dl_f022_debt_level_per_debtusd_63d_accel_v049_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_debtusd debt
def dl_f022_debt_level_per_debtusd_63d_accel_v050_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_debtusd debt
def dl_f022_debt_level_per_debtusd_63d_accel_v051_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_debtusd debt
def dl_f022_debt_level_per_debtusd_126d_accel_v052_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_debtusd debt
def dl_f022_debt_level_per_debtusd_126d_accel_v053_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_debtusd debt
def dl_f022_debt_level_per_debtusd_126d_accel_v054_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_debtusd debt
def dl_f022_debt_level_per_debtusd_252d_accel_v055_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_debtusd debt
def dl_f022_debt_level_per_debtusd_252d_accel_v056_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_debtusd debt
def dl_f022_debt_level_per_debtusd_252d_accel_v057_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_debtusd debt
def dl_f022_debt_level_per_debtusd_504d_accel_v058_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_debtusd debt
def dl_f022_debt_level_per_debtusd_504d_accel_v059_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_debtusd debt
def dl_f022_debt_level_per_debtusd_504d_accel_v060_signal(debt, debtusd):
    base = _mean(_debt_level_scaled(debt, debtusd), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets debt
def dl_f022_debt_level_per_assets_21d_accel_v061_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets debt
def dl_f022_debt_level_per_assets_21d_accel_v062_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets debt
def dl_f022_debt_level_per_assets_21d_accel_v063_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets debt
def dl_f022_debt_level_per_assets_63d_accel_v064_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets debt
def dl_f022_debt_level_per_assets_63d_accel_v065_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets debt
def dl_f022_debt_level_per_assets_63d_accel_v066_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets debt
def dl_f022_debt_level_per_assets_126d_accel_v067_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets debt
def dl_f022_debt_level_per_assets_126d_accel_v068_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets debt
def dl_f022_debt_level_per_assets_126d_accel_v069_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets debt
def dl_f022_debt_level_per_assets_252d_accel_v070_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets debt
def dl_f022_debt_level_per_assets_252d_accel_v071_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets debt
def dl_f022_debt_level_per_assets_252d_accel_v072_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets debt
def dl_f022_debt_level_per_assets_504d_accel_v073_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets debt
def dl_f022_debt_level_per_assets_504d_accel_v074_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets debt
def dl_f022_debt_level_per_assets_504d_accel_v075_signal(debt, assets):
    base = _mean(_debt_level_scaled(debt, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity debt
def dl_f022_debt_level_per_equity_21d_accel_v076_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity debt
def dl_f022_debt_level_per_equity_21d_accel_v077_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity debt
def dl_f022_debt_level_per_equity_21d_accel_v078_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity debt
def dl_f022_debt_level_per_equity_63d_accel_v079_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity debt
def dl_f022_debt_level_per_equity_63d_accel_v080_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity debt
def dl_f022_debt_level_per_equity_63d_accel_v081_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity debt
def dl_f022_debt_level_per_equity_126d_accel_v082_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity debt
def dl_f022_debt_level_per_equity_126d_accel_v083_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity debt
def dl_f022_debt_level_per_equity_126d_accel_v084_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity debt
def dl_f022_debt_level_per_equity_252d_accel_v085_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity debt
def dl_f022_debt_level_per_equity_252d_accel_v086_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity debt
def dl_f022_debt_level_per_equity_252d_accel_v087_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity debt
def dl_f022_debt_level_per_equity_504d_accel_v088_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity debt
def dl_f022_debt_level_per_equity_504d_accel_v089_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity debt
def dl_f022_debt_level_per_equity_504d_accel_v090_signal(debt, equity):
    base = _mean(_debt_level_scaled(debt, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std debt
def dl_f022_debt_level_std_21d_accel_v091_signal(debt, closeadj):
    base = _std(debt, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std debt
def dl_f022_debt_level_std_21d_accel_v092_signal(debt, closeadj):
    base = _std(debt, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std debt
def dl_f022_debt_level_std_21d_accel_v093_signal(debt, closeadj):
    base = _std(debt, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std debt
def dl_f022_debt_level_std_63d_accel_v094_signal(debt, closeadj):
    base = _std(debt, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std debt
def dl_f022_debt_level_std_63d_accel_v095_signal(debt, closeadj):
    base = _std(debt, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std debt
def dl_f022_debt_level_std_63d_accel_v096_signal(debt, closeadj):
    base = _std(debt, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std debt
def dl_f022_debt_level_std_126d_accel_v097_signal(debt, closeadj):
    base = _std(debt, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std debt
def dl_f022_debt_level_std_126d_accel_v098_signal(debt, closeadj):
    base = _std(debt, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std debt
def dl_f022_debt_level_std_126d_accel_v099_signal(debt, closeadj):
    base = _std(debt, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std debt
def dl_f022_debt_level_std_252d_accel_v100_signal(debt, closeadj):
    base = _std(debt, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std debt
def dl_f022_debt_level_std_252d_accel_v101_signal(debt, closeadj):
    base = _std(debt, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std debt
def dl_f022_debt_level_std_252d_accel_v102_signal(debt, closeadj):
    base = _std(debt, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std debt
def dl_f022_debt_level_std_504d_accel_v103_signal(debt, closeadj):
    base = _std(debt, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std debt
def dl_f022_debt_level_std_504d_accel_v104_signal(debt, closeadj):
    base = _std(debt, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std debt
def dl_f022_debt_level_std_504d_accel_v105_signal(debt, closeadj):
    base = _std(debt, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm debt
def dl_f022_debt_level_ewm_21d_accel_v106_signal(debt, closeadj):
    base = debt.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm debt
def dl_f022_debt_level_ewm_21d_accel_v107_signal(debt, closeadj):
    base = debt.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm debt
def dl_f022_debt_level_ewm_21d_accel_v108_signal(debt, closeadj):
    base = debt.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm debt
def dl_f022_debt_level_ewm_63d_accel_v109_signal(debt, closeadj):
    base = debt.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm debt
def dl_f022_debt_level_ewm_63d_accel_v110_signal(debt, closeadj):
    base = debt.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm debt
def dl_f022_debt_level_ewm_63d_accel_v111_signal(debt, closeadj):
    base = debt.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm debt
def dl_f022_debt_level_ewm_126d_accel_v112_signal(debt, closeadj):
    base = debt.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm debt
def dl_f022_debt_level_ewm_126d_accel_v113_signal(debt, closeadj):
    base = debt.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm debt
def dl_f022_debt_level_ewm_126d_accel_v114_signal(debt, closeadj):
    base = debt.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm debt
def dl_f022_debt_level_ewm_252d_accel_v115_signal(debt, closeadj):
    base = debt.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm debt
def dl_f022_debt_level_ewm_252d_accel_v116_signal(debt, closeadj):
    base = debt.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm debt
def dl_f022_debt_level_ewm_252d_accel_v117_signal(debt, closeadj):
    base = debt.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm debt
def dl_f022_debt_level_ewm_504d_accel_v118_signal(debt, closeadj):
    base = debt.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm debt
def dl_f022_debt_level_ewm_504d_accel_v119_signal(debt, closeadj):
    base = debt.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm debt
def dl_f022_debt_level_ewm_504d_accel_v120_signal(debt, closeadj):
    base = debt.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq debt
def dl_f022_debt_level_sq_21d_accel_v121_signal(debt, closeadj):
    base = _mean(debt * debt, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq debt
def dl_f022_debt_level_sq_21d_accel_v122_signal(debt, closeadj):
    base = _mean(debt * debt, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq debt
def dl_f022_debt_level_sq_21d_accel_v123_signal(debt, closeadj):
    base = _mean(debt * debt, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq debt
def dl_f022_debt_level_sq_63d_accel_v124_signal(debt, closeadj):
    base = _mean(debt * debt, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq debt
def dl_f022_debt_level_sq_63d_accel_v125_signal(debt, closeadj):
    base = _mean(debt * debt, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq debt
def dl_f022_debt_level_sq_63d_accel_v126_signal(debt, closeadj):
    base = _mean(debt * debt, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq debt
def dl_f022_debt_level_sq_126d_accel_v127_signal(debt, closeadj):
    base = _mean(debt * debt, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq debt
def dl_f022_debt_level_sq_126d_accel_v128_signal(debt, closeadj):
    base = _mean(debt * debt, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq debt
def dl_f022_debt_level_sq_126d_accel_v129_signal(debt, closeadj):
    base = _mean(debt * debt, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq debt
def dl_f022_debt_level_sq_252d_accel_v130_signal(debt, closeadj):
    base = _mean(debt * debt, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq debt
def dl_f022_debt_level_sq_252d_accel_v131_signal(debt, closeadj):
    base = _mean(debt * debt, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq debt
def dl_f022_debt_level_sq_252d_accel_v132_signal(debt, closeadj):
    base = _mean(debt * debt, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq debt
def dl_f022_debt_level_sq_504d_accel_v133_signal(debt, closeadj):
    base = _mean(debt * debt, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq debt
def dl_f022_debt_level_sq_504d_accel_v134_signal(debt, closeadj):
    base = _mean(debt * debt, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq debt
def dl_f022_debt_level_sq_504d_accel_v135_signal(debt, closeadj):
    base = _mean(debt * debt, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z debt
def dl_f022_debt_level_z_21d_accel_v136_signal(debt):
    base = _z(debt, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z debt
def dl_f022_debt_level_z_21d_accel_v137_signal(debt):
    base = _z(debt, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z debt
def dl_f022_debt_level_z_21d_accel_v138_signal(debt):
    base = _z(debt, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z debt
def dl_f022_debt_level_z_63d_accel_v139_signal(debt):
    base = _z(debt, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z debt
def dl_f022_debt_level_z_63d_accel_v140_signal(debt):
    base = _z(debt, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z debt
def dl_f022_debt_level_z_63d_accel_v141_signal(debt):
    base = _z(debt, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z debt
def dl_f022_debt_level_z_126d_accel_v142_signal(debt):
    base = _z(debt, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z debt
def dl_f022_debt_level_z_126d_accel_v143_signal(debt):
    base = _z(debt, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z debt
def dl_f022_debt_level_z_126d_accel_v144_signal(debt):
    base = _z(debt, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z debt
def dl_f022_debt_level_z_252d_accel_v145_signal(debt):
    base = _z(debt, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z debt
def dl_f022_debt_level_z_252d_accel_v146_signal(debt):
    base = _z(debt, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z debt
def dl_f022_debt_level_z_252d_accel_v147_signal(debt):
    base = _z(debt, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z debt
def dl_f022_debt_level_z_504d_accel_v148_signal(debt):
    base = _z(debt, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z debt
def dl_f022_debt_level_z_504d_accel_v149_signal(debt):
    base = _z(debt, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z debt
def dl_f022_debt_level_z_504d_accel_v150_signal(debt):
    base = _z(debt, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
