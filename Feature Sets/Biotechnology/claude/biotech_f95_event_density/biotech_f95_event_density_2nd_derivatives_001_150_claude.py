"""Family f95 - SEC 8-K event density & mix  (Q_Actions_Events) | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw eventcount
def ed_f95_event_density_raw_21d_slope_v001_signal(eventcount, closeadj):
    base = _mean(eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw eventcount
def ed_f95_event_density_raw_21d_slope_v002_signal(eventcount, closeadj):
    base = _mean(eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw eventcount
def ed_f95_event_density_raw_21d_slope_v003_signal(eventcount, closeadj):
    base = _mean(eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw eventcount
def ed_f95_event_density_raw_63d_slope_v004_signal(eventcount, closeadj):
    base = _mean(eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw eventcount
def ed_f95_event_density_raw_63d_slope_v005_signal(eventcount, closeadj):
    base = _mean(eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw eventcount
def ed_f95_event_density_raw_63d_slope_v006_signal(eventcount, closeadj):
    base = _mean(eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw eventcount
def ed_f95_event_density_raw_126d_slope_v007_signal(eventcount, closeadj):
    base = _mean(eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw eventcount
def ed_f95_event_density_raw_126d_slope_v008_signal(eventcount, closeadj):
    base = _mean(eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw eventcount
def ed_f95_event_density_raw_126d_slope_v009_signal(eventcount, closeadj):
    base = _mean(eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw eventcount
def ed_f95_event_density_raw_252d_slope_v010_signal(eventcount, closeadj):
    base = _mean(eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw eventcount
def ed_f95_event_density_raw_252d_slope_v011_signal(eventcount, closeadj):
    base = _mean(eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw eventcount
def ed_f95_event_density_raw_252d_slope_v012_signal(eventcount, closeadj):
    base = _mean(eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw eventcount
def ed_f95_event_density_raw_504d_slope_v013_signal(eventcount, closeadj):
    base = _mean(eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw eventcount
def ed_f95_event_density_raw_504d_slope_v014_signal(eventcount, closeadj):
    base = _mean(eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw eventcount
def ed_f95_event_density_raw_504d_slope_v015_signal(eventcount, closeadj):
    base = _mean(eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log eventcount
def ed_f95_event_density_log_21d_slope_v016_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log eventcount
def ed_f95_event_density_log_21d_slope_v017_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log eventcount
def ed_f95_event_density_log_21d_slope_v018_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log eventcount
def ed_f95_event_density_log_63d_slope_v019_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log eventcount
def ed_f95_event_density_log_63d_slope_v020_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log eventcount
def ed_f95_event_density_log_63d_slope_v021_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log eventcount
def ed_f95_event_density_log_126d_slope_v022_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log eventcount
def ed_f95_event_density_log_126d_slope_v023_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log eventcount
def ed_f95_event_density_log_126d_slope_v024_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log eventcount
def ed_f95_event_density_log_252d_slope_v025_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log eventcount
def ed_f95_event_density_log_252d_slope_v026_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log eventcount
def ed_f95_event_density_log_252d_slope_v027_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log eventcount
def ed_f95_event_density_log_504d_slope_v028_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log eventcount
def ed_f95_event_density_log_504d_slope_v029_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log eventcount
def ed_f95_event_density_log_504d_slope_v030_signal(eventcount, closeadj):
    base = _mean(_event_density_log(eventcount), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare eventcount
def ed_f95_event_density_pershare_21d_slope_v031_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare eventcount
def ed_f95_event_density_pershare_21d_slope_v032_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare eventcount
def ed_f95_event_density_pershare_21d_slope_v033_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare eventcount
def ed_f95_event_density_pershare_63d_slope_v034_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare eventcount
def ed_f95_event_density_pershare_63d_slope_v035_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare eventcount
def ed_f95_event_density_pershare_63d_slope_v036_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare eventcount
def ed_f95_event_density_pershare_126d_slope_v037_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare eventcount
def ed_f95_event_density_pershare_126d_slope_v038_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare eventcount
def ed_f95_event_density_pershare_126d_slope_v039_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare eventcount
def ed_f95_event_density_pershare_252d_slope_v040_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare eventcount
def ed_f95_event_density_pershare_252d_slope_v041_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare eventcount
def ed_f95_event_density_pershare_252d_slope_v042_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare eventcount
def ed_f95_event_density_pershare_504d_slope_v043_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare eventcount
def ed_f95_event_density_pershare_504d_slope_v044_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare eventcount
def ed_f95_event_density_pershare_504d_slope_v045_signal(eventcount, sharesbas, closeadj):
    base = _mean(_event_density_per_share(eventcount, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets eventcount
def ed_f95_event_density_per_assets_21d_slope_v046_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets eventcount
def ed_f95_event_density_per_assets_21d_slope_v047_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets eventcount
def ed_f95_event_density_per_assets_21d_slope_v048_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets eventcount
def ed_f95_event_density_per_assets_63d_slope_v049_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets eventcount
def ed_f95_event_density_per_assets_63d_slope_v050_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets eventcount
def ed_f95_event_density_per_assets_63d_slope_v051_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets eventcount
def ed_f95_event_density_per_assets_126d_slope_v052_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets eventcount
def ed_f95_event_density_per_assets_126d_slope_v053_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets eventcount
def ed_f95_event_density_per_assets_126d_slope_v054_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets eventcount
def ed_f95_event_density_per_assets_252d_slope_v055_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets eventcount
def ed_f95_event_density_per_assets_252d_slope_v056_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets eventcount
def ed_f95_event_density_per_assets_252d_slope_v057_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets eventcount
def ed_f95_event_density_per_assets_504d_slope_v058_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets eventcount
def ed_f95_event_density_per_assets_504d_slope_v059_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets eventcount
def ed_f95_event_density_per_assets_504d_slope_v060_signal(eventcount, assets):
    base = _mean(_event_density_scaled(eventcount, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_21d_slope_v061_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_21d_slope_v062_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_21d_slope_v063_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_63d_slope_v064_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_63d_slope_v065_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_63d_slope_v066_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_126d_slope_v067_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_126d_slope_v068_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_126d_slope_v069_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_252d_slope_v070_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_252d_slope_v071_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_252d_slope_v072_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_504d_slope_v073_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_504d_slope_v074_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap eventcount
def ed_f95_event_density_per_marketcap_504d_slope_v075_signal(eventcount, marketcap):
    base = _mean(_event_density_scaled(eventcount, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity eventcount
def ed_f95_event_density_per_equity_21d_slope_v076_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity eventcount
def ed_f95_event_density_per_equity_21d_slope_v077_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity eventcount
def ed_f95_event_density_per_equity_21d_slope_v078_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity eventcount
def ed_f95_event_density_per_equity_63d_slope_v079_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity eventcount
def ed_f95_event_density_per_equity_63d_slope_v080_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity eventcount
def ed_f95_event_density_per_equity_63d_slope_v081_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity eventcount
def ed_f95_event_density_per_equity_126d_slope_v082_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity eventcount
def ed_f95_event_density_per_equity_126d_slope_v083_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity eventcount
def ed_f95_event_density_per_equity_126d_slope_v084_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity eventcount
def ed_f95_event_density_per_equity_252d_slope_v085_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity eventcount
def ed_f95_event_density_per_equity_252d_slope_v086_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity eventcount
def ed_f95_event_density_per_equity_252d_slope_v087_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity eventcount
def ed_f95_event_density_per_equity_504d_slope_v088_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity eventcount
def ed_f95_event_density_per_equity_504d_slope_v089_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity eventcount
def ed_f95_event_density_per_equity_504d_slope_v090_signal(eventcount, equity):
    base = _mean(_event_density_scaled(eventcount, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std eventcount
def ed_f95_event_density_std_21d_slope_v091_signal(eventcount, closeadj):
    base = _std(eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std eventcount
def ed_f95_event_density_std_21d_slope_v092_signal(eventcount, closeadj):
    base = _std(eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std eventcount
def ed_f95_event_density_std_21d_slope_v093_signal(eventcount, closeadj):
    base = _std(eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std eventcount
def ed_f95_event_density_std_63d_slope_v094_signal(eventcount, closeadj):
    base = _std(eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std eventcount
def ed_f95_event_density_std_63d_slope_v095_signal(eventcount, closeadj):
    base = _std(eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std eventcount
def ed_f95_event_density_std_63d_slope_v096_signal(eventcount, closeadj):
    base = _std(eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std eventcount
def ed_f95_event_density_std_126d_slope_v097_signal(eventcount, closeadj):
    base = _std(eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std eventcount
def ed_f95_event_density_std_126d_slope_v098_signal(eventcount, closeadj):
    base = _std(eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std eventcount
def ed_f95_event_density_std_126d_slope_v099_signal(eventcount, closeadj):
    base = _std(eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std eventcount
def ed_f95_event_density_std_252d_slope_v100_signal(eventcount, closeadj):
    base = _std(eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std eventcount
def ed_f95_event_density_std_252d_slope_v101_signal(eventcount, closeadj):
    base = _std(eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std eventcount
def ed_f95_event_density_std_252d_slope_v102_signal(eventcount, closeadj):
    base = _std(eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std eventcount
def ed_f95_event_density_std_504d_slope_v103_signal(eventcount, closeadj):
    base = _std(eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std eventcount
def ed_f95_event_density_std_504d_slope_v104_signal(eventcount, closeadj):
    base = _std(eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std eventcount
def ed_f95_event_density_std_504d_slope_v105_signal(eventcount, closeadj):
    base = _std(eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm eventcount
def ed_f95_event_density_ewm_21d_slope_v106_signal(eventcount, closeadj):
    base = eventcount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm eventcount
def ed_f95_event_density_ewm_21d_slope_v107_signal(eventcount, closeadj):
    base = eventcount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm eventcount
def ed_f95_event_density_ewm_21d_slope_v108_signal(eventcount, closeadj):
    base = eventcount.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm eventcount
def ed_f95_event_density_ewm_63d_slope_v109_signal(eventcount, closeadj):
    base = eventcount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm eventcount
def ed_f95_event_density_ewm_63d_slope_v110_signal(eventcount, closeadj):
    base = eventcount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm eventcount
def ed_f95_event_density_ewm_63d_slope_v111_signal(eventcount, closeadj):
    base = eventcount.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm eventcount
def ed_f95_event_density_ewm_126d_slope_v112_signal(eventcount, closeadj):
    base = eventcount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm eventcount
def ed_f95_event_density_ewm_126d_slope_v113_signal(eventcount, closeadj):
    base = eventcount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm eventcount
def ed_f95_event_density_ewm_126d_slope_v114_signal(eventcount, closeadj):
    base = eventcount.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm eventcount
def ed_f95_event_density_ewm_252d_slope_v115_signal(eventcount, closeadj):
    base = eventcount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm eventcount
def ed_f95_event_density_ewm_252d_slope_v116_signal(eventcount, closeadj):
    base = eventcount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm eventcount
def ed_f95_event_density_ewm_252d_slope_v117_signal(eventcount, closeadj):
    base = eventcount.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm eventcount
def ed_f95_event_density_ewm_504d_slope_v118_signal(eventcount, closeadj):
    base = eventcount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm eventcount
def ed_f95_event_density_ewm_504d_slope_v119_signal(eventcount, closeadj):
    base = eventcount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm eventcount
def ed_f95_event_density_ewm_504d_slope_v120_signal(eventcount, closeadj):
    base = eventcount.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq eventcount
def ed_f95_event_density_sq_21d_slope_v121_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq eventcount
def ed_f95_event_density_sq_21d_slope_v122_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq eventcount
def ed_f95_event_density_sq_21d_slope_v123_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq eventcount
def ed_f95_event_density_sq_63d_slope_v124_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq eventcount
def ed_f95_event_density_sq_63d_slope_v125_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq eventcount
def ed_f95_event_density_sq_63d_slope_v126_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq eventcount
def ed_f95_event_density_sq_126d_slope_v127_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq eventcount
def ed_f95_event_density_sq_126d_slope_v128_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq eventcount
def ed_f95_event_density_sq_126d_slope_v129_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq eventcount
def ed_f95_event_density_sq_252d_slope_v130_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq eventcount
def ed_f95_event_density_sq_252d_slope_v131_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq eventcount
def ed_f95_event_density_sq_252d_slope_v132_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq eventcount
def ed_f95_event_density_sq_504d_slope_v133_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq eventcount
def ed_f95_event_density_sq_504d_slope_v134_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq eventcount
def ed_f95_event_density_sq_504d_slope_v135_signal(eventcount, closeadj):
    base = _mean(eventcount * eventcount, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z eventcount
def ed_f95_event_density_z_21d_slope_v136_signal(eventcount):
    base = _z(eventcount, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z eventcount
def ed_f95_event_density_z_21d_slope_v137_signal(eventcount):
    base = _z(eventcount, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z eventcount
def ed_f95_event_density_z_21d_slope_v138_signal(eventcount):
    base = _z(eventcount, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z eventcount
def ed_f95_event_density_z_63d_slope_v139_signal(eventcount):
    base = _z(eventcount, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z eventcount
def ed_f95_event_density_z_63d_slope_v140_signal(eventcount):
    base = _z(eventcount, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z eventcount
def ed_f95_event_density_z_63d_slope_v141_signal(eventcount):
    base = _z(eventcount, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z eventcount
def ed_f95_event_density_z_126d_slope_v142_signal(eventcount):
    base = _z(eventcount, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z eventcount
def ed_f95_event_density_z_126d_slope_v143_signal(eventcount):
    base = _z(eventcount, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z eventcount
def ed_f95_event_density_z_126d_slope_v144_signal(eventcount):
    base = _z(eventcount, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z eventcount
def ed_f95_event_density_z_252d_slope_v145_signal(eventcount):
    base = _z(eventcount, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z eventcount
def ed_f95_event_density_z_252d_slope_v146_signal(eventcount):
    base = _z(eventcount, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z eventcount
def ed_f95_event_density_z_252d_slope_v147_signal(eventcount):
    base = _z(eventcount, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z eventcount
def ed_f95_event_density_z_504d_slope_v148_signal(eventcount):
    base = _z(eventcount, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z eventcount
def ed_f95_event_density_z_504d_slope_v149_signal(eventcount):
    base = _z(eventcount, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z eventcount
def ed_f95_event_density_z_504d_slope_v150_signal(eventcount):
    base = _z(eventcount, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
