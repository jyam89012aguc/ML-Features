"""Family f029 - Book equity trajectory (Capital Structure) | Sharadar tables: SF1 | fields: equity, assets, liabilities, bvps | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw equity
def et_f029_equity_trajectory_raw_21d_slope_v001_signal(equity, closeadj):
    base = _mean(equity, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw equity
def et_f029_equity_trajectory_raw_21d_slope_v002_signal(equity, closeadj):
    base = _mean(equity, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw equity
def et_f029_equity_trajectory_raw_21d_slope_v003_signal(equity, closeadj):
    base = _mean(equity, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw equity
def et_f029_equity_trajectory_raw_63d_slope_v004_signal(equity, closeadj):
    base = _mean(equity, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw equity
def et_f029_equity_trajectory_raw_63d_slope_v005_signal(equity, closeadj):
    base = _mean(equity, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw equity
def et_f029_equity_trajectory_raw_63d_slope_v006_signal(equity, closeadj):
    base = _mean(equity, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw equity
def et_f029_equity_trajectory_raw_126d_slope_v007_signal(equity, closeadj):
    base = _mean(equity, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw equity
def et_f029_equity_trajectory_raw_126d_slope_v008_signal(equity, closeadj):
    base = _mean(equity, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw equity
def et_f029_equity_trajectory_raw_126d_slope_v009_signal(equity, closeadj):
    base = _mean(equity, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw equity
def et_f029_equity_trajectory_raw_252d_slope_v010_signal(equity, closeadj):
    base = _mean(equity, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw equity
def et_f029_equity_trajectory_raw_252d_slope_v011_signal(equity, closeadj):
    base = _mean(equity, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw equity
def et_f029_equity_trajectory_raw_252d_slope_v012_signal(equity, closeadj):
    base = _mean(equity, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw equity
def et_f029_equity_trajectory_raw_504d_slope_v013_signal(equity, closeadj):
    base = _mean(equity, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw equity
def et_f029_equity_trajectory_raw_504d_slope_v014_signal(equity, closeadj):
    base = _mean(equity, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw equity
def et_f029_equity_trajectory_raw_504d_slope_v015_signal(equity, closeadj):
    base = _mean(equity, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log equity
def et_f029_equity_trajectory_log_21d_slope_v016_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log equity
def et_f029_equity_trajectory_log_21d_slope_v017_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log equity
def et_f029_equity_trajectory_log_21d_slope_v018_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log equity
def et_f029_equity_trajectory_log_63d_slope_v019_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log equity
def et_f029_equity_trajectory_log_63d_slope_v020_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log equity
def et_f029_equity_trajectory_log_63d_slope_v021_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log equity
def et_f029_equity_trajectory_log_126d_slope_v022_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log equity
def et_f029_equity_trajectory_log_126d_slope_v023_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log equity
def et_f029_equity_trajectory_log_126d_slope_v024_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log equity
def et_f029_equity_trajectory_log_252d_slope_v025_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log equity
def et_f029_equity_trajectory_log_252d_slope_v026_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log equity
def et_f029_equity_trajectory_log_252d_slope_v027_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log equity
def et_f029_equity_trajectory_log_504d_slope_v028_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log equity
def et_f029_equity_trajectory_log_504d_slope_v029_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log equity
def et_f029_equity_trajectory_log_504d_slope_v030_signal(equity, closeadj):
    base = _mean(_equity_trajectory_log(equity), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare equity
def et_f029_equity_trajectory_pershare_21d_slope_v031_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare equity
def et_f029_equity_trajectory_pershare_21d_slope_v032_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare equity
def et_f029_equity_trajectory_pershare_21d_slope_v033_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare equity
def et_f029_equity_trajectory_pershare_63d_slope_v034_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare equity
def et_f029_equity_trajectory_pershare_63d_slope_v035_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare equity
def et_f029_equity_trajectory_pershare_63d_slope_v036_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare equity
def et_f029_equity_trajectory_pershare_126d_slope_v037_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare equity
def et_f029_equity_trajectory_pershare_126d_slope_v038_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare equity
def et_f029_equity_trajectory_pershare_126d_slope_v039_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare equity
def et_f029_equity_trajectory_pershare_252d_slope_v040_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare equity
def et_f029_equity_trajectory_pershare_252d_slope_v041_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare equity
def et_f029_equity_trajectory_pershare_252d_slope_v042_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare equity
def et_f029_equity_trajectory_pershare_504d_slope_v043_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare equity
def et_f029_equity_trajectory_pershare_504d_slope_v044_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare equity
def et_f029_equity_trajectory_pershare_504d_slope_v045_signal(equity, sharesbas, closeadj):
    base = _mean(_equity_trajectory_per_share(equity, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets equity
def et_f029_equity_trajectory_per_assets_21d_slope_v046_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets equity
def et_f029_equity_trajectory_per_assets_21d_slope_v047_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets equity
def et_f029_equity_trajectory_per_assets_21d_slope_v048_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets equity
def et_f029_equity_trajectory_per_assets_63d_slope_v049_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets equity
def et_f029_equity_trajectory_per_assets_63d_slope_v050_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets equity
def et_f029_equity_trajectory_per_assets_63d_slope_v051_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets equity
def et_f029_equity_trajectory_per_assets_126d_slope_v052_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets equity
def et_f029_equity_trajectory_per_assets_126d_slope_v053_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets equity
def et_f029_equity_trajectory_per_assets_126d_slope_v054_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets equity
def et_f029_equity_trajectory_per_assets_252d_slope_v055_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets equity
def et_f029_equity_trajectory_per_assets_252d_slope_v056_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets equity
def et_f029_equity_trajectory_per_assets_252d_slope_v057_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets equity
def et_f029_equity_trajectory_per_assets_504d_slope_v058_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets equity
def et_f029_equity_trajectory_per_assets_504d_slope_v059_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets equity
def et_f029_equity_trajectory_per_assets_504d_slope_v060_signal(equity, assets):
    base = _mean(_equity_trajectory_scaled(equity, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_bvps equity
def et_f029_equity_trajectory_per_bvps_21d_slope_v061_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_bvps equity
def et_f029_equity_trajectory_per_bvps_21d_slope_v062_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_bvps equity
def et_f029_equity_trajectory_per_bvps_21d_slope_v063_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_bvps equity
def et_f029_equity_trajectory_per_bvps_63d_slope_v064_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_bvps equity
def et_f029_equity_trajectory_per_bvps_63d_slope_v065_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_bvps equity
def et_f029_equity_trajectory_per_bvps_63d_slope_v066_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_bvps equity
def et_f029_equity_trajectory_per_bvps_126d_slope_v067_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_bvps equity
def et_f029_equity_trajectory_per_bvps_126d_slope_v068_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_bvps equity
def et_f029_equity_trajectory_per_bvps_126d_slope_v069_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_bvps equity
def et_f029_equity_trajectory_per_bvps_252d_slope_v070_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_bvps equity
def et_f029_equity_trajectory_per_bvps_252d_slope_v071_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_bvps equity
def et_f029_equity_trajectory_per_bvps_252d_slope_v072_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_bvps equity
def et_f029_equity_trajectory_per_bvps_504d_slope_v073_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_bvps equity
def et_f029_equity_trajectory_per_bvps_504d_slope_v074_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_bvps equity
def et_f029_equity_trajectory_per_bvps_504d_slope_v075_signal(equity, bvps):
    base = _mean(_equity_trajectory_scaled(equity, bvps), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_21d_slope_v076_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_21d_slope_v077_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_21d_slope_v078_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_63d_slope_v079_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_63d_slope_v080_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_63d_slope_v081_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_126d_slope_v082_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_126d_slope_v083_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_126d_slope_v084_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_252d_slope_v085_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_252d_slope_v086_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_252d_slope_v087_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_504d_slope_v088_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_504d_slope_v089_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap equity
def et_f029_equity_trajectory_per_marketcap_504d_slope_v090_signal(equity, marketcap):
    base = _mean(_equity_trajectory_scaled(equity, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std equity
def et_f029_equity_trajectory_std_21d_slope_v091_signal(equity, closeadj):
    base = _std(equity, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std equity
def et_f029_equity_trajectory_std_21d_slope_v092_signal(equity, closeadj):
    base = _std(equity, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std equity
def et_f029_equity_trajectory_std_21d_slope_v093_signal(equity, closeadj):
    base = _std(equity, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std equity
def et_f029_equity_trajectory_std_63d_slope_v094_signal(equity, closeadj):
    base = _std(equity, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std equity
def et_f029_equity_trajectory_std_63d_slope_v095_signal(equity, closeadj):
    base = _std(equity, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std equity
def et_f029_equity_trajectory_std_63d_slope_v096_signal(equity, closeadj):
    base = _std(equity, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std equity
def et_f029_equity_trajectory_std_126d_slope_v097_signal(equity, closeadj):
    base = _std(equity, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std equity
def et_f029_equity_trajectory_std_126d_slope_v098_signal(equity, closeadj):
    base = _std(equity, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std equity
def et_f029_equity_trajectory_std_126d_slope_v099_signal(equity, closeadj):
    base = _std(equity, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std equity
def et_f029_equity_trajectory_std_252d_slope_v100_signal(equity, closeadj):
    base = _std(equity, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std equity
def et_f029_equity_trajectory_std_252d_slope_v101_signal(equity, closeadj):
    base = _std(equity, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std equity
def et_f029_equity_trajectory_std_252d_slope_v102_signal(equity, closeadj):
    base = _std(equity, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std equity
def et_f029_equity_trajectory_std_504d_slope_v103_signal(equity, closeadj):
    base = _std(equity, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std equity
def et_f029_equity_trajectory_std_504d_slope_v104_signal(equity, closeadj):
    base = _std(equity, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std equity
def et_f029_equity_trajectory_std_504d_slope_v105_signal(equity, closeadj):
    base = _std(equity, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm equity
def et_f029_equity_trajectory_ewm_21d_slope_v106_signal(equity, closeadj):
    base = equity.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm equity
def et_f029_equity_trajectory_ewm_21d_slope_v107_signal(equity, closeadj):
    base = equity.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm equity
def et_f029_equity_trajectory_ewm_21d_slope_v108_signal(equity, closeadj):
    base = equity.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm equity
def et_f029_equity_trajectory_ewm_63d_slope_v109_signal(equity, closeadj):
    base = equity.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm equity
def et_f029_equity_trajectory_ewm_63d_slope_v110_signal(equity, closeadj):
    base = equity.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm equity
def et_f029_equity_trajectory_ewm_63d_slope_v111_signal(equity, closeadj):
    base = equity.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm equity
def et_f029_equity_trajectory_ewm_126d_slope_v112_signal(equity, closeadj):
    base = equity.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm equity
def et_f029_equity_trajectory_ewm_126d_slope_v113_signal(equity, closeadj):
    base = equity.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm equity
def et_f029_equity_trajectory_ewm_126d_slope_v114_signal(equity, closeadj):
    base = equity.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm equity
def et_f029_equity_trajectory_ewm_252d_slope_v115_signal(equity, closeadj):
    base = equity.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm equity
def et_f029_equity_trajectory_ewm_252d_slope_v116_signal(equity, closeadj):
    base = equity.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm equity
def et_f029_equity_trajectory_ewm_252d_slope_v117_signal(equity, closeadj):
    base = equity.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm equity
def et_f029_equity_trajectory_ewm_504d_slope_v118_signal(equity, closeadj):
    base = equity.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm equity
def et_f029_equity_trajectory_ewm_504d_slope_v119_signal(equity, closeadj):
    base = equity.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm equity
def et_f029_equity_trajectory_ewm_504d_slope_v120_signal(equity, closeadj):
    base = equity.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq equity
def et_f029_equity_trajectory_sq_21d_slope_v121_signal(equity, closeadj):
    base = _mean(equity * equity, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq equity
def et_f029_equity_trajectory_sq_21d_slope_v122_signal(equity, closeadj):
    base = _mean(equity * equity, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq equity
def et_f029_equity_trajectory_sq_21d_slope_v123_signal(equity, closeadj):
    base = _mean(equity * equity, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq equity
def et_f029_equity_trajectory_sq_63d_slope_v124_signal(equity, closeadj):
    base = _mean(equity * equity, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq equity
def et_f029_equity_trajectory_sq_63d_slope_v125_signal(equity, closeadj):
    base = _mean(equity * equity, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq equity
def et_f029_equity_trajectory_sq_63d_slope_v126_signal(equity, closeadj):
    base = _mean(equity * equity, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq equity
def et_f029_equity_trajectory_sq_126d_slope_v127_signal(equity, closeadj):
    base = _mean(equity * equity, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq equity
def et_f029_equity_trajectory_sq_126d_slope_v128_signal(equity, closeadj):
    base = _mean(equity * equity, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq equity
def et_f029_equity_trajectory_sq_126d_slope_v129_signal(equity, closeadj):
    base = _mean(equity * equity, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq equity
def et_f029_equity_trajectory_sq_252d_slope_v130_signal(equity, closeadj):
    base = _mean(equity * equity, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq equity
def et_f029_equity_trajectory_sq_252d_slope_v131_signal(equity, closeadj):
    base = _mean(equity * equity, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq equity
def et_f029_equity_trajectory_sq_252d_slope_v132_signal(equity, closeadj):
    base = _mean(equity * equity, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq equity
def et_f029_equity_trajectory_sq_504d_slope_v133_signal(equity, closeadj):
    base = _mean(equity * equity, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq equity
def et_f029_equity_trajectory_sq_504d_slope_v134_signal(equity, closeadj):
    base = _mean(equity * equity, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq equity
def et_f029_equity_trajectory_sq_504d_slope_v135_signal(equity, closeadj):
    base = _mean(equity * equity, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z equity
def et_f029_equity_trajectory_z_21d_slope_v136_signal(equity):
    base = _z(equity, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z equity
def et_f029_equity_trajectory_z_21d_slope_v137_signal(equity):
    base = _z(equity, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z equity
def et_f029_equity_trajectory_z_21d_slope_v138_signal(equity):
    base = _z(equity, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z equity
def et_f029_equity_trajectory_z_63d_slope_v139_signal(equity):
    base = _z(equity, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z equity
def et_f029_equity_trajectory_z_63d_slope_v140_signal(equity):
    base = _z(equity, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z equity
def et_f029_equity_trajectory_z_63d_slope_v141_signal(equity):
    base = _z(equity, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z equity
def et_f029_equity_trajectory_z_126d_slope_v142_signal(equity):
    base = _z(equity, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z equity
def et_f029_equity_trajectory_z_126d_slope_v143_signal(equity):
    base = _z(equity, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z equity
def et_f029_equity_trajectory_z_126d_slope_v144_signal(equity):
    base = _z(equity, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z equity
def et_f029_equity_trajectory_z_252d_slope_v145_signal(equity):
    base = _z(equity, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z equity
def et_f029_equity_trajectory_z_252d_slope_v146_signal(equity):
    base = _z(equity, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z equity
def et_f029_equity_trajectory_z_252d_slope_v147_signal(equity):
    base = _z(equity, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z equity
def et_f029_equity_trajectory_z_504d_slope_v148_signal(equity):
    base = _z(equity, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z equity
def et_f029_equity_trajectory_z_504d_slope_v149_signal(equity):
    base = _z(equity, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z equity
def et_f029_equity_trajectory_z_504d_slope_v150_signal(equity):
    base = _z(equity, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
