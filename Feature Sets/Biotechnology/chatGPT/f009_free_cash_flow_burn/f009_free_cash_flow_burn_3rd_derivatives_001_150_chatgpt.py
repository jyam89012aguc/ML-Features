"""Family f009 - Free cash flow burn (Cash Flow and Burn) | Sharadar tables: SF1 | fields: fcf, fcfps, ncfo, capex | 3rd derivatives 001-150"""
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
def _free_cash_flow_burn_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _free_cash_flow_burn_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _free_cash_flow_burn_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_21d_accel_v001_signal(fcf, closeadj):
    base = _mean(fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_21d_accel_v002_signal(fcf, closeadj):
    base = _mean(fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_21d_accel_v003_signal(fcf, closeadj):
    base = _mean(fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_63d_accel_v004_signal(fcf, closeadj):
    base = _mean(fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_63d_accel_v005_signal(fcf, closeadj):
    base = _mean(fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_63d_accel_v006_signal(fcf, closeadj):
    base = _mean(fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_126d_accel_v007_signal(fcf, closeadj):
    base = _mean(fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_126d_accel_v008_signal(fcf, closeadj):
    base = _mean(fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_126d_accel_v009_signal(fcf, closeadj):
    base = _mean(fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_252d_accel_v010_signal(fcf, closeadj):
    base = _mean(fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_252d_accel_v011_signal(fcf, closeadj):
    base = _mean(fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_252d_accel_v012_signal(fcf, closeadj):
    base = _mean(fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_504d_accel_v013_signal(fcf, closeadj):
    base = _mean(fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_504d_accel_v014_signal(fcf, closeadj):
    base = _mean(fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw fcf
def fcfb_f009_free_cash_flow_burn_raw_504d_accel_v015_signal(fcf, closeadj):
    base = _mean(fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log fcf
def fcfb_f009_free_cash_flow_burn_log_21d_accel_v016_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log fcf
def fcfb_f009_free_cash_flow_burn_log_21d_accel_v017_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log fcf
def fcfb_f009_free_cash_flow_burn_log_21d_accel_v018_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log fcf
def fcfb_f009_free_cash_flow_burn_log_63d_accel_v019_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log fcf
def fcfb_f009_free_cash_flow_burn_log_63d_accel_v020_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log fcf
def fcfb_f009_free_cash_flow_burn_log_63d_accel_v021_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log fcf
def fcfb_f009_free_cash_flow_burn_log_126d_accel_v022_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log fcf
def fcfb_f009_free_cash_flow_burn_log_126d_accel_v023_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log fcf
def fcfb_f009_free_cash_flow_burn_log_126d_accel_v024_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log fcf
def fcfb_f009_free_cash_flow_burn_log_252d_accel_v025_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log fcf
def fcfb_f009_free_cash_flow_burn_log_252d_accel_v026_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log fcf
def fcfb_f009_free_cash_flow_burn_log_252d_accel_v027_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log fcf
def fcfb_f009_free_cash_flow_burn_log_504d_accel_v028_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log fcf
def fcfb_f009_free_cash_flow_burn_log_504d_accel_v029_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log fcf
def fcfb_f009_free_cash_flow_burn_log_504d_accel_v030_signal(fcf, closeadj):
    base = _mean(_free_cash_flow_burn_log(fcf), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_21d_accel_v031_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_21d_accel_v032_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_21d_accel_v033_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_63d_accel_v034_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_63d_accel_v035_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_63d_accel_v036_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_126d_accel_v037_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_126d_accel_v038_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_126d_accel_v039_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_252d_accel_v040_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_252d_accel_v041_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_252d_accel_v042_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_504d_accel_v043_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_504d_accel_v044_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare fcf
def fcfb_f009_free_cash_flow_burn_pershare_504d_accel_v045_signal(fcf, sharesbas, closeadj):
    base = _mean(_free_cash_flow_burn_per_share(fcf, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_21d_accel_v046_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_21d_accel_v047_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_21d_accel_v048_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_63d_accel_v049_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_63d_accel_v050_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_63d_accel_v051_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_126d_accel_v052_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_126d_accel_v053_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_126d_accel_v054_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_252d_accel_v055_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_252d_accel_v056_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_252d_accel_v057_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_504d_accel_v058_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_504d_accel_v059_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_fcfps fcf
def fcfb_f009_free_cash_flow_burn_per_fcfps_504d_accel_v060_signal(fcf, fcfps):
    base = _mean(_free_cash_flow_burn_scaled(fcf, fcfps), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_21d_accel_v061_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_21d_accel_v062_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_21d_accel_v063_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_63d_accel_v064_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_63d_accel_v065_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_63d_accel_v066_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_126d_accel_v067_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_126d_accel_v068_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_126d_accel_v069_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_252d_accel_v070_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_252d_accel_v071_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_252d_accel_v072_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_504d_accel_v073_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_504d_accel_v074_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ncfo fcf
def fcfb_f009_free_cash_flow_burn_per_ncfo_504d_accel_v075_signal(fcf, ncfo):
    base = _mean(_free_cash_flow_burn_scaled(fcf, ncfo), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_21d_accel_v076_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_21d_accel_v077_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_21d_accel_v078_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_63d_accel_v079_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_63d_accel_v080_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_63d_accel_v081_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_126d_accel_v082_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_126d_accel_v083_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_126d_accel_v084_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_252d_accel_v085_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_252d_accel_v086_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_252d_accel_v087_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_504d_accel_v088_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_504d_accel_v089_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets fcf
def fcfb_f009_free_cash_flow_burn_per_assets_504d_accel_v090_signal(fcf, assets):
    base = _mean(_free_cash_flow_burn_scaled(fcf, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std fcf
def fcfb_f009_free_cash_flow_burn_std_21d_accel_v091_signal(fcf, closeadj):
    base = _std(fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std fcf
def fcfb_f009_free_cash_flow_burn_std_21d_accel_v092_signal(fcf, closeadj):
    base = _std(fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std fcf
def fcfb_f009_free_cash_flow_burn_std_21d_accel_v093_signal(fcf, closeadj):
    base = _std(fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std fcf
def fcfb_f009_free_cash_flow_burn_std_63d_accel_v094_signal(fcf, closeadj):
    base = _std(fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std fcf
def fcfb_f009_free_cash_flow_burn_std_63d_accel_v095_signal(fcf, closeadj):
    base = _std(fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std fcf
def fcfb_f009_free_cash_flow_burn_std_63d_accel_v096_signal(fcf, closeadj):
    base = _std(fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std fcf
def fcfb_f009_free_cash_flow_burn_std_126d_accel_v097_signal(fcf, closeadj):
    base = _std(fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std fcf
def fcfb_f009_free_cash_flow_burn_std_126d_accel_v098_signal(fcf, closeadj):
    base = _std(fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std fcf
def fcfb_f009_free_cash_flow_burn_std_126d_accel_v099_signal(fcf, closeadj):
    base = _std(fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std fcf
def fcfb_f009_free_cash_flow_burn_std_252d_accel_v100_signal(fcf, closeadj):
    base = _std(fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std fcf
def fcfb_f009_free_cash_flow_burn_std_252d_accel_v101_signal(fcf, closeadj):
    base = _std(fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std fcf
def fcfb_f009_free_cash_flow_burn_std_252d_accel_v102_signal(fcf, closeadj):
    base = _std(fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std fcf
def fcfb_f009_free_cash_flow_burn_std_504d_accel_v103_signal(fcf, closeadj):
    base = _std(fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std fcf
def fcfb_f009_free_cash_flow_burn_std_504d_accel_v104_signal(fcf, closeadj):
    base = _std(fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std fcf
def fcfb_f009_free_cash_flow_burn_std_504d_accel_v105_signal(fcf, closeadj):
    base = _std(fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_21d_accel_v106_signal(fcf, closeadj):
    base = fcf.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_21d_accel_v107_signal(fcf, closeadj):
    base = fcf.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_21d_accel_v108_signal(fcf, closeadj):
    base = fcf.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_63d_accel_v109_signal(fcf, closeadj):
    base = fcf.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_63d_accel_v110_signal(fcf, closeadj):
    base = fcf.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_63d_accel_v111_signal(fcf, closeadj):
    base = fcf.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_126d_accel_v112_signal(fcf, closeadj):
    base = fcf.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_126d_accel_v113_signal(fcf, closeadj):
    base = fcf.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_126d_accel_v114_signal(fcf, closeadj):
    base = fcf.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_252d_accel_v115_signal(fcf, closeadj):
    base = fcf.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_252d_accel_v116_signal(fcf, closeadj):
    base = fcf.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_252d_accel_v117_signal(fcf, closeadj):
    base = fcf.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_504d_accel_v118_signal(fcf, closeadj):
    base = fcf.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_504d_accel_v119_signal(fcf, closeadj):
    base = fcf.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm fcf
def fcfb_f009_free_cash_flow_burn_ewm_504d_accel_v120_signal(fcf, closeadj):
    base = fcf.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_21d_accel_v121_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_21d_accel_v122_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_21d_accel_v123_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_63d_accel_v124_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_63d_accel_v125_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_63d_accel_v126_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_126d_accel_v127_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_126d_accel_v128_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_126d_accel_v129_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_252d_accel_v130_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_252d_accel_v131_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_252d_accel_v132_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_504d_accel_v133_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_504d_accel_v134_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq fcf
def fcfb_f009_free_cash_flow_burn_sq_504d_accel_v135_signal(fcf, closeadj):
    base = _mean(fcf * fcf, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z fcf
def fcfb_f009_free_cash_flow_burn_z_21d_accel_v136_signal(fcf):
    base = _z(fcf, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z fcf
def fcfb_f009_free_cash_flow_burn_z_21d_accel_v137_signal(fcf):
    base = _z(fcf, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z fcf
def fcfb_f009_free_cash_flow_burn_z_21d_accel_v138_signal(fcf):
    base = _z(fcf, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z fcf
def fcfb_f009_free_cash_flow_burn_z_63d_accel_v139_signal(fcf):
    base = _z(fcf, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z fcf
def fcfb_f009_free_cash_flow_burn_z_63d_accel_v140_signal(fcf):
    base = _z(fcf, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z fcf
def fcfb_f009_free_cash_flow_burn_z_63d_accel_v141_signal(fcf):
    base = _z(fcf, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z fcf
def fcfb_f009_free_cash_flow_burn_z_126d_accel_v142_signal(fcf):
    base = _z(fcf, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z fcf
def fcfb_f009_free_cash_flow_burn_z_126d_accel_v143_signal(fcf):
    base = _z(fcf, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z fcf
def fcfb_f009_free_cash_flow_burn_z_126d_accel_v144_signal(fcf):
    base = _z(fcf, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z fcf
def fcfb_f009_free_cash_flow_burn_z_252d_accel_v145_signal(fcf):
    base = _z(fcf, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z fcf
def fcfb_f009_free_cash_flow_burn_z_252d_accel_v146_signal(fcf):
    base = _z(fcf, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z fcf
def fcfb_f009_free_cash_flow_burn_z_252d_accel_v147_signal(fcf):
    base = _z(fcf, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z fcf
def fcfb_f009_free_cash_flow_burn_z_504d_accel_v148_signal(fcf):
    base = _z(fcf, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z fcf
def fcfb_f009_free_cash_flow_burn_z_504d_accel_v149_signal(fcf):
    base = _z(fcf, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z fcf
def fcfb_f009_free_cash_flow_burn_z_504d_accel_v150_signal(fcf):
    base = _z(fcf, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
