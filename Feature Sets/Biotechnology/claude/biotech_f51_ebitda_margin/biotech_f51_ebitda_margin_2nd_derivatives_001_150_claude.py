"""Family f51 - EBITDA / EBIT margins  (H_Margins) | 2nd derivatives 001-150"""
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
def _ebitda_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _ebitda_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _ebitda_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw ebitda
def em_f51_ebitda_margin_raw_21d_slope_v001_signal(ebitda, closeadj):
    base = _mean(ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw ebitda
def em_f51_ebitda_margin_raw_21d_slope_v002_signal(ebitda, closeadj):
    base = _mean(ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw ebitda
def em_f51_ebitda_margin_raw_21d_slope_v003_signal(ebitda, closeadj):
    base = _mean(ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw ebitda
def em_f51_ebitda_margin_raw_63d_slope_v004_signal(ebitda, closeadj):
    base = _mean(ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw ebitda
def em_f51_ebitda_margin_raw_63d_slope_v005_signal(ebitda, closeadj):
    base = _mean(ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw ebitda
def em_f51_ebitda_margin_raw_63d_slope_v006_signal(ebitda, closeadj):
    base = _mean(ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw ebitda
def em_f51_ebitda_margin_raw_126d_slope_v007_signal(ebitda, closeadj):
    base = _mean(ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw ebitda
def em_f51_ebitda_margin_raw_126d_slope_v008_signal(ebitda, closeadj):
    base = _mean(ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw ebitda
def em_f51_ebitda_margin_raw_126d_slope_v009_signal(ebitda, closeadj):
    base = _mean(ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw ebitda
def em_f51_ebitda_margin_raw_252d_slope_v010_signal(ebitda, closeadj):
    base = _mean(ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw ebitda
def em_f51_ebitda_margin_raw_252d_slope_v011_signal(ebitda, closeadj):
    base = _mean(ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw ebitda
def em_f51_ebitda_margin_raw_252d_slope_v012_signal(ebitda, closeadj):
    base = _mean(ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw ebitda
def em_f51_ebitda_margin_raw_504d_slope_v013_signal(ebitda, closeadj):
    base = _mean(ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw ebitda
def em_f51_ebitda_margin_raw_504d_slope_v014_signal(ebitda, closeadj):
    base = _mean(ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw ebitda
def em_f51_ebitda_margin_raw_504d_slope_v015_signal(ebitda, closeadj):
    base = _mean(ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log ebitda
def em_f51_ebitda_margin_log_21d_slope_v016_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log ebitda
def em_f51_ebitda_margin_log_21d_slope_v017_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log ebitda
def em_f51_ebitda_margin_log_21d_slope_v018_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log ebitda
def em_f51_ebitda_margin_log_63d_slope_v019_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log ebitda
def em_f51_ebitda_margin_log_63d_slope_v020_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log ebitda
def em_f51_ebitda_margin_log_63d_slope_v021_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log ebitda
def em_f51_ebitda_margin_log_126d_slope_v022_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log ebitda
def em_f51_ebitda_margin_log_126d_slope_v023_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log ebitda
def em_f51_ebitda_margin_log_126d_slope_v024_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log ebitda
def em_f51_ebitda_margin_log_252d_slope_v025_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log ebitda
def em_f51_ebitda_margin_log_252d_slope_v026_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log ebitda
def em_f51_ebitda_margin_log_252d_slope_v027_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log ebitda
def em_f51_ebitda_margin_log_504d_slope_v028_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log ebitda
def em_f51_ebitda_margin_log_504d_slope_v029_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log ebitda
def em_f51_ebitda_margin_log_504d_slope_v030_signal(ebitda, closeadj):
    base = _mean(_ebitda_margin_log(ebitda), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare ebitda
def em_f51_ebitda_margin_pershare_21d_slope_v031_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare ebitda
def em_f51_ebitda_margin_pershare_21d_slope_v032_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare ebitda
def em_f51_ebitda_margin_pershare_21d_slope_v033_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare ebitda
def em_f51_ebitda_margin_pershare_63d_slope_v034_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare ebitda
def em_f51_ebitda_margin_pershare_63d_slope_v035_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare ebitda
def em_f51_ebitda_margin_pershare_63d_slope_v036_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare ebitda
def em_f51_ebitda_margin_pershare_126d_slope_v037_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare ebitda
def em_f51_ebitda_margin_pershare_126d_slope_v038_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare ebitda
def em_f51_ebitda_margin_pershare_126d_slope_v039_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare ebitda
def em_f51_ebitda_margin_pershare_252d_slope_v040_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare ebitda
def em_f51_ebitda_margin_pershare_252d_slope_v041_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare ebitda
def em_f51_ebitda_margin_pershare_252d_slope_v042_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare ebitda
def em_f51_ebitda_margin_pershare_504d_slope_v043_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare ebitda
def em_f51_ebitda_margin_pershare_504d_slope_v044_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare ebitda
def em_f51_ebitda_margin_pershare_504d_slope_v045_signal(ebitda, sharesbas, closeadj):
    base = _mean(_ebitda_margin_per_share(ebitda, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets ebitda
def em_f51_ebitda_margin_per_assets_21d_slope_v046_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets ebitda
def em_f51_ebitda_margin_per_assets_21d_slope_v047_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets ebitda
def em_f51_ebitda_margin_per_assets_21d_slope_v048_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets ebitda
def em_f51_ebitda_margin_per_assets_63d_slope_v049_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets ebitda
def em_f51_ebitda_margin_per_assets_63d_slope_v050_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets ebitda
def em_f51_ebitda_margin_per_assets_63d_slope_v051_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets ebitda
def em_f51_ebitda_margin_per_assets_126d_slope_v052_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets ebitda
def em_f51_ebitda_margin_per_assets_126d_slope_v053_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets ebitda
def em_f51_ebitda_margin_per_assets_126d_slope_v054_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets ebitda
def em_f51_ebitda_margin_per_assets_252d_slope_v055_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets ebitda
def em_f51_ebitda_margin_per_assets_252d_slope_v056_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets ebitda
def em_f51_ebitda_margin_per_assets_252d_slope_v057_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets ebitda
def em_f51_ebitda_margin_per_assets_504d_slope_v058_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets ebitda
def em_f51_ebitda_margin_per_assets_504d_slope_v059_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets ebitda
def em_f51_ebitda_margin_per_assets_504d_slope_v060_signal(ebitda, assets):
    base = _mean(_ebitda_margin_scaled(ebitda, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_21d_slope_v061_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_21d_slope_v062_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_21d_slope_v063_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_63d_slope_v064_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_63d_slope_v065_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_63d_slope_v066_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_126d_slope_v067_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_126d_slope_v068_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_126d_slope_v069_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_252d_slope_v070_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_252d_slope_v071_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_252d_slope_v072_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_504d_slope_v073_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_504d_slope_v074_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap ebitda
def em_f51_ebitda_margin_per_marketcap_504d_slope_v075_signal(ebitda, marketcap):
    base = _mean(_ebitda_margin_scaled(ebitda, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity ebitda
def em_f51_ebitda_margin_per_equity_21d_slope_v076_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity ebitda
def em_f51_ebitda_margin_per_equity_21d_slope_v077_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity ebitda
def em_f51_ebitda_margin_per_equity_21d_slope_v078_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity ebitda
def em_f51_ebitda_margin_per_equity_63d_slope_v079_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity ebitda
def em_f51_ebitda_margin_per_equity_63d_slope_v080_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity ebitda
def em_f51_ebitda_margin_per_equity_63d_slope_v081_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity ebitda
def em_f51_ebitda_margin_per_equity_126d_slope_v082_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity ebitda
def em_f51_ebitda_margin_per_equity_126d_slope_v083_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity ebitda
def em_f51_ebitda_margin_per_equity_126d_slope_v084_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity ebitda
def em_f51_ebitda_margin_per_equity_252d_slope_v085_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity ebitda
def em_f51_ebitda_margin_per_equity_252d_slope_v086_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity ebitda
def em_f51_ebitda_margin_per_equity_252d_slope_v087_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity ebitda
def em_f51_ebitda_margin_per_equity_504d_slope_v088_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity ebitda
def em_f51_ebitda_margin_per_equity_504d_slope_v089_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity ebitda
def em_f51_ebitda_margin_per_equity_504d_slope_v090_signal(ebitda, equity):
    base = _mean(_ebitda_margin_scaled(ebitda, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std ebitda
def em_f51_ebitda_margin_std_21d_slope_v091_signal(ebitda, closeadj):
    base = _std(ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std ebitda
def em_f51_ebitda_margin_std_21d_slope_v092_signal(ebitda, closeadj):
    base = _std(ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std ebitda
def em_f51_ebitda_margin_std_21d_slope_v093_signal(ebitda, closeadj):
    base = _std(ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std ebitda
def em_f51_ebitda_margin_std_63d_slope_v094_signal(ebitda, closeadj):
    base = _std(ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std ebitda
def em_f51_ebitda_margin_std_63d_slope_v095_signal(ebitda, closeadj):
    base = _std(ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std ebitda
def em_f51_ebitda_margin_std_63d_slope_v096_signal(ebitda, closeadj):
    base = _std(ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std ebitda
def em_f51_ebitda_margin_std_126d_slope_v097_signal(ebitda, closeadj):
    base = _std(ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std ebitda
def em_f51_ebitda_margin_std_126d_slope_v098_signal(ebitda, closeadj):
    base = _std(ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std ebitda
def em_f51_ebitda_margin_std_126d_slope_v099_signal(ebitda, closeadj):
    base = _std(ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std ebitda
def em_f51_ebitda_margin_std_252d_slope_v100_signal(ebitda, closeadj):
    base = _std(ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std ebitda
def em_f51_ebitda_margin_std_252d_slope_v101_signal(ebitda, closeadj):
    base = _std(ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std ebitda
def em_f51_ebitda_margin_std_252d_slope_v102_signal(ebitda, closeadj):
    base = _std(ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std ebitda
def em_f51_ebitda_margin_std_504d_slope_v103_signal(ebitda, closeadj):
    base = _std(ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std ebitda
def em_f51_ebitda_margin_std_504d_slope_v104_signal(ebitda, closeadj):
    base = _std(ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std ebitda
def em_f51_ebitda_margin_std_504d_slope_v105_signal(ebitda, closeadj):
    base = _std(ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm ebitda
def em_f51_ebitda_margin_ewm_21d_slope_v106_signal(ebitda, closeadj):
    base = ebitda.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm ebitda
def em_f51_ebitda_margin_ewm_21d_slope_v107_signal(ebitda, closeadj):
    base = ebitda.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm ebitda
def em_f51_ebitda_margin_ewm_21d_slope_v108_signal(ebitda, closeadj):
    base = ebitda.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm ebitda
def em_f51_ebitda_margin_ewm_63d_slope_v109_signal(ebitda, closeadj):
    base = ebitda.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm ebitda
def em_f51_ebitda_margin_ewm_63d_slope_v110_signal(ebitda, closeadj):
    base = ebitda.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm ebitda
def em_f51_ebitda_margin_ewm_63d_slope_v111_signal(ebitda, closeadj):
    base = ebitda.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm ebitda
def em_f51_ebitda_margin_ewm_126d_slope_v112_signal(ebitda, closeadj):
    base = ebitda.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm ebitda
def em_f51_ebitda_margin_ewm_126d_slope_v113_signal(ebitda, closeadj):
    base = ebitda.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm ebitda
def em_f51_ebitda_margin_ewm_126d_slope_v114_signal(ebitda, closeadj):
    base = ebitda.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm ebitda
def em_f51_ebitda_margin_ewm_252d_slope_v115_signal(ebitda, closeadj):
    base = ebitda.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm ebitda
def em_f51_ebitda_margin_ewm_252d_slope_v116_signal(ebitda, closeadj):
    base = ebitda.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm ebitda
def em_f51_ebitda_margin_ewm_252d_slope_v117_signal(ebitda, closeadj):
    base = ebitda.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm ebitda
def em_f51_ebitda_margin_ewm_504d_slope_v118_signal(ebitda, closeadj):
    base = ebitda.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm ebitda
def em_f51_ebitda_margin_ewm_504d_slope_v119_signal(ebitda, closeadj):
    base = ebitda.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm ebitda
def em_f51_ebitda_margin_ewm_504d_slope_v120_signal(ebitda, closeadj):
    base = ebitda.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq ebitda
def em_f51_ebitda_margin_sq_21d_slope_v121_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq ebitda
def em_f51_ebitda_margin_sq_21d_slope_v122_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq ebitda
def em_f51_ebitda_margin_sq_21d_slope_v123_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq ebitda
def em_f51_ebitda_margin_sq_63d_slope_v124_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq ebitda
def em_f51_ebitda_margin_sq_63d_slope_v125_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq ebitda
def em_f51_ebitda_margin_sq_63d_slope_v126_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq ebitda
def em_f51_ebitda_margin_sq_126d_slope_v127_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq ebitda
def em_f51_ebitda_margin_sq_126d_slope_v128_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq ebitda
def em_f51_ebitda_margin_sq_126d_slope_v129_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq ebitda
def em_f51_ebitda_margin_sq_252d_slope_v130_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq ebitda
def em_f51_ebitda_margin_sq_252d_slope_v131_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq ebitda
def em_f51_ebitda_margin_sq_252d_slope_v132_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq ebitda
def em_f51_ebitda_margin_sq_504d_slope_v133_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq ebitda
def em_f51_ebitda_margin_sq_504d_slope_v134_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq ebitda
def em_f51_ebitda_margin_sq_504d_slope_v135_signal(ebitda, closeadj):
    base = _mean(ebitda * ebitda, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z ebitda
def em_f51_ebitda_margin_z_21d_slope_v136_signal(ebitda):
    base = _z(ebitda, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z ebitda
def em_f51_ebitda_margin_z_21d_slope_v137_signal(ebitda):
    base = _z(ebitda, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z ebitda
def em_f51_ebitda_margin_z_21d_slope_v138_signal(ebitda):
    base = _z(ebitda, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z ebitda
def em_f51_ebitda_margin_z_63d_slope_v139_signal(ebitda):
    base = _z(ebitda, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z ebitda
def em_f51_ebitda_margin_z_63d_slope_v140_signal(ebitda):
    base = _z(ebitda, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z ebitda
def em_f51_ebitda_margin_z_63d_slope_v141_signal(ebitda):
    base = _z(ebitda, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z ebitda
def em_f51_ebitda_margin_z_126d_slope_v142_signal(ebitda):
    base = _z(ebitda, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z ebitda
def em_f51_ebitda_margin_z_126d_slope_v143_signal(ebitda):
    base = _z(ebitda, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z ebitda
def em_f51_ebitda_margin_z_126d_slope_v144_signal(ebitda):
    base = _z(ebitda, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z ebitda
def em_f51_ebitda_margin_z_252d_slope_v145_signal(ebitda):
    base = _z(ebitda, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z ebitda
def em_f51_ebitda_margin_z_252d_slope_v146_signal(ebitda):
    base = _z(ebitda, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z ebitda
def em_f51_ebitda_margin_z_252d_slope_v147_signal(ebitda):
    base = _z(ebitda, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z ebitda
def em_f51_ebitda_margin_z_504d_slope_v148_signal(ebitda):
    base = _z(ebitda, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z ebitda
def em_f51_ebitda_margin_z_504d_slope_v149_signal(ebitda):
    base = _z(ebitda, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z ebitda
def em_f51_ebitda_margin_z_504d_slope_v150_signal(ebitda):
    base = _z(ebitda, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
