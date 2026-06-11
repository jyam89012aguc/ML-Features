"""Family f05 - Current ratio & trend  (A_Liquidity_Runway) | 3rd derivatives 001-150"""
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
def _current_ratio_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _current_ratio_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _current_ratio_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw currentratio
def cur_f05_current_ratio_raw_21d_accel_v001_signal(currentratio, closeadj):
    base = _mean(currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw currentratio
def cur_f05_current_ratio_raw_21d_accel_v002_signal(currentratio, closeadj):
    base = _mean(currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw currentratio
def cur_f05_current_ratio_raw_21d_accel_v003_signal(currentratio, closeadj):
    base = _mean(currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw currentratio
def cur_f05_current_ratio_raw_63d_accel_v004_signal(currentratio, closeadj):
    base = _mean(currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw currentratio
def cur_f05_current_ratio_raw_63d_accel_v005_signal(currentratio, closeadj):
    base = _mean(currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw currentratio
def cur_f05_current_ratio_raw_63d_accel_v006_signal(currentratio, closeadj):
    base = _mean(currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw currentratio
def cur_f05_current_ratio_raw_126d_accel_v007_signal(currentratio, closeadj):
    base = _mean(currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw currentratio
def cur_f05_current_ratio_raw_126d_accel_v008_signal(currentratio, closeadj):
    base = _mean(currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw currentratio
def cur_f05_current_ratio_raw_126d_accel_v009_signal(currentratio, closeadj):
    base = _mean(currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw currentratio
def cur_f05_current_ratio_raw_252d_accel_v010_signal(currentratio, closeadj):
    base = _mean(currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw currentratio
def cur_f05_current_ratio_raw_252d_accel_v011_signal(currentratio, closeadj):
    base = _mean(currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw currentratio
def cur_f05_current_ratio_raw_252d_accel_v012_signal(currentratio, closeadj):
    base = _mean(currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw currentratio
def cur_f05_current_ratio_raw_504d_accel_v013_signal(currentratio, closeadj):
    base = _mean(currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw currentratio
def cur_f05_current_ratio_raw_504d_accel_v014_signal(currentratio, closeadj):
    base = _mean(currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw currentratio
def cur_f05_current_ratio_raw_504d_accel_v015_signal(currentratio, closeadj):
    base = _mean(currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log currentratio
def cur_f05_current_ratio_log_21d_accel_v016_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log currentratio
def cur_f05_current_ratio_log_21d_accel_v017_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log currentratio
def cur_f05_current_ratio_log_21d_accel_v018_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log currentratio
def cur_f05_current_ratio_log_63d_accel_v019_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log currentratio
def cur_f05_current_ratio_log_63d_accel_v020_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log currentratio
def cur_f05_current_ratio_log_63d_accel_v021_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log currentratio
def cur_f05_current_ratio_log_126d_accel_v022_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log currentratio
def cur_f05_current_ratio_log_126d_accel_v023_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log currentratio
def cur_f05_current_ratio_log_126d_accel_v024_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log currentratio
def cur_f05_current_ratio_log_252d_accel_v025_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log currentratio
def cur_f05_current_ratio_log_252d_accel_v026_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log currentratio
def cur_f05_current_ratio_log_252d_accel_v027_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log currentratio
def cur_f05_current_ratio_log_504d_accel_v028_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log currentratio
def cur_f05_current_ratio_log_504d_accel_v029_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log currentratio
def cur_f05_current_ratio_log_504d_accel_v030_signal(currentratio, closeadj):
    base = _mean(_current_ratio_log(currentratio), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare currentratio
def cur_f05_current_ratio_pershare_21d_accel_v031_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare currentratio
def cur_f05_current_ratio_pershare_21d_accel_v032_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare currentratio
def cur_f05_current_ratio_pershare_21d_accel_v033_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare currentratio
def cur_f05_current_ratio_pershare_63d_accel_v034_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare currentratio
def cur_f05_current_ratio_pershare_63d_accel_v035_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare currentratio
def cur_f05_current_ratio_pershare_63d_accel_v036_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare currentratio
def cur_f05_current_ratio_pershare_126d_accel_v037_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare currentratio
def cur_f05_current_ratio_pershare_126d_accel_v038_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare currentratio
def cur_f05_current_ratio_pershare_126d_accel_v039_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare currentratio
def cur_f05_current_ratio_pershare_252d_accel_v040_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare currentratio
def cur_f05_current_ratio_pershare_252d_accel_v041_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare currentratio
def cur_f05_current_ratio_pershare_252d_accel_v042_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare currentratio
def cur_f05_current_ratio_pershare_504d_accel_v043_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare currentratio
def cur_f05_current_ratio_pershare_504d_accel_v044_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare currentratio
def cur_f05_current_ratio_pershare_504d_accel_v045_signal(currentratio, sharesbas, closeadj):
    base = _mean(_current_ratio_per_share(currentratio, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets currentratio
def cur_f05_current_ratio_per_assets_21d_accel_v046_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets currentratio
def cur_f05_current_ratio_per_assets_21d_accel_v047_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets currentratio
def cur_f05_current_ratio_per_assets_21d_accel_v048_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets currentratio
def cur_f05_current_ratio_per_assets_63d_accel_v049_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets currentratio
def cur_f05_current_ratio_per_assets_63d_accel_v050_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets currentratio
def cur_f05_current_ratio_per_assets_63d_accel_v051_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets currentratio
def cur_f05_current_ratio_per_assets_126d_accel_v052_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets currentratio
def cur_f05_current_ratio_per_assets_126d_accel_v053_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets currentratio
def cur_f05_current_ratio_per_assets_126d_accel_v054_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets currentratio
def cur_f05_current_ratio_per_assets_252d_accel_v055_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets currentratio
def cur_f05_current_ratio_per_assets_252d_accel_v056_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets currentratio
def cur_f05_current_ratio_per_assets_252d_accel_v057_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets currentratio
def cur_f05_current_ratio_per_assets_504d_accel_v058_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets currentratio
def cur_f05_current_ratio_per_assets_504d_accel_v059_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets currentratio
def cur_f05_current_ratio_per_assets_504d_accel_v060_signal(currentratio, assets):
    base = _mean(_current_ratio_scaled(currentratio, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_21d_accel_v061_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_21d_accel_v062_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_21d_accel_v063_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_63d_accel_v064_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_63d_accel_v065_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_63d_accel_v066_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_126d_accel_v067_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_126d_accel_v068_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_126d_accel_v069_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_252d_accel_v070_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_252d_accel_v071_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_252d_accel_v072_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_504d_accel_v073_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_504d_accel_v074_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap currentratio
def cur_f05_current_ratio_per_marketcap_504d_accel_v075_signal(currentratio, marketcap):
    base = _mean(_current_ratio_scaled(currentratio, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity currentratio
def cur_f05_current_ratio_per_equity_21d_accel_v076_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity currentratio
def cur_f05_current_ratio_per_equity_21d_accel_v077_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity currentratio
def cur_f05_current_ratio_per_equity_21d_accel_v078_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity currentratio
def cur_f05_current_ratio_per_equity_63d_accel_v079_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity currentratio
def cur_f05_current_ratio_per_equity_63d_accel_v080_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity currentratio
def cur_f05_current_ratio_per_equity_63d_accel_v081_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity currentratio
def cur_f05_current_ratio_per_equity_126d_accel_v082_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity currentratio
def cur_f05_current_ratio_per_equity_126d_accel_v083_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity currentratio
def cur_f05_current_ratio_per_equity_126d_accel_v084_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity currentratio
def cur_f05_current_ratio_per_equity_252d_accel_v085_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity currentratio
def cur_f05_current_ratio_per_equity_252d_accel_v086_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity currentratio
def cur_f05_current_ratio_per_equity_252d_accel_v087_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity currentratio
def cur_f05_current_ratio_per_equity_504d_accel_v088_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity currentratio
def cur_f05_current_ratio_per_equity_504d_accel_v089_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity currentratio
def cur_f05_current_ratio_per_equity_504d_accel_v090_signal(currentratio, equity):
    base = _mean(_current_ratio_scaled(currentratio, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std currentratio
def cur_f05_current_ratio_std_21d_accel_v091_signal(currentratio, closeadj):
    base = _std(currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std currentratio
def cur_f05_current_ratio_std_21d_accel_v092_signal(currentratio, closeadj):
    base = _std(currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std currentratio
def cur_f05_current_ratio_std_21d_accel_v093_signal(currentratio, closeadj):
    base = _std(currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std currentratio
def cur_f05_current_ratio_std_63d_accel_v094_signal(currentratio, closeadj):
    base = _std(currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std currentratio
def cur_f05_current_ratio_std_63d_accel_v095_signal(currentratio, closeadj):
    base = _std(currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std currentratio
def cur_f05_current_ratio_std_63d_accel_v096_signal(currentratio, closeadj):
    base = _std(currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std currentratio
def cur_f05_current_ratio_std_126d_accel_v097_signal(currentratio, closeadj):
    base = _std(currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std currentratio
def cur_f05_current_ratio_std_126d_accel_v098_signal(currentratio, closeadj):
    base = _std(currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std currentratio
def cur_f05_current_ratio_std_126d_accel_v099_signal(currentratio, closeadj):
    base = _std(currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std currentratio
def cur_f05_current_ratio_std_252d_accel_v100_signal(currentratio, closeadj):
    base = _std(currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std currentratio
def cur_f05_current_ratio_std_252d_accel_v101_signal(currentratio, closeadj):
    base = _std(currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std currentratio
def cur_f05_current_ratio_std_252d_accel_v102_signal(currentratio, closeadj):
    base = _std(currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std currentratio
def cur_f05_current_ratio_std_504d_accel_v103_signal(currentratio, closeadj):
    base = _std(currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std currentratio
def cur_f05_current_ratio_std_504d_accel_v104_signal(currentratio, closeadj):
    base = _std(currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std currentratio
def cur_f05_current_ratio_std_504d_accel_v105_signal(currentratio, closeadj):
    base = _std(currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm currentratio
def cur_f05_current_ratio_ewm_21d_accel_v106_signal(currentratio, closeadj):
    base = currentratio.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm currentratio
def cur_f05_current_ratio_ewm_21d_accel_v107_signal(currentratio, closeadj):
    base = currentratio.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm currentratio
def cur_f05_current_ratio_ewm_21d_accel_v108_signal(currentratio, closeadj):
    base = currentratio.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm currentratio
def cur_f05_current_ratio_ewm_63d_accel_v109_signal(currentratio, closeadj):
    base = currentratio.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm currentratio
def cur_f05_current_ratio_ewm_63d_accel_v110_signal(currentratio, closeadj):
    base = currentratio.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm currentratio
def cur_f05_current_ratio_ewm_63d_accel_v111_signal(currentratio, closeadj):
    base = currentratio.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm currentratio
def cur_f05_current_ratio_ewm_126d_accel_v112_signal(currentratio, closeadj):
    base = currentratio.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm currentratio
def cur_f05_current_ratio_ewm_126d_accel_v113_signal(currentratio, closeadj):
    base = currentratio.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm currentratio
def cur_f05_current_ratio_ewm_126d_accel_v114_signal(currentratio, closeadj):
    base = currentratio.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm currentratio
def cur_f05_current_ratio_ewm_252d_accel_v115_signal(currentratio, closeadj):
    base = currentratio.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm currentratio
def cur_f05_current_ratio_ewm_252d_accel_v116_signal(currentratio, closeadj):
    base = currentratio.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm currentratio
def cur_f05_current_ratio_ewm_252d_accel_v117_signal(currentratio, closeadj):
    base = currentratio.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm currentratio
def cur_f05_current_ratio_ewm_504d_accel_v118_signal(currentratio, closeadj):
    base = currentratio.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm currentratio
def cur_f05_current_ratio_ewm_504d_accel_v119_signal(currentratio, closeadj):
    base = currentratio.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm currentratio
def cur_f05_current_ratio_ewm_504d_accel_v120_signal(currentratio, closeadj):
    base = currentratio.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq currentratio
def cur_f05_current_ratio_sq_21d_accel_v121_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq currentratio
def cur_f05_current_ratio_sq_21d_accel_v122_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq currentratio
def cur_f05_current_ratio_sq_21d_accel_v123_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq currentratio
def cur_f05_current_ratio_sq_63d_accel_v124_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq currentratio
def cur_f05_current_ratio_sq_63d_accel_v125_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq currentratio
def cur_f05_current_ratio_sq_63d_accel_v126_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq currentratio
def cur_f05_current_ratio_sq_126d_accel_v127_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq currentratio
def cur_f05_current_ratio_sq_126d_accel_v128_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq currentratio
def cur_f05_current_ratio_sq_126d_accel_v129_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq currentratio
def cur_f05_current_ratio_sq_252d_accel_v130_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq currentratio
def cur_f05_current_ratio_sq_252d_accel_v131_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq currentratio
def cur_f05_current_ratio_sq_252d_accel_v132_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq currentratio
def cur_f05_current_ratio_sq_504d_accel_v133_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq currentratio
def cur_f05_current_ratio_sq_504d_accel_v134_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq currentratio
def cur_f05_current_ratio_sq_504d_accel_v135_signal(currentratio, closeadj):
    base = _mean(currentratio * currentratio, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z currentratio
def cur_f05_current_ratio_z_21d_accel_v136_signal(currentratio):
    base = _z(currentratio, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z currentratio
def cur_f05_current_ratio_z_21d_accel_v137_signal(currentratio):
    base = _z(currentratio, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z currentratio
def cur_f05_current_ratio_z_21d_accel_v138_signal(currentratio):
    base = _z(currentratio, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z currentratio
def cur_f05_current_ratio_z_63d_accel_v139_signal(currentratio):
    base = _z(currentratio, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z currentratio
def cur_f05_current_ratio_z_63d_accel_v140_signal(currentratio):
    base = _z(currentratio, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z currentratio
def cur_f05_current_ratio_z_63d_accel_v141_signal(currentratio):
    base = _z(currentratio, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z currentratio
def cur_f05_current_ratio_z_126d_accel_v142_signal(currentratio):
    base = _z(currentratio, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z currentratio
def cur_f05_current_ratio_z_126d_accel_v143_signal(currentratio):
    base = _z(currentratio, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z currentratio
def cur_f05_current_ratio_z_126d_accel_v144_signal(currentratio):
    base = _z(currentratio, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z currentratio
def cur_f05_current_ratio_z_252d_accel_v145_signal(currentratio):
    base = _z(currentratio, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z currentratio
def cur_f05_current_ratio_z_252d_accel_v146_signal(currentratio):
    base = _z(currentratio, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z currentratio
def cur_f05_current_ratio_z_252d_accel_v147_signal(currentratio):
    base = _z(currentratio, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z currentratio
def cur_f05_current_ratio_z_504d_accel_v148_signal(currentratio):
    base = _z(currentratio, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z currentratio
def cur_f05_current_ratio_z_504d_accel_v149_signal(currentratio):
    base = _z(currentratio, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z currentratio
def cur_f05_current_ratio_z_504d_accel_v150_signal(currentratio):
    base = _z(currentratio, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
