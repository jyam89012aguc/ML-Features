"""Family f83 - Trend-break / regime change  (N_Fundamental_Dynamics) | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw rnd
def rc_f83_regime_change_raw_21d_slope_v001_signal(rnd, closeadj):
    base = _mean(rnd, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw rnd
def rc_f83_regime_change_raw_21d_slope_v002_signal(rnd, closeadj):
    base = _mean(rnd, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw rnd
def rc_f83_regime_change_raw_21d_slope_v003_signal(rnd, closeadj):
    base = _mean(rnd, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw rnd
def rc_f83_regime_change_raw_63d_slope_v004_signal(rnd, closeadj):
    base = _mean(rnd, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw rnd
def rc_f83_regime_change_raw_63d_slope_v005_signal(rnd, closeadj):
    base = _mean(rnd, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw rnd
def rc_f83_regime_change_raw_63d_slope_v006_signal(rnd, closeadj):
    base = _mean(rnd, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw rnd
def rc_f83_regime_change_raw_126d_slope_v007_signal(rnd, closeadj):
    base = _mean(rnd, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw rnd
def rc_f83_regime_change_raw_126d_slope_v008_signal(rnd, closeadj):
    base = _mean(rnd, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw rnd
def rc_f83_regime_change_raw_126d_slope_v009_signal(rnd, closeadj):
    base = _mean(rnd, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw rnd
def rc_f83_regime_change_raw_252d_slope_v010_signal(rnd, closeadj):
    base = _mean(rnd, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw rnd
def rc_f83_regime_change_raw_252d_slope_v011_signal(rnd, closeadj):
    base = _mean(rnd, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw rnd
def rc_f83_regime_change_raw_252d_slope_v012_signal(rnd, closeadj):
    base = _mean(rnd, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw rnd
def rc_f83_regime_change_raw_504d_slope_v013_signal(rnd, closeadj):
    base = _mean(rnd, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw rnd
def rc_f83_regime_change_raw_504d_slope_v014_signal(rnd, closeadj):
    base = _mean(rnd, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw rnd
def rc_f83_regime_change_raw_504d_slope_v015_signal(rnd, closeadj):
    base = _mean(rnd, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log rnd
def rc_f83_regime_change_log_21d_slope_v016_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log rnd
def rc_f83_regime_change_log_21d_slope_v017_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log rnd
def rc_f83_regime_change_log_21d_slope_v018_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log rnd
def rc_f83_regime_change_log_63d_slope_v019_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log rnd
def rc_f83_regime_change_log_63d_slope_v020_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log rnd
def rc_f83_regime_change_log_63d_slope_v021_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log rnd
def rc_f83_regime_change_log_126d_slope_v022_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log rnd
def rc_f83_regime_change_log_126d_slope_v023_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log rnd
def rc_f83_regime_change_log_126d_slope_v024_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log rnd
def rc_f83_regime_change_log_252d_slope_v025_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log rnd
def rc_f83_regime_change_log_252d_slope_v026_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log rnd
def rc_f83_regime_change_log_252d_slope_v027_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log rnd
def rc_f83_regime_change_log_504d_slope_v028_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log rnd
def rc_f83_regime_change_log_504d_slope_v029_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log rnd
def rc_f83_regime_change_log_504d_slope_v030_signal(rnd, closeadj):
    base = _mean(_regime_change_log(rnd), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare rnd
def rc_f83_regime_change_pershare_21d_slope_v031_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare rnd
def rc_f83_regime_change_pershare_21d_slope_v032_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare rnd
def rc_f83_regime_change_pershare_21d_slope_v033_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare rnd
def rc_f83_regime_change_pershare_63d_slope_v034_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare rnd
def rc_f83_regime_change_pershare_63d_slope_v035_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare rnd
def rc_f83_regime_change_pershare_63d_slope_v036_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare rnd
def rc_f83_regime_change_pershare_126d_slope_v037_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare rnd
def rc_f83_regime_change_pershare_126d_slope_v038_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare rnd
def rc_f83_regime_change_pershare_126d_slope_v039_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare rnd
def rc_f83_regime_change_pershare_252d_slope_v040_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare rnd
def rc_f83_regime_change_pershare_252d_slope_v041_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare rnd
def rc_f83_regime_change_pershare_252d_slope_v042_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare rnd
def rc_f83_regime_change_pershare_504d_slope_v043_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare rnd
def rc_f83_regime_change_pershare_504d_slope_v044_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare rnd
def rc_f83_regime_change_pershare_504d_slope_v045_signal(rnd, sharesbas, closeadj):
    base = _mean(_regime_change_per_share(rnd, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets rnd
def rc_f83_regime_change_per_assets_21d_slope_v046_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets rnd
def rc_f83_regime_change_per_assets_21d_slope_v047_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets rnd
def rc_f83_regime_change_per_assets_21d_slope_v048_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets rnd
def rc_f83_regime_change_per_assets_63d_slope_v049_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets rnd
def rc_f83_regime_change_per_assets_63d_slope_v050_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets rnd
def rc_f83_regime_change_per_assets_63d_slope_v051_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets rnd
def rc_f83_regime_change_per_assets_126d_slope_v052_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets rnd
def rc_f83_regime_change_per_assets_126d_slope_v053_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets rnd
def rc_f83_regime_change_per_assets_126d_slope_v054_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets rnd
def rc_f83_regime_change_per_assets_252d_slope_v055_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets rnd
def rc_f83_regime_change_per_assets_252d_slope_v056_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets rnd
def rc_f83_regime_change_per_assets_252d_slope_v057_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets rnd
def rc_f83_regime_change_per_assets_504d_slope_v058_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets rnd
def rc_f83_regime_change_per_assets_504d_slope_v059_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets rnd
def rc_f83_regime_change_per_assets_504d_slope_v060_signal(rnd, assets):
    base = _mean(_regime_change_scaled(rnd, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_21d_slope_v061_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_21d_slope_v062_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_21d_slope_v063_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_63d_slope_v064_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_63d_slope_v065_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_63d_slope_v066_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_126d_slope_v067_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_126d_slope_v068_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_126d_slope_v069_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_252d_slope_v070_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_252d_slope_v071_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_252d_slope_v072_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_504d_slope_v073_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_504d_slope_v074_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap rnd
def rc_f83_regime_change_per_marketcap_504d_slope_v075_signal(rnd, marketcap):
    base = _mean(_regime_change_scaled(rnd, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity rnd
def rc_f83_regime_change_per_equity_21d_slope_v076_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity rnd
def rc_f83_regime_change_per_equity_21d_slope_v077_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity rnd
def rc_f83_regime_change_per_equity_21d_slope_v078_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity rnd
def rc_f83_regime_change_per_equity_63d_slope_v079_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity rnd
def rc_f83_regime_change_per_equity_63d_slope_v080_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity rnd
def rc_f83_regime_change_per_equity_63d_slope_v081_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity rnd
def rc_f83_regime_change_per_equity_126d_slope_v082_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity rnd
def rc_f83_regime_change_per_equity_126d_slope_v083_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity rnd
def rc_f83_regime_change_per_equity_126d_slope_v084_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity rnd
def rc_f83_regime_change_per_equity_252d_slope_v085_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity rnd
def rc_f83_regime_change_per_equity_252d_slope_v086_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity rnd
def rc_f83_regime_change_per_equity_252d_slope_v087_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity rnd
def rc_f83_regime_change_per_equity_504d_slope_v088_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity rnd
def rc_f83_regime_change_per_equity_504d_slope_v089_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity rnd
def rc_f83_regime_change_per_equity_504d_slope_v090_signal(rnd, equity):
    base = _mean(_regime_change_scaled(rnd, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std rnd
def rc_f83_regime_change_std_21d_slope_v091_signal(rnd, closeadj):
    base = _std(rnd, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std rnd
def rc_f83_regime_change_std_21d_slope_v092_signal(rnd, closeadj):
    base = _std(rnd, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std rnd
def rc_f83_regime_change_std_21d_slope_v093_signal(rnd, closeadj):
    base = _std(rnd, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std rnd
def rc_f83_regime_change_std_63d_slope_v094_signal(rnd, closeadj):
    base = _std(rnd, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std rnd
def rc_f83_regime_change_std_63d_slope_v095_signal(rnd, closeadj):
    base = _std(rnd, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std rnd
def rc_f83_regime_change_std_63d_slope_v096_signal(rnd, closeadj):
    base = _std(rnd, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std rnd
def rc_f83_regime_change_std_126d_slope_v097_signal(rnd, closeadj):
    base = _std(rnd, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std rnd
def rc_f83_regime_change_std_126d_slope_v098_signal(rnd, closeadj):
    base = _std(rnd, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std rnd
def rc_f83_regime_change_std_126d_slope_v099_signal(rnd, closeadj):
    base = _std(rnd, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std rnd
def rc_f83_regime_change_std_252d_slope_v100_signal(rnd, closeadj):
    base = _std(rnd, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std rnd
def rc_f83_regime_change_std_252d_slope_v101_signal(rnd, closeadj):
    base = _std(rnd, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std rnd
def rc_f83_regime_change_std_252d_slope_v102_signal(rnd, closeadj):
    base = _std(rnd, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std rnd
def rc_f83_regime_change_std_504d_slope_v103_signal(rnd, closeadj):
    base = _std(rnd, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std rnd
def rc_f83_regime_change_std_504d_slope_v104_signal(rnd, closeadj):
    base = _std(rnd, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std rnd
def rc_f83_regime_change_std_504d_slope_v105_signal(rnd, closeadj):
    base = _std(rnd, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm rnd
def rc_f83_regime_change_ewm_21d_slope_v106_signal(rnd, closeadj):
    base = rnd.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm rnd
def rc_f83_regime_change_ewm_21d_slope_v107_signal(rnd, closeadj):
    base = rnd.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm rnd
def rc_f83_regime_change_ewm_21d_slope_v108_signal(rnd, closeadj):
    base = rnd.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm rnd
def rc_f83_regime_change_ewm_63d_slope_v109_signal(rnd, closeadj):
    base = rnd.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm rnd
def rc_f83_regime_change_ewm_63d_slope_v110_signal(rnd, closeadj):
    base = rnd.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm rnd
def rc_f83_regime_change_ewm_63d_slope_v111_signal(rnd, closeadj):
    base = rnd.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm rnd
def rc_f83_regime_change_ewm_126d_slope_v112_signal(rnd, closeadj):
    base = rnd.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm rnd
def rc_f83_regime_change_ewm_126d_slope_v113_signal(rnd, closeadj):
    base = rnd.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm rnd
def rc_f83_regime_change_ewm_126d_slope_v114_signal(rnd, closeadj):
    base = rnd.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm rnd
def rc_f83_regime_change_ewm_252d_slope_v115_signal(rnd, closeadj):
    base = rnd.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm rnd
def rc_f83_regime_change_ewm_252d_slope_v116_signal(rnd, closeadj):
    base = rnd.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm rnd
def rc_f83_regime_change_ewm_252d_slope_v117_signal(rnd, closeadj):
    base = rnd.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm rnd
def rc_f83_regime_change_ewm_504d_slope_v118_signal(rnd, closeadj):
    base = rnd.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm rnd
def rc_f83_regime_change_ewm_504d_slope_v119_signal(rnd, closeadj):
    base = rnd.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm rnd
def rc_f83_regime_change_ewm_504d_slope_v120_signal(rnd, closeadj):
    base = rnd.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq rnd
def rc_f83_regime_change_sq_21d_slope_v121_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq rnd
def rc_f83_regime_change_sq_21d_slope_v122_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq rnd
def rc_f83_regime_change_sq_21d_slope_v123_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq rnd
def rc_f83_regime_change_sq_63d_slope_v124_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq rnd
def rc_f83_regime_change_sq_63d_slope_v125_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq rnd
def rc_f83_regime_change_sq_63d_slope_v126_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq rnd
def rc_f83_regime_change_sq_126d_slope_v127_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq rnd
def rc_f83_regime_change_sq_126d_slope_v128_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq rnd
def rc_f83_regime_change_sq_126d_slope_v129_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq rnd
def rc_f83_regime_change_sq_252d_slope_v130_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq rnd
def rc_f83_regime_change_sq_252d_slope_v131_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq rnd
def rc_f83_regime_change_sq_252d_slope_v132_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq rnd
def rc_f83_regime_change_sq_504d_slope_v133_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq rnd
def rc_f83_regime_change_sq_504d_slope_v134_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq rnd
def rc_f83_regime_change_sq_504d_slope_v135_signal(rnd, closeadj):
    base = _mean(rnd * rnd, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z rnd
def rc_f83_regime_change_z_21d_slope_v136_signal(rnd):
    base = _z(rnd, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z rnd
def rc_f83_regime_change_z_21d_slope_v137_signal(rnd):
    base = _z(rnd, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z rnd
def rc_f83_regime_change_z_21d_slope_v138_signal(rnd):
    base = _z(rnd, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z rnd
def rc_f83_regime_change_z_63d_slope_v139_signal(rnd):
    base = _z(rnd, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z rnd
def rc_f83_regime_change_z_63d_slope_v140_signal(rnd):
    base = _z(rnd, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z rnd
def rc_f83_regime_change_z_63d_slope_v141_signal(rnd):
    base = _z(rnd, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z rnd
def rc_f83_regime_change_z_126d_slope_v142_signal(rnd):
    base = _z(rnd, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z rnd
def rc_f83_regime_change_z_126d_slope_v143_signal(rnd):
    base = _z(rnd, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z rnd
def rc_f83_regime_change_z_126d_slope_v144_signal(rnd):
    base = _z(rnd, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z rnd
def rc_f83_regime_change_z_252d_slope_v145_signal(rnd):
    base = _z(rnd, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z rnd
def rc_f83_regime_change_z_252d_slope_v146_signal(rnd):
    base = _z(rnd, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z rnd
def rc_f83_regime_change_z_252d_slope_v147_signal(rnd):
    base = _z(rnd, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z rnd
def rc_f83_regime_change_z_504d_slope_v148_signal(rnd):
    base = _z(rnd, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z rnd
def rc_f83_regime_change_z_504d_slope_v149_signal(rnd):
    base = _z(rnd, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z rnd
def rc_f83_regime_change_z_504d_slope_v150_signal(rnd):
    base = _z(rnd, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
