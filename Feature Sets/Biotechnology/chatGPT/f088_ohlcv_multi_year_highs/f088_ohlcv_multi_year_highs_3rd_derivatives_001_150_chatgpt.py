"""Family f088 - OHLCV highest-highs context (Market Context from Sharadar Prices) | Sharadar tables: SEP,SFP | fields: date, open, high, low, close, volume, closeadj, closeunadj | 3rd derivatives 001-150"""
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
def _ohlcv_multi_year_highs_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ohlcv_multi_year_highs_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ohlcv_multi_year_highs_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_21d_accel_v001_signal(open, closeadj):
    base = _mean(open, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_21d_accel_v002_signal(open, closeadj):
    base = _mean(open, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_21d_accel_v003_signal(open, closeadj):
    base = _mean(open, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_63d_accel_v004_signal(open, closeadj):
    base = _mean(open, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_63d_accel_v005_signal(open, closeadj):
    base = _mean(open, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_63d_accel_v006_signal(open, closeadj):
    base = _mean(open, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_126d_accel_v007_signal(open, closeadj):
    base = _mean(open, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_126d_accel_v008_signal(open, closeadj):
    base = _mean(open, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_126d_accel_v009_signal(open, closeadj):
    base = _mean(open, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_252d_accel_v010_signal(open, closeadj):
    base = _mean(open, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_252d_accel_v011_signal(open, closeadj):
    base = _mean(open, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_252d_accel_v012_signal(open, closeadj):
    base = _mean(open, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_504d_accel_v013_signal(open, closeadj):
    base = _mean(open, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_504d_accel_v014_signal(open, closeadj):
    base = _mean(open, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_504d_accel_v015_signal(open, closeadj):
    base = _mean(open, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log open
def omyh_f088_ohlcv_multi_year_highs_log_21d_accel_v016_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log open
def omyh_f088_ohlcv_multi_year_highs_log_21d_accel_v017_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log open
def omyh_f088_ohlcv_multi_year_highs_log_21d_accel_v018_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log open
def omyh_f088_ohlcv_multi_year_highs_log_63d_accel_v019_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log open
def omyh_f088_ohlcv_multi_year_highs_log_63d_accel_v020_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log open
def omyh_f088_ohlcv_multi_year_highs_log_63d_accel_v021_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log open
def omyh_f088_ohlcv_multi_year_highs_log_126d_accel_v022_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log open
def omyh_f088_ohlcv_multi_year_highs_log_126d_accel_v023_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log open
def omyh_f088_ohlcv_multi_year_highs_log_126d_accel_v024_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log open
def omyh_f088_ohlcv_multi_year_highs_log_252d_accel_v025_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log open
def omyh_f088_ohlcv_multi_year_highs_log_252d_accel_v026_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log open
def omyh_f088_ohlcv_multi_year_highs_log_252d_accel_v027_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log open
def omyh_f088_ohlcv_multi_year_highs_log_504d_accel_v028_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log open
def omyh_f088_ohlcv_multi_year_highs_log_504d_accel_v029_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log open
def omyh_f088_ohlcv_multi_year_highs_log_504d_accel_v030_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_21d_accel_v031_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_21d_accel_v032_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_21d_accel_v033_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_63d_accel_v034_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_63d_accel_v035_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_63d_accel_v036_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_126d_accel_v037_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_126d_accel_v038_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_126d_accel_v039_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_252d_accel_v040_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_252d_accel_v041_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_252d_accel_v042_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_504d_accel_v043_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_504d_accel_v044_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_504d_accel_v045_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_21d_accel_v046_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_21d_accel_v047_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_21d_accel_v048_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_63d_accel_v049_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_63d_accel_v050_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_63d_accel_v051_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_126d_accel_v052_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_126d_accel_v053_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_126d_accel_v054_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_252d_accel_v055_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_252d_accel_v056_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_252d_accel_v057_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_504d_accel_v058_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_504d_accel_v059_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_504d_accel_v060_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_21d_accel_v061_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_21d_accel_v062_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_21d_accel_v063_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_63d_accel_v064_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_63d_accel_v065_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_63d_accel_v066_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_126d_accel_v067_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_126d_accel_v068_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_126d_accel_v069_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_252d_accel_v070_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_252d_accel_v071_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_252d_accel_v072_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_504d_accel_v073_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_504d_accel_v074_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_504d_accel_v075_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_21d_accel_v076_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_21d_accel_v077_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_21d_accel_v078_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_63d_accel_v079_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_63d_accel_v080_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_63d_accel_v081_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_126d_accel_v082_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_126d_accel_v083_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_126d_accel_v084_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_252d_accel_v085_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_252d_accel_v086_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_252d_accel_v087_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_504d_accel_v088_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_504d_accel_v089_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_504d_accel_v090_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std open
def omyh_f088_ohlcv_multi_year_highs_std_21d_accel_v091_signal(open, closeadj):
    base = _std(open, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std open
def omyh_f088_ohlcv_multi_year_highs_std_21d_accel_v092_signal(open, closeadj):
    base = _std(open, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std open
def omyh_f088_ohlcv_multi_year_highs_std_21d_accel_v093_signal(open, closeadj):
    base = _std(open, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std open
def omyh_f088_ohlcv_multi_year_highs_std_63d_accel_v094_signal(open, closeadj):
    base = _std(open, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std open
def omyh_f088_ohlcv_multi_year_highs_std_63d_accel_v095_signal(open, closeadj):
    base = _std(open, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std open
def omyh_f088_ohlcv_multi_year_highs_std_63d_accel_v096_signal(open, closeadj):
    base = _std(open, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std open
def omyh_f088_ohlcv_multi_year_highs_std_126d_accel_v097_signal(open, closeadj):
    base = _std(open, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std open
def omyh_f088_ohlcv_multi_year_highs_std_126d_accel_v098_signal(open, closeadj):
    base = _std(open, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std open
def omyh_f088_ohlcv_multi_year_highs_std_126d_accel_v099_signal(open, closeadj):
    base = _std(open, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std open
def omyh_f088_ohlcv_multi_year_highs_std_252d_accel_v100_signal(open, closeadj):
    base = _std(open, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std open
def omyh_f088_ohlcv_multi_year_highs_std_252d_accel_v101_signal(open, closeadj):
    base = _std(open, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std open
def omyh_f088_ohlcv_multi_year_highs_std_252d_accel_v102_signal(open, closeadj):
    base = _std(open, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std open
def omyh_f088_ohlcv_multi_year_highs_std_504d_accel_v103_signal(open, closeadj):
    base = _std(open, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std open
def omyh_f088_ohlcv_multi_year_highs_std_504d_accel_v104_signal(open, closeadj):
    base = _std(open, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std open
def omyh_f088_ohlcv_multi_year_highs_std_504d_accel_v105_signal(open, closeadj):
    base = _std(open, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_21d_accel_v106_signal(open, closeadj):
    base = open.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_21d_accel_v107_signal(open, closeadj):
    base = open.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_21d_accel_v108_signal(open, closeadj):
    base = open.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_63d_accel_v109_signal(open, closeadj):
    base = open.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_63d_accel_v110_signal(open, closeadj):
    base = open.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_63d_accel_v111_signal(open, closeadj):
    base = open.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_126d_accel_v112_signal(open, closeadj):
    base = open.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_126d_accel_v113_signal(open, closeadj):
    base = open.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_126d_accel_v114_signal(open, closeadj):
    base = open.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_252d_accel_v115_signal(open, closeadj):
    base = open.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_252d_accel_v116_signal(open, closeadj):
    base = open.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_252d_accel_v117_signal(open, closeadj):
    base = open.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_504d_accel_v118_signal(open, closeadj):
    base = open.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_504d_accel_v119_signal(open, closeadj):
    base = open.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_504d_accel_v120_signal(open, closeadj):
    base = open.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_21d_accel_v121_signal(open, closeadj):
    base = _mean(open * open, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_21d_accel_v122_signal(open, closeadj):
    base = _mean(open * open, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_21d_accel_v123_signal(open, closeadj):
    base = _mean(open * open, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_63d_accel_v124_signal(open, closeadj):
    base = _mean(open * open, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_63d_accel_v125_signal(open, closeadj):
    base = _mean(open * open, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_63d_accel_v126_signal(open, closeadj):
    base = _mean(open * open, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_126d_accel_v127_signal(open, closeadj):
    base = _mean(open * open, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_126d_accel_v128_signal(open, closeadj):
    base = _mean(open * open, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_126d_accel_v129_signal(open, closeadj):
    base = _mean(open * open, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_252d_accel_v130_signal(open, closeadj):
    base = _mean(open * open, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_252d_accel_v131_signal(open, closeadj):
    base = _mean(open * open, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_252d_accel_v132_signal(open, closeadj):
    base = _mean(open * open, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_504d_accel_v133_signal(open, closeadj):
    base = _mean(open * open, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_504d_accel_v134_signal(open, closeadj):
    base = _mean(open * open, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_504d_accel_v135_signal(open, closeadj):
    base = _mean(open * open, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z open
def omyh_f088_ohlcv_multi_year_highs_z_21d_accel_v136_signal(open):
    base = _z(open, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z open
def omyh_f088_ohlcv_multi_year_highs_z_21d_accel_v137_signal(open):
    base = _z(open, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z open
def omyh_f088_ohlcv_multi_year_highs_z_21d_accel_v138_signal(open):
    base = _z(open, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z open
def omyh_f088_ohlcv_multi_year_highs_z_63d_accel_v139_signal(open):
    base = _z(open, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z open
def omyh_f088_ohlcv_multi_year_highs_z_63d_accel_v140_signal(open):
    base = _z(open, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z open
def omyh_f088_ohlcv_multi_year_highs_z_63d_accel_v141_signal(open):
    base = _z(open, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z open
def omyh_f088_ohlcv_multi_year_highs_z_126d_accel_v142_signal(open):
    base = _z(open, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z open
def omyh_f088_ohlcv_multi_year_highs_z_126d_accel_v143_signal(open):
    base = _z(open, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z open
def omyh_f088_ohlcv_multi_year_highs_z_126d_accel_v144_signal(open):
    base = _z(open, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z open
def omyh_f088_ohlcv_multi_year_highs_z_252d_accel_v145_signal(open):
    base = _z(open, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z open
def omyh_f088_ohlcv_multi_year_highs_z_252d_accel_v146_signal(open):
    base = _z(open, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z open
def omyh_f088_ohlcv_multi_year_highs_z_252d_accel_v147_signal(open):
    base = _z(open, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z open
def omyh_f088_ohlcv_multi_year_highs_z_504d_accel_v148_signal(open):
    base = _z(open, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z open
def omyh_f088_ohlcv_multi_year_highs_z_504d_accel_v149_signal(open):
    base = _z(open, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z open
def omyh_f088_ohlcv_multi_year_highs_z_504d_accel_v150_signal(open):
    base = _z(open, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
