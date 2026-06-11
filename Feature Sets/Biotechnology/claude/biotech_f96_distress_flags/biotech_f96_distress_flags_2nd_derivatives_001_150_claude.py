"""Family f96 - Distress & structural flags  (Q_Actions_Events) | 2nd derivatives 001-150"""
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
def _distress_flags_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _distress_flags_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _distress_flags_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw distressflag
def df_f96_distress_flags_raw_21d_slope_v001_signal(distressflag, closeadj):
    base = _mean(distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw distressflag
def df_f96_distress_flags_raw_21d_slope_v002_signal(distressflag, closeadj):
    base = _mean(distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw distressflag
def df_f96_distress_flags_raw_21d_slope_v003_signal(distressflag, closeadj):
    base = _mean(distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw distressflag
def df_f96_distress_flags_raw_63d_slope_v004_signal(distressflag, closeadj):
    base = _mean(distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw distressflag
def df_f96_distress_flags_raw_63d_slope_v005_signal(distressflag, closeadj):
    base = _mean(distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw distressflag
def df_f96_distress_flags_raw_63d_slope_v006_signal(distressflag, closeadj):
    base = _mean(distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw distressflag
def df_f96_distress_flags_raw_126d_slope_v007_signal(distressflag, closeadj):
    base = _mean(distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw distressflag
def df_f96_distress_flags_raw_126d_slope_v008_signal(distressflag, closeadj):
    base = _mean(distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw distressflag
def df_f96_distress_flags_raw_126d_slope_v009_signal(distressflag, closeadj):
    base = _mean(distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw distressflag
def df_f96_distress_flags_raw_252d_slope_v010_signal(distressflag, closeadj):
    base = _mean(distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw distressflag
def df_f96_distress_flags_raw_252d_slope_v011_signal(distressflag, closeadj):
    base = _mean(distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw distressflag
def df_f96_distress_flags_raw_252d_slope_v012_signal(distressflag, closeadj):
    base = _mean(distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw distressflag
def df_f96_distress_flags_raw_504d_slope_v013_signal(distressflag, closeadj):
    base = _mean(distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw distressflag
def df_f96_distress_flags_raw_504d_slope_v014_signal(distressflag, closeadj):
    base = _mean(distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw distressflag
def df_f96_distress_flags_raw_504d_slope_v015_signal(distressflag, closeadj):
    base = _mean(distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log distressflag
def df_f96_distress_flags_log_21d_slope_v016_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log distressflag
def df_f96_distress_flags_log_21d_slope_v017_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log distressflag
def df_f96_distress_flags_log_21d_slope_v018_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log distressflag
def df_f96_distress_flags_log_63d_slope_v019_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log distressflag
def df_f96_distress_flags_log_63d_slope_v020_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log distressflag
def df_f96_distress_flags_log_63d_slope_v021_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log distressflag
def df_f96_distress_flags_log_126d_slope_v022_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log distressflag
def df_f96_distress_flags_log_126d_slope_v023_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log distressflag
def df_f96_distress_flags_log_126d_slope_v024_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log distressflag
def df_f96_distress_flags_log_252d_slope_v025_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log distressflag
def df_f96_distress_flags_log_252d_slope_v026_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log distressflag
def df_f96_distress_flags_log_252d_slope_v027_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log distressflag
def df_f96_distress_flags_log_504d_slope_v028_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log distressflag
def df_f96_distress_flags_log_504d_slope_v029_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log distressflag
def df_f96_distress_flags_log_504d_slope_v030_signal(distressflag, closeadj):
    base = _mean(_distress_flags_log(distressflag), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare distressflag
def df_f96_distress_flags_pershare_21d_slope_v031_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare distressflag
def df_f96_distress_flags_pershare_21d_slope_v032_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare distressflag
def df_f96_distress_flags_pershare_21d_slope_v033_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare distressflag
def df_f96_distress_flags_pershare_63d_slope_v034_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare distressflag
def df_f96_distress_flags_pershare_63d_slope_v035_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare distressflag
def df_f96_distress_flags_pershare_63d_slope_v036_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare distressflag
def df_f96_distress_flags_pershare_126d_slope_v037_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare distressflag
def df_f96_distress_flags_pershare_126d_slope_v038_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare distressflag
def df_f96_distress_flags_pershare_126d_slope_v039_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare distressflag
def df_f96_distress_flags_pershare_252d_slope_v040_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare distressflag
def df_f96_distress_flags_pershare_252d_slope_v041_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare distressflag
def df_f96_distress_flags_pershare_252d_slope_v042_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare distressflag
def df_f96_distress_flags_pershare_504d_slope_v043_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare distressflag
def df_f96_distress_flags_pershare_504d_slope_v044_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare distressflag
def df_f96_distress_flags_pershare_504d_slope_v045_signal(distressflag, sharesbas, closeadj):
    base = _mean(_distress_flags_per_share(distressflag, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets distressflag
def df_f96_distress_flags_per_assets_21d_slope_v046_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets distressflag
def df_f96_distress_flags_per_assets_21d_slope_v047_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets distressflag
def df_f96_distress_flags_per_assets_21d_slope_v048_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets distressflag
def df_f96_distress_flags_per_assets_63d_slope_v049_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets distressflag
def df_f96_distress_flags_per_assets_63d_slope_v050_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets distressflag
def df_f96_distress_flags_per_assets_63d_slope_v051_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets distressflag
def df_f96_distress_flags_per_assets_126d_slope_v052_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets distressflag
def df_f96_distress_flags_per_assets_126d_slope_v053_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets distressflag
def df_f96_distress_flags_per_assets_126d_slope_v054_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets distressflag
def df_f96_distress_flags_per_assets_252d_slope_v055_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets distressflag
def df_f96_distress_flags_per_assets_252d_slope_v056_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets distressflag
def df_f96_distress_flags_per_assets_252d_slope_v057_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets distressflag
def df_f96_distress_flags_per_assets_504d_slope_v058_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets distressflag
def df_f96_distress_flags_per_assets_504d_slope_v059_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets distressflag
def df_f96_distress_flags_per_assets_504d_slope_v060_signal(distressflag, assets):
    base = _mean(_distress_flags_scaled(distressflag, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_21d_slope_v061_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_21d_slope_v062_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_21d_slope_v063_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_63d_slope_v064_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_63d_slope_v065_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_63d_slope_v066_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_126d_slope_v067_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_126d_slope_v068_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_126d_slope_v069_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_252d_slope_v070_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_252d_slope_v071_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_252d_slope_v072_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_504d_slope_v073_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_504d_slope_v074_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap distressflag
def df_f96_distress_flags_per_marketcap_504d_slope_v075_signal(distressflag, marketcap):
    base = _mean(_distress_flags_scaled(distressflag, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity distressflag
def df_f96_distress_flags_per_equity_21d_slope_v076_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity distressflag
def df_f96_distress_flags_per_equity_21d_slope_v077_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity distressflag
def df_f96_distress_flags_per_equity_21d_slope_v078_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity distressflag
def df_f96_distress_flags_per_equity_63d_slope_v079_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity distressflag
def df_f96_distress_flags_per_equity_63d_slope_v080_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity distressflag
def df_f96_distress_flags_per_equity_63d_slope_v081_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity distressflag
def df_f96_distress_flags_per_equity_126d_slope_v082_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity distressflag
def df_f96_distress_flags_per_equity_126d_slope_v083_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity distressflag
def df_f96_distress_flags_per_equity_126d_slope_v084_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity distressflag
def df_f96_distress_flags_per_equity_252d_slope_v085_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity distressflag
def df_f96_distress_flags_per_equity_252d_slope_v086_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity distressflag
def df_f96_distress_flags_per_equity_252d_slope_v087_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity distressflag
def df_f96_distress_flags_per_equity_504d_slope_v088_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity distressflag
def df_f96_distress_flags_per_equity_504d_slope_v089_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity distressflag
def df_f96_distress_flags_per_equity_504d_slope_v090_signal(distressflag, equity):
    base = _mean(_distress_flags_scaled(distressflag, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std distressflag
def df_f96_distress_flags_std_21d_slope_v091_signal(distressflag, closeadj):
    base = _std(distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std distressflag
def df_f96_distress_flags_std_21d_slope_v092_signal(distressflag, closeadj):
    base = _std(distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std distressflag
def df_f96_distress_flags_std_21d_slope_v093_signal(distressflag, closeadj):
    base = _std(distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std distressflag
def df_f96_distress_flags_std_63d_slope_v094_signal(distressflag, closeadj):
    base = _std(distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std distressflag
def df_f96_distress_flags_std_63d_slope_v095_signal(distressflag, closeadj):
    base = _std(distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std distressflag
def df_f96_distress_flags_std_63d_slope_v096_signal(distressflag, closeadj):
    base = _std(distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std distressflag
def df_f96_distress_flags_std_126d_slope_v097_signal(distressflag, closeadj):
    base = _std(distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std distressflag
def df_f96_distress_flags_std_126d_slope_v098_signal(distressflag, closeadj):
    base = _std(distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std distressflag
def df_f96_distress_flags_std_126d_slope_v099_signal(distressflag, closeadj):
    base = _std(distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std distressflag
def df_f96_distress_flags_std_252d_slope_v100_signal(distressflag, closeadj):
    base = _std(distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std distressflag
def df_f96_distress_flags_std_252d_slope_v101_signal(distressflag, closeadj):
    base = _std(distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std distressflag
def df_f96_distress_flags_std_252d_slope_v102_signal(distressflag, closeadj):
    base = _std(distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std distressflag
def df_f96_distress_flags_std_504d_slope_v103_signal(distressflag, closeadj):
    base = _std(distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std distressflag
def df_f96_distress_flags_std_504d_slope_v104_signal(distressflag, closeadj):
    base = _std(distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std distressflag
def df_f96_distress_flags_std_504d_slope_v105_signal(distressflag, closeadj):
    base = _std(distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm distressflag
def df_f96_distress_flags_ewm_21d_slope_v106_signal(distressflag, closeadj):
    base = distressflag.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm distressflag
def df_f96_distress_flags_ewm_21d_slope_v107_signal(distressflag, closeadj):
    base = distressflag.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm distressflag
def df_f96_distress_flags_ewm_21d_slope_v108_signal(distressflag, closeadj):
    base = distressflag.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm distressflag
def df_f96_distress_flags_ewm_63d_slope_v109_signal(distressflag, closeadj):
    base = distressflag.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm distressflag
def df_f96_distress_flags_ewm_63d_slope_v110_signal(distressflag, closeadj):
    base = distressflag.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm distressflag
def df_f96_distress_flags_ewm_63d_slope_v111_signal(distressflag, closeadj):
    base = distressflag.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm distressflag
def df_f96_distress_flags_ewm_126d_slope_v112_signal(distressflag, closeadj):
    base = distressflag.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm distressflag
def df_f96_distress_flags_ewm_126d_slope_v113_signal(distressflag, closeadj):
    base = distressflag.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm distressflag
def df_f96_distress_flags_ewm_126d_slope_v114_signal(distressflag, closeadj):
    base = distressflag.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm distressflag
def df_f96_distress_flags_ewm_252d_slope_v115_signal(distressflag, closeadj):
    base = distressflag.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm distressflag
def df_f96_distress_flags_ewm_252d_slope_v116_signal(distressflag, closeadj):
    base = distressflag.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm distressflag
def df_f96_distress_flags_ewm_252d_slope_v117_signal(distressflag, closeadj):
    base = distressflag.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm distressflag
def df_f96_distress_flags_ewm_504d_slope_v118_signal(distressflag, closeadj):
    base = distressflag.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm distressflag
def df_f96_distress_flags_ewm_504d_slope_v119_signal(distressflag, closeadj):
    base = distressflag.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm distressflag
def df_f96_distress_flags_ewm_504d_slope_v120_signal(distressflag, closeadj):
    base = distressflag.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq distressflag
def df_f96_distress_flags_sq_21d_slope_v121_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq distressflag
def df_f96_distress_flags_sq_21d_slope_v122_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq distressflag
def df_f96_distress_flags_sq_21d_slope_v123_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq distressflag
def df_f96_distress_flags_sq_63d_slope_v124_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq distressflag
def df_f96_distress_flags_sq_63d_slope_v125_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq distressflag
def df_f96_distress_flags_sq_63d_slope_v126_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq distressflag
def df_f96_distress_flags_sq_126d_slope_v127_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq distressflag
def df_f96_distress_flags_sq_126d_slope_v128_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq distressflag
def df_f96_distress_flags_sq_126d_slope_v129_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq distressflag
def df_f96_distress_flags_sq_252d_slope_v130_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq distressflag
def df_f96_distress_flags_sq_252d_slope_v131_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq distressflag
def df_f96_distress_flags_sq_252d_slope_v132_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq distressflag
def df_f96_distress_flags_sq_504d_slope_v133_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq distressflag
def df_f96_distress_flags_sq_504d_slope_v134_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq distressflag
def df_f96_distress_flags_sq_504d_slope_v135_signal(distressflag, closeadj):
    base = _mean(distressflag * distressflag, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z distressflag
def df_f96_distress_flags_z_21d_slope_v136_signal(distressflag):
    base = _z(distressflag, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z distressflag
def df_f96_distress_flags_z_21d_slope_v137_signal(distressflag):
    base = _z(distressflag, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z distressflag
def df_f96_distress_flags_z_21d_slope_v138_signal(distressflag):
    base = _z(distressflag, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z distressflag
def df_f96_distress_flags_z_63d_slope_v139_signal(distressflag):
    base = _z(distressflag, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z distressflag
def df_f96_distress_flags_z_63d_slope_v140_signal(distressflag):
    base = _z(distressflag, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z distressflag
def df_f96_distress_flags_z_63d_slope_v141_signal(distressflag):
    base = _z(distressflag, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z distressflag
def df_f96_distress_flags_z_126d_slope_v142_signal(distressflag):
    base = _z(distressflag, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z distressflag
def df_f96_distress_flags_z_126d_slope_v143_signal(distressflag):
    base = _z(distressflag, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z distressflag
def df_f96_distress_flags_z_126d_slope_v144_signal(distressflag):
    base = _z(distressflag, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z distressflag
def df_f96_distress_flags_z_252d_slope_v145_signal(distressflag):
    base = _z(distressflag, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z distressflag
def df_f96_distress_flags_z_252d_slope_v146_signal(distressflag):
    base = _z(distressflag, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z distressflag
def df_f96_distress_flags_z_252d_slope_v147_signal(distressflag):
    base = _z(distressflag, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z distressflag
def df_f96_distress_flags_z_504d_slope_v148_signal(distressflag):
    base = _z(distressflag, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z distressflag
def df_f96_distress_flags_z_504d_slope_v149_signal(distressflag):
    base = _z(distressflag, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z distressflag
def df_f96_distress_flags_z_504d_slope_v150_signal(distressflag):
    base = _z(distressflag, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
