"""Family f33 - Sharefactor / split continuity  (E_Dilution_Shares) | 2nd derivatives 001-150"""
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
def _sharefactor_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _sharefactor_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _sharefactor_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw sharefactor
def sf_f33_sharefactor_raw_21d_slope_v001_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw sharefactor
def sf_f33_sharefactor_raw_21d_slope_v002_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw sharefactor
def sf_f33_sharefactor_raw_21d_slope_v003_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw sharefactor
def sf_f33_sharefactor_raw_63d_slope_v004_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw sharefactor
def sf_f33_sharefactor_raw_63d_slope_v005_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw sharefactor
def sf_f33_sharefactor_raw_63d_slope_v006_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw sharefactor
def sf_f33_sharefactor_raw_126d_slope_v007_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw sharefactor
def sf_f33_sharefactor_raw_126d_slope_v008_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw sharefactor
def sf_f33_sharefactor_raw_126d_slope_v009_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw sharefactor
def sf_f33_sharefactor_raw_252d_slope_v010_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw sharefactor
def sf_f33_sharefactor_raw_252d_slope_v011_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw sharefactor
def sf_f33_sharefactor_raw_252d_slope_v012_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw sharefactor
def sf_f33_sharefactor_raw_504d_slope_v013_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw sharefactor
def sf_f33_sharefactor_raw_504d_slope_v014_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw sharefactor
def sf_f33_sharefactor_raw_504d_slope_v015_signal(sharefactor, closeadj):
    base = _mean(sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log sharefactor
def sf_f33_sharefactor_log_21d_slope_v016_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log sharefactor
def sf_f33_sharefactor_log_21d_slope_v017_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log sharefactor
def sf_f33_sharefactor_log_21d_slope_v018_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log sharefactor
def sf_f33_sharefactor_log_63d_slope_v019_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log sharefactor
def sf_f33_sharefactor_log_63d_slope_v020_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log sharefactor
def sf_f33_sharefactor_log_63d_slope_v021_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log sharefactor
def sf_f33_sharefactor_log_126d_slope_v022_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log sharefactor
def sf_f33_sharefactor_log_126d_slope_v023_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log sharefactor
def sf_f33_sharefactor_log_126d_slope_v024_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log sharefactor
def sf_f33_sharefactor_log_252d_slope_v025_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log sharefactor
def sf_f33_sharefactor_log_252d_slope_v026_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log sharefactor
def sf_f33_sharefactor_log_252d_slope_v027_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log sharefactor
def sf_f33_sharefactor_log_504d_slope_v028_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log sharefactor
def sf_f33_sharefactor_log_504d_slope_v029_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log sharefactor
def sf_f33_sharefactor_log_504d_slope_v030_signal(sharefactor, closeadj):
    base = _mean(_sharefactor_log(sharefactor), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare sharefactor
def sf_f33_sharefactor_pershare_21d_slope_v031_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare sharefactor
def sf_f33_sharefactor_pershare_21d_slope_v032_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare sharefactor
def sf_f33_sharefactor_pershare_21d_slope_v033_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare sharefactor
def sf_f33_sharefactor_pershare_63d_slope_v034_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare sharefactor
def sf_f33_sharefactor_pershare_63d_slope_v035_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare sharefactor
def sf_f33_sharefactor_pershare_63d_slope_v036_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare sharefactor
def sf_f33_sharefactor_pershare_126d_slope_v037_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare sharefactor
def sf_f33_sharefactor_pershare_126d_slope_v038_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare sharefactor
def sf_f33_sharefactor_pershare_126d_slope_v039_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare sharefactor
def sf_f33_sharefactor_pershare_252d_slope_v040_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare sharefactor
def sf_f33_sharefactor_pershare_252d_slope_v041_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare sharefactor
def sf_f33_sharefactor_pershare_252d_slope_v042_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare sharefactor
def sf_f33_sharefactor_pershare_504d_slope_v043_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare sharefactor
def sf_f33_sharefactor_pershare_504d_slope_v044_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare sharefactor
def sf_f33_sharefactor_pershare_504d_slope_v045_signal(sharefactor, sharesbas, closeadj):
    base = _mean(_sharefactor_per_share(sharefactor, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets sharefactor
def sf_f33_sharefactor_per_assets_21d_slope_v046_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets sharefactor
def sf_f33_sharefactor_per_assets_21d_slope_v047_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets sharefactor
def sf_f33_sharefactor_per_assets_21d_slope_v048_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets sharefactor
def sf_f33_sharefactor_per_assets_63d_slope_v049_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets sharefactor
def sf_f33_sharefactor_per_assets_63d_slope_v050_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets sharefactor
def sf_f33_sharefactor_per_assets_63d_slope_v051_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets sharefactor
def sf_f33_sharefactor_per_assets_126d_slope_v052_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets sharefactor
def sf_f33_sharefactor_per_assets_126d_slope_v053_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets sharefactor
def sf_f33_sharefactor_per_assets_126d_slope_v054_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets sharefactor
def sf_f33_sharefactor_per_assets_252d_slope_v055_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets sharefactor
def sf_f33_sharefactor_per_assets_252d_slope_v056_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets sharefactor
def sf_f33_sharefactor_per_assets_252d_slope_v057_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets sharefactor
def sf_f33_sharefactor_per_assets_504d_slope_v058_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets sharefactor
def sf_f33_sharefactor_per_assets_504d_slope_v059_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets sharefactor
def sf_f33_sharefactor_per_assets_504d_slope_v060_signal(sharefactor, assets):
    base = _mean(_sharefactor_scaled(sharefactor, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_21d_slope_v061_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_21d_slope_v062_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_21d_slope_v063_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_63d_slope_v064_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_63d_slope_v065_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_63d_slope_v066_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_126d_slope_v067_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_126d_slope_v068_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_126d_slope_v069_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_252d_slope_v070_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_252d_slope_v071_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_252d_slope_v072_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_504d_slope_v073_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_504d_slope_v074_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap sharefactor
def sf_f33_sharefactor_per_marketcap_504d_slope_v075_signal(sharefactor, marketcap):
    base = _mean(_sharefactor_scaled(sharefactor, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity sharefactor
def sf_f33_sharefactor_per_equity_21d_slope_v076_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity sharefactor
def sf_f33_sharefactor_per_equity_21d_slope_v077_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity sharefactor
def sf_f33_sharefactor_per_equity_21d_slope_v078_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity sharefactor
def sf_f33_sharefactor_per_equity_63d_slope_v079_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity sharefactor
def sf_f33_sharefactor_per_equity_63d_slope_v080_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity sharefactor
def sf_f33_sharefactor_per_equity_63d_slope_v081_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity sharefactor
def sf_f33_sharefactor_per_equity_126d_slope_v082_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity sharefactor
def sf_f33_sharefactor_per_equity_126d_slope_v083_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity sharefactor
def sf_f33_sharefactor_per_equity_126d_slope_v084_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity sharefactor
def sf_f33_sharefactor_per_equity_252d_slope_v085_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity sharefactor
def sf_f33_sharefactor_per_equity_252d_slope_v086_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity sharefactor
def sf_f33_sharefactor_per_equity_252d_slope_v087_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity sharefactor
def sf_f33_sharefactor_per_equity_504d_slope_v088_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity sharefactor
def sf_f33_sharefactor_per_equity_504d_slope_v089_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity sharefactor
def sf_f33_sharefactor_per_equity_504d_slope_v090_signal(sharefactor, equity):
    base = _mean(_sharefactor_scaled(sharefactor, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std sharefactor
def sf_f33_sharefactor_std_21d_slope_v091_signal(sharefactor, closeadj):
    base = _std(sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std sharefactor
def sf_f33_sharefactor_std_21d_slope_v092_signal(sharefactor, closeadj):
    base = _std(sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std sharefactor
def sf_f33_sharefactor_std_21d_slope_v093_signal(sharefactor, closeadj):
    base = _std(sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std sharefactor
def sf_f33_sharefactor_std_63d_slope_v094_signal(sharefactor, closeadj):
    base = _std(sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std sharefactor
def sf_f33_sharefactor_std_63d_slope_v095_signal(sharefactor, closeadj):
    base = _std(sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std sharefactor
def sf_f33_sharefactor_std_63d_slope_v096_signal(sharefactor, closeadj):
    base = _std(sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std sharefactor
def sf_f33_sharefactor_std_126d_slope_v097_signal(sharefactor, closeadj):
    base = _std(sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std sharefactor
def sf_f33_sharefactor_std_126d_slope_v098_signal(sharefactor, closeadj):
    base = _std(sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std sharefactor
def sf_f33_sharefactor_std_126d_slope_v099_signal(sharefactor, closeadj):
    base = _std(sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std sharefactor
def sf_f33_sharefactor_std_252d_slope_v100_signal(sharefactor, closeadj):
    base = _std(sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std sharefactor
def sf_f33_sharefactor_std_252d_slope_v101_signal(sharefactor, closeadj):
    base = _std(sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std sharefactor
def sf_f33_sharefactor_std_252d_slope_v102_signal(sharefactor, closeadj):
    base = _std(sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std sharefactor
def sf_f33_sharefactor_std_504d_slope_v103_signal(sharefactor, closeadj):
    base = _std(sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std sharefactor
def sf_f33_sharefactor_std_504d_slope_v104_signal(sharefactor, closeadj):
    base = _std(sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std sharefactor
def sf_f33_sharefactor_std_504d_slope_v105_signal(sharefactor, closeadj):
    base = _std(sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm sharefactor
def sf_f33_sharefactor_ewm_21d_slope_v106_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm sharefactor
def sf_f33_sharefactor_ewm_21d_slope_v107_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm sharefactor
def sf_f33_sharefactor_ewm_21d_slope_v108_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm sharefactor
def sf_f33_sharefactor_ewm_63d_slope_v109_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm sharefactor
def sf_f33_sharefactor_ewm_63d_slope_v110_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm sharefactor
def sf_f33_sharefactor_ewm_63d_slope_v111_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm sharefactor
def sf_f33_sharefactor_ewm_126d_slope_v112_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm sharefactor
def sf_f33_sharefactor_ewm_126d_slope_v113_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm sharefactor
def sf_f33_sharefactor_ewm_126d_slope_v114_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm sharefactor
def sf_f33_sharefactor_ewm_252d_slope_v115_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm sharefactor
def sf_f33_sharefactor_ewm_252d_slope_v116_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm sharefactor
def sf_f33_sharefactor_ewm_252d_slope_v117_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm sharefactor
def sf_f33_sharefactor_ewm_504d_slope_v118_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm sharefactor
def sf_f33_sharefactor_ewm_504d_slope_v119_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm sharefactor
def sf_f33_sharefactor_ewm_504d_slope_v120_signal(sharefactor, closeadj):
    base = sharefactor.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq sharefactor
def sf_f33_sharefactor_sq_21d_slope_v121_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq sharefactor
def sf_f33_sharefactor_sq_21d_slope_v122_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq sharefactor
def sf_f33_sharefactor_sq_21d_slope_v123_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq sharefactor
def sf_f33_sharefactor_sq_63d_slope_v124_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq sharefactor
def sf_f33_sharefactor_sq_63d_slope_v125_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq sharefactor
def sf_f33_sharefactor_sq_63d_slope_v126_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq sharefactor
def sf_f33_sharefactor_sq_126d_slope_v127_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq sharefactor
def sf_f33_sharefactor_sq_126d_slope_v128_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq sharefactor
def sf_f33_sharefactor_sq_126d_slope_v129_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq sharefactor
def sf_f33_sharefactor_sq_252d_slope_v130_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq sharefactor
def sf_f33_sharefactor_sq_252d_slope_v131_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq sharefactor
def sf_f33_sharefactor_sq_252d_slope_v132_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq sharefactor
def sf_f33_sharefactor_sq_504d_slope_v133_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq sharefactor
def sf_f33_sharefactor_sq_504d_slope_v134_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq sharefactor
def sf_f33_sharefactor_sq_504d_slope_v135_signal(sharefactor, closeadj):
    base = _mean(sharefactor * sharefactor, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z sharefactor
def sf_f33_sharefactor_z_21d_slope_v136_signal(sharefactor):
    base = _z(sharefactor, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z sharefactor
def sf_f33_sharefactor_z_21d_slope_v137_signal(sharefactor):
    base = _z(sharefactor, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z sharefactor
def sf_f33_sharefactor_z_21d_slope_v138_signal(sharefactor):
    base = _z(sharefactor, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z sharefactor
def sf_f33_sharefactor_z_63d_slope_v139_signal(sharefactor):
    base = _z(sharefactor, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z sharefactor
def sf_f33_sharefactor_z_63d_slope_v140_signal(sharefactor):
    base = _z(sharefactor, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z sharefactor
def sf_f33_sharefactor_z_63d_slope_v141_signal(sharefactor):
    base = _z(sharefactor, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z sharefactor
def sf_f33_sharefactor_z_126d_slope_v142_signal(sharefactor):
    base = _z(sharefactor, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z sharefactor
def sf_f33_sharefactor_z_126d_slope_v143_signal(sharefactor):
    base = _z(sharefactor, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z sharefactor
def sf_f33_sharefactor_z_126d_slope_v144_signal(sharefactor):
    base = _z(sharefactor, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z sharefactor
def sf_f33_sharefactor_z_252d_slope_v145_signal(sharefactor):
    base = _z(sharefactor, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z sharefactor
def sf_f33_sharefactor_z_252d_slope_v146_signal(sharefactor):
    base = _z(sharefactor, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z sharefactor
def sf_f33_sharefactor_z_252d_slope_v147_signal(sharefactor):
    base = _z(sharefactor, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z sharefactor
def sf_f33_sharefactor_z_504d_slope_v148_signal(sharefactor):
    base = _z(sharefactor, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z sharefactor
def sf_f33_sharefactor_z_504d_slope_v149_signal(sharefactor):
    base = _z(sharefactor, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z sharefactor
def sf_f33_sharefactor_z_504d_slope_v150_signal(sharefactor):
    base = _z(sharefactor, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
