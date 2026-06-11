"""Family f79 - EV/EBIT EV/EBITDA P/E P/S  (M_Valuation) | 3rd derivatives 001-150"""
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
def _standard_multiples_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _standard_multiples_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _standard_multiples_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d accel of 21d raw evebit
def sm_f79_standard_multiples_raw_21d_accel_v001_signal(evebit, closeadj):
    base = _mean(evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d raw evebit
def sm_f79_standard_multiples_raw_21d_accel_v002_signal(evebit, closeadj):
    base = _mean(evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d raw evebit
def sm_f79_standard_multiples_raw_21d_accel_v003_signal(evebit, closeadj):
    base = _mean(evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d raw evebit
def sm_f79_standard_multiples_raw_63d_accel_v004_signal(evebit, closeadj):
    base = _mean(evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d raw evebit
def sm_f79_standard_multiples_raw_63d_accel_v005_signal(evebit, closeadj):
    base = _mean(evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d raw evebit
def sm_f79_standard_multiples_raw_63d_accel_v006_signal(evebit, closeadj):
    base = _mean(evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d raw evebit
def sm_f79_standard_multiples_raw_126d_accel_v007_signal(evebit, closeadj):
    base = _mean(evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d raw evebit
def sm_f79_standard_multiples_raw_126d_accel_v008_signal(evebit, closeadj):
    base = _mean(evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d raw evebit
def sm_f79_standard_multiples_raw_126d_accel_v009_signal(evebit, closeadj):
    base = _mean(evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d raw evebit
def sm_f79_standard_multiples_raw_252d_accel_v010_signal(evebit, closeadj):
    base = _mean(evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d raw evebit
def sm_f79_standard_multiples_raw_252d_accel_v011_signal(evebit, closeadj):
    base = _mean(evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d raw evebit
def sm_f79_standard_multiples_raw_252d_accel_v012_signal(evebit, closeadj):
    base = _mean(evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d raw evebit
def sm_f79_standard_multiples_raw_504d_accel_v013_signal(evebit, closeadj):
    base = _mean(evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d raw evebit
def sm_f79_standard_multiples_raw_504d_accel_v014_signal(evebit, closeadj):
    base = _mean(evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d raw evebit
def sm_f79_standard_multiples_raw_504d_accel_v015_signal(evebit, closeadj):
    base = _mean(evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d log evebit
def sm_f79_standard_multiples_log_21d_accel_v016_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d log evebit
def sm_f79_standard_multiples_log_21d_accel_v017_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d log evebit
def sm_f79_standard_multiples_log_21d_accel_v018_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d log evebit
def sm_f79_standard_multiples_log_63d_accel_v019_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d log evebit
def sm_f79_standard_multiples_log_63d_accel_v020_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d log evebit
def sm_f79_standard_multiples_log_63d_accel_v021_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d log evebit
def sm_f79_standard_multiples_log_126d_accel_v022_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d log evebit
def sm_f79_standard_multiples_log_126d_accel_v023_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d log evebit
def sm_f79_standard_multiples_log_126d_accel_v024_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d log evebit
def sm_f79_standard_multiples_log_252d_accel_v025_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d log evebit
def sm_f79_standard_multiples_log_252d_accel_v026_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d log evebit
def sm_f79_standard_multiples_log_252d_accel_v027_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d log evebit
def sm_f79_standard_multiples_log_504d_accel_v028_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d log evebit
def sm_f79_standard_multiples_log_504d_accel_v029_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d log evebit
def sm_f79_standard_multiples_log_504d_accel_v030_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d pershare evebit
def sm_f79_standard_multiples_pershare_21d_accel_v031_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d pershare evebit
def sm_f79_standard_multiples_pershare_21d_accel_v032_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d pershare evebit
def sm_f79_standard_multiples_pershare_21d_accel_v033_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d pershare evebit
def sm_f79_standard_multiples_pershare_63d_accel_v034_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d pershare evebit
def sm_f79_standard_multiples_pershare_63d_accel_v035_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d pershare evebit
def sm_f79_standard_multiples_pershare_63d_accel_v036_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d pershare evebit
def sm_f79_standard_multiples_pershare_126d_accel_v037_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d pershare evebit
def sm_f79_standard_multiples_pershare_126d_accel_v038_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d pershare evebit
def sm_f79_standard_multiples_pershare_126d_accel_v039_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d pershare evebit
def sm_f79_standard_multiples_pershare_252d_accel_v040_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d pershare evebit
def sm_f79_standard_multiples_pershare_252d_accel_v041_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d pershare evebit
def sm_f79_standard_multiples_pershare_252d_accel_v042_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d pershare evebit
def sm_f79_standard_multiples_pershare_504d_accel_v043_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d pershare evebit
def sm_f79_standard_multiples_pershare_504d_accel_v044_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d pershare evebit
def sm_f79_standard_multiples_pershare_504d_accel_v045_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_assets evebit
def sm_f79_standard_multiples_per_assets_21d_accel_v046_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_assets evebit
def sm_f79_standard_multiples_per_assets_21d_accel_v047_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_assets evebit
def sm_f79_standard_multiples_per_assets_21d_accel_v048_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_assets evebit
def sm_f79_standard_multiples_per_assets_63d_accel_v049_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_assets evebit
def sm_f79_standard_multiples_per_assets_63d_accel_v050_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_assets evebit
def sm_f79_standard_multiples_per_assets_63d_accel_v051_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_assets evebit
def sm_f79_standard_multiples_per_assets_126d_accel_v052_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_assets evebit
def sm_f79_standard_multiples_per_assets_126d_accel_v053_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_assets evebit
def sm_f79_standard_multiples_per_assets_126d_accel_v054_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_assets evebit
def sm_f79_standard_multiples_per_assets_252d_accel_v055_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_assets evebit
def sm_f79_standard_multiples_per_assets_252d_accel_v056_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_assets evebit
def sm_f79_standard_multiples_per_assets_252d_accel_v057_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_assets evebit
def sm_f79_standard_multiples_per_assets_504d_accel_v058_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_assets evebit
def sm_f79_standard_multiples_per_assets_504d_accel_v059_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_assets evebit
def sm_f79_standard_multiples_per_assets_504d_accel_v060_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_21d_accel_v061_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_21d_accel_v062_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_21d_accel_v063_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_63d_accel_v064_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_63d_accel_v065_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_63d_accel_v066_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_126d_accel_v067_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_126d_accel_v068_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_126d_accel_v069_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_252d_accel_v070_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_252d_accel_v071_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_252d_accel_v072_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_504d_accel_v073_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_504d_accel_v074_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_504d_accel_v075_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d per_equity evebit
def sm_f79_standard_multiples_per_equity_21d_accel_v076_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d per_equity evebit
def sm_f79_standard_multiples_per_equity_21d_accel_v077_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d per_equity evebit
def sm_f79_standard_multiples_per_equity_21d_accel_v078_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d per_equity evebit
def sm_f79_standard_multiples_per_equity_63d_accel_v079_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d per_equity evebit
def sm_f79_standard_multiples_per_equity_63d_accel_v080_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d per_equity evebit
def sm_f79_standard_multiples_per_equity_63d_accel_v081_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d per_equity evebit
def sm_f79_standard_multiples_per_equity_126d_accel_v082_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d per_equity evebit
def sm_f79_standard_multiples_per_equity_126d_accel_v083_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d per_equity evebit
def sm_f79_standard_multiples_per_equity_126d_accel_v084_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d per_equity evebit
def sm_f79_standard_multiples_per_equity_252d_accel_v085_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d per_equity evebit
def sm_f79_standard_multiples_per_equity_252d_accel_v086_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d per_equity evebit
def sm_f79_standard_multiples_per_equity_252d_accel_v087_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d per_equity evebit
def sm_f79_standard_multiples_per_equity_504d_accel_v088_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d per_equity evebit
def sm_f79_standard_multiples_per_equity_504d_accel_v089_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d per_equity evebit
def sm_f79_standard_multiples_per_equity_504d_accel_v090_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d std evebit
def sm_f79_standard_multiples_std_21d_accel_v091_signal(evebit, closeadj):
    base = _std(evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d std evebit
def sm_f79_standard_multiples_std_21d_accel_v092_signal(evebit, closeadj):
    base = _std(evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d std evebit
def sm_f79_standard_multiples_std_21d_accel_v093_signal(evebit, closeadj):
    base = _std(evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d std evebit
def sm_f79_standard_multiples_std_63d_accel_v094_signal(evebit, closeadj):
    base = _std(evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d std evebit
def sm_f79_standard_multiples_std_63d_accel_v095_signal(evebit, closeadj):
    base = _std(evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d std evebit
def sm_f79_standard_multiples_std_63d_accel_v096_signal(evebit, closeadj):
    base = _std(evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d std evebit
def sm_f79_standard_multiples_std_126d_accel_v097_signal(evebit, closeadj):
    base = _std(evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d std evebit
def sm_f79_standard_multiples_std_126d_accel_v098_signal(evebit, closeadj):
    base = _std(evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d std evebit
def sm_f79_standard_multiples_std_126d_accel_v099_signal(evebit, closeadj):
    base = _std(evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d std evebit
def sm_f79_standard_multiples_std_252d_accel_v100_signal(evebit, closeadj):
    base = _std(evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d std evebit
def sm_f79_standard_multiples_std_252d_accel_v101_signal(evebit, closeadj):
    base = _std(evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d std evebit
def sm_f79_standard_multiples_std_252d_accel_v102_signal(evebit, closeadj):
    base = _std(evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d std evebit
def sm_f79_standard_multiples_std_504d_accel_v103_signal(evebit, closeadj):
    base = _std(evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d std evebit
def sm_f79_standard_multiples_std_504d_accel_v104_signal(evebit, closeadj):
    base = _std(evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d std evebit
def sm_f79_standard_multiples_std_504d_accel_v105_signal(evebit, closeadj):
    base = _std(evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d ewm evebit
def sm_f79_standard_multiples_ewm_21d_accel_v106_signal(evebit, closeadj):
    base = evebit.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d ewm evebit
def sm_f79_standard_multiples_ewm_21d_accel_v107_signal(evebit, closeadj):
    base = evebit.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d ewm evebit
def sm_f79_standard_multiples_ewm_21d_accel_v108_signal(evebit, closeadj):
    base = evebit.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d ewm evebit
def sm_f79_standard_multiples_ewm_63d_accel_v109_signal(evebit, closeadj):
    base = evebit.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d ewm evebit
def sm_f79_standard_multiples_ewm_63d_accel_v110_signal(evebit, closeadj):
    base = evebit.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d ewm evebit
def sm_f79_standard_multiples_ewm_63d_accel_v111_signal(evebit, closeadj):
    base = evebit.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d ewm evebit
def sm_f79_standard_multiples_ewm_126d_accel_v112_signal(evebit, closeadj):
    base = evebit.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d ewm evebit
def sm_f79_standard_multiples_ewm_126d_accel_v113_signal(evebit, closeadj):
    base = evebit.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d ewm evebit
def sm_f79_standard_multiples_ewm_126d_accel_v114_signal(evebit, closeadj):
    base = evebit.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d ewm evebit
def sm_f79_standard_multiples_ewm_252d_accel_v115_signal(evebit, closeadj):
    base = evebit.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d ewm evebit
def sm_f79_standard_multiples_ewm_252d_accel_v116_signal(evebit, closeadj):
    base = evebit.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d ewm evebit
def sm_f79_standard_multiples_ewm_252d_accel_v117_signal(evebit, closeadj):
    base = evebit.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d ewm evebit
def sm_f79_standard_multiples_ewm_504d_accel_v118_signal(evebit, closeadj):
    base = evebit.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d ewm evebit
def sm_f79_standard_multiples_ewm_504d_accel_v119_signal(evebit, closeadj):
    base = evebit.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d ewm evebit
def sm_f79_standard_multiples_ewm_504d_accel_v120_signal(evebit, closeadj):
    base = evebit.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d sq evebit
def sm_f79_standard_multiples_sq_21d_accel_v121_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d sq evebit
def sm_f79_standard_multiples_sq_21d_accel_v122_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d sq evebit
def sm_f79_standard_multiples_sq_21d_accel_v123_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 21) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d sq evebit
def sm_f79_standard_multiples_sq_63d_accel_v124_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d sq evebit
def sm_f79_standard_multiples_sq_63d_accel_v125_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d sq evebit
def sm_f79_standard_multiples_sq_63d_accel_v126_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 63) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d sq evebit
def sm_f79_standard_multiples_sq_126d_accel_v127_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d sq evebit
def sm_f79_standard_multiples_sq_126d_accel_v128_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d sq evebit
def sm_f79_standard_multiples_sq_126d_accel_v129_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 126) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d sq evebit
def sm_f79_standard_multiples_sq_252d_accel_v130_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d sq evebit
def sm_f79_standard_multiples_sq_252d_accel_v131_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d sq evebit
def sm_f79_standard_multiples_sq_252d_accel_v132_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 252) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d sq evebit
def sm_f79_standard_multiples_sq_504d_accel_v133_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d sq evebit
def sm_f79_standard_multiples_sq_504d_accel_v134_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d sq evebit
def sm_f79_standard_multiples_sq_504d_accel_v135_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 504) * closeadj
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 21d z evebit
def sm_f79_standard_multiples_z_21d_accel_v136_signal(evebit):
    base = _z(evebit, 21)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 21d z evebit
def sm_f79_standard_multiples_z_21d_accel_v137_signal(evebit):
    base = _z(evebit, 21)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 21d z evebit
def sm_f79_standard_multiples_z_21d_accel_v138_signal(evebit):
    base = _z(evebit, 21)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 63d z evebit
def sm_f79_standard_multiples_z_63d_accel_v139_signal(evebit):
    base = _z(evebit, 63)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 63d z evebit
def sm_f79_standard_multiples_z_63d_accel_v140_signal(evebit):
    base = _z(evebit, 63)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 63d z evebit
def sm_f79_standard_multiples_z_63d_accel_v141_signal(evebit):
    base = _z(evebit, 63)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 126d z evebit
def sm_f79_standard_multiples_z_126d_accel_v142_signal(evebit):
    base = _z(evebit, 126)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 126d z evebit
def sm_f79_standard_multiples_z_126d_accel_v143_signal(evebit):
    base = _z(evebit, 126)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 126d z evebit
def sm_f79_standard_multiples_z_126d_accel_v144_signal(evebit):
    base = _z(evebit, 126)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 252d z evebit
def sm_f79_standard_multiples_z_252d_accel_v145_signal(evebit):
    base = _z(evebit, 252)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 252d z evebit
def sm_f79_standard_multiples_z_252d_accel_v146_signal(evebit):
    base = _z(evebit, 252)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 252d z evebit
def sm_f79_standard_multiples_z_252d_accel_v147_signal(evebit):
    base = _z(evebit, 252)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d accel of 504d z evebit
def sm_f79_standard_multiples_z_504d_accel_v148_signal(evebit):
    base = _z(evebit, 504)
    slope = _slope_diff_norm(base, 5)
    result = _diff(slope, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d accel of 504d z evebit
def sm_f79_standard_multiples_z_504d_accel_v149_signal(evebit):
    base = _z(evebit, 504)
    slope = _slope_diff_norm(base, 21)
    result = _diff(slope, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d accel of 504d z evebit
def sm_f79_standard_multiples_z_504d_accel_v150_signal(evebit):
    base = _z(evebit, 504)
    slope = _slope_diff_norm(base, 63)
    result = _diff(slope, 63)
    return result.replace([np.inf, -np.inf], np.nan)
