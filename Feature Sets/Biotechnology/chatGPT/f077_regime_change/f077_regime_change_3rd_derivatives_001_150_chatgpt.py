"""Family f077 - Fundamental regime changes (Fundamental Dynamics) | Sharadar tables: SF1 | fields: revenue, rnd, ncfo, opex, cashneq | 3rd derivatives 001-150"""
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
def _regime_change_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _regime_change_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _regime_change_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw revenue
def rc_f077_regime_change_raw_21d_accel_v001_signal(revenue, closeadj):
    base = _mean(revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw revenue
def rc_f077_regime_change_raw_21d_accel_v002_signal(revenue, closeadj):
    base = _mean(revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw revenue
def rc_f077_regime_change_raw_21d_accel_v003_signal(revenue, closeadj):
    base = _mean(revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw revenue
def rc_f077_regime_change_raw_63d_accel_v004_signal(revenue, closeadj):
    base = _mean(revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw revenue
def rc_f077_regime_change_raw_63d_accel_v005_signal(revenue, closeadj):
    base = _mean(revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw revenue
def rc_f077_regime_change_raw_63d_accel_v006_signal(revenue, closeadj):
    base = _mean(revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw revenue
def rc_f077_regime_change_raw_126d_accel_v007_signal(revenue, closeadj):
    base = _mean(revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw revenue
def rc_f077_regime_change_raw_126d_accel_v008_signal(revenue, closeadj):
    base = _mean(revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw revenue
def rc_f077_regime_change_raw_126d_accel_v009_signal(revenue, closeadj):
    base = _mean(revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw revenue
def rc_f077_regime_change_raw_252d_accel_v010_signal(revenue, closeadj):
    base = _mean(revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw revenue
def rc_f077_regime_change_raw_252d_accel_v011_signal(revenue, closeadj):
    base = _mean(revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw revenue
def rc_f077_regime_change_raw_252d_accel_v012_signal(revenue, closeadj):
    base = _mean(revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw revenue
def rc_f077_regime_change_raw_504d_accel_v013_signal(revenue, closeadj):
    base = _mean(revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw revenue
def rc_f077_regime_change_raw_504d_accel_v014_signal(revenue, closeadj):
    base = _mean(revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw revenue
def rc_f077_regime_change_raw_504d_accel_v015_signal(revenue, closeadj):
    base = _mean(revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log revenue
def rc_f077_regime_change_log_21d_accel_v016_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log revenue
def rc_f077_regime_change_log_21d_accel_v017_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log revenue
def rc_f077_regime_change_log_21d_accel_v018_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log revenue
def rc_f077_regime_change_log_63d_accel_v019_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log revenue
def rc_f077_regime_change_log_63d_accel_v020_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log revenue
def rc_f077_regime_change_log_63d_accel_v021_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log revenue
def rc_f077_regime_change_log_126d_accel_v022_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log revenue
def rc_f077_regime_change_log_126d_accel_v023_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log revenue
def rc_f077_regime_change_log_126d_accel_v024_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log revenue
def rc_f077_regime_change_log_252d_accel_v025_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log revenue
def rc_f077_regime_change_log_252d_accel_v026_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log revenue
def rc_f077_regime_change_log_252d_accel_v027_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log revenue
def rc_f077_regime_change_log_504d_accel_v028_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log revenue
def rc_f077_regime_change_log_504d_accel_v029_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log revenue
def rc_f077_regime_change_log_504d_accel_v030_signal(revenue, closeadj):
    base = _mean(_regime_change_log(revenue), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare revenue
def rc_f077_regime_change_pershare_21d_accel_v031_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare revenue
def rc_f077_regime_change_pershare_21d_accel_v032_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare revenue
def rc_f077_regime_change_pershare_21d_accel_v033_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare revenue
def rc_f077_regime_change_pershare_63d_accel_v034_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare revenue
def rc_f077_regime_change_pershare_63d_accel_v035_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare revenue
def rc_f077_regime_change_pershare_63d_accel_v036_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare revenue
def rc_f077_regime_change_pershare_126d_accel_v037_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare revenue
def rc_f077_regime_change_pershare_126d_accel_v038_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare revenue
def rc_f077_regime_change_pershare_126d_accel_v039_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare revenue
def rc_f077_regime_change_pershare_252d_accel_v040_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare revenue
def rc_f077_regime_change_pershare_252d_accel_v041_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare revenue
def rc_f077_regime_change_pershare_252d_accel_v042_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare revenue
def rc_f077_regime_change_pershare_504d_accel_v043_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare revenue
def rc_f077_regime_change_pershare_504d_accel_v044_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare revenue
def rc_f077_regime_change_pershare_504d_accel_v045_signal(revenue, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(revenue, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_rnd revenue
def rc_f077_regime_change_per_rnd_21d_accel_v046_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_rnd revenue
def rc_f077_regime_change_per_rnd_21d_accel_v047_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_rnd revenue
def rc_f077_regime_change_per_rnd_21d_accel_v048_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_rnd revenue
def rc_f077_regime_change_per_rnd_63d_accel_v049_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_rnd revenue
def rc_f077_regime_change_per_rnd_63d_accel_v050_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_rnd revenue
def rc_f077_regime_change_per_rnd_63d_accel_v051_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_rnd revenue
def rc_f077_regime_change_per_rnd_126d_accel_v052_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_rnd revenue
def rc_f077_regime_change_per_rnd_126d_accel_v053_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_rnd revenue
def rc_f077_regime_change_per_rnd_126d_accel_v054_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_rnd revenue
def rc_f077_regime_change_per_rnd_252d_accel_v055_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_rnd revenue
def rc_f077_regime_change_per_rnd_252d_accel_v056_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_rnd revenue
def rc_f077_regime_change_per_rnd_252d_accel_v057_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_rnd revenue
def rc_f077_regime_change_per_rnd_504d_accel_v058_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_rnd revenue
def rc_f077_regime_change_per_rnd_504d_accel_v059_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_rnd revenue
def rc_f077_regime_change_per_rnd_504d_accel_v060_signal(revenue, rnd):
    base = _mean(_regime_change_scaled(revenue, rnd), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_21d_accel_v061_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_21d_accel_v062_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_21d_accel_v063_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_63d_accel_v064_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_63d_accel_v065_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_63d_accel_v066_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_126d_accel_v067_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_126d_accel_v068_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_126d_accel_v069_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_252d_accel_v070_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_252d_accel_v071_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_252d_accel_v072_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_504d_accel_v073_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_504d_accel_v074_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_ncfo revenue
def rc_f077_regime_change_per_ncfo_504d_accel_v075_signal(revenue, ncfo):
    base = _mean(_regime_change_scaled(revenue, ncfo), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_21d_accel_v076_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_21d_accel_v077_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_21d_accel_v078_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_63d_accel_v079_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_63d_accel_v080_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_63d_accel_v081_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_126d_accel_v082_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_126d_accel_v083_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_126d_accel_v084_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_252d_accel_v085_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_252d_accel_v086_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_252d_accel_v087_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_504d_accel_v088_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_504d_accel_v089_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_cashneq revenue
def rc_f077_regime_change_per_cashneq_504d_accel_v090_signal(revenue, cashneq):
    base = _mean(_regime_change_scaled(revenue, cashneq), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std revenue
def rc_f077_regime_change_std_21d_accel_v091_signal(revenue, closeadj):
    base = _std(revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std revenue
def rc_f077_regime_change_std_21d_accel_v092_signal(revenue, closeadj):
    base = _std(revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std revenue
def rc_f077_regime_change_std_21d_accel_v093_signal(revenue, closeadj):
    base = _std(revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std revenue
def rc_f077_regime_change_std_63d_accel_v094_signal(revenue, closeadj):
    base = _std(revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std revenue
def rc_f077_regime_change_std_63d_accel_v095_signal(revenue, closeadj):
    base = _std(revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std revenue
def rc_f077_regime_change_std_63d_accel_v096_signal(revenue, closeadj):
    base = _std(revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std revenue
def rc_f077_regime_change_std_126d_accel_v097_signal(revenue, closeadj):
    base = _std(revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std revenue
def rc_f077_regime_change_std_126d_accel_v098_signal(revenue, closeadj):
    base = _std(revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std revenue
def rc_f077_regime_change_std_126d_accel_v099_signal(revenue, closeadj):
    base = _std(revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std revenue
def rc_f077_regime_change_std_252d_accel_v100_signal(revenue, closeadj):
    base = _std(revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std revenue
def rc_f077_regime_change_std_252d_accel_v101_signal(revenue, closeadj):
    base = _std(revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std revenue
def rc_f077_regime_change_std_252d_accel_v102_signal(revenue, closeadj):
    base = _std(revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std revenue
def rc_f077_regime_change_std_504d_accel_v103_signal(revenue, closeadj):
    base = _std(revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std revenue
def rc_f077_regime_change_std_504d_accel_v104_signal(revenue, closeadj):
    base = _std(revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std revenue
def rc_f077_regime_change_std_504d_accel_v105_signal(revenue, closeadj):
    base = _std(revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm revenue
def rc_f077_regime_change_ewm_21d_accel_v106_signal(revenue, closeadj):
    base = revenue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm revenue
def rc_f077_regime_change_ewm_21d_accel_v107_signal(revenue, closeadj):
    base = revenue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm revenue
def rc_f077_regime_change_ewm_21d_accel_v108_signal(revenue, closeadj):
    base = revenue.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm revenue
def rc_f077_regime_change_ewm_63d_accel_v109_signal(revenue, closeadj):
    base = revenue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm revenue
def rc_f077_regime_change_ewm_63d_accel_v110_signal(revenue, closeadj):
    base = revenue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm revenue
def rc_f077_regime_change_ewm_63d_accel_v111_signal(revenue, closeadj):
    base = revenue.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm revenue
def rc_f077_regime_change_ewm_126d_accel_v112_signal(revenue, closeadj):
    base = revenue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm revenue
def rc_f077_regime_change_ewm_126d_accel_v113_signal(revenue, closeadj):
    base = revenue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm revenue
def rc_f077_regime_change_ewm_126d_accel_v114_signal(revenue, closeadj):
    base = revenue.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm revenue
def rc_f077_regime_change_ewm_252d_accel_v115_signal(revenue, closeadj):
    base = revenue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm revenue
def rc_f077_regime_change_ewm_252d_accel_v116_signal(revenue, closeadj):
    base = revenue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm revenue
def rc_f077_regime_change_ewm_252d_accel_v117_signal(revenue, closeadj):
    base = revenue.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm revenue
def rc_f077_regime_change_ewm_504d_accel_v118_signal(revenue, closeadj):
    base = revenue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm revenue
def rc_f077_regime_change_ewm_504d_accel_v119_signal(revenue, closeadj):
    base = revenue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm revenue
def rc_f077_regime_change_ewm_504d_accel_v120_signal(revenue, closeadj):
    base = revenue.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq revenue
def rc_f077_regime_change_sq_21d_accel_v121_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq revenue
def rc_f077_regime_change_sq_21d_accel_v122_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq revenue
def rc_f077_regime_change_sq_21d_accel_v123_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq revenue
def rc_f077_regime_change_sq_63d_accel_v124_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq revenue
def rc_f077_regime_change_sq_63d_accel_v125_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq revenue
def rc_f077_regime_change_sq_63d_accel_v126_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq revenue
def rc_f077_regime_change_sq_126d_accel_v127_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq revenue
def rc_f077_regime_change_sq_126d_accel_v128_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq revenue
def rc_f077_regime_change_sq_126d_accel_v129_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq revenue
def rc_f077_regime_change_sq_252d_accel_v130_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq revenue
def rc_f077_regime_change_sq_252d_accel_v131_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq revenue
def rc_f077_regime_change_sq_252d_accel_v132_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq revenue
def rc_f077_regime_change_sq_504d_accel_v133_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq revenue
def rc_f077_regime_change_sq_504d_accel_v134_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq revenue
def rc_f077_regime_change_sq_504d_accel_v135_signal(revenue, closeadj):
    base = _mean(revenue * revenue, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z revenue
def rc_f077_regime_change_z_21d_accel_v136_signal(revenue):
    base = _z(revenue, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z revenue
def rc_f077_regime_change_z_21d_accel_v137_signal(revenue):
    base = _z(revenue, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z revenue
def rc_f077_regime_change_z_21d_accel_v138_signal(revenue):
    base = _z(revenue, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z revenue
def rc_f077_regime_change_z_63d_accel_v139_signal(revenue):
    base = _z(revenue, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z revenue
def rc_f077_regime_change_z_63d_accel_v140_signal(revenue):
    base = _z(revenue, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z revenue
def rc_f077_regime_change_z_63d_accel_v141_signal(revenue):
    base = _z(revenue, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z revenue
def rc_f077_regime_change_z_126d_accel_v142_signal(revenue):
    base = _z(revenue, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z revenue
def rc_f077_regime_change_z_126d_accel_v143_signal(revenue):
    base = _z(revenue, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z revenue
def rc_f077_regime_change_z_126d_accel_v144_signal(revenue):
    base = _z(revenue, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z revenue
def rc_f077_regime_change_z_252d_accel_v145_signal(revenue):
    base = _z(revenue, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z revenue
def rc_f077_regime_change_z_252d_accel_v146_signal(revenue):
    base = _z(revenue, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z revenue
def rc_f077_regime_change_z_252d_accel_v147_signal(revenue):
    base = _z(revenue, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z revenue
def rc_f077_regime_change_z_504d_accel_v148_signal(revenue):
    base = _z(revenue, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z revenue
def rc_f077_regime_change_z_504d_accel_v149_signal(revenue):
    base = _z(revenue, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z revenue
def rc_f077_regime_change_z_504d_accel_v150_signal(revenue):
    base = _z(revenue, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
