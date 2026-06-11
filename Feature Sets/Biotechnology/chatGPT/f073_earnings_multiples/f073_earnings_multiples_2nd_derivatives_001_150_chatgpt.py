"""Family f073 - Earnings and EBITDA multiples (Valuation Multiples) | Sharadar tables: SF1,DAILY | fields: pe, evebit, evebitda, ebit, ebitda | 2nd derivatives 001-150"""
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
def _earnings_multiples_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _earnings_multiples_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _earnings_multiples_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw pe
def em_f073_earnings_multiples_raw_21d_slope_v001_signal(pe, closeadj):
    base = _mean(pe, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw pe
def em_f073_earnings_multiples_raw_21d_slope_v002_signal(pe, closeadj):
    base = _mean(pe, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw pe
def em_f073_earnings_multiples_raw_21d_slope_v003_signal(pe, closeadj):
    base = _mean(pe, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw pe
def em_f073_earnings_multiples_raw_63d_slope_v004_signal(pe, closeadj):
    base = _mean(pe, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw pe
def em_f073_earnings_multiples_raw_63d_slope_v005_signal(pe, closeadj):
    base = _mean(pe, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw pe
def em_f073_earnings_multiples_raw_63d_slope_v006_signal(pe, closeadj):
    base = _mean(pe, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw pe
def em_f073_earnings_multiples_raw_126d_slope_v007_signal(pe, closeadj):
    base = _mean(pe, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw pe
def em_f073_earnings_multiples_raw_126d_slope_v008_signal(pe, closeadj):
    base = _mean(pe, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw pe
def em_f073_earnings_multiples_raw_126d_slope_v009_signal(pe, closeadj):
    base = _mean(pe, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw pe
def em_f073_earnings_multiples_raw_252d_slope_v010_signal(pe, closeadj):
    base = _mean(pe, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw pe
def em_f073_earnings_multiples_raw_252d_slope_v011_signal(pe, closeadj):
    base = _mean(pe, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw pe
def em_f073_earnings_multiples_raw_252d_slope_v012_signal(pe, closeadj):
    base = _mean(pe, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw pe
def em_f073_earnings_multiples_raw_504d_slope_v013_signal(pe, closeadj):
    base = _mean(pe, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw pe
def em_f073_earnings_multiples_raw_504d_slope_v014_signal(pe, closeadj):
    base = _mean(pe, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw pe
def em_f073_earnings_multiples_raw_504d_slope_v015_signal(pe, closeadj):
    base = _mean(pe, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log pe
def em_f073_earnings_multiples_log_21d_slope_v016_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log pe
def em_f073_earnings_multiples_log_21d_slope_v017_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log pe
def em_f073_earnings_multiples_log_21d_slope_v018_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log pe
def em_f073_earnings_multiples_log_63d_slope_v019_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log pe
def em_f073_earnings_multiples_log_63d_slope_v020_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log pe
def em_f073_earnings_multiples_log_63d_slope_v021_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log pe
def em_f073_earnings_multiples_log_126d_slope_v022_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log pe
def em_f073_earnings_multiples_log_126d_slope_v023_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log pe
def em_f073_earnings_multiples_log_126d_slope_v024_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log pe
def em_f073_earnings_multiples_log_252d_slope_v025_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log pe
def em_f073_earnings_multiples_log_252d_slope_v026_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log pe
def em_f073_earnings_multiples_log_252d_slope_v027_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log pe
def em_f073_earnings_multiples_log_504d_slope_v028_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log pe
def em_f073_earnings_multiples_log_504d_slope_v029_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log pe
def em_f073_earnings_multiples_log_504d_slope_v030_signal(pe, closeadj):
    base = _mean(_earnings_multiples_log(pe), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare pe
def em_f073_earnings_multiples_pershare_21d_slope_v031_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare pe
def em_f073_earnings_multiples_pershare_21d_slope_v032_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare pe
def em_f073_earnings_multiples_pershare_21d_slope_v033_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare pe
def em_f073_earnings_multiples_pershare_63d_slope_v034_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare pe
def em_f073_earnings_multiples_pershare_63d_slope_v035_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare pe
def em_f073_earnings_multiples_pershare_63d_slope_v036_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare pe
def em_f073_earnings_multiples_pershare_126d_slope_v037_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare pe
def em_f073_earnings_multiples_pershare_126d_slope_v038_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare pe
def em_f073_earnings_multiples_pershare_126d_slope_v039_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare pe
def em_f073_earnings_multiples_pershare_252d_slope_v040_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare pe
def em_f073_earnings_multiples_pershare_252d_slope_v041_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare pe
def em_f073_earnings_multiples_pershare_252d_slope_v042_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare pe
def em_f073_earnings_multiples_pershare_504d_slope_v043_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare pe
def em_f073_earnings_multiples_pershare_504d_slope_v044_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare pe
def em_f073_earnings_multiples_pershare_504d_slope_v045_signal(pe, sharesbas, closeadj):
    base = _mean(_earnings_multiples_per_share(pe, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_evebit pe
def em_f073_earnings_multiples_per_evebit_21d_slope_v046_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_evebit pe
def em_f073_earnings_multiples_per_evebit_21d_slope_v047_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_evebit pe
def em_f073_earnings_multiples_per_evebit_21d_slope_v048_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_evebit pe
def em_f073_earnings_multiples_per_evebit_63d_slope_v049_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_evebit pe
def em_f073_earnings_multiples_per_evebit_63d_slope_v050_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_evebit pe
def em_f073_earnings_multiples_per_evebit_63d_slope_v051_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_evebit pe
def em_f073_earnings_multiples_per_evebit_126d_slope_v052_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_evebit pe
def em_f073_earnings_multiples_per_evebit_126d_slope_v053_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_evebit pe
def em_f073_earnings_multiples_per_evebit_126d_slope_v054_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_evebit pe
def em_f073_earnings_multiples_per_evebit_252d_slope_v055_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_evebit pe
def em_f073_earnings_multiples_per_evebit_252d_slope_v056_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_evebit pe
def em_f073_earnings_multiples_per_evebit_252d_slope_v057_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_evebit pe
def em_f073_earnings_multiples_per_evebit_504d_slope_v058_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_evebit pe
def em_f073_earnings_multiples_per_evebit_504d_slope_v059_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_evebit pe
def em_f073_earnings_multiples_per_evebit_504d_slope_v060_signal(pe, evebit):
    base = _mean(_earnings_multiples_scaled(pe, evebit), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_21d_slope_v061_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_21d_slope_v062_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_21d_slope_v063_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_63d_slope_v064_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_63d_slope_v065_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_63d_slope_v066_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_126d_slope_v067_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_126d_slope_v068_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_126d_slope_v069_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_252d_slope_v070_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_252d_slope_v071_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_252d_slope_v072_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_504d_slope_v073_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_504d_slope_v074_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_evebitda pe
def em_f073_earnings_multiples_per_evebitda_504d_slope_v075_signal(pe, evebitda):
    base = _mean(_earnings_multiples_scaled(pe, evebitda), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_ebit pe
def em_f073_earnings_multiples_per_ebit_21d_slope_v076_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_ebit pe
def em_f073_earnings_multiples_per_ebit_21d_slope_v077_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_ebit pe
def em_f073_earnings_multiples_per_ebit_21d_slope_v078_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_ebit pe
def em_f073_earnings_multiples_per_ebit_63d_slope_v079_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_ebit pe
def em_f073_earnings_multiples_per_ebit_63d_slope_v080_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_ebit pe
def em_f073_earnings_multiples_per_ebit_63d_slope_v081_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_ebit pe
def em_f073_earnings_multiples_per_ebit_126d_slope_v082_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_ebit pe
def em_f073_earnings_multiples_per_ebit_126d_slope_v083_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_ebit pe
def em_f073_earnings_multiples_per_ebit_126d_slope_v084_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_ebit pe
def em_f073_earnings_multiples_per_ebit_252d_slope_v085_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_ebit pe
def em_f073_earnings_multiples_per_ebit_252d_slope_v086_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_ebit pe
def em_f073_earnings_multiples_per_ebit_252d_slope_v087_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_ebit pe
def em_f073_earnings_multiples_per_ebit_504d_slope_v088_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_ebit pe
def em_f073_earnings_multiples_per_ebit_504d_slope_v089_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_ebit pe
def em_f073_earnings_multiples_per_ebit_504d_slope_v090_signal(pe, ebit):
    base = _mean(_earnings_multiples_scaled(pe, ebit), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std pe
def em_f073_earnings_multiples_std_21d_slope_v091_signal(pe, closeadj):
    base = _std(pe, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std pe
def em_f073_earnings_multiples_std_21d_slope_v092_signal(pe, closeadj):
    base = _std(pe, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std pe
def em_f073_earnings_multiples_std_21d_slope_v093_signal(pe, closeadj):
    base = _std(pe, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std pe
def em_f073_earnings_multiples_std_63d_slope_v094_signal(pe, closeadj):
    base = _std(pe, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std pe
def em_f073_earnings_multiples_std_63d_slope_v095_signal(pe, closeadj):
    base = _std(pe, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std pe
def em_f073_earnings_multiples_std_63d_slope_v096_signal(pe, closeadj):
    base = _std(pe, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std pe
def em_f073_earnings_multiples_std_126d_slope_v097_signal(pe, closeadj):
    base = _std(pe, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std pe
def em_f073_earnings_multiples_std_126d_slope_v098_signal(pe, closeadj):
    base = _std(pe, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std pe
def em_f073_earnings_multiples_std_126d_slope_v099_signal(pe, closeadj):
    base = _std(pe, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std pe
def em_f073_earnings_multiples_std_252d_slope_v100_signal(pe, closeadj):
    base = _std(pe, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std pe
def em_f073_earnings_multiples_std_252d_slope_v101_signal(pe, closeadj):
    base = _std(pe, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std pe
def em_f073_earnings_multiples_std_252d_slope_v102_signal(pe, closeadj):
    base = _std(pe, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std pe
def em_f073_earnings_multiples_std_504d_slope_v103_signal(pe, closeadj):
    base = _std(pe, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std pe
def em_f073_earnings_multiples_std_504d_slope_v104_signal(pe, closeadj):
    base = _std(pe, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std pe
def em_f073_earnings_multiples_std_504d_slope_v105_signal(pe, closeadj):
    base = _std(pe, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm pe
def em_f073_earnings_multiples_ewm_21d_slope_v106_signal(pe, closeadj):
    base = pe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm pe
def em_f073_earnings_multiples_ewm_21d_slope_v107_signal(pe, closeadj):
    base = pe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm pe
def em_f073_earnings_multiples_ewm_21d_slope_v108_signal(pe, closeadj):
    base = pe.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm pe
def em_f073_earnings_multiples_ewm_63d_slope_v109_signal(pe, closeadj):
    base = pe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm pe
def em_f073_earnings_multiples_ewm_63d_slope_v110_signal(pe, closeadj):
    base = pe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm pe
def em_f073_earnings_multiples_ewm_63d_slope_v111_signal(pe, closeadj):
    base = pe.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm pe
def em_f073_earnings_multiples_ewm_126d_slope_v112_signal(pe, closeadj):
    base = pe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm pe
def em_f073_earnings_multiples_ewm_126d_slope_v113_signal(pe, closeadj):
    base = pe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm pe
def em_f073_earnings_multiples_ewm_126d_slope_v114_signal(pe, closeadj):
    base = pe.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm pe
def em_f073_earnings_multiples_ewm_252d_slope_v115_signal(pe, closeadj):
    base = pe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm pe
def em_f073_earnings_multiples_ewm_252d_slope_v116_signal(pe, closeadj):
    base = pe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm pe
def em_f073_earnings_multiples_ewm_252d_slope_v117_signal(pe, closeadj):
    base = pe.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm pe
def em_f073_earnings_multiples_ewm_504d_slope_v118_signal(pe, closeadj):
    base = pe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm pe
def em_f073_earnings_multiples_ewm_504d_slope_v119_signal(pe, closeadj):
    base = pe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm pe
def em_f073_earnings_multiples_ewm_504d_slope_v120_signal(pe, closeadj):
    base = pe.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq pe
def em_f073_earnings_multiples_sq_21d_slope_v121_signal(pe, closeadj):
    base = _mean(pe * pe, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq pe
def em_f073_earnings_multiples_sq_21d_slope_v122_signal(pe, closeadj):
    base = _mean(pe * pe, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq pe
def em_f073_earnings_multiples_sq_21d_slope_v123_signal(pe, closeadj):
    base = _mean(pe * pe, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq pe
def em_f073_earnings_multiples_sq_63d_slope_v124_signal(pe, closeadj):
    base = _mean(pe * pe, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq pe
def em_f073_earnings_multiples_sq_63d_slope_v125_signal(pe, closeadj):
    base = _mean(pe * pe, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq pe
def em_f073_earnings_multiples_sq_63d_slope_v126_signal(pe, closeadj):
    base = _mean(pe * pe, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq pe
def em_f073_earnings_multiples_sq_126d_slope_v127_signal(pe, closeadj):
    base = _mean(pe * pe, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq pe
def em_f073_earnings_multiples_sq_126d_slope_v128_signal(pe, closeadj):
    base = _mean(pe * pe, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq pe
def em_f073_earnings_multiples_sq_126d_slope_v129_signal(pe, closeadj):
    base = _mean(pe * pe, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq pe
def em_f073_earnings_multiples_sq_252d_slope_v130_signal(pe, closeadj):
    base = _mean(pe * pe, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq pe
def em_f073_earnings_multiples_sq_252d_slope_v131_signal(pe, closeadj):
    base = _mean(pe * pe, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq pe
def em_f073_earnings_multiples_sq_252d_slope_v132_signal(pe, closeadj):
    base = _mean(pe * pe, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq pe
def em_f073_earnings_multiples_sq_504d_slope_v133_signal(pe, closeadj):
    base = _mean(pe * pe, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq pe
def em_f073_earnings_multiples_sq_504d_slope_v134_signal(pe, closeadj):
    base = _mean(pe * pe, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq pe
def em_f073_earnings_multiples_sq_504d_slope_v135_signal(pe, closeadj):
    base = _mean(pe * pe, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z pe
def em_f073_earnings_multiples_z_21d_slope_v136_signal(pe):
    base = _z(pe, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z pe
def em_f073_earnings_multiples_z_21d_slope_v137_signal(pe):
    base = _z(pe, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z pe
def em_f073_earnings_multiples_z_21d_slope_v138_signal(pe):
    base = _z(pe, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z pe
def em_f073_earnings_multiples_z_63d_slope_v139_signal(pe):
    base = _z(pe, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z pe
def em_f073_earnings_multiples_z_63d_slope_v140_signal(pe):
    base = _z(pe, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z pe
def em_f073_earnings_multiples_z_63d_slope_v141_signal(pe):
    base = _z(pe, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z pe
def em_f073_earnings_multiples_z_126d_slope_v142_signal(pe):
    base = _z(pe, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z pe
def em_f073_earnings_multiples_z_126d_slope_v143_signal(pe):
    base = _z(pe, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z pe
def em_f073_earnings_multiples_z_126d_slope_v144_signal(pe):
    base = _z(pe, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z pe
def em_f073_earnings_multiples_z_252d_slope_v145_signal(pe):
    base = _z(pe, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z pe
def em_f073_earnings_multiples_z_252d_slope_v146_signal(pe):
    base = _z(pe, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z pe
def em_f073_earnings_multiples_z_252d_slope_v147_signal(pe):
    base = _z(pe, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z pe
def em_f073_earnings_multiples_z_504d_slope_v148_signal(pe):
    base = _z(pe, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z pe
def em_f073_earnings_multiples_z_504d_slope_v149_signal(pe):
    base = _z(pe, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z pe
def em_f073_earnings_multiples_z_504d_slope_v150_signal(pe):
    base = _z(pe, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
