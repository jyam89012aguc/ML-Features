"""Family f064 - Return on equity (Returns and Efficiency) | Sharadar tables: SF1 | fields: roe, netinc, equity | 3rd derivatives 001-150"""
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
def _return_on_equity_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _return_on_equity_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _return_on_equity_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw roe
def roe_f064_return_on_equity_raw_21d_accel_v001_signal(roe, closeadj):
    base = _mean(roe, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw roe
def roe_f064_return_on_equity_raw_21d_accel_v002_signal(roe, closeadj):
    base = _mean(roe, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw roe
def roe_f064_return_on_equity_raw_21d_accel_v003_signal(roe, closeadj):
    base = _mean(roe, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw roe
def roe_f064_return_on_equity_raw_63d_accel_v004_signal(roe, closeadj):
    base = _mean(roe, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw roe
def roe_f064_return_on_equity_raw_63d_accel_v005_signal(roe, closeadj):
    base = _mean(roe, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw roe
def roe_f064_return_on_equity_raw_63d_accel_v006_signal(roe, closeadj):
    base = _mean(roe, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw roe
def roe_f064_return_on_equity_raw_126d_accel_v007_signal(roe, closeadj):
    base = _mean(roe, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw roe
def roe_f064_return_on_equity_raw_126d_accel_v008_signal(roe, closeadj):
    base = _mean(roe, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw roe
def roe_f064_return_on_equity_raw_126d_accel_v009_signal(roe, closeadj):
    base = _mean(roe, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw roe
def roe_f064_return_on_equity_raw_252d_accel_v010_signal(roe, closeadj):
    base = _mean(roe, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw roe
def roe_f064_return_on_equity_raw_252d_accel_v011_signal(roe, closeadj):
    base = _mean(roe, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw roe
def roe_f064_return_on_equity_raw_252d_accel_v012_signal(roe, closeadj):
    base = _mean(roe, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw roe
def roe_f064_return_on_equity_raw_504d_accel_v013_signal(roe, closeadj):
    base = _mean(roe, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw roe
def roe_f064_return_on_equity_raw_504d_accel_v014_signal(roe, closeadj):
    base = _mean(roe, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw roe
def roe_f064_return_on_equity_raw_504d_accel_v015_signal(roe, closeadj):
    base = _mean(roe, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log roe
def roe_f064_return_on_equity_log_21d_accel_v016_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log roe
def roe_f064_return_on_equity_log_21d_accel_v017_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log roe
def roe_f064_return_on_equity_log_21d_accel_v018_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log roe
def roe_f064_return_on_equity_log_63d_accel_v019_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log roe
def roe_f064_return_on_equity_log_63d_accel_v020_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log roe
def roe_f064_return_on_equity_log_63d_accel_v021_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log roe
def roe_f064_return_on_equity_log_126d_accel_v022_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log roe
def roe_f064_return_on_equity_log_126d_accel_v023_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log roe
def roe_f064_return_on_equity_log_126d_accel_v024_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log roe
def roe_f064_return_on_equity_log_252d_accel_v025_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log roe
def roe_f064_return_on_equity_log_252d_accel_v026_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log roe
def roe_f064_return_on_equity_log_252d_accel_v027_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log roe
def roe_f064_return_on_equity_log_504d_accel_v028_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log roe
def roe_f064_return_on_equity_log_504d_accel_v029_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log roe
def roe_f064_return_on_equity_log_504d_accel_v030_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare roe
def roe_f064_return_on_equity_pershare_21d_accel_v031_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare roe
def roe_f064_return_on_equity_pershare_21d_accel_v032_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare roe
def roe_f064_return_on_equity_pershare_21d_accel_v033_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare roe
def roe_f064_return_on_equity_pershare_63d_accel_v034_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare roe
def roe_f064_return_on_equity_pershare_63d_accel_v035_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare roe
def roe_f064_return_on_equity_pershare_63d_accel_v036_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare roe
def roe_f064_return_on_equity_pershare_126d_accel_v037_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare roe
def roe_f064_return_on_equity_pershare_126d_accel_v038_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare roe
def roe_f064_return_on_equity_pershare_126d_accel_v039_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare roe
def roe_f064_return_on_equity_pershare_252d_accel_v040_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare roe
def roe_f064_return_on_equity_pershare_252d_accel_v041_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare roe
def roe_f064_return_on_equity_pershare_252d_accel_v042_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare roe
def roe_f064_return_on_equity_pershare_504d_accel_v043_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare roe
def roe_f064_return_on_equity_pershare_504d_accel_v044_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare roe
def roe_f064_return_on_equity_pershare_504d_accel_v045_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_netinc roe
def roe_f064_return_on_equity_per_netinc_21d_accel_v046_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_netinc roe
def roe_f064_return_on_equity_per_netinc_21d_accel_v047_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_netinc roe
def roe_f064_return_on_equity_per_netinc_21d_accel_v048_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_netinc roe
def roe_f064_return_on_equity_per_netinc_63d_accel_v049_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_netinc roe
def roe_f064_return_on_equity_per_netinc_63d_accel_v050_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_netinc roe
def roe_f064_return_on_equity_per_netinc_63d_accel_v051_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_netinc roe
def roe_f064_return_on_equity_per_netinc_126d_accel_v052_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_netinc roe
def roe_f064_return_on_equity_per_netinc_126d_accel_v053_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_netinc roe
def roe_f064_return_on_equity_per_netinc_126d_accel_v054_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_netinc roe
def roe_f064_return_on_equity_per_netinc_252d_accel_v055_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_netinc roe
def roe_f064_return_on_equity_per_netinc_252d_accel_v056_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_netinc roe
def roe_f064_return_on_equity_per_netinc_252d_accel_v057_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_netinc roe
def roe_f064_return_on_equity_per_netinc_504d_accel_v058_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_netinc roe
def roe_f064_return_on_equity_per_netinc_504d_accel_v059_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_netinc roe
def roe_f064_return_on_equity_per_netinc_504d_accel_v060_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity roe
def roe_f064_return_on_equity_per_equity_21d_accel_v061_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity roe
def roe_f064_return_on_equity_per_equity_21d_accel_v062_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity roe
def roe_f064_return_on_equity_per_equity_21d_accel_v063_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity roe
def roe_f064_return_on_equity_per_equity_63d_accel_v064_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity roe
def roe_f064_return_on_equity_per_equity_63d_accel_v065_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity roe
def roe_f064_return_on_equity_per_equity_63d_accel_v066_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity roe
def roe_f064_return_on_equity_per_equity_126d_accel_v067_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity roe
def roe_f064_return_on_equity_per_equity_126d_accel_v068_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity roe
def roe_f064_return_on_equity_per_equity_126d_accel_v069_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity roe
def roe_f064_return_on_equity_per_equity_252d_accel_v070_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity roe
def roe_f064_return_on_equity_per_equity_252d_accel_v071_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity roe
def roe_f064_return_on_equity_per_equity_252d_accel_v072_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity roe
def roe_f064_return_on_equity_per_equity_504d_accel_v073_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity roe
def roe_f064_return_on_equity_per_equity_504d_accel_v074_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity roe
def roe_f064_return_on_equity_per_equity_504d_accel_v075_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets roe
def roe_f064_return_on_equity_per_assets_21d_accel_v076_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets roe
def roe_f064_return_on_equity_per_assets_21d_accel_v077_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets roe
def roe_f064_return_on_equity_per_assets_21d_accel_v078_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets roe
def roe_f064_return_on_equity_per_assets_63d_accel_v079_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets roe
def roe_f064_return_on_equity_per_assets_63d_accel_v080_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets roe
def roe_f064_return_on_equity_per_assets_63d_accel_v081_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets roe
def roe_f064_return_on_equity_per_assets_126d_accel_v082_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets roe
def roe_f064_return_on_equity_per_assets_126d_accel_v083_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets roe
def roe_f064_return_on_equity_per_assets_126d_accel_v084_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets roe
def roe_f064_return_on_equity_per_assets_252d_accel_v085_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets roe
def roe_f064_return_on_equity_per_assets_252d_accel_v086_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets roe
def roe_f064_return_on_equity_per_assets_252d_accel_v087_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets roe
def roe_f064_return_on_equity_per_assets_504d_accel_v088_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets roe
def roe_f064_return_on_equity_per_assets_504d_accel_v089_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets roe
def roe_f064_return_on_equity_per_assets_504d_accel_v090_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std roe
def roe_f064_return_on_equity_std_21d_accel_v091_signal(roe, closeadj):
    base = _std(roe, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std roe
def roe_f064_return_on_equity_std_21d_accel_v092_signal(roe, closeadj):
    base = _std(roe, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std roe
def roe_f064_return_on_equity_std_21d_accel_v093_signal(roe, closeadj):
    base = _std(roe, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std roe
def roe_f064_return_on_equity_std_63d_accel_v094_signal(roe, closeadj):
    base = _std(roe, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std roe
def roe_f064_return_on_equity_std_63d_accel_v095_signal(roe, closeadj):
    base = _std(roe, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std roe
def roe_f064_return_on_equity_std_63d_accel_v096_signal(roe, closeadj):
    base = _std(roe, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std roe
def roe_f064_return_on_equity_std_126d_accel_v097_signal(roe, closeadj):
    base = _std(roe, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std roe
def roe_f064_return_on_equity_std_126d_accel_v098_signal(roe, closeadj):
    base = _std(roe, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std roe
def roe_f064_return_on_equity_std_126d_accel_v099_signal(roe, closeadj):
    base = _std(roe, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std roe
def roe_f064_return_on_equity_std_252d_accel_v100_signal(roe, closeadj):
    base = _std(roe, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std roe
def roe_f064_return_on_equity_std_252d_accel_v101_signal(roe, closeadj):
    base = _std(roe, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std roe
def roe_f064_return_on_equity_std_252d_accel_v102_signal(roe, closeadj):
    base = _std(roe, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std roe
def roe_f064_return_on_equity_std_504d_accel_v103_signal(roe, closeadj):
    base = _std(roe, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std roe
def roe_f064_return_on_equity_std_504d_accel_v104_signal(roe, closeadj):
    base = _std(roe, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std roe
def roe_f064_return_on_equity_std_504d_accel_v105_signal(roe, closeadj):
    base = _std(roe, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm roe
def roe_f064_return_on_equity_ewm_21d_accel_v106_signal(roe, closeadj):
    base = roe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm roe
def roe_f064_return_on_equity_ewm_21d_accel_v107_signal(roe, closeadj):
    base = roe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm roe
def roe_f064_return_on_equity_ewm_21d_accel_v108_signal(roe, closeadj):
    base = roe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm roe
def roe_f064_return_on_equity_ewm_63d_accel_v109_signal(roe, closeadj):
    base = roe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm roe
def roe_f064_return_on_equity_ewm_63d_accel_v110_signal(roe, closeadj):
    base = roe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm roe
def roe_f064_return_on_equity_ewm_63d_accel_v111_signal(roe, closeadj):
    base = roe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm roe
def roe_f064_return_on_equity_ewm_126d_accel_v112_signal(roe, closeadj):
    base = roe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm roe
def roe_f064_return_on_equity_ewm_126d_accel_v113_signal(roe, closeadj):
    base = roe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm roe
def roe_f064_return_on_equity_ewm_126d_accel_v114_signal(roe, closeadj):
    base = roe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm roe
def roe_f064_return_on_equity_ewm_252d_accel_v115_signal(roe, closeadj):
    base = roe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm roe
def roe_f064_return_on_equity_ewm_252d_accel_v116_signal(roe, closeadj):
    base = roe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm roe
def roe_f064_return_on_equity_ewm_252d_accel_v117_signal(roe, closeadj):
    base = roe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm roe
def roe_f064_return_on_equity_ewm_504d_accel_v118_signal(roe, closeadj):
    base = roe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm roe
def roe_f064_return_on_equity_ewm_504d_accel_v119_signal(roe, closeadj):
    base = roe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm roe
def roe_f064_return_on_equity_ewm_504d_accel_v120_signal(roe, closeadj):
    base = roe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq roe
def roe_f064_return_on_equity_sq_21d_accel_v121_signal(roe, closeadj):
    base = _mean(roe * roe, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq roe
def roe_f064_return_on_equity_sq_21d_accel_v122_signal(roe, closeadj):
    base = _mean(roe * roe, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq roe
def roe_f064_return_on_equity_sq_21d_accel_v123_signal(roe, closeadj):
    base = _mean(roe * roe, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq roe
def roe_f064_return_on_equity_sq_63d_accel_v124_signal(roe, closeadj):
    base = _mean(roe * roe, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq roe
def roe_f064_return_on_equity_sq_63d_accel_v125_signal(roe, closeadj):
    base = _mean(roe * roe, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq roe
def roe_f064_return_on_equity_sq_63d_accel_v126_signal(roe, closeadj):
    base = _mean(roe * roe, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq roe
def roe_f064_return_on_equity_sq_126d_accel_v127_signal(roe, closeadj):
    base = _mean(roe * roe, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq roe
def roe_f064_return_on_equity_sq_126d_accel_v128_signal(roe, closeadj):
    base = _mean(roe * roe, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq roe
def roe_f064_return_on_equity_sq_126d_accel_v129_signal(roe, closeadj):
    base = _mean(roe * roe, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq roe
def roe_f064_return_on_equity_sq_252d_accel_v130_signal(roe, closeadj):
    base = _mean(roe * roe, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq roe
def roe_f064_return_on_equity_sq_252d_accel_v131_signal(roe, closeadj):
    base = _mean(roe * roe, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq roe
def roe_f064_return_on_equity_sq_252d_accel_v132_signal(roe, closeadj):
    base = _mean(roe * roe, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq roe
def roe_f064_return_on_equity_sq_504d_accel_v133_signal(roe, closeadj):
    base = _mean(roe * roe, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq roe
def roe_f064_return_on_equity_sq_504d_accel_v134_signal(roe, closeadj):
    base = _mean(roe * roe, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq roe
def roe_f064_return_on_equity_sq_504d_accel_v135_signal(roe, closeadj):
    base = _mean(roe * roe, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z roe
def roe_f064_return_on_equity_z_21d_accel_v136_signal(roe):
    base = _z(roe, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z roe
def roe_f064_return_on_equity_z_21d_accel_v137_signal(roe):
    base = _z(roe, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z roe
def roe_f064_return_on_equity_z_21d_accel_v138_signal(roe):
    base = _z(roe, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z roe
def roe_f064_return_on_equity_z_63d_accel_v139_signal(roe):
    base = _z(roe, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z roe
def roe_f064_return_on_equity_z_63d_accel_v140_signal(roe):
    base = _z(roe, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z roe
def roe_f064_return_on_equity_z_63d_accel_v141_signal(roe):
    base = _z(roe, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z roe
def roe_f064_return_on_equity_z_126d_accel_v142_signal(roe):
    base = _z(roe, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z roe
def roe_f064_return_on_equity_z_126d_accel_v143_signal(roe):
    base = _z(roe, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z roe
def roe_f064_return_on_equity_z_126d_accel_v144_signal(roe):
    base = _z(roe, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z roe
def roe_f064_return_on_equity_z_252d_accel_v145_signal(roe):
    base = _z(roe, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z roe
def roe_f064_return_on_equity_z_252d_accel_v146_signal(roe):
    base = _z(roe, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z roe
def roe_f064_return_on_equity_z_252d_accel_v147_signal(roe):
    base = _z(roe, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z roe
def roe_f064_return_on_equity_z_504d_accel_v148_signal(roe):
    base = _z(roe, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z roe
def roe_f064_return_on_equity_z_504d_accel_v149_signal(roe):
    base = _z(roe, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z roe
def roe_f064_return_on_equity_z_504d_accel_v150_signal(roe):
    base = _z(roe, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
