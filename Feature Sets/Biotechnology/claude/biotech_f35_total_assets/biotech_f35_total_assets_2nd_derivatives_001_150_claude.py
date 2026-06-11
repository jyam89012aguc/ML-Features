"""Family f35 - Total assets level & growth  (F_BalanceSheet) | 2nd derivatives 001-150"""
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
def _total_assets_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _total_assets_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _total_assets_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw assets
def ta_f35_total_assets_raw_21d_slope_v001_signal(assets, closeadj):
    base = _mean(assets, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw assets
def ta_f35_total_assets_raw_21d_slope_v002_signal(assets, closeadj):
    base = _mean(assets, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw assets
def ta_f35_total_assets_raw_21d_slope_v003_signal(assets, closeadj):
    base = _mean(assets, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw assets
def ta_f35_total_assets_raw_63d_slope_v004_signal(assets, closeadj):
    base = _mean(assets, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw assets
def ta_f35_total_assets_raw_63d_slope_v005_signal(assets, closeadj):
    base = _mean(assets, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw assets
def ta_f35_total_assets_raw_63d_slope_v006_signal(assets, closeadj):
    base = _mean(assets, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw assets
def ta_f35_total_assets_raw_126d_slope_v007_signal(assets, closeadj):
    base = _mean(assets, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw assets
def ta_f35_total_assets_raw_126d_slope_v008_signal(assets, closeadj):
    base = _mean(assets, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw assets
def ta_f35_total_assets_raw_126d_slope_v009_signal(assets, closeadj):
    base = _mean(assets, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw assets
def ta_f35_total_assets_raw_252d_slope_v010_signal(assets, closeadj):
    base = _mean(assets, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw assets
def ta_f35_total_assets_raw_252d_slope_v011_signal(assets, closeadj):
    base = _mean(assets, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw assets
def ta_f35_total_assets_raw_252d_slope_v012_signal(assets, closeadj):
    base = _mean(assets, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw assets
def ta_f35_total_assets_raw_504d_slope_v013_signal(assets, closeadj):
    base = _mean(assets, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw assets
def ta_f35_total_assets_raw_504d_slope_v014_signal(assets, closeadj):
    base = _mean(assets, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw assets
def ta_f35_total_assets_raw_504d_slope_v015_signal(assets, closeadj):
    base = _mean(assets, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log assets
def ta_f35_total_assets_log_21d_slope_v016_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log assets
def ta_f35_total_assets_log_21d_slope_v017_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log assets
def ta_f35_total_assets_log_21d_slope_v018_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log assets
def ta_f35_total_assets_log_63d_slope_v019_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log assets
def ta_f35_total_assets_log_63d_slope_v020_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log assets
def ta_f35_total_assets_log_63d_slope_v021_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log assets
def ta_f35_total_assets_log_126d_slope_v022_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log assets
def ta_f35_total_assets_log_126d_slope_v023_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log assets
def ta_f35_total_assets_log_126d_slope_v024_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log assets
def ta_f35_total_assets_log_252d_slope_v025_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log assets
def ta_f35_total_assets_log_252d_slope_v026_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log assets
def ta_f35_total_assets_log_252d_slope_v027_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log assets
def ta_f35_total_assets_log_504d_slope_v028_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log assets
def ta_f35_total_assets_log_504d_slope_v029_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log assets
def ta_f35_total_assets_log_504d_slope_v030_signal(assets, closeadj):
    base = _mean(_total_assets_log(assets), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare assets
def ta_f35_total_assets_pershare_21d_slope_v031_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare assets
def ta_f35_total_assets_pershare_21d_slope_v032_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare assets
def ta_f35_total_assets_pershare_21d_slope_v033_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare assets
def ta_f35_total_assets_pershare_63d_slope_v034_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare assets
def ta_f35_total_assets_pershare_63d_slope_v035_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare assets
def ta_f35_total_assets_pershare_63d_slope_v036_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare assets
def ta_f35_total_assets_pershare_126d_slope_v037_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare assets
def ta_f35_total_assets_pershare_126d_slope_v038_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare assets
def ta_f35_total_assets_pershare_126d_slope_v039_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare assets
def ta_f35_total_assets_pershare_252d_slope_v040_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare assets
def ta_f35_total_assets_pershare_252d_slope_v041_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare assets
def ta_f35_total_assets_pershare_252d_slope_v042_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare assets
def ta_f35_total_assets_pershare_504d_slope_v043_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare assets
def ta_f35_total_assets_pershare_504d_slope_v044_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare assets
def ta_f35_total_assets_pershare_504d_slope_v045_signal(assets, sharesbas, closeadj):
    base = _mean(_total_assets_per_share(assets, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets assets
def ta_f35_total_assets_per_assets_21d_slope_v046_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets assets
def ta_f35_total_assets_per_assets_21d_slope_v047_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets assets
def ta_f35_total_assets_per_assets_21d_slope_v048_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets assets
def ta_f35_total_assets_per_assets_63d_slope_v049_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets assets
def ta_f35_total_assets_per_assets_63d_slope_v050_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets assets
def ta_f35_total_assets_per_assets_63d_slope_v051_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets assets
def ta_f35_total_assets_per_assets_126d_slope_v052_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets assets
def ta_f35_total_assets_per_assets_126d_slope_v053_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets assets
def ta_f35_total_assets_per_assets_126d_slope_v054_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets assets
def ta_f35_total_assets_per_assets_252d_slope_v055_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets assets
def ta_f35_total_assets_per_assets_252d_slope_v056_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets assets
def ta_f35_total_assets_per_assets_252d_slope_v057_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets assets
def ta_f35_total_assets_per_assets_504d_slope_v058_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets assets
def ta_f35_total_assets_per_assets_504d_slope_v059_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets assets
def ta_f35_total_assets_per_assets_504d_slope_v060_signal(assets):
    base = _mean(_total_assets_scaled(assets, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap assets
def ta_f35_total_assets_per_marketcap_21d_slope_v061_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap assets
def ta_f35_total_assets_per_marketcap_21d_slope_v062_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap assets
def ta_f35_total_assets_per_marketcap_21d_slope_v063_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap assets
def ta_f35_total_assets_per_marketcap_63d_slope_v064_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap assets
def ta_f35_total_assets_per_marketcap_63d_slope_v065_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap assets
def ta_f35_total_assets_per_marketcap_63d_slope_v066_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap assets
def ta_f35_total_assets_per_marketcap_126d_slope_v067_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap assets
def ta_f35_total_assets_per_marketcap_126d_slope_v068_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap assets
def ta_f35_total_assets_per_marketcap_126d_slope_v069_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap assets
def ta_f35_total_assets_per_marketcap_252d_slope_v070_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap assets
def ta_f35_total_assets_per_marketcap_252d_slope_v071_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap assets
def ta_f35_total_assets_per_marketcap_252d_slope_v072_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap assets
def ta_f35_total_assets_per_marketcap_504d_slope_v073_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap assets
def ta_f35_total_assets_per_marketcap_504d_slope_v074_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap assets
def ta_f35_total_assets_per_marketcap_504d_slope_v075_signal(assets, marketcap):
    base = _mean(_total_assets_scaled(assets, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity assets
def ta_f35_total_assets_per_equity_21d_slope_v076_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity assets
def ta_f35_total_assets_per_equity_21d_slope_v077_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity assets
def ta_f35_total_assets_per_equity_21d_slope_v078_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity assets
def ta_f35_total_assets_per_equity_63d_slope_v079_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity assets
def ta_f35_total_assets_per_equity_63d_slope_v080_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity assets
def ta_f35_total_assets_per_equity_63d_slope_v081_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity assets
def ta_f35_total_assets_per_equity_126d_slope_v082_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity assets
def ta_f35_total_assets_per_equity_126d_slope_v083_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity assets
def ta_f35_total_assets_per_equity_126d_slope_v084_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity assets
def ta_f35_total_assets_per_equity_252d_slope_v085_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity assets
def ta_f35_total_assets_per_equity_252d_slope_v086_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity assets
def ta_f35_total_assets_per_equity_252d_slope_v087_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity assets
def ta_f35_total_assets_per_equity_504d_slope_v088_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity assets
def ta_f35_total_assets_per_equity_504d_slope_v089_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity assets
def ta_f35_total_assets_per_equity_504d_slope_v090_signal(assets, equity):
    base = _mean(_total_assets_scaled(assets, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std assets
def ta_f35_total_assets_std_21d_slope_v091_signal(assets, closeadj):
    base = _std(assets, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std assets
def ta_f35_total_assets_std_21d_slope_v092_signal(assets, closeadj):
    base = _std(assets, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std assets
def ta_f35_total_assets_std_21d_slope_v093_signal(assets, closeadj):
    base = _std(assets, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std assets
def ta_f35_total_assets_std_63d_slope_v094_signal(assets, closeadj):
    base = _std(assets, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std assets
def ta_f35_total_assets_std_63d_slope_v095_signal(assets, closeadj):
    base = _std(assets, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std assets
def ta_f35_total_assets_std_63d_slope_v096_signal(assets, closeadj):
    base = _std(assets, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std assets
def ta_f35_total_assets_std_126d_slope_v097_signal(assets, closeadj):
    base = _std(assets, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std assets
def ta_f35_total_assets_std_126d_slope_v098_signal(assets, closeadj):
    base = _std(assets, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std assets
def ta_f35_total_assets_std_126d_slope_v099_signal(assets, closeadj):
    base = _std(assets, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std assets
def ta_f35_total_assets_std_252d_slope_v100_signal(assets, closeadj):
    base = _std(assets, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std assets
def ta_f35_total_assets_std_252d_slope_v101_signal(assets, closeadj):
    base = _std(assets, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std assets
def ta_f35_total_assets_std_252d_slope_v102_signal(assets, closeadj):
    base = _std(assets, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std assets
def ta_f35_total_assets_std_504d_slope_v103_signal(assets, closeadj):
    base = _std(assets, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std assets
def ta_f35_total_assets_std_504d_slope_v104_signal(assets, closeadj):
    base = _std(assets, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std assets
def ta_f35_total_assets_std_504d_slope_v105_signal(assets, closeadj):
    base = _std(assets, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm assets
def ta_f35_total_assets_ewm_21d_slope_v106_signal(assets, closeadj):
    base = assets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm assets
def ta_f35_total_assets_ewm_21d_slope_v107_signal(assets, closeadj):
    base = assets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm assets
def ta_f35_total_assets_ewm_21d_slope_v108_signal(assets, closeadj):
    base = assets.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm assets
def ta_f35_total_assets_ewm_63d_slope_v109_signal(assets, closeadj):
    base = assets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm assets
def ta_f35_total_assets_ewm_63d_slope_v110_signal(assets, closeadj):
    base = assets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm assets
def ta_f35_total_assets_ewm_63d_slope_v111_signal(assets, closeadj):
    base = assets.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm assets
def ta_f35_total_assets_ewm_126d_slope_v112_signal(assets, closeadj):
    base = assets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm assets
def ta_f35_total_assets_ewm_126d_slope_v113_signal(assets, closeadj):
    base = assets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm assets
def ta_f35_total_assets_ewm_126d_slope_v114_signal(assets, closeadj):
    base = assets.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm assets
def ta_f35_total_assets_ewm_252d_slope_v115_signal(assets, closeadj):
    base = assets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm assets
def ta_f35_total_assets_ewm_252d_slope_v116_signal(assets, closeadj):
    base = assets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm assets
def ta_f35_total_assets_ewm_252d_slope_v117_signal(assets, closeadj):
    base = assets.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm assets
def ta_f35_total_assets_ewm_504d_slope_v118_signal(assets, closeadj):
    base = assets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm assets
def ta_f35_total_assets_ewm_504d_slope_v119_signal(assets, closeadj):
    base = assets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm assets
def ta_f35_total_assets_ewm_504d_slope_v120_signal(assets, closeadj):
    base = assets.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq assets
def ta_f35_total_assets_sq_21d_slope_v121_signal(assets, closeadj):
    base = _mean(assets * assets, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq assets
def ta_f35_total_assets_sq_21d_slope_v122_signal(assets, closeadj):
    base = _mean(assets * assets, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq assets
def ta_f35_total_assets_sq_21d_slope_v123_signal(assets, closeadj):
    base = _mean(assets * assets, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq assets
def ta_f35_total_assets_sq_63d_slope_v124_signal(assets, closeadj):
    base = _mean(assets * assets, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq assets
def ta_f35_total_assets_sq_63d_slope_v125_signal(assets, closeadj):
    base = _mean(assets * assets, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq assets
def ta_f35_total_assets_sq_63d_slope_v126_signal(assets, closeadj):
    base = _mean(assets * assets, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq assets
def ta_f35_total_assets_sq_126d_slope_v127_signal(assets, closeadj):
    base = _mean(assets * assets, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq assets
def ta_f35_total_assets_sq_126d_slope_v128_signal(assets, closeadj):
    base = _mean(assets * assets, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq assets
def ta_f35_total_assets_sq_126d_slope_v129_signal(assets, closeadj):
    base = _mean(assets * assets, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq assets
def ta_f35_total_assets_sq_252d_slope_v130_signal(assets, closeadj):
    base = _mean(assets * assets, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq assets
def ta_f35_total_assets_sq_252d_slope_v131_signal(assets, closeadj):
    base = _mean(assets * assets, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq assets
def ta_f35_total_assets_sq_252d_slope_v132_signal(assets, closeadj):
    base = _mean(assets * assets, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq assets
def ta_f35_total_assets_sq_504d_slope_v133_signal(assets, closeadj):
    base = _mean(assets * assets, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq assets
def ta_f35_total_assets_sq_504d_slope_v134_signal(assets, closeadj):
    base = _mean(assets * assets, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq assets
def ta_f35_total_assets_sq_504d_slope_v135_signal(assets, closeadj):
    base = _mean(assets * assets, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z assets
def ta_f35_total_assets_z_21d_slope_v136_signal(assets):
    base = _z(assets, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z assets
def ta_f35_total_assets_z_21d_slope_v137_signal(assets):
    base = _z(assets, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z assets
def ta_f35_total_assets_z_21d_slope_v138_signal(assets):
    base = _z(assets, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z assets
def ta_f35_total_assets_z_63d_slope_v139_signal(assets):
    base = _z(assets, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z assets
def ta_f35_total_assets_z_63d_slope_v140_signal(assets):
    base = _z(assets, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z assets
def ta_f35_total_assets_z_63d_slope_v141_signal(assets):
    base = _z(assets, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z assets
def ta_f35_total_assets_z_126d_slope_v142_signal(assets):
    base = _z(assets, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z assets
def ta_f35_total_assets_z_126d_slope_v143_signal(assets):
    base = _z(assets, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z assets
def ta_f35_total_assets_z_126d_slope_v144_signal(assets):
    base = _z(assets, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z assets
def ta_f35_total_assets_z_252d_slope_v145_signal(assets):
    base = _z(assets, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z assets
def ta_f35_total_assets_z_252d_slope_v146_signal(assets):
    base = _z(assets, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z assets
def ta_f35_total_assets_z_252d_slope_v147_signal(assets):
    base = _z(assets, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z assets
def ta_f35_total_assets_z_504d_slope_v148_signal(assets):
    base = _z(assets, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z assets
def ta_f35_total_assets_z_504d_slope_v149_signal(assets):
    base = _z(assets, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z assets
def ta_f35_total_assets_z_504d_slope_v150_signal(assets):
    base = _z(assets, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
