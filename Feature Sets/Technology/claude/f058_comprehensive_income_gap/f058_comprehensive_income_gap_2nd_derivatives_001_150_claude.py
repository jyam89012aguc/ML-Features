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
def _f058_gap(consolinc, netinc):
    return consolinc - netinc


# 21d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slope_21d_2d_v001_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slope_63d_2d_v002_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slope_126d_2d_v003_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slope_252d_2d_v004_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slope_504d_2d_v005_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slope_21d_2d_v006_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slope_63d_2d_v007_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slope_126d_2d_v008_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slope_252d_2d_v009_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slope_504d_2d_v010_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slope_21d_2d_v011_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slope_63d_2d_v012_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slope_126d_2d_v013_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slope_252d_2d_v014_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slope_504d_2d_v015_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slope_21d_2d_v016_signal(consolinc, closeadj):
    base = consolinc
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slope_63d_2d_v017_signal(consolinc, closeadj):
    base = consolinc
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slope_126d_2d_v018_signal(consolinc, closeadj):
    base = consolinc
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slope_252d_2d_v019_signal(consolinc, closeadj):
    base = consolinc
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slope_504d_2d_v020_signal(consolinc, closeadj):
    base = consolinc
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slope_21d_2d_v021_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slope_63d_2d_v022_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slope_126d_2d_v023_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slope_252d_2d_v024_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slope_504d_2d_v025_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slope_21d_2d_v026_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slope_63d_2d_v027_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slope_126d_2d_v028_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slope_252d_2d_v029_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slope_504d_2d_v030_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slope_21d_2d_v031_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slope_63d_2d_v032_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slope_126d_2d_v033_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slope_252d_2d_v034_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slope_504d_2d_v035_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_sm21_sl21_2d_v036_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_sm63_sl21_2d_v037_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_sm63_sl63_2d_v038_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_sm252_sl63_2d_v039_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_sm252_sl126_2d_v040_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_sm21_sl21_2d_v041_signal(consolinc, netinc, equity, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_sm63_sl21_2d_v042_signal(consolinc, netinc, equity, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_sm63_sl63_2d_v043_signal(consolinc, netinc, equity, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_sm252_sl63_2d_v044_signal(consolinc, netinc, equity, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_sm252_sl126_2d_v045_signal(consolinc, netinc, equity, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_sm21_sl21_2d_v046_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_sm63_sl21_2d_v047_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_sm63_sl63_2d_v048_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_sm252_sl63_2d_v049_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_sm252_sl126_2d_v050_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_sm21_sl21_2d_v051_signal(consolinc, closeadj):
    base = _mean(consolinc, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_sm63_sl21_2d_v052_signal(consolinc, closeadj):
    base = _mean(consolinc, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_sm63_sl63_2d_v053_signal(consolinc, closeadj):
    base = _mean(consolinc, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_sm252_sl63_2d_v054_signal(consolinc, closeadj):
    base = _mean(consolinc, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_sm252_sl126_2d_v055_signal(consolinc, closeadj):
    base = _mean(consolinc, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_sm21_sl21_2d_v056_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc).diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_sm63_sl21_2d_v057_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc).diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_sm63_sl63_2d_v058_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc).diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_sm252_sl63_2d_v059_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc).diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_sm252_sl126_2d_v060_signal(consolinc, netinc, closeadj):
    base = _mean(_f058_gap(consolinc, netinc).diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_sm21_sl21_2d_v061_signal(consolinc, netinc, revenue, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_sm63_sl21_2d_v062_signal(consolinc, netinc, revenue, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_sm63_sl63_2d_v063_signal(consolinc, netinc, revenue, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_sm252_sl63_2d_v064_signal(consolinc, netinc, revenue, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_sm252_sl126_2d_v065_signal(consolinc, netinc, revenue, closeadj):
    base = _mean(_f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_sm21_sl21_2d_v066_signal(consolinc, netinc, closeadj):
    base = _mean(np.sign(_f058_gap(consolinc, netinc)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_sm63_sl21_2d_v067_signal(consolinc, netinc, closeadj):
    base = _mean(np.sign(_f058_gap(consolinc, netinc)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_sm63_sl63_2d_v068_signal(consolinc, netinc, closeadj):
    base = _mean(np.sign(_f058_gap(consolinc, netinc)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_sm252_sl63_2d_v069_signal(consolinc, netinc, closeadj):
    base = _mean(np.sign(_f058_gap(consolinc, netinc)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_sm252_sl126_2d_v070_signal(consolinc, netinc, closeadj):
    base = _mean(np.sign(_f058_gap(consolinc, netinc)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_pctslope_21d_2d_v071_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_pctslope_63d_2d_v072_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_pctslope_252d_2d_v073_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_pctslope_21d_2d_v074_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_pctslope_63d_2d_v075_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_pctslope_252d_2d_v076_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_pctslope_21d_2d_v077_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_pctslope_63d_2d_v078_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_pctslope_252d_2d_v079_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_pctslope_21d_2d_v080_signal(consolinc, closeadj):
    base = consolinc
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_pctslope_63d_2d_v081_signal(consolinc, closeadj):
    base = consolinc
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_pctslope_252d_2d_v082_signal(consolinc, closeadj):
    base = consolinc
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_pctslope_21d_2d_v083_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_pctslope_63d_2d_v084_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_pctslope_252d_2d_v085_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_pctslope_21d_2d_v086_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_pctslope_63d_2d_v087_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_pctslope_252d_2d_v088_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_pctslope_21d_2d_v089_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_pctslope_63d_2d_v090_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_pctslope_252d_2d_v091_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_sgnslope_21d_2d_v092_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_sgnslope_63d_2d_v093_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_sgnslope_252d_2d_v094_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_sgnslope_21d_2d_v095_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_sgnslope_63d_2d_v096_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_sgnslope_252d_2d_v097_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_sgnslope_21d_2d_v098_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_sgnslope_63d_2d_v099_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_sgnslope_252d_2d_v100_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_sgnslope_21d_2d_v101_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_sgnslope_63d_2d_v102_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_sgnslope_252d_2d_v103_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_sgnslope_21d_2d_v104_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_sgnslope_63d_2d_v105_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_sgnslope_252d_2d_v106_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_sgnslope_21d_2d_v107_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_sgnslope_63d_2d_v108_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_sgnslope_252d_2d_v109_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_sgnslope_21d_2d_v110_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_sgnslope_63d_2d_v111_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_sgnslope_252d_2d_v112_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_logmagslope_21d_2d_v113_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_logmagslope_63d_2d_v114_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_logmagslope_252d_2d_v115_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_logmagslope_21d_2d_v116_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_logmagslope_63d_2d_v117_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_logmagslope_252d_2d_v118_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_logmagslope_21d_2d_v119_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_logmagslope_63d_2d_v120_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_logmagslope_252d_2d_v121_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_logmagslope_21d_2d_v122_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_logmagslope_63d_2d_v123_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_logmagslope_252d_2d_v124_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_logmagslope_21d_2d_v125_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_logmagslope_63d_2d_v126_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_logmagslope_252d_2d_v127_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_logmagslope_21d_2d_v128_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_logmagslope_63d_2d_v129_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_logmagslope_252d_2d_v130_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_logmagslope_21d_2d_v131_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_logmagslope_63d_2d_v132_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_logmagslope_252d_2d_v133_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ci_gap|
def f058cig_f058_comprehensive_income_gap_ci_gap_logslope_63d_2d_v134_signal(consolinc, netinc, closeadj):
    base = np.log((_f058_gap(consolinc, netinc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ci_gap|
def f058cig_f058_comprehensive_income_gap_ci_gap_logslope_252d_2d_v135_signal(consolinc, netinc, closeadj):
    base = np.log((_f058_gap(consolinc, netinc)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ci_gap_to_equity|
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_logslope_63d_2d_v136_signal(consolinc, netinc, equity, closeadj):
    base = np.log((_f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ci_gap_to_equity|
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_logslope_252d_2d_v137_signal(consolinc, netinc, equity, closeadj):
    base = np.log((_f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ci_gap_to_ni|
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_logslope_63d_2d_v138_signal(consolinc, netinc, closeadj):
    base = np.log((_f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ci_gap_to_ni|
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_logslope_252d_2d_v139_signal(consolinc, netinc, closeadj):
    base = np.log((_f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|consolinc_lvl|
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_logslope_63d_2d_v140_signal(consolinc, closeadj):
    base = np.log((consolinc).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|consolinc_lvl|
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_logslope_252d_2d_v141_signal(consolinc, closeadj):
    base = np.log((consolinc).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ci_gap_yoy|
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_logslope_63d_2d_v142_signal(consolinc, netinc, closeadj):
    base = np.log((_f058_gap(consolinc, netinc).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ci_gap_yoy|
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_logslope_252d_2d_v143_signal(consolinc, netinc, closeadj):
    base = np.log((_f058_gap(consolinc, netinc).diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ci_gap_to_rev|
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_logslope_63d_2d_v144_signal(consolinc, netinc, revenue, closeadj):
    base = np.log((_f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ci_gap_to_rev|
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_logslope_252d_2d_v145_signal(consolinc, netinc, revenue, closeadj):
    base = np.log((_f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|ci_gap_sign|
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_logslope_63d_2d_v146_signal(consolinc, netinc, closeadj):
    base = np.log((np.sign(_f058_gap(consolinc, netinc))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|ci_gap_sign|
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_logslope_252d_2d_v147_signal(consolinc, netinc, closeadj):
    base = np.log((np.sign(_f058_gap(consolinc, netinc))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

