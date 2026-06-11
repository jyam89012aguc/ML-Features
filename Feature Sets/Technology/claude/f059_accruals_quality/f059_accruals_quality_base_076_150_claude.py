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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f059_accruals(netinc, ncfo):
    return netinc - ncfo


# 63d z-score of accruals
def f059aqq_f059_accruals_quality_accruals_z_63d_base_v076_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of accruals
def f059aqq_f059_accruals_quality_accruals_z_126d_base_v077_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of accruals
def f059aqq_f059_accruals_quality_accruals_z_252d_base_v078_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of accruals
def f059aqq_f059_accruals_quality_accruals_z_504d_base_v079_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_z_63d_base_v080_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_z_126d_base_v081_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_z_252d_base_v082_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_z_504d_base_v083_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_z_63d_base_v084_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_z_126d_base_v085_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_z_252d_base_v086_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_z_504d_base_v087_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_z_63d_base_v088_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_z_126d_base_v089_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_z_252d_base_v090_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_z_504d_base_v091_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_z_63d_base_v092_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_z_126d_base_v093_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_z_252d_base_v094_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_z_504d_base_v095_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_z_63d_base_v096_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_z_126d_base_v097_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_z_252d_base_v098_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_z_504d_base_v099_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_z_63d_base_v100_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_z_126d_base_v101_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_z_252d_base_v102_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_z_504d_base_v103_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of accruals
def f059aqq_f059_accruals_quality_accruals_distmax_252d_base_v104_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of accruals
def f059aqq_f059_accruals_quality_accruals_distmax_504d_base_v105_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_distmax_252d_base_v106_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_distmax_504d_base_v107_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_distmax_252d_base_v108_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_distmax_504d_base_v109_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_distmax_252d_base_v110_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_distmax_504d_base_v111_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_distmax_252d_base_v112_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_distmax_504d_base_v113_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_distmax_252d_base_v114_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_distmax_504d_base_v115_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_distmax_252d_base_v116_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_distmax_504d_base_v117_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of accruals
def f059aqq_f059_accruals_quality_accruals_distmed_126d_base_v118_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of accruals
def f059aqq_f059_accruals_quality_accruals_distmed_252d_base_v119_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of accruals
def f059aqq_f059_accruals_quality_accruals_distmed_504d_base_v120_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_distmed_126d_base_v121_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_distmed_252d_base_v122_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_distmed_504d_base_v123_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_distmed_126d_base_v124_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_distmed_252d_base_v125_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_distmed_504d_base_v126_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_distmed_126d_base_v127_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_distmed_252d_base_v128_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_distmed_504d_base_v129_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_distmed_126d_base_v130_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_distmed_252d_base_v131_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_distmed_504d_base_v132_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_distmed_126d_base_v133_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_distmed_252d_base_v134_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_distmed_504d_base_v135_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_distmed_126d_base_v136_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_distmed_252d_base_v137_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of accruals_z_252
def f059aqq_f059_accruals_quality_accruals_z_252_distmed_504d_base_v138_signal(netinc, ncfo, closeadj):
    base = (_f059_accruals(netinc, ncfo) - _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).mean()) / _f059_accruals(netinc, ncfo).rolling(252, min_periods=63).std().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in accruals
def f059aqq_f059_accruals_quality_accruals_chg_63d_base_v139_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in accruals
def f059aqq_f059_accruals_quality_accruals_chg_252d_base_v140_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_chg_63d_base_v141_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in accruals_to_asset
def f059aqq_f059_accruals_quality_accruals_to_asset_chg_252d_base_v142_signal(netinc, ncfo, assets, closeadj):
    base = _f059_accruals(netinc, ncfo) / assets.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_chg_63d_base_v143_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in accruals_to_rev
def f059aqq_f059_accruals_quality_accruals_to_rev_chg_252d_base_v144_signal(netinc, ncfo, revenue, closeadj):
    base = _f059_accruals(netinc, ncfo) / revenue.abs().replace(0, np.nan)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_chg_63d_base_v145_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in accruals_yoy
def f059aqq_f059_accruals_quality_accruals_yoy_chg_252d_base_v146_signal(netinc, ncfo, closeadj):
    base = _f059_accruals(netinc, ncfo).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_chg_63d_base_v147_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in accruals_sign
def f059aqq_f059_accruals_quality_accruals_sign_chg_252d_base_v148_signal(netinc, ncfo, closeadj):
    base = np.sign(_f059_accruals(netinc, ncfo))
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_chg_63d_base_v149_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in ni_to_ocf_ratio
def f059aqq_f059_accruals_quality_ni_to_ocf_ratio_chg_252d_base_v150_signal(netinc, ncfo, closeadj):
    base = netinc / ncfo.replace(0, np.nan).abs()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

