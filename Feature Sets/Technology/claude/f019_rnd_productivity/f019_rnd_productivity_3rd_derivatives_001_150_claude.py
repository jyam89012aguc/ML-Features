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
def _f019_rev_per_rnd(revenue, rnd):
    return revenue / rnd.abs().replace(0, np.nan)


def _f019_gp_per_rnd(gp, rnd):
    return gp / rnd.abs().replace(0, np.nan)


# 21d acceleration of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_accel_21d_3d_v001_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_accel_63d_3d_v002_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_accel_126d_3d_v003_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_accel_252d_3d_v004_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_accel_21d_3d_v005_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_accel_63d_3d_v006_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_accel_126d_3d_v007_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_accel_252d_3d_v008_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_accel_21d_3d_v009_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_accel_63d_3d_v010_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_accel_126d_3d_v011_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_accel_252d_3d_v012_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_accel_21d_3d_v013_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_accel_63d_3d_v014_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_accel_126d_3d_v015_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_accel_252d_3d_v016_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_accel_21d_3d_v017_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_accel_63d_3d_v018_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_accel_126d_3d_v019_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_accel_252d_3d_v020_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_accel_21d_3d_v021_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_accel_63d_3d_v022_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_accel_126d_3d_v023_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_accel_252d_3d_v024_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_accel_21d_3d_v025_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_accel_63d_3d_v026_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_accel_126d_3d_v027_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_accel_252d_3d_v028_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slopez_21d_z126_3d_v029_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slopez_63d_z252_3d_v030_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slopez_126d_z252_3d_v031_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_slopez_252d_z504_3d_v032_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slopez_21d_z126_3d_v033_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slopez_63d_z252_3d_v034_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slopez_126d_z252_3d_v035_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_slopez_252d_z504_3d_v036_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slopez_21d_z126_3d_v037_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slopez_63d_z252_3d_v038_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slopez_126d_z252_3d_v039_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_slopez_252d_z504_3d_v040_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slopez_21d_z126_3d_v041_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slopez_63d_z252_3d_v042_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slopez_126d_z252_3d_v043_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_slopez_252d_z504_3d_v044_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slopez_21d_z126_3d_v045_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slopez_63d_z252_3d_v046_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slopez_126d_z252_3d_v047_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_slopez_252d_z504_3d_v048_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slopez_21d_z126_3d_v049_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slopez_63d_z252_3d_v050_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slopez_126d_z252_3d_v051_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_slopez_252d_z504_3d_v052_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slopez_21d_z126_3d_v053_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slopez_63d_z252_3d_v054_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slopez_126d_z252_3d_v055_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_slopez_252d_z504_3d_v056_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_jerk_21d_3d_v057_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_jerk_63d_3d_v058_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_jerk_126d_3d_v059_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_jerk_21d_3d_v060_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_jerk_63d_3d_v061_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_jerk_126d_3d_v062_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_jerk_21d_3d_v063_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_jerk_63d_3d_v064_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_jerk_126d_3d_v065_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_jerk_21d_3d_v066_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_jerk_63d_3d_v067_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_jerk_126d_3d_v068_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_jerk_21d_3d_v069_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_jerk_63d_3d_v070_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_jerk_126d_3d_v071_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_jerk_21d_3d_v072_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_jerk_63d_3d_v073_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_jerk_126d_3d_v074_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_jerk_21d_3d_v075_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_jerk_63d_3d_v076_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_jerk_126d_3d_v077_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_per_rnd smoothed over 252d
def f019rdp_f019_rnd_productivity_rev_per_rnd_smoothaccel_63d_sm252_3d_v078_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_per_rnd smoothed over 504d
def f019rdp_f019_rnd_productivity_rev_per_rnd_smoothaccel_252d_sm504_3d_v079_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of gp_per_rnd smoothed over 252d
def f019rdp_f019_rnd_productivity_gp_per_rnd_smoothaccel_63d_sm252_3d_v080_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of gp_per_rnd smoothed over 504d
def f019rdp_f019_rnd_productivity_gp_per_rnd_smoothaccel_252d_sm504_3d_v081_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opinc_per_rnd smoothed over 252d
def f019rdp_f019_rnd_productivity_opinc_per_rnd_smoothaccel_63d_sm252_3d_v082_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opinc_per_rnd smoothed over 504d
def f019rdp_f019_rnd_productivity_opinc_per_rnd_smoothaccel_252d_sm504_3d_v083_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of rev_growth_per_rnd smoothed over 252d
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_smoothaccel_63d_sm252_3d_v084_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of rev_growth_per_rnd smoothed over 504d
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_smoothaccel_252d_sm504_3d_v085_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ebitda_per_rnd smoothed over 252d
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_smoothaccel_63d_sm252_3d_v086_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ebitda_per_rnd smoothed over 504d
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_smoothaccel_252d_sm504_3d_v087_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_per_rnd smoothed over 252d
def f019rdp_f019_rnd_productivity_fcf_per_rnd_smoothaccel_63d_sm252_3d_v088_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_per_rnd smoothed over 504d
def f019rdp_f019_rnd_productivity_fcf_per_rnd_smoothaccel_252d_sm504_3d_v089_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of ocf_per_rnd smoothed over 252d
def f019rdp_f019_rnd_productivity_ocf_per_rnd_smoothaccel_63d_sm252_3d_v090_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of ocf_per_rnd smoothed over 504d
def f019rdp_f019_rnd_productivity_ocf_per_rnd_smoothaccel_252d_sm504_3d_v091_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_accelz_21d_z252_3d_v092_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_accelz_63d_z504_3d_v093_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_accelz_21d_z252_3d_v094_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_accelz_63d_z504_3d_v095_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_accelz_21d_z252_3d_v096_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_accelz_63d_z504_3d_v097_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_accelz_21d_z252_3d_v098_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_accelz_63d_z504_3d_v099_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_accelz_21d_z252_3d_v100_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_accelz_63d_z504_3d_v101_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_accelz_21d_z252_3d_v102_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_accelz_63d_z504_3d_v103_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_accelz_21d_z252_3d_v104_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of ocf_per_rnd
def f019rdp_f019_rnd_productivity_ocf_per_rnd_accelz_63d_z504_3d_v105_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_rev_per_rnd_signflip_63d_3d_v106_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_rev_per_rnd_signflip_252d_3d_v107_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in gp_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_gp_per_rnd_signflip_63d_3d_v108_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in gp_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_gp_per_rnd_signflip_252d_3d_v109_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in opinc_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_opinc_per_rnd_signflip_63d_3d_v110_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in opinc_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_opinc_per_rnd_signflip_252d_3d_v111_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in rev_growth_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_signflip_63d_3d_v112_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in rev_growth_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_signflip_252d_3d_v113_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ebitda_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_signflip_63d_3d_v114_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ebitda_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_signflip_252d_3d_v115_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_fcf_per_rnd_signflip_63d_3d_v116_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_fcf_per_rnd_signflip_252d_3d_v117_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in ocf_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_ocf_per_rnd_signflip_63d_3d_v118_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in ocf_per_rnd (raw count, no price scaling)
def f019rdp_f019_rnd_productivity_ocf_per_rnd_signflip_252d_3d_v119_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_per_rnd normalized by 252d range
def f019rdp_f019_rnd_productivity_rev_per_rnd_rngaccel_63d_r252_3d_v120_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_per_rnd normalized by 504d range
def f019rdp_f019_rnd_productivity_rev_per_rnd_rngaccel_252d_r504_3d_v121_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of gp_per_rnd normalized by 252d range
def f019rdp_f019_rnd_productivity_gp_per_rnd_rngaccel_63d_r252_3d_v122_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of gp_per_rnd normalized by 504d range
def f019rdp_f019_rnd_productivity_gp_per_rnd_rngaccel_252d_r504_3d_v123_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opinc_per_rnd normalized by 252d range
def f019rdp_f019_rnd_productivity_opinc_per_rnd_rngaccel_63d_r252_3d_v124_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opinc_per_rnd normalized by 504d range
def f019rdp_f019_rnd_productivity_opinc_per_rnd_rngaccel_252d_r504_3d_v125_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of rev_growth_per_rnd normalized by 252d range
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_rngaccel_63d_r252_3d_v126_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of rev_growth_per_rnd normalized by 504d range
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_rngaccel_252d_r504_3d_v127_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ebitda_per_rnd normalized by 252d range
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_rngaccel_63d_r252_3d_v128_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ebitda_per_rnd normalized by 504d range
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_rngaccel_252d_r504_3d_v129_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_per_rnd normalized by 252d range
def f019rdp_f019_rnd_productivity_fcf_per_rnd_rngaccel_63d_r252_3d_v130_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_per_rnd normalized by 504d range
def f019rdp_f019_rnd_productivity_fcf_per_rnd_rngaccel_252d_r504_3d_v131_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of ocf_per_rnd normalized by 252d range
def f019rdp_f019_rnd_productivity_ocf_per_rnd_rngaccel_63d_r252_3d_v132_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of ocf_per_rnd normalized by 504d range
def f019rdp_f019_rnd_productivity_ocf_per_rnd_rngaccel_252d_r504_3d_v133_signal(ncfo, rnd, closeadj):
    base = ncfo / rnd.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_cumslope_21d_3d_v134_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_cumslope_63d_3d_v135_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_per_rnd
def f019rdp_f019_rnd_productivity_rev_per_rnd_cumslope_252d_3d_v136_signal(revenue, rnd, closeadj):
    base = _f019_rev_per_rnd(revenue, rnd)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_cumslope_21d_3d_v137_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_cumslope_63d_3d_v138_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of gp_per_rnd
def f019rdp_f019_rnd_productivity_gp_per_rnd_cumslope_252d_3d_v139_signal(gp, rnd, closeadj):
    base = _f019_gp_per_rnd(gp, rnd)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_cumslope_21d_3d_v140_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_cumslope_63d_3d_v141_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of opinc_per_rnd
def f019rdp_f019_rnd_productivity_opinc_per_rnd_cumslope_252d_3d_v142_signal(opinc, rnd, closeadj):
    base = opinc / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_cumslope_21d_3d_v143_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_cumslope_63d_3d_v144_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of rev_growth_per_rnd
def f019rdp_f019_rnd_productivity_rev_growth_per_rnd_cumslope_252d_3d_v145_signal(revenue, rnd, closeadj):
    base = revenue.pct_change(periods=252) / rnd.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_cumslope_21d_3d_v146_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_cumslope_63d_3d_v147_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of ebitda_per_rnd
def f019rdp_f019_rnd_productivity_ebitda_per_rnd_cumslope_252d_3d_v148_signal(ebitda, rnd, closeadj):
    base = ebitda / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_cumslope_21d_3d_v149_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of fcf_per_rnd
def f019rdp_f019_rnd_productivity_fcf_per_rnd_cumslope_63d_3d_v150_signal(fcf, rnd, closeadj):
    base = fcf / rnd.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

