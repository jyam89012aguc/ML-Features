"""Family f063 - Return on assets (Returns and Efficiency) | Sharadar tables: SF1 | fields: roa, netinc, assetsavg | 3rd derivatives 001-150"""
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
def _return_on_assets_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _return_on_assets_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _return_on_assets_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw roa
def roa_f063_return_on_assets_raw_21d_accel_v001_signal(roa, closeadj):
    base = _mean(roa, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw roa
def roa_f063_return_on_assets_raw_21d_accel_v002_signal(roa, closeadj):
    base = _mean(roa, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw roa
def roa_f063_return_on_assets_raw_21d_accel_v003_signal(roa, closeadj):
    base = _mean(roa, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw roa
def roa_f063_return_on_assets_raw_63d_accel_v004_signal(roa, closeadj):
    base = _mean(roa, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw roa
def roa_f063_return_on_assets_raw_63d_accel_v005_signal(roa, closeadj):
    base = _mean(roa, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw roa
def roa_f063_return_on_assets_raw_63d_accel_v006_signal(roa, closeadj):
    base = _mean(roa, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw roa
def roa_f063_return_on_assets_raw_126d_accel_v007_signal(roa, closeadj):
    base = _mean(roa, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw roa
def roa_f063_return_on_assets_raw_126d_accel_v008_signal(roa, closeadj):
    base = _mean(roa, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw roa
def roa_f063_return_on_assets_raw_126d_accel_v009_signal(roa, closeadj):
    base = _mean(roa, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw roa
def roa_f063_return_on_assets_raw_252d_accel_v010_signal(roa, closeadj):
    base = _mean(roa, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw roa
def roa_f063_return_on_assets_raw_252d_accel_v011_signal(roa, closeadj):
    base = _mean(roa, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw roa
def roa_f063_return_on_assets_raw_252d_accel_v012_signal(roa, closeadj):
    base = _mean(roa, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw roa
def roa_f063_return_on_assets_raw_504d_accel_v013_signal(roa, closeadj):
    base = _mean(roa, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw roa
def roa_f063_return_on_assets_raw_504d_accel_v014_signal(roa, closeadj):
    base = _mean(roa, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw roa
def roa_f063_return_on_assets_raw_504d_accel_v015_signal(roa, closeadj):
    base = _mean(roa, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log roa
def roa_f063_return_on_assets_log_21d_accel_v016_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log roa
def roa_f063_return_on_assets_log_21d_accel_v017_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log roa
def roa_f063_return_on_assets_log_21d_accel_v018_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log roa
def roa_f063_return_on_assets_log_63d_accel_v019_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log roa
def roa_f063_return_on_assets_log_63d_accel_v020_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log roa
def roa_f063_return_on_assets_log_63d_accel_v021_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log roa
def roa_f063_return_on_assets_log_126d_accel_v022_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log roa
def roa_f063_return_on_assets_log_126d_accel_v023_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log roa
def roa_f063_return_on_assets_log_126d_accel_v024_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log roa
def roa_f063_return_on_assets_log_252d_accel_v025_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log roa
def roa_f063_return_on_assets_log_252d_accel_v026_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log roa
def roa_f063_return_on_assets_log_252d_accel_v027_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log roa
def roa_f063_return_on_assets_log_504d_accel_v028_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log roa
def roa_f063_return_on_assets_log_504d_accel_v029_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log roa
def roa_f063_return_on_assets_log_504d_accel_v030_signal(roa, closeadj):
    base = _mean(_return_on_assets_log(roa), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare roa
def roa_f063_return_on_assets_pershare_21d_accel_v031_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare roa
def roa_f063_return_on_assets_pershare_21d_accel_v032_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare roa
def roa_f063_return_on_assets_pershare_21d_accel_v033_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare roa
def roa_f063_return_on_assets_pershare_63d_accel_v034_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare roa
def roa_f063_return_on_assets_pershare_63d_accel_v035_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare roa
def roa_f063_return_on_assets_pershare_63d_accel_v036_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare roa
def roa_f063_return_on_assets_pershare_126d_accel_v037_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare roa
def roa_f063_return_on_assets_pershare_126d_accel_v038_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare roa
def roa_f063_return_on_assets_pershare_126d_accel_v039_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare roa
def roa_f063_return_on_assets_pershare_252d_accel_v040_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare roa
def roa_f063_return_on_assets_pershare_252d_accel_v041_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare roa
def roa_f063_return_on_assets_pershare_252d_accel_v042_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare roa
def roa_f063_return_on_assets_pershare_504d_accel_v043_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare roa
def roa_f063_return_on_assets_pershare_504d_accel_v044_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare roa
def roa_f063_return_on_assets_pershare_504d_accel_v045_signal(roa, sharesbas, closeadj):
    base = _mean(_return_on_assets_per_share(roa, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_netinc roa
def roa_f063_return_on_assets_per_netinc_21d_accel_v046_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_netinc roa
def roa_f063_return_on_assets_per_netinc_21d_accel_v047_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_netinc roa
def roa_f063_return_on_assets_per_netinc_21d_accel_v048_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_netinc roa
def roa_f063_return_on_assets_per_netinc_63d_accel_v049_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_netinc roa
def roa_f063_return_on_assets_per_netinc_63d_accel_v050_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_netinc roa
def roa_f063_return_on_assets_per_netinc_63d_accel_v051_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_netinc roa
def roa_f063_return_on_assets_per_netinc_126d_accel_v052_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_netinc roa
def roa_f063_return_on_assets_per_netinc_126d_accel_v053_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_netinc roa
def roa_f063_return_on_assets_per_netinc_126d_accel_v054_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_netinc roa
def roa_f063_return_on_assets_per_netinc_252d_accel_v055_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_netinc roa
def roa_f063_return_on_assets_per_netinc_252d_accel_v056_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_netinc roa
def roa_f063_return_on_assets_per_netinc_252d_accel_v057_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_netinc roa
def roa_f063_return_on_assets_per_netinc_504d_accel_v058_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_netinc roa
def roa_f063_return_on_assets_per_netinc_504d_accel_v059_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_netinc roa
def roa_f063_return_on_assets_per_netinc_504d_accel_v060_signal(roa, netinc):
    base = _mean(_return_on_assets_scaled(roa, netinc), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_21d_accel_v061_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_21d_accel_v062_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_21d_accel_v063_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_63d_accel_v064_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_63d_accel_v065_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_63d_accel_v066_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_126d_accel_v067_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_126d_accel_v068_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_126d_accel_v069_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_252d_accel_v070_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_252d_accel_v071_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_252d_accel_v072_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_504d_accel_v073_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_504d_accel_v074_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assetsavg roa
def roa_f063_return_on_assets_per_assetsavg_504d_accel_v075_signal(roa, assetsavg):
    base = _mean(_return_on_assets_scaled(roa, assetsavg), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets roa
def roa_f063_return_on_assets_per_assets_21d_accel_v076_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets roa
def roa_f063_return_on_assets_per_assets_21d_accel_v077_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets roa
def roa_f063_return_on_assets_per_assets_21d_accel_v078_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets roa
def roa_f063_return_on_assets_per_assets_63d_accel_v079_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets roa
def roa_f063_return_on_assets_per_assets_63d_accel_v080_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets roa
def roa_f063_return_on_assets_per_assets_63d_accel_v081_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets roa
def roa_f063_return_on_assets_per_assets_126d_accel_v082_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets roa
def roa_f063_return_on_assets_per_assets_126d_accel_v083_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets roa
def roa_f063_return_on_assets_per_assets_126d_accel_v084_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets roa
def roa_f063_return_on_assets_per_assets_252d_accel_v085_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets roa
def roa_f063_return_on_assets_per_assets_252d_accel_v086_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets roa
def roa_f063_return_on_assets_per_assets_252d_accel_v087_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets roa
def roa_f063_return_on_assets_per_assets_504d_accel_v088_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets roa
def roa_f063_return_on_assets_per_assets_504d_accel_v089_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets roa
def roa_f063_return_on_assets_per_assets_504d_accel_v090_signal(roa, assets):
    base = _mean(_return_on_assets_scaled(roa, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std roa
def roa_f063_return_on_assets_std_21d_accel_v091_signal(roa, closeadj):
    base = _std(roa, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std roa
def roa_f063_return_on_assets_std_21d_accel_v092_signal(roa, closeadj):
    base = _std(roa, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std roa
def roa_f063_return_on_assets_std_21d_accel_v093_signal(roa, closeadj):
    base = _std(roa, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std roa
def roa_f063_return_on_assets_std_63d_accel_v094_signal(roa, closeadj):
    base = _std(roa, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std roa
def roa_f063_return_on_assets_std_63d_accel_v095_signal(roa, closeadj):
    base = _std(roa, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std roa
def roa_f063_return_on_assets_std_63d_accel_v096_signal(roa, closeadj):
    base = _std(roa, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std roa
def roa_f063_return_on_assets_std_126d_accel_v097_signal(roa, closeadj):
    base = _std(roa, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std roa
def roa_f063_return_on_assets_std_126d_accel_v098_signal(roa, closeadj):
    base = _std(roa, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std roa
def roa_f063_return_on_assets_std_126d_accel_v099_signal(roa, closeadj):
    base = _std(roa, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std roa
def roa_f063_return_on_assets_std_252d_accel_v100_signal(roa, closeadj):
    base = _std(roa, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std roa
def roa_f063_return_on_assets_std_252d_accel_v101_signal(roa, closeadj):
    base = _std(roa, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std roa
def roa_f063_return_on_assets_std_252d_accel_v102_signal(roa, closeadj):
    base = _std(roa, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std roa
def roa_f063_return_on_assets_std_504d_accel_v103_signal(roa, closeadj):
    base = _std(roa, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std roa
def roa_f063_return_on_assets_std_504d_accel_v104_signal(roa, closeadj):
    base = _std(roa, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std roa
def roa_f063_return_on_assets_std_504d_accel_v105_signal(roa, closeadj):
    base = _std(roa, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm roa
def roa_f063_return_on_assets_ewm_21d_accel_v106_signal(roa, closeadj):
    base = roa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm roa
def roa_f063_return_on_assets_ewm_21d_accel_v107_signal(roa, closeadj):
    base = roa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm roa
def roa_f063_return_on_assets_ewm_21d_accel_v108_signal(roa, closeadj):
    base = roa.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm roa
def roa_f063_return_on_assets_ewm_63d_accel_v109_signal(roa, closeadj):
    base = roa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm roa
def roa_f063_return_on_assets_ewm_63d_accel_v110_signal(roa, closeadj):
    base = roa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm roa
def roa_f063_return_on_assets_ewm_63d_accel_v111_signal(roa, closeadj):
    base = roa.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm roa
def roa_f063_return_on_assets_ewm_126d_accel_v112_signal(roa, closeadj):
    base = roa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm roa
def roa_f063_return_on_assets_ewm_126d_accel_v113_signal(roa, closeadj):
    base = roa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm roa
def roa_f063_return_on_assets_ewm_126d_accel_v114_signal(roa, closeadj):
    base = roa.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm roa
def roa_f063_return_on_assets_ewm_252d_accel_v115_signal(roa, closeadj):
    base = roa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm roa
def roa_f063_return_on_assets_ewm_252d_accel_v116_signal(roa, closeadj):
    base = roa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm roa
def roa_f063_return_on_assets_ewm_252d_accel_v117_signal(roa, closeadj):
    base = roa.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm roa
def roa_f063_return_on_assets_ewm_504d_accel_v118_signal(roa, closeadj):
    base = roa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm roa
def roa_f063_return_on_assets_ewm_504d_accel_v119_signal(roa, closeadj):
    base = roa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm roa
def roa_f063_return_on_assets_ewm_504d_accel_v120_signal(roa, closeadj):
    base = roa.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq roa
def roa_f063_return_on_assets_sq_21d_accel_v121_signal(roa, closeadj):
    base = _mean(roa * roa, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq roa
def roa_f063_return_on_assets_sq_21d_accel_v122_signal(roa, closeadj):
    base = _mean(roa * roa, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq roa
def roa_f063_return_on_assets_sq_21d_accel_v123_signal(roa, closeadj):
    base = _mean(roa * roa, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq roa
def roa_f063_return_on_assets_sq_63d_accel_v124_signal(roa, closeadj):
    base = _mean(roa * roa, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq roa
def roa_f063_return_on_assets_sq_63d_accel_v125_signal(roa, closeadj):
    base = _mean(roa * roa, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq roa
def roa_f063_return_on_assets_sq_63d_accel_v126_signal(roa, closeadj):
    base = _mean(roa * roa, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq roa
def roa_f063_return_on_assets_sq_126d_accel_v127_signal(roa, closeadj):
    base = _mean(roa * roa, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq roa
def roa_f063_return_on_assets_sq_126d_accel_v128_signal(roa, closeadj):
    base = _mean(roa * roa, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq roa
def roa_f063_return_on_assets_sq_126d_accel_v129_signal(roa, closeadj):
    base = _mean(roa * roa, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq roa
def roa_f063_return_on_assets_sq_252d_accel_v130_signal(roa, closeadj):
    base = _mean(roa * roa, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq roa
def roa_f063_return_on_assets_sq_252d_accel_v131_signal(roa, closeadj):
    base = _mean(roa * roa, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq roa
def roa_f063_return_on_assets_sq_252d_accel_v132_signal(roa, closeadj):
    base = _mean(roa * roa, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq roa
def roa_f063_return_on_assets_sq_504d_accel_v133_signal(roa, closeadj):
    base = _mean(roa * roa, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq roa
def roa_f063_return_on_assets_sq_504d_accel_v134_signal(roa, closeadj):
    base = _mean(roa * roa, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq roa
def roa_f063_return_on_assets_sq_504d_accel_v135_signal(roa, closeadj):
    base = _mean(roa * roa, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z roa
def roa_f063_return_on_assets_z_21d_accel_v136_signal(roa):
    base = _z(roa, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z roa
def roa_f063_return_on_assets_z_21d_accel_v137_signal(roa):
    base = _z(roa, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z roa
def roa_f063_return_on_assets_z_21d_accel_v138_signal(roa):
    base = _z(roa, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z roa
def roa_f063_return_on_assets_z_63d_accel_v139_signal(roa):
    base = _z(roa, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z roa
def roa_f063_return_on_assets_z_63d_accel_v140_signal(roa):
    base = _z(roa, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z roa
def roa_f063_return_on_assets_z_63d_accel_v141_signal(roa):
    base = _z(roa, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z roa
def roa_f063_return_on_assets_z_126d_accel_v142_signal(roa):
    base = _z(roa, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z roa
def roa_f063_return_on_assets_z_126d_accel_v143_signal(roa):
    base = _z(roa, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z roa
def roa_f063_return_on_assets_z_126d_accel_v144_signal(roa):
    base = _z(roa, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z roa
def roa_f063_return_on_assets_z_252d_accel_v145_signal(roa):
    base = _z(roa, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z roa
def roa_f063_return_on_assets_z_252d_accel_v146_signal(roa):
    base = _z(roa, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z roa
def roa_f063_return_on_assets_z_252d_accel_v147_signal(roa):
    base = _z(roa, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z roa
def roa_f063_return_on_assets_z_504d_accel_v148_signal(roa):
    base = _z(roa, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z roa
def roa_f063_return_on_assets_z_504d_accel_v149_signal(roa):
    base = _z(roa, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z roa
def roa_f063_return_on_assets_z_504d_accel_v150_signal(roa):
    base = _z(roa, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
