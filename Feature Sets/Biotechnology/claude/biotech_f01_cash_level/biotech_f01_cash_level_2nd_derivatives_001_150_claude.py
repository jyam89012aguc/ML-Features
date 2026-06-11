"""Family f01 - Cash & equivalents level  (A_Liquidity_Runway) | 2nd derivatives 001-150"""
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
def _cash_level_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _cash_level_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _cash_level_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw cashneq
def cl_f01_cash_level_raw_21d_slope_v001_signal(cashneq, closeadj):
    base = _mean(cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw cashneq
def cl_f01_cash_level_raw_21d_slope_v002_signal(cashneq, closeadj):
    base = _mean(cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw cashneq
def cl_f01_cash_level_raw_21d_slope_v003_signal(cashneq, closeadj):
    base = _mean(cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw cashneq
def cl_f01_cash_level_raw_63d_slope_v004_signal(cashneq, closeadj):
    base = _mean(cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw cashneq
def cl_f01_cash_level_raw_63d_slope_v005_signal(cashneq, closeadj):
    base = _mean(cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw cashneq
def cl_f01_cash_level_raw_63d_slope_v006_signal(cashneq, closeadj):
    base = _mean(cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw cashneq
def cl_f01_cash_level_raw_126d_slope_v007_signal(cashneq, closeadj):
    base = _mean(cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw cashneq
def cl_f01_cash_level_raw_126d_slope_v008_signal(cashneq, closeadj):
    base = _mean(cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw cashneq
def cl_f01_cash_level_raw_126d_slope_v009_signal(cashneq, closeadj):
    base = _mean(cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw cashneq
def cl_f01_cash_level_raw_252d_slope_v010_signal(cashneq, closeadj):
    base = _mean(cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw cashneq
def cl_f01_cash_level_raw_252d_slope_v011_signal(cashneq, closeadj):
    base = _mean(cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw cashneq
def cl_f01_cash_level_raw_252d_slope_v012_signal(cashneq, closeadj):
    base = _mean(cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw cashneq
def cl_f01_cash_level_raw_504d_slope_v013_signal(cashneq, closeadj):
    base = _mean(cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw cashneq
def cl_f01_cash_level_raw_504d_slope_v014_signal(cashneq, closeadj):
    base = _mean(cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw cashneq
def cl_f01_cash_level_raw_504d_slope_v015_signal(cashneq, closeadj):
    base = _mean(cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log cashneq
def cl_f01_cash_level_log_21d_slope_v016_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log cashneq
def cl_f01_cash_level_log_21d_slope_v017_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log cashneq
def cl_f01_cash_level_log_21d_slope_v018_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log cashneq
def cl_f01_cash_level_log_63d_slope_v019_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log cashneq
def cl_f01_cash_level_log_63d_slope_v020_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log cashneq
def cl_f01_cash_level_log_63d_slope_v021_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log cashneq
def cl_f01_cash_level_log_126d_slope_v022_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log cashneq
def cl_f01_cash_level_log_126d_slope_v023_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log cashneq
def cl_f01_cash_level_log_126d_slope_v024_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log cashneq
def cl_f01_cash_level_log_252d_slope_v025_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log cashneq
def cl_f01_cash_level_log_252d_slope_v026_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log cashneq
def cl_f01_cash_level_log_252d_slope_v027_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log cashneq
def cl_f01_cash_level_log_504d_slope_v028_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log cashneq
def cl_f01_cash_level_log_504d_slope_v029_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log cashneq
def cl_f01_cash_level_log_504d_slope_v030_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare cashneq
def cl_f01_cash_level_pershare_21d_slope_v031_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare cashneq
def cl_f01_cash_level_pershare_21d_slope_v032_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare cashneq
def cl_f01_cash_level_pershare_21d_slope_v033_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare cashneq
def cl_f01_cash_level_pershare_63d_slope_v034_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare cashneq
def cl_f01_cash_level_pershare_63d_slope_v035_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare cashneq
def cl_f01_cash_level_pershare_63d_slope_v036_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare cashneq
def cl_f01_cash_level_pershare_126d_slope_v037_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare cashneq
def cl_f01_cash_level_pershare_126d_slope_v038_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare cashneq
def cl_f01_cash_level_pershare_126d_slope_v039_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare cashneq
def cl_f01_cash_level_pershare_252d_slope_v040_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare cashneq
def cl_f01_cash_level_pershare_252d_slope_v041_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare cashneq
def cl_f01_cash_level_pershare_252d_slope_v042_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare cashneq
def cl_f01_cash_level_pershare_504d_slope_v043_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare cashneq
def cl_f01_cash_level_pershare_504d_slope_v044_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare cashneq
def cl_f01_cash_level_pershare_504d_slope_v045_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets cashneq
def cl_f01_cash_level_per_assets_21d_slope_v046_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets cashneq
def cl_f01_cash_level_per_assets_21d_slope_v047_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets cashneq
def cl_f01_cash_level_per_assets_21d_slope_v048_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets cashneq
def cl_f01_cash_level_per_assets_63d_slope_v049_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets cashneq
def cl_f01_cash_level_per_assets_63d_slope_v050_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets cashneq
def cl_f01_cash_level_per_assets_63d_slope_v051_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets cashneq
def cl_f01_cash_level_per_assets_126d_slope_v052_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets cashneq
def cl_f01_cash_level_per_assets_126d_slope_v053_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets cashneq
def cl_f01_cash_level_per_assets_126d_slope_v054_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets cashneq
def cl_f01_cash_level_per_assets_252d_slope_v055_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets cashneq
def cl_f01_cash_level_per_assets_252d_slope_v056_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets cashneq
def cl_f01_cash_level_per_assets_252d_slope_v057_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets cashneq
def cl_f01_cash_level_per_assets_504d_slope_v058_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets cashneq
def cl_f01_cash_level_per_assets_504d_slope_v059_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets cashneq
def cl_f01_cash_level_per_assets_504d_slope_v060_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_21d_slope_v061_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_21d_slope_v062_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_21d_slope_v063_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_63d_slope_v064_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_63d_slope_v065_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_63d_slope_v066_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_126d_slope_v067_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_126d_slope_v068_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_126d_slope_v069_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_252d_slope_v070_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_252d_slope_v071_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_252d_slope_v072_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_504d_slope_v073_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_504d_slope_v074_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_504d_slope_v075_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity cashneq
def cl_f01_cash_level_per_equity_21d_slope_v076_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity cashneq
def cl_f01_cash_level_per_equity_21d_slope_v077_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity cashneq
def cl_f01_cash_level_per_equity_21d_slope_v078_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity cashneq
def cl_f01_cash_level_per_equity_63d_slope_v079_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity cashneq
def cl_f01_cash_level_per_equity_63d_slope_v080_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity cashneq
def cl_f01_cash_level_per_equity_63d_slope_v081_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity cashneq
def cl_f01_cash_level_per_equity_126d_slope_v082_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity cashneq
def cl_f01_cash_level_per_equity_126d_slope_v083_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity cashneq
def cl_f01_cash_level_per_equity_126d_slope_v084_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity cashneq
def cl_f01_cash_level_per_equity_252d_slope_v085_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity cashneq
def cl_f01_cash_level_per_equity_252d_slope_v086_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity cashneq
def cl_f01_cash_level_per_equity_252d_slope_v087_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity cashneq
def cl_f01_cash_level_per_equity_504d_slope_v088_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity cashneq
def cl_f01_cash_level_per_equity_504d_slope_v089_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity cashneq
def cl_f01_cash_level_per_equity_504d_slope_v090_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std cashneq
def cl_f01_cash_level_std_21d_slope_v091_signal(cashneq, closeadj):
    base = _std(cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std cashneq
def cl_f01_cash_level_std_21d_slope_v092_signal(cashneq, closeadj):
    base = _std(cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std cashneq
def cl_f01_cash_level_std_21d_slope_v093_signal(cashneq, closeadj):
    base = _std(cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std cashneq
def cl_f01_cash_level_std_63d_slope_v094_signal(cashneq, closeadj):
    base = _std(cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std cashneq
def cl_f01_cash_level_std_63d_slope_v095_signal(cashneq, closeadj):
    base = _std(cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std cashneq
def cl_f01_cash_level_std_63d_slope_v096_signal(cashneq, closeadj):
    base = _std(cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std cashneq
def cl_f01_cash_level_std_126d_slope_v097_signal(cashneq, closeadj):
    base = _std(cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std cashneq
def cl_f01_cash_level_std_126d_slope_v098_signal(cashneq, closeadj):
    base = _std(cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std cashneq
def cl_f01_cash_level_std_126d_slope_v099_signal(cashneq, closeadj):
    base = _std(cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std cashneq
def cl_f01_cash_level_std_252d_slope_v100_signal(cashneq, closeadj):
    base = _std(cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std cashneq
def cl_f01_cash_level_std_252d_slope_v101_signal(cashneq, closeadj):
    base = _std(cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std cashneq
def cl_f01_cash_level_std_252d_slope_v102_signal(cashneq, closeadj):
    base = _std(cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std cashneq
def cl_f01_cash_level_std_504d_slope_v103_signal(cashneq, closeadj):
    base = _std(cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std cashneq
def cl_f01_cash_level_std_504d_slope_v104_signal(cashneq, closeadj):
    base = _std(cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std cashneq
def cl_f01_cash_level_std_504d_slope_v105_signal(cashneq, closeadj):
    base = _std(cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm cashneq
def cl_f01_cash_level_ewm_21d_slope_v106_signal(cashneq, closeadj):
    base = cashneq.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm cashneq
def cl_f01_cash_level_ewm_21d_slope_v107_signal(cashneq, closeadj):
    base = cashneq.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm cashneq
def cl_f01_cash_level_ewm_21d_slope_v108_signal(cashneq, closeadj):
    base = cashneq.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm cashneq
def cl_f01_cash_level_ewm_63d_slope_v109_signal(cashneq, closeadj):
    base = cashneq.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm cashneq
def cl_f01_cash_level_ewm_63d_slope_v110_signal(cashneq, closeadj):
    base = cashneq.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm cashneq
def cl_f01_cash_level_ewm_63d_slope_v111_signal(cashneq, closeadj):
    base = cashneq.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm cashneq
def cl_f01_cash_level_ewm_126d_slope_v112_signal(cashneq, closeadj):
    base = cashneq.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm cashneq
def cl_f01_cash_level_ewm_126d_slope_v113_signal(cashneq, closeadj):
    base = cashneq.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm cashneq
def cl_f01_cash_level_ewm_126d_slope_v114_signal(cashneq, closeadj):
    base = cashneq.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm cashneq
def cl_f01_cash_level_ewm_252d_slope_v115_signal(cashneq, closeadj):
    base = cashneq.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm cashneq
def cl_f01_cash_level_ewm_252d_slope_v116_signal(cashneq, closeadj):
    base = cashneq.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm cashneq
def cl_f01_cash_level_ewm_252d_slope_v117_signal(cashneq, closeadj):
    base = cashneq.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm cashneq
def cl_f01_cash_level_ewm_504d_slope_v118_signal(cashneq, closeadj):
    base = cashneq.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm cashneq
def cl_f01_cash_level_ewm_504d_slope_v119_signal(cashneq, closeadj):
    base = cashneq.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm cashneq
def cl_f01_cash_level_ewm_504d_slope_v120_signal(cashneq, closeadj):
    base = cashneq.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq cashneq
def cl_f01_cash_level_sq_21d_slope_v121_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq cashneq
def cl_f01_cash_level_sq_21d_slope_v122_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq cashneq
def cl_f01_cash_level_sq_21d_slope_v123_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq cashneq
def cl_f01_cash_level_sq_63d_slope_v124_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq cashneq
def cl_f01_cash_level_sq_63d_slope_v125_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq cashneq
def cl_f01_cash_level_sq_63d_slope_v126_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq cashneq
def cl_f01_cash_level_sq_126d_slope_v127_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq cashneq
def cl_f01_cash_level_sq_126d_slope_v128_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq cashneq
def cl_f01_cash_level_sq_126d_slope_v129_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq cashneq
def cl_f01_cash_level_sq_252d_slope_v130_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq cashneq
def cl_f01_cash_level_sq_252d_slope_v131_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq cashneq
def cl_f01_cash_level_sq_252d_slope_v132_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq cashneq
def cl_f01_cash_level_sq_504d_slope_v133_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq cashneq
def cl_f01_cash_level_sq_504d_slope_v134_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq cashneq
def cl_f01_cash_level_sq_504d_slope_v135_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z cashneq
def cl_f01_cash_level_z_21d_slope_v136_signal(cashneq):
    base = _z(cashneq, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z cashneq
def cl_f01_cash_level_z_21d_slope_v137_signal(cashneq):
    base = _z(cashneq, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z cashneq
def cl_f01_cash_level_z_21d_slope_v138_signal(cashneq):
    base = _z(cashneq, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z cashneq
def cl_f01_cash_level_z_63d_slope_v139_signal(cashneq):
    base = _z(cashneq, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z cashneq
def cl_f01_cash_level_z_63d_slope_v140_signal(cashneq):
    base = _z(cashneq, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z cashneq
def cl_f01_cash_level_z_63d_slope_v141_signal(cashneq):
    base = _z(cashneq, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z cashneq
def cl_f01_cash_level_z_126d_slope_v142_signal(cashneq):
    base = _z(cashneq, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z cashneq
def cl_f01_cash_level_z_126d_slope_v143_signal(cashneq):
    base = _z(cashneq, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z cashneq
def cl_f01_cash_level_z_126d_slope_v144_signal(cashneq):
    base = _z(cashneq, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z cashneq
def cl_f01_cash_level_z_252d_slope_v145_signal(cashneq):
    base = _z(cashneq, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z cashneq
def cl_f01_cash_level_z_252d_slope_v146_signal(cashneq):
    base = _z(cashneq, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z cashneq
def cl_f01_cash_level_z_252d_slope_v147_signal(cashneq):
    base = _z(cashneq, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z cashneq
def cl_f01_cash_level_z_504d_slope_v148_signal(cashneq):
    base = _z(cashneq, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z cashneq
def cl_f01_cash_level_z_504d_slope_v149_signal(cashneq):
    base = _z(cashneq, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z cashneq
def cl_f01_cash_level_z_504d_slope_v150_signal(cashneq):
    base = _z(cashneq, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
