"""Family f50 - Net margin  (H_Margins) | 2nd derivatives 001-150"""
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
def _net_margin_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _net_margin_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _net_margin_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw netmargin
def nm_f50_net_margin_raw_21d_slope_v001_signal(netmargin, closeadj):
    base = _mean(netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw netmargin
def nm_f50_net_margin_raw_21d_slope_v002_signal(netmargin, closeadj):
    base = _mean(netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw netmargin
def nm_f50_net_margin_raw_21d_slope_v003_signal(netmargin, closeadj):
    base = _mean(netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw netmargin
def nm_f50_net_margin_raw_63d_slope_v004_signal(netmargin, closeadj):
    base = _mean(netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw netmargin
def nm_f50_net_margin_raw_63d_slope_v005_signal(netmargin, closeadj):
    base = _mean(netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw netmargin
def nm_f50_net_margin_raw_63d_slope_v006_signal(netmargin, closeadj):
    base = _mean(netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw netmargin
def nm_f50_net_margin_raw_126d_slope_v007_signal(netmargin, closeadj):
    base = _mean(netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw netmargin
def nm_f50_net_margin_raw_126d_slope_v008_signal(netmargin, closeadj):
    base = _mean(netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw netmargin
def nm_f50_net_margin_raw_126d_slope_v009_signal(netmargin, closeadj):
    base = _mean(netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw netmargin
def nm_f50_net_margin_raw_252d_slope_v010_signal(netmargin, closeadj):
    base = _mean(netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw netmargin
def nm_f50_net_margin_raw_252d_slope_v011_signal(netmargin, closeadj):
    base = _mean(netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw netmargin
def nm_f50_net_margin_raw_252d_slope_v012_signal(netmargin, closeadj):
    base = _mean(netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw netmargin
def nm_f50_net_margin_raw_504d_slope_v013_signal(netmargin, closeadj):
    base = _mean(netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw netmargin
def nm_f50_net_margin_raw_504d_slope_v014_signal(netmargin, closeadj):
    base = _mean(netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw netmargin
def nm_f50_net_margin_raw_504d_slope_v015_signal(netmargin, closeadj):
    base = _mean(netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log netmargin
def nm_f50_net_margin_log_21d_slope_v016_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log netmargin
def nm_f50_net_margin_log_21d_slope_v017_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log netmargin
def nm_f50_net_margin_log_21d_slope_v018_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log netmargin
def nm_f50_net_margin_log_63d_slope_v019_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log netmargin
def nm_f50_net_margin_log_63d_slope_v020_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log netmargin
def nm_f50_net_margin_log_63d_slope_v021_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log netmargin
def nm_f50_net_margin_log_126d_slope_v022_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log netmargin
def nm_f50_net_margin_log_126d_slope_v023_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log netmargin
def nm_f50_net_margin_log_126d_slope_v024_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log netmargin
def nm_f50_net_margin_log_252d_slope_v025_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log netmargin
def nm_f50_net_margin_log_252d_slope_v026_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log netmargin
def nm_f50_net_margin_log_252d_slope_v027_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log netmargin
def nm_f50_net_margin_log_504d_slope_v028_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log netmargin
def nm_f50_net_margin_log_504d_slope_v029_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log netmargin
def nm_f50_net_margin_log_504d_slope_v030_signal(netmargin, closeadj):
    base = _mean(_net_margin_log(netmargin), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare netmargin
def nm_f50_net_margin_pershare_21d_slope_v031_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare netmargin
def nm_f50_net_margin_pershare_21d_slope_v032_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare netmargin
def nm_f50_net_margin_pershare_21d_slope_v033_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare netmargin
def nm_f50_net_margin_pershare_63d_slope_v034_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare netmargin
def nm_f50_net_margin_pershare_63d_slope_v035_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare netmargin
def nm_f50_net_margin_pershare_63d_slope_v036_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare netmargin
def nm_f50_net_margin_pershare_126d_slope_v037_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare netmargin
def nm_f50_net_margin_pershare_126d_slope_v038_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare netmargin
def nm_f50_net_margin_pershare_126d_slope_v039_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare netmargin
def nm_f50_net_margin_pershare_252d_slope_v040_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare netmargin
def nm_f50_net_margin_pershare_252d_slope_v041_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare netmargin
def nm_f50_net_margin_pershare_252d_slope_v042_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare netmargin
def nm_f50_net_margin_pershare_504d_slope_v043_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare netmargin
def nm_f50_net_margin_pershare_504d_slope_v044_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare netmargin
def nm_f50_net_margin_pershare_504d_slope_v045_signal(netmargin, sharesbas, closeadj):
    base = _mean(_net_margin_per_share(netmargin, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets netmargin
def nm_f50_net_margin_per_assets_21d_slope_v046_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets netmargin
def nm_f50_net_margin_per_assets_21d_slope_v047_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets netmargin
def nm_f50_net_margin_per_assets_21d_slope_v048_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets netmargin
def nm_f50_net_margin_per_assets_63d_slope_v049_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets netmargin
def nm_f50_net_margin_per_assets_63d_slope_v050_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets netmargin
def nm_f50_net_margin_per_assets_63d_slope_v051_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets netmargin
def nm_f50_net_margin_per_assets_126d_slope_v052_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets netmargin
def nm_f50_net_margin_per_assets_126d_slope_v053_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets netmargin
def nm_f50_net_margin_per_assets_126d_slope_v054_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets netmargin
def nm_f50_net_margin_per_assets_252d_slope_v055_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets netmargin
def nm_f50_net_margin_per_assets_252d_slope_v056_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets netmargin
def nm_f50_net_margin_per_assets_252d_slope_v057_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets netmargin
def nm_f50_net_margin_per_assets_504d_slope_v058_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets netmargin
def nm_f50_net_margin_per_assets_504d_slope_v059_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets netmargin
def nm_f50_net_margin_per_assets_504d_slope_v060_signal(netmargin, assets):
    base = _mean(_net_margin_scaled(netmargin, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_21d_slope_v061_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_21d_slope_v062_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_21d_slope_v063_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_63d_slope_v064_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_63d_slope_v065_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_63d_slope_v066_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_126d_slope_v067_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_126d_slope_v068_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_126d_slope_v069_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_252d_slope_v070_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_252d_slope_v071_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_252d_slope_v072_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_504d_slope_v073_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_504d_slope_v074_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap netmargin
def nm_f50_net_margin_per_marketcap_504d_slope_v075_signal(netmargin, marketcap):
    base = _mean(_net_margin_scaled(netmargin, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_equity netmargin
def nm_f50_net_margin_per_equity_21d_slope_v076_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_equity netmargin
def nm_f50_net_margin_per_equity_21d_slope_v077_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_equity netmargin
def nm_f50_net_margin_per_equity_21d_slope_v078_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_equity netmargin
def nm_f50_net_margin_per_equity_63d_slope_v079_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_equity netmargin
def nm_f50_net_margin_per_equity_63d_slope_v080_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_equity netmargin
def nm_f50_net_margin_per_equity_63d_slope_v081_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_equity netmargin
def nm_f50_net_margin_per_equity_126d_slope_v082_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_equity netmargin
def nm_f50_net_margin_per_equity_126d_slope_v083_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_equity netmargin
def nm_f50_net_margin_per_equity_126d_slope_v084_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_equity netmargin
def nm_f50_net_margin_per_equity_252d_slope_v085_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_equity netmargin
def nm_f50_net_margin_per_equity_252d_slope_v086_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_equity netmargin
def nm_f50_net_margin_per_equity_252d_slope_v087_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_equity netmargin
def nm_f50_net_margin_per_equity_504d_slope_v088_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_equity netmargin
def nm_f50_net_margin_per_equity_504d_slope_v089_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_equity netmargin
def nm_f50_net_margin_per_equity_504d_slope_v090_signal(netmargin, equity):
    base = _mean(_net_margin_scaled(netmargin, equity), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std netmargin
def nm_f50_net_margin_std_21d_slope_v091_signal(netmargin, closeadj):
    base = _std(netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std netmargin
def nm_f50_net_margin_std_21d_slope_v092_signal(netmargin, closeadj):
    base = _std(netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std netmargin
def nm_f50_net_margin_std_21d_slope_v093_signal(netmargin, closeadj):
    base = _std(netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std netmargin
def nm_f50_net_margin_std_63d_slope_v094_signal(netmargin, closeadj):
    base = _std(netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std netmargin
def nm_f50_net_margin_std_63d_slope_v095_signal(netmargin, closeadj):
    base = _std(netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std netmargin
def nm_f50_net_margin_std_63d_slope_v096_signal(netmargin, closeadj):
    base = _std(netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std netmargin
def nm_f50_net_margin_std_126d_slope_v097_signal(netmargin, closeadj):
    base = _std(netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std netmargin
def nm_f50_net_margin_std_126d_slope_v098_signal(netmargin, closeadj):
    base = _std(netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std netmargin
def nm_f50_net_margin_std_126d_slope_v099_signal(netmargin, closeadj):
    base = _std(netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std netmargin
def nm_f50_net_margin_std_252d_slope_v100_signal(netmargin, closeadj):
    base = _std(netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std netmargin
def nm_f50_net_margin_std_252d_slope_v101_signal(netmargin, closeadj):
    base = _std(netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std netmargin
def nm_f50_net_margin_std_252d_slope_v102_signal(netmargin, closeadj):
    base = _std(netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std netmargin
def nm_f50_net_margin_std_504d_slope_v103_signal(netmargin, closeadj):
    base = _std(netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std netmargin
def nm_f50_net_margin_std_504d_slope_v104_signal(netmargin, closeadj):
    base = _std(netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std netmargin
def nm_f50_net_margin_std_504d_slope_v105_signal(netmargin, closeadj):
    base = _std(netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm netmargin
def nm_f50_net_margin_ewm_21d_slope_v106_signal(netmargin, closeadj):
    base = netmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm netmargin
def nm_f50_net_margin_ewm_21d_slope_v107_signal(netmargin, closeadj):
    base = netmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm netmargin
def nm_f50_net_margin_ewm_21d_slope_v108_signal(netmargin, closeadj):
    base = netmargin.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm netmargin
def nm_f50_net_margin_ewm_63d_slope_v109_signal(netmargin, closeadj):
    base = netmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm netmargin
def nm_f50_net_margin_ewm_63d_slope_v110_signal(netmargin, closeadj):
    base = netmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm netmargin
def nm_f50_net_margin_ewm_63d_slope_v111_signal(netmargin, closeadj):
    base = netmargin.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm netmargin
def nm_f50_net_margin_ewm_126d_slope_v112_signal(netmargin, closeadj):
    base = netmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm netmargin
def nm_f50_net_margin_ewm_126d_slope_v113_signal(netmargin, closeadj):
    base = netmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm netmargin
def nm_f50_net_margin_ewm_126d_slope_v114_signal(netmargin, closeadj):
    base = netmargin.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm netmargin
def nm_f50_net_margin_ewm_252d_slope_v115_signal(netmargin, closeadj):
    base = netmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm netmargin
def nm_f50_net_margin_ewm_252d_slope_v116_signal(netmargin, closeadj):
    base = netmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm netmargin
def nm_f50_net_margin_ewm_252d_slope_v117_signal(netmargin, closeadj):
    base = netmargin.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm netmargin
def nm_f50_net_margin_ewm_504d_slope_v118_signal(netmargin, closeadj):
    base = netmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm netmargin
def nm_f50_net_margin_ewm_504d_slope_v119_signal(netmargin, closeadj):
    base = netmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm netmargin
def nm_f50_net_margin_ewm_504d_slope_v120_signal(netmargin, closeadj):
    base = netmargin.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq netmargin
def nm_f50_net_margin_sq_21d_slope_v121_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq netmargin
def nm_f50_net_margin_sq_21d_slope_v122_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq netmargin
def nm_f50_net_margin_sq_21d_slope_v123_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq netmargin
def nm_f50_net_margin_sq_63d_slope_v124_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq netmargin
def nm_f50_net_margin_sq_63d_slope_v125_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq netmargin
def nm_f50_net_margin_sq_63d_slope_v126_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq netmargin
def nm_f50_net_margin_sq_126d_slope_v127_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq netmargin
def nm_f50_net_margin_sq_126d_slope_v128_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq netmargin
def nm_f50_net_margin_sq_126d_slope_v129_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq netmargin
def nm_f50_net_margin_sq_252d_slope_v130_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq netmargin
def nm_f50_net_margin_sq_252d_slope_v131_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq netmargin
def nm_f50_net_margin_sq_252d_slope_v132_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq netmargin
def nm_f50_net_margin_sq_504d_slope_v133_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq netmargin
def nm_f50_net_margin_sq_504d_slope_v134_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq netmargin
def nm_f50_net_margin_sq_504d_slope_v135_signal(netmargin, closeadj):
    base = _mean(netmargin * netmargin, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z netmargin
def nm_f50_net_margin_z_21d_slope_v136_signal(netmargin):
    base = _z(netmargin, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z netmargin
def nm_f50_net_margin_z_21d_slope_v137_signal(netmargin):
    base = _z(netmargin, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z netmargin
def nm_f50_net_margin_z_21d_slope_v138_signal(netmargin):
    base = _z(netmargin, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z netmargin
def nm_f50_net_margin_z_63d_slope_v139_signal(netmargin):
    base = _z(netmargin, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z netmargin
def nm_f50_net_margin_z_63d_slope_v140_signal(netmargin):
    base = _z(netmargin, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z netmargin
def nm_f50_net_margin_z_63d_slope_v141_signal(netmargin):
    base = _z(netmargin, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z netmargin
def nm_f50_net_margin_z_126d_slope_v142_signal(netmargin):
    base = _z(netmargin, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z netmargin
def nm_f50_net_margin_z_126d_slope_v143_signal(netmargin):
    base = _z(netmargin, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z netmargin
def nm_f50_net_margin_z_126d_slope_v144_signal(netmargin):
    base = _z(netmargin, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z netmargin
def nm_f50_net_margin_z_252d_slope_v145_signal(netmargin):
    base = _z(netmargin, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z netmargin
def nm_f50_net_margin_z_252d_slope_v146_signal(netmargin):
    base = _z(netmargin, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z netmargin
def nm_f50_net_margin_z_252d_slope_v147_signal(netmargin):
    base = _z(netmargin, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z netmargin
def nm_f50_net_margin_z_504d_slope_v148_signal(netmargin):
    base = _z(netmargin, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z netmargin
def nm_f50_net_margin_z_504d_slope_v149_signal(netmargin):
    base = _z(netmargin, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z netmargin
def nm_f50_net_margin_z_504d_slope_v150_signal(netmargin):
    base = _z(netmargin, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
