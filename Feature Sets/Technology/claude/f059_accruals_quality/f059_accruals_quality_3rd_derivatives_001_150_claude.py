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


# 21d acceleration of accruals
def f059aqq_f059_accruals_quality_accruals_accel_21d_3d_v001_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals
def f059aqq_f059_accruals_quality_accruals_accel_63d_3d_v002_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of accruals
def f059aqq_f059_accruals_quality_accruals_accel_126d_3d_v003_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals
def f059aqq_f059_accruals_quality_accruals_accel_252d_3d_v004_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_accel_21d_3d_v005_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_accel_63d_3d_v006_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_accel_126d_3d_v007_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_accel_252d_3d_v008_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_accel_21d_3d_v009_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_accel_63d_3d_v010_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_accel_126d_3d_v011_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_accel_252d_3d_v012_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_accel_21d_3d_v013_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_accel_63d_3d_v014_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_accel_126d_3d_v015_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_accel_252d_3d_v016_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_accel_21d_3d_v017_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_accel_63d_3d_v018_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_accel_126d_3d_v019_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_accel_252d_3d_v020_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_accel_21d_3d_v021_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_accel_63d_3d_v022_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_accel_126d_3d_v023_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_accel_252d_3d_v024_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_accel_21d_3d_v025_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_accel_63d_3d_v026_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_accel_126d_3d_v027_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_accel_252d_3d_v028_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of accruals
def f059aqq_f059_accruals_quality_accruals_slopez_21d_z126_3d_v029_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of accruals
def f059aqq_f059_accruals_quality_accruals_slopez_63d_z252_3d_v030_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of accruals
def f059aqq_f059_accruals_quality_accruals_slopez_126d_z252_3d_v031_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of accruals
def f059aqq_f059_accruals_quality_accruals_slopez_252d_z504_3d_v032_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slopez_21d_z126_3d_v033_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slopez_63d_z252_3d_v034_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slopez_126d_z252_3d_v035_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_slopez_252d_z504_3d_v036_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slopez_21d_z126_3d_v037_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slopez_63d_z252_3d_v038_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slopez_126d_z252_3d_v039_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_slopez_252d_z504_3d_v040_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slopez_21d_z126_3d_v041_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slopez_63d_z252_3d_v042_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slopez_126d_z252_3d_v043_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_slopez_252d_z504_3d_v044_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slopez_21d_z126_3d_v045_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slopez_63d_z252_3d_v046_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slopez_126d_z252_3d_v047_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_slopez_252d_z504_3d_v048_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slopez_21d_z126_3d_v049_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slopez_63d_z252_3d_v050_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slopez_126d_z252_3d_v051_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_slopez_252d_z504_3d_v052_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slopez_21d_z126_3d_v053_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slopez_63d_z252_3d_v054_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slopez_126d_z252_3d_v055_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_slopez_252d_z504_3d_v056_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of accruals
def f059aqq_f059_accruals_quality_accruals_jerk_21d_3d_v057_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of accruals
def f059aqq_f059_accruals_quality_accruals_jerk_63d_3d_v058_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of accruals
def f059aqq_f059_accruals_quality_accruals_jerk_126d_3d_v059_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_jerk_21d_3d_v060_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_jerk_63d_3d_v061_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_jerk_126d_3d_v062_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_jerk_21d_3d_v063_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_jerk_63d_3d_v064_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_jerk_126d_3d_v065_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_jerk_21d_3d_v066_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_jerk_63d_3d_v067_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_jerk_126d_3d_v068_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_jerk_21d_3d_v069_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_jerk_63d_3d_v070_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_jerk_126d_3d_v071_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_jerk_21d_3d_v072_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_jerk_63d_3d_v073_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_jerk_126d_3d_v074_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_jerk_21d_3d_v075_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_jerk_63d_3d_v076_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_jerk_126d_3d_v077_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of accruals smoothed over 252d
def f059aqq_f059_accruals_quality_accruals_smoothaccel_63d_sm252_3d_v078_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of accruals smoothed over 504d
def f059aqq_f059_accruals_quality_accruals_smoothaccel_252d_sm504_3d_v079_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of accruals_to_asset smoothed over 252d
def f059aqq_f059_accruals_quality_accruals_to_asset_smoothaccel_63d_sm252_3d_v080_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of accruals_to_asset smoothed over 504d
def f059aqq_f059_accruals_quality_accruals_to_asset_smoothaccel_252d_sm504_3d_v081_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of accruals_to_rev smoothed over 252d
def f059aqq_f059_accruals_quality_accruals_to_rev_smoothaccel_63d_sm252_3d_v082_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of accruals_to_rev smoothed over 504d
def f059aqq_f059_accruals_quality_accruals_to_rev_smoothaccel_252d_sm504_3d_v083_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of accruals_yoy smoothed over 252d
def f059aqq_f059_accruals_quality_accruals_yoy_smoothaccel_63d_sm252_3d_v084_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of accruals_yoy smoothed over 504d
def f059aqq_f059_accruals_quality_accruals_yoy_smoothaccel_252d_sm504_3d_v085_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of accruals_sign smoothed over 252d
def f059aqq_f059_accruals_quality_accruals_sign_smoothaccel_63d_sm252_3d_v086_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of accruals_sign smoothed over 504d
def f059aqq_f059_accruals_quality_accruals_sign_smoothaccel_252d_sm504_3d_v087_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ni_to_ocf_ratio smoothed over 252d
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_smoothaccel_63d_sm252_3d_v088_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ni_to_ocf_ratio smoothed over 504d
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_smoothaccel_252d_sm504_3d_v089_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of accruals_z_252 smoothed over 252d
def f059aqq_f059_accruals_quality_accruals_z_252_smoothaccel_63d_sm252_3d_v090_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of accruals_z_252 smoothed over 504d
def f059aqq_f059_accruals_quality_accruals_z_252_smoothaccel_252d_sm504_3d_v091_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of accruals
def f059aqq_f059_accruals_quality_accruals_accelz_21d_z252_3d_v092_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of accruals
def f059aqq_f059_accruals_quality_accruals_accelz_63d_z504_3d_v093_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_accelz_21d_z252_3d_v094_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_accelz_63d_z504_3d_v095_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_accelz_21d_z252_3d_v096_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_accelz_63d_z504_3d_v097_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_accelz_21d_z252_3d_v098_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_accelz_63d_z504_3d_v099_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_accelz_21d_z252_3d_v100_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_accelz_63d_z504_3d_v101_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_accelz_21d_z252_3d_v102_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_accelz_63d_z504_3d_v103_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_accelz_21d_z252_3d_v104_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_accelz_63d_z504_3d_v105_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in accruals (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_signflip_63d_3d_v106_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in accruals (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_signflip_252d_3d_v107_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in accruals_to_asset (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_to_asset_signflip_63d_3d_v108_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in accruals_to_asset (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_to_asset_signflip_252d_3d_v109_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in accruals_to_rev (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_to_rev_signflip_63d_3d_v110_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in accruals_to_rev (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_to_rev_signflip_252d_3d_v111_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in accruals_yoy (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_yoy_signflip_63d_3d_v112_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in accruals_yoy (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_yoy_signflip_252d_3d_v113_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in accruals_sign (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_sign_signflip_63d_3d_v114_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in accruals_sign (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_sign_signflip_252d_3d_v115_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ni_to_ocf_ratio (raw count, no price scaling)
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_signflip_63d_3d_v116_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ni_to_ocf_ratio (raw count, no price scaling)
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_signflip_252d_3d_v117_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in accruals_z_252 (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_z_252_signflip_63d_3d_v118_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in accruals_z_252 (raw count, no price scaling)
def f059aqq_f059_accruals_quality_accruals_z_252_signflip_252d_3d_v119_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals normalized by 252d range
def f059aqq_f059_accruals_quality_accruals_rngaccel_63d_r252_3d_v120_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals normalized by 504d range
def f059aqq_f059_accruals_quality_accruals_rngaccel_252d_r504_3d_v121_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_to_asset normalized by 252d range
def f059aqq_f059_accruals_quality_accruals_to_asset_rngaccel_63d_r252_3d_v122_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_to_asset normalized by 504d range
def f059aqq_f059_accruals_quality_accruals_to_asset_rngaccel_252d_r504_3d_v123_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_to_rev normalized by 252d range
def f059aqq_f059_accruals_quality_accruals_to_rev_rngaccel_63d_r252_3d_v124_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_to_rev normalized by 504d range
def f059aqq_f059_accruals_quality_accruals_to_rev_rngaccel_252d_r504_3d_v125_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_yoy normalized by 252d range
def f059aqq_f059_accruals_quality_accruals_yoy_rngaccel_63d_r252_3d_v126_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_yoy normalized by 504d range
def f059aqq_f059_accruals_quality_accruals_yoy_rngaccel_252d_r504_3d_v127_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_sign normalized by 252d range
def f059aqq_f059_accruals_quality_accruals_sign_rngaccel_63d_r252_3d_v128_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_sign normalized by 504d range
def f059aqq_f059_accruals_quality_accruals_sign_rngaccel_252d_r504_3d_v129_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_to_ocf_ratio normalized by 252d range
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_rngaccel_63d_r252_3d_v130_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_to_ocf_ratio normalized by 504d range
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_rngaccel_252d_r504_3d_v131_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of accruals_z_252 normalized by 252d range
def f059aqq_f059_accruals_quality_accruals_z_252_rngaccel_63d_r252_3d_v132_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of accruals_z_252 normalized by 504d range
def f059aqq_f059_accruals_quality_accruals_z_252_rngaccel_252d_r504_3d_v133_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of accruals
def f059aqq_f059_accruals_quality_accruals_cumslope_21d_3d_v134_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of accruals
def f059aqq_f059_accruals_quality_accruals_cumslope_63d_3d_v135_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of accruals
def f059aqq_f059_accruals_quality_accruals_cumslope_252d_3d_v136_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_cumslope_21d_3d_v137_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_cumslope_63d_3d_v138_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_cumslope_252d_3d_v139_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_cumslope_21d_3d_v140_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_cumslope_63d_3d_v141_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_cumslope_252d_3d_v142_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_cumslope_21d_3d_v143_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_cumslope_63d_3d_v144_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_cumslope_252d_3d_v145_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_cumslope_21d_3d_v146_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_cumslope_63d_3d_v147_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_cumslope_252d_3d_v148_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_cumslope_21d_3d_v149_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_cumslope_63d_3d_v150_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

