"""Family f057 - EPS growth and improvement (Earnings and Quality) | Sharadar tables: SF1 | fields: eps, epsdil | 3rd derivatives 001-150"""
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
def _eps_growth_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _eps_growth_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _eps_growth_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw eps
def eg_f057_eps_growth_raw_21d_accel_v001_signal(eps, closeadj):
    base = _mean(eps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw eps
def eg_f057_eps_growth_raw_21d_accel_v002_signal(eps, closeadj):
    base = _mean(eps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw eps
def eg_f057_eps_growth_raw_21d_accel_v003_signal(eps, closeadj):
    base = _mean(eps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw eps
def eg_f057_eps_growth_raw_63d_accel_v004_signal(eps, closeadj):
    base = _mean(eps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw eps
def eg_f057_eps_growth_raw_63d_accel_v005_signal(eps, closeadj):
    base = _mean(eps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw eps
def eg_f057_eps_growth_raw_63d_accel_v006_signal(eps, closeadj):
    base = _mean(eps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw eps
def eg_f057_eps_growth_raw_126d_accel_v007_signal(eps, closeadj):
    base = _mean(eps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw eps
def eg_f057_eps_growth_raw_126d_accel_v008_signal(eps, closeadj):
    base = _mean(eps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw eps
def eg_f057_eps_growth_raw_126d_accel_v009_signal(eps, closeadj):
    base = _mean(eps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw eps
def eg_f057_eps_growth_raw_252d_accel_v010_signal(eps, closeadj):
    base = _mean(eps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw eps
def eg_f057_eps_growth_raw_252d_accel_v011_signal(eps, closeadj):
    base = _mean(eps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw eps
def eg_f057_eps_growth_raw_252d_accel_v012_signal(eps, closeadj):
    base = _mean(eps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw eps
def eg_f057_eps_growth_raw_504d_accel_v013_signal(eps, closeadj):
    base = _mean(eps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw eps
def eg_f057_eps_growth_raw_504d_accel_v014_signal(eps, closeadj):
    base = _mean(eps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw eps
def eg_f057_eps_growth_raw_504d_accel_v015_signal(eps, closeadj):
    base = _mean(eps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log eps
def eg_f057_eps_growth_log_21d_accel_v016_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log eps
def eg_f057_eps_growth_log_21d_accel_v017_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log eps
def eg_f057_eps_growth_log_21d_accel_v018_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log eps
def eg_f057_eps_growth_log_63d_accel_v019_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log eps
def eg_f057_eps_growth_log_63d_accel_v020_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log eps
def eg_f057_eps_growth_log_63d_accel_v021_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log eps
def eg_f057_eps_growth_log_126d_accel_v022_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log eps
def eg_f057_eps_growth_log_126d_accel_v023_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log eps
def eg_f057_eps_growth_log_126d_accel_v024_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log eps
def eg_f057_eps_growth_log_252d_accel_v025_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log eps
def eg_f057_eps_growth_log_252d_accel_v026_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log eps
def eg_f057_eps_growth_log_252d_accel_v027_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log eps
def eg_f057_eps_growth_log_504d_accel_v028_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log eps
def eg_f057_eps_growth_log_504d_accel_v029_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log eps
def eg_f057_eps_growth_log_504d_accel_v030_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare eps
def eg_f057_eps_growth_pershare_21d_accel_v031_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare eps
def eg_f057_eps_growth_pershare_21d_accel_v032_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare eps
def eg_f057_eps_growth_pershare_21d_accel_v033_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare eps
def eg_f057_eps_growth_pershare_63d_accel_v034_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare eps
def eg_f057_eps_growth_pershare_63d_accel_v035_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare eps
def eg_f057_eps_growth_pershare_63d_accel_v036_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare eps
def eg_f057_eps_growth_pershare_126d_accel_v037_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare eps
def eg_f057_eps_growth_pershare_126d_accel_v038_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare eps
def eg_f057_eps_growth_pershare_126d_accel_v039_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare eps
def eg_f057_eps_growth_pershare_252d_accel_v040_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare eps
def eg_f057_eps_growth_pershare_252d_accel_v041_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare eps
def eg_f057_eps_growth_pershare_252d_accel_v042_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare eps
def eg_f057_eps_growth_pershare_504d_accel_v043_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare eps
def eg_f057_eps_growth_pershare_504d_accel_v044_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare eps
def eg_f057_eps_growth_pershare_504d_accel_v045_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_21d_accel_v046_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_21d_accel_v047_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_21d_accel_v048_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_63d_accel_v049_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_63d_accel_v050_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_63d_accel_v051_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_126d_accel_v052_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_126d_accel_v053_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_126d_accel_v054_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_252d_accel_v055_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_252d_accel_v056_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_252d_accel_v057_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_504d_accel_v058_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_504d_accel_v059_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_504d_accel_v060_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets eps
def eg_f057_eps_growth_per_assets_21d_accel_v061_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets eps
def eg_f057_eps_growth_per_assets_21d_accel_v062_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets eps
def eg_f057_eps_growth_per_assets_21d_accel_v063_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets eps
def eg_f057_eps_growth_per_assets_63d_accel_v064_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets eps
def eg_f057_eps_growth_per_assets_63d_accel_v065_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets eps
def eg_f057_eps_growth_per_assets_63d_accel_v066_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets eps
def eg_f057_eps_growth_per_assets_126d_accel_v067_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets eps
def eg_f057_eps_growth_per_assets_126d_accel_v068_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets eps
def eg_f057_eps_growth_per_assets_126d_accel_v069_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets eps
def eg_f057_eps_growth_per_assets_252d_accel_v070_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets eps
def eg_f057_eps_growth_per_assets_252d_accel_v071_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets eps
def eg_f057_eps_growth_per_assets_252d_accel_v072_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets eps
def eg_f057_eps_growth_per_assets_504d_accel_v073_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets eps
def eg_f057_eps_growth_per_assets_504d_accel_v074_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets eps
def eg_f057_eps_growth_per_assets_504d_accel_v075_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_21d_accel_v076_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_21d_accel_v077_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_21d_accel_v078_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_63d_accel_v079_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_63d_accel_v080_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_63d_accel_v081_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_126d_accel_v082_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_126d_accel_v083_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_126d_accel_v084_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_252d_accel_v085_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_252d_accel_v086_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_252d_accel_v087_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_504d_accel_v088_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_504d_accel_v089_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_504d_accel_v090_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std eps
def eg_f057_eps_growth_std_21d_accel_v091_signal(eps, closeadj):
    base = _std(eps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std eps
def eg_f057_eps_growth_std_21d_accel_v092_signal(eps, closeadj):
    base = _std(eps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std eps
def eg_f057_eps_growth_std_21d_accel_v093_signal(eps, closeadj):
    base = _std(eps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std eps
def eg_f057_eps_growth_std_63d_accel_v094_signal(eps, closeadj):
    base = _std(eps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std eps
def eg_f057_eps_growth_std_63d_accel_v095_signal(eps, closeadj):
    base = _std(eps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std eps
def eg_f057_eps_growth_std_63d_accel_v096_signal(eps, closeadj):
    base = _std(eps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std eps
def eg_f057_eps_growth_std_126d_accel_v097_signal(eps, closeadj):
    base = _std(eps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std eps
def eg_f057_eps_growth_std_126d_accel_v098_signal(eps, closeadj):
    base = _std(eps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std eps
def eg_f057_eps_growth_std_126d_accel_v099_signal(eps, closeadj):
    base = _std(eps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std eps
def eg_f057_eps_growth_std_252d_accel_v100_signal(eps, closeadj):
    base = _std(eps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std eps
def eg_f057_eps_growth_std_252d_accel_v101_signal(eps, closeadj):
    base = _std(eps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std eps
def eg_f057_eps_growth_std_252d_accel_v102_signal(eps, closeadj):
    base = _std(eps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std eps
def eg_f057_eps_growth_std_504d_accel_v103_signal(eps, closeadj):
    base = _std(eps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std eps
def eg_f057_eps_growth_std_504d_accel_v104_signal(eps, closeadj):
    base = _std(eps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std eps
def eg_f057_eps_growth_std_504d_accel_v105_signal(eps, closeadj):
    base = _std(eps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm eps
def eg_f057_eps_growth_ewm_21d_accel_v106_signal(eps, closeadj):
    base = eps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm eps
def eg_f057_eps_growth_ewm_21d_accel_v107_signal(eps, closeadj):
    base = eps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm eps
def eg_f057_eps_growth_ewm_21d_accel_v108_signal(eps, closeadj):
    base = eps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm eps
def eg_f057_eps_growth_ewm_63d_accel_v109_signal(eps, closeadj):
    base = eps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm eps
def eg_f057_eps_growth_ewm_63d_accel_v110_signal(eps, closeadj):
    base = eps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm eps
def eg_f057_eps_growth_ewm_63d_accel_v111_signal(eps, closeadj):
    base = eps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm eps
def eg_f057_eps_growth_ewm_126d_accel_v112_signal(eps, closeadj):
    base = eps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm eps
def eg_f057_eps_growth_ewm_126d_accel_v113_signal(eps, closeadj):
    base = eps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm eps
def eg_f057_eps_growth_ewm_126d_accel_v114_signal(eps, closeadj):
    base = eps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm eps
def eg_f057_eps_growth_ewm_252d_accel_v115_signal(eps, closeadj):
    base = eps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm eps
def eg_f057_eps_growth_ewm_252d_accel_v116_signal(eps, closeadj):
    base = eps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm eps
def eg_f057_eps_growth_ewm_252d_accel_v117_signal(eps, closeadj):
    base = eps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm eps
def eg_f057_eps_growth_ewm_504d_accel_v118_signal(eps, closeadj):
    base = eps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm eps
def eg_f057_eps_growth_ewm_504d_accel_v119_signal(eps, closeadj):
    base = eps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm eps
def eg_f057_eps_growth_ewm_504d_accel_v120_signal(eps, closeadj):
    base = eps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq eps
def eg_f057_eps_growth_sq_21d_accel_v121_signal(eps, closeadj):
    base = _mean(eps * eps, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq eps
def eg_f057_eps_growth_sq_21d_accel_v122_signal(eps, closeadj):
    base = _mean(eps * eps, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq eps
def eg_f057_eps_growth_sq_21d_accel_v123_signal(eps, closeadj):
    base = _mean(eps * eps, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq eps
def eg_f057_eps_growth_sq_63d_accel_v124_signal(eps, closeadj):
    base = _mean(eps * eps, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq eps
def eg_f057_eps_growth_sq_63d_accel_v125_signal(eps, closeadj):
    base = _mean(eps * eps, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq eps
def eg_f057_eps_growth_sq_63d_accel_v126_signal(eps, closeadj):
    base = _mean(eps * eps, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq eps
def eg_f057_eps_growth_sq_126d_accel_v127_signal(eps, closeadj):
    base = _mean(eps * eps, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq eps
def eg_f057_eps_growth_sq_126d_accel_v128_signal(eps, closeadj):
    base = _mean(eps * eps, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq eps
def eg_f057_eps_growth_sq_126d_accel_v129_signal(eps, closeadj):
    base = _mean(eps * eps, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq eps
def eg_f057_eps_growth_sq_252d_accel_v130_signal(eps, closeadj):
    base = _mean(eps * eps, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq eps
def eg_f057_eps_growth_sq_252d_accel_v131_signal(eps, closeadj):
    base = _mean(eps * eps, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq eps
def eg_f057_eps_growth_sq_252d_accel_v132_signal(eps, closeadj):
    base = _mean(eps * eps, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq eps
def eg_f057_eps_growth_sq_504d_accel_v133_signal(eps, closeadj):
    base = _mean(eps * eps, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq eps
def eg_f057_eps_growth_sq_504d_accel_v134_signal(eps, closeadj):
    base = _mean(eps * eps, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq eps
def eg_f057_eps_growth_sq_504d_accel_v135_signal(eps, closeadj):
    base = _mean(eps * eps, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z eps
def eg_f057_eps_growth_z_21d_accel_v136_signal(eps):
    base = _z(eps, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z eps
def eg_f057_eps_growth_z_21d_accel_v137_signal(eps):
    base = _z(eps, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z eps
def eg_f057_eps_growth_z_21d_accel_v138_signal(eps):
    base = _z(eps, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z eps
def eg_f057_eps_growth_z_63d_accel_v139_signal(eps):
    base = _z(eps, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z eps
def eg_f057_eps_growth_z_63d_accel_v140_signal(eps):
    base = _z(eps, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z eps
def eg_f057_eps_growth_z_63d_accel_v141_signal(eps):
    base = _z(eps, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z eps
def eg_f057_eps_growth_z_126d_accel_v142_signal(eps):
    base = _z(eps, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z eps
def eg_f057_eps_growth_z_126d_accel_v143_signal(eps):
    base = _z(eps, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z eps
def eg_f057_eps_growth_z_126d_accel_v144_signal(eps):
    base = _z(eps, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z eps
def eg_f057_eps_growth_z_252d_accel_v145_signal(eps):
    base = _z(eps, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z eps
def eg_f057_eps_growth_z_252d_accel_v146_signal(eps):
    base = _z(eps, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z eps
def eg_f057_eps_growth_z_252d_accel_v147_signal(eps):
    base = _z(eps, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z eps
def eg_f057_eps_growth_z_504d_accel_v148_signal(eps):
    base = _z(eps, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z eps
def eg_f057_eps_growth_z_504d_accel_v149_signal(eps):
    base = _z(eps, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z eps
def eg_f057_eps_growth_z_504d_accel_v150_signal(eps):
    base = _z(eps, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
