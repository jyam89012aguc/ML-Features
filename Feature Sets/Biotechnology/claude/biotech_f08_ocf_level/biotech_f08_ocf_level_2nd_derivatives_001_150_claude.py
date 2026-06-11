"""Family f08 - Operating cash flow level  (B_CashFlow_Burn) | 2nd derivatives 001-150"""
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
def _ocf_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ocf_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ocf_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw ncfo
def ocf_f08_ocf_level_raw_21d_slope_v001_signal(ncfo, closeadj):
    base = _mean(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw ncfo
def ocf_f08_ocf_level_raw_21d_slope_v002_signal(ncfo, closeadj):
    base = _mean(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw ncfo
def ocf_f08_ocf_level_raw_21d_slope_v003_signal(ncfo, closeadj):
    base = _mean(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw ncfo
def ocf_f08_ocf_level_raw_63d_slope_v004_signal(ncfo, closeadj):
    base = _mean(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw ncfo
def ocf_f08_ocf_level_raw_63d_slope_v005_signal(ncfo, closeadj):
    base = _mean(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw ncfo
def ocf_f08_ocf_level_raw_63d_slope_v006_signal(ncfo, closeadj):
    base = _mean(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw ncfo
def ocf_f08_ocf_level_raw_126d_slope_v007_signal(ncfo, closeadj):
    base = _mean(ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw ncfo
def ocf_f08_ocf_level_raw_126d_slope_v008_signal(ncfo, closeadj):
    base = _mean(ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw ncfo
def ocf_f08_ocf_level_raw_126d_slope_v009_signal(ncfo, closeadj):
    base = _mean(ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw ncfo
def ocf_f08_ocf_level_raw_252d_slope_v010_signal(ncfo, closeadj):
    base = _mean(ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw ncfo
def ocf_f08_ocf_level_raw_252d_slope_v011_signal(ncfo, closeadj):
    base = _mean(ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw ncfo
def ocf_f08_ocf_level_raw_252d_slope_v012_signal(ncfo, closeadj):
    base = _mean(ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw ncfo
def ocf_f08_ocf_level_raw_504d_slope_v013_signal(ncfo, closeadj):
    base = _mean(ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw ncfo
def ocf_f08_ocf_level_raw_504d_slope_v014_signal(ncfo, closeadj):
    base = _mean(ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw ncfo
def ocf_f08_ocf_level_raw_504d_slope_v015_signal(ncfo, closeadj):
    base = _mean(ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log ncfo
def ocf_f08_ocf_level_log_21d_slope_v016_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log ncfo
def ocf_f08_ocf_level_log_21d_slope_v017_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log ncfo
def ocf_f08_ocf_level_log_21d_slope_v018_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log ncfo
def ocf_f08_ocf_level_log_63d_slope_v019_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log ncfo
def ocf_f08_ocf_level_log_63d_slope_v020_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log ncfo
def ocf_f08_ocf_level_log_63d_slope_v021_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log ncfo
def ocf_f08_ocf_level_log_126d_slope_v022_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log ncfo
def ocf_f08_ocf_level_log_126d_slope_v023_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log ncfo
def ocf_f08_ocf_level_log_126d_slope_v024_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log ncfo
def ocf_f08_ocf_level_log_252d_slope_v025_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log ncfo
def ocf_f08_ocf_level_log_252d_slope_v026_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log ncfo
def ocf_f08_ocf_level_log_252d_slope_v027_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log ncfo
def ocf_f08_ocf_level_log_504d_slope_v028_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log ncfo
def ocf_f08_ocf_level_log_504d_slope_v029_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log ncfo
def ocf_f08_ocf_level_log_504d_slope_v030_signal(ncfo, closeadj):
    base = _mean(_ocf_level_log(ncfo), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare ncfo
def ocf_f08_ocf_level_pershare_21d_slope_v031_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare ncfo
def ocf_f08_ocf_level_pershare_21d_slope_v032_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare ncfo
def ocf_f08_ocf_level_pershare_21d_slope_v033_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare ncfo
def ocf_f08_ocf_level_pershare_63d_slope_v034_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare ncfo
def ocf_f08_ocf_level_pershare_63d_slope_v035_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare ncfo
def ocf_f08_ocf_level_pershare_63d_slope_v036_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare ncfo
def ocf_f08_ocf_level_pershare_126d_slope_v037_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare ncfo
def ocf_f08_ocf_level_pershare_126d_slope_v038_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare ncfo
def ocf_f08_ocf_level_pershare_126d_slope_v039_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare ncfo
def ocf_f08_ocf_level_pershare_252d_slope_v040_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare ncfo
def ocf_f08_ocf_level_pershare_252d_slope_v041_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare ncfo
def ocf_f08_ocf_level_pershare_252d_slope_v042_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare ncfo
def ocf_f08_ocf_level_pershare_504d_slope_v043_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare ncfo
def ocf_f08_ocf_level_pershare_504d_slope_v044_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare ncfo
def ocf_f08_ocf_level_pershare_504d_slope_v045_signal(ncfo, sharesbas, closeadj):
    base = _mean(_ocf_level_per_share(ncfo, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets ncfo
def ocf_f08_ocf_level_per_assets_21d_slope_v046_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets ncfo
def ocf_f08_ocf_level_per_assets_21d_slope_v047_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets ncfo
def ocf_f08_ocf_level_per_assets_21d_slope_v048_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets ncfo
def ocf_f08_ocf_level_per_assets_63d_slope_v049_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets ncfo
def ocf_f08_ocf_level_per_assets_63d_slope_v050_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets ncfo
def ocf_f08_ocf_level_per_assets_63d_slope_v051_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets ncfo
def ocf_f08_ocf_level_per_assets_126d_slope_v052_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets ncfo
def ocf_f08_ocf_level_per_assets_126d_slope_v053_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets ncfo
def ocf_f08_ocf_level_per_assets_126d_slope_v054_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets ncfo
def ocf_f08_ocf_level_per_assets_252d_slope_v055_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets ncfo
def ocf_f08_ocf_level_per_assets_252d_slope_v056_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets ncfo
def ocf_f08_ocf_level_per_assets_252d_slope_v057_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets ncfo
def ocf_f08_ocf_level_per_assets_504d_slope_v058_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets ncfo
def ocf_f08_ocf_level_per_assets_504d_slope_v059_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets ncfo
def ocf_f08_ocf_level_per_assets_504d_slope_v060_signal(ncfo, assets):
    base = _mean(_ocf_level_scaled(ncfo, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_21d_slope_v061_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_21d_slope_v062_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_21d_slope_v063_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_63d_slope_v064_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_63d_slope_v065_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_63d_slope_v066_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_126d_slope_v067_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_126d_slope_v068_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_126d_slope_v069_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_252d_slope_v070_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_252d_slope_v071_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_252d_slope_v072_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_504d_slope_v073_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_504d_slope_v074_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap ncfo
def ocf_f08_ocf_level_per_marketcap_504d_slope_v075_signal(ncfo, marketcap):
    base = _mean(_ocf_level_scaled(ncfo, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity ncfo
def ocf_f08_ocf_level_per_equity_21d_slope_v076_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity ncfo
def ocf_f08_ocf_level_per_equity_21d_slope_v077_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity ncfo
def ocf_f08_ocf_level_per_equity_21d_slope_v078_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity ncfo
def ocf_f08_ocf_level_per_equity_63d_slope_v079_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity ncfo
def ocf_f08_ocf_level_per_equity_63d_slope_v080_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity ncfo
def ocf_f08_ocf_level_per_equity_63d_slope_v081_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity ncfo
def ocf_f08_ocf_level_per_equity_126d_slope_v082_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity ncfo
def ocf_f08_ocf_level_per_equity_126d_slope_v083_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity ncfo
def ocf_f08_ocf_level_per_equity_126d_slope_v084_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity ncfo
def ocf_f08_ocf_level_per_equity_252d_slope_v085_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity ncfo
def ocf_f08_ocf_level_per_equity_252d_slope_v086_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity ncfo
def ocf_f08_ocf_level_per_equity_252d_slope_v087_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity ncfo
def ocf_f08_ocf_level_per_equity_504d_slope_v088_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity ncfo
def ocf_f08_ocf_level_per_equity_504d_slope_v089_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity ncfo
def ocf_f08_ocf_level_per_equity_504d_slope_v090_signal(ncfo, equity):
    base = _mean(_ocf_level_scaled(ncfo, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std ncfo
def ocf_f08_ocf_level_std_21d_slope_v091_signal(ncfo, closeadj):
    base = _std(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std ncfo
def ocf_f08_ocf_level_std_21d_slope_v092_signal(ncfo, closeadj):
    base = _std(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std ncfo
def ocf_f08_ocf_level_std_21d_slope_v093_signal(ncfo, closeadj):
    base = _std(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std ncfo
def ocf_f08_ocf_level_std_63d_slope_v094_signal(ncfo, closeadj):
    base = _std(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std ncfo
def ocf_f08_ocf_level_std_63d_slope_v095_signal(ncfo, closeadj):
    base = _std(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std ncfo
def ocf_f08_ocf_level_std_63d_slope_v096_signal(ncfo, closeadj):
    base = _std(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std ncfo
def ocf_f08_ocf_level_std_126d_slope_v097_signal(ncfo, closeadj):
    base = _std(ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std ncfo
def ocf_f08_ocf_level_std_126d_slope_v098_signal(ncfo, closeadj):
    base = _std(ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std ncfo
def ocf_f08_ocf_level_std_126d_slope_v099_signal(ncfo, closeadj):
    base = _std(ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std ncfo
def ocf_f08_ocf_level_std_252d_slope_v100_signal(ncfo, closeadj):
    base = _std(ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std ncfo
def ocf_f08_ocf_level_std_252d_slope_v101_signal(ncfo, closeadj):
    base = _std(ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std ncfo
def ocf_f08_ocf_level_std_252d_slope_v102_signal(ncfo, closeadj):
    base = _std(ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std ncfo
def ocf_f08_ocf_level_std_504d_slope_v103_signal(ncfo, closeadj):
    base = _std(ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std ncfo
def ocf_f08_ocf_level_std_504d_slope_v104_signal(ncfo, closeadj):
    base = _std(ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std ncfo
def ocf_f08_ocf_level_std_504d_slope_v105_signal(ncfo, closeadj):
    base = _std(ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm ncfo
def ocf_f08_ocf_level_ewm_21d_slope_v106_signal(ncfo, closeadj):
    base = ncfo.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm ncfo
def ocf_f08_ocf_level_ewm_21d_slope_v107_signal(ncfo, closeadj):
    base = ncfo.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm ncfo
def ocf_f08_ocf_level_ewm_21d_slope_v108_signal(ncfo, closeadj):
    base = ncfo.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm ncfo
def ocf_f08_ocf_level_ewm_63d_slope_v109_signal(ncfo, closeadj):
    base = ncfo.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm ncfo
def ocf_f08_ocf_level_ewm_63d_slope_v110_signal(ncfo, closeadj):
    base = ncfo.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm ncfo
def ocf_f08_ocf_level_ewm_63d_slope_v111_signal(ncfo, closeadj):
    base = ncfo.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm ncfo
def ocf_f08_ocf_level_ewm_126d_slope_v112_signal(ncfo, closeadj):
    base = ncfo.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm ncfo
def ocf_f08_ocf_level_ewm_126d_slope_v113_signal(ncfo, closeadj):
    base = ncfo.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm ncfo
def ocf_f08_ocf_level_ewm_126d_slope_v114_signal(ncfo, closeadj):
    base = ncfo.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm ncfo
def ocf_f08_ocf_level_ewm_252d_slope_v115_signal(ncfo, closeadj):
    base = ncfo.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm ncfo
def ocf_f08_ocf_level_ewm_252d_slope_v116_signal(ncfo, closeadj):
    base = ncfo.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm ncfo
def ocf_f08_ocf_level_ewm_252d_slope_v117_signal(ncfo, closeadj):
    base = ncfo.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm ncfo
def ocf_f08_ocf_level_ewm_504d_slope_v118_signal(ncfo, closeadj):
    base = ncfo.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm ncfo
def ocf_f08_ocf_level_ewm_504d_slope_v119_signal(ncfo, closeadj):
    base = ncfo.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm ncfo
def ocf_f08_ocf_level_ewm_504d_slope_v120_signal(ncfo, closeadj):
    base = ncfo.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq ncfo
def ocf_f08_ocf_level_sq_21d_slope_v121_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq ncfo
def ocf_f08_ocf_level_sq_21d_slope_v122_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq ncfo
def ocf_f08_ocf_level_sq_21d_slope_v123_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq ncfo
def ocf_f08_ocf_level_sq_63d_slope_v124_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq ncfo
def ocf_f08_ocf_level_sq_63d_slope_v125_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq ncfo
def ocf_f08_ocf_level_sq_63d_slope_v126_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq ncfo
def ocf_f08_ocf_level_sq_126d_slope_v127_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq ncfo
def ocf_f08_ocf_level_sq_126d_slope_v128_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq ncfo
def ocf_f08_ocf_level_sq_126d_slope_v129_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq ncfo
def ocf_f08_ocf_level_sq_252d_slope_v130_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq ncfo
def ocf_f08_ocf_level_sq_252d_slope_v131_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq ncfo
def ocf_f08_ocf_level_sq_252d_slope_v132_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq ncfo
def ocf_f08_ocf_level_sq_504d_slope_v133_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq ncfo
def ocf_f08_ocf_level_sq_504d_slope_v134_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq ncfo
def ocf_f08_ocf_level_sq_504d_slope_v135_signal(ncfo, closeadj):
    base = _mean(ncfo * ncfo, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z ncfo
def ocf_f08_ocf_level_z_21d_slope_v136_signal(ncfo):
    base = _z(ncfo, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z ncfo
def ocf_f08_ocf_level_z_21d_slope_v137_signal(ncfo):
    base = _z(ncfo, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z ncfo
def ocf_f08_ocf_level_z_21d_slope_v138_signal(ncfo):
    base = _z(ncfo, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z ncfo
def ocf_f08_ocf_level_z_63d_slope_v139_signal(ncfo):
    base = _z(ncfo, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z ncfo
def ocf_f08_ocf_level_z_63d_slope_v140_signal(ncfo):
    base = _z(ncfo, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z ncfo
def ocf_f08_ocf_level_z_63d_slope_v141_signal(ncfo):
    base = _z(ncfo, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z ncfo
def ocf_f08_ocf_level_z_126d_slope_v142_signal(ncfo):
    base = _z(ncfo, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z ncfo
def ocf_f08_ocf_level_z_126d_slope_v143_signal(ncfo):
    base = _z(ncfo, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z ncfo
def ocf_f08_ocf_level_z_126d_slope_v144_signal(ncfo):
    base = _z(ncfo, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z ncfo
def ocf_f08_ocf_level_z_252d_slope_v145_signal(ncfo):
    base = _z(ncfo, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z ncfo
def ocf_f08_ocf_level_z_252d_slope_v146_signal(ncfo):
    base = _z(ncfo, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z ncfo
def ocf_f08_ocf_level_z_252d_slope_v147_signal(ncfo):
    base = _z(ncfo, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z ncfo
def ocf_f08_ocf_level_z_504d_slope_v148_signal(ncfo):
    base = _z(ncfo, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z ncfo
def ocf_f08_ocf_level_z_504d_slope_v149_signal(ncfo):
    base = _z(ncfo, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z ncfo
def ocf_f08_ocf_level_z_504d_slope_v150_signal(ncfo):
    base = _z(ncfo, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
