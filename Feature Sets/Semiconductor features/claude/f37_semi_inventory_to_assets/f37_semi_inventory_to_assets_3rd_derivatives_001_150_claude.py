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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f37iat_pct_change(s, n=1):
    return s.pct_change(periods=n)


def _f37iat_log_change(s, n=1):
    return np.log(s.replace(0, np.nan).abs() / s.shift(n).replace(0, np.nan).abs())


def _f37iat_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f37iat_diff(a, b):
    return a - b


# 5d curvature of 21d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_21d_curv_v001_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_21d_curv_v002_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_21d_curv_v003_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_21d_curv_v004_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d level of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevel_21d_curv_v005_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d levelrel of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_63d_curv_v006_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d levelrel of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_63d_curv_v007_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d levelrel of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_63d_curv_v008_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d levelrel of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_63d_curv_v009_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d levelrel of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlevelrel_63d_curv_v010_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_126d_curv_v011_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_126d_curv_v012_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_126d_curv_v013_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_126d_curv_v014_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d mean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmean_126d_curv_v015_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d z of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_252d_curv_v016_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d z of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_252d_curv_v017_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d z of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_252d_curv_v018_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d z of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_252d_curv_v019_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d z of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastz_252d_curv_v020_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d robz of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrobz_504d_curv_v021_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d robz of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrobz_504d_curv_v022_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d robz of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrobz_504d_curv_v023_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d robz of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrobz_504d_curv_v024_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d robz of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrobz_504d_curv_v025_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(504, min_periods=252).median()
    mad = (M - med).abs().rolling(504, min_periods=252).median()
    base = (M - med) / (1.4826 * mad).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_21d_curv_v026_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_21d_curv_v027_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_21d_curv_v028_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_21d_curv_v029_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d max of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmax_21d_curv_v030_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_63d_curv_v031_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _min(M, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_63d_curv_v032_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _min(M, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_63d_curv_v033_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _min(M, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_63d_curv_v034_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _min(M, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d min of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastmin_63d_curv_v035_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _min(M, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d rng of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_126d_curv_v036_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d rng of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_126d_curv_v037_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d rng of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_126d_curv_v038_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d rng of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_126d_curv_v039_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d rng of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastrng_126d_curv_v040_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _max(M, 126) - _min(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d pos of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpos_252d_curv_v041_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d pos of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpos_252d_curv_v042_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d pos of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpos_252d_curv_v043_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d pos of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpos_252d_curv_v044_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d pos of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpos_252d_curv_v045_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    lo = _min(M, 252)
    hi = _max(M, 252)
    base = (M - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d dd of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdd_504d_curv_v046_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d dd of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdd_504d_curv_v047_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d dd of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdd_504d_curv_v048_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d dd of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdd_504d_curv_v049_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d dd of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdd_504d_curv_v050_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    peak = _max(M, 504)
    base = M - peak
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d up of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastup_21d_curv_v051_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d up of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastup_21d_curv_v052_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d up of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastup_21d_curv_v053_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d up of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastup_21d_curv_v054_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d up of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastup_21d_curv_v055_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    trough = _min(M, 21)
    base = M - trough
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_63d_curv_v056_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_63d_curv_v057_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_63d_curv_v058_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_63d_curv_v059_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d std of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invaststd_63d_curv_v060_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_126d_curv_v061_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_126d_curv_v062_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_126d_curv_v063_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_126d_curv_v064_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d skew of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastskew_126d_curv_v065_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(126, min_periods=63).skew()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d kurt of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_252d_curv_v066_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d kurt of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_252d_curv_v067_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d kurt of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_252d_curv_v068_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d kurt of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_252d_curv_v069_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d kurt of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastkurt_252d_curv_v070_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.rolling(252, min_periods=126).kurt()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d hits of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_504d_curv_v071_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d hits of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_504d_curv_v072_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d hits of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_504d_curv_v073_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d hits of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_504d_curv_v074_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d hits of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthits_504d_curv_v075_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = (M.diff() > 0).astype(float).rolling(504, min_periods=252).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d signcum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_21d_curv_v076_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d signcum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_21d_curv_v077_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d signcum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_21d_curv_v078_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d signcum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_21d_curv_v079_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d signcum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastsigncum_21d_curv_v080_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = pd.Series(np.sign(M.diff()), index=M.index).rolling(21, min_periods=10).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d cum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_63d_curv_v081_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d cum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_63d_curv_v082_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d cum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_63d_curv_v083_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d cum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_63d_curv_v084_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d cum of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcum_63d_curv_v085_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(63, min_periods=31).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d emafast of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemafast_126d_curv_v086_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d emafast of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemafast_126d_curv_v087_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d emafast of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemafast_126d_curv_v088_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d emafast of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemafast_126d_curv_v089_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d emafast of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemafast_126d_curv_v090_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=63, adjust=False).mean() - M.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d emaslow of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemaslow_252d_curv_v091_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d emaslow of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemaslow_252d_curv_v092_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d emaslow of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemaslow_252d_curv_v093_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d emaslow of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemaslow_252d_curv_v094_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d emaslow of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastemaslow_252d_curv_v095_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.ewm(span=252, adjust=False).mean() - M.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d zabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_504d_curv_v096_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504).abs()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d zabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_504d_curv_v097_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504).abs()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d zabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_504d_curv_v098_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504).abs()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d zabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_504d_curv_v099_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504).abs()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d zabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastzabs_504d_curv_v100_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504).abs()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d posmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_21d_curv_v101_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d posmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_21d_curv_v102_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d posmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_21d_curv_v103_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d posmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_21d_curv_v104_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d posmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastposmean_21d_curv_v105_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d > 0), 21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d negmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_63d_curv_v106_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d negmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_63d_curv_v107_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d negmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_63d_curv_v108_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d negmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_63d_curv_v109_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d negmean of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastnegmean_63d_curv_v110_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    d = M.diff()
    base = _mean(d.where(d < 0), 63)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d cvar of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_126d_curv_v111_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d cvar of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_126d_curv_v112_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d cvar of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_126d_curv_v113_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d cvar of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_126d_curv_v114_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d cvar of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcvar_126d_curv_v115_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _std(M, 126) / _mean(M, 126).replace(0, np.nan)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d logabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlogabs_252d_curv_v116_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d logabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlogabs_252d_curv_v117_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d logabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlogabs_252d_curv_v118_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d logabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlogabs_252d_curv_v119_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d logabs of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastlogabs_252d_curv_v120_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = np.log(M.abs().replace(0, np.nan)).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d diff of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_504d_curv_v121_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff(periods=504)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d diff of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_504d_curv_v122_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff(periods=504)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d diff of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_504d_curv_v123_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff(periods=504)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d diff of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_504d_curv_v124_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff(periods=504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d diff of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastdiff_504d_curv_v125_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff(periods=504)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d pctchg of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_21d_curv_v126_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.pct_change(periods=21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 21d pctchg of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_21d_curv_v127_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.pct_change(periods=21)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 21d pctchg of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_21d_curv_v128_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.pct_change(periods=21)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 21d pctchg of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_21d_curv_v129_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.pct_change(periods=21)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 21d pctchg of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastpctchg_21d_curv_v130_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.pct_change(periods=21)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 63d xover of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastxover_63d_curv_v131_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 63d xover of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastxover_63d_curv_v132_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 63d xover of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastxover_63d_curv_v133_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 63d xover of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastxover_63d_curv_v134_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 63d xover of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastxover_63d_curv_v135_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M - _mean(M, 126)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 126d trend of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_126d_curv_v136_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 126d trend of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_126d_curv_v137_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 126d trend of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_126d_curv_v138_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 126d trend of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_126d_curv_v139_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 126d trend of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasttrend_126d_curv_v140_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = M.diff().rolling(126, min_periods=63).sum()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 252d highmask of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthighmask_252d_curv_v141_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 252d highmask of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthighmask_252d_curv_v142_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d highmask of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthighmask_252d_curv_v143_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 252d highmask of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthighmask_252d_curv_v144_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 252d highmask of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invasthighmask_252d_curv_v145_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    med = M.rolling(252, min_periods=126).median()
    base = (M > med).astype(float).rolling(252, min_periods=126).mean()
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 504d compositez of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcompositez_504d_curv_v146_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d curvature of 504d compositez of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcompositez_504d_curv_v147_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 504d compositez of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcompositez_504d_curv_v148_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d compositez of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcompositez_504d_curv_v149_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d curvature of 504d compositez of inventory to assets ratio
def f37iat_f37_semi_inventory_to_assets_invastcompositez_504d_curv_v150_signal(inventory, assets, closeadj):
    M = _f37iat_ratio(inventory, assets)
    base = _z(M, 504) + _z(M, 252)
    result = _curvature(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


