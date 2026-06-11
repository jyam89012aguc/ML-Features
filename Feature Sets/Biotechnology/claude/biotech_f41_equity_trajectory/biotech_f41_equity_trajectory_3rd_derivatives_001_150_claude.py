"""Family f41 - Book value & equity trajectory  (F_BalanceSheet) | 3rd derivatives 001-150"""
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
def _equity_trajectory_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _equity_trajectory_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _equity_trajectory_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw equity
def eqt_f41_equity_trajectory_raw_21d_accel_v001_signal(equity, closeadj):
    base = _mean(equity, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw equity
def eqt_f41_equity_trajectory_raw_21d_accel_v002_signal(equity, closeadj):
    base = _mean(equity, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw equity
def eqt_f41_equity_trajectory_raw_21d_accel_v003_signal(equity, closeadj):
    base = _mean(equity, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw equity
def eqt_f41_equity_trajectory_raw_63d_accel_v004_signal(equity, closeadj):
    base = _mean(equity, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw equity
def eqt_f41_equity_trajectory_raw_63d_accel_v005_signal(equity, closeadj):
    base = _mean(equity, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw equity
def eqt_f41_equity_trajectory_raw_63d_accel_v006_signal(equity, closeadj):
    base = _mean(equity, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw equity
def eqt_f41_equity_trajectory_raw_126d_accel_v007_signal(equity, closeadj):
    base = _mean(equity, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw equity
def eqt_f41_equity_trajectory_raw_126d_accel_v008_signal(equity, closeadj):
    base = _mean(equity, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw equity
def eqt_f41_equity_trajectory_raw_126d_accel_v009_signal(equity, closeadj):
    base = _mean(equity, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw equity
def eqt_f41_equity_trajectory_raw_252d_accel_v010_signal(equity, closeadj):
    base = _mean(equity, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw equity
def eqt_f41_equity_trajectory_raw_252d_accel_v011_signal(equity, closeadj):
    base = _mean(equity, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw equity
def eqt_f41_equity_trajectory_raw_252d_accel_v012_signal(equity, closeadj):
    base = _mean(equity, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw equity
def eqt_f41_equity_trajectory_raw_504d_accel_v013_signal(equity, closeadj):
    base = _mean(equity, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw equity
def eqt_f41_equity_trajectory_raw_504d_accel_v014_signal(equity, closeadj):
    base = _mean(equity, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw equity
def eqt_f41_equity_trajectory_raw_504d_accel_v015_signal(equity, closeadj):
    base = _mean(equity, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log equity
def eqt_f41_equity_trajectory_log_21d_accel_v016_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log equity
def eqt_f41_equity_trajectory_log_21d_accel_v017_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log equity
def eqt_f41_equity_trajectory_log_21d_accel_v018_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log equity
def eqt_f41_equity_trajectory_log_63d_accel_v019_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log equity
def eqt_f41_equity_trajectory_log_63d_accel_v020_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log equity
def eqt_f41_equity_trajectory_log_63d_accel_v021_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log equity
def eqt_f41_equity_trajectory_log_126d_accel_v022_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log equity
def eqt_f41_equity_trajectory_log_126d_accel_v023_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log equity
def eqt_f41_equity_trajectory_log_126d_accel_v024_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log equity
def eqt_f41_equity_trajectory_log_252d_accel_v025_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log equity
def eqt_f41_equity_trajectory_log_252d_accel_v026_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log equity
def eqt_f41_equity_trajectory_log_252d_accel_v027_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log equity
def eqt_f41_equity_trajectory_log_504d_accel_v028_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log equity
def eqt_f41_equity_trajectory_log_504d_accel_v029_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log equity
def eqt_f41_equity_trajectory_log_504d_accel_v030_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare equity
def eqt_f41_equity_trajectory_pershare_21d_accel_v031_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare equity
def eqt_f41_equity_trajectory_pershare_21d_accel_v032_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare equity
def eqt_f41_equity_trajectory_pershare_21d_accel_v033_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare equity
def eqt_f41_equity_trajectory_pershare_63d_accel_v034_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare equity
def eqt_f41_equity_trajectory_pershare_63d_accel_v035_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare equity
def eqt_f41_equity_trajectory_pershare_63d_accel_v036_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare equity
def eqt_f41_equity_trajectory_pershare_126d_accel_v037_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare equity
def eqt_f41_equity_trajectory_pershare_126d_accel_v038_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare equity
def eqt_f41_equity_trajectory_pershare_126d_accel_v039_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare equity
def eqt_f41_equity_trajectory_pershare_252d_accel_v040_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare equity
def eqt_f41_equity_trajectory_pershare_252d_accel_v041_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare equity
def eqt_f41_equity_trajectory_pershare_252d_accel_v042_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare equity
def eqt_f41_equity_trajectory_pershare_504d_accel_v043_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare equity
def eqt_f41_equity_trajectory_pershare_504d_accel_v044_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare equity
def eqt_f41_equity_trajectory_pershare_504d_accel_v045_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets equity
def eqt_f41_equity_trajectory_per_assets_21d_accel_v046_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets equity
def eqt_f41_equity_trajectory_per_assets_21d_accel_v047_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets equity
def eqt_f41_equity_trajectory_per_assets_21d_accel_v048_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets equity
def eqt_f41_equity_trajectory_per_assets_63d_accel_v049_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets equity
def eqt_f41_equity_trajectory_per_assets_63d_accel_v050_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets equity
def eqt_f41_equity_trajectory_per_assets_63d_accel_v051_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets equity
def eqt_f41_equity_trajectory_per_assets_126d_accel_v052_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets equity
def eqt_f41_equity_trajectory_per_assets_126d_accel_v053_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets equity
def eqt_f41_equity_trajectory_per_assets_126d_accel_v054_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets equity
def eqt_f41_equity_trajectory_per_assets_252d_accel_v055_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets equity
def eqt_f41_equity_trajectory_per_assets_252d_accel_v056_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets equity
def eqt_f41_equity_trajectory_per_assets_252d_accel_v057_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets equity
def eqt_f41_equity_trajectory_per_assets_504d_accel_v058_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets equity
def eqt_f41_equity_trajectory_per_assets_504d_accel_v059_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets equity
def eqt_f41_equity_trajectory_per_assets_504d_accel_v060_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_21d_accel_v061_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_21d_accel_v062_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_21d_accel_v063_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_63d_accel_v064_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_63d_accel_v065_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_63d_accel_v066_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_126d_accel_v067_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_126d_accel_v068_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_126d_accel_v069_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_252d_accel_v070_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_252d_accel_v071_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_252d_accel_v072_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_504d_accel_v073_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_504d_accel_v074_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap equity
def eqt_f41_equity_trajectory_per_marketcap_504d_accel_v075_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity equity
def eqt_f41_equity_trajectory_per_equity_21d_accel_v076_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity equity
def eqt_f41_equity_trajectory_per_equity_21d_accel_v077_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity equity
def eqt_f41_equity_trajectory_per_equity_21d_accel_v078_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity equity
def eqt_f41_equity_trajectory_per_equity_63d_accel_v079_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity equity
def eqt_f41_equity_trajectory_per_equity_63d_accel_v080_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity equity
def eqt_f41_equity_trajectory_per_equity_63d_accel_v081_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity equity
def eqt_f41_equity_trajectory_per_equity_126d_accel_v082_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity equity
def eqt_f41_equity_trajectory_per_equity_126d_accel_v083_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity equity
def eqt_f41_equity_trajectory_per_equity_126d_accel_v084_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity equity
def eqt_f41_equity_trajectory_per_equity_252d_accel_v085_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity equity
def eqt_f41_equity_trajectory_per_equity_252d_accel_v086_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity equity
def eqt_f41_equity_trajectory_per_equity_252d_accel_v087_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity equity
def eqt_f41_equity_trajectory_per_equity_504d_accel_v088_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity equity
def eqt_f41_equity_trajectory_per_equity_504d_accel_v089_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity equity
def eqt_f41_equity_trajectory_per_equity_504d_accel_v090_signal(equity):
    base = _mean(_equity_trajectory_scaled(equity, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std equity
def eqt_f41_equity_trajectory_std_21d_accel_v091_signal(equity, closeadj):
    base = _std(equity, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std equity
def eqt_f41_equity_trajectory_std_21d_accel_v092_signal(equity, closeadj):
    base = _std(equity, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std equity
def eqt_f41_equity_trajectory_std_21d_accel_v093_signal(equity, closeadj):
    base = _std(equity, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std equity
def eqt_f41_equity_trajectory_std_63d_accel_v094_signal(equity, closeadj):
    base = _std(equity, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std equity
def eqt_f41_equity_trajectory_std_63d_accel_v095_signal(equity, closeadj):
    base = _std(equity, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std equity
def eqt_f41_equity_trajectory_std_63d_accel_v096_signal(equity, closeadj):
    base = _std(equity, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std equity
def eqt_f41_equity_trajectory_std_126d_accel_v097_signal(equity, closeadj):
    base = _std(equity, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std equity
def eqt_f41_equity_trajectory_std_126d_accel_v098_signal(equity, closeadj):
    base = _std(equity, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std equity
def eqt_f41_equity_trajectory_std_126d_accel_v099_signal(equity, closeadj):
    base = _std(equity, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std equity
def eqt_f41_equity_trajectory_std_252d_accel_v100_signal(equity, closeadj):
    base = _std(equity, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std equity
def eqt_f41_equity_trajectory_std_252d_accel_v101_signal(equity, closeadj):
    base = _std(equity, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std equity
def eqt_f41_equity_trajectory_std_252d_accel_v102_signal(equity, closeadj):
    base = _std(equity, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std equity
def eqt_f41_equity_trajectory_std_504d_accel_v103_signal(equity, closeadj):
    base = _std(equity, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std equity
def eqt_f41_equity_trajectory_std_504d_accel_v104_signal(equity, closeadj):
    base = _std(equity, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std equity
def eqt_f41_equity_trajectory_std_504d_accel_v105_signal(equity, closeadj):
    base = _std(equity, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm equity
def eqt_f41_equity_trajectory_ewm_21d_accel_v106_signal(equity, closeadj):
    base = equity.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm equity
def eqt_f41_equity_trajectory_ewm_21d_accel_v107_signal(equity, closeadj):
    base = equity.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm equity
def eqt_f41_equity_trajectory_ewm_21d_accel_v108_signal(equity, closeadj):
    base = equity.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm equity
def eqt_f41_equity_trajectory_ewm_63d_accel_v109_signal(equity, closeadj):
    base = equity.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm equity
def eqt_f41_equity_trajectory_ewm_63d_accel_v110_signal(equity, closeadj):
    base = equity.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm equity
def eqt_f41_equity_trajectory_ewm_63d_accel_v111_signal(equity, closeadj):
    base = equity.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm equity
def eqt_f41_equity_trajectory_ewm_126d_accel_v112_signal(equity, closeadj):
    base = equity.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm equity
def eqt_f41_equity_trajectory_ewm_126d_accel_v113_signal(equity, closeadj):
    base = equity.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm equity
def eqt_f41_equity_trajectory_ewm_126d_accel_v114_signal(equity, closeadj):
    base = equity.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm equity
def eqt_f41_equity_trajectory_ewm_252d_accel_v115_signal(equity, closeadj):
    base = equity.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm equity
def eqt_f41_equity_trajectory_ewm_252d_accel_v116_signal(equity, closeadj):
    base = equity.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm equity
def eqt_f41_equity_trajectory_ewm_252d_accel_v117_signal(equity, closeadj):
    base = equity.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm equity
def eqt_f41_equity_trajectory_ewm_504d_accel_v118_signal(equity, closeadj):
    base = equity.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm equity
def eqt_f41_equity_trajectory_ewm_504d_accel_v119_signal(equity, closeadj):
    base = equity.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm equity
def eqt_f41_equity_trajectory_ewm_504d_accel_v120_signal(equity, closeadj):
    base = equity.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq equity
def eqt_f41_equity_trajectory_sq_21d_accel_v121_signal(equity, closeadj):
    base = _mean(equity * equity, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq equity
def eqt_f41_equity_trajectory_sq_21d_accel_v122_signal(equity, closeadj):
    base = _mean(equity * equity, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq equity
def eqt_f41_equity_trajectory_sq_21d_accel_v123_signal(equity, closeadj):
    base = _mean(equity * equity, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq equity
def eqt_f41_equity_trajectory_sq_63d_accel_v124_signal(equity, closeadj):
    base = _mean(equity * equity, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq equity
def eqt_f41_equity_trajectory_sq_63d_accel_v125_signal(equity, closeadj):
    base = _mean(equity * equity, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq equity
def eqt_f41_equity_trajectory_sq_63d_accel_v126_signal(equity, closeadj):
    base = _mean(equity * equity, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq equity
def eqt_f41_equity_trajectory_sq_126d_accel_v127_signal(equity, closeadj):
    base = _mean(equity * equity, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq equity
def eqt_f41_equity_trajectory_sq_126d_accel_v128_signal(equity, closeadj):
    base = _mean(equity * equity, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq equity
def eqt_f41_equity_trajectory_sq_126d_accel_v129_signal(equity, closeadj):
    base = _mean(equity * equity, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq equity
def eqt_f41_equity_trajectory_sq_252d_accel_v130_signal(equity, closeadj):
    base = _mean(equity * equity, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq equity
def eqt_f41_equity_trajectory_sq_252d_accel_v131_signal(equity, closeadj):
    base = _mean(equity * equity, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq equity
def eqt_f41_equity_trajectory_sq_252d_accel_v132_signal(equity, closeadj):
    base = _mean(equity * equity, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq equity
def eqt_f41_equity_trajectory_sq_504d_accel_v133_signal(equity, closeadj):
    base = _mean(equity * equity, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq equity
def eqt_f41_equity_trajectory_sq_504d_accel_v134_signal(equity, closeadj):
    base = _mean(equity * equity, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq equity
def eqt_f41_equity_trajectory_sq_504d_accel_v135_signal(equity, closeadj):
    base = _mean(equity * equity, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z equity
def eqt_f41_equity_trajectory_z_21d_accel_v136_signal(equity):
    base = _z(equity, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z equity
def eqt_f41_equity_trajectory_z_21d_accel_v137_signal(equity):
    base = _z(equity, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z equity
def eqt_f41_equity_trajectory_z_21d_accel_v138_signal(equity):
    base = _z(equity, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z equity
def eqt_f41_equity_trajectory_z_63d_accel_v139_signal(equity):
    base = _z(equity, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z equity
def eqt_f41_equity_trajectory_z_63d_accel_v140_signal(equity):
    base = _z(equity, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z equity
def eqt_f41_equity_trajectory_z_63d_accel_v141_signal(equity):
    base = _z(equity, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z equity
def eqt_f41_equity_trajectory_z_126d_accel_v142_signal(equity):
    base = _z(equity, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z equity
def eqt_f41_equity_trajectory_z_126d_accel_v143_signal(equity):
    base = _z(equity, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z equity
def eqt_f41_equity_trajectory_z_126d_accel_v144_signal(equity):
    base = _z(equity, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z equity
def eqt_f41_equity_trajectory_z_252d_accel_v145_signal(equity):
    base = _z(equity, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z equity
def eqt_f41_equity_trajectory_z_252d_accel_v146_signal(equity):
    base = _z(equity, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z equity
def eqt_f41_equity_trajectory_z_252d_accel_v147_signal(equity):
    base = _z(equity, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z equity
def eqt_f41_equity_trajectory_z_504d_accel_v148_signal(equity):
    base = _z(equity, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z equity
def eqt_f41_equity_trajectory_z_504d_accel_v149_signal(equity):
    base = _z(equity, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z equity
def eqt_f41_equity_trajectory_z_504d_accel_v150_signal(equity):
    base = _z(equity, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
