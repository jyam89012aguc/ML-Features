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
def _f078_ttm_minus_ann(ttm, ann):
    return (ttm - ann) / ann.replace(0, np.nan).abs()


# 21d acceleration of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_accel_21d_3d_v001_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_accel_63d_3d_v002_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_accel_126d_3d_v003_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_accel_252d_3d_v004_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_accel_21d_3d_v005_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_accel_63d_3d_v006_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_accel_126d_3d_v007_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_accel_252d_3d_v008_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_accel_21d_3d_v009_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_accel_63d_3d_v010_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_accel_126d_3d_v011_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_accel_252d_3d_v012_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_accel_21d_3d_v013_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_accel_63d_3d_v014_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_accel_126d_3d_v015_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_accel_252d_3d_v016_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_accel_21d_3d_v017_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_accel_63d_3d_v018_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_accel_126d_3d_v019_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_accel_252d_3d_v020_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_accel_21d_3d_v021_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_accel_63d_3d_v022_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_accel_126d_3d_v023_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_accel_252d_3d_v024_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_accel_21d_3d_v025_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_accel_63d_3d_v026_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_accel_126d_3d_v027_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_accel_252d_3d_v028_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_slopez_21d_z126_3d_v029_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_slopez_63d_z252_3d_v030_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_slopez_126d_z252_3d_v031_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_slopez_252d_z504_3d_v032_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_slopez_21d_z126_3d_v033_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_slopez_63d_z252_3d_v034_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_slopez_126d_z252_3d_v035_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_slopez_252d_z504_3d_v036_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_slopez_21d_z126_3d_v037_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_slopez_63d_z252_3d_v038_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_slopez_126d_z252_3d_v039_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_slopez_252d_z504_3d_v040_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_slopez_21d_z126_3d_v041_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_slopez_63d_z252_3d_v042_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_slopez_126d_z252_3d_v043_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_slopez_252d_z504_3d_v044_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_slopez_21d_z126_3d_v045_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_slopez_63d_z252_3d_v046_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_slopez_126d_z252_3d_v047_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_slopez_252d_z504_3d_v048_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_slopez_21d_z126_3d_v049_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_slopez_63d_z252_3d_v050_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_slopez_126d_z252_3d_v051_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_slopez_252d_z504_3d_v052_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_slopez_21d_z126_3d_v053_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_slopez_63d_z252_3d_v054_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_slopez_126d_z252_3d_v055_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_slopez_252d_z504_3d_v056_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_jerk_21d_3d_v057_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_jerk_63d_3d_v058_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_jerk_126d_3d_v059_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_jerk_21d_3d_v060_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_jerk_63d_3d_v061_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_jerk_126d_3d_v062_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_jerk_21d_3d_v063_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_jerk_63d_3d_v064_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_jerk_126d_3d_v065_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_jerk_21d_3d_v066_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_jerk_63d_3d_v067_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_jerk_126d_3d_v068_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_jerk_21d_3d_v069_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_jerk_63d_3d_v070_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_jerk_126d_3d_v071_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_jerk_21d_3d_v072_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_jerk_63d_3d_v073_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_jerk_126d_3d_v074_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_jerk_21d_3d_v075_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_jerk_63d_3d_v076_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_jerk_126d_3d_v077_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_smoothed_252 smoothed over 252d
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_smoothaccel_63d_sm252_3d_v078_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_smoothed_252 smoothed over 504d
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_smoothaccel_252d_sm504_3d_v079_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_vs_rolling_y smoothed over 252d
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_smoothaccel_63d_sm252_3d_v080_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_vs_rolling_y smoothed over 504d
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_smoothaccel_252d_sm504_3d_v081_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_vs_rolling_y smoothed over 252d
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_smoothaccel_63d_sm252_3d_v082_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_vs_rolling_y smoothed over 504d
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_smoothaccel_252d_sm504_3d_v083_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ni_vs_rolling_y smoothed over 252d
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_smoothaccel_63d_sm252_3d_v084_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ni_vs_rolling_y smoothed over 504d
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_smoothaccel_252d_sm504_3d_v085_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rnd_vs_rolling_y smoothed over 252d
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_smoothaccel_63d_sm252_3d_v086_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rnd_vs_rolling_y smoothed over 504d
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_smoothaccel_252d_sm504_3d_v087_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_smoothing_disp smoothed over 252d
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_smoothaccel_63d_sm252_3d_v088_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_smoothing_disp smoothed over 504d
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_smoothaccel_252d_sm504_3d_v089_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of composite_consistency smoothed over 252d
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_smoothaccel_63d_sm252_3d_v090_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of composite_consistency smoothed over 504d
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_smoothaccel_252d_sm504_3d_v091_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_accelz_21d_z252_3d_v092_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_accelz_63d_z504_3d_v093_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_accelz_21d_z252_3d_v094_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_accelz_63d_z504_3d_v095_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_accelz_21d_z252_3d_v096_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_accelz_63d_z504_3d_v097_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_accelz_21d_z252_3d_v098_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_accelz_63d_z504_3d_v099_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_accelz_21d_z252_3d_v100_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_accelz_63d_z504_3d_v101_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_accelz_21d_z252_3d_v102_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_accelz_63d_z504_3d_v103_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_accelz_21d_z252_3d_v104_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of composite_consistency
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_accelz_63d_z504_3d_v105_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_smoothed_252 (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_signflip_63d_3d_v106_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_smoothed_252 (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_signflip_252d_3d_v107_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_vs_rolling_y (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_signflip_63d_3d_v108_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_vs_rolling_y (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_signflip_252d_3d_v109_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_vs_rolling_y (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_signflip_63d_3d_v110_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_vs_rolling_y (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_signflip_252d_3d_v111_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ni_vs_rolling_y (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_signflip_63d_3d_v112_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ni_vs_rolling_y (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_signflip_252d_3d_v113_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rnd_vs_rolling_y (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_signflip_63d_3d_v114_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rnd_vs_rolling_y (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_signflip_252d_3d_v115_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_smoothing_disp (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_signflip_63d_3d_v116_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_smoothing_disp (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_signflip_252d_3d_v117_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in composite_consistency (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_signflip_63d_3d_v118_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in composite_consistency (raw count, no price scaling)
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_signflip_252d_3d_v119_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_smoothed_252 normalized by 252d range
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_rngaccel_63d_r252_3d_v120_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_smoothed_252 normalized by 504d range
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_rngaccel_252d_r504_3d_v121_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_vs_rolling_y normalized by 252d range
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_rngaccel_63d_r252_3d_v122_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_vs_rolling_y normalized by 504d range
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_rngaccel_252d_r504_3d_v123_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_vs_rolling_y normalized by 252d range
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_rngaccel_63d_r252_3d_v124_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_vs_rolling_y normalized by 504d range
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_rngaccel_252d_r504_3d_v125_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ni_vs_rolling_y normalized by 252d range
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_rngaccel_63d_r252_3d_v126_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ni_vs_rolling_y normalized by 504d range
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_rngaccel_252d_r504_3d_v127_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rnd_vs_rolling_y normalized by 252d range
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_rngaccel_63d_r252_3d_v128_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rnd_vs_rolling_y normalized by 504d range
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_rngaccel_252d_r504_3d_v129_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_smoothing_disp normalized by 252d range
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_rngaccel_63d_r252_3d_v130_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_smoothing_disp normalized by 504d range
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_rngaccel_252d_r504_3d_v131_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of composite_consistency normalized by 252d range
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_rngaccel_63d_r252_3d_v132_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of composite_consistency normalized by 504d range
def f078tvc_f078_ttm_vs_annual_consistency_composite_consistency_rngaccel_252d_r504_3d_v133_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()).abs() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_cumslope_21d_3d_v134_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_cumslope_63d_3d_v135_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_smoothed_252
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothed_252_cumslope_252d_3d_v136_signal(revenue, closeadj):
    base = revenue.rolling(252, min_periods=63).mean()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_cumslope_21d_3d_v137_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_cumslope_63d_3d_v138_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rev_vs_rolling_y_cumslope_252d_3d_v139_signal(revenue, closeadj):
    base = (revenue - revenue.rolling(252, min_periods=63).mean()) / revenue.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_cumslope_21d_3d_v140_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_cumslope_63d_3d_v141_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ocf_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ocf_vs_rolling_y_cumslope_252d_3d_v142_signal(ncfo, closeadj):
    base = (ncfo - ncfo.rolling(252, min_periods=63).mean()) / ncfo.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_cumslope_21d_3d_v143_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_cumslope_63d_3d_v144_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ni_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_ni_vs_rolling_y_cumslope_252d_3d_v145_signal(netinc, closeadj):
    base = (netinc - netinc.rolling(252, min_periods=63).mean()) / netinc.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_cumslope_21d_3d_v146_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_cumslope_63d_3d_v147_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rnd_vs_rolling_y
def f078tvc_f078_ttm_vs_annual_consistency_rnd_vs_rolling_y_cumslope_252d_3d_v148_signal(rnd, closeadj):
    base = (rnd - rnd.rolling(252, min_periods=63).mean()) / rnd.rolling(252, min_periods=63).mean().replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_cumslope_21d_3d_v149_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_smoothing_disp
def f078tvc_f078_ttm_vs_annual_consistency_rev_smoothing_disp_cumslope_63d_3d_v150_signal(revenue, closeadj):
    base = revenue.rolling(63, min_periods=21).std() / revenue.rolling(252, min_periods=63).std().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

