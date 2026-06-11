"""Family f67 - Working-capital change as cash drag  (K_WorkingCapital) | 3rd derivatives 001-150"""
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
def _working_capital_change_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _working_capital_change_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _working_capital_change_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw workingcapital
def wcc_f67_working_capital_change_raw_21d_accel_v001_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw workingcapital
def wcc_f67_working_capital_change_raw_21d_accel_v002_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw workingcapital
def wcc_f67_working_capital_change_raw_21d_accel_v003_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw workingcapital
def wcc_f67_working_capital_change_raw_63d_accel_v004_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw workingcapital
def wcc_f67_working_capital_change_raw_63d_accel_v005_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw workingcapital
def wcc_f67_working_capital_change_raw_63d_accel_v006_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw workingcapital
def wcc_f67_working_capital_change_raw_126d_accel_v007_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw workingcapital
def wcc_f67_working_capital_change_raw_126d_accel_v008_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw workingcapital
def wcc_f67_working_capital_change_raw_126d_accel_v009_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw workingcapital
def wcc_f67_working_capital_change_raw_252d_accel_v010_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw workingcapital
def wcc_f67_working_capital_change_raw_252d_accel_v011_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw workingcapital
def wcc_f67_working_capital_change_raw_252d_accel_v012_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw workingcapital
def wcc_f67_working_capital_change_raw_504d_accel_v013_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw workingcapital
def wcc_f67_working_capital_change_raw_504d_accel_v014_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw workingcapital
def wcc_f67_working_capital_change_raw_504d_accel_v015_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log workingcapital
def wcc_f67_working_capital_change_log_21d_accel_v016_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log workingcapital
def wcc_f67_working_capital_change_log_21d_accel_v017_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log workingcapital
def wcc_f67_working_capital_change_log_21d_accel_v018_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log workingcapital
def wcc_f67_working_capital_change_log_63d_accel_v019_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log workingcapital
def wcc_f67_working_capital_change_log_63d_accel_v020_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log workingcapital
def wcc_f67_working_capital_change_log_63d_accel_v021_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log workingcapital
def wcc_f67_working_capital_change_log_126d_accel_v022_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log workingcapital
def wcc_f67_working_capital_change_log_126d_accel_v023_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log workingcapital
def wcc_f67_working_capital_change_log_126d_accel_v024_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log workingcapital
def wcc_f67_working_capital_change_log_252d_accel_v025_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log workingcapital
def wcc_f67_working_capital_change_log_252d_accel_v026_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log workingcapital
def wcc_f67_working_capital_change_log_252d_accel_v027_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log workingcapital
def wcc_f67_working_capital_change_log_504d_accel_v028_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log workingcapital
def wcc_f67_working_capital_change_log_504d_accel_v029_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log workingcapital
def wcc_f67_working_capital_change_log_504d_accel_v030_signal(workingcapital, closeadj):
    base = _mean(_working_capital_change_log(workingcapital), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare workingcapital
def wcc_f67_working_capital_change_pershare_21d_accel_v031_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare workingcapital
def wcc_f67_working_capital_change_pershare_21d_accel_v032_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare workingcapital
def wcc_f67_working_capital_change_pershare_21d_accel_v033_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare workingcapital
def wcc_f67_working_capital_change_pershare_63d_accel_v034_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare workingcapital
def wcc_f67_working_capital_change_pershare_63d_accel_v035_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare workingcapital
def wcc_f67_working_capital_change_pershare_63d_accel_v036_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare workingcapital
def wcc_f67_working_capital_change_pershare_126d_accel_v037_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare workingcapital
def wcc_f67_working_capital_change_pershare_126d_accel_v038_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare workingcapital
def wcc_f67_working_capital_change_pershare_126d_accel_v039_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare workingcapital
def wcc_f67_working_capital_change_pershare_252d_accel_v040_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare workingcapital
def wcc_f67_working_capital_change_pershare_252d_accel_v041_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare workingcapital
def wcc_f67_working_capital_change_pershare_252d_accel_v042_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare workingcapital
def wcc_f67_working_capital_change_pershare_504d_accel_v043_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare workingcapital
def wcc_f67_working_capital_change_pershare_504d_accel_v044_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare workingcapital
def wcc_f67_working_capital_change_pershare_504d_accel_v045_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_change_per_share(workingcapital, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_21d_accel_v046_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_21d_accel_v047_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_21d_accel_v048_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_63d_accel_v049_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_63d_accel_v050_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_63d_accel_v051_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_126d_accel_v052_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_126d_accel_v053_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_126d_accel_v054_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_252d_accel_v055_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_252d_accel_v056_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_252d_accel_v057_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_504d_accel_v058_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_504d_accel_v059_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets workingcapital
def wcc_f67_working_capital_change_per_assets_504d_accel_v060_signal(workingcapital, assets):
    base = _mean(_working_capital_change_scaled(workingcapital, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_21d_accel_v061_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_21d_accel_v062_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_21d_accel_v063_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_63d_accel_v064_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_63d_accel_v065_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_63d_accel_v066_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_126d_accel_v067_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_126d_accel_v068_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_126d_accel_v069_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_252d_accel_v070_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_252d_accel_v071_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_252d_accel_v072_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_504d_accel_v073_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_504d_accel_v074_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap workingcapital
def wcc_f67_working_capital_change_per_marketcap_504d_accel_v075_signal(workingcapital, marketcap):
    base = _mean(_working_capital_change_scaled(workingcapital, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_21d_accel_v076_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_21d_accel_v077_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_21d_accel_v078_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_63d_accel_v079_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_63d_accel_v080_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_63d_accel_v081_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_126d_accel_v082_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_126d_accel_v083_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_126d_accel_v084_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_252d_accel_v085_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_252d_accel_v086_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_252d_accel_v087_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_504d_accel_v088_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_504d_accel_v089_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity workingcapital
def wcc_f67_working_capital_change_per_equity_504d_accel_v090_signal(workingcapital, equity):
    base = _mean(_working_capital_change_scaled(workingcapital, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std workingcapital
def wcc_f67_working_capital_change_std_21d_accel_v091_signal(workingcapital, closeadj):
    base = _std(workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std workingcapital
def wcc_f67_working_capital_change_std_21d_accel_v092_signal(workingcapital, closeadj):
    base = _std(workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std workingcapital
def wcc_f67_working_capital_change_std_21d_accel_v093_signal(workingcapital, closeadj):
    base = _std(workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std workingcapital
def wcc_f67_working_capital_change_std_63d_accel_v094_signal(workingcapital, closeadj):
    base = _std(workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std workingcapital
def wcc_f67_working_capital_change_std_63d_accel_v095_signal(workingcapital, closeadj):
    base = _std(workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std workingcapital
def wcc_f67_working_capital_change_std_63d_accel_v096_signal(workingcapital, closeadj):
    base = _std(workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std workingcapital
def wcc_f67_working_capital_change_std_126d_accel_v097_signal(workingcapital, closeadj):
    base = _std(workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std workingcapital
def wcc_f67_working_capital_change_std_126d_accel_v098_signal(workingcapital, closeadj):
    base = _std(workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std workingcapital
def wcc_f67_working_capital_change_std_126d_accel_v099_signal(workingcapital, closeadj):
    base = _std(workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std workingcapital
def wcc_f67_working_capital_change_std_252d_accel_v100_signal(workingcapital, closeadj):
    base = _std(workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std workingcapital
def wcc_f67_working_capital_change_std_252d_accel_v101_signal(workingcapital, closeadj):
    base = _std(workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std workingcapital
def wcc_f67_working_capital_change_std_252d_accel_v102_signal(workingcapital, closeadj):
    base = _std(workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std workingcapital
def wcc_f67_working_capital_change_std_504d_accel_v103_signal(workingcapital, closeadj):
    base = _std(workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std workingcapital
def wcc_f67_working_capital_change_std_504d_accel_v104_signal(workingcapital, closeadj):
    base = _std(workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std workingcapital
def wcc_f67_working_capital_change_std_504d_accel_v105_signal(workingcapital, closeadj):
    base = _std(workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm workingcapital
def wcc_f67_working_capital_change_ewm_21d_accel_v106_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm workingcapital
def wcc_f67_working_capital_change_ewm_21d_accel_v107_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm workingcapital
def wcc_f67_working_capital_change_ewm_21d_accel_v108_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm workingcapital
def wcc_f67_working_capital_change_ewm_63d_accel_v109_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm workingcapital
def wcc_f67_working_capital_change_ewm_63d_accel_v110_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm workingcapital
def wcc_f67_working_capital_change_ewm_63d_accel_v111_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm workingcapital
def wcc_f67_working_capital_change_ewm_126d_accel_v112_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm workingcapital
def wcc_f67_working_capital_change_ewm_126d_accel_v113_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm workingcapital
def wcc_f67_working_capital_change_ewm_126d_accel_v114_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm workingcapital
def wcc_f67_working_capital_change_ewm_252d_accel_v115_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm workingcapital
def wcc_f67_working_capital_change_ewm_252d_accel_v116_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm workingcapital
def wcc_f67_working_capital_change_ewm_252d_accel_v117_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm workingcapital
def wcc_f67_working_capital_change_ewm_504d_accel_v118_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm workingcapital
def wcc_f67_working_capital_change_ewm_504d_accel_v119_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm workingcapital
def wcc_f67_working_capital_change_ewm_504d_accel_v120_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq workingcapital
def wcc_f67_working_capital_change_sq_21d_accel_v121_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq workingcapital
def wcc_f67_working_capital_change_sq_21d_accel_v122_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq workingcapital
def wcc_f67_working_capital_change_sq_21d_accel_v123_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq workingcapital
def wcc_f67_working_capital_change_sq_63d_accel_v124_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq workingcapital
def wcc_f67_working_capital_change_sq_63d_accel_v125_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq workingcapital
def wcc_f67_working_capital_change_sq_63d_accel_v126_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq workingcapital
def wcc_f67_working_capital_change_sq_126d_accel_v127_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq workingcapital
def wcc_f67_working_capital_change_sq_126d_accel_v128_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq workingcapital
def wcc_f67_working_capital_change_sq_126d_accel_v129_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq workingcapital
def wcc_f67_working_capital_change_sq_252d_accel_v130_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq workingcapital
def wcc_f67_working_capital_change_sq_252d_accel_v131_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq workingcapital
def wcc_f67_working_capital_change_sq_252d_accel_v132_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq workingcapital
def wcc_f67_working_capital_change_sq_504d_accel_v133_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq workingcapital
def wcc_f67_working_capital_change_sq_504d_accel_v134_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq workingcapital
def wcc_f67_working_capital_change_sq_504d_accel_v135_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z workingcapital
def wcc_f67_working_capital_change_z_21d_accel_v136_signal(workingcapital):
    base = _z(workingcapital, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z workingcapital
def wcc_f67_working_capital_change_z_21d_accel_v137_signal(workingcapital):
    base = _z(workingcapital, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z workingcapital
def wcc_f67_working_capital_change_z_21d_accel_v138_signal(workingcapital):
    base = _z(workingcapital, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z workingcapital
def wcc_f67_working_capital_change_z_63d_accel_v139_signal(workingcapital):
    base = _z(workingcapital, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z workingcapital
def wcc_f67_working_capital_change_z_63d_accel_v140_signal(workingcapital):
    base = _z(workingcapital, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z workingcapital
def wcc_f67_working_capital_change_z_63d_accel_v141_signal(workingcapital):
    base = _z(workingcapital, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z workingcapital
def wcc_f67_working_capital_change_z_126d_accel_v142_signal(workingcapital):
    base = _z(workingcapital, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z workingcapital
def wcc_f67_working_capital_change_z_126d_accel_v143_signal(workingcapital):
    base = _z(workingcapital, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z workingcapital
def wcc_f67_working_capital_change_z_126d_accel_v144_signal(workingcapital):
    base = _z(workingcapital, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z workingcapital
def wcc_f67_working_capital_change_z_252d_accel_v145_signal(workingcapital):
    base = _z(workingcapital, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z workingcapital
def wcc_f67_working_capital_change_z_252d_accel_v146_signal(workingcapital):
    base = _z(workingcapital, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z workingcapital
def wcc_f67_working_capital_change_z_252d_accel_v147_signal(workingcapital):
    base = _z(workingcapital, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z workingcapital
def wcc_f67_working_capital_change_z_504d_accel_v148_signal(workingcapital):
    base = _z(workingcapital, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z workingcapital
def wcc_f67_working_capital_change_z_504d_accel_v149_signal(workingcapital):
    base = _z(workingcapital, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z workingcapital
def wcc_f67_working_capital_change_z_504d_accel_v150_signal(workingcapital):
    base = _z(workingcapital, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
