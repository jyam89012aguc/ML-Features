"""Family f064 - Return on equity (Returns and Efficiency) | Sharadar tables: SF1 | fields: roe, netinc, equity | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw roe
def roe_f064_return_on_equity_raw_21d_slope_v001_signal(roe, closeadj):
    base = _mean(roe, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw roe
def roe_f064_return_on_equity_raw_21d_slope_v002_signal(roe, closeadj):
    base = _mean(roe, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw roe
def roe_f064_return_on_equity_raw_21d_slope_v003_signal(roe, closeadj):
    base = _mean(roe, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw roe
def roe_f064_return_on_equity_raw_63d_slope_v004_signal(roe, closeadj):
    base = _mean(roe, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw roe
def roe_f064_return_on_equity_raw_63d_slope_v005_signal(roe, closeadj):
    base = _mean(roe, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw roe
def roe_f064_return_on_equity_raw_63d_slope_v006_signal(roe, closeadj):
    base = _mean(roe, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw roe
def roe_f064_return_on_equity_raw_126d_slope_v007_signal(roe, closeadj):
    base = _mean(roe, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw roe
def roe_f064_return_on_equity_raw_126d_slope_v008_signal(roe, closeadj):
    base = _mean(roe, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw roe
def roe_f064_return_on_equity_raw_126d_slope_v009_signal(roe, closeadj):
    base = _mean(roe, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw roe
def roe_f064_return_on_equity_raw_252d_slope_v010_signal(roe, closeadj):
    base = _mean(roe, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw roe
def roe_f064_return_on_equity_raw_252d_slope_v011_signal(roe, closeadj):
    base = _mean(roe, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw roe
def roe_f064_return_on_equity_raw_252d_slope_v012_signal(roe, closeadj):
    base = _mean(roe, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw roe
def roe_f064_return_on_equity_raw_504d_slope_v013_signal(roe, closeadj):
    base = _mean(roe, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw roe
def roe_f064_return_on_equity_raw_504d_slope_v014_signal(roe, closeadj):
    base = _mean(roe, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw roe
def roe_f064_return_on_equity_raw_504d_slope_v015_signal(roe, closeadj):
    base = _mean(roe, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log roe
def roe_f064_return_on_equity_log_21d_slope_v016_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log roe
def roe_f064_return_on_equity_log_21d_slope_v017_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log roe
def roe_f064_return_on_equity_log_21d_slope_v018_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log roe
def roe_f064_return_on_equity_log_63d_slope_v019_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log roe
def roe_f064_return_on_equity_log_63d_slope_v020_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log roe
def roe_f064_return_on_equity_log_63d_slope_v021_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log roe
def roe_f064_return_on_equity_log_126d_slope_v022_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log roe
def roe_f064_return_on_equity_log_126d_slope_v023_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log roe
def roe_f064_return_on_equity_log_126d_slope_v024_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log roe
def roe_f064_return_on_equity_log_252d_slope_v025_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log roe
def roe_f064_return_on_equity_log_252d_slope_v026_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log roe
def roe_f064_return_on_equity_log_252d_slope_v027_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log roe
def roe_f064_return_on_equity_log_504d_slope_v028_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log roe
def roe_f064_return_on_equity_log_504d_slope_v029_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log roe
def roe_f064_return_on_equity_log_504d_slope_v030_signal(roe, closeadj):
    base = _mean(_return_on_equity_log(roe), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare roe
def roe_f064_return_on_equity_pershare_21d_slope_v031_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare roe
def roe_f064_return_on_equity_pershare_21d_slope_v032_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare roe
def roe_f064_return_on_equity_pershare_21d_slope_v033_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare roe
def roe_f064_return_on_equity_pershare_63d_slope_v034_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare roe
def roe_f064_return_on_equity_pershare_63d_slope_v035_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare roe
def roe_f064_return_on_equity_pershare_63d_slope_v036_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare roe
def roe_f064_return_on_equity_pershare_126d_slope_v037_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare roe
def roe_f064_return_on_equity_pershare_126d_slope_v038_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare roe
def roe_f064_return_on_equity_pershare_126d_slope_v039_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare roe
def roe_f064_return_on_equity_pershare_252d_slope_v040_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare roe
def roe_f064_return_on_equity_pershare_252d_slope_v041_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare roe
def roe_f064_return_on_equity_pershare_252d_slope_v042_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare roe
def roe_f064_return_on_equity_pershare_504d_slope_v043_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare roe
def roe_f064_return_on_equity_pershare_504d_slope_v044_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare roe
def roe_f064_return_on_equity_pershare_504d_slope_v045_signal(roe, sharesbas, closeadj):
    base = _mean(_return_on_equity_per_share(roe, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_netinc roe
def roe_f064_return_on_equity_per_netinc_21d_slope_v046_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_netinc roe
def roe_f064_return_on_equity_per_netinc_21d_slope_v047_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_netinc roe
def roe_f064_return_on_equity_per_netinc_21d_slope_v048_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_netinc roe
def roe_f064_return_on_equity_per_netinc_63d_slope_v049_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_netinc roe
def roe_f064_return_on_equity_per_netinc_63d_slope_v050_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_netinc roe
def roe_f064_return_on_equity_per_netinc_63d_slope_v051_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_netinc roe
def roe_f064_return_on_equity_per_netinc_126d_slope_v052_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_netinc roe
def roe_f064_return_on_equity_per_netinc_126d_slope_v053_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_netinc roe
def roe_f064_return_on_equity_per_netinc_126d_slope_v054_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_netinc roe
def roe_f064_return_on_equity_per_netinc_252d_slope_v055_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_netinc roe
def roe_f064_return_on_equity_per_netinc_252d_slope_v056_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_netinc roe
def roe_f064_return_on_equity_per_netinc_252d_slope_v057_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_netinc roe
def roe_f064_return_on_equity_per_netinc_504d_slope_v058_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_netinc roe
def roe_f064_return_on_equity_per_netinc_504d_slope_v059_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_netinc roe
def roe_f064_return_on_equity_per_netinc_504d_slope_v060_signal(roe, netinc):
    base = _mean(_return_on_equity_scaled(roe, netinc), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity roe
def roe_f064_return_on_equity_per_equity_21d_slope_v061_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity roe
def roe_f064_return_on_equity_per_equity_21d_slope_v062_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity roe
def roe_f064_return_on_equity_per_equity_21d_slope_v063_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity roe
def roe_f064_return_on_equity_per_equity_63d_slope_v064_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity roe
def roe_f064_return_on_equity_per_equity_63d_slope_v065_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity roe
def roe_f064_return_on_equity_per_equity_63d_slope_v066_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity roe
def roe_f064_return_on_equity_per_equity_126d_slope_v067_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity roe
def roe_f064_return_on_equity_per_equity_126d_slope_v068_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity roe
def roe_f064_return_on_equity_per_equity_126d_slope_v069_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity roe
def roe_f064_return_on_equity_per_equity_252d_slope_v070_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity roe
def roe_f064_return_on_equity_per_equity_252d_slope_v071_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity roe
def roe_f064_return_on_equity_per_equity_252d_slope_v072_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity roe
def roe_f064_return_on_equity_per_equity_504d_slope_v073_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity roe
def roe_f064_return_on_equity_per_equity_504d_slope_v074_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity roe
def roe_f064_return_on_equity_per_equity_504d_slope_v075_signal(roe, equity):
    base = _mean(_return_on_equity_scaled(roe, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets roe
def roe_f064_return_on_equity_per_assets_21d_slope_v076_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets roe
def roe_f064_return_on_equity_per_assets_21d_slope_v077_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets roe
def roe_f064_return_on_equity_per_assets_21d_slope_v078_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets roe
def roe_f064_return_on_equity_per_assets_63d_slope_v079_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets roe
def roe_f064_return_on_equity_per_assets_63d_slope_v080_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets roe
def roe_f064_return_on_equity_per_assets_63d_slope_v081_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets roe
def roe_f064_return_on_equity_per_assets_126d_slope_v082_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets roe
def roe_f064_return_on_equity_per_assets_126d_slope_v083_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets roe
def roe_f064_return_on_equity_per_assets_126d_slope_v084_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets roe
def roe_f064_return_on_equity_per_assets_252d_slope_v085_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets roe
def roe_f064_return_on_equity_per_assets_252d_slope_v086_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets roe
def roe_f064_return_on_equity_per_assets_252d_slope_v087_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets roe
def roe_f064_return_on_equity_per_assets_504d_slope_v088_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets roe
def roe_f064_return_on_equity_per_assets_504d_slope_v089_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets roe
def roe_f064_return_on_equity_per_assets_504d_slope_v090_signal(roe, assets):
    base = _mean(_return_on_equity_scaled(roe, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std roe
def roe_f064_return_on_equity_std_21d_slope_v091_signal(roe, closeadj):
    base = _std(roe, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std roe
def roe_f064_return_on_equity_std_21d_slope_v092_signal(roe, closeadj):
    base = _std(roe, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std roe
def roe_f064_return_on_equity_std_21d_slope_v093_signal(roe, closeadj):
    base = _std(roe, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std roe
def roe_f064_return_on_equity_std_63d_slope_v094_signal(roe, closeadj):
    base = _std(roe, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std roe
def roe_f064_return_on_equity_std_63d_slope_v095_signal(roe, closeadj):
    base = _std(roe, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std roe
def roe_f064_return_on_equity_std_63d_slope_v096_signal(roe, closeadj):
    base = _std(roe, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std roe
def roe_f064_return_on_equity_std_126d_slope_v097_signal(roe, closeadj):
    base = _std(roe, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std roe
def roe_f064_return_on_equity_std_126d_slope_v098_signal(roe, closeadj):
    base = _std(roe, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std roe
def roe_f064_return_on_equity_std_126d_slope_v099_signal(roe, closeadj):
    base = _std(roe, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std roe
def roe_f064_return_on_equity_std_252d_slope_v100_signal(roe, closeadj):
    base = _std(roe, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std roe
def roe_f064_return_on_equity_std_252d_slope_v101_signal(roe, closeadj):
    base = _std(roe, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std roe
def roe_f064_return_on_equity_std_252d_slope_v102_signal(roe, closeadj):
    base = _std(roe, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std roe
def roe_f064_return_on_equity_std_504d_slope_v103_signal(roe, closeadj):
    base = _std(roe, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std roe
def roe_f064_return_on_equity_std_504d_slope_v104_signal(roe, closeadj):
    base = _std(roe, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std roe
def roe_f064_return_on_equity_std_504d_slope_v105_signal(roe, closeadj):
    base = _std(roe, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm roe
def roe_f064_return_on_equity_ewm_21d_slope_v106_signal(roe, closeadj):
    base = roe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm roe
def roe_f064_return_on_equity_ewm_21d_slope_v107_signal(roe, closeadj):
    base = roe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm roe
def roe_f064_return_on_equity_ewm_21d_slope_v108_signal(roe, closeadj):
    base = roe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm roe
def roe_f064_return_on_equity_ewm_63d_slope_v109_signal(roe, closeadj):
    base = roe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm roe
def roe_f064_return_on_equity_ewm_63d_slope_v110_signal(roe, closeadj):
    base = roe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm roe
def roe_f064_return_on_equity_ewm_63d_slope_v111_signal(roe, closeadj):
    base = roe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm roe
def roe_f064_return_on_equity_ewm_126d_slope_v112_signal(roe, closeadj):
    base = roe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm roe
def roe_f064_return_on_equity_ewm_126d_slope_v113_signal(roe, closeadj):
    base = roe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm roe
def roe_f064_return_on_equity_ewm_126d_slope_v114_signal(roe, closeadj):
    base = roe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm roe
def roe_f064_return_on_equity_ewm_252d_slope_v115_signal(roe, closeadj):
    base = roe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm roe
def roe_f064_return_on_equity_ewm_252d_slope_v116_signal(roe, closeadj):
    base = roe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm roe
def roe_f064_return_on_equity_ewm_252d_slope_v117_signal(roe, closeadj):
    base = roe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm roe
def roe_f064_return_on_equity_ewm_504d_slope_v118_signal(roe, closeadj):
    base = roe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm roe
def roe_f064_return_on_equity_ewm_504d_slope_v119_signal(roe, closeadj):
    base = roe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm roe
def roe_f064_return_on_equity_ewm_504d_slope_v120_signal(roe, closeadj):
    base = roe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq roe
def roe_f064_return_on_equity_sq_21d_slope_v121_signal(roe, closeadj):
    base = _mean(roe * roe, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq roe
def roe_f064_return_on_equity_sq_21d_slope_v122_signal(roe, closeadj):
    base = _mean(roe * roe, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq roe
def roe_f064_return_on_equity_sq_21d_slope_v123_signal(roe, closeadj):
    base = _mean(roe * roe, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq roe
def roe_f064_return_on_equity_sq_63d_slope_v124_signal(roe, closeadj):
    base = _mean(roe * roe, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq roe
def roe_f064_return_on_equity_sq_63d_slope_v125_signal(roe, closeadj):
    base = _mean(roe * roe, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq roe
def roe_f064_return_on_equity_sq_63d_slope_v126_signal(roe, closeadj):
    base = _mean(roe * roe, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq roe
def roe_f064_return_on_equity_sq_126d_slope_v127_signal(roe, closeadj):
    base = _mean(roe * roe, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq roe
def roe_f064_return_on_equity_sq_126d_slope_v128_signal(roe, closeadj):
    base = _mean(roe * roe, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq roe
def roe_f064_return_on_equity_sq_126d_slope_v129_signal(roe, closeadj):
    base = _mean(roe * roe, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq roe
def roe_f064_return_on_equity_sq_252d_slope_v130_signal(roe, closeadj):
    base = _mean(roe * roe, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq roe
def roe_f064_return_on_equity_sq_252d_slope_v131_signal(roe, closeadj):
    base = _mean(roe * roe, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq roe
def roe_f064_return_on_equity_sq_252d_slope_v132_signal(roe, closeadj):
    base = _mean(roe * roe, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq roe
def roe_f064_return_on_equity_sq_504d_slope_v133_signal(roe, closeadj):
    base = _mean(roe * roe, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq roe
def roe_f064_return_on_equity_sq_504d_slope_v134_signal(roe, closeadj):
    base = _mean(roe * roe, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq roe
def roe_f064_return_on_equity_sq_504d_slope_v135_signal(roe, closeadj):
    base = _mean(roe * roe, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z roe
def roe_f064_return_on_equity_z_21d_slope_v136_signal(roe):
    base = _z(roe, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z roe
def roe_f064_return_on_equity_z_21d_slope_v137_signal(roe):
    base = _z(roe, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z roe
def roe_f064_return_on_equity_z_21d_slope_v138_signal(roe):
    base = _z(roe, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z roe
def roe_f064_return_on_equity_z_63d_slope_v139_signal(roe):
    base = _z(roe, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z roe
def roe_f064_return_on_equity_z_63d_slope_v140_signal(roe):
    base = _z(roe, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z roe
def roe_f064_return_on_equity_z_63d_slope_v141_signal(roe):
    base = _z(roe, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z roe
def roe_f064_return_on_equity_z_126d_slope_v142_signal(roe):
    base = _z(roe, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z roe
def roe_f064_return_on_equity_z_126d_slope_v143_signal(roe):
    base = _z(roe, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z roe
def roe_f064_return_on_equity_z_126d_slope_v144_signal(roe):
    base = _z(roe, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z roe
def roe_f064_return_on_equity_z_252d_slope_v145_signal(roe):
    base = _z(roe, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z roe
def roe_f064_return_on_equity_z_252d_slope_v146_signal(roe):
    base = _z(roe, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z roe
def roe_f064_return_on_equity_z_252d_slope_v147_signal(roe):
    base = _z(roe, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z roe
def roe_f064_return_on_equity_z_504d_slope_v148_signal(roe):
    base = _z(roe, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z roe
def roe_f064_return_on_equity_z_504d_slope_v149_signal(roe):
    base = _z(roe, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z roe
def roe_f064_return_on_equity_z_504d_slope_v150_signal(roe):
    base = _z(roe, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
