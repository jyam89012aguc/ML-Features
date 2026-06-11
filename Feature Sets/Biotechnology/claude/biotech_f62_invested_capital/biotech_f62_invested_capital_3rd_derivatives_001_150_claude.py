"""Family f62 - Invested capital  (J_Returns_Efficiency) | 3rd derivatives 001-150"""
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
def _invested_capital_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _invested_capital_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _invested_capital_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw invcap
def ivc_f62_invested_capital_raw_21d_accel_v001_signal(invcap, closeadj):
    base = _mean(invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw invcap
def ivc_f62_invested_capital_raw_21d_accel_v002_signal(invcap, closeadj):
    base = _mean(invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw invcap
def ivc_f62_invested_capital_raw_21d_accel_v003_signal(invcap, closeadj):
    base = _mean(invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw invcap
def ivc_f62_invested_capital_raw_63d_accel_v004_signal(invcap, closeadj):
    base = _mean(invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw invcap
def ivc_f62_invested_capital_raw_63d_accel_v005_signal(invcap, closeadj):
    base = _mean(invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw invcap
def ivc_f62_invested_capital_raw_63d_accel_v006_signal(invcap, closeadj):
    base = _mean(invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw invcap
def ivc_f62_invested_capital_raw_126d_accel_v007_signal(invcap, closeadj):
    base = _mean(invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw invcap
def ivc_f62_invested_capital_raw_126d_accel_v008_signal(invcap, closeadj):
    base = _mean(invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw invcap
def ivc_f62_invested_capital_raw_126d_accel_v009_signal(invcap, closeadj):
    base = _mean(invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw invcap
def ivc_f62_invested_capital_raw_252d_accel_v010_signal(invcap, closeadj):
    base = _mean(invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw invcap
def ivc_f62_invested_capital_raw_252d_accel_v011_signal(invcap, closeadj):
    base = _mean(invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw invcap
def ivc_f62_invested_capital_raw_252d_accel_v012_signal(invcap, closeadj):
    base = _mean(invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw invcap
def ivc_f62_invested_capital_raw_504d_accel_v013_signal(invcap, closeadj):
    base = _mean(invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw invcap
def ivc_f62_invested_capital_raw_504d_accel_v014_signal(invcap, closeadj):
    base = _mean(invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw invcap
def ivc_f62_invested_capital_raw_504d_accel_v015_signal(invcap, closeadj):
    base = _mean(invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log invcap
def ivc_f62_invested_capital_log_21d_accel_v016_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log invcap
def ivc_f62_invested_capital_log_21d_accel_v017_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log invcap
def ivc_f62_invested_capital_log_21d_accel_v018_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log invcap
def ivc_f62_invested_capital_log_63d_accel_v019_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log invcap
def ivc_f62_invested_capital_log_63d_accel_v020_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log invcap
def ivc_f62_invested_capital_log_63d_accel_v021_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log invcap
def ivc_f62_invested_capital_log_126d_accel_v022_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log invcap
def ivc_f62_invested_capital_log_126d_accel_v023_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log invcap
def ivc_f62_invested_capital_log_126d_accel_v024_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log invcap
def ivc_f62_invested_capital_log_252d_accel_v025_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log invcap
def ivc_f62_invested_capital_log_252d_accel_v026_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log invcap
def ivc_f62_invested_capital_log_252d_accel_v027_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log invcap
def ivc_f62_invested_capital_log_504d_accel_v028_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log invcap
def ivc_f62_invested_capital_log_504d_accel_v029_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log invcap
def ivc_f62_invested_capital_log_504d_accel_v030_signal(invcap, closeadj):
    base = _mean(_invested_capital_log(invcap), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare invcap
def ivc_f62_invested_capital_pershare_21d_accel_v031_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare invcap
def ivc_f62_invested_capital_pershare_21d_accel_v032_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare invcap
def ivc_f62_invested_capital_pershare_21d_accel_v033_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare invcap
def ivc_f62_invested_capital_pershare_63d_accel_v034_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare invcap
def ivc_f62_invested_capital_pershare_63d_accel_v035_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare invcap
def ivc_f62_invested_capital_pershare_63d_accel_v036_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare invcap
def ivc_f62_invested_capital_pershare_126d_accel_v037_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare invcap
def ivc_f62_invested_capital_pershare_126d_accel_v038_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare invcap
def ivc_f62_invested_capital_pershare_126d_accel_v039_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare invcap
def ivc_f62_invested_capital_pershare_252d_accel_v040_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare invcap
def ivc_f62_invested_capital_pershare_252d_accel_v041_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare invcap
def ivc_f62_invested_capital_pershare_252d_accel_v042_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare invcap
def ivc_f62_invested_capital_pershare_504d_accel_v043_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare invcap
def ivc_f62_invested_capital_pershare_504d_accel_v044_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare invcap
def ivc_f62_invested_capital_pershare_504d_accel_v045_signal(invcap, sharesbas, closeadj):
    base = _mean(_invested_capital_per_share(invcap, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets invcap
def ivc_f62_invested_capital_per_assets_21d_accel_v046_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets invcap
def ivc_f62_invested_capital_per_assets_21d_accel_v047_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets invcap
def ivc_f62_invested_capital_per_assets_21d_accel_v048_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets invcap
def ivc_f62_invested_capital_per_assets_63d_accel_v049_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets invcap
def ivc_f62_invested_capital_per_assets_63d_accel_v050_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets invcap
def ivc_f62_invested_capital_per_assets_63d_accel_v051_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets invcap
def ivc_f62_invested_capital_per_assets_126d_accel_v052_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets invcap
def ivc_f62_invested_capital_per_assets_126d_accel_v053_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets invcap
def ivc_f62_invested_capital_per_assets_126d_accel_v054_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets invcap
def ivc_f62_invested_capital_per_assets_252d_accel_v055_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets invcap
def ivc_f62_invested_capital_per_assets_252d_accel_v056_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets invcap
def ivc_f62_invested_capital_per_assets_252d_accel_v057_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets invcap
def ivc_f62_invested_capital_per_assets_504d_accel_v058_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets invcap
def ivc_f62_invested_capital_per_assets_504d_accel_v059_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets invcap
def ivc_f62_invested_capital_per_assets_504d_accel_v060_signal(invcap, assets):
    base = _mean(_invested_capital_scaled(invcap, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_21d_accel_v061_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_21d_accel_v062_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_21d_accel_v063_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_63d_accel_v064_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_63d_accel_v065_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_63d_accel_v066_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_126d_accel_v067_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_126d_accel_v068_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_126d_accel_v069_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_252d_accel_v070_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_252d_accel_v071_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_252d_accel_v072_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_504d_accel_v073_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_504d_accel_v074_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap invcap
def ivc_f62_invested_capital_per_marketcap_504d_accel_v075_signal(invcap, marketcap):
    base = _mean(_invested_capital_scaled(invcap, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity invcap
def ivc_f62_invested_capital_per_equity_21d_accel_v076_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity invcap
def ivc_f62_invested_capital_per_equity_21d_accel_v077_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity invcap
def ivc_f62_invested_capital_per_equity_21d_accel_v078_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity invcap
def ivc_f62_invested_capital_per_equity_63d_accel_v079_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity invcap
def ivc_f62_invested_capital_per_equity_63d_accel_v080_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity invcap
def ivc_f62_invested_capital_per_equity_63d_accel_v081_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity invcap
def ivc_f62_invested_capital_per_equity_126d_accel_v082_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity invcap
def ivc_f62_invested_capital_per_equity_126d_accel_v083_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity invcap
def ivc_f62_invested_capital_per_equity_126d_accel_v084_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity invcap
def ivc_f62_invested_capital_per_equity_252d_accel_v085_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity invcap
def ivc_f62_invested_capital_per_equity_252d_accel_v086_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity invcap
def ivc_f62_invested_capital_per_equity_252d_accel_v087_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity invcap
def ivc_f62_invested_capital_per_equity_504d_accel_v088_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity invcap
def ivc_f62_invested_capital_per_equity_504d_accel_v089_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity invcap
def ivc_f62_invested_capital_per_equity_504d_accel_v090_signal(invcap, equity):
    base = _mean(_invested_capital_scaled(invcap, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std invcap
def ivc_f62_invested_capital_std_21d_accel_v091_signal(invcap, closeadj):
    base = _std(invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std invcap
def ivc_f62_invested_capital_std_21d_accel_v092_signal(invcap, closeadj):
    base = _std(invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std invcap
def ivc_f62_invested_capital_std_21d_accel_v093_signal(invcap, closeadj):
    base = _std(invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std invcap
def ivc_f62_invested_capital_std_63d_accel_v094_signal(invcap, closeadj):
    base = _std(invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std invcap
def ivc_f62_invested_capital_std_63d_accel_v095_signal(invcap, closeadj):
    base = _std(invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std invcap
def ivc_f62_invested_capital_std_63d_accel_v096_signal(invcap, closeadj):
    base = _std(invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std invcap
def ivc_f62_invested_capital_std_126d_accel_v097_signal(invcap, closeadj):
    base = _std(invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std invcap
def ivc_f62_invested_capital_std_126d_accel_v098_signal(invcap, closeadj):
    base = _std(invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std invcap
def ivc_f62_invested_capital_std_126d_accel_v099_signal(invcap, closeadj):
    base = _std(invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std invcap
def ivc_f62_invested_capital_std_252d_accel_v100_signal(invcap, closeadj):
    base = _std(invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std invcap
def ivc_f62_invested_capital_std_252d_accel_v101_signal(invcap, closeadj):
    base = _std(invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std invcap
def ivc_f62_invested_capital_std_252d_accel_v102_signal(invcap, closeadj):
    base = _std(invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std invcap
def ivc_f62_invested_capital_std_504d_accel_v103_signal(invcap, closeadj):
    base = _std(invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std invcap
def ivc_f62_invested_capital_std_504d_accel_v104_signal(invcap, closeadj):
    base = _std(invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std invcap
def ivc_f62_invested_capital_std_504d_accel_v105_signal(invcap, closeadj):
    base = _std(invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm invcap
def ivc_f62_invested_capital_ewm_21d_accel_v106_signal(invcap, closeadj):
    base = invcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm invcap
def ivc_f62_invested_capital_ewm_21d_accel_v107_signal(invcap, closeadj):
    base = invcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm invcap
def ivc_f62_invested_capital_ewm_21d_accel_v108_signal(invcap, closeadj):
    base = invcap.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm invcap
def ivc_f62_invested_capital_ewm_63d_accel_v109_signal(invcap, closeadj):
    base = invcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm invcap
def ivc_f62_invested_capital_ewm_63d_accel_v110_signal(invcap, closeadj):
    base = invcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm invcap
def ivc_f62_invested_capital_ewm_63d_accel_v111_signal(invcap, closeadj):
    base = invcap.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm invcap
def ivc_f62_invested_capital_ewm_126d_accel_v112_signal(invcap, closeadj):
    base = invcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm invcap
def ivc_f62_invested_capital_ewm_126d_accel_v113_signal(invcap, closeadj):
    base = invcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm invcap
def ivc_f62_invested_capital_ewm_126d_accel_v114_signal(invcap, closeadj):
    base = invcap.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm invcap
def ivc_f62_invested_capital_ewm_252d_accel_v115_signal(invcap, closeadj):
    base = invcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm invcap
def ivc_f62_invested_capital_ewm_252d_accel_v116_signal(invcap, closeadj):
    base = invcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm invcap
def ivc_f62_invested_capital_ewm_252d_accel_v117_signal(invcap, closeadj):
    base = invcap.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm invcap
def ivc_f62_invested_capital_ewm_504d_accel_v118_signal(invcap, closeadj):
    base = invcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm invcap
def ivc_f62_invested_capital_ewm_504d_accel_v119_signal(invcap, closeadj):
    base = invcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm invcap
def ivc_f62_invested_capital_ewm_504d_accel_v120_signal(invcap, closeadj):
    base = invcap.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq invcap
def ivc_f62_invested_capital_sq_21d_accel_v121_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq invcap
def ivc_f62_invested_capital_sq_21d_accel_v122_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq invcap
def ivc_f62_invested_capital_sq_21d_accel_v123_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq invcap
def ivc_f62_invested_capital_sq_63d_accel_v124_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq invcap
def ivc_f62_invested_capital_sq_63d_accel_v125_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq invcap
def ivc_f62_invested_capital_sq_63d_accel_v126_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq invcap
def ivc_f62_invested_capital_sq_126d_accel_v127_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq invcap
def ivc_f62_invested_capital_sq_126d_accel_v128_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq invcap
def ivc_f62_invested_capital_sq_126d_accel_v129_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq invcap
def ivc_f62_invested_capital_sq_252d_accel_v130_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq invcap
def ivc_f62_invested_capital_sq_252d_accel_v131_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq invcap
def ivc_f62_invested_capital_sq_252d_accel_v132_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq invcap
def ivc_f62_invested_capital_sq_504d_accel_v133_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq invcap
def ivc_f62_invested_capital_sq_504d_accel_v134_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq invcap
def ivc_f62_invested_capital_sq_504d_accel_v135_signal(invcap, closeadj):
    base = _mean(invcap * invcap, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z invcap
def ivc_f62_invested_capital_z_21d_accel_v136_signal(invcap):
    base = _z(invcap, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z invcap
def ivc_f62_invested_capital_z_21d_accel_v137_signal(invcap):
    base = _z(invcap, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z invcap
def ivc_f62_invested_capital_z_21d_accel_v138_signal(invcap):
    base = _z(invcap, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z invcap
def ivc_f62_invested_capital_z_63d_accel_v139_signal(invcap):
    base = _z(invcap, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z invcap
def ivc_f62_invested_capital_z_63d_accel_v140_signal(invcap):
    base = _z(invcap, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z invcap
def ivc_f62_invested_capital_z_63d_accel_v141_signal(invcap):
    base = _z(invcap, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z invcap
def ivc_f62_invested_capital_z_126d_accel_v142_signal(invcap):
    base = _z(invcap, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z invcap
def ivc_f62_invested_capital_z_126d_accel_v143_signal(invcap):
    base = _z(invcap, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z invcap
def ivc_f62_invested_capital_z_126d_accel_v144_signal(invcap):
    base = _z(invcap, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z invcap
def ivc_f62_invested_capital_z_252d_accel_v145_signal(invcap):
    base = _z(invcap, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z invcap
def ivc_f62_invested_capital_z_252d_accel_v146_signal(invcap):
    base = _z(invcap, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z invcap
def ivc_f62_invested_capital_z_252d_accel_v147_signal(invcap):
    base = _z(invcap, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z invcap
def ivc_f62_invested_capital_z_504d_accel_v148_signal(invcap):
    base = _z(invcap, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z invcap
def ivc_f62_invested_capital_z_504d_accel_v149_signal(invcap):
    base = _z(invcap, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z invcap
def ivc_f62_invested_capital_z_504d_accel_v150_signal(invcap):
    base = _z(invcap, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
