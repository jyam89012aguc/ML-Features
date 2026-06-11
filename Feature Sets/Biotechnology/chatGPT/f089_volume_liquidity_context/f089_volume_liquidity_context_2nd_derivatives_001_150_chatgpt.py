"""Family f089 - Volume and dollar liquidity context (Market Context from Sharadar Prices) | Sharadar tables: SEP,SFP | fields: volume, close, closeadj, sharesbas | 2nd derivatives 001-150"""
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
def _volume_liquidity_context_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _volume_liquidity_context_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _volume_liquidity_context_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw volume
def vlc_f089_volume_liquidity_context_raw_21d_slope_v001_signal(volume, closeadj):
    base = _mean(volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw volume
def vlc_f089_volume_liquidity_context_raw_21d_slope_v002_signal(volume, closeadj):
    base = _mean(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw volume
def vlc_f089_volume_liquidity_context_raw_21d_slope_v003_signal(volume, closeadj):
    base = _mean(volume, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw volume
def vlc_f089_volume_liquidity_context_raw_63d_slope_v004_signal(volume, closeadj):
    base = _mean(volume, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw volume
def vlc_f089_volume_liquidity_context_raw_63d_slope_v005_signal(volume, closeadj):
    base = _mean(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw volume
def vlc_f089_volume_liquidity_context_raw_63d_slope_v006_signal(volume, closeadj):
    base = _mean(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw volume
def vlc_f089_volume_liquidity_context_raw_126d_slope_v007_signal(volume, closeadj):
    base = _mean(volume, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw volume
def vlc_f089_volume_liquidity_context_raw_126d_slope_v008_signal(volume, closeadj):
    base = _mean(volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw volume
def vlc_f089_volume_liquidity_context_raw_126d_slope_v009_signal(volume, closeadj):
    base = _mean(volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw volume
def vlc_f089_volume_liquidity_context_raw_252d_slope_v010_signal(volume, closeadj):
    base = _mean(volume, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw volume
def vlc_f089_volume_liquidity_context_raw_252d_slope_v011_signal(volume, closeadj):
    base = _mean(volume, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw volume
def vlc_f089_volume_liquidity_context_raw_252d_slope_v012_signal(volume, closeadj):
    base = _mean(volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw volume
def vlc_f089_volume_liquidity_context_raw_504d_slope_v013_signal(volume, closeadj):
    base = _mean(volume, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw volume
def vlc_f089_volume_liquidity_context_raw_504d_slope_v014_signal(volume, closeadj):
    base = _mean(volume, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw volume
def vlc_f089_volume_liquidity_context_raw_504d_slope_v015_signal(volume, closeadj):
    base = _mean(volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log volume
def vlc_f089_volume_liquidity_context_log_21d_slope_v016_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log volume
def vlc_f089_volume_liquidity_context_log_21d_slope_v017_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log volume
def vlc_f089_volume_liquidity_context_log_21d_slope_v018_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log volume
def vlc_f089_volume_liquidity_context_log_63d_slope_v019_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log volume
def vlc_f089_volume_liquidity_context_log_63d_slope_v020_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log volume
def vlc_f089_volume_liquidity_context_log_63d_slope_v021_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log volume
def vlc_f089_volume_liquidity_context_log_126d_slope_v022_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log volume
def vlc_f089_volume_liquidity_context_log_126d_slope_v023_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log volume
def vlc_f089_volume_liquidity_context_log_126d_slope_v024_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log volume
def vlc_f089_volume_liquidity_context_log_252d_slope_v025_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log volume
def vlc_f089_volume_liquidity_context_log_252d_slope_v026_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log volume
def vlc_f089_volume_liquidity_context_log_252d_slope_v027_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log volume
def vlc_f089_volume_liquidity_context_log_504d_slope_v028_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log volume
def vlc_f089_volume_liquidity_context_log_504d_slope_v029_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log volume
def vlc_f089_volume_liquidity_context_log_504d_slope_v030_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_log(volume), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare volume
def vlc_f089_volume_liquidity_context_pershare_21d_slope_v031_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare volume
def vlc_f089_volume_liquidity_context_pershare_21d_slope_v032_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare volume
def vlc_f089_volume_liquidity_context_pershare_21d_slope_v033_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare volume
def vlc_f089_volume_liquidity_context_pershare_63d_slope_v034_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare volume
def vlc_f089_volume_liquidity_context_pershare_63d_slope_v035_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare volume
def vlc_f089_volume_liquidity_context_pershare_63d_slope_v036_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare volume
def vlc_f089_volume_liquidity_context_pershare_126d_slope_v037_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare volume
def vlc_f089_volume_liquidity_context_pershare_126d_slope_v038_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare volume
def vlc_f089_volume_liquidity_context_pershare_126d_slope_v039_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare volume
def vlc_f089_volume_liquidity_context_pershare_252d_slope_v040_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare volume
def vlc_f089_volume_liquidity_context_pershare_252d_slope_v041_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare volume
def vlc_f089_volume_liquidity_context_pershare_252d_slope_v042_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare volume
def vlc_f089_volume_liquidity_context_pershare_504d_slope_v043_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare volume
def vlc_f089_volume_liquidity_context_pershare_504d_slope_v044_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare volume
def vlc_f089_volume_liquidity_context_pershare_504d_slope_v045_signal(volume, sharesbas, closeadj):
    base = _mean(_volume_liquidity_context_per_share(volume, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_close volume
def vlc_f089_volume_liquidity_context_per_close_21d_slope_v046_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_close volume
def vlc_f089_volume_liquidity_context_per_close_21d_slope_v047_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_close volume
def vlc_f089_volume_liquidity_context_per_close_21d_slope_v048_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_close volume
def vlc_f089_volume_liquidity_context_per_close_63d_slope_v049_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_close volume
def vlc_f089_volume_liquidity_context_per_close_63d_slope_v050_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_close volume
def vlc_f089_volume_liquidity_context_per_close_63d_slope_v051_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_close volume
def vlc_f089_volume_liquidity_context_per_close_126d_slope_v052_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_close volume
def vlc_f089_volume_liquidity_context_per_close_126d_slope_v053_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_close volume
def vlc_f089_volume_liquidity_context_per_close_126d_slope_v054_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_close volume
def vlc_f089_volume_liquidity_context_per_close_252d_slope_v055_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_close volume
def vlc_f089_volume_liquidity_context_per_close_252d_slope_v056_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_close volume
def vlc_f089_volume_liquidity_context_per_close_252d_slope_v057_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_close volume
def vlc_f089_volume_liquidity_context_per_close_504d_slope_v058_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_close volume
def vlc_f089_volume_liquidity_context_per_close_504d_slope_v059_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_close volume
def vlc_f089_volume_liquidity_context_per_close_504d_slope_v060_signal(volume, close):
    base = _mean(_volume_liquidity_context_scaled(volume, close), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_21d_slope_v061_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_21d_slope_v062_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_21d_slope_v063_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_63d_slope_v064_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_63d_slope_v065_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_63d_slope_v066_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_126d_slope_v067_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_126d_slope_v068_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_126d_slope_v069_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_252d_slope_v070_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_252d_slope_v071_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_252d_slope_v072_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_504d_slope_v073_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_504d_slope_v074_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_closeadj volume
def vlc_f089_volume_liquidity_context_per_closeadj_504d_slope_v075_signal(volume, closeadj):
    base = _mean(_volume_liquidity_context_scaled(volume, closeadj), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_21d_slope_v076_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_21d_slope_v077_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_21d_slope_v078_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_63d_slope_v079_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_63d_slope_v080_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_63d_slope_v081_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_126d_slope_v082_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_126d_slope_v083_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_126d_slope_v084_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_252d_slope_v085_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_252d_slope_v086_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_252d_slope_v087_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_504d_slope_v088_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_504d_slope_v089_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_sharesbas volume
def vlc_f089_volume_liquidity_context_per_sharesbas_504d_slope_v090_signal(volume, sharesbas):
    base = _mean(_volume_liquidity_context_scaled(volume, sharesbas), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std volume
def vlc_f089_volume_liquidity_context_std_21d_slope_v091_signal(volume, closeadj):
    base = _std(volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std volume
def vlc_f089_volume_liquidity_context_std_21d_slope_v092_signal(volume, closeadj):
    base = _std(volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std volume
def vlc_f089_volume_liquidity_context_std_21d_slope_v093_signal(volume, closeadj):
    base = _std(volume, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std volume
def vlc_f089_volume_liquidity_context_std_63d_slope_v094_signal(volume, closeadj):
    base = _std(volume, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std volume
def vlc_f089_volume_liquidity_context_std_63d_slope_v095_signal(volume, closeadj):
    base = _std(volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std volume
def vlc_f089_volume_liquidity_context_std_63d_slope_v096_signal(volume, closeadj):
    base = _std(volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std volume
def vlc_f089_volume_liquidity_context_std_126d_slope_v097_signal(volume, closeadj):
    base = _std(volume, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std volume
def vlc_f089_volume_liquidity_context_std_126d_slope_v098_signal(volume, closeadj):
    base = _std(volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std volume
def vlc_f089_volume_liquidity_context_std_126d_slope_v099_signal(volume, closeadj):
    base = _std(volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std volume
def vlc_f089_volume_liquidity_context_std_252d_slope_v100_signal(volume, closeadj):
    base = _std(volume, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std volume
def vlc_f089_volume_liquidity_context_std_252d_slope_v101_signal(volume, closeadj):
    base = _std(volume, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std volume
def vlc_f089_volume_liquidity_context_std_252d_slope_v102_signal(volume, closeadj):
    base = _std(volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std volume
def vlc_f089_volume_liquidity_context_std_504d_slope_v103_signal(volume, closeadj):
    base = _std(volume, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std volume
def vlc_f089_volume_liquidity_context_std_504d_slope_v104_signal(volume, closeadj):
    base = _std(volume, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std volume
def vlc_f089_volume_liquidity_context_std_504d_slope_v105_signal(volume, closeadj):
    base = _std(volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm volume
def vlc_f089_volume_liquidity_context_ewm_21d_slope_v106_signal(volume, closeadj):
    base = volume.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm volume
def vlc_f089_volume_liquidity_context_ewm_21d_slope_v107_signal(volume, closeadj):
    base = volume.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm volume
def vlc_f089_volume_liquidity_context_ewm_21d_slope_v108_signal(volume, closeadj):
    base = volume.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm volume
def vlc_f089_volume_liquidity_context_ewm_63d_slope_v109_signal(volume, closeadj):
    base = volume.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm volume
def vlc_f089_volume_liquidity_context_ewm_63d_slope_v110_signal(volume, closeadj):
    base = volume.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm volume
def vlc_f089_volume_liquidity_context_ewm_63d_slope_v111_signal(volume, closeadj):
    base = volume.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm volume
def vlc_f089_volume_liquidity_context_ewm_126d_slope_v112_signal(volume, closeadj):
    base = volume.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm volume
def vlc_f089_volume_liquidity_context_ewm_126d_slope_v113_signal(volume, closeadj):
    base = volume.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm volume
def vlc_f089_volume_liquidity_context_ewm_126d_slope_v114_signal(volume, closeadj):
    base = volume.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm volume
def vlc_f089_volume_liquidity_context_ewm_252d_slope_v115_signal(volume, closeadj):
    base = volume.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm volume
def vlc_f089_volume_liquidity_context_ewm_252d_slope_v116_signal(volume, closeadj):
    base = volume.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm volume
def vlc_f089_volume_liquidity_context_ewm_252d_slope_v117_signal(volume, closeadj):
    base = volume.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm volume
def vlc_f089_volume_liquidity_context_ewm_504d_slope_v118_signal(volume, closeadj):
    base = volume.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm volume
def vlc_f089_volume_liquidity_context_ewm_504d_slope_v119_signal(volume, closeadj):
    base = volume.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm volume
def vlc_f089_volume_liquidity_context_ewm_504d_slope_v120_signal(volume, closeadj):
    base = volume.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq volume
def vlc_f089_volume_liquidity_context_sq_21d_slope_v121_signal(volume, closeadj):
    base = _mean(volume * volume, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq volume
def vlc_f089_volume_liquidity_context_sq_21d_slope_v122_signal(volume, closeadj):
    base = _mean(volume * volume, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq volume
def vlc_f089_volume_liquidity_context_sq_21d_slope_v123_signal(volume, closeadj):
    base = _mean(volume * volume, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq volume
def vlc_f089_volume_liquidity_context_sq_63d_slope_v124_signal(volume, closeadj):
    base = _mean(volume * volume, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq volume
def vlc_f089_volume_liquidity_context_sq_63d_slope_v125_signal(volume, closeadj):
    base = _mean(volume * volume, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq volume
def vlc_f089_volume_liquidity_context_sq_63d_slope_v126_signal(volume, closeadj):
    base = _mean(volume * volume, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq volume
def vlc_f089_volume_liquidity_context_sq_126d_slope_v127_signal(volume, closeadj):
    base = _mean(volume * volume, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq volume
def vlc_f089_volume_liquidity_context_sq_126d_slope_v128_signal(volume, closeadj):
    base = _mean(volume * volume, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq volume
def vlc_f089_volume_liquidity_context_sq_126d_slope_v129_signal(volume, closeadj):
    base = _mean(volume * volume, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq volume
def vlc_f089_volume_liquidity_context_sq_252d_slope_v130_signal(volume, closeadj):
    base = _mean(volume * volume, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq volume
def vlc_f089_volume_liquidity_context_sq_252d_slope_v131_signal(volume, closeadj):
    base = _mean(volume * volume, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq volume
def vlc_f089_volume_liquidity_context_sq_252d_slope_v132_signal(volume, closeadj):
    base = _mean(volume * volume, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq volume
def vlc_f089_volume_liquidity_context_sq_504d_slope_v133_signal(volume, closeadj):
    base = _mean(volume * volume, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq volume
def vlc_f089_volume_liquidity_context_sq_504d_slope_v134_signal(volume, closeadj):
    base = _mean(volume * volume, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq volume
def vlc_f089_volume_liquidity_context_sq_504d_slope_v135_signal(volume, closeadj):
    base = _mean(volume * volume, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z volume
def vlc_f089_volume_liquidity_context_z_21d_slope_v136_signal(volume):
    base = _z(volume, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z volume
def vlc_f089_volume_liquidity_context_z_21d_slope_v137_signal(volume):
    base = _z(volume, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z volume
def vlc_f089_volume_liquidity_context_z_21d_slope_v138_signal(volume):
    base = _z(volume, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z volume
def vlc_f089_volume_liquidity_context_z_63d_slope_v139_signal(volume):
    base = _z(volume, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z volume
def vlc_f089_volume_liquidity_context_z_63d_slope_v140_signal(volume):
    base = _z(volume, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z volume
def vlc_f089_volume_liquidity_context_z_63d_slope_v141_signal(volume):
    base = _z(volume, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z volume
def vlc_f089_volume_liquidity_context_z_126d_slope_v142_signal(volume):
    base = _z(volume, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z volume
def vlc_f089_volume_liquidity_context_z_126d_slope_v143_signal(volume):
    base = _z(volume, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z volume
def vlc_f089_volume_liquidity_context_z_126d_slope_v144_signal(volume):
    base = _z(volume, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z volume
def vlc_f089_volume_liquidity_context_z_252d_slope_v145_signal(volume):
    base = _z(volume, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z volume
def vlc_f089_volume_liquidity_context_z_252d_slope_v146_signal(volume):
    base = _z(volume, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z volume
def vlc_f089_volume_liquidity_context_z_252d_slope_v147_signal(volume):
    base = _z(volume, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z volume
def vlc_f089_volume_liquidity_context_z_504d_slope_v148_signal(volume):
    base = _z(volume, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z volume
def vlc_f089_volume_liquidity_context_z_504d_slope_v149_signal(volume):
    base = _z(volume, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z volume
def vlc_f089_volume_liquidity_context_z_504d_slope_v150_signal(volume):
    base = _z(volume, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
