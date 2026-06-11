"""Family f011 - Capital raised through financing (Cash Flow and Burn) | Sharadar tables: SF1 | fields: ncff, ncfcommon, ncfdebt, ncfi | 3rd derivatives 001-150"""
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
def _financing_cash_flow_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _financing_cash_flow_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _financing_cash_flow_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw ncff
def fcf_f011_financing_cash_flow_raw_21d_accel_v001_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw ncff
def fcf_f011_financing_cash_flow_raw_21d_accel_v002_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw ncff
def fcf_f011_financing_cash_flow_raw_21d_accel_v003_signal(ncff, closeadj):
    base = _mean(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw ncff
def fcf_f011_financing_cash_flow_raw_63d_accel_v004_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw ncff
def fcf_f011_financing_cash_flow_raw_63d_accel_v005_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw ncff
def fcf_f011_financing_cash_flow_raw_63d_accel_v006_signal(ncff, closeadj):
    base = _mean(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw ncff
def fcf_f011_financing_cash_flow_raw_126d_accel_v007_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw ncff
def fcf_f011_financing_cash_flow_raw_126d_accel_v008_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw ncff
def fcf_f011_financing_cash_flow_raw_126d_accel_v009_signal(ncff, closeadj):
    base = _mean(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw ncff
def fcf_f011_financing_cash_flow_raw_252d_accel_v010_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw ncff
def fcf_f011_financing_cash_flow_raw_252d_accel_v011_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw ncff
def fcf_f011_financing_cash_flow_raw_252d_accel_v012_signal(ncff, closeadj):
    base = _mean(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw ncff
def fcf_f011_financing_cash_flow_raw_504d_accel_v013_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw ncff
def fcf_f011_financing_cash_flow_raw_504d_accel_v014_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw ncff
def fcf_f011_financing_cash_flow_raw_504d_accel_v015_signal(ncff, closeadj):
    base = _mean(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log ncff
def fcf_f011_financing_cash_flow_log_21d_accel_v016_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log ncff
def fcf_f011_financing_cash_flow_log_21d_accel_v017_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log ncff
def fcf_f011_financing_cash_flow_log_21d_accel_v018_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log ncff
def fcf_f011_financing_cash_flow_log_63d_accel_v019_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log ncff
def fcf_f011_financing_cash_flow_log_63d_accel_v020_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log ncff
def fcf_f011_financing_cash_flow_log_63d_accel_v021_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log ncff
def fcf_f011_financing_cash_flow_log_126d_accel_v022_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log ncff
def fcf_f011_financing_cash_flow_log_126d_accel_v023_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log ncff
def fcf_f011_financing_cash_flow_log_126d_accel_v024_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log ncff
def fcf_f011_financing_cash_flow_log_252d_accel_v025_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log ncff
def fcf_f011_financing_cash_flow_log_252d_accel_v026_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log ncff
def fcf_f011_financing_cash_flow_log_252d_accel_v027_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log ncff
def fcf_f011_financing_cash_flow_log_504d_accel_v028_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log ncff
def fcf_f011_financing_cash_flow_log_504d_accel_v029_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log ncff
def fcf_f011_financing_cash_flow_log_504d_accel_v030_signal(ncff, closeadj):
    base = _mean(_financing_cash_flow_log(ncff), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare ncff
def fcf_f011_financing_cash_flow_pershare_21d_accel_v031_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare ncff
def fcf_f011_financing_cash_flow_pershare_21d_accel_v032_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare ncff
def fcf_f011_financing_cash_flow_pershare_21d_accel_v033_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare ncff
def fcf_f011_financing_cash_flow_pershare_63d_accel_v034_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare ncff
def fcf_f011_financing_cash_flow_pershare_63d_accel_v035_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare ncff
def fcf_f011_financing_cash_flow_pershare_63d_accel_v036_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare ncff
def fcf_f011_financing_cash_flow_pershare_126d_accel_v037_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare ncff
def fcf_f011_financing_cash_flow_pershare_126d_accel_v038_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare ncff
def fcf_f011_financing_cash_flow_pershare_126d_accel_v039_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare ncff
def fcf_f011_financing_cash_flow_pershare_252d_accel_v040_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare ncff
def fcf_f011_financing_cash_flow_pershare_252d_accel_v041_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare ncff
def fcf_f011_financing_cash_flow_pershare_252d_accel_v042_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare ncff
def fcf_f011_financing_cash_flow_pershare_504d_accel_v043_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare ncff
def fcf_f011_financing_cash_flow_pershare_504d_accel_v044_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare ncff
def fcf_f011_financing_cash_flow_pershare_504d_accel_v045_signal(ncff, sharesbas, closeadj):
    base = _mean(_financing_cash_flow_per_share(ncff, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_21d_accel_v046_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_21d_accel_v047_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_21d_accel_v048_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_63d_accel_v049_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_63d_accel_v050_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_63d_accel_v051_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_126d_accel_v052_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_126d_accel_v053_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_126d_accel_v054_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_252d_accel_v055_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_252d_accel_v056_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_252d_accel_v057_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_504d_accel_v058_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_504d_accel_v059_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ncfcommon ncff
def fcf_f011_financing_cash_flow_per_ncfcommon_504d_accel_v060_signal(ncff, ncfcommon):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfcommon), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_21d_accel_v061_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_21d_accel_v062_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_21d_accel_v063_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_63d_accel_v064_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_63d_accel_v065_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_63d_accel_v066_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_126d_accel_v067_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_126d_accel_v068_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_126d_accel_v069_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_252d_accel_v070_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_252d_accel_v071_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_252d_accel_v072_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_504d_accel_v073_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_504d_accel_v074_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ncfdebt ncff
def fcf_f011_financing_cash_flow_per_ncfdebt_504d_accel_v075_signal(ncff, ncfdebt):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfdebt), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_21d_accel_v076_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_21d_accel_v077_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_21d_accel_v078_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_63d_accel_v079_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_63d_accel_v080_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_63d_accel_v081_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_126d_accel_v082_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_126d_accel_v083_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_126d_accel_v084_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_252d_accel_v085_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_252d_accel_v086_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_252d_accel_v087_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_504d_accel_v088_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_504d_accel_v089_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ncfi ncff
def fcf_f011_financing_cash_flow_per_ncfi_504d_accel_v090_signal(ncff, ncfi):
    base = _mean(_financing_cash_flow_scaled(ncff, ncfi), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std ncff
def fcf_f011_financing_cash_flow_std_21d_accel_v091_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std ncff
def fcf_f011_financing_cash_flow_std_21d_accel_v092_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std ncff
def fcf_f011_financing_cash_flow_std_21d_accel_v093_signal(ncff, closeadj):
    base = _std(ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std ncff
def fcf_f011_financing_cash_flow_std_63d_accel_v094_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std ncff
def fcf_f011_financing_cash_flow_std_63d_accel_v095_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std ncff
def fcf_f011_financing_cash_flow_std_63d_accel_v096_signal(ncff, closeadj):
    base = _std(ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std ncff
def fcf_f011_financing_cash_flow_std_126d_accel_v097_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std ncff
def fcf_f011_financing_cash_flow_std_126d_accel_v098_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std ncff
def fcf_f011_financing_cash_flow_std_126d_accel_v099_signal(ncff, closeadj):
    base = _std(ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std ncff
def fcf_f011_financing_cash_flow_std_252d_accel_v100_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std ncff
def fcf_f011_financing_cash_flow_std_252d_accel_v101_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std ncff
def fcf_f011_financing_cash_flow_std_252d_accel_v102_signal(ncff, closeadj):
    base = _std(ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std ncff
def fcf_f011_financing_cash_flow_std_504d_accel_v103_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std ncff
def fcf_f011_financing_cash_flow_std_504d_accel_v104_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std ncff
def fcf_f011_financing_cash_flow_std_504d_accel_v105_signal(ncff, closeadj):
    base = _std(ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm ncff
def fcf_f011_financing_cash_flow_ewm_21d_accel_v106_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm ncff
def fcf_f011_financing_cash_flow_ewm_21d_accel_v107_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm ncff
def fcf_f011_financing_cash_flow_ewm_21d_accel_v108_signal(ncff, closeadj):
    base = ncff.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm ncff
def fcf_f011_financing_cash_flow_ewm_63d_accel_v109_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm ncff
def fcf_f011_financing_cash_flow_ewm_63d_accel_v110_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm ncff
def fcf_f011_financing_cash_flow_ewm_63d_accel_v111_signal(ncff, closeadj):
    base = ncff.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm ncff
def fcf_f011_financing_cash_flow_ewm_126d_accel_v112_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm ncff
def fcf_f011_financing_cash_flow_ewm_126d_accel_v113_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm ncff
def fcf_f011_financing_cash_flow_ewm_126d_accel_v114_signal(ncff, closeadj):
    base = ncff.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm ncff
def fcf_f011_financing_cash_flow_ewm_252d_accel_v115_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm ncff
def fcf_f011_financing_cash_flow_ewm_252d_accel_v116_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm ncff
def fcf_f011_financing_cash_flow_ewm_252d_accel_v117_signal(ncff, closeadj):
    base = ncff.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm ncff
def fcf_f011_financing_cash_flow_ewm_504d_accel_v118_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm ncff
def fcf_f011_financing_cash_flow_ewm_504d_accel_v119_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm ncff
def fcf_f011_financing_cash_flow_ewm_504d_accel_v120_signal(ncff, closeadj):
    base = ncff.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq ncff
def fcf_f011_financing_cash_flow_sq_21d_accel_v121_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq ncff
def fcf_f011_financing_cash_flow_sq_21d_accel_v122_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq ncff
def fcf_f011_financing_cash_flow_sq_21d_accel_v123_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq ncff
def fcf_f011_financing_cash_flow_sq_63d_accel_v124_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq ncff
def fcf_f011_financing_cash_flow_sq_63d_accel_v125_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq ncff
def fcf_f011_financing_cash_flow_sq_63d_accel_v126_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq ncff
def fcf_f011_financing_cash_flow_sq_126d_accel_v127_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq ncff
def fcf_f011_financing_cash_flow_sq_126d_accel_v128_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq ncff
def fcf_f011_financing_cash_flow_sq_126d_accel_v129_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq ncff
def fcf_f011_financing_cash_flow_sq_252d_accel_v130_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq ncff
def fcf_f011_financing_cash_flow_sq_252d_accel_v131_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq ncff
def fcf_f011_financing_cash_flow_sq_252d_accel_v132_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq ncff
def fcf_f011_financing_cash_flow_sq_504d_accel_v133_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq ncff
def fcf_f011_financing_cash_flow_sq_504d_accel_v134_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq ncff
def fcf_f011_financing_cash_flow_sq_504d_accel_v135_signal(ncff, closeadj):
    base = _mean(ncff * ncff, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z ncff
def fcf_f011_financing_cash_flow_z_21d_accel_v136_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z ncff
def fcf_f011_financing_cash_flow_z_21d_accel_v137_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z ncff
def fcf_f011_financing_cash_flow_z_21d_accel_v138_signal(ncff):
    base = _z(ncff, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z ncff
def fcf_f011_financing_cash_flow_z_63d_accel_v139_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z ncff
def fcf_f011_financing_cash_flow_z_63d_accel_v140_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z ncff
def fcf_f011_financing_cash_flow_z_63d_accel_v141_signal(ncff):
    base = _z(ncff, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z ncff
def fcf_f011_financing_cash_flow_z_126d_accel_v142_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z ncff
def fcf_f011_financing_cash_flow_z_126d_accel_v143_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z ncff
def fcf_f011_financing_cash_flow_z_126d_accel_v144_signal(ncff):
    base = _z(ncff, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z ncff
def fcf_f011_financing_cash_flow_z_252d_accel_v145_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z ncff
def fcf_f011_financing_cash_flow_z_252d_accel_v146_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z ncff
def fcf_f011_financing_cash_flow_z_252d_accel_v147_signal(ncff):
    base = _z(ncff, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z ncff
def fcf_f011_financing_cash_flow_z_504d_accel_v148_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z ncff
def fcf_f011_financing_cash_flow_z_504d_accel_v149_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z ncff
def fcf_f011_financing_cash_flow_z_504d_accel_v150_signal(ncff):
    base = _z(ncff, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
