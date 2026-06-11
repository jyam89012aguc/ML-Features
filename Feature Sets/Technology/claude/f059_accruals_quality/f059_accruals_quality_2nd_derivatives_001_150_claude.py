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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f059_accruals(netinc, ncfo):
    return netinc - ncfo


# 21d slope of accruals
def f059aqq_f059_accruals_quality_accruals_slope_21d_2d_v001_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of accruals
def f059aqq_f059_accruals_quality_accruals_slope_63d_2d_v002_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of accruals
def f059aqq_f059_accruals_quality_accruals_slope_126d_2d_v003_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of accruals
def f059aqq_f059_accruals_quality_accruals_slope_252d_2d_v004_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of accruals
def f059aqq_f059_accruals_quality_accruals_slope_504d_2d_v005_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slope_21d_2d_v006_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slope_63d_2d_v007_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slope_126d_2d_v008_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slope_252d_2d_v009_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slope_504d_2d_v010_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slope_21d_2d_v011_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slope_63d_2d_v012_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slope_126d_2d_v013_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slope_252d_2d_v014_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slope_504d_2d_v015_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slope_21d_2d_v016_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slope_63d_2d_v017_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slope_126d_2d_v018_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slope_252d_2d_v019_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slope_504d_2d_v020_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slope_21d_2d_v021_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slope_63d_2d_v022_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slope_126d_2d_v023_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slope_252d_2d_v024_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slope_504d_2d_v025_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slope_21d_2d_v026_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slope_63d_2d_v027_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slope_126d_2d_v028_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slope_252d_2d_v029_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slope_504d_2d_v030_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slope_21d_2d_v031_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slope_63d_2d_v032_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slope_126d_2d_v033_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slope_252d_2d_v034_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slope_504d_2d_v035_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of accruals
def f059aqq_f059_accruals_quality_accruals_sm21_sl21_2d_v036_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of accruals
def f059aqq_f059_accruals_quality_accruals_sm63_sl21_2d_v037_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of accruals
def f059aqq_f059_accruals_quality_accruals_sm63_sl63_2d_v038_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of accruals
def f059aqq_f059_accruals_quality_accruals_sm252_sl63_2d_v039_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of accruals
def f059aqq_f059_accruals_quality_accruals_sm252_sl126_2d_v040_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_sm21_sl21_2d_v041_signal(netinc, ncfo, assets, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_sm63_sl21_2d_v042_signal(netinc, ncfo, assets, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_sm63_sl63_2d_v043_signal(netinc, ncfo, assets, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_sm252_sl63_2d_v044_signal(netinc, ncfo, assets, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_sm252_sl126_2d_v045_signal(netinc, ncfo, assets, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_sm21_sl21_2d_v046_signal(netinc, ncfo, revenue, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_sm63_sl21_2d_v047_signal(netinc, ncfo, revenue, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_sm63_sl63_2d_v048_signal(netinc, ncfo, revenue, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_sm252_sl63_2d_v049_signal(netinc, ncfo, revenue, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_sm252_sl126_2d_v050_signal(netinc, ncfo, revenue, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_sm21_sl21_2d_v051_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_sm63_sl21_2d_v052_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_sm63_sl63_2d_v053_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_sm252_sl63_2d_v054_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_sm252_sl126_2d_v055_signal(netinc, ncfo, closeadj):
    base = _mean(_f059_accruals(netinc, ncfo).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_sm21_sl21_2d_v056_signal(netinc, ncfo, closeadj):
    base = _mean(np.sign(_f059_accruals(netinc, ncfo)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_sm63_sl21_2d_v057_signal(netinc, ncfo, closeadj):
    base = _mean(np.sign(_f059_accruals(netinc, ncfo)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_sm63_sl63_2d_v058_signal(netinc, ncfo, closeadj):
    base = _mean(np.sign(_f059_accruals(netinc, ncfo)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_sm252_sl63_2d_v059_signal(netinc, ncfo, closeadj):
    base = _mean(np.sign(_f059_accruals(netinc, ncfo)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_sm252_sl126_2d_v060_signal(netinc, ncfo, closeadj):
    base = _mean(np.sign(_f059_accruals(netinc, ncfo)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_sm21_sl21_2d_v061_signal(netinc, ncfo, closeadj):
    base = _mean(netinc / ncfo.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_sm63_sl21_2d_v062_signal(netinc, ncfo, closeadj):
    base = _mean(netinc / ncfo.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_sm63_sl63_2d_v063_signal(netinc, ncfo, closeadj):
    base = _mean(netinc / ncfo.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_sm252_sl63_2d_v064_signal(netinc, ncfo, closeadj):
    base = _mean(netinc / ncfo.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_sm252_sl126_2d_v065_signal(netinc, ncfo, closeadj):
    base = _mean(netinc / ncfo.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_sm21_sl21_2d_v066_signal(netinc, ncfo, closeadj):
    base = _mean((_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_sm63_sl21_2d_v067_signal(netinc, ncfo, closeadj):
    base = _mean((_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_sm63_sl63_2d_v068_signal(netinc, ncfo, closeadj):
    base = _mean((_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_sm252_sl63_2d_v069_signal(netinc, ncfo, closeadj):
    base = _mean((_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_sm252_sl126_2d_v070_signal(netinc, ncfo, closeadj):
    base = _mean((_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of accruals
def f059aqq_f059_accruals_quality_accruals_pctslope_21d_2d_v071_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of accruals
def f059aqq_f059_accruals_quality_accruals_pctslope_63d_2d_v072_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of accruals
def f059aqq_f059_accruals_quality_accruals_pctslope_252d_2d_v073_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_pctslope_21d_2d_v074_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_pctslope_63d_2d_v075_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_pctslope_252d_2d_v076_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_pctslope_21d_2d_v077_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_pctslope_63d_2d_v078_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_pctslope_252d_2d_v079_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_pctslope_21d_2d_v080_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_pctslope_63d_2d_v081_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_pctslope_252d_2d_v082_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_pctslope_21d_2d_v083_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_pctslope_63d_2d_v084_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_pctslope_252d_2d_v085_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_pctslope_21d_2d_v086_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_pctslope_63d_2d_v087_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_pctslope_252d_2d_v088_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_pctslope_21d_2d_v089_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_pctslope_63d_2d_v090_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_pctslope_252d_2d_v091_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of accruals
def f059aqq_f059_accruals_quality_accruals_sgnslope_21d_2d_v092_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of accruals
def f059aqq_f059_accruals_quality_accruals_sgnslope_63d_2d_v093_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of accruals
def f059aqq_f059_accruals_quality_accruals_sgnslope_252d_2d_v094_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_sgnslope_21d_2d_v095_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_sgnslope_63d_2d_v096_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_sgnslope_252d_2d_v097_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_sgnslope_21d_2d_v098_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_sgnslope_63d_2d_v099_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_sgnslope_252d_2d_v100_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_sgnslope_21d_2d_v101_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_sgnslope_63d_2d_v102_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_sgnslope_252d_2d_v103_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_sgnslope_21d_2d_v104_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_sgnslope_63d_2d_v105_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_sgnslope_252d_2d_v106_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_sgnslope_21d_2d_v107_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_sgnslope_63d_2d_v108_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_sgnslope_252d_2d_v109_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_sgnslope_21d_2d_v110_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_sgnslope_63d_2d_v111_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_sgnslope_252d_2d_v112_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of accruals
def f059aqq_f059_accruals_quality_accruals_logmagslope_21d_2d_v113_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of accruals
def f059aqq_f059_accruals_quality_accruals_logmagslope_63d_2d_v114_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of accruals
def f059aqq_f059_accruals_quality_accruals_logmagslope_252d_2d_v115_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_logmagslope_21d_2d_v116_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_logmagslope_63d_2d_v117_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_logmagslope_252d_2d_v118_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_logmagslope_21d_2d_v119_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_logmagslope_63d_2d_v120_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_logmagslope_252d_2d_v121_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_logmagslope_21d_2d_v122_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_logmagslope_63d_2d_v123_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_logmagslope_252d_2d_v124_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_logmagslope_21d_2d_v125_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_logmagslope_63d_2d_v126_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_logmagslope_252d_2d_v127_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_logmagslope_21d_2d_v128_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_logmagslope_63d_2d_v129_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_logmagslope_252d_2d_v130_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_logmagslope_21d_2d_v131_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_logmagslope_63d_2d_v132_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_logmagslope_252d_2d_v133_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|accruals|
def f059aqq_f059_accruals_quality_accruals_logslope_63d_2d_v134_signal(netinc, ncfo, closeadj):
    base = np.log((_f059_accruals(netinc, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|accruals|
def f059aqq_f059_accruals_quality_accruals_logslope_252d_2d_v135_signal(netinc, ncfo, closeadj):
    base = np.log((_f059_accruals(netinc, ncfo)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|accruals_to_asset|
def f059aqq_f059_accruals_quality_accruals_to_asset_logslope_63d_2d_v136_signal(netinc, ncfo, assets, closeadj):
    base = np.log((_f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|accruals_to_asset|
def f059aqq_f059_accruals_quality_accruals_to_asset_logslope_252d_2d_v137_signal(netinc, ncfo, assets, closeadj):
    base = np.log((_f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|accruals_to_rev|
def f059aqq_f059_accruals_quality_accruals_to_rev_logslope_63d_2d_v138_signal(netinc, ncfo, revenue, closeadj):
    base = np.log((_f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|accruals_to_rev|
def f059aqq_f059_accruals_quality_accruals_to_rev_logslope_252d_2d_v139_signal(netinc, ncfo, revenue, closeadj):
    base = np.log((_f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|accruals_yoy|
def f059aqq_f059_accruals_quality_accruals_yoy_logslope_63d_2d_v140_signal(netinc, ncfo, closeadj):
    base = np.log((_f059_accruals(netinc, ncfo).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|accruals_yoy|
def f059aqq_f059_accruals_quality_accruals_yoy_logslope_252d_2d_v141_signal(netinc, ncfo, closeadj):
    base = np.log((_f059_accruals(netinc, ncfo).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|accruals_sign|
def f059aqq_f059_accruals_quality_accruals_sign_logslope_63d_2d_v142_signal(netinc, ncfo, closeadj):
    base = np.log((np.sign(_f059_accruals(netinc, ncfo))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|accruals_sign|
def f059aqq_f059_accruals_quality_accruals_sign_logslope_252d_2d_v143_signal(netinc, ncfo, closeadj):
    base = np.log((np.sign(_f059_accruals(netinc, ncfo))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ni_to_ocf_ratio|
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_logslope_63d_2d_v144_signal(netinc, ncfo, closeadj):
    base = np.log((netinc / ncfo.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ni_to_ocf_ratio|
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_logslope_252d_2d_v145_signal(netinc, ncfo, closeadj):
    base = np.log((netinc / ncfo.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|accruals_z_252|
def f059aqq_f059_accruals_quality_accruals_z_252_logslope_63d_2d_v146_signal(netinc, ncfo, closeadj):
    base = np.log(((_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|accruals_z_252|
def f059aqq_f059_accruals_quality_accruals_z_252_logslope_252d_2d_v147_signal(netinc, ncfo, closeadj):
    base = np.log(((_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

