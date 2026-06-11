"""Family f088 - OHLCV highest-highs context (Market Context from Sharadar Prices) | Sharadar tables: SEP,SFP | fields: date, open, high, low, close, volume, closeadj, closeunadj | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_21d_slope_v001_signal(open, closeadj):
    base = _mean(open, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_21d_slope_v002_signal(open, closeadj):
    base = _mean(open, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_21d_slope_v003_signal(open, closeadj):
    base = _mean(open, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_63d_slope_v004_signal(open, closeadj):
    base = _mean(open, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_63d_slope_v005_signal(open, closeadj):
    base = _mean(open, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_63d_slope_v006_signal(open, closeadj):
    base = _mean(open, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_126d_slope_v007_signal(open, closeadj):
    base = _mean(open, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_126d_slope_v008_signal(open, closeadj):
    base = _mean(open, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_126d_slope_v009_signal(open, closeadj):
    base = _mean(open, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_252d_slope_v010_signal(open, closeadj):
    base = _mean(open, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_252d_slope_v011_signal(open, closeadj):
    base = _mean(open, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_252d_slope_v012_signal(open, closeadj):
    base = _mean(open, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_504d_slope_v013_signal(open, closeadj):
    base = _mean(open, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_504d_slope_v014_signal(open, closeadj):
    base = _mean(open, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw open
def omyh_f088_ohlcv_multi_year_highs_raw_504d_slope_v015_signal(open, closeadj):
    base = _mean(open, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log open
def omyh_f088_ohlcv_multi_year_highs_log_21d_slope_v016_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log open
def omyh_f088_ohlcv_multi_year_highs_log_21d_slope_v017_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log open
def omyh_f088_ohlcv_multi_year_highs_log_21d_slope_v018_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log open
def omyh_f088_ohlcv_multi_year_highs_log_63d_slope_v019_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log open
def omyh_f088_ohlcv_multi_year_highs_log_63d_slope_v020_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log open
def omyh_f088_ohlcv_multi_year_highs_log_63d_slope_v021_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log open
def omyh_f088_ohlcv_multi_year_highs_log_126d_slope_v022_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log open
def omyh_f088_ohlcv_multi_year_highs_log_126d_slope_v023_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log open
def omyh_f088_ohlcv_multi_year_highs_log_126d_slope_v024_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log open
def omyh_f088_ohlcv_multi_year_highs_log_252d_slope_v025_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log open
def omyh_f088_ohlcv_multi_year_highs_log_252d_slope_v026_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log open
def omyh_f088_ohlcv_multi_year_highs_log_252d_slope_v027_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log open
def omyh_f088_ohlcv_multi_year_highs_log_504d_slope_v028_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log open
def omyh_f088_ohlcv_multi_year_highs_log_504d_slope_v029_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log open
def omyh_f088_ohlcv_multi_year_highs_log_504d_slope_v030_signal(open, closeadj):
    base = _mean(_ohlcv_multi_year_highs_log(open), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_21d_slope_v031_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_21d_slope_v032_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_21d_slope_v033_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_63d_slope_v034_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_63d_slope_v035_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_63d_slope_v036_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_126d_slope_v037_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_126d_slope_v038_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_126d_slope_v039_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_252d_slope_v040_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_252d_slope_v041_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_252d_slope_v042_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_504d_slope_v043_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_504d_slope_v044_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare open
def omyh_f088_ohlcv_multi_year_highs_pershare_504d_slope_v045_signal(open, sharesbas, closeadj):
    base = _mean(_ohlcv_multi_year_highs_per_share(open, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_21d_slope_v046_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_21d_slope_v047_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_21d_slope_v048_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_63d_slope_v049_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_63d_slope_v050_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_63d_slope_v051_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_126d_slope_v052_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_126d_slope_v053_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_126d_slope_v054_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_252d_slope_v055_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_252d_slope_v056_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_252d_slope_v057_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_504d_slope_v058_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_504d_slope_v059_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_high open
def omyh_f088_ohlcv_multi_year_highs_per_high_504d_slope_v060_signal(open, high):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, high), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_21d_slope_v061_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_21d_slope_v062_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_21d_slope_v063_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_63d_slope_v064_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_63d_slope_v065_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_63d_slope_v066_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_126d_slope_v067_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_126d_slope_v068_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_126d_slope_v069_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_252d_slope_v070_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_252d_slope_v071_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_252d_slope_v072_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_504d_slope_v073_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_504d_slope_v074_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_low open
def omyh_f088_ohlcv_multi_year_highs_per_low_504d_slope_v075_signal(open, low):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, low), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_21d_slope_v076_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_21d_slope_v077_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_21d_slope_v078_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_63d_slope_v079_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_63d_slope_v080_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_63d_slope_v081_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_126d_slope_v082_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_126d_slope_v083_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_126d_slope_v084_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_252d_slope_v085_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_252d_slope_v086_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_252d_slope_v087_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_504d_slope_v088_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_504d_slope_v089_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_close open
def omyh_f088_ohlcv_multi_year_highs_per_close_504d_slope_v090_signal(open, close):
    base = _mean(_ohlcv_multi_year_highs_scaled(open, close), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std open
def omyh_f088_ohlcv_multi_year_highs_std_21d_slope_v091_signal(open, closeadj):
    base = _std(open, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std open
def omyh_f088_ohlcv_multi_year_highs_std_21d_slope_v092_signal(open, closeadj):
    base = _std(open, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std open
def omyh_f088_ohlcv_multi_year_highs_std_21d_slope_v093_signal(open, closeadj):
    base = _std(open, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std open
def omyh_f088_ohlcv_multi_year_highs_std_63d_slope_v094_signal(open, closeadj):
    base = _std(open, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std open
def omyh_f088_ohlcv_multi_year_highs_std_63d_slope_v095_signal(open, closeadj):
    base = _std(open, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std open
def omyh_f088_ohlcv_multi_year_highs_std_63d_slope_v096_signal(open, closeadj):
    base = _std(open, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std open
def omyh_f088_ohlcv_multi_year_highs_std_126d_slope_v097_signal(open, closeadj):
    base = _std(open, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std open
def omyh_f088_ohlcv_multi_year_highs_std_126d_slope_v098_signal(open, closeadj):
    base = _std(open, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std open
def omyh_f088_ohlcv_multi_year_highs_std_126d_slope_v099_signal(open, closeadj):
    base = _std(open, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std open
def omyh_f088_ohlcv_multi_year_highs_std_252d_slope_v100_signal(open, closeadj):
    base = _std(open, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std open
def omyh_f088_ohlcv_multi_year_highs_std_252d_slope_v101_signal(open, closeadj):
    base = _std(open, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std open
def omyh_f088_ohlcv_multi_year_highs_std_252d_slope_v102_signal(open, closeadj):
    base = _std(open, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std open
def omyh_f088_ohlcv_multi_year_highs_std_504d_slope_v103_signal(open, closeadj):
    base = _std(open, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std open
def omyh_f088_ohlcv_multi_year_highs_std_504d_slope_v104_signal(open, closeadj):
    base = _std(open, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std open
def omyh_f088_ohlcv_multi_year_highs_std_504d_slope_v105_signal(open, closeadj):
    base = _std(open, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_21d_slope_v106_signal(open, closeadj):
    base = open.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_21d_slope_v107_signal(open, closeadj):
    base = open.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_21d_slope_v108_signal(open, closeadj):
    base = open.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_63d_slope_v109_signal(open, closeadj):
    base = open.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_63d_slope_v110_signal(open, closeadj):
    base = open.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_63d_slope_v111_signal(open, closeadj):
    base = open.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_126d_slope_v112_signal(open, closeadj):
    base = open.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_126d_slope_v113_signal(open, closeadj):
    base = open.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_126d_slope_v114_signal(open, closeadj):
    base = open.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_252d_slope_v115_signal(open, closeadj):
    base = open.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_252d_slope_v116_signal(open, closeadj):
    base = open.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_252d_slope_v117_signal(open, closeadj):
    base = open.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_504d_slope_v118_signal(open, closeadj):
    base = open.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_504d_slope_v119_signal(open, closeadj):
    base = open.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm open
def omyh_f088_ohlcv_multi_year_highs_ewm_504d_slope_v120_signal(open, closeadj):
    base = open.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_21d_slope_v121_signal(open, closeadj):
    base = _mean(open * open, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_21d_slope_v122_signal(open, closeadj):
    base = _mean(open * open, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_21d_slope_v123_signal(open, closeadj):
    base = _mean(open * open, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_63d_slope_v124_signal(open, closeadj):
    base = _mean(open * open, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_63d_slope_v125_signal(open, closeadj):
    base = _mean(open * open, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_63d_slope_v126_signal(open, closeadj):
    base = _mean(open * open, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_126d_slope_v127_signal(open, closeadj):
    base = _mean(open * open, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_126d_slope_v128_signal(open, closeadj):
    base = _mean(open * open, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_126d_slope_v129_signal(open, closeadj):
    base = _mean(open * open, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_252d_slope_v130_signal(open, closeadj):
    base = _mean(open * open, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_252d_slope_v131_signal(open, closeadj):
    base = _mean(open * open, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_252d_slope_v132_signal(open, closeadj):
    base = _mean(open * open, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_504d_slope_v133_signal(open, closeadj):
    base = _mean(open * open, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_504d_slope_v134_signal(open, closeadj):
    base = _mean(open * open, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq open
def omyh_f088_ohlcv_multi_year_highs_sq_504d_slope_v135_signal(open, closeadj):
    base = _mean(open * open, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z open
def omyh_f088_ohlcv_multi_year_highs_z_21d_slope_v136_signal(open):
    base = _z(open, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z open
def omyh_f088_ohlcv_multi_year_highs_z_21d_slope_v137_signal(open):
    base = _z(open, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z open
def omyh_f088_ohlcv_multi_year_highs_z_21d_slope_v138_signal(open):
    base = _z(open, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z open
def omyh_f088_ohlcv_multi_year_highs_z_63d_slope_v139_signal(open):
    base = _z(open, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z open
def omyh_f088_ohlcv_multi_year_highs_z_63d_slope_v140_signal(open):
    base = _z(open, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z open
def omyh_f088_ohlcv_multi_year_highs_z_63d_slope_v141_signal(open):
    base = _z(open, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z open
def omyh_f088_ohlcv_multi_year_highs_z_126d_slope_v142_signal(open):
    base = _z(open, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z open
def omyh_f088_ohlcv_multi_year_highs_z_126d_slope_v143_signal(open):
    base = _z(open, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z open
def omyh_f088_ohlcv_multi_year_highs_z_126d_slope_v144_signal(open):
    base = _z(open, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z open
def omyh_f088_ohlcv_multi_year_highs_z_252d_slope_v145_signal(open):
    base = _z(open, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z open
def omyh_f088_ohlcv_multi_year_highs_z_252d_slope_v146_signal(open):
    base = _z(open, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z open
def omyh_f088_ohlcv_multi_year_highs_z_252d_slope_v147_signal(open):
    base = _z(open, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z open
def omyh_f088_ohlcv_multi_year_highs_z_504d_slope_v148_signal(open):
    base = _z(open, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z open
def omyh_f088_ohlcv_multi_year_highs_z_504d_slope_v149_signal(open):
    base = _z(open, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z open
def omyh_f088_ohlcv_multi_year_highs_z_504d_slope_v150_signal(open):
    base = _z(open, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
