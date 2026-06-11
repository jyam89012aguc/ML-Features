"""Family f95 - SEC 8-K event density & mix  (Q_Actions_Events) | 3rd derivatives 001-150"""
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
def _event_density_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _event_density_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _event_density_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw eventcount
def ed_f95_event_density_raw_21d_accel_v001_signal(eventcount, closeadj):
    base = _mean(eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw eventcount
def ed_f95_event_density_raw_21d_accel_v002_signal(eventcount, closeadj):
    base = _mean(eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw eventcount
def ed_f95_event_density_raw_21d_accel_v003_signal(eventcount, closeadj):
    base = _mean(eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw eventcount
def ed_f95_event_density_raw_63d_accel_v004_signal(eventcount, closeadj):
    base = _mean(eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw eventcount
def ed_f95_event_density_raw_63d_accel_v005_signal(eventcount, closeadj):
    base = _mean(eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw eventcount
def ed_f95_event_density_raw_63d_accel_v006_signal(eventcount, closeadj):
    base = _mean(eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw eventcount
def ed_f95_event_density_raw_126d_accel_v007_signal(eventcount, closeadj):
    base = _mean(eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw eventcount
def ed_f95_event_density_raw_126d_accel_v008_signal(eventcount, closeadj):
    base = _mean(eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw eventcount
def ed_f95_event_density_raw_126d_accel_v009_signal(eventcount, closeadj):
    base = _mean(eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw eventcount
def ed_f95_event_density_raw_252d_accel_v010_signal(eventcount, closeadj):
    base = _mean(eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw eventcount
def ed_f95_event_density_raw_252d_accel_v011_signal(eventcount, closeadj):
    base = _mean(eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw eventcount
def ed_f95_event_density_raw_252d_accel_v012_signal(eventcount, closeadj):
    base = _mean(eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw eventcount
def ed_f95_event_density_raw_504d_accel_v013_signal(eventcount, closeadj):
    base = _mean(eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw eventcount
def ed_f95_event_density_raw_504d_accel_v014_signal(eventcount, closeadj):
    base = _mean(eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw eventcount
def ed_f95_event_density_raw_504d_accel_v015_signal(eventcount, closeadj):
    base = _mean(eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log eventcount
def ed_f95_event_density_log_21d_accel_v016_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log eventcount
def ed_f95_event_density_log_21d_accel_v017_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log eventcount
def ed_f95_event_density_log_21d_accel_v018_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log eventcount
def ed_f95_event_density_log_63d_accel_v019_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log eventcount
def ed_f95_event_density_log_63d_accel_v020_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log eventcount
def ed_f95_event_density_log_63d_accel_v021_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log eventcount
def ed_f95_event_density_log_126d_accel_v022_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log eventcount
def ed_f95_event_density_log_126d_accel_v023_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log eventcount
def ed_f95_event_density_log_126d_accel_v024_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log eventcount
def ed_f95_event_density_log_252d_accel_v025_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log eventcount
def ed_f95_event_density_log_252d_accel_v026_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log eventcount
def ed_f95_event_density_log_252d_accel_v027_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log eventcount
def ed_f95_event_density_log_504d_accel_v028_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log eventcount
def ed_f95_event_density_log_504d_accel_v029_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log eventcount
def ed_f95_event_density_log_504d_accel_v030_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare eventcount
def ed_f95_event_density_pershare_21d_accel_v031_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare eventcount
def ed_f95_event_density_pershare_21d_accel_v032_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare eventcount
def ed_f95_event_density_pershare_21d_accel_v033_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare eventcount
def ed_f95_event_density_pershare_63d_accel_v034_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare eventcount
def ed_f95_event_density_pershare_63d_accel_v035_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare eventcount
def ed_f95_event_density_pershare_63d_accel_v036_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare eventcount
def ed_f95_event_density_pershare_126d_accel_v037_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare eventcount
def ed_f95_event_density_pershare_126d_accel_v038_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare eventcount
def ed_f95_event_density_pershare_126d_accel_v039_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare eventcount
def ed_f95_event_density_pershare_252d_accel_v040_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare eventcount
def ed_f95_event_density_pershare_252d_accel_v041_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare eventcount
def ed_f95_event_density_pershare_252d_accel_v042_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare eventcount
def ed_f95_event_density_pershare_504d_accel_v043_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare eventcount
def ed_f95_event_density_pershare_504d_accel_v044_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare eventcount
def ed_f95_event_density_pershare_504d_accel_v045_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets eventcount
def ed_f95_event_density_per_assets_21d_accel_v046_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets eventcount
def ed_f95_event_density_per_assets_21d_accel_v047_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets eventcount
def ed_f95_event_density_per_assets_21d_accel_v048_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets eventcount
def ed_f95_event_density_per_assets_63d_accel_v049_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets eventcount
def ed_f95_event_density_per_assets_63d_accel_v050_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets eventcount
def ed_f95_event_density_per_assets_63d_accel_v051_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets eventcount
def ed_f95_event_density_per_assets_126d_accel_v052_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets eventcount
def ed_f95_event_density_per_assets_126d_accel_v053_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets eventcount
def ed_f95_event_density_per_assets_126d_accel_v054_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets eventcount
def ed_f95_event_density_per_assets_252d_accel_v055_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets eventcount
def ed_f95_event_density_per_assets_252d_accel_v056_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets eventcount
def ed_f95_event_density_per_assets_252d_accel_v057_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets eventcount
def ed_f95_event_density_per_assets_504d_accel_v058_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets eventcount
def ed_f95_event_density_per_assets_504d_accel_v059_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets eventcount
def ed_f95_event_density_per_assets_504d_accel_v060_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_21d_accel_v061_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_21d_accel_v062_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_21d_accel_v063_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_63d_accel_v064_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_63d_accel_v065_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_63d_accel_v066_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_126d_accel_v067_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_126d_accel_v068_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_126d_accel_v069_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_252d_accel_v070_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_252d_accel_v071_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_252d_accel_v072_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_504d_accel_v073_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_504d_accel_v074_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_504d_accel_v075_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity eventcount
def ed_f95_event_density_per_equity_21d_accel_v076_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity eventcount
def ed_f95_event_density_per_equity_21d_accel_v077_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity eventcount
def ed_f95_event_density_per_equity_21d_accel_v078_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity eventcount
def ed_f95_event_density_per_equity_63d_accel_v079_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity eventcount
def ed_f95_event_density_per_equity_63d_accel_v080_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity eventcount
def ed_f95_event_density_per_equity_63d_accel_v081_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity eventcount
def ed_f95_event_density_per_equity_126d_accel_v082_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity eventcount
def ed_f95_event_density_per_equity_126d_accel_v083_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity eventcount
def ed_f95_event_density_per_equity_126d_accel_v084_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity eventcount
def ed_f95_event_density_per_equity_252d_accel_v085_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity eventcount
def ed_f95_event_density_per_equity_252d_accel_v086_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity eventcount
def ed_f95_event_density_per_equity_252d_accel_v087_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity eventcount
def ed_f95_event_density_per_equity_504d_accel_v088_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity eventcount
def ed_f95_event_density_per_equity_504d_accel_v089_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity eventcount
def ed_f95_event_density_per_equity_504d_accel_v090_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std eventcount
def ed_f95_event_density_std_21d_accel_v091_signal(eventcount, closeadj):
    base = _std(eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std eventcount
def ed_f95_event_density_std_21d_accel_v092_signal(eventcount, closeadj):
    base = _std(eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std eventcount
def ed_f95_event_density_std_21d_accel_v093_signal(eventcount, closeadj):
    base = _std(eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std eventcount
def ed_f95_event_density_std_63d_accel_v094_signal(eventcount, closeadj):
    base = _std(eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std eventcount
def ed_f95_event_density_std_63d_accel_v095_signal(eventcount, closeadj):
    base = _std(eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std eventcount
def ed_f95_event_density_std_63d_accel_v096_signal(eventcount, closeadj):
    base = _std(eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std eventcount
def ed_f95_event_density_std_126d_accel_v097_signal(eventcount, closeadj):
    base = _std(eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std eventcount
def ed_f95_event_density_std_126d_accel_v098_signal(eventcount, closeadj):
    base = _std(eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std eventcount
def ed_f95_event_density_std_126d_accel_v099_signal(eventcount, closeadj):
    base = _std(eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std eventcount
def ed_f95_event_density_std_252d_accel_v100_signal(eventcount, closeadj):
    base = _std(eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std eventcount
def ed_f95_event_density_std_252d_accel_v101_signal(eventcount, closeadj):
    base = _std(eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std eventcount
def ed_f95_event_density_std_252d_accel_v102_signal(eventcount, closeadj):
    base = _std(eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std eventcount
def ed_f95_event_density_std_504d_accel_v103_signal(eventcount, closeadj):
    base = _std(eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std eventcount
def ed_f95_event_density_std_504d_accel_v104_signal(eventcount, closeadj):
    base = _std(eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std eventcount
def ed_f95_event_density_std_504d_accel_v105_signal(eventcount, closeadj):
    base = _std(eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm eventcount
def ed_f95_event_density_ewm_21d_accel_v106_signal(eventcount, closeadj):
    base = eventcount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm eventcount
def ed_f95_event_density_ewm_21d_accel_v107_signal(eventcount, closeadj):
    base = eventcount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm eventcount
def ed_f95_event_density_ewm_21d_accel_v108_signal(eventcount, closeadj):
    base = eventcount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm eventcount
def ed_f95_event_density_ewm_63d_accel_v109_signal(eventcount, closeadj):
    base = eventcount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm eventcount
def ed_f95_event_density_ewm_63d_accel_v110_signal(eventcount, closeadj):
    base = eventcount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm eventcount
def ed_f95_event_density_ewm_63d_accel_v111_signal(eventcount, closeadj):
    base = eventcount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm eventcount
def ed_f95_event_density_ewm_126d_accel_v112_signal(eventcount, closeadj):
    base = eventcount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm eventcount
def ed_f95_event_density_ewm_126d_accel_v113_signal(eventcount, closeadj):
    base = eventcount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm eventcount
def ed_f95_event_density_ewm_126d_accel_v114_signal(eventcount, closeadj):
    base = eventcount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm eventcount
def ed_f95_event_density_ewm_252d_accel_v115_signal(eventcount, closeadj):
    base = eventcount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm eventcount
def ed_f95_event_density_ewm_252d_accel_v116_signal(eventcount, closeadj):
    base = eventcount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm eventcount
def ed_f95_event_density_ewm_252d_accel_v117_signal(eventcount, closeadj):
    base = eventcount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm eventcount
def ed_f95_event_density_ewm_504d_accel_v118_signal(eventcount, closeadj):
    base = eventcount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm eventcount
def ed_f95_event_density_ewm_504d_accel_v119_signal(eventcount, closeadj):
    base = eventcount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm eventcount
def ed_f95_event_density_ewm_504d_accel_v120_signal(eventcount, closeadj):
    base = eventcount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq eventcount
def ed_f95_event_density_sq_21d_accel_v121_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq eventcount
def ed_f95_event_density_sq_21d_accel_v122_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq eventcount
def ed_f95_event_density_sq_21d_accel_v123_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq eventcount
def ed_f95_event_density_sq_63d_accel_v124_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq eventcount
def ed_f95_event_density_sq_63d_accel_v125_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq eventcount
def ed_f95_event_density_sq_63d_accel_v126_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq eventcount
def ed_f95_event_density_sq_126d_accel_v127_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq eventcount
def ed_f95_event_density_sq_126d_accel_v128_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq eventcount
def ed_f95_event_density_sq_126d_accel_v129_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq eventcount
def ed_f95_event_density_sq_252d_accel_v130_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq eventcount
def ed_f95_event_density_sq_252d_accel_v131_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq eventcount
def ed_f95_event_density_sq_252d_accel_v132_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq eventcount
def ed_f95_event_density_sq_504d_accel_v133_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq eventcount
def ed_f95_event_density_sq_504d_accel_v134_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq eventcount
def ed_f95_event_density_sq_504d_accel_v135_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z eventcount
def ed_f95_event_density_z_21d_accel_v136_signal(eventcount):
    base = _z(eventcount, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z eventcount
def ed_f95_event_density_z_21d_accel_v137_signal(eventcount):
    base = _z(eventcount, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z eventcount
def ed_f95_event_density_z_21d_accel_v138_signal(eventcount):
    base = _z(eventcount, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z eventcount
def ed_f95_event_density_z_63d_accel_v139_signal(eventcount):
    base = _z(eventcount, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z eventcount
def ed_f95_event_density_z_63d_accel_v140_signal(eventcount):
    base = _z(eventcount, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z eventcount
def ed_f95_event_density_z_63d_accel_v141_signal(eventcount):
    base = _z(eventcount, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z eventcount
def ed_f95_event_density_z_126d_accel_v142_signal(eventcount):
    base = _z(eventcount, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z eventcount
def ed_f95_event_density_z_126d_accel_v143_signal(eventcount):
    base = _z(eventcount, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z eventcount
def ed_f95_event_density_z_126d_accel_v144_signal(eventcount):
    base = _z(eventcount, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z eventcount
def ed_f95_event_density_z_252d_accel_v145_signal(eventcount):
    base = _z(eventcount, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z eventcount
def ed_f95_event_density_z_252d_accel_v146_signal(eventcount):
    base = _z(eventcount, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z eventcount
def ed_f95_event_density_z_252d_accel_v147_signal(eventcount):
    base = _z(eventcount, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z eventcount
def ed_f95_event_density_z_504d_accel_v148_signal(eventcount):
    base = _z(eventcount, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z eventcount
def ed_f95_event_density_z_504d_accel_v149_signal(eventcount):
    base = _z(eventcount, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z eventcount
def ed_f95_event_density_z_504d_accel_v150_signal(eventcount):
    base = _z(eventcount, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
