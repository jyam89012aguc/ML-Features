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


# 21d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slope_21d_2d_v001_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slope_63d_2d_v002_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slope_126d_2d_v003_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slope_252d_2d_v004_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_slope_504d_2d_v005_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slope_21d_2d_v006_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slope_63d_2d_v007_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slope_126d_2d_v008_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slope_252d_2d_v009_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_slope_504d_2d_v010_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slope_21d_2d_v011_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slope_63d_2d_v012_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slope_126d_2d_v013_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slope_252d_2d_v014_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_slope_504d_2d_v015_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slope_21d_2d_v016_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slope_63d_2d_v017_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slope_126d_2d_v018_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slope_252d_2d_v019_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_slope_504d_2d_v020_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slope_21d_2d_v021_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slope_63d_2d_v022_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slope_126d_2d_v023_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slope_252d_2d_v024_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_slope_504d_2d_v025_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slope_21d_2d_v026_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slope_63d_2d_v027_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slope_126d_2d_v028_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slope_252d_2d_v029_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_slope_504d_2d_v030_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slope_21d_2d_v031_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slope_63d_2d_v032_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slope_126d_2d_v033_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slope_252d_2d_v034_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_slope_504d_2d_v035_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_sm21_sl21_2d_v036_signal(gp, revenue, closeadj):
    base = _mean(_f055_gm_slope(gp, revenue, 252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_sm63_sl21_2d_v037_signal(gp, revenue, closeadj):
    base = _mean(_f055_gm_slope(gp, revenue, 252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_sm63_sl63_2d_v038_signal(gp, revenue, closeadj):
    base = _mean(_f055_gm_slope(gp, revenue, 252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_sm252_sl63_2d_v039_signal(gp, revenue, closeadj):
    base = _mean(_f055_gm_slope(gp, revenue, 252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_sm252_sl126_2d_v040_signal(gp, revenue, closeadj):
    base = _mean(_f055_gm_slope(gp, revenue, 252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_sm21_sl21_2d_v041_signal(opinc, revenue, closeadj):
    base = _mean((opinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_sm63_sl21_2d_v042_signal(opinc, revenue, closeadj):
    base = _mean((opinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_sm63_sl63_2d_v043_signal(opinc, revenue, closeadj):
    base = _mean((opinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_sm252_sl63_2d_v044_signal(opinc, revenue, closeadj):
    base = _mean((opinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_sm252_sl126_2d_v045_signal(opinc, revenue, closeadj):
    base = _mean((opinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_sm21_sl21_2d_v046_signal(netinc, revenue, closeadj):
    base = _mean((netinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_sm63_sl21_2d_v047_signal(netinc, revenue, closeadj):
    base = _mean((netinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_sm63_sl63_2d_v048_signal(netinc, revenue, closeadj):
    base = _mean((netinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_sm252_sl63_2d_v049_signal(netinc, revenue, closeadj):
    base = _mean((netinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_sm252_sl126_2d_v050_signal(netinc, revenue, closeadj):
    base = _mean((netinc / revenue.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_sm21_sl21_2d_v051_signal(opex, revenue, closeadj):
    base = _mean((opex / revenue.abs().replace(0, np.nan)).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_sm63_sl21_2d_v052_signal(opex, revenue, closeadj):
    base = _mean((opex / revenue.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_sm63_sl63_2d_v053_signal(opex, revenue, closeadj):
    base = _mean((opex / revenue.abs().replace(0, np.nan)).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_sm252_sl63_2d_v054_signal(opex, revenue, closeadj):
    base = _mean((opex / revenue.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_sm252_sl126_2d_v055_signal(opex, revenue, closeadj):
    base = _mean((opex / revenue.abs().replace(0, np.nan)).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_sm21_sl21_2d_v056_signal(gp, revenue, closeadj):
    base = _mean((_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_sm63_sl21_2d_v057_signal(gp, revenue, closeadj):
    base = _mean((_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_sm63_sl63_2d_v058_signal(gp, revenue, closeadj):
    base = _mean((_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_sm252_sl63_2d_v059_signal(gp, revenue, closeadj):
    base = _mean((_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_sm252_sl126_2d_v060_signal(gp, revenue, closeadj):
    base = _mean((_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_sm21_sl21_2d_v061_signal(opinc, revenue, closeadj):
    base = _mean(((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_sm63_sl21_2d_v062_signal(opinc, revenue, closeadj):
    base = _mean(((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_sm63_sl63_2d_v063_signal(opinc, revenue, closeadj):
    base = _mean(((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_sm252_sl63_2d_v064_signal(opinc, revenue, closeadj):
    base = _mean(((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_sm252_sl126_2d_v065_signal(opinc, revenue, closeadj):
    base = _mean(((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_sm21_sl21_2d_v066_signal(netinc, revenue, closeadj):
    base = _mean(-netinc / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_sm63_sl21_2d_v067_signal(netinc, revenue, closeadj):
    base = _mean(-netinc / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_sm63_sl63_2d_v068_signal(netinc, revenue, closeadj):
    base = _mean(-netinc / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_sm252_sl63_2d_v069_signal(netinc, revenue, closeadj):
    base = _mean(-netinc / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_sm252_sl126_2d_v070_signal(netinc, revenue, closeadj):
    base = _mean(-netinc / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_pctslope_21d_2d_v071_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_pctslope_63d_2d_v072_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_pctslope_252d_2d_v073_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_pctslope_21d_2d_v074_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_pctslope_63d_2d_v075_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_pctslope_252d_2d_v076_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_pctslope_21d_2d_v077_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_pctslope_63d_2d_v078_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_pctslope_252d_2d_v079_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_pctslope_21d_2d_v080_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_pctslope_63d_2d_v081_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_pctslope_252d_2d_v082_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_pctslope_21d_2d_v083_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_pctslope_63d_2d_v084_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_pctslope_252d_2d_v085_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_pctslope_21d_2d_v086_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_pctslope_63d_2d_v087_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_pctslope_252d_2d_v088_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_pctslope_21d_2d_v089_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_pctslope_63d_2d_v090_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_pctslope_252d_2d_v091_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_sgnslope_21d_2d_v092_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_sgnslope_63d_2d_v093_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_sgnslope_252d_2d_v094_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_sgnslope_21d_2d_v095_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_sgnslope_63d_2d_v096_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_sgnslope_252d_2d_v097_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_sgnslope_21d_2d_v098_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_sgnslope_63d_2d_v099_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_sgnslope_252d_2d_v100_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_sgnslope_21d_2d_v101_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_sgnslope_63d_2d_v102_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_sgnslope_252d_2d_v103_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_sgnslope_21d_2d_v104_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_sgnslope_63d_2d_v105_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_sgnslope_252d_2d_v106_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_sgnslope_21d_2d_v107_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_sgnslope_63d_2d_v108_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_sgnslope_252d_2d_v109_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_sgnslope_21d_2d_v110_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_sgnslope_63d_2d_v111_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_sgnslope_252d_2d_v112_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_logmagslope_21d_2d_v113_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_logmagslope_63d_2d_v114_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_logmagslope_252d_2d_v115_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_logmagslope_21d_2d_v116_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_logmagslope_63d_2d_v117_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_logmagslope_252d_2d_v118_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_logmagslope_21d_2d_v119_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_logmagslope_63d_2d_v120_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_logmagslope_252d_2d_v121_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_logmagslope_21d_2d_v122_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_logmagslope_63d_2d_v123_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_logmagslope_252d_2d_v124_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_logmagslope_21d_2d_v125_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_logmagslope_63d_2d_v126_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_logmagslope_252d_2d_v127_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_logmagslope_21d_2d_v128_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_logmagslope_63d_2d_v129_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_logmagslope_252d_2d_v130_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_logmagslope_21d_2d_v131_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_logmagslope_63d_2d_v132_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_logmagslope_252d_2d_v133_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|gm_slope_y|
def f055met_f055_margin_expansion_trajectory_gm_slope_y_logslope_63d_2d_v134_signal(gp, revenue, closeadj):
    base = np.log((_f055_gm_slope(gp, revenue, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|gm_slope_y|
def f055met_f055_margin_expansion_trajectory_gm_slope_y_logslope_252d_2d_v135_signal(gp, revenue, closeadj):
    base = np.log((_f055_gm_slope(gp, revenue, 252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|om_slope_y|
def f055met_f055_margin_expansion_trajectory_om_slope_y_logslope_63d_2d_v136_signal(opinc, revenue, closeadj):
    base = np.log(((opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|om_slope_y|
def f055met_f055_margin_expansion_trajectory_om_slope_y_logslope_252d_2d_v137_signal(opinc, revenue, closeadj):
    base = np.log(((opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|nm_slope_y|
def f055met_f055_margin_expansion_trajectory_nm_slope_y_logslope_63d_2d_v138_signal(netinc, revenue, closeadj):
    base = np.log(((netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|nm_slope_y|
def f055met_f055_margin_expansion_trajectory_nm_slope_y_logslope_252d_2d_v139_signal(netinc, revenue, closeadj):
    base = np.log(((netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|opex_slope_y|
def f055met_f055_margin_expansion_trajectory_opex_slope_y_logslope_63d_2d_v140_signal(opex, revenue, closeadj):
    base = np.log(((opex / revenue.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|opex_slope_y|
def f055met_f055_margin_expansion_trajectory_opex_slope_y_logslope_252d_2d_v141_signal(opex, revenue, closeadj):
    base = np.log(((opex / revenue.abs().replace(0, np.nan)).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|gm_stack_count|
def f055met_f055_margin_expansion_trajectory_gm_stack_count_logslope_63d_2d_v142_signal(gp, revenue, closeadj):
    base = np.log(((_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|gm_stack_count|
def f055met_f055_margin_expansion_trajectory_gm_stack_count_logslope_252d_2d_v143_signal(gp, revenue, closeadj):
    base = np.log(((_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|om_stack_count|
def f055met_f055_margin_expansion_trajectory_om_stack_count_logslope_63d_2d_v144_signal(opinc, revenue, closeadj):
    base = np.log((((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|om_stack_count|
def f055met_f055_margin_expansion_trajectory_om_stack_count_logslope_252d_2d_v145_signal(opinc, revenue, closeadj):
    base = np.log((((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|breakeven_gap|
def f055met_f055_margin_expansion_trajectory_breakeven_gap_logslope_63d_2d_v146_signal(netinc, revenue, closeadj):
    base = np.log((-netinc / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|breakeven_gap|
def f055met_f055_margin_expansion_trajectory_breakeven_gap_logslope_252d_2d_v147_signal(netinc, revenue, closeadj):
    base = np.log((-netinc / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

