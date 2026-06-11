"""Family f055 - Distance to breakeven (Margins and Profitability) | Sharadar tables: SF1 | fields: netinc, opinc, revenue, opex | 3rd derivatives 001-150"""
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


# 5d accel of 21d raw netinc
def bd_f055_breakeven_distance_raw_21d_accel_v001_signal(netinc, closeadj):
    base = _mean(netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw netinc
def bd_f055_breakeven_distance_raw_21d_accel_v002_signal(netinc, closeadj):
    base = _mean(netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw netinc
def bd_f055_breakeven_distance_raw_21d_accel_v003_signal(netinc, closeadj):
    base = _mean(netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw netinc
def bd_f055_breakeven_distance_raw_63d_accel_v004_signal(netinc, closeadj):
    base = _mean(netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw netinc
def bd_f055_breakeven_distance_raw_63d_accel_v005_signal(netinc, closeadj):
    base = _mean(netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw netinc
def bd_f055_breakeven_distance_raw_63d_accel_v006_signal(netinc, closeadj):
    base = _mean(netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw netinc
def bd_f055_breakeven_distance_raw_126d_accel_v007_signal(netinc, closeadj):
    base = _mean(netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw netinc
def bd_f055_breakeven_distance_raw_126d_accel_v008_signal(netinc, closeadj):
    base = _mean(netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw netinc
def bd_f055_breakeven_distance_raw_126d_accel_v009_signal(netinc, closeadj):
    base = _mean(netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw netinc
def bd_f055_breakeven_distance_raw_252d_accel_v010_signal(netinc, closeadj):
    base = _mean(netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw netinc
def bd_f055_breakeven_distance_raw_252d_accel_v011_signal(netinc, closeadj):
    base = _mean(netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw netinc
def bd_f055_breakeven_distance_raw_252d_accel_v012_signal(netinc, closeadj):
    base = _mean(netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw netinc
def bd_f055_breakeven_distance_raw_504d_accel_v013_signal(netinc, closeadj):
    base = _mean(netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw netinc
def bd_f055_breakeven_distance_raw_504d_accel_v014_signal(netinc, closeadj):
    base = _mean(netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw netinc
def bd_f055_breakeven_distance_raw_504d_accel_v015_signal(netinc, closeadj):
    base = _mean(netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log netinc
def bd_f055_breakeven_distance_log_21d_accel_v016_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log netinc
def bd_f055_breakeven_distance_log_21d_accel_v017_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log netinc
def bd_f055_breakeven_distance_log_21d_accel_v018_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log netinc
def bd_f055_breakeven_distance_log_63d_accel_v019_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log netinc
def bd_f055_breakeven_distance_log_63d_accel_v020_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log netinc
def bd_f055_breakeven_distance_log_63d_accel_v021_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log netinc
def bd_f055_breakeven_distance_log_126d_accel_v022_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log netinc
def bd_f055_breakeven_distance_log_126d_accel_v023_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log netinc
def bd_f055_breakeven_distance_log_126d_accel_v024_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log netinc
def bd_f055_breakeven_distance_log_252d_accel_v025_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log netinc
def bd_f055_breakeven_distance_log_252d_accel_v026_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log netinc
def bd_f055_breakeven_distance_log_252d_accel_v027_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log netinc
def bd_f055_breakeven_distance_log_504d_accel_v028_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log netinc
def bd_f055_breakeven_distance_log_504d_accel_v029_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log netinc
def bd_f055_breakeven_distance_log_504d_accel_v030_signal(netinc, closeadj):
    base = _mean(_breakeven_distance_log(netinc), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare netinc
def bd_f055_breakeven_distance_pershare_21d_accel_v031_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare netinc
def bd_f055_breakeven_distance_pershare_21d_accel_v032_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare netinc
def bd_f055_breakeven_distance_pershare_21d_accel_v033_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare netinc
def bd_f055_breakeven_distance_pershare_63d_accel_v034_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare netinc
def bd_f055_breakeven_distance_pershare_63d_accel_v035_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare netinc
def bd_f055_breakeven_distance_pershare_63d_accel_v036_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare netinc
def bd_f055_breakeven_distance_pershare_126d_accel_v037_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare netinc
def bd_f055_breakeven_distance_pershare_126d_accel_v038_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare netinc
def bd_f055_breakeven_distance_pershare_126d_accel_v039_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare netinc
def bd_f055_breakeven_distance_pershare_252d_accel_v040_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare netinc
def bd_f055_breakeven_distance_pershare_252d_accel_v041_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare netinc
def bd_f055_breakeven_distance_pershare_252d_accel_v042_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare netinc
def bd_f055_breakeven_distance_pershare_504d_accel_v043_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare netinc
def bd_f055_breakeven_distance_pershare_504d_accel_v044_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare netinc
def bd_f055_breakeven_distance_pershare_504d_accel_v045_signal(netinc, sharesbas, closeadj):
    base = _mean(_breakeven_distance_per_share(netinc, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_21d_accel_v046_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_21d_accel_v047_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_21d_accel_v048_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_63d_accel_v049_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_63d_accel_v050_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_63d_accel_v051_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_126d_accel_v052_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_126d_accel_v053_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_126d_accel_v054_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_252d_accel_v055_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_252d_accel_v056_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_252d_accel_v057_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_504d_accel_v058_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_504d_accel_v059_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_opinc netinc
def bd_f055_breakeven_distance_per_opinc_504d_accel_v060_signal(netinc, opinc):
    base = _mean(_breakeven_distance_scaled(netinc, opinc), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_21d_accel_v061_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_21d_accel_v062_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_21d_accel_v063_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_63d_accel_v064_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_63d_accel_v065_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_63d_accel_v066_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_126d_accel_v067_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_126d_accel_v068_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_126d_accel_v069_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_252d_accel_v070_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_252d_accel_v071_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_252d_accel_v072_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_504d_accel_v073_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_504d_accel_v074_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_revenue netinc
def bd_f055_breakeven_distance_per_revenue_504d_accel_v075_signal(netinc, revenue):
    base = _mean(_breakeven_distance_scaled(netinc, revenue), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets netinc
def bd_f055_breakeven_distance_per_assets_21d_accel_v076_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets netinc
def bd_f055_breakeven_distance_per_assets_21d_accel_v077_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets netinc
def bd_f055_breakeven_distance_per_assets_21d_accel_v078_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets netinc
def bd_f055_breakeven_distance_per_assets_63d_accel_v079_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets netinc
def bd_f055_breakeven_distance_per_assets_63d_accel_v080_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets netinc
def bd_f055_breakeven_distance_per_assets_63d_accel_v081_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets netinc
def bd_f055_breakeven_distance_per_assets_126d_accel_v082_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets netinc
def bd_f055_breakeven_distance_per_assets_126d_accel_v083_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets netinc
def bd_f055_breakeven_distance_per_assets_126d_accel_v084_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets netinc
def bd_f055_breakeven_distance_per_assets_252d_accel_v085_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets netinc
def bd_f055_breakeven_distance_per_assets_252d_accel_v086_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets netinc
def bd_f055_breakeven_distance_per_assets_252d_accel_v087_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets netinc
def bd_f055_breakeven_distance_per_assets_504d_accel_v088_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets netinc
def bd_f055_breakeven_distance_per_assets_504d_accel_v089_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets netinc
def bd_f055_breakeven_distance_per_assets_504d_accel_v090_signal(netinc, assets):
    base = _mean(_breakeven_distance_scaled(netinc, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std netinc
def bd_f055_breakeven_distance_std_21d_accel_v091_signal(netinc, closeadj):
    base = _std(netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std netinc
def bd_f055_breakeven_distance_std_21d_accel_v092_signal(netinc, closeadj):
    base = _std(netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std netinc
def bd_f055_breakeven_distance_std_21d_accel_v093_signal(netinc, closeadj):
    base = _std(netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std netinc
def bd_f055_breakeven_distance_std_63d_accel_v094_signal(netinc, closeadj):
    base = _std(netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std netinc
def bd_f055_breakeven_distance_std_63d_accel_v095_signal(netinc, closeadj):
    base = _std(netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std netinc
def bd_f055_breakeven_distance_std_63d_accel_v096_signal(netinc, closeadj):
    base = _std(netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std netinc
def bd_f055_breakeven_distance_std_126d_accel_v097_signal(netinc, closeadj):
    base = _std(netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std netinc
def bd_f055_breakeven_distance_std_126d_accel_v098_signal(netinc, closeadj):
    base = _std(netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std netinc
def bd_f055_breakeven_distance_std_126d_accel_v099_signal(netinc, closeadj):
    base = _std(netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std netinc
def bd_f055_breakeven_distance_std_252d_accel_v100_signal(netinc, closeadj):
    base = _std(netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std netinc
def bd_f055_breakeven_distance_std_252d_accel_v101_signal(netinc, closeadj):
    base = _std(netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std netinc
def bd_f055_breakeven_distance_std_252d_accel_v102_signal(netinc, closeadj):
    base = _std(netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std netinc
def bd_f055_breakeven_distance_std_504d_accel_v103_signal(netinc, closeadj):
    base = _std(netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std netinc
def bd_f055_breakeven_distance_std_504d_accel_v104_signal(netinc, closeadj):
    base = _std(netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std netinc
def bd_f055_breakeven_distance_std_504d_accel_v105_signal(netinc, closeadj):
    base = _std(netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm netinc
def bd_f055_breakeven_distance_ewm_21d_accel_v106_signal(netinc, closeadj):
    base = netinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm netinc
def bd_f055_breakeven_distance_ewm_21d_accel_v107_signal(netinc, closeadj):
    base = netinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm netinc
def bd_f055_breakeven_distance_ewm_21d_accel_v108_signal(netinc, closeadj):
    base = netinc.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm netinc
def bd_f055_breakeven_distance_ewm_63d_accel_v109_signal(netinc, closeadj):
    base = netinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm netinc
def bd_f055_breakeven_distance_ewm_63d_accel_v110_signal(netinc, closeadj):
    base = netinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm netinc
def bd_f055_breakeven_distance_ewm_63d_accel_v111_signal(netinc, closeadj):
    base = netinc.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm netinc
def bd_f055_breakeven_distance_ewm_126d_accel_v112_signal(netinc, closeadj):
    base = netinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm netinc
def bd_f055_breakeven_distance_ewm_126d_accel_v113_signal(netinc, closeadj):
    base = netinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm netinc
def bd_f055_breakeven_distance_ewm_126d_accel_v114_signal(netinc, closeadj):
    base = netinc.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm netinc
def bd_f055_breakeven_distance_ewm_252d_accel_v115_signal(netinc, closeadj):
    base = netinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm netinc
def bd_f055_breakeven_distance_ewm_252d_accel_v116_signal(netinc, closeadj):
    base = netinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm netinc
def bd_f055_breakeven_distance_ewm_252d_accel_v117_signal(netinc, closeadj):
    base = netinc.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm netinc
def bd_f055_breakeven_distance_ewm_504d_accel_v118_signal(netinc, closeadj):
    base = netinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm netinc
def bd_f055_breakeven_distance_ewm_504d_accel_v119_signal(netinc, closeadj):
    base = netinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm netinc
def bd_f055_breakeven_distance_ewm_504d_accel_v120_signal(netinc, closeadj):
    base = netinc.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq netinc
def bd_f055_breakeven_distance_sq_21d_accel_v121_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq netinc
def bd_f055_breakeven_distance_sq_21d_accel_v122_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq netinc
def bd_f055_breakeven_distance_sq_21d_accel_v123_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq netinc
def bd_f055_breakeven_distance_sq_63d_accel_v124_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq netinc
def bd_f055_breakeven_distance_sq_63d_accel_v125_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq netinc
def bd_f055_breakeven_distance_sq_63d_accel_v126_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq netinc
def bd_f055_breakeven_distance_sq_126d_accel_v127_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq netinc
def bd_f055_breakeven_distance_sq_126d_accel_v128_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq netinc
def bd_f055_breakeven_distance_sq_126d_accel_v129_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq netinc
def bd_f055_breakeven_distance_sq_252d_accel_v130_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq netinc
def bd_f055_breakeven_distance_sq_252d_accel_v131_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq netinc
def bd_f055_breakeven_distance_sq_252d_accel_v132_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq netinc
def bd_f055_breakeven_distance_sq_504d_accel_v133_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq netinc
def bd_f055_breakeven_distance_sq_504d_accel_v134_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq netinc
def bd_f055_breakeven_distance_sq_504d_accel_v135_signal(netinc, closeadj):
    base = _mean(netinc * netinc, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z netinc
def bd_f055_breakeven_distance_z_21d_accel_v136_signal(netinc):
    base = _z(netinc, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z netinc
def bd_f055_breakeven_distance_z_21d_accel_v137_signal(netinc):
    base = _z(netinc, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z netinc
def bd_f055_breakeven_distance_z_21d_accel_v138_signal(netinc):
    base = _z(netinc, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z netinc
def bd_f055_breakeven_distance_z_63d_accel_v139_signal(netinc):
    base = _z(netinc, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z netinc
def bd_f055_breakeven_distance_z_63d_accel_v140_signal(netinc):
    base = _z(netinc, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z netinc
def bd_f055_breakeven_distance_z_63d_accel_v141_signal(netinc):
    base = _z(netinc, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z netinc
def bd_f055_breakeven_distance_z_126d_accel_v142_signal(netinc):
    base = _z(netinc, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z netinc
def bd_f055_breakeven_distance_z_126d_accel_v143_signal(netinc):
    base = _z(netinc, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z netinc
def bd_f055_breakeven_distance_z_126d_accel_v144_signal(netinc):
    base = _z(netinc, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z netinc
def bd_f055_breakeven_distance_z_252d_accel_v145_signal(netinc):
    base = _z(netinc, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z netinc
def bd_f055_breakeven_distance_z_252d_accel_v146_signal(netinc):
    base = _z(netinc, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z netinc
def bd_f055_breakeven_distance_z_252d_accel_v147_signal(netinc):
    base = _z(netinc, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z netinc
def bd_f055_breakeven_distance_z_504d_accel_v148_signal(netinc):
    base = _z(netinc, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z netinc
def bd_f055_breakeven_distance_z_504d_accel_v149_signal(netinc):
    base = _z(netinc, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z netinc
def bd_f055_breakeven_distance_z_504d_accel_v150_signal(netinc):
    base = _z(netinc, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
