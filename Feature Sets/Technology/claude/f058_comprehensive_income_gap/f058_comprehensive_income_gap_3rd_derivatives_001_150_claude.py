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


# 21d acceleration of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_accel_21d_3d_v001_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_accel_63d_3d_v002_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_accel_126d_3d_v003_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_accel_252d_3d_v004_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_accel_21d_3d_v005_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_accel_63d_3d_v006_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_accel_126d_3d_v007_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_accel_252d_3d_v008_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_accel_21d_3d_v009_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_accel_63d_3d_v010_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_accel_126d_3d_v011_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_accel_252d_3d_v012_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_accel_21d_3d_v013_signal(consolinc, closeadj):
    base = consolinc
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_accel_63d_3d_v014_signal(consolinc, closeadj):
    base = consolinc
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_accel_126d_3d_v015_signal(consolinc, closeadj):
    base = consolinc
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_accel_252d_3d_v016_signal(consolinc, closeadj):
    base = consolinc
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_accel_21d_3d_v017_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_accel_63d_3d_v018_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_accel_126d_3d_v019_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_accel_252d_3d_v020_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_accel_21d_3d_v021_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_accel_63d_3d_v022_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_accel_126d_3d_v023_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_accel_252d_3d_v024_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_accel_21d_3d_v025_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_accel_63d_3d_v026_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_accel_126d_3d_v027_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_accel_252d_3d_v028_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slopez_21d_z126_3d_v029_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slopez_63d_z252_3d_v030_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slopez_126d_z252_3d_v031_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_slopez_252d_z504_3d_v032_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slopez_21d_z126_3d_v033_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slopez_63d_z252_3d_v034_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slopez_126d_z252_3d_v035_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_slopez_252d_z504_3d_v036_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slopez_21d_z126_3d_v037_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slopez_63d_z252_3d_v038_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slopez_126d_z252_3d_v039_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_slopez_252d_z504_3d_v040_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slopez_21d_z126_3d_v041_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slopez_63d_z252_3d_v042_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slopez_126d_z252_3d_v043_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_slopez_252d_z504_3d_v044_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slopez_21d_z126_3d_v045_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slopez_63d_z252_3d_v046_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slopez_126d_z252_3d_v047_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_slopez_252d_z504_3d_v048_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slopez_21d_z126_3d_v049_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slopez_63d_z252_3d_v050_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slopez_126d_z252_3d_v051_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_slopez_252d_z504_3d_v052_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slopez_21d_z126_3d_v053_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slopez_63d_z252_3d_v054_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slopez_126d_z252_3d_v055_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_slopez_252d_z504_3d_v056_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_jerk_21d_3d_v057_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_jerk_63d_3d_v058_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_jerk_126d_3d_v059_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_jerk_21d_3d_v060_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_jerk_63d_3d_v061_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_jerk_126d_3d_v062_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_jerk_21d_3d_v063_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_jerk_63d_3d_v064_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_jerk_126d_3d_v065_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_jerk_21d_3d_v066_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_jerk_63d_3d_v067_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_jerk_126d_3d_v068_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_jerk_21d_3d_v069_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_jerk_63d_3d_v070_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_jerk_126d_3d_v071_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_jerk_21d_3d_v072_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_jerk_63d_3d_v073_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_jerk_126d_3d_v074_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_jerk_21d_3d_v075_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_jerk_63d_3d_v076_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_jerk_126d_3d_v077_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ci_gap smoothed over 252d
def f058cig_f058_comprehensive_income_gap_ci_gap_smoothaccel_63d_sm252_3d_v078_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ci_gap smoothed over 504d
def f058cig_f058_comprehensive_income_gap_ci_gap_smoothaccel_252d_sm504_3d_v079_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ci_gap_to_equity smoothed over 252d
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_smoothaccel_63d_sm252_3d_v080_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ci_gap_to_equity smoothed over 504d
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_smoothaccel_252d_sm504_3d_v081_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ci_gap_to_ni smoothed over 252d
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_smoothaccel_63d_sm252_3d_v082_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ci_gap_to_ni smoothed over 504d
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_smoothaccel_252d_sm504_3d_v083_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of consolinc_lvl smoothed over 252d
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_smoothaccel_63d_sm252_3d_v084_signal(consolinc, closeadj):
    base = consolinc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of consolinc_lvl smoothed over 504d
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_smoothaccel_252d_sm504_3d_v085_signal(consolinc, closeadj):
    base = consolinc
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ci_gap_yoy smoothed over 252d
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_smoothaccel_63d_sm252_3d_v086_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ci_gap_yoy smoothed over 504d
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_smoothaccel_252d_sm504_3d_v087_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ci_gap_to_rev smoothed over 252d
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_smoothaccel_63d_sm252_3d_v088_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ci_gap_to_rev smoothed over 504d
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_smoothaccel_252d_sm504_3d_v089_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ci_gap_sign smoothed over 252d
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_smoothaccel_63d_sm252_3d_v090_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ci_gap_sign smoothed over 504d
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_smoothaccel_252d_sm504_3d_v091_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_accelz_21d_z252_3d_v092_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_accelz_63d_z504_3d_v093_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_accelz_21d_z252_3d_v094_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_accelz_63d_z504_3d_v095_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_accelz_21d_z252_3d_v096_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_accelz_63d_z504_3d_v097_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_accelz_21d_z252_3d_v098_signal(consolinc, closeadj):
    base = consolinc
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_accelz_63d_z504_3d_v099_signal(consolinc, closeadj):
    base = consolinc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_accelz_21d_z252_3d_v100_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_accelz_63d_z504_3d_v101_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_accelz_21d_z252_3d_v102_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_accelz_63d_z504_3d_v103_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_accelz_21d_z252_3d_v104_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ci_gap_sign
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_accelz_63d_z504_3d_v105_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ci_gap (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_signflip_63d_3d_v106_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ci_gap (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_signflip_252d_3d_v107_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ci_gap_to_equity (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_signflip_63d_3d_v108_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ci_gap_to_equity (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_signflip_252d_3d_v109_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ci_gap_to_ni (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_signflip_63d_3d_v110_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ci_gap_to_ni (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_signflip_252d_3d_v111_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in consolinc_lvl (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_signflip_63d_3d_v112_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in consolinc_lvl (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_signflip_252d_3d_v113_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ci_gap_yoy (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_signflip_63d_3d_v114_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ci_gap_yoy (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_signflip_252d_3d_v115_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ci_gap_to_rev (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_signflip_63d_3d_v116_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ci_gap_to_rev (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_signflip_252d_3d_v117_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ci_gap_sign (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_signflip_63d_3d_v118_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ci_gap_sign (raw count, no price scaling)
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_signflip_252d_3d_v119_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap normalized by 252d range
def f058cig_f058_comprehensive_income_gap_ci_gap_rngaccel_63d_r252_3d_v120_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap normalized by 504d range
def f058cig_f058_comprehensive_income_gap_ci_gap_rngaccel_252d_r504_3d_v121_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_to_equity normalized by 252d range
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_rngaccel_63d_r252_3d_v122_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_to_equity normalized by 504d range
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_rngaccel_252d_r504_3d_v123_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_to_ni normalized by 252d range
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_rngaccel_63d_r252_3d_v124_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_to_ni normalized by 504d range
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_rngaccel_252d_r504_3d_v125_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of consolinc_lvl normalized by 252d range
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_rngaccel_63d_r252_3d_v126_signal(consolinc, closeadj):
    base = consolinc
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of consolinc_lvl normalized by 504d range
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_rngaccel_252d_r504_3d_v127_signal(consolinc, closeadj):
    base = consolinc
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_yoy normalized by 252d range
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_rngaccel_63d_r252_3d_v128_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_yoy normalized by 504d range
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_rngaccel_252d_r504_3d_v129_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_to_rev normalized by 252d range
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_rngaccel_63d_r252_3d_v130_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_to_rev normalized by 504d range
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_rngaccel_252d_r504_3d_v131_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ci_gap_sign normalized by 252d range
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_rngaccel_63d_r252_3d_v132_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ci_gap_sign normalized by 504d range
def f058cig_f058_comprehensive_income_gap_ci_gap_sign_rngaccel_252d_r504_3d_v133_signal(consolinc, netinc, closeadj):
    base = np.sign(_f058_gap(consolinc, netinc))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_cumslope_21d_3d_v134_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_cumslope_63d_3d_v135_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ci_gap
def f058cig_f058_comprehensive_income_gap_ci_gap_cumslope_252d_3d_v136_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_cumslope_21d_3d_v137_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_cumslope_63d_3d_v138_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ci_gap_to_equity
def f058cig_f058_comprehensive_income_gap_ci_gap_to_equity_cumslope_252d_3d_v139_signal(consolinc, netinc, equity, closeadj):
    base = _f058_gap(consolinc, netinc) / equity.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_cumslope_21d_3d_v140_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_cumslope_63d_3d_v141_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ci_gap_to_ni
def f058cig_f058_comprehensive_income_gap_ci_gap_to_ni_cumslope_252d_3d_v142_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc) / netinc.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_cumslope_21d_3d_v143_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_cumslope_63d_3d_v144_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of consolinc_lvl
def f058cig_f058_comprehensive_income_gap_consolinc_lvl_cumslope_252d_3d_v145_signal(consolinc, closeadj):
    base = consolinc
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_cumslope_21d_3d_v146_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_cumslope_63d_3d_v147_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ci_gap_yoy
def f058cig_f058_comprehensive_income_gap_ci_gap_yoy_cumslope_252d_3d_v148_signal(consolinc, netinc, closeadj):
    base = _f058_gap(consolinc, netinc).diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_cumslope_21d_3d_v149_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ci_gap_to_rev
def f058cig_f058_comprehensive_income_gap_ci_gap_to_rev_cumslope_63d_3d_v150_signal(consolinc, netinc, revenue, closeadj):
    base = _f058_gap(consolinc, netinc) / revenue.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

