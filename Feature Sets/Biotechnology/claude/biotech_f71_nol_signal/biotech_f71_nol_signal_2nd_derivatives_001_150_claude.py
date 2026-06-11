"""Family f71 - Tax position / NOL signal  (L_EarningsQuality) | 2nd derivatives 001-150"""
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
def _nol_signal_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _nol_signal_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _nol_signal_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw taxexp
def nol_f71_nol_signal_raw_21d_slope_v001_signal(taxexp, closeadj):
    base = _mean(taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw taxexp
def nol_f71_nol_signal_raw_21d_slope_v002_signal(taxexp, closeadj):
    base = _mean(taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw taxexp
def nol_f71_nol_signal_raw_21d_slope_v003_signal(taxexp, closeadj):
    base = _mean(taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw taxexp
def nol_f71_nol_signal_raw_63d_slope_v004_signal(taxexp, closeadj):
    base = _mean(taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw taxexp
def nol_f71_nol_signal_raw_63d_slope_v005_signal(taxexp, closeadj):
    base = _mean(taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw taxexp
def nol_f71_nol_signal_raw_63d_slope_v006_signal(taxexp, closeadj):
    base = _mean(taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw taxexp
def nol_f71_nol_signal_raw_126d_slope_v007_signal(taxexp, closeadj):
    base = _mean(taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw taxexp
def nol_f71_nol_signal_raw_126d_slope_v008_signal(taxexp, closeadj):
    base = _mean(taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw taxexp
def nol_f71_nol_signal_raw_126d_slope_v009_signal(taxexp, closeadj):
    base = _mean(taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw taxexp
def nol_f71_nol_signal_raw_252d_slope_v010_signal(taxexp, closeadj):
    base = _mean(taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw taxexp
def nol_f71_nol_signal_raw_252d_slope_v011_signal(taxexp, closeadj):
    base = _mean(taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw taxexp
def nol_f71_nol_signal_raw_252d_slope_v012_signal(taxexp, closeadj):
    base = _mean(taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw taxexp
def nol_f71_nol_signal_raw_504d_slope_v013_signal(taxexp, closeadj):
    base = _mean(taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw taxexp
def nol_f71_nol_signal_raw_504d_slope_v014_signal(taxexp, closeadj):
    base = _mean(taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw taxexp
def nol_f71_nol_signal_raw_504d_slope_v015_signal(taxexp, closeadj):
    base = _mean(taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log taxexp
def nol_f71_nol_signal_log_21d_slope_v016_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log taxexp
def nol_f71_nol_signal_log_21d_slope_v017_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log taxexp
def nol_f71_nol_signal_log_21d_slope_v018_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log taxexp
def nol_f71_nol_signal_log_63d_slope_v019_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log taxexp
def nol_f71_nol_signal_log_63d_slope_v020_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log taxexp
def nol_f71_nol_signal_log_63d_slope_v021_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log taxexp
def nol_f71_nol_signal_log_126d_slope_v022_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log taxexp
def nol_f71_nol_signal_log_126d_slope_v023_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log taxexp
def nol_f71_nol_signal_log_126d_slope_v024_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log taxexp
def nol_f71_nol_signal_log_252d_slope_v025_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log taxexp
def nol_f71_nol_signal_log_252d_slope_v026_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log taxexp
def nol_f71_nol_signal_log_252d_slope_v027_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log taxexp
def nol_f71_nol_signal_log_504d_slope_v028_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log taxexp
def nol_f71_nol_signal_log_504d_slope_v029_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log taxexp
def nol_f71_nol_signal_log_504d_slope_v030_signal(taxexp, closeadj):
    base = _mean(_nol_signal_log(taxexp), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare taxexp
def nol_f71_nol_signal_pershare_21d_slope_v031_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare taxexp
def nol_f71_nol_signal_pershare_21d_slope_v032_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare taxexp
def nol_f71_nol_signal_pershare_21d_slope_v033_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare taxexp
def nol_f71_nol_signal_pershare_63d_slope_v034_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare taxexp
def nol_f71_nol_signal_pershare_63d_slope_v035_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare taxexp
def nol_f71_nol_signal_pershare_63d_slope_v036_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare taxexp
def nol_f71_nol_signal_pershare_126d_slope_v037_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare taxexp
def nol_f71_nol_signal_pershare_126d_slope_v038_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare taxexp
def nol_f71_nol_signal_pershare_126d_slope_v039_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare taxexp
def nol_f71_nol_signal_pershare_252d_slope_v040_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare taxexp
def nol_f71_nol_signal_pershare_252d_slope_v041_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare taxexp
def nol_f71_nol_signal_pershare_252d_slope_v042_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare taxexp
def nol_f71_nol_signal_pershare_504d_slope_v043_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare taxexp
def nol_f71_nol_signal_pershare_504d_slope_v044_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare taxexp
def nol_f71_nol_signal_pershare_504d_slope_v045_signal(taxexp, sharesbas, closeadj):
    base = _mean(_nol_signal_per_share(taxexp, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets taxexp
def nol_f71_nol_signal_per_assets_21d_slope_v046_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets taxexp
def nol_f71_nol_signal_per_assets_21d_slope_v047_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets taxexp
def nol_f71_nol_signal_per_assets_21d_slope_v048_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets taxexp
def nol_f71_nol_signal_per_assets_63d_slope_v049_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets taxexp
def nol_f71_nol_signal_per_assets_63d_slope_v050_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets taxexp
def nol_f71_nol_signal_per_assets_63d_slope_v051_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets taxexp
def nol_f71_nol_signal_per_assets_126d_slope_v052_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets taxexp
def nol_f71_nol_signal_per_assets_126d_slope_v053_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets taxexp
def nol_f71_nol_signal_per_assets_126d_slope_v054_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets taxexp
def nol_f71_nol_signal_per_assets_252d_slope_v055_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets taxexp
def nol_f71_nol_signal_per_assets_252d_slope_v056_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets taxexp
def nol_f71_nol_signal_per_assets_252d_slope_v057_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets taxexp
def nol_f71_nol_signal_per_assets_504d_slope_v058_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets taxexp
def nol_f71_nol_signal_per_assets_504d_slope_v059_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets taxexp
def nol_f71_nol_signal_per_assets_504d_slope_v060_signal(taxexp, assets):
    base = _mean(_nol_signal_scaled(taxexp, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_21d_slope_v061_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_21d_slope_v062_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_21d_slope_v063_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_63d_slope_v064_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_63d_slope_v065_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_63d_slope_v066_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_126d_slope_v067_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_126d_slope_v068_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_126d_slope_v069_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_252d_slope_v070_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_252d_slope_v071_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_252d_slope_v072_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_504d_slope_v073_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_504d_slope_v074_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap taxexp
def nol_f71_nol_signal_per_marketcap_504d_slope_v075_signal(taxexp, marketcap):
    base = _mean(_nol_signal_scaled(taxexp, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity taxexp
def nol_f71_nol_signal_per_equity_21d_slope_v076_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity taxexp
def nol_f71_nol_signal_per_equity_21d_slope_v077_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity taxexp
def nol_f71_nol_signal_per_equity_21d_slope_v078_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity taxexp
def nol_f71_nol_signal_per_equity_63d_slope_v079_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity taxexp
def nol_f71_nol_signal_per_equity_63d_slope_v080_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity taxexp
def nol_f71_nol_signal_per_equity_63d_slope_v081_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity taxexp
def nol_f71_nol_signal_per_equity_126d_slope_v082_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity taxexp
def nol_f71_nol_signal_per_equity_126d_slope_v083_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity taxexp
def nol_f71_nol_signal_per_equity_126d_slope_v084_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity taxexp
def nol_f71_nol_signal_per_equity_252d_slope_v085_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity taxexp
def nol_f71_nol_signal_per_equity_252d_slope_v086_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity taxexp
def nol_f71_nol_signal_per_equity_252d_slope_v087_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity taxexp
def nol_f71_nol_signal_per_equity_504d_slope_v088_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity taxexp
def nol_f71_nol_signal_per_equity_504d_slope_v089_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity taxexp
def nol_f71_nol_signal_per_equity_504d_slope_v090_signal(taxexp, equity):
    base = _mean(_nol_signal_scaled(taxexp, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std taxexp
def nol_f71_nol_signal_std_21d_slope_v091_signal(taxexp, closeadj):
    base = _std(taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std taxexp
def nol_f71_nol_signal_std_21d_slope_v092_signal(taxexp, closeadj):
    base = _std(taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std taxexp
def nol_f71_nol_signal_std_21d_slope_v093_signal(taxexp, closeadj):
    base = _std(taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std taxexp
def nol_f71_nol_signal_std_63d_slope_v094_signal(taxexp, closeadj):
    base = _std(taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std taxexp
def nol_f71_nol_signal_std_63d_slope_v095_signal(taxexp, closeadj):
    base = _std(taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std taxexp
def nol_f71_nol_signal_std_63d_slope_v096_signal(taxexp, closeadj):
    base = _std(taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std taxexp
def nol_f71_nol_signal_std_126d_slope_v097_signal(taxexp, closeadj):
    base = _std(taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std taxexp
def nol_f71_nol_signal_std_126d_slope_v098_signal(taxexp, closeadj):
    base = _std(taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std taxexp
def nol_f71_nol_signal_std_126d_slope_v099_signal(taxexp, closeadj):
    base = _std(taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std taxexp
def nol_f71_nol_signal_std_252d_slope_v100_signal(taxexp, closeadj):
    base = _std(taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std taxexp
def nol_f71_nol_signal_std_252d_slope_v101_signal(taxexp, closeadj):
    base = _std(taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std taxexp
def nol_f71_nol_signal_std_252d_slope_v102_signal(taxexp, closeadj):
    base = _std(taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std taxexp
def nol_f71_nol_signal_std_504d_slope_v103_signal(taxexp, closeadj):
    base = _std(taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std taxexp
def nol_f71_nol_signal_std_504d_slope_v104_signal(taxexp, closeadj):
    base = _std(taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std taxexp
def nol_f71_nol_signal_std_504d_slope_v105_signal(taxexp, closeadj):
    base = _std(taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm taxexp
def nol_f71_nol_signal_ewm_21d_slope_v106_signal(taxexp, closeadj):
    base = taxexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm taxexp
def nol_f71_nol_signal_ewm_21d_slope_v107_signal(taxexp, closeadj):
    base = taxexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm taxexp
def nol_f71_nol_signal_ewm_21d_slope_v108_signal(taxexp, closeadj):
    base = taxexp.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm taxexp
def nol_f71_nol_signal_ewm_63d_slope_v109_signal(taxexp, closeadj):
    base = taxexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm taxexp
def nol_f71_nol_signal_ewm_63d_slope_v110_signal(taxexp, closeadj):
    base = taxexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm taxexp
def nol_f71_nol_signal_ewm_63d_slope_v111_signal(taxexp, closeadj):
    base = taxexp.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm taxexp
def nol_f71_nol_signal_ewm_126d_slope_v112_signal(taxexp, closeadj):
    base = taxexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm taxexp
def nol_f71_nol_signal_ewm_126d_slope_v113_signal(taxexp, closeadj):
    base = taxexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm taxexp
def nol_f71_nol_signal_ewm_126d_slope_v114_signal(taxexp, closeadj):
    base = taxexp.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm taxexp
def nol_f71_nol_signal_ewm_252d_slope_v115_signal(taxexp, closeadj):
    base = taxexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm taxexp
def nol_f71_nol_signal_ewm_252d_slope_v116_signal(taxexp, closeadj):
    base = taxexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm taxexp
def nol_f71_nol_signal_ewm_252d_slope_v117_signal(taxexp, closeadj):
    base = taxexp.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm taxexp
def nol_f71_nol_signal_ewm_504d_slope_v118_signal(taxexp, closeadj):
    base = taxexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm taxexp
def nol_f71_nol_signal_ewm_504d_slope_v119_signal(taxexp, closeadj):
    base = taxexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm taxexp
def nol_f71_nol_signal_ewm_504d_slope_v120_signal(taxexp, closeadj):
    base = taxexp.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq taxexp
def nol_f71_nol_signal_sq_21d_slope_v121_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq taxexp
def nol_f71_nol_signal_sq_21d_slope_v122_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq taxexp
def nol_f71_nol_signal_sq_21d_slope_v123_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq taxexp
def nol_f71_nol_signal_sq_63d_slope_v124_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq taxexp
def nol_f71_nol_signal_sq_63d_slope_v125_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq taxexp
def nol_f71_nol_signal_sq_63d_slope_v126_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq taxexp
def nol_f71_nol_signal_sq_126d_slope_v127_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq taxexp
def nol_f71_nol_signal_sq_126d_slope_v128_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq taxexp
def nol_f71_nol_signal_sq_126d_slope_v129_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq taxexp
def nol_f71_nol_signal_sq_252d_slope_v130_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq taxexp
def nol_f71_nol_signal_sq_252d_slope_v131_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq taxexp
def nol_f71_nol_signal_sq_252d_slope_v132_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq taxexp
def nol_f71_nol_signal_sq_504d_slope_v133_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq taxexp
def nol_f71_nol_signal_sq_504d_slope_v134_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq taxexp
def nol_f71_nol_signal_sq_504d_slope_v135_signal(taxexp, closeadj):
    base = _mean(taxexp * taxexp, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z taxexp
def nol_f71_nol_signal_z_21d_slope_v136_signal(taxexp):
    base = _z(taxexp, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z taxexp
def nol_f71_nol_signal_z_21d_slope_v137_signal(taxexp):
    base = _z(taxexp, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z taxexp
def nol_f71_nol_signal_z_21d_slope_v138_signal(taxexp):
    base = _z(taxexp, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z taxexp
def nol_f71_nol_signal_z_63d_slope_v139_signal(taxexp):
    base = _z(taxexp, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z taxexp
def nol_f71_nol_signal_z_63d_slope_v140_signal(taxexp):
    base = _z(taxexp, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z taxexp
def nol_f71_nol_signal_z_63d_slope_v141_signal(taxexp):
    base = _z(taxexp, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z taxexp
def nol_f71_nol_signal_z_126d_slope_v142_signal(taxexp):
    base = _z(taxexp, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z taxexp
def nol_f71_nol_signal_z_126d_slope_v143_signal(taxexp):
    base = _z(taxexp, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z taxexp
def nol_f71_nol_signal_z_126d_slope_v144_signal(taxexp):
    base = _z(taxexp, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z taxexp
def nol_f71_nol_signal_z_252d_slope_v145_signal(taxexp):
    base = _z(taxexp, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z taxexp
def nol_f71_nol_signal_z_252d_slope_v146_signal(taxexp):
    base = _z(taxexp, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z taxexp
def nol_f71_nol_signal_z_252d_slope_v147_signal(taxexp):
    base = _z(taxexp, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z taxexp
def nol_f71_nol_signal_z_504d_slope_v148_signal(taxexp):
    base = _z(taxexp, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z taxexp
def nol_f71_nol_signal_z_504d_slope_v149_signal(taxexp):
    base = _z(taxexp, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z taxexp
def nol_f71_nol_signal_z_504d_slope_v150_signal(taxexp):
    base = _z(taxexp, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
