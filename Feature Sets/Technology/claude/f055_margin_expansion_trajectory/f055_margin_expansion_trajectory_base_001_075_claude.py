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


# 21d mean of gm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_slope_y_mean_21d_base_v001_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_slope_y_mean_63d_base_v002_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_slope_y_mean_126d_base_v003_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_slope_y_mean_252d_base_v004_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_slope_y_mean_504d_base_v005_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_slope_y_mean_21d_base_v006_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_slope_y_mean_63d_base_v007_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_slope_y_mean_126d_base_v008_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_slope_y_mean_252d_base_v009_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_slope_y_mean_504d_base_v010_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of nm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_nm_slope_y_mean_21d_base_v011_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of nm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_nm_slope_y_mean_63d_base_v012_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of nm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_nm_slope_y_mean_126d_base_v013_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of nm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_nm_slope_y_mean_252d_base_v014_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of nm_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_nm_slope_y_mean_504d_base_v015_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of opex_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_opex_slope_y_mean_21d_base_v016_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of opex_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_opex_slope_y_mean_63d_base_v017_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of opex_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_opex_slope_y_mean_126d_base_v018_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of opex_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_opex_slope_y_mean_252d_base_v019_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of opex_slope_y scaled by closeadj
def f055met_f055_margin_expansion_trajectory_opex_slope_y_mean_504d_base_v020_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of gm_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_stack_count_mean_21d_base_v021_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of gm_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_stack_count_mean_63d_base_v022_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of gm_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_stack_count_mean_126d_base_v023_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of gm_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_stack_count_mean_252d_base_v024_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of gm_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_gm_stack_count_mean_504d_base_v025_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of om_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_stack_count_mean_21d_base_v026_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of om_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_stack_count_mean_63d_base_v027_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of om_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_stack_count_mean_126d_base_v028_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of om_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_stack_count_mean_252d_base_v029_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of om_stack_count scaled by closeadj
def f055met_f055_margin_expansion_trajectory_om_stack_count_mean_504d_base_v030_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of breakeven_gap scaled by closeadj
def f055met_f055_margin_expansion_trajectory_breakeven_gap_mean_21d_base_v031_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of breakeven_gap scaled by closeadj
def f055met_f055_margin_expansion_trajectory_breakeven_gap_mean_63d_base_v032_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of breakeven_gap scaled by closeadj
def f055met_f055_margin_expansion_trajectory_breakeven_gap_mean_126d_base_v033_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of breakeven_gap scaled by closeadj
def f055met_f055_margin_expansion_trajectory_breakeven_gap_mean_252d_base_v034_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of breakeven_gap scaled by closeadj
def f055met_f055_margin_expansion_trajectory_breakeven_gap_mean_504d_base_v035_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_median_63d_base_v036_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_median_252d_base_v037_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_median_504d_base_v038_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_median_63d_base_v039_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_median_252d_base_v040_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_median_504d_base_v041_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_median_63d_base_v042_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_median_252d_base_v043_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_median_504d_base_v044_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_median_63d_base_v045_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_median_252d_base_v046_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_median_504d_base_v047_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_median_63d_base_v048_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_median_252d_base_v049_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_median_504d_base_v050_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_median_63d_base_v051_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_median_252d_base_v052_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_median_504d_base_v053_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_median_63d_base_v054_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_median_252d_base_v055_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_median_504d_base_v056_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_rmax_252d_base_v057_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_rmax_504d_base_v058_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_rmax_252d_base_v059_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_rmax_504d_base_v060_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_rmax_252d_base_v061_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_rmax_504d_base_v062_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_rmax_252d_base_v063_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of opex_slope_y
def f055met_f055_margin_expansion_trajectory_opex_slope_y_rmax_504d_base_v064_signal(opex, revenue, closeadj):
    base = (opex / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_rmax_252d_base_v065_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of gm_stack_count
def f055met_f055_margin_expansion_trajectory_gm_stack_count_rmax_504d_base_v066_signal(gp, revenue, closeadj):
    base = (_f055_gm_slope(gp, revenue, 63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_rmax_252d_base_v067_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of om_stack_count
def f055met_f055_margin_expansion_trajectory_om_stack_count_rmax_504d_base_v068_signal(opinc, revenue, closeadj):
    base = ((opinc / revenue.abs().replace(0, np.nan)).diff(periods=63) > 0).astype(float).rolling(252, min_periods=63).sum()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_rmax_252d_base_v069_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of breakeven_gap
def f055met_f055_margin_expansion_trajectory_breakeven_gap_rmax_504d_base_v070_signal(netinc, revenue, closeadj):
    base = -netinc / revenue.abs().replace(0, np.nan)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_rmin_252d_base_v071_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of gm_slope_y
def f055met_f055_margin_expansion_trajectory_gm_slope_y_rmin_504d_base_v072_signal(gp, revenue, closeadj):
    base = _f055_gm_slope(gp, revenue, 252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_rmin_252d_base_v073_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of om_slope_y
def f055met_f055_margin_expansion_trajectory_om_slope_y_rmin_504d_base_v074_signal(opinc, revenue, closeadj):
    base = (opinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of nm_slope_y
def f055met_f055_margin_expansion_trajectory_nm_slope_y_rmin_252d_base_v075_signal(netinc, revenue, closeadj):
    base = (netinc / revenue.abs().replace(0, np.nan)).diff(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

