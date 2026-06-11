"""Family f01 - Cash & equivalents level  (A_Liquidity_Runway) | 3rd derivatives 001-150"""
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


# 5d accel of 21d raw cashneq
def cl_f01_cash_level_raw_21d_accel_v001_signal(cashneq, closeadj):
    base = _mean(cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw cashneq
def cl_f01_cash_level_raw_21d_accel_v002_signal(cashneq, closeadj):
    base = _mean(cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw cashneq
def cl_f01_cash_level_raw_21d_accel_v003_signal(cashneq, closeadj):
    base = _mean(cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw cashneq
def cl_f01_cash_level_raw_63d_accel_v004_signal(cashneq, closeadj):
    base = _mean(cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw cashneq
def cl_f01_cash_level_raw_63d_accel_v005_signal(cashneq, closeadj):
    base = _mean(cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw cashneq
def cl_f01_cash_level_raw_63d_accel_v006_signal(cashneq, closeadj):
    base = _mean(cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw cashneq
def cl_f01_cash_level_raw_126d_accel_v007_signal(cashneq, closeadj):
    base = _mean(cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw cashneq
def cl_f01_cash_level_raw_126d_accel_v008_signal(cashneq, closeadj):
    base = _mean(cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw cashneq
def cl_f01_cash_level_raw_126d_accel_v009_signal(cashneq, closeadj):
    base = _mean(cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw cashneq
def cl_f01_cash_level_raw_252d_accel_v010_signal(cashneq, closeadj):
    base = _mean(cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw cashneq
def cl_f01_cash_level_raw_252d_accel_v011_signal(cashneq, closeadj):
    base = _mean(cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw cashneq
def cl_f01_cash_level_raw_252d_accel_v012_signal(cashneq, closeadj):
    base = _mean(cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw cashneq
def cl_f01_cash_level_raw_504d_accel_v013_signal(cashneq, closeadj):
    base = _mean(cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw cashneq
def cl_f01_cash_level_raw_504d_accel_v014_signal(cashneq, closeadj):
    base = _mean(cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw cashneq
def cl_f01_cash_level_raw_504d_accel_v015_signal(cashneq, closeadj):
    base = _mean(cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log cashneq
def cl_f01_cash_level_log_21d_accel_v016_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log cashneq
def cl_f01_cash_level_log_21d_accel_v017_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log cashneq
def cl_f01_cash_level_log_21d_accel_v018_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log cashneq
def cl_f01_cash_level_log_63d_accel_v019_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log cashneq
def cl_f01_cash_level_log_63d_accel_v020_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log cashneq
def cl_f01_cash_level_log_63d_accel_v021_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log cashneq
def cl_f01_cash_level_log_126d_accel_v022_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log cashneq
def cl_f01_cash_level_log_126d_accel_v023_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log cashneq
def cl_f01_cash_level_log_126d_accel_v024_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log cashneq
def cl_f01_cash_level_log_252d_accel_v025_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log cashneq
def cl_f01_cash_level_log_252d_accel_v026_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log cashneq
def cl_f01_cash_level_log_252d_accel_v027_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log cashneq
def cl_f01_cash_level_log_504d_accel_v028_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log cashneq
def cl_f01_cash_level_log_504d_accel_v029_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log cashneq
def cl_f01_cash_level_log_504d_accel_v030_signal(cashneq, closeadj):
    base = _mean(_cash_level_log(cashneq), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare cashneq
def cl_f01_cash_level_pershare_21d_accel_v031_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare cashneq
def cl_f01_cash_level_pershare_21d_accel_v032_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare cashneq
def cl_f01_cash_level_pershare_21d_accel_v033_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare cashneq
def cl_f01_cash_level_pershare_63d_accel_v034_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare cashneq
def cl_f01_cash_level_pershare_63d_accel_v035_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare cashneq
def cl_f01_cash_level_pershare_63d_accel_v036_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare cashneq
def cl_f01_cash_level_pershare_126d_accel_v037_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare cashneq
def cl_f01_cash_level_pershare_126d_accel_v038_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare cashneq
def cl_f01_cash_level_pershare_126d_accel_v039_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare cashneq
def cl_f01_cash_level_pershare_252d_accel_v040_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare cashneq
def cl_f01_cash_level_pershare_252d_accel_v041_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare cashneq
def cl_f01_cash_level_pershare_252d_accel_v042_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare cashneq
def cl_f01_cash_level_pershare_504d_accel_v043_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare cashneq
def cl_f01_cash_level_pershare_504d_accel_v044_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare cashneq
def cl_f01_cash_level_pershare_504d_accel_v045_signal(cashneq, sharesbas, closeadj):
    base = _mean(_cash_level_per_share(cashneq, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets cashneq
def cl_f01_cash_level_per_assets_21d_accel_v046_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets cashneq
def cl_f01_cash_level_per_assets_21d_accel_v047_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets cashneq
def cl_f01_cash_level_per_assets_21d_accel_v048_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets cashneq
def cl_f01_cash_level_per_assets_63d_accel_v049_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets cashneq
def cl_f01_cash_level_per_assets_63d_accel_v050_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets cashneq
def cl_f01_cash_level_per_assets_63d_accel_v051_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets cashneq
def cl_f01_cash_level_per_assets_126d_accel_v052_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets cashneq
def cl_f01_cash_level_per_assets_126d_accel_v053_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets cashneq
def cl_f01_cash_level_per_assets_126d_accel_v054_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets cashneq
def cl_f01_cash_level_per_assets_252d_accel_v055_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets cashneq
def cl_f01_cash_level_per_assets_252d_accel_v056_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets cashneq
def cl_f01_cash_level_per_assets_252d_accel_v057_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets cashneq
def cl_f01_cash_level_per_assets_504d_accel_v058_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets cashneq
def cl_f01_cash_level_per_assets_504d_accel_v059_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets cashneq
def cl_f01_cash_level_per_assets_504d_accel_v060_signal(cashneq, assets):
    base = _mean(_cash_level_scaled(cashneq, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_21d_accel_v061_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_21d_accel_v062_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_21d_accel_v063_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_63d_accel_v064_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_63d_accel_v065_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_63d_accel_v066_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_126d_accel_v067_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_126d_accel_v068_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_126d_accel_v069_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_252d_accel_v070_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_252d_accel_v071_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_252d_accel_v072_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_504d_accel_v073_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_504d_accel_v074_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap cashneq
def cl_f01_cash_level_per_marketcap_504d_accel_v075_signal(cashneq, marketcap):
    base = _mean(_cash_level_scaled(cashneq, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity cashneq
def cl_f01_cash_level_per_equity_21d_accel_v076_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity cashneq
def cl_f01_cash_level_per_equity_21d_accel_v077_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity cashneq
def cl_f01_cash_level_per_equity_21d_accel_v078_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity cashneq
def cl_f01_cash_level_per_equity_63d_accel_v079_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity cashneq
def cl_f01_cash_level_per_equity_63d_accel_v080_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity cashneq
def cl_f01_cash_level_per_equity_63d_accel_v081_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity cashneq
def cl_f01_cash_level_per_equity_126d_accel_v082_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity cashneq
def cl_f01_cash_level_per_equity_126d_accel_v083_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity cashneq
def cl_f01_cash_level_per_equity_126d_accel_v084_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity cashneq
def cl_f01_cash_level_per_equity_252d_accel_v085_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity cashneq
def cl_f01_cash_level_per_equity_252d_accel_v086_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity cashneq
def cl_f01_cash_level_per_equity_252d_accel_v087_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity cashneq
def cl_f01_cash_level_per_equity_504d_accel_v088_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity cashneq
def cl_f01_cash_level_per_equity_504d_accel_v089_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity cashneq
def cl_f01_cash_level_per_equity_504d_accel_v090_signal(cashneq, equity):
    base = _mean(_cash_level_scaled(cashneq, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std cashneq
def cl_f01_cash_level_std_21d_accel_v091_signal(cashneq, closeadj):
    base = _std(cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std cashneq
def cl_f01_cash_level_std_21d_accel_v092_signal(cashneq, closeadj):
    base = _std(cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std cashneq
def cl_f01_cash_level_std_21d_accel_v093_signal(cashneq, closeadj):
    base = _std(cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std cashneq
def cl_f01_cash_level_std_63d_accel_v094_signal(cashneq, closeadj):
    base = _std(cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std cashneq
def cl_f01_cash_level_std_63d_accel_v095_signal(cashneq, closeadj):
    base = _std(cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std cashneq
def cl_f01_cash_level_std_63d_accel_v096_signal(cashneq, closeadj):
    base = _std(cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std cashneq
def cl_f01_cash_level_std_126d_accel_v097_signal(cashneq, closeadj):
    base = _std(cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std cashneq
def cl_f01_cash_level_std_126d_accel_v098_signal(cashneq, closeadj):
    base = _std(cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std cashneq
def cl_f01_cash_level_std_126d_accel_v099_signal(cashneq, closeadj):
    base = _std(cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std cashneq
def cl_f01_cash_level_std_252d_accel_v100_signal(cashneq, closeadj):
    base = _std(cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std cashneq
def cl_f01_cash_level_std_252d_accel_v101_signal(cashneq, closeadj):
    base = _std(cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std cashneq
def cl_f01_cash_level_std_252d_accel_v102_signal(cashneq, closeadj):
    base = _std(cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std cashneq
def cl_f01_cash_level_std_504d_accel_v103_signal(cashneq, closeadj):
    base = _std(cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std cashneq
def cl_f01_cash_level_std_504d_accel_v104_signal(cashneq, closeadj):
    base = _std(cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std cashneq
def cl_f01_cash_level_std_504d_accel_v105_signal(cashneq, closeadj):
    base = _std(cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm cashneq
def cl_f01_cash_level_ewm_21d_accel_v106_signal(cashneq, closeadj):
    base = cashneq.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm cashneq
def cl_f01_cash_level_ewm_21d_accel_v107_signal(cashneq, closeadj):
    base = cashneq.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm cashneq
def cl_f01_cash_level_ewm_21d_accel_v108_signal(cashneq, closeadj):
    base = cashneq.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm cashneq
def cl_f01_cash_level_ewm_63d_accel_v109_signal(cashneq, closeadj):
    base = cashneq.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm cashneq
def cl_f01_cash_level_ewm_63d_accel_v110_signal(cashneq, closeadj):
    base = cashneq.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm cashneq
def cl_f01_cash_level_ewm_63d_accel_v111_signal(cashneq, closeadj):
    base = cashneq.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm cashneq
def cl_f01_cash_level_ewm_126d_accel_v112_signal(cashneq, closeadj):
    base = cashneq.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm cashneq
def cl_f01_cash_level_ewm_126d_accel_v113_signal(cashneq, closeadj):
    base = cashneq.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm cashneq
def cl_f01_cash_level_ewm_126d_accel_v114_signal(cashneq, closeadj):
    base = cashneq.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm cashneq
def cl_f01_cash_level_ewm_252d_accel_v115_signal(cashneq, closeadj):
    base = cashneq.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm cashneq
def cl_f01_cash_level_ewm_252d_accel_v116_signal(cashneq, closeadj):
    base = cashneq.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm cashneq
def cl_f01_cash_level_ewm_252d_accel_v117_signal(cashneq, closeadj):
    base = cashneq.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm cashneq
def cl_f01_cash_level_ewm_504d_accel_v118_signal(cashneq, closeadj):
    base = cashneq.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm cashneq
def cl_f01_cash_level_ewm_504d_accel_v119_signal(cashneq, closeadj):
    base = cashneq.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm cashneq
def cl_f01_cash_level_ewm_504d_accel_v120_signal(cashneq, closeadj):
    base = cashneq.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq cashneq
def cl_f01_cash_level_sq_21d_accel_v121_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq cashneq
def cl_f01_cash_level_sq_21d_accel_v122_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq cashneq
def cl_f01_cash_level_sq_21d_accel_v123_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq cashneq
def cl_f01_cash_level_sq_63d_accel_v124_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq cashneq
def cl_f01_cash_level_sq_63d_accel_v125_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq cashneq
def cl_f01_cash_level_sq_63d_accel_v126_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq cashneq
def cl_f01_cash_level_sq_126d_accel_v127_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq cashneq
def cl_f01_cash_level_sq_126d_accel_v128_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq cashneq
def cl_f01_cash_level_sq_126d_accel_v129_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq cashneq
def cl_f01_cash_level_sq_252d_accel_v130_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq cashneq
def cl_f01_cash_level_sq_252d_accel_v131_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq cashneq
def cl_f01_cash_level_sq_252d_accel_v132_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq cashneq
def cl_f01_cash_level_sq_504d_accel_v133_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq cashneq
def cl_f01_cash_level_sq_504d_accel_v134_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq cashneq
def cl_f01_cash_level_sq_504d_accel_v135_signal(cashneq, closeadj):
    base = _mean(cashneq * cashneq, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z cashneq
def cl_f01_cash_level_z_21d_accel_v136_signal(cashneq):
    base = _z(cashneq, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z cashneq
def cl_f01_cash_level_z_21d_accel_v137_signal(cashneq):
    base = _z(cashneq, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z cashneq
def cl_f01_cash_level_z_21d_accel_v138_signal(cashneq):
    base = _z(cashneq, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z cashneq
def cl_f01_cash_level_z_63d_accel_v139_signal(cashneq):
    base = _z(cashneq, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z cashneq
def cl_f01_cash_level_z_63d_accel_v140_signal(cashneq):
    base = _z(cashneq, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z cashneq
def cl_f01_cash_level_z_63d_accel_v141_signal(cashneq):
    base = _z(cashneq, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z cashneq
def cl_f01_cash_level_z_126d_accel_v142_signal(cashneq):
    base = _z(cashneq, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z cashneq
def cl_f01_cash_level_z_126d_accel_v143_signal(cashneq):
    base = _z(cashneq, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z cashneq
def cl_f01_cash_level_z_126d_accel_v144_signal(cashneq):
    base = _z(cashneq, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z cashneq
def cl_f01_cash_level_z_252d_accel_v145_signal(cashneq):
    base = _z(cashneq, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z cashneq
def cl_f01_cash_level_z_252d_accel_v146_signal(cashneq):
    base = _z(cashneq, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z cashneq
def cl_f01_cash_level_z_252d_accel_v147_signal(cashneq):
    base = _z(cashneq, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z cashneq
def cl_f01_cash_level_z_504d_accel_v148_signal(cashneq):
    base = _z(cashneq, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z cashneq
def cl_f01_cash_level_z_504d_accel_v149_signal(cashneq):
    base = _z(cashneq, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z cashneq
def cl_f01_cash_level_z_504d_accel_v150_signal(cashneq):
    base = _z(cashneq, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
