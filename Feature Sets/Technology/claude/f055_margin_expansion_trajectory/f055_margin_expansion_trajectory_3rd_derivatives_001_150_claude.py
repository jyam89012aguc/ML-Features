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
def _f055_gm_slope(gp, revenue, n):
    gm = gp / revenue.abs().replace(0, np.nan)
    return gm.diff(periods=n)


# 21d acceleration of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_accel_21d_3d_v001_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_accel_63d_3d_v002_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_accel_126d_3d_v003_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_accel_252d_3d_v004_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_accel_21d_3d_v005_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_accel_63d_3d_v006_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_accel_126d_3d_v007_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_accel_252d_3d_v008_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_accel_21d_3d_v009_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_accel_63d_3d_v010_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_accel_126d_3d_v011_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_accel_252d_3d_v012_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_accel_21d_3d_v013_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_accel_63d_3d_v014_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_accel_126d_3d_v015_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_accel_252d_3d_v016_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_accel_21d_3d_v017_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_accel_63d_3d_v018_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_accel_126d_3d_v019_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_accel_252d_3d_v020_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_accel_21d_3d_v021_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_accel_63d_3d_v022_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_accel_126d_3d_v023_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_accel_252d_3d_v024_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_accel_21d_3d_v025_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_accel_63d_3d_v026_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_accel_126d_3d_v027_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_accel_252d_3d_v028_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slopez_21d_z126_3d_v029_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slopez_63d_z252_3d_v030_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slopez_126d_z252_3d_v031_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slopez_252d_z504_3d_v032_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slopez_21d_z126_3d_v033_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slopez_63d_z252_3d_v034_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slopez_126d_z252_3d_v035_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slopez_252d_z504_3d_v036_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slopez_21d_z126_3d_v037_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slopez_63d_z252_3d_v038_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slopez_126d_z252_3d_v039_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slopez_252d_z504_3d_v040_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slopez_21d_z126_3d_v041_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slopez_63d_z252_3d_v042_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slopez_126d_z252_3d_v043_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slopez_252d_z504_3d_v044_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slopez_21d_z126_3d_v045_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slopez_63d_z252_3d_v046_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slopez_126d_z252_3d_v047_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slopez_252d_z504_3d_v048_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slopez_21d_z126_3d_v049_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slopez_63d_z252_3d_v050_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slopez_126d_z252_3d_v051_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slopez_252d_z504_3d_v052_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slopez_21d_z126_3d_v053_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slopez_63d_z252_3d_v054_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slopez_126d_z252_3d_v055_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slopez_252d_z504_3d_v056_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_jerk_21d_3d_v057_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_jerk_63d_3d_v058_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_jerk_126d_3d_v059_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_jerk_21d_3d_v060_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_jerk_63d_3d_v061_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_jerk_126d_3d_v062_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_jerk_21d_3d_v063_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_jerk_63d_3d_v064_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_jerk_126d_3d_v065_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_jerk_21d_3d_v066_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_jerk_63d_3d_v067_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_jerk_126d_3d_v068_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_jerk_21d_3d_v069_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_jerk_63d_3d_v070_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_jerk_126d_3d_v071_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_jerk_21d_3d_v072_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_jerk_63d_3d_v073_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_jerk_126d_3d_v074_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_jerk_21d_3d_v075_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_jerk_63d_3d_v076_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_jerk_126d_3d_v077_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_slope_y smoothed over 252d
def f055met_f055_margin_expansion_trajectory_gm_slope_y_smoothaccel_63d_sm252_3d_v078_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_slope_y smoothed over 504d
def f055met_f055_margin_expansion_trajectory_gm_slope_y_smoothaccel_252d_sm504_3d_v079_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_slope_y smoothed over 252d
def f055met_f055_margin_expansion_trajectory_om_slope_y_smoothaccel_63d_sm252_3d_v080_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_slope_y smoothed over 504d
def f055met_f055_margin_expansion_trajectory_om_slope_y_smoothaccel_252d_sm504_3d_v081_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of nm_slope_y smoothed over 252d
def f055met_f055_margin_expansion_trajectory_nm_slope_y_smoothaccel_63d_sm252_3d_v082_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of nm_slope_y smoothed over 504d
def f055met_f055_margin_expansion_trajectory_nm_slope_y_smoothaccel_252d_sm504_3d_v083_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opex_slope_y smoothed over 252d
def f055met_f055_margin_expansion_trajectory_opex_slope_y_smoothaccel_63d_sm252_3d_v084_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opex_slope_y smoothed over 504d
def f055met_f055_margin_expansion_trajectory_opex_slope_y_smoothaccel_252d_sm504_3d_v085_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gm_stack_count smoothed over 252d
def f055met_f055_margin_expansion_trajectory_gm_stack_count_smoothaccel_63d_sm252_3d_v086_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gm_stack_count smoothed over 504d
def f055met_f055_margin_expansion_trajectory_gm_stack_count_smoothaccel_252d_sm504_3d_v087_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of om_stack_count smoothed over 252d
def f055met_f055_margin_expansion_trajectory_om_stack_count_smoothaccel_63d_sm252_3d_v088_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of om_stack_count smoothed over 504d
def f055met_f055_margin_expansion_trajectory_om_stack_count_smoothaccel_252d_sm504_3d_v089_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of breakeven_gap smoothed over 252d
def f055met_f055_margin_expansion_trajectory_breakeven_gap_smoothaccel_63d_sm252_3d_v090_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of breakeven_gap smoothed over 504d
def f055met_f055_margin_expansion_trajectory_breakeven_gap_smoothaccel_252d_sm504_3d_v091_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_accelz_21d_z252_3d_v092_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_accelz_63d_z504_3d_v093_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_accelz_21d_z252_3d_v094_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_accelz_63d_z504_3d_v095_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_accelz_21d_z252_3d_v096_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_accelz_63d_z504_3d_v097_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_accelz_21d_z252_3d_v098_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_accelz_63d_z504_3d_v099_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_accelz_21d_z252_3d_v100_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_accelz_63d_z504_3d_v101_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_accelz_21d_z252_3d_v102_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_accelz_63d_z504_3d_v103_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_accelz_21d_z252_3d_v104_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_accelz_63d_z504_3d_v105_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in gm_slope_y (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_gm_slope_y_signflip_63d_3d_v106_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in gm_slope_y (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_gm_slope_y_signflip_252d_3d_v107_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in om_slope_y (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_om_slope_y_signflip_63d_3d_v108_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in om_slope_y (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_om_slope_y_signflip_252d_3d_v109_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in nm_slope_y (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_nm_slope_y_signflip_63d_3d_v110_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in nm_slope_y (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_nm_slope_y_signflip_252d_3d_v111_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in opex_slope_y (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_opex_slope_y_signflip_63d_3d_v112_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in opex_slope_y (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_opex_slope_y_signflip_252d_3d_v113_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in gm_stack_count (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_gm_stack_count_signflip_63d_3d_v114_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in gm_stack_count (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_gm_stack_count_signflip_252d_3d_v115_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in om_stack_count (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_om_stack_count_signflip_63d_3d_v116_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in om_stack_count (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_om_stack_count_signflip_252d_3d_v117_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in breakeven_gap (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_breakeven_gap_signflip_63d_3d_v118_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in breakeven_gap (raw count, no price scaling)
def f055met_f055_margin_expansion_trajectory_breakeven_gap_signflip_252d_3d_v119_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_slope_y normalized by 252d range
def f055met_f055_margin_expansion_trajectory_gm_slope_y_rngaccel_63d_r252_3d_v120_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_slope_y normalized by 504d range
def f055met_f055_margin_expansion_trajectory_gm_slope_y_rngaccel_252d_r504_3d_v121_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_slope_y normalized by 252d range
def f055met_f055_margin_expansion_trajectory_om_slope_y_rngaccel_63d_r252_3d_v122_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_slope_y normalized by 504d range
def f055met_f055_margin_expansion_trajectory_om_slope_y_rngaccel_252d_r504_3d_v123_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of nm_slope_y normalized by 252d range
def f055met_f055_margin_expansion_trajectory_nm_slope_y_rngaccel_63d_r252_3d_v124_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of nm_slope_y normalized by 504d range
def f055met_f055_margin_expansion_trajectory_nm_slope_y_rngaccel_252d_r504_3d_v125_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opex_slope_y normalized by 252d range
def f055met_f055_margin_expansion_trajectory_opex_slope_y_rngaccel_63d_r252_3d_v126_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opex_slope_y normalized by 504d range
def f055met_f055_margin_expansion_trajectory_opex_slope_y_rngaccel_252d_r504_3d_v127_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gm_stack_count normalized by 252d range
def f055met_f055_margin_expansion_trajectory_gm_stack_count_rngaccel_63d_r252_3d_v128_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gm_stack_count normalized by 504d range
def f055met_f055_margin_expansion_trajectory_gm_stack_count_rngaccel_252d_r504_3d_v129_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of om_stack_count normalized by 252d range
def f055met_f055_margin_expansion_trajectory_om_stack_count_rngaccel_63d_r252_3d_v130_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of om_stack_count normalized by 504d range
def f055met_f055_margin_expansion_trajectory_om_stack_count_rngaccel_252d_r504_3d_v131_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of breakeven_gap normalized by 252d range
def f055met_f055_margin_expansion_trajectory_breakeven_gap_rngaccel_63d_r252_3d_v132_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of breakeven_gap normalized by 504d range
def f055met_f055_margin_expansion_trajectory_breakeven_gap_rngaccel_252d_r504_3d_v133_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_cumslope_21d_3d_v134_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_cumslope_63d_3d_v135_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_cumslope_252d_3d_v136_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_cumslope_21d_3d_v137_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_cumslope_63d_3d_v138_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_cumslope_252d_3d_v139_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_cumslope_21d_3d_v140_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_cumslope_63d_3d_v141_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_cumslope_252d_3d_v142_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_cumslope_21d_3d_v143_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_cumslope_63d_3d_v144_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_cumslope_252d_3d_v145_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_cumslope_21d_3d_v146_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_cumslope_63d_3d_v147_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_cumslope_252d_3d_v148_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_cumslope_21d_3d_v149_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_cumslope_63d_3d_v150_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

