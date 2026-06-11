"""Family f18 - R&D share of total burn  (C_RnD_Innovation) | 3rd derivatives 001-150"""
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
def _rnd_share_of_burn_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _rnd_share_of_burn_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _rnd_share_of_burn_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw rnd
def rsb_f18_rnd_share_of_burn_raw_21d_accel_v001_signal(rnd, closeadj):
    base = _mean(rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw rnd
def rsb_f18_rnd_share_of_burn_raw_21d_accel_v002_signal(rnd, closeadj):
    base = _mean(rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw rnd
def rsb_f18_rnd_share_of_burn_raw_21d_accel_v003_signal(rnd, closeadj):
    base = _mean(rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw rnd
def rsb_f18_rnd_share_of_burn_raw_63d_accel_v004_signal(rnd, closeadj):
    base = _mean(rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw rnd
def rsb_f18_rnd_share_of_burn_raw_63d_accel_v005_signal(rnd, closeadj):
    base = _mean(rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw rnd
def rsb_f18_rnd_share_of_burn_raw_63d_accel_v006_signal(rnd, closeadj):
    base = _mean(rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw rnd
def rsb_f18_rnd_share_of_burn_raw_126d_accel_v007_signal(rnd, closeadj):
    base = _mean(rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw rnd
def rsb_f18_rnd_share_of_burn_raw_126d_accel_v008_signal(rnd, closeadj):
    base = _mean(rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw rnd
def rsb_f18_rnd_share_of_burn_raw_126d_accel_v009_signal(rnd, closeadj):
    base = _mean(rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw rnd
def rsb_f18_rnd_share_of_burn_raw_252d_accel_v010_signal(rnd, closeadj):
    base = _mean(rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw rnd
def rsb_f18_rnd_share_of_burn_raw_252d_accel_v011_signal(rnd, closeadj):
    base = _mean(rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw rnd
def rsb_f18_rnd_share_of_burn_raw_252d_accel_v012_signal(rnd, closeadj):
    base = _mean(rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw rnd
def rsb_f18_rnd_share_of_burn_raw_504d_accel_v013_signal(rnd, closeadj):
    base = _mean(rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw rnd
def rsb_f18_rnd_share_of_burn_raw_504d_accel_v014_signal(rnd, closeadj):
    base = _mean(rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw rnd
def rsb_f18_rnd_share_of_burn_raw_504d_accel_v015_signal(rnd, closeadj):
    base = _mean(rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log rnd
def rsb_f18_rnd_share_of_burn_log_21d_accel_v016_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log rnd
def rsb_f18_rnd_share_of_burn_log_21d_accel_v017_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log rnd
def rsb_f18_rnd_share_of_burn_log_21d_accel_v018_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log rnd
def rsb_f18_rnd_share_of_burn_log_63d_accel_v019_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log rnd
def rsb_f18_rnd_share_of_burn_log_63d_accel_v020_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log rnd
def rsb_f18_rnd_share_of_burn_log_63d_accel_v021_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log rnd
def rsb_f18_rnd_share_of_burn_log_126d_accel_v022_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log rnd
def rsb_f18_rnd_share_of_burn_log_126d_accel_v023_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log rnd
def rsb_f18_rnd_share_of_burn_log_126d_accel_v024_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log rnd
def rsb_f18_rnd_share_of_burn_log_252d_accel_v025_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log rnd
def rsb_f18_rnd_share_of_burn_log_252d_accel_v026_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log rnd
def rsb_f18_rnd_share_of_burn_log_252d_accel_v027_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log rnd
def rsb_f18_rnd_share_of_burn_log_504d_accel_v028_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log rnd
def rsb_f18_rnd_share_of_burn_log_504d_accel_v029_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log rnd
def rsb_f18_rnd_share_of_burn_log_504d_accel_v030_signal(rnd, closeadj):
    base = _mean(_rnd_share_of_burn_log(rnd), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_21d_accel_v031_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_21d_accel_v032_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_21d_accel_v033_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_63d_accel_v034_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_63d_accel_v035_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_63d_accel_v036_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_126d_accel_v037_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_126d_accel_v038_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_126d_accel_v039_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_252d_accel_v040_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_252d_accel_v041_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_252d_accel_v042_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_504d_accel_v043_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_504d_accel_v044_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare rnd
def rsb_f18_rnd_share_of_burn_pershare_504d_accel_v045_signal(rnd, sharesbas, closeadj):
    base = _mean(_rnd_share_of_burn_per_share(rnd, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_21d_accel_v046_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_21d_accel_v047_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_21d_accel_v048_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_63d_accel_v049_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_63d_accel_v050_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_63d_accel_v051_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_126d_accel_v052_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_126d_accel_v053_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_126d_accel_v054_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_252d_accel_v055_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_252d_accel_v056_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_252d_accel_v057_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_504d_accel_v058_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_504d_accel_v059_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets rnd
def rsb_f18_rnd_share_of_burn_per_assets_504d_accel_v060_signal(rnd, assets):
    base = _mean(_rnd_share_of_burn_scaled(rnd, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_21d_accel_v061_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_21d_accel_v062_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_21d_accel_v063_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_63d_accel_v064_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_63d_accel_v065_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_63d_accel_v066_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_126d_accel_v067_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_126d_accel_v068_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_126d_accel_v069_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_252d_accel_v070_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_252d_accel_v071_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_252d_accel_v072_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_504d_accel_v073_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_504d_accel_v074_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap rnd
def rsb_f18_rnd_share_of_burn_per_marketcap_504d_accel_v075_signal(rnd, marketcap):
    base = _mean(_rnd_share_of_burn_scaled(rnd, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_21d_accel_v076_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_21d_accel_v077_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_21d_accel_v078_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_63d_accel_v079_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_63d_accel_v080_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_63d_accel_v081_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_126d_accel_v082_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_126d_accel_v083_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_126d_accel_v084_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_252d_accel_v085_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_252d_accel_v086_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_252d_accel_v087_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_504d_accel_v088_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_504d_accel_v089_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity rnd
def rsb_f18_rnd_share_of_burn_per_equity_504d_accel_v090_signal(rnd, equity):
    base = _mean(_rnd_share_of_burn_scaled(rnd, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std rnd
def rsb_f18_rnd_share_of_burn_std_21d_accel_v091_signal(rnd, closeadj):
    base = _std(rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std rnd
def rsb_f18_rnd_share_of_burn_std_21d_accel_v092_signal(rnd, closeadj):
    base = _std(rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std rnd
def rsb_f18_rnd_share_of_burn_std_21d_accel_v093_signal(rnd, closeadj):
    base = _std(rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std rnd
def rsb_f18_rnd_share_of_burn_std_63d_accel_v094_signal(rnd, closeadj):
    base = _std(rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std rnd
def rsb_f18_rnd_share_of_burn_std_63d_accel_v095_signal(rnd, closeadj):
    base = _std(rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std rnd
def rsb_f18_rnd_share_of_burn_std_63d_accel_v096_signal(rnd, closeadj):
    base = _std(rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std rnd
def rsb_f18_rnd_share_of_burn_std_126d_accel_v097_signal(rnd, closeadj):
    base = _std(rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std rnd
def rsb_f18_rnd_share_of_burn_std_126d_accel_v098_signal(rnd, closeadj):
    base = _std(rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std rnd
def rsb_f18_rnd_share_of_burn_std_126d_accel_v099_signal(rnd, closeadj):
    base = _std(rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std rnd
def rsb_f18_rnd_share_of_burn_std_252d_accel_v100_signal(rnd, closeadj):
    base = _std(rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std rnd
def rsb_f18_rnd_share_of_burn_std_252d_accel_v101_signal(rnd, closeadj):
    base = _std(rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std rnd
def rsb_f18_rnd_share_of_burn_std_252d_accel_v102_signal(rnd, closeadj):
    base = _std(rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std rnd
def rsb_f18_rnd_share_of_burn_std_504d_accel_v103_signal(rnd, closeadj):
    base = _std(rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std rnd
def rsb_f18_rnd_share_of_burn_std_504d_accel_v104_signal(rnd, closeadj):
    base = _std(rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std rnd
def rsb_f18_rnd_share_of_burn_std_504d_accel_v105_signal(rnd, closeadj):
    base = _std(rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_21d_accel_v106_signal(rnd, closeadj):
    base = rnd.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_21d_accel_v107_signal(rnd, closeadj):
    base = rnd.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_21d_accel_v108_signal(rnd, closeadj):
    base = rnd.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_63d_accel_v109_signal(rnd, closeadj):
    base = rnd.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_63d_accel_v110_signal(rnd, closeadj):
    base = rnd.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_63d_accel_v111_signal(rnd, closeadj):
    base = rnd.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_126d_accel_v112_signal(rnd, closeadj):
    base = rnd.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_126d_accel_v113_signal(rnd, closeadj):
    base = rnd.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_126d_accel_v114_signal(rnd, closeadj):
    base = rnd.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_252d_accel_v115_signal(rnd, closeadj):
    base = rnd.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_252d_accel_v116_signal(rnd, closeadj):
    base = rnd.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_252d_accel_v117_signal(rnd, closeadj):
    base = rnd.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_504d_accel_v118_signal(rnd, closeadj):
    base = rnd.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_504d_accel_v119_signal(rnd, closeadj):
    base = rnd.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm rnd
def rsb_f18_rnd_share_of_burn_ewm_504d_accel_v120_signal(rnd, closeadj):
    base = rnd.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq rnd
def rsb_f18_rnd_share_of_burn_sq_21d_accel_v121_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq rnd
def rsb_f18_rnd_share_of_burn_sq_21d_accel_v122_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq rnd
def rsb_f18_rnd_share_of_burn_sq_21d_accel_v123_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq rnd
def rsb_f18_rnd_share_of_burn_sq_63d_accel_v124_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq rnd
def rsb_f18_rnd_share_of_burn_sq_63d_accel_v125_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq rnd
def rsb_f18_rnd_share_of_burn_sq_63d_accel_v126_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq rnd
def rsb_f18_rnd_share_of_burn_sq_126d_accel_v127_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq rnd
def rsb_f18_rnd_share_of_burn_sq_126d_accel_v128_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq rnd
def rsb_f18_rnd_share_of_burn_sq_126d_accel_v129_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq rnd
def rsb_f18_rnd_share_of_burn_sq_252d_accel_v130_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq rnd
def rsb_f18_rnd_share_of_burn_sq_252d_accel_v131_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq rnd
def rsb_f18_rnd_share_of_burn_sq_252d_accel_v132_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq rnd
def rsb_f18_rnd_share_of_burn_sq_504d_accel_v133_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq rnd
def rsb_f18_rnd_share_of_burn_sq_504d_accel_v134_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq rnd
def rsb_f18_rnd_share_of_burn_sq_504d_accel_v135_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z rnd
def rsb_f18_rnd_share_of_burn_z_21d_accel_v136_signal(rnd):
    base = _z(rnd, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z rnd
def rsb_f18_rnd_share_of_burn_z_21d_accel_v137_signal(rnd):
    base = _z(rnd, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z rnd
def rsb_f18_rnd_share_of_burn_z_21d_accel_v138_signal(rnd):
    base = _z(rnd, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z rnd
def rsb_f18_rnd_share_of_burn_z_63d_accel_v139_signal(rnd):
    base = _z(rnd, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z rnd
def rsb_f18_rnd_share_of_burn_z_63d_accel_v140_signal(rnd):
    base = _z(rnd, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z rnd
def rsb_f18_rnd_share_of_burn_z_63d_accel_v141_signal(rnd):
    base = _z(rnd, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z rnd
def rsb_f18_rnd_share_of_burn_z_126d_accel_v142_signal(rnd):
    base = _z(rnd, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z rnd
def rsb_f18_rnd_share_of_burn_z_126d_accel_v143_signal(rnd):
    base = _z(rnd, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z rnd
def rsb_f18_rnd_share_of_burn_z_126d_accel_v144_signal(rnd):
    base = _z(rnd, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z rnd
def rsb_f18_rnd_share_of_burn_z_252d_accel_v145_signal(rnd):
    base = _z(rnd, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z rnd
def rsb_f18_rnd_share_of_burn_z_252d_accel_v146_signal(rnd):
    base = _z(rnd, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z rnd
def rsb_f18_rnd_share_of_burn_z_252d_accel_v147_signal(rnd):
    base = _z(rnd, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z rnd
def rsb_f18_rnd_share_of_burn_z_504d_accel_v148_signal(rnd):
    base = _z(rnd, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z rnd
def rsb_f18_rnd_share_of_burn_z_504d_accel_v149_signal(rnd):
    base = _z(rnd, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z rnd
def rsb_f18_rnd_share_of_burn_z_504d_accel_v150_signal(rnd):
    base = _z(rnd, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
