"""Family f027 - Accumulated deficit and retained earnings (Capital Structure) | Sharadar tables: SF1 | fields: retearn, equity, assets | 3rd derivatives 001-150"""
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
def _retained_deficit_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _retained_deficit_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _retained_deficit_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw retearn
def rd_f027_retained_deficit_raw_21d_accel_v001_signal(retearn, closeadj):
    base = _mean(retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw retearn
def rd_f027_retained_deficit_raw_21d_accel_v002_signal(retearn, closeadj):
    base = _mean(retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw retearn
def rd_f027_retained_deficit_raw_21d_accel_v003_signal(retearn, closeadj):
    base = _mean(retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw retearn
def rd_f027_retained_deficit_raw_63d_accel_v004_signal(retearn, closeadj):
    base = _mean(retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw retearn
def rd_f027_retained_deficit_raw_63d_accel_v005_signal(retearn, closeadj):
    base = _mean(retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw retearn
def rd_f027_retained_deficit_raw_63d_accel_v006_signal(retearn, closeadj):
    base = _mean(retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw retearn
def rd_f027_retained_deficit_raw_126d_accel_v007_signal(retearn, closeadj):
    base = _mean(retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw retearn
def rd_f027_retained_deficit_raw_126d_accel_v008_signal(retearn, closeadj):
    base = _mean(retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw retearn
def rd_f027_retained_deficit_raw_126d_accel_v009_signal(retearn, closeadj):
    base = _mean(retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw retearn
def rd_f027_retained_deficit_raw_252d_accel_v010_signal(retearn, closeadj):
    base = _mean(retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw retearn
def rd_f027_retained_deficit_raw_252d_accel_v011_signal(retearn, closeadj):
    base = _mean(retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw retearn
def rd_f027_retained_deficit_raw_252d_accel_v012_signal(retearn, closeadj):
    base = _mean(retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw retearn
def rd_f027_retained_deficit_raw_504d_accel_v013_signal(retearn, closeadj):
    base = _mean(retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw retearn
def rd_f027_retained_deficit_raw_504d_accel_v014_signal(retearn, closeadj):
    base = _mean(retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw retearn
def rd_f027_retained_deficit_raw_504d_accel_v015_signal(retearn, closeadj):
    base = _mean(retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log retearn
def rd_f027_retained_deficit_log_21d_accel_v016_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log retearn
def rd_f027_retained_deficit_log_21d_accel_v017_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log retearn
def rd_f027_retained_deficit_log_21d_accel_v018_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log retearn
def rd_f027_retained_deficit_log_63d_accel_v019_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log retearn
def rd_f027_retained_deficit_log_63d_accel_v020_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log retearn
def rd_f027_retained_deficit_log_63d_accel_v021_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log retearn
def rd_f027_retained_deficit_log_126d_accel_v022_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log retearn
def rd_f027_retained_deficit_log_126d_accel_v023_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log retearn
def rd_f027_retained_deficit_log_126d_accel_v024_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log retearn
def rd_f027_retained_deficit_log_252d_accel_v025_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log retearn
def rd_f027_retained_deficit_log_252d_accel_v026_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log retearn
def rd_f027_retained_deficit_log_252d_accel_v027_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log retearn
def rd_f027_retained_deficit_log_504d_accel_v028_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log retearn
def rd_f027_retained_deficit_log_504d_accel_v029_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log retearn
def rd_f027_retained_deficit_log_504d_accel_v030_signal(retearn, closeadj):
    base = _mean(_retained_deficit_log(retearn), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare retearn
def rd_f027_retained_deficit_pershare_21d_accel_v031_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare retearn
def rd_f027_retained_deficit_pershare_21d_accel_v032_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare retearn
def rd_f027_retained_deficit_pershare_21d_accel_v033_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare retearn
def rd_f027_retained_deficit_pershare_63d_accel_v034_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare retearn
def rd_f027_retained_deficit_pershare_63d_accel_v035_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare retearn
def rd_f027_retained_deficit_pershare_63d_accel_v036_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare retearn
def rd_f027_retained_deficit_pershare_126d_accel_v037_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare retearn
def rd_f027_retained_deficit_pershare_126d_accel_v038_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare retearn
def rd_f027_retained_deficit_pershare_126d_accel_v039_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare retearn
def rd_f027_retained_deficit_pershare_252d_accel_v040_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare retearn
def rd_f027_retained_deficit_pershare_252d_accel_v041_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare retearn
def rd_f027_retained_deficit_pershare_252d_accel_v042_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare retearn
def rd_f027_retained_deficit_pershare_504d_accel_v043_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare retearn
def rd_f027_retained_deficit_pershare_504d_accel_v044_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare retearn
def rd_f027_retained_deficit_pershare_504d_accel_v045_signal(retearn, sharesbas, closeadj):
    base = _mean(_retained_deficit_per_share(retearn, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity retearn
def rd_f027_retained_deficit_per_equity_21d_accel_v046_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity retearn
def rd_f027_retained_deficit_per_equity_21d_accel_v047_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity retearn
def rd_f027_retained_deficit_per_equity_21d_accel_v048_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity retearn
def rd_f027_retained_deficit_per_equity_63d_accel_v049_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity retearn
def rd_f027_retained_deficit_per_equity_63d_accel_v050_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity retearn
def rd_f027_retained_deficit_per_equity_63d_accel_v051_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity retearn
def rd_f027_retained_deficit_per_equity_126d_accel_v052_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity retearn
def rd_f027_retained_deficit_per_equity_126d_accel_v053_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity retearn
def rd_f027_retained_deficit_per_equity_126d_accel_v054_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity retearn
def rd_f027_retained_deficit_per_equity_252d_accel_v055_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity retearn
def rd_f027_retained_deficit_per_equity_252d_accel_v056_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity retearn
def rd_f027_retained_deficit_per_equity_252d_accel_v057_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity retearn
def rd_f027_retained_deficit_per_equity_504d_accel_v058_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity retearn
def rd_f027_retained_deficit_per_equity_504d_accel_v059_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity retearn
def rd_f027_retained_deficit_per_equity_504d_accel_v060_signal(retearn, equity):
    base = _mean(_retained_deficit_scaled(retearn, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets retearn
def rd_f027_retained_deficit_per_assets_21d_accel_v061_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets retearn
def rd_f027_retained_deficit_per_assets_21d_accel_v062_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets retearn
def rd_f027_retained_deficit_per_assets_21d_accel_v063_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets retearn
def rd_f027_retained_deficit_per_assets_63d_accel_v064_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets retearn
def rd_f027_retained_deficit_per_assets_63d_accel_v065_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets retearn
def rd_f027_retained_deficit_per_assets_63d_accel_v066_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets retearn
def rd_f027_retained_deficit_per_assets_126d_accel_v067_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets retearn
def rd_f027_retained_deficit_per_assets_126d_accel_v068_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets retearn
def rd_f027_retained_deficit_per_assets_126d_accel_v069_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets retearn
def rd_f027_retained_deficit_per_assets_252d_accel_v070_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets retearn
def rd_f027_retained_deficit_per_assets_252d_accel_v071_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets retearn
def rd_f027_retained_deficit_per_assets_252d_accel_v072_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets retearn
def rd_f027_retained_deficit_per_assets_504d_accel_v073_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets retearn
def rd_f027_retained_deficit_per_assets_504d_accel_v074_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets retearn
def rd_f027_retained_deficit_per_assets_504d_accel_v075_signal(retearn, assets):
    base = _mean(_retained_deficit_scaled(retearn, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_21d_accel_v076_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_21d_accel_v077_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_21d_accel_v078_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_63d_accel_v079_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_63d_accel_v080_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_63d_accel_v081_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_126d_accel_v082_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_126d_accel_v083_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_126d_accel_v084_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_252d_accel_v085_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_252d_accel_v086_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_252d_accel_v087_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_504d_accel_v088_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_504d_accel_v089_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap retearn
def rd_f027_retained_deficit_per_marketcap_504d_accel_v090_signal(retearn, marketcap):
    base = _mean(_retained_deficit_scaled(retearn, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std retearn
def rd_f027_retained_deficit_std_21d_accel_v091_signal(retearn, closeadj):
    base = _std(retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std retearn
def rd_f027_retained_deficit_std_21d_accel_v092_signal(retearn, closeadj):
    base = _std(retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std retearn
def rd_f027_retained_deficit_std_21d_accel_v093_signal(retearn, closeadj):
    base = _std(retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std retearn
def rd_f027_retained_deficit_std_63d_accel_v094_signal(retearn, closeadj):
    base = _std(retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std retearn
def rd_f027_retained_deficit_std_63d_accel_v095_signal(retearn, closeadj):
    base = _std(retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std retearn
def rd_f027_retained_deficit_std_63d_accel_v096_signal(retearn, closeadj):
    base = _std(retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std retearn
def rd_f027_retained_deficit_std_126d_accel_v097_signal(retearn, closeadj):
    base = _std(retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std retearn
def rd_f027_retained_deficit_std_126d_accel_v098_signal(retearn, closeadj):
    base = _std(retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std retearn
def rd_f027_retained_deficit_std_126d_accel_v099_signal(retearn, closeadj):
    base = _std(retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std retearn
def rd_f027_retained_deficit_std_252d_accel_v100_signal(retearn, closeadj):
    base = _std(retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std retearn
def rd_f027_retained_deficit_std_252d_accel_v101_signal(retearn, closeadj):
    base = _std(retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std retearn
def rd_f027_retained_deficit_std_252d_accel_v102_signal(retearn, closeadj):
    base = _std(retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std retearn
def rd_f027_retained_deficit_std_504d_accel_v103_signal(retearn, closeadj):
    base = _std(retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std retearn
def rd_f027_retained_deficit_std_504d_accel_v104_signal(retearn, closeadj):
    base = _std(retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std retearn
def rd_f027_retained_deficit_std_504d_accel_v105_signal(retearn, closeadj):
    base = _std(retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm retearn
def rd_f027_retained_deficit_ewm_21d_accel_v106_signal(retearn, closeadj):
    base = retearn.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm retearn
def rd_f027_retained_deficit_ewm_21d_accel_v107_signal(retearn, closeadj):
    base = retearn.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm retearn
def rd_f027_retained_deficit_ewm_21d_accel_v108_signal(retearn, closeadj):
    base = retearn.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm retearn
def rd_f027_retained_deficit_ewm_63d_accel_v109_signal(retearn, closeadj):
    base = retearn.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm retearn
def rd_f027_retained_deficit_ewm_63d_accel_v110_signal(retearn, closeadj):
    base = retearn.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm retearn
def rd_f027_retained_deficit_ewm_63d_accel_v111_signal(retearn, closeadj):
    base = retearn.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm retearn
def rd_f027_retained_deficit_ewm_126d_accel_v112_signal(retearn, closeadj):
    base = retearn.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm retearn
def rd_f027_retained_deficit_ewm_126d_accel_v113_signal(retearn, closeadj):
    base = retearn.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm retearn
def rd_f027_retained_deficit_ewm_126d_accel_v114_signal(retearn, closeadj):
    base = retearn.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm retearn
def rd_f027_retained_deficit_ewm_252d_accel_v115_signal(retearn, closeadj):
    base = retearn.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm retearn
def rd_f027_retained_deficit_ewm_252d_accel_v116_signal(retearn, closeadj):
    base = retearn.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm retearn
def rd_f027_retained_deficit_ewm_252d_accel_v117_signal(retearn, closeadj):
    base = retearn.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm retearn
def rd_f027_retained_deficit_ewm_504d_accel_v118_signal(retearn, closeadj):
    base = retearn.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm retearn
def rd_f027_retained_deficit_ewm_504d_accel_v119_signal(retearn, closeadj):
    base = retearn.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm retearn
def rd_f027_retained_deficit_ewm_504d_accel_v120_signal(retearn, closeadj):
    base = retearn.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq retearn
def rd_f027_retained_deficit_sq_21d_accel_v121_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq retearn
def rd_f027_retained_deficit_sq_21d_accel_v122_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq retearn
def rd_f027_retained_deficit_sq_21d_accel_v123_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq retearn
def rd_f027_retained_deficit_sq_63d_accel_v124_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq retearn
def rd_f027_retained_deficit_sq_63d_accel_v125_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq retearn
def rd_f027_retained_deficit_sq_63d_accel_v126_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq retearn
def rd_f027_retained_deficit_sq_126d_accel_v127_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq retearn
def rd_f027_retained_deficit_sq_126d_accel_v128_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq retearn
def rd_f027_retained_deficit_sq_126d_accel_v129_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq retearn
def rd_f027_retained_deficit_sq_252d_accel_v130_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq retearn
def rd_f027_retained_deficit_sq_252d_accel_v131_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq retearn
def rd_f027_retained_deficit_sq_252d_accel_v132_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq retearn
def rd_f027_retained_deficit_sq_504d_accel_v133_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq retearn
def rd_f027_retained_deficit_sq_504d_accel_v134_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq retearn
def rd_f027_retained_deficit_sq_504d_accel_v135_signal(retearn, closeadj):
    base = _mean(retearn * retearn, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z retearn
def rd_f027_retained_deficit_z_21d_accel_v136_signal(retearn):
    base = _z(retearn, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z retearn
def rd_f027_retained_deficit_z_21d_accel_v137_signal(retearn):
    base = _z(retearn, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z retearn
def rd_f027_retained_deficit_z_21d_accel_v138_signal(retearn):
    base = _z(retearn, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z retearn
def rd_f027_retained_deficit_z_63d_accel_v139_signal(retearn):
    base = _z(retearn, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z retearn
def rd_f027_retained_deficit_z_63d_accel_v140_signal(retearn):
    base = _z(retearn, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z retearn
def rd_f027_retained_deficit_z_63d_accel_v141_signal(retearn):
    base = _z(retearn, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z retearn
def rd_f027_retained_deficit_z_126d_accel_v142_signal(retearn):
    base = _z(retearn, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z retearn
def rd_f027_retained_deficit_z_126d_accel_v143_signal(retearn):
    base = _z(retearn, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z retearn
def rd_f027_retained_deficit_z_126d_accel_v144_signal(retearn):
    base = _z(retearn, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z retearn
def rd_f027_retained_deficit_z_252d_accel_v145_signal(retearn):
    base = _z(retearn, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z retearn
def rd_f027_retained_deficit_z_252d_accel_v146_signal(retearn):
    base = _z(retearn, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z retearn
def rd_f027_retained_deficit_z_252d_accel_v147_signal(retearn):
    base = _z(retearn, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z retearn
def rd_f027_retained_deficit_z_504d_accel_v148_signal(retearn):
    base = _z(retearn, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z retearn
def rd_f027_retained_deficit_z_504d_accel_v149_signal(retearn):
    base = _z(retearn, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z retearn
def rd_f027_retained_deficit_z_504d_accel_v150_signal(retearn):
    base = _z(retearn, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
