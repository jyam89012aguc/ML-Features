"""Family f79 - EV/EBIT EV/EBITDA P/E P/S  (M_Valuation) | 2nd derivatives 001-150"""
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


# 5d slope of 21d raw evebit
def sm_f79_standard_multiples_raw_21d_slope_v001_signal(evebit, closeadj):
    base = _mean(evebit, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw evebit
def sm_f79_standard_multiples_raw_21d_slope_v002_signal(evebit, closeadj):
    base = _mean(evebit, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw evebit
def sm_f79_standard_multiples_raw_21d_slope_v003_signal(evebit, closeadj):
    base = _mean(evebit, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw evebit
def sm_f79_standard_multiples_raw_63d_slope_v004_signal(evebit, closeadj):
    base = _mean(evebit, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw evebit
def sm_f79_standard_multiples_raw_63d_slope_v005_signal(evebit, closeadj):
    base = _mean(evebit, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw evebit
def sm_f79_standard_multiples_raw_63d_slope_v006_signal(evebit, closeadj):
    base = _mean(evebit, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw evebit
def sm_f79_standard_multiples_raw_126d_slope_v007_signal(evebit, closeadj):
    base = _mean(evebit, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw evebit
def sm_f79_standard_multiples_raw_126d_slope_v008_signal(evebit, closeadj):
    base = _mean(evebit, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw evebit
def sm_f79_standard_multiples_raw_126d_slope_v009_signal(evebit, closeadj):
    base = _mean(evebit, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw evebit
def sm_f79_standard_multiples_raw_252d_slope_v010_signal(evebit, closeadj):
    base = _mean(evebit, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw evebit
def sm_f79_standard_multiples_raw_252d_slope_v011_signal(evebit, closeadj):
    base = _mean(evebit, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw evebit
def sm_f79_standard_multiples_raw_252d_slope_v012_signal(evebit, closeadj):
    base = _mean(evebit, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw evebit
def sm_f79_standard_multiples_raw_504d_slope_v013_signal(evebit, closeadj):
    base = _mean(evebit, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw evebit
def sm_f79_standard_multiples_raw_504d_slope_v014_signal(evebit, closeadj):
    base = _mean(evebit, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw evebit
def sm_f79_standard_multiples_raw_504d_slope_v015_signal(evebit, closeadj):
    base = _mean(evebit, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log evebit
def sm_f79_standard_multiples_log_21d_slope_v016_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log evebit
def sm_f79_standard_multiples_log_21d_slope_v017_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log evebit
def sm_f79_standard_multiples_log_21d_slope_v018_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log evebit
def sm_f79_standard_multiples_log_63d_slope_v019_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log evebit
def sm_f79_standard_multiples_log_63d_slope_v020_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log evebit
def sm_f79_standard_multiples_log_63d_slope_v021_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log evebit
def sm_f79_standard_multiples_log_126d_slope_v022_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log evebit
def sm_f79_standard_multiples_log_126d_slope_v023_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log evebit
def sm_f79_standard_multiples_log_126d_slope_v024_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log evebit
def sm_f79_standard_multiples_log_252d_slope_v025_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log evebit
def sm_f79_standard_multiples_log_252d_slope_v026_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log evebit
def sm_f79_standard_multiples_log_252d_slope_v027_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log evebit
def sm_f79_standard_multiples_log_504d_slope_v028_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log evebit
def sm_f79_standard_multiples_log_504d_slope_v029_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log evebit
def sm_f79_standard_multiples_log_504d_slope_v030_signal(evebit, closeadj):
    base = _mean(_standard_multiples_log(evebit), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare evebit
def sm_f79_standard_multiples_pershare_21d_slope_v031_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare evebit
def sm_f79_standard_multiples_pershare_21d_slope_v032_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare evebit
def sm_f79_standard_multiples_pershare_21d_slope_v033_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare evebit
def sm_f79_standard_multiples_pershare_63d_slope_v034_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare evebit
def sm_f79_standard_multiples_pershare_63d_slope_v035_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare evebit
def sm_f79_standard_multiples_pershare_63d_slope_v036_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare evebit
def sm_f79_standard_multiples_pershare_126d_slope_v037_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare evebit
def sm_f79_standard_multiples_pershare_126d_slope_v038_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare evebit
def sm_f79_standard_multiples_pershare_126d_slope_v039_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare evebit
def sm_f79_standard_multiples_pershare_252d_slope_v040_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare evebit
def sm_f79_standard_multiples_pershare_252d_slope_v041_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare evebit
def sm_f79_standard_multiples_pershare_252d_slope_v042_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare evebit
def sm_f79_standard_multiples_pershare_504d_slope_v043_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare evebit
def sm_f79_standard_multiples_pershare_504d_slope_v044_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare evebit
def sm_f79_standard_multiples_pershare_504d_slope_v045_signal(evebit, sharesbas, closeadj):
    base = _mean(_standard_multiples_per_share(evebit, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets evebit
def sm_f79_standard_multiples_per_assets_21d_slope_v046_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets evebit
def sm_f79_standard_multiples_per_assets_21d_slope_v047_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets evebit
def sm_f79_standard_multiples_per_assets_21d_slope_v048_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets evebit
def sm_f79_standard_multiples_per_assets_63d_slope_v049_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets evebit
def sm_f79_standard_multiples_per_assets_63d_slope_v050_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets evebit
def sm_f79_standard_multiples_per_assets_63d_slope_v051_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets evebit
def sm_f79_standard_multiples_per_assets_126d_slope_v052_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets evebit
def sm_f79_standard_multiples_per_assets_126d_slope_v053_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets evebit
def sm_f79_standard_multiples_per_assets_126d_slope_v054_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets evebit
def sm_f79_standard_multiples_per_assets_252d_slope_v055_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets evebit
def sm_f79_standard_multiples_per_assets_252d_slope_v056_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets evebit
def sm_f79_standard_multiples_per_assets_252d_slope_v057_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets evebit
def sm_f79_standard_multiples_per_assets_504d_slope_v058_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets evebit
def sm_f79_standard_multiples_per_assets_504d_slope_v059_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets evebit
def sm_f79_standard_multiples_per_assets_504d_slope_v060_signal(evebit, assets):
    base = _mean(_standard_multiples_scaled(evebit, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_21d_slope_v061_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_21d_slope_v062_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_21d_slope_v063_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_63d_slope_v064_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_63d_slope_v065_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_63d_slope_v066_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_126d_slope_v067_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_126d_slope_v068_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_126d_slope_v069_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_252d_slope_v070_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_252d_slope_v071_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_252d_slope_v072_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_504d_slope_v073_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_504d_slope_v074_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap evebit
def sm_f79_standard_multiples_per_marketcap_504d_slope_v075_signal(evebit, marketcap):
    base = _mean(_standard_multiples_scaled(evebit, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity evebit
def sm_f79_standard_multiples_per_equity_21d_slope_v076_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity evebit
def sm_f79_standard_multiples_per_equity_21d_slope_v077_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity evebit
def sm_f79_standard_multiples_per_equity_21d_slope_v078_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity evebit
def sm_f79_standard_multiples_per_equity_63d_slope_v079_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity evebit
def sm_f79_standard_multiples_per_equity_63d_slope_v080_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity evebit
def sm_f79_standard_multiples_per_equity_63d_slope_v081_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity evebit
def sm_f79_standard_multiples_per_equity_126d_slope_v082_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity evebit
def sm_f79_standard_multiples_per_equity_126d_slope_v083_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity evebit
def sm_f79_standard_multiples_per_equity_126d_slope_v084_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity evebit
def sm_f79_standard_multiples_per_equity_252d_slope_v085_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity evebit
def sm_f79_standard_multiples_per_equity_252d_slope_v086_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity evebit
def sm_f79_standard_multiples_per_equity_252d_slope_v087_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity evebit
def sm_f79_standard_multiples_per_equity_504d_slope_v088_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity evebit
def sm_f79_standard_multiples_per_equity_504d_slope_v089_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity evebit
def sm_f79_standard_multiples_per_equity_504d_slope_v090_signal(evebit, equity):
    base = _mean(_standard_multiples_scaled(evebit, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std evebit
def sm_f79_standard_multiples_std_21d_slope_v091_signal(evebit, closeadj):
    base = _std(evebit, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std evebit
def sm_f79_standard_multiples_std_21d_slope_v092_signal(evebit, closeadj):
    base = _std(evebit, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std evebit
def sm_f79_standard_multiples_std_21d_slope_v093_signal(evebit, closeadj):
    base = _std(evebit, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std evebit
def sm_f79_standard_multiples_std_63d_slope_v094_signal(evebit, closeadj):
    base = _std(evebit, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std evebit
def sm_f79_standard_multiples_std_63d_slope_v095_signal(evebit, closeadj):
    base = _std(evebit, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std evebit
def sm_f79_standard_multiples_std_63d_slope_v096_signal(evebit, closeadj):
    base = _std(evebit, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std evebit
def sm_f79_standard_multiples_std_126d_slope_v097_signal(evebit, closeadj):
    base = _std(evebit, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std evebit
def sm_f79_standard_multiples_std_126d_slope_v098_signal(evebit, closeadj):
    base = _std(evebit, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std evebit
def sm_f79_standard_multiples_std_126d_slope_v099_signal(evebit, closeadj):
    base = _std(evebit, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std evebit
def sm_f79_standard_multiples_std_252d_slope_v100_signal(evebit, closeadj):
    base = _std(evebit, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std evebit
def sm_f79_standard_multiples_std_252d_slope_v101_signal(evebit, closeadj):
    base = _std(evebit, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std evebit
def sm_f79_standard_multiples_std_252d_slope_v102_signal(evebit, closeadj):
    base = _std(evebit, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std evebit
def sm_f79_standard_multiples_std_504d_slope_v103_signal(evebit, closeadj):
    base = _std(evebit, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std evebit
def sm_f79_standard_multiples_std_504d_slope_v104_signal(evebit, closeadj):
    base = _std(evebit, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std evebit
def sm_f79_standard_multiples_std_504d_slope_v105_signal(evebit, closeadj):
    base = _std(evebit, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm evebit
def sm_f79_standard_multiples_ewm_21d_slope_v106_signal(evebit, closeadj):
    base = evebit.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm evebit
def sm_f79_standard_multiples_ewm_21d_slope_v107_signal(evebit, closeadj):
    base = evebit.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm evebit
def sm_f79_standard_multiples_ewm_21d_slope_v108_signal(evebit, closeadj):
    base = evebit.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm evebit
def sm_f79_standard_multiples_ewm_63d_slope_v109_signal(evebit, closeadj):
    base = evebit.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm evebit
def sm_f79_standard_multiples_ewm_63d_slope_v110_signal(evebit, closeadj):
    base = evebit.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm evebit
def sm_f79_standard_multiples_ewm_63d_slope_v111_signal(evebit, closeadj):
    base = evebit.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm evebit
def sm_f79_standard_multiples_ewm_126d_slope_v112_signal(evebit, closeadj):
    base = evebit.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm evebit
def sm_f79_standard_multiples_ewm_126d_slope_v113_signal(evebit, closeadj):
    base = evebit.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm evebit
def sm_f79_standard_multiples_ewm_126d_slope_v114_signal(evebit, closeadj):
    base = evebit.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm evebit
def sm_f79_standard_multiples_ewm_252d_slope_v115_signal(evebit, closeadj):
    base = evebit.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm evebit
def sm_f79_standard_multiples_ewm_252d_slope_v116_signal(evebit, closeadj):
    base = evebit.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm evebit
def sm_f79_standard_multiples_ewm_252d_slope_v117_signal(evebit, closeadj):
    base = evebit.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm evebit
def sm_f79_standard_multiples_ewm_504d_slope_v118_signal(evebit, closeadj):
    base = evebit.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm evebit
def sm_f79_standard_multiples_ewm_504d_slope_v119_signal(evebit, closeadj):
    base = evebit.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm evebit
def sm_f79_standard_multiples_ewm_504d_slope_v120_signal(evebit, closeadj):
    base = evebit.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq evebit
def sm_f79_standard_multiples_sq_21d_slope_v121_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq evebit
def sm_f79_standard_multiples_sq_21d_slope_v122_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq evebit
def sm_f79_standard_multiples_sq_21d_slope_v123_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq evebit
def sm_f79_standard_multiples_sq_63d_slope_v124_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq evebit
def sm_f79_standard_multiples_sq_63d_slope_v125_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq evebit
def sm_f79_standard_multiples_sq_63d_slope_v126_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq evebit
def sm_f79_standard_multiples_sq_126d_slope_v127_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq evebit
def sm_f79_standard_multiples_sq_126d_slope_v128_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq evebit
def sm_f79_standard_multiples_sq_126d_slope_v129_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq evebit
def sm_f79_standard_multiples_sq_252d_slope_v130_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq evebit
def sm_f79_standard_multiples_sq_252d_slope_v131_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq evebit
def sm_f79_standard_multiples_sq_252d_slope_v132_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq evebit
def sm_f79_standard_multiples_sq_504d_slope_v133_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq evebit
def sm_f79_standard_multiples_sq_504d_slope_v134_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq evebit
def sm_f79_standard_multiples_sq_504d_slope_v135_signal(evebit, closeadj):
    base = _mean(evebit * evebit, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z evebit
def sm_f79_standard_multiples_z_21d_slope_v136_signal(evebit):
    base = _z(evebit, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z evebit
def sm_f79_standard_multiples_z_21d_slope_v137_signal(evebit):
    base = _z(evebit, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z evebit
def sm_f79_standard_multiples_z_21d_slope_v138_signal(evebit):
    base = _z(evebit, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z evebit
def sm_f79_standard_multiples_z_63d_slope_v139_signal(evebit):
    base = _z(evebit, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z evebit
def sm_f79_standard_multiples_z_63d_slope_v140_signal(evebit):
    base = _z(evebit, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z evebit
def sm_f79_standard_multiples_z_63d_slope_v141_signal(evebit):
    base = _z(evebit, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z evebit
def sm_f79_standard_multiples_z_126d_slope_v142_signal(evebit):
    base = _z(evebit, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z evebit
def sm_f79_standard_multiples_z_126d_slope_v143_signal(evebit):
    base = _z(evebit, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z evebit
def sm_f79_standard_multiples_z_126d_slope_v144_signal(evebit):
    base = _z(evebit, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z evebit
def sm_f79_standard_multiples_z_252d_slope_v145_signal(evebit):
    base = _z(evebit, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z evebit
def sm_f79_standard_multiples_z_252d_slope_v146_signal(evebit):
    base = _z(evebit, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z evebit
def sm_f79_standard_multiples_z_252d_slope_v147_signal(evebit):
    base = _z(evebit, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z evebit
def sm_f79_standard_multiples_z_504d_slope_v148_signal(evebit):
    base = _z(evebit, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z evebit
def sm_f79_standard_multiples_z_504d_slope_v149_signal(evebit):
    base = _z(evebit, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z evebit
def sm_f79_standard_multiples_z_504d_slope_v150_signal(evebit):
    base = _z(evebit, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
