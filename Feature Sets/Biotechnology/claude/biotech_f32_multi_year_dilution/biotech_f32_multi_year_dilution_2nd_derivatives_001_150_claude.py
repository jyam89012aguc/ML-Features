"""Family f32 - Cumulative multi-year dilution  (E_Dilution_Shares) | 2nd derivatives 001-150"""
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
def _multi_year_dilution_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _multi_year_dilution_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _multi_year_dilution_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw sharesbas
def myd_f32_multi_year_dilution_raw_21d_slope_v001_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw sharesbas
def myd_f32_multi_year_dilution_raw_21d_slope_v002_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw sharesbas
def myd_f32_multi_year_dilution_raw_21d_slope_v003_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw sharesbas
def myd_f32_multi_year_dilution_raw_63d_slope_v004_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw sharesbas
def myd_f32_multi_year_dilution_raw_63d_slope_v005_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw sharesbas
def myd_f32_multi_year_dilution_raw_63d_slope_v006_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw sharesbas
def myd_f32_multi_year_dilution_raw_126d_slope_v007_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw sharesbas
def myd_f32_multi_year_dilution_raw_126d_slope_v008_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw sharesbas
def myd_f32_multi_year_dilution_raw_126d_slope_v009_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw sharesbas
def myd_f32_multi_year_dilution_raw_252d_slope_v010_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw sharesbas
def myd_f32_multi_year_dilution_raw_252d_slope_v011_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw sharesbas
def myd_f32_multi_year_dilution_raw_252d_slope_v012_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw sharesbas
def myd_f32_multi_year_dilution_raw_504d_slope_v013_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw sharesbas
def myd_f32_multi_year_dilution_raw_504d_slope_v014_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw sharesbas
def myd_f32_multi_year_dilution_raw_504d_slope_v015_signal(sharesbas, closeadj):
    base = _mean(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log sharesbas
def myd_f32_multi_year_dilution_log_21d_slope_v016_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log sharesbas
def myd_f32_multi_year_dilution_log_21d_slope_v017_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log sharesbas
def myd_f32_multi_year_dilution_log_21d_slope_v018_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log sharesbas
def myd_f32_multi_year_dilution_log_63d_slope_v019_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log sharesbas
def myd_f32_multi_year_dilution_log_63d_slope_v020_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log sharesbas
def myd_f32_multi_year_dilution_log_63d_slope_v021_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log sharesbas
def myd_f32_multi_year_dilution_log_126d_slope_v022_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log sharesbas
def myd_f32_multi_year_dilution_log_126d_slope_v023_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log sharesbas
def myd_f32_multi_year_dilution_log_126d_slope_v024_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log sharesbas
def myd_f32_multi_year_dilution_log_252d_slope_v025_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log sharesbas
def myd_f32_multi_year_dilution_log_252d_slope_v026_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log sharesbas
def myd_f32_multi_year_dilution_log_252d_slope_v027_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log sharesbas
def myd_f32_multi_year_dilution_log_504d_slope_v028_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log sharesbas
def myd_f32_multi_year_dilution_log_504d_slope_v029_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log sharesbas
def myd_f32_multi_year_dilution_log_504d_slope_v030_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_log(sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_21d_slope_v031_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_21d_slope_v032_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_21d_slope_v033_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_63d_slope_v034_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_63d_slope_v035_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_63d_slope_v036_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_126d_slope_v037_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_126d_slope_v038_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_126d_slope_v039_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_252d_slope_v040_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_252d_slope_v041_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_252d_slope_v042_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_504d_slope_v043_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_504d_slope_v044_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare sharesbas
def myd_f32_multi_year_dilution_pershare_504d_slope_v045_signal(sharesbas, closeadj):
    base = _mean(_multi_year_dilution_per_share(sharesbas, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_21d_slope_v046_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_21d_slope_v047_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_21d_slope_v048_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_63d_slope_v049_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_63d_slope_v050_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_63d_slope_v051_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_126d_slope_v052_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_126d_slope_v053_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_126d_slope_v054_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_252d_slope_v055_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_252d_slope_v056_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_252d_slope_v057_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_504d_slope_v058_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_504d_slope_v059_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets sharesbas
def myd_f32_multi_year_dilution_per_assets_504d_slope_v060_signal(sharesbas, assets):
    base = _mean(_multi_year_dilution_scaled(sharesbas, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_21d_slope_v061_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_21d_slope_v062_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_21d_slope_v063_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_63d_slope_v064_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_63d_slope_v065_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_63d_slope_v066_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_126d_slope_v067_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_126d_slope_v068_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_126d_slope_v069_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_252d_slope_v070_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_252d_slope_v071_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_252d_slope_v072_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_504d_slope_v073_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_504d_slope_v074_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap sharesbas
def myd_f32_multi_year_dilution_per_marketcap_504d_slope_v075_signal(sharesbas, marketcap):
    base = _mean(_multi_year_dilution_scaled(sharesbas, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_21d_slope_v076_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_21d_slope_v077_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_21d_slope_v078_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_63d_slope_v079_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_63d_slope_v080_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_63d_slope_v081_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_126d_slope_v082_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_126d_slope_v083_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_126d_slope_v084_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_252d_slope_v085_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_252d_slope_v086_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_252d_slope_v087_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_504d_slope_v088_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_504d_slope_v089_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity sharesbas
def myd_f32_multi_year_dilution_per_equity_504d_slope_v090_signal(sharesbas, equity):
    base = _mean(_multi_year_dilution_scaled(sharesbas, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std sharesbas
def myd_f32_multi_year_dilution_std_21d_slope_v091_signal(sharesbas, closeadj):
    base = _std(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std sharesbas
def myd_f32_multi_year_dilution_std_21d_slope_v092_signal(sharesbas, closeadj):
    base = _std(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std sharesbas
def myd_f32_multi_year_dilution_std_21d_slope_v093_signal(sharesbas, closeadj):
    base = _std(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std sharesbas
def myd_f32_multi_year_dilution_std_63d_slope_v094_signal(sharesbas, closeadj):
    base = _std(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std sharesbas
def myd_f32_multi_year_dilution_std_63d_slope_v095_signal(sharesbas, closeadj):
    base = _std(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std sharesbas
def myd_f32_multi_year_dilution_std_63d_slope_v096_signal(sharesbas, closeadj):
    base = _std(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std sharesbas
def myd_f32_multi_year_dilution_std_126d_slope_v097_signal(sharesbas, closeadj):
    base = _std(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std sharesbas
def myd_f32_multi_year_dilution_std_126d_slope_v098_signal(sharesbas, closeadj):
    base = _std(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std sharesbas
def myd_f32_multi_year_dilution_std_126d_slope_v099_signal(sharesbas, closeadj):
    base = _std(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std sharesbas
def myd_f32_multi_year_dilution_std_252d_slope_v100_signal(sharesbas, closeadj):
    base = _std(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std sharesbas
def myd_f32_multi_year_dilution_std_252d_slope_v101_signal(sharesbas, closeadj):
    base = _std(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std sharesbas
def myd_f32_multi_year_dilution_std_252d_slope_v102_signal(sharesbas, closeadj):
    base = _std(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std sharesbas
def myd_f32_multi_year_dilution_std_504d_slope_v103_signal(sharesbas, closeadj):
    base = _std(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std sharesbas
def myd_f32_multi_year_dilution_std_504d_slope_v104_signal(sharesbas, closeadj):
    base = _std(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std sharesbas
def myd_f32_multi_year_dilution_std_504d_slope_v105_signal(sharesbas, closeadj):
    base = _std(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_21d_slope_v106_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_21d_slope_v107_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_21d_slope_v108_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_63d_slope_v109_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_63d_slope_v110_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_63d_slope_v111_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_126d_slope_v112_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_126d_slope_v113_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_126d_slope_v114_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_252d_slope_v115_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_252d_slope_v116_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_252d_slope_v117_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_504d_slope_v118_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_504d_slope_v119_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm sharesbas
def myd_f32_multi_year_dilution_ewm_504d_slope_v120_signal(sharesbas, closeadj):
    base = sharesbas.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq sharesbas
def myd_f32_multi_year_dilution_sq_21d_slope_v121_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq sharesbas
def myd_f32_multi_year_dilution_sq_21d_slope_v122_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq sharesbas
def myd_f32_multi_year_dilution_sq_21d_slope_v123_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq sharesbas
def myd_f32_multi_year_dilution_sq_63d_slope_v124_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq sharesbas
def myd_f32_multi_year_dilution_sq_63d_slope_v125_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq sharesbas
def myd_f32_multi_year_dilution_sq_63d_slope_v126_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq sharesbas
def myd_f32_multi_year_dilution_sq_126d_slope_v127_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq sharesbas
def myd_f32_multi_year_dilution_sq_126d_slope_v128_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq sharesbas
def myd_f32_multi_year_dilution_sq_126d_slope_v129_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq sharesbas
def myd_f32_multi_year_dilution_sq_252d_slope_v130_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq sharesbas
def myd_f32_multi_year_dilution_sq_252d_slope_v131_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq sharesbas
def myd_f32_multi_year_dilution_sq_252d_slope_v132_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq sharesbas
def myd_f32_multi_year_dilution_sq_504d_slope_v133_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq sharesbas
def myd_f32_multi_year_dilution_sq_504d_slope_v134_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq sharesbas
def myd_f32_multi_year_dilution_sq_504d_slope_v135_signal(sharesbas, closeadj):
    base = _mean(sharesbas * sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z sharesbas
def myd_f32_multi_year_dilution_z_21d_slope_v136_signal(sharesbas):
    base = _z(sharesbas, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z sharesbas
def myd_f32_multi_year_dilution_z_21d_slope_v137_signal(sharesbas):
    base = _z(sharesbas, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z sharesbas
def myd_f32_multi_year_dilution_z_21d_slope_v138_signal(sharesbas):
    base = _z(sharesbas, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z sharesbas
def myd_f32_multi_year_dilution_z_63d_slope_v139_signal(sharesbas):
    base = _z(sharesbas, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z sharesbas
def myd_f32_multi_year_dilution_z_63d_slope_v140_signal(sharesbas):
    base = _z(sharesbas, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z sharesbas
def myd_f32_multi_year_dilution_z_63d_slope_v141_signal(sharesbas):
    base = _z(sharesbas, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z sharesbas
def myd_f32_multi_year_dilution_z_126d_slope_v142_signal(sharesbas):
    base = _z(sharesbas, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z sharesbas
def myd_f32_multi_year_dilution_z_126d_slope_v143_signal(sharesbas):
    base = _z(sharesbas, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z sharesbas
def myd_f32_multi_year_dilution_z_126d_slope_v144_signal(sharesbas):
    base = _z(sharesbas, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z sharesbas
def myd_f32_multi_year_dilution_z_252d_slope_v145_signal(sharesbas):
    base = _z(sharesbas, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z sharesbas
def myd_f32_multi_year_dilution_z_252d_slope_v146_signal(sharesbas):
    base = _z(sharesbas, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z sharesbas
def myd_f32_multi_year_dilution_z_252d_slope_v147_signal(sharesbas):
    base = _z(sharesbas, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z sharesbas
def myd_f32_multi_year_dilution_z_504d_slope_v148_signal(sharesbas):
    base = _z(sharesbas, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z sharesbas
def myd_f32_multi_year_dilution_z_504d_slope_v149_signal(sharesbas):
    base = _z(sharesbas, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z sharesbas
def myd_f32_multi_year_dilution_z_504d_slope_v150_signal(sharesbas):
    base = _z(sharesbas, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
