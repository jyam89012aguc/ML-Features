"""Family f065 - ROIC and invested capital returns (Returns and Efficiency) | Sharadar tables: SF1 | fields: roic, invcap, invcapavg | 3rd derivatives 001-150"""
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
def _return_on_invested_capital_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _return_on_invested_capital_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _return_on_invested_capital_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw roic
def roic_f065_return_on_invested_capital_raw_21d_accel_v001_signal(roic, closeadj):
    base = _mean(roic, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw roic
def roic_f065_return_on_invested_capital_raw_21d_accel_v002_signal(roic, closeadj):
    base = _mean(roic, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw roic
def roic_f065_return_on_invested_capital_raw_21d_accel_v003_signal(roic, closeadj):
    base = _mean(roic, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw roic
def roic_f065_return_on_invested_capital_raw_63d_accel_v004_signal(roic, closeadj):
    base = _mean(roic, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw roic
def roic_f065_return_on_invested_capital_raw_63d_accel_v005_signal(roic, closeadj):
    base = _mean(roic, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw roic
def roic_f065_return_on_invested_capital_raw_63d_accel_v006_signal(roic, closeadj):
    base = _mean(roic, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw roic
def roic_f065_return_on_invested_capital_raw_126d_accel_v007_signal(roic, closeadj):
    base = _mean(roic, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw roic
def roic_f065_return_on_invested_capital_raw_126d_accel_v008_signal(roic, closeadj):
    base = _mean(roic, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw roic
def roic_f065_return_on_invested_capital_raw_126d_accel_v009_signal(roic, closeadj):
    base = _mean(roic, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw roic
def roic_f065_return_on_invested_capital_raw_252d_accel_v010_signal(roic, closeadj):
    base = _mean(roic, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw roic
def roic_f065_return_on_invested_capital_raw_252d_accel_v011_signal(roic, closeadj):
    base = _mean(roic, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw roic
def roic_f065_return_on_invested_capital_raw_252d_accel_v012_signal(roic, closeadj):
    base = _mean(roic, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw roic
def roic_f065_return_on_invested_capital_raw_504d_accel_v013_signal(roic, closeadj):
    base = _mean(roic, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw roic
def roic_f065_return_on_invested_capital_raw_504d_accel_v014_signal(roic, closeadj):
    base = _mean(roic, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw roic
def roic_f065_return_on_invested_capital_raw_504d_accel_v015_signal(roic, closeadj):
    base = _mean(roic, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log roic
def roic_f065_return_on_invested_capital_log_21d_accel_v016_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log roic
def roic_f065_return_on_invested_capital_log_21d_accel_v017_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log roic
def roic_f065_return_on_invested_capital_log_21d_accel_v018_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log roic
def roic_f065_return_on_invested_capital_log_63d_accel_v019_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log roic
def roic_f065_return_on_invested_capital_log_63d_accel_v020_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log roic
def roic_f065_return_on_invested_capital_log_63d_accel_v021_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log roic
def roic_f065_return_on_invested_capital_log_126d_accel_v022_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log roic
def roic_f065_return_on_invested_capital_log_126d_accel_v023_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log roic
def roic_f065_return_on_invested_capital_log_126d_accel_v024_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log roic
def roic_f065_return_on_invested_capital_log_252d_accel_v025_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log roic
def roic_f065_return_on_invested_capital_log_252d_accel_v026_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log roic
def roic_f065_return_on_invested_capital_log_252d_accel_v027_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log roic
def roic_f065_return_on_invested_capital_log_504d_accel_v028_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log roic
def roic_f065_return_on_invested_capital_log_504d_accel_v029_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log roic
def roic_f065_return_on_invested_capital_log_504d_accel_v030_signal(roic, closeadj):
    base = _mean(_return_on_invested_capital_log(roic), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare roic
def roic_f065_return_on_invested_capital_pershare_21d_accel_v031_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare roic
def roic_f065_return_on_invested_capital_pershare_21d_accel_v032_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare roic
def roic_f065_return_on_invested_capital_pershare_21d_accel_v033_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare roic
def roic_f065_return_on_invested_capital_pershare_63d_accel_v034_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare roic
def roic_f065_return_on_invested_capital_pershare_63d_accel_v035_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare roic
def roic_f065_return_on_invested_capital_pershare_63d_accel_v036_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare roic
def roic_f065_return_on_invested_capital_pershare_126d_accel_v037_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare roic
def roic_f065_return_on_invested_capital_pershare_126d_accel_v038_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare roic
def roic_f065_return_on_invested_capital_pershare_126d_accel_v039_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare roic
def roic_f065_return_on_invested_capital_pershare_252d_accel_v040_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare roic
def roic_f065_return_on_invested_capital_pershare_252d_accel_v041_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare roic
def roic_f065_return_on_invested_capital_pershare_252d_accel_v042_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare roic
def roic_f065_return_on_invested_capital_pershare_504d_accel_v043_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare roic
def roic_f065_return_on_invested_capital_pershare_504d_accel_v044_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare roic
def roic_f065_return_on_invested_capital_pershare_504d_accel_v045_signal(roic, sharesbas, closeadj):
    base = _mean(_return_on_invested_capital_per_share(roic, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_21d_accel_v046_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_21d_accel_v047_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_21d_accel_v048_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_63d_accel_v049_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_63d_accel_v050_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_63d_accel_v051_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_126d_accel_v052_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_126d_accel_v053_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_126d_accel_v054_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_252d_accel_v055_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_252d_accel_v056_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_252d_accel_v057_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_504d_accel_v058_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_504d_accel_v059_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_invcap roic
def roic_f065_return_on_invested_capital_per_invcap_504d_accel_v060_signal(roic, invcap):
    base = _mean(_return_on_invested_capital_scaled(roic, invcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_21d_accel_v061_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_21d_accel_v062_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_21d_accel_v063_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_63d_accel_v064_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_63d_accel_v065_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_63d_accel_v066_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_126d_accel_v067_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_126d_accel_v068_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_126d_accel_v069_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_252d_accel_v070_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_252d_accel_v071_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_252d_accel_v072_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_504d_accel_v073_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_504d_accel_v074_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_invcapavg roic
def roic_f065_return_on_invested_capital_per_invcapavg_504d_accel_v075_signal(roic, invcapavg):
    base = _mean(_return_on_invested_capital_scaled(roic, invcapavg), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_21d_accel_v076_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_21d_accel_v077_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_21d_accel_v078_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_63d_accel_v079_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_63d_accel_v080_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_63d_accel_v081_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_126d_accel_v082_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_126d_accel_v083_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_126d_accel_v084_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_252d_accel_v085_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_252d_accel_v086_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_252d_accel_v087_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_504d_accel_v088_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_504d_accel_v089_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets roic
def roic_f065_return_on_invested_capital_per_assets_504d_accel_v090_signal(roic, assets):
    base = _mean(_return_on_invested_capital_scaled(roic, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std roic
def roic_f065_return_on_invested_capital_std_21d_accel_v091_signal(roic, closeadj):
    base = _std(roic, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std roic
def roic_f065_return_on_invested_capital_std_21d_accel_v092_signal(roic, closeadj):
    base = _std(roic, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std roic
def roic_f065_return_on_invested_capital_std_21d_accel_v093_signal(roic, closeadj):
    base = _std(roic, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std roic
def roic_f065_return_on_invested_capital_std_63d_accel_v094_signal(roic, closeadj):
    base = _std(roic, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std roic
def roic_f065_return_on_invested_capital_std_63d_accel_v095_signal(roic, closeadj):
    base = _std(roic, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std roic
def roic_f065_return_on_invested_capital_std_63d_accel_v096_signal(roic, closeadj):
    base = _std(roic, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std roic
def roic_f065_return_on_invested_capital_std_126d_accel_v097_signal(roic, closeadj):
    base = _std(roic, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std roic
def roic_f065_return_on_invested_capital_std_126d_accel_v098_signal(roic, closeadj):
    base = _std(roic, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std roic
def roic_f065_return_on_invested_capital_std_126d_accel_v099_signal(roic, closeadj):
    base = _std(roic, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std roic
def roic_f065_return_on_invested_capital_std_252d_accel_v100_signal(roic, closeadj):
    base = _std(roic, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std roic
def roic_f065_return_on_invested_capital_std_252d_accel_v101_signal(roic, closeadj):
    base = _std(roic, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std roic
def roic_f065_return_on_invested_capital_std_252d_accel_v102_signal(roic, closeadj):
    base = _std(roic, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std roic
def roic_f065_return_on_invested_capital_std_504d_accel_v103_signal(roic, closeadj):
    base = _std(roic, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std roic
def roic_f065_return_on_invested_capital_std_504d_accel_v104_signal(roic, closeadj):
    base = _std(roic, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std roic
def roic_f065_return_on_invested_capital_std_504d_accel_v105_signal(roic, closeadj):
    base = _std(roic, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm roic
def roic_f065_return_on_invested_capital_ewm_21d_accel_v106_signal(roic, closeadj):
    base = roic.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm roic
def roic_f065_return_on_invested_capital_ewm_21d_accel_v107_signal(roic, closeadj):
    base = roic.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm roic
def roic_f065_return_on_invested_capital_ewm_21d_accel_v108_signal(roic, closeadj):
    base = roic.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm roic
def roic_f065_return_on_invested_capital_ewm_63d_accel_v109_signal(roic, closeadj):
    base = roic.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm roic
def roic_f065_return_on_invested_capital_ewm_63d_accel_v110_signal(roic, closeadj):
    base = roic.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm roic
def roic_f065_return_on_invested_capital_ewm_63d_accel_v111_signal(roic, closeadj):
    base = roic.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm roic
def roic_f065_return_on_invested_capital_ewm_126d_accel_v112_signal(roic, closeadj):
    base = roic.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm roic
def roic_f065_return_on_invested_capital_ewm_126d_accel_v113_signal(roic, closeadj):
    base = roic.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm roic
def roic_f065_return_on_invested_capital_ewm_126d_accel_v114_signal(roic, closeadj):
    base = roic.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm roic
def roic_f065_return_on_invested_capital_ewm_252d_accel_v115_signal(roic, closeadj):
    base = roic.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm roic
def roic_f065_return_on_invested_capital_ewm_252d_accel_v116_signal(roic, closeadj):
    base = roic.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm roic
def roic_f065_return_on_invested_capital_ewm_252d_accel_v117_signal(roic, closeadj):
    base = roic.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm roic
def roic_f065_return_on_invested_capital_ewm_504d_accel_v118_signal(roic, closeadj):
    base = roic.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm roic
def roic_f065_return_on_invested_capital_ewm_504d_accel_v119_signal(roic, closeadj):
    base = roic.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm roic
def roic_f065_return_on_invested_capital_ewm_504d_accel_v120_signal(roic, closeadj):
    base = roic.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq roic
def roic_f065_return_on_invested_capital_sq_21d_accel_v121_signal(roic, closeadj):
    base = _mean(roic * roic, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq roic
def roic_f065_return_on_invested_capital_sq_21d_accel_v122_signal(roic, closeadj):
    base = _mean(roic * roic, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq roic
def roic_f065_return_on_invested_capital_sq_21d_accel_v123_signal(roic, closeadj):
    base = _mean(roic * roic, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq roic
def roic_f065_return_on_invested_capital_sq_63d_accel_v124_signal(roic, closeadj):
    base = _mean(roic * roic, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq roic
def roic_f065_return_on_invested_capital_sq_63d_accel_v125_signal(roic, closeadj):
    base = _mean(roic * roic, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq roic
def roic_f065_return_on_invested_capital_sq_63d_accel_v126_signal(roic, closeadj):
    base = _mean(roic * roic, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq roic
def roic_f065_return_on_invested_capital_sq_126d_accel_v127_signal(roic, closeadj):
    base = _mean(roic * roic, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq roic
def roic_f065_return_on_invested_capital_sq_126d_accel_v128_signal(roic, closeadj):
    base = _mean(roic * roic, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq roic
def roic_f065_return_on_invested_capital_sq_126d_accel_v129_signal(roic, closeadj):
    base = _mean(roic * roic, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq roic
def roic_f065_return_on_invested_capital_sq_252d_accel_v130_signal(roic, closeadj):
    base = _mean(roic * roic, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq roic
def roic_f065_return_on_invested_capital_sq_252d_accel_v131_signal(roic, closeadj):
    base = _mean(roic * roic, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq roic
def roic_f065_return_on_invested_capital_sq_252d_accel_v132_signal(roic, closeadj):
    base = _mean(roic * roic, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq roic
def roic_f065_return_on_invested_capital_sq_504d_accel_v133_signal(roic, closeadj):
    base = _mean(roic * roic, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq roic
def roic_f065_return_on_invested_capital_sq_504d_accel_v134_signal(roic, closeadj):
    base = _mean(roic * roic, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq roic
def roic_f065_return_on_invested_capital_sq_504d_accel_v135_signal(roic, closeadj):
    base = _mean(roic * roic, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z roic
def roic_f065_return_on_invested_capital_z_21d_accel_v136_signal(roic):
    base = _z(roic, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z roic
def roic_f065_return_on_invested_capital_z_21d_accel_v137_signal(roic):
    base = _z(roic, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z roic
def roic_f065_return_on_invested_capital_z_21d_accel_v138_signal(roic):
    base = _z(roic, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z roic
def roic_f065_return_on_invested_capital_z_63d_accel_v139_signal(roic):
    base = _z(roic, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z roic
def roic_f065_return_on_invested_capital_z_63d_accel_v140_signal(roic):
    base = _z(roic, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z roic
def roic_f065_return_on_invested_capital_z_63d_accel_v141_signal(roic):
    base = _z(roic, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z roic
def roic_f065_return_on_invested_capital_z_126d_accel_v142_signal(roic):
    base = _z(roic, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z roic
def roic_f065_return_on_invested_capital_z_126d_accel_v143_signal(roic):
    base = _z(roic, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z roic
def roic_f065_return_on_invested_capital_z_126d_accel_v144_signal(roic):
    base = _z(roic, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z roic
def roic_f065_return_on_invested_capital_z_252d_accel_v145_signal(roic):
    base = _z(roic, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z roic
def roic_f065_return_on_invested_capital_z_252d_accel_v146_signal(roic):
    base = _z(roic, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z roic
def roic_f065_return_on_invested_capital_z_252d_accel_v147_signal(roic):
    base = _z(roic, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z roic
def roic_f065_return_on_invested_capital_z_504d_accel_v148_signal(roic):
    base = _z(roic, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z roic
def roic_f065_return_on_invested_capital_z_504d_accel_v149_signal(roic):
    base = _z(roic, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z roic
def roic_f065_return_on_invested_capital_z_504d_accel_v150_signal(roic):
    base = _z(roic, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
