"""Family f055 - Distance to breakeven (Margins and Profitability) | Sharadar tables: SF1 | fields: netinc, opinc, revenue, opex | 2nd derivatives 001-150"""
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
def _breakeven_distance_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _breakeven_distance_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _breakeven_distance_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw netinc
def bd_f055_breakeven_distance_raw_21d_slope_v001_signal(netinc, closeadj):
    base = _mean(netinc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw netinc
def bd_f055_breakeven_distance_raw_21d_slope_v002_signal(netinc, closeadj):
    base = _mean(netinc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw netinc
def bd_f055_breakeven_distance_raw_21d_slope_v003_signal(netinc, closeadj):
    base = _mean(netinc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw netinc
def bd_f055_breakeven_distance_raw_63d_slope_v004_signal(netinc, closeadj):
    base = _mean(netinc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw netinc
def bd_f055_breakeven_distance_raw_63d_slope_v005_signal(netinc, closeadj):
    base = _mean(netinc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw netinc
def bd_f055_breakeven_distance_raw_63d_slope_v006_signal(netinc, closeadj):
    base = _mean(netinc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw netinc
def bd_f055_breakeven_distance_raw_126d_slope_v007_signal(netinc, closeadj):
    base = _mean(netinc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw netinc
def bd_f055_breakeven_distance_raw_126d_slope_v008_signal(netinc, closeadj):
    base = _mean(netinc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw netinc
def bd_f055_breakeven_distance_raw_126d_slope_v009_signal(netinc, closeadj):
    base = _mean(netinc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw netinc
def bd_f055_breakeven_distance_raw_252d_slope_v010_signal(netinc, closeadj):
    base = _mean(netinc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw netinc
def bd_f055_breakeven_distance_raw_252d_slope_v011_signal(netinc, closeadj):
    base = _mean(netinc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw netinc
def bd_f055_breakeven_distance_raw_252d_slope_v012_signal(netinc, closeadj):
    base = _mean(netinc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw netinc
def bd_f055_breakeven_distance_raw_504d_slope_v013_signal(netinc, closeadj):
    base = _mean(netinc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw netinc
def bd_f055_breakeven_distance_raw_504d_slope_v014_signal(netinc, closeadj):
    base = _mean(netinc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw netinc
def bd_f055_breakeven_distance_raw_504d_slope_v015_signal(netinc, closeadj):
    base = _mean(netinc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log netinc
def bd_f055_breakeven_distance_log_21d_slope_v016_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log netinc
def bd_f055_breakeven_distance_log_21d_slope_v017_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log netinc
def bd_f055_breakeven_distance_log_21d_slope_v018_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log netinc
def bd_f055_breakeven_distance_log_63d_slope_v019_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log netinc
def bd_f055_breakeven_distance_log_63d_slope_v020_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log netinc
def bd_f055_breakeven_distance_log_63d_slope_v021_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log netinc
def bd_f055_breakeven_distance_log_126d_slope_v022_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log netinc
def bd_f055_breakeven_distance_log_126d_slope_v023_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log netinc
def bd_f055_breakeven_distance_log_126d_slope_v024_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log netinc
def bd_f055_breakeven_distance_log_252d_slope_v025_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log netinc
def bd_f055_breakeven_distance_log_252d_slope_v026_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log netinc
def bd_f055_breakeven_distance_log_252d_slope_v027_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log netinc
def bd_f055_breakeven_distance_log_504d_slope_v028_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log netinc
def bd_f055_breakeven_distance_log_504d_slope_v029_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log netinc
def bd_f055_breakeven_distance_log_504d_slope_v030_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare netinc
def bd_f055_breakeven_distance_pershare_21d_slope_v031_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare netinc
def bd_f055_breakeven_distance_pershare_21d_slope_v032_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare netinc
def bd_f055_breakeven_distance_pershare_21d_slope_v033_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare netinc
def bd_f055_breakeven_distance_pershare_63d_slope_v034_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare netinc
def bd_f055_breakeven_distance_pershare_63d_slope_v035_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare netinc
def bd_f055_breakeven_distance_pershare_63d_slope_v036_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare netinc
def bd_f055_breakeven_distance_pershare_126d_slope_v037_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare netinc
def bd_f055_breakeven_distance_pershare_126d_slope_v038_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare netinc
def bd_f055_breakeven_distance_pershare_126d_slope_v039_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare netinc
def bd_f055_breakeven_distance_pershare_252d_slope_v040_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare netinc
def bd_f055_breakeven_distance_pershare_252d_slope_v041_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare netinc
def bd_f055_breakeven_distance_pershare_252d_slope_v042_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare netinc
def bd_f055_breakeven_distance_pershare_504d_slope_v043_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare netinc
def bd_f055_breakeven_distance_pershare_504d_slope_v044_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare netinc
def bd_f055_breakeven_distance_pershare_504d_slope_v045_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_21d_slope_v046_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_21d_slope_v047_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_21d_slope_v048_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_63d_slope_v049_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_63d_slope_v050_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_63d_slope_v051_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_126d_slope_v052_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_126d_slope_v053_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_126d_slope_v054_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_252d_slope_v055_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_252d_slope_v056_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_252d_slope_v057_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_504d_slope_v058_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_504d_slope_v059_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_504d_slope_v060_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_21d_slope_v061_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_21d_slope_v062_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_21d_slope_v063_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_63d_slope_v064_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_63d_slope_v065_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_63d_slope_v066_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_126d_slope_v067_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_126d_slope_v068_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_126d_slope_v069_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_252d_slope_v070_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_252d_slope_v071_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_252d_slope_v072_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_504d_slope_v073_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_504d_slope_v074_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_504d_slope_v075_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets netinc
def bd_f055_breakeven_distance_per_assets_21d_slope_v076_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets netinc
def bd_f055_breakeven_distance_per_assets_21d_slope_v077_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets netinc
def bd_f055_breakeven_distance_per_assets_21d_slope_v078_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets netinc
def bd_f055_breakeven_distance_per_assets_63d_slope_v079_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets netinc
def bd_f055_breakeven_distance_per_assets_63d_slope_v080_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets netinc
def bd_f055_breakeven_distance_per_assets_63d_slope_v081_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets netinc
def bd_f055_breakeven_distance_per_assets_126d_slope_v082_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets netinc
def bd_f055_breakeven_distance_per_assets_126d_slope_v083_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets netinc
def bd_f055_breakeven_distance_per_assets_126d_slope_v084_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets netinc
def bd_f055_breakeven_distance_per_assets_252d_slope_v085_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets netinc
def bd_f055_breakeven_distance_per_assets_252d_slope_v086_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets netinc
def bd_f055_breakeven_distance_per_assets_252d_slope_v087_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets netinc
def bd_f055_breakeven_distance_per_assets_504d_slope_v088_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets netinc
def bd_f055_breakeven_distance_per_assets_504d_slope_v089_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets netinc
def bd_f055_breakeven_distance_per_assets_504d_slope_v090_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std netinc
def bd_f055_breakeven_distance_std_21d_slope_v091_signal(netinc, closeadj):
    base = _std(netinc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std netinc
def bd_f055_breakeven_distance_std_21d_slope_v092_signal(netinc, closeadj):
    base = _std(netinc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std netinc
def bd_f055_breakeven_distance_std_21d_slope_v093_signal(netinc, closeadj):
    base = _std(netinc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std netinc
def bd_f055_breakeven_distance_std_63d_slope_v094_signal(netinc, closeadj):
    base = _std(netinc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std netinc
def bd_f055_breakeven_distance_std_63d_slope_v095_signal(netinc, closeadj):
    base = _std(netinc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std netinc
def bd_f055_breakeven_distance_std_63d_slope_v096_signal(netinc, closeadj):
    base = _std(netinc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std netinc
def bd_f055_breakeven_distance_std_126d_slope_v097_signal(netinc, closeadj):
    base = _std(netinc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std netinc
def bd_f055_breakeven_distance_std_126d_slope_v098_signal(netinc, closeadj):
    base = _std(netinc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std netinc
def bd_f055_breakeven_distance_std_126d_slope_v099_signal(netinc, closeadj):
    base = _std(netinc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std netinc
def bd_f055_breakeven_distance_std_252d_slope_v100_signal(netinc, closeadj):
    base = _std(netinc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std netinc
def bd_f055_breakeven_distance_std_252d_slope_v101_signal(netinc, closeadj):
    base = _std(netinc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std netinc
def bd_f055_breakeven_distance_std_252d_slope_v102_signal(netinc, closeadj):
    base = _std(netinc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std netinc
def bd_f055_breakeven_distance_std_504d_slope_v103_signal(netinc, closeadj):
    base = _std(netinc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std netinc
def bd_f055_breakeven_distance_std_504d_slope_v104_signal(netinc, closeadj):
    base = _std(netinc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std netinc
def bd_f055_breakeven_distance_std_504d_slope_v105_signal(netinc, closeadj):
    base = _std(netinc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm netinc
def bd_f055_breakeven_distance_ewm_21d_slope_v106_signal(netinc, closeadj):
    base = netinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm netinc
def bd_f055_breakeven_distance_ewm_21d_slope_v107_signal(netinc, closeadj):
    base = netinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm netinc
def bd_f055_breakeven_distance_ewm_21d_slope_v108_signal(netinc, closeadj):
    base = netinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm netinc
def bd_f055_breakeven_distance_ewm_63d_slope_v109_signal(netinc, closeadj):
    base = netinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm netinc
def bd_f055_breakeven_distance_ewm_63d_slope_v110_signal(netinc, closeadj):
    base = netinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm netinc
def bd_f055_breakeven_distance_ewm_63d_slope_v111_signal(netinc, closeadj):
    base = netinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm netinc
def bd_f055_breakeven_distance_ewm_126d_slope_v112_signal(netinc, closeadj):
    base = netinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm netinc
def bd_f055_breakeven_distance_ewm_126d_slope_v113_signal(netinc, closeadj):
    base = netinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm netinc
def bd_f055_breakeven_distance_ewm_126d_slope_v114_signal(netinc, closeadj):
    base = netinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm netinc
def bd_f055_breakeven_distance_ewm_252d_slope_v115_signal(netinc, closeadj):
    base = netinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm netinc
def bd_f055_breakeven_distance_ewm_252d_slope_v116_signal(netinc, closeadj):
    base = netinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm netinc
def bd_f055_breakeven_distance_ewm_252d_slope_v117_signal(netinc, closeadj):
    base = netinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm netinc
def bd_f055_breakeven_distance_ewm_504d_slope_v118_signal(netinc, closeadj):
    base = netinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm netinc
def bd_f055_breakeven_distance_ewm_504d_slope_v119_signal(netinc, closeadj):
    base = netinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm netinc
def bd_f055_breakeven_distance_ewm_504d_slope_v120_signal(netinc, closeadj):
    base = netinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq netinc
def bd_f055_breakeven_distance_sq_21d_slope_v121_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq netinc
def bd_f055_breakeven_distance_sq_21d_slope_v122_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq netinc
def bd_f055_breakeven_distance_sq_21d_slope_v123_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq netinc
def bd_f055_breakeven_distance_sq_63d_slope_v124_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq netinc
def bd_f055_breakeven_distance_sq_63d_slope_v125_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq netinc
def bd_f055_breakeven_distance_sq_63d_slope_v126_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq netinc
def bd_f055_breakeven_distance_sq_126d_slope_v127_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq netinc
def bd_f055_breakeven_distance_sq_126d_slope_v128_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq netinc
def bd_f055_breakeven_distance_sq_126d_slope_v129_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq netinc
def bd_f055_breakeven_distance_sq_252d_slope_v130_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq netinc
def bd_f055_breakeven_distance_sq_252d_slope_v131_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq netinc
def bd_f055_breakeven_distance_sq_252d_slope_v132_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq netinc
def bd_f055_breakeven_distance_sq_504d_slope_v133_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq netinc
def bd_f055_breakeven_distance_sq_504d_slope_v134_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq netinc
def bd_f055_breakeven_distance_sq_504d_slope_v135_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z netinc
def bd_f055_breakeven_distance_z_21d_slope_v136_signal(netinc):
    base = _z(netinc, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z netinc
def bd_f055_breakeven_distance_z_21d_slope_v137_signal(netinc):
    base = _z(netinc, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z netinc
def bd_f055_breakeven_distance_z_21d_slope_v138_signal(netinc):
    base = _z(netinc, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z netinc
def bd_f055_breakeven_distance_z_63d_slope_v139_signal(netinc):
    base = _z(netinc, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z netinc
def bd_f055_breakeven_distance_z_63d_slope_v140_signal(netinc):
    base = _z(netinc, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z netinc
def bd_f055_breakeven_distance_z_63d_slope_v141_signal(netinc):
    base = _z(netinc, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z netinc
def bd_f055_breakeven_distance_z_126d_slope_v142_signal(netinc):
    base = _z(netinc, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z netinc
def bd_f055_breakeven_distance_z_126d_slope_v143_signal(netinc):
    base = _z(netinc, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z netinc
def bd_f055_breakeven_distance_z_126d_slope_v144_signal(netinc):
    base = _z(netinc, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z netinc
def bd_f055_breakeven_distance_z_252d_slope_v145_signal(netinc):
    base = _z(netinc, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z netinc
def bd_f055_breakeven_distance_z_252d_slope_v146_signal(netinc):
    base = _z(netinc, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z netinc
def bd_f055_breakeven_distance_z_252d_slope_v147_signal(netinc):
    base = _z(netinc, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z netinc
def bd_f055_breakeven_distance_z_504d_slope_v148_signal(netinc):
    base = _z(netinc, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z netinc
def bd_f055_breakeven_distance_z_504d_slope_v149_signal(netinc):
    base = _z(netinc, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z netinc
def bd_f055_breakeven_distance_z_504d_slope_v150_signal(netinc):
    base = _z(netinc, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
