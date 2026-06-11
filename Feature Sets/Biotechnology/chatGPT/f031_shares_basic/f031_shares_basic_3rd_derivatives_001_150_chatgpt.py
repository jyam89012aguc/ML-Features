"""Family f031 - Basic share count expansion (Dilution and Share Count) | Sharadar tables: SF1 | fields: sharesbas, sharefactor | 3rd derivatives 001-150"""
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
def _shares_basic_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _shares_basic_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _shares_basic_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw sharesbas
def sb_f031_shares_basic_raw_21d_accel_v001_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw sharesbas
def sb_f031_shares_basic_raw_21d_accel_v002_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw sharesbas
def sb_f031_shares_basic_raw_21d_accel_v003_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw sharesbas
def sb_f031_shares_basic_raw_63d_accel_v004_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw sharesbas
def sb_f031_shares_basic_raw_63d_accel_v005_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw sharesbas
def sb_f031_shares_basic_raw_63d_accel_v006_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw sharesbas
def sb_f031_shares_basic_raw_126d_accel_v007_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw sharesbas
def sb_f031_shares_basic_raw_126d_accel_v008_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw sharesbas
def sb_f031_shares_basic_raw_126d_accel_v009_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw sharesbas
def sb_f031_shares_basic_raw_252d_accel_v010_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw sharesbas
def sb_f031_shares_basic_raw_252d_accel_v011_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw sharesbas
def sb_f031_shares_basic_raw_252d_accel_v012_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw sharesbas
def sb_f031_shares_basic_raw_504d_accel_v013_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw sharesbas
def sb_f031_shares_basic_raw_504d_accel_v014_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw sharesbas
def sb_f031_shares_basic_raw_504d_accel_v015_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log sharesbas
def sb_f031_shares_basic_log_21d_accel_v016_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log sharesbas
def sb_f031_shares_basic_log_21d_accel_v017_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log sharesbas
def sb_f031_shares_basic_log_21d_accel_v018_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log sharesbas
def sb_f031_shares_basic_log_63d_accel_v019_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log sharesbas
def sb_f031_shares_basic_log_63d_accel_v020_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log sharesbas
def sb_f031_shares_basic_log_63d_accel_v021_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log sharesbas
def sb_f031_shares_basic_log_126d_accel_v022_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log sharesbas
def sb_f031_shares_basic_log_126d_accel_v023_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log sharesbas
def sb_f031_shares_basic_log_126d_accel_v024_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log sharesbas
def sb_f031_shares_basic_log_252d_accel_v025_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log sharesbas
def sb_f031_shares_basic_log_252d_accel_v026_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log sharesbas
def sb_f031_shares_basic_log_252d_accel_v027_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log sharesbas
def sb_f031_shares_basic_log_504d_accel_v028_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log sharesbas
def sb_f031_shares_basic_log_504d_accel_v029_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log sharesbas
def sb_f031_shares_basic_log_504d_accel_v030_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_log(sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare sharesbas
def sb_f031_shares_basic_pershare_21d_accel_v031_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare sharesbas
def sb_f031_shares_basic_pershare_21d_accel_v032_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare sharesbas
def sb_f031_shares_basic_pershare_21d_accel_v033_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare sharesbas
def sb_f031_shares_basic_pershare_63d_accel_v034_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare sharesbas
def sb_f031_shares_basic_pershare_63d_accel_v035_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare sharesbas
def sb_f031_shares_basic_pershare_63d_accel_v036_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare sharesbas
def sb_f031_shares_basic_pershare_126d_accel_v037_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare sharesbas
def sb_f031_shares_basic_pershare_126d_accel_v038_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare sharesbas
def sb_f031_shares_basic_pershare_126d_accel_v039_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare sharesbas
def sb_f031_shares_basic_pershare_252d_accel_v040_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare sharesbas
def sb_f031_shares_basic_pershare_252d_accel_v041_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare sharesbas
def sb_f031_shares_basic_pershare_252d_accel_v042_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare sharesbas
def sb_f031_shares_basic_pershare_504d_accel_v043_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare sharesbas
def sb_f031_shares_basic_pershare_504d_accel_v044_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare sharesbas
def sb_f031_shares_basic_pershare_504d_accel_v045_signal(sharesbas, closeadj):
    base = _mean(_shares_basic_per_share(sharesbas, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_21d_accel_v046_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_21d_accel_v047_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_21d_accel_v048_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_63d_accel_v049_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_63d_accel_v050_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_63d_accel_v051_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_126d_accel_v052_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_126d_accel_v053_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_126d_accel_v054_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_252d_accel_v055_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_252d_accel_v056_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_252d_accel_v057_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_504d_accel_v058_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_504d_accel_v059_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_sharefactor sharesbas
def sb_f031_shares_basic_per_sharefactor_504d_accel_v060_signal(sharesbas, sharefactor):
    base = _mean(_shares_basic_scaled(sharesbas, sharefactor), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets sharesbas
def sb_f031_shares_basic_per_assets_21d_accel_v061_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets sharesbas
def sb_f031_shares_basic_per_assets_21d_accel_v062_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets sharesbas
def sb_f031_shares_basic_per_assets_21d_accel_v063_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets sharesbas
def sb_f031_shares_basic_per_assets_63d_accel_v064_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets sharesbas
def sb_f031_shares_basic_per_assets_63d_accel_v065_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets sharesbas
def sb_f031_shares_basic_per_assets_63d_accel_v066_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets sharesbas
def sb_f031_shares_basic_per_assets_126d_accel_v067_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets sharesbas
def sb_f031_shares_basic_per_assets_126d_accel_v068_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets sharesbas
def sb_f031_shares_basic_per_assets_126d_accel_v069_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets sharesbas
def sb_f031_shares_basic_per_assets_252d_accel_v070_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets sharesbas
def sb_f031_shares_basic_per_assets_252d_accel_v071_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets sharesbas
def sb_f031_shares_basic_per_assets_252d_accel_v072_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets sharesbas
def sb_f031_shares_basic_per_assets_504d_accel_v073_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets sharesbas
def sb_f031_shares_basic_per_assets_504d_accel_v074_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets sharesbas
def sb_f031_shares_basic_per_assets_504d_accel_v075_signal(sharesbas, assets):
    base = _mean(_shares_basic_scaled(sharesbas, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_21d_accel_v076_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_21d_accel_v077_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_21d_accel_v078_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_63d_accel_v079_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_63d_accel_v080_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_63d_accel_v081_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_126d_accel_v082_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_126d_accel_v083_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_126d_accel_v084_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_252d_accel_v085_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_252d_accel_v086_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_252d_accel_v087_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_504d_accel_v088_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_504d_accel_v089_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap sharesbas
def sb_f031_shares_basic_per_marketcap_504d_accel_v090_signal(sharesbas, marketcap):
    base = _mean(_shares_basic_scaled(sharesbas, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std sharesbas
def sb_f031_shares_basic_std_21d_accel_v091_signal(sharesbas, closeadj):
    base = _std(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std sharesbas
def sb_f031_shares_basic_std_21d_accel_v092_signal(sharesbas, closeadj):
    base = _std(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std sharesbas
def sb_f031_shares_basic_std_21d_accel_v093_signal(sharesbas, closeadj):
    base = _std(sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std sharesbas
def sb_f031_shares_basic_std_63d_accel_v094_signal(sharesbas, closeadj):
    base = _std(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std sharesbas
def sb_f031_shares_basic_std_63d_accel_v095_signal(sharesbas, closeadj):
    base = _std(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std sharesbas
def sb_f031_shares_basic_std_63d_accel_v096_signal(sharesbas, closeadj):
    base = _std(sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std sharesbas
def sb_f031_shares_basic_std_126d_accel_v097_signal(sharesbas, closeadj):
    base = _std(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std sharesbas
def sb_f031_shares_basic_std_126d_accel_v098_signal(sharesbas, closeadj):
    base = _std(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std sharesbas
def sb_f031_shares_basic_std_126d_accel_v099_signal(sharesbas, closeadj):
    base = _std(sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std sharesbas
def sb_f031_shares_basic_std_252d_accel_v100_signal(sharesbas, closeadj):
    base = _std(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std sharesbas
def sb_f031_shares_basic_std_252d_accel_v101_signal(sharesbas, closeadj):
    base = _std(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std sharesbas
def sb_f031_shares_basic_std_252d_accel_v102_signal(sharesbas, closeadj):
    base = _std(sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std sharesbas
def sb_f031_shares_basic_std_504d_accel_v103_signal(sharesbas, closeadj):
    base = _std(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std sharesbas
def sb_f031_shares_basic_std_504d_accel_v104_signal(sharesbas, closeadj):
    base = _std(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std sharesbas
def sb_f031_shares_basic_std_504d_accel_v105_signal(sharesbas, closeadj):
    base = _std(sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm sharesbas
def sb_f031_shares_basic_ewm_21d_accel_v106_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm sharesbas
def sb_f031_shares_basic_ewm_21d_accel_v107_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm sharesbas
def sb_f031_shares_basic_ewm_21d_accel_v108_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm sharesbas
def sb_f031_shares_basic_ewm_63d_accel_v109_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm sharesbas
def sb_f031_shares_basic_ewm_63d_accel_v110_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm sharesbas
def sb_f031_shares_basic_ewm_63d_accel_v111_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm sharesbas
def sb_f031_shares_basic_ewm_126d_accel_v112_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm sharesbas
def sb_f031_shares_basic_ewm_126d_accel_v113_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm sharesbas
def sb_f031_shares_basic_ewm_126d_accel_v114_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm sharesbas
def sb_f031_shares_basic_ewm_252d_accel_v115_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm sharesbas
def sb_f031_shares_basic_ewm_252d_accel_v116_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm sharesbas
def sb_f031_shares_basic_ewm_252d_accel_v117_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm sharesbas
def sb_f031_shares_basic_ewm_504d_accel_v118_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm sharesbas
def sb_f031_shares_basic_ewm_504d_accel_v119_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm sharesbas
def sb_f031_shares_basic_ewm_504d_accel_v120_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq sharesbas
def sb_f031_shares_basic_sq_21d_accel_v121_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq sharesbas
def sb_f031_shares_basic_sq_21d_accel_v122_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq sharesbas
def sb_f031_shares_basic_sq_21d_accel_v123_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq sharesbas
def sb_f031_shares_basic_sq_63d_accel_v124_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq sharesbas
def sb_f031_shares_basic_sq_63d_accel_v125_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq sharesbas
def sb_f031_shares_basic_sq_63d_accel_v126_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq sharesbas
def sb_f031_shares_basic_sq_126d_accel_v127_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq sharesbas
def sb_f031_shares_basic_sq_126d_accel_v128_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq sharesbas
def sb_f031_shares_basic_sq_126d_accel_v129_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq sharesbas
def sb_f031_shares_basic_sq_252d_accel_v130_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq sharesbas
def sb_f031_shares_basic_sq_252d_accel_v131_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq sharesbas
def sb_f031_shares_basic_sq_252d_accel_v132_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq sharesbas
def sb_f031_shares_basic_sq_504d_accel_v133_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq sharesbas
def sb_f031_shares_basic_sq_504d_accel_v134_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq sharesbas
def sb_f031_shares_basic_sq_504d_accel_v135_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z sharesbas
def sb_f031_shares_basic_z_21d_accel_v136_signal(sharesbas):
    base = _z(sharesbas, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z sharesbas
def sb_f031_shares_basic_z_21d_accel_v137_signal(sharesbas):
    base = _z(sharesbas, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z sharesbas
def sb_f031_shares_basic_z_21d_accel_v138_signal(sharesbas):
    base = _z(sharesbas, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z sharesbas
def sb_f031_shares_basic_z_63d_accel_v139_signal(sharesbas):
    base = _z(sharesbas, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z sharesbas
def sb_f031_shares_basic_z_63d_accel_v140_signal(sharesbas):
    base = _z(sharesbas, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z sharesbas
def sb_f031_shares_basic_z_63d_accel_v141_signal(sharesbas):
    base = _z(sharesbas, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z sharesbas
def sb_f031_shares_basic_z_126d_accel_v142_signal(sharesbas):
    base = _z(sharesbas, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z sharesbas
def sb_f031_shares_basic_z_126d_accel_v143_signal(sharesbas):
    base = _z(sharesbas, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z sharesbas
def sb_f031_shares_basic_z_126d_accel_v144_signal(sharesbas):
    base = _z(sharesbas, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z sharesbas
def sb_f031_shares_basic_z_252d_accel_v145_signal(sharesbas):
    base = _z(sharesbas, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z sharesbas
def sb_f031_shares_basic_z_252d_accel_v146_signal(sharesbas):
    base = _z(sharesbas, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z sharesbas
def sb_f031_shares_basic_z_252d_accel_v147_signal(sharesbas):
    base = _z(sharesbas, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z sharesbas
def sb_f031_shares_basic_z_504d_accel_v148_signal(sharesbas):
    base = _z(sharesbas, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z sharesbas
def sb_f031_shares_basic_z_504d_accel_v149_signal(sharesbas):
    base = _z(sharesbas, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z sharesbas
def sb_f031_shares_basic_z_504d_accel_v150_signal(sharesbas):
    base = _z(sharesbas, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
