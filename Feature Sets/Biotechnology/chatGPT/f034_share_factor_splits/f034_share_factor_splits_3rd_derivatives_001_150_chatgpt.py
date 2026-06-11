"""Family f034 - Share factor and split adjustments (Dilution and Share Count) | Sharadar tables: SF1,ACTIONS | fields: sharefactor, action, value, date | 3rd derivatives 001-150"""
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
def _share_factor_splits_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _share_factor_splits_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _share_factor_splits_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw sharefactor
def sfs_f034_share_factor_splits_raw_21d_accel_v001_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw sharefactor
def sfs_f034_share_factor_splits_raw_21d_accel_v002_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw sharefactor
def sfs_f034_share_factor_splits_raw_21d_accel_v003_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw sharefactor
def sfs_f034_share_factor_splits_raw_63d_accel_v004_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw sharefactor
def sfs_f034_share_factor_splits_raw_63d_accel_v005_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw sharefactor
def sfs_f034_share_factor_splits_raw_63d_accel_v006_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw sharefactor
def sfs_f034_share_factor_splits_raw_126d_accel_v007_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw sharefactor
def sfs_f034_share_factor_splits_raw_126d_accel_v008_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw sharefactor
def sfs_f034_share_factor_splits_raw_126d_accel_v009_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw sharefactor
def sfs_f034_share_factor_splits_raw_252d_accel_v010_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw sharefactor
def sfs_f034_share_factor_splits_raw_252d_accel_v011_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw sharefactor
def sfs_f034_share_factor_splits_raw_252d_accel_v012_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw sharefactor
def sfs_f034_share_factor_splits_raw_504d_accel_v013_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw sharefactor
def sfs_f034_share_factor_splits_raw_504d_accel_v014_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw sharefactor
def sfs_f034_share_factor_splits_raw_504d_accel_v015_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log sharefactor
def sfs_f034_share_factor_splits_log_21d_accel_v016_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log sharefactor
def sfs_f034_share_factor_splits_log_21d_accel_v017_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log sharefactor
def sfs_f034_share_factor_splits_log_21d_accel_v018_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log sharefactor
def sfs_f034_share_factor_splits_log_63d_accel_v019_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log sharefactor
def sfs_f034_share_factor_splits_log_63d_accel_v020_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log sharefactor
def sfs_f034_share_factor_splits_log_63d_accel_v021_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log sharefactor
def sfs_f034_share_factor_splits_log_126d_accel_v022_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log sharefactor
def sfs_f034_share_factor_splits_log_126d_accel_v023_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log sharefactor
def sfs_f034_share_factor_splits_log_126d_accel_v024_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log sharefactor
def sfs_f034_share_factor_splits_log_252d_accel_v025_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log sharefactor
def sfs_f034_share_factor_splits_log_252d_accel_v026_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log sharefactor
def sfs_f034_share_factor_splits_log_252d_accel_v027_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log sharefactor
def sfs_f034_share_factor_splits_log_504d_accel_v028_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log sharefactor
def sfs_f034_share_factor_splits_log_504d_accel_v029_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log sharefactor
def sfs_f034_share_factor_splits_log_504d_accel_v030_signal(sharefactor, closeadj):
    base = _mean(_share_factor_splits_log(sharefactor), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_21d_accel_v031_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_21d_accel_v032_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_21d_accel_v033_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_63d_accel_v034_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_63d_accel_v035_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_63d_accel_v036_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_126d_accel_v037_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_126d_accel_v038_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_126d_accel_v039_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_252d_accel_v040_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_252d_accel_v041_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_252d_accel_v042_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_504d_accel_v043_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_504d_accel_v044_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare sharefactor
def sfs_f034_share_factor_splits_pershare_504d_accel_v045_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_share_factor_splits_per_share(sharefactor, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_21d_accel_v046_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_21d_accel_v047_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_21d_accel_v048_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_63d_accel_v049_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_63d_accel_v050_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_63d_accel_v051_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_126d_accel_v052_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_126d_accel_v053_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_126d_accel_v054_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_252d_accel_v055_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_252d_accel_v056_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_252d_accel_v057_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_504d_accel_v058_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_504d_accel_v059_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_value sharefactor
def sfs_f034_share_factor_splits_per_value_504d_accel_v060_signal(sharefactor, value):
    base = _mean(_share_factor_splits_scaled(sharefactor, value), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_21d_accel_v061_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_21d_accel_v062_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_21d_accel_v063_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_63d_accel_v064_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_63d_accel_v065_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_63d_accel_v066_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_126d_accel_v067_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_126d_accel_v068_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_126d_accel_v069_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_252d_accel_v070_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_252d_accel_v071_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_252d_accel_v072_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_504d_accel_v073_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_504d_accel_v074_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets sharefactor
def sfs_f034_share_factor_splits_per_assets_504d_accel_v075_signal(sharefactor, assets):
    base = _mean(_share_factor_splits_scaled(sharefactor, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_21d_accel_v076_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_21d_accel_v077_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_21d_accel_v078_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_63d_accel_v079_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_63d_accel_v080_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_63d_accel_v081_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_126d_accel_v082_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_126d_accel_v083_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_126d_accel_v084_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_252d_accel_v085_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_252d_accel_v086_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_252d_accel_v087_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_504d_accel_v088_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_504d_accel_v089_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap sharefactor
def sfs_f034_share_factor_splits_per_marketcap_504d_accel_v090_signal(sharefactor, marketcap):
    base = _mean(_share_factor_splits_scaled(sharefactor, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std sharefactor
def sfs_f034_share_factor_splits_std_21d_accel_v091_signal(sharefactor, closeadj):
    base = _std(sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std sharefactor
def sfs_f034_share_factor_splits_std_21d_accel_v092_signal(sharefactor, closeadj):
    base = _std(sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std sharefactor
def sfs_f034_share_factor_splits_std_21d_accel_v093_signal(sharefactor, closeadj):
    base = _std(sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std sharefactor
def sfs_f034_share_factor_splits_std_63d_accel_v094_signal(sharefactor, closeadj):
    base = _std(sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std sharefactor
def sfs_f034_share_factor_splits_std_63d_accel_v095_signal(sharefactor, closeadj):
    base = _std(sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std sharefactor
def sfs_f034_share_factor_splits_std_63d_accel_v096_signal(sharefactor, closeadj):
    base = _std(sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std sharefactor
def sfs_f034_share_factor_splits_std_126d_accel_v097_signal(sharefactor, closeadj):
    base = _std(sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std sharefactor
def sfs_f034_share_factor_splits_std_126d_accel_v098_signal(sharefactor, closeadj):
    base = _std(sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std sharefactor
def sfs_f034_share_factor_splits_std_126d_accel_v099_signal(sharefactor, closeadj):
    base = _std(sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std sharefactor
def sfs_f034_share_factor_splits_std_252d_accel_v100_signal(sharefactor, closeadj):
    base = _std(sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std sharefactor
def sfs_f034_share_factor_splits_std_252d_accel_v101_signal(sharefactor, closeadj):
    base = _std(sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std sharefactor
def sfs_f034_share_factor_splits_std_252d_accel_v102_signal(sharefactor, closeadj):
    base = _std(sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std sharefactor
def sfs_f034_share_factor_splits_std_504d_accel_v103_signal(sharefactor, closeadj):
    base = _std(sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std sharefactor
def sfs_f034_share_factor_splits_std_504d_accel_v104_signal(sharefactor, closeadj):
    base = _std(sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std sharefactor
def sfs_f034_share_factor_splits_std_504d_accel_v105_signal(sharefactor, closeadj):
    base = _std(sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_21d_accel_v106_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_21d_accel_v107_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_21d_accel_v108_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_63d_accel_v109_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_63d_accel_v110_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_63d_accel_v111_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_126d_accel_v112_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_126d_accel_v113_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_126d_accel_v114_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_252d_accel_v115_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_252d_accel_v116_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_252d_accel_v117_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_504d_accel_v118_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_504d_accel_v119_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm sharefactor
def sfs_f034_share_factor_splits_ewm_504d_accel_v120_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq sharefactor
def sfs_f034_share_factor_splits_sq_21d_accel_v121_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq sharefactor
def sfs_f034_share_factor_splits_sq_21d_accel_v122_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq sharefactor
def sfs_f034_share_factor_splits_sq_21d_accel_v123_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq sharefactor
def sfs_f034_share_factor_splits_sq_63d_accel_v124_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq sharefactor
def sfs_f034_share_factor_splits_sq_63d_accel_v125_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq sharefactor
def sfs_f034_share_factor_splits_sq_63d_accel_v126_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq sharefactor
def sfs_f034_share_factor_splits_sq_126d_accel_v127_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq sharefactor
def sfs_f034_share_factor_splits_sq_126d_accel_v128_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq sharefactor
def sfs_f034_share_factor_splits_sq_126d_accel_v129_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq sharefactor
def sfs_f034_share_factor_splits_sq_252d_accel_v130_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq sharefactor
def sfs_f034_share_factor_splits_sq_252d_accel_v131_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq sharefactor
def sfs_f034_share_factor_splits_sq_252d_accel_v132_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq sharefactor
def sfs_f034_share_factor_splits_sq_504d_accel_v133_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq sharefactor
def sfs_f034_share_factor_splits_sq_504d_accel_v134_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq sharefactor
def sfs_f034_share_factor_splits_sq_504d_accel_v135_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z sharefactor
def sfs_f034_share_factor_splits_z_21d_accel_v136_signal(sharefactor):
    base = _z(sharefactor, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z sharefactor
def sfs_f034_share_factor_splits_z_21d_accel_v137_signal(sharefactor):
    base = _z(sharefactor, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z sharefactor
def sfs_f034_share_factor_splits_z_21d_accel_v138_signal(sharefactor):
    base = _z(sharefactor, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z sharefactor
def sfs_f034_share_factor_splits_z_63d_accel_v139_signal(sharefactor):
    base = _z(sharefactor, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z sharefactor
def sfs_f034_share_factor_splits_z_63d_accel_v140_signal(sharefactor):
    base = _z(sharefactor, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z sharefactor
def sfs_f034_share_factor_splits_z_63d_accel_v141_signal(sharefactor):
    base = _z(sharefactor, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z sharefactor
def sfs_f034_share_factor_splits_z_126d_accel_v142_signal(sharefactor):
    base = _z(sharefactor, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z sharefactor
def sfs_f034_share_factor_splits_z_126d_accel_v143_signal(sharefactor):
    base = _z(sharefactor, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z sharefactor
def sfs_f034_share_factor_splits_z_126d_accel_v144_signal(sharefactor):
    base = _z(sharefactor, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z sharefactor
def sfs_f034_share_factor_splits_z_252d_accel_v145_signal(sharefactor):
    base = _z(sharefactor, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z sharefactor
def sfs_f034_share_factor_splits_z_252d_accel_v146_signal(sharefactor):
    base = _z(sharefactor, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z sharefactor
def sfs_f034_share_factor_splits_z_252d_accel_v147_signal(sharefactor):
    base = _z(sharefactor, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z sharefactor
def sfs_f034_share_factor_splits_z_504d_accel_v148_signal(sharefactor):
    base = _z(sharefactor, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z sharefactor
def sfs_f034_share_factor_splits_z_504d_accel_v149_signal(sharefactor):
    base = _z(sharefactor, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z sharefactor
def sfs_f034_share_factor_splits_z_504d_accel_v150_signal(sharefactor):
    base = _z(sharefactor, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
