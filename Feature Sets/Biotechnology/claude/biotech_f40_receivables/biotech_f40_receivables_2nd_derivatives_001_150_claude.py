"""Family f40 - Receivables level & quality  (F_BalanceSheet) | 2nd derivatives 001-150"""
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
def _receivables_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _receivables_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _receivables_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw receivables
def rec_f40_receivables_raw_21d_slope_v001_signal(receivables, closeadj):
    base = _mean(receivables, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw receivables
def rec_f40_receivables_raw_21d_slope_v002_signal(receivables, closeadj):
    base = _mean(receivables, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw receivables
def rec_f40_receivables_raw_21d_slope_v003_signal(receivables, closeadj):
    base = _mean(receivables, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw receivables
def rec_f40_receivables_raw_63d_slope_v004_signal(receivables, closeadj):
    base = _mean(receivables, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw receivables
def rec_f40_receivables_raw_63d_slope_v005_signal(receivables, closeadj):
    base = _mean(receivables, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw receivables
def rec_f40_receivables_raw_63d_slope_v006_signal(receivables, closeadj):
    base = _mean(receivables, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw receivables
def rec_f40_receivables_raw_126d_slope_v007_signal(receivables, closeadj):
    base = _mean(receivables, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw receivables
def rec_f40_receivables_raw_126d_slope_v008_signal(receivables, closeadj):
    base = _mean(receivables, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw receivables
def rec_f40_receivables_raw_126d_slope_v009_signal(receivables, closeadj):
    base = _mean(receivables, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw receivables
def rec_f40_receivables_raw_252d_slope_v010_signal(receivables, closeadj):
    base = _mean(receivables, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw receivables
def rec_f40_receivables_raw_252d_slope_v011_signal(receivables, closeadj):
    base = _mean(receivables, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw receivables
def rec_f40_receivables_raw_252d_slope_v012_signal(receivables, closeadj):
    base = _mean(receivables, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw receivables
def rec_f40_receivables_raw_504d_slope_v013_signal(receivables, closeadj):
    base = _mean(receivables, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw receivables
def rec_f40_receivables_raw_504d_slope_v014_signal(receivables, closeadj):
    base = _mean(receivables, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw receivables
def rec_f40_receivables_raw_504d_slope_v015_signal(receivables, closeadj):
    base = _mean(receivables, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log receivables
def rec_f40_receivables_log_21d_slope_v016_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log receivables
def rec_f40_receivables_log_21d_slope_v017_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log receivables
def rec_f40_receivables_log_21d_slope_v018_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log receivables
def rec_f40_receivables_log_63d_slope_v019_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log receivables
def rec_f40_receivables_log_63d_slope_v020_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log receivables
def rec_f40_receivables_log_63d_slope_v021_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log receivables
def rec_f40_receivables_log_126d_slope_v022_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log receivables
def rec_f40_receivables_log_126d_slope_v023_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log receivables
def rec_f40_receivables_log_126d_slope_v024_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log receivables
def rec_f40_receivables_log_252d_slope_v025_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log receivables
def rec_f40_receivables_log_252d_slope_v026_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log receivables
def rec_f40_receivables_log_252d_slope_v027_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log receivables
def rec_f40_receivables_log_504d_slope_v028_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log receivables
def rec_f40_receivables_log_504d_slope_v029_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log receivables
def rec_f40_receivables_log_504d_slope_v030_signal(receivables, closeadj):
    base = _mean(_receivables_log(receivables), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare receivables
def rec_f40_receivables_pershare_21d_slope_v031_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare receivables
def rec_f40_receivables_pershare_21d_slope_v032_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare receivables
def rec_f40_receivables_pershare_21d_slope_v033_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare receivables
def rec_f40_receivables_pershare_63d_slope_v034_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare receivables
def rec_f40_receivables_pershare_63d_slope_v035_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare receivables
def rec_f40_receivables_pershare_63d_slope_v036_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare receivables
def rec_f40_receivables_pershare_126d_slope_v037_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare receivables
def rec_f40_receivables_pershare_126d_slope_v038_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare receivables
def rec_f40_receivables_pershare_126d_slope_v039_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare receivables
def rec_f40_receivables_pershare_252d_slope_v040_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare receivables
def rec_f40_receivables_pershare_252d_slope_v041_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare receivables
def rec_f40_receivables_pershare_252d_slope_v042_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare receivables
def rec_f40_receivables_pershare_504d_slope_v043_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare receivables
def rec_f40_receivables_pershare_504d_slope_v044_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare receivables
def rec_f40_receivables_pershare_504d_slope_v045_signal(receivables, sharesbas, closeadj):
    base = _mean(_receivables_per_share(receivables, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets receivables
def rec_f40_receivables_per_assets_21d_slope_v046_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets receivables
def rec_f40_receivables_per_assets_21d_slope_v047_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets receivables
def rec_f40_receivables_per_assets_21d_slope_v048_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets receivables
def rec_f40_receivables_per_assets_63d_slope_v049_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets receivables
def rec_f40_receivables_per_assets_63d_slope_v050_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets receivables
def rec_f40_receivables_per_assets_63d_slope_v051_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets receivables
def rec_f40_receivables_per_assets_126d_slope_v052_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets receivables
def rec_f40_receivables_per_assets_126d_slope_v053_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets receivables
def rec_f40_receivables_per_assets_126d_slope_v054_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets receivables
def rec_f40_receivables_per_assets_252d_slope_v055_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets receivables
def rec_f40_receivables_per_assets_252d_slope_v056_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets receivables
def rec_f40_receivables_per_assets_252d_slope_v057_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets receivables
def rec_f40_receivables_per_assets_504d_slope_v058_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets receivables
def rec_f40_receivables_per_assets_504d_slope_v059_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets receivables
def rec_f40_receivables_per_assets_504d_slope_v060_signal(receivables, assets):
    base = _mean(_receivables_scaled(receivables, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap receivables
def rec_f40_receivables_per_marketcap_21d_slope_v061_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap receivables
def rec_f40_receivables_per_marketcap_21d_slope_v062_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap receivables
def rec_f40_receivables_per_marketcap_21d_slope_v063_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap receivables
def rec_f40_receivables_per_marketcap_63d_slope_v064_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap receivables
def rec_f40_receivables_per_marketcap_63d_slope_v065_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap receivables
def rec_f40_receivables_per_marketcap_63d_slope_v066_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap receivables
def rec_f40_receivables_per_marketcap_126d_slope_v067_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap receivables
def rec_f40_receivables_per_marketcap_126d_slope_v068_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap receivables
def rec_f40_receivables_per_marketcap_126d_slope_v069_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap receivables
def rec_f40_receivables_per_marketcap_252d_slope_v070_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap receivables
def rec_f40_receivables_per_marketcap_252d_slope_v071_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap receivables
def rec_f40_receivables_per_marketcap_252d_slope_v072_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap receivables
def rec_f40_receivables_per_marketcap_504d_slope_v073_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap receivables
def rec_f40_receivables_per_marketcap_504d_slope_v074_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap receivables
def rec_f40_receivables_per_marketcap_504d_slope_v075_signal(receivables, marketcap):
    base = _mean(_receivables_scaled(receivables, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity receivables
def rec_f40_receivables_per_equity_21d_slope_v076_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity receivables
def rec_f40_receivables_per_equity_21d_slope_v077_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity receivables
def rec_f40_receivables_per_equity_21d_slope_v078_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity receivables
def rec_f40_receivables_per_equity_63d_slope_v079_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity receivables
def rec_f40_receivables_per_equity_63d_slope_v080_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity receivables
def rec_f40_receivables_per_equity_63d_slope_v081_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity receivables
def rec_f40_receivables_per_equity_126d_slope_v082_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity receivables
def rec_f40_receivables_per_equity_126d_slope_v083_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity receivables
def rec_f40_receivables_per_equity_126d_slope_v084_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity receivables
def rec_f40_receivables_per_equity_252d_slope_v085_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity receivables
def rec_f40_receivables_per_equity_252d_slope_v086_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity receivables
def rec_f40_receivables_per_equity_252d_slope_v087_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity receivables
def rec_f40_receivables_per_equity_504d_slope_v088_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity receivables
def rec_f40_receivables_per_equity_504d_slope_v089_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity receivables
def rec_f40_receivables_per_equity_504d_slope_v090_signal(receivables, equity):
    base = _mean(_receivables_scaled(receivables, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std receivables
def rec_f40_receivables_std_21d_slope_v091_signal(receivables, closeadj):
    base = _std(receivables, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std receivables
def rec_f40_receivables_std_21d_slope_v092_signal(receivables, closeadj):
    base = _std(receivables, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std receivables
def rec_f40_receivables_std_21d_slope_v093_signal(receivables, closeadj):
    base = _std(receivables, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std receivables
def rec_f40_receivables_std_63d_slope_v094_signal(receivables, closeadj):
    base = _std(receivables, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std receivables
def rec_f40_receivables_std_63d_slope_v095_signal(receivables, closeadj):
    base = _std(receivables, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std receivables
def rec_f40_receivables_std_63d_slope_v096_signal(receivables, closeadj):
    base = _std(receivables, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std receivables
def rec_f40_receivables_std_126d_slope_v097_signal(receivables, closeadj):
    base = _std(receivables, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std receivables
def rec_f40_receivables_std_126d_slope_v098_signal(receivables, closeadj):
    base = _std(receivables, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std receivables
def rec_f40_receivables_std_126d_slope_v099_signal(receivables, closeadj):
    base = _std(receivables, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std receivables
def rec_f40_receivables_std_252d_slope_v100_signal(receivables, closeadj):
    base = _std(receivables, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std receivables
def rec_f40_receivables_std_252d_slope_v101_signal(receivables, closeadj):
    base = _std(receivables, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std receivables
def rec_f40_receivables_std_252d_slope_v102_signal(receivables, closeadj):
    base = _std(receivables, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std receivables
def rec_f40_receivables_std_504d_slope_v103_signal(receivables, closeadj):
    base = _std(receivables, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std receivables
def rec_f40_receivables_std_504d_slope_v104_signal(receivables, closeadj):
    base = _std(receivables, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std receivables
def rec_f40_receivables_std_504d_slope_v105_signal(receivables, closeadj):
    base = _std(receivables, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm receivables
def rec_f40_receivables_ewm_21d_slope_v106_signal(receivables, closeadj):
    base = receivables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm receivables
def rec_f40_receivables_ewm_21d_slope_v107_signal(receivables, closeadj):
    base = receivables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm receivables
def rec_f40_receivables_ewm_21d_slope_v108_signal(receivables, closeadj):
    base = receivables.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm receivables
def rec_f40_receivables_ewm_63d_slope_v109_signal(receivables, closeadj):
    base = receivables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm receivables
def rec_f40_receivables_ewm_63d_slope_v110_signal(receivables, closeadj):
    base = receivables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm receivables
def rec_f40_receivables_ewm_63d_slope_v111_signal(receivables, closeadj):
    base = receivables.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm receivables
def rec_f40_receivables_ewm_126d_slope_v112_signal(receivables, closeadj):
    base = receivables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm receivables
def rec_f40_receivables_ewm_126d_slope_v113_signal(receivables, closeadj):
    base = receivables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm receivables
def rec_f40_receivables_ewm_126d_slope_v114_signal(receivables, closeadj):
    base = receivables.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm receivables
def rec_f40_receivables_ewm_252d_slope_v115_signal(receivables, closeadj):
    base = receivables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm receivables
def rec_f40_receivables_ewm_252d_slope_v116_signal(receivables, closeadj):
    base = receivables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm receivables
def rec_f40_receivables_ewm_252d_slope_v117_signal(receivables, closeadj):
    base = receivables.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm receivables
def rec_f40_receivables_ewm_504d_slope_v118_signal(receivables, closeadj):
    base = receivables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm receivables
def rec_f40_receivables_ewm_504d_slope_v119_signal(receivables, closeadj):
    base = receivables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm receivables
def rec_f40_receivables_ewm_504d_slope_v120_signal(receivables, closeadj):
    base = receivables.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq receivables
def rec_f40_receivables_sq_21d_slope_v121_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq receivables
def rec_f40_receivables_sq_21d_slope_v122_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq receivables
def rec_f40_receivables_sq_21d_slope_v123_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq receivables
def rec_f40_receivables_sq_63d_slope_v124_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq receivables
def rec_f40_receivables_sq_63d_slope_v125_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq receivables
def rec_f40_receivables_sq_63d_slope_v126_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq receivables
def rec_f40_receivables_sq_126d_slope_v127_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq receivables
def rec_f40_receivables_sq_126d_slope_v128_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq receivables
def rec_f40_receivables_sq_126d_slope_v129_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq receivables
def rec_f40_receivables_sq_252d_slope_v130_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq receivables
def rec_f40_receivables_sq_252d_slope_v131_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq receivables
def rec_f40_receivables_sq_252d_slope_v132_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq receivables
def rec_f40_receivables_sq_504d_slope_v133_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq receivables
def rec_f40_receivables_sq_504d_slope_v134_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq receivables
def rec_f40_receivables_sq_504d_slope_v135_signal(receivables, closeadj):
    base = _mean(receivables * receivables, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z receivables
def rec_f40_receivables_z_21d_slope_v136_signal(receivables):
    base = _z(receivables, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z receivables
def rec_f40_receivables_z_21d_slope_v137_signal(receivables):
    base = _z(receivables, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z receivables
def rec_f40_receivables_z_21d_slope_v138_signal(receivables):
    base = _z(receivables, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z receivables
def rec_f40_receivables_z_63d_slope_v139_signal(receivables):
    base = _z(receivables, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z receivables
def rec_f40_receivables_z_63d_slope_v140_signal(receivables):
    base = _z(receivables, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z receivables
def rec_f40_receivables_z_63d_slope_v141_signal(receivables):
    base = _z(receivables, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z receivables
def rec_f40_receivables_z_126d_slope_v142_signal(receivables):
    base = _z(receivables, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z receivables
def rec_f40_receivables_z_126d_slope_v143_signal(receivables):
    base = _z(receivables, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z receivables
def rec_f40_receivables_z_126d_slope_v144_signal(receivables):
    base = _z(receivables, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z receivables
def rec_f40_receivables_z_252d_slope_v145_signal(receivables):
    base = _z(receivables, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z receivables
def rec_f40_receivables_z_252d_slope_v146_signal(receivables):
    base = _z(receivables, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z receivables
def rec_f40_receivables_z_252d_slope_v147_signal(receivables):
    base = _z(receivables, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z receivables
def rec_f40_receivables_z_504d_slope_v148_signal(receivables):
    base = _z(receivables, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z receivables
def rec_f40_receivables_z_504d_slope_v149_signal(receivables):
    base = _z(receivables, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z receivables
def rec_f40_receivables_z_504d_slope_v150_signal(receivables):
    base = _z(receivables, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
