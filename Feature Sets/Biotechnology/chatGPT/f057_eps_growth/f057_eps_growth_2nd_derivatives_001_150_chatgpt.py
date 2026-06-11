"""Family f057 - EPS growth and improvement (Earnings and Quality) | Sharadar tables: SF1 | fields: eps, epsdil | 2nd derivatives 001-150"""
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
def _eps_growth_scaled(field, scale):
    return field / scale.replace(0, np.nan).abs()


def _eps_growth_log(field):
    return np.log(field.abs().replace(0, np.nan))


def _eps_growth_per_share(field, sharesbas):
    return field / sharesbas.replace(0, np.nan).abs()


# 5d slope of 21d raw eps
def eg_f057_eps_growth_raw_21d_slope_v001_signal(eps, closeadj):
    base = _mean(eps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d raw eps
def eg_f057_eps_growth_raw_21d_slope_v002_signal(eps, closeadj):
    base = _mean(eps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d raw eps
def eg_f057_eps_growth_raw_21d_slope_v003_signal(eps, closeadj):
    base = _mean(eps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d raw eps
def eg_f057_eps_growth_raw_63d_slope_v004_signal(eps, closeadj):
    base = _mean(eps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d raw eps
def eg_f057_eps_growth_raw_63d_slope_v005_signal(eps, closeadj):
    base = _mean(eps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d raw eps
def eg_f057_eps_growth_raw_63d_slope_v006_signal(eps, closeadj):
    base = _mean(eps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d raw eps
def eg_f057_eps_growth_raw_126d_slope_v007_signal(eps, closeadj):
    base = _mean(eps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d raw eps
def eg_f057_eps_growth_raw_126d_slope_v008_signal(eps, closeadj):
    base = _mean(eps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d raw eps
def eg_f057_eps_growth_raw_126d_slope_v009_signal(eps, closeadj):
    base = _mean(eps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d raw eps
def eg_f057_eps_growth_raw_252d_slope_v010_signal(eps, closeadj):
    base = _mean(eps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d raw eps
def eg_f057_eps_growth_raw_252d_slope_v011_signal(eps, closeadj):
    base = _mean(eps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d raw eps
def eg_f057_eps_growth_raw_252d_slope_v012_signal(eps, closeadj):
    base = _mean(eps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d raw eps
def eg_f057_eps_growth_raw_504d_slope_v013_signal(eps, closeadj):
    base = _mean(eps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d raw eps
def eg_f057_eps_growth_raw_504d_slope_v014_signal(eps, closeadj):
    base = _mean(eps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d raw eps
def eg_f057_eps_growth_raw_504d_slope_v015_signal(eps, closeadj):
    base = _mean(eps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d log eps
def eg_f057_eps_growth_log_21d_slope_v016_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d log eps
def eg_f057_eps_growth_log_21d_slope_v017_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d log eps
def eg_f057_eps_growth_log_21d_slope_v018_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d log eps
def eg_f057_eps_growth_log_63d_slope_v019_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d log eps
def eg_f057_eps_growth_log_63d_slope_v020_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d log eps
def eg_f057_eps_growth_log_63d_slope_v021_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d log eps
def eg_f057_eps_growth_log_126d_slope_v022_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d log eps
def eg_f057_eps_growth_log_126d_slope_v023_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d log eps
def eg_f057_eps_growth_log_126d_slope_v024_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d log eps
def eg_f057_eps_growth_log_252d_slope_v025_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d log eps
def eg_f057_eps_growth_log_252d_slope_v026_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d log eps
def eg_f057_eps_growth_log_252d_slope_v027_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d log eps
def eg_f057_eps_growth_log_504d_slope_v028_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d log eps
def eg_f057_eps_growth_log_504d_slope_v029_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d log eps
def eg_f057_eps_growth_log_504d_slope_v030_signal(eps, closeadj):
    base = _mean(_eps_growth_log(eps), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d pershare eps
def eg_f057_eps_growth_pershare_21d_slope_v031_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d pershare eps
def eg_f057_eps_growth_pershare_21d_slope_v032_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d pershare eps
def eg_f057_eps_growth_pershare_21d_slope_v033_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d pershare eps
def eg_f057_eps_growth_pershare_63d_slope_v034_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d pershare eps
def eg_f057_eps_growth_pershare_63d_slope_v035_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d pershare eps
def eg_f057_eps_growth_pershare_63d_slope_v036_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d pershare eps
def eg_f057_eps_growth_pershare_126d_slope_v037_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d pershare eps
def eg_f057_eps_growth_pershare_126d_slope_v038_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d pershare eps
def eg_f057_eps_growth_pershare_126d_slope_v039_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d pershare eps
def eg_f057_eps_growth_pershare_252d_slope_v040_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d pershare eps
def eg_f057_eps_growth_pershare_252d_slope_v041_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d pershare eps
def eg_f057_eps_growth_pershare_252d_slope_v042_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d pershare eps
def eg_f057_eps_growth_pershare_504d_slope_v043_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d pershare eps
def eg_f057_eps_growth_pershare_504d_slope_v044_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d pershare eps
def eg_f057_eps_growth_pershare_504d_slope_v045_signal(eps, sharesbas, closeadj):
    base = _mean(_eps_growth_per_share(eps, sharesbas), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_21d_slope_v046_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_21d_slope_v047_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_21d_slope_v048_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_63d_slope_v049_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_63d_slope_v050_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_63d_slope_v051_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_126d_slope_v052_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_126d_slope_v053_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_126d_slope_v054_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_252d_slope_v055_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_252d_slope_v056_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_252d_slope_v057_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_504d_slope_v058_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_504d_slope_v059_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_epsdil eps
def eg_f057_eps_growth_per_epsdil_504d_slope_v060_signal(eps, epsdil):
    base = _mean(_eps_growth_scaled(eps, epsdil), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_assets eps
def eg_f057_eps_growth_per_assets_21d_slope_v061_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_assets eps
def eg_f057_eps_growth_per_assets_21d_slope_v062_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_assets eps
def eg_f057_eps_growth_per_assets_21d_slope_v063_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_assets eps
def eg_f057_eps_growth_per_assets_63d_slope_v064_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_assets eps
def eg_f057_eps_growth_per_assets_63d_slope_v065_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_assets eps
def eg_f057_eps_growth_per_assets_63d_slope_v066_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_assets eps
def eg_f057_eps_growth_per_assets_126d_slope_v067_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_assets eps
def eg_f057_eps_growth_per_assets_126d_slope_v068_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_assets eps
def eg_f057_eps_growth_per_assets_126d_slope_v069_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_assets eps
def eg_f057_eps_growth_per_assets_252d_slope_v070_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_assets eps
def eg_f057_eps_growth_per_assets_252d_slope_v071_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_assets eps
def eg_f057_eps_growth_per_assets_252d_slope_v072_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_assets eps
def eg_f057_eps_growth_per_assets_504d_slope_v073_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_assets eps
def eg_f057_eps_growth_per_assets_504d_slope_v074_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_assets eps
def eg_f057_eps_growth_per_assets_504d_slope_v075_signal(eps, assets):
    base = _mean(_eps_growth_scaled(eps, assets), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_21d_slope_v076_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_21d_slope_v077_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_21d_slope_v078_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_63d_slope_v079_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_63d_slope_v080_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_63d_slope_v081_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_126d_slope_v082_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_126d_slope_v083_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_126d_slope_v084_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_252d_slope_v085_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_252d_slope_v086_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_252d_slope_v087_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_504d_slope_v088_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_504d_slope_v089_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d per_marketcap eps
def eg_f057_eps_growth_per_marketcap_504d_slope_v090_signal(eps, marketcap):
    base = _mean(_eps_growth_scaled(eps, marketcap), 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d std eps
def eg_f057_eps_growth_std_21d_slope_v091_signal(eps, closeadj):
    base = _std(eps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d std eps
def eg_f057_eps_growth_std_21d_slope_v092_signal(eps, closeadj):
    base = _std(eps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d std eps
def eg_f057_eps_growth_std_21d_slope_v093_signal(eps, closeadj):
    base = _std(eps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d std eps
def eg_f057_eps_growth_std_63d_slope_v094_signal(eps, closeadj):
    base = _std(eps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d std eps
def eg_f057_eps_growth_std_63d_slope_v095_signal(eps, closeadj):
    base = _std(eps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d std eps
def eg_f057_eps_growth_std_63d_slope_v096_signal(eps, closeadj):
    base = _std(eps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d std eps
def eg_f057_eps_growth_std_126d_slope_v097_signal(eps, closeadj):
    base = _std(eps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d std eps
def eg_f057_eps_growth_std_126d_slope_v098_signal(eps, closeadj):
    base = _std(eps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d std eps
def eg_f057_eps_growth_std_126d_slope_v099_signal(eps, closeadj):
    base = _std(eps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d std eps
def eg_f057_eps_growth_std_252d_slope_v100_signal(eps, closeadj):
    base = _std(eps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d std eps
def eg_f057_eps_growth_std_252d_slope_v101_signal(eps, closeadj):
    base = _std(eps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d std eps
def eg_f057_eps_growth_std_252d_slope_v102_signal(eps, closeadj):
    base = _std(eps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d std eps
def eg_f057_eps_growth_std_504d_slope_v103_signal(eps, closeadj):
    base = _std(eps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d std eps
def eg_f057_eps_growth_std_504d_slope_v104_signal(eps, closeadj):
    base = _std(eps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d std eps
def eg_f057_eps_growth_std_504d_slope_v105_signal(eps, closeadj):
    base = _std(eps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ewm eps
def eg_f057_eps_growth_ewm_21d_slope_v106_signal(eps, closeadj):
    base = eps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d ewm eps
def eg_f057_eps_growth_ewm_21d_slope_v107_signal(eps, closeadj):
    base = eps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d ewm eps
def eg_f057_eps_growth_ewm_21d_slope_v108_signal(eps, closeadj):
    base = eps.ewm(span=21, min_periods=max(1, 21//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d ewm eps
def eg_f057_eps_growth_ewm_63d_slope_v109_signal(eps, closeadj):
    base = eps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ewm eps
def eg_f057_eps_growth_ewm_63d_slope_v110_signal(eps, closeadj):
    base = eps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d ewm eps
def eg_f057_eps_growth_ewm_63d_slope_v111_signal(eps, closeadj):
    base = eps.ewm(span=63, min_periods=max(1, 63//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d ewm eps
def eg_f057_eps_growth_ewm_126d_slope_v112_signal(eps, closeadj):
    base = eps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d ewm eps
def eg_f057_eps_growth_ewm_126d_slope_v113_signal(eps, closeadj):
    base = eps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d ewm eps
def eg_f057_eps_growth_ewm_126d_slope_v114_signal(eps, closeadj):
    base = eps.ewm(span=126, min_periods=max(1, 126//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d ewm eps
def eg_f057_eps_growth_ewm_252d_slope_v115_signal(eps, closeadj):
    base = eps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d ewm eps
def eg_f057_eps_growth_ewm_252d_slope_v116_signal(eps, closeadj):
    base = eps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ewm eps
def eg_f057_eps_growth_ewm_252d_slope_v117_signal(eps, closeadj):
    base = eps.ewm(span=252, min_periods=max(1, 252//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d ewm eps
def eg_f057_eps_growth_ewm_504d_slope_v118_signal(eps, closeadj):
    base = eps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d ewm eps
def eg_f057_eps_growth_ewm_504d_slope_v119_signal(eps, closeadj):
    base = eps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d ewm eps
def eg_f057_eps_growth_ewm_504d_slope_v120_signal(eps, closeadj):
    base = eps.ewm(span=504, min_periods=max(1, 504//2)).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d sq eps
def eg_f057_eps_growth_sq_21d_slope_v121_signal(eps, closeadj):
    base = _mean(eps * eps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d sq eps
def eg_f057_eps_growth_sq_21d_slope_v122_signal(eps, closeadj):
    base = _mean(eps * eps, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d sq eps
def eg_f057_eps_growth_sq_21d_slope_v123_signal(eps, closeadj):
    base = _mean(eps * eps, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d sq eps
def eg_f057_eps_growth_sq_63d_slope_v124_signal(eps, closeadj):
    base = _mean(eps * eps, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d sq eps
def eg_f057_eps_growth_sq_63d_slope_v125_signal(eps, closeadj):
    base = _mean(eps * eps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d sq eps
def eg_f057_eps_growth_sq_63d_slope_v126_signal(eps, closeadj):
    base = _mean(eps * eps, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d sq eps
def eg_f057_eps_growth_sq_126d_slope_v127_signal(eps, closeadj):
    base = _mean(eps * eps, 126) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d sq eps
def eg_f057_eps_growth_sq_126d_slope_v128_signal(eps, closeadj):
    base = _mean(eps * eps, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d sq eps
def eg_f057_eps_growth_sq_126d_slope_v129_signal(eps, closeadj):
    base = _mean(eps * eps, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d sq eps
def eg_f057_eps_growth_sq_252d_slope_v130_signal(eps, closeadj):
    base = _mean(eps * eps, 252) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d sq eps
def eg_f057_eps_growth_sq_252d_slope_v131_signal(eps, closeadj):
    base = _mean(eps * eps, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d sq eps
def eg_f057_eps_growth_sq_252d_slope_v132_signal(eps, closeadj):
    base = _mean(eps * eps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d sq eps
def eg_f057_eps_growth_sq_504d_slope_v133_signal(eps, closeadj):
    base = _mean(eps * eps, 504) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d sq eps
def eg_f057_eps_growth_sq_504d_slope_v134_signal(eps, closeadj):
    base = _mean(eps * eps, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d sq eps
def eg_f057_eps_growth_sq_504d_slope_v135_signal(eps, closeadj):
    base = _mean(eps * eps, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d z eps
def eg_f057_eps_growth_z_21d_slope_v136_signal(eps):
    base = _z(eps, 21)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d z eps
def eg_f057_eps_growth_z_21d_slope_v137_signal(eps):
    base = _z(eps, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 21d z eps
def eg_f057_eps_growth_z_21d_slope_v138_signal(eps):
    base = _z(eps, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d z eps
def eg_f057_eps_growth_z_63d_slope_v139_signal(eps):
    base = _z(eps, 63)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d z eps
def eg_f057_eps_growth_z_63d_slope_v140_signal(eps):
    base = _z(eps, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d z eps
def eg_f057_eps_growth_z_63d_slope_v141_signal(eps):
    base = _z(eps, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 126d z eps
def eg_f057_eps_growth_z_126d_slope_v142_signal(eps):
    base = _z(eps, 126)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d z eps
def eg_f057_eps_growth_z_126d_slope_v143_signal(eps):
    base = _z(eps, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d z eps
def eg_f057_eps_growth_z_126d_slope_v144_signal(eps):
    base = _z(eps, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 252d z eps
def eg_f057_eps_growth_z_252d_slope_v145_signal(eps):
    base = _z(eps, 252)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d z eps
def eg_f057_eps_growth_z_252d_slope_v146_signal(eps):
    base = _z(eps, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d z eps
def eg_f057_eps_growth_z_252d_slope_v147_signal(eps):
    base = _z(eps, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 504d z eps
def eg_f057_eps_growth_z_504d_slope_v148_signal(eps):
    base = _z(eps, 504)
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 504d z eps
def eg_f057_eps_growth_z_504d_slope_v149_signal(eps):
    base = _z(eps, 504)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d z eps
def eg_f057_eps_growth_z_504d_slope_v150_signal(eps):
    base = _z(eps, 504)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)
