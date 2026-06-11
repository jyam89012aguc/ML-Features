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
def _f055_gm_slope(gp, revenue, n):
    gm = gp / revenue.abs().replace(0, np.nan)
    return gm.diff(periods=n)


# 63d z-score of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_z_63d_base_v076_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_z_126d_base_v077_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_z_252d_base_v078_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_z_504d_base_v079_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_z_63d_base_v080_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_z_126d_base_v081_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_z_252d_base_v082_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_z_504d_base_v083_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_z_63d_base_v084_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_z_126d_base_v085_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_z_252d_base_v086_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_z_504d_base_v087_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_z_63d_base_v088_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_z_126d_base_v089_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_z_252d_base_v090_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_z_504d_base_v091_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_z_63d_base_v092_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_z_126d_base_v093_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_z_252d_base_v094_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_z_504d_base_v095_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_z_63d_base_v096_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_z_126d_base_v097_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_z_252d_base_v098_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_z_504d_base_v099_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d z-score of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_z_63d_base_v100_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d z-score of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_z_126d_base_v101_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d z-score of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_z_252d_base_v102_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d z-score of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_z_504d_base_v103_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_distmax_252d_base_v104_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_distmax_504d_base_v105_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_distmax_252d_base_v106_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_distmax_504d_base_v107_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_distmax_252d_base_v108_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_distmax_504d_base_v109_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_distmax_252d_base_v110_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_distmax_504d_base_v111_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_distmax_252d_base_v112_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_distmax_504d_base_v113_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_distmax_252d_base_v114_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_distmax_504d_base_v115_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling max of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_distmax_252d_base_v116_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    mx = base.rolling(252, min_periods=max(1, 252//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling max of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_distmax_504d_base_v117_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    mx = base.rolling(504, min_periods=max(1, 504//2)).max()
    result = (base - mx) / mx.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_distmed_126d_base_v118_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_distmed_252d_base_v119_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_distmed_504d_base_v120_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_distmed_126d_base_v121_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_distmed_252d_base_v122_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_distmed_504d_base_v123_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_distmed_126d_base_v124_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_distmed_252d_base_v125_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_distmed_504d_base_v126_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_distmed_126d_base_v127_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_distmed_252d_base_v128_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_distmed_504d_base_v129_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_distmed_126d_base_v130_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_distmed_252d_base_v131_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_distmed_504d_base_v132_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_distmed_126d_base_v133_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_distmed_252d_base_v134_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_distmed_504d_base_v135_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d distance from rolling median of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_distmed_126d_base_v136_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    med = base.rolling(126, min_periods=max(1, 126//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d distance from rolling median of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_distmed_252d_base_v137_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    med = base.rolling(252, min_periods=max(1, 252//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d distance from rolling median of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_distmed_504d_base_v138_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    med = base.rolling(504, min_periods=max(1, 504//2)).median()
    result = (base - med) / med.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_chg_63d_base_v139_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_chg_252d_base_v140_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_chg_63d_base_v141_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_chg_252d_base_v142_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_chg_63d_base_v143_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_chg_252d_base_v144_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_chg_63d_base_v145_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_chg_252d_base_v146_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_chg_63d_base_v147_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_chg_252d_base_v148_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d change in om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_chg_63d_base_v149_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.diff(periods=63) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d change in om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_chg_252d_base_v150_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.diff(periods=252) * closeadj / closeadj.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

