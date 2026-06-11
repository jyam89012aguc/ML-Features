"""Family f078 - TTM versus annual consistency (Fundamental Dynamics) | Sharadar tables: SF1 | fields: dimension, revenue, ncfo, netinc, rnd | 2nd derivatives 001-150"""
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
def _ttm_vs_annual_consistency_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ttm_vs_annual_consistency_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ttm_vs_annual_consistency_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_21d_slope_v001_signal(dimension, closeadj):
    base = _mean(dimension, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_21d_slope_v002_signal(dimension, closeadj):
    base = _mean(dimension, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_21d_slope_v003_signal(dimension, closeadj):
    base = _mean(dimension, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_63d_slope_v004_signal(dimension, closeadj):
    base = _mean(dimension, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_63d_slope_v005_signal(dimension, closeadj):
    base = _mean(dimension, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_63d_slope_v006_signal(dimension, closeadj):
    base = _mean(dimension, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_126d_slope_v007_signal(dimension, closeadj):
    base = _mean(dimension, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_126d_slope_v008_signal(dimension, closeadj):
    base = _mean(dimension, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_126d_slope_v009_signal(dimension, closeadj):
    base = _mean(dimension, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_252d_slope_v010_signal(dimension, closeadj):
    base = _mean(dimension, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_252d_slope_v011_signal(dimension, closeadj):
    base = _mean(dimension, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_252d_slope_v012_signal(dimension, closeadj):
    base = _mean(dimension, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_504d_slope_v013_signal(dimension, closeadj):
    base = _mean(dimension, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_504d_slope_v014_signal(dimension, closeadj):
    base = _mean(dimension, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw dimension
def tvac_f078_ttm_vs_annual_consistency_raw_504d_slope_v015_signal(dimension, closeadj):
    base = _mean(dimension, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_21d_slope_v016_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_21d_slope_v017_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_21d_slope_v018_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_63d_slope_v019_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_63d_slope_v020_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_63d_slope_v021_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_126d_slope_v022_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_126d_slope_v023_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_126d_slope_v024_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_252d_slope_v025_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_252d_slope_v026_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_252d_slope_v027_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_504d_slope_v028_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_504d_slope_v029_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log dimension
def tvac_f078_ttm_vs_annual_consistency_log_504d_slope_v030_signal(dimension, closeadj):
    base = _mean(_ttm_vs_annual_consistency_log(dimension), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_21d_slope_v031_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_21d_slope_v032_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_21d_slope_v033_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_63d_slope_v034_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_63d_slope_v035_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_63d_slope_v036_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_126d_slope_v037_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_126d_slope_v038_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_126d_slope_v039_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_252d_slope_v040_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_252d_slope_v041_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_252d_slope_v042_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_504d_slope_v043_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_504d_slope_v044_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare dimension
def tvac_f078_ttm_vs_annual_consistency_pershare_504d_slope_v045_signal(dimension, sharesbas, closeadj):
    base = _mean(_ttm_vs_annual_consistency_per_share(dimension, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_21d_slope_v046_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_21d_slope_v047_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_21d_slope_v048_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_63d_slope_v049_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_63d_slope_v050_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_63d_slope_v051_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_126d_slope_v052_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_126d_slope_v053_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_126d_slope_v054_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_252d_slope_v055_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_252d_slope_v056_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_252d_slope_v057_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_504d_slope_v058_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_504d_slope_v059_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_revenue dimension
def tvac_f078_ttm_vs_annual_consistency_per_revenue_504d_slope_v060_signal(dimension, revenue):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, revenue), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_21d_slope_v061_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_21d_slope_v062_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_21d_slope_v063_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_63d_slope_v064_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_63d_slope_v065_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_63d_slope_v066_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_126d_slope_v067_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_126d_slope_v068_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_126d_slope_v069_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_252d_slope_v070_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_252d_slope_v071_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_252d_slope_v072_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_504d_slope_v073_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_504d_slope_v074_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_ncfo dimension
def tvac_f078_ttm_vs_annual_consistency_per_ncfo_504d_slope_v075_signal(dimension, ncfo):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, ncfo), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_21d_slope_v076_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_21d_slope_v077_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_21d_slope_v078_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_63d_slope_v079_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_63d_slope_v080_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_63d_slope_v081_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_126d_slope_v082_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_126d_slope_v083_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_126d_slope_v084_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_252d_slope_v085_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_252d_slope_v086_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_252d_slope_v087_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_504d_slope_v088_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_504d_slope_v089_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_netinc dimension
def tvac_f078_ttm_vs_annual_consistency_per_netinc_504d_slope_v090_signal(dimension, netinc):
    base = _mean(_ttm_vs_annual_consistency_scaled(dimension, netinc), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_21d_slope_v091_signal(dimension, closeadj):
    base = _std(dimension, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_21d_slope_v092_signal(dimension, closeadj):
    base = _std(dimension, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_21d_slope_v093_signal(dimension, closeadj):
    base = _std(dimension, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_63d_slope_v094_signal(dimension, closeadj):
    base = _std(dimension, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_63d_slope_v095_signal(dimension, closeadj):
    base = _std(dimension, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_63d_slope_v096_signal(dimension, closeadj):
    base = _std(dimension, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_126d_slope_v097_signal(dimension, closeadj):
    base = _std(dimension, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_126d_slope_v098_signal(dimension, closeadj):
    base = _std(dimension, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_126d_slope_v099_signal(dimension, closeadj):
    base = _std(dimension, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_252d_slope_v100_signal(dimension, closeadj):
    base = _std(dimension, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_252d_slope_v101_signal(dimension, closeadj):
    base = _std(dimension, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_252d_slope_v102_signal(dimension, closeadj):
    base = _std(dimension, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_504d_slope_v103_signal(dimension, closeadj):
    base = _std(dimension, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_504d_slope_v104_signal(dimension, closeadj):
    base = _std(dimension, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std dimension
def tvac_f078_ttm_vs_annual_consistency_std_504d_slope_v105_signal(dimension, closeadj):
    base = _std(dimension, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_21d_slope_v106_signal(dimension, closeadj):
    base = dimension.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_21d_slope_v107_signal(dimension, closeadj):
    base = dimension.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_21d_slope_v108_signal(dimension, closeadj):
    base = dimension.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_63d_slope_v109_signal(dimension, closeadj):
    base = dimension.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_63d_slope_v110_signal(dimension, closeadj):
    base = dimension.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_63d_slope_v111_signal(dimension, closeadj):
    base = dimension.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_126d_slope_v112_signal(dimension, closeadj):
    base = dimension.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_126d_slope_v113_signal(dimension, closeadj):
    base = dimension.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_126d_slope_v114_signal(dimension, closeadj):
    base = dimension.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_252d_slope_v115_signal(dimension, closeadj):
    base = dimension.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_252d_slope_v116_signal(dimension, closeadj):
    base = dimension.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_252d_slope_v117_signal(dimension, closeadj):
    base = dimension.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_504d_slope_v118_signal(dimension, closeadj):
    base = dimension.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_504d_slope_v119_signal(dimension, closeadj):
    base = dimension.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm dimension
def tvac_f078_ttm_vs_annual_consistency_ewm_504d_slope_v120_signal(dimension, closeadj):
    base = dimension.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_21d_slope_v121_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_21d_slope_v122_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_21d_slope_v123_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_63d_slope_v124_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_63d_slope_v125_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_63d_slope_v126_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_126d_slope_v127_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_126d_slope_v128_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_126d_slope_v129_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_252d_slope_v130_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_252d_slope_v131_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_252d_slope_v132_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_504d_slope_v133_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_504d_slope_v134_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq dimension
def tvac_f078_ttm_vs_annual_consistency_sq_504d_slope_v135_signal(dimension, closeadj):
    base = _mean(dimension * dimension, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_21d_slope_v136_signal(dimension):
    base = _z(dimension, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_21d_slope_v137_signal(dimension):
    base = _z(dimension, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_21d_slope_v138_signal(dimension):
    base = _z(dimension, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_63d_slope_v139_signal(dimension):
    base = _z(dimension, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_63d_slope_v140_signal(dimension):
    base = _z(dimension, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_63d_slope_v141_signal(dimension):
    base = _z(dimension, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_126d_slope_v142_signal(dimension):
    base = _z(dimension, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_126d_slope_v143_signal(dimension):
    base = _z(dimension, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_126d_slope_v144_signal(dimension):
    base = _z(dimension, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_252d_slope_v145_signal(dimension):
    base = _z(dimension, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_252d_slope_v146_signal(dimension):
    base = _z(dimension, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_252d_slope_v147_signal(dimension):
    base = _z(dimension, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_504d_slope_v148_signal(dimension):
    base = _z(dimension, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_504d_slope_v149_signal(dimension):
    base = _z(dimension, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z dimension
def tvac_f078_ttm_vs_annual_consistency_z_504d_slope_v150_signal(dimension):
    base = _z(dimension, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
