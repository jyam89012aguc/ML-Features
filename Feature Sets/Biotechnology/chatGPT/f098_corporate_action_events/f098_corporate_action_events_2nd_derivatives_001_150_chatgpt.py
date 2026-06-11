"""Family f098 - Corporate actions density and type (Corporate Actions and Events) | Sharadar tables: ACTIONS,SF1,SEP | fields: value, sharesbas, assets, equity, debt | 2nd derivatives 001-150"""
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
def _corporate_action_events_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _corporate_action_events_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _corporate_action_events_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw value
def cae_f098_corporate_action_events_raw_21d_slope_v001_signal(value, closeadj):
    base = _mean(value, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw value
def cae_f098_corporate_action_events_raw_21d_slope_v002_signal(value, closeadj):
    base = _mean(value, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw value
def cae_f098_corporate_action_events_raw_21d_slope_v003_signal(value, closeadj):
    base = _mean(value, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw value
def cae_f098_corporate_action_events_raw_63d_slope_v004_signal(value, closeadj):
    base = _mean(value, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw value
def cae_f098_corporate_action_events_raw_63d_slope_v005_signal(value, closeadj):
    base = _mean(value, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw value
def cae_f098_corporate_action_events_raw_63d_slope_v006_signal(value, closeadj):
    base = _mean(value, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw value
def cae_f098_corporate_action_events_raw_126d_slope_v007_signal(value, closeadj):
    base = _mean(value, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw value
def cae_f098_corporate_action_events_raw_126d_slope_v008_signal(value, closeadj):
    base = _mean(value, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw value
def cae_f098_corporate_action_events_raw_126d_slope_v009_signal(value, closeadj):
    base = _mean(value, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw value
def cae_f098_corporate_action_events_raw_252d_slope_v010_signal(value, closeadj):
    base = _mean(value, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw value
def cae_f098_corporate_action_events_raw_252d_slope_v011_signal(value, closeadj):
    base = _mean(value, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw value
def cae_f098_corporate_action_events_raw_252d_slope_v012_signal(value, closeadj):
    base = _mean(value, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw value
def cae_f098_corporate_action_events_raw_504d_slope_v013_signal(value, closeadj):
    base = _mean(value, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw value
def cae_f098_corporate_action_events_raw_504d_slope_v014_signal(value, closeadj):
    base = _mean(value, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw value
def cae_f098_corporate_action_events_raw_504d_slope_v015_signal(value, closeadj):
    base = _mean(value, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log value
def cae_f098_corporate_action_events_log_21d_slope_v016_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log value
def cae_f098_corporate_action_events_log_21d_slope_v017_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log value
def cae_f098_corporate_action_events_log_21d_slope_v018_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log value
def cae_f098_corporate_action_events_log_63d_slope_v019_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log value
def cae_f098_corporate_action_events_log_63d_slope_v020_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log value
def cae_f098_corporate_action_events_log_63d_slope_v021_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log value
def cae_f098_corporate_action_events_log_126d_slope_v022_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log value
def cae_f098_corporate_action_events_log_126d_slope_v023_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log value
def cae_f098_corporate_action_events_log_126d_slope_v024_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log value
def cae_f098_corporate_action_events_log_252d_slope_v025_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log value
def cae_f098_corporate_action_events_log_252d_slope_v026_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log value
def cae_f098_corporate_action_events_log_252d_slope_v027_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log value
def cae_f098_corporate_action_events_log_504d_slope_v028_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log value
def cae_f098_corporate_action_events_log_504d_slope_v029_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log value
def cae_f098_corporate_action_events_log_504d_slope_v030_signal(value, closeadj):
    base = _mean(_corporate_action_events_log(value), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare value
def cae_f098_corporate_action_events_pershare_21d_slope_v031_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare value
def cae_f098_corporate_action_events_pershare_21d_slope_v032_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare value
def cae_f098_corporate_action_events_pershare_21d_slope_v033_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare value
def cae_f098_corporate_action_events_pershare_63d_slope_v034_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare value
def cae_f098_corporate_action_events_pershare_63d_slope_v035_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare value
def cae_f098_corporate_action_events_pershare_63d_slope_v036_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare value
def cae_f098_corporate_action_events_pershare_126d_slope_v037_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare value
def cae_f098_corporate_action_events_pershare_126d_slope_v038_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare value
def cae_f098_corporate_action_events_pershare_126d_slope_v039_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare value
def cae_f098_corporate_action_events_pershare_252d_slope_v040_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare value
def cae_f098_corporate_action_events_pershare_252d_slope_v041_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare value
def cae_f098_corporate_action_events_pershare_252d_slope_v042_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare value
def cae_f098_corporate_action_events_pershare_504d_slope_v043_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare value
def cae_f098_corporate_action_events_pershare_504d_slope_v044_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare value
def cae_f098_corporate_action_events_pershare_504d_slope_v045_signal(value, sharesbas, closeadj):
    base = _mean(_corporate_action_events_per_share(value, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_21d_slope_v046_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_21d_slope_v047_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_21d_slope_v048_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_63d_slope_v049_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_63d_slope_v050_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_63d_slope_v051_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_126d_slope_v052_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_126d_slope_v053_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_126d_slope_v054_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_252d_slope_v055_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_252d_slope_v056_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_252d_slope_v057_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_504d_slope_v058_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_504d_slope_v059_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_504d_slope_v060_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets value
def cae_f098_corporate_action_events_per_assets_21d_slope_v061_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets value
def cae_f098_corporate_action_events_per_assets_21d_slope_v062_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets value
def cae_f098_corporate_action_events_per_assets_21d_slope_v063_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets value
def cae_f098_corporate_action_events_per_assets_63d_slope_v064_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets value
def cae_f098_corporate_action_events_per_assets_63d_slope_v065_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets value
def cae_f098_corporate_action_events_per_assets_63d_slope_v066_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets value
def cae_f098_corporate_action_events_per_assets_126d_slope_v067_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets value
def cae_f098_corporate_action_events_per_assets_126d_slope_v068_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets value
def cae_f098_corporate_action_events_per_assets_126d_slope_v069_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets value
def cae_f098_corporate_action_events_per_assets_252d_slope_v070_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets value
def cae_f098_corporate_action_events_per_assets_252d_slope_v071_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets value
def cae_f098_corporate_action_events_per_assets_252d_slope_v072_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets value
def cae_f098_corporate_action_events_per_assets_504d_slope_v073_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets value
def cae_f098_corporate_action_events_per_assets_504d_slope_v074_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets value
def cae_f098_corporate_action_events_per_assets_504d_slope_v075_signal(value, assets):
    base = _mean(_corporate_action_events_scaled(value, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_21d_slope_v076_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_21d_slope_v077_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_21d_slope_v078_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_63d_slope_v079_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_63d_slope_v080_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_63d_slope_v081_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_126d_slope_v082_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_126d_slope_v083_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_126d_slope_v084_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_252d_slope_v085_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_252d_slope_v086_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_252d_slope_v087_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_504d_slope_v088_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_504d_slope_v089_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_sharesbas value
def cae_f098_corporate_action_events_per_sharesbas_504d_slope_v090_signal(value, sharesbas):
    base = _mean(_corporate_action_events_scaled(value, sharesbas), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std value
def cae_f098_corporate_action_events_std_21d_slope_v091_signal(value, closeadj):
    base = _std(value, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std value
def cae_f098_corporate_action_events_std_21d_slope_v092_signal(value, closeadj):
    base = _std(value, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std value
def cae_f098_corporate_action_events_std_21d_slope_v093_signal(value, closeadj):
    base = _std(value, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std value
def cae_f098_corporate_action_events_std_63d_slope_v094_signal(value, closeadj):
    base = _std(value, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std value
def cae_f098_corporate_action_events_std_63d_slope_v095_signal(value, closeadj):
    base = _std(value, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std value
def cae_f098_corporate_action_events_std_63d_slope_v096_signal(value, closeadj):
    base = _std(value, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std value
def cae_f098_corporate_action_events_std_126d_slope_v097_signal(value, closeadj):
    base = _std(value, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std value
def cae_f098_corporate_action_events_std_126d_slope_v098_signal(value, closeadj):
    base = _std(value, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std value
def cae_f098_corporate_action_events_std_126d_slope_v099_signal(value, closeadj):
    base = _std(value, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std value
def cae_f098_corporate_action_events_std_252d_slope_v100_signal(value, closeadj):
    base = _std(value, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std value
def cae_f098_corporate_action_events_std_252d_slope_v101_signal(value, closeadj):
    base = _std(value, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std value
def cae_f098_corporate_action_events_std_252d_slope_v102_signal(value, closeadj):
    base = _std(value, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std value
def cae_f098_corporate_action_events_std_504d_slope_v103_signal(value, closeadj):
    base = _std(value, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std value
def cae_f098_corporate_action_events_std_504d_slope_v104_signal(value, closeadj):
    base = _std(value, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std value
def cae_f098_corporate_action_events_std_504d_slope_v105_signal(value, closeadj):
    base = _std(value, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm value
def cae_f098_corporate_action_events_ewm_21d_slope_v106_signal(value, closeadj):
    base = value.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm value
def cae_f098_corporate_action_events_ewm_21d_slope_v107_signal(value, closeadj):
    base = value.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm value
def cae_f098_corporate_action_events_ewm_21d_slope_v108_signal(value, closeadj):
    base = value.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm value
def cae_f098_corporate_action_events_ewm_63d_slope_v109_signal(value, closeadj):
    base = value.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm value
def cae_f098_corporate_action_events_ewm_63d_slope_v110_signal(value, closeadj):
    base = value.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm value
def cae_f098_corporate_action_events_ewm_63d_slope_v111_signal(value, closeadj):
    base = value.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm value
def cae_f098_corporate_action_events_ewm_126d_slope_v112_signal(value, closeadj):
    base = value.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm value
def cae_f098_corporate_action_events_ewm_126d_slope_v113_signal(value, closeadj):
    base = value.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm value
def cae_f098_corporate_action_events_ewm_126d_slope_v114_signal(value, closeadj):
    base = value.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm value
def cae_f098_corporate_action_events_ewm_252d_slope_v115_signal(value, closeadj):
    base = value.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm value
def cae_f098_corporate_action_events_ewm_252d_slope_v116_signal(value, closeadj):
    base = value.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm value
def cae_f098_corporate_action_events_ewm_252d_slope_v117_signal(value, closeadj):
    base = value.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm value
def cae_f098_corporate_action_events_ewm_504d_slope_v118_signal(value, closeadj):
    base = value.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm value
def cae_f098_corporate_action_events_ewm_504d_slope_v119_signal(value, closeadj):
    base = value.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm value
def cae_f098_corporate_action_events_ewm_504d_slope_v120_signal(value, closeadj):
    base = value.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq value
def cae_f098_corporate_action_events_sq_21d_slope_v121_signal(value, closeadj):
    base = _mean(value * value, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq value
def cae_f098_corporate_action_events_sq_21d_slope_v122_signal(value, closeadj):
    base = _mean(value * value, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq value
def cae_f098_corporate_action_events_sq_21d_slope_v123_signal(value, closeadj):
    base = _mean(value * value, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq value
def cae_f098_corporate_action_events_sq_63d_slope_v124_signal(value, closeadj):
    base = _mean(value * value, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq value
def cae_f098_corporate_action_events_sq_63d_slope_v125_signal(value, closeadj):
    base = _mean(value * value, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq value
def cae_f098_corporate_action_events_sq_63d_slope_v126_signal(value, closeadj):
    base = _mean(value * value, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq value
def cae_f098_corporate_action_events_sq_126d_slope_v127_signal(value, closeadj):
    base = _mean(value * value, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq value
def cae_f098_corporate_action_events_sq_126d_slope_v128_signal(value, closeadj):
    base = _mean(value * value, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq value
def cae_f098_corporate_action_events_sq_126d_slope_v129_signal(value, closeadj):
    base = _mean(value * value, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq value
def cae_f098_corporate_action_events_sq_252d_slope_v130_signal(value, closeadj):
    base = _mean(value * value, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq value
def cae_f098_corporate_action_events_sq_252d_slope_v131_signal(value, closeadj):
    base = _mean(value * value, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq value
def cae_f098_corporate_action_events_sq_252d_slope_v132_signal(value, closeadj):
    base = _mean(value * value, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq value
def cae_f098_corporate_action_events_sq_504d_slope_v133_signal(value, closeadj):
    base = _mean(value * value, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq value
def cae_f098_corporate_action_events_sq_504d_slope_v134_signal(value, closeadj):
    base = _mean(value * value, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq value
def cae_f098_corporate_action_events_sq_504d_slope_v135_signal(value, closeadj):
    base = _mean(value * value, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z value
def cae_f098_corporate_action_events_z_21d_slope_v136_signal(value):
    base = _z(value, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z value
def cae_f098_corporate_action_events_z_21d_slope_v137_signal(value):
    base = _z(value, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z value
def cae_f098_corporate_action_events_z_21d_slope_v138_signal(value):
    base = _z(value, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z value
def cae_f098_corporate_action_events_z_63d_slope_v139_signal(value):
    base = _z(value, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z value
def cae_f098_corporate_action_events_z_63d_slope_v140_signal(value):
    base = _z(value, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z value
def cae_f098_corporate_action_events_z_63d_slope_v141_signal(value):
    base = _z(value, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z value
def cae_f098_corporate_action_events_z_126d_slope_v142_signal(value):
    base = _z(value, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z value
def cae_f098_corporate_action_events_z_126d_slope_v143_signal(value):
    base = _z(value, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z value
def cae_f098_corporate_action_events_z_126d_slope_v144_signal(value):
    base = _z(value, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z value
def cae_f098_corporate_action_events_z_252d_slope_v145_signal(value):
    base = _z(value, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z value
def cae_f098_corporate_action_events_z_252d_slope_v146_signal(value):
    base = _z(value, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z value
def cae_f098_corporate_action_events_z_252d_slope_v147_signal(value):
    base = _z(value, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z value
def cae_f098_corporate_action_events_z_504d_slope_v148_signal(value):
    base = _z(value, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z value
def cae_f098_corporate_action_events_z_504d_slope_v149_signal(value):
    base = _z(value, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z value
def cae_f098_corporate_action_events_z_504d_slope_v150_signal(value):
    base = _z(value, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
