"""Family f013 - Capex and manufacturing buildout (Cash Flow and Burn) | Sharadar tables: SF1 | fields: capex, ppnenet, assets, revenue | 2nd derivatives 001-150"""
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
def _capex_and_manufacturing_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _capex_and_manufacturing_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _capex_and_manufacturing_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw capex
def cam_f013_capex_and_manufacturing_raw_21d_slope_v001_signal(capex, closeadj):
    base = _mean(capex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw capex
def cam_f013_capex_and_manufacturing_raw_21d_slope_v002_signal(capex, closeadj):
    base = _mean(capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw capex
def cam_f013_capex_and_manufacturing_raw_21d_slope_v003_signal(capex, closeadj):
    base = _mean(capex, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw capex
def cam_f013_capex_and_manufacturing_raw_63d_slope_v004_signal(capex, closeadj):
    base = _mean(capex, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw capex
def cam_f013_capex_and_manufacturing_raw_63d_slope_v005_signal(capex, closeadj):
    base = _mean(capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw capex
def cam_f013_capex_and_manufacturing_raw_63d_slope_v006_signal(capex, closeadj):
    base = _mean(capex, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw capex
def cam_f013_capex_and_manufacturing_raw_126d_slope_v007_signal(capex, closeadj):
    base = _mean(capex, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw capex
def cam_f013_capex_and_manufacturing_raw_126d_slope_v008_signal(capex, closeadj):
    base = _mean(capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw capex
def cam_f013_capex_and_manufacturing_raw_126d_slope_v009_signal(capex, closeadj):
    base = _mean(capex, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw capex
def cam_f013_capex_and_manufacturing_raw_252d_slope_v010_signal(capex, closeadj):
    base = _mean(capex, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw capex
def cam_f013_capex_and_manufacturing_raw_252d_slope_v011_signal(capex, closeadj):
    base = _mean(capex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw capex
def cam_f013_capex_and_manufacturing_raw_252d_slope_v012_signal(capex, closeadj):
    base = _mean(capex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw capex
def cam_f013_capex_and_manufacturing_raw_504d_slope_v013_signal(capex, closeadj):
    base = _mean(capex, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw capex
def cam_f013_capex_and_manufacturing_raw_504d_slope_v014_signal(capex, closeadj):
    base = _mean(capex, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw capex
def cam_f013_capex_and_manufacturing_raw_504d_slope_v015_signal(capex, closeadj):
    base = _mean(capex, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log capex
def cam_f013_capex_and_manufacturing_log_21d_slope_v016_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log capex
def cam_f013_capex_and_manufacturing_log_21d_slope_v017_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log capex
def cam_f013_capex_and_manufacturing_log_21d_slope_v018_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log capex
def cam_f013_capex_and_manufacturing_log_63d_slope_v019_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log capex
def cam_f013_capex_and_manufacturing_log_63d_slope_v020_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log capex
def cam_f013_capex_and_manufacturing_log_63d_slope_v021_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log capex
def cam_f013_capex_and_manufacturing_log_126d_slope_v022_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log capex
def cam_f013_capex_and_manufacturing_log_126d_slope_v023_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log capex
def cam_f013_capex_and_manufacturing_log_126d_slope_v024_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log capex
def cam_f013_capex_and_manufacturing_log_252d_slope_v025_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log capex
def cam_f013_capex_and_manufacturing_log_252d_slope_v026_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log capex
def cam_f013_capex_and_manufacturing_log_252d_slope_v027_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log capex
def cam_f013_capex_and_manufacturing_log_504d_slope_v028_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log capex
def cam_f013_capex_and_manufacturing_log_504d_slope_v029_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log capex
def cam_f013_capex_and_manufacturing_log_504d_slope_v030_signal(capex, closeadj):
    base = _mean(_capex_and_manufacturing_log(capex), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare capex
def cam_f013_capex_and_manufacturing_pershare_21d_slope_v031_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare capex
def cam_f013_capex_and_manufacturing_pershare_21d_slope_v032_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare capex
def cam_f013_capex_and_manufacturing_pershare_21d_slope_v033_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare capex
def cam_f013_capex_and_manufacturing_pershare_63d_slope_v034_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare capex
def cam_f013_capex_and_manufacturing_pershare_63d_slope_v035_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare capex
def cam_f013_capex_and_manufacturing_pershare_63d_slope_v036_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare capex
def cam_f013_capex_and_manufacturing_pershare_126d_slope_v037_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare capex
def cam_f013_capex_and_manufacturing_pershare_126d_slope_v038_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare capex
def cam_f013_capex_and_manufacturing_pershare_126d_slope_v039_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare capex
def cam_f013_capex_and_manufacturing_pershare_252d_slope_v040_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare capex
def cam_f013_capex_and_manufacturing_pershare_252d_slope_v041_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare capex
def cam_f013_capex_and_manufacturing_pershare_252d_slope_v042_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare capex
def cam_f013_capex_and_manufacturing_pershare_504d_slope_v043_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare capex
def cam_f013_capex_and_manufacturing_pershare_504d_slope_v044_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare capex
def cam_f013_capex_and_manufacturing_pershare_504d_slope_v045_signal(capex, sharesbas, closeadj):
    base = _mean(_capex_and_manufacturing_per_share(capex, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_21d_slope_v046_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_21d_slope_v047_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_21d_slope_v048_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_63d_slope_v049_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_63d_slope_v050_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_63d_slope_v051_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_126d_slope_v052_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_126d_slope_v053_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_126d_slope_v054_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_252d_slope_v055_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_252d_slope_v056_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_252d_slope_v057_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_504d_slope_v058_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_504d_slope_v059_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_ppnenet capex
def cam_f013_capex_and_manufacturing_per_ppnenet_504d_slope_v060_signal(capex, ppnenet):
    base = _mean(_capex_and_manufacturing_scaled(capex, ppnenet), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_21d_slope_v061_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_21d_slope_v062_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_21d_slope_v063_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_63d_slope_v064_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_63d_slope_v065_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_63d_slope_v066_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_126d_slope_v067_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_126d_slope_v068_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_126d_slope_v069_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_252d_slope_v070_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_252d_slope_v071_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_252d_slope_v072_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_504d_slope_v073_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_504d_slope_v074_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets capex
def cam_f013_capex_and_manufacturing_per_assets_504d_slope_v075_signal(capex, assets):
    base = _mean(_capex_and_manufacturing_scaled(capex, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_21d_slope_v076_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_21d_slope_v077_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_21d_slope_v078_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_63d_slope_v079_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_63d_slope_v080_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_63d_slope_v081_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_126d_slope_v082_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_126d_slope_v083_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_126d_slope_v084_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_252d_slope_v085_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_252d_slope_v086_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_252d_slope_v087_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_504d_slope_v088_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_504d_slope_v089_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_revenue capex
def cam_f013_capex_and_manufacturing_per_revenue_504d_slope_v090_signal(capex, revenue):
    base = _mean(_capex_and_manufacturing_scaled(capex, revenue), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std capex
def cam_f013_capex_and_manufacturing_std_21d_slope_v091_signal(capex, closeadj):
    base = _std(capex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std capex
def cam_f013_capex_and_manufacturing_std_21d_slope_v092_signal(capex, closeadj):
    base = _std(capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std capex
def cam_f013_capex_and_manufacturing_std_21d_slope_v093_signal(capex, closeadj):
    base = _std(capex, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std capex
def cam_f013_capex_and_manufacturing_std_63d_slope_v094_signal(capex, closeadj):
    base = _std(capex, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std capex
def cam_f013_capex_and_manufacturing_std_63d_slope_v095_signal(capex, closeadj):
    base = _std(capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std capex
def cam_f013_capex_and_manufacturing_std_63d_slope_v096_signal(capex, closeadj):
    base = _std(capex, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std capex
def cam_f013_capex_and_manufacturing_std_126d_slope_v097_signal(capex, closeadj):
    base = _std(capex, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std capex
def cam_f013_capex_and_manufacturing_std_126d_slope_v098_signal(capex, closeadj):
    base = _std(capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std capex
def cam_f013_capex_and_manufacturing_std_126d_slope_v099_signal(capex, closeadj):
    base = _std(capex, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std capex
def cam_f013_capex_and_manufacturing_std_252d_slope_v100_signal(capex, closeadj):
    base = _std(capex, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std capex
def cam_f013_capex_and_manufacturing_std_252d_slope_v101_signal(capex, closeadj):
    base = _std(capex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std capex
def cam_f013_capex_and_manufacturing_std_252d_slope_v102_signal(capex, closeadj):
    base = _std(capex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std capex
def cam_f013_capex_and_manufacturing_std_504d_slope_v103_signal(capex, closeadj):
    base = _std(capex, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std capex
def cam_f013_capex_and_manufacturing_std_504d_slope_v104_signal(capex, closeadj):
    base = _std(capex, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std capex
def cam_f013_capex_and_manufacturing_std_504d_slope_v105_signal(capex, closeadj):
    base = _std(capex, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm capex
def cam_f013_capex_and_manufacturing_ewm_21d_slope_v106_signal(capex, closeadj):
    base = capex.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm capex
def cam_f013_capex_and_manufacturing_ewm_21d_slope_v107_signal(capex, closeadj):
    base = capex.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm capex
def cam_f013_capex_and_manufacturing_ewm_21d_slope_v108_signal(capex, closeadj):
    base = capex.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm capex
def cam_f013_capex_and_manufacturing_ewm_63d_slope_v109_signal(capex, closeadj):
    base = capex.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm capex
def cam_f013_capex_and_manufacturing_ewm_63d_slope_v110_signal(capex, closeadj):
    base = capex.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm capex
def cam_f013_capex_and_manufacturing_ewm_63d_slope_v111_signal(capex, closeadj):
    base = capex.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm capex
def cam_f013_capex_and_manufacturing_ewm_126d_slope_v112_signal(capex, closeadj):
    base = capex.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm capex
def cam_f013_capex_and_manufacturing_ewm_126d_slope_v113_signal(capex, closeadj):
    base = capex.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm capex
def cam_f013_capex_and_manufacturing_ewm_126d_slope_v114_signal(capex, closeadj):
    base = capex.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm capex
def cam_f013_capex_and_manufacturing_ewm_252d_slope_v115_signal(capex, closeadj):
    base = capex.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm capex
def cam_f013_capex_and_manufacturing_ewm_252d_slope_v116_signal(capex, closeadj):
    base = capex.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm capex
def cam_f013_capex_and_manufacturing_ewm_252d_slope_v117_signal(capex, closeadj):
    base = capex.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm capex
def cam_f013_capex_and_manufacturing_ewm_504d_slope_v118_signal(capex, closeadj):
    base = capex.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm capex
def cam_f013_capex_and_manufacturing_ewm_504d_slope_v119_signal(capex, closeadj):
    base = capex.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm capex
def cam_f013_capex_and_manufacturing_ewm_504d_slope_v120_signal(capex, closeadj):
    base = capex.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq capex
def cam_f013_capex_and_manufacturing_sq_21d_slope_v121_signal(capex, closeadj):
    base = _mean(capex * capex, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq capex
def cam_f013_capex_and_manufacturing_sq_21d_slope_v122_signal(capex, closeadj):
    base = _mean(capex * capex, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq capex
def cam_f013_capex_and_manufacturing_sq_21d_slope_v123_signal(capex, closeadj):
    base = _mean(capex * capex, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq capex
def cam_f013_capex_and_manufacturing_sq_63d_slope_v124_signal(capex, closeadj):
    base = _mean(capex * capex, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq capex
def cam_f013_capex_and_manufacturing_sq_63d_slope_v125_signal(capex, closeadj):
    base = _mean(capex * capex, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq capex
def cam_f013_capex_and_manufacturing_sq_63d_slope_v126_signal(capex, closeadj):
    base = _mean(capex * capex, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq capex
def cam_f013_capex_and_manufacturing_sq_126d_slope_v127_signal(capex, closeadj):
    base = _mean(capex * capex, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq capex
def cam_f013_capex_and_manufacturing_sq_126d_slope_v128_signal(capex, closeadj):
    base = _mean(capex * capex, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq capex
def cam_f013_capex_and_manufacturing_sq_126d_slope_v129_signal(capex, closeadj):
    base = _mean(capex * capex, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq capex
def cam_f013_capex_and_manufacturing_sq_252d_slope_v130_signal(capex, closeadj):
    base = _mean(capex * capex, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq capex
def cam_f013_capex_and_manufacturing_sq_252d_slope_v131_signal(capex, closeadj):
    base = _mean(capex * capex, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq capex
def cam_f013_capex_and_manufacturing_sq_252d_slope_v132_signal(capex, closeadj):
    base = _mean(capex * capex, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq capex
def cam_f013_capex_and_manufacturing_sq_504d_slope_v133_signal(capex, closeadj):
    base = _mean(capex * capex, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq capex
def cam_f013_capex_and_manufacturing_sq_504d_slope_v134_signal(capex, closeadj):
    base = _mean(capex * capex, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq capex
def cam_f013_capex_and_manufacturing_sq_504d_slope_v135_signal(capex, closeadj):
    base = _mean(capex * capex, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z capex
def cam_f013_capex_and_manufacturing_z_21d_slope_v136_signal(capex):
    base = _z(capex, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z capex
def cam_f013_capex_and_manufacturing_z_21d_slope_v137_signal(capex):
    base = _z(capex, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z capex
def cam_f013_capex_and_manufacturing_z_21d_slope_v138_signal(capex):
    base = _z(capex, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z capex
def cam_f013_capex_and_manufacturing_z_63d_slope_v139_signal(capex):
    base = _z(capex, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z capex
def cam_f013_capex_and_manufacturing_z_63d_slope_v140_signal(capex):
    base = _z(capex, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z capex
def cam_f013_capex_and_manufacturing_z_63d_slope_v141_signal(capex):
    base = _z(capex, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z capex
def cam_f013_capex_and_manufacturing_z_126d_slope_v142_signal(capex):
    base = _z(capex, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z capex
def cam_f013_capex_and_manufacturing_z_126d_slope_v143_signal(capex):
    base = _z(capex, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z capex
def cam_f013_capex_and_manufacturing_z_126d_slope_v144_signal(capex):
    base = _z(capex, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z capex
def cam_f013_capex_and_manufacturing_z_252d_slope_v145_signal(capex):
    base = _z(capex, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z capex
def cam_f013_capex_and_manufacturing_z_252d_slope_v146_signal(capex):
    base = _z(capex, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z capex
def cam_f013_capex_and_manufacturing_z_252d_slope_v147_signal(capex):
    base = _z(capex, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z capex
def cam_f013_capex_and_manufacturing_z_504d_slope_v148_signal(capex):
    base = _z(capex, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z capex
def cam_f013_capex_and_manufacturing_z_504d_slope_v149_signal(capex):
    base = _z(capex, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z capex
def cam_f013_capex_and_manufacturing_z_504d_slope_v150_signal(capex):
    base = _z(capex, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
