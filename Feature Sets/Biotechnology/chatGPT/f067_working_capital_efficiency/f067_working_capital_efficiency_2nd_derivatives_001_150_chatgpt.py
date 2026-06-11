"""Family f067 - Working capital productivity (Returns and Efficiency) | Sharadar tables: SF1 | fields: workingcapital, revenue, assets | 2nd derivatives 001-150"""
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
def _working_capital_efficiency_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _working_capital_efficiency_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _working_capital_efficiency_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw workingcapital
def wce_f067_working_capital_efficiency_raw_21d_slope_v001_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw workingcapital
def wce_f067_working_capital_efficiency_raw_21d_slope_v002_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw workingcapital
def wce_f067_working_capital_efficiency_raw_21d_slope_v003_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw workingcapital
def wce_f067_working_capital_efficiency_raw_63d_slope_v004_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw workingcapital
def wce_f067_working_capital_efficiency_raw_63d_slope_v005_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw workingcapital
def wce_f067_working_capital_efficiency_raw_63d_slope_v006_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw workingcapital
def wce_f067_working_capital_efficiency_raw_126d_slope_v007_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw workingcapital
def wce_f067_working_capital_efficiency_raw_126d_slope_v008_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw workingcapital
def wce_f067_working_capital_efficiency_raw_126d_slope_v009_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw workingcapital
def wce_f067_working_capital_efficiency_raw_252d_slope_v010_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw workingcapital
def wce_f067_working_capital_efficiency_raw_252d_slope_v011_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw workingcapital
def wce_f067_working_capital_efficiency_raw_252d_slope_v012_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw workingcapital
def wce_f067_working_capital_efficiency_raw_504d_slope_v013_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw workingcapital
def wce_f067_working_capital_efficiency_raw_504d_slope_v014_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw workingcapital
def wce_f067_working_capital_efficiency_raw_504d_slope_v015_signal(workingcapital, closeadj):
    base = _mean(workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log workingcapital
def wce_f067_working_capital_efficiency_log_21d_slope_v016_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log workingcapital
def wce_f067_working_capital_efficiency_log_21d_slope_v017_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log workingcapital
def wce_f067_working_capital_efficiency_log_21d_slope_v018_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log workingcapital
def wce_f067_working_capital_efficiency_log_63d_slope_v019_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log workingcapital
def wce_f067_working_capital_efficiency_log_63d_slope_v020_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log workingcapital
def wce_f067_working_capital_efficiency_log_63d_slope_v021_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log workingcapital
def wce_f067_working_capital_efficiency_log_126d_slope_v022_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log workingcapital
def wce_f067_working_capital_efficiency_log_126d_slope_v023_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log workingcapital
def wce_f067_working_capital_efficiency_log_126d_slope_v024_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log workingcapital
def wce_f067_working_capital_efficiency_log_252d_slope_v025_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log workingcapital
def wce_f067_working_capital_efficiency_log_252d_slope_v026_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log workingcapital
def wce_f067_working_capital_efficiency_log_252d_slope_v027_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log workingcapital
def wce_f067_working_capital_efficiency_log_504d_slope_v028_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log workingcapital
def wce_f067_working_capital_efficiency_log_504d_slope_v029_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log workingcapital
def wce_f067_working_capital_efficiency_log_504d_slope_v030_signal(workingcapital, closeadj):
    base = _mean(_working_capital_efficiency_log(workingcapital), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_21d_slope_v031_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_21d_slope_v032_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_21d_slope_v033_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_63d_slope_v034_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_63d_slope_v035_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_63d_slope_v036_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_126d_slope_v037_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_126d_slope_v038_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_126d_slope_v039_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_252d_slope_v040_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_252d_slope_v041_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_252d_slope_v042_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_504d_slope_v043_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_504d_slope_v044_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare workingcapital
def wce_f067_working_capital_efficiency_pershare_504d_slope_v045_signal(workingcapital, sharesbas, closeadj):
    base = _mean(_working_capital_efficiency_per_share(workingcapital, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_21d_slope_v046_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_21d_slope_v047_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_21d_slope_v048_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_63d_slope_v049_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_63d_slope_v050_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_63d_slope_v051_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_126d_slope_v052_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_126d_slope_v053_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_126d_slope_v054_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_252d_slope_v055_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_252d_slope_v056_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_252d_slope_v057_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_504d_slope_v058_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_504d_slope_v059_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_revenue workingcapital
def wce_f067_working_capital_efficiency_per_revenue_504d_slope_v060_signal(workingcapital, revenue):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, revenue), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_21d_slope_v061_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_21d_slope_v062_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_21d_slope_v063_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_63d_slope_v064_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_63d_slope_v065_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_63d_slope_v066_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_126d_slope_v067_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_126d_slope_v068_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_126d_slope_v069_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_252d_slope_v070_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_252d_slope_v071_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_252d_slope_v072_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_504d_slope_v073_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_504d_slope_v074_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets workingcapital
def wce_f067_working_capital_efficiency_per_assets_504d_slope_v075_signal(workingcapital, assets):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_21d_slope_v076_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_21d_slope_v077_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_21d_slope_v078_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_63d_slope_v079_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_63d_slope_v080_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_63d_slope_v081_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_126d_slope_v082_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_126d_slope_v083_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_126d_slope_v084_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_252d_slope_v085_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_252d_slope_v086_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_252d_slope_v087_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_504d_slope_v088_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_504d_slope_v089_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap workingcapital
def wce_f067_working_capital_efficiency_per_marketcap_504d_slope_v090_signal(workingcapital, marketcap):
    base = _mean(_working_capital_efficiency_scaled(workingcapital, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std workingcapital
def wce_f067_working_capital_efficiency_std_21d_slope_v091_signal(workingcapital, closeadj):
    base = _std(workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std workingcapital
def wce_f067_working_capital_efficiency_std_21d_slope_v092_signal(workingcapital, closeadj):
    base = _std(workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std workingcapital
def wce_f067_working_capital_efficiency_std_21d_slope_v093_signal(workingcapital, closeadj):
    base = _std(workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std workingcapital
def wce_f067_working_capital_efficiency_std_63d_slope_v094_signal(workingcapital, closeadj):
    base = _std(workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std workingcapital
def wce_f067_working_capital_efficiency_std_63d_slope_v095_signal(workingcapital, closeadj):
    base = _std(workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std workingcapital
def wce_f067_working_capital_efficiency_std_63d_slope_v096_signal(workingcapital, closeadj):
    base = _std(workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std workingcapital
def wce_f067_working_capital_efficiency_std_126d_slope_v097_signal(workingcapital, closeadj):
    base = _std(workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std workingcapital
def wce_f067_working_capital_efficiency_std_126d_slope_v098_signal(workingcapital, closeadj):
    base = _std(workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std workingcapital
def wce_f067_working_capital_efficiency_std_126d_slope_v099_signal(workingcapital, closeadj):
    base = _std(workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std workingcapital
def wce_f067_working_capital_efficiency_std_252d_slope_v100_signal(workingcapital, closeadj):
    base = _std(workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std workingcapital
def wce_f067_working_capital_efficiency_std_252d_slope_v101_signal(workingcapital, closeadj):
    base = _std(workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std workingcapital
def wce_f067_working_capital_efficiency_std_252d_slope_v102_signal(workingcapital, closeadj):
    base = _std(workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std workingcapital
def wce_f067_working_capital_efficiency_std_504d_slope_v103_signal(workingcapital, closeadj):
    base = _std(workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std workingcapital
def wce_f067_working_capital_efficiency_std_504d_slope_v104_signal(workingcapital, closeadj):
    base = _std(workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std workingcapital
def wce_f067_working_capital_efficiency_std_504d_slope_v105_signal(workingcapital, closeadj):
    base = _std(workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_21d_slope_v106_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_21d_slope_v107_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_21d_slope_v108_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_63d_slope_v109_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_63d_slope_v110_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_63d_slope_v111_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_126d_slope_v112_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_126d_slope_v113_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_126d_slope_v114_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_252d_slope_v115_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_252d_slope_v116_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_252d_slope_v117_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_504d_slope_v118_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_504d_slope_v119_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm workingcapital
def wce_f067_working_capital_efficiency_ewm_504d_slope_v120_signal(workingcapital, closeadj):
    base = workingcapital.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq workingcapital
def wce_f067_working_capital_efficiency_sq_21d_slope_v121_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq workingcapital
def wce_f067_working_capital_efficiency_sq_21d_slope_v122_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq workingcapital
def wce_f067_working_capital_efficiency_sq_21d_slope_v123_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq workingcapital
def wce_f067_working_capital_efficiency_sq_63d_slope_v124_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq workingcapital
def wce_f067_working_capital_efficiency_sq_63d_slope_v125_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq workingcapital
def wce_f067_working_capital_efficiency_sq_63d_slope_v126_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq workingcapital
def wce_f067_working_capital_efficiency_sq_126d_slope_v127_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq workingcapital
def wce_f067_working_capital_efficiency_sq_126d_slope_v128_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq workingcapital
def wce_f067_working_capital_efficiency_sq_126d_slope_v129_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq workingcapital
def wce_f067_working_capital_efficiency_sq_252d_slope_v130_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq workingcapital
def wce_f067_working_capital_efficiency_sq_252d_slope_v131_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq workingcapital
def wce_f067_working_capital_efficiency_sq_252d_slope_v132_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq workingcapital
def wce_f067_working_capital_efficiency_sq_504d_slope_v133_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq workingcapital
def wce_f067_working_capital_efficiency_sq_504d_slope_v134_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq workingcapital
def wce_f067_working_capital_efficiency_sq_504d_slope_v135_signal(workingcapital, closeadj):
    base = _mean(workingcapital * workingcapital, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z workingcapital
def wce_f067_working_capital_efficiency_z_21d_slope_v136_signal(workingcapital):
    base = _z(workingcapital, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z workingcapital
def wce_f067_working_capital_efficiency_z_21d_slope_v137_signal(workingcapital):
    base = _z(workingcapital, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z workingcapital
def wce_f067_working_capital_efficiency_z_21d_slope_v138_signal(workingcapital):
    base = _z(workingcapital, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z workingcapital
def wce_f067_working_capital_efficiency_z_63d_slope_v139_signal(workingcapital):
    base = _z(workingcapital, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z workingcapital
def wce_f067_working_capital_efficiency_z_63d_slope_v140_signal(workingcapital):
    base = _z(workingcapital, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z workingcapital
def wce_f067_working_capital_efficiency_z_63d_slope_v141_signal(workingcapital):
    base = _z(workingcapital, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z workingcapital
def wce_f067_working_capital_efficiency_z_126d_slope_v142_signal(workingcapital):
    base = _z(workingcapital, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z workingcapital
def wce_f067_working_capital_efficiency_z_126d_slope_v143_signal(workingcapital):
    base = _z(workingcapital, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z workingcapital
def wce_f067_working_capital_efficiency_z_126d_slope_v144_signal(workingcapital):
    base = _z(workingcapital, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z workingcapital
def wce_f067_working_capital_efficiency_z_252d_slope_v145_signal(workingcapital):
    base = _z(workingcapital, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z workingcapital
def wce_f067_working_capital_efficiency_z_252d_slope_v146_signal(workingcapital):
    base = _z(workingcapital, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z workingcapital
def wce_f067_working_capital_efficiency_z_252d_slope_v147_signal(workingcapital):
    base = _z(workingcapital, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z workingcapital
def wce_f067_working_capital_efficiency_z_504d_slope_v148_signal(workingcapital):
    base = _z(workingcapital, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z workingcapital
def wce_f067_working_capital_efficiency_z_504d_slope_v149_signal(workingcapital):
    base = _z(workingcapital, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z workingcapital
def wce_f067_working_capital_efficiency_z_504d_slope_v150_signal(workingcapital):
    base = _z(workingcapital, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
